package OwnCollections;

public interface IntegerContainer {
    // renvoie le plus petit entier de la structure
    Integer minimum();
    // renvoie le plus grand entier de la structure
    Integer maximum();
    // ajoute l'élément x à la structure
    void add(Integer x);
    // supprime un élément
    void remove(Integer x);
    // renvoie la taille
    Integer size();
    // vous devez garder les 100 000 mesures les plus hautes de la série précédente (ça sent la fraude scientifique mais vous êtes bien payé);
    void purify();
    // agréger les données reçues;
    void eat(int x);
    // vous devez supprimer les 100 000 mesures les plus faibles (je vous rappelle que vous êtes toujours bien payé).
    void carrot();
}
