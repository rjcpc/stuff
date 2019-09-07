/*
======= SHORTEST SEEK-TIME FIRST ===========
Traversing from:53
to track : 65:12
to track : 67:2
to track : 37:30
to track : 14:23
to track : 98:84
to track : 122:24
to track : 124:2
to track : 183:59
Total cylinders traversed = 236
*/
import java.io.*;    
class DevMgmt{  
    String disk_sequence;  
    DevMgmt(String fs){  
        disk_sequence = fs;  
    }  
    void sstf(int start_track){  
        System.out.println("======= SHORTEST SEEK-TIME FIRST ===========");  
        String disknums[] = disk_sequence.split(" ");  
        int tracks[] = new int[disknums.length];  
        boolean tracks_bool[] = new boolean[disknums.length];  
        int min_dist=0,max_dist=0;  
        for(int i=0; i<disknums.length; i++){  
            tracks[i] = Integer.parseInt(disknums[i]);  
            tracks_bool[i] = false;  
            max_dist = max_dist+tracks[i];  
        }  
        min_dist = max_dist;  
        int total_cylinders=0,from_track=start_track,current_track_index=-1;  
        System.out.println("Traversing from:" + from_track);  
        for(int i=0; i<tracks.length; i++){  
            int to_track_index=0;  
            for(int t=0; t<tracks.length;t++){  
                if((!tracks_bool[t]) && (Math.abs(from_track-tracks[t])<min_dist) && (t!=current_track_index)){  
                    to_track_index=t;  
                    min_dist = Math.abs(from_track-tracks[t]);  
                }  
            }  
            System.out.println("to track : " + tracks[to_track_index] +":" + min_dist);  
            total_cylinders+= Math.abs(from_track-tracks[to_track_index]);  
            tracks_bool[to_track_index] = true;  
            from_track = tracks[to_track_index];  
            current_track_index=to_track_index;  
            min_dist=max_dist;  
        }  
        System.out.println("Total cylinders traversed = " + total_cylinders);  
    }  
}    
class SSTF{  
    public static void main(String args[]) throws Exception{  
    String disk_sequence = "98 183 37 122 14 124 65 67";  
    int track = 53;  
    DevMgmt m = new DevMgmt(disk_sequence);  
    m.sstf(track);  
}  
}  
