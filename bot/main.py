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
# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


# --- REPLY MENU MARKUP ---
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


# --- INLINE MENU ---
def i_test_menu():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Item1", callback_data="itm1")],
            [InlineKeyboardButton(text="Item2", callback_data="itm2")],
            [InlineKeyboardButton(text="Item3", callback_data="itm3")],
            [InlineKeyboardButton(text="Item4", callback_data="itm4")],
            [InlineKeyboardButton(text="Item5", callback_data="itm5")],
            [InlineKeyboardButton(text="Item6", callback_data="itm6")],
        ]
    )
    return kb


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm ready!", reply_markup=r_main_menu())


@dp.message()
async def reply_kb_handler(message: types.Message) -> None:
    msg = message.text
    cid = message.from_user.id
    if msg == "Про нас🤭":
        print("Створив: Коломоєць Тимофій, новачок зі створення ботів")
        # await bot.send_message(cid, "Some Text")
        text = ("Adjust previously added buttons to specific row sizes.\n"
                "\n"
                "By default, when the sum of passed sizes is lower than buttons count the last one size will be used "
                "for tail of the markup. If repeat=True is passed - all sizes will be cycled when available more "
                "buttons count than all sizes")
        await message.answer(text)
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
        return kb
    elif msg == "Назад":
        await message.answer("Ви повернулись назад", reply_markup=r_main_menu())
    elif msg == "Інформація про жаб":
        await message.answer("В Японії жаб вважають символом удачі.  У Франції жаб’ячі лапки вживаються в їжу. Основними імпортерами жаб є Франція, Бельгія, Люксембург і США, основні експортери – Китай та Індонезія. Жаби здатні дихати під водою. Жаби пересуваються стрибками, але деякі види освоїли і інші методи пересування: ходіння, біг, плавання і політ", reply_markup=i_test_menu())
    elif msg == "Інформація про жаб":
        await message.answer("Коли настав чудовий май,Садочків розвивання,Тоді у серденьку моїмПрокинулось кохання.Коли настав чудовий май І пташок щебетання,Тоді я милій розказав Мою журбу й кохання.")

async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if name == "main":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())