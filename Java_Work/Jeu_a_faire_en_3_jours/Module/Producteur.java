package Module;

import java.nio.charset.StandardCharsets;
import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class Producteur extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    BoutonA fbut = new BoutonA("Facile",Essential.createImageIcon("button.png","Bouton"));
    BoutonA nbut = new BoutonA("Normal",Essential.createImageIcon("button.png","Bouton"));
    BoutonA dbut = new BoutonA("Difficile",Essential.createImageIcon("button.png","Bouton"));
    public Producteur(){
        setLayout(new BorderLayout());
        fbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new PGameMenu(0));}
        }); add(fbut, BorderLayout.WEST);
        nbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new PGameMenu(1));}
        }); add(nbut, BorderLayout.CENTER);
        dbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new PGameMenu(2));}
        }); add(dbut, BorderLayout.EAST);
        
    }
    public void Change(JPanel jp){
        Cleanup();
        setLayout(new BorderLayout());
        add(jp, BorderLayout.CENTER);
        Essential.changeFont(jp, defFont);
        repaint(); validate();
    }
    public void Cleanup(){
        removeAll();
    }
}
class PGameMenu extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    JTextArea intro = new JTextArea(5, 30);
    BoutonA begin = new BoutonA("Commencer",Essential.createImageIcon("button.png","Bouton"));

    public PGameMenu(int i){
        String txt = "Bonjour nouveau producteurs, "+
        "Ta mission, réussir à faire tourner ton affaire sans que ton entreprise soit insolvable.";
        intro.setLineWrap(true);
        intro.setWrapStyleWord(true);
        byte[] biteTxt = txt.getBytes();
        intro.setText(new String(biteTxt, StandardCharsets.UTF_8));
        intro.setLineWrap(true);
        intro.setWrapStyleWord(true);
        add(intro, BorderLayout.CENTER);
        begin.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new PGame(i));}
        }); 
        add(begin, BorderLayout.SOUTH);
    }
    
    public void Change(JPanel jp){
        Cleanup();
        setLayout(new BorderLayout());
        add(jp, BorderLayout.CENTER);
        Essential.changeFont(jp, defFont);
        repaint(); validate();
    }
    public void Cleanup(){
        removeAll();
    }
}
class PGame extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    Calcule calc;
    JLabel money;
    int nbday = 0;
    JLabel jour = new JLabel("Jour 0");
    BoutonA next = new BoutonA("Jour suivant",Essential.createImageIcon("button.png","Bouton"));
    JLabel lblextra = new JLabel();
    JLabel lblExtraPrix = new JLabel("Prix : ");
    JLabel lblExtraQuantity = new JLabel("Quantite : ");
    JLabel lblExtraQuality = new JLabel("Qualite : ");
    JSlider sdprice = new JSlider(JSlider.HORIZONTAL, 0, 100, 60);
    JSlider sdquantity = new JSlider(JSlider.HORIZONTAL, 0, 100, 60);
    JSlider sdquality = new JSlider(JSlider.HORIZONTAL, 0, 100, 60);
    JPanel info=new JPanel();
    JPanel vals=new JPanel();
    JPanel end=new JPanel();
    public PGame(int i){
        String txt = "Activité et Extra : "; byte[] biteTxt = txt.getBytes(); lblextra.setText(new String(biteTxt, StandardCharsets.UTF_8));
        txt = "Quantité : "; biteTxt = txt.getBytes(); lblExtraQuantity.setText(new String(biteTxt, StandardCharsets.UTF_8));
        txt = "Qualité : "; biteTxt = txt.getBytes(); lblExtraQuality.setText(new String(biteTxt, StandardCharsets.UTF_8));
        calc = new Calcule(i, false);
        money = new JLabel("Argent : "+calc.argent);
        next.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){update();}
        });
        setLayout(new BorderLayout()); JPanel info = new JPanel();
        info.setLayout(new GridBagLayout()); GridBagConstraints constraints = new GridBagConstraints(); constraints.fill = GridBagConstraints.VERTICAL;
        constraints.insets = new Insets(0, 0, 0, 10);
        constraints.gridx = 0; constraints.gridy = 0; info.add(jour, constraints); constraints.gridx = 1; info.add(money, constraints);
        add(info, BorderLayout.NORTH); JPanel vals = new JPanel();
        vals.setLayout(new GridBagLayout());
        constraints.gridx = 1; constraints.gridy = 0; vals.add(lblExtraPrix, constraints); constraints.gridx = 2; vals.add(sdprice, constraints);
        constraints.gridx = 0; constraints.gridy = 1; vals.add(lblextra, constraints); constraints.gridx = 1; vals.add(lblExtraQuantity, constraints); constraints.gridx = 2; vals.add(sdquantity, constraints);
        constraints.gridx = 1; constraints.gridy = 2; vals.add(lblExtraQuality, constraints); constraints.gridx = 2; vals.add(sdquality, constraints);
        add(vals, BorderLayout.CENTER);
        JPanel end = new JPanel(); end.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; end.add(next, constraints);
        add(end, BorderLayout.SOUTH);
        repaint(); validate();
    }
    public void update(){
        calc.next(sdprice.getValue(),sdquality.getValue(),sdquantity.getValue()); removeAll(); nbday++;
        jour = new JLabel("Jour "+nbday);
        money = new JLabel("Argent : "+calc.argent);
        setLayout(new BorderLayout()); JPanel info = new JPanel();
        info.setLayout(new GridBagLayout()); GridBagConstraints constraints = new GridBagConstraints(); constraints.fill = GridBagConstraints.VERTICAL;
        constraints.insets = new Insets(0, 0, 0, 10);
        constraints.gridx = 0; constraints.gridy = 0; info.add(jour, constraints); constraints.gridx = 1; info.add(money, constraints);
        add(info, BorderLayout.NORTH); JPanel vals = new JPanel();
        vals.setLayout(new GridBagLayout());
        constraints.gridx = 1; constraints.gridy = 0; vals.add(lblExtraPrix, constraints); constraints.gridx = 2; vals.add(sdprice, constraints);
        constraints.gridx = 0; constraints.gridy = 1; vals.add(lblextra, constraints); constraints.gridx = 1; vals.add(lblExtraQuantity, constraints); constraints.gridx = 2; vals.add(sdquantity, constraints);
        constraints.gridx = 1; constraints.gridy = 2; vals.add(lblExtraQuality, constraints); constraints.gridx = 2; vals.add(sdquality, constraints);
        add(vals, BorderLayout.CENTER);
        JPanel end = new JPanel(); end.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; end.add(next, constraints);
        add(end, BorderLayout.SOUTH);
        Essential.changeFont(this, defFont);
        repaint(); validate();
    }
}