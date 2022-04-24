# Jeitos de usar uma string
#
#Var = "Jeito";
#
#print("Tem " + Var);
#print(Var);
#print("Tem {}".format(Var));
#print(f"Tem {Var}");

#---------------------------------------------------------------------------------------------------------------------------

import random


Selector = input("Precisa de uma motivação? ");

Frase1 = f"\nTudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado!\n";
Frase2 = f"\nA persistência é o caminho do êxito.\n";
Frase3 = f"\nÉ parte da cura o desejo de ser curado.\n";
Frase4 = f"\nNo meio da dificuldade encontra-se a oportunidade.\n";
Frase5 = f"\nAs pessoas costumam dizer que a motivação não dura sempre. Bem, nem o efeito do banho, por isso recomenda-se diariamente.\n";
Frase6 = f"\nMotivação é a arte de fazer as pessoas fazerem o que você quer que elas façam porque elas o querem fazer.\n";
Frase7 = f"\nToda ação humana, quer se torne positiva ou negativa, precisa depender de motivação.\n";
Frase8 = f"\nLute. Acredite. Conquiste. Perca. Deseje. Espere. Alcance. Invada. Caia. Seja tudo o quiser ser, mas, acima de tudo, seja você sempre.\n";
Frase9 = f"\nA verdadeira motivação vem de realização, desenvolvimento pessoal, satisfação no trabalho e reconhecimento.\n";
Frase10 = f"\nImagine uma nova história para sua vida e acredite nela.\n";

y = random.choice([Frase1,Frase2,Frase3,Frase4,Frase5,Frase6,Frase7,Frase8,Frase9,Frase10]);

if(Selector == "Sim"):
    print(y);

else:
    print("Nhe");
