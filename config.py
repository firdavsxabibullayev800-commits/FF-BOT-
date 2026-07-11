import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Majburiy obuna kanallari (@ belgisisiz, faqat username)
REQUIRED_CHANNELS = [
    "ffpanelchit",
    "xonfirestream",
    "sunniyintellekt_darslar",
]

HELP_CONTACT = "@ffhelpnastroyka"

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi! .env faylida yoki Railway Variables'da BOT_TOKEN kiriting.")
