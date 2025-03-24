from aiogram.fsm.state import StatesGroup, State


class WaitingStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_location = State()
    waiting_approve_city = State()
    waiting_role_state = State()
