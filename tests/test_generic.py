import allure


@allure.title("Generic Test")
@allure.description("This is a generic allure description")
def test_generic_success() -> None:
    success: bool = True
    assert success


def test_generic_fail() -> None:
    success: bool = False
    assert success


def test_generic_success_with_fixture(generic_fixture) -> None:
    assert generic_fixture == 0
