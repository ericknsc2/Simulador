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
    .trophy-card {
        background-color: #fff9c4;
        padding: 12px 15px;
        border-radius: 8px;
        border: 1px solid #fbc02d;
        margin-bottom: 10px;
        font-weight: bold;
        color: #5d4037;
        display: flex;
        align-items: center;
        gap: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- MAPA COMPLETO DE ESCUDOS E CLUBES ---
CLUBES_INFO = {
    "Fluminense": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Fluminense_FC_escudo.png/120px-Fluminense_FC_escudo.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Flamengo": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flamengo_braz_logo.svg/120px-Flamengo_braz_logo.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Palmeiras": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Palmeiras_logo.svg/120px-Palmeiras_logo.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "São Paulo": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sao_Paulo_Futebol_Clube.svg/120px-Sao_Paulo_Futebol_Clube.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Corinthians": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Sport_Club_Corinthians_Paulista.svg/120px-Sport_Club_Corinthians_Paulista.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Atlético Mineiro": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Atletico_mineiro_galo.png/120px-Atletico_mineiro_galo.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Grêmio": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Gremio_fbpa_logo.svg/120px-Gremio_fbpa_logo.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Internacional": {
        "pais": "Brasil 🇧🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Sport_Club_Internacional_logo.svg/120px-Sport_Club_Internacional_logo.svg.png",
        "nacionais": ["Campeonato Brasileiro (Brasileirão)", "Copa do Brasil"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "Real Madrid": {
        "pais": "Espanha 🇪🇸",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Real_Madrid_CF.svg/120px-Real_Madrid_CF.svg.png",
        "nacionais": ["La Liga (Espanha)", "Copa do Rei"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Barcelona": {
        "pais": "Espanha 🇪🇸",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/FC_Barcelona_%28crest%29.svg/120px-FC_Barcelona_%28crest%29.svg.png",
        "nacionais": ["La Liga (Espanha)", "Copa do Rei"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Manchester City": {
        "pais": "Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Manchester_City_FC_badge.svg/120px-Manchester_City_FC_badge.svg.png",
        "nacionais": ["Premier League (Inglaterra)", "FA Cup (Copa da Inglaterra)"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Manchester United": {
        "pais": "Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Manchester_United_FC_crest.svg/120px-Manchester_United_FC_crest.svg.png",
        "nacionais": ["Premier League (Inglaterra)", "FA Cup (Copa da Inglaterra)"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Liverpool": {
        "pais": "Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Liverpool_FC.svg/120px-Liverpool_FC.svg.png",
        "nacionais": ["Premier League (Inglaterra)", "FA Cup (Copa da Inglaterra)"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Bayern de Munique": {
        "pais": "Alemanha 🇩🇪",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg/120px-FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg.png",
        "nacionais": ["Bundesliga (Alemanha)", "DFB-Pokal (Copa da Alemanha)"],
        "internacionais": ["UEFA Champions League", "Mundial de Clubes da FIFA"],
    },
    "Paris Saint-Germain": {
        "pais": "França 🇫🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Paris_Saint-Germain_F.C..svg/120px-Paris_Saint-Germain_F.C..svg.png",
        "nacionais": ["Ligue 1 (França)", "Copa da França"],
        "internacionais": ["UEFA Champions League"],
    },
    "Boca Juniors": {
        "pais": "Argentina 🇦🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/CABJ_logo.svg/120px-CABJ_logo.svg.png",
        "nacionais": ["Campeonato Argentino", "Copa da Argentina"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
    },
    "River Plate": {
        "pais": "Argentina 🇦🇷",
        "escudo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/CA_River_Plate_logo_%282022%29.svg/120px-CA_River_Plate_logo_%282022%29.svg.png",
        "nacionais": ["Campeonato Argentino", "Copa da Argentina"],
        "internacionais": ["Copa Libertadores da América", "Recopa Sul-Americana"],
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
      "lista_titulos": [],  # Armazenará dicionários: {"nome": ..., "clube": ..., "escudo": ...}
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
      " com escudos personalizados e decida seu destino no mercado!"
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
      {
          "pais": "Desconhecido",
          "escudo": "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
          "nacionais": ["Liga Nacional", "Copa Nacional"],
          "internacionais": ["Competição Continental"],
      },
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
    titulos_bloco_nomes = []

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

      # Chance de ganhar títulos específicos do país e internacionais do clube
      if (
          clube_atual
          in [
              "Real Madrid",
              "Barcelona",
              "Manchester City",
              "Bayern de Munique",
              "Flamengo",
              "Palmeiras",
          ]
          and random.random() < 0.60
      ):
        conquista = random.choice(info["nacionais"] + info["internacionais"])
        titulos_bloco_nomes.append(conquista)
      elif random.random() < 0.35:
        conquista = random.choice(info["nacionais"])
        titulos_bloco_nomes.append(conquista)

    j["total_jogos"] += jogos_bloco
    j["total_gols"] += gols_bloco
    j["total_assistencias"] += assists_bloco
    
    # Salva cada título junto com o clube e o escudo da época
    for tit in titulos_bloco_nomes:
      j["lista_titulos"].append({
          "nome": tit,
          "clube": clube_atual,
          "escudo": info["escudo"]
      })

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
            "titulos": titulos_bloco_nomes,
        },
    )

    j["bloco_atual"] += 1

    # Sorteio super aleatório de 2 propostas entre todos os outros clubes
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

  # Agrupa os títulos contando a quantidade e mantendo a referência do escudo/clube
  contagem_titulos = {}
  for item in j["lista_titulos"]:
    nome_t = item["nome"]
    escudo_t = item["escudo"]
    if nome_t not in contagem_titulos:
      contagem_titulos[nome_t] = {"qtd": 0, "escudo": escudo_t}
    contagem_titulos[nome_t]["qtd"] += 1

  st.markdown(
      f"""
    ### 📊 Resumo Definitivo da Carreira
    * **Partidas Totais:** {j['total_jogos']}
    * **Gols Marcados:** {j['total_gols']}
    * **Assistências:** {j['total_assistencias']}
    * **Participações em Gols:** {j['total_gols'] + j['total_assistencias']}
    """
  )

  st.markdown("### 🥇 Galeria de Títulos Conquistados")
  if contagem_titulos:
    for t, dados in contagem_titulos.items():
      st.markdown(
          f"""
            <div class="trophy-card">
                <img src="{dados['escudo']}" width="35" style="margin-right: 10px;">
                <span>🏆 {dados['qtd']}x - {t}</span>
            </div>
            """,
          unsafe_allow_html=True,
      )
  else:
    st.markdown(
        "<div class='trophy-card'>Nenhum título de expressão conquistado na"
        " carreira.</div>",
        unsafe_allow_html=True,
    )

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🔄 Iniciar Nova Carreira"):
    st.session_state.etapa = "criacao"
    st.session_state.jogador = {}
    st.session_state.historico_blocos = []
    st.session_state.propostas_atuais = []
    st.rerun()
