package Samsung_Communication_Package;
import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Scanner;

public class TCP_Comms 
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
	
	public static int convert(int n) // return a HEX value
		{
		return Integer.valueOf(String.valueOf(n),16);
		}
	
	public void Construct_Transmission(String temp_app_name,String temp_ipaddress, String temp_remote_name, String temp_device_name) throws IOException
		{
		//TEMP_TV_STRING = "$00, $13, $00, 'iphone.iapp.samsung', $38, $00, $64, $00, $10, $00,'MTkyLjE2OC4xLjYy', $10, $00,'TG91bmdSZW1vdGU=', $10, $00, 'Q2hyaXNOZXRsaW54'"
		
		int HeaderString = convert(00); // convert to HEX
		int SpacerString = convert(00); // convert to HEX
		int MidHeaderString = convert(100); // convert to HEX 64
		String strI = "" + HeaderString;
		String strJ = "" + SpacerString;
		String strK = "" + MidHeaderString;
		String temp_app_name_ret = Encode_Base64(temp_app_name); //convert to Code64
		String temp_ipaddress_ret = Encode_Base64(temp_ipaddress); //convert to Code64				
		String temp_remote_name_ret = Encode_Base64(temp_remote_name); //convert to Code64
		String temp_device_name_ret = Encode_Base64(temp_device_name); //convert to Code64
		int Count1 = convert(temp_app_name.length()); // convert to HEX
		int Count2 = convert(temp_ipaddress_ret.length()); // convert to HEX
		int Count3 = convert(temp_remote_name_ret.length()); // convert to HEX
		int Count4 = convert(temp_device_name_ret.length()); // convert to HEX
		int Count5 = Count1 + Count2 + Count3 + Count4 + 8;
		String strA = "" + Count1;
		String strB = "" + Count2;
		String strC = "" + Count3;
		String strD = "" + Count4;
		String strE = "" + Count5;
		System.out.println( "String to send - " + strI + "," + strA + "," + strJ + "," + temp_app_name + "," + strE + "," + strJ + "," + strK + "," + strJ + "," + strB + "," + strJ + "," + temp_ipaddress_ret + "," + strC + "," + strJ + "," + temp_remote_name_ret + "," + strD + "," + strJ + "," + temp_device_name_ret );
		//                                        "$00,        $13,          $00,     'iphone.iapp.samsung',  $38,         $00,         $64,        $00,         $10,         $00,         'MTkyLjE2OC4xLjYy',        $10,         $00,  'TG91bmdSZW1vdGU=',     $10,         $00,   'Q2hyaXNOZXRsaW54'"		
		
		// construct transmission code
		//                    "$00, $13, $00, 'iphone.iapp.samsung', $38, $00, $64, $00, $10, $00,'MTkyLjE2OC4xLjYy', $10, $00,'TG91bmdSZW1vdGU=', $10, $00, 'Q2hyaXNOZXRsaW54'"
		//  SPC  CN4  SPC  CN4                    CN0           SPC   CN1  SPC 192.168.1.62        CN2  SPC LoungRemote        CN3   SPC  ChrisNetlinx
		//                                        CN0=CN1+CN2+CN3+08
		// try 
		// 
		}

	public void Authenticate(String temp_tvIP,int temp_tvport) throws IOException
		{
		//TEMP_TV_STRING = "$00, $13, $00, 'iphone.iapp.samsung', $38, $00, $64, $00, $10, $00,'MTkyLjE2OC4xLjYy', $10, $00,'TG91bmdSZW1vdGU=', $10, $00, 'Q2hyaXNOZXRsaW54'"
		String scData = "Authenticated";
		System.out.println( "Comms Reported - Authenticating to - " + temp_tvIP + " on port- " + temp_tvport );
		// construct transmission code
		//"$00, $13, $00, 'iphone.iapp.samsung', $38, $00, $64, $00, $10, $00,'MTkyLjE2OC4xLjYy', $10, $00,'TG91bmdSZW1vdGU=', $10, $00, 'Q2hyaXNOZXRsaW54'"
		//  SPC  CN4  SPC  CN4                    CN0           SPC   CN1  SPC 192.168.1.62        CN2  SPC LoungRemote        CN3   SPC  ChrisNetlinx
		//                                        CN0=CN1+CN2+CN3+08
		// try 
		// 
		Base64_Encoder obj2 = new Base64_Encoder();
		obj2.Encode_Base64(scData);
		//Socket TV_soc = new Socket(temp_tvIP,temp_tvport);
		//Socket TXDataSoc = TV_soc.accept();
		
		//PrintStream p = new PrintStream(TV_soc.getOutputStream());
		//p.println(scData);
		}
	public void Connect(String temp_tvIP,int temp_tvport) throws IOException
		{
		String scData = "Connect";
		System.out.println( "Comms Reported - Connecting to - " + temp_tvIP + " on port- " + temp_tvport );
		//Socket TV_soc = new Socket(temp_tvIP,temp_tvport);
		//PrintStream p = new PrintStream(TV_soc.getOutputStream());
		//p.println(scData);
		}
	public void PowerOnButton(String temp_tvIP,int temp_tvport) throws IOException
		{
		String scData = "Turning ON TV";
		System.out.println( "Comms Reported - " +scData);
		//Socket TV_soc = new Socket(temp_tvIP,temp_tvport);
		//PrintStream p = new PrintStream(TV_soc.getOutputStream());
		//p.println(scData);
		}	
	
	public void PowerOffButton(String temp_tvIP,int temp_tvport) throws IOException
		{
		String scData = "Turning OFF TV";
		System.out.println( "Comms Reported - " +scData);
		//Socket TV_soc = new Socket(temp_tvIP,temp_tvport);
		//PrintStream p = new PrintStream(TV_soc.getOutputStream());
		//p.println(scData);
		}	
	public void HDMI1Button(String temp_tvIP,int temp_tvport) throws IOException
		{
		String scData = "HDMI 1";
		System.out.println( "Comms Reported - " +scData +" selected");
		
		//Socket TV_soc = new Socket(temp_tvIP,temp_tvport);
		//PrintStream p = new PrintStream(TV_soc.getOutputStream());
		//p.println(scData);
		}	
	//TV_soc.close;
	}
		
	