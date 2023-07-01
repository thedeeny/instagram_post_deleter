import time
from instabot import Bot
import my_config
import random

bot = Bot()
bot.login(username=YOUR_USERNAME, password=YOUR_PASSWORD) # fill in your username and password for instagram

medias = bot.get_total_user_medias(bot.user_id)

for media in medias:
    try:
        bot.delete_media(media)
        print("deleted media")
        time.sleep(random.randint(5, 15))
    except:
        print("error")
        time.sleep(random.randint(100, 200))                                                                                       
