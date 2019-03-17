import operator
from functools import reduce

from pyknow import *


def somatorio(lista_sintomas):
    return reduce(operator.add, lista_sintomas)


class Sintomas(Fact):
    pass


class Bipolar(KnowledgeEngine):

    @Rule(AND(Sintomas(humor_anormal=1), Sintomas(fisiologico=1)))
    def mania(self):
        self.declare(Sintomas(mania=1))
        print("mania")

    @Rule(OR(Sintomas(prejuizo_social=1), Sintomas(prejuiso_profissional=1)))
    def prejuiso_acentuado(self):
        self.declare(Sintomas(prejuizo_acentuado=1))
        print("prejuizo acentuado")

    @Rule(OR(Sintomas(prejuizo_si=1, prejuizo_outros=1)))
    def risco_potencial(self):
        self.declare(Sintomas(risco_potencial=1))
        print("risco potencial")

    @Rule(OR(OR(Sintomas(prejuizo_acentuado=1), Sintomas(risco_potencial=1)), Sintomas(psicose=1)))
    def perturbacao_humor(self):
        self.declare(Sintomas(perturbacao_humor=1))
        print("perturbacao_humor")

    @Rule(OR(Sintomas(autoestima_inflada=1), Sintomas(grandiosidade=1)))
    def autoestima_excessiva(self):
        Sintomas(autoestima_excessiva=1)
        print("autoestima_excessiva")

    @Rule(OR(Sintomas(loquaz=1), Sintomas(pressao_continuar_falando=1)))
    def aumento_fala(self):
        Sintomas(aumento_fala=1)

    @Rule(OR(Sintomas(fuga_ideias=1), Sintomas(pensamento_acelerado=1)))
    def mudanca_modo_pensar(self):
        Sintomas(mudanca_modo_pensar=1)
        print("mudanca_modo_pensar")

    @Rule(Sintomas(aumento_atividade_objetivo=1), Sintomas(agitacao_psicomotora=1))
    def agitacao(self):
        Sintomas(agitacao=1)
        print("Agitacao")

    @Rule(TEST(somatorio([
        MATCH.autoestima_excessiva,
        MATCH.reducao_sono,
        MATCH.aumento_fala,
        MATCH.mudanca_modo_pensar,
        MATCH.distrabilidade,
        MATCH.agitacao,
        MATCH.envolvimento_atividade_risco
    ]) >= 3))  # TODO
    def mudanca_comportamental(self):
        Sintomas(mudanca_comportamental=1)
        print("mudanca_comportamental")

    @Rule(AND(Sintomas(mania=1), Sintomas(psicose=1)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=1))

    @Rule(OR(Sintomas(humor_deprimido=1), Sintomas(irritavel=1)))
    def humor_deprimido(self):
        self.declare(Sintomas(humor_deprimido=1))

    @Rule(OR(Sintomas(perda_interesse=1), Sintomas(perda_prazer=1)))
    def perda_interesse(self):
        self.declare(Sintomas(perda_interesse=1))

    @Rule(OR(OR(Sintomas(perda_peso=1), Sintomas(ganho_peso=1)),
             OR(Sintomas(reducao_alimentacao=1), Sintomas(aumento_alimentacao=1))))
    def alteracao_alimentacao(self):
        self.declare(Sintomas(Sintomas(alteracao_alimentacao=1)))

    @Rule(OR(Sintomas(insonia=1), Sintomas(hipersonia=1)))
    def alteracao_sono(self):
        self.declare(Sintomas(alteracao_sono=1))

    @Rule(OR(Sintomas(agitacao=1), Sintomas(retardo_psicomotor=1)))
    def alteracao_comportamentao(self):
        self.declare(Sintomas(alteracao_comportamentao=1))

    @Rule(OR(Sintomas(fadiga=1), Sintomas(perda_energia=1)))
    def cansaco(self):
        self.declare(Sintomas(cansaco=1))

    @Rule(OR(Sintomas(inutilidade=1), Sintomas(culpa_excessiva=1), Sintomas(culpa_inapropriada=1)))
    def sentimento_depressivo(self):
        self.declare(Sintomas(sentimento_depressivo=1))

    @Rule(OR(Sintomas(capacidade_diminuida=1), Sintomas(indecisao=1)))
    def alteracao_pensamento(self):
        self.declare(Sintomas(alteracao_pensamento=1))

    @Rule(AND(OR(Sintomas(humor_deprimido=1), Sintomas(perda_interesse=1)), TEST(somatorio([
        MATCH.humor_deprimido,
        MATCH.perda_interesse,
        MATCH.alteracao_alimentacao,
        MATCH.alteracao_sono,
        MATCH.alteracao_comportamentao,
        MATCH.cansaco,
        MATCH.sentimento_depressivo,
        MATCH.alteracao_pensamento,
        MATCH.pensamentos_morte
    ]) >= 5)))
    def sintomas_depressivos(self):
        self.declare(Sintomas(sintomas_depressivos=1))

    @Rule(OR(OR(Sintomas(sofrimento_clinico=1), Sintomas(prejuiso_social=1)),
             OR(Sintomas(prejuiso_profissional=1), Sintomas(prejuiso_area_importancia=1))))
    def transtorno(self):
        self.declare(Sintomas(transtorno=1))

    @Rule(AND(Sintomas(sintomas_depressivos=1), Sintomas(fisiologico=1)))
    def depressao(self):
        self.declare(Sintomas(depressao=1))

    @Rule(AND(Sintomas(mania=1), Sintomas(depressao=1)))
    def bipolar_i(self):
        self.declare(Sintomas(bipolar_i=1))

    @Rule(AND(Sintomas(hipomania=1), Sintomas(depressao=1)))
    def bipolar_ii(self):
        self.declare(Sintomas(bipolar_ii=1))

    @Rule(AND(OR(Sintomas(pensamentos_morte=1), Sintomas(psicose=1), Sintomas(transtorno=1)),
              Sintomas(mania=0), Sintomas(hipomania=0), Sintomas(depressao=0)))
    def outro_transtorno(self):
        self.declare(Sintomas(outro_transtorno=1))


if __name__ == "__main__":
    print("maaaaaain")
