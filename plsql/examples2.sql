--create sequence example
create sequence student_id
increment by 5
start with 100
maxvalue 9999
nocache
nocycle;

--create sequence example
create sequence student_no
increment by 1
start with 1
maxvalue 80
nocache;

--get sequences from user_objects
select * from user_objects
where object_type='SEQUENCE';

--get sequences from user_sequences
select sequence_name,min_value,max_value,increment_by,last_number
from user_sequences;

--refer sequence by nextval
insert into employee values ('a',null,student_id.nextval);
/* 
E_NAME               DATE_OF_J     SALARY
-------------------- --------- ----------
a                                     100
a                                     105
a                                     110
a                                     115
a                                     120
a                                     125
a                                     130
a                                     135
a                                     140
a                                     145
 */

--refer sequence by currval

SELECT STUDENT_NO.CURRVAL FROM DUAL;
--refer sequence by currval
SELECT STUDENT_ID.CURRVAL FROM DUAL;


--alter sequence
alter sequence student_id
increment by 2
maxvalue 999
nocache
nocycle;


--create or replace procedures
CREATE OR REPLACE PROCEDURE GREETINGS
AS
BEGIN
DBMS_OUTPUT.PUT_LINE('Hello');
END;
/
--execute above procedure
EXECUTE GREETINGS;
--also
BEGIN
	GREETINGS;
END;
/


--declare procedure within a plsql block
declare
a number;
b number;
c number;
procedure find_min(x in number, y in number, z out number) IS
begin
	if x<y then
		z:=x;
	else
		z:=y;
	end if;
	end;
begin
a:=23;
b:=45;
find_min(a,b,c);
DBMS_OUTPUT.PUT_LINE('Minimum of 23 and 45 is '||c);
end;
/

