## PassMan - Your new favorite password manager. 

PassMan is a barebones password manager for you. You can customize as much as you like with very little tinkering. 

### Installation
```python -m pip install mysql-connector-python cryptography```

### Setup
- Duplicate src/config.py.example to config.py and enter the requried values.
- It is recommended to generate a new key using openssl. (``)

### Documentation
- [Fernet](https://cryptography.io/en/latest/fernet/)
- [MySQL](https://dev.mysql.com/doc/connector-python/en/)
- [Typer](https://typer.tiangolo.com/)

### Start Project
```python -m src [commmand]```

### CLI Menu
```
Usage: passman [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  add
  get
  list
  remove
```


> This is a CBSE AISCE Project for the session 2021-22, developed by Suryavir Kapur and Jai Sharma.