
package Student;

import javax.ejb.Stateless;

@Stateless
public class StudentBean implements java.io.Serializable{
 private String firstName=null;
 private String lastName=null;
 private int age=0;

    public StudentBean() {
        
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
   
}
