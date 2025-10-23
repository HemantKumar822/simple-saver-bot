#!/bin/bash
# Railway Build Script
echo "🚀 Building Simple Saver Bot for Railway..."

# Install system dependencies
apt-get update && apt-get install -y ffmpeg

# Create necessary directories
mkdir -p database/simplesaver
mkdir -p database/video_cache
mkdir -p database/video_cache/playlists
mkdir -p database/video_cache/images
mkdir -p users
mkdir -p logs

echo "✅ Railway build complete!"