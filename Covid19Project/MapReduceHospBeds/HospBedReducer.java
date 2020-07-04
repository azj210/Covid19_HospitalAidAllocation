import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class HospBedReducer
    extends Reducer<Text, IntWritable, Text, IntWritable> {
  
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException {

        int totalValue = 0;
        for (IntWritable value : values) {
            totalValue += value.get();
        }
        //key is city!state and value is hospital beds for all hospitals in that city!state
        context.write(key, new IntWritable(totalValue));
    }
}




