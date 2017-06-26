
public class TVControlGUI 
	{
	import java.awt.EventQueue;

	import javax.swing.JFrame;
	import javax.swing.JButton;
	import java.awt.BorderLayout;
	import java.awt.event.ActionListener;
	import java.awt.event.ActionEvent;
	import javax.swing.JLabel;
	import java.awt.Font;
	import javax.swing.JList;
	import javax.swing.JTree;
	import javax.swing.border.BevelBorder;
	import javax.swing.SwingConstants;
	import java.awt.Color;
	import java.awt.SystemColor;
	import javax.swing.tree.DefaultTreeModel;
	import javax.swing.tree.DefaultMutableTreeNode;
	import javax.swing.event.TreeSelectionListener;
	import javax.swing.event.TreeSelectionEvent;


		private JFrame frmTvControlPanel;
		private JTree TVModelTree;
		private JLabel lblBrandUsed;
		private JLabel lblModelSelected;
		
		/**
		 * Launch the application.
		 */
		public static void main(String[] args) 
			{
			EventQueue.invokeLater(new Runnable() 
				{
				public void run() 
					{
					try 
						{
						TVControlGUI window = new TVControlGUI();
						window.frmTvControlPanel.setVisible(true);
						} 
						catch (Exception e) 
							{
							e.printStackTrace();
							}
						}
					}
			}
			);
			

		/**
		 * Create the application.
		 */
		public TVControlGUI() 
			{
			initialize();
			}

		/**
		 * Initialize the contents of the frame.
		 */
		private void initialize() 
			{
			frmTvControlPanel = new JFrame();
			frmTvControlPanel.setTitle("TV Control Panel");
			frmTvControlPanel.setBounds(100, 100, 482, 478);
			frmTvControlPanel.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frmTvControlPanel.getContentPane().setLayout(null);
			
			JButton btnClear = new JButton("Clear");
			btnClear.setBounds(35, 50, 97, 25);
			frmTvControlPanel.getContentPane().add(btnClear);
			
			JLabel lblDataRx = new JLabel("Data Received");
			lblDataRx.setFont(new Font("Tahoma", Font.BOLD, 16));
			lblDataRx.setBounds(155, 83, 222, 25);
			frmTvControlPanel.getContentPane().add(lblDataRx);
			
			JButton btnNewButton = new JButton("Send");
			btnNewButton.setBounds(35, 84, 97, 25);
			frmTvControlPanel.getContentPane().add(btnNewButton);
			
			JLabel lblDataTx = new JLabel("Data to Send");
			lblDataTx.setFont(new Font("Tahoma", Font.BOLD, 16));
			lblDataTx.setBounds(155, 49, 222, 25);
			frmTvControlPanel.getContentPane().add(lblDataTx);
			
			JButton btnEnterData = new JButton("Enter Data");
			btnEnterData.setBounds(315, 50, 97, 25);
			frmTvControlPanel.getContentPane().add(btnEnterData);
			
			TVModelTree = new JTree();
			TVModelTree.addTreeSelectionListener(new TreeSelectionListener() {
				public void valueChanged(TreeSelectionEvent e) {
					lblModelSelected.setText(e.getPath().toString());
				}
			});
			TVModelTree.setModel(new DefaultTreeModel(
				new DefaultMutableTreeNode("TV Brand") {
					{
						DefaultMutableTreeNode node_1;
						node_1 = new DefaultMutableTreeNode("Samsung");
							node_1.add(new DefaultMutableTreeNode("UA55C7000 (Lounge)"));
							node_1.add(new DefaultMutableTreeNode("UA40F6400 (Helen)"));
						add(node_1);
					}
				}
			));
			TVModelTree.setVisible(false);
			TVModelTree.setForeground(Color.WHITE);
			TVModelTree.setBackground(SystemColor.window);
			TVModelTree.setToolTipText("Select TV Brand");
			TVModelTree.setBorder(new BevelBorder(BevelBorder.RAISED, null, null, null, null));
			TVModelTree.setBounds(36, 172, 178, 131);
			frmTvControlPanel.getContentPane().add(TVModelTree);
			
			lblBrandUsed = new JLabel("TV Model");
			lblBrandUsed.setHorizontalAlignment(SwingConstants.CENTER);
			lblBrandUsed.setToolTipText("TV Brand selected");
			lblBrandUsed.setFont(new Font("Tahoma", Font.BOLD, 15));
			lblBrandUsed.setBounds(36, 147, 178, 25);
			frmTvControlPanel.getContentPane().add(lblBrandUsed);
			
			JButton button = new JButton("Select TV Brand");
			button.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent arg0) {
				}
			});
			button.setBounds(226, 170, 150, 25);
			frmTvControlPanel.getContentPane().add(button);
			
			JLabel lblModelSelected = new JLabel("Model Selected");
			lblModelSelected.setHorizontalAlignment(SwingConstants.CENTER);
			lblModelSelected.setFont(new Font("Tahoma", Font.BOLD, 16));
			lblModelSelected.setBounds(226, 208, 159, 38);
			frmTvControlPanel.getContentPane().add(lblModelSelected);
			}
		}