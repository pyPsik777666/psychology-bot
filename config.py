import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Конфигурация бота"""
    
    # Telegram
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    CHANNEL_ID = os.getenv('CHANNEL_ID', '@The_5way')
    
    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # Hugging Face
    HF_TOKEN = os.getenv('HF_TOKEN')
    
    # App settings
    DEFAULT_INTERVAL = 6  # hours
    MAX_RETRIES = 3
    LOG_LEVEL = 'INFO'
    
    @classmethod
    def validate_config(cls):
        """Проверка обязательных переменных"""
        required = ['TELEGRAM_TOKEN', 'SUPABASE_URL', 'SUPABASE_KEY']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required variables: {missing}")
        return True
