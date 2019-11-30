/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package practicle6;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;

/**
 *
 * @author admin
 */
public class Practicle6 extends JFrame implements ActionListener{
    JTextField t1,t2,t3,t4;
    JButton b1,b2;
    Container c;
    JLabel l1,l2,l3,l4;
    String rows[][]=new String[10][4];
    String cols[]={"Name","DOB","Address","Contactno"};
    JTable tb;
    JScrollPane jsp;
    
    public Practicle6()
    {c=getContentPane();
    c.setLayout(new FlowLayout());
    l1=new JLabel("Name");
    l2=new JLabel("date of birth");
    l3=new JLabel("address");
    l4=new JLabel("telephone no:");
    t1=new JTextField(10);
    t2=new JTextField(10);
    t3=new JTextField(10);
    t4=new JTextField(10);
    b1=new JButton("insert");
    b2=new JButton("show all");
    c.add(l1);
    c.add(t1);
    c.add(l2);
    c.add(t2);
    c.add(l3);
    c.add(t3);
    c.add(l4);
    c.add(t4);
    c.add(b1);
    c.add(b2);
    b1.addActionListener(this);
    b2.addActionListener(this);
    }
    public void actionPerformed(ActionEvent ae)
    {
        Connection con;
        Statement st;
        try
        {
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            con=DriverManager.getConnection("jdbc:odbc:test","system","system");
            st=con.createStatement();
            String s1="",s2="",s3="",s4="";
            s1=t1.getText();
            s2=t2.getText();
            s3=t3.getText();
            s4=t4.getText();
            
            if(ae.getSource()==b1)
            {st.executeUpdate("insert into frnds1  values('"+s1+"','"+s2+"','"+s3+"',"+s4+")");
            System.out.println("Record inserted");
            t1.setText("");
            t2.setText("");
            t3.setText("");
            t4.setText("");
            l1.requestFocus();
            }
            
            if(ae.getSource()==b2)
            {
                ResultSet rs=st.executeQuery("select*from frnds1");
                ResultSetMetaData rsmd=rs.getMetaData();
                System.out.println(rsmd.getColumnCount());
                int i=0,j;
                while(rs.next())
                {
                    for(j=0;j<rsmd.getColumnCount();j++)
                    {
                        rows[i][j]=rs.getString(j+1);
                    }
                    i++;
                }
                tb=new JTable(rows,cols);
                jsp=new JScrollPane(tb);
                c.add(jsp);
                System.out.println("table inserted");
            }}
        catch(Exception e)
        {
            System.out.println(e);
            e.printStackTrace();
        }}
    
    public static void main(String[] args) {
    Practicle6 m=new Practicle6();
    m.setSize(500,500);
    m.setVisible(true);    // TODO code application logic here
}
    
}
