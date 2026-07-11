from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from handlers.subscription import is_subscribed
from keyboards import subscribe_kb, ff_settings_kb, back_to_devices_kb
from texts import (
    SUBSCRIBE_TEXT,
    HELP_TEXT,
    FF_IMAGES_TEXT,
    CHOOSE_DEVICE_TEXT,
    FF_SETTINGS,
    NOT_SUBSCRIBED_ALERT,
)

router = Router()


async def guard_subscribed(message: Message, bot: Bot) -> bool:
    """Obuna bo'lmagan bo'lsa, ogohlantirish yuborib False qaytaradi."""
    if not await is_subscribed(bot, message.from_user.id):
        await message.answer(SUBSCRIBE_TEXT, reply_markup=subscribe_kb())
        return False
    return True


@router.message(F.text == "ℹ️ Yordam")
async def help_handler(message: Message, bot: Bot):
    if not await guard_subscribed(message, bot):
        return
    await message.answer(HELP_TEXT)


@router.message(F.text == "🎯 Free Fire nastroykalar")
async def ff_settings_menu(message: Message, bot: Bot):
    if not await guard_subscribed(message, bot):
        return
    await message.answer(CHOOSE_DEVICE_TEXT, reply_markup=ff_settings_kb())


@router.message(F.text == "🖼 Free Fire rasmlar")
async def ff_images_handler(message: Message, bot: Bot):
    if not await guard_subscribed(message, bot):
        return
    await message.answer(FF_IMAGES_TEXT)


@router.callback_query(F.data.startswith("ff:"))
async def show_device_settings(callback: CallbackQuery, bot: Bot):
    if not await is_subscribed(bot, callback.from_user.id):
        await callback.answer(NOT_SUBSCRIBED_ALERT, show_alert=True)
        return
    device = callback.data.split(":")[1]
    text = FF_SETTINGS.get(device)
    if not text:
        await callback.answer("Topilmadi", show_alert=True)
        return
    await callback.message.edit_text(text, reply_markup=back_to_devices_kb())
    await callback.answer()


@router.callback_query(F.data == "back_to_devices")
async def back_to_devices(callback: CallbackQuery):
    await callback.message.edit_text(CHOOSE_DEVICE_TEXT, reply_markup=ff_settings_kb())
    await callback.answer()
