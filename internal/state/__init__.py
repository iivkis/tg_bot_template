from aiogram.fsm.state import State, StatesGroup

# class ExapleState(StatesGroup):
#     set_example = State()


class MailingState(StatesGroup):
    set_text = State()
    start_mailing = State()
