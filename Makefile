noop:

edit:
	vi $(shell find . -type f -name '*.py' \
					-and -not -name '__init__.py' \
					-and -not -name '__main__.py') \
					Makefile config.yaml

profile:
	mprof run --include-children python main.py

plot:
	mprof plot --output memory-profile.png
