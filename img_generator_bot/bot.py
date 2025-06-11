import telebot
from logic import FusionBrainAPI
from config import TOKEN, API_KEY, SECRET_KEY

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Обработчик стартового сообщения
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши, какую картинку ты хочешь создать, и я сделаю её для тебя.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text

    # Используем FusionBrainAPI для генерации изображения
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    pipeline_id = api.get_pipeline()
    uuid = api.generate(prompt, pipeline_id)
    files = api.check_generation(uuid)[0]
    
    # Сохраняем изображение на диск
    api.save_image(files, "generated_image.jpg")


    # Отправляем изображение пользователю
    with open("generated_image.jpg", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

# Запуск бота
bot.polling()