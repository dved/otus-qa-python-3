# tests for service https://dog.ceo/dog-api/

from src.CBaseRequests import CBaseRequest
import pytest

BASE_URL = "https://dog.ceo/api"
STATUS_SUCCESS = 'success'
#MAX_PICTURES_COUNT_PER_REQUEST = 50

def test_all_breeds():
    request = CBaseRequest(BASE_URL)
    endpoint = 'breeds/list/all'
    response = request.get(f'{endpoint}', expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert len(response['message']) > 0

# def test_specific_breed():
#     request = CBaseRequest(BASE_URL)
#     breed = 'affenpinscher'
#     endpoint = f'breed/{breed}/images/random'
#     response = request.get(f'{breed}/{endpoint}', expected_error=False)
def assert_link_is_picture(link: str):
    return link.startswith('https') and (link.endswith('.jpg'))

def assert_list_links(list):
    result = True
    for link in list:
        if not assert_link_is_picture(link):
            result = False
    return result

def get_breeds_to_test():
    request = CBaseRequest(BASE_URL)
    return list((request.get('breeds/list/all', expected_error=False))['message'])


def number_images_by_breed(breed):
    request = CBaseRequest(BASE_URL)
    return len((request.get(f'breed/{breed}/images', expected_error=False)['message']))


def assert_responses(response, max_pictures_per_request, pictures_count):
    if pictures_count and pictures_count > 0:
        # if pictures_count >= 1 the response['message'] is a list,
        # test if number of pictures equal to passed parameter
        max_pictures_per_request
        # if max_pictures_per_request is not None:
        if pictures_count > max_pictures_per_request:
            assert len(response['message']) == max_pictures_per_request
        else:
            assert len(response['message']) == pictures_count
        # iterate and check if all links are valuable
        for i in response['message']:
            assert assert_link_is_picture(i)
    else:
        assert assert_link_is_picture(response['message'])


# testing for {BASE_URL}/breeds/list/all
@pytest.mark.parametrize('endpoint',
                         [
                            'breeds/list/all',
                         ]
                         )
def test_basic_enpoints(endpoint):
    request = CBaseRequest(BASE_URL)
    response = request.get(f'{endpoint}', expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert len(response['message']) > 0


# tests for endpoints: breed/{breed}/images/random and breed/{breed}/images
all_breeds = get_breeds_to_test()
@pytest.mark.parametrize('endpoint_prefix, endpoint_suffix',
                         [
                             ('breed', 'images/random')
                         ])
@pytest.mark.parametrize('breed',
                         [
                             all_breeds[0], all_breeds[len(all_breeds) - 1]
                         ])
def test_breed_images(endpoint_prefix, breed, endpoint_suffix):
    request = CBaseRequest(BASE_URL)
    response = request.get(f'{endpoint_prefix}/{breed}/{endpoint_suffix}', expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert len(response['message']) > 1
    assert assert_link_is_picture(response['message'])


# testing {BASE_URL}/breeds/image/random/{n}
@pytest.mark.parametrize('pictures_count',['',0, 1, 50, 51, 4.9999999999999999])
@pytest.mark.parametrize('endpoint_prefix, max_pictures_per_request',
                         [
                            ('breeds/image/random', 50)
                         ])
def test_breeds_random(endpoint_prefix, max_pictures_per_request, pictures_count):
    request = CBaseRequest(BASE_URL)
    response = request.get(endpoint_prefix, endpoint_id=pictures_count, expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert_responses(response, max_pictures_per_request, pictures_count)


# testing {BASE_URL}/breed/{breed}/images
# testing {BASE_URL}/breed/{breed}/images/random/{n}
@pytest.mark.parametrize('pictures_count',
                         [
                             '',
                             0,
                             1,
                             4.9999999999999999,
                             number_images_by_breed(all_breeds[0]),
                             number_images_by_breed(all_breeds[0])+1
                         ])
@pytest.mark.parametrize('endpoint_prefix, max_pictures_per_request',
                         [
                            (f'breed/{all_breeds[0]}/images/random', number_images_by_breed(all_breeds[0]))
                         ])
def test_images_by_breed(endpoint_prefix, max_pictures_per_request, pictures_count):
    request = CBaseRequest(BASE_URL)
    response = request.get(endpoint_prefix, endpoint_id=pictures_count, expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert_responses(response, max_pictures_per_request, pictures_count)


# testing {BASE_URL}/breed/{breed}/list
@pytest.mark.parametrize('endpoint_prefix, breed, endpoint_suffix',
                         [
                             ('breed', 'hound', 'list')
                         ])
def test_sub_breeds(endpoint_prefix, breed, endpoint_suffix):
    request = CBaseRequest(BASE_URL)
    response = request.get(f'{endpoint_prefix}/{breed}/{endpoint_suffix}', expected_error=False)
    assert response['status'] == STATUS_SUCCESS
    assert len(response['message']) > 1


def get_sub_breeds_by_breed(breed):
    request = CBaseRequest(BASE_URL)
    response =  request.get(f'breed/{breed}/list', expected_error=False)
    return response['message']


def get_breeds_with_sub_breeds_sorted():
    request = CBaseRequest(BASE_URL)
    response = request.get(f'breeds/list/all', expected_error=False)
    breeds_list = {key:value for key, value in response['message'].items() if value}
    return list(sorted(breeds_list.items(), key=lambda item: len(item[1])))

breeds_with_sub_breeds = get_breeds_with_sub_breeds_sorted()
#testing {BASE_URL}/breed/{breed}/{sub_breed}/images
# testing breed with minimal sub breeds
breed_min_sub_breeds = breeds_with_sub_breeds[0]
breed_max_sub_breeds = breeds_with_sub_breeds[-1]

@pytest.mark.parametrize('endpoint_prefix, endpoint_suffix',
                         [
                             ('breed', 'images')
                         ])
@pytest.mark.parametrize('breed_with_sub_breeds',
                         [
                            breed_min_sub_breeds,
                            breed_max_sub_breeds
                         ])
def test_subbreed_images(endpoint_prefix, endpoint_suffix, breed_with_sub_breeds):
    request = CBaseRequest(BASE_URL)
    breed, sub_breed_list = breed_with_sub_breeds
    for sub_breed in sub_breed_list:
        response = request.get(f'{endpoint_prefix}/{breed}/{sub_breed}/{endpoint_suffix}', expected_error=False)
        assert response['status'] == STATUS_SUCCESS
        assert len(response['message'])
        assert assert_list_links(response['message'])