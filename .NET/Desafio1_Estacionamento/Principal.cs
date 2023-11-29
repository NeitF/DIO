using Desafio1_Estacionamento.Models;

public class Principal
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Digite o preço inicial: ");
        decimal precoInicial = decimal.Parse(Console.ReadLine());

        Console.WriteLine("Digite o preço por hora: ");
        decimal precoPorHora = decimal.Parse(Console.ReadLine());

        Estacionamento e1 = new Estacionamento(precoInicial, precoPorHora);
        bool continuarExecucao = true;
        int opcao;


        while (continuarExecucao)
        {
            Console.Clear();
            Console.WriteLine("Digite a sua opção:" +
                "\n1 - Cadastrar veículo " +
                "\n2 - Remover veículo" +
                "\n3 - Listar veículos" +
                "\n4 - Encerrar");

            try
            {
                opcao = int.Parse(Console.ReadLine());
            }
            catch(Exception e)
            {
                continue;
            }

            switch (opcao)
            {
                case 1:
                    e1.adicionarVeiculo();
                    break;
                case 2:
                    e1.removerVeiculo();
                    break;
                case 3:
                    try
                    {
                        e1.listarVeiculo();
                    }
                    catch(ArgumentOutOfRangeException e)
                    {
                        Console.WriteLine(e.Message);
                    }
                    break;
                case 4:
                    continuarExecucao = false;
                    break;
                default:
                    Console.WriteLine("A opção inserida é inválida");
                    break;
            }

            Console.WriteLine("Pressione qualquer tecla para continuar...");
            Console.ReadLine();
        }
    }
}