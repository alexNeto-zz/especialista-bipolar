import operator
from functools import reduce

from pyknow import *


def somatorio(lista_sintomas):
    return reduce(operator.add, lista_sintomas)


def ask(question):
    return 1 if int(input(question + " (s/n)")) == 's' else 0


class Sintomas(Fact):
    pass


class Bipolar(KnowledgeEngine):
    """
    Coleta dos dados
    """

    @Rule(NOT(Sintomas(humor_anormal=W())))
    def ask_data_humor_anormal(self):
        value = ask("humor_anormal? ")
        print(value)
        self.declare(Sintomas(humor_anormal=value))

    @Rule(NOT(Sintomas(fisiologico=W())))
    def ask_data_fisiologico(self):
        value = ask("fisiologico? ")
        print(value)
        self.declare(Sintomas(fisiologico=value))

    @Rule(NOT(Sintomas(prejuizo_social=W())))
    def ask_data_prejuizo_social(self):
        value = ask("prejuizo_social? ")
        print(value)
        self.declare(Sintomas(prejuizo_social=value))

    @Rule(NOT(Sintomas(prejuiso_profissional=W())))
    def ask_data_prejuiso_profissional(self):
        value = ask("prejuiso_profissional? ")
        print(value)
        self.declare(Sintomas(prejuiso_profissional=value))

    @Rule(NOT(Sintomas(prejuizo_si=W())))
    def ask_data_prejuizo_si(self):
        value = ask("prejuizo_si? ")
        print(value)
        self.declare(Sintomas(prejuizo_si=value))

    @Rule(NOT(Sintomas(prejuizo_outros=W())))
    def ask_data_prejuizo_outros(self):
        value = ask("prejuizo_outros? ")
        print(value)
        self.declare(Sintomas(prejuizo_outros=value))

    @Rule(NOT(Sintomas(psicose=W())))
    def ask_data_psicose(self):
        value = ask("psicose? ")
        print(value)
        self.declare(Sintomas(psicose=value))

    @Rule(NOT(Sintomas(autoestima_inflada=W())))
    def ask_data_autoestima_inflada(self):
        value = ask("autoestima_inflada? ")
        print(value)
        self.declare(Sintomas(autoestima_inflada=value))

    @Rule(NOT(Sintomas(grandiosidade=W())))
    def ask_data_grandiosidade(self):
        value = ask("grandiosidade? ")
        print(value)
        self.declare(Sintomas(grandiosidade=value))

    @Rule(NOT(Sintomas(loquaz=W())))
    def ask_data_loquaz(self):
        value = ask("loquaz? ")
        print(value)
        self.declare(Sintomas(loquaz=value))

    @Rule(NOT(Sintomas(pressao_continuar_falando=W())))
    def ask_data_pressao_continuar_falando(self):
        value = ask("pressao_continuar_falando? ")
        print(value)
        self.declare(Sintomas(pressao_continuar_falando=value))

    @Rule(NOT(Sintomas(fuga_ideias=W())))
    def ask_data_fuga_ideias(self):
        value = ask("fuga_ideias? ")
        print(value)
        self.declare(Sintomas(fuga_ideias=value))

    @Rule(NOT(Sintomas(pensamento_acelerado=W())))
    def ask_data_pensamento_acelerado(self):
        value = ask("pensamento_acelerado? ")
        print(value)
        self.declare(Sintomas(pensamento_acelerado=value))

    @Rule(NOT(Sintomas(aumento_atividade_objetivo=W())))
    def ask_data_aumento_atividade_objetivo(self):
        value = ask("aumento_atividade_objetivo? ")
        print(value)
        self.declare(Sintomas(aumento_atividade_objetivo=value))

    @Rule(NOT(Sintomas(agitacao_psicomotora=W())))
    def ask_data_agitacao_psicomotora(self):
        value = ask("agitacao_psicomotora? ")
        print(value)
        self.declare(Sintomas(agitacao_psicomotora=value))

    @Rule(NOT(Sintomas(reducao_sono=W())))
    def ask_data_reducao_sono(self):
        value = ask("reducao_sono? ")
        print(value)
        self.declare(Sintomas(reducao_sono=value))

    @Rule(NOT(Sintomas(distrabilidade=W())))
    def ask_data_distrabilidade(self):
        value = ask("distrabilidade? ")
        print(value)
        self.declare(Sintomas(distrabilidade=value))

    @Rule(NOT(Sintomas(envolvimento_atividade_risco=W())))
    def ask_data_envolvimento_atividade_risco(self):
        value = ask("envolvimento_atividade_risco? ")
        print(value)
        self.declare(Sintomas(envolvimento_atividade_risco=value))

    @Rule(NOT(Sintomas(irritavel=W())))
    def ask_data_irritavel(self):
        value = ask("irritavel? ")
        print(value)
        self.declare(Sintomas(irritavel=value))

    @Rule(NOT(Sintomas(perda_prazer=W())))
    def ask_data_perda_prazer(self):
        value = ask("perda_prazer? ")
        print(value)
        self.declare(Sintomas(perda_prazer=value))

    @Rule(NOT(Sintomas(perda_peso=W())))
    def ask_data_perda_peso(self):
        value = ask("perda_peso? ")
        print(value)
        self.declare(Sintomas(perda_peso=value))

    @Rule(NOT(Sintomas(ganho_peso=W())))
    def ask_data_ganho_peso(self):
        value = ask("ganho_peso? ")
        print(value)
        self.declare(Sintomas(ganho_peso=value))

    @Rule(NOT(Sintomas(reducao_alimentacao=W())))
    def ask_data_reducao_alimentacao(self):
        value = ask("reducao_alimentacao? ")
        print(value)
        self.declare(Sintomas(reducao_alimentacao=value))

    @Rule(NOT(Sintomas(aumento_alimentacao=W())))
    def ask_data_aumento_alimentacao(self):
        value = ask("aumento_alimentacao? ")
        print(value)
        self.declare(Sintomas(aumento_alimentacao=value))

    @Rule(NOT(Sintomas(insonia=W())))
    def ask_data_insonia(self):
        value = ask("insonia? ")
        print(value)
        self.declare(Sintomas(insonia=value))

    @Rule(NOT(Sintomas(hipersonia=W())))
    def ask_data_hipersonia(self):
        value = ask("hipersonia? ")
        print(value)
        self.declare(Sintomas(hipersonia=value))

    @Rule(NOT(Sintomas(retardo_psicomotor=W())))
    def ask_data_retardo_psicomotor(self):
        value = ask("retardo_psicomotor? ")
        print(value)
        self.declare(Sintomas(retardo_psicomotor=value))

    @Rule(NOT(Sintomas(fadiga=W())))
    def ask_data_fadiga(self):
        value = ask("fadiga? ")
        print(value)
        self.declare(Sintomas(fadiga=value))

    @Rule(NOT(Sintomas(perda_energia=W())))
    def ask_data_perda_energia(self):
        value = ask("perda_energia? ")
        print(value)
        self.declare(Sintomas(perda_energia=value))

    @Rule(NOT(Sintomas(inutilidade=W())))
    def ask_data_inutilidade(self):
        value = ask("inutilidade? ")
        print(value)
        self.declare(Sintomas(inutilidade=value))

    @Rule(NOT(Sintomas(culpa_excessiva=W())))
    def ask_data_culpa_excessiva(self):
        value = ask("culpa_excessiva? ")
        print(value)
        self.declare(Sintomas(culpa_excessiva=value))

    @Rule(NOT(Sintomas(culpa_inapropriada=W())))
    def ask_data_culpa_inapropriada(self):
        value = ask("culpa_inapropriada? ")
        print(value)
        self.declare(Sintomas(culpa_inapropriada=value))

    @Rule(NOT(Sintomas(capacidade_diminuida=W())))
    def ask_data_capacidade_diminuida(self):
        value = ask("capacidade_diminuida? ")
        print(value)
        self.declare(Sintomas(capacidade_diminuida=value))

    @Rule(NOT(Sintomas(indecisao=W())))
    def ask_data_indecisao(self):
        value = ask("indecisao? ")
        print(value)
        self.declare(Sintomas(indecisao=value))

    @Rule(NOT(Sintomas(pensamentos_morte=W())))
    def ask_data_pensamentos_morte(self):
        value = ask("pensamentos_morte? ")
        print(value)
        self.declare(Sintomas(pensamentos_morte=value))

    @Rule(NOT(Sintomas(sofrimento_clinico=W())))
    def ask_data_sofrimento_clinico(self):
        value = ask("sofrimento_clinico? ")
        print(value)
        self.declare(Sintomas(sofrimento_clinico=value))

    @Rule(NOT(Sintomas(prejuiso_social=W())))
    def ask_data_prejuiso_social(self):
        value = ask("prejuiso_social? ")
        print(value)
        self.declare(Sintomas(prejuiso_social=value))

    @Rule(NOT(Sintomas(prejuiso_area_importancia=W())))
    def ask_data_prejuiso_area_importancia(self):
        value = ask("prejuiso_area_importancia? ")
        print(value)
        self.declare(Sintomas(prejuiso_area_importancia=value))


"""
Verificação das regras 
"""


@Rule(AND(Sintomas(humor_anormal=1), Sintomas(fisiologico=1)))
def mania(self):
    self.declare(Sintomas(mania=1))
    print("mania")


@Rule(OR(Sintomas(prejuizo_social=1), Sintomas(prejuiso_profissional=1)))
def prejuiso_acentuado(self):
    self.declare(Sintomas(prejuizo_acentuado=1))
    print("prejuizo acentuado")


@Rule(OR(Sintomas(prejuizo_si=1), Sintomas(prejuizo_outros=1)))
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
