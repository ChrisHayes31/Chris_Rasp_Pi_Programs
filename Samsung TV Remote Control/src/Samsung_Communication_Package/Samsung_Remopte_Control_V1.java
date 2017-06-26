package Samsung_Communication_Package;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.awt.event.ActionEvent;


public class Samsung_Remopte_Control_V1 
	{
	private JFrame frmTelevisionRemoteControl;
	public static void main(String[] args) 
		{
		EventQueue.invokeLater(new Runnable()	
			{
			public void run() 
				{
				try 
					{
					Samsung_Remopte_Control_V1 window = new Samsung_Remopte_Control_V1();
					window.frmTelevisionRemoteControl.setVisible(true);
					} 
				catch (Exception e) 
					{
					e.printStackTrace();
					}
				}
			});
	}

	/**
	 * Create the application.
	 */
	public Samsung_Remopte_Control_V1() 
		{
		initialize();
		}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() 
		{
		String temp_app_name = "iphone.iapp.raspberrypi";
		String temp_ipaddress = "127.0.0.1";
		String temp_remote_name = "Local Remote";
		String temp_device_name = "raspberrypi";
		frmTelevisionRemoteControl = new JFrame();
		frmTelevisionRemoteControl.setTitle("TV Remote Control");
		frmTelevisionRemoteControl.setBounds(100, 100, 321, 418);
		frmTelevisionRemoteControl.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTelevisionRemoteControl.getContentPane().setLayout(null);
		
		JButton btnPowerButton = new JButton("Power");
		btnPowerButton.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent e) 
				{
				try
					{
					String serverHostname;
					int serverPortNumber;
					System.out.println( "Turning TV Power Off" );
					serverHostname = ("192.168.1.62");
					serverPortNumber = 55000;
					TCP_Comms obj1 = new TCP_Comms();
					//obj1.Authenticate("192.168.1.62", 55000);
					obj1.PowerOffButton(serverHostname, serverPortNumber);
					}
				catch (Exception e1) 
					{
					e1.printStackTrace();
					}
				}
			});
		
		btnPowerButton.setToolTipText("to turn TV on or Off");
		btnPowerButton.setBounds(83, 25, 97, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnPowerButton);
		
		JMenuBar menuBar = new JMenuBar();
		frmTelevisionRemoteControl.setJMenuBar(menuBar);
		
		JMenu mnNewMenu = new JMenu("File");
		menuBar.add(mnNewMenu);
		
		JMenuItem mntmNewMenuItem = new JMenuItem("Open");
		mnNewMenu.add(mntmNewMenuItem);
		
		JMenuItem mntmNewMenuItem_1 = new JMenuItem("Exit");
		mntmNewMenuItem_1.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent arg0) 
				{
				// close program
				System.exit(1);
				}
			});

		// Authenticate Button
		JButton btnAuthenticateButton_1 = new JButton("Authenticate");
		btnAuthenticateButton_1.setToolTipText("Press to Authenticate to TV");
		btnAuthenticateButton_1.setBounds(134, 64, 112, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnAuthenticateButton_1);
		btnAuthenticateButton_1.addActionListener(new ActionListener() 
		{
		public void actionPerformed(ActionEvent arg0) 
			{
			try
			{
			String serverHostname;
			int serverPortNumber;
			System.out.println( "We will now Authenticate to TV!" );
			serverHostname = ("192.168.1.62");
			serverPortNumber = 55000;
			
			TCP_Comms obj1 = new TCP_Comms();
			//obj1.Authenticate("192.168.1.62", 55000);
			obj1.Authenticate(serverHostname, serverPortNumber);

			//Construct_Transmission(String temp_app_name,String temp_ipaddress, String temp_remote_name, String temp_device_name)
			TCP_Comms obj2 = new TCP_Comms();
			//obj1.Authenticate("192.168.1.62", 55000);
			obj2.Construct_Transmission(temp_app_name, temp_ipaddress, temp_remote_name, temp_device_name);
			}
		catch (Exception e1) 
			{
			e1.printStackTrace();
			}			}
		});
		
		//Connect Button
		JButton btnConnectButton = new JButton("Connect");
		btnConnectButton.setToolTipText("Press to connect to TV");
		btnConnectButton.setBounds(12, 64, 110, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnConnectButton);
		
		JButton btnHDMI1Button = new JButton("HDMI 1");
		btnHDMI1Button.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent e) 
				{
				try
				{
				String serverHostname;
				int serverPortNumber;
				System.out.println( "Input Selection HDMI 1" );
				serverHostname = ("192.168.1.62");
				serverPortNumber = 55000;
				TCP_Comms obj1 = new TCP_Comms();
				//obj1.Authenticate("192.168.1.62", 55000);
				obj1.HDMI1Button(serverHostname, serverPortNumber);
				}
			catch (Exception e1) 
				{
				e1.printStackTrace();
				}			}
			});
		
		btnHDMI1Button.setToolTipText("Press to select HDMI 1 input");
		btnHDMI1Button.setBounds(12, 102, 110, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnHDMI1Button);
		
		JButton btnAV1Button = new JButton("AV1");
		btnAV1Button.setToolTipText("Press to select AV1 input");
		btnAV1Button.setBounds(134, 102, 112, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnAV1Button);
		
		JButton btnHDMI2Button = new JButton("HDMI 2");
		btnHDMI2Button.setBounds(12, 140, 110, 25);
		frmTelevisionRemoteControl.getContentPane().add(btnHDMI2Button);

		btnConnectButton.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e)
				{
				try
					{
					String serverHostname;
					int serverPortNumber;
					System.out.println( "We will now Connect to TV!" );
					serverHostname = ("192.168.1.62");
					serverPortNumber = 55000;
					TCP_Comms obj1 = new TCP_Comms();
					//obj1.Connect("192.168.1.62", 55000);
					obj1.Connect(serverHostname, serverPortNumber);
					}
				catch (Exception e1) 
					{
					e1.printStackTrace();
					}
				}
		});
				
		mnNewMenu.add(mntmNewMenuItem_1);
		JMenu mnNewMenu_1 = new JMenu("About");
		menuBar.add(mnNewMenu_1);
		}
	}
	
