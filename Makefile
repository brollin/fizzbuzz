test:
	nose2

init:
	pip install -r requirements.txt

lint:
	flake8 src/ test/

.PHONY: test
