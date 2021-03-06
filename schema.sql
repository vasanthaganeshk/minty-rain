create table auth(
       uid integer primary key autoincrement,
       uname varchar(200) not null,
       passwd varchar(200) not null);

create table problems(
       problemid integer primary key autoincrement,
       problemname varchar(200) not null,
       pstatement text);

create table transactions(
       transactionid integer primary key autoincrement,
       uid integer,
       problemid integer,
       solsubmission text,
       tmstmp datetime,
       status varchar(10),
       foreign key(uid) references auth,
       foreign key(problemid) references problems);       

create table testcases(
       problemid integer,
       testcase text);       
