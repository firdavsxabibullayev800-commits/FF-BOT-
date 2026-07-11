from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from config import REQUIRED_CHANNELS
from texts import DEVICE_LABELS


def subscribe_kb() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=f"📢 Kanal {i+1}", url=f"https://t.me/{ch}")]
        for i, ch in enumerate(REQUIRED_CHANNELS)
    ]
    rows.append([InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_sub")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def main_menu_kb() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="ℹ️ Yordam")],
        [KeyboardButton(text="🎯 Free Fire nastroykalar")],
        [KeyboardButton(text="🖼 Free Fire rasmlar")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def ff_settings_kb() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=label, callback_data=f"ff:{key}")]
        for key, label in DEVICE_LABELS.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_devices_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_devices")]]
    return InlineKeyboardMarkup(inline_keyboard=rows)
