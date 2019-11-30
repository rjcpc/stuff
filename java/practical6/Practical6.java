
package practical6;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;


public abstract class Practical6 extends JFrame implements ActionListener{
    
    JTextField t1, t2, t3, t4;
    JButton b1, b2;
    Container c;
    JLabel l1,l2,l3,l4;
    String rows[][]=new String[10][4];
    String cols[]={"Name","DOB","Address","ContactNo"};
    JTable tb;
    JScrollPane jsp;
    public Practical6(){
        c=getContentPane();
        c.setLayout(new FlowLayout());
        l1=new JLabel("Name : ");
        l2=new JLabel("Date Of Birth : ");
        l3=new JLabel("Address : ");
        l4=new JLabel("Telephone No : ");
        t1=new JTextField(10);
        t2=new JTextField(10);
        t3=new JTextField(10);
        t4=new JTextField(10);
        b1=new JButton("Insert");
        b2=new JButton("Show All");
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
    public void actionPerformed(ActionEvent ae){
        Connection con;
        Statement st;
        try{
            Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
            con=DriverManager.getConnection("jdbc:odbc:test","system","server");
            st=con.createStatement();
            String s1="",s2="",s3="",s4="";
            s1=t1.getText();
            s2=t2.getText();
            s3=t3.getText();
            s4=t4.getText();
            
            if (ae.getSource()==b1){
                st.executeUpdate("insert into friends values ('"+s1+"','"+s2+"','"+s3+"','"+s4+"')");
                System.out.println("Record Inserted");
                t1.setText("");
                t2.setText("");
                t3.setText("");
                t4.setText("");
                t1.setText("");                
            }
            if (ae.getSource()==b2){
                ResultSet rs=st.executeQuery("Select * from friends");
                ResultSetMetaData rsmd=rs.getMetaData();
                System.out.println(rsmd.getColumnCount());
                int i=0, j;
                while (rs.next()){
                    for(j=0; j<=rsmd.getColumnCount(); j++){
                    System.out.print("|"+rs.getString(j)+"\t|");
                }//for end
                i++;
            }//while end
            tb = new JTable(rows, cols);
            jsp=new JScrollPane(tb);
            c.add(jsp);
            System.out.println("Table Inserted");
            }//if end
        }//try end
        catch(Exception e){
                System.out.println(e);
                e.printStackTrace();
        }//catch end
        
    }

    
    public static void main(String[] args) {
        Practical6 m = new Practical6() {};
        m.setSize(500, 500);
        m.setVisible(true);
        
    }
    
}
