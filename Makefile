.PHONY: setup test clean

setup:
	cd password-generator && python3 -m venv .venv && ./.venv/bin/pip install --upgrade pip && ./.venv/bin/pip install -r requirements.txt pytest

test:
	cd password-generator && ./.venv/bin/pytest

clean:
	rm -rf password-generator/.venv password-generator/__pycache__ password-generator/tests/__pycache__ password-generator/.pytest_cache
