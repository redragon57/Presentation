import java.util.*;
import java.awt.*;
import javax.swing.*;

import javax.imageio.ImageIO;
import java.awt.event.*;
import java.awt.image.*;
import java.io.File;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import Module.*;

public class Main {
  public static void main(String[] args) {
  	new JHome();
  }
}
class JHome extends JFrame{
  Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
  JPanel conso = new Consommateur();
  JPanel prod = new Producteur();
  BoutonA BCons=new BoutonA("Consommateur",Essential.createImageIcon("button.png","Bouton"));
  BoutonA BProd=new BoutonA("Producteur",Essential.createImageIcon("button.png","Bouton"));
  public JHome() {
    super("T4");
    setLayout(new GridBagLayout());
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setSize(640,480);

    JMenuBar menuBar = new JMenuBar();
    JMenu gMenu = new JMenu("Game");
    JMenu gMenu2 = new JMenu("Extra");
    JMenuItem newG = new JMenuItem("New Game");
    JMenuItem quit = new JMenuItem("Quit Game");
    JMenuItem help = new JMenuItem("Help");
    JMenuItem about = new JMenuItem("About");
    quit.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        JHome.this.setVisible(false);
        JHome.this.dispose();
      }
    });
    newG.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        JHome.this.setVisible(false);
        JHome.this.dispose();
        new JHome();
      }
    });
    gMenu.add(newG);
    gMenu.add(quit);
    gMenu2.add(help);
    gMenu2.add(about);
    menuBar.add(gMenu);
    menuBar.add(gMenu2);
    setJMenuBar(menuBar);

    JLabel mainPanel = new JLabel(Essential.createImageIcon("background.gif","Background")) {
      @Override
      public Dimension getPreferredSize() {
        Dimension size = super.getPreferredSize();
        Dimension lmPrefSize = getLayout().preferredLayoutSize(this);
        size.width = Math.max(size.width, lmPrefSize.width);
        size.height = Math.max(size.height, lmPrefSize.height);
        return size;
      }
    };
    mainPanel.setLayout(new GridBagLayout());
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(10, 10, 10, 10);
    gbc.weightx = 1.0;
    gbc.anchor = GridBagConstraints.WEST;
    gbc.gridwidth = GridBagConstraints.REMAINDER;

    BCons.addActionListener(new ActionListener(){  
      public void actionPerformed(ActionEvent e){Change(conso);}
    }); mainPanel.add(BCons);

    BProd.addActionListener(new ActionListener(){  
      public void actionPerformed(ActionEvent e){Change(prod);}
    }); mainPanel.add(BProd);
    gbc.weighty = 1.0;
    mainPanel.add(Box.createGlue(), gbc);
    add(mainPanel); Essential.changeFont(this,defFont); pack(); setVisible(true);

    setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
  }

  public void Change(JPanel jp){
    Cleanup();
    setLayout(new BorderLayout());
    add(jp, BorderLayout.CENTER);
    Essential.changeFont(jp, defFont);
    repaint(); validate();
  }

  public void Cleanup(){
    getContentPane().removeAll();
  }
}