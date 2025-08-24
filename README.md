# tg-ytdlp-bot (supports your own cookies)

Support me on [BuyMeACoffee](https://buymeacoffee.com/upekshaip) \
Thanks to Contributor - [@IIlIlIlIIIlllIIlIIlIllIIllIlIIIl](https://t.me/IIlIlIlIIIlllIIlIIlIllIIllIlIIIl) - [chelaxian](https://github.com/chelaxian/tg-ytdlp-bot)

Download private YouTube/videos using a cookie file with advanced format selection, codec support (H.264/AVC, AV1, VP9), and intelligent subtitle handling.

Test free Telegram bots - https://t.me/tg_ytdlp \
https://t.me/tgytdlp_uae_bot \
https://t.me/tgytdlp_uk_bot \
https://t.me/tgytdlp_fr_bot \
https://t.me/tgytdlp_bot

## Full Documentation
[https://upekshaip.com/projects/-O0t36gRpfJR1p8KB7vU](https://upekshaip.com/projects/-O0t36gRpfJR1p8KB7vU)

---

## Deploy on a VM 

- First, add your bot to the **logging channel** and **subscription channel**. Both are required.
- Star and fork this repository. Then rename the file **_config.py** to **config.py**.
- Add your configuration to the **config.py** file.
- Install required dependencies and start the bot.

---

#### Get YouTube cookies

YouTube rotates account cookies frequently on open YouTube browser tabs as a security measure. To export cookies that will remain working with yt-dlp, you will need to export cookies in such a way that they are never rotated.

One way to do this is through a private browsing/incognito window:

- Open a new private browsing/incognito window and log into YouTube
- Open a new tab and close the YouTube tab
- Export youtube.com cookies from the browser then close the private browsing/incognito window so the session is never opened in the browser again.

For export you can use browser extension [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)

create in project folder subfolder `TXT` and place `cookie.txt` extracted from YouTube here

```sh
cd tg-ytdlp-bot/TXT
nano cookie.txt
```

#### Advanced YouTube Cookie Management

The bot now supports automatic downloading and validation of YouTube cookies from multiple sources:

**Features:**
- **Multiple Sources**: Configure up to 10 different cookie sources
- **Automatic Validation**: Each downloaded cookie is tested for functionality
- **Fallback System**: If one source fails, automatically tries the next
- **Real-time Progress**: Shows download and validation progress to users

**Configuration in `CONFIG/config.py`:**
```python
# YouTube cookies URLs - main URL and backups
# The bot will check cookies in the order: YOUTUBE_COOKIE_URL, YOUTUBE_COOKIE_URL_1, YOUTUBE_COOKIE_URL_2, etc.
# If one URL does not work or the cookies are expired, the bot will automatically try the next one
YOUTUBE_COOKIE_URL = "https://your-domain.com/cookies/youtube/cookie1.txt"
YOUTUBE_COOKIE_URL_1 = "https://your-domain.com/cookies/youtube/cookie2.txt"
YOUTUBE_COOKIE_URL_2 = "https://your-domain.com/cookies/youtube/cookie3.txt"
YOUTUBE_COOKIE_URL_3 = "https://your-domain.com/cookies/youtube/cookie4.txt"
YOUTUBE_COOKIE_URL_4 = "https://your-domain.com/cookies/youtube/cookie5.txt"
# Add more sources as needed (up to YOUTUBE_COOKIE_URL_9)
```

**How it works:**
1. User runs `/download_cookie` and selects YouTube
2. Bot downloads cookies from the first available source
3. Validates cookies by testing them with a YouTube video
4. If validation fails, automatically tries the next source
5. Continues until working cookies are found or all sources are exhausted

**User Experience:**
- Progress updates: "🔄 Downloading and checking YouTube cookies... Attempt 1 of 4"
- Success message: "✅ YouTube cookies successfully downloaded and validated! Used source 2 of 4"
- Failure message: "❌ All YouTube cookies are expired or unavailable! Contact the bot administrator to replace them."

Also you may fill in `porn_domains.txt` `porn_keywords.txt` files in `TXT` folder if you want to tag #porn videos and hide them under spoiler

---

##  local deployment on a VM 
For local deployment you should use this commands:

#### Install `git` and `python3` (example for Ubuntu/Debian)
```sh
sudo apt update
sudo apt install mediainfo rsync
sudo apt install git python3.10 python3-pip python3.10-venv
```
#### Setting up `config.py`
```sh
git clone https://github.com/upekshaip/tg-ytdlp-bot.git
cd tg-ytdlp-bot/CONFIG
sudo mv _config.py config.py
nano config.py
```

**Required Configuration Fields:**

```python
# Bot Configuration
BOT_NAME = "your_bot_name"                    # Your bot's name
BOT_NAME_FOR_USERS = "tg-ytdlp-bot"          # Name in database
ADMIN = [123456789, 987654321]               # List of admin user IDs
API_ID = 12345678                            # Your Telegram API ID
API_HASH = "your_api_hash_here"              # Your Telegram API Hash
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # Your bot token

# Channel Configuration
LOGS_ID = -1001234567890                     # Logging channel ID
SUBSCRIBE_CHANNEL = -1001234567890           # Subscription channel ID
SUBSCRIBE_CHANNEL_URL = "https://t.me/your_channel"  # Channel invite link

# Cookie Configuration
COOKIE_URL = "https://your-domain.com/cookies/cookie.txt"  # Fallback cookie URL

# YouTube Cookie URLs (Multiple Sources)
YOUTUBE_COOKIE_URL = "https://your-domain.com/cookies/youtube/cookie1.txt"
YOUTUBE_COOKIE_URL_1 = "https://your-domain.com/cookies/youtube/cookie2.txt"
YOUTUBE_COOKIE_URL_2 = "https://your-domain.com/cookies/youtube/cookie3.txt"
YOUTUBE_COOKIE_URL_3 = "https://your-domain.com/cookies/youtube/cookie4.txt"
YOUTUBE_COOKIE_URL_4 = "https://your-domain.com/cookies/youtube/cookie5.txt"

# Other Service Cookies
INSTAGRAM_COOKIE_URL = "https://your-domain.com/cookies/instagram_cookie.txt"
TIKTOK_COOKIE_URL = "https://your-domain.com/cookies/tiktok_cookie.txt"
FACEBOOK_COOKIE_URL = "https://your-domain.com/cookies/facebook_cookie.txt"
TWITTER_COOKIE_URL = "https://your-domain.com/cookies/twitter_cookie.txt"

# Firebase Configuration
FIREBASE_USER = "your-email@gmail.com"
FIREBASE_PASSWORD = "your-firebase-password"
FIREBASE_CONF = {
    "apiKey": "your-api-key",
    "authDomain": "your-project.firebaseapp.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project.appspot.com",
    "messagingSenderId": "123456789",
    "appId": "1:123456789:web:abcdef123456",
    "databaseURL": "https://your-project-default-rtdb.firebaseio.com"
}
```

**Important Notes:**
- **Admin IDs**: Add your Telegram user ID to the `ADMIN` list to access admin commands
- **Channel IDs**: Both logging and subscription channels are required
- **Cookie URLs**: Must point to `.txt` files with Netscape cookie format
- **Firebase**: Required for caching and user data management
- **API Credentials**: Get from [@BotFather](https://t.me/BotFather) and [my.telegram.org](https://my.telegram.org)

**Getting API Credentials:**
1. **Bot Token**: Message [@BotFather](https://t.me/BotFather) and create a new bot
2. **API ID & Hash**: Visit [my.telegram.org](https://my.telegram.org), log in, and go to "API development tools"
3. **Channel IDs**: Add your bot to the channels and get the channel IDs (they start with -100)

**Getting Your User ID:**
- Message [@UserInfoToBot](https://t.me/UserInfoToBot) to get your Telegram user ID
- Add this ID to the `ADMIN` list in config.py

**Setting Up Firebase:**
1. Go to [Firebase Console](https://console.firebase.google.com/) and create a new project
2. Enable Realtime Database and Authentication
3. Create a user with email/password authentication
4. Get your Firebase configuration from Project Settings
5. Update the `FIREBASE_CONF` section in config.py with your project details

**Cookie File Setup:**
1. Create cookie files in Netscape format for each service. You can use this browser extension https://cookie-editor.com/  
2. Upload them to a web server accessible via HTTPS. You can use your own Github repo for that.
3. Update the cookie URLs in config.py to point to your files. For Github repo ensure you use RAW URLs to your text cookie files.
4. Ensure files are under 100KB and accessible without authentication

**Setting Up Channels:**
1. **Logging Channel**: Create a private channel for bot logs
   - Add your bot as admin with "Send Messages" permission
   - Get the channel ID (starts with -100)
   - Update `LOGS_ID` in config.py

2. **Subscription Channel**: Create a public/private channel for user subscription
   - Add your bot as admin
   - Get the channel ID and invite link
   - Update `SUBSCRIBE_CHANNEL` and `SUBSCRIBE_CHANNEL_URL` in config.py

**Channel ID Format:**
- Public channels: `-100` + channel ID
- Private channels: `-100` + channel ID
- Example: If your channel ID is `1234567890`, use `-1001234567890`

**Getting Channel IDs:**
1. **Method 1**: Forward a message from your channel to [@userinfobot](https://t.me/userinfobot)
2. **Method 2**: Use [@getidsbot](https://t.me/getidsbot) - send it a link to your channel
3. **Method 3**: Add [@RawDataBot](https://t.me/RawDataBot) to your channel and check the forwarded message

**Important**: Both channels are required for the bot to function properly.

Edit your configuration before deployment.

#### Install `python` modules

```sh
python3 -m venv venv
source venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```
---
### Installing ffmpeg (example for Ubuntu/Debian)
      
   you also need to install `ffmpeg` https://github.com/btbn/ffmpeg-builds/releases
   **ffmpeg** is essential since **yt-dlp** relies on it for merging streams (and in some cases for transcoding or extracting thumbnails). Also ffmpeg is needed for embedding subtitles and for slpitting bigger that 2gb videos into parts. To install ffmpeg on a Debian-based system, run:

   ```sh
   sudo apt-get update
   sudo apt-get install -y ffmpeg
   ```

   Verify the installation:
   ```sh
   ffmpeg -version
   ```
---
### (Optional) Arabic and Asian fonts

<details>
   <summary>spoiler</summary> 
      
If you need to support extra languages such as arabic, chinese, japanese, korean - you also need to install this language packs:
   ```sh
   sudo apt update
   sudo add-apt-repository universe
   sudo apt update

   sudo apt install fonts-noto-core             # – Noto Sans, Noto Serif, … base fonts Google Noto
   sudo apt install fonts-noto-extra            # – extra fonts (including arabic)
   sudo apt install fonts-kacst fonts-kacst-one # – KACST arabic fonts
   sudo apt install fonts-noto-cjk              # – Chinese-Japanese-Korean characters
   sudo apt install fonts-indic                 # – extra indian fonts

   sudo apt install fonts-noto-color-emoji fontconfig libass9
   ```

   For Amiri arabic:
   ```sh
   git clone https://github.com/aliftype/amiri.git
   sudo mkdir -p /usr/share/fonts/truetype/amiri
   sudo cp amiri/fonts/*.ttf /usr/share/fonts/truetype/amiri/
   ```
   
   Update font cache
   ```sh
   sudo fc-cache -fv
   fc-list | grep -i amiri
   ``` 
</details>

---
### (Optional) Preparing `yt-dlp` for `/cookies_from_browser`
<details>
   <summary>spoiler</summary> 

   To use the `/cookies_from_browser` command (which extracts cookies from installed browsers on your server), ensure that the **yt-dlp** binary is set up properly:
  
   1. **Download `yt-dlp`**  
      Visit the [official `yt-dlp` releases page](https://github.com/yt-dlp/yt-dlp/releases) and download the binary for your CPU architecture (e.g., `yt-dlp_x86_64`, `yt-dlp_arm`, etc.).  
      Place the binary executable in the `tg-ytdlp-bot` project folder.
 
  2. **Rename and make it executable**  
     ```bash
     mv yt-dlp_linux yt-dlp
     chmod +x yt-dlp
     ```

   3. **Create a symbolic link**  
      Create a symlink so that `yt-dlp` can be run from any directory (for example, in `/usr/local/bin`):
      ```bash
      sudo ln -s /full/path/to/tg-ytdlp-bot/yt-dlp /usr/local/bin/yt-dlp
      ```
      Ensure `/usr/local/bin` is in your `PATH`. Now you can run `yt-dlp` directly.

   (Also in that case you must install desktop environment (GUI) and any supported by `yt-dlp` browser by yourself)

</details>

---

## Running Telegram bot
Now you can start the bot via commands:
```sh
source venv/bin/activate
python3 magic.py
```

---

## User Commands

- **/start** - Start the bot.
- **/help** - Display help message.
- **/settings** - Open settings menu with categories and quick actions.
- **/clean** - Clean your working directory or specific files (see /help).
- **/usage** - Show your usage statistics and logs.
- **/tags** - Get all your #tags.
- **/audio** - Download audio from a video URL.
- **/format** - Choose media format options with advanced codec selection (H.264/AVC, AV1, VP9) and container preferences (MP4, MKV).
- **/split** - Change splitted video part size (0.25-2GB).
- **/mediainfo** - Turn ON/OFF sending mediainfo (`/mediainfo on|off`).
- **/check_cookie** - Check the cookie file.
- **/download_cookie** - Download the cookie file with additional "From Browser" option.
- **/save_as_cookie** - Save text as cookie (or upload TXT-doc).
- **/cookies_from_browser** - Get cookies from browser (if supported) with fallback to Config.COOKIE_URL.
- **/subs** - Enable/disable subtitle embedding for videos with enhanced language selection and "Always Ask" mode.

---

## Advanced Features

### Enhanced Format Selection (`/format`)
- **Codec Support**: Choose between H.264/AVC (avc1), AV1 (av01), and VP9 (vp9)
- **Container Toggle**: Switch between MP4 and MKV containers
- **Smart Quality Selection**: Prioritizes exact height matches before falling back to "less than or equal to"
- **Persistent Preferences**: Your codec and container choices are saved per-user

### Always Ask Menu
- **📼 CODEC Button**: Access advanced codec and container filters
  - AVC (H.264/AVC) - Traditional, widely supported
  - AV1 - Modern royalty-free codec with ~25-40% better efficiency
  - VP9 - Google's VP9 codec
  - MP4/MKV container selection
- **📹 DUBS Button**: Select audio language with flag indicators
  - Only appears when multiple audio languages are detected
  - Pagination support for long language lists
- **💬 SUBS Button**: Choose subtitle language with smart detection
  - Auto-generated vs. normal captions
  - Translation indicators
  - Pagination support
- **Dynamic Filtering**: Real-time quality filtering based on selected codec/container
- **Smart Subtitle Logic**: Differentiates between "Always Ask" mode and manual subtitle selection

### Intelligent Subtitle Handling
- **Container-Aware Embedding**:
  - **MKV**: Soft-muxing (subtitles as separate track, no quality loss)
  - **MP4**: Hard-embedding (burned into video for universal compatibility)
- **Language Detection**: Optimized yt-dlp client selection for faster subtitle discovery
- **Auto Mode**: Automatically selects auto-generated or normal captions based on user preference
- **Always Ask Mode**: Shows all available subtitle languages for manual selection

### Enhanced Cookie Management
- **Browser Integration**: Extract cookies from installed browsers
- **Fallback Support**: Automatic download from Config.COOKIE_URL if no browsers found
- **Multiple Sources**: Choose between browser extraction and direct download
- **YouTube Cookie Validation**: Automatic testing and validation of YouTube cookies
- **Multi-Source Fallback**: Automatic switching between multiple cookie sources
- **Real-time Progress**: Live updates during cookie download and validation process

### Improved Error Handling
- **Upload Retries**: Smart retry logic for failed uploads with fallback to document mode
- **Dynamic Disk Space**: Intelligent space estimation based on video size
- **Graceful Degradation**: Better handling of format unavailability and network issues

---

## Cookie Management System

The bot features a comprehensive cookie management system that supports multiple services and automatic validation.

### YouTube Cookie Management

**Automatic Download and Validation:**
- **Multiple Sources**: Configure up to 10 different cookie sources in `config.py`
- **Sequential Testing**: Bot tests each source in order until working cookies are found
- **Real-time Validation**: Each downloaded cookie is tested with a YouTube video
- **Automatic Fallback**: If one source fails, automatically tries the next

**Configuration Example:**
```python
# In CONFIG/config.py
YOUTUBE_COOKIE_URL = "https://your-domain.com/cookies/youtube/cookie1.txt"
YOUTUBE_COOKIE_URL_1 = "https://your-domain.com/cookies/youtube/cookie2.txt"
YOUTUBE_COOKIE_URL_2 = "https://your-domain.com/cookies/youtube/cookie3.txt"
# ... up to YOUTUBE_COOKIE_URL_9
```

**User Commands:**
- `/download_cookie` → YouTube: Downloads and validates cookies from multiple sources
- `/check_cookie`: Validates existing cookies and checks YouTube functionality
- `/cookies_from_browser`: Extracts cookies from installed browsers
- `/save_as_cookie`: Upload custom cookie file

**Cookie Validation Process:**
1. **Download**: Fetches cookie file from configured source
2. **Format Check**: Validates Netscape cookie format
3. **Size Validation**: Ensures file size is under 100KB
4. **YouTube Test**: Tests cookies with a short YouTube video
5. **Error Analysis**: Distinguishes between authentication and network errors
6. **Fallback**: Tries next source if current one fails

### Other Service Cookies

The bot also supports cookies for other platforms:
- **Instagram**: `INSTAGRAM_COOKIE_URL`
- **TikTok**: `TIKTOK_COOKIE_URL`
- **Facebook**: `FACEBOOK_COOKIE_URL`
- **Twitter**: `TWITTER_COOKIE_URL`

### Cookie File Requirements

**Format**: Must be in Netscape cookie format:
```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	TRUE	1735689600	VISITOR_INFO1_LIVE	abc123
.youtube.com	TRUE	/	TRUE	1735689600	LOGIN_INFO	abc123
```

**Size Limit**: Maximum 100KB per cookie file

**Access**: Cookie files must be accessible via HTTP/HTTPS URLs

### Security Features

- **URL Hiding**: Source URLs are hidden from users in error messages
- **Error Sanitization**: Sensitive information is removed from logs
- **Temporary Files**: Cookie files are cleaned up after validation
- **Access Control**: Cookie management commands are properly restricted

---

## Admin Commands

- **/start** - Start the bot.
- **/help** - Send help text.
- **/run_time** - Show bot runtime.
- **/log** - Get user logs (e.g., `/log 10101010`).
- **/broadcast** - Broadcast a message to all users (reply to any message with this command).
- **/clean** - Clean the working directory.
- **/usage** - Get all logs.
- **/check_cookie** - Check the cookie file.
- **/save_as_cookie** - Save text as cookie.
- **/download_cookie** - Download the cookie file.
- **/cookies_from_browser** - Get cookies from your browser.
- **/format** - Choose media format options.
- **/block_user** - Block a user (e.g., `/block_user 10101010`).
- **/unblock_user** - Unblock a user (e.g., `/unblock_user 10101010`).
- **/all_users** - Get all users.
- **/all_blocked** - Get all blocked users.
- **/all_unblocked** - Get all unblocked users.
- **/uncache** - Clear cached subtitle language data.
- **/reload_cache** - Reload cache from firebase to local json file
- **/auto_cache** - Control auto cache reload: `/auto_cache on` | `/auto_cache off` | `/auto_cache N` (N = 1..168 hours, persisted to `CONFIG/config.py`).
- **/update_porn** - Run script to update porn domains and keywords from external sources.
- **/reload_porn** - Reload porn detection cache (domains, keywords, supported sites) without restarting the bot.
---

## Auto cache – how it works (on/off/N)

The bot maintains a local JSON cache (dump) of Firebase data. A background reloader can periodically refresh this cache by first downloading a fresh dump and then reloading it into memory.

- Refresh cycle:
  - Download dump via REST (`download_firebase.py` logic)
  - Reload local JSON into memory
- Interval alignment: next run is aligned to steps from midnight (00:00) with your interval step (N hours).
- Logging examples you will see:
  - `🔄 Downloading and reloading Firebase cache dump...`
  - `✅ Firebase cache refreshed successfully!`

### Command usage
- `/auto_cache on` – enable background auto-refresh
- `/auto_cache off` – disable background auto-refresh
- `/auto_cache N` – set refresh interval to N hours (1..168)
  - This immediately updates runtime settings
  - The value is also persisted to `CONFIG/config.py` by updating `RELOAD_CACHE_EVERY = N`
  - The background thread is safely restarted so the new interval takes effect right away

Your current default interval comes from `CONFIG/config.py`:
```python
RELOAD_CACHE_EVERY = 24  # in hours
```

---

## Porn Detection Management

The bot includes advanced porn detection capabilities with configurable domain and keyword lists. Admins can manage these lists using dedicated commands.

### Porn Detection Commands

#### `/update_porn`
Runs an external script to update porn domains and keywords from external sources.

**Features:**
- Executes customizable script (default: `./script.sh`)
- Shows real-time script output and execution status
- Comprehensive error handling and logging
- Script path configurable via `CONFIG/domains.py`

**Configuration:**
```python
# In CONFIG/domains.py
UPDATE_PORN_SCRIPT_PATH = "./script.sh"  # Customize script path
```

#### `/reload_porn`
Reloads the porn detection cache without restarting the bot.

**Features:**
- Hot-reloads porn domains from `TXT/porn_domains.txt`
- Hot-reloads porn keywords from `TXT/porn_keywords.txt`
- Hot-reloads supported sites from `TXT/supported_sites.txt`
- Shows current cache statistics
- Immediate effect - no bot restart required

### File Structure
```
TXT/
├── porn_domains.txt      # List of porn domains (one per line)
├── porn_keywords.txt     # List of porn keywords (one per line)
└── supported_sites.txt   # List of supported video sites

script.sh                 # Update script (customizable)
```

### Integration
These commands integrate with the existing porn detection system:
- **Domain Detection**: Checks video URLs against porn domain lists
- **Keyword Detection**: Scans video titles, descriptions, and captions
- **Auto-tagging**: Automatically adds `#porn` tag to detected content
- **Spoiler Protection**: Hides porn content under spoiler tags in Telegram

### Security
- Both commands are admin-only with proper access control
- Script execution is logged for audit purposes
- Script runs from the bot's root directory
- Script output is captured and displayed to the admin

---

## Updating the bot (updater scripts)

You can update only Python files from the `main` branch of `chelaxian/tg-ytdlp-bot` using provided scripts. The updater will:
- Clone the repository to a temporary directory
- Update only `*.py` files in your working directory
- Preserve your `CONFIG/config.py` and other excluded files/directories
- Make backups of changed files with suffix `.backup_YYYYMMDD_HHMM` and move them into `_backup/` (original structure preserved)
- Ask for confirmation before applying changes

### One-command update (recommended)
```bash
./update.sh
```
- The script checks prerequisites and runs the Python updater.
- After a successful update, restart the bot service (if you use systemd):
```bash
systemctl restart tg-ytdlp-bot
journalctl -u tg-ytdlp-bot -f
```

### Manual update via Python
```bash
python3 update_from_repo.py --show-excluded   # show excluded files/folders
python3 update_from_repo.py                   # interactive update (prompts for confirmation)
```

---

## Restoring from backups

When the updater changes files, it creates backups and moves them into the `_backup/` folder, preserving the original directory structure. Backup filenames have a suffix `.backup_YYYYMMDD_HHMM` (minute-level). The restore tool allows you to revert to a selected backup index.

### Interactive restore (recommended)
```bash
python3 restore_from_backup.py
```
- Use Arrow keys (or j/k) to navigate, PgUp/PgDn for paging, Enter to select, q to quit.
- The list shows grouped backups by minute: `[YYYY-MM-DD HH:MM:SS] files: N (id: YYYYMMDD_HHMM)`.
- After confirmation, all files from that backup are restored to the project root, with the `.backup_YYYYMMDD_HHMM` suffix stripped.

### List available backups
```bash
python3 restore_from_backup.py --list
```
Outputs available backup IDs (newest first) with file counts.

### Non-interactive restore by ID
```bash
python3 restore_from_backup.py --timestamp YYYYMMDD_HHMM
```
Restores all files for the specified backup ID.

### After restore
If you run the bot as a service, restart it:
```bash
systemctl restart tg-ytdlp-bot
journalctl -u tg-ytdlp-bot -f
```

## Link Command Pattern Spec

- **`https://example.com`** \
  Download the video with its original name. \
  If it is a playlist, only the first video is downloaded. 

- **`https://example.com*1*3`**  \
  Download a specified range of videos from the playlist with their original names. 

- **`https://example.com*1*3*name`**  \
  Download a specified range of videos from the playlist with a custom name. \
  Videos will be named as: 
  - `name - Part 1` 
  - `name - Part 2` 

---

## Tags System (Navigation Tags)

You can add tags to any link (video, playlist, audio) directly in your message:

- Format: `https://site.com/link#tag1#tag2#my_tag`
- Tags must start with `#` and contain only letters, digits, and underscore (`_`).
- Tags are automatically added to the caption of the video/audio, separated by spaces.
- All unique tags you send are saved in the `tags.txt` file in your user folder.

### Example of using tags:
```
https://youtu.be/STeeOaX2FBs?si=5rz1QhvuiauZ7A4d#youtube#mytag#tag123
```
The video caption will include:
```
#youtube #mytag #tag123
```

---

### /tags Command

The `/tags` command lets you get a list of all your unique tags (one per line). If the list is long, the bot will send several messages.

**Example:**
```
/tags
```
Response:
```
#youtube
#mytag
#tag123
...
```
---

## Auto-Cleaning User Directories with Crontab

To prevent your server from filling up with downloaded files, you can set up a crontab task that runs every 24 hours and deletes all files in user directories (except for `cookie.txt` and `logs.txt`).

For example, add the following line to your crontab:

```bash
0 0 * * * /usr/bin/find /root/Telegram/tg-ytdlp-bot/users -type f ! -name "cookie.txt" ! -name "logs.txt" -delete
```

**Explanation:**
- `0 0 * * *` – Executes the command every day at midnight.
- `/usr/bin/find /CHANGE/ME/TO/REAL/PATH/TO/tg-ytdlp-bot/users -type f` – Searches for all files under the users directory.
- `! -name "cookie.txt" ! -name "logs.txt"` – Excludes `cookie.txt` and `logs.txt` files from deletion.
- `-delete` – Deletes the files found.

---

## Firebase Setup for Telegram Bot

This section describes how to create a Firebase project, set up the Realtime Database with authentication, create a test user, and integrate Firebase into your Telegram bot.

### 1. Create a Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/) and click **Add Project** (or select an existing project).
2. Follow the setup wizard to create your new project.
3. After the project is created, navigate to **Project Settings** and copy your configuration parameters (such as `apiKey`, `authDomain`, `databaseURL`, `projectId`, etc.). These values are required for configuring the connection in your bot.

### 2. Create a Realtime Database

1. In the Firebase Console, select **Realtime Database**.
2. Click **Create Database**.
3. Choose your database location and set the mode. For initial testing, you may choose **Test Mode** (keep in mind that test mode does not enforce authentication).
4. Once your database is created, update its security rules as described in Step 4.

### 3. Enable Authentication

1. In the left-hand menu of the Firebase Console, select **Authentication**.
2. Click **Get Started**.
3. Navigate to the **Sign-in Method** tab and enable the desired provider. For a basic setup, enable **Email/Password**:
   - Click on **Email/Password**.
   - Toggle the switch to **Enable**.
4. After enabling the sign-in method, create a test user manually in the **Users** tab, or implement user registration in your application.

### 4. Update Realtime Database Security Rules

To restrict access to your database only to authenticated users, update your security rules as follows:

```json
{
  "rules": {
    // Allow access only to authenticated user with certain email
    ".read":  "auth != null && auth.token.email === 'YOUREMAIL@gmail.com'",
    ".write": "auth != null && auth.token.email === 'YOUREMAIL@gmail.com'"
  }
}
```

These rules allow read and write operations only if the request contains a valid `idToken`—meaning the user is authenticated.

### 5. Autostart service

To create auto-start service for this bot - copy text from this file https://github.com/chelaxian/tg-ytdlp-bot/blob/main/etc/systemd/system/tg-ytdlp-bot.service and paste it to 
```bash
/etc/systemd/system/tg-ytdlp-bot.service
```
do not forget to change path in service to yoyr actual path

reload systemctl and enable/start service
```bash
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable tg-ytdlp-bot.service
systemctl restart tg-ytdlp-bot.service
journalctl -u tg-ytdlp-bot -f
```

---

## Troubleshooting

### Common Issues and Solutions

**Bot doesn't start:**
- Check that all required fields in `config.py` are filled
- Verify API credentials are correct
- Ensure both channels are set up and bot has admin permissions
- Check Firebase configuration and credentials

**Cookie download fails:**
- Verify cookie URLs are accessible via HTTPS
- Check file size is under 100KB
- Ensure files are in Netscape cookie format
- Test URLs in browser to confirm they work

**YouTube videos fail to download:**
- Run `/check_cookie` to verify YouTube cookies are working
- Use `/download_cookie` to get fresh cookies
- Check if video is age-restricted or private
- Verify yt-dlp is properly installed and up to date

**Firebase connection errors:**
- Verify Firebase project is set up correctly
- Check authentication credentials
- Ensure Realtime Database rules allow read/write access
- Verify database URL is correct

**Channel subscription issues:**
- Ensure bot is admin in subscription channel
- Check channel invite link is valid
- Verify channel ID format (should start with -100)
- Test channel access manually

### Getting Help

If you encounter issues:
1. Check the bot logs for error messages
2. Verify all configuration fields are correct
3. Test individual components (cookies, Firebase, channels)
4. Check the [GitHub Issues](https://github.com/upekshaip/tg-ytdlp-bot/issues) for similar problems
5. Create a new issue with detailed error information and logs
