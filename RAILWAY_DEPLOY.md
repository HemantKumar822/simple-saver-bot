# Railway Deployment Guide for Simple Saver Bot

## 🚀 Deploy to Railway (Free & Easy)

### Step 1: Fork & Connect Repository

1. **Fork this repository** to your GitHub account
2. **Go to [Railway.app](https://railway.app)**
3. **Sign up/Login** with your GitHub account
4. **Click "New Project"**
5. **Select "Deploy from GitHub repo"**
6. **Choose your forked repository**

### Step 2: Configure Environment Variables

In Railway dashboard, go to **Variables** tab and add:

```
BOT_TOKEN=8001258930:AAEmInNBucSfuixbhHOu-rv1zZe2xPTqO-Q
API_ID=26106446
API_HASH=5377b3f8f89ad518e7aadadecbd27a99
OWNER_ID=1647031358
```

### Step 3: Deploy!

Railway will automatically:
- ✅ Build the Docker container
- ✅ Install all dependencies
- ✅ Start your bot
- ✅ Provide persistent storage
- ✅ Auto-scale as needed

### Step 4: Check Logs

```bash
# In Railway dashboard, go to "Logs" tab
# Or use Railway CLI:
railway logs
```

### Step 5: Test Your Bot

1. Open Telegram
2. Search for `@SimplySaverBot`
3. Send `/start`
4. Try downloading: `https://youtu.be/dQw4w9WgXcQ`

---

## 🎯 Railway Benefits

- ✅ **Free tier:** 512MB RAM, 1GB storage, 512 hours/month
- ✅ **Persistent storage:** Downloads don't disappear
- ✅ **Auto-scaling:** Handles traffic spikes
- ✅ **PostgreSQL:** Database included (optional)
- ✅ **GitHub integration:** Deploy on every push
- ✅ **Global CDN:** Fast worldwide performance

---

## 📊 Railway Limits (Free Tier)

| Resource | Limit | Notes |
|----------|-------|-------|
| RAM | 512MB | Enough for most bots |
| Storage | 1GB | Clean downloads regularly |
| Hours | 512/month | ~21 days continuous |
| Bandwidth | Unlimited | No bandwidth limits |

---

## 🛠️ Troubleshooting

### Bot not starting?
```bash
# Check Railway logs for errors
railway logs --tail 100
```

### Downloads failing?
- Railway includes FFmpeg automatically
- Check storage usage in Railway dashboard
- Clean old downloads: Files may accumulate

### Out of hours?
- Railway free tier gives 512 hours/month
- Upgrade to Pro for unlimited hours ($5/month)

### Need more storage?
- Clean user download folders regularly
- Railway Pro offers more storage

---

## 🔧 Advanced Configuration

### Custom Domain (Optional)
1. Go to Railway dashboard → Settings
2. Add custom domain
3. Configure DNS

### Database (Optional)
Railway provides PostgreSQL automatically. To use it:
```python
# In config.py, you can add:
DATABASE_URL = os.getenv('DATABASE_URL')  # Railway provides this
```

### Environment Variables
```bash
# View all variables
railway variables

# Set a variable
railway variables set NEW_VAR=value
```

---

## 📞 Support

- **Railway Docs:** https://docs.railway.app/
- **Telegram:** [@hemantkumar822](https://t.me/hemantkumar822)
- **GitHub Issues:** Report bugs here

---

## 🎉 You're Live!

Your **Simple Saver Bot** is now running on Railway! 🚀

**Bot:** @SimplySaverBot
**Status:** 🟢 Production Ready
**Hosting:** Railway (Free)

---

*Made for Railway deployment by Hemant Kumar*