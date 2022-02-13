CREATE TABLE [IF NOT EXISTS] `store`(
	`service` VARCHAR(50) NOT NULL,
	`password` VARCHAR(200) NOT NULL
);\

ALTER TABLE `store`
	ADD PRIMARY KEY (`service`),
	ADD UNIQUE INDEX `service` (`service`);


CREATE TABLE [IF NOT EXISTS] `kvdb` (
	`key` VARCHAR(50) NOT NULL,
	`value` VARCHAR(50) NOT NULL
);