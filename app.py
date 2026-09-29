import random
import streamlit as st

st.set_page_config(
    page_title="Simulador de Estatísticas - Carreira",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILIZAÇÃO CSS ---
st.markdown(
    """
<style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
    }
    .stats-box {
        background-color: #f1f8e9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-bottom: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- INICIALIZAÇÃO SEGURA DO ESTADO ---
if "etapa" not in st.session_state:
  st.session_state.etapa = "criacao"

if "jogador" not in st.session_state or not st.session_state.jogador:
  st.session_state.jogador = {
      "nome": "Erick",
      "posicao": "Centroavante (Atacante)",
      "clube": "Fluminense (Brasil)",
      "idade": 18,
      "tempor_atual": 1,
      "total_jogos": 0,
      "total_gols": 0,
      "total_assistencias": 0,
      "total_titulos": 0,
  }

if "historico" not in st.session_state:
  st.session_state.historico = []

CLUBES = [
    "Fluminense (Brasil)",
    "Flamengo (Brasil)",
    "Palmeiras (Brasil)",
    "São Paulo (Brasil)",
    "Real Madrid (Espanha)",
    "Manchester City (Inglaterra)",
    "Bayern de Munique (Alemanha)",
]

# ==========================================
# TELA 1: CRIAÇÃO DO JOGADOR
# ==========================================
if st.session_state.etapa == "criacao":
  st.title("⚽ Simulador de Carreira e Estatísticas")
  st.markdown(
      "Acompanhe cada gol, assistência, partida e título da sua trajetória"
      " profissional até a aposentadoria!"
  )
  st.markdown("---")

  with st.form("form_stats"):
    nome = st.text_input("Nome do Jogador:", value="Erick")
    posicao = st.selectbox(
        "Posição:",
        [
            "Centroavante (Atacante)",
            "Ponta / Extremo",
            "Meia Ofensivo (Camisa 10)",
            "Volante / Meia Central",
            "Zagueiro / Lateral",
        ],
    )
    clube_atual = st.selectbox("Clube de Estreia:", CLUBES)

    enviar = st.form_submit_button("🎯 Iniciar Trajetória")

    if enviar:
      if not nome.strip():
        st.error("Digite um nome válido.")
      else:
        st.session_state.jogador = {
            "nome": nome,
            "posicao": posicao,
            "clube": clube_atual,
            "idade": 18,
            "tempor_atual": 1,
            "total_jogos": 0,
            "total_gols": 0,
            "total_assistencias": 0,
            "total_titulos": 0,
        }
        st.session_state.historico = []
        st.session_state.etapa = "simulacao"
        st.rerun()

# ==========================================
# TELA 2: PAINEL DE SIMULAÇÃO POR TEMPORADA
# ==========================================
elif st.session_state.etapa == "simulacao":
  j = st.session_state.jogador

  st.title(f"📊 Carreira de {j['nome']}")
  st.markdown(
      f"**Posição:** {j['posicao']} &nbsp;|&nbsp; **Clube Atual:** {j['clube']}"
      f" &nbsp;|&nbsp; **Idade:** {j['idade']} anos"
  )

  # Totais da Carreira
  st.markdown("<div class='stats-box'>", unsafe_allow_html=True)
  st.markdown("### 🏆 Totais na Carreira")
  c1, c2, c3, c4 = st.columns(4)
  c1.metric("Partidas", j["total_jogos"])
  c2.metric("Gols", j["total_gols"])
  c3.metric("Assistências", j["total_assistencias"])
  c4.metric("Títulos", j["total_titulos"])
  st.markdown("</div>", unsafe_allow_html=True)

  st.subheader(f"📅 Simular Temporada {j['tempor_atual']}/15")

  col_a, col_b = st.columns(2)
  com_lesao = col_a.checkbox(
      "Enfrentar lesão leve na temporada?",
      value=False,
      help="Reduz um pouco o número de jogos disputados.",
  )
  fase_boa = col_b.checkbox(
      "Fase iluminada (Artilheiro/Destaque)?",
      value=True,
      help="Aumenta as chances de gols e títulos.",
  )

  if st.button("▶️ Jogar Temporada"):
    fator = 1.2 if fase_boa else 0.8
    if com_lesao:
      fator *= 0.75

    if "Centroavante" in j["posicao"]:
      jogos = int(random.randint(45, 60) * (0.9 if com_lesao else 1.0))
      gols = int(random.randint(15, 35) * fator)
      assists = int(random.randint(3, 10) * fator)
    elif "Ponta" in j["posicao"]:
      jogos = int(random.randint(45, 60) * (0.9 if com_lesao else 1.0))
      gols = int(random.randint(10, 22) * fator)
      assists = int(random.randint(10, 20) * fator)
    elif "Meia" in j["posicao"]:
      jogos = int(random.randint(48, 62) * (0.9 if com_lesao else 1.0))
      gols = int(random.randint(5, 14) * fator)
      assists = int(random.randint(15, 28) * fator)
    else:
      jogos = int(random.randint(45, 60) * (0.9 if com_lesao else 1.0))
      gols = int(random.randint(1, 6) * fator)
      assists = int(random.randint(2, 8) * fator)

    titulos_ano = 0
    if random.random() < (0.5 if fase_boa else 0.2):
      titulos_ano = random.randint(1, 3)

    j["total_jogos"] += jogos
    j["total_gols"] += gols
    j["total_assistencias"] += assists
    j["total_titulos"] += titulos_ano

    st.session_state.historico.insert(
        0,
        {
            "temporada": j["tempor_atual"],
            "idade": j["idade"],
            "clube": j["clube"],
            "jogos": jogos,
            "gols": gols,
            "assists": assists,
            "titulos": titulos_ano,
        },
    )

    j["idade"] += 1
    j["tempor_atual"] += 1

    if j["tempor_atual"] % 3 == 0:
      j["clube"] = random.choice([c for c in CLUBES if c != j["clube"]])
      st.toast(
          f"Mercado da bola: {j['nome']} transferiu-se para o {j['clube']}!",
          icon="🚨",
      )

    if j["tempor_atual"] > 15 or j["idade"] >= 38:
      st.session_state.etapa = "fim"

    st.rerun()

  if st.button("🔄 Reiniciar Carreira"):
    st.session_state.etapa = "criacao"
    st.session_state.jogador = {}
    st.session_state.historico = []
    st.rerun()

  if st.session_state.historico:
    st.markdown("---")
    st.subheader("📜 Desempenho por Temporada")
    for h in st.session_state.historico:
      st.write(
          f"**Temporada {h['temporada']} ({h['idade']} anos) - {h['clube']}**"
          f" ➡ Jogos: **{h['jogos']}** | Gols: **{h['gols']}** | Assistências:"
          f" **{h['assists']}** | Títulos: **{h['titulos']}**"
      )

# ==========================================
# TELA 3: APOSENTADORIA / ESTATÍSTICAS FINAIS
# ==========================================
elif st.session_state.etapa == "fim":
  j = st.session_state.jogador
  st.title("🏆 Fim da Carreira - Relatório Estatístico")

  st.success(
      f"{j['nome']} pendurou as chuteiras após uma jornada marcante nos"
      " gramados!"
  )

  st.markdown(
      f"""
    ### 📈 Números Finais da Carreira
    * **Partidas Totais:** {j['total_jogos']}
    * **Gols Marcados:** {j['total_gols']}
    * **Assistências:** {j['total_assistencias']}
    * **Participações em Gols:** {j['total_gols'] + j['total_assistencias']}
    * **Títulos Conquistados:** {j['total_titulos']}
    """
  )

  if st.button("🔄 Iniciar Nova Carreira"):
    st.session_state.etapa = "criacao"
    st.session_state.jogador = {}
    st.session_state.historico = []
    st.rerun()
