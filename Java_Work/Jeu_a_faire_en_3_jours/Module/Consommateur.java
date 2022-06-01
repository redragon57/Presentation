package Module;

import java.nio.charset.StandardCharsets;
import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;

public class Consommateur extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    BoutonA fbut = new BoutonA("Facile",Essential.createImageIcon("button.png","Bouton"));
    BoutonA nbut = new BoutonA("Normal",Essential.createImageIcon("button.png","Bouton"));
    BoutonA dbut = new BoutonA("Difficile",Essential.createImageIcon("button.png","Bouton"));
    public Consommateur(){
        setLayout(new BorderLayout());
        fbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new CGameMenu(0));}
        }); add(fbut, BorderLayout.WEST);
        nbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new CGameMenu(1));}
        }); add(nbut, BorderLayout.CENTER);
        dbut.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new CGameMenu(2));}
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
class CGameMenu extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    JTextArea intro = new JTextArea(5, 30);
    BoutonA begin = new BoutonA("Commencer",Essential.createImageIcon("button.png","Bouton"));
    public CGameMenu(int i){
        String txt = "Bonjour nouveau consommateur, Ta mission, réussir à finir tes fins de mois durant ";
        if (i == 0) txt += "le passage à une nouvelle monnais";
        else if (i == 1) txt += "une pandémie";
        else txt += "une crise boursière incroyable";
        txt += ". Pour ce faire, vas devoir changer ta consommation et tes achats pour rester en bonne santé et ne pas être à découvert.";
        byte[] biteTxt = txt.getBytes();
        intro.setText(new String(biteTxt, StandardCharsets.UTF_8));
        intro.setLineWrap(true); intro.setWrapStyleWord(true);
        add(intro, BorderLayout.CENTER);
        begin.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){Change(new CGame(i));}
        }); add(begin, BorderLayout.SOUTH);
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
class CGame extends JPanel {
    Font defFont = new Font("resources/Ubuntu/Ubuntu-Regular.ttf",0,14);
    Calcule calc;
    JLabel money;
    int nbday = 0;
    JLabel jour = new JLabel("Jour 0");
    LabelA satis;
    LabelA sante;
    int pf = 15;
    int pe = 5;
    String euro = "€";
    byte[] biteTxt2 = euro.getBytes();
    String txt = "Activités"; byte[] biteTxt = txt.getBytes(); JLabel activite = new JLabel(new String(biteTxt, StandardCharsets.UTF_8));
    JLabel quantity = new JLabel();
    JLabel price = new JLabel("Prix");
    BoutonA next = new BoutonA("Jour suivant",Essential.createImageIcon("button.png","Bouton"));
    JLabel lblfood = new JLabel("Alimentation : ");
    JLabel lblexterne = new JLabel();
    JLabel lblmobilier = new JLabel("Mobilier : ");
    JSlider sdfood = new JSlider(JSlider.HORIZONTAL, 0, 10, 5){
        @Override
            public void updateUI() {
                setUI(new CustomSlider(this));
            }
    };
    JSlider sdexterne = new JSlider(JSlider.HORIZONTAL, 0, 10, 5){
        @Override
            public void updateUI() {
                setUI(new CustomSlider(this));
            }
    };
    JLabel priceFood;
    JLabel priceexterne;
    public CGame(int i){
        txt = "Quantité acheté"; biteTxt = txt.getBytes(); quantity.setText(new String(biteTxt, StandardCharsets.UTF_8));
        txt = "Activité externe : "; biteTxt = txt.getBytes(); lblexterne.setText(new String(biteTxt, StandardCharsets.UTF_8));
        calc = new Calcule(i, true);
        satis = new LabelA("Satisfaction ",calc.satisfaction);
        sante = new LabelA("Sante ",calc.sante);
        money = new JLabel("Argent : "+calc.argent);
        priceFood = new JLabel("Prix : " + Integer.toString(sdfood.getValue()*calc.pf) + new String(biteTxt2, StandardCharsets.UTF_8));
        priceexterne = new JLabel("Prix : " + Integer.toString(sdexterne.getValue()*calc.pe) + new String(biteTxt2, StandardCharsets.UTF_8));
        sdexterne.addChangeListener(new ChangeListener() {
            public void stateChanged(ChangeEvent ce) {
                priceexterne.setText("Prix : " + Integer.toString(sdexterne.getValue()*calc.pe) + new String(biteTxt2, StandardCharsets.UTF_8));
                repaint();
            }
        });
        sdfood.addChangeListener(new ChangeListener() {
            public void stateChanged(ChangeEvent ce) {
                priceFood.setText("Prix : " + Integer.toString(sdfood.getValue()*calc.pf) + new String(biteTxt2, StandardCharsets.UTF_8));
                repaint();
            }
        });
        next.addActionListener(new ActionListener(){  
            public void actionPerformed(ActionEvent e){update();}
        });
        setLayout(new BorderLayout()); JPanel info = new JPanel();
        info.setLayout(new GridBagLayout()); GridBagConstraints constraints = new GridBagConstraints(); constraints.fill = GridBagConstraints.VERTICAL;
        constraints.insets = new Insets(0, 0, 0, 10);
        constraints.gridx = 0; constraints.gridy = 0; info.add(jour, constraints); constraints.gridx = 1; info.add(satis, constraints);
        constraints.gridx = 2; info.add(sante, constraints); constraints.gridx = 3; info.add(money, constraints);
        add(info, BorderLayout.NORTH); JPanel vals = new JPanel();
        vals.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; vals.add(activite, constraints); constraints.gridx = 1; vals.add(quantity, constraints); constraints.gridx = 2; vals.add(price, constraints);
        constraints.gridx = 0; constraints.gridy = 1; vals.add(lblexterne, constraints); constraints.gridx = 1; vals.add(sdexterne, constraints); constraints.gridx = 2; vals.add(priceexterne, constraints);
        constraints.gridx = 0; constraints.gridy = 2; vals.add(lblfood, constraints); constraints.gridx = 1; vals.add(sdfood, constraints); constraints.gridx = 2; vals.add(priceFood, constraints);
        add(vals, BorderLayout.CENTER);
        JPanel end = new JPanel(); end.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; end.add(next, constraints);
        add(end, BorderLayout.SOUTH);
    }
    public void update(){
        calc.next(sdexterne.getValue(),sdfood.getValue()); removeAll(); nbday++;
        if (nbday==30/(calc.difficulty+1)){
            calc.crise = true;
            txt = "";
            if (calc.difficulty==0) txt += "Le passage à une nouvelle monnais";
            else if (calc.difficulty == 1) txt += "Une pandémie";
            else txt += "Une crise boursière incroyable";
            txt+=" à été déclaré.\nDe lourde retombé économique sont préconniser et le prix des choses va donc augmenter en conséquence.";
            biteTxt = txt.getBytes();
            JOptionPane.showMessageDialog(null, new String(biteTxt, StandardCharsets.UTF_8), "Alert crise", JOptionPane.INFORMATION_MESSAGE);
        }
        priceFood.setText("Prix : " + Integer.toString(sdfood.getValue()*calc.pf) + new String(biteTxt2, StandardCharsets.UTF_8));
        priceexterne.setText("Prix : " + Integer.toString(sdexterne.getValue()*calc.pe) + new String(biteTxt2, StandardCharsets.UTF_8));
        jour.setText("Jour "+nbday);
        satis.update("Satisfaction ",calc.satisfaction);
        sante.update("Sante ",calc.sante);
        money.setText("Argent : "+calc.argent);
        setLayout(new BorderLayout()); JPanel info = new JPanel();
        info.setLayout(new GridBagLayout()); GridBagConstraints constraints = new GridBagConstraints(); constraints.fill = GridBagConstraints.VERTICAL;
        constraints.insets = new Insets(0, 0, 0, 10);
        constraints.gridx = 0; constraints.gridy = 0; info.add(jour, constraints); constraints.gridx = 1; info.add(satis, constraints);
        constraints.gridx = 2; info.add(sante, constraints); constraints.gridx = 3; info.add(money, constraints);
        add(info, BorderLayout.NORTH); JPanel vals = new JPanel();
        vals.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; vals.add(activite, constraints); constraints.gridx = 1; vals.add(quantity, constraints); constraints.gridx = 2; vals.add(price, constraints);
        constraints.gridx = 0; constraints.gridy = 1; vals.add(lblexterne, constraints); constraints.gridx = 1; vals.add(sdexterne, constraints); constraints.gridx = 2; vals.add(priceexterne, constraints);
        constraints.gridx = 0; constraints.gridy = 2; vals.add(lblfood, constraints); constraints.gridx = 1; vals.add(sdfood, constraints); constraints.gridx = 2; vals.add(priceFood, constraints);
        add(vals, BorderLayout.CENTER);
        JPanel end = new JPanel(); end.setLayout(new GridBagLayout());
        constraints.gridx = 0; constraints.gridy = 0; end.add(next, constraints);
        add(end, BorderLayout.SOUTH);
        Essential.changeFont(this, defFont);
        repaint(); validate();
        if (calc.satisfaction==0||calc.sante==0||calc.argent<-500||nbday>60) Change(new EndGame(calc));
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
