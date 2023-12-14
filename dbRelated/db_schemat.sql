drop database ContactsKS;
create database ContactsKS;

use ContactsKS;

create table Contacts(
id int(11) NOT NULL AUTO_INCREMENT,	
firstName varchar(30),
lastName varchar(30),
phone int(12),
isFriend boolean,
email varchar(50),
birthday varchar(15),
PRIMARY KEY (id)
);