from src.CBaseRequests import CBaseRequest
from helpers import *
import pytest


def assert_object_keys(object: dict):
    missing_fields = [field for field in BREWERY_OBJECT_KEYS if field not in object]
    assert not missing_fields
def test_list_breweries():
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    response = request.get(f'{endpoint}', expected_error=False)
    #assert response['status'] == STATUS_SUCCESS
    assert len(response) > 0


def assert_filter_value(brewery_object, filter_value):
    assert normalize_str(filter_value) in normalize_str(brewery_object)

def assert_filter_eq_value(brewery_object, filter_value):
    assert normalize_str(filter_value) == normalize_str(brewery_object)

@pytest.mark.parametrize('index',
                         [
                             0,
                             -1

                         ])
def test_list_brewery_by_id(index, breweries_objects):
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    brewery = breweries_objects[index]
    response = request.get(f'{endpoint}', endpoint_id=brewery['id'], expected_error=False)
    assert_object_keys(response)




# def assert_filter_value_entering(brewery_object, key, filter_value)
@pytest.mark.parametrize('filter_name, key, filter_value',
                         [
                             ('by_city', 'city', 'san_diego'),
                             ('by_city', 'city', 'San diego'),
                             ('by_name', 'name', '인천맥주'),
                             ('by_name', 'name', 'cooper'),
                             ('by_name', 'name', 'Brewing Cooperative'),
                             ('by_state', 'state', 'New York'),
                             ('by_postal','postal_code','44107')
                         ])
def test_breweries_filter_value_check(filter_name, key, filter_value):
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    response = request.get(endpoint, filter=f'{filter_name}={filter_value}')
    assert_filter_value(response[0][key], filter_value)


@pytest.mark.parametrize('filter_name, key, filter_value',
                         [
                             ('by_city', 'city', 'san_diego'),
                             ('by_name', 'name', 'cooper'),
                             ('by_state', 'state', 'new_york')
                         ])
def test_filter_per_page(filter_name, key, filter_value, filters_metadata):
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    page_prefix = 'per_page='
    total_items = int(filters_metadata[filter_name][filter_value][TOTAL])
    if total_items > MAX_ITEMS_PER_PAGE:
        total_items = MAX_ITEMS_PER_PAGE
    response = request.get(endpoint,
                           filter=f'{filter_name}={filter_value}',
                           paged=f'{page_prefix}{total_items}'
                           )
    assert len(response) == total_items

@pytest.mark.parametrize('num_ids',
                         [
                             1,
                             5,
                             50
                         ])
def test_filters_by_ids(num_ids, breweries_ids_50):
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    filter_name = 'by_ids'
    filter_value = ','.join(map(str, breweries_ids_50[:num_ids]))
    response = request.get(endpoint,
                           filter=f'{filter_name}={filter_value}')
    assert num_ids == len(response)
    for i, item in enumerate(response):
        assert_filter_eq_value(item['id'], breweries_ids_50[i])