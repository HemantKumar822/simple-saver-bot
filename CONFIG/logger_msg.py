class LoggerMsg(object):
    # Generic user/admin/access
    ACCESS_DENIED_ADMIN = "❌ Access denied. Admin only."
    WELCOME_MASTER = "Welcome Master 🥷"

    # URL Extractor / start logs
    USER_STARTED_BOT = "{chat_id} - user started the bot"
    HELP_SENT_TO_USER = "Send help txt to user"
    ADD_BOT_TO_GROUP_SENT = "Send add_bot_to_group txt to user"

    # Image command logs
    IMG_HELP_SHOWN = "Showed /img help"
    INVALID_URL_PROVIDED = "Invalid URL provided: {url}"
    REPOSTED_CACHED_ALBUMS = "Reposted {count} cached albums for {url}"
    FAILED_ANALYZE_IMAGE = "Failed to analyze image URL: {url}"
    STREAMED_AND_SENT_MEDIA = "Streamed and sent {total_sent} media: {url}"
    IMAGE_COMMAND_ERROR = "Error in image command: {url}, error: {error}"

    # Search helper logs
    SEARCH_HELPER_OPENED = "User {user_id} opened search helper"
    SEARCH_HELPER_CLOSED = "User {user_id} closed search command"
    SEARCH_CALLBACK_ERROR = "Error in search callback handler: {error}"

    # Settings menu logs
    SETTINGS_OPENED = "Opened /settings menu"

    # Direct link flows
    DIRECT_LINK_EXTRACTED = "Direct link extracted via {source} for user {user_id} from {url}"
    DIRECT_LINK_FAILED = "Failed to extract direct link via {source} for user {user_id} from {url}: {error}"

    # Cache and sends
    PLAYLIST_VIDEOS_SENT_FROM_CACHE = "Playlist videos sent from cache (quality={quality}) to user {user_id}"
    VIDEO_SENT_FROM_CACHE = "Video sent from cache (quality={quality}) to user {user_id}"
    PLAYLIST_AUDIO_SENT_FROM_CACHE = "Playlist audio sent from cache (quality={quality}) to user{user_id}"
    AUDIO_SENT_FROM_CACHE = "Audio sent from cache (quality={quality}) to user{user_id}"

    # Limits and errors
    SIZE_LIMIT_EXCEEDED = "❌ The file size exceeds the {max_size_gb} GB limit. Please select a smaller file within the allowed size."
    DOWNLOAD_ERROR_GENERIC = "❌ Sorry... Some error occurred during download."
    DOWNLOAD_TIMEOUT_LOG = "Download cancelled due to timeout"

