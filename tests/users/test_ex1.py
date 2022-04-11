import pytest

# function 	Run once per test
# class	 	Run once per class of tests
# module 	Run once per module
# session 	Run once per session

def test_one():
	assert 1 == 1

@pytest.fixture
def fixture_per_func():
	print('run-fixture-per-func')
	return 1

def test_func_example1(fixture_per_func):
	print('run-func_example-1')
	num = fixture_per_func
	assert num == 1

def test_func_example2(fixture_per_func):
	print('run-func-example-2')
	num = fixture_per_func
	assert num == 1
	
@pytest.fixture(scope = 'session')
def fixture_per_session():
	print('run-fixture-per-session')
	return 2

def test_session_example1(fixture_per_session):
	print('run-session-example-1')
	num = fixture_per_session
	assert num == 2

def test_session_example2(fixture_per_session):
	print('run-session-example-2')
	num = fixture_per_session
	assert num == 2


@pytest.fixture
def yield_fixture():
	print('Start test phase')
	yield 3
	print('End test phase')

def test_yield_ex(yield_fixture):
	print('Run yield ex')
	assert yield_fixture == 3