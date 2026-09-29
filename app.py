import random
import streamlit as st

st.set_page_config(
    page_title="Simulador de Carreira - Estatísticas",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILIZAÇÃO VISUAL ---
st.markdown(
    """
<style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
        background-color: #1f77b4;
        color: white;
    }
    .stButton>button:hover {
        background-color: #135d8a;
    }
    .stats-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- MAPA DE ESCUDOS / BANDEIRAS PARA OS CLUBES ---
CLUBES_INFO = {
    "Fluminense": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Fluminense_FC_escudo.png/120px-Fluminense_FC_escudo.png",
    },
    "Flamengo": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flamengo_braz_logo.svg/120px-Flamengo_braz_logo.svg.png",
    },
    "Palmeiras": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Palmeiras_logo.svg/120px-Palmeiras_logo.svg.png",
    },
    "São Paulo": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sao_Paulo_Futebol_Clube.svg/120px-Sao_Paulo_Futebol_Clube.svg.png",
    },
    "Real Madrid": {
        "pais": "Espanha 🇪🇸",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Real_Madrid_CF.svg/120px-Real_Madrid_CF.svg.png",
    },
    "Manchester City": {
        "pais": "Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Manchester_City_FC_badge.svg/120px-Manchester_City_FC_badge.svg.png",
    },
    "Bayern de Munique": {
        "pais": "Alemanha 🇩🇪",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg/120px-FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg.png",
    },
}

# --- INICIALIZAÇÃO DO ESTADO ---
if "etapa" not in st.session_state:
  st.session_state.etapa = "criacao"

if "jogador" not in st.session_state or not st.session_state.jogador:
  st.session_state.jogador = {
      "nome": "Erick",
      "posicao": "Centroavante (Atacante)",
      "clube": "Fluminense",
      "idade": 18,
      "bloco_atual": 1,
      "total_jogos": 0,
      "total_gols": 0,
      "total_assistencias": 0,
      "lista_titulos": [],
  }

if "historico_blocos" not in st.session_state:
  st.session_state.historico_blocos = []

if "propostas_atuais" not in st.session_state:
  st.session_state.propostas_atuais = []

# ==========================================
# TELA 1: CRIAÇÃO DO JOGADOR
# ==========================================
if st.session_state.etapa == "criacao":
  st.title("⚽ Simulador de Carreira em Blocos")
  st.markdown(
      "Simule ciclos de 3 a 4 temporadas, veja seus números, conquiste títulos"
      " e decida seu destino no mercado!"
  )
  st.markdown("---")

  with st.form("form_criacao"):
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
    clube_inicial = st.selectbox("Clube de Estreia:", list(CLUBES_INFO.keys()))

    enviar = st.form_submit_button("🚀 Iniciar Trajetória")

    if enviar:
      if not nome.strip():
        st.error("Digite um nome válido.")
      else:
        st.session_state.jogador = {
            "nome": nome,
            "posicao": posicao,
            "clube": clube_inicial,
            "idade": 18,
            "bloco_atual": 1,
            "total_jogos": 0,
            "total_gols": 0,
            "total_assistencias": 0,
            "lista_titulos": [],
        }
        st.session_state.historico_blocos = []
        st.session_state.etapa = "simulacao"
        st.rerun()

# ==========================================
# TELA 2: SIMULAÇÃO DE BLOCO (3 a 4 Temporadas)
# ==========================================
elif st.session_state.etapa == "simulacao":
  j = st.session_state.jogador
  clube_atual = j["clube"]
  info = CLUBES_INFO.get(
      clube_atual,
      {"pais": "Desconhecido", "escudo": "https://via.placeholder.com/120"},
  )

  col_img, col_txt = st.columns([1, 4])
  with col_img:
    st.image(info["escudo"], width=90)
  with col_txt:
    st.title(f"{j['nome']}")
    st.markdown(
        f"**Posição:** {j['posicao']} &nbsp;|&nbsp; **Clube:** {clube_atual}"
        f" ({info['pais']}) &nbsp;|&nbsp; **Idade:** {j['idade']} anos"
    )

  st.markdown("<div class='stats-box'>", unsafe_allow_html=True)
  st.markdown("### 📊 Totais na Carreira Até o Momento")
  c1, c2, c3, c4 = st.columns(4)
  c1.metric("Partidas", j["total_jogos"])
  c2.metric("Gols", j["total_gols"])
  c3.metric("Assistências", j["total_assistencias"])
  c4.metric("Títulos", len(j["lista_titulos"]))
  st.markdown("</div>", unsafe_allow_html=True)

  st.subheader(
      f"⚡ Bloco {j['bloco_atual']} (Simulação de 3 a 4 Temporadas)"
  )
  st.markdown(
      "Clique abaixo para simular este ciclo de desempenho e ver o que"
      " aconteceu em campo!"
  )

  if st.button("▶️ Simular Próximas Temporadas"):
    qtd_temporadas = random.choice([3, 4])

    jogos_bloco = 0
    gols_bloco = 0
    assists_bloco = 0
    titulos_bloco = []

    opcoes_titulos = [
        "Campeonato Nacional",
        "Copa Nacional",
        "Supercopa",
        "Libertadores / Champions League",
    ]

    for t in range(qtd_temporadas):
      if "Centroavante" in j["posicao"]:
        j_temp = random.randint(45, 55)
        g_temp = random.randint(18, 35)
        a_temp = random.randint(3, 9)
      elif "Ponta" in j["posicao"]:
        j_temp = random.randint(45, 55)
        g_temp = random.randint(12, 24)
        a_temp = random.randint(10, 20)
      elif "Meia" in j["posicao"]:
        j_temp = random.randint(48, 58)
        g_temp = random.randint(6, 15)
        a_temp = random.randint(15, 28)
      else:
        j_temp = random.randint(45, 55)
        g_temp = random.randint(1, 6)
        a_temp = random.randint(3, 9)

      jogos_bloco += j_temp
      gols_bloco += g_temp
      assists_bloco += a_temp

      if (
          clube_atual
          in ["Real Madrid", "Manchester City", "Bayern de Munique", "Flamengo"]
          and random.random() < 0.65
      ):
        conquista = random.choice(opcoes_titulos)
        titulos_bloco.append(conquista)
      elif random.random() < 0.35:
        conquista = random.choice(
            ["Campeonato Estadual / Regional", "Copa Nacional"]
        )
        titulos_bloco.append(conquista)

    j["total_jogos"] += jogos_bloco
    j["total_gols"] += gols_bloco
    j["total_assistencias"] += assists_bloco
    j["lista_titulos"].extend(titulos_bloco)
    j["idade"] += qtd_temporadas

    st.session_state.historico_blocos.insert(
        0,
        {
            "bloco": j["bloco_atual"],
            "clube": clube_atual,
            "temporadas": qtd_temporadas,
            "jogos": jogos_bloco,
            "gols": gols_bloco,
            "assists": assists_bloco,
            "titulos": titulos_bloco,
        },
    )

    j["bloco_atual"] += 1

    # Prepara as propostas para a tela seguinte
    outros_times = [c for c in CLUBES_INFO.keys() if c != j["clube"]]
    st.session_state.propostas_atuais = random.sample(outros_times, 2)

    if j["idade"] >= 38 or j["bloco_atual"] > 5:
      st.session_state.etapa = "fim"
    else:
      st.session_state.etapa = "transferencia"

    st.rerun()

  if st.session_state.historico_blocos:
    st.markdown("---")
    st.subheader("📜 Histórico de Ciclos Anteriores")
    for h in st.session_state.historico_blocos:
      titulos_str = ", ".join(h["titulos"]) if h["titulos"] else "Nenhum título"
      st.write(
          f"**{h['clube']}** ({h['temporadas']} temporadas) ➡ Jogos:"
          f" **{h['jogos']}** | Gols: **{h['gols']}** | Assistências:"
          f" **{h['assists']}** | Títulos: *{titulos_str}*"
      )

# ==========================================
# TELA 3: DECISÃO DE TRANSFERÊNCIA
# ==========================================
elif st.session_state.etapa == "transferencia":
  j = st.session_state.jogador
  ultimo_bloco = st.session_state.historico_blocos[0]

  st.title("🔄 Janela de Transferências")
  st.success(
      f"Você concluiu mais um ciclo de {ultimo_bloco['temporadas']} temporadas"
      f" no **{ultimo_bloco['clube']}**!"
  )

  st.markdown(
      f"""
    ### 📈 Desempenho no último ciclo:
    * **Partidas:** {ultimo_bloco['jogos']} | **Gols:** {ultimo_bloco['gols']} | **Assistências:** {ultimo_bloco['assists']}
    * **Títulos conquistados:** {', '.join(ultimo_bloco['titulos']) if ultimo_bloco['titulos'] else 'Nenhum'}
    """
  )

  st.markdown("---")
  st.subheader("O que você deseja fazer para a próxima fase?")

  opcoes = [f"Continuar no clube atual ({j['clube']})"] + [
      f"Aceitar proposta do {p}" for p in st.session_state.propostas_atuais
  ]

  with st.form("form_transferencia"):
    escolha_usuario = st.radio("Escolha seu destino:", opcoes)
    confirmar = st.form_submit_button("Confirmar Destino e Continuar Carreira")

    if confirmar:
      if "Continuar" not in escolha_usuario:
        novo_clube = escolha_usuario.replace("Aceitar proposta do ", "").strip()
        j["clube"] = novo_clube
      
      st.session_state.etapa = "simulacao"
      st.rerun()

# ==========================================
# TELA 4: APOSENTADORIA / RELATÓRIO FINAL
# ==========================================
elif st.session_state.etapa == "fim":
  j = st.session_state.jogador
  st.title("🏆 Fim da Carreira - Relatório Oficial")

  st.success(
      f"{j['nome']} pendurou as chuteiras aos {j['idade']} anos de idade!"
  )

  contagem_titulos = {}
  for tit in j["lista_titulos"]:
    contagem_titulos[tit] = contagem_titulos.get(tit, 0) + 1

  texto_titulos_formatado = ""
  if contagem_titulos:
    for t, qtd in contagem_titulos.items():
      texto_titulos_formatado += f"* **{qtd}x** {t}\n"
  else:
    texto_titulos_formatado = "* Nenhum título de expressão conquistado.\n"

  st.markdown(
      f"""
    ### 📊 Resumo Definitivo da Carreira
    * **Partidas Totais:** {j['total_jogos']}
    * **Gols Marcados:** {j['total_gols']}
    * **Assistências:** {j['total_assistencias']}
    * **Participações em Gols:** {j['total_gols'] + j['total_assistencias']}

    ### 🥇 Galeria de Títulos Conquistados ({len(j['lista_titulos'])} no total):
    {texto_titulos_formatado}
    """
  )

  if st.button("🔄 Iniciar Nova Carreira"):
    st.session_state.etapa = "criacao"
    st.session_state.jogador = {}
    st.session_state.historico_blocos = []
    st.session_state.propostas_atuais = []
    st.rerun()
  if st.button("🔄 Iniciar Nova Carreira"):
    st.session_state.etapa = "criacao"
    st.session_state.jogador = {}
    st.session_state.historico_blocos = []
    st.rerun()
