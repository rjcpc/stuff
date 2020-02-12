notification :

a notification is a message you can display to the user
when you tell the system to issue a notification it first appears as an icon in their 
notification area to see the details of the notification the user opens the notification drawer 
both the notification area and the notification drawer are system-controlled areas 
that the user can view at any time



create and send a notification :

step 1:

create notification builder 
as the first step is to create a notification builder using notificationcompatbuilder

step 2:

notification properties once you have builder object 
you can set its notification properties using builder object as per your requirement 
a small icon set by setsmallicon
a title set by setcontenttitle

step3:

issue the notification finally you pass the notification object 
to the system by calling notificationmanager.notify() to send your notification
make sure you callnotificationcompatbuilser.build method on builder object before notifying it
this method combines all of the options that have been set and return a new notification object





alarm manager:

android alarm manager allows you to access system alarm
by the help of androidalarmamnager you can schedule your application 
to run at a specific time in the future it works whether your phone is running or not

methods:

set:
schedule an alarm for one time

set repeating:
schedules an alarm with exact repeating time 

set time:
set the system walllclocktime
