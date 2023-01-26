from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import HELP
from tgbot.handlers.onboarding.static_text import github_button_text, ask_for_help_button_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(github_button_text, url="https://github.com/ohld/django-telegram-bot"),
        InlineKeyboardButton(ask_for_help_button_text, callback_data=f'{HELP}')
    ]]

    return InlineKeyboardMarkup(buttons)
