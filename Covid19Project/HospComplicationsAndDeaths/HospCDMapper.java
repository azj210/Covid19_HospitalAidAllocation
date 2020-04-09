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
          fullState = (String)GetState.get(line[endLine-13].toUpperCase()).toLowerCase();
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
public string GetState(State state)
    {
        switch (state)
        {
            case State.AL:
                return "ALABAMA";

            case State.AK:
                return "ALASKA";

            case State.AS:
                return "AMERICAN SAMOA";

            case State.AZ:
                return "ARIZONA";

            case State.AR:
                return "ARKANSAS";

            case State.CA:
                return "CALIFORNIA";

            case State.CO:
                return "COLORADO";

            case State.CT:
                return "CONNECTICUT";

            case State.DE:
                return "DELAWARE";

            case State.DC:
                return "DISTRICT OF COLUMBIA";

            case State.FM:
                return "FEDERATED STATES OF MICRONESIA";

            case State.FL:
                return "FLORIDA";

            case State.GA:
                return "GEORGIA";

            case State.GU:
                return "GUAM";

            case State.HI:
                return "HAWAII";

            case State.ID:
                return "IDAHO";

            case State.IL:
                return "ILLINOIS";

            case State.IN:
                return "INDIANA";

            case State.IA:
                return "IOWA";

            case State.KS:
                return "KANSAS";

            case State.KY:
                return "KENTUCKY";

            case State.LA:
                return "LOUISIANA";

            case State.ME:
                return "MAINE";

            case State.MH:
                return "MARSHALL ISLANDS";

            case State.MD:
                return "MARYLAND";

            case State.MA:
                return "MASSACHUSETTS";

            case State.MI:
                return "MICHIGAN";

            case State.MN:
                return "MINNESOTA";

            case State.MS:
                return "MISSISSIPPI";

            case State.MO:
                return "MISSOURI";

            case State.MT:
                return "MONTANA";

            case State.NE:
                return "NEBRASKA";

            case State.NV:
                return "NEVADA";

            case State.NH:
                return "NEW HAMPSHIRE";

            case State.NJ:
                return "NEW JERSEY";

            case State.NM:
                return "NEW MEXICO";

            case State.NY:
                return "NEW YORK";

            case State.NC:
                return "NORTH CAROLINA";

            case State.ND:
                return "NORTH DAKOTA";

            case State.MP:
                return "NORTHERN MARIANA ISLANDS";

            case State.OH: 
                return "OHIO";

            case State.OK:
                return "OKLAHOMA";

            case State.OR:
                return "OREGON";

            case State.PW:
                return "PALAU";

            case State.PA:
                return "PENNSYLVANIA";

            case State.PR:
                return "PUERTO RICO";

            case State.RI:
                return "RHODE ISLAND";

            case State.SC:
                return "SOUTH CAROLINA";

            case State.SD:
                return "SOUTH DAKOTA";

            case State.TN:
                return "TENNESSEE";

            case State.TX:
                return "TEXAS";

            case State.UT:
                return "UTAH";

            case State.VT:
                return "VERMONT";

            case State.VI:
                return "VIRGIN ISLANDS";

            case State.VA:
                return "VIRGINIA";

            case State.WA:
                return "WASHINGTON";

            case State.WV:
                return "WEST VIRGINIA";

            case State.WI:
                return "WISCONSIN";

            case State.WY:
                return "WYOMING";
        }

        throw new Exception("Not Available");
    }
}
}








