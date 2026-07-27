import asyncio
import time
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8444536750:AAHfP5U_yEMLdq3JOvyawRyufM3lGtCPRb0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Словник для збереження часу останньої відповіді користувачу
last_response_time = {}

# КД в секундах (15 хвилин = 900 секунд)
COOLDOWN_SECONDS = 900

@dp.message_handler()
async def send_reply(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    # Перевіряємо, чи пройшло 15 хвилин з останньої відповіді цьому користувачу
    if user_id not in last_response_time or (current_time - last_response_time[user_id]) > COOLDOWN_SECONDS:
        
        # Імітуємо статус "друкує" (це показує, що бот нібито в мережі)
        await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)
        
        # Невелика пауза для реалістичності
        await asyncio.sleep(2) 
        
        await message.answer("Привіт! Я зараз зайнятий, але обов'язково відповім тобі пізніше!")
        
        # Оновлюємо час останньої відповіді
        last_response_time[user_id] = current_time
    else:
        # Якщо 15 хвилин ще не пройшло — ігноруємо повідомлення (КД працює)
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    