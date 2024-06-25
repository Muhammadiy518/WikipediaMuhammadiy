import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart , command , Command , Command
from aiogram.types import Message
from wiki import WikipediaFunction
import wikipedia
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7259770835:AAHgGc9U73pjFKxY0Piz1ZQNYzxUEGc9C48"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()







@dp.message(Command("rus"))
async def RUCommandHandler(message : Message):
    wikipedia.set_lang("rus")
    await message.answer("Rus tiliga o'girildi")


@dp.message(Command("en"))
async def ingCommandHandler(message : Message):
    wikipedia.set_lang("en")
    await message.answer("Ingliz tiliga o'girildi")





@dp.message(command.Command("uz"))
async def uzCommandHandler(message : Message):
    wikipedia.set_lang("uz")
    await message.answer("O'zbek tiliga o'girildi"),


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Assalomu aleykum wikipedia botga xush kelibsiz bu botda siz malumotlar topishingiz mumkin va hohlagan tilda malumot qidirishingiz mumkin, {html.bold(message.from_user.full_name)}! \n O'zbek tilini tanlash uchun /uz, \n Ingliz tilini tanlsh uchun esa /en, bosing \n Rus tilini tanlash uchun /rus ni bosing")


@dp.message()
async def WikipediaHandler(message : Message):
    malumot = WikipediaFunction(malumot=message.text)
    await message.answer(malumot)

    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())









