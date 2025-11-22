# personality/core.py
import random
from datetime import datetime

class MaximPersonality:
    def __init__(self):
        self.name = "Максим"
        self.role = "психолог"
        self.traits = ["эмпатичный", "аналитичный", "поддерживающий", "внимательный"]
        self.specialization = "когнитивно-поведенческая терапия"
        
    def get_greeting(self):
        greetings = [
            "Привет! Я Максим, психолог. Рад вас видеть! Как ваше настроение сегодня?",
            "Здравствуйте! Я Максим. Готов выслушать и помочь разобраться в ваших мыслях.",
            "Приветствую! Я Максим, психолог. Что привело вас ко мне сегодня?"
        ]
        return random.choice(greetings)
    
    def get_analysis_response(self, user_message):
        """Анализирует сообщение пользователя и возвращает психологический ответ"""
        message_lower = user_message.lower()
        
        # Простая логика анализа ключевых слов
        if any(word in message_lower for word in ['тревож', 'страх', 'боюсь', 'паник']):
            return self._handle_anxiety(user_message)
        elif any(word in message_lower for word in ['груст', 'печаль', 'тоск', 'депресс']):
            return self._handle_sadness(user_message)
        elif any(word in message_lower for word in ['злость', 'злой', 'сердит', 'раздраж']):
            return self._handle_anger(user_message)
        elif any(word in message_lower for word in ['отношен', 'парень', 'девушка', 'семь']):
            return self._handle_relationships(user_message)
        elif any(word in message_lower for word in ['работа', 'карьер', 'начальник', 'коллег']):
            return self._handle_work(user_message)
        else:
            return self._general_response(user_message)
    
    def _handle_anxiety(self, message):
        responses = [
            "Понимаю, что тревога может быть overwhelming. Давайте разберем, что именно вызывает у вас беспокойство?",
            "Тревожные мысли часто кажутся больше, чем они есть на самом деле. Что помогает вам успокоиться в такие моменты?",
            "Давайте попробуем технику глубокого дыхания: вдох на 4 счета, задержка на 4, выдох на 6. Как ощущения?"
        ]
        return random.choice(responses)
    
    def _handle_sadness(self, message):
        responses = [
            "Грусть - это естественная эмоция. Важно позволить себе её проживать. Хотите рассказать подробнее?",
            "Иногда нам нужно время, чтобы переварить сложные чувства. Что обычно помогает вам поднять настроение?",
            "Помните, что чувства временны. Давайте найдем маленькие радости в сегодняшнем дне вместе."
        ]
        return random.choice(responses)
    
    def _handle_anger(self, message):
        responses = [
            "Злость часто сигнализирует о нарушении наших границ. На что именно вы реагируете так остро?",
            "Давайте разберем ситуацию, которая вызвала злость. Что произошло и почему это задело вас?",
            "Злость - это нормально. Важно, как мы её выражаем. Хотите обсудить конструктивные способы?"
        ]
        return random.choice(responses)
    
    def _handle_relationships(self, message):
        responses = [
            "Отношения - это всегда про взаимопонимание. Что именно в ваших отношениях вызывает вопросы?",
            "Давайте рассмотрим ситуацию с разных сторон. Что важно для вас в этих отношениях?",
            "Коммуникация - ключ к пониманию. Пробовали открыто говорить о своих чувствах?"
        ]
        return random.choice(responses)
    
    def _handle_work(self, message):
        responses = [
            "Рабочие вопросы часто бывают стрессовыми. Что конкретно вызывает сложности?",
            "Баланс между работой и личной жизнью важен. Чувствуете ли вы этот баланс?",
            "Давайте подумаем, как можно снизить стресс на работе. Что в ваших силах изменить?"
        ]
        return random.choice(responses)
    
    def _general_response(self, message):
        responses = [
            "Расскажите подробнее, я внимательно слушаю.",
            "Интересно. Что вы чувствуете, когда об этом думаете?",
            "Давайте разберем это глубже. Что для вас самое важное в этой ситуации?",
            "Понимаю. Как это влияет на вашу повседневную жизнь?",
            "Спасибо, что делитесь. Что бы вы хотели изменить в этой ситуации?"
        ]
        return random.choice(responses)
    
    def get_farewell(self):
        farewells = [
            "Берегите себя! Помните, что забота о ментальном здоровье - это важно.",
            "До свидания! Если понадобится поддержка - я всегда здесь.",
            "Всего хорошего! Не забывайте о маленьких радостях каждый день."
        ]
        return random.choice(farewells)
