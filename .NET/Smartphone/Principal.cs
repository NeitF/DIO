using Smartphone.Entitites;
public class Principal
{
    public static void Main(string[] args)
    {
        SmartphoneClass nokia = new Nokia("1234-5678", "G11", "12345678901234", 32);
        SmartphoneClass Iphone = new Iphone("1234-5678", "14", "1323424sfsdf", 64);

        Iphone.Ligar();
        nokia.ReceberLigacao();

        nokia.InstalarAplicativo("Zap");
        Iphone.InstalarAplicativo("Youtube");
    }
}