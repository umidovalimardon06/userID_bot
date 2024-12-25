from aiogram import Bot, Dispatcher, types   ## Importing Aiogram libs
from aiogram.filters import CommandStart
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties
from asyncio import run

# Bot sozlamalari
bot = Bot(
    token="7596639329:AAGgXFoQ5g5R0suzp7EkDB9zOFnpyVGj3wY",
    session=AiohttpSession(),
    default=DefaultBotProperties(parse_mode="HTML")  # HTML formatni o'rnatamiz
)
dp = Dispatcher()

###################################################################

@dp.message(CommandStart())
async def send_user_id(message: types.Message):
    user = message.from_user
    # ID ni kopyalash uchun HTML formatda yuboramiz
    await message.answer(f"Here is your ID: <code>{user.id}</code>")

@dp.message()
async def echo(message: types.Message):
    user = message.from_user
    # ID ni kopyalash uchun HTML formatda yuboramiz
    await message.answer(f"Here is your ID: <code>{user.id}</code>")

###################################################################

async def main():
    await dp.start_polling(bot)

run(main())
