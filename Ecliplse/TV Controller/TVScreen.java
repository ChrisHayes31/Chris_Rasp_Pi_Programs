import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TVScreen {

	private JFrame frmTvController;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TVScreen window = new TVScreen();
					window.frmTvController.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public TVScreen() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmTvController = new JFrame();
		frmTvController.setTitle("TV Controller");
		frmTvController.setBounds(100, 100, 450, 300);
		frmTvController.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmTvController.getContentPane().setLayout(null);
		
		JMenuBar menuBar = new JMenuBar();
		frmTvController.setJMenuBar(menuBar);
		
		JMenu mnNewMenu = new JMenu("File");
		menuBar.add(mnNewMenu);
		
		JMenuItem mntmNewMenuItem = new JMenuItem("Exit");
		mntmNewMenuItem.addActionListener(new ActionListener() 
			{
			public void actionPerformed(ActionEvent arg0) 
				{
				System.exit(1);
				}
			});
		mnNewMenu.add(mntmNewMenuItem);
	}
}
