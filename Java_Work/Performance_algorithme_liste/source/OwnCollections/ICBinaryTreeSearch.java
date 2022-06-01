package OwnCollections;

import java.util.Random;

public class ICBinaryTreeSearch implements IntegerContainer {
    BinaryTree li; int taille = 0;
    public ICBinaryTreeSearch(){
      li = new BinaryTree();
    }
    public Integer minimum(){
      return li.minimum().racine();
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
      return li.maximum().racine();
    }
    public void purify(){
      while(size()>100000) remove(minimum());
    }
    public void eat(int x){
      Random rnd = new Random();
      for (int i = 0; i < x; i++) add(rnd.nextInt());
    }
    public void carrot(){
      for (int i = 0; i < 100000; i++) remove(minimum());
    }
}
class BinaryTree{
    private Integer val;
    private BinaryTree fg,fd;
    private BinaryTree prev;

    public Integer racine(){
      return this.val;
    }

    public Integer previous(){
      return this.prev.racine();
    }

    public void setPrevious(BinaryTree b){
      this.prev = b;
    }

    public BinaryTree ag(){
      return this.fg;
    }

    public BinaryTree ad(){
      return this.fd;
    }

    public void setAd(BinaryTree b){
      this.fd = b;
    }

    public BinaryTree maximum(){
      if(fd != null) if(fd.racine() != null) return fd.maximum();
      return this;
    }

    public BinaryTree minimum(){
      if(fg != null) if(fg.racine() != null) return fg.minimum();
      return this;
    }

    public void add(Integer newVal){
      if(this.val == null) this.val = newVal;
      else if(newVal <= this.val){
        if(fg == null) fg = new BinaryTree();
        fg.setPrevious(this);
        fg.add(newVal);
      }else{
        if(fd == null) fd = new BinaryTree();
        fd.setPrevious(this);
        fd.add(newVal);
      }
    }

    public void remove(Integer x){
      if(this.val == x){
        this.val = null;
        if(fg != null){
          BinaryTree max = fg.maximum();
          this.val = max.racine();
        }
        else if(fd != null){
          BinaryTree min = fd.minimum();
          this.val = min.racine();
        }
      }
      else if(this.val > x && fg != null) fg.remove(x);
      else if(this.val < x && fd != null) fd.remove(x);
    }

}
