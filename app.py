from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Про нас')],
        [KeyboardButton(text='Наші послуги'), KeyboardButton(text='Ваша філія в ЄС')],
        [KeyboardButton(text='Ваша компанія в ЄС'), KeyboardButton(text='Ваш товар в ЄС')],
        [KeyboardButton(text='Умови надання консультацій')],
        [KeyboardButton(text='Контакти📞')],
    ]
)