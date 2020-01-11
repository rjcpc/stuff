<%-- 
    Document   : dept
    Created on : Jan 11, 2020, 2:59:06 PM
    Author     : admin
--%>
<%@page import="java.sql.*"
contentType="text/html"
pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            try{
                int dno=Integer.parseInt(request.getParameter("t1"));
                String dname=request.getParameter("t2");
                String dloc=request.getParameter("t3");
                Connection conn;
                Statement st;
                Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
                conn=DriverManager.getConnection("Jdbc:Odbc:test","system","server");
                st=conn.createStatement();
                System .out.println( dno+" , "+dname+" , "+dloc);
                st.executeUpdate("insert into dept values ("+dno+" ,'"+dname+" ', '"+dloc+"' );");
                
                out.println("number : "+dno+"<br>");
                out.println("name : "+dname+"<br>");
                out.println("location : "+dloc+"<br>");
                out.println("done");
            }catch(Exception e){
                
            System.out.println(e);
            }
            %>
    </body>
</html>
