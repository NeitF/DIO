using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Smartphone.Entitites
{
    internal class Iphone : SmartphoneClass
    {
        public Iphone(string numero, string modelo, string imei, int memoria)
            : base(numero, modelo, imei, memoria) { }

        public override void InstalarAplicativo(string nome)
        {
            Console.WriteLine($"O aplicativo {nome} está sendo instalado em um " +
                $"Iphone modelo {this.Modelo}");
        }
    }
}
