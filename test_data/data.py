import os
from dotenv import load_dotenv
from .users import User

load_dotenv()

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas'))
tmp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))


class ExpectedMessagesMOEX:
    iss_engines = 'engines'
    iss_securities = 'securities'
    iss_markets = 'markets'
    iss_boards = 'boards'
    iss_trades = 'trades'


class MoexDataVariables:
    engine_by_stock = 'stock'
    market_by_index = 'index'


class FileTypes:
    xml = 'xml'
    json = 'json'
    html = 'html'
    non_type = ''


class Method:
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class StatusCode:
    SUCCESS = 200


class MoexUrl:
    BASE_URL = 'https://iss.moex.com'
    SCHOOL_URL = 'https://school.moex.com/'


class MoexVariables:
    rus_text = 'Продукты и услуги'
    eng_text = 'Markets'
    auth_email = os.getenv('AUTHORIZATION_LOGIN')
    auth_password = os.getenv('AUTHORIZATION_PASSWORD')
    wrong_email = 'sdfsdf'
    wrong_password = 'sdfdsfsd'


class CoreEndpoints:
    ISS = '/iss'


class EngineEndpoints(CoreEndpoints):
    def __init__(self, add_first_node=None, add_sec_node=None):
        self.ENGINE_LIST = f'{super().ISS}/engines.'  # endpoint engine list
        self.MARKETS_LIST = f'{super().ISS}/engines/{add_first_node}/markets.'  # endpoint markets list
        self.BOARDS_LIST = f'{super().ISS}/engines/{add_first_node}/markets/{add_sec_node}/boards.'  # endpoint boards list
        self.TRADES_LIST = f'{super().ISS}/engines/{add_first_node}/markets/{add_sec_node}/trades.'  # endpoint boards list


class SecuritiesEndpoints(CoreEndpoints):
    def __init__(self):
        self.SECURITIES_LIST = super().ISS + '/securities.'  # endpoint securities list


user_ui = User(
    email=MoexVariables.auth_email,
    password=MoexVariables.auth_password)

wrong_user_ui = User(
    email=MoexVariables.wrong_email,
    password=MoexVariables.wrong_password)
