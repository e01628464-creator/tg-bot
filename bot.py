import os
import asyncio
from telethon import TelegramClient

API_ID = 32681074
API_HASH = '59181b6a0f9d5d01456b5b53b0806b22'

STRING_SESSION = os.getenv('STRING_SESSION')
CHAT_USERNAME = '@patrickstarsrobot'
BUTTON_TEXT = 'Кликер'

client = TelegramClient(STRING_SESSION, API_ID, API_HASH)

async def auto_clicker():
    print("Бот-кликер успешно запущен!")
    
    while True:
        try:
            print("Ищу кнопку 'Кликер' у Патрика...")
            messages = await client.get_messages(CHAT_USERNAME, limit=5)
            
            clicked = False
            for message in messages:
                if message.buttons:
                    for row in message.buttons:
                        for button in row:
                            if BUTTON_TEXT.lower() in button.text.lower():
                                await button.click()
                                print(f"Успешно нажата кнопка: {button.text}")
                                clicked = True
                                break
                        if clicked:
                            break
                if clicked:
                    break
            
            if not clicked:
                print("Кнопка 'Кликер' не найдена в последних сообщениях.")
                
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        print("Ожидание 6 минут до следующего нажатия...")
        await asyncio.sleep(360)

with client:
    client.loop.run_until_complete(auto_clicker())
                
