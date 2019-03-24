from pyknow import AND, OR, NOT, Rule, Fact, KnowledgeEngine, W, MATCH

from bipolar.services import ask, verifica_conjunto


class Sintomas(Fact):
    pass


class Bipolar(KnowledgeEngine):
    """
    Coleta dos dados
    """

    @Rule(NOT(Sintomas(verifica_humor_deprimido=W())))
    def ask_verifica_humor_deprimido(self):
        self.declare(Sintomas(verifica_humor_deprimido=ask("verifica_humor_deprimido? ")))

    @Rule(NOT(Sintomas(fisiologico=W())))
    def ask_data_fisiologico(self):
        self.declare(Sintomas(fisiologico=ask("fisiologico? ")))

    @Rule(NOT(Sintomas(prejuizo_social=W())))
    def ask_data_prejuizo_social(self):
        self.declare(Sintomas(prejuizo_social=ask("prejuizo_social? ")))

    @Rule(NOT(Sintomas(prejuiso_profissional=W())))
    def ask_data_prejuiso_profissional(self):
        self.declare(Sintomas(prejuiso_profissional=ask("prejuiso_profissional? ")))

    @Rule(NOT(Sintomas(prejuizo_si=W())))
    def ask_data_prejuizo_si(self):
        self.declare(Sintomas(prejuizo_si=ask("prejuizo_si? ")))

    @Rule(NOT(Sintomas(prejuizo_outros=W())))
    def ask_data_prejuizo_outros(self):
        self.declare(Sintomas(prejuizo_outros=ask("prejuizo_outros? ")))

    @Rule(NOT(Sintomas(psicose=W())))
    def ask_data_psicose(self):
        self.declare(Sintomas(psicose=ask("psicose? ")))

    @Rule(NOT(Sintomas(autoestima_inflada=W())))
    def ask_data_autoestima_inflada(self):
        self.declare(Sintomas(autoestima_inflada=ask("autoestima_inflada? ")))

    @Rule(NOT(Sintomas(grandiosidade=W())))
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

    @Rule(NOT(Sintomas(irritavel=W())))
    def ask_data_irritavel(self):
        self.declare(Sintomas(irritavel=ask("irritavel? ")))

    @Rule(NOT(Sintomas(verifica_perda_interesse=W())))
    def aks_perda_interesse(self):
        self.declare(Sintomas(verifica_perda_interesse=ask("perda_interesse? ")))

    @Rule(NOT(Sintomas(perda_prazer=W())))
    def ask_data_perda_prazer(self):
        self.declare(Sintomas(perda_prazer=ask("perda_prazer? ")))

    @Rule(NOT(Sintomas(perda_peso=W())))
    def ask_data_perda_peso(self):
        self.declare(Sintomas(perda_peso=ask("perda_peso? ")))

    @Rule(NOT(Sintomas(ganho_peso=W())))
    def ask_data_ganho_peso(self):
        self.declare(Sintomas(ganho_peso=ask("ganho_peso? ")))

    @Rule(NOT(Sintomas(reducao_alimentacao=W())))
    def ask_data_reducao_alimentacao(self):
        self.declare(Sintomas(reducao_alimentacao=ask("reducao_alimentacao? ")))

    @Rule(NOT(Sintomas(aumento_alimentacao=W())))
    def ask_data_aumento_alimentacao(self):
        self.declare(Sintomas(aumento_alimentacao=ask("aumento_alimentacao? ")))

    @Rule(NOT(Sintomas(insonia=W())))
    def ask_data_insonia(self):
        self.declare(Sintomas(insonia=ask("insonia? ")))

    @Rule(NOT(Sintomas(hipersonia=W())))
    def ask_data_hipersonia(self):
        self.declare(Sintomas(hipersonia=ask("hipersonia? ")))

    @Rule(NOT(Sintomas(retardo_psicomotor=W())))
    def ask_data_retardo_psicomotor(self):
        self.declare(Sintomas(retardo_psicomotor=ask("retardo_psicomotor? ")))

    @Rule(NOT(Sintomas(fadiga=W())))
    def ask_data_fadiga(self):
        self.declare(Sintomas(fadiga=ask("fadiga? ")))

    @Rule(NOT(Sintomas(perda_energia=W())))
    def ask_data_perda_energia(self):
        self.declare(Sintomas(perda_energia=ask("perda_energia? ")))

    @Rule(NOT(Sintomas(inutilidade=W())))
    def ask_data_inutilidade(self):
        self.declare(Sintomas(inutilidade=ask("inutilidade? ")))

    @Rule(NOT(Sintomas(culpa_excessiva=W())))
    def ask_data_culpa_excessiva(self):
        self.declare(Sintomas(culpa_excessiva=ask("culpa_excessiva? ")))

    @Rule(NOT(Sintomas(culpa_inapropriada=W())))
    def ask_data_culpa_inapropriada(self):
        self.declare(Sintomas(culpa_inapropriada=ask("culpa_inapropriada? ")))

    @Rule(NOT(Sintomas(capacidade_diminuida=W())))
    def ask_data_capacidade_diminuida(self):
        self.declare(Sintomas(capacidade_diminuida=ask("capacidade_diminuida? ")))

    @Rule(NOT(Sintomas(indecisao=W())))
    def ask_data_indecisao(self):
        self.declare(Sintomas(indecisao=ask("indecisao? ")))

    @Rule(NOT(Sintomas(pensamentos_morte=W())))
    def ask_data_pensamentos_morte(self):
        self.declare(Sintomas(pensamentos_morte=ask("pensamentos_morte? ")))

    @Rule(NOT(Sintomas(sofrimento_clinico=W())))
    def ask_data_sofrimento_clinico(self):
        self.declare(Sintomas(sofrimento_clinico=ask("sofrimento_clinico? ")))

    @Rule(NOT(Sintomas(prejuiso_social=W())))
    def ask_data_prejuiso_social(self):
        self.declare(Sintomas(prejuiso_social=ask("prejuiso_social? ")))

    @Rule(NOT(Sintomas(prejuiso_area_importancia=W())))
    def ask_data_prejuiso_area_importancia(self):
        self.declare(Sintomas(prejuiso_area_importancia=ask("prejuiso_area_importancia? ")))

    @Rule(AND(
        NOT(Sintomas(verifica_mudanca_comportamental=W())),
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
        self.declare(Sintomas(verifica_mudanca_comportamental=verifica_conjunto(
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

    @Rule(AND(
        NOT(Sintomas(verifica_sintomas_depressivos=W())),
        AND(
            OR(Sintomas(humor_deprimido=0), Sintomas(humor_deprimido=1)),
            Sintomas(humor_deprimido=MATCH.humor_deprimido)
        ),
        AND(
            OR(Sintomas(perda_interesse=0), Sintomas(perda_interesse=1)),
            Sintomas(perda_interesse=MATCH.perda_interesse)
        ),
        AND(
            OR(Sintomas(alteracao_alimentacao=0), Sintomas(alteracao_alimentacao=1)),
            Sintomas(alteracao_alimentacao=MATCH.alteracao_alimentacao)
        ),
        AND(
            OR(Sintomas(alteracao_sono=0), Sintomas(alteracao_sono=1)),
            Sintomas(alteracao_sono=MATCH.alteracao_sono)
        ),
        AND(
            OR(Sintomas(alteracao_comportamentao=0), Sintomas(alteracao_comportamentao=1)),
            Sintomas(alteracao_comportamentao=MATCH.alteracao_comportamentao)
        ),
        AND(
            OR(Sintomas(cansaco=0), Sintomas(cansaco=1)),
            Sintomas(cansaco=MATCH.cansaco)
        ),
        AND(
            OR(Sintomas(sentimento_depressivo=0), Sintomas(sentimento_depressivo=1)),
            Sintomas(sentimento_depressivo=MATCH.sentimento_depressivo)
        ),
        AND(
            OR(Sintomas(alteracao_pensamento=0), Sintomas(alteracao_pensamento=1)),
            Sintomas(alteracao_pensamento=MATCH.alteracao_pensamento)
        ),
        AND(
            OR(Sintomas(pensamentos_morte=0), Sintomas(pensamentos_morte=1)),
            Sintomas(pensamentos_morte=MATCH.pensamentos_morte)
        )
    ))
    def define_sintomas_depressivos(self,
                                    humor_deprimido,
                                    perda_interesse,
                                    alteracao_alimentacao,
                                    alteracao_sono,
                                    alteracao_comportamentao,
                                    cansaco,
                                    sentimento_depressivo,
                                    alteracao_pensamento,
                                    pensamentos_morte
                                    ):
        self.declare(Sintomas(verifica_sintomas_depressivos=verifica_conjunto(
            [
                humor_deprimido,
                perda_interesse,
                alteracao_alimentacao,
                alteracao_sono,
                alteracao_comportamentao,
                cansaco,
                sentimento_depressivo,
                alteracao_pensamento,
                pensamentos_morte
            ]
            , 5)))

    """
    Verificação das regras 
    """

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=1)))
    def mania(self):
        self.declare(Sintomas(mania=1))

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=0), Sintomas(psicose=1)))
    def nao_mania(self):
        self.declare(Sintomas(mania=0))

    @Rule(AND(Sintomas(mudanca_comportamental=0), Sintomas(fisiologico=0), Sintomas(psicose=W())))
    def nao_2_mania(self):
        self.declare(Sintomas(mania=0))

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=1), Sintomas(psicose=0)))
    def hipomania(self):
        self.declare(Sintomas(hipomania=1))

    @Rule(AND(Sintomas(mudanca_comportamental=1), Sintomas(fisiologico=0), Sintomas(psicose=0)))
    def nao_hipomania(self):
        self.declare(Sintomas(hipomania=0))

    @Rule(AND(Sintomas(mudanca_comportamental=0), Sintomas(fisiologico=W()), Sintomas(psicose=0)))
    def nao_2_hipomania(self):
        self.declare(Sintomas(hipomania=0))

    @Rule(OR(Sintomas(prejuizo_social=1), Sintomas(prejuiso_profissional=1)))
    def prejuiso_acentuado(self):
        self.declare(Sintomas(prejuizo_acentuado=1))

    @Rule(OR(Sintomas(prejuizo_si=1), Sintomas(prejuizo_outros=1)))
    def risco_potencial(self):
        self.declare(Sintomas(risco_potencial=1))

    @Rule(NOT(OR(Sintomas(prejuizo_si=1), Sintomas(prejuizo_outros=1))))
    def risco_potencial(self):
        self.declare(Sintomas(risco_potencial=0))

    @Rule(OR(OR(Sintomas(prejuizo_acentuado=1), Sintomas(risco_potencial=1)), Sintomas(psicose=1)))
    def perturbacao_humor(self):
        self.declare(Sintomas(perturbacao_humor=1))

    @Rule(NOT(OR(OR(Sintomas(prejuizo_acentuado=1), Sintomas(risco_potencial=1)), Sintomas(psicose=1))))
    def perturbacao_humor(self):
        self.declare(Sintomas(perturbacao_humor=0))

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

    @Rule(Sintomas(verifica_mudanca_comportamental=1))
    def mudanca_comportamental(self):
        self.declare(Sintomas(mudanca_comportamental=1))

    @Rule(OR(Sintomas(verifica_humor_deprimido=1), Sintomas(irritavel=1)))
    def humor_deprimido(self):
        print("humor_deprimido")
        self.declare(Sintomas(humor_deprimido=1))

    @Rule(OR(Sintomas(verifica_perda_interesse=1), Sintomas(perda_prazer=1)))
    def perda_interesse(self):
        print("perda_interesse")
        self.declare(Sintomas(perda_interesse=1))

    @Rule(OR(
        OR(Sintomas(perda_peso=1), Sintomas(ganho_peso=1)),
        OR(Sintomas(reducao_alimentacao=1), Sintomas(aumento_alimentacao=1))
    ))
    def alteracao_alimentacao(self):
        print("alteracao_alimentacao")
        self.declare(Sintomas(Sintomas(alteracao_alimentacao=1)))

    @Rule(OR(Sintomas(insonia=1), Sintomas(hipersonia=1)))
    def alteracao_sono(self):
        print("alteracao_sono")
        self.declare(Sintomas(alteracao_sono=1))

    @Rule(OR(Sintomas(agitacao=1), Sintomas(retardo_psicomotor=1)))
    def alteracao_comportamentao(self):
        print("alteracao_comportamentao")
        self.declare(Sintomas(alteracao_comportamentao=1))

    @Rule(OR(Sintomas(fadiga=1), Sintomas(perda_energia=1)))
    def cansaco(self):
        print("cansaco")
        self.declare(Sintomas(cansaco=1))

    @Rule(OR(Sintomas(inutilidade=1), Sintomas(culpa_excessiva=1), Sintomas(culpa_inapropriada=1)))
    def sentimento_depressivo(self):
        print("sentimento_depressivo")
        self.declare(Sintomas(sentimento_depressivo=1))

    @Rule(OR(Sintomas(capacidade_diminuida=1), Sintomas(indecisao=1)))
    def alteracao_pensamento(self):
        print("alteracao_pensamento")
        self.declare(Sintomas(alteracao_pensamento=1))

    @Rule(AND(
        OR(Sintomas(humor_deprimido=1), Sintomas(perda_interesse=1)),
        Sintomas(verifica_sintomas_depressivos=1)
    ))
    def sintomas_depressivos(self):
        print("sintomas_depressivos")
        self.declare(Sintomas(sintomas_depressivos=1))

    @Rule(OR(
        OR(Sintomas(sofrimento_clinico=1), Sintomas(prejuiso_social=1)),
        OR(Sintomas(prejuiso_profissional=1), Sintomas(prejuiso_area_importancia=1))
    ))
    def transtorno(self):
        print("transtorno")
        self.declare(Sintomas(transtorno=1))

    @Rule(AND(Sintomas(sintomas_depressivos=1), Sintomas(fisiologico=1)))
    def depressao(self):
        print("depressao")
        self.declare(Sintomas(depressao=1))

    @Rule(AND(Sintomas(mania=1), Sintomas(depressao=1)))
    def bipolar_i(self):
        print("bipolar_i")
        self.declare(Sintomas(bipolar_i=1))

    @Rule(AND(Sintomas(hipomania=1), Sintomas(depressao=1)))
    def bipolar_ii(self):
        print("bipolar_ii")
        self.declare(Sintomas(bipolar_ii=1))

    @Rule(AND(
        OR(Sintomas(pensamentos_morte=1),
           Sintomas(psicose=1),
           Sintomas(transtorno=1)),
        Sintomas(mania=0),
        Sintomas(hipomania=0),
        Sintomas(depressao=0)
    ))
    def outro_transtorno(self):
        print("outro_transtorno")
        self.declare(Sintomas(outro_transtorno=1))

    @Rule(Sintomas(bipolar_i=1))
    def tem_bipolar_i(self):
        print("bipolar tipo I")
        self.halt()

    @Rule(Sintomas(bipolar_ii=1))
    def tem_bipolar_ii(self):
        print("bipolar tipo II")
        self.halt()

    @Rule(OR(
        AND(Sintomas(mania=0), Sintomas(depressao=1)),
        AND(Sintomas(hipomania=0), Sintomas(depressao=1))
    ))
    def tem_depressao(self):
        print("tem depressão")
        self.halt()

    @Rule(Sintomas(outro_transtorno=1))
    def tem_outro_transtorno(self):
        print("possue outro transtorno")
        self.halt()

    @Rule(Sintomas(outro_transtorno=0))
    def nao_tem_outro_transtorno(self):
        print("Não possue outro transtorno")
        self.halt()


if __name__ == "__main__":
    engine = Bipolar()
    engine.reset()
    engine.run()
