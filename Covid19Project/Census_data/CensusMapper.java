import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.util.*;

public class CensusMapper
    extends Mapper<LongWritable, Text, Text, Text> {
  
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    
    String[] line = value.toString().toLowerCase().split(",");
    String[] AGEGRP = {"12", "13", "14", "15", "16", "17", "18"};

    for (int i=0; i < AGEGRP.length; i++){
      if (line[5].equals("11") && line[6].equals(AGEGRP[i])){
        //indexes: STNAME -3, CTYNAME -4, YEAR -5, AGEGRP -6, TOT_POP -7, TOT_MALE -8
        //setting the key value pair
        if ((line[4].equals("kings county") || line[4].equals("queens county") || line[4].equals("bronx county")) && line[3].equals("new york")){
          line[4] = "new york county";
        }
        String ST_CTY = line[3] + "!" + line[4].substring(0,line[4].length()-7);
        String TotPop_and_Male = line[7] + "!" + line[8];
        //key is STNAME!CTYNAME and value is TOT_POP!TOT_MALE of a particular age group in the 55+ age group range
        context.write(new Text(ST_CTY), new Text(TotPop_and_Male));
        break;
      } 
    } 
  }
}




