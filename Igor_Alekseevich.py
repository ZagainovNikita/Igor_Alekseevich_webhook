from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
import json
abc = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
ops = '+-/*'
nums = '1234567890'
bot_name = '@kurakin_igor_bot'
even = 'УуЕеЫыАаОоЭэЯяИиЮюЁё'
cmds = ['/start', '/help', '/lecture', '/outrage', '/solve', '/dickify', '/dialogue', '/mirrorleft', '/mirrorright']
keywords = ['@kurakin_igor_bot'] + cmds + list(map(lambda x: x + '@kurakin_igor_bot', cmds))
token = '5919598868:AAGkH6FcvNHnzq95Ddqm3mkRfoAEW_w7SIQ'
base_url = 'https://api.telegram.org/bot'
proxy_url = 'http://proxy.com:8585'
# Настройка Webhook
WEBHOOK_HOST = 'https://0081-2a02-2698-242b-230-35ff-13c7-ae9e-fd70.ngrok-free.app' # -> Адрес сервера
WEBHOOK_PATH = ''# -> Путь до api, где слушает бот
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}' # -> URL на который будут приниматься запросы

# Настройка web-сервера
WEBAPP_HOST = '127.0.0.1' # -> хост нашего приложения, оставляем локальным
WEBAPP_PORT = 5000 # -> port на котором работает наше приложение

bot = Bot(token = token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

def read():
    import random as r
    f = open(r'1.txt', encoding = 'UTF-8')
    info = list(map(lambda x: x.strip().strip('\ufeff'), f.readlines()))
    return r.choice(info)
def outrage():
    import random as r
    f = open(r'2.txt', encoding = 'UTF-8')
    info = list(map(lambda x: x.strip().strip('\ufeff'), f.readlines()))
    return r.choice(info)
########################################################################################
@dp.message_handler(commands = 'start')
async def begin(message: types.Message):
    await message.reply('Я готов к работе для школы!')
@dp.message_handler(commands = 'help')
async def tell_funcs(message: types.Message):
    await bot.send_message(message.chat.id, \
                           'Я могу отвечать на такие команды:\n' + '\n'.join(cmds))
@dp.message_handler(commands = 'lecture')
async def lecture(message: types.Message):
        #await bot.send_message(message.chat.id, read())
        await message.reply(read())
@dp.message_handler(commands = 'outrage')
async def bully(message: types.Message):
        #await bot.send_message(message.chat.id, f'{message.from_user.first_name} {outrage()}')
        await message.reply(f'{message.from_user.first_name} {outrage()}')
@dp.message_handler(commands = 'solve')
async def solve(message: types.Message):
    if message.text == '/solve' or message.text == '/solve@test_n0_bot':

        await message.reply('Я решу твою задачу!\n\
Введи формулу из 3 различных переменных, а затем \
через запятую введи 2 переменые и их значения из \
правой части уравнения, а я мгновенно посчитаю значние третьей.\n\
Пример ввода:\n\
/solve I = U / R, U = 120, R = 30\n\
Пример вывода:\n\
4')
    else:
        txt = message.text[6:]
        if bot_name in txt:
            txt = txt[12:]
        d = {}
        op = None
        to_fill = None
        value = None
        i = 0
        first = None
        second = None
        solved = False

        try:
            while i < len(txt):

                if txt[i] != ' ' and txt[i] != '=':

                    if txt[i] in abc:
                        if d.get(txt[i],-1) == -1:
                            d[txt[i]] = 0
                        else:
                            if not first:
                                first = txt[i]
                            else:
                                second = txt[i]
                            to_fill = txt[i]
                    elif txt[i] in ops:
                        op = txt[i]
                    elif txt[i] in nums:
                        if value:
                            value = value*10 + int(txt[i])
                        else:
                            value = int(txt[i])
                    elif value and to_fill:
                        d[to_fill] = value
                        value = None
                        to_fill = None

                i += 1
            if value and to_fill:
                d[to_fill] = value
            if op and first and second:
                if op == '+':
                    await message.reply(f'{d[first]+d[second]}')
                    solved = 1
                if op == '-':
                    await message.reply(f'{d[first]-d[second]}')
                    solved = 1
                if op == '*':
                    await message.reply(f'{d[first]*d[second]}')
                    solved = 1
                if op == '/':
                    await message.reply(f'{d[first]/d[second]}')
                    solved = 1
            if not solved:
                await message.reply('Неверный формат ввода. \
Попробуй еще раз')
        except ZeroDivisionError:
            await message.reply('Я не делю на ноль')
        except:
            await message.reply('Неверный формат ввода. \
Попробуй еще раз')
@dp.message_handler(commands = 'dickify')
async def dick(message: types.Message):
    txt = message.text
    flg = True
    flg2 = True
    ans = []
    if txt in keywords:
        flg = False
        flg2 = False
        await message.reply('Напиши мне сообщиние, а я его ХУЕФИЦИРУЮ!\nПример ввода:\n/dickificky Привет мир!\nПример вывода:\nХуепривет Хуемир!')
    elif len(txt) > 1000:
        flg = False
    elif flg:
        a = txt.split()
        for i in range(len(a)):
            if a[i] in keywords:
                pass
            else:
                word = a[i]
                for j in word:
                    if j in abc:
                        flg = False
                        break

                for j in range(len(word)):
                    if word[j] not in even:
                        if len(word)-j >=3:
                            ans += ['Хуе' + word[j:].lower()]
                        else:
                            ans += [word.lower()]
                        break
    if flg:
        await message.reply(' '.join(ans))
    elif flg2:
        await message.reply('Найдены недопустимые символы или превышен лимит длины сообщения')
@dp.message_handler(commands = 'dialogue')
async def talk(message: types.Message):
    import random as r
    ans_length = r.choice(list(range(15,26)))
    txt = message.text.lower()
    word_bag = list(map(lambda x: x.lower().strip('.').strip('!').strip('?').strip(':').strip(','), txt.split()))
    for i in range(min(2,len(word_bag))):
        if word_bag[0] in keywords:
            word_bag = word_bag[1:]
    with open('word_store.json','r', encoding = 'UTF-8') as f:
        info = json.loads(f.read())
    for i in range(len(word_bag)-1):
        if len(word_bag[i]) < 15 and len(word_bag[i+1]) < 15:
            if word_bag[i] not in info:
                info[word_bag[i]] = []
            info[word_bag[i]] += [word_bag[i+1]]
            info[word_bag[i]] = list(set(info[word_bag[i]]))
    with open('word_store.json','w', encoding = 'UTF-8') as f:
        f.write(json.dumps(info, ensure_ascii=0))
    ans = []
    if len(word_bag) > 0:
        if word_bag[-1] in info:
            cur_word = r.choice(info[word_bag[-1]])
        else:
            cur_word = r.choice(list(info.keys()))
        r_state = r.randint(1,10)
        for i in range(ans_length):
            if cur_word in ans or r_state <= 1:
                cur_word = r.choice(list(info.keys()))
            ans += [cur_word]
            if cur_word in info:
                cur_word = r.choice(info[cur_word])
            else:
                cur_word = r.choice(list(info.keys()))
        if len(ans[0]) == 1:
            ans[0] = ans[0].upper()
        else:
            ans[0] = ans[0][0].upper() + ans[0][1:]
        if len(ans) > 0:
            await message.reply(' '.join(ans))
    if txt in keywords:
        await message.reply('Давай поговорим!\nПример ввода:\n/dialogue Привет мир!')
@dp.message_handler(content_types=['photo'])
async def get_photo(msg : types.Message):
    img = await bot.get_file(msg['photo'][-1]['file_id'])
    file = await bot.download_file(img.file_path)

    await msg.photo[-1].download(r'\photos\image.jpg')
@dp.message_handler(commands='mirrorleft')
async def mirror1(msg : types.Message):
    from PIL import Image
    with Image.open(r'\photos\image.jpg') as img:
        img.load()
        half = img.crop((0,0,img.size[0]//2,img.size[1]))
        half = half.transpose(Image.FLIP_LEFT_RIGHT)
        img.paste(half, (img.size[0]//2, 0))
        img.save(r'\photos\mirror.jpg')
    await msg.reply_photo(open(r'\photos\mirror.jpg', 'rb'))
@dp.message_handler(commands='mirrorright')
async def mirror2(msg : types.Message):
    from PIL import Image
    with Image.open(r'\photos\image.jpg') as img:
        img.load()
        half = img.crop((img.size[0]//2,0,img.size[0],img.size[1]))
        half = half.transpose(Image.FLIP_LEFT_RIGHT)
        img.paste(half, (0, 0))
        img.save(r'\photos\mirror.jpg')
    await msg.reply_photo(open(r'\photos\mirror.jpg', 'rb'))
if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
