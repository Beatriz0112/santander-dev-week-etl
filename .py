# --- ETAPA 1: EXTRAÇÃO (E) ---
# Simulando a extração de dados (pode ser uma lista ou leitura de CSV)
clientes = [
    {"id": 1, "nome": "Alice", "saldo": 1500.0, "tipo": "Premium"},
    {"id": 2, "nome": "Bruno", "saldo": 500.0, "tipo": "Fidelizado"},
    {"id": 3, "nome": "Carla", "saldo": 100.0, "tipo": "Novo cliente"}
]

print("Extração concluída: Dados carregados com sucesso.")

# --- ETAPA 2: TRANSFORMAÇÃO (T) ---
# Aqui criamos a lógica de negócio (ex: gerar uma mensagem de boas-vindas)
def gerar_mensagem(cliente):
    nome = cliente["nome"]
    saldo = cliente["saldo"]
    
    if saldo > 1000:
        return f"Olá {nome}, vimos que seu saldo de R${saldo:.2f} está rendendo! Conheça nossas opções de investimento VIP."
    else:
        return f"Olá {nome}, aproveite as vantagens de ser um cliente {cliente['tipo']}!"

# Aplicando a transformação
for cliente in clientes:
    cliente["mensagem_personalizada"] = gerar_mensagem(cliente)

print("Transformação concluída: Mensagens geradas.")

# --- ETAPA 3: CARREGAMENTO (L) ---
# Salvando o resultado (aqui exibimos no console, simulando o envio para um banco/arquivo)
print("\n--- RESULTADO FINAL DO PROCESSO ETL ---")
for cliente in clientes:
    print(f"ID: {cliente['id']} | Cliente: {cliente['nome']}")
    print(f"Mensagem: {cliente['mensagem_personalizada']}")
    print("-" * 30)

print("\nCarga concluída: Dados prontos para o marketing.")
