from aiogram import Bot, Dispatcher
from sqlalchemy import types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bot_utils import handlers as hs
from config import TOKEN
from bot_utils.states import UserMessageState

redis_storage = RedisStorage2(host="localhost",port=6379)
bot = Bot(token=TOKEN)


dp = Dispatcher(bot, storage=redis_storage)

dp.register_message_handler(hs.welcome_message, commands=["start"])
dp.register_message_handler(hs.start_game, commands=["start_game"])
dp.register_message_handler(hs.finish_game, commands=["finish_game"])
dp.register_message_handler(hs.send_questions)

# Callback buttons handlers

dp.register_callback_query_handler(
    hs.start_with_category, 
    lambda c: str(c.data).startswith("category_") 
)