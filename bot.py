import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = тут має бути код 
API_HASH = 'тут має бути код '

SESSION_STRING = os.getenv('STRING_SESSION', '')

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

CHAT_USERNAME = '@patrickstarsrobot'
BUTTON_TEXT = 'Кликер'

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

async def main():
    await client.start()
    await auto_clicker()

if __name__ == '__main__':
    asyncio.run(main())
    
