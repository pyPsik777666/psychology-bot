import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SimpleConfig:
    """Упрощенный конфиг"""
    def __init__(self):
        self.TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.CHANNEL_ID = os.getenv('CHANNEL_ID')
        self.SUPABASE_URL = os.getenv('SUPABASE_URL')
        self.SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        self.RENDER_EXTERNAL_URL = os.getenv('RENDER_EXTERNAL_URL', '')  # URL вашего сервиса на Render
    
    def validate_config(self):
        required = ['TELEGRAM_TOKEN', 'CHANNEL_ID', 'SUPABASE_URL', 'SUPABASE_KEY']
        for var in required:
            if not getattr(self, var):
                raise ValueError(f"Missing environment variable: {var}")

class SimpleMaximPersonality:
    """Упрощенная личность Максима"""
    def __init__(self):
        self.name = "Максим"
        self.role = "психолог"
    
    def get_introduction(self):
        return """Привет! Я Максим, ваш психолог-бот 🤗

Я здесь чтобы:
• Помочь разобраться в ваших мыслях и чувствах
• Предложить психологические упражнения
• Поддержать в сложные моменты

Просто напишите мне о том, что вас беспокоит, и я постараюсь помочь!"""
    
    def add_personality_flavor(self, text):
        return f"🤔 {text}"

class SimplePsychologyBot:
    """Упрощенная версия бота"""
    
    def __init__(self):
        self.config = SimpleConfig()
        self.config.validate_config()
        self.personality = SimpleMaximPersonality()
        
        self.logger = logger
        self.logger.info(f"🤖 Бот {self.personality.name} инициализирован!")
        self.application = None
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /start"""
        welcome_text = self.personality.get_introduction()
        await update.message.reply_text(welcome_text)
        
        user = update.effective_user
        self.logger.info(f"👋 Новый пользователь: {user.username}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработка обычных сообщений"""
        user_message = update.message.text
        user = update.effective_user
        
        self.logger.info(f"💬 Сообщение от {user.first_name}: {user_message}")
        
        # Простые ответы для начала
        responses = [
            "Понимаю ваши чувства. Расскажите подробнее, что вас беспокоит?",
            "Спасибо, что делитесь этим. Давайте разберем ситуацию вместе.",
            "Интересно. Что вы чувствуете, когда об этом думаете?",
            "Это важное наблюдение. Как это влияет на вашу жизнь?",
            "Понимаю. Давайте найдем способы справиться с этим."
        ]
        
        import random
        response = random.choice(responses)
        personalized_response = self.personality.add_personality_flavor(response)
        
        await update.message.reply_text(personalized_response)
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик ошибок"""
        self.logger.error(f"Ошибка: {context.error}")
        
        error_response = self.personality.add_personality_flavor(
            "Ой, что-то пошло не так... Попробуйте еще раз!"
        )
        
        if update and update.message:
            await update.message.reply_text(error_response)

    def setup_handlers(self):
        """Настройка обработчиков"""
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_error_handler(self.error_handler)

async def main():
    """Точка входа"""
    try:
        logger.info("🤖 ЗАПУСК ПСИХОЛОГИЧЕСКОГО БОТА...")
        
        # Проверяем переменные окружения
        required_vars = ['TELEGRAM_TOKEN', 'CHANNEL_ID', 'SUPABASE_URL', 'SUPABASE_KEY']
        for var in required_vars:
            value = os.getenv(var)
            if value:
                logger.info(f"✅ {var}: {value[:10]}...")
            else:
                logger.error(f"❌ {var}: НЕ УСТАНОВЛЕН!")
                return
        
        bot = SimplePsychologyBot()
        
        # Создаем приложение
        application = Application.builder().token(bot.config.TELEGRAM_TOKEN).build()
        bot.application = application
        bot.setup_handlers()
        
        # Запускаем бота в режиме polling
        logger.info("🚀 Бот запускается в режиме polling...")
        await application.run_polling()
        
    except Exception as e:
        logger.error(f"💥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    # Запускаем асинхронную main функцию
    asyncio.run(main())
