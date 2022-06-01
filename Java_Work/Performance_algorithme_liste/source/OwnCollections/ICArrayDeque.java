package OwnCollections;

import java.util.Random;
import java.util.ArrayDeque;

public class ICArrayDeque implements IntegerContainer {
    ArrayDeque<Integer> li; int taille = 0;
    public ICArrayDeque(){
        li = new ArrayDeque<Integer>();
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
        li.remove(x);
        taille--;
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
        ArrayDeque<Integer> nli = new ArrayDeque<Integer>();
        int val = 0;
        int max = 100000;
        if(max>size())max=size();
        for (int i = 0; i < max; i++){
          val = maximum();
          nli.add(val);
          li.remove(val);
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
