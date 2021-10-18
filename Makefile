.PHONY: clean
clean:
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '*.pyc' -delete

