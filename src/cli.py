
import typer
import mysql.connector

from typing import Optional
from cryptography.fernet import Fernet
from src import __app_name__, __version__
from src.config import __username__, __password__, __host__, __database__,__key__

db = mysql.connector.connect(user=__username__, password=__password__, host=__host__, database=__database__)
cr = db.cursor()

app = typer.Typer()

fernet = Fernet(__key__)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo("{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def add(service: str, password: str):
    password_enc = fernet.encrypt(password.encode())
    cr.execute('SELECT * FROM store;')
    res = cr.fetchall()
    for x in res:
        if service == x[0]:
            return typer.echo("Service already exists. Kindly try another name.")
    sql = "INSERT INTO store (`service`, `password`) VALUES (%s, %s)"
    val = (service, password_enc)
    cr.execute(sql, val)
    db.commit()
    db.close()
    typer.echo(f"Added `{password}` as a password to the service: `{service}`.")

@app.command()
def remove(service: str):
    sql = f"DELETE FROM store WHERE service='{service}'"
    cr.execute(sql)
    db.commit()
    db.close()
    typer.echo(f"Removed {service}")

@app.command()
def get(service: str):
    sql = f"SELECT * FROM store WHERE service='{service}'"
    cr.execute(sql)
    res = cr.fetchone();
    db.commit()
    db.close()

    if res:
        dec = bytes(res[1], 'utf-8')
        typer.echo(f"Your password for `{service}` is `{fernet.decrypt(dec).decode()}`")
    else:
        typer.echo("That service does not exist.")

@app.command()
def list():
    typer.echo(f"Here are all your passwords:")
    sql = f"SELECT * FROM store;"
    cr.execute(sql)
    res = cr.fetchall()
    for x in res: 
        typer.echo(f"{x[0]} | {x[1]}")
    db.close()


