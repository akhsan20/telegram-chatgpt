import telebot
import openai
from telebot import custom_filters

bot = telebot.TeleBot('YOUR API KEY telegram, chat whith @BotFather')
openai.api_key = "YOUR API KEY OPEN AI"

# Check if message starts with bot tag
@bot.message_handler(text_startswith="bot")
def start_filter(message):
    psn = message.text
    cmd = psn.split("bot ") 
    #chat gpt here
    model_engine = "text-davinci-003" #"text-davinci-002"
    prompt = (cmd[1])
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048, #max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message_gpt = completions.choices[0].text
    answer = message_gpt.strip()
    #end chat gpt
    bot.send_message(message.chat.id, answer) #send response

@bot.message_handler(text_startswith="img")
def start_filter(message):
    psn = message.text
    cmd = psn.split("img ")
    bot.send_message('893059', message.from_user.first_name + ' - ' + psn)
    #openai here
    response = openai.Image.create(
      prompt=cmd[1],
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    #end of openai 
    bot.send_photo(message.chat.id, image_url)

# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())

bot.infinity_polling()
