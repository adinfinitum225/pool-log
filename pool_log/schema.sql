DROP TABLE IF EXISTS pool;
DROP TABLE IF EXISTS log;
DROP TABLE IF EXISTS maint;

CREATE TABLE pool(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	volume INTEGER NOT NULL
);

CREATE TABLE log(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	pool INTEGER NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	temperature REAL NOT NULL,
	ph REAL NOT NULL,
	chlorine REAL NOT NULL,
	cya REAL NOT NULL,
	clarity TEXT NOT NULL,
	FOREIGN KEY (pool) REFERENCES pool(id)
);

CREATE TABLE main(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	chlorine INTEGER NOT NULL DEFAULT 0,
	shock INTEGER NOT NULL DEFAULT 0,
	acid INTEGER NOT NULL DEFAULT 0,
	base INTEGER NOT NULL DEFAULT 0,
	algaecide INTEGER NOT NULL DEFAULT 0,
	backwash INTEGER NOT NULL DEFAULT 0,
	vacuum INTEGER NOT NULL DEFAULT 0,
	skimmer INTEGER NOT NULL DEFAULT 0,
	motor_basket INTEGER NOT NULL DEFAULT 0
);
