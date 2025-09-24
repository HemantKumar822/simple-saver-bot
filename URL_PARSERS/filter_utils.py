# Filter utilities for yt-dlp
import yt_dlp
from CONFIG.config import Config
from HELPERS.logger import logger

def create_smart_match_filter():
    """
    Создает умный match_filter, который разрешает скачивание если:
    1. Видео не является живым (!is_live)
    2. Длительность определена и <= MAX_VIDEO_DURATION
    3. Длительность не определена (duration is None) - разрешаем скачивание
    
    Returns:
        function: Функция фильтра для yt-dlp
    """
    def match_filter(info_dict):
        """
        Умный фильтр для yt-dlp
        
        Args:
            info_dict (dict): Словарь с информацией о видео
            
        Returns:
            str or None: None если видео проходит фильтр, иначе сообщение об ошибке
        """
        try:
            # Проверяем, является ли видео живым
            is_live = info_dict.get('is_live', False)
            if is_live:
                return "LIVE_STREAM_DETECTED"
            
            # Получаем длительность
            duration = info_dict.get('duration')
            
            # Если длительность не определена (None), разрешаем скачивание
            if duration is None:
                logger.info("Duration not available, allowing download")
                return None
            
            # Проверяем, является ли это завершенным стримом
            was_live = info_dict.get('was_live', False)
            if was_live and not is_live:
                logger.info(f"Completed live stream detected (duration: {duration}s), allowing download")
                return None
            
            # Если длительность определена, проверяем лимит
            if duration > Config.MAX_VIDEO_DURATION:
                return f"Video too long: {duration}s > {Config.MAX_VIDEO_DURATION}s"
            
            # Все проверки пройдены
            return None
            
        except Exception as e:
            logger.error(f"Error in match_filter: {e}")
            # В случае ошибки разрешаем скачивание
            return None
    
    return match_filter

def create_legacy_match_filter():
    """
    Создает стандартный match_filter для обратной совместимости
    
    Returns:
        function: Функция фильтра для yt-dlp
    """
    return yt_dlp.utils.match_filter_func(f'!is_live & duration <= {Config.MAX_VIDEO_DURATION}')
