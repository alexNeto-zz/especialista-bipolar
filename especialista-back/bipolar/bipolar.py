import operator

from pyknow import *


class Sintomas(Fact):

    def somatorio(self, listaSintomas):
        return reduce(operator.add, map(lambda i: 1 if i == True else 0, listaSintomas))


class Bipolar(KnowledgeEngine):

    @Rule(AND(Sintomas(humor_anormal=True), Sintomas(fisiologico=True)))
    def mania(self):
        self.declare(Sintomas(mania=True)) # fazer isso com todos
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

    @Rule(TEST()) # TODO
    def mudanca_comportamental(self):
        Sintomas(mudanca_comportamental=True)
        print("mudanca_comportamental")

    #SE somatorio(
    #    autoestima_excessiva
    #    reducao_sono
    #    aumento_fala
    #    mudanca_modo_pensar
    #    distrabilidade
    #    agitacao
    #    envolvimento_atividade_risco
    #) >= 3
    #ENTÃO mudanca_comportamental = sim

    @Rule(AND(Sintomas(mania=True), Sintomas(psicose=True)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=True))

    @Rule(OR(Sintomas(humor_deprimido=True), Sintomas(irri)))
    def humor_deprimido(self):
        self.declare(Sintomas(humor_deprimido=True))

    REGRA
    SE
    humor_deprimido = sim
    OU
    irritavel = sim
    ENTAO
    humor_deprimido = sim

    REGRA
    SE
    perda_interesse = sim
    OU
    perda_prazer = sim
    ENTAO
    perda_interesse = sim

    REGRA
    SE
    perda_peso = sim
    OU
    ganho_peso = sim
    OU
    reducao_alimentacao = sim
    OU
    aumento_alimentacao = sim
    ENTAO
    alteracao_alimentacao = sim

    REGRA
    SE
    insonia = sim
    OU
    hipersonia = sim
    ENTAO
    alteracao_sono = sim

    REGRA
    SE
    agitacao = sim
    OU
    retardo_psicomotor = sim
    ENTAO
    alteracao_comportamentao = sim

    REGRA
    SE
    fadiga = sim
    OU
    perda_energia = sim
    ENTAO
    cansaco = sim

    REGRA
    SE
    inutilidade = sim
    OU
    culpa_excessiva = sim
    OU
    culpa_inapropriada = sim
    ENTAO
    sentimento_depressivo = sim

    REGRA
    SE
    capacidade_diminuida = sim
    OU
    indecisao = sim
    ENTAO
    alteracao_pensamento = sim

    REGRA
    SE
    pensamentos_morte = sim
    ENTAO
    pensamentos_morte = sim

    REGRA
    SE
    humor_deprimido = sim
    OU
    perda_interesse = sim
    AND
    soma(
        humor_deprimido,
        perda_interesse,
        alteracao_alimentacao,
        alteracao_sono,
        alteracao_comportamentao,
        cansaco,
        sentimento_depressivo,
        alteracao_pensamento,
        pensamentos_morte
    )
    ENTAO
    sintomas_depressivos = sim

    REGRA
    SE
    sofrimento_clinico = sim
    OU
    prejuiso_social = sim
    OU
    prejuiso_profissional = sim
    OU
    prejuiso_area_importancia = sim
    ENTAO
    transtorno = sim

    REGRA

    REGRA
    SE
    sintomas_depressivos = sim
    E
    fisiologico = sim
    ENTAO
    depressao = sim

    REGRA
    SE
    mania = sim
    E
    depressao = sim
    ENTAO
    bipolar_i = sim

    REGRA
    SE
    hipomania = sim
    E
    depressao = sim
    ENTAO
    bipolar_ii = sim

    REGRA
    SE
    psicose = sim
    E
    mania = nao
    E
    hipomania = nao
    E
    depressao = nao
    ENTAO
    outro_transtorno = sim


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])
