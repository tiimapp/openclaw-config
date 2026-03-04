#!/usr/bin/env python3
"""
Benchmark script for CF2605 Cotton Futures data retrieval
Compares AKShare library vs direct Sina API calls
"""

import time
import requests
import statistics
import akshare as ak
from datetime import datetime

def benchmark_akshare(iterations=10):
    """Benchmark AKShare futures_zh_daily_sina for CF2605"""
    print(f"\n{'='*60}")
    print(f"AKShare Benchmark - CF2605 Cotton Futures")
    print(f"Iterations: {iterations}")
    print(f"{'='*60}")
    
    times = []
    data_samples = []
    
    for i in range(iterations):
        start = time.time()
        try:
            df = ak.futures_zh_daily_sina(symbol="CF2605")
            elapsed = time.time() - start
            times.append(elapsed)
            
            if i == 0 and df is not None and len(df) > 0:
                data_samples.append(df.iloc[0].to_dict())
                
            status = "✓" if df is not None and len(df) > 0 else "✗"
            print(f"  Run {i+1:2d}: {elapsed:.3f}s {status}")
        except Exception as e:
            elapsed = time.time() - start
            times.append(elapsed)
            print(f"  Run {i+1:2d}: {elapsed:.3f}s ✗ ERROR: {str(e)[:50]}")
    
    if times:
        return {
            'times': times,
            'avg': statistics.mean(times),
            'min': min(times),
            'max': max(times),
            'std': statistics.stdev(times) if len(times) > 1 else 0,
            'data_sample': data_samples[0] if data_samples else None,
            'success_rate': sum(1 for t in times if t > 0) / len(times) * 100
        }
    return None

def benchmark_sina_api(iterations=10):
    """Benchmark direct Sina API call for CF2605"""
    print(f"\n{'='*60}")
    print(f"Sina Direct API Benchmark - czce_cf2605")
    print(f"Iterations: {iterations}")
    print(f"{'='*60}")
    
    times = []
    data_samples = []
    url = "http://hq.sinajs.cn/list=czce_cf2605"
    
    for i in range(iterations):
        start = time.time()
        try:
            response = requests.get(url, timeout=10)
            elapsed = time.time() - start
            times.append(elapsed)
            
            if i == 0 and response.status_code == 200:
                data_samples.append(response.text[:500])
                
            status = "✓" if response.status_code == 200 else "✗"
            print(f"  Run {i+1:2d}: {elapsed:.3f}s {status}")
        except Exception as e:
            elapsed = time.time() - start
            times.append(elapsed)
            print(f"  Run {i+1:2d}: {elapsed:.3f}s ✗ ERROR: {str(e)[:50]}")
    
    if times:
        return {
            'times': times,
            'avg': statistics.mean(times),
            'min': min(times),
            'max': max(times),
            'std': statistics.stdev(times) if len(times) > 1 else 0,
            'data_sample': data_samples[0] if data_samples else None,
            'success_rate': sum(1 for t in times if t > 0) / len(times) * 100
        }
    return None

def print_results(label, results):
    """Print benchmark results in formatted way"""
    if not results:
        print(f"\n{label}: No results")
        return
    
    print(f"\n📊 {label} Results:")
    print(f"  Average: {results['avg']*1000:.1f}ms")
    print(f"  Min:     {results['min']*1000:.1f}ms")
    print(f"  Max:     {results['max']*1000:.1f}ms")
    print(f"  Std Dev: {results['std']*1000:.1f}ms")
    print(f"  Success: {results['success_rate']:.0f}%")

def main():
    print(f"\n🚀 CF2605 Cotton Futures Benchmark")
    print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run benchmarks
    akshare_results = benchmark_akshare(iterations=10)
    sina_results = benchmark_sina_api(iterations=10)
    
    # Print summaries
    print_results("AKShare", akshare_results)
    print_results("Sina API", sina_results)
    
    # Show sample data
    print(f"\n{'='*60}")
    print("📋 Sample Data")
    print(f"{'='*60}")
    
    if akshare_results and akshare_results['data_sample']:
        print("\nAKShare Data (latest row):")
        for key, value in akshare_results['data_sample'].items():
            print(f"  {key}: {value}")
    
    if sina_results and sina_results['data_sample']:
        print(f"\nSina API Raw Response (first 500 chars):")
        print(f"  {sina_results['data_sample'][:300]}...")
    
    # Comparison and recommendation
    print(f"\n{'='*60}")
    print("💡 Recommendation")
    print(f"{'='*60}")
    
    if akshare_results and sina_results:
        ak_avg = akshare_results['avg']
        sina_avg = sina_results['avg']
        
        if ak_avg < sina_avg:
            faster = "AKShare"
            diff = ((sina_avg - ak_avg) / sina_avg) * 100
        else:
            faster = "Sina API"
            diff = ((ak_avg - sina_avg) / ak_avg) * 100
        
        print(f"\n⚡ Faster: {faster} by {diff:.1f}%")
        print(f"\n📌 For Production Use:")
        
        if akshare_results['success_rate'] >= 90:
            print("  ✓ AKShare is RELIABLE for cron job automation")
            print(f"  ✓ Expected response time: ~{akshare_results['avg']*1000:.0f}ms per call")
        else:
            print("  ⚠ AKShare has reliability issues, consider fallback")
        
        print(f"\n  Pros of AKShare:")
        print(f"    - Structured DataFrame output (easy to process)")
        print(f"    - Built-in error handling")
        print(f"    - No parsing required")
        
        print(f"\n  Cons of AKShare:")
        print(f"    - Heavier dependency (more packages)")
        print(f"    - Slightly slower than raw API")
        
        print(f"\n  Pros of Sina Direct API:")
        print(f"    - Faster response time")
        print(f"    - Minimal dependencies")
        
        print(f"\n  Cons of Sina Direct API:")
        print(f"    - Requires manual parsing")
        print(f"    - Raw string format")
        
        print(f"\n🎯 Final Verdict: {'Use AKShare for ease of use' if akshare_results['success_rate'] >= 90 else 'Use Sina API with custom parser'}")

if __name__ == "__main__":
    main()
