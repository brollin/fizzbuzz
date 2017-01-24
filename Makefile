test:
	nose2 --verbose

init:
	pip install -r requirements.txt

lint:
	flake8 fizzbuzz/ test/

.PHONY: test
