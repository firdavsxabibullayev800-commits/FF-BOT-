from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from config import REQUIRED_CHANNELS
from texts import DEVICE_LABELS


def subscribe_kb() -> InlineKeyboardMarkup:
    channel_buttons = [
        InlineKeyboardButton(text=f"📢 Kanal {i+1}", url=f"https://t.me/{ch}")
        for i, ch in enumerate(REQUIRED_CHANNELS)
    ]
    rows = [channel_buttons[i:i+2] for i in range(0, len(channel_buttons), 2)]
    rows.append([InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_sub")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def main_menu_kb(is_admin: bool = False) -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="🆔 Free Fire niklar"), KeyboardButton(text="🎯 Free Fire nastroykalar")],
        [KeyboardButton(text="📚 Qo'llanmalar"), KeyboardButton(text="🎨 Premium bo'lim")],
        [KeyboardButton(text="🛠 Cheat va Panellar"), KeyboardButton(text="🌐 Proxy Server")],
        [KeyboardButton(text="ℹ️ Yordam")],
    ]
    if is_admin:
        kb.append([KeyboardButton(text="📊 Statistika")])
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def ff_settings_kb() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=label, callback_data=f"ff:{key}")
        for key, label in DEVICE_LABELS.items()
    ]
    rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_devices_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_devices")]]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def niklar_kb() -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(text="👑 Super niklar", callback_data="nik:super"),
            InlineKeyboardButton(text="🎮 Gamer niklar", callback_data="nik:gamer"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_niklar_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_niklar")]]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def guides_kb() -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(text="🎯 Headshot sirlari", callback_data="guide:headshot"),
            InlineKeyboardButton(text="🏆 Rank ko'tarish", callback_data="guide:rank"),
        ],
        [
            InlineKeyboardButton(text="🛡️ Gloo Wall", callback_data="guide:gloowall"),
            InlineKeyboardButton(text="⚔️ Rush usullari", callback_data="guide:rush"),
        ],
        [
            InlineKeyboardButton(text="🎯 Snayper maslahatlar", callback_data="guide:sniper"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def back_to_guides_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_guides")]]
    return InlineKeyboardMarkup(inline_keyboard=rows)
