import java.util.Random;

import OwnCollections.*;

public class Main {
  public static Random rnd = new Random();
  public static void main(String[] args) {
    int i = 0, j, nbpoint, k, nbechant = Integer.parseInt(args[0]),nbrep=Integer.parseInt(args[2]);
    long startTime;
    String[] structtype = {"ArrayDeque","BinTreeSrch","LinkedList","OwnLinkedList","Stack"};
    IntegerContainer struct = new ICStack();
    float moymin, moyadd, moyrem, eat, purify, carrot;

    if(Integer.parseInt(args[3])==0){
      System.out.println("type\tnumber\tmin\tadd\tremove\ttime");
      for (; i < 5; i++){
        if(i==3)i++;
        nbrep=Integer.parseInt(args[2]);
        for (nbpoint = 0; nbpoint < Integer.parseInt(args[1]); nbpoint++){
          moymin = 0; moyadd = 0; moyrem = 0;
          try {
            for (k = 0; k < nbechant; k++){
              startTime = System.currentTimeMillis();
              // crÃ©ation de la structure
              switch (i){
                case 0:struct = new ICArrayDeque();break;
                case 1:struct = new ICBinaryTreeSearch();break;
                case 2:struct = new ICLinkedList();break;
                case 3:struct = new ICOwnLinkedList();break;
                default:struct = new ICStack();break;
              }
              for (j = 0; j < nbrep; j++) struct.add(rnd.nextInt());
              moyadd+= (System.currentTimeMillis()-startTime);
              // Test minimum
              startTime = System.currentTimeMillis();
              Integer min = struct.minimum();
              moymin+= (System.currentTimeMillis()-startTime);
              // Test remove
              startTime = System.currentTimeMillis();
              struct.remove(min);
              moyrem+= (System.currentTimeMillis()-startTime);
            }
            System.out.printf("%s\t%d\t%.2f\t%.2f\t%.2f\t%.2f\n", structtype[i], nbrep,
              moymin/nbechant, moyadd/nbechant, moyrem/nbechant,
              (moyrem+moymin+moyadd)/nbechant);
            nbrep+=Integer.parseInt(args[2]);
          }
          catch (Exception e){
            break;
          }
        }
      }
    }
    else{
      System.out.println("type\tnumber\teat\tcarrot\tpurify\ttime");
      for (; i < 5; i++){
        if(i==3)i++;
        nbrep=Integer.parseInt(args[2]);
        for (nbpoint = 0; nbpoint < Integer.parseInt(args[1]); nbpoint++){
          switch (i){
            case 0:struct = new ICArrayDeque();break;
            case 1:struct = new ICBinaryTreeSearch();break;
            case 2:struct = new ICLinkedList();break;
            case 3:struct = new ICOwnLinkedList();break;
            default:struct = new ICStack();break;
          }
          startTime = System.currentTimeMillis();
          struct.eat(nbrep);
          eat = (System.currentTimeMillis()-startTime);
          startTime = System.currentTimeMillis();
          struct.carrot();
          carrot = (System.currentTimeMillis()-startTime);
          startTime = System.currentTimeMillis();
          struct.purify();
          purify = (System.currentTimeMillis()-startTime);
          System.out.printf("%s\t%d\t%.2f\t%.2f\t%.2f\t%.2f\n", structtype[i], nbrep,
                eat, carrot, purify, eat+purify+carrot);
          if (eat+purify+carrot>300000)break;
          nbrep+=Integer.parseInt(args[2]);
        }
      }
    }
  }
}
