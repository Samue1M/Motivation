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

y = random.choice([Frase1,Frase2,Frase3,Frase4]);

if(Selector == "Sim"):
    print(y);

else:
    print("Nhe");