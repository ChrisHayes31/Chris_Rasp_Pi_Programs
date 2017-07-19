package Samsung_Communication_Package;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
//import com.sun.org.apache.xerces.internal.impl.dv.util.Base64;

public class Base64_Encoder 
	{
	public String Encode_Base64(String temp_b64encode) throws IOException
		{
		final String text = temp_b64encode;
		//final String text = "Base64 finally in Java 8!";
		final String encoded = Base64
			.getEncoder()
			.encodeToString( text.getBytes( StandardCharsets.UTF_8 ) );
		return encoded;
		//System.out.println( encoded );;
		}

	public void Decode_Base64(String temp_b64decode) throws IOException
		{
		final String decoded = new String(
			Base64.getDecoder().decode( temp_b64decode ),
			StandardCharsets.UTF_8 );
		System.out.println( decoded );
		}	
	}
