DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS method;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);



CREATE TABLE product(
    uri TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    activity_code_1 TEXT,
    activity_code_2 TEXT,
    introduction TEXT,
    entityType TEXT,
    graphdbName TEXT,
    dataSpace TEXT,
    abstractField TEXT,
    creationDate TEXT,
    sameAs TEXT,
    industry TEXT,
    outputOf TEXT,
    inputOf TEXT,
    productionVolume INTEGER,
    productionVolumeUnit TEXT,
    pedigreeMatrix TEXT,
    imageUrl TEXT

);

CREATE TABLE method(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_method TEXT NOT NULL,
    name_impact TEXT NOT NULL,
    unit TEXT NOT NULL
);
