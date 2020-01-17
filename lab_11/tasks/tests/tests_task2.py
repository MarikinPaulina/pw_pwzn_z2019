import pytest
from unittest.mock import (
    Mock,
    patch
)

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)


API_URL = 'https://www.metaweather.com/api/'


@patch('requests')
def test_json1(requests_mock):
    response_mock = Mock()
    response_mock.json.return_value = []
    requests_mock.get.return_value = response_mock

    assert get_cities_woeid('Warszawa') == {}
    assert response_mock.call_args_list == [call('')]


def test_json1(requests_mock):
    response_mock = Mock()
    response_mock.json.return_value = [
        {'title': 'Warsaw', 'woeid': 523920},
        {'title': 'Newark', 'woeid': 2459269}
    ]
    requests_mock.get.return_value = response_mock

    assert get_cities_woeid('Warszawa') == {}

