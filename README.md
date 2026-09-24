.
├── .env.example
├── .git
│   ├── branches
│   ├── config
│   ├── description
│   ├── HEAD
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── push-to-checkout.sample
│   │   ├── sendemail-validate.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   ├── objects
│   │   ├── info
│   │   └── pack
│   ├── packed-refs
│   └── refs
│       ├── heads
│       ├── remotes
│       └── tags
├── .gitignore
├── LICENSE
├── __pycache__
│   └── main.cpython-312.pyc
├── pyproject.toml
├── .python-version
├── README.md
├── src
│   └── track_flow
│       ├── __init__.py
│       ├── main.py
│       └── __pycache__
├── tests
├── uv.lock
└── .venv
    ├── bin
    │   ├── activate
    │   ├── activate.bat
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── activate.nu
    │   ├── activate.ps1
    │   ├── activate_this.py
    │   ├── activate.xsh
    │   ├── agent-detector
    │   ├── deactivate.bat
    │   ├── detect-installer-test
    │   ├── dotenv
    │   ├── email_validator
    │   ├── fastapi
    │   ├── httpx
    │   ├── idna
    │   ├── markdown-it
    │   ├── pydoc.bat
    │   ├── pygmentize
    │   ├── python -> /usr/bin/python3.12
    │   ├── python3 -> python
    │   ├── python3.12 -> python
    │   ├── track-flow
    │   ├── typer
    │   ├── uvicorn
    │   ├── watchfiles
    │   └── websockets
    ├── CACHEDIR.TAG
    ├── .gitignore
    ├── lib
    │   └── python3.12
    ├── lib64 -> lib
    ├── .lock
    └── pyvenv.cfg

24 directories, 62 files; 1. O que é FastAPI? R: e um framework para criar API para as nossas aplicacoes; 2. O que acontece quando fazemos uma requisição GET /health? R: Quando fazemos uma requisicao o servidor recebe, interpreta e  executa a funcao referente ao path do endpoint da requisicao que criamos; 