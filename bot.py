import logging
import os

from aiogram import Bot, types, executor, Dispatcher

# from config import TOKEN 
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.answer(f'Привет, {user_name}! Я помогу тебе транслитировать ФИО с кириллицы на латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113. Напиши ФИО')
    logging.basicConfig(level='INFO', filename='py_test.log', format="%(levelname)s %(message)s")
    logging.info(f'user_id = {user_id} user_name = {user_name} text = {message.text}')

@dp.message_handler()
async def translit(message: types.Message):
    dict_translite = {
        'А':	'A',
        'Б':	'B',
        'В':	'V',
        'Г':	'G',
        'Д':	'D',
        'Е':	'E',
        'Ё':	'E',
        'Ж':	'ZH',
        'З':	'Z',
        'И':	'I',
        'Й':	'I',
        'К':	'K',
        'Л':	'L',
        'М':	'M',
        'Н':	'N',
        'О':	'O',
        'П':	'P',
        'Р':	'R',
        'С':	'S',
        'Т':	'T',
        'У':	'U',
        'Ф':	'F',
        'Х':	'KH',
        'Ц':	'TS',
        'Ч':	'CH',
        'Ш':	'SH',
        'Щ':	'SHCH',
        'Ы':	'Y',
        'Ъ':	'IE',
        'Э':	'E',
        'Ю':	'IU',
        'Я':	'IA',
        ' ':	' '}
    
    translite = ''.join(dict_translite[i] for i in message.text.upper() if i in dict_translite)
    await message.answer(translite)
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'user_id = {user_id} user_name = {user_name} text = {message.text}, answer = {translite}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)