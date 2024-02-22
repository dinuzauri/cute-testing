import pytest


@pytest.fixture(scope="session")
def generic_fixture() -> int:
    yield 0
