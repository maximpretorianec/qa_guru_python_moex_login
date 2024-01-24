import pytest
import random
import os

from utils import tmp_path
from test_data import MoexUrl, EngineEndpoints, FileTypes
from api_models import get_data_by_moex_api


@pytest.fixture()
def tmp_dir_control():
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    yield
    if os.listdir(tmp_path):
        for filename in os.listdir(tmp_path):
            os.remove(os.path.join(tmp_path, filename))


@pytest.fixture()
def base_url():
    return MoexUrl.BASE_URL


@pytest.fixture()
def get_engine_from_list(base_url):
    return random.choice(
        get_data_by_moex_api(base_url, EngineEndpoints().ENGINE_LIST, FileTypes.json).json()['engines']['data'])[1]


@pytest.fixture()
def get_market_from_list_by_engine(base_url, get_engine_from_list):
    engine = get_engine_from_list
    return engine, random.choice(
        get_data_by_moex_api(base_url,
                             EngineEndpoints(engine).MARKETS_LIST,
                             FileTypes.json).json()['markets']['data'])[1]
