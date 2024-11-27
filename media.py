nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota:"))
nota3 = float(input("Escreva a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3
print('a media é:', media)
if media < 6 :
    print('Reprovado')
else:
    print('Aprovado')


git add . > serve para adicionar o commit
git commit -m "" > serve para marcar o ponto na historia
git branch > cria um projeto que nao altera o projeto inicial mas pode ser mesclado nele
git checkout > entra e sai do merge ou a brach criada
git merge > mescla a branch no projeto principal "main"
git push origin main > salva o processo todo no git 

PASSO 1 "fiz um commit para adicionar o codigo que calculava a media dos alunos"
PASSO 2 "fiz a branch"
PASSO 3 "mesclei a branch no projeto original"
PASSO 4 "repeti o processo acima para adicionar outras funçoes ao codigo"