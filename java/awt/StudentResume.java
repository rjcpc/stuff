import java.awt.*;
import java.awt.Font;
public class StudentResume extends Frame{
	Button btnSubmit;
	Label lblName ,lblAge ,lblAddr ,lblGender ,lblQua;
	TextField txtName,txtAge;
	TextArea txtAddr;
	CheckboxGroup ChkGrp;
	Checkbox ChkMale,ChkFemale;
	Checkbox ChkMca ,ChkBca ,ChkBba ,ChkMba;
	StudentResume(){
		setLayout(new FlowLayout());
		lblName=new Label("NAME : ");
		lblAge=new Label("AGE : ");
		lblAddr=new Label("ADDRESS : ");
		lblGender=new Label("GENDER : ");
		lblQua=new Label("QUALIFICATION : ");
		txtAge=new TextField(20);
		txtName=new TextField(20);
		txtAddr=new TextArea();
		ChkGrp=new CheckboxGroup();
		ChkMale=new Checkbox("MALE ",ChkGrp,false);
		ChkFemale=new Checkbox("FEMALE",ChkGrp,false);
		ChkMca=new Checkbox("MCA");
		ChkBca=new Checkbox("BCA");
		ChkBba=new Checkbox("BBA");
		ChkMba=new Checkbox("MBA");
		btnSubmit=new Button("SUBMIT ");
		// add everything to window
		add(lblName);
		add(txtName);
		add(lblAge);
		add(txtAge);
		add(lblAddr);
		add(txtAddr);
		add(lblGender);
		add(ChkMale);
		add(ChkFemale);
		add(lblQua);
		add(ChkMca);
		add(ChkBca);
		add(ChkBba);
		add(ChkMba);
		add(btnSubmit);
		setSize(500, 500);
		setVisible(true);
		
	}
	public static void main(String[] args){
		new StudentResume();
	}
}