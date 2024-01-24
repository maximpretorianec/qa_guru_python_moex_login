import jsonschema
import pytest
import allure
import json
import os

from api_models import get_data_by_moex_api
from utils import load_schema, log_to_allure, log_to_console, TypeTag, Severity
from test_data import ExpectedMessagesMOEX, FileTypes, MoexDataVariables, StatusCode, EngineEndpoints, \
    SecuritiesEndpoints, tmp_path


@allure.tag(TypeTag.API)
@allure.severity(Severity.MAJOR)
@allure.label("owner", "mgolubev")
@allure.label('layer', TypeTag.API)
@allure.title("Проверка получения торговых систем Мосбиржи по апи, в разных форматах")
@allure.feature("Получить доступные торговые системы")
@pytest.mark.parametrize("file_type", [FileTypes.xml, FileTypes.html, FileTypes.json, FileTypes.non_type])
def test_get_available_trade_system(base_url, file_type):
    with allure.step("Отправка запроса"):
        result = get_data_by_moex_api(base_url, EngineEndpoints().ENGINE_LIST, file_type)

    with allure.step("Проверка запроса"):
        assert file_type in result.headers['Content-Type']
        assert StatusCode.SUCCESS == result.status_code
        assert ExpectedMessagesMOEX.iss_engines in result.text
        if file_type == FileTypes.json:
            jsonschema.validate(result.json(), load_schema('get_iss_engines.json'))

    log_to_allure(result.request, result)
    log_to_console(result)


@allure.tag(TypeTag.API)
@allure.severity(Severity.MAJOR)
@allure.label("owner", "mgolubev")
@allure.label('layer', TypeTag.API)
@allure.title("Проверка получения торговых ценных бумаг Мосбиржи по апи, в разных форматах")
@allure.feature("Получить торгуемые ценные бумаги Мосбиржи")
@pytest.mark.parametrize("file_type", [FileTypes.xml, FileTypes.html, FileTypes.json, FileTypes.non_type])
def test_get_securities_list(base_url, file_type):
    with allure.step("Отправка запроса"):
        result = get_data_by_moex_api(base_url, SecuritiesEndpoints().SECURITIES_LIST, file_type)

    with allure.step("Проверка запроса"):
        assert file_type in result.headers['Content-Type']
        assert StatusCode.SUCCESS == result.status_code
        assert ExpectedMessagesMOEX.iss_securities in result.text
        if file_type == FileTypes.json:
            jsonschema.validate(result.json(), load_schema('get_iss_security.json'))

    log_to_allure(result.request, result)
    log_to_console(result)


@allure.tag(TypeTag.API)
@allure.severity(Severity.MAJOR)
@allure.label("owner", "mgolubev")
@allure.label('layer', TypeTag.API)
@allure.title("Проверка получения списка рынков торговых систем Мосбиржи по апи, в разных форматах")
@allure.feature("Получить список рынков торговой системы")
@pytest.mark.parametrize("file_type", [FileTypes.xml, FileTypes.html, FileTypes.json, FileTypes.non_type])
def test_get_market_list_by_engine_item(base_url, get_engine_from_list, file_type):
    with allure.step("Отправка запроса"):
        engine = get_engine_from_list
        result = get_data_by_moex_api(base_url, EngineEndpoints(engine).MARKETS_LIST, file_type)

    with allure.step("Проверка запроса"):
        assert file_type in result.headers['Content-Type']
        assert StatusCode.SUCCESS == result.status_code
        assert ExpectedMessagesMOEX.iss_markets in result.text
        if file_type == FileTypes.json:
            jsonschema.validate(result.json(), load_schema(f'get_iss_markets_by_engine_{engine}.json'))

    log_to_allure(result.request, result)
    log_to_console(result)


@allure.tag(TypeTag.API)
@allure.severity(Severity.MAJOR)
@allure.label("owner", "mgolubev")
@allure.label('layer', TypeTag.API)
@allure.title("Проверка получения, в разных форматах и выгрузки в json файл всех режимов торгов рынка Мосбиржи по апи")
@allure.feature("Получить справочник режимов торгов рынка")
@pytest.mark.parametrize("file_type", [FileTypes.xml, FileTypes.html, FileTypes.json, FileTypes.non_type])
def test_get_directory_of_market_trading_modes(tmp_dir_control, base_url, get_market_from_list_by_engine, file_type):
    with allure.step("Отправка запроса"):
        engine, market = get_market_from_list_by_engine
        boards_data = get_data_by_moex_api(base_url,
                                           EngineEndpoints(add_first_node=engine, add_sec_node=market).BOARDS_LIST,
                                           file_type)

    with allure.step("Выгрузка данных в json файл"):
        if file_type == FileTypes.json:
            json_file = os.path.join(tmp_path, f'{engine}_{market}.json')
            with open(f'{json_file}', 'w') as outfile:
                json.dump(boards_data.json(), outfile)

    with allure.step("Проверка запроса"):
        assert file_type in boards_data.headers['Content-Type']
        assert StatusCode.SUCCESS == boards_data.status_code
        assert ExpectedMessagesMOEX.iss_boards in boards_data.text
        if file_type == FileTypes.json:
            assert os.path.getsize(f'{json_file}') > 0

    log_to_allure(boards_data.request, boards_data)
    log_to_console(boards_data)


@allure.tag(TypeTag.API)
@allure.severity(Severity.MAJOR)
@allure.label("owner", "mgolubev")
@allure.label('layer', TypeTag.API)
@allure.title("Проверка получения, в разных лимитах всех сделок рынка Мосбиржи по апи")
@allure.feature("Получить все сделки рынка")
@pytest.mark.parametrize("limit", [{'limit': 100},
                                   {'limit': 1},
                                   {'limit': 10},
                                   {'limit': 0}])
def test_get_all_trades_by_market(base_url, limit):
    with allure.step("Отправка запроса"):
        trades_data = get_data_by_moex_api(base_url,
                                           EngineEndpoints(add_first_node=MoexDataVariables.engine_by_stock,
                                                           add_sec_node=MoexDataVariables.market_by_index).TRADES_LIST,
                                           FileTypes.json, params=limit)

    with allure.step("Проверка запроса"):
        assert FileTypes.json in trades_data.headers['Content-Type']
        assert StatusCode.SUCCESS == trades_data.status_code
        assert ExpectedMessagesMOEX.iss_trades in trades_data.text

        if limit['limit'] > 0:
            assert len(trades_data.json()['trades']['data']) == limit['limit']
        else:
            assert len(trades_data.json()['trades']['data']) == limit['limit'] + 1

    log_to_allure(trades_data.request, trades_data)
    log_to_console(trades_data)
