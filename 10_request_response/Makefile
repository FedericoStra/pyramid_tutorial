.phony: all install test run

all: install test

install:
	pip install -e .

test:
	py.test tests/

run:
	pserve development.ini --reload
