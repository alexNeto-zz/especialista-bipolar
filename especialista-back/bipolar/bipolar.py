import operator
from functools import reduce

from pyknow import *


class Sintomas(Fact):

    def somatorio(self, listaSintomas):
        return reduce(operator.add, map(lambda i: 1 if i is True else 0, listaSintomas))


class Bipolar(KnowledgeEngine):

    @Rule(AND(Sintomas(humor_anormal=True), Sintomas(fisiologico=True)))
    def mania(self):
        self.declare(Sintomas(mania=True))  # fazer isso com todos
        print("mania")

    @Rule(OR(Sintomas(prejuizo_social=True), Sintomas(prejuiso_profissional=True)))
    def prejuiso_acentuado(self):
        Sintomas(prejuizo_acentuado=True)
        print("prejuizo acentuado")

    @Rule(OR(Sintomas(prejuizo_si=True, prejuizo_outros=True)))
    def risco_potencial(self):
        Sintomas(risco_potencial=True)
        print("risco potencial")

    @Rule(OR(OR(Sintomas(prejuizo_acentuado=True), Sintomas(risco_potencial=True)), Sintomas(psicose=True)))
    def perturbacao_humor(self):
        Sintomas(perturbacao_humor=True)
        print("perturbacao_humor")

    @Rule(OR(Sintomas(autoestima_inflada=True), Sintomas(grandiosidade=True)))
    def autoestima_excessiva(self):
        Sintomas(autoestima_excessiva=True)
        print("autoestima_excessiva")

    @Rule(OR(Sintomas(loquaz=True), Sintomas(pressao_continuar_falando=True)))
    def aumento_fala(self):
        Sintomas(aumento_fala=True)

    @Rule(OR(Sintomas(fuga_ideias=True), Sintomas(pensamento_acelerado=True)))
    def mudanca_modo_pensar(self):
        Sintomas(mudanca_modo_pensar=True)
        print("mudanca_modo_pensar")

    @Rule(Sintomas(aumento_atividade_objetivo=True), Sintomas(agitacao_psicomotora=True))
    def agitacao(self):
        Sintomas(agitacao=True)
        print("Agitacao")

    @Rule(TEST())  # TODO
    def mudanca_comportamental(self):
        Sintomas(mudanca_comportamental=True)
        print("mudanca_comportamental")

    # SE somatorio(
    #    autoestima_excessiva
    #    reducao_sono
    #    aumento_fala
    #    mudanca_modo_pensar
    #    distrabilidade
    #    agitacao
    #    envolvimento_atividade_risco
    # ) >= 3
    # ENTÃO mudanca_comportamental = sim

    @Rule(AND(Sintomas(mania=True), Sintomas(psicose=True)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=True))

    @Rule(OR(Sintomas(humor_deprimido=True), Sintomas(irritavel=True)))
    def humor_deprimido(self):
        self.declare(Sintomas(humor_deprimido=True))

    @Rule(OR(Sintomas(perda_interesse=True), Sintomas(perda_prazer=True)))
    def perda_interesse(self):
        self.declare(Sintomas(perda_interesse=True))

    @Rule(OR(OR(Sintomas(perda_peso=True), Sintomas(ganho_peso=True)),
             OR(Sintomas(reducao_alimentacao=True), Sintomas(aumento_alimentacao=True))))
    def alteracao_alimentacao(self):
        self.declare(Sintomas(Sintomas(alteracao_alimentacao=True)))

    @Rule(OR(Sintomas(insonia=True), Sintomas(hipersonia=True)))
    def alteracao_sono(self):
        self.declare(Sintomas(alteracao_sono=True))

    @Rule(OR(Sintomas(agitacao=True), Sintomas(retardo_psicomotor=True)))
    def alteracao_comportamentao(self):
        self.declare(Sintomas(alteracao_comportamentao=True))

    @Rule(OR(Sintomas(fadiga=True), Sintomas(perda_energia=True)))
    def cansaco(self):
        self.declare(Sintomas(cansaco=True))

    @Rule(OR(Sintomas(inutilidade=True), Sintomas(culpa_excessiva=True), Sintomas(culpa_inapropriada=True)))
    def sentimento_depressivo(self):
        self.declare(Sintomas(sentimento_depressivo=True))

    @Rule(OR(Sintomas(capacidade_diminuida=True), Sintomas(indecisao=True)))
    def alteracao_pensamento(self):
        self.declare(Sintomas(alteracao_pensamento=True))

    @Rule(AND(OR(), ))  # TODO
    def sintomas_depressivos(self):
        self.declare(Sintomas(sintomas_depressivos=True))

    # SE humor_deprimido = sim
    # OU perda_interesse = sim
    # AND soma(
    #    humor_deprimido,
    #    perda_interesse,
    #    alteracao_alimentacao,
    #    alteracao_sono,
    #    alteracao_comportamentao,
    #    cansaco,
    #    sentimento_depressivo,
    #    alteracao_pensamento,
    #    pensamentos_morte
    # ) >= 5
    # ENTAO sintomas_depressivos = sim

    @Rule(OR(OR(Sintomas(sofrimento_clinico=True), Sintomas(prejuiso_social=True)),
             OR(Sintomas(prejuiso_profissional=True), Sintomas(prejuiso_area_importancia=True))))
    def transtorno(self):
        self.declare(Sintomas(transtorno=True))

    @Rule(AND(Sintomas(sintomas_depressivos=True), Sintomas(fisiologico=True)))
    def depressao(self):
        self.declare(Sintomas(depressao=True))

    @Rule(AND(Sintomas(mania=True), Sintomas(depressao=True)))
    def bipolar_i(self):
        self.declare(Sintomas(bipolar_i=True))

    @Rule(AND(Sintomas(hipomania=True), Sintomas(depressao=True)))
    def bipolar_ii(self):
        self.declare(Sintomas(bipolar_ii=True))

    @Rule(AND(OR(Sintomas(pensamentos_morte=True), Sintomas(psicose=True), Sintomas(transtorno=True)),
              Sintomas(mania=False), Sintomas(hipomania=False), Sintomas(depressao=False)))
    def outro_transtorno(self):
        self.declare(Sintomas(outro_transtorno=True))


if __name__ == "__main__":
    print("maaaaaain")
