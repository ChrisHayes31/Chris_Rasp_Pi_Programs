import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TVCtl {

	private JFrame frmTvCtl;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TVCtl window = new TVCtl();
					window.frmTvCtl.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public TVCtl() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() 
		{
		frmTvCtl = new JFrame();
		frmTvCtl.setTitle("TV Ctl");
		frmTvCtl.setBounds(100, 100, 280, 424);
		frmTvCtl.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTvCtl.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("Power");
		btnNewButton.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent arg0) 
				{
				}
			});
		btnNewButton.setBounds(83, 30, 89, 23);
		btnNewButton.setToolTipText("Press to turn Power on or off");
		frmTvCtl.getContentPane().add(btnNewButton);
	
		JButton btnAuthenticateButton_1 = new JButton("Authenticate");
		btnAuthenticateButton_1.setToolTipText("Press to Authenticate to TV");
		btnAuthenticateButton_1.setBounds(134, 64, 112, 25);
		frmTvCtl.getContentPane().add(btnAuthenticateButton_1);
	
		JButton btnConnectButton = new JButton("Connect");
		btnConnectButton.setToolTipText("Press to Connect to TV");
		btnConnectButton.setBounds(10, 64, 112, 25);
		frmTvCtl.getContentPane().add(btnConnectButton);
		
		JButton btnHDMI1button = new JButton("HDMI 1");
		btnHDMI1button.setToolTipText("Press to Connect to switch to HDMI 1");
		btnHDMI1button.setBounds(10, 99, 112, 25);
		frmTvCtl.getContentPane().add(btnHDMI1button);
		
		JButton btnHDMI2button = new JButton("HDMI 2");
		btnHDMI2button.setToolTipText("Press to Connect to switch to HDMI 2");
		btnHDMI2button.setBounds(10, 135, 112, 25);
		frmTvCtl.getContentPane().add(btnHDMI2button);
		
		JButton btnAv1button = new JButton("AV 1");
		btnAv1button.setToolTipText("Press to Connect to switch to AV 1");
		btnAv1button.setBounds(134, 100, 112, 25);
		frmTvCtl.getContentPane().add(btnAv1button);
		
		JButton btnAv2button = new JButton("AV 2");
		btnAv2button.setToolTipText("Press to Connect to switch to AV 2");
		btnAv2button.setBounds(134, 136, 112, 25);
		frmTvCtl.getContentPane().add(btnAv2button);
	
		JMenuBar menuBar = new JMenuBar();
		frmTvCtl.setJMenuBar(menuBar);
	
		JMenu mnFileMenu = new JMenu("File");
		menuBar.add(mnFileMenu);
	
		JMenuItem mntmOpenMenuItem = new JMenuItem("Open");
		mnFileMenu.add(mntmOpenMenuItem);
	
		JMenuItem mntmSaveMenuItem = new JMenuItem("Save");
		mnFileMenu.add(mntmSaveMenuItem);
	
		JMenuItem mntmSaveAsMenuItem = new JMenuItem("Save As");
		mnFileMenu.add(mntmSaveAsMenuItem);
	
		JMenuItem mntmExitMenuItem = new JMenuItem("Exit");
		mntmExitMenuItem.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent arg0) 
				{
				System.exit(1);
				}
			});
		mnFileMenu.add(mntmExitMenuItem);
		}
	}
