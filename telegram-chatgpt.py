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

# Check if message starts with @admin tag
@bot.message_handler(text_startswith="@admin")
def start_filter(message):
    bot.send_message(message.chat.id, "Looks like you are calling admin, wait...")

# Check if text is hi or hello
@bot.message_handler(text=['hi','hello'])
def text_filter(message):
    bot.send_message(message.chat.id, "Hi, {name}!".format(name=message.from_user.first_name))

# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())

bot.infinity_polling()
