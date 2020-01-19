import pytest
import requests
import requests_mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)


location_url = 'https://www.metaweather.com/api/location/search'


@pytest.fixture()
def mock():
    with requests_mock.Mocker() as m:
        yield m


def test_json1(mock):
    mock.get(location_url, json=[])
    assert get_cities_woeid('Warszawa') == {}


def test_json2(mock):
    mock.get(location_url, json = [
        {'title': 'Warsaw', 'woeid': 523920},
        {'title': 'Newark', 'woeid': 2459269}
    ])
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }


def test_status(mock):
    mock.get(location_url, status_code = 404)
    with pytest.raises(requests.exceptions.HTTPError):
        get_cities_woeid('wrr')


def test_json_conversion(mock):
    mock.get(location_url, text='!?')
    # with pytest.raises(RuntimeError) as exc:
    #     get_cities_woeid('fluskaki')
    #     assert isinstance(exc.__cause__, TypeError)


def test_status_timeout():
    with pytest.raises(requests.exceptions.Timeout):
        get_cities_woeid('Warszawa', timeout=1e-7)