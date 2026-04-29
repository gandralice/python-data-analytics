from sys import argv
preco_cenoura = 5
preco_oleo = 7
preco_fermento = 4
preco_leite = 7
preco_acucar = 6
preco_ovos = 14
preco_farinha = 5
def soma_lista(tem_cenoura, tem_oleo, tem_fermento, tem_leite, tem_acucar, tem_ovos, tem_farinha):
  total = 0
  if tem_cenoura:
    total = total + preco_cenoura
  if tem_oleo:
    total = total + preco_oleo
  if tem_fermento:
    total = total + preco_fermento
  if tem_leite:
    total = total + preco_leite
  if tem_acucar:
    total = total + preco_acucar
  if tem_ovos:
    total = total + preco_ovos
  if tem_farinha:
    total = total + preco_farinha
  return total


if __name__ == "__main__":
  terminal_tem_cenoura = argv[1] == "Sim"
  terminal_tem_oleo = argv[2] == "Sim"
  terminal_tem_fermento = argv[3] == "Sim"
  terminal_tem_leite = argv[4] == "Sim"
  terminal_tem_acucar = argv[5] == "Sim"
  terminal_tem_ovos = argv[6] == "Sim"
  terminal_tem_farinha = argv[7] == "Sim"
  
  resultado = soma_lista(terminal_tem_cenoura, terminal_tem_oleo, terminal_tem_fermento, terminal_tem_leite, terminal_tem_acucar, terminal_tem_ovos, terminal_tem_farinha)  
  print(resultado)