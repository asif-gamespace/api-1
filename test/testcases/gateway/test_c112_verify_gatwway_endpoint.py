import allure
from testdata.gateway_api.gateway_endpoint import response, response_body


@allure.step('Gateway api, status code validation')
def test_c112_01_status_code_is_200():
    assert response.status_code == 200


@allure.step("Gateway, response body not none validation")
def test_c112_02_response_body_not_none():
    assert response_body is not None


@allure.step("Check Email")
def test_c112_03_email():
    assert 'email' in response_body['data']['submit']