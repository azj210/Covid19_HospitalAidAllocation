import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class HospBedMapper
    extends Mapper<LongWritable, Text, Text, IntWritable> {

	@Override
	public void map(LongWritable key, Text value, Context context)
	  throws IOException, InterruptedException {

		String[] line = value.toString().toLowerCase().split(",");
		for (int i = 0; i<line.length; i++){
			//when you encounter an int aka hospital beds then write
			try{
				int result = Integer.parseInt(line[i]);
				//key is city!state and value is hospital beds of this particular line aka hospital
				String keyVal = line[i-1] + "!" + line[line.length -1]; 
				context.write(new Text(keyVal), new IntWritable(result)); 
				break;	
			}
			catch(Exception e){

			}
		}
	}
}




