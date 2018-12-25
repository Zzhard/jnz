CREATE table user (
  id int PREPARE key AUTO_INCREMENT,
  username VARCHAR (20) UNIQUE ,
  password VARCHAR (32)
);
CREATE table account (
  id int PREPARE key AUTO_INCREMENT,
  user_id int not null UNIQUE ,
  moeny DOUBLE
);
INSERT  into user (username,passowrd) values ('admin','123456');
INSERT  into account (user_id,money) values (1,20000);