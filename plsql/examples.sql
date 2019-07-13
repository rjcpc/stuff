	--template
	declare
	-- prompt
		n integer:='&number';
	begin
	--print 
		dbms_output.put_line(to_char(n)||' is prime number');

	end;
	/

--basic loop

declare
V_NUM number(5):=10;
begin
loop
DBMS_OUTPUT.PUT_LINE(V_NUM);
V_NUM :=V_NUM+10;
exit when V_NUM>=100;
end loop;
end;
/

--for loop

declare
V_NUM number(5):=1;
begin
for i in 1..20
loop
DBMS_OUTPUT.PUT_LINE(V_NUM);
V_NUM :=V_NUM+2;
end loop;
end;
/

--reverse loop


begin
for i in reverse 1..20
loop
DBMS_OUTPUT.PUT_LINE(i);
end loop;
end;
/


--insert  data in table
declare
v_part_id part_details.part_id %type:='&part_id';
v_counter number(2):=1;
begin
for i in  1..10
loop
v_counter:=i;
insert into part_details (part_id,subpart_id)
values (v_part_id,v_counter);
end loop;
end;
/

--odd numbers while loop
declare
v_counter number(2) :=1;
v_number number(2):=1;

begin
dbms_output.put_line('before loop: counter='||to_char(v_counter));
dbms_output.put_line('before loop: number='||to_char(v_number));
dbms_output.put_line('#############################');
while (v_counter<=10)
loop
dbms_output.put_line(to_char(v_number));
v_counter:=v_counter+1;
v_number:=v_number+2;

end loop;
dbms_output.put_line('#############################');
dbms_output.put_line('after loop: counter='||to_char(v_counter));
dbms_output.put_line('after loop: number='||to_char(v_number));
end;
/

--loop in a table
declare
v_part_id part_details.part_id %type:=50;
v_counter number(2):=0;
begin
loop
insert into part_details(part_id,subpart_id) values(v_part_id,v_counter);
v_counter:=v_counter+1;
if v_counter>10 then
exit;
end if;
end loop;
end;
/

--prime number checking
declare
p integer;
n integer:='&number';
begin
for i in 2..round(sqrt(n))
loop
if n mod i=0 then
p:=0;
goto print_data;
end if;
end loop;
p:=1;
	<<print_data>>
	if p=1 then
	dbms_output.put_line(to_char(n)||' is prime number');
	else
	dbms_output.put_line(to_char(n)||' is not prime number');
	end if;
end;
/


--AREA AND PERIMETER OF CIRCLE AND SQUARE
declare
mathpi number(5,2):=3.14;
area_c number(7,2):=null;
area_s number(7,2):=null;
peri_s number(7,2):=null;
peri_c number(7,2):=null;
radius number(7):='&radius';
side number(7):='&side';
begin
area_c:=mathpi*radius*radius;
area_s:=side*side;
peri_c:=2*mathpi*radius;
peri_s:=4*side;
dbms_output.put_line('###############################');
dbms_output.put_line('Area of circle is : '||area_c);
dbms_output.put_line('Area of square is : '||area_s);
dbms_output.put_line('Perimeter of circle is : '||peri_c);
dbms_output.put_line('Perimeter of square is : '||peri_s);
end;
/




