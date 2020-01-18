<%-- 
    Document   : student
    Created on : Jan 18, 2020, 1:46:20 PM
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
        <jsp:useBean class="Student.StudentBean" id="students">
            <jsp:setProperty name="students" property="firstName" value="zara"></jsp:setProperty>
            <jsp:setProperty name="students" property="lastName" value="Ali" ></jsp:setProperty>
            <jsp:setProperty name="students" property="age" value="10" ></jsp:setProperty>
            
            
        </jsp:useBean>
        <p>first name:  <jsp:getProperty name="students" property="firstName"/></p>
         <p>last name: <jsp:getProperty name="students" property="lastName"/></p>
          <p>age:  <jsp:getProperty name="students" property="age"/></p>
    </body>
</html>
