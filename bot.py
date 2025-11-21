import os
import time
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_environment():
    """Проверяем все переменные окружения"""
    logger.info("🔍 Проверка переменных окружения...")
    
    required_vars = ['TELEGRAM_TOKEN', 'CHANNEL_ID', 'SUPABASE_URL', 'SUPABASE_KEY']
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            logger.info(f"✅ {var}: {value[:10]}...")  # Показываем только начало
        else:
            logger.error(f"❌ {var}: НЕ УСТАНОВЛЕН!")
            return False
    
    return True

def simple_bot():
    """Упрощенная версия бота"""
    try:
        logger.info("🤖 ЗАПУСК ПСИХОЛОГИЧЕСКОГО БОТА...")
        
        # Проверяем окружение
        if not check_environment():
            logger.error("🚫 Не все переменные установлены!")
            return
        
        logger.info("✅ Все переменные в порядке!")
        logger.info("🧪 Тест импортов...")
        
        # Тестируем импорты
        try:
            from config import Config
            logger.info("✅ config.py - OK")
        except Exception as e:
            logger.error(f"❌ config.py: {e}")
            return
            
        try:
            from personality.core import MaximPersonality
            logger.info("✅ personality/core.py - OK")
        except Exception as e:
            logger.error(f"❌ personality/core.py: {e}")
            return
        
        logger.info("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        logger.info("🚀 Бот готов к работе!")
        
        # Держим приложение запущенным
        while True:
            logger.info("💤 Бот работает...")
            time.sleep(60)
            
    except Exception as e:
        logger.error(f"💥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    simple_bot()
