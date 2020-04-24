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
		   		//new york city instead of new york county edge case
		   		if (line[1].equals("new york city")){
		   			String keyVal = "new york" + "!" + line[2];
		   			String res = String.format("%.2f",(Float.parseFloat(line[8]) / Float.parseFloat(line[7])) * 100);
			   		String result = line[7] + "!" + line[8] + "!" + res;
			   		//key is county!state and value is confirmed_cases!deaths		
			    	context.write(new Text(keyVal), new Text(result)); 
		   		}
		   		else{
		   			String keyVal = line[1] + "!" + line[2];
		   			if (line[7].equals("0")){
		   				String result = line[7] + "!" + line[8] + "!" + "0";
		   				//key is county!state and value is confirmed_cases!deaths!deathrate		
			    		context.write(new Text(keyVal), new Text(result)); 
		   			}
		   			else{
		   				String res = String.format("%.2f",(Float.parseFloat(line[8]) / Float.parseFloat(line[7])) * 100);
		   				String result = line[7] + "!" + line[8] + "!" + res;
		   				context.write(new Text(keyVal), new Text(result)); 
		   			}
		   		}
		   	}
	    }
	}
}