package OwnCollections;

import java.util.Random;
import java.util.LinkedList;

public class ICLinkedList implements IntegerContainer {
    LinkedList<Integer> li; int taille = 0;
    public ICLinkedList(){
        li = new LinkedList<Integer>();
    }
    public Integer minimum(){
        Integer min = Integer.MAX_VALUE;
        for (Integer i : li) if (i<min)min=i;
        return min;
    }
    public void add(Integer x){
        li.add(x);
        taille++;
    }
    public void remove(Integer x){
        try {
            li.remove(x);
            taille--;
        }
        catch(Exception e){

        }
    }
    public Integer size(){
        return taille;
    }
    public Integer maximum(){
        Integer max = Integer.MIN_VALUE;
        for (Integer i : li) if (i>max)max=i;
        return max;
    }
    public void purify(){
        LinkedList<Integer> nli = new LinkedList<Integer>();
        int i = 0, val = 0, max = 100000;
        if(max>size())max=size()-1;
        for (; i < max; i++){
          val = maximum();
          nli.add(val);
          remove(val);
        }
        li = nli;
    }
    public void eat(int x){
        Random rnd = new Random();
        for (int i = 0; i < x; i++) add(rnd.nextInt());
    }
    public void carrot(){
        for (int i = 0; i < 100000; i++) remove(minimum());
    }
}
