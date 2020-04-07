all:
	python3 setup.py build

install:
	pip3 install --ignore-installed .

uninstall:
	pip3 uninstall --yes gymjam

clean:
	python3 setup.py clean --all


.PHONY: all install uninstall clean
