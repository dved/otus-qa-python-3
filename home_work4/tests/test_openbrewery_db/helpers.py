def normalize_str(s: str):
    return (s.replace(' ', '_')).lower()

DEFAULT_ITEMS_PER_PAGE = 50
MAX_ITEMS_PER_PAGE = 200
PAGED_PREFIX = 'per_page='
BASE_URL = "https://api.openbrewerydb.org/v1"
STATUS_SUCCESS = 'success'
TOTAL = 'total'
BREWERY_OBJECT_KEYS = ['id',
                     'name',
                     'brewery_type',
                     'address_1',
                     'address_2',
                     'address_3',
                     'city',
                     'state_province',
                     'postal_code',
                     'country',
                     'longitude',
                     'latitude',
                     'phone',
                     'website_url',
                     'state',
                     'street'
                       ]
