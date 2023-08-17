from src.CBaseRequests import CBaseRequest
from helpers import *
import pytest




def get_filter_stats(request, endpoint, filter_name, filter_key, filter_value):
    response = request.get(endpoint, filter=f'{filter_name}={filter_value}')
    filter_stat = {}
    filter_stat[filter_value] = response
    return filter_stat

@pytest.fixture(scope="module")
def filters_metadata():
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries/meta'

    filters_stats = {}
    filters_stats['by_city'] = get_filter_stats(request, endpoint, 'by_city', 'city', 'san_diego')
    filters_stats['by_name'] = get_filter_stats(request, endpoint, 'by_name', 'name', 'cooper')
    filters_stats['by_state'] = get_filter_stats(request, endpoint, 'by_state', 'state', 'new_york')
    filters_stats['by_postal'] = get_filter_stats(request, endpoint, 'by_postal', 'postal_code', '44107')

    return filters_stats


def get_breweries(number_breweries):
    request = CBaseRequest(BASE_URL)
    endpoint = 'breweries'
    if number_breweries > MAX_ITEMS_PER_PAGE:
        number_breweries = MAX_ITEMS_PER_PAGE
    return request.get(f'{endpoint}', paged=f'{PAGED_PREFIX}{number_breweries}')

@pytest.fixture()
def breweries_objects():
    return get_breweries(DEFAULT_ITEMS_PER_PAGE)
@pytest.fixture()
def breweries_ids_50():
    breweries = get_breweries(DEFAULT_ITEMS_PER_PAGE)
    return [item['id'] for item in breweries]
#filters_metadata()