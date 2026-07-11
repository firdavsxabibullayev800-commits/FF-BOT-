# 🎮 Free Fire Nastroyka Boti

Majburiy obuna talab qiluvchi, Free Fire sensitivity/nastroyka ma'lumotlarini beruvchi Telegram bot.

## Bot tuzilishi

**/start** bosilganda:
- Foydalanuvchi 3 ta kanalga obuna bo'lganmi tekshiriladi
- Obuna bo'lmasa — 3 kanal + "✅ Obunani tekshirish" tugmasi chiqadi, bot ishlamaydi
- Obuna bo'lgach — asosiy menyu ochiladi

**Asosiy menyu:**
1. ℹ️ Yordam — kontakt ma'lumot
2. 🎯 Free Fire nastroykalar — 6 ta qurilma tanlovi (iPhone, Samsung, Infinix, Tecno, Redmi, Honor)
3. 🖼 Free Fire rasmlar — hozircha "ishlamayapti" xabari (keyinchalik rasm qo'shsangiz bo'ladi)

---

## ⚠️ MUHIM: Botni kanallarga ADMIN qilib qo'shish kerak!

Obuna tekshiruvi ishlashi uchun bot quyidagi 3 kanalning barchasiga **admin** sifatida qo'shilishi shart (oddiy a'zo emas — Telegram API shuni talab qiladi):

- @ffpanelchit
- @xonfirestream
- @sunniyintellekt_darslar

**Qanday qilish kerak:** har bir kanalga kiring → Administrators → Add Administrator → botingizni qidirib toping → qo'shing (minimal huquqlar yetarli, masalan faqat "Invite users via link" yoqilgan bo'lsa ham bo'ladi, lekin eng ishonchlisi barcha huquqlarni yoqib qo'yish).

Agar bot biror kanalga admin qilib qo'shilmasa, o'sha kanal uchun tekshiruv doim "obuna emas" deb hisoblaydi.

---

## 🔑 Bot tokeningiz

```
8860661571:AAHhQtfma0GbGuZihzdfVdEily_wHVTKDAI
```

Bu token `.env` faylida saqlangan (Git'ga yuklanmaydi). **Muhim:** bu token endi shu suhbatda ko'rinib turibdi — agar botni boshqa birov bilan baham ko'rmoqchi bo'lmasangiz, xavotir olmang, chunki faqat siz kirasiz. Lekin agar tokenni kimdir bilib qolishidan xavotirdasiz, @BotFather → `/mybots` → botingiz → **Revoke token** orqali istalgan vaqtda yangisini olishingiz mumkin (keyin Railway'dagi `BOT_TOKEN`ni ham yangilashingiz kerak bo'ladi).

---

## 1-QADAM: GitHub'ga yuklash

```bash
cd freefire_bot
git init
git add .
git commit -m "Free Fire nastroyka boti"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NOMI.git
git push -u origin main
```

`.env` fayli `.gitignore`da bo'lgani uchun tokeningiz GitHub'ga yuklanmaydi — xavfsiz.

## 2-QADAM: Railway'da deploy

1. [railway.app](https://railway.app) → GitHub akkount bilan kiring
2. **New Project** → **Deploy from GitHub repo** → repozitoriyangizni tanlang
3. **Variables** bo'limiga o'ting, qo'shing:
   - `BOT_TOKEN` = `8860661571:AAHhQtfma0GbGuZihzdfVdEily_wHVTKDAI`
4. Deploy avtomatik boshlanadi (`Procfile` orqali `worker: python main.py` ishga tushadi)
5. Botga Telegram'da `/start` yozib tekshiring

---

## Loyiha tuzilishi

```
freefire_bot/
├── main.py                  # Botni ishga tushiruvchi fayl
├── config.py                 # Token, majburiy kanallar ro'yxati
├── texts.py                  # Barcha matnlar (nastroykalar, yordam)
├── keyboards.py               # Tugmalar
├── handlers/
│   ├── subscription.py        # Majburiy obuna tekshiruvi
│   └── menu.py                 # Yordam / Nastroykalar / Rasmlar
├── requirements.txt
├── Procfile
├── .env                        # Haqiqiy token (Git'ga yuklanmaydi)
└── .gitignore
```

## Nastroyka matnlarini o'zgartirish

Barcha qurilma nastroykalari `texts.py` faylidagi `FF_SETTINGS` lug'atida. Raqamlarni yoki matnni o'zgartirish uchun shu faylni tahrirlab, qayta deploy qilsangiz yetarli.

## Kanal ro'yxatini o'zgartirish

`config.py` faylidagi `REQUIRED_CHANNELS` ro'yxatiga kanal username'larini (`@` belgisisiz) qo'shing yoki olib tashlang.

---

### Keyingi qadamlar (xohlasangiz qo'shib beraman)
- 🖼 "Free Fire rasmlar" tugmasiga haqiqiy rasmlar qo'shish
- 📊 Foydalanuvchilar sonini kuzatish (statistika)
- 🔔 Barcha foydalanuvchilarga xabar yuborish (broadcast) — admin buyrug'i orqali
- ➕ Yangi qurilma turlarini qo'shish (masalan Oppo, Vivo)
