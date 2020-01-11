<%-- 
    Document   : date
    Created on : Jan 11, 2020, 3:52:45 PM
    Author     : admin
--%>

<%@page import="java.util.Date"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
        Date d=new Date();
        out.print(d.toString());
        %>
    </body>
</html>
