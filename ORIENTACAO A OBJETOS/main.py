class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
def adicionar_pessoa(vet):
  name = input("\nDigite o NOME da pessoa\n")
  correto= False
  while(correto!=True):
    sexo = input("\nDigite o SEXO da pessoa EX(masc/fem)\n")
    if sexo=="masc" or sexo=="fem":
      correto=True
    else:
      print("Valor Inválido\n")
  correto=False
  while(correto!=True):
    cpf = input("\nDigite o CPF da pessoa Ex(XXX.XXX.XXX-XX)\n")
    if len(cpf) == 14:
      if cpf[3]=='.' and cpf[7]=='.'and cpf[11]=='-':
        correto=True
      else:
        print("Formato Inválido\n")
    else:
      print("Formato Inválido\n")
  p1 = Pessoa(name,sexo,cpf)
  vet.append(p1)
  print("\nPESSOA ADICIONA COM SUCESSO\n")
def consultar_pessoa(vet):
  found = False
  correto= False
  while(correto!=True):
    cpf = input("\nDigite o CPF da pessoa Ex(XXX.XXX.XXX-XX)\n")
    if len(cpf) == 14:
      if cpf[3]=='.' and cpf[7]=='.'and cpf[11]=='-':
        correto=True
      else:
        print("Formato Inválido\n")
    else:
      print("Formato Inválido\n")
  for i in range(0,len(vet)):
    if vet[i].cpf==cpf:
      print("\nPessoa encontrada :)","nome: ",vet[i].nome,"\nsexo:",vet[i].sexo, "\ncpf:",vet[i].cpf, "\n")
      found=True
  if(found==False):
    print("Pessoa não encontrada :(")
  else:
    found=False

def deletar_pessoa(vet):
  found = False
  correto= False
  while(correto!=True):
    cpf = input("\nDigite o CPF da pessoa Ex(XXX.XXX.XXX-XX)\n")
    if len(cpf) == 14:
      if cpf[3]=='.' and cpf[7]=='.'and cpf[11]=='-':
        correto=True
      else:
        print("Formato Inválido\n")
    else:
      print("Formato Inválido\n")
  for i in range(0,len(vet)):
    if vet[i].cpf==cpf:
      del(vet[i])
      print("\nPessoa Deletada :)\n")
      found=True
  if(found==False):
    print("Pessoa não encontrada :(")
  else:
    found=False
sair = 0
vet= []
while(sair==0):
  menu = int(input("    ---Menu---\n1-Adicionar uma pessoa\n2-Procurar uma pessoa \n3-deletar uma pessa\n4-Total de pessas\n5-sair\n"))
  if menu==1:
    adicionar_pessoa(vet)
  elif menu==2:
    consultar_pessoa(vet)
  elif menu==3:
    deletar_pessoa(vet)
  elif menu==4:
    print("\nTotal de pessoas cadastradas :",len(vet),"\n")
  elif menu==5:
    print("\nAté mais")
    sair=1
  else:
    print("\nComando inválido!\n")
