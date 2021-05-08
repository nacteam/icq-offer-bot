from api.bot import Bot
import asyncio

TOKEN = "***.**********.**********:*********"
CHAT = "**********@chat.agent"
bot = Bot(token=TOKEN)

replics = {
  "start": "Привет! С помощью этого бота ты можешь отправить материал в предложку каналов Night Admin Community!\nРазработчик: @night_admin\nНажми кнопку ниже для добавления поста в очередь рассмотрения.",
  "startInline": "[{}]".format(json.dumps([{"text": "Отправить пост", "callbackData": "post"}]),
  "post": '''Отлично! Теперь выбери канал для публикации из списка ниже. Просто введи его название без лишних символов:
  Андроид (канал про Android OS), Социопат (мемы), Котики, Экология.
  Не нашли нужный канал или хотите создать новый? Напишите "/new Название канала <Enter> Краткое описание" без кавычек, и мы добавим этот канал в список бота! Спасибо, что помогаешь нам!
  ''',
  "category_yes": "Почти всё готово! Теперь прикрепи картинку, текст или другой медиафайл одним сообщением. Только первое сообщение уйдёт в пост!",
  "nopost": "Упс... У нас нет такого канала. Проверь написание: отсутствие символов или опечатки. Введи только название канала, например: Социопат. Если считаешь, что необходимо создать новый канал, напиши боту '/new Название <Enter> Описание'!",
  "success": "Поздравляю! Твой пост успешно отправлен и скоро появится у нас на канале!",
  "postSuccess": "Пост {author} для канала {channel}:\n\n\n==================================\n\n{post}"
}

async def start_cb(event):
  await bot.send_text(chatId=event["fromChat"], text=replics["start"], inlineKeyboardMarkup=replics["startInline"])
async def post_cb(event):
  await bot.send_text(chatId=event["fromChat"], text=replics["post"])
  category = await bot.wait(event["payload"]["from"]["chatId"])
  category = category.replace(" ", "").lower()
  if category in categories:
    await bot.send_text(chatId=event["fromChat"], text=replics["category_yes"])
    post = await bot.wait(event["payload"]["from"]["chatId"])
    await bot.send_text(chatId=event["fromChat"], text=replics["success"])
    await bot.send_text(chatId=CHAT, text=replics["postSuccess"].format(author=event["payload"]["from"]["chatId"], channel=category, post = post))
  else:
    await bot.send_text(chatId=event["fromChat"], text=replics["nopost"])
                               
async def main():
  sociopath = []
  android = []
  cats = []
  eco = []
  await bot.add_handler(sociopath)
  await bot.add_handler(android)
  await bot.add_handler(cats)
  await bot.add_handler(eco)
    
