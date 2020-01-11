<%-- 
    Document   : newjsp
    Created on : Jan 11, 2020, 2:54:30 PM
    Author     : admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <form name="f1" method="get" action="dept.jsp">
                    Enter the department number : 
                    <input type="text" name="t1">    
                    <br> 
                    Enter the department name : 
                    <input type="text" name="t2">       
                    <br> 
                    Enter the department location : 
                    <input type="text" name="t3">        
                    <br> 
                    <input type="submit" value="submit">
        </form>
   
    </body>
</html>
