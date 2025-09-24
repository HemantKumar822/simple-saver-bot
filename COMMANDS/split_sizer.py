from pyrogram import filters
from CONFIG.config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from HELPERS.app_instance import get_app
from HELPERS.filesystem_hlp import create_directory
from HELPERS.logger import send_to_logger, logger
from HELPERS.safe_messeger import safe_send_message, safe_edit_message_text
from HELPERS.limitter import humanbytes, is_user_in_channel
import re

def parse_size_argument(arg):
    """
    Parse size argument and return size in bytes
    
    Args:
        arg (str): Size argument (e.g., "250mb", "1.5gb", "2GB", "100mb", "2000mb")
        
    Returns:
        int: Size in bytes or None if invalid
    """
    if not arg:
        return None
    
    # Remove spaces and convert to lowercase
    arg = arg.lower().replace(" ", "")
    
    # Match patterns like "250mb", "1.5gb", "2GB", "100mb", "2000mb"
    match = re.match(r'^(\d+(?:\.\d+)?)(mb|gb)$', arg)
    if not match:
        return None
    
    number = float(match.group(1))
    unit = match.group(2)
    
    # Convert to bytes
    if unit == "mb":
        size_bytes = int(number * 1024 * 1024)
    elif unit == "gb":
        size_bytes = int(number * 1024 * 1024 * 1024)
    else:
        return None
    
    # Check limits: 100MB to 2GB
    min_size = 100 * 1024 * 1024  # 100MB
    max_size = 2 * 1024 * 1024 * 1024  # 2GB
    
    if size_bytes < min_size:
        return None  # Too small
    elif size_bytes > max_size:
        return None  # Too large
    
    return size_bytes

# Get app instance for decorators
app = get_app()

@app.on_message(filters.command("split") & filters.private)
# @reply_with_keyboard
def split_command(app, message):
    user_id = message.chat.id
    # Subscription check for non-admines
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return
    
    # Check if arguments are provided
    if len(message.command) > 1:
        arg = message.command[1].lower()
        size = parse_size_argument(arg)
        if size:
            # Apply size directly
            user_dir = os.path.join("users", str(user_id))
            create_directory(user_dir)
            split_file = os.path.join(user_dir, "split.txt")
            with open(split_file, "w", encoding="utf-8") as f:
                f.write(str(size))
            
            safe_send_message(user_id, f"✅ Split part size set to: {humanbytes(size)}", message=message)
            send_to_logger(message, f"Split size set to {size} bytes via argument.")
            return
        else:
            safe_send_message(user_id, 
                "❌ **Invalid size!**\n\n"
                "**Valid range:** 100MB to 2GB\n\n"
                "**Valid formats:**\n"
                "• `100mb` to `2000mb` (megabytes)\n"
                "• `0.1gb` to `2gb` (gigabytes)\n\n"
                "**Examples:**\n"
                "• `/split 100mb` - 100 megabytes\n"
                "• `/split 500mb` - 500 megabytes\n"
                "• `/split 1.5gb` - 1.5 gigabytes\n"
                "• `/split 2gb` - 2 gigabytes\n"
                "• `/split 2000mb` - 2000 megabytes (2GB)\n\n"
                "**Presets:**\n"
                "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
            , message=message)
            return
    
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    # 2-3 row buttons with more presets
    sizes = [
        ("100 MB", 100 * 1024 * 1024),
        ("250 MB", 250 * 1024 * 1024),
        ("500 MB", 500 * 1024 * 1024),
        ("750 MB", 750 * 1024 * 1024),
        ("1 GB", 1024 * 1024 * 1024),
        ("1.5 GB", 1536 * 1024 * 1024),
        ("2 GB (max)", 2 * 1024 * 1024 * 1024)
    ]
    buttons = []
    # Pass the buttons in 2-3 rows
    for i in range(0, len(sizes), 2):
        row = []
        for j in range(2):
            if i + j < len(sizes):
                text, size = sizes[i + j]
                row.append(InlineKeyboardButton(text, callback_data=f"split_size|{size}"))
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🔚Close", callback_data="split_size|close")])
    keyboard = InlineKeyboardMarkup(buttons)
    safe_send_message(user_id, 
        "🎬 **Choose max part size for video splitting:**\n\n"
        "**Range:** 100MB to 2GB\n\n"
        "**Quick commands:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Examples:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`", 
        reply_markup=keyboard,
        message=message
    )
    send_to_logger(message, "User opened /split menu.")

@app.on_callback_query(filters.regex(r"^split_size\|"))
# @reply_with_keyboard
def split_size_callback(app, callback_query):
    logger.info(f"[SPLIT] callback: {callback_query.data}")
    user_id = callback_query.from_user.id
    data = callback_query.data.split("|")[1]
    if data == "close":
        try:
            callback_query.message.delete()
        except Exception:
            callback_query.edit_message_reply_markup(reply_markup=None)
        try:
            callback_query.answer("Menu closed.")
        except Exception:
            pass
        send_to_logger(callback_query.message, "Split selection closed.")
        return
    try:
        size = int(data)
    except Exception:
        callback_query.answer("Invalid size.")
        return
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    split_file = os.path.join(user_dir, "split.txt")
    with open(split_file, "w", encoding="utf-8") as f:
        f.write(str(size))
    safe_edit_message_text(callback_query.message.chat.id, callback_query.message.id, f"✅ Split part size set to: {humanbytes(size)}")
    send_to_logger(callback_query.message, f"Split size set to {size} bytes.")

# --- Function for reading split.txt ---
def get_user_split_size(user_id):
    user_dir = os.path.join("users", str(user_id))
    split_file = os.path.join(user_dir, "split.txt")
    if os.path.exists(split_file):
        try:
            with open(split_file, "r", encoding="utf-8") as f:
                size = int(f.read().strip())
                return size
        except Exception:
            pass
    return 1950 * 1024 * 1024  # default 1.95GB

