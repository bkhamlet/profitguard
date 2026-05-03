import streamlit as st

# Configurações básicas da página
st.set_page_config(page_title="ProfitGuard", page_icon="🛡️")

st.title("🛡️ ProfitGuard")
st.subheader("Calculadora de Impacto Financeiro do Retrabalho")

# Entradas de dados
valor_hora = st.number_input("💰 Valor da Hora (R$)", value=150.0)
horas_total = st.number_input("⏱️ Total de Horas do Projeto", value=200.0)
horas_retrabalho = st.number_input("🔁 Horas de Retrabalho", value=40.0)

# Cálculos
custo_direto = valor_hora * horas_retrabalho
custo_oportunidade = custo_direto * 3
preco_do_erro = custo_direto + custo_oportunidade

# Exibição do Resultado
st.error(f"🚨 Preço do Erro: R$ {preco_do_erro:,.2f}")

st.markdown("---")
st.subheader("🤖 Insights de IA")
st.write("1. Implemente revisões de código semanais.")
st.write("2. Melhore a definição de requisitos antes de iniciar o desenvolvimento.")
st.write("3. Invista em testes automatizados para detectar erros mais cedo.")
