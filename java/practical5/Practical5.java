
package practical5;

import java.sql.*;
import java.io.*;


public class Practical5 {

    
    public static void main(String[] args) {
        try{
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            Connection con = DriverManager.getConnection("jdbc:odbc:test", "system", "server");
            BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
            String str;
            str = br.readLine();
            Statement st= con.createStatement();
            ResultSet rs = st.executeQuery(str);
            ResultSetMetaData rsmd = rs.getMetaData();
            
            for(int i=1;i<=rsmd.getColumnCount();i++){
                System.out.print(rsmd.getColumnName(i)+"\t");
            }
            System.out.println();
            while (rs.next()){
                for (int j=1;j<=rsmd.getColumnCount();j++){
                    System.out.print(rs.getString(j)+"\t");
                }
                System.out.println();
            }
            
        }catch (Exception e){
            System.out.println(e);
            e.printStackTrace();
        }
    }
    
}
