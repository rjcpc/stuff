import java.awt.*;
import java.awt.event.*;
public class EvenOdd extends Frame implements ActionListener{
	Label lblnum ,lblresult;
	TextField txtnum;
	Button btnDisplay;
	EvenOdd(){
		setLayout(new FlowLayout());
		lblnum=new Label("ENTER NUMBER : ");
		lblresult=new Label("");
		txtnum=new TextField();
		btnDisplay=new Button("EVEN/ODD");
		
		add(lblnum);
		
		add(txtnum);
		add(btnDisplay);
		add(lblresult);
		btnDisplay.addActionListener(this);
		setSize(600,300);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent  e){
		int num=Integer.parseInt(txtnum.getText());
		if (e.getSource()==btnDisplay){
			if (num%2==0){
				lblresult.setText("THE NUMBER IS EVEN");
			}else{
				lblresult.setText("THE NUMBER IS ODD ");
			}
		}
	}
	public static void main(String[] args){
		new EvenOdd();
	}
	
}
