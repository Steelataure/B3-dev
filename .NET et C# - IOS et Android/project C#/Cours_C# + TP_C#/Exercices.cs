//EXERCICES

internal class Program
{
     private static void Main(string[] args)
    {
        //INPUT
        Question_One("test", "ing");
        Same_sign(10, 5);
        Magasin(50);
        Nombre_entier(10);
        Nombre_premier(17);
}
// ------------------
    private static void Question_One(string var_1, string var_2)
    {
        System.Console.WriteLine(var_1 + var_2); 
    }
// ------------------
    private static void Same_sign(int a, int b)
    {
        if (a >= 0 & b >= 0){
            System.Console.WriteLine(true);
            }
        else if (a <= 0 & b <= 0){
            System.Console.WriteLine(true);
        }
    }
// ------------------
    private static void Magasin(int nombre)
    {
        double montant = 0;
        foreach (int value in Enumerable.Range(1, nombre)){
            if (value < 11){
                montant += 2;
            }
            if (value >= 11){
                montant += 1.50;
            }
        }
        System.Console.WriteLine($"Le montant pour ces {nombre} livres est de {montant} euros");
// ------------------
    }
    private static void Nombre_entier(int n)
    {
        int somme = 0;
        foreach (int value in Enumerable.Range(1, n))
        {
            somme += value;
        }
        System.Console.WriteLine(somme);
    }
// ------------------
    private static void Nombre_premier(int nombre)
    {
        if (nombre % 2 != 0)
        {
            System.Console.WriteLine($"{nombre} est un nombre premier");
        }
        else{
            System.Console.WriteLine($"{nombre} n'est pas un nombre premier");
        }
    }
}

