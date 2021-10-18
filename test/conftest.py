import pytest

@pytest.fixture()
def sample_response():
    """Sample response from octobre 18th 2021
    """
    with open(r"sampledata\2021_10_18.html", "r") as fh:
        content = fh.read()
    return content

