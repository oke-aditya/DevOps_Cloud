import pytest

@pytest.fixture
def error_fixture():
	assert 0

def test_ok():
	print("ok")

def test_fail():
	assert 0

def test_error(error_fixture):
	pass

def test_skip():
	pytest.skip("This test was skipped")

def test_xfail():
	pytest.xfail("Failing this test")

@pytest.mark.fail(reason="always fail")
def test_xpass():
	pass

