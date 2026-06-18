import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from openai import OpenAI

TOKEN = '8982006024:AAEID_ht_eDOgOdvdDJQmFqrRLMS5wseuys'
GROQ_API_KEY = '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'

logging.basicConfig(level=logging.INFO)

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Здарова! Я GANG$TER в сети. Че надо? 😎")

@dp.message()
async def handle_message(message: types.Message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Ты — GANG$TER из GTA Online. Твой стиль: дерзкий, уличный сленг, эмодзи (😎, 💰, 🚗, 🔫). Ты всегда на движе, решаешь вопросы, не любишь нытиков. Отвечай кратко и четко."},
                {"role": "user", "content": message.text}
            ]
        )
        answer = response.choices[0].message.content
        await message.answer(answer)
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Слышь, я сейчас не в духе, попробуй позже! 🔫")

async def main():
    print("GANG$TER зашел в сеть...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
