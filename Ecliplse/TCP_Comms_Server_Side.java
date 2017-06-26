package Samsung_Communication_Package;

import java.io.IOException;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class TCP_Comms_Server_Side
	{
	public static void main(String[] tvIP, int tvPort) throws IOException 
		{
		String txData, temp;
		ServerSocket scTx = new ServerSocket(tvPort);
		Socket ss = scTx.accept();
		Scanner sc = new Scanner(ss.getInputStream());
		txData = sc.next();
		temp = "Authenticated";
		PrintStream p = new PrintStream(ss.getOutputStream());
		p.println(temp);
		}
}
