import tkinter as tk

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.num_saques = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            self.info_var.set("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            self.info_var.set("Erro: Valor de depósito inválido.")

    def saque(self, valor):
        if self.num_saques < 3:
            if valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.num_saques += 1
                self.info_var.set("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            elif valor > self.saldo:
                self.info_var.set("Erro: Saldo insuficiente para realizar o saque.")
            else:
                self.info_var.set("Erro: Valor de saque excede o limite permitido (R$ 500).")
        else:
            self.info_var.set("Erro: Limite de saques diários excedido.")

    def extrato(self):
        extrato = "--- Extrato ---\n"
        extrato += "Depósitos:\n"
        for deposito in self.depositos:
            extrato += "R$ {:.2f}\n".format(deposito)
        extrato += "Saques:\n"
        for saque in self.saques:
            extrato += "R$ {:.2f}\n".format(saque)
        extrato += "\nSaldo atual: R$ {:.2f}".format(self.saldo)
        self.info_var.set(extrato)

def deposito_click():
    valor = float(valor_entry.get())
    banco.deposito(valor)

def saque_click():
    valor = float(valor_entry.get())
    banco.saque(valor)

def extrato_click():
    banco.extrato()


#interface gráfica
root = tk.Tk()
root.title("Sistema Bancário")

banco = Banco()

# Labels
tk.Label(root, text="Valor:").grid(row=0, column=0, padx=5, pady=5)

# Entradas
valor_entry = tk.Entry(root)
valor_entry.grid(row=0, column=1, padx=5, pady=5)

# Botões
deposito_btn = tk.Button(root, text="Depósito", command=deposito_click)
deposito_btn.grid(row=1, column=0, padx=5, pady=5)

saque_btn = tk.Button(root, text="Saque", command=saque_click)
saque_btn.grid(row=1, column=1, padx=5, pady=5)

extrato_btn = tk.Button(root, text="Extrato", command=extrato_click)
extrato_btn.grid(row=1, column=2, padx=5, pady=5)

# Informações
banco.info_var = tk.StringVar()
info_label = tk.Label(root, textvariable=banco.info_var, wraplength=300)
info_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
