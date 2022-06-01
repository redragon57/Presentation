package OwnCollections;

import java.util.Random;

public class ICOwnLinkedList implements IntegerContainer {
    OwnLinkedList<Integer> li;
    public ICOwnLinkedList(){
        li = new OwnLinkedList<Integer>();
    }
    public Integer minimum(){
        return li.min();
    }
    public void add(Integer x){
        li.add(x);
    }
    public void remove(Integer x){
        li.remove(x);
    }
    public Integer size(){
        return li.size();
    }
    public Integer maximum(){
        return li.max();
    }
    public void purify(){
        OwnLinkedList<Integer> nli = new OwnLinkedList<Integer>();
        for (int i = 0; i < 100000; i++){
            nli.add(maximum());
            li.remove(maximum());
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

class OwnLinkedList<T>{
    private OwnLinkedList<T> suiv = null;
    private T val;
    private int taille = 0;
    public OwnLinkedList(){

    }

    public void add(T v){
        if (val==null){
            val = v;
            suiv = new OwnLinkedList<T>();
        }
        else suiv.add(v);
        taille++;
    }
    public void add(T v, long ind){
        if (val==null){
            val = v;
            suiv = new OwnLinkedList<T>();
        }
        else if (ind==0){
            OwnLinkedList<T> savesuiv = this.suiv;
            suiv = this;
            suiv.suiv = savesuiv;
            val = v;
        }
        else suiv.add(v,ind--);
        taille++;
    }
    public void remove(T v){
        if (v == val) {
            val = suiv.val;
            suiv = suiv.suiv;
        }
        else suiv.remove(v);
        taille--;
    }
    public void remove(long ind){
        if (ind == 0) {
            val = suiv.val;
            suiv = suiv.suiv;
        }
        else remove(ind--);
        taille--;
    }
    public void replace(T v, long ind){
        if (ind==0) val = v;
        else if (suiv==null) throw new IndexOutOfBoundsException();
        else replace(v, ind--);
    }

    public Integer min(){
        if (suiv.suiv!=null){
            Integer min = suiv.min();
            if (min<(Integer)val) return min;
        }
        return (Integer)val;
    }
    public Integer max(){
        if (suiv.suiv!=null) if (suiv.max()>(Integer)val) return suiv.max();
        return (Integer)val;
    }
    public Integer size(){
        return taille;
    }

    //non récursif
    /*    
    public void add(T v){
        OwnLinkedList<T> s = suiv;
        while (s.suiv!=null) s = s.suiv;
        s.suiv = new OwnLinkedList<T>();
        s.val = v;
        taille++;
    }
    public void remove(T v){
        OwnLinkedList<T> s = suiv;
        while (s.suiv!=null){
            if (v==val){
                s.val = s.suiv.val;
                s = s.suiv;
                taille--;
                break;
            }
            s = s.suiv;
        }
    }

    public Integer min(){
        OwnLinkedList<T> s = suiv;
        Integer min = (Integer)val;
        while (s.suiv!=null){
            if (min>(Integer)s.val) min = (Integer)s.val;
            s = s.suiv;
        }
        return min;
    }
    public Integer max(){
        OwnLinkedList<T> s = suiv;
        Integer max = (Integer)val;
        while (s.suiv!=null){
            if (max<(Integer)s.val) max = (Integer)s.val;
            s = s.suiv;
        }
        return max;
    }
    */
}


class OLL2<T>{
    private OLL2<T> prec, suiv;
    private T val;
    private long length, index;
    public OLL2(){
        length = 0; prec = this; suiv = this; index = 0;
    }
    public long size(){
        return get(0).length;
    }
    public long index(){
        return index;
    }
    public OLL2<T> get(long ind){
        if (ind == index) return this;
        else if (index>ind/2) return suiv.get(ind);
        else return prec.get(ind);
    }


    public void add(T v){
        add(v, size());
    }
    public void add(T v, long ind){
        if (size()==0) val = v;
        else {
            OLL2<T> newoll = new OLL2<T>();
            newoll.val = v;
            newoll.index = ind;

            OLL2<T> oll = get(ind-1);
            newoll.suiv = oll.suiv;
            newoll.prec = oll;
            oll.suiv = newoll;
            newoll.suiv.prec = newoll;
        }
        get(0).length++;
    }
    public void remove(T v){
        get(0).removei(v);
    }
    private void removei(T v){
        if (v==val){
            prec.suiv=suiv;
            suiv.prec=prec;
        }
        else if (index!=length) suiv.remove(v);
    }
    public void remove(long ind){
        OLL2<T> rmoll = get(ind);
        rmoll.suiv.prec = rmoll.prec;
        rmoll.prec.suiv = rmoll.suiv;
    }
    public void replace(T v, long ind){
        OLL2<T> rpoll = get(ind);
        rpoll.val = v;
    }

    // faire une version multithread
    public <T extends Integer> Integer min(){
        OLL2<Integer> init = (OLL2<Integer>) get(0);
        Integer min = init.val;
        for (int i = 0; i < length; i++){
            Integer v = init.val;
            if (min>v) min=v;
            init = init.suiv;
        }
        return min;
    }
    public <T extends Integer> Integer max(){
        OLL2<Integer> init = (OLL2<Integer>) get(0);
        Integer max = init.val;
        for (int i = 0; i < length; i++){
            Integer v = init.val;
            if (max<v) max=v;
            init = init.suiv;
        }
        return max;
    }
    public <T extends Integer> Integer smin(){
        Integer min = (Integer) val;
        for (int i = 0; i < length; i++){
            Integer v = (Integer) get(i).val;
            if (min>v) min=v;
        }
        return min;
    }
    public <T extends Integer> Integer smax(){
        Integer max = (Integer) val;
        for (int i = 0; i < length; i++){
            Integer v = (Integer) get(i).val;
            if (max<v) max=v;
        }
        return max;
    }
}
