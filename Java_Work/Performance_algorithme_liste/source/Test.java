import OwnCollections.*;

public class Test {
  public static void main(String[] args) {
    ICBinaryTreeSearch bts = new ICBinaryTreeSearch();
    bts.add(10);
    bts.add(26);
    bts.add(16);
    bts.add(4);
    bts.add(6);
    bts.add(9);
    System.out.println(bts.minimum());
    bts.remove(50);
    System.out.println(bts.minimum());
  }
}
