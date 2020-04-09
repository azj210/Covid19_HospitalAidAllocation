import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.util.*;

public class HospCDMapper
    extends Mapper<LongWritable, Text, Text, Text> {
  
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    
    String[] line = value.toString().toLowerCase().split(",");
    String[] causes = {"death rate for copd patients", "death rate for pneumonia patients", "postoperative respiratory failure rate"};
    int endLine = (line.length - 1);   

    for (int i=0; i < causes.length; i++){
      if (causes[i].equals(line[9])){
        //indexes: death rate -5, denom -6, condition -8, county -11, state -13, city -14

        //get the state name from the abbreviated form
        String fullState = "not available";
        try{
          fullState = (String)STATE_MAP.get(line[endLine-13].toUpperCase()).toLowerCase();
        }
        catch (Exception e){

        }
        //setting the key value pair
        String locationRecord = line[endLine-14] + "!" + line[endLine-11] + "!" + fullState;
        String complicationRecord = line[endLine-6] + "!" + line[endLine-5];
        //key is city!county!state and value is patients!deaths of a particular complication for a hospital in a city!county!state
        context.write(new Text(locationRecord), new Text(complicationRecord));
        break;
      }
    }  
  } 
  //Dictionary of state_abbreviation, full state name
  public static final Map<String, String> STATE_MAP;
  static {
    STATE_MAP = new HashMap<String, String>();
    STATE_MAP.put("AL", "Alabama");
    STATE_MAP.put("AK", "Alaska");
    STATE_MAP.put("AZ", "Arizona");
    STATE_MAP.put("AR", "Arkansas");
    STATE_MAP.put("CA", "California");
    STATE_MAP.put("CO", "Colorado");
    STATE_MAP.put("CT", "Connecticut");
    STATE_MAP.put("DE", "Delaware");
    STATE_MAP.put("DC", "District Of Columbia");
    STATE_MAP.put("FL", "Florida");
    STATE_MAP.put("GA", "Georgia");
    STATE_MAP.put("GU", "Guam");
    STATE_MAP.put("HI", "Hawaii");
    STATE_MAP.put("ID", "Idaho");
    STATE_MAP.put("IL", "Illinois");
    STATE_MAP.put("IN", "Indiana");
    STATE_MAP.put("IA", "Iowa");
    STATE_MAP.put("KS", "Kansas");
    STATE_MAP.put("KY", "Kentucky");
    STATE_MAP.put("LA", "Louisiana");
    STATE_MAP.put("ME", "Maine");
    STATE_MAP.put("MD", "Maryland");
    STATE_MAP.put("MA", "Massachusetts");
    STATE_MAP.put("MI", "Michigan");
    STATE_MAP.put("MN", "Minnesota");
    STATE_MAP.put("MS", "Mississippi");
    STATE_MAP.put("MO", "Missouri");
    STATE_MAP.put("MT", "Montana");
    STATE_MAP.put("NE", "Nebraska");
    STATE_MAP.put("NV", "Nevada");
    STATE_MAP.put("MP", "Northern Mariana Islands");
    STATE_MAP.put("NH", "New Hampshire");
    STATE_MAP.put("NJ", "New Jersey");
    STATE_MAP.put("NM", "New Mexico");
    STATE_MAP.put("NY", "New York");
    STATE_MAP.put("NC", "North Carolina");
    STATE_MAP.put("ND", "North Dakota");
    STATE_MAP.put("OH", "Ohio");
    STATE_MAP.put("OK", "Oklahoma");
    STATE_MAP.put("OR", "Oregon");
    STATE_MAP.put("PA", "Pennsylvania");
    STATE_MAP.put("PR", "Puerto Rico");
    STATE_MAP.put("RI", "Rhode Island");
    STATE_MAP.put("SC", "South Carolina");
    STATE_MAP.put("SD", "South Dakota");
    STATE_MAP.put("TN", "Tennessee");
    STATE_MAP.put("TX", "Texas");
    STATE_MAP.put("UT", "Utah");
    STATE_MAP.put("VT", "Vermont");
    STATE_MAP.put("VI", "Virgin Islands");
    STATE_MAP.put("VA", "Virginia");
    STATE_MAP.put("WA", "Washington");
    STATE_MAP.put("WV", "West Virginia");
    STATE_MAP.put("WI", "Wisconsin");
    STATE_MAP.put("WY", "Wyoming");
  }
  
}








