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

--declare procedure within a plsql block  and use it directly
declare
a number;
procedure square_it(x in out number) IS
begin
	x:=x*x;
	end;
begin
a:=23;
square_it(a);
DBMS_OUTPUT.PUT_LINE('square of  23  is '||a);
end;
/

--declare function
CREATE OR REPLACE FUNCTION TOTAL_IT
RETURN NUMBER
	IS TOTAL NUMBER(2):=0;
	BEGIN SELECT COUNT(*) INTO TOTAL FROM EMPLOYEE;
	RETURN TOTAL;
	END;
/
--use function within a plsql block
DECLARE
C NUMBER(2);
BEGIN
C:=TOTAL_IT();
DBMS_OUTPUT.PUT_LINE('Total number of employees is '||C);
END;
/


--declare function within a plsql block  and use it directly
DECLARE
A NUMBER;
B NUMBER;
C NUMBER;
FUNCTION FIND_MAX(X IN NUMBER, Y IN NUMBER)	
	RETURN NUMBER
	IS
	Z NUMBER; 
BEGIN
		IF X>Y THEN 
		Z:=X;
		ELSE
		Z:=Y;
	END IF;
	RETURN Z;
	END;
BEGIN
A:=44;
B:=55;
C:=FIND_MAX(A,B);
DBMS_OUTPUT.PUT_LINE('Maximum number is '||C);
END;
/


--RECURSIVE FUNCTION
DECLARE  
NUM NUMBER;
FACTORIAL NUMBER;
FUNCTION FACT(X NUMBER)
	RETURN NUMBER
	IS
	F NUMBER;
BEGIN
IF X=0 
	THEN
		F:=1;
	ELSE
		F:=X*FACT(X-1);
END IF;
RETURN F;
END;
BEGIN
NUM:=5;
FACTORIAL:=FACT(NUM);
DBMS_OUTPUT.PUT_LINE('Factorial OF  '|| NUM ||' IS '|| FACTORIAL);
END;
/

--SAVEPOINT DEMO
DECLARE
VAR_SAL EMP.SAL%TYPE;
BEGIN SELECT SAL INTO VAR_SAL FROM EMP WHERE EMPNO=7844;
DBMS_OUTPUT.PUT_LINE('Salary is '||VAR_SAL||'(ORIGINAL)');
--
UPDATE EMP SET SAL=SAL*1.1;
SELECT SAL INTO VAR_SAL FROM EMP WHERE EMPNO=7844;
DBMS_OUTPUT.PUT_LINE('Salary '||VAR_SAL||'(Before Savepoint A)');
SAVEPOINT A;
--
UPDATE EMP SET SAL=SAL*0.8;
SELECT SAL INTO VAR_SAL FROM EMP WHERE EMPNO=7844;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Savepoint A)');
SAVEPOINT B;
--
UPDATE EMP SET SAL=SAL*1.3;
SELECT SAL INTO VAR_SAL FROM EMP WHERE EMPNO=7844;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Savepoint B)');
ROLLBACK TO SAVEPOINT B;
--
SELECT SAL INTO VAR_SAL FROM EMP WHERE EMPNO=7844;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Rollback B)');
END;
/