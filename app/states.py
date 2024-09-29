from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    name = State()
    age = State()
