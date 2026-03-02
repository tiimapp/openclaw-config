#!/usr/bin/env node

/**
 * DashScope QWen ASR CLI Wrapper
 * Uses the audio transcription API with task submission
 * Usage: dashscope-asr --file <audio_file> [--model <model_name>]
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

// Config
const API_KEY = process.env.DASHSCOPE_API_KEY || 'sk-9fd1be825af0419c88382485d119451c';
const DEFAULT_MODEL = 'qwen3-asr-flash';

// Parse arguments
const args = process.argv.slice(2);
let filePath = null;
let model = DEFAULT_MODEL;

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--file' && args[i + 1]) {
    filePath = args[++i];
  } else if (args[i] === '--model' && args[i + 1]) {
    model = args[++i];
  }
}

if (!filePath) {
  console.error('Error: --file argument is required');
  process.exit(1);
}

if (!fs.existsSync(filePath)) {
  console.error(`Error: File not found: ${filePath}`);
  process.exit(1);
}

// Read file and convert to base64
const audioBuffer = fs.readFileSync(filePath);
const audioBase64 = audioBuffer.toString('base64');
const fileExt = path.extname(filePath).toLowerCase().replace('.', '');

// Build task submission request
const requestBody = {
  model: model,
  input: {
    file_url: `data:audio/${fileExt};base64,${audioBase64}`
  },
  task_group: 'audio',
  task: 'transcription',
  function: {
    type: 'transcription'
  },
  parameters: {
    format: fileExt
  }
};

const requestJson = JSON.stringify(requestBody);

const options = {
  hostname: 'dashscope.aliyuncs.com',
  port: 443,
  path: '/api/v1/services/audio/transcription',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(requestJson)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  
  res.on('data', (chunk) => {
    data += chunk;
  });
  
  res.on('end', () => {
    try {
      const response = JSON.parse(data);
      
      // Handle task-based response
      if (response.output && response.output.task_id) {
        pollTask(response.output.task_id);
        return;
      }
      
      // Handle direct response
      if (response.output && response.output.results) {
        const text = response.output.results
          .map(r => r.text || '')
          .filter(t => t)
          .join(' ');
        console.log(text);
      } else if (response.output && response.output.text) {
        console.log(response.output.text);
      } else if (response.message) {
        console.error(`API Error: ${response.message}`);
        process.exit(1);
      } else if (response.code) {
        console.error(`API Error (${response.code}): ${response.message || response.code}`);
        process.exit(1);
      } else {
        console.error('Unexpected response:', JSON.stringify(response, null, 2));
        process.exit(1);
      }
    } catch (e) {
      console.error('Parse error:', e.message);
      console.error('Raw response:', data);
      process.exit(1);
    }
  });
});

req.on('error', (e) => {
  console.error(`Request error: ${e.message}`);
  process.exit(1);
});

req.write(requestJson);
req.end();

function pollTask(taskId) {
  const pollOptions = {
    hostname: 'dashscope.aliyuncs.com',
    port: 443,
    path: `/api/v1/tasks/${taskId}`,
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${API_KEY}`
    }
  };

  const pollReq = https.request(pollOptions, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
      try {
        const response = JSON.parse(data);
        
        if (response.output && response.output.task_status === 'SUCCEEDED' && response.output.results) {
          const text = response.output.results
            .map(r => r.text || '')
            .filter(t => t)
            .join(' ');
          console.log(text);
        } else if (response.output && response.output.task_status === 'SUCCEEDED' && response.output.text) {
          console.log(response.output.text);
        } else if (response.output && response.output.task_status === 'RUNNING') {
          setTimeout(() => pollTask(taskId), 1000);
        } else if (response.output && response.output.task_status === 'FAILED') {
          console.error(`Task failed: ${response.output.message || 'unknown error'}`);
          process.exit(1);
        } else {
          console.error('Unexpected poll response:', JSON.stringify(response, null, 2));
          process.exit(1);
        }
      } catch (e) {
        console.error('Parse error:', e.message);
        process.exit(1);
      }
    });
  });

  pollReq.on('error', (e) => {
    console.error(`Poll error: ${e.message}`);
    process.exit(1);
  });

  pollReq.end();
}
