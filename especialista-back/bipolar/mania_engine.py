from flask import Blueprint
from pyknow import AND, OR, NOT, Rule, KnowledgeEngine, W, MATCH

from bipolar.bipolar_engine import Sintomas
from bipolar.services import ask, verifica_conjunto

mania = Blueprint(r'mania', __name__)


@mania.route('/')
def verifica_mania(sockets):
    mania_engine = Mania(sockets)
    mania_engine.reset()
    mania_engine.run()


class Mania(KnowledgeEngine):
    """
    Coleta dos dados
    """

    def __init__(self, sockets):
        super().__init__()
        self.sockets = sockets

    @Rule(NOT(Sintomas(fisiologico=W())))
    def ask_data_fisiologico(self):
        self.sockets.send("fisiologico")
        self.declare(Sintomas(fisiologico=self.sockets.receive()))

    @Rule(NOT(Sintomas(prejuizo_social=W())))
    def ask_data_prejuizo_social(self):
        self.declare(Sintomas(prejuizo_social=ask("prejuizo_social? ")))

    @Rule(NOT(Sintomas(prejuiso_profissional=W())))
    def ask_data_prejuiso_profissional(self):
        self.declare(Sintomas(prejuiso_profissional=ask("prejuiso_profissional? ")))

    @Rule(NOT(Sintomas(psicose=W())))
    def ask_data_psicose(self):
        self.declare(Sintomas(psicose=ask("psicose? ")))

    @Rule(NOT(Sintomas(autoestima_inflada=W())))
    def ask_data_autoestima_inflada(self):
        self.declare(Sintomas(autoestima_inflada=ask("autoestima_inflada? ")))

    @Rule(NOT(Sintomas(grafndiosidade=W())))
    def ask_data_grandiosidade(self):
        self.declare(Sintomas(grandiosidade=ask("grandiosidade? ")))

    @Rule(NOT(Sintomas(loquaz=W())))
    def ask_data_loquaz(self):
        self.declare(Sintomas(loquaz=ask("loquaz? ")))

    @Rule(NOT(Sintomas(pressao_continuar_falando=W())))
    def ask_data_pressao_continuar_falando(self):
        self.declare(Sintomas(pressao_continuar_falando=ask("pressao_continuar_falando? ")))

    @Rule(NOT(Sintomas(fuga_ideias=W())))
    def ask_data_fuga_ideias(self):
        self.declare(Sintomas(fuga_ideias=ask("fuga_ideias? ")))

    @Rule(NOT(Sintomas(pensamento_acelerado=W())))
    def ask_data_pensamento_acelerado(self):
        self.declare(Sintomas(pensamento_acelerado=ask("pensamento_acelerado? ")))

    @Rule(NOT(Sintomas(aumento_atividade_objetivo=W())))
    def ask_data_aumento_atividade_objetivo(self):
        self.declare(Sintomas(aumento_atividade_objetivo=ask("aumento_atividade_objetivo? ")))

    @Rule(NOT(Sintomas(agitacao_psicomotora=W())))
    def ask_data_agitacao_psicomotora(self):
        self.declare(Sintomas(agitacao_psicomotora=ask("agitacao_psicomotora? ")))

    @Rule(NOT(Sintomas(reducao_sono=W())))
    def ask_data_reducao_sono(self):
        self.declare(Sintomas(reducao_sono=ask("reducao_sono? ")))

    @Rule(NOT(Sintomas(distrabilidade=W())))
    def ask_data_distrabilidade(self):
        self.declare(Sintomas(distrabilidade=ask("distrabilidade? ")))

    @Rule(NOT(Sintomas(envolvimento_atividade_risco=W())))
    def ask_data_envolvimento_atividade_risco(self):
        self.declare(Sintomas(envolvimento_atividade_risco=ask("envolvimento_atividade_risco? ")))

    @Rule(AND(
        NOT(Sintomas(mudanca_comportamental=W())),
        AND(
            OR(Sintomas(autoestima_excessiva=0), Sintomas(autoestima_excessiva=1)),
            Sintomas(autoestima_excessiva=MATCH.autoestima_excessiva)
        ),
        AND(
            OR(Sintomas(reducao_sono=0), Sintomas(reducao_sono=1)),
            Sintomas(reducao_sono=MATCH.reducao_sono)
        ),
        AND(
            OR(Sintomas(aumento_fala=0), Sintomas(aumento_fala=1)),
            Sintomas(aumento_fala=MATCH.aumento_fala)
        ),
        AND(
            OR(Sintomas(mudanca_modo_pensar=0), Sintomas(mudanca_modo_pensar=1)),
            Sintomas(mudanca_modo_pensar=MATCH.mudanca_modo_pensar)
        ),
        AND(
            OR(Sintomas(distrabilidade=0), Sintomas(distrabilidade=1)),
            Sintomas(distrabilidade=MATCH.distrabilidade)
        ),
        AND(
            OR(Sintomas(agitacao=0), Sintomas(agitacao=1)),
            Sintomas(agitacao=MATCH.agitacao)
        ),
        AND(
            OR(Sintomas(envolvimento_atividade_risco=0), Sintomas(envolvimento_atividade_risco=1)),
            Sintomas(envolvimento_atividade_risco=MATCH.envolvimento_atividade_risco)
        )
    ))
    def define_mudanca_comportamental(self,
                                      autoestima_excessiva,
                                      reducao_sono,
                                      aumento_fala,
                                      mudanca_modo_pensar,
                                      distrabilidade,
                                      agitacao,
                                      envolvimento_atividade_risco
                                      ):
        self.declare(Sintomas(mudanca_comportamental=verifica_conjunto(
            [
                autoestima_excessiva,
                reducao_sono,
                aumento_fala,
                mudanca_modo_pensar,
                distrabilidade,
                agitacao,
                envolvimento_atividade_risco
            ], 3)))

    """
    Verificação das regras 
    """

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=1)))
    def mania(self):
        self.declare(Sintomas(mania=1))
        self.halt()
        print("tem mania")

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=0), Sintomas(psicose=1)))
    def nao_mania(self):
        self.declare(Sintomas(mania=0))
        self.halt()
        print("não tem mania")

    @Rule(AND(Sintomas(mudanca_comportamental=0), Sintomas(fisiologico=0), Sintomas(psicose=W())))
    def nao_2_mania(self):
        self.declare(Sintomas(mania=0))
        self.halt()
        print("não tem mania")

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=0)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=1))
        self.halt()
        print("tem hipomania")

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=0), Sintomas(psicose=0)))
    def nao_hipomania(self):
        self.declare(Sintomas(hipomania=0))
        self.halt()
        print("não tem hipomania")

    @Rule(AND(Sintomas(mudanca_comportamental=0), Sintomas(fisiologico=W()), Sintomas(psicose=0)))
    def nao_2_hipomania(self):
        self.declare(Sintomas(hipomania=0))
        self.halt()
        print("não tem hipomania")

    @Rule(OR(Sintomas(prejuizo_social=1), Sintomas(prejuiso_profissional=1)))
    def prejuiso_acentuado(self):
        self.declare(Sintomas(prejuizo_acentuado=1))

    @Rule(OR(Sintomas(autoestima_inflada=1), Sintomas(grandiosidade=1)))
    def autoestima_excessiva(self):
        self.declare(Sintomas(autoestima_excessiva=1))

    @Rule(OR(Sintomas(loquaz=1), Sintomas(pressao_continuar_falando=1)))
    def aumento_fala(self):
        self.declare(Sintomas(aumento_fala=1))

    @Rule(OR(Sintomas(fuga_ideias=1), Sintomas(pensamento_acelerado=1)))
    def mudanca_modo_pensar(self):
        self.declare(Sintomas(mudanca_modo_pensar=1))

    @Rule(OR(Sintomas(aumento_atividade_objetivo=1), Sintomas(agitacao_psicomotora=1)))
    def agitacao(self):
        self.declare(Sintomas(agitacao=1))


if __name__ == "__main__":
    engine = Mania()
    engine.reset()
    engine.run()
