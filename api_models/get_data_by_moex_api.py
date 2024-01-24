from utils import send_request
from test_data import FileTypes, Method


def get_data_by_moex_api(base_url, endpoint, type_resp=FileTypes.non_type, params=None):
    return send_request(base_url, endpoint + type_resp, Method.GET, data=None, params=params)
