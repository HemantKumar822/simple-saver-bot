#!/bin/bash
# Railway startup script
echo "🚀 Starting Simple Saver Bot on Railway..."

# Set Railway environment
export RAILWAY_ENVIRONMENT=production

# Create directories
mkdir -p database/simplesaver database/video_cache database/video_cache/playlists database/video_cache/images users logs

# Start health check in background (optional)
python health.py &
HEALTH_PID=$!

# Start the bot
python magic.py

# Cleanup
kill $HEALTH_PID 2>/dev/null