import java.util.HashMap;
import java.util.Set;

public class TrackList {
    public static void main(String[] args) {
        HashMap<String, String> trackList = new HashMap<String, String>();
        trackList.put("Panini", "Daytrip took it to 10 (hey) Ayy, Panini, don't you be a meanie Thought you wanted me to go up");
        trackList.put("Better", "Nothin' feels better than this Nothin' feels better Nothin' feels better than this");
        trackList.put("Monkey in the grave", "When I die, put my money in the grave I really gotta put a couple niggas in they place Really just lapped every nigga in the race");
        trackList.put("No Guidance", "I don't wanna play no games, play no games Fuck around, give you my last name (oh) Know you tired of the same damn thing");
        Set<String> keys = trackList.keySet();
        for (String key : keys) {
            System.out.println(key + ": " + trackList.get(key));
        }
    
    }
}