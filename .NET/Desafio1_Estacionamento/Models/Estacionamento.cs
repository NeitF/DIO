using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Desafio1_Estacionamento.Models
{
    internal class Estacionamento
    {
        public decimal PrecoInicial { get; set; }
        public decimal PrecoPorHora { get; set; }
        public List<string> Veiculos { get; set; }

        public Estacionamento(decimal precoInicial, decimal precoPorHora)
        {
            PrecoInicial = precoInicial;
            PrecoPorHora = precoPorHora;
            Veiculos = new List<string>();
        }

        public void adicionarVeiculo()
        {
            Console.WriteLine("Digite a placa do veículo: ");
            Veiculos.Add(Console.ReadLine());
        }

        public void removerVeiculo()
        {
            Console.WriteLine("Digite o veículo para remover: ");
            string remVeiculo = Console.ReadLine();

            if (Veiculos.Contains(remVeiculo))
            {
                Console.WriteLine("Quantidade de horas que permaneceu estacionado: ");
                int horas = int.Parse(Console.ReadLine());
                
                decimal precoFinal = PrecoInicial + (PrecoPorHora * horas);

                Console.WriteLine($"O veículo {remVeiculo} foi removido e o preço total foi de {precoFinal + PrecoInicial}");
            }
            else
            {
                throw new ArgumentOutOfRangeException("O veículo não foi encontrado");
            }

        }

        public void listarVeiculo()
        {
            Console.WriteLine("Lista de veículos estacionados");
            if (Veiculos.Any())
            {
                Veiculos.ForEach(v => Console.WriteLine(v));
            }
            else
            {
                Console.WriteLine("Nenhum veículo foi encontrado");
            }
        }
    }
}
