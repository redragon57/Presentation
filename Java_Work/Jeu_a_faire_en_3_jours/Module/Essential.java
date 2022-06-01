package Module;

import javax.swing.*;
import java.awt.*;


public class Essential {
    public static ImageIcon createImageIcon(String path, String description){
        java.net.URL imgURL = Essential.class.getClassLoader().getResource("resources/Images/"+path);
        if (imgURL != null) {
            return new ImageIcon(imgURL, description);
        } else {
            System.err.println("Couldn't find file: " + path);
            return null;
        }
    }
    public static void changeFont(Component component, Font font){
        component.setFont(font);
        if (component instanceof Container)
            for (Component child : ((Container) component).getComponents())
                changeFont(child,font);
    }
}