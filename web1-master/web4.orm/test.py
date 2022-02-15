from models_holiday.db_session_holiday import global_init, create_session
from models_holiday.__all_models_holidays import *


global_init("sqlite:///db/holidays_studio.db")
session = create_session()
client = Client(full_name="Chelik 1", phone='5876876', email="ya_sobaka@ti_sobaka.com")
session.add(client)
session.commit()