.PHONY: help all ts-install ts-test ts-typecheck ts-build py-test go-test

TS_DIR := typescript-solution
PY_DIR := python-solution
GO_DIR := golang-solution

help:
	@echo "Targets:"
	@echo "  make all          - run all test suites (ts, py, go)"
	@echo "  make ts-install   - install TypeScript deps"
	@echo "  make ts-test      - run TypeScript tests"
	@echo "  make ts-typecheck - run TypeScript typecheck"
	@echo "  make ts-build     - build TypeScript (tsc)"
	@echo "  make py-test      - run Python unittest suite"
	@echo "  make go-test      - run Go unit tests"

all: ts-test py-test go-test

ts-install:
	cd "$(TS_DIR)" && npm install

ts-test: ts-install
	cd "$(TS_DIR)" && npm test

ts-typecheck: ts-install
	cd "$(TS_DIR)" && npm run typecheck

ts-build: ts-install
	cd "$(TS_DIR)" && npm run build

py-test:
	cd "$(PY_DIR)" && python -m unittest discover -s tests -p "test_*.py"

go-test:
	cd "$(GO_DIR)" && go test ./...

