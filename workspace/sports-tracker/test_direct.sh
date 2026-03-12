#!/bin/bash
# 直接测试 dashscope-websearch 调用

echo "测试直接调用..."
mcporter call dashscope-websearch.bailian_web_search query="今日热门体育比赛" count=3
