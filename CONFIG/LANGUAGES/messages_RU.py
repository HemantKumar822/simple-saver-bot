# Messages Configuration

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = "<blockquote><i>Managed by</i> @iilililiiillliiliililliilliliiil\n🇮🇹 @tgytdlp_it_bot\n🇦🇪 @tgytdlp_uae_bot\n🇬🇧 @tgytdlp_uk_bot\n🇫🇷 @tgytdlp_fr_bot</blockquote>"
    TO_USE_MSG = "<i>Для использования этого бота вам нужно подписаться на канал @tg_ytdlp Telegram.</i>\nПосле того, как вы присоединитесь к каналу, <b>отправьте ссылку на видео снова, и бот скачает его для вас</b> ❤️  "

    ERROR1 = "Не найдена ссылка URL. Пожалуйста, введите URL с <b>https://</b> или <b>http://</b>"

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>Плейлисты (yt-dlp)</b>

Для скачивания плейлистов отправьте его URL с диапазонами <code>*начало*конец</code> в конце. Например: <code>URL*1*5</code>.
Или вы можете использовать <code>/vid ОТ-ДО URL</code>. Например: <code>/vid 3-7 URL</code>. Также работает для команды <code>/audio</code>.

<b>Примеры:</b>

🟥 <b>Диапазон видео из плейлиста YouTube:</b> (нужны 🍪)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(скачивает видео с 1 по 5 включительно)
🟥 <b>Одно видео из плейлиста YouTube:</b> (нужны 🍪)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(скачивает только 3-е видео)

⬛️ <b>Профиль TikTok:</b> (нужны ваши 🍪)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(скачивает первые 10 видео из профиля пользователя)

🟪 <b>Истории Instagram:</b> (нужны ваши 🍪)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(скачивает первые 3 истории)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(скачивает первые 10 историй из альбома)

🟦 <b>Видео VK:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(скачивает первые 3 видео из профиля пользователя/группы)

⬛️<b>Каналы Rutube:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(скачивает видео с 2 по 4 включительно из канала)

🟪 <b>Клипы Twitch:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(скачивает первые 3 клипа из канала)

🟦 <b>Группы Vimeo:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(скачивает первые 2 видео из группы)

🟧 <b>Модели Pornhub:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(скачивает первые 2 видео из профиля модели)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(скачивает первые 3 видео из результатов поиска по вашему запросу)

и так далее...
см. <a href=\"https://raw.githubusercontent.com/yt-dlp/yt-dlp/refs/heads/master/supportedsites.md\">список поддерживаемых сайтов</a>
</blockquote>

<blockquote expandable>🖼 <b>Изображения (gallery-dl)</b>

Используйте <code>/img URL</code> для скачивания изображений/фото/альбомов с множества платформ.

<b>Примеры:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>Диапазоны:</b>
<code>/img 11-20 https://example.com/album</code> — элементы 11..20
<code>/img 11- https://example.com/album</code> — с 11 до конца (или лимит бота)

<i>Поддерживаемые платформы включают vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, и т.д. Полный список:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">поддерживаемые сайты gallery-dl</a>
</blockquote>
"""
    HELP_MSG = """
🎬 <b>Бот для скачивания видео - Помощь</b>

📥 <b>Основное использование:</b>
• Отправьте любую ссылку → бот скачает её
  <i>бот автоматически попробует скачать видео через yt-dlp и изображения через gallery-dl.</i>
• <code>/audio URL</code> → извлечь аудио
• <code>/link [качество] URL</code> → получить прямые ссылки
• <code>/proxy</code> → включить/выключить прокси для всех загрузок
• Ответьте на видео текстом → изменить подпись

📋 <b>Плейлисты и диапазоны:</b>
• <code>URL*1*5</code> → скачать видео 1-5
• <code>/vid 3-7 URL</code> → становится <code>URL*3*7</code>

🍪 <b>Cookies и приватные:</b>
• Загрузите *.txt cookie для приватных видео
• <code>/cookie [сервис]</code> → скачать куки (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → выбрать источник по индексу (1–N)
• <code>/cookies_from_browser</code> → извлечь из браузера
• <code>/check_cookie</code> → проверить cookie
• <code>/save_as_cookie</code> → сохранить текст как cookie

🧹 <b>Очистка:</b>
• <code>/clean</code> → только медиа файлы
• <code>/clean all</code> → всё
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Настройки:</b>
• <code>/settings</code> → меню настроек
• <code>/format</code> → качество и формат
• <code>/split</code> → разделить видео на части
• <code>/mediainfo on/off</code> → информация о медиа
• <code>/nsfw on/off</code> → размытие NSFW
• <code>/tags</code> → просмотр сохранённых тегов
• <code>/sub on/off</code> → субтитры
• <code>/keyboard</code> → клавиатура (OFF/1x3/2x3)

🏷️ <b>Теги:</b>
• Добавьте <code>#тег1#тег2</code> после URL
• Теги появляются в подписях
• <code>/tags</code> → просмотр всех тегов

🔗 <b>Прямые ссылки:</b>
• <code>/link URL</code> → лучшее качество
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → конкретное качество

⚙️ <b>Быстрые команды:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → установить качество
• <code>/keyboard off/1x3/2x3/full</code> → раскладка клавиатуры
• <code>/split 100mb-2000mb</code> → изменить размер части
• <code>/subs off/ru/en auto</code> → язык субтитров
• <code>/list URL</code> → список доступных форматов
• <code>/mediainfo on/off</code> → вкл/выкл медиаинфо
• <code>/proxy on/off</code> → включить/выключить прокси для всех загрузок

📊 <b>Информация:</b>
• <code>/usage</code> → история загрузок
• <code>/search</code> → поиск через @vid

🖼 <b>Изображения:</b>
• <code>URL</code> → скачать изображения с URL
• <code>/img URL</code> → скачать изображения с URL
• <code>/img 11-20 URL</code> → скачать конкретный диапазон
• <code>/img 11- URL</code> → скачать с 11-го до конца

<blockquote expandable>🇷🇺 <b>Бот для скачивания видео - Помощь</b>

📥 <b>Основное:</b>
• Отправьте любую ссылку → бот скачает её
  <i>бот автоматически попробует скачать видео через yt-dlp и изображения через gallery-dl.</i>
• <code>/audio URL</code> → аудио
• <code>/link [качество] URL</code> → прямые ссылки
• <code>/proxy</code> → включить/выключить прокси для всех загрузок
• Ответьте на видео текстом → изменить подпись

📋 <b>Плейлисты:</b>
• <code>URL*1*5</code> → скачать видео 1-5
• <code>/vid 3-7 URL</code> → становится <code>URL*3*7</code>

🍪 <b>Cookies:</b>
• Загрузите *.txt для приватных видео
• <code>/cookie [сервис]</code> → скачать куки (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → выбрать источник по индексу (1–N)
• <code>/cookies_from_browser</code> → из браузера
• <code>/check_cookie</code> → проверить cookie
• <code>/save_as_cookie</code> → сохранить текст как cookie

🧹 <b>Очистка:</b>
• <code>/clean</code> → медиа файлы
• <code>/clean all</code> → всё
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>Настройки:</b>
• <code>/settings</code> → меню настроек
• <code>/format</code> → качество и формат
• <code>/split</code> → резать видео на части
• <code>/mediainfo on/off</code> → информация о файле
• <code>/nsfw on/off</code> → размытие NSFW
• <code>/tags</code> → ваши теги
• <code>/sub on/off</code> → субтитры
• <code>/keyboard</code> → клавиатура (OFF/1x3/2x3)

🏷️ <b>Теги:</b>
• Добавьте <code>#тег1#тег2</code> после ссылки
• Теги появляются в подписях
• <code>/tags</code> → все теги

🔗 <b>Прямые ссылки:</b>
• <code>/link URL</code> → лучшее качество
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → конкретное качество

⚙️ <b>Быстрые команды:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → качество
• <code>/keyboard off/1x3/2x3/full</code> → клавиатура
• <code>/split 100mb-2000mb</code> → резать видео на части
• <code>/subs off/ru/en auto</code> → язык субтитров
• <code>/list URL</code> → список доступных форматов
• <code>/mediainfo on/off</code> → вкл/выкл медиаинфо
• <code>/proxy on/off</code> → включить/выключить прокси для всех загрузок

📊 <b>Информация:</b>
• <code>/usage</code> → история загрузок
• <code>/search</code> → поиск через @vid

🖼 <b>Изображения:</b>
• <code>URL</code> → скачать изображения с URL
• <code>/img URL</code> → скачать изображения с URL
• <code>/img 11-20 URL</code> → скачать конкретный диапазон
• <code>/img 11- URL</code> → скачать с 11-го до конца
</blockquote>

👨‍💻 <i>Developer:</i> @upekshaip
🤝 <i>Contributor:</i> @IIlIlIlIIIlllIIlIIlIllIIllIlIIIl
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "Just save your cookie as <b><u>cookie.txt</u></b> and send it to bot as a document.\n\n"
        "You can also send cookies as plain text with <b><u>/save_as_cookie</u></b> command.\n"
        "<b>Usage of <b><u>/save_as_cookie</u></b>:</b>\n\n"
        "<pre>"
        "/save_as_cookie\n"
        "# Netscape HTTP Cookie File\n"
        "# http://curl.haxx.se/rfc/cookie_spec.html\n"
        "# This file was generated by Cookie-Editor\n"
        ".youtube.com  TRUE  /  FALSE  111  ST-xxxxx  session_logininfo=AAA\n"
        ".youtube.com  TRUE  /  FALSE  222  ST-xxxxx  session_logininfo=BBB\n"
        ".youtube.com  TRUE  /  FALSE  33333  ST-xxxxx  session_logininfo=CCC\n"
        "</pre>\n"
        "<blockquote>"
        "<b><u>Instructions:</u></b>\n"
        "https://t.me/c/2303231066/18 \n"
        "https://t.me/c/2303231066/22 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>Video search</b>

Press the button below to activate inline search via @vid.

<blockquote>On PC just type <b>"@vid Your_Search_Query"</b> in any chat.</blockquote>
    """
    
    # Settings and Hints (English)
    
    AUDIO_HINT_MSG = (
        "Download only audio from video source.\n\n"
        "Usage: /audio + URL \n\n"
        "(ex. /audio https://youtu.be/abc123)\n"
        "(ex. /audio https://youtu.be/playlist?list=abc123*1*10)"
    )
    
    IMG_HELP_MSG = (
        "<b>🖼 Image Download Command</b>\n\n"
        "Usage: <code>/img URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>Supported platforms (examples):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, etc. — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">full list</a></blockquote>"
        "Also see: "
    )
    
    LINK_HINT_MSG = (
        "Get direct video links with quality selection.\n\n"
        "Usage: /link + URL \n\n"
        "(ex. /link https://youtu.be/abc123)\n"
        "(ex. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>Add Bot to Group</b>

Add my bots to your groups to get enhanced features and higher limits!
————————————
📊 <b>Current FREE Limits (in Bot’s DM):</b>
<blockquote>•🗑 Messy junk from all the files unsorted 👎
• Max 1 file size: <b>8 GB </b>
• Max 1 file quality: <b>UNLIM</b>
• Max 1 file duration: <b>UNLIM</b>
• Max number of downloads: <b>UNLIM</b>
• Max playlist items per 1 time: <b>50</b>
• Max TikTok videos per 1 time: <b>500</b>
• Max images per 1 time: <b>1000</b>
• 1 Download max time: <b>2 hours</b>
• 🔞 NSFW content is paid! 1⭐️ = $0.02
• 🆓 ALL OTHER MEDIA ARE TOTALY FREE
• 📝 All content logs & caching to my log-channels for instant repost when re-downloading</blockquote>

💬<b>This limits only for video with subtitles:</b>
<blockquote>• Max video+subs duration: <b>1.5 hours</b>
• Max video+subs file size: <b>500 MB</b>
• Max video+subs quality: <b>720p</b></blockquote>
————————————
🚀 <b>Paid Group Benefits (2️⃣x Limits):</b>
<blockquote>•  🗂 Structured neat media vault sorted by topics 👍
•  📁 Bots reply in the topic you call them
•  📌 Auto pin status message with download progress
•  🖼 /img command downloads media as 10-item albums
• Max 1 file size: <b>16 GB</b> ⬆️
• Max playlist items per 1 time: <b>100</b> ⬆️
• Max TikTok videos per 1 time: 1000 ⬆️
• Max images per 1 time: 2000 ⬆️
• 1 Download max time: <b>4 hours</b> ⬆️
• 🔞 NSFW content: Free with full metadata 🆓
• 📢 No need to subscribe to my channel for groups
• 👥 All group members will have access to paid functions!
• 🗒 No logs / no cache to my log-channels! You can reject copy/repost in group settings</blockquote>

💬 <b>2️⃣x limits for video with subtitles:</b>
<blockquote>• Max video+subs duration: <b>3 hours</b> ⬆️
• Max video+subs file size: <b>1000 MB</b> ⬆️
• Max video+subs quality: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>Pricing & Setup:</b>
<blockquote>• Price: <b>$5/month</b> per 1 bot in group
• Setup: Contact @iilililiiillliiliililliilliliiil
• Payment: 💎TON or other methods💲
• Support: Full technical support included</blockquote>
————————————
You can add my bots to your group to unblock free 🔞<b>NSFW</b> and to double (x2️⃣) all limits.
Contact me if you want me to allow your group to use my bots @iilililiiillliiliililliilliliiil
————————————
💡<b>TIP:</b> <blockquote>You can chip in money with any amount of your friends (for example 100 people) and made 1 purchase for whole group - ALL GROUP MEMBERS WILL HAVE FULL UNLIMITED ACCESS to all bots functions in that group for just <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW Mode: ON✅</b>

• NSFW content will be displayed without blurring.
• Spoilers will not apply to NSFW media.
• The content will be visible immediately

<i>Use /nsfw off to enable blur</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW Mode: OFF</b>

⚠️ <b>Blur enabled</b>
• NSFW content will be hidden under spoiler   
• To view, you will need to click on the media
• Spoilers will apply to NSFW media.

<i>Use /nsfw on to disable blur</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>Invalid parameter</b>

Use:
• <code>/nsfw on</code> - disable blur
• <code>/nsfw off</code> - enable blur
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>Проверка кэша...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 Обработка..."
    DOWNLOADING_MSG = "📥 <b>Загрузка медиа...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>Загрузка изображения...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>Загрузка завершена</b>\n\n"
    VIDEO_PROCESSING_MSG = "📽 Видео обрабатывается..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>Отправлено из кэша</b>\n\nОтправлено альбомов: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ Видео успешно отправлено из кэша."
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ Видео плейлиста отправлены из кэша ({cached}/{total} файлов)."
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} видео отправлены из кэша, загружаем недостающие..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>Неверный URL</b>\n\nПожалуйста, предоставьте действительный URL, начинающийся с http:// или https://"

    ERROR_OCCURRED_MSG = "❌ <b>Произошла ошибка</b>\n\n<code>{url}</code>\n\nОшибка: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ Ошибка отправки видео: {error}"
    ERROR_UNKNOWN_MSG = "❌ Неизвестная ошибка: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ Недостаточно места на диске для загрузки видео."
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ Размер файла превышает лимит {limit} ГБ. Пожалуйста, выберите файл меньшего размера в пределах допустимого."

    ERROR_GETTING_LINK_MSG = "❌ <b>Ошибка получения ссылки:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ограничил отправку сообщений.\n⏳ Пожалуйста, подождите: {time}\nДля обновления таймера отправьте URL еще 2 раза."
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ограничил отправку сообщений.\n⏳ Пожалуйста, подождите: \nДля обновления таймера отправьте URL еще 2 раза."
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ Не удалось загрузить субтитры"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>Прямые ссылки на поток</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>Название:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>Длительность:</b> {duration} сек\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Ошибка: Original Сообщение not found."

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{tag} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ Playlist videos sent: {sent}/{total} files."
    PLAYLIST_CACHE_SENT_MSG = "✅ Sent from cache: {cached}/{total} files."
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ Не удалось К get stream links"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "Выбрать a Браузер К Скачать cookies От:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Нет browsers found На this Система. You can Скачать cookies От Удаленный URL or monitor Браузер Статус:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Open Browser</b> - to monitor browser status in mini-app"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Открыть Браузер"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Скачать От Удаленный URL"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie Файл downloaded via fallback and saved as cookie.txt"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No supported browsers found and no COOKIE_URL configured. Use /cookie or upload cookie.txt."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL must point to a .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback cookie Файл is too large (>100KB)."
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback cookie source unavailable (status {status}). Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Ошибка Загрузка fallback cookie. Try /cookie or Загрузить cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unexpected Ошибка Во время fallback cookie Скачать."
    BTN_CLOSE = "🔚Close"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ Недействительно Булевый Значение"
    ARGS_CLOSED_MSG = "Закрыт"
    ARGS_ALL_RESET_MSG = "✅ Все arguments Сбросить"
    ARGS_RESET_ERROR_MSG = "❌ Ошибка resetting arguments"
    ARGS_INVALID_PARAM_MSG = "❌ Недействительно parameter"
    ARGS_BOOL_SET_MSG = "Set to {value}"
    ARGS_BOOL_ALREADY_SET_MSG = "Already set to {value}"
    ARGS_INVALID_SELECT_MSG = "❌ Недействительно Выбрать Значение"
    ARGS_VALUE_SET_MSG = "Set to {value}"
    ARGS_VALUE_ALREADY_SET_MSG = "Already set to {value}"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>Current value:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>Examples:</b>\n• <code>default</code> - Use default XFF strategy\n• <code>never</code> - Never use XFF header\n• <code>US</code> - United States country code\n• <code>GB</code> - United Kingdom country code\n• <code>DE</code> - Germany country code\n• <code>FR</code> - France country code\n• <code>JP</code> - Japan country code\n• <code>192.168.1.0/24</code> - IP block (CIDR)\n• <code>10.0.0.0/8</code> - Private IP range\n• <code>203.0.113.0/24</code> - Public IP block\n\n"
    ARGS_XFF_NOTE_MSG = "<b>Note:</b> This replaces --geo-bypass options. Use any 2-letter country code or IP block in CIDR notation.\n\n"
    ARGS_EXAMPLE_MSG = "<b>Example:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "Please Отправить your Новый Значение."
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>Range:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "Please Отправить a Число."
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>Examples:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>Note:</b> These headers will be added to existing Referer and User-Agent headers.\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 Current yt-dlp Arguments:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>Boolean</b> - True/False switches\n• 📋 <b>Select</b> - Choose from options\n• 🔢 <b>Numeric</b> - Number input\n• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\nThese settings will be applied to all your downloads."
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp Arguments Configuration</b>\n\n<blockquote>📋 <b>Groups:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp Arguments Configuration</b>\n\n"
        "<blockquote>📋 <b>Groups:</b>\n"
        "• ✅/❌ <b>Boolean</b> - True/False switches\n"
        "• 📋 <b>Select</b> - Choose from options\n"
        "• 🔢 <b>Numeric</b> - Number input\n"
        "• 📝🔧 <b>Text</b> - Text/JSON input</blockquote>\n\n"
        "These settings will be applied to all your downloads."
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ Пожалуйста, подождите..."
    ERROR_OCCURRED_SHORT_MSG = "❌ Ошибка occurred"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Input Режим automatically Закрыт Срок К inactivity (5 minutes)."
    ARGS_INPUT_DANGEROUS_MSG = "❌ Input contains potentially dangerous content: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ Input too long (max 1000 characters)"
    ARGS_INVALID_URL_MSG = "❌ Invalid URL format. Must start with http:// or https://"
    ARGS_INVALID_JSON_MSG = "❌ Недействительно JSON Формат"
    ARGS_NUMBER_RANGE_MSG = "❌ Number must be between {min_val} and {max_val}"
    ARGS_INVALID_NUMBER_MSG = "❌ Недействительно Число Формат"
    ARGS_DATE_FORMAT_MSG = "❌ Дата must be В YYYYMMDD Формат (e.g., 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ Year must be Между 1900 and 2100"
    ARGS_MONTH_RANGE_MSG = "❌ Month must be Между 01 and 12"
    ARGS_DAY_RANGE_MSG = "❌ Day must be Между 01 and 31"
    ARGS_INVALID_DATE_MSG = "❌ Недействительно Дата Формат"
    ARGS_INVALID_XFF_MSG = "❌ XFF must be 'По умолчанию', 'never', Страна code (e.g., US), or IP Заблокировать (e.g., 192.168.1.0/24)"
    ARGS_NO_CUSTOM_MSG = "Нет Пользовательский arguments Множество. Все parameters use По умолчанию values."
    ARGS_RESET_SUCCESS_MSG = "✅ Все arguments Сбросить К defaults."
    ARGS_TEXT_TOO_LONG_MSG = "❌ Текст too long. Максимум 500 characters."
    ARGS_ERROR_PROCESSING_MSG = "❌ Ошибка Обработка input. Пожалуйста, попробуйте снова."
    ARGS_BOOL_INPUT_MSG = "❌ Please enter 'Истина' or 'Ложь' for Отправить As Файл Опция."
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ Please provide a Действительно Число."
    ARGS_BOOL_VALUE_REQUEST_MSG = "Please send <code>True</code> or <code>False</code> to enable/disable this option."
    ARGS_JSON_VALUE_REQUEST_MSG = "Please Отправить Действительно JSON."
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "You have Нет tags Еще."
    TAGS_MESSAGE_CLOSED_MSG = "Tags Сообщение Закрыт."
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ Subtitles Отключен and Always Ask Режим turned Выкл."
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ SUBS Always Ask Включен."
    SUBS_LANGUAGE_SET_MSG = "✅ Subtitle language set to: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️WARNING: due to high CPU impact this function is very slow (near real-time) and limited to:\n"
        "- 720p max quality\n"
        "- 1.5 hour max duration\n"
        "- 500mb max video size</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>Quick commands:</b>\n"
        "• <code>/subs off</code> - disable subtitles\n"
        "• <code>/subs on</code> - enable Always Ask mode\n"
        "• <code>/subs ru</code> - set language\n"
        "• <code>/subs ru auto</code> - set language with AUTO/TRANS"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitles are Отключен"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Selected language: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 Загрузка subtitles..."
    SUBS_DISABLED_ERROR_MSG = "❌ Subtitles are Отключен. Use /subs К configure."
    SUBS_YOUTUBE_ONLY_MSG = "❌ Subtitle Загрузка is Только supported for YouTube."
    SUBS_CAPTION_MSG = (
        "<b>💬 Subtitles</b>\n\n"
        "<b>Video:</b> {title}\n"
        "<b>Language:</b> {lang}\n"
        "<b>Type:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 Subtitles SRT-Файл sent К Пользователь."
    SUBS_ERROR_PROCESSING_MSG = "❌ Ошибка Обработка subtitle Файл."
    SUBS_ERROR_DOWNLOAD_MSG = "❌ Не удалось К Скачать subtitles."
    SUBS_ERROR_MSG = "❌ Error downloading subtitles: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ Split part size set to: {size}"
    SPLIT_INVALID_SIZE_MSG = (
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
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **Choose max part size for video splitting:**\n\n"
        "**Range:** 100MB to 2GB\n\n"
        "**Quick commands:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**Examples:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "Меню Закрыт."
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>Bot Settings</b>\n\nChoose a category:"
    SETTINGS_MENU_CLOSED_MSG = "Меню Закрыт."
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 MEDIA</b>\n\nChoose an action:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 INFO</b>\n\nChoose an action:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ MORE COMMANDS</b>\n\nChoose an action:"
    SETTINGS_COMMAND_EXECUTED_MSG = "Command executed."
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ Flood Лимит. Try Позже."
    SETTINGS_HINT_SENT_MSG = "Подсказка sent."
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "Поиск helper opened."
    SETTINGS_UNKNOWN_COMMAND_MSG = "Unknown command."
    SETTINGS_HINT_CLOSED_MSG = "Подсказка Закрыт."
    SETTINGS_HELP_SENT_MSG = "Отправить Помощь txt К Пользователь"
    SETTINGS_MENU_OPENED_MSG = "Opened /Настройки Меню"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 Поиск helper Закрыт"
    SEARCH_CLOSED_MSG = "Закрыт"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ Proxy {status}."
    PROXY_ERROR_SAVING_MSG = "❌ Ошибка saving proxy Настройки."
    PROXY_MENU_TEXT_MSG = "Включить or Отключить using proxy Сервер for Все yt-dlp operations?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "Enable or disable using proxy servers ({count} available) for all yt-dlp operations?\n\nWhen enabled, proxies will be selected using {method} method."
    PROXY_MENU_CLOSED_MSG = "Меню Закрыт."
    PROXY_ENABLED_CONFIRM_MSG = "✅ Proxy Включен. Все yt-dlp operations will use proxy."
    PROXY_ENABLED_MULTIPLE_MSG = "✅ Proxy enabled. All yt-dlp operations will use {count} proxy servers with {method} selection method."
    PROXY_DISABLED_MSG = "❌ Proxy Отключен."
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ Ошибка saving proxy Настройки."
    PROXY_ENABLED_CALLBACK_MSG = "Proxy Включен."
    PROXY_DISABLED_CALLBACK_MSG = "Proxy Отключен."
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ WAIT До YOUR Предыдущий Скачать IS FINISHED"
    AUDIO_HELP_MSG = (
        "<b>🎧 Audio Download Command</b>\n\n"
        "Usage: <code>/audio URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "Also see: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "Аудио Подсказка Закрыт."
    PLAYLIST_HELP_CLOSED_MSG = "Playlist Помощь Закрыт."
    USERLOGS_CLOSED_MSG = "Логи Сообщение Закрыт."
    HELP_CLOSED_MSG = "Помощь Закрыт."
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW Blur Settings</b>\n\nNSFW content is <b>{status}</b>.\n\nChoose whether to blur NSFW content:"
    NSFW_MENU_CLOSED_MSG = "Меню Закрыт."
    NSFW_BLUR_DISABLED_MSG = "NSFW blur Отключен."
    NSFW_BLUR_ENABLED_MSG = "NSFW blur Включен."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur Отключен."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur Включен."
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}."
    MEDIAINFO_MENU_TITLE_MSG = "Включить or Отключить sending MediaInfo for downloaded files?"
    MEDIAINFO_MENU_CLOSED_MSG = "Меню Закрыт."
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo Включен. После Загрузка, Файл Информация will be sent."
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo Отключен."
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo Включен."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo Отключен."
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 List Available Formats</b>\n\n"
        "Get available video/audio formats for a URL.\n\n"
        "<b>Usage:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>Examples:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 How to use format IDs:</b>\n"
        "After getting the list, use specific format ID:\n"
        "• <code>/format id 401</code> - download format 401\n"
        "• <code>/format id401</code> - same as above\n\n"
        "This command will show all available formats that can be downloaded."
    )
    LIST_PROCESSING_MSG = "🔄 Getting Доступно formats..."
    LIST_INVALID_URL_MSG = "❌ Please provide a valid URL starting with http:// or https://"
    LIST_CAPTION_MSG = (
        "📃 Available formats for:\n<code>{url}</code>\n\n"
        "💡 <b>How to set format:</b>\n"
        "• <code>/format id 134</code> - Download specific format ID\n"
        "• <code>/format 720p</code> - Download by quality\n"
        "• <code>/format best</code> - Download best quality\n"
        "• <code>/format ask</code> - Always ask for quality\n\n"
        "{audio_note}\n"
        "📋 Use format ID from the list above"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>Audio-only formats:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - Download format 140 as MP3 audio\n"
        "• <code>/format id140 audio</code> - same as above\n"
        "These will be downloaded as MP3 audio files.\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ Error sending formats file: {error}"
    LIST_ERROR_GETTING_MSG = "❌ Failed to get formats:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ An Ошибка occurred Пока Обработка the command"
    LIST_ERROR_CALLBACK_MSG = "Ошибка occurred"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 How to use format IDs:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "After getting the list, use specific format ID:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - download format 401\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - same as above\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - download format 140 as MP3 audio\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - same as above\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 Audio-only formats detected: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "These formats will be downloaded as MP3 audio files.\n"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>Usage:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>Examples:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - best quality\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p or lower\n"
        "• /link 720p https://youtube.com/watch?v=... - same as above\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K or lower\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K or lower"
        "</blockquote>\n\n"
        "<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ Please provide a Действительно URL"
    LINK_PROCESSING_MSG = "🔗 Getting direct Ссылка..."
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **Invalid argument!**\n\n"
        "Valid options: `off`, `1x3`, `2x3`, `full`\n\n"
        "Example: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **Keyboard Settings**\n\n"
        "Current: **{current}**\n\n"
        "Choose an option:\n\n"
        "Or use: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    KEYBOARD_HIDDEN_MSG = "⌨️ Keyboard hidden"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 keyboard activated!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 keyboard activated!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 Emoji keyboard activated!"
    KEYBOARD_ERROR_APPLYING_MSG = "Error applying keyboard setting {setting}: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ Формат Множество К: Always Ask. You will be prompted for Качество each Время you Отправить a URL."
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат Множество К: Always Ask. Now you will be prompted for Качество each Время you Отправить a URL."
    FORMAT_BEST_UPDATED_MSG = "✅ Format updated to best quality (AVC+MP4 priority):\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ Format updated to ID {id}:\n{format}\n\n💡 <b>Note:</b> If this is an audio-only format, it will be downloaded as MP3 audio file."
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ Format updated to ID {id} (audio-only):\n{format}\n\n💡 This will be downloaded as MP3 audio file."
    FORMAT_QUALITY_UPDATED_MSG = "✅ Format updated to quality {quality}:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ Format updated to:\n{format}"
    FORMAT_MENU_MSG = (
        "Select a format option or send a custom one using:\n"
        "• <code>/format &lt;format_string&gt;</code> - custom format\n"
        "• <code>/format 720</code> - 720p quality\n"
        "• <code>/format 4k</code> - 4K quality\n"
        "• <code>/format 8k</code> - 8K quality\n"
        "• <code>/format id 401</code> - specific format ID\n"
        "• <code>/format ask</code> - always show menu\n"
        "• <code>/format best</code> - bv+ba/best quality"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "To use a custom format, send the command in the following form:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "Replace <code>bestvideo+bestaudio/best</code> with your desired format string."
    )
    FORMAT_RESOLUTION_MENU_MSG = "Выбрать your desired resolution and codec:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ Формат Множество К: Always Ask. Now you will be prompted for Качество each Время you Отправить a URL."
    FORMAT_UPDATED_MSG = "✅ Format updated to:\n{format}"
    FORMAT_SAVED_MSG = "✅ Формат saved."
    FORMAT_CHOICE_UPDATED_MSG = "✅ Формат Выбор updated."
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "Пользовательский Формат Меню Закрыт"
    FORMAT_CODEC_SET_MSG = "✅ Codec set to {codec}"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ Браузер Выбор updated."
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    ACCESS_DENIED_ADMIN = "❌ Access denied. Admin only."
    WELCOME_MASTER = "Welcome Master 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ Sorry... Some error occurred during download."
    SIZE_LIMIT_EXCEEDED = "❌ The file size exceeds the {max_size_gb} GB limit. Please select a smaller file within the allowed size."
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script not found: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Downloading fresh Firebase dump using {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase cache reloaded successfully!"
    ADMIN_CACHE_FAILED_MSG = "❌ Failed to reload Firebase cache. Check if {cache_file} exists."
    ADMIN_ERROR_RELOADING_MSG = "❌ Error reloading cache: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ Error running {script_path}:\n{stdout}\n{stderr}"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ Script not found: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ Downloading fresh Firebase dump using {script_path} ..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase cache reloaded successfully!"
    ADMIN_CACHE_FAILED_MSG = "❌ Failed to reload Firebase cache. Check if {cache_file} exists."
    ADMIN_ERROR_RELOADING_MSG = "❌ Error reloading cache: {error}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ Promo message sent to all other users</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ Cannot send the promo message. Try replying to a message\nOr some error occurred</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ User did not download any content yet...</b> Not exist in logs"
    ADMIN_INVALID_COMMAND_MSG = "❌ Invalid command"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ No data found in cache for <code>{{path}}</code>"
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ Usage: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 Admin cannot delete an admin"
    ADMIN_USER_BLOCKED_MSG = "User blocked 🔒❌\n \nID: <code>{user_id}</code>\nBlocked Date: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> is already blocked ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 Sorry! You are not an admin"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ Usage: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "User unblocked 🔓✅\n \nID: <code>{user_id}</code>\nUnblocked Date: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> is already unblocked ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>Bot running time -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ Please provide a URL to clear cache for.\nUsage: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ Please provide a valid URL.\nUsage: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ Cache cleared successfully for URL:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ No cache found for this link."
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ Error clearing cache: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ Running porn list update script: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ Script completed successfully!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ Script completed successfully!\n\nOutput:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ Script failed with return code {returncode}:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ Error running script: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ Reloading porn and domain-related caches..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ Porn caches reloaded successfully!\n\n"
        "📊 Current cache status:\n"
        "• Porn domains: {porn_domains}\n"
        "• Porn keywords: {porn_keywords}\n"
        "• Supported sites: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ Error reloading porn cache: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ Please provide a URL to check.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ Please provide a valid URL.\nUsage: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 Checking URL for NSFW content...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>Porn Check Result</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>Status:</b> <b>{status_text}</b>\n\n"
        "<b>Explanation:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ Error checking URL: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "Cookies cleaned."
    CLEAN_LOGS_CLEANED_MSG = "Логи cleaned."
    CLEAN_TAGS_CLEANED_MSG = "tags cleaned."
    CLEAN_FORMAT_CLEANED_MSG = "Формат cleaned."
    CLEAN_SPLIT_CLEANED_MSG = "split cleaned."
    CLEAN_MEDIAINFO_CLEANED_MSG = "mediainfo cleaned."
    CLEAN_SUBS_CLEANED_MSG = "Subtitle Настройки cleaned."
    CLEAN_KEYBOARD_CLEANED_MSG = "Keyboard Настройки cleaned."
    CLEAN_ARGS_CLEANED_MSG = "Args Настройки cleaned."
    CLEAN_NSFW_CLEANED_MSG = "NSFW Настройки cleaned."
    CLEAN_PROXY_CLEANED_MSG = "Proxy Настройки cleaned."
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "Flood wait Настройки cleaned."
    CLEAN_ALL_CLEANED_MSG = "Все files cleaned."
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 COOKIES</b>\n\nChoose an action:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ Cookie Файл saved"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ Skipped validation for non-YouTube cookies"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ Cookie Файл exists but has Неправильно Формат"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ Cookie Файл is not found."
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starting YouTube cookies Тест...\n\nPlease wait Пока I Проверить and Проверить your cookies."
    COOKIES_YOUTUBE_WORKING_MSG = "✅ Your existing YouTube cookies are working properly!\n\nNo Нужно К Скачать Новый ones."
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ Your existing YouTube cookies are Истекший or Недействительно.\n\n🔄 Загрузка Новый cookies..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} cookie source is not configured!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} cookie source must be a .txt file!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded: {range_count} files requested (maximum {max_img_files}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚Близко"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ Media limit exceeded: {count} files requested (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "Браузер impersonation"
    ARGS_REFERER_DESC_MSG = "Заголовок Реферер"
    ARGS_USER_AGENT_DESC_MSG = "Пользователь-Agent header"
    ARGS_GEO_BYPASS_DESC_MSG = "Bypass geographic restrictions"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "Проверить SSL certificate"
    ARGS_LIVE_FROM_START_DESC_MSG = "Скачать live streams От Запустить"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "Do not Скачать live streams От Запустить"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "Use MPEG-TS container for HLS videos"
    ARGS_NO_PLAYLIST_DESC_MSG = "Скачать Только single Видео, not playlist"
    ARGS_NO_PART_DESC_MSG = "Do not use .Часть files"
    ARGS_NO_CONTINUE_DESC_MSG = "Do not Возобновить Частично downloads"
    ARGS_AUDIO_FORMAT_DESC_MSG = "Аудио Формат for extraction"
    ARGS_EMBED_METADATA_DESC_MSG = "Embed metadata В Видео Файл"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "Embed thumbnail В Видео Файл"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "Write thumbnail К Файл"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "Число of concurrent fragments К Скачать"
    ARGS_FORCE_IPV4_DESC_MSG = "Сила IPv4 connections"
    ARGS_FORCE_IPV6_DESC_MSG = "Сила IPv6 connections"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For header Стратегия"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP chunk Размер (bytes)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "Sleep До subtitle Скачать (seconds)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "Разрешить legacy Сервер connections"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "Suppress HTTPS certificate validation"
    ARGS_USERNAME_DESC_MSG = "Имя Пользователя Аккаунта"
    ARGS_PASSWORD_DESC_MSG = "Пароль Аккаунта"
    ARGS_TWOFACTOR_DESC_MSG = "Два-Фактор authentication code"
    ARGS_IGNORE_ERRORS_DESC_MSG = "Ignore Скачать errors and Продолжить"
    ARGS_MIN_FILESIZE_DESC_MSG = "Минимум Файл Размер (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "Максимум Файл Размер (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "Playlist items К Скачать (e.g., 1,3,5 or 1-5)"
    ARGS_DATE_DESC_MSG = "Скачать videos uploaded На this Дата (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "Скачать videos uploaded До this Дата (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "Скачать videos uploaded После this Дата (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "Пользовательский HTTP headers (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "Sleep Интервал Между requests (seconds)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "Максимум sleep Интервал (seconds)"
    ARGS_RETRIES_DESC_MSG = "Число of retries"
    ARGS_VIDEO_FORMAT_DESC_MSG = "Видео container Формат"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "Output container Формат for merging"
    ARGS_SEND_AS_FILE_DESC_MSG = "Отправить Все Медиа as document instead of Медиа"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "Имперсонация"
    ARGS_REFERER_SHORT_MSG = "Реферер"
    ARGS_GEO_BYPASS_SHORT_MSG = "Гео Обход"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "Проверить Cert"
    ARGS_LIVE_FROM_START_SHORT_MSG = "Live Запустить"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "Нет Live Запустить"
    ARGS_USER_AGENT_SHORT_MSG = "Пользователь Agent"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "Нет Playlist"
    ARGS_NO_PART_SHORT_MSG = "Нет Часть"
    ARGS_NO_CONTINUE_SHORT_MSG = "Нет Продолжить"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "Аудио Формат"
    ARGS_EMBED_METADATA_SHORT_MSG = "Встроить Мета"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "Встроить Миниатюру"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "Записать Миниатюру"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "Параллельно"
    ARGS_FORCE_IPV4_SHORT_MSG = "Сила IPv4"
    ARGS_FORCE_IPV6_SHORT_MSG = "Сила IPv6"
    ARGS_XFF_SHORT_MSG = "XFF Header"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "Chunk Размер"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "Ожидание Субтитров"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "Устаревшее Подключение"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "Нет Проверить Cert"
    ARGS_USERNAME_SHORT_MSG = "Имя Пользователя"
    ARGS_PASSWORD_SHORT_MSG = "Пароль"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "Игнорировать Ошибки"
    ARGS_MIN_FILESIZE_SHORT_MSG = "Min Размер"
    ARGS_MAX_FILESIZE_SHORT_MSG = "Max Размер"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "Элементы Плейлиста"
    ARGS_DATE_SHORT_MSG = "Дата"
    ARGS_DATEBEFORE_SHORT_MSG = "Дата До"
    ARGS_DATEAFTER_SHORT_MSG = "Дата После"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP Headers"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "Sleep Интервал"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "Макс Ожидание"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "Видео Формат"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "Merge Формат"
    ARGS_SEND_AS_FILE_SHORT_MSG = "Отправить As Файл"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ The Файл is too large. Максимум Размер is 100 KB."
    COOKIES_INVALID_FORMAT_MSG = "❌ Только files of the following Формат are allowed .txt."
    COOKIES_INVALID_COOKIE_MSG = "❌ The Файл does not look Нравится cookie.txt (there is Нет Линия '# Netscape HTTP Cookie Файл')."
    COOKIES_ERROR_READING_MSG = "❌ Error reading file: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ Cookie Файл exists and has Правильно Формат"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} cookie file is too large! Max 100KB, got {size}KB."
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} cookie file downloaded and saved as cookie.txt in your folder.</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} cookie source is unavailable (status {status}). Please try again later."
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ Error downloading {service} cookie file. Please try again later."
    COOKIES_USER_PROVIDED_MSG = "<b>✅ User provided a new cookie file.</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ Cookie successfully updated:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ Not a valid cookie.</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube cookie sources are not configured!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ Access denied. Admin only."
    ADMIN_USER_LOGS_TOTAL_MSG = "Total: <b>{total}</b>\n<b>{user_id}</b> - logs (Last 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 keyboard activated!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ Subtitle language set to: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ Subtitle language set to: {flag} {name} with AUTO/TRANS enabled."
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "Subtitle language Меню Закрыт."
    SUBS_DOWNLOADING_MSG = "💬 Загрузка subtitles..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Reloading Firebase cache into memory..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ No COOKIE_URL configured. Use /cookie or upload cookie.txt."
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 Загрузка cookies От Удаленный URL..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ Fallback COOKIE_URL must point to a .txt file."
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ Fallback cookie Файл is too large (>100KB)."
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube cookie Файл downloaded via fallback and saved as cookie.txt"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ Fallback cookie source unavailable (status {status}). Try /cookie or upload cookie.txt."
    COOKIE_FALLBACK_ERROR_MSG = "❌ Ошибка Загрузка fallback cookie. Try /cookie or Загрузить cookie.txt."
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ Unexpected Ошибка Во время fallback cookie Скачать."
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} browser not installed."
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ Cookies saved using browser: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ Failed to save cookies: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube cookies are working properly"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube cookies are Истекший or Недействительно\n\nUse /cookie К get Новый cookies"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format\n• <code>/format 720</code> - 720p quality\n• <code>/format 4k</code> - 4K quality"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "Подсказка sent."
    FORMAT_MKV_TOGGLE_MSG = "MKV is now {status}"
    COOKIES_NO_REMOTE_URL_MSG = "❌ Нет Удаленный URL configured"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ Недействительно Файл Формат"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ Файл too large"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ Cookies downloaded successfully"
    COOKIES_SERVER_ERROR_MSG = "❌ Server error {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ Скачать Не удалось"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ Unexpected Ошибка"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ Браузер not installed."
    COOKIES_MENU_CLOSED_MSG = "Меню Закрыт."
    COOKIES_HINT_CLOSED_MSG = "Cookie Подсказка Закрыт."
    IMG_HELP_CLOSED_MSG = "Помощь Закрыт."
    SUBS_LANGUAGE_UPDATED_MSG = "Subtitle language Настройки updated."
    SUBS_MENU_CLOSED_MSG = "Subtitle language Меню Закрыт."
    KEYBOARD_SET_TO_MSG = "Keyboard set to {setting}"
    KEYBOARD_ERROR_PROCESSING_MSG = "Ошибка Обработка setting"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo Включен."
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo Отключен."
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW blur Отключен."
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW blur Включен."
    SETTINGS_MENU_CLOSED_MSG = "Меню Закрыт."
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "Flood wait Активен. Try Позже."
    OTHER_HELP_CLOSED_MSG = "Помощь Закрыт."
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "Логи Сообщение Закрыт."
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "Меню Закрыт."
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "Недействительно Размер."
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ Error sending MediaInfo: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ An error occurred: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - all logs"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - all {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 Скачать От Удаленный URL"
    BROWSER_OPEN_BUTTON_MSG = "🌐 Открыть Браузер"
    SELECT_BROWSER_MSG = "Выбрать a Браузер К Скачать cookies От:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "Нет browsers found На this Система. You can Скачать cookies От Удаленный URL or monitor Браузер Статус:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>Open Browser</b> - to monitor browser status in mini-app"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 Starting YouTube cookies Тест...\n\nPlease wait Пока I Проверить and Проверить your cookies."
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ Не удалось К Запустить /check_cookie"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ Flood Лимит. Try Позже."
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ Не удалось К Открыть Браузер cookie Меню"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "Сохранить as cookie Подсказка Закрыт."
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>Usage:</b>\n<code>/link [quality] URL</code>\n\n<b>Examples:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - best quality\n• /link 720 https://youtube.com/watch?v=... - 720p or lower\n• /link 720p https://youtube.com/watch?v=... - same as above\n• /link 4k https://youtube.com/watch?v=... - 4K or lower\n• /link 8k https://youtube.com/watch?v=... - 8K or lower</blockquote>\n\n<b>Quality:</b> from 1 to 10000 (e.g., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K quality"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ Не удалось К get stream links"
    LINK_ERROR_GETTING_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ Invalid YouTube cookie index: {selected_index}. Available range is 1-{total_urls}"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 Downloading and checking YouTube cookies...\n\nAttempt {attempt} of {total}\n🔍 Testing cookies..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube cookies successfully downloaded and validated!\n\nUsed source {source} of {total}"
    COOKIES_ALL_EXPIRED_MSG = "❌ Все YouTube cookies are Истекший or Недоступно!\n\nContact the bot administrator К replace them."
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **Недействительно argument!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ Subtitle language set: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "Example: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} Selected language: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ Always Ask mode {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 Subtitles are Отключен"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 Subtitle settings</b>\n\n{status_text}\n\nSelect subtitle language:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - disable subtitles\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 Subtitle settings</b>\n\n{status_text}\n\nSelect subtitle language:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>Title:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p max quality\n- 1.5 hour max duration\n- 500mb max video size</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️WARNING: due to high CPU impact this function is very slow (near real-time) and limited to:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>Quick commands:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - disable subtitles\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - enable Always Ask mode\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - set language\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - set language with AUTO/TRANS enabled\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - enable Always Ask mode\n"
    SUBS_AUTO_SUBS_TEXT = " (auto-subs)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs mode {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "SUBS disabled via command: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "SUBS Always Ask enabled via command: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "SUBS language set via command: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "SUBS language + auto mode set via command: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "Пользователь opened /subs Меню."
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "User set subtitle language to: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "User toggled AUTO/TRANS mode to: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "User toggled Always Ask mode to: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "Пользователь requested cookies От Браузер."
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "Браузер selection keyboard sent with installed browsers Только."
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "Браузер selection Закрыт."
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "Fallback COOKIE_URL used successfully (source hidden)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "Fallback COOKIE_URL failed: status={status} (hidden)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "Fallback COOKIE_URL unexpected error: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "Browser {browser} not installed."
    COOKIES_SAVED_BROWSER_LOG_MSG = "Cookies saved using browser: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "Cookie file saved for user {user_id}."
    COOKIES_FILE_WORKING_LOG_MSG = "Cookie Файл exists, has Правильно Формат, and YouTube cookies are working."
    COOKIES_FILE_EXPIRED_LOG_MSG = "Cookie Файл exists and has Правильно Формат, but YouTube cookies are Истекший."
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "Cookie Файл exists and has Правильно Формат."
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "Cookie Файл exists but has Неправильно Формат."
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "Cookie Файл not found."
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "{service} cookie URL is empty for user {user_id}."
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} cookie URL is not .txt (hidden)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} cookie file too large: {size} bytes (source hidden)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "{service} cookie file downloaded for user {user_id} (source hidden)."
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Script not found: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "Failed to send initial status message"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "Error running {script_path}: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "Firebase cache reloaded by auto task."
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "Firebase cache reloaded by admin."
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Error reloading Firebase cache: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "Broadcast initiated. Text:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "Broadcast message sent to all users."
    ADMIN_BROADCAST_FAILED_LOG_MSG = "Failed to broadcast message: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "Admin {user_id} cleared cache for URL: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "Admin {user_id} started porn list update script: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "Porn list update script completed successfully by admin {user_id}"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "Porn list update script failed by admin {user_id}: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "Admin {user_id} tried to run non-existent script: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "Error running porn update script by admin {user_id}: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "Admin {user_id} started porn cache reload"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "Error reloading porn cache by admin {user_id}: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "Admin {user_id} checked URL for NSFW: {url} - Result: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "Пользователь requested Формат change."
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "Format set to ALWAYS_ASK."
    FORMAT_UPDATED_BEST_LOG_MSG = "Format updated to best: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "Format updated to ID {format_id}: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "Format updated to ID {format_id} (audio-only): {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "Format updated to quality {quality}: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "Format updated to: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "Формат Меню sent."
    FORMAT_SELECTION_CLOSED_LOG_MSG = "Формат selection Закрыт."
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "Пользовательский Формат Подсказка sent."
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "Формат resolution Меню sent."
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "Returned К main Формат Меню."
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "Format updated to: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "Format set to ALWAYS_ASK."
    FORMAT_CODEC_SET_LOG_MSG = "Codec preference set to {codec}"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "Пользовательский Формат Меню Закрыт"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "Direct link extracted for user {user_id} from {url}"
    LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link for user {user_id} from {url}: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "Error in link command for user {user_id}: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "User {user_id} set keyboard to {setting}"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "User {user_id} set keyboard to {setting}"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo set via command: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "Пользователь opened /mediainfo Меню."
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: Закрыт."
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo Включен."
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo Отключен."
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "Split size set to {size} bytes via argument."
    SPLIT_MENU_OPENED_LOG_MSG = "Пользователь opened /split Меню."
    SPLIT_SELECTION_CLOSED_LOG_MSG = "Split selection Закрыт."
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split size set to {size} bytes."
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "Proxy set via command: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "Пользователь opened /proxy Меню."
    PROXY_MENU_CLOSED_LOG_MSG = "Proxy: Закрыт."
    PROXY_ENABLED_LOG_MSG = "Proxy Включен."
    PROXY_DISABLED_LOG_MSG = "Proxy Отключен."
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "Помощь Сообщение Закрыт."
    AUDIO_HELP_SHOWN_LOG_MSG = "Showed /Аудио Помощь"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "Пользователь requested playlist Помощь."
    PLAYLIST_HELP_CLOSED_LOG_MSG = "Playlist Помощь Закрыт."
    AUDIO_HINT_CLOSED_LOG_MSG = "Аудио Подсказка Закрыт."
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "Direct link menu created via LINK button for user {user_id} from {url}"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "Failed to extract direct link via LINK button for user {user_id} from {url}: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "LIST command executed for user {user_id}, url: {url}"
    QUICK_EMBED_LOG_MSG = "Quick Embed: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "Always Ask menu sent for {url}"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "Created cached qualities menu for user {user_id} after error: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "Always Ask menu error for {url}: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "Формат is fixed via /args Настройки"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "Аудио"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "Видео"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "Видео"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "Следующий ▶️"
    SUBTITLES_NEXT_BUTTON_MSG = "Следующий ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ Все Текст fields are Пусто"
    SENDER_VIDEO_DURATION_MSG = "Видео Продолжительность:"
    SENDER_UPLOADING_FILE_MSG = "📤 Uploading Файл..."
    DOWN_UP_VIDEO_INFO_MSG = "📋 Видео Информация"
    DOWN_UP_NUMBER_MSG = "Число"
    DOWN_UP_TITLE_MSG = "Название"
    DOWN_UP_ID_MSG = "ID"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ Downloaded Видео."
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 Обработка for Загрузить..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 Splitted part {part} file uploaded"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ Загрузить Полностью"
    DOWN_UP_FILES_UPLOADED_MSG = "files uploaded"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 Близко"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼CODEC"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 DUBS"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 SUBS"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 Браузер"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 Getting direct Ссылка..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 Getting Доступно formats..."
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 Starting gallery-dl…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>Duration:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>Browser:</b> Open in web browser"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "Доступно formats for"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 How К use Формат IDs:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "После getting the Список, use specific Формат ID:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /Формат id 401 - Скачать Формат 401"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /Формат id401 - same as Выше"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /Формат id 140 Аудио - Скачать Формат 140 as MP3 Аудио"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 Аудио-Только formats detected"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "These formats will be downloaded as MP3 Аудио files."
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>How to set format:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - Download specific format ID"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - Download by quality"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - Download best quality"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - Always ask for quality"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>Audio-only formats:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - Download format 140 as MP3 audio"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "These will be downloaded as MP3 Аудио files."
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 Use Формат ID От the Список Выше"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ Ошибка: Original Сообщение not found."
    ALWAYS_ASK_FORMATS_PAGE_MSG = "Formats Страница"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ Ошибка showing formats Меню"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ Ошибка getting formats"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ Ошибка getting Доступно formats."
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "Пожалуйста, попробуйте снова Позже."
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp cannot process this content"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "The Система recommends using gallery-dl instead."
    ALWAYS_ASK_OPTIONS_MSG = "**Опции:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• For image galleries: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• For single images: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl often works Лучше for Instagram, Twitter, and other social Медиа Содержимое."
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Try Gallery-dl"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 Формат fixed via /args"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 Subtitles"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 Dubbed Аудио"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — Subtitles are Доступно"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — Выбрать subtitle language"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ Subs not found & won't embed"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — Instant repost От cache"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — Выбрать Аудио language"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW is paid (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — Выбрать Скачать Качество"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — Скачать Изображение (gallery-dl)"
    ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — Watch Видео В poketube"
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — Get direct Ссылка К Видео"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — Show Доступно formats Список"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — Сhange Видео ext/codec"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛Other"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝sub Только"
    ALWAYS_ASK_SMART_GROUPING_MSG = "Умная группировка"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "Added action Кнопка Строка (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "Added action Кнопка rows (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "Added bottom buttons К existing Строка"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "Created Новый bottom Строка"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "Нет videos found В playlist"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "Unsupported URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "Нет Видео could be found"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "Нет Видео found"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "Нет Медиа found"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "This tweet does not contain"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>Error retrieving video information:</b>"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "Try the <code>/clean</code> command and try again. If the error persists, YouTube requires authorization. Update cookies.txt via <code>/cookie</code> or <code>/cookies_from_browser</code> and try again."
    ALWAYS_ASK_MENU_CLOSED_MSG = "Меню Закрыт."
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 Руководство Качество Selection"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "Выбрать Качество manually С тех пор Автоматический detection Не удалось:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 Все Доступно Formats"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 Доступно Qualities (От cache)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ Using cached qualities - Новый formats may not be Доступно"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 Загрузка Формат"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 Загрузка"
    ALWAYS_ASK_FORMATS_PAGE_FROM_CACHE_MSG = "Formats Страница"
    ALWAYS_ASK_FROM_CACHE_MSG = "(От cache)"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_DETAILED_MSG = "❌ Ошибка: Original Сообщение not found. It might have been deleted. Please Отправить the Ссылка again."
    ALWAYS_ASK_ERROR_ORIGINAL_URL_NOT_FOUND_MSG = "❌ Ошибка: Original URL not found. Please Отправить the Ссылка again."
    ALWAYS_ASK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>"
    ALWAYS_ASK_TITLE_MSG = "📹 <b>Title:</b>"
    ALWAYS_ASK_DURATION_SEC_MSG = "⏱ <b>Duration:</b>"
    ALWAYS_ASK_FORMAT_CODE_MSG = "🎛 <b>Format:</b>"
    ALWAYS_ASK_VIDEO_STREAM_MSG = "🎬 <b>Video stream:</b>"
    ALWAYS_ASK_AUDIO_STREAM_MSG = "🎵 <b>Audio stream:</b>"
    ALWAYS_ASK_FAILED_TO_GET_STREAM_LINKS_MSG = "❌ Не удалось К get stream links"
    DIRECT_LINK_EXTRACTED_ALWAYS_ASK_LOG_MSG = "Direct link extracted via Always Ask menu for user {user_id} from {url}"
    DIRECT_LINK_FAILED_ALWAYS_ASK_LOG_MSG = "Failed to extract direct link via Always Ask menu for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_UP_LOG_MSG = "Direct link extracted via down_and_up_with_format for user {user_id} from {url}"
    DIRECT_LINK_FAILED_DOWN_UP_LOG_MSG = "Failed to extract direct link via down_and_up_with_format for user {user_id} from {url}: {error}"
    DIRECT_LINK_EXTRACTED_DOWN_AUDIO_LOG_MSG = "Direct link extracted via down_and_audio for user {user_id} from {url}"
    DIRECT_LINK_FAILED_DOWN_AUDIO_LOG_MSG = "Failed to extract direct link via down_and_audio for user {user_id} from {url}: {error}"
    
    # Audio processing messages
    AUDIO_SENT_FROM_CACHE_MSG = "✅ Аудио sent От cache."
    AUDIO_PROCESSING_MSG = "🎙️ Аудио is Обработка..."
    AUDIO_DOWNLOADING_PROGRESS_MSG = "{process}\n📥 Downloading audio:\n{bar}   {percent:.1f}%"
    AUDIO_DOWNLOAD_ERROR_MSG = "Ошибка occurred Во время Аудио Скачать."
    AUDIO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    AUDIO_EXTRACTION_FAILED_MSG = "❌ Не удалось К extract Аудио Информация"
    AUDIO_UNSUPPORTED_FILE_TYPE_MSG = "Skipping unsupported file type in playlist at index {index}"
    AUDIO_FILE_NOT_FOUND_MSG = "Аудио Файл not found После Скачать."
    AUDIO_UPLOADING_MSG = "{process}\n📤 Uploading audio file...\n{bar}   100.0%"
    AUDIO_SEND_FAILED_MSG = "❌ Failed to send audio: {error}"
    PLAYLIST_AUDIO_SENT_LOG_MSG = "Playlist audio sent: {sent}/{total} files (quality={quality}) to user{user_id}"
    AUDIO_DOWNLOAD_FAILED_MSG = "❌ Failed to download audio: {error}"
    DOWNLOAD_TIMEOUT_MSG = "⏰ Скачать cancelled Срок К Таймаут (2 hours)"
    VIDEO_DOWNLOAD_COMPLETE_MSG = "{process}\n{bar}   100.0%"
    
    # FFmpeg messages
    VIDEO_FILE_NOT_FOUND_MSG = "❌ Video file not found: {filename}"
    VIDEO_PROCESSING_ERROR_MSG = "❌ Error processing video: {error}"
    
    # Sender messages
    ERROR_SENDING_DESCRIPTION_FILE_MSG = "❌ Error sending description file: {error}"
    CHANGE_CAPTION_HINT_MSG = "<blockquote>📝 if you want to change video caption - reply to video with new text</blockquote>"
    
    # Always Ask Menu Messages
    NO_SUBTITLES_DETECTED_MSG = "Нет subtitles detected"
    CHOOSE_SUBTITLE_LANGUAGE_MSG = "Выбрать subtitle language"
    NO_ALTERNATIVE_AUDIO_LANGUAGES_MSG = "Нет Альтернатива Аудио languages"
    CHOOSE_AUDIO_LANGUAGE_MSG = "Выбрать Аудио language"
    PAGE_NUMBER_MSG = "Page {page}"
    SUBTITLE_MENU_CLOSED_MSG = "Subtitle Меню Закрыт."
    SUBTITLE_LANGUAGE_SET_MSG = "Subtitle language set: {value}"
    AUDIO_SET_MSG = "Audio set: {value}"
    FILTERS_UPDATED_MSG = "Фильтры обновлены"
    
    # Always Ask Menu Buttons
    BACK_BUTTON_TEXT = "🔙Back"
    CLOSE_BUTTON_TEXT = "🔚Close"
    LIST_BUTTON_TEXT = "📃List"
    IMAGE_BUTTON_TEXT = "🖼Image"
    
    # Always Ask Menu Notes
    QUALITIES_NOT_AUTO_DETECTED_NOTE = "<blockquote>⚠️ Qualities not auto-detected\nUse 'Other' button to see all available formats.</blockquote>"
    
    # Live Stream Messages
    LIVE_STREAM_DETECTED_MSG = "🚫 **Live Stream Detected**\n\nDownloading of ongoing or infinite live streams is not allowed.\n\nPlease wait for the stream К Конец and try Загрузка again when:\n• The stream Продолжительность is known\n• The stream has finished\n"
    AV1_NOT_AVAILABLE_FORMAT_SELECT_MSG = "Please select a different format using `/format` command."
    
    # Direct Link Messages
    DIRECT_LINK_OBTAINED_MSG = "🔗 <b>Direct link obtained</b>\n\n"
    TITLE_FIELD_MSG = "📹 <b>Title:</b> {title}\n"
    DURATION_FIELD_MSG = "⏱ <b>Duration:</b> {duration} sec\n"
    FORMAT_FIELD_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    VIDEO_STREAM_FIELD_MSG = "🎬 <b>Video stream:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    AUDIO_STREAM_FIELD_MSG = "🎵 <b>Audio stream:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    
    # Processing Error Messages
    FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Файл Обработка Ошибка**\n\nThe Видео was downloaded but couldn't be processed Срок К Недействительно characters В the filename.\n\n"
    FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Файл Обработка Ошибка**\n\nThe Видео was downloaded but couldn't be processed Срок К an Недействительно argument Ошибка.\n\n"
    FORMAT_NOT_AVAILABLE_MSG = "❌ **Формат Not Доступно**\n\nThe requested Видео Формат is not Доступно for this Видео.\n\n"
    FORMAT_ID_NOT_FOUND_MSG = "❌ Format ID {format_id} not found for this video.\n\nAvailable format IDs: {available_ids}\n"
    AV1_FORMAT_NOT_AVAILABLE_MSG = "❌ **AV1 format is not available for this video.**\n\n**Available formats:**\n{formats_text}\n\n"
    
    # Additional Error Messages  
    AUDIO_FILE_PROCESSING_ERROR_INVALID_CHARS_MSG = "❌ **Файл Обработка Ошибка**\n\nThe Аудио was downloaded but couldn't be processed Срок К Недействительно characters В the filename.\n\n"
    AUDIO_FILE_PROCESSING_ERROR_INVALID_ARG_MSG = "❌ **Файл Обработка Ошибка**\n\nThe Аудио was downloaded but couldn't be processed Срок К an Недействительно argument Ошибка.\n\n"
    
    # Keyboard Buttons
    CLEAN_EMOJI = "🧹"
    COOKIE_EMOJI = "🍪" 
    SETTINGS_EMOJI = "⚙️"
    PROXY_EMOJI = "🌐"
    IMAGE_EMOJI = "🖼"
    SEARCH_EMOJI = "🔍"
    VIDEO_EMOJI = "📼"
    USAGE_EMOJI = "📊"
    SPLIT_EMOJI = "✂️"
    AUDIO_EMOJI = "🎧"
    SUBTITLE_EMOJI = "💬"
    LANGUAGE_EMOJI = "🌎"
    TAG_EMOJI = "#️⃣"
    HELP_EMOJI = "🆘"
    LIST_EMOJI = "📃"
    PLAY_EMOJI = "⏯️"
    KEYBOARD_EMOJI = "🎹"
    LINK_EMOJI = "🔗"
    ARGS_EMOJI = "🧰"
    NSFW_EMOJI = "🔞"
    LIST_EMOJI = "📃"
    
    # NSFW Content Messages
    PORN_CONTENT_CANNOT_DOWNLOAD_MSG = "Пользователь entered a porn Содержимое. Cannot be downloaded."
    
    # Additional Log Messages
    NSFW_BLUR_SET_COMMAND_LOG_MSG = "NSFW blur set via command: {arg}"
    NSFW_MENU_OPENED_LOG_MSG = "Пользователь opened /nsfw Меню."
    NSFW_MENU_CLOSED_LOG_MSG = "NSFW: Закрыт."
    COOKIES_DOWNLOAD_FAILED_LOG_MSG = "Failed to download {service} cookie: status={status} (url hidden)"
    COOKIES_DOWNLOAD_ERROR_LOG_MSG = "Error downloading {service} cookie: {error} (url hidden)"
    COOKIES_DOWNLOAD_UNEXPECTED_ERROR_LOG_MSG = "Unexpected error while downloading {service} cookie (url hidden): {error_type}: {error}"
    COOKIES_FILE_UPDATED_LOG_MSG = "Cookie file updated for user {user_id}."
    COOKIES_INVALID_CONTENT_LOG_MSG = "Invalid cookie content provided by user {user_id}."
    COOKIES_YOUTUBE_URLS_EMPTY_LOG_MSG = "YouTube cookie URLs are empty for user {user_id}."
    COOKIES_YOUTUBE_DOWNLOADED_VALIDATED_LOG_MSG = "YouTube cookies downloaded and validated for user {user_id} from source {source}."
    COOKIES_YOUTUBE_ALL_FAILED_LOG_MSG = "All YouTube cookie sources failed for user {user_id}."
    ADMIN_CHECK_PORN_ERROR_LOG_MSG = "Error in check_porn command by admin {admin_id}: {error}"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "Split part size set to {size} bytes."
    VIDEO_UPLOAD_COMPLETED_SPLITTING_LOG_MSG = "Видео Загрузить completed with Файл splitting."
    PLAYLIST_VIDEOS_SENT_LOG_MSG = "Playlist videos sent: {sent}/{total} files (quality={quality}) to user {user_id}"
    UNKNOWN_ERROR_MSG = "❌ Unknown error: {error}"
    SKIPPING_UNSUPPORTED_FILE_TYPE_MSG = "Skipping unsupported file type in playlist at index {index}"
    FFMPEG_NOT_FOUND_MSG = "❌ FFmpeg not found. Please Установить FFmpeg."
    CONVERSION_TO_MP4_FAILED_MSG = "❌ Conversion to MP4 failed: {error}"
    EMBEDDING_SUBTITLES_WARNING_MSG = "⚠️ Embedding subtitles may take a long Время (up К 1 min per 1 min of Видео)!\n🔥 Starting К burn subtitles..."
    SUBTITLES_CANNOT_EMBED_LIMITS_MSG = "ℹ️ Subtitles cannot be embedded Срок К limits (Качество/Продолжительность/Размер)"
    SUBTITLES_NOT_AVAILABLE_LANGUAGE_MSG = "ℹ️ Subtitles are not Доступно for the selected language"
    ERROR_SENDING_VIDEO_MSG = "❌ Error sending video: {error}"
    PLAYLIST_VIDEOS_SENT_MSG = "✅ Playlist videos sent: {sent}/{total} files."
    DOWNLOAD_CANCELLED_TIMEOUT_MSG = "⏰ Скачать cancelled Срок К Таймаут (2 hours)"
    FAILED_DOWNLOAD_VIDEO_MSG = "❌ Failed to download video: {error}"
    ERROR_SUBTITLES_NOT_FOUND_MSG = "❌ Error: {error}"
    
    # Args command error messages
    ARGS_JSON_MUST_BE_OBJECT_MSG = "❌ JSON must be an Объект (Словарь)."
    ARGS_INVALID_JSON_FORMAT_MSG = "❌ Недействительно JSON Формат. Please provide Действительно JSON."
    ARGS_VALUE_MUST_BE_BETWEEN_MSG = "❌ Value must be between {min_val} and {max_val}."
    ARGS_PARAM_SET_TO_MSG = "✅ {description} set to: <code>{value}</code>"
    
    # Args command button texts
    ARGS_TRUE_BUTTON_MSG = "✅ Истина"
    ARGS_FALSE_BUTTON_MSG = "❌ Ложь"
    ARGS_BACK_BUTTON_MSG = "🔙 Назад"
    
    # Args command status texts
    ARGS_STATUS_TRUE_MSG = "✅"
    ARGS_STATUS_FALSE_MSG = "❌"
    ARGS_STATUS_TRUE_DISPLAY_MSG = "✅ Истина"
    ARGS_STATUS_FALSE_DISPLAY_MSG = "❌ Ложь"
    
    # Args command status indicators
    ARGS_STATUS_SELECTED_MSG = "✅"
    ARGS_STATUS_UNSELECTED_MSG = "⚪"
    
    # Down and Up error messages
    DOWN_UP_AV1_NOT_AVAILABLE_MSG = "❌ AV1 format is not available for this video.\n\nAvailable formats:\n{formats_text}"
    DOWN_UP_ERROR_DOWNLOADING_MSG = "❌ Error downloading: {error_message}"
    DOWN_UP_NO_VIDEOS_PLAYLIST_MSG = "❌ No videos found in playlist at index {index}."
    DOWN_UP_VIDEO_CONVERSION_FAILED_INVALID_MSG = "❌ **Видео Conversion Не удалось**\n\nThe Видео couldn't be converted К MP4 Срок К an Недействительно argument Ошибка.\n\n"
    DOWN_UP_VIDEO_CONVERSION_FAILED_MSG = "❌ **Видео Conversion Не удалось**\n\nThe Видео couldn't be converted К MP4.\n\n"
    DOWN_UP_FAILED_STREAM_LINKS_MSG = "❌ Не удалось К get stream links"
    DOWN_UP_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    DOWN_UP_NO_CONTENT_FOUND_MSG = "❌ No content found at index {index}"

    # Always Ask Menu error messages
    AA_ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ Ошибка: Original Сообщение not found."
    AA_ERROR_URL_NOT_FOUND_MSG = "❌ Ошибка: URL not found."
    AA_ERROR_URL_NOT_EMBEDDABLE_MSG = "❌ This URL cannot be embedded."
    AA_ERROR_CODEC_NOT_AVAILABLE_MSG = "❌ {codec} codec not available for this video"
    AA_ERROR_FORMAT_NOT_AVAILABLE_MSG = "❌ {format} format not available for this video"
    
    # Always Ask Menu button texts
    AA_AVC_BUTTON_MSG = "✅ AVC"
    AA_AVC_BUTTON_INACTIVE_MSG = "☑️ AVC"
    AA_AVC_BUTTON_UNAVAILABLE_MSG = "❌ AVC"
    AA_AV1_BUTTON_MSG = "✅ AV1"
    AA_AV1_BUTTON_INACTIVE_MSG = "☑️ AV1"
    AA_AV1_BUTTON_UNAVAILABLE_MSG = "❌ AV1"
    AA_VP9_BUTTON_MSG = "✅ VP9"
    AA_VP9_BUTTON_INACTIVE_MSG = "☑️ VP9"
    AA_VP9_BUTTON_UNAVAILABLE_MSG = "❌ VP9"
    AA_MP4_BUTTON_MSG = "✅ MP4"
    AA_MP4_BUTTON_INACTIVE_MSG = "☑️ MP4"
    AA_MP4_BUTTON_UNAVAILABLE_MSG = "❌ MP4"
    AA_MKV_BUTTON_MSG = "✅ MKV"
    AA_MKV_BUTTON_INACTIVE_MSG = "☑️ MKV"
    AA_MKV_BUTTON_UNAVAILABLE_MSG = "❌ MKV"

    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood Лимит. Try Позже."
    
    # Cookies command button texts
    COOKIES_BROWSER_BUTTON_MSG = "✅ {browser_name}"
    COOKIES_CHECK_COOKIE_BUTTON_MSG = "✅ Проверить Cookie"
    
    # Proxy command button texts
    PROXY_ON_BUTTON_MSG = "✅ На"
    PROXY_OFF_BUTTON_MSG = "❌ Выкл"
    PROXY_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # MediaInfo command button texts
    MEDIAINFO_ON_BUTTON_MSG = "✅ На"
    MEDIAINFO_OFF_BUTTON_MSG = "❌ Выкл"
    MEDIAINFO_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # Format command button texts
    FORMAT_AVC1_BUTTON_MSG = "✅ avc1 (H.264)"
    FORMAT_AVC1_BUTTON_INACTIVE_MSG = "☑️ avc1 (H.264)"
    FORMAT_AV01_BUTTON_MSG = "✅ av01 (AV1)"
    FORMAT_AV01_BUTTON_INACTIVE_MSG = "☑️ av01 (AV1)"
    FORMAT_VP9_BUTTON_MSG = "✅ vp09 (VP9)"
    FORMAT_VP9_BUTTON_INACTIVE_MSG = "☑️ vp09 (VP9)"
    FORMAT_MKV_ON_BUTTON_MSG = "✅ MKV: На"
    FORMAT_MKV_OFF_BUTTON_MSG = "☑️ MKV: Выкл"
    
    # Subtitles command button texts
    SUBS_LANGUAGE_CHECKMARK_MSG = "✅ "
    SUBS_AUTO_EMOJI_MSG = "✅"
    SUBS_AUTO_EMOJI_INACTIVE_MSG = "☑️"
    SUBS_ALWAYS_ASK_EMOJI_MSG = "✅"
    SUBS_ALWAYS_ASK_EMOJI_INACTIVE_MSG = "☑️"
    
    # NSFW command button texts
    NSFW_ON_NO_BLUR_MSG = "✅ На (Нет Blur)"
    NSFW_ON_NO_BLUR_INACTIVE_MSG = "☑️ На (Нет Blur)"
    NSFW_OFF_BLUR_MSG = "✅ Выкл (Blur)"
    NSFW_OFF_BLUR_INACTIVE_MSG = "☑️ Выкл (Blur)"
    
    # Admin command status texts
    ADMIN_STATUS_NSFW_MSG = "🔞"
    ADMIN_STATUS_CLEAN_MSG = "✅"
    ADMIN_STATUS_NSFW_TEXT_MSG = "NSFW"
    ADMIN_STATUS_CLEAN_TEXT_MSG = "Чистый"
    
    # Admin command additional messages
    ADMIN_ERROR_PROCESSING_REPLY_MSG = "Error processing reply message for user {user}: {error}"
    ADMIN_ERROR_SENDING_BROADCAST_MSG = "Error sending broadcast to user {user}: {error}"
    ADMIN_LOGS_FORMAT_MSG = "Logs of {bot_name}\nUser: {user_id}\nTotal logs: {total}\nCurrent time: {now}\n\n{logs}"
    ADMIN_BOT_DATA_FORMAT_MSG = "{bot_name} {path}\nTotal {path}: {count}\nCurrent time: {now}\n\n{data}"
    ADMIN_TOTAL_USERS_MSG = "<i>Total Users: {count}</i>\nLast 20 {path}:\n\n{display_list}"
    ADMIN_PORN_CACHE_RELOADED_MSG = "Porn caches reloaded by admin {admin_id}. Domains: {domains}, Keywords: {keywords}, Sites: {sites}, WHITELIST: {whitelist}, GREYLIST: {greylist}, BLACK_LIST: {black_list}, WHITE_KEYWORDS: {white_keywords}, PROXY_DOMAINS: {proxy_domains}, PROXY_2_DOMAINS: {proxy_2_domains}, CLEAN_QUERY: {clean_query}, NO_COOKIE_DOMAINS: {no_cookie_domains}"
    
    # Args command additional messages
    ARGS_ERROR_SENDING_TIMEOUT_MSG = "Ошибка отправки сообщения о таймауте: {error}"
    
    # Language selection messages
    LANG_SELECTION_MSG = "🌍 <b>Выберите язык</b>\n\n🇺🇸 English\n🇷🇺 Русский\n🇸🇦 العربية\n🇮🇳 हिन्दी"
    LANG_CHANGED_MSG = "✅ Язык изменён на {lang_name}"
    LANG_ERROR_MSG = "❌ Ошибка изменения языка"
    LANG_CLOSED_MSG = "Выбор языка закрыт"
    
    # Clean command additional messages
    
    # Cookies command additional messages
    COOKIES_BROWSER_CALLBACK_MSG = "[BROWSER] callback: {callback_data}"
    COOKIES_ADDING_BROWSER_MONITORING_MSG = "Adding browser monitoring button with URL: {miniapp_url}"
    COOKIES_BROWSER_MONITORING_URL_NOT_CONFIGURED_MSG = "Browser monitoring URL not configured: {miniapp_url}"
    
    # Format command additional messages
    
    # Keyboard command additional messages
    KEYBOARD_SETTING_UPDATED_MSG = "🎹 **Keyboard setting updated!**\n\nNew setting: **{setting}**"
    KEYBOARD_FAILED_HIDE_MSG = "Failed to hide keyboard: {error}"
    
    # Link command additional messages
    LINK_USING_WORKING_YOUTUBE_COOKIES_MSG = "Using working YouTube cookies for link extraction for user {user_id}"
    LINK_NO_WORKING_YOUTUBE_COOKIES_MSG = "No working YouTube cookies available for link extraction for user {user_id}"
    LINK_USING_EXISTING_YOUTUBE_COOKIES_MSG = "Using existing YouTube cookies for link extraction for user {user_id}"
    LINK_NO_YOUTUBE_COOKIES_FOUND_MSG = "No YouTube cookies found for link extraction for user {user_id}"
    LINK_COPIED_GLOBAL_COOKIE_FILE_MSG = "Copied global cookie file to user {user_id} folder for link extraction"
    
    # MediaInfo command additional messages
    MEDIAINFO_USER_REQUESTED_MSG = "[MEDIAINFO] User {user_id} requested mediainfo command"
    MEDIAINFO_USER_IS_ADMIN_MSG = "[MEDIAINFO] User {user_id} is admin: {is_admin}"
    MEDIAINFO_USER_IS_IN_CHANNEL_MSG = "[MEDIAINFO] User {user_id} is in channel: {is_in_channel}"
    MEDIAINFO_ACCESS_DENIED_MSG = "[MEDIAINFO] User {user_id} access denied - not admin and not in channel"
    MEDIAINFO_ACCESS_GRANTED_MSG = "[MEDIAINFO] User {user_id} access granted"
    MEDIAINFO_CALLBACK_MSG = "[MEDIAINFO] callback: {callback_data}"
    
    # URL Parser error messages
    URL_PARSER_ADMIN_ONLY_MSG = "❌ This command is only available for administrators."
    
    # Helper messages
    HELPER_DOWNLOAD_FINISHED_PO_MSG = "✅ Скачать finished with PO token support"
    HELPER_FLOOD_LIMIT_TRY_LATER_MSG = "⏳ Flood Лимит. Try Позже."
    
    # Database error messages
    DB_REST_TOKEN_REFRESH_ERROR_MSG = "❌ REST token refresh error: {error}"
    DB_ERROR_CLOSING_SESSION_MSG = "❌ Error closing Firebase session: {error}"
    DB_ERROR_INITIALIZING_BASE_MSG = "❌ Error initializing base db structure: {error}"

    DB_NOT_ALL_PARAMETERS_SET_MSG = "❌ Not all parameters are set in config.py (FIREBASE_CONF, FIREBASE_USER, FIREBASE_PASSWORD)"
    DB_DATABASE_URL_NOT_SET_MSG = "❌ FIREBASE_CONF.databaseURL is not set"
    DB_API_KEY_NOT_SET_MSG = "❌ FIREBASE_CONF.apiKey is not set for getting idToken"
    DB_ERROR_DOWNLOADING_DUMP_MSG = "❌ Error downloading Firebase dump: {error}"
    DB_FAILED_DOWNLOAD_DUMP_REST_MSG = "❌ Failed to download Firebase dump via REST"
    DB_ERROR_DOWNLOAD_RELOAD_CACHE_MSG = "❌ Error in _download_and_reload_cache: {error}"
    DB_ERROR_RUNNING_AUTO_RELOAD_MSG = "❌ Error running auto reload_cache (attempt {attempt}/{max_retries}): {error}"
    DB_ALL_RETRY_ATTEMPTS_FAILED_MSG = "❌ All retry attempts failed"
    DB_STARTING_FIREBASE_DUMP_MSG = "🔄 Starting Firebase dump download at {datetime}"
    DB_DEPENDENCY_NOT_AVAILABLE_MSG = "⚠️ Dependency not available: requests or Session"
    DB_DATABASE_EMPTY_MSG = "⚠️ Database is empty"
    
    # Magic.py error messages
    MAGIC_ERROR_CLOSING_LOGGER_MSG = "❌ Error closing logger: {error}"
    MAGIC_ERROR_DURING_CLEANUP_MSG = "❌ Error during cleanup: {error}"
    
    # Update from repo error messages
    UPDATE_CLONE_ERROR_MSG = "❌ Clone error: {error}"
    UPDATE_CLONE_TIMEOUT_MSG = "❌ Clone Таймаут"
    UPDATE_CLONE_EXCEPTION_MSG = "❌ Clone exception: {error}"
    UPDATE_CANCELED_BY_USER_MSG = "❌ Обновить canceled by Пользователь"

    # Update from repo success messages
    UPDATE_REPOSITORY_CLONED_SUCCESS_MSG = "✅ Repository cloned successfully"
    UPDATE_BACKUPS_MOVED_MSG = "✅ Backups moved К _backup/"
    
    # Magic.py success messages
    MAGIC_ALL_MODULES_LOADED_MSG = "✅ All modules are loaded"
    MAGIC_CLEANUP_COMPLETED_MSG = "✅ Cleanup completed on exit"
    MAGIC_SIGNAL_RECEIVED_MSG = "\n🛑 Received signal {signal}, shutting down gracefully..."
    
    # Removed duplicate logger messages - these are user messages, not logger messages
    
    # Download status messages
    DOWNLOAD_STATUS_PLEASE_WAIT_MSG = "Пожалуйста, подождите..."
    DOWNLOAD_STATUS_HOURGLASS_EMOJIS = ["⏳", "⌛"]
    DOWNLOAD_STATUS_DOWNLOADING_HLS_MSG = "📥 Загрузка HLS stream:"
    DOWNLOAD_STATUS_WAITING_FRAGMENTS_MSG = "Ожидание for fragments"
    
    # Restore from backup messages
    RESTORE_BACKUP_NOT_FOUND_MSG = "❌ Backup {ts} not found in _backup/"
    RESTORE_FAILED_RESTORE_MSG = "❌ Failed to restore {src} -> {dest_path}: {e}"
    RESTORE_SUCCESS_RESTORED_MSG = "✅ Restored: {dest_path}"
    
    # Image command messages
    IMG_INSTAGRAM_AUTH_ERROR_MSG = "❌ <b>{error_type}</b>\n\n<b>URL:</b> <code>{url}</code>\n\n<b>Details:</b> {error_details}\n\nDownload stopped due to critical error.\n\n💡 <b>Tip:</b> If you're getting 401 Unauthorized error, try using <code>/cookie instagram</code> command or send your own cookies to authenticate with Instagram."
    
    # Porn filter messages
    PORN_DOMAIN_BLACKLIST_MSG = "❌ Domain in porn blacklist: {domain_parts}"
    PORN_KEYWORDS_FOUND_MSG = "❌ Found porn keywords: {keywords}"
    PORN_DOMAIN_WHITELIST_MSG = "✅ Domain in whitelist: {domain}"
    PORN_WHITELIST_KEYWORDS_MSG = "✅ Found whitelist keywords: {keywords}"
    PORN_NO_KEYWORDS_FOUND_MSG = "✅ Нет porn keywords found"
    
    # Audio download messages
    AUDIO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error at index {index}, skipping to next audio..."
    
    # Video download messages  
    VIDEO_TIKTOK_API_ERROR_SKIP_MSG = "⚠️ TikTok API error at index {index}, skipping to next video..."
    
    # URL Parser messages
    URL_PARSER_USER_ENTERED_URL_LOG_MSG = "User entered a <b>url</b>\n <b>user's name:</b> {user_name}\nURL: {url}"
    URL_PARSER_USER_ENTERED_INVALID_MSG = "<b>User entered like this:</b> {input}\n{error_msg}"
    
    # Channel subscription messages
    CHANNEL_JOIN_BUTTON_MSG = "Присоединиться к Каналу"
    
    # Handler registry messages
    HANDLER_REGISTERING_MSG = "🔍 Registering handler: {handler_type} - {func_name}"
    
    # Clean command button messages
    CLEAN_COOKIE_DOWNLOAD_BUTTON_MSG = "📥 /cookie - Скачать my 5 cookies"
    CLEAN_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Get Браузер's YT-cookie"
    CLEAN_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Проверить your cookie Файл"
    CLEAN_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Загрузить Пользовательский cookie"
    
    # List command messages
    LIST_CLOSE_BUTTON_MSG = "🔚 Близко"
    LIST_AVAILABLE_FORMATS_HEADER_MSG = "Available formats for: {url}"
    LIST_FORMATS_FILE_NAME_MSG = "formats_{user_id}.txt"
    
    # Other handlers button messages
    OTHER_AUDIO_HINT_CLOSE_BUTTON_MSG = "🔚Близко"
    OTHER_PLAYLIST_HELP_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # Search command button messages
    SEARCH_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # Tag command button messages
    TAG_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # Magic.py callback messages
    MAGIC_HELP_CLOSED_MSG = "Помощь Закрыт."
    
    # URL extractor callback messages
    URL_EXTRACTOR_CLOSED_MSG = "Закрыт"
    URL_EXTRACTOR_ERROR_OCCURRED_MSG = "Ошибка occurred"
    
    # FFmpeg messages
    FFMPEG_NOT_FOUND_MSG = "ffmpeg not found В Путь or project Каталог. Please Установить FFmpeg."
    YTDLP_NOT_FOUND_MSG = "yt-dlp binary not found В Путь or project Каталог. Please Установить yt-dlp."
    FFMPEG_VIDEO_SPLIT_EXCESSIVE_MSG = "Video will be split into {rounds} parts, which may be excessive"
    FFMPEG_SPLITTING_VIDEO_PART_MSG = "Splitting video part {current}/{total}: {start_time:.2f}s to {end_time:.2f}s"
    FFMPEG_FAILED_CREATE_SPLIT_PART_MSG = "Failed to create split part {part}: {target_name}"
    FFMPEG_SUCCESSFULLY_CREATED_SPLIT_PART_MSG = "Successfully created split part {part}: {target_name} ({size} bytes)"
    FFMPEG_ERROR_SPLITTING_VIDEO_PART_MSG = "Error splitting video part {part}: {error}"
    FFMPEG_VIDEO_SPLIT_SUCCESS_MSG = "Video split into {count} parts successfully"
    FFMPEG_ERROR_VIDEO_SPLITTING_PROCESS_MSG = "Error in video splitting process: {error}"
    FFMPEG_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error while processing video {video_path}: {error}"
    FFMPEG_VIDEO_FILE_NOT_EXISTS_MSG = "Video file does not exist: {video_path}"
    FFMPEG_ERROR_PARSING_DIMENSIONS_MSG = "Error parsing dimensions '{size_result}': {error}"
    FFMPEG_COULD_NOT_DETERMINE_DIMENSIONS_MSG = "Could not determine video dimensions from '{size_result}', using default: {width}x{height}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_MSG = "Error creating thumbnail: {stderr}"
    FFMPEG_ERROR_PARSING_DURATION_MSG = "Error parsing video duration: {error}, result was: {result}"
    FFMPEG_THUMBNAIL_NOT_CREATED_MSG = "Thumbnail not created at {thumb_dir}, using default"
    FFMPEG_COMMAND_EXECUTION_ERROR_MSG = "Command execution error: {error}"
    FFMPEG_ERROR_CREATING_THUMBNAIL_WITH_FFMPEG_MSG = "Error creating thumbnail with FFmpeg: {error}"
    
    # Gallery-dl messages
    GALLERY_DL_SKIPPING_NON_DICT_CONFIG_MSG = "Skipping non-dict config section: {section}={opts}"
    GALLERY_DL_SETTING_CONFIG_MSG = "Setting {section}.{key} = {value}"
    GALLERY_DL_USING_USER_COOKIES_MSG = "[gallery-dl] Using user cookies: {cookie_path}"
    GALLERY_DL_USING_YOUTUBE_COOKIES_MSG = "Using YouTube cookies for user {user_id}"
    GALLERY_DL_COPIED_GLOBAL_COOKIE_MSG = "Copied global cookie file to user {user_id} folder"
    GALLERY_DL_USING_COPIED_GLOBAL_COOKIES_MSG = "[gallery-dl] Using copied global cookies as user cookies: {cookie_path}"
    GALLERY_DL_FAILED_COPY_GLOBAL_COOKIE_MSG = "Failed to copy global cookie file for user {user_id}: {error}"
    GALLERY_DL_USING_NO_COOKIES_MSG = "Using --no-cookies for domain: {url}"
    GALLERY_DL_PROXY_REQUESTED_FAILED_MSG = "Proxy requested but failed to import/get config: {error}"
    GALLERY_DL_FORCE_USING_PROXY_MSG = "Force using proxy for gallery-dl: {proxy_url}"
    GALLERY_DL_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy requested but proxy Конфигурация is Неполно"
    GALLERY_DL_PROXY_HELPER_FAILED_MSG = "Proxy helper failed: {error}"
    GALLERY_DL_PARSING_EXTRACTOR_ITEMS_MSG = "Parsing extractor items..."
    GALLERY_DL_ITEM_COUNT_MSG = "Item {count}: {item}"
    GALLERY_DL_FOUND_METADATA_TAG2_MSG = "Found metadata (tag 2): {info}"
    GALLERY_DL_FOUND_URL_TAG3_MSG = "Found URL (tag 3): {url}, metadata: {metadata}"
    GALLERY_DL_FOUND_METADATA_LEGACY_MSG = "Found metadata (legacy): {info}"
    GALLERY_DL_FOUND_URL_LEGACY_MSG = "Found URL (legacy): {url}"
    GALLERY_DL_FOUND_FILENAME_MSG = "Found filename: {filename}"
    GALLERY_DL_FOUND_DIRECTORY_MSG = "Found directory: {directory}"
    GALLERY_DL_FOUND_EXTENSION_MSG = "Found extension: {extension}"
    GALLERY_DL_PARSED_ITEMS_MSG = "Parsed {count} items, info: {info}, fallback: {fallback}"
    GALLERY_DL_SETTING_CONFIG_MSG2 = "Setting gallery-dl config: {config}"
    GALLERY_DL_TRYING_STRATEGY_A_MSG = "Trying Стратегия A: extractor.find + items()"
    GALLERY_DL_EXTRACTOR_MODULE_NOT_FOUND_MSG = "gallery_dl.extractor module not found"
    GALLERY_DL_EXTRACTOR_FIND_NOT_AVAILABLE_MSG = "gallery_dl.extractor.find() not Доступно В this Сборка"
    GALLERY_DL_CALLING_EXTRACTOR_FIND_MSG = "Calling extractor.find({url})"
    GALLERY_DL_NO_EXTRACTOR_MATCHED_MSG = "Нет extractor matched the URL"
    GALLERY_DL_SETTING_COOKIES_ON_EXTRACTOR_MSG = "Setting cookies on extractor: {cookie_path}"
    GALLERY_DL_FAILED_SET_COOKIES_ON_EXTRACTOR_MSG = "Failed to set cookies on extractor: {error}"
    GALLERY_DL_EXTRACTOR_FOUND_CALLING_ITEMS_MSG = "Extractor found, calling items()"
    GALLERY_DL_STRATEGY_A_SUCCEEDED_MSG = "Strategy A succeeded, got info: {info}"
    GALLERY_DL_STRATEGY_A_NO_VALID_INFO_MSG = "Стратегия A: extractor.items() returned Нет Действительно Информация"
    GALLERY_DL_STRATEGY_A_FAILED_MSG = "Strategy A (extractor.find) failed: {error}"
    GALLERY_DL_FALLBACK_METADATA_MSG = "Fallback metadata from --get-urls: total={total}"
    GALLERY_DL_ALL_STRATEGIES_FAILED_MSG = "Все strategies Не удалось К obtain metadata"
    GALLERY_DL_FAILED_EXTRACT_IMAGE_INFO_MSG = "Failed to extract image info: {error}"
    GALLERY_DL_JOB_MODULE_NOT_FOUND_MSG = "gallery_dl.job module not found (broken Установить?)"
    GALLERY_DL_DOWNLOAD_JOB_NOT_AVAILABLE_MSG = "gallery_dl.job.DownloadJob not Доступно В this Сборка"
    GALLERY_DL_SEARCHING_DOWNLOADED_FILES_MSG = "Searching for downloaded files В gallery-dl Каталог"
    GALLERY_DL_TRYING_FIND_FILES_BY_NAMES_MSG = "Trying К find files by names От extractor"
    
    # Sender messages
    SENDER_ERROR_READING_USER_ARGS_MSG = "Error reading user args for {user_id}: {error}"
    SENDER_FFPROBE_BYPASS_ERROR_MSG = "[FFPROBE BYPASS] Error while processing video{video_path}: {error}"
    SENDER_USER_SEND_AS_FILE_ENABLED_MSG = "User {user_id} has send_as_file enabled, sending as document"
    SENDER_SEND_VIDEO_TIMED_OUT_MSG = "send_video timed out repeatedly; falling Назад К send_document"
    SENDER_CAPTION_TOO_LONG_MSG = "Caption too long, trying with minimal caption"
    SENDER_SEND_VIDEO_MINIMAL_CAPTION_TIMED_OUT_MSG = "send_video (minimal caption) timed out; fallback К send_document"
    SENDER_ERROR_SENDING_VIDEO_MINIMAL_CAPTION_MSG = "Error sending video with minimal caption: {error}"
    SENDER_ERROR_SENDING_FULL_DESCRIPTION_FILE_MSG = "Error sending full description file: {error}"
    SENDER_ERROR_REMOVING_TEMP_DESCRIPTION_FILE_MSG = "Error removing temporary description file: {error}"
    
    # YT-DLP hook messages
    YTDLP_SKIPPING_MATCH_FILTER_MSG = "Skipping match_filter for domain in NO_FILTER_DOMAINS: {url}"
    YTDLP_CHECKING_EXISTING_YOUTUBE_COOKIES_MSG = "Checking existing YouTube cookies on user's URL for format detection for user {user_id}"
    YTDLP_EXISTING_YOUTUBE_COOKIES_WORK_MSG = "Existing YouTube cookies work on user's URL for format detection for user {user_id} - using them"
    YTDLP_EXISTING_YOUTUBE_COOKIES_FAILED_MSG = "Existing YouTube cookies failed on user's URL, trying to get new ones for format detection for user {user_id}"
    YTDLP_TRYING_YOUTUBE_COOKIE_SOURCE_MSG = "Trying YouTube cookie source {i} for format detection for user {user_id}"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_WORK_MSG = "YouTube cookies from source {i} work on user's URL for format detection for user {user_id} - saved to user folder"
    YTDLP_YOUTUBE_COOKIES_FROM_SOURCE_DONT_WORK_MSG = "YouTube cookies from source {i} don't work on user's URL for format detection for user {user_id}"
    YTDLP_FAILED_DOWNLOAD_YOUTUBE_COOKIES_MSG = "Failed to download YouTube cookies from source {i} for format detection for user {user_id}"
    YTDLP_ALL_YOUTUBE_COOKIE_SOURCES_FAILED_MSG = "All YouTube cookie sources failed for format detection for user {user_id}, will try without cookies"
    YTDLP_NO_YOUTUBE_COOKIE_SOURCES_CONFIGURED_MSG = "No YouTube cookie sources configured for format detection for user {user_id}, will try without cookies"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_MSG = "No YouTube cookies found for format detection for user {user_id}, attempting to get new ones"
    YTDLP_USING_YOUTUBE_COOKIES_ALREADY_VALIDATED_MSG = "Using YouTube cookies for format detection for user {user_id} (already validated in Always Ask menu)"
    YTDLP_NO_YOUTUBE_COOKIES_FOUND_ATTEMPTING_RESTORE_MSG = "No YouTube cookies found for format detection for user {user_id}, attempting to restore..."
    YTDLP_COPIED_GLOBAL_COOKIE_FILE_MSG = "Copied global cookie file to user {user_id} folder for format detection"
    YTDLP_FAILED_COPY_GLOBAL_COOKIE_FILE_MSG = "Failed to copy global cookie file for user {user_id}: {error}"
    YTDLP_USING_NO_COOKIES_FOR_DOMAIN_MSG = "Using --no-cookies for domain in get_video_formats: {url}"
    
    # App instance messages
    APP_INSTANCE_NOT_INITIALIZED_MSG = "App not initialized yet. Cannot access {name}"
    
    # Caption messages
    CAPTION_INFO_OF_VIDEO_MSG = "\n<b>Caption:</b> <code>{caption}</code>\n<b>User id:</b> <code>{user_id}</code>\n<b>User first name:</b> <code>{users_name}</code>\n<b>Video file id:</b> <code>{video_file_id}</code>"
    CAPTION_ERROR_IN_CAPTION_EDITOR_MSG = "Error in caption_editor: {error}"
    CAPTION_UNEXPECTED_ERROR_IN_CAPTION_EDITOR_MSG = "Unexpected error in caption_editor: {error}"
    CAPTION_VIDEO_URL_LINK_MSG = '<a href="{url}">🔗 Video URL</a>{bot_mention}'
    
    # Database messages
    DB_DATABASE_URL_MISSING_MSG = "FIREBASE_CONF.databaseURL отсутствует в Config"
    DB_FIREBASE_ADMIN_INITIALIZED_MSG = "✅ firebase_admin initialized"
    DB_REST_ID_TOKEN_REFRESHED_MSG = "🔁 REST idToken refreshed"
    DB_LOG_FOR_USER_ADDED_MSG = "Log for user added"
    DB_DATABASE_CREATED_MSG = "база данных создана"
    DB_BOT_STARTED_MSG = "Бот запущен"
    DB_RELOAD_CACHE_EVERY_PERSISTED_MSG = "RELOAD_CACHE_EVERY persisted to config.py: {hours}h"
    DB_PLAYLIST_PART_ALREADY_CACHED_MSG = "Playlist part already cached: {path_parts}, skipping"
    DB_GET_CACHED_PLAYLIST_VIDEOS_NO_CACHE_MSG = "get_cached_playlist_videos: no cache found for any URL/quality variant, returning empty dict"
    DB_GET_CACHED_PLAYLIST_COUNT_FAST_COUNT_MSG = "get_cached_playlist_count: fast count for large range: {cached_count} cached videos"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_MSG = "get_cached_message_ids: no cache found for hash {url_hash}, quality {quality_key}"
    DB_GET_CACHED_MESSAGE_IDS_NO_CACHE_ANY_VARIANT_MSG = "get_cached_message_ids: no cache found for any URL variant, returning None"
    
    # Database cache auto-reload messages
    DB_AUTO_CACHE_ACCESS_DENIED_MSG = "❌ Access denied. Admin only."
    DB_AUTO_CACHE_RELOADING_UPDATED_MSG = "🔄 Auto Firebase cache reloading updated!\n\n📊 Status: {status}\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_INVALID_ARGUMENT_MSG = "❌ Invalid argument. Use /auto_cache on | off | N (1..168)"
    DB_AUTO_CACHE_INTERVAL_RANGE_MSG = "❌ Interval must be between 1 and 168 hours"
    DB_AUTO_CACHE_FAILED_SET_INTERVAL_MSG = "❌ Failed to set interval"
    DB_AUTO_CACHE_INTERVAL_UPDATED_MSG = "⏱️ Auto Firebase cache interval updated!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STARTED_MSG = "🔄 Auto Firebase cache reloading started!\n\n📊 Status: ✅ ENABLED\n⏰ Schedule: every {interval} hours from 00:00\n🕒 Next reload: {next_exec} (in {delta_min} minutes)"
    DB_AUTO_CACHE_RELOADING_STOPPED_BY_ADMIN_MSG = "🛑 Auto Firebase cache reloading stopped!\n\n📊 Status: ❌ DISABLED\n💡 Use /auto_cache on to re-enable"
    DB_AUTO_CACHE_RELOAD_ENABLED_LOG_MSG = "Auto reload ENABLED; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_DISABLED_LOG_MSG = "Auto reload DISABLED by admin."
    DB_AUTO_CACHE_INTERVAL_SET_LOG_MSG = "Auto reload interval set to {interval}h; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_STARTED_LOG_MSG = "Auto reload started; next at {next_exec}"
    DB_AUTO_CACHE_RELOAD_STOPPED_LOG_MSG = "Auto reload stopped by admin."
    
    # Database cache messages (console output)
    DB_FIREBASE_CACHE_LOADED_MSG = "✅ Firebase cache loaded: {count} root nodes"
    DB_FIREBASE_CACHE_NOT_FOUND_MSG = "⚠️ Firebase cache file not found, starting with empty cache: {cache_file}"
    DB_FAILED_LOAD_FIREBASE_CACHE_MSG = "❌ Failed to load firebase cache: {error}"
    DB_FIREBASE_CACHE_RELOADED_MSG = "✅ Firebase cache reloaded: {count} root nodes"
    DB_FIREBASE_CACHE_FILE_NOT_FOUND_MSG = "⚠️ Firebase cache file not found: {cache_file}"
    DB_FAILED_RELOAD_FIREBASE_CACHE_MSG = "❌ Failed to reload firebase cache: {error}"
    
    # Database user ban messages
    DB_USER_BANNED_MSG = "🚫 You are banned from the bot!"
    
    # Always Ask Menu messages
    AA_NO_VIDEO_FORMATS_FOUND_MSG = "❔ Нет Видео formats found. Trying Изображение downloader…"
    AA_FLOOD_WAIT_MSG = "⚠️ Telegram has limited message sending.\n⏳ Please wait: {time_str}\nTo update timer send URL again 2 times."
    AA_VLC_IOS_MSG = "🎬 <b><a href=\"https://itunes.apple.com/app/apple-store/id650377962\">VLC Player (iOS)</a></b>\n\n<i>Click button to copy stream URL, then paste it in VLC app</i>"
    AA_VLC_ANDROID_MSG = "🎬 <b><a href=\"https://play.google.com/store/apps/details?id=org.videolan.vlc\">VLC Player (Android)</a></b>\n\n<i>Click button to copy stream URL, then paste it in VLC app</i>"
    AA_ERROR_GETTING_LINK_MSG = "❌ <b>Error getting link:</b>\n{error_msg}"
    AA_ERROR_SENDING_FORMATS_MSG = "❌ Error sending formats file: {error}"
    AA_FAILED_GET_FORMATS_MSG = "❌ Failed to get formats:\n<code>{output}</code>"
    AA_PROCESSING_WAIT_MSG = "🔄 Обработка... (wait 6 sec)"
    AA_PROCESSING_MSG = "🔄 Обработка..."
    AA_TAG_FORBIDDEN_CHARS_MSG = "❌ Tag #{wrong} contains forbidden characters. Only letters, digits and _ are allowed.\nPlease use: {example}"
    
    # Helper limitter messages
    HELPER_ADMIN_RIGHTS_REQUIRED_MSG = "❗️ Для работы в группе боту нужны права администратора. Пожалуйста, сделайте бота админом этой группы."
    
    # URL extractor messages
    URL_EXTRACTOR_AUDIO_HINT_MSG = "Download only audio from video source.\n\nUsage: /audio + URL \n\n(ex. /audio https://youtu.be/abc123)\n(ex. /audio https://youtu.be/playlist?list=abc123*1*10)"
    URL_EXTRACTOR_WELCOME_MSG = "Hello {first_name},\n \n<i>This bot🤖 can download any videos into telegram directly.😊 For more information press <b>/help</b></i> 👈\n \n {credits}"
    URL_EXTRACTOR_NO_FILES_TO_REMOVE_MSG = "🗑 Нет files К Удалить."
    URL_EXTRACTOR_ALL_FILES_REMOVED_MSG = "🗑 All files removed successfully!\n\nRemoved files:\n{files_list}"
    URL_EXTRACTOR_ALL_MEDIA_FILES_REMOVED_MSG = "🗑 Все Медиа files are removed."
    
    # Video extractor messages
    VIDEO_EXTRACTOR_WAIT_DOWNLOAD_MSG = "⏰ WAIT До YOUR Предыдущий Скачать IS FINISHED"
    
    # Helper messages
    HELPER_APP_INSTANCE_NONE_MSG = "App instance is Никто В check_user"
    HELPER_CHECK_FILE_SIZE_LIMIT_INFO_DICT_NONE_MSG = "check_file_size_limit: info_dict is Никто, allowing Скачать"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_NONE_MSG = "check_subs_limits: info_dict is Никто, allowing subtitle embedding"
    HELPER_CHECK_SUBS_LIMITS_CHECKING_LIMITS_MSG = "check_subs_limits: checking limits - max_quality={max_quality}p, max_duration={max_duration}s, max_size={max_size}MB"
    HELPER_CHECK_SUBS_LIMITS_INFO_DICT_KEYS_MSG = "check_subs_limits: info_dict keys: {keys}"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_DURATION_MSG = "Subtitle embedding skipped: duration {duration}s exceeds limit {max_duration}s"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_SIZE_MSG = "Subtitle embedding skipped: size {size_mb:.2f}MB exceeds limit {max_size}MB"
    HELPER_SUBTITLE_EMBEDDING_SKIPPED_QUALITY_MSG = "Subtitle embedding skipped: quality {width}x{height} (min side {min_side}p) exceeds limit {max_quality}p"
    HELPER_COMMAND_TYPE_TIKTOK_MSG = "ТикТок"
    HELPER_COMMAND_TYPE_INSTAGRAM_MSG = "Инстаграм"
    HELPER_COMMAND_TYPE_PLAYLIST_MSG = "плейлист"
    HELPER_RANGE_LIMIT_EXCEEDED_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count}).\n\nUse one of these commands to download maximum available files:\n\n<code>{suggested_command_url_format}</code>\n\n"
    HELPER_RANGE_LIMIT_EXCEEDED_LOG_MSG = "❗️ Range limit exceeded for {service}: {count} (maximum {max_count})\nUser ID: {user_id}"
    
    # Handler registry messages
    
    # Download status messages
    
    # POT helper messages
    HELPER_POT_PROVIDER_DISABLED_MSG = "PO token provider Отключен В config"
    HELPER_POT_URL_NOT_YOUTUBE_MSG = "URL {url} is not a YouTube domain, skipping PO token"
    HELPER_POT_PROVIDER_NOT_AVAILABLE_MSG = "PO token provider is not available at {base_url}, falling back to standard YouTube extraction"
    HELPER_POT_PROVIDER_CACHE_CLEARED_MSG = "PO token provider cache cleared, will Проверить availability На Следующий request"
    HELPER_POT_GENERIC_ARGS_MSG = "generic:impersonate=chrome,youtubetab:skip=authcheck"
    
    # Safe messenger messages
    HELPER_APP_INSTANCE_NOT_AVAILABLE_MSG = "App instance not Доступно Еще"
    HELPER_USER_NAME_MSG = "Пользователь"
    HELPER_FLOOD_WAIT_DETECTED_SLEEPING_MSG = "Flood wait detected, sleeping for {wait_seconds} seconds"
    HELPER_FLOOD_WAIT_DETECTED_COULDNT_EXTRACT_MSG = "Flood wait detected but couldn't extract time, sleeping for {retry_delay} seconds"
    HELPER_MSG_SEQNO_ERROR_DETECTED_MSG = "msg_seqno error detected, sleeping for {retry_delay} seconds"
    HELPER_MESSAGE_ID_INVALID_MSG = "MESSAGE_ID_INVALID"
    HELPER_MESSAGE_DELETE_FORBIDDEN_MSG = "MESSAGE_DELETE_FORBIDDEN"
    
    # Proxy helper messages
    HELPER_PROXY_CONFIG_INCOMPLETE_MSG = "Proxy Конфигурация Неполно, using direct Соединение"
    HELPER_PROXY_COOKIE_PATH_MSG = "users/{user_id}/cookie.txt"
    
    # URL extractor messages
    URL_EXTRACTOR_HELP_CLOSE_BUTTON_MSG = "🔚Близко"
    URL_EXTRACTOR_ADD_GROUP_CLOSE_BUTTON_MSG = "🔚Близко"
    URL_EXTRACTOR_COOKIE_ARGS_YOUTUBE_MSG = "youtube"
    URL_EXTRACTOR_COOKIE_ARGS_TIKTOK_MSG = "tiktok"
    URL_EXTRACTOR_COOKIE_ARGS_INSTAGRAM_MSG = "instagram"
    URL_EXTRACTOR_COOKIE_ARGS_TWITTER_MSG = "twitter"
    URL_EXTRACTOR_COOKIE_ARGS_CUSTOM_MSG = "Пользовательский"
    URL_EXTRACTOR_SAVE_AS_COOKIE_HINT_CLOSE_BUTTON_MSG = "🔚Близко"
    URL_EXTRACTOR_CLEAN_LOGS_FILE_REMOVED_MSG = "🗑 Логи Файл removed."
    URL_EXTRACTOR_CLEAN_TAGS_FILE_REMOVED_MSG = "🗑 Tags Файл removed."
    URL_EXTRACTOR_CLEAN_FORMAT_FILE_REMOVED_MSG = "🗑 Формат Файл removed."
    URL_EXTRACTOR_CLEAN_SPLIT_FILE_REMOVED_MSG = "🗑 Split Файл removed."
    URL_EXTRACTOR_CLEAN_MEDIAINFO_FILE_REMOVED_MSG = "🗑 Mediainfo Файл removed."
    URL_EXTRACTOR_CLEAN_SUBS_SETTINGS_REMOVED_MSG = "🗑 Subtitle Настройки removed."
    URL_EXTRACTOR_CLEAN_KEYBOARD_SETTINGS_REMOVED_MSG = "🗑 Keyboard Настройки removed."
    URL_EXTRACTOR_CLEAN_ARGS_SETTINGS_REMOVED_MSG = "🗑 Args Настройки removed."
    URL_EXTRACTOR_CLEAN_NSFW_SETTINGS_REMOVED_MSG = "🗑 NSFW Настройки removed."
    URL_EXTRACTOR_CLEAN_PROXY_SETTINGS_REMOVED_MSG = "🗑 Proxy Настройки removed."
    URL_EXTRACTOR_CLEAN_FLOOD_WAIT_SETTINGS_REMOVED_MSG = "🗑 Flood wait Настройки removed."
    URL_EXTRACTOR_VID_HELP_CLOSE_BUTTON_MSG = "🔚Близко"
    URL_EXTRACTOR_VID_HELP_TITLE_MSG = "🎬 Видео Скачать Command"
    URL_EXTRACTOR_VID_HELP_USAGE_MSG = "Usage: <code>/vid URL</code>"
    URL_EXTRACTOR_VID_HELP_EXAMPLES_MSG = "Examples:"
    URL_EXTRACTOR_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>"
    URL_EXTRACTOR_VID_HELP_ALSO_SEE_MSG = "Also see: /Аудио, /img, /Помощь, /playlist, /Настройки"
    URL_EXTRACTOR_ADD_GROUP_USER_CLOSED_MSG = "User {user_id} closed add_bot_to_group command"

    # YouTube messages
    YOUTUBE_FAILED_EXTRACT_ID_MSG = "Не удалось К extract YouTube ID"
    YOUTUBE_FAILED_DOWNLOAD_THUMBNAIL_MSG = "Не удалось К Скачать thumbnail or it is too big"
        
    # Thumbnail downloader messages
    
    # Commands messages   
    
    # Always Ask menu callback messages
    AA_CHOOSE_AUDIO_LANGUAGE_MSG = "Выбрать Аудио language"
    AA_NO_SUBTITLES_DETECTED_MSG = "Нет subtitles detected"
    AA_CHOOSE_SUBTITLE_LANGUAGE_MSG = "Выбрать subtitle language"
    
    # Gallery-dl error type messages
    GALLERY_DL_AUTH_ERROR_MSG = "Authentication Ошибка"
    GALLERY_DL_ACCOUNT_NOT_FOUND_MSG = "Account Not Found"
    GALLERY_DL_ACCOUNT_UNAVAILABLE_MSG = "Account Недоступно"
    GALLERY_DL_RATE_LIMIT_EXCEEDED_MSG = "Скорость Лимит Exceeded"
    GALLERY_DL_NETWORK_ERROR_MSG = "Сеть Ошибка"
    GALLERY_DL_CONTENT_UNAVAILABLE_MSG = "Содержимое Недоступно"
    GALLERY_DL_GEOGRAPHIC_RESTRICTIONS_MSG = "Географические Ограничения"
    GALLERY_DL_VERIFICATION_REQUIRED_MSG = "Требуется Проверка"
    GALLERY_DL_POLICY_VIOLATION_MSG = "Нарушение Политики"
    GALLERY_DL_UNKNOWN_ERROR_MSG = "Unknown Ошибка"
    
    # Download started message (used in both audio and video downloads)
    DOWNLOAD_STARTED_MSG = "<b>▶️ Download started</b>"
    
    # Split command constants
    SPLIT_CLOSE_BUTTON_MSG = "🔚Близко"
    
    # Always ask menu constants
    
    # Search command constants
    
    # List command constants
    
    # Magic.py messages
    MAGIC_VID_HELP_TITLE_MSG = "<b>🎬 Video Download Command</b>\n\n"
    MAGIC_VID_HELP_USAGE_MSG = "Usage: <code>/vid URL</code>\n\n"
    MAGIC_VID_HELP_EXAMPLES_MSG = "<b>Examples:</b>\n"
    MAGIC_VID_HELP_EXAMPLE_1_MSG = "• <code>/vid https://youtube.com/watch?v=123abc</code>\n"
    MAGIC_VID_HELP_EXAMPLE_2_MSG = "• <code>/vid https://youtube.com/playlist?list=123abc*1*5</code>\n"
    MAGIC_VID_HELP_EXAMPLE_3_MSG = "• <code>/vid 3-7 https://youtube.com/playlist?list=123abc</code>\n\n"
    MAGIC_VID_HELP_ALSO_SEE_MSG = "Also see: /audio, /img, /help, /playlist, /settings"
    
    # Flood limit messages
    FLOOD_LIMIT_TRY_LATER_FALLBACK_MSG = "⏳ Flood Лимит. Try Позже."
    
    # Cookie command usage messages
    COOKIE_COMMAND_USAGE_MSG = """<b>🍪 Cookie Command Usage</b>

<code>/cookie</code> - Show cookie menu
<code>/cookie youtube</code> - Download YouTube cookies
<code>/cookie instagram</code> - Download Instagram cookies
<code>/cookie tiktok</code> - Download TikTok cookies
<code>/cookie x</code> or <code>/cookie twitter</code> - Download Twitter/X cookies
<code>/cookie facebook</code> - Download Facebook cookies
<code>/cookie custom</code> - Show custom cookie instructions

<i>Available services depend on bot configuration.</i>"""
    
    # Cookie cache messages
    COOKIE_FILE_REMOVED_CACHE_CLEARED_MSG = "🗑 Cookie Файл removed and cache cleared."
    
    # Subtitles Command Messages
    SUBS_PREV_BUTTON_MSG = "⬅️ Prev"
    SUBS_BACK_BUTTON_MSG = "🔙Назад"
    SUBS_OFF_BUTTON_MSG = "🚫 Выкл"
    SUBS_SET_LANGUAGE_MSG = "• <code>/subs ru</code> - set language"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• <code>/subs ru auto</code> - set language with AUTO/TRANS"
    SUBS_VALID_OPTIONS_MSG = "Действительно Опции:"
    
    # Settings Command Messages
    SETTINGS_DEV_GITHUB_BUTTON_MSG = "🛠 Dev GitHub"
    SETTINGS_CONTR_GITHUB_BUTTON_MSG = "🛠 Contr GitHub"
    SETTINGS_CLEAN_BUTTON_MSG = "🧹 CLEAN"
    SETTINGS_COOKIES_BUTTON_MSG = "🍪 COOKIES"
    SETTINGS_MEDIA_BUTTON_MSG = "🎞 Медиа"
    SETTINGS_INFO_BUTTON_MSG = "📖 Информация"
    SETTINGS_MORE_BUTTON_MSG = "⚙️ Больше"
    SETTINGS_COOKIES_ONLY_BUTTON_MSG = "🍪 Cookies Только"
    SETTINGS_LOGS_BUTTON_MSG = "📃 Логи "
    SETTINGS_TAGS_BUTTON_MSG = "#️⃣ Tags"
    SETTINGS_FORMAT_BUTTON_MSG = "📼 Формат"
    SETTINGS_SPLIT_BUTTON_MSG = "✂️ Split"
    SETTINGS_MEDIAINFO_BUTTON_MSG = "📊 Mediainfo"
    SETTINGS_SUBTITLES_BUTTON_MSG = "💬 Subtitles"
    SETTINGS_KEYBOARD_BUTTON_MSG = "🎹 Keyboard"
    SETTINGS_ARGS_BUTTON_MSG = "⚙️ Args"
    SETTINGS_NSFW_BUTTON_MSG = "🔞 NSFW"
    SETTINGS_PROXY_BUTTON_MSG = "🌎 Proxy"
    SETTINGS_FLOOD_WAIT_BUTTON_MSG = "🔄 Flood wait"
    SETTINGS_ALL_FILES_BUTTON_MSG = "🗑  Все files"
    SETTINGS_DOWNLOAD_COOKIE_BUTTON_MSG = "📥 /cookie - Скачать my 5 cookies"
    SETTINGS_COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 /cookies_from_browser - Get Браузер's YT-cookie"
    SETTINGS_CHECK_COOKIE_BUTTON_MSG = "🔎 /check_cookie - Проверить your cookie Файл"
    SETTINGS_SAVE_AS_COOKIE_BUTTON_MSG = "🔖 /save_as_cookie - Загрузить Пользовательский cookie"
    SETTINGS_FORMAT_CMD_BUTTON_MSG = "📼 /Формат - Change Качество & Формат"
    SETTINGS_MEDIAINFO_CMD_BUTTON_MSG = "📊 /mediainfo - Turn На / Выкл MediaInfo"
    SETTINGS_SPLIT_CMD_BUTTON_MSG = "✂️ /split - Change split Видео Часть Размер"
    SETTINGS_AUDIO_CMD_BUTTON_MSG = "🎧 /Аудио - Скачать Видео as Аудио"
    SETTINGS_SUBS_CMD_BUTTON_MSG = "💬 /subs - Subtitles language Настройки"
    SETTINGS_PLAYLIST_CMD_BUTTON_MSG = "⏯️ /playlist - How К Скачать playlists"
    SETTINGS_IMG_CMD_BUTTON_MSG = "🖼 /img - Скачать images via gallery-dl"
    SETTINGS_TAGS_CMD_BUTTON_MSG = "#️⃣ /tags - Отправить your #tags"
    SETTINGS_HELP_CMD_BUTTON_MSG = "🆘 /Помощь - Get Инструкции"
    SETTINGS_USAGE_CMD_BUTTON_MSG = "📃 /usage -Отправить your Логи"
    SETTINGS_PLAYLIST_HELP_CMD_BUTTON_MSG = "⏯️ /playlist - Playlist's Помощь"
    SETTINGS_ADD_BOT_CMD_BUTTON_MSG = "🤖 /add_bot_to_group - howto"
    SETTINGS_LINK_CMD_BUTTON_MSG = "🔗 /Ссылка - Get direct Видео links"
    SETTINGS_PROXY_CMD_BUTTON_MSG = "🌍 /proxy - Включить/Отключить proxy"
    SETTINGS_KEYBOARD_CMD_BUTTON_MSG = "🎹 /keyboard - Keyboard layout"
    SETTINGS_SEARCH_CMD_BUTTON_MSG = "🔍 /Поиск - Inline Поиск helper"
    SETTINGS_ARGS_CMD_BUTTON_MSG = "⚙️ /args - yt-dlp arguments"
    SETTINGS_NSFW_CMD_BUTTON_MSG = "🔞 /nsfw - NSFW blur Настройки"
    SETTINGS_CLEAN_OPTIONS_MSG = "<b>🧹 Clean Options</b>\n\nChoose what to clean:"
    SETTINGS_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Activate @vid search"
    
    # Search Command Messages
    SEARCH_MOBILE_ACTIVATE_SEARCH_MSG = "📱 Mobile: Activate @vid search"
    
    # Keyboard Command Messages
    KEYBOARD_OFF_BUTTON_MSG = "🔴 Выкл"
    KEYBOARD_FULL_BUTTON_MSG = "🔣 Полно"
    KEYBOARD_1X3_BUTTON_MSG = "📱 1x3"
    KEYBOARD_2X3_BUTTON_MSG = "📱 2x3"
    
    # Image Command Messages
    IMAGE_URL_CAPTION_MSG = "🔗[Images URL]({url}) @{Config.BOT_NAME}"
    IMAGE_ERROR_MSG = "❌ Error: {str(e)}"
    
    # Format Command Messages
    FORMAT_BACK_BUTTON_MSG = "🔙Назад"
    FORMAT_CUSTOM_FORMAT_MSG = "• <code>/format &lt;format_string&gt;</code> - custom format"
    FORMAT_720P_MSG = "• <code>/format 720</code> - 720p quality"
    FORMAT_4K_MSG = "• <code>/format 4k</code> - 4K quality"
    FORMAT_8K_MSG = "• <code>/format 8k</code> - 8K quality"
    FORMAT_ID_MSG = "• <code>/format id 401</code> - specific format ID"
    FORMAT_ASK_MSG = "• <code>/format ask</code> - always show menu"
    FORMAT_BEST_MSG = "• <code>/format best</code> - bv+ba/best quality"
    FORMAT_ALWAYS_ASK_BUTTON_MSG = "❓ Always Ask (Меню + buttons)"
    FORMAT_OTHERS_BUTTON_MSG = "🎛 Others (144p - 4320p)"
    FORMAT_4K_PC_BUTTON_MSG = "💻4k (Лучший for PC/Mac Telegram)"
    FORMAT_FULLHD_MOBILE_BUTTON_MSG = "📱FullHD (Лучший for Мобильный Telegram)"
    FORMAT_BESTVIDEO_BUTTON_MSG = "📈Bestvideo+Bestaudio (MAX Качество)"
    FORMAT_CUSTOM_BUTTON_MSG = "🎚 Пользовательский (enter your own)"
    
    # Cookies Command Messages
    COOKIES_YOUTUBE_BUTTON_MSG = "📺 YouTube (1-{max(1, len(get_youtube_cookie_urls()))})"
    COOKIES_FROM_BROWSER_BUTTON_MSG = "🌐 От Браузер"
    COOKIES_TWITTER_BUTTON_MSG = "🐦 Twitter/X"
    COOKIES_TIKTOK_BUTTON_MSG = "🎵 TikTok"
    COOKIES_VK_BUTTON_MSG = "📘 Vkontakte"
    COOKIES_INSTAGRAM_BUTTON_MSG = "📷 Instagram"
    COOKIES_YOUR_OWN_BUTTON_MSG = "📝 Your Own"
    
    # Args Command Messages
    ARGS_INPUT_TIMEOUT_MSG = "⏰ Input Режим automatically Закрыт Срок К inactivity (5 minutes)."
    ARGS_RESET_ALL_BUTTON_MSG = "🔄 Сбросить Все"
    ARGS_VIEW_CURRENT_BUTTON_MSG = "📋 Взгляд Текущий"
    ARGS_BACK_BUTTON_MSG = "🔙 Назад"
    ARGS_FORWARD_TEMPLATE_MSG = "\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    ARGS_NO_SETTINGS_MSG = "📋 Current yt-dlp Arguments:\n\nNo custom settings configured.\n\n---\n\n<i>Forward this message to your favorites to save these settings as a template.</i> \n\n<i>Forward this message back here to apply these settings.</i>"
    ARGS_CURRENT_ARGUMENTS_MSG = "📋 Текущий yt-dlp Arguments:\n\n"
    ARGS_EXPORT_SETTINGS_BUTTON_MSG = "📤 Export Настройки"
    ARGS_SETTINGS_READY_MSG = "Настройки Готов for export! Forward this Сообщение К favorites К Сохранить."
    ARGS_CURRENT_VALUE_MSG = "Current value: <code>{value}</code>"
    ARGS_CURRENT_ARGUMENTS_HEADER_MSG = "📋 Текущий yt-dlp Arguments:"
    ARGS_FAILED_RECOGNIZE_MSG = "❌ Не удалось К recognize Настройки В Сообщение. Make sure you sent a Правильно Настройки template."
    ARGS_SUCCESSFULLY_IMPORTED_MSG = "✅ Settings successfully imported!\n\nApplied parameters: {applied_count}\n\n"
    ARGS_KEY_SETTINGS_MSG = "Key Настройки:\n"
    ARGS_ERROR_SAVING_MSG = "❌ Ошибка saving imported Настройки."
    ARGS_ERROR_IMPORTING_MSG = "❌ An Ошибка occurred Пока importing Настройки."

    #######################################################
