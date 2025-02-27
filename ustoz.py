from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Dispatcher, Bot
import asyncio
from aiogram.filters import Command
import requests
import re

bot = Bot(token="7876493127:AAHAqtjReSOwWBOWvE2_1XBbxEeLqQsQKVg")
dp = Dispatcher()

chat_id = ""
# @aiogramstart
url = f"https://api.telegram.org/bot{bot}/sendMessage"

class Registratsiya(StatesGroup):
    name = State()
    age = State()
    aloqa = State()
    texnoliya = State()
    hudud = State()
    tolov = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    city = State()

class Sherik(StatesGroup):
    name = State()
    user = State()
    aloqa = State()
    texnoliya = State()
    hudud = State()
    tolov = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    city = State()

class Xodim(StatesGroup):
    iroda = State()
    texnologiya = State()
    telegram = State()
    aloqa = State()
    hudud = State()
    masul = State()
    murojat = State()
    ish_vaqt = State()
    moash = State()
    qoshimcha = State()

class Ustoz(StatesGroup):
    name = State()
    age = State()
    aloqa = State()
    texnoliya = State()
    hudud = State()
    tolov = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    city = State()

class Shogird(StatesGroup):
    name = State()
    age = State()
    aloqa = State()
    texnoliya = State()
    hudud = State()
    tolov = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    city = State()

@dp.message(Command("start"))
async def kirish(message:Message):
    await message.answer(f"salom sizga qanday yordam bera olamiz{message.from_user.username}")

@dp.message(Command("menu"))
async def catch_commend(message: Message):
    keyword = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ish joyi kerak"), KeyboardButton(text="Sherik Kerak")],
            [KeyboardButton(text="Xodim Kerak"), KeyboardButton(text="Ustoz Kerak")],
            [KeyboardButton(text="Shogird Kerak")]
        ],
        resize_keyboard=True
    )
    await message.answer(text="Quyidagi tugmadan foydalaning:", reply_markup=keyword)

@dp.message(lambda message: message.text == "Ish joyi kerak")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Ism, Familiyangizni kiriting")
    await state.set_state(Registratsiya.name)

@dp.message(lambda message: message.text == "Sherik Kerak")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Ism, Familiyangizni kiriting")
    await state.set_state(Sherik.name)

@dp.message(lambda message: message.text == "Xodim Kerak")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("🏢Iroda nomi")
    await state.set_state(Xodim.iroda)

@dp.message(lambda message: message.text == "Shogird Kerak")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Shogird topish uchun ariza berish\n"
                         "Hozir sizga birnecha savollar beriladi. \n"
                         "Har biriga javob bering. \n"
                         "Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
                         "arizangiz Adminga yuboriladi.\n"
                         )
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Shogird.name)


@dp.message(Shogird.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer("🕙Yoshingizni kiriting:\n"
                         "Masalan: 20 ")
    await state.set_state(Shogird.age)

@dp.message(Shogird.age)
async def get_name(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer("📡 Texnologiya kiriting:\n"
                             "Talab qilinadigan texnologiyalarni kiriting\n"
                             "Texnologiyalarni nomlarni vergul bilan ajrating.Masalan\n"
                             "Java,C++,C#,Python kabi")
        await state.set_state(Shogird.texnoliya)
    else:
        await message.answer("Siz xato ma'lumot kiritdingiz")

@dp.message(Shogird.texnoliya)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(texnoliya=message.text)

    await message.answer("📞Aloqa:\n"
                         "Siz o'zingizning telefon raqamingizni kiriting\n"
                         "Masalan: +998935589898")
    await state.set_state(Shogird.aloqa)

@dp.message(Shogird.aloqa)
async def get_texnoliya(message: Message, state: FSMContext):
    if re.match(r"^\+998[0-9]{9}$",message.text):
        await state.update_data(aloqa=message.text)
        await message.answer("🌐 Hudud:\n"
                             "Qaysi hududdan ekanligizni kiriting")
        await state.set_state(Shogird.hudud)
    else:
        "❌ Xatolik bo'ldi iltimos telefon raqamingizni qaytadan kiriting"

@dp.message(Shogird.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("💰 Narx\n"
                         "To'lov qilish summasini kiriting:")
    await state.set_state(Shogird.tolov)

@dp.message(Shogird.tolov)
async def get_tolov(message:Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(tolov=message.text)
        await message.answer("👨🏻‍💻 Kasbi:\n"
                             "Ishlaysizmi yoki o'qiysizmi\n"
                             "masalan: Talaba")
        await  state.set_state(Shogird.kasbi)
    else:
        await message.answer("🔢Siz kiritayotgan ma'lumot son ko'rinishida bo'lishi kerak\n"
                             "ILtimos yana qaytadan urunib ko'ring")

@dp.message(Shogird.kasbi)
async def get_kasb(message:Message, state:FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("🕰 Murojaat qilish vaqti:\n"
                       "Qaysi vaqt oraliqda bo'lishi kerak?\n"
                       "Masalan: 9:00-20:00 gacha")
    await state.set_state(Shogird.murojat)

@dp.message(Shogird.murojat)
async def get_maqsad(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("🔎 Maqsad: \n"
                         "Maqsad haqida qisqacha ma'lumot bering")
    await state.set_state(Ustoz.maqsad)


@dp.message(lambda message: message.text == "Ustoz Kerak")
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Ustoz topish uchun ariza berish\n"
                         "Hozir sizga birnecha savollar beriladi. \n"
                         "Har biriga javob bering. \n"
                         "Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\n"
                         "arizangiz Adminga yuboriladi.\n")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(Ustoz.name)
    # name = State()
    # age = State()
    # aloqa = State()
    # texnoliya = State()
    # hudud = State()
    # tolov = State()
    # kasbi = State()
    # murojat = State()
    # maqsad = State()
    # city = State()

@dp.message(Ustoz.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer("🕙Yoshingizni kiriting:\n"
                         "Masalan: 20 ")
    await state.set_state(Ustoz.age)

@dp.message(Ustoz.age)
async def get_name(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer("📡 Texnologiya kiriting:\n"
                             "Talab qilinadigan texnologiyalarni kiriting\n"
                             "Texnologiyalarni nomlarni vergul bilan ajrating.Masalan\n"
                             "Java,C++,C#,Python kabi")
        await state.set_state(Ustoz.texnoliya)
    else:
        await message.answer("Siz xato ma'lumot kiritdingiz")

@dp.message(Ustoz.texnoliya)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(texnoliya=message.text)

    await message.answer("📞Aloqa:\n"
                         "Siz o'zingizning telefon raqamingizni kiriting\n"
                         "Masalan: +998935589898")
    await state.set_state(Ustoz.aloqa)

@dp.message(Ustoz.aloqa)
async def get_texnoliya(message: Message, state: FSMContext):
    if re.match(r"^\+998[0-9]{9}$",message.text):
        await state.update_data(aloqa=message.text)
        await message.answer("🌐 Hudud:\n"
                             "Qaysi hududdan ekanligizni kiriting")
        await state.set_state(Ustoz.hudud)
    else:
        "❌ Xatolik bo'ldi iltimos telefon raqamingizni qaytadan kiriting"

@dp.message(Ustoz.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("💰 Narx\n"
                         "To'lov qilish summasini kiriting:")
    await state.set_state(Ustoz.tolov)

@dp.message(Ustoz.tolov)
async def get_tolov(message:Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(tolov=message.text)
        await message.answer("👨🏻‍💻 Kasbi:\n"
                             "Ishlaysizmi yoki o'qiysizmi\n"
                             "masalan: Talaba")
        await  state.set_state(Ustoz.kasbi)
    else:
        await message.answer("🔢Siz kiritayotgan ma'lumot son ko'rinishida bo'lishi kerak\n"
                             "ILtimos yana qaytadan urunib ko'ring")

@dp.message(Ustoz.kasbi)
async def get_kasb(message:Message, state:FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("🕰 Murojaat qilish vaqti:\n"
                       "Qaysi vaqt oraliqda bo'lishi kerak?\n"
                       "Masalan: 9:00-20:00 gacha")
    await state.set_state(Ustoz.murojat)

@dp.message(Ustoz.murojat)
async def get_maqsad(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("🔎 Maqsad: \n"
                         "Maqsad haqida qisqacha ma'lumot bering")
    await state.set_state(Ustoz.maqsad)


@dp.message(Registratsiya.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer("🕙Yoshingizni kiriting:\n"
                         "Masalan: 20 ")
    await state.set_state(Registratsiya.age)

@dp.message(Sherik.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer("📡 Texnologiya kiriting:\n"
                             "Talab qilinadigan texnologiyalarni kiriting\n"
                             "Texnologiyalarni nomlarni vergul bilan ajrating.Masalan\n"
                             "Java,C++,C#,Python kabi ")
    await state.set_state(Sherik.texnoliya)

@dp.message(Xodim.iroda)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(iroda= message.text)
    await message.answer("📡 Texnologiya :\n"
                             "Siz talab qiladigan texnologiya nomini kiriting\n"
                             "Masalan\n"
                             "Java,C++,C#,Python kabi ")
    await state.set_state(Xodim.texnologiya)

@dp.message(Registratsiya.age)
async def get_name(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer("📡 Texnologiya kiriting:\n"
                             "Talab qilinadigan texnologiyalarni kiriting\n"
                             "Texnologiyalarni nomlarni vergul bilan ajrating.Masalan\n"
                             "Java,C++,C#,Python kabi")
        await state.set_state(Registratsiya.texnoliya)
    else:
        await message.answer("Siz xato ma'lumot kiritdingiz")

@dp.message(Registratsiya.texnoliya)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(texnoliya=message.text)

    await message.answer("📞Aloqa:\n"
                         "Siz o'zingizning telefon raqamingizni kiriting\n"
                         "Masalan: +998935589898")
    await state.set_state(Registratsiya.aloqa)

@dp.message(Sherik.texnoliya)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(texnoliya=message.text)
    await message.answer("📞Aloqa:\n"
                         "Siz o'zingizning telefon raqamingizni kiriting\n"
                         "Masalan: +998935589898")
    await state.set_state(Sherik.aloqa)

@dp.message(Xodim.texnologiya)
async def get_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("📞Aloqa:\n"
                         "Siz o'zingizning telefon raqamingizni kiriting\n"
                         "Masalan: +998935589898")
    await state.set_state(Xodim.aloqa)


# natija = re.compile(r"^\+998[0-9]{9}$")
# print(natija.search("+998939898988"))
@dp.message(Registratsiya.aloqa)
async def get_texnoliya(message: Message, state: FSMContext):
    if re.match(r"^\+998[0-9]{9}$",message.text):
        await state.update_data(aloqa=message.text)
        await message.answer("🌐 Hudud:\n"
                             "Qaysi hududdan ekanligizni kiriting")
        await state.set_state(Registratsiya.hudud)
    else:
        "❌ Xatolik bo'ldi iltimos telefon raqamingizni qaytadan kiriting"


@dp.message(Sherik.aloqa)
async def get_texnoliya(message: Message, state: FSMContext):
    if re.match(r"^\+998[0-9]{9}$",message.text):
        await state.update_data(aloqa=message.text)
        await message.answer("🌐 Hudud:\n"
                             "Qaysi hududdan ekanligizni kiriting")
        await state.set_state(Sherik.hudud)
    else:
        "❌ Xatolik yuz berdi "


@dp.message(Xodim.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    if re.match(r"^\+998[0-9]{9}$",message.text):
        await state.update_data(aloqa=message.text)
        await message.answer("🌐 Hudud:\n"
                             "Qaysi hududdan ekanligizni kiriting")
        await state.set_state(Xodim.masul)
    else:
        "❌ Xatolik yuz berdi "

@dp.message(Xodim.masul)
async def get_masul(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)
    await message.answer("✍️ Mas'ul ism sharifi")
    await state.set_state(Xodim.murojat)

@dp.message(Xodim.murojat)
async def get_murojat(message: Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("🕰 Murojaat qilish vaqti: \n"
                         "Qaysi vaqtda murojaat qilish mumkin?\n"
                         "Masalan, 9:00 - 18:00")
    await state.set_state(Xodim.ish_vaqt)

@dp.message(Xodim.ish_vaqt)
async def get_ish_vaqt(message: Message, state: FSMContext):
    await state.update_data(ish_vaqt=message.text)
    await message.answer("✍🕰 Ish vaqtini kiriting?")
    await state.set_state(Xodim.moash)

@dp.message(Xodim.moash)
async def get_moash(message: Message, state: FSMContext):
    await state.update_data(moash=message.text)
    await message.answer("💰 Maoshni kiriting?")
    await state.set_state(Xodim.qoshimcha)

@dp.message(Registratsiya.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("💰 Narx\n"
                         "To'lov qilish summasini kiriting:")
    await state.set_state(Registratsiya.tolov)

@dp.message(Sherik.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("💰 Narx\n"
                         "To'lov qilish summasini kiriting:")
    await state.set_state(Sherik.tolov)

@dp.message(Xodim.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("💰 Narx\n"
                         "To'lov qilish summasini kiriting:")
    await state.set_state(Sherik.murojat)

@dp.message(Registratsiya.tolov)
async def get_tolov(message:Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(tolov=message.text)
        await message.answer("👨🏻‍💻 Kasbi:\n"
                             "Ishlaysizmi yoki o'qiysizmi\n"
                             "masalan: Talaba")
        await  state.set_state(Registratsiya.kasbi)
    else:
        await message.answer("🔢Siz kiritayotgan ma'lumot son ko'rinishida bo'lishi kerak\n"
                             "ILtimos yana qaytadan urunib ko'ring")


@dp.message(Sherik.tolov)
async def get_tolov(message:Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(tolov=message.text)
        await message.answer("👨🏻‍💻 Kasbi:\n"
                             "Ishlaysizmi yoki o'qiysizmi\n"
                             "masalan: Talaba")
        await  state.set_state(Sherik.kasbi)
    else:
        await message.answer("🔢Siz kiritayotgan ma'lumot son bo'lishi kerak")


@dp.message(Registratsiya.kasbi)
async def get_kasb(message:Message, state:FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("🕰 Murojaat qilish vaqti:\n"
                         "Qaysi vaqt oraliqda bo'lishi kerak?\n"
                         "Masalan: 9:00-20:00 gacha")
    await state.set_state(Registratsiya.murojat)

@dp.message(Sherik.kasbi)
async def get_kasb(message:Message, state:FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("🕰 Murojaat qilish vaqti:\n"
                       "Qaysi vaqt oraliqda bo'lishi kerak?\n"
                       "Masalan: 9:00-20:00 gacha")
    await state.set_state(Sherik.murojat)

@dp.message(Registratsiya.murojat)
async def get_maqsad(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("🔎 Maqsad: \n"
                         "Maqsad haqida qisqacha ma'lumot bering")
    await state.set_state(Registratsiya.maqsad)

@dp.message(Sherik.murojat)
async def get_maqsad(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("🔎 Maqsad: \n"
                         "Maqsad haqida qisqacha ma'lumot bering")
    await state.set_state(Sherik.maqsad)

@dp.message(Registratsiya.maqsad)
async def get_city(message: Message, state: FSMContext):
    user_data = await  state.get_data()
    keyword = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="send_result"), InlineKeyboardButton(text="yo'q", callback_data="cancel")]
        ]
    )

    result_text = ( f"✅ Ro'yxatdan o'tdingiz!\n\n"
                         f"👤 Ism: {user_data['name']}\n"
                         f"🎂 Yosh: {user_data.get('age')}\n"
                         f"📚 Texnoligiya:{user_data.get("texnoliya")}\n"
                         f"📞 Aloqa:{user_data.get("aloqa")}\n"
                         f"🌆 Hudud: {user_data.get("hudud")}\n"
                         f"💰 Narx: {user_data.get("tolov")}$\n"
                         f"‍💻 Kasbi:{user_data.get("kasbi")}\n"
                         f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                         f"🔎 Maqsad:{message.text}"
                         )
    await message.answer(result_text, reply_markup=keyword)
    await message.answer("Barcha ma'lumot to'g'ri kirtildimi")
    await state.clear()


@dp.message(Sherik.maqsad)
async def get_city(message: Message, state: FSMContext):
    username = message.from_user.username
    await state.update_data(user=username)
    user_data = await  state.get_data()
    keyword = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="send_result1"), InlineKeyboardButton(text="yo'q", callback_data="cancel1")]
        ]
    )
    await message.answer(text="barcha ma'lumot to'g'ri kiritildimi")
    result_text = ( f"✅ SHERIK KERAK!\n\n"
                         f"👤 Ism: {user_data['name']}\n"
                         # f"🎂 Yosh: {user_data.get('age')}\n"
                         f"📚 Texnoligiya:{user_data.get("texnoliya")}\n"
                         f"👤Telegram: {user_data.get("user")}\n"
                         f"📞 Aloqa:{user_data.get("aloqa")}\n"
                         f"🌆 Hudud: {user_data.get("hudud")}\n"
                         f"💰 Narx: {user_data.get("tolov")}$\n"
                         f"‍💻 Kasbi:{user_data.get("kasbi")}\n"
                         f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                         f"🔎 Maqsad:{message.text}"
                         )
    await message.answer(result_text, reply_markup=keyword)
    await state.clear()


@dp.message(Xodim.qoshimcha)
async def get_qoshimcha(message: Message, state: FSMContext):
    username = message.from_user.username
    await state.update_data(user=username)
    user_data = await  state.get_data()
    keyword = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="send_result3"), InlineKeyboardButton(text="yo'q", callback_data="cancel3")]
        ]
    )
    await message.answer(text="barcha ma'lumot to'g'ri kiritildimi")
    result_text = ( f"✅ SHERIK KERAK!\n\n"
                         f"🏢 Idora: {user_data['iroda']}\n"                                   
                         # f"🎂 Yosh: {user_data.get('age')}\n"
                         f"📚 Texnoligiya:{user_data.get("texnologiya")}\n"
                         f"👤Telegram: {user_data.get("user")}\n"
                         f"📞 Aloqa:{user_data.get("aloqa")}\n"
                         f"🌆 Hudud: {user_data.get("hudud")}\n"
                         f"✍️ Mas'ul: {user_data.get("masul")}\n"
                         f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                         f"🕰 Ish vaqti: {user_data.get("ish_vaqt")}\n"
                         f"💰 Moash: {user_data.get("moash")}$\n"
                         f"‍‼️ Qo`shimcha:{user_data.get("qoshimcha")}\n\n"
                        # f"👤 Ism: {user_data['name']}\n"
                        #  f"🎂 Yosh: {user_data.get('age')}\n"
                        #  f"📚 Texnoligiya:{user_data.get("texnoliya")}\n"
                        #  f"👤Telegram: {user_data.get("user")}\n"
                        #  f"📞 Aloqa:{user_data.get("aloqa")}\n"
                        #  f"🌆 Hudud: {user_data.get("hudud")}\n"
                        #  f"💰 Narx: {user_data.get("tolov")}$\n"
                        #  f"‍💻 Kasbi:{user_data.get("kasbi")}\n"
                        #  f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                        #  f"🔎 Maqsad:{message.text}"
                         "#ishjoyi"
                         )
    await message.answer(result_text, reply_markup=keyword)
    await state.clear()

@dp.message(Ustoz.maqsad)
async def get_qoshimcha(message: Message, state: FSMContext):
    username = message.from_user.username
    await state.update_data(user=username)
    user_data = await  state.get_data()
    keyword = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="send_result3"), InlineKeyboardButton(text="yo'q", callback_data="cancel3")]
        ]
    )
    await message.answer(text="barcha ma'lumot to'g'ri kiritildimi")
    result_text = ( f"✅ Uztoz Kerak!\n\n"
                         f"🎓 Shogird: {user_data['name']}\n"                                   
                         f"🎂 Yosh: {user_data.get('age')}\n"
                         f"📚 Texnoligiya:{user_data.get("texnologiya")}\n"
                         f"👤Telegram: {user_data.get("user")}\n"
                         f"📞 Aloqa:{user_data.get("aloqa")}\n"
                         f"🌆 Hudud: {user_data.get("hudud")}\n"
                         # f"✍️ Mas'ul: {user_data.get("masul")}\n"
                         # f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                         # f"🕰 Ish vaqti: {user_data.get("ish_vaqt")}\n"
                         f""
                         f"💰 Narxi: {user_data.get("tolov")}$\n"
                         f"‍🔎 Maqsad:{user_data.get("maqsad")}\n\n"
                         "#shogird"
                         )
    await message.answer(result_text, reply_markup=keyword)
    await state.clear()

@dp.message(Shogird.maqsad)
async def get_qoshimcha(message: Message, state: FSMContext):
    username = message.from_user.username
    await state.update_data(user=username)
    user_data = await  state.get_data()
    keyword = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="send_result4"), InlineKeyboardButton(text="yo'q", callback_data="cancel4")]
        ]
    )
    await message.answer(text="barcha ma'lumot to'g'ri kiritildimi")
    result_text = ( f"✅ Shogird Kerak!\n\n"
                         f"🎓 Uztoz: {user_data['name']}\n"                                   
                         f"🎂 Yosh: {user_data.get('age')}\n"
                         f"📚 Texnoligiya:{user_data.get("texnologiya")}\n"
                         f"👤Telegram: {user_data.get("user")}\n"
                         f"📞 Aloqa:{user_data.get("aloqa")}\n"
                         f"🌆 Hudud: {user_data.get("hudud")}\n"
                         # f"✍️ Mas'ul: {user_data.get("masul")}\n"
                         f"🕰 Murojaat qilish vaqti:{user_data.get("murojat")}\n"
                         # f"🕰 Ish vaqti: {user_data.get("ish_vaqt")}\n"
                         f"💰 Narxi: {user_data.get("tolov")}$\n"
                         f"‍🔎 Maqsad:{user_data.get("maqsad")}\n\n"
                         "#shogird"
                         )
    await message.answer(result_text, reply_markup=keyword)
    await state.clear()

# 📌 "Ha" tugmasi bosilganda ma'lumotlarni boshqa Telegramga yuborish
@dp.callback_query(lambda callback: callback.data == "send_result3")
async def send_result(callback):
    result_text = callback.message.text  # Foydalanuvchining barcha ma’lumotlari

    url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": result_text})

    if response.status_code == 200:
        await callback.message.answer("✅ Ma’lumot yuborildi!")
    else:
        await callback.message.answer("❌ Xatolik yuz berdi, qayta urinib ko‘ring.")

    await callback.answer()

# 📌 "Yo‘q" tugmasi bosilganda bekor qilish
@dp.callback_query(lambda callback: callback.data == "cancel3")
async def cancel_result(callback):
    await callback.message.answer("❌ Ma’lumot yuborilmadi, qayta tahrirlashingiz mumkin.")
    await callback.answer()

# response = requests.post(url=url, data={"chat_id": chat_id, "text": get_city})

# 📌 "Ha" tugmasi bosilganda ma'lumotlarni boshqa Telegramga yuborish
@dp.callback_query(lambda callback: callback.data == "send_result")
async def send_result(callback):
    result_text = callback.message.text  # Foydalanuvchining barcha ma’lumotlari

    # # Telegram API orqali boshqa chatga yuborish
    # url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    # response = requests.post(url, data={"chat_id": chat_id, "text": result_text})
    #
    # if response.status_code == 200:
    #     await callback.message.answer("✅ Ma’lumot yuborildi!")
    # else:
    #     await callback.message.answer(response.reason)
    # # await bot.send_message(chat_id=chat_id, text=result_text)
    #
    # await callback.answer()


    # Telegram API orqali boshqa chatga yuborish
    url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": result_text})

    if response.status_code == 200:
        await callback.message.answer("✅ Ma’lumot yuborildi!")
    else:
        await callback.message.answer("❌ Xatolik yuz berdi, qayta urinib ko‘ring.")

    await callback.answer()

# 📌 "Yo‘q" tugmasi bosilganda bekor qilish
@dp.callback_query(lambda callback: callback.data == "cancel")
async def cancel_result(callback):
    await callback.message.answer("❌ Ma’lumot yuborilmadi, qayta tahrirlashingiz mumkin.")
    await callback.answer()


@dp.callback_query(lambda callback: callback.data == "send_result1")
async def send_result(callback):
    result_text = callback.message.text  # Foydalanuvchining barcha ma’lumotlari

    # Telegram API orqali boshqa chatga yuborish
    url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": result_text})

    if response.status_code == 200:
        await callback.message.answer("✅ Ma’lumot yuborildi!")
    else:
        await callback.message.answer("❌ Xatolik yuz berdi, qayta urinib ko‘ring.")

    await callback.answer()

# 📌 "Yo‘q" tugmasi bosilganda bekor qilish
@dp.callback_query(lambda callback: callback.data == "cancel1")
async def cancel_result(callback):
    await callback.message.answer("❌ Ma’lumot yuborilmadi, qayta tahrirlashingiz mumkin.")
    await callback.answer()


@dp.callback_query(lambda callback: callback.data == "send_result3")
async def send_result(callback):
    result_text = callback.message.text  # Foydalanuvchining barcha ma’lumotlari

    # Telegram API orqali boshqa chatga yuborish
    url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": result_text})

    if response.status_code == 200:
        await callback.message.answer("✅ Ma’lumot yuborildi!")
    else:
        await callback.message.answer("❌ Xatolik yuz berdi, qayta urinib ko‘ring.")

    await callback.answer()

# 📌 "Yo‘q" tugmasi bosilganda bekor qilish
@dp.callback_query(lambda callback: callback.data == "cancel3   ")
async def cancel_result(callback):
    await callback.message.answer("❌ Ma’lumot yuborilmadi, qayta tahrirlashingiz mumkin.")
    await callback.answer()

@dp.callback_query(lambda callback: callback.data == "send_result4")
async def send_result(callback):
    result_text = callback.message.text  # Foydalanuvchining barcha ma’lumotlari

    # Telegram API orqali boshqa chatga yuborish
    url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": result_text})

    if response.status_code == 200:
        await callback.message.answer("✅ Ma’lumot yuborildi!")
    else:
        await callback.message.answer("❌ Xatolik yuz berdi, qayta urinib ko‘ring.")

    await callback.answer()

# 📌 "Yo‘q" tugmasi bosilganda bekor qilish
@dp.callback_query(lambda callback: callback.data == "cancel4")
async def cancel_result(callback):
    await callback.message.answer("❌ Ma’lumot yuborilmadi, qayta tahrirlashingiz mumkin.")
    await callback.answer()

async def main():
    # await catch_commend()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
