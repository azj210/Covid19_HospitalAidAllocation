import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CensusReducer
    extends Reducer<Text, Text, Text, Text> {
  
    @Override
    public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {

        int totalPOP = 0;
        int totalMale = 0;

        for (Text value : values) {
            String[] calc = value.toString().split("!");
            //calculate total population
            totalPOP += Integer.parseInt(calc[0]);
            //calculate total male population
            totalMale += Integer.parseInt(calc[1]);
        }

        String TotPop_and_Male = Integer.toString(totalPOP) + "!" +  Integer.toString(totalMale);
        //key is STNAME!CTYNAME and value is TOT_POP!TOT_MALE of a everyone in the 60+ age group range for a particular STNAME!CTYNAME
        context.write(key, new Text(TotPop_and_Male));
     
    }
}




