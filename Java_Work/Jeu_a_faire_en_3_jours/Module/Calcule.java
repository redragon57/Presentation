package Module;

import java.util.*;

public class Calcule {
  public static Random rnd = new Random();
  public int difficulty = 0;
  public Boolean isconso = true;
  public int satisfaction = 0;
  public int sante = 0;
  public int argent = 0;
  public int nextra = 0;
  public int nfood = 0;
  public int pf = 15;
  public int pe = 10;
  public int utiliteFood = 7;
  public int utiliteActivite = 7;
  public int taille;
  public Boolean crise = false;
  public List<Integer> conshistory = new ArrayList();
  public List<Integer> hextra = new ArrayList();
  public List<Integer> hfood = new ArrayList();
  public Calcule(int i, Boolean conso){
    difficulty = i;
    isconso = conso;
    satisfaction = 90-i*20;
    sante = 100-i*10;
    if (conso) argent = 30000/(i+1);
    else argent = 10000000/((i+1)*(i+1));
    prodhistory.add(argent);
    conshistory.add(argent);
  }
  public void next(int extra, int food){
    market(extra*pf,food*pe); hextra.add(extra); hfood.add(food);
    if(utiliteFood - food < 0){
      sante-=(utiliteFood - food)*2;
      utiliteFood--;
      if(utiliteFood<4) utiliteFood=4;
    }
    else{
      sante+=Math.sqrt(nfood)-7;
      if (sante>100) sante=100;
      if(food < 3) utiliteFood=7;
      if(utiliteFood>9) utiliteFood=9;
    }
    if(utiliteActivite - extra < 0){
      satisfaction-=(utiliteActivite - extra)*2;
      utiliteActivite--;
      if(utiliteActivite<0) utiliteActivite=0;
    }
    else{
      satisfaction+=Math.log(nextra+nfood/2+1)*2-3;
      if (satisfaction>100) satisfaction=100;
      if(extra < 3) utiliteActivite=7;
      if(utiliteActivite>10) utiliteActivite=10;
    }
    if(taille>1){
      if(food > 7 && hfood.get(hfood.size()-2) > 7) pf--;
      if(pf < 12) pf=12;
      if(food < 4 && hfood.get(hfood.size()-2) < 4) pf++;
      if(pf > 18) pf=18;
      if((food > 4 && food < 7) && (hfood.get(hfood.size()-2) > 4 && hfood.get(hfood.size()-2) < 7)){
        if(food<15) pf++;
        if(food>15) pf--;
      }
      if(extra > 7 && hextra.get(hextra.size()-2) > 7) pe--;
      if(pe < 7) pe=7;
      if(extra < 4 && hextra.get(hextra.size()-2) < 4) pe++;
      if(pe > 13) pe=13;
      if((extra > 4 && extra < 7) && (hextra.get(hextra.size()-2) > 4 && hextra.get(hextra.size()-2) < 7)){
        if(extra<10) pe++;
        if(extra>10) pe--;
      }
    }
    argent+=57-nextra-nfood;
    System.out.println(crise);
    if (crise) argent-=(nextra+nfood)*0.7*Math.sqrt(difficulty+1);
    conshistory.add(argent);
  }
  public void market(int e, int f){
    taille = hextra.size();
    if (taille!=0){
      int moye = 0;
      int moyf = 0;
      int sum = 0;
      for (int i = 0; i < taille; i++){
        moye+=hextra.get(i)/taille*(i+1);
        moyf+=hfood.get(i)/taille*(i+1);
        sum+=(i+1);
      }
      nextra = e-moye/sum+35/2;
      nfood = f-moyf/sum+35/2;
    }
    else {
      nextra = e;
      nfood = f;
    }
  }
  public int cout_prod = 0;
  public int stock = 0;
  public double[] otherprice;
  public List<Integer> prodhistory = new ArrayList();
  public void next(double price, int quality, int quantity){
    cout_prod = (int)(quality/50*quantity/3-Math.sqrt(quantity));
    otherprice = new double[]{randdouble(-0.2, 0.5)+cout_prod/quantity,
      randdouble(-0.2, 0.5)+cout_prod/quantity,randdouble(-0.2, 0.5)+cout_prod/quantity};
    if (crise) cout_prod *= (1.7 + difficulty/2);
    int nbvente = (int)(quantity*price/3*(otherprice[0]+otherprice[1]+otherprice[2]));
    if (nbvente>quantity) nbvente = quantity;
    stock = quantity-nbvente;
    argent+=price*nbvente-cout_prod;
    prodhistory.add(argent);
  }
  public double randdouble(double min, double max){
    return min+(max-min)*rnd.nextDouble();
  }
}
