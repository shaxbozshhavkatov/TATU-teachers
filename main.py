shaxboz='5706025375:AAFbMXtw754wyEDqBH0SnZHrMvka9tKHVCs'

from random import randint
from aiogram import Bot, Dispatcher, executor, types
from keyboard1 import *
from aiogram.utils.exceptions import *




from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot=Bot(token=shaxboz)
dp=Dispatcher(bot)




@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Salom {message.from_user.first_name}  TATU Samarqand Filiali botiga xush kelibsiz:",reply_markup=keyboard)

@dp.errors_handler(exception= BotBlocked)
async def errorbot(update:types.Update,exception:BotBlocked):
    return True 

@dp.message_handler(commands='Oqituvchilar')
async def vote(message:types.Message):
    await message.answer("👇🏻",reply_markup=keyboard2)

@dp.message_handler()
async def keyboard_answer(message:types.Message):
    if message.text=="Pirimova":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Pirimova",reply_markup=keyboard3)
        
    elif message.text=="Shokirov":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Shokirov",reply_markup=keyboard4)

    elif message.text=="Shodmonov":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Shodmonov",reply_markup=keyboard5)

    elif message.text=="Xo`jayorov":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Xo`jayorov",reply_markup=keyboard6)

    elif message.text=="Jiyanov":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Jiyanov",reply_markup=keyboard7)

    elif message.text=="Xolmatov":
        file=open("main.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Xolmatov",reply_markup=keyboard8)


@dp.callback_query_handler(text=["dars","lavozim"])
async def start(call:types.CallbackQuery):
    if call.data=="dars":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard9)
    elif call.data=="lavozim":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")
   

@dp.callback_query_handler(text=["dars1","lavozim1"])
async def start(call:types.CallbackQuery):
    if call.data=="dars1":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard10)
    elif call.data=="lavozim1":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")


@dp.callback_query_handler(text=["dars2","lavozim2"])
async def start(call:types.CallbackQuery):
    if call.data=="dars2":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard11)
    elif call.data=="lavozim2":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")
    


@dp.callback_query_handler(text=["dars3","lavozim3"])
async def start(call:types.CallbackQuery):
    if call.data=="dars3":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard12)
    elif call.data=="lavozim3":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")
       

@dp.callback_query_handler(text=["dars4","lavozim4"])
async def start(call:types.CallbackQuery):
    if call.data=="dars4":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard13)
    elif call.data=="lavozim4":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")
       

@dp.callback_query_handler(text=["dars5","lavozim5"])
async def start(call:types.CallbackQuery):
    if call.data=="dars5":
        await call.message.answer("guruhni tanlang",reply_markup=keyboard14)
    elif call.data=="lavozim5":
        file=open("main1.jpg","rb")
        await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="lavozim")
        


@dp.callback_query_handler(text=["guruh","guruh1","guruh2"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard15)
    elif call.data=="guruh1":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard16)
    elif call.data=="guruh2":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard17)

@dp.callback_query_handler(text=["guruh3","guruh4","guruh5"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh3":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard18)
    elif call.data=="guruh4":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard19)
    elif call.data=="guruh5":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard20)


@dp.callback_query_handler(text=["guruh6","guruh7","guruh8"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh6":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard21)
    elif call.data=="guruh7":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard22)
    elif call.data=="guruh8":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard23)


@dp.callback_query_handler(text=["guruh9","guruh10","guruh11"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh9":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard24)
    elif call.data=="guruh10":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard25)
    elif call.data=="guruh11":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard26)


@dp.callback_query_handler(text=["guruh12","guruh13","guruh14"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh12":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard27)
    elif call.data=="guruh13":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard28)
    elif call.data=="guruh14":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard29)

@dp.callback_query_handler(text=["guruh15","guruh16","guruh17"])
async def start(call:types.CallbackQuery):
    if call.data=="guruh15":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard30)
    elif call.data=="guruh16":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard31)
    elif call.data=="guruh17":
        await call.message.answer("hafta kunini tanlang",reply_markup=keyboard32)


# @dp.message_handler(commands='link')

@dp.callback_query_handler(text=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba1","Seshanba1","Chorshanba1","Payshanba1","Juma1","Shanba1"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba1":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba1":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba1":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba1":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma1":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba1":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba2","Seshanba2","Chorshanba2","Payshanba2","Juma2","Shanba2"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba2":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba2":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba2":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba2":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma2":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba2":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba3","Seshanba3","Chorshanba3","Payshanba3","Juma3","Shanba3"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba3":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba3":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba3":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba3":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma3":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba3":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')


@dp.callback_query_handler(text=["Dushanba4","Seshanba4","Chorshanba4","Payshanba4","Juma4","Shanba4"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba4":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba4":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba4":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba4":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma4":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba4":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')


@dp.callback_query_handler(text=["Dushanba5","Seshanba5","Chorshanba5","Payshanba5","Juma5","Shanba5"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba5":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba5":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba5":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba5":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma5":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba5":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba6","Seshanba6","Chorshanba6","Payshanba6","Juma6","Shanba6"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba6":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba6":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba6":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba6":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma6":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba6":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba6","Seshanba6","Chorshanba6","Payshanba6","Juma6","Shanba6"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba6":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba6":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba6":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba6":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma6":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba6":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba7","Seshanba7","Chorshanba7","Payshanba7","Juma7","Shanba7"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba7":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba7":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba7":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba7":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma7":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba7":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba8","Seshanba8","Chorshanba8","Payshanba8","Juma8","Shanba8"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba8":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba8":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba8":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba8":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma8":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba8":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')




@dp.callback_query_handler(text=["Dushanba8","Seshanba8","Chorshanba8","Payshanba8","Juma8","Shanba8"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba8":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba8":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba8":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba8":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma8":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba8":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')


@dp.callback_query_handler(text=["Dushanba8","Seshanba8","Chorshanba8","Payshanba8","Juma8","Shanba8"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba8":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba8":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba8":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba8":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma8":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba8":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba8","Seshanba8","Chorshanba8","Payshanba8","Juma8","Shanba8"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba8":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba8":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba8":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba8":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma8":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba8":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')

@dp.callback_query_handler(text=["Dushanba8","Seshanba8","Chorshanba8","Payshanba8","Juma8","Shanba8"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba8":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba8":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba8":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba8":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma8":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba8":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba9","Seshanba9","Chorshanba9","Payshanba9","Juma9","Shanba9"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba9":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba9":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba9":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba9":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma9":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba9":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba9","Seshanba9","Chorshanba9","Payshanba9","Juma9","Shanba9"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba9":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba9":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba9":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba9":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma9":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba9":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')




@dp.callback_query_handler(text=["Dushanba10","Seshanba10","Chorshanba10","Payshanba10","Juma10","Shanba10"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba10":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba10":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba10":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba10":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma10":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba10":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba10","Seshanba10","Chorshanba10","Payshanba10","Juma10","Shanba10"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba10":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba10":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba10":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba10":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma10":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba10":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba11","Seshanba11","Chorshanba11","Payshanba11","Juma11","Shanba11"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba11":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba11":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba11":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba11":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma11":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba11":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')




@dp.callback_query_handler(text=["Dushanba12","Seshanba12","Chorshanba12","Payshanba12","Juma12","Shanba12"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba12":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba12":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba12":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba12":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma12":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba12":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



@dp.callback_query_handler(text=["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba12":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba12":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba12":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba12":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma12":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba12":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')





@dp.callback_query_handler(text=["Dushanba13","Seshanba13","Chorshanba13","Payshanba13","Juma13","Shanba13"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba13":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba13":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba13":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba13":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma13":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba13":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')





@dp.callback_query_handler(text=["Dushanba14","Seshanba14","Chorshanba14","Payshanba14","Juma14","Shanba14"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba14":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba14":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba14":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba14":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma14":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba14":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')





@dp.callback_query_handler(text=["Dushanba15","Seshanba15","Chorshanba15","Payshanba15","Juma15","Shanba15"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba15":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba15":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba15":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba15":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma15":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba15":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')




@dp.callback_query_handler(text=["Dushanba16","Seshanba16","Chorshanba16","Payshanba16","Juma16","Shanba16"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba16":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba16":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba16":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba16":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma16":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba16":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')





@dp.callback_query_handler(text=["Dushanba17","Seshanba17","Chorshanba17","Payshanba17","Juma17","Shanba17"])
async def start(call:types.CallbackQuery):
    if call.data=="Dushanba17":
        await call.message.answer('''1.Geografiya
2.Biologiya
3.Ingliz tili
4.CHQBT
5.Ona tili
6.O'zbekiston tarixi''')
    elif call.data=="Seshanba17":
        await call.message.answer('''1.Algebra
2.Geometriya
3.tarbiya
4.Ingliz tili
5.Fizika
6.Kimyo''')
    elif call.data=="Chorshanba17":
        await call.message.answer('''1.Jahon Tarixi 
2.Geometriya
3.Algebra
4.Informatika
5.Informatika
6.Kimyo''')
    elif call.data=="Payshanba17":
        await call.message.answer('''1.Algebra
2.Biologiya
3.Jismoniy tarbiya
4.Ingliz tili
5.Adabiyot
6.Fizika''')
    elif call.data=="Juma17":
        await call.message.answer('''1.sinf soat
2.Geografiya
3.Jismoniy tarbiya
4.Rus tili''')
    elif call.data=="Shanba17":
        await call.message.answer('''1.Ona tili
2.Adabiyot
3.Rus tili
4.Huquq''')



# async def start(message:types.Message):
#     await message.answer("How are you.....",reply_markup=keyboard)


# @dp.message_handler(commands='vote')
# async def vote(message:types.Message):
#     file=open("main.jpg","rb")
#     await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="hdwbka",reply_markup=keyboard3)

   # photo="https://images.pexels.com/photos/3441201/pexels-photo-3441201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",




# @dp.message_handler(commands='video')
# async def vote(message:types.Message):
#     file=open("new1.MOV","rb")
#     await bot.send_video(chat_id=message.from_user.id,video=file)

# @dp.message_handler()
# async def keyboard_answer(message:types.Message):
#     if message.text=="O`zbekiston":
#         await message.answer("o`zbekiston",reply_markup=keyboard5)

# @dp.callback_query_handler(text=["poytaxt"])
# async def start(call:types.CallbackQuery):
#     if call.data=="poytaxt":
#         await call.message.answer("poytaxt:toshkent")
          

# @dp.callback_query_handler(text=["bayroq"])
# async def start(call:types.CallbackQuery):
#     if call.data=="bayroq":
#         file=open("O`zbekiston.jpg","rb")
#         await bot.send_photo(chat_id=call.from_user.id,photo=file,caption="O`zbekiston Bayrog`i")    
                



# @dp.message_handler()
# async def keyboard_answer(message:types.Message):
#     if message.text=="Qirg`iziston":
#         await message.answer("Qirg`iziston",reply_markup=keyboard6)
        
# @dp.callback_query_handler(text=["poytaxt"])
# async def start(call:types.CallbackQuery):
#     if call.data=="poytaxt1":
#         await call.message.answer("poytaxt:Bishkek")
          

# @dp.callback_query_handler(text=["bayroq"])
# async def start(call:types.CallbackQuery):
#     if call.data=="bayroq1":
#         file=open("Qirg`iziston.jpg","rb")
#         await bot.send_photo(chat_id=call.from_user.id,photo=file,caption="Qirg`iziston Bayrog`i")   



    # if message.text=="rossiya":
    #     file=open("rossiya.jpg","rb")
    #     await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="rossiya Bayrog`i")
    #     await message.answer("poytaxti:moskva")




    # elif message.text=="Aqsh":
    #     file=open("aqsh.png","rb")
    #     await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Aqsh Bayrog`i")
    #     await message.answer("poytaxti:Washington")
        

    # elif message.text=="Tojikiston":
    #     file=open("tojikiston.jpg","rb")
    #     await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Tojikiston Bayrog`i")
    #     await message.answer("poytaxti:Dushanbe")



    # elif message.text=="Sweden":
    #     file=open("sweden.jpg","rb")
    #     await bot.send_photo(chat_id=message.from_user.id,photo=file,caption="Sweden Bayrog`i")
    #     await message.answer("poytaxti:stocholm")


# s=0
# a=0
# @dp.callback_query_handler()
# async def vote_call(callback:types.CallbackQuery):

#     if callback.data=="like":
#         global s
#         s+=1
#         await callback.message.edit_caption(f"likelar soni:{s}",reply_markup=keyboard3)
#     elif callback.data=="dislike":
#         global a
#         a+=1
#         await callback.message.edit_caption(f"dislikelar soni:{a}",reply_markup=keyboard3)











if __name__=="__main__":
    executor.start_polling(dp)