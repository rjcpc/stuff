
package practical_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Practical_2 extends JFrame implements ActionListener 
{
    JLabel lblname,lblfname,lblphone,lblemail,lblgender,lblcity,lblAddress;
    JTextField name_txt,fname_txt,phone_txt,email_txt;
    JRadioButton male,female;
    JComboBox jcbcity;
    JTextArea add_txtArea,output_txtArea;
    JCheckBox chkbox;
    JButton submit_btn;
    Practical_2()
    {
        JLabel heading_lbl=new JLabel();
        heading_lbl.setBounds(250,5,200,40);
        heading_lbl.setText("<html><font><u><b>Registration form</b></u></html>");
        
       lblname=new JLabel("Name");
       lblname.setBounds(50,80,100,30);
       
       name_txt=new JTextField();
       name_txt.setBounds(180,80,180,30);
       
       lblfname=new JLabel("Father name");
       lblfname.setBounds(50,120,150,30);
       
       fname_txt=new JTextField();
       fname_txt.setBounds(180,120,180,30);
       
       lblgender=new JLabel("Gender");
       lblgender.setBounds(50,160,150,30);
       
       male=new JRadioButton("Male");
       male.setBounds(180,160,70,30);
       
        female=new JRadioButton("Female");
       female.setBounds(280,160,80,30);
       ButtonGroup gender_grp=new ButtonGroup();
       gender_grp.add(male);
       gender_grp.add(female);
       
       lblcity=new JLabel("City");
       lblcity.setBounds(50,200,100,30);
       
       String city[]={"Mumbai","Thane","Pune"};
       jcbcity=new JComboBox(city);
       jcbcity.setBounds(180,200,40,30);
       
       lblAddress=new JLabel("Address");
       lblAddress.setBounds(50,240,100,30);
       
       add_txtArea=new JTextArea();
       add_txtArea.setBounds(180,240,180,100);
       lblphone=new JLabel("Phone");
       lblphone.setBounds(50,350,100,30);
       
       phone_txt=new JTextField();
       phone_txt.setBounds(180,350,180,30);
       
       lblemail=new JLabel("Email");
       lblemail.setBounds(50,390,100,30);
       
       email_txt=new JTextField();
       email_txt.setBounds(180,390,180,30);
       
       chkbox=new JCheckBox("I accept the terms and conditions");
       chkbox.setBounds(50,430,300,30);
       
       submit_btn=new JButton("Submit");
       submit_btn.setBounds(180,500,120,40);
       
        output_txtArea=new JTextArea();
       output_txtArea.setBounds(500,80,500,320);
       
       add(heading_lbl);
       add(lblname);
       add(lblfname);
       add(lblgender);
       add(male);
       add(female);
       add(lblcity);
       add(lblAddress);
       add(lblphone);
       add(lblemail);
       add(name_txt);
       add(fname_txt);
       add(jcbcity);
       add(add_txtArea);
       add(phone_txt);
       add(email_txt);
       add(chkbox);
       add(submit_btn);
       add(output_txtArea);
      submit_btn.addActionListener(this);
      setSize(700,700);
      setVisible(true);
     }
 public void actionPerformed(ActionEvent e)
     {
         if(chkbox.isSelected()==true)
         {
             String name=name_txt.getText();
             String fname=fname_txt.getText();
             String gender="Male";
              if(female.isSelected()==true)
                  gender="Female";
              String city_name=(String)jcbcity.getSelectedItem();
              String add=add_txtArea.getText();
              String phone=phone_txt.getText();
              String email=email_txt.getText();
              output_txtArea.setText("Name: "+name+"\nFathers name: "+fname+"\nGender: "+gender+"\nDate of Birth: "+city_name+"\nAddress: "+add+"\nPhone"+phone+"\n Email"+email+"\n");
         }
         else{
             output_txtArea.setText("please go home");
         }
     } 
    public static void main(String args[]){
        new Practical_2();
    }
    
}