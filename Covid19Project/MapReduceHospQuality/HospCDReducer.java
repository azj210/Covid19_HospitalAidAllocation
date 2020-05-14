import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class HospCDReducer
    extends Reducer<Text, Text, Text, Text> {
  
  @Override
  public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {
    
    double totalCases = 0;
    double totalDeaths = 0;

    for (Text value : values) {
      if (!value.toString().contains("not available")){
        String[] calc = value.toString().split("!");
        //calculate total deaths from a particular case and add it to total deaths
        totalDeaths += Double.parseDouble(calc[0]) * (Double.parseDouble(calc[1]));
        //add cases from this particular case to total cases
        totalCases += Double.parseDouble(calc[0]);
      }
    }

    //larger negative deviation means more worse than national avg
    Double totalDeviation = (10.0684932586596 - ((totalDeaths / totalCases)) + 1);
    String formatDeviation = String.format("%.4f", totalDeviation);

    if (totalCases != 0) {
      //key is city!county!state and value is deviation of %deaths related to respiratory illness compared to the national average
      context.write(key, new Text(formatDeviation));
    }
    else{
      //complications data was not available
      context.write(key, new Text("not available"));
    }
  }
}




