from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '6807340372:AAG0aXi2JwDkb1ewyxZax98iivmU_8GGHXs'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Словари для текста кнопок
LEXICON = {
  'main_menu': 'Главное меню',
  'proverb': 'Написать пословицу',
  'message': 'Напечатать сообщение',
  'back_to_main': 'Вернуться в главное меню',
  'but_1': 'Кнопка 1',
  'but_2': 'Кнопка 2',
  'but_3': 'Кнопка 3',
  'but_4': 'Кнопка 4',
  'but_5': 'Кнопка 5',
  'but_6': 'Кнопка 6',
  'but_7': 'Кнопка 7',
  'but_8': 'Кнопка 8',
  'but_9': 'Кнопка 9',
  'but_10': 'Кнопка 10',
  'but_11': 'Кнопка 11',
}

# Функция для генерации инлайн-клавиатур
def create_inline_kb(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
  kb_builder = InlineKeyboardBuilder()
  buttons = []
  if args:
    for button in args:
      buttons.append(InlineKeyboardButton(
        text=LEXICON.get(button, button),
        callback_data=button
      ))
  if kwargs:
    for button, text in kwargs.items():
      buttons.append(InlineKeyboardButton(
        text=text,
        callback_data=button
      ))
  kb_builder.row(*buttons, width=width)
  return kb_builder.as_markup()

# Главное меню (5 кнопок)
@dp.message(CommandStart())
async def process_start_command(message: Message):
  main_menu_keyboard = create_inline_kb(
    5,
    'but_1',
    'but_2',
    'but_3',
    'but_4',
    'but_5'
  )
  await message.answer(
    text='Выберите действие:',
    reply_markup=main_menu_keyboard
  )

# Обработчик нажатия на кнопки главного меню
@dp.callback_query(lambda c: c.data in ['but_1', 'but_2', 'but_3', 'but_4', 'but_5'])
async def handle_main_menu_button(call: types.CallbackQuery):
  await call.answer()
  await call.message.edit_text(
    text=f'Вы выбрали кнопку: {LEXICON.get(call.data, call.data)}',
    reply_markup=create_inline_kb(
      3,
      'back_to_main',
      'proverb',
      'message'
    )
  )

# Обработчик нажатия на "Вернуться в главное меню"
@dp.callback_query(lambda c: c.data == 'back_to_main')
async def handle_back_to_main(call: types.CallbackQuery):
  await call.answer()
  await call.message.edit_text(
    text='Вы вернулись в главное меню.',
    reply_markup=create_inline_kb(
      5,
      'but_1',
      'but_2',
      'but_3',
      'but_4',
      'but_5'
    )
  )

# Обработчик нажатия на "Написать пословицу"
@dp.callback_query(lambda c: c.data == 'proverb')
async def handle_proverb(call: types.CallbackQuery):
  await call.answer()
  await call.message.edit_text(
    text='Введите пословицу:',
    reply_markup=create_inline_kb(
      1,
      'back_to_main'
    )
  )

# Обработчик нажатия на "Напечатать сообщение"
@dp.callback_query(lambda c: c.data == 'message')
async def handle_message(call: types.CallbackQuery):
  await call.answer()
  await call.message.edit_text(
    text='Введите сообщение:',
    reply_markup=create_inline_kb(
      1,
      'back_to_main'
    )
  )

if __name__ == '__main__':
    dp.run_polling(bot)