package Module;

import java.awt.*;
import javax.swing.*;

import java.awt.event.*;

public class BoutonA extends JButton{
    public BoutonA(String txt, ImageIcon icone){
        super(txt);
        Image image = icone.getImage();
        Image newimg = image.getScaledInstance(getPreferredSize().width+10, getPreferredSize().height+20, Image.SCALE_SMOOTH);
        super.setIcon(new ImageIcon(newimg));
        setHorizontalTextPosition(JButton.CENTER);
        setVerticalTextPosition(JButton.CENTER);
        setBorder(BorderFactory.createEmptyBorder());
        setContentAreaFilled(false);
    }
}
