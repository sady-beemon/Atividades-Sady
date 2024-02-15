"""Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak."""

cond = ['e','a','i','o','s','t']
repl = ['3','4','1','0','5','7']
plv = str(input("Digite uma palavra: "))
leet = []

for i in range(len(plv)):
    leet.append(plv[i])
    for i2 in range(len(cond)):
        if plv[i] == cond[i2]:
            leet[i] = repl[i2]
print("Palavra antiga: ",plv,
      "\nPalavra com leet: ",''.join(leet))