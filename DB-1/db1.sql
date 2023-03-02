-- Active: 1677763456317@@127.0.0.1@3306@test
create table student(stud_name varchar(20), stud_id int(4), stud_standard int(2));

drop table student;

alter table student add (age int(3), course VARCHAR(10));
desc student;

truncate table student;
insert into student values ("Chintu", 001,9, 14, "Higher");


update student set stud_name="Pintu" where stud_id =001;

SELECT * from student;

delete from student where stud_id=001; 

select * from student where stud_id=001; 