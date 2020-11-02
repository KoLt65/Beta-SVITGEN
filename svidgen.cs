//SVIDGEN beta v0.1
using System;
using System.Threading;

namespace SVIDGEN
{
	class Program
	{
        static void Main(string[] args) 
        {
            Console.Clear();
            Console.WriteLine(@"  ______     _____ ____   ____ _____ _   _ ");
			Console.WriteLine(@" / ___\ \   / /_ _|  _ \ / ___| ____| \ | |  ");
			Console.WriteLine(@" \___  \ \ / / | || | | | |  _|  _| |  \| |");
			Console.WriteLine(@"  ___) |\ V /  | || |_| | |_| | |___| |\  | ");
			Console.WriteLine(@" |____/  \_/  |___|____/ \____|_____|_| \_| ");
			Console.WriteLine("");
			Console.WriteLine("1. Генерировать");
			Console.WriteLine("2. Как пользоваться");
			Console.WriteLine("3. Выйти");
			string title = Console.ReadLine();
			if (title == "3"){
				//Application.Exit();
			}
			else if (title == "2"){
				Console.WriteLine("Это приложение SVIDGEN. Оно специализируется на генерации свидание по таким параметра как время и бюджет.");
			}

			else if (title == "1"){
				Console.WriteLine("1. Утро (до 12 часов)");
				Console.WriteLine("2. День (с 13 до 18)");
				Console.WriteLine("3. Вечер (с 19 до 22)");
				Console.WriteLine("4. Ночь (с 22 до 00)");
			}

			string time = Console.ReadLine();
			Console.WriteLine("Введите бюджет: ");
			string budget = Console.ReadLine();
			if ((budget == "100") && (time == "1")){
				Console.WriteLine("100");
			}
			else if ((budget == "150") && (time == "1")){
				Console.WriteLine("150");
			}

			else if ((budget == "200") && (time == "1")){
				Console.WriteLine("200");
			}

			else if ((time == "250") && (time == "1")){
				Console.WriteLine("250");
			}

			else if ((budget == "300") && (time == "1")){
				Console.WriteLine("");
			}

			else if ((budget == "350") && (time == "1")){
				Console.WriteLine("");
			}

			else if ((budget == "400") && (time == "1")){
				Console.WriteLine("");
			}

			else if ((budget == "450") && (time == "1")){
				Console.WriteLine("");
			}

			else if (budget == "500" && time == "1"){
				Console.WriteLine("");
			}




			if (budget == "100" && time == "2"){
				Console.WriteLine("100");
			}
			else if (budget == "150" && time == "2"){
				Console.WriteLine("150");
			}

			else if (budget == "200" && time == "2"){
				Console.WriteLine("200");
			}

			else if (time == "250" && time == "2"){
				Console.WriteLine("250");
			}

			else if (budget == "300" && time == "2"){
				Console.WriteLine("");
			}

			else if (budget == "350" && time == "2"){
				Console.WriteLine("");
			}

			else if (budget == "400" && time == "2"){
				Console.WriteLine("");
			}

			else if (budget == "450" && time == "2"){
				Console.WriteLine("");
			}

			else if (budget == "500" && time == "2"){
				Console.WriteLine("");
			}


			if (budget == "100" && time == "3"){
				Console.WriteLine("1003");
			}
			else if (budget == "150" && time == "3"){
				Console.WriteLine("150");
			}

			else if (budget == "200" && time == "3"){
				Console.WriteLine("200");
			}

			else if (time == "250" && time == "3"){
				Console.WriteLine("250");
			}

			else if (budget == "300" && time == "3"){
				Console.WriteLine("");
			}

			else if (budget == "350" && time == "3"){
				Console.WriteLine("");
			}

			else if (budget == "400" && time == "3"){
				Console.WriteLine("");
			}

			else if (budget == "450" && time == "3"){
				Console.WriteLine("");
			}

			else if (budget == "500" && time == "3"){
				Console.WriteLine("");
			}


			if (budget == "100" && time == "4"){
				Console.WriteLine("100");
			}
			else if (budget == "150" && time == "4"){
				Console.WriteLine("150");
			}

			else if (budget == "200" && time == "4"){
				Console.WriteLine("200");
			}

			else if (time == "250" && time == "4"){
				Console.WriteLine("250");
			}

			else if (budget == "300" && time == "4"){
				Console.WriteLine("");
			}

			else if (budget == "350" && time == "4"){
				Console.WriteLine("");
			}

			else if (budget == "400" && time == "4"){
				Console.WriteLine("");
			}

			else if (budget == "450" && time == "4"){
				Console.WriteLine("");
			}

			else if (budget == "500" && time == "4"){
				Console.WriteLine("");
			}
			else{
				Console.WriteLine("kavo");
			}
			Console.ReadKey(true);
		}
	}
}
