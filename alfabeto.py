palavra = input()
letra = ['a', 'A']
tamanho = len(palavra)
quantidade = 0

for i in palavra:
     for j in letra:
          if i == j:
               quantidade += 1
print(f"Tem {quantidade} a na palavra")