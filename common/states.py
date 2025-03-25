from aiogram.fsm.state import StatesGroup, State


class WaitingAuthStates(StatesGroup):
    waiting_for_phone = State()
    waiting_for_location = State()
    waiting_approve_city = State()
    waiting_role_state = State()

class ProfileChangesStates(StatesGroup):
    main_state = State()
    change_name = State()
    change_city = State()
    change_phone_number = State()
