from pyknow import AND, OR, NOT, Rule, KnowledgeEngine, W, MATCH

from bipolar.services import ask, verifica_conjunto
from bipolar.sintomas import Sintomas


class Mania(KnowledgeEngine):
    """
    Coleta dos dados
    """

    result = {
        'variable': None,
        'isFinalAnswer': False,
        'answer': None,
    }
    is_rest = True

    def ask(self, variable):
        if not self.is_rest:
            return ask(variable)
        else:
            self.result['variable'] = variable
            self.result['isFinalAnswer'] = False
            self.result['answer'] = None
            self.halt()

    def send(self, message):
        if not self.is_rest:
            print(message)
        else:
            self.result['variable'] = None
            self.result['isFinalAnswer'] = True
            self.result['answer'] = message
        self.halt()

    @Rule(Sintomas(fisiologico=None))
    def ask_data_fisiologico(self):
        self.declare(Sintomas(fisiologico=self.ask("fisiologico")))

    @Rule(Sintomas(prejuizo_social=None))
    def ask_data_prejuizo_social(self):
        self.declare(Sintomas(prejuizo_social=self.ask("prejuizo_social")))

    @Rule(Sintomas(prejuiso_profissional=None))
    def ask_data_prejuiso_profissional(self):
        self.declare(Sintomas(prejuiso_profissional=self.ask("prejuiso_profissional")))

    @Rule(Sintomas(psicose=None))
    def ask_data_psicose(self):
        self.declare(Sintomas(psicose=self.ask("psicose")))

    @Rule(Sintomas(autoestima_inflada=None))
    def ask_data_autoestima_inflada(self):
        self.declare(Sintomas(autoestima_inflada=self.ask("autoestima_inflada")))

    @Rule(Sintomas(grafndiosidade=None))
    def ask_data_grandiosidade(self):
        self.declare(Sintomas(grandiosidade=self.ask("grandiosidade")))

    @Rule(Sintomas(loquaz=None))
    def ask_data_loquaz(self):
        self.declare(Sintomas(loquaz=self.ask("loquaz")))

    @Rule(Sintomas(pressao_continuar_falando=None))
    def ask_data_pressao_continuar_falando(self):
        self.declare(Sintomas(pressao_continuar_falando=self.ask("pressao_continuar_falando")))

    @Rule(Sintomas(fuga_ideias=None))
    def ask_data_fuga_ideias(self):
        self.declare(Sintomas(fuga_ideias=self.ask("fuga_ideias")))

    @Rule(Sintomas(pensamento_acelerado=None))
    def ask_data_pensamento_acelerado(self):
        self.declare(Sintomas(pensamento_acelerado=self.ask("pensamento_acelerado")))

    @Rule(Sintomas(aumento_atividade_objetivo=None))
    def ask_data_aumento_atividade_objetivo(self):
        self.declare(Sintomas(aumento_atividade_objetivo=self.ask("aumento_atividade_objetivo")))

    @Rule(Sintomas(agitacao_psicomotora=None))
    def ask_data_agitacao_psicomotora(self):
        self.declare(Sintomas(agitacao_psicomotora=self.ask("agitacao_psicomotora")))

    @Rule(Sintomas(reducao_sono=None))
    def ask_data_reducao_sono(self):
        self.declare(Sintomas(reducao_sono=self.ask("reducao_sono")))

    @Rule(Sintomas(distrabilidade=None))
    def ask_data_distrabilidade(self):
        self.declare(Sintomas(distrabilidade=self.ask("distrabilidade")))

    @Rule(Sintomas(envolvimento_atividade_risco=None))
    def ask_data_envolvimento_atividade_risco(self):
        self.declare(Sintomas(envolvimento_atividade_risco=self.ask("envolvimento_atividade_risco")))

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
            ]
            , 3)))

    """
    Verificação das regras 
    """

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=1)))
    def mania(self):
        self.declare(Sintomas(mania=1))
        self.send("mania:1")

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=0)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=1))
        self.send("hipomania:1")

    @Rule(Sintomas(fisiologico=0))
    def nao_fisiologico(self):
        self.declare(Sintomas(mania=0))
        self.declare(Sintomas(hipomania=0))
        self.send(":0")

    @Rule(Sintomas(mudanca_comportamental=0))
    def nao_mudanca_comportamental(self):
        self.declare(Sintomas(mania=0))
        self.declare(Sintomas(hipomania=0))
        self.send(":0")

    @Rule(OR(Sintomas(prejuizo_social=1), Sintomas(prejuiso_profissional=1)))
    def prejuiso_acentuado(self):
        self.declare(Sintomas(prejuizo_acentuado=1))

    @Rule(AND(Sintomas(prejuizo_social=0), Sintomas(prejuiso_profissional=0)))
    def nao_prejuiso_acentuado(self):
        self.declare(Sintomas(prejuizo_acentuado=0))

    @Rule(OR(Sintomas(autoestima_inflada=1), Sintomas(grandiosidade=1)))
    def autoestima_excessiva(self):
        self.declare(Sintomas(autoestima_excessiva=1))

    @Rule(AND(Sintomas(autoestima_inflada=0), Sintomas(grandiosidade=0)))
    def nao_autoestima_excessiva(self):
        self.declare(Sintomas(autoestima_excessiva=0))

    @Rule(OR(Sintomas(loquaz=1), Sintomas(pressao_continuar_falando=1)))
    def aumento_fala(self):
        self.declare(Sintomas(aumento_fala=1))

    @Rule(AND(Sintomas(loquaz=0), Sintomas(pressao_continuar_falando=0)))
    def nao_aumento_fala(self):
        self.declare(Sintomas(aumento_fala=0))

    @Rule(OR(Sintomas(fuga_ideias=1), Sintomas(pensamento_acelerado=1)))
    def mudanca_modo_pensar(self):
        self.declare(Sintomas(mudanca_modo_pensar=1))

    @Rule(AND(Sintomas(fuga_ideias=0), Sintomas(pensamento_acelerado=0)))
    def nao_mudanca_modo_pensar(self):
        self.declare(Sintomas(mudanca_modo_pensar=0))

    @Rule(OR(Sintomas(aumento_atividade_objetivo=1), Sintomas(agitacao_psicomotora=1)))
    def agitacao(self):
        self.declare(Sintomas(agitacao=1))

    @Rule(AND(Sintomas(aumento_atividade_objetivo=0), Sintomas(agitacao_psicomotora=0)))
    def nao_agitacao(self):
        self.declare(Sintomas(agitacao=0))


if __name__ == "__main__":
    engine = Mania()
    engine.is_rest = False
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=None,
        prejuizo_social=None,
        prejuiso_profissional=None,
        psicose=None,
        autoestima_inflada=None,
        grandiosidade=None,
        loquaz=None,
        pressao_continuar_falando=None,
        fuga_ideias=None,
        pensamento_acelerado=None,
        aumento_atividade_objetivo=None,
        agitacao_psicomotora=None,
        reducao_sono=None,
        distrabilidade=None,
        envolvimento_atividade_risco=None
    ))
    engine.run()
