--trigger
-- set serveroutput on

create or replace trigger display_salary_change --triggername
before delete or insert or update on emp --tablename
for each row
when ( NEW.empno > 0 ) --columnname
declare
sal_diff number;
begin
sal_diff:= :NEW.sal -:OLD.sal;
DBMS_OUTPUT.PUT_LINE('Old salary:'|| :OLD.sal);
DBMS_OUTPUT.PUT_LINE('New salary : '|| :NEW.sal);
DBMS_OUTPUT.PUT_LINE('Salary difference: '|| sal_diff);
end;
/



--SAVEPOINT DEMO
DECLARE
VAR_SAL EMP.SAL%TYPE;
BEGIN SELECT SAL INTO VAR_SAL 
FROM EMP
WHERE EMPNO=5;
DBMS_OUTPUT.PUT_LINE('Salary is '||VAR_SAL||'(ORIGINAL)');
--
UPDATE EMP SET SAL=SAL*1.1;
SELECT SAL INTO VAR_SAL 
FROM EMP 
WHERE EMPNO=5;
DBMS_OUTPUT.PUT_LINE('Salary '||VAR_SAL||'(Before Savepoint A)');
SAVEPOINT A;
--
UPDATE EMP SET SAL=SAL*0.8;
SELECT SAL INTO VAR_SAL 
FROM EMP 
WHERE EMPNO=5;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Savepoint A)');
SAVEPOINT B;
--
UPDATE EMP SET SAL=SAL*1.3;
SELECT SAL INTO VAR_SAL 
FROM EMP 
WHERE EMPNO=5;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Savepoint B)');
ROLLBACK TO SAVEPOINT B;
--
SELECT SAL INTO VAR_SAL 
FROM EMP 
WHERE EMPNO=5;
DBMS_OUTPUT.PUT_LINE('Salary :'||VAR_SAL||'(Rollback B)');
END;
/
--output
/*
Salary is 3000(ORIGINAL)
Old salary:2000
New salary : 2200
Salary difference: 200
Old salary:2000
New salary : 2200
Salary difference: 200
Old salary:3000
New salary : 3300
Salary difference: 300
Old salary:4000
New salary : 4400
Salary difference: 400
Old salary:5000
New salary : 5500
Salary difference: 500
Old salary:6000
New salary : 6600
Salary difference: 600
Salary 3300(Before Savepoint A)
Old salary:2200
New salary : 1760
Salary difference: -440
Old salary:2200
New salary : 1760
Salary difference: -440
Old salary:3300
New salary : 2640
Salary difference: -660
Old salary:4400
New salary : 3520
Salary difference: -880
Old salary:5500
New salary : 4400
Salary difference: -1100
Old salary:6600
New salary : 5280
Salary difference: -1320
Salary :2640(Savepoint A)
Old salary:1760
New salary : 2288
Salary difference: 528
Old salary:1760
New salary : 2288
Salary difference: 528
Old salary:2640
New salary : 3432
Salary difference: 792
Old salary:3520
New salary : 4576
Salary difference: 1056
Old salary:4400
New salary : 5720
Salary difference: 1320
Old salary:5280
New salary : 6864
Salary difference: 1584
Salary :3432(Savepoint B)
Salary :2640(Rollback B)

PL/SQL procedure successfully completed.
*/