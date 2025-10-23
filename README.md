# 🎯 Simple Saver Bot

[![Telegram](https://img.shields.io/badge/Telegram-@SimplySaverBot-blue.svg)](https://t.me/SimplySaverBot)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-0B0D17.svg)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Your hassle-free download companion for YouTube, Instagram, Threads, and TikTok!**

Send me any link and I'll quickly fetch and deliver the video or image directly to you.

**Created by:** Hemant Kumar ([@hemantkumar822](https://t.me/hemantkumar822))

---

## ✨ Features

- 🎬 **YouTube Downloads** - Videos, shorts, playlists
- 📸 **Instagram Media** - Posts, reels, stories
- 🧵 **Threads Content** - Videos and images
- 🎵 **TikTok Videos** - Individual videos and profiles
- 🎵 **Audio Extraction** - MP3 from any video
- 🎯 **Quality Selection** - Choose your preferred quality
- 📊 **Usage Statistics** - Track your downloads
- 🏷️ **Tag System** - Organize with custom tags
- ⚡ **Fast & Reliable** - No ads, no waiting
- 🆓 **Completely Free** - No subscriptions required

---

## 🚀 Quick Start

### For Users

1. **Open Telegram** and search for [@SimplySaverBot](https://t.me/SimplySaverBot)
2. **Send any link** from:
   - YouTube: `https://youtube.com/watch?v=...`
   - Instagram: `https://instagram.com/p/...`
   - Threads: `https://threads.net/@user/post/...`
   - TikTok: `https://tiktok.com/@user/video/...`
3. **Get your media** instantly!

### Basic Commands

```
/start - Start the bot
/help - Show help message
/audio URL - Extract audio only
/format - Set video quality
/settings - Customize preferences
/clean - Clean your files
/usage - View download stats
```

---

## 🛠️ Deployment

This bot is configured for **Railway** deployment with automatic scaling and persistent storage.

### Quick Deploy

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

### Manual Deploy

1. **Fork this repository**
2. **Connect to Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your forked repository
3. **Set Environment Variables:**
   ```
   BOT_TOKEN=your_telegram_bot_token
   API_ID=your_telegram_api_id
   API_HASH=your_telegram_api_hash
   OWNER_ID=1647031358
   ```
4. **Deploy!** Railway will automatically build and deploy your bot

---

## 🔧 Configuration

All configuration is in `CONFIG/config.py`. The bot is pre-configured for:
- **No Firebase** (uses local JSON database)
- **No subscriptions** (free for everyone)
- **Railway optimization** (persistent storage, auto-scaling)

---

## 📊 Supported Platforms

| Platform | Video | Audio | Images | Playlists |
|----------|-------|-------|--------|-----------|
| YouTube | ✅ | ✅ | ❌ | ✅ |
| Instagram | ✅ | ✅ | ✅ | ❌ |
| Threads | ✅ | ✅ | ✅ | ❌ |
| TikTok | ✅ | ✅ | ❌ | ✅ |
| And 1500+ more sites via yt-dlp! | | | |

---

## 🐛 Troubleshooting

### Bot not responding?
```bash
# Check Railway logs
railway logs
```

### Downloads failing?
- Ensure FFmpeg is installed (Railway handles this automatically)
- Check file size limits (Railway has storage constraints)

### Need help?
- Check Railway documentation
- Contact [@hemantkumar822](https://t.me/hemantkumar822)

---

## � License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **Developer:** Hemant Kumar ([@hemantkumar822](https://t.me/hemantkumar822))
- **Framework:** [PyroTGFork](https://github.com/pyrogram/pyrotgfork)
- **Downloader:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Gallery:** [gallery-dl](https://github.com/mikf/gallery-dl)
- **Hosting:** [Railway](https://railway.app)

---

**Made with ❤️ for the Telegram community**
