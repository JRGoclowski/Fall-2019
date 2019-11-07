package cecs378.IpProject;

import java.time.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.*; 
import java.util.*; 


public class Main {
	
	public static void main(String args[]) throws UnknownHostException {
		List<String> lines = new ArrayList<String>();
		String dateTime = LocalDateTime.now().toString();
		lines.add(dateTime);
		InetAddress localhost = InetAddress.getLocalHost();
		lines.add("local IP");
		lines.add((localhost.getHostAddress()).trim()); 

	    // Find public IP address 
	    String systemipaddress = ""; 
	    try
	    { 
	        URL url_name = new URL("http://bot.whatismyipaddress.com"); 

	        BufferedReader sc = new BufferedReader(new InputStreamReader(url_name.openStream())); 

	        // reads system IPAddress 
	        systemipaddress = sc.readLine().trim(); 
	    } 
	    catch (Exception e) 
	    { 
	        systemipaddress = "Cannot Execute Properly"; 
	    } 
	    lines.add("Public IP");
	    lines.add(systemipaddress);
	    Path file = Paths.get("Collections.txt");
	    try {
			Files.write(file, lines, StandardCharsets.UTF_8);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	} 
}
   
/*
 * List<String> lines = Arrays.asList("The first line", "The second line");
Path file = Paths.get("the-file-name.txt");
Files.write(file, lines, StandardCharsets.UTF_8);
//Files.write(file, lines, StandardCharsets.UTF_8, StandardOpenOption.APPEND);*/

