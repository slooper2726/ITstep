import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6865233291:AAEgws23mMQXsmWz3BOqCiDrWkHqUPMmwn4"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про нас🤭")],
            [KeyboardButton(text="Корисні смаколики"), KeyboardButton(text="Інформація про жаб")],
            [KeyboardButton(text="Коли настав чудовий май")]
        ],
        resize_keyboard=True
    )
    return kb


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привіт. Я готовий!", reply_markup=r_main_menu())


FOOD = ["ябко", "груша", "полуниця", "апельсин", "морква", "слива", "мандарин"]


@dp.message()
async def reply_kb_handler(message: types.Message) -> None:
    msg = message.text
    if msg == "Про нас🤭":
        await message.answer("Створив: Коломоєць Тимофій, новачок зі створення ботів")
    elif msg == "Корисні смаколики":
        kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="ябко")],
                [KeyboardButton(text="груша"), KeyboardButton(text="морква")],
                [KeyboardButton(text="полуниця"), KeyboardButton(text="слива")],
                [KeyboardButton(text="апельсин"), KeyboardButton(text="мандарин")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Виберіть смаколик", reply_markup=kb)
    elif msg in FOOD:
        await message.answer(f"{msg} - смачний вибір!")
    elif msg == "Назад":
        await message.answer("Ви повернулись назад", reply_markup=r_main_menu())
    elif msg == "Інформація про жаб":
        await message.answer(
            "В Японії жаб вважають символом удачі. "
            "У Франції жаб’ячі лапки вживаються в їжу. "
            "Основними імпортерами жаб є Франція, Бельгія, Люксембург і США, основні експортери – Китай та Індонезія. "
            "Жаби здатні дихати під водою. "
            "Жаби пересуваються стрибками, але деякі види освоїли і інші методи пересування: "
            "ходіння, біг, плавання і політ"
        )
    elif msg == "Коли настав чудовий май":
        await message.answer(
            "Коли настав чудовий май,\n"
            "Садочків розвивання,\n"
            "Тоді у серденьку моїм\n"
            "Прокинулось кохання.\n"
            "Коли настав чудовий май\n"
            "І пташок щебетання,\n"
            "Тоді я милій розказав\n"
            "Мою журбу й кохання."
        )


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
