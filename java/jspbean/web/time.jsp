<%-- 
    Document   : time
    Created on : Jan 11, 2020, 3:58:18 PM
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
        <jsp:useBean class="GetTime.CalendarBean1" id="cal"/>
        <pre>
                time : <jsp:getProperty name="cal" property="time" /><br>
                hour : <jsp:getProperty name="cal" property="hour" /><br>
                minute : <jsp:getProperty name="cal" property="minute" /><br>
                second : <jsp:getProperty name="cal" property="second" /><br>
        </pre>
    </body>
</html>
