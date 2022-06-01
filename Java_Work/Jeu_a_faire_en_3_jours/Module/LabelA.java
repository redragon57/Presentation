package Module;

import javax.swing.*;
import java.awt.*;
import javax.swing.plaf.ProgressBarUI;

public class LabelA extends JProgressBar{
    public LabelA(String txt, int i){
        super(0, 100);
        setPreferredSize(new Dimension(130, 14));
        setValue(i);
        setString(txt+i);
        setStringPainted(true);
        UIManager.put("ProgressBar.repaintInterval", 100);
    }

    public void update(String txt, int i){
        setValue(i);
        setString(txt+i);
        setStringPainted(true);
    }
}
