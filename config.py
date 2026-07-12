import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Majburiy obuna kanallari (@ belgisisiz, faqat username)
REQUIRED_CHANNELS = [
    "freefirepanelchit",
    "xonfirestream",
    "sunniyintellekt_darslar",
]

HELP_CONTACT = "@ffhelpnastroyka"
CHEAT_PANEL_CONTACT = "@freefirechitpanel"

# Bot egasi (admin) — butun raqamli Telegram ID. @userinfobot orqali oling.
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

DB_PATH = os.getenv("DB_PATH", "bot.db")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi! .env faylida yoki Railway Variables'da BOT_TOKEN kiriting.")
