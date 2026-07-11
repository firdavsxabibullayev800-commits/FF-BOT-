from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from config import REQUIRED_CHANNELS
from keyboards import subscribe_kb, main_menu_kb
from texts import WELCOME_TEXT, SUBSCRIBE_TEXT, NOT_SUBSCRIBED_ALERT, SUBSCRIBED_OK_TEXT

router = Router()


async def is_subscribed(bot: Bot, user_id: int) -> bool:
    """Foydalanuvchi barcha majburiy kanallarga obuna bo'lganini tekshiradi."""
    for channel in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(f"@{channel}", user_id)
            if member.status in ("left", "kicked"):
                return False
        except Exception:
            return False
    return True


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    if await is_subscribed(bot, message.from_user.id):
        await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())
    else:
        await message.answer(SUBSCRIBE_TEXT, reply_markup=subscribe_kb())


@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery, bot: Bot):
    if await is_subscribed(bot, callback.from_user.id):
        await callback.message.edit_text(SUBSCRIBED_OK_TEXT)
        await callback.message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())
    else:
        await callback.answer(NOT_SUBSCRIBED_ALERT, show_alert=True)
