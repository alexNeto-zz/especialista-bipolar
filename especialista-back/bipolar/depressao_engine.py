from pyknow import AND, OR, NOT, Rule, KnowledgeEngine, W, MATCH

from bipolar.bipolar_engine import Sintomas
from bipolar.services import ask, verifica_conjunto


class Depressao(KnowledgeEngine):
    """
    Coleta dos dados
    """

    @Rule(NOT(Sintomas(pensamentos_morte=W())))
    def ask_pensamentos_morte(self):
        self.declare(Sintomas(pensamentos_morte=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(alteracao_pensamento=W())))
    def ask_alteracao_pensamento(self):
        self.declare(Sintomas(alteracao_pensamento=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(sentimento_depressivo=W())))
    def ask_sentimento_depressivo(self):
        self.declare(Sintomas(sentimento_depressivo=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(cansaco=W())))
    def ask_cansaco(self):
        self.declare(Sintomas(cansaco=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(alteracao_comportamentao=W())))
    def ask_alteracao_comportamentao(self):
        self.declare(Sintomas(alteracao_comportamentao=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(alteracao_sono=W())))
    def ask_alteracao_sono(self):
        self.declare(Sintomas(alteracao_sono=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(alteracao_alimentacao=W())))
    def ask_alteracao_alimentacao(self):
        self.declare(Sintomas(alteracao_alimentacao=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(perda_interesse=W())))
    def ask_perda_interesse(self):
        self.declare(Sintomas(perda_interesse=ask("prejuiso_area_importancia? ")))

    @Rule(NOT(Sintomas(humor_deprimido=W())))
    def ask_humor_deprimido(self):
        self.declare(Sintomas(humor_deprimido=ask("prejuiso_area_importancia? ")))

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

    @Rule(AND(
        OR(Sintomas(humor_deprimido=1), Sintomas(perda_interesse=1)),
        Sintomas(verifica_sintomas_depressivos=1)
    ))
    def sintomas_depressivos(self):
        self.declare(Sintomas(sintomas_depressivos=1))


if __name__ == "__main__":
    engine = Depressao()
    engine.reset()
    engine.run()
