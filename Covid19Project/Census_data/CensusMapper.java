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
    String[] AGEGRP = {"13", "14", "15", "16", "17", "18"};
    //int endLine = (line.length - 1);   

    for (int i=0; i < AGEGRP.length; i++){
      if (line[5].equals("11") && line[6].equals(AGEGRP[i])){
        //indexes: STNAME -3, CTYNAME -4, YEAR -5, AGEGRP -6, TOT_POP -7, TOT_MALE -8

        
        //setting the key value pair
        String ST_CTY = line[3] + "!" + line[4];
        String TotPop_and_Male = line[7] + "!" + line[8];
        
        context.write(new Text(ST_CTY), new Text(TotPop_and_Male));
        break;
      } 
    } 
  
  }
  
}








