import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Sample_GUI {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Sample_GUI window = new Sample_GUI();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Sample_GUI() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 674, 501);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("Power");
		btnNewButton.setToolTipText("Press to turn Power on or off");
		btnNewButton.setBounds(83, 26, 97, 25);
		frame.getContentPane().add(btnNewButton);
		
		JButton btnAuthenticateButton_1 = new JButton("Authenticate");
		btnAuthenticateButton_1.setToolTipText("Press to Authenticate to TV");
		btnAuthenticateButton_1.setBounds(134, 64, 112, 25);
		frame.getContentPane().add(btnAuthenticateButton_1);
		
		JButton btnConnectButton = new JButton("Connect");
		btnConnectButton.setToolTipText("Press to Connect to TV");
		btnConnectButton.setBounds(10, 64, 112, 25);
		frame.getContentPane().add(btnConnectButton);
		
		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);
		
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
