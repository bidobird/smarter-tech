# Smarter Technology — Package sorting task

This repository contains solutions (with tests) for the package dispatching function:

- A package is **bulky** if volume \(w \* h \* l\) \(\ge 1000000\) cm³ **or** any dimension \(\ge 150\) cm
- A package is **heavy** if mass \(\ge 20\) kg
- Dispatch rules:
  - **STANDARD**: not bulky and not heavy
  - **SPECIAL**: bulky or heavy (but not both)
  - **REJECTED**: bulky and heavy

## Project layout

- `typescript-solution/`: TypeScript implementation + `vitest` tests
- `python-solution/`: Python implementation + `unittest` tests
- `golang-solution/`: Go implementation + `go test` tests

## Run everything via Make

If you have `make` available:

```bash
make all
```

### TypeScript

```bash
make ts-test
make ts-typecheck
make ts-build
```

### Python

```bash
make py-test
```

### Go

```bash
make go-test
```

## Run each solution directly

See the README inside each solution folder for exact commands.

