import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CovidMapper
    extends Mapper<LongWritable, Text, Text, Text> {

	@Override
	public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    
	    String[] line = value.toString().toLowerCase().split(",");
	    if (line.length >1){
	    	if ((!line[1].equals("admin2")) && (!line[1].equals("unassigned")) && (!line[2].equals("diamond princess")) && (line[3].equals("us")) && (!line[1].equals("")) && (!line[2].equals(""))){
		   		String keyVal = line[1] + "!" + line[2];
		   		String result = line[7] + "!" + line[8];
		   		//key is county!state and value is confirmed_cases!deaths		
		    	context.write(new Text(keyVal), new Text(result)); 
		   	}
	    }
	}
}