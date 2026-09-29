import random
import streamlit as st

st.set_page_config(
    page_title="Carreira 99 - Simulador de Jogador",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILIZAÇÃO CSS (Visual Gamer / Moderno) ---
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
    .card-stats {
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

# --- INICIALIZAÇÃO DO ESTADO DO JOGO ---
if "etapa" not in st.session_state:
  st.session_state.etapa = "criacao"
if "jogador" not in st.session_state:
  st.session_state.jogador = {}
if "log_eventos" not in st.session_state:
  st.session_state.log_eventos = []

# --- BANCO DE EVENTOS DA CARREIRA ---
EVENTOS_POSSIVEIS = [
    {
        "titulo": "Treinador Briga com o Craque do Time",
        "texto": (
            "O principal jogador do time discutiu com o técnico no vestiário"
            " e foi afastado. O treinador olha para você e pergunta se você"
            " está pronto para assumir a titularidade na próxima partida."
        ),
        "opcoes": [
            (
                "Chamar a responsabilidade (Treinar duro e pedir titularidade)",
                {"tecnica": +3, "fama": +2, "relacionamento": +2},
                (
                    "Você jogou muito bem, marcou gol e a torcida começou a"
                    " cantar seu nome!"
                ),
            ),
            (
                "Ficar na sua (Continuar trabalhando quieto no banco)",
                {"energia": +1, "relacionamento": +1},
                (
                    "Você evitou polêmicas, ganhou a confiança do grupo mas"
                    " seguiu na reserva por enquanto."
                ),
            ),
            (
                "Reclamar nas redes sociais que merecia mais chances",
                {"fama": +3, "relacionamento": -4, "tecnica": -1},
                (
                    "A torcida achou ousado, mas o técnico odiou sua postura e"
                    " te colocou na geladeira."
                ),
            ),
        ],
    },
    {
        "titulo": "Proposta Tentadora da Noite",
        "texto": (
            "Vseus amigos te convidaram para uma festa open bar na véspera de"
            " um jogo decisivo fora de casa. Amanhã tem treino físico puxado."
        ),
        "opcoes": [
            (
                "Recusar e focar no descanso em casa",
                {"energia": +2, "tecnica": +1},
                (
                    "Você acordou revigorado, treinou como um monstro e foi"
                    " elogiado pela comissão técnica."
                ),
            ),
            (
                "Ir pra festa escondido só por duas horinhas",
                {"energia": -3, "fama": +2, "dinheiro": -500},
                (
                    "Você curtiu, mas chegou exausto no CT. O preparador físico"
                    " percebeu seu cansaço."
                ),
            ),
        ],
    },
    {
        "titulo": "Oferta de Patrocínio de Marca Exótica",
        "texto": (
            "Uma marca de energético duvidosa quer que você use os produtos"
            " deles e poste nas redes sociais em troca de um bom dinheiro."
        ),
        "opcoes": [
            (
                "Aceitar o contrato e fazer a publi",
                {"dinheiro": +3000, "fama": +2, "relacionamento": -1},
                (
                    "Sua conta bancária engordou, mas o clube não gostou muito da"
                    " sua exposição extra-campo."
                ),
            ),
            (
                "Recusar para manter o foco total na carreira profissional",
                {"tecnica": +2, "relacionamento": +2},
                (
                    "Você mostrou profissionalismo exemplar e ganhou moral com a"
                    " diretoria."
                ),
            ),
        ],
    },
    {
        "titulo": "Lesão no Treinamento",
        "texto": (
            "Em uma dividida forte no treino de quinta-feira, você sente uma"
            " pontada na posterior da coxa esquerda."
        ),
        "opcoes": [
            (
                "Esconder a dor e continuar treinando",
                {"tecnica": -2, "energia": -4, "relacionamento": -2},
                (
                    "A lesão piorou no jogo do fim de semana. Você vai precisar"
                    " de semanas de recuperação."
                ),
            ),
            (
                "Avisar o departamento médico imediatamente",
                {"energia": +1, "tecnica": -1},
                (
                    "Você ficou de fora por uma rodada, mas se recuperou 100%"
                    " sem sequelas."
                ),
            ),
        ],
    },
]

# ==========================================
# TELA 1: CRIAÇÃO DO JOGADOR
# ==========================================
if st.session_state.etapa == "criacao":
  st.title("⚽ Carreira 99 - O Simulador")
  st.markdown(
      "Viva a vida de um jogador de futebol profissional tomadas de decisão,"
      " festas, treinos e transferências!"
  )
  st.markdown("---")

  with st.form("form_criacao"):
    nome = st.text_input("Nome do Jogador:", value="Erick")
    posicao = st.selectbox(
        "Posição em Campo:",
        [
            "Atacante (Artilheiro)",
            "Meia Construtor (Camisa 10)",
            "Volante Cão de Guarda",
            "Zagueiro Xerife",
            "Goleiro Paredão",
        ],
    )
    clube_inicio = st.selectbox(
        "Clube de Início:",
        [
            "Remo (Série B - Brasil)",
            "Chapecoense (Série B - Brasil)",
            "Coritiba (Série B - Brasil)",
            "Mirassol (Série B - Brasil)",
        ],
    )

    enviar = st.form_submit_button("🚀 Iniciar Carreira Profissional")

    if enviar:
      if not nome.strip():
        st.error("Por favor, digite um nome válido para o jogador.")
      else:
        st.session_state.jogador = {
            "nome": nome,
            "posicao": posicao,
            "clube": clube_inicio.split(" (")[0],
            "idade": 18,
            "temporada": 1,
            "tecnica": random.randint(55, 65),
            "fama": 10,
            "dinheiro": 2500,
            "energia": 80,
            "relacionamento": 50,
            "gols": 0,
            "titulos": 0,
        }
        st.session_state.etapa = "jogo"
        st.session_state.log_eventos = [
            f"Contrato profissional assinado com o {st.session_state.jogador['clube']}!"
        ]
        st.rerun()

# ==========================================
# TELA 2: PAINEL PRINCIPAL DO JOGO
# ==========================================
elif st.session_state.etapa == "jogo":
  j = st.session_state.jogador

  st.title(f"⭐ {j['nome']} ({j['idade']} anos)")
  st.markdown(
      f"**Clube atual:** {j['clube']} &nbsp;|&nbsp; **Posição:**"
      f" {j['posicao']} &nbsp;|&nbsp; **Temporada:** {j['temporada']}/10"
  )

  # Painel de Atributos em Colunas
  st.markdown("<div class='card-stats'>", unsafe_allow_html=True)
  c1, c2, c3, c4, c5 = st.columns(5)
  c1.metric("🎯 Técnica", f"{j['tecnica']}")
  c2.metric("⚡ Energia", f"{j['energia']}%")
  c3.metric("🌟 Fama", f"{j['fama']}")
  c4.metric("💰 Saldo", f"R$ {j['dinheiro']:,}")
  c5.metric("⚽ Gols", f"{j['gols']}")
  st.markdown("</div>", unsafe_allow_html=True)

  st.subheader(f"📅 Temporada {j['temporada']} - Decisão de Carreira")

  # Sorteia um evento aleatório para esta rodada
  if "evento_atual" not in st.session_state:
    st.session_state.evento_atual = random.choice(EVENTOS_POSSIVEIS)

  ev = st.session_state.evento_atual

  st.info(f"**{ev['titulo']}**\n\n{ev['texto']}")

  escolha_usuario = st.radio(
      "O que você decide fazer?",
      range(len(ev["opcoes"])),
      format_func=lambda x: ev["opcoes"][x][0],
  )

  if st.button("Confirmar Decisão e Avançar"):
    _, alteracoes, feedback = ev["opcoes"][escolha_usuario]

    # Aplica alterações nos atributos
    j["tecnica"] = max(10, min(99, j["tecnica"] + alteracoes.get("tecnica", 0)))
    j["energia"] = max(0, min(100, j["energia"] + alteracoes.get("energia", 0)))
    j["fama"] = max(0, min(100, j["fama"] + alteracoes.get("fama", 0)))
    j["dinheiro"] += alteracoes.get("dinheiro", 1500)  # Salário base por rodada
    j["relacionamento"] = max(
        0, min(100, j["relacionamento"] + alteracoes.get("relacionamento", 0))
    )

    # Simula desempenho esportivo da rodada
    if j["tecnica"] > 70 and random.random() > 0.3:
      gols_partida = random.randint(1, 2)
      j["gols"] += gols_partida
      feedback += f" Você jogou muito bem e marcou {gols_partida} gol(s) nesta fase!"
    else:
      feedback += " Sua atuação passou um pouco apagada nesta rodada."

    st.success(feedback)
    st.session_state.log_eventos.insert(
        0, f"Temporada {j['temporada']}: {feedback}"
    )

    # Avança temporada ou finaliza jogo
    if j["temporada"] >= 10 or j["energia"] <= 0:
      st.session_state.etapa = "fim"
    else:
      j["temporada"] += 1
      j["energia"] = min(
          100, j["energia"] + 25
      )  # Recupera um pouco de energia nas férias
      del st.session_state.evento_atual

    st.rerun()

  with st.expander("📜 Histórico da Carreira"):
    for log in st.session_state.log_eventos:
      st.write(f"- {log}")

# ==========================================
# TELA 3: FIM DE CARREIRA / LEGADO
# ==========================================
elif st.session_state.etapa == "fim":
  j = st.session_state.jogador
  st.title("🏆 Fim da Carreira - Ficha de Legado")

  # Define status de aposentadoria
  if j["fama"] >= 75 and j["tecnica"] >= 80:
    status_final = (
        "Lenda do Futebol! Você se aposentou ovacionado e virou ídolo"
        " internacional."
    )
  elif j["fama"] >= 50:
    status_final = (
        "Carreira Sólida! Jogou em bons clubes, ganhou dinheiro e construiu"
        " respeito."
    )
  else:
    status_final = (
        "Carreira Modesta. Pendurou as chuteiras cedo e virou comentarista de"
        " podcast regional."
    )

  st.success(status_final)

  st.markdown(
      f"""
    ### 📊 Resumo Final de {j['nome']}
    * **Clube de Aposentadoria:** {j['clube']}
    * **Gols na Carreira:** {j['gols']} gols marcados
    * **Patrimônio Acumulado:** R$ {j['dinheiro']:,}
    * **Nível Técnico Final:** {j['tecnica']} / 99
    * **Fama Final:** {j['fama']} / 100
    """
  )

  if st.button("🔄 Jogar Novamente"):
    for key in list(st.session_state.keys()):
      del st.session_state[key]
    st.rerun()