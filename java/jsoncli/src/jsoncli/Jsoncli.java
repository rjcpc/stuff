/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package jsoncli;

import org.json.simple.JSONObject;
public class Jsoncli {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        JSONObject obj=new JSONObject();
        obj.put("name","rahul");
        obj.put("num", new Integer(100));
        obj.put("balance", new Double(100.99));
        obj.put("vip", new Boolean(true));
        
        System.out.println(obj);
        
        
    }
    
}
