/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package GetTime;

import javax.ejb.Stateless;
import java.util.Calendar;
import java.util.Date;
/**
 *
 * @author admin
 */
@Stateless
public class CalendarBean1 {

    private Calendar calendar;
    public CalendarBean1(){
            calendar=Calendar.getInstance();
            
                    }
    public Calendar getCalendar(){
    return calendar;
    
    }
    public Date getTime(){
    return calendar.getTime();
    }
    public int getHour(){
    return calendar.get( Calendar.HOUR_OF_DAY);
    
}
    public int getMinute(){
    return calendar.get( Calendar.MINUTE);
    
}
    public int getSecond(){
    return calendar.get( Calendar.SECOND);
    
}
}