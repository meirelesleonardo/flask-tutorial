CREATE TABLE IF NOT EXISTS produtos(
    code INT(4) USIGNED ZEROFILL NOT NULL,
    name CHAR(50),
    stock INT NOT NULL,
    id_category tinyint NULL,
    PRIMARY KEY('code')
);


CREATE TABLE IF NOT EXISTS categories(
    id tinyint NULL,
    name CHAR(40) NOT NULL,
    description VARCHAR(200) NOT NULL,
    PRIMARY KEY('id')
);


ALTER TABLE produtos ADD FOREIGN KEY ('id_category') REFERENCES categories('id');