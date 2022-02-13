import mysql.connector

from src import cli, __app_name__
from src.config import __username__, __password__, __host__, __database__

db = mysql.connector.connect(user=__username__, password=__password__, host=__host__, database=__database__)
cr = db.cursor()

sql = """
CREATE TABLE [IF NOT EXISTS] `store`(
	`service` VARCHAR(50) NOT NULL,
	`password` VARCHAR(200) NOT NULL
);

ALTER TABLE `store`
	ADD PRIMARY KEY (`service`),
	ADD UNIQUE INDEX `service` (`service`);


CREATE TABLE [IF NOT EXISTS] `kvdb` (
	`key` VARCHAR(50) NOT NULL,
	`value` VARCHAR(50) NOT NULL
);
"""
def main():
    cli.app(prog_name=__app_name__)
    cr.execute(sql)
    db.close()

if __name__ == "__main__":
    main()