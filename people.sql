CREATE TABLE IF NOT EXISTS people (
    `Person` VARCHAR(17) CHARACTER SET utf8,
    `Year` VARCHAR(4) CHARACTER SET utf8,
    `Picture` VARCHAR(14) CHARACTER SET utf8,
    `Description` VARCHAR(47) CHARACTER SET utf8
);
INSERT INTO people VALUES
    ('Shaffi Goldwasser','2012','goldwasser.jpg','cryptography theory computational number theory'),
    ('Edwin Catmull',' ','naur.jpg','graphics animation'),
    ('Raj Reddy','1994','reddy.jpg','ai speech language recognition'),
    ('Manuel Blum','1995','blum.jpg','theory numeric computation Goldwasser advisor'),
    ('Alan Turing',NULL,'turing.jpg','did not get the turing prize'),
    ('Jim Gray','1998',NULL,'database theory'),
    ('Leslie Lamport','2008',NULL,'distributed concurrent system logical clock'),
    ('Barbara Liskov','2002',NULL,'distributed concurrent system'),
    ('Yoshua Bengio','2018','bengio.jpg','neural networks deep leaning ai'),
    ('Whitfield Diffie','2015','diffie.jpg','public key cryptography key exchange'),
    ('Marvin Minsky','1969',NULL,'artificial intelligence theory'),
    ('Donald Knuth','1974','knuth.jpg','analysis algorithm elmasri advisor'),
    ('Ken Thompson','1983','thompson.jpg','unix operating systems theory'),
    ('Peter Naur','2005','naur.jpg','compilers theory programming language'),
    ('Vint Cerf',' ',NULL,'internet www tcp/ip'),
    ('Fred Brooks','1999',NULL,'software engineering computer architecture');
