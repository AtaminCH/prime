```bash
clang-cl -help
```

```bash
git clone https://github.com/python/cpython.git
```

```bash
cd cpython
```

```bash
git checkout v3.13.x
```

```bash
notepad Tools\jit\_llvm.py
```

```bash
PCbuild\build.bat --experimental-jit
```

```bash
PCbuild\amd64\python
```

```bash
python3 prime.py
```

```bash
PCbuild\amd64\python prime.py
```

```bash
cd ..
```

```bash
cpython\PCbuild\amd64\python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install flask
```

```bash
python prime_flask.py
```
