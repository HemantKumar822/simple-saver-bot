#!/usr/bin/env python3
"""
Railway Health Check Endpoint (Simple version without Flask)
"""
import json
import time
import os

def health_check():
    """Railway health check response"""
    return {
        "status": "healthy",
        "timestamp": int(time.time()),
        "service": "simple-saver-bot",
        "version": "1.0.0"
    }

if __name__ == '__main__':
    # Simple health check for Railway
    response = health_check()
    print(json.dumps(response, indent=2))