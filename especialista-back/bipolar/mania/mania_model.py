from flask import jsonify

from bipolar.mania.mania_engine import Mania
from bipolar.sintomas import Sintomas


class ManiaModel:

    def __init__(self, parameters):
        self.parameters = parameters

    def resolve(self):
        mania_engine = Mania()
        mania_engine.reset()
        mania_engine.declare(self.__get_sintomas())
        mania_engine.run()
        result = jsonify(mania_engine.result)
        return result

    def __get_sintomas(self):
        return Sintomas(
            fisiologico=self.__get_as_int_or_none('fisiologico'),
            prejuizo_social=self.__get_as_int_or_none('prejuizo_social'),
            prejuiso_profissional=self.__get_as_int_or_none('prejuiso_profissional'),
            psicose=self.__get_as_int_or_none('psicose'),
            autoestima_inflada=self.__get_as_int_or_none('autoestima_inflada'),
            grandiosidade=self.__get_as_int_or_none('grandiosidade'),
            loquaz=self.__get_as_int_or_none('loquaz'),
            pressao_continuar_falando=self.__get_as_int_or_none('pressao_continuar_falando'),
            fuga_ideias=self.__get_as_int_or_none('fuga_ideias'),
            pensamento_acelerado=self.__get_as_int_or_none('pensamento_acelerado'),
            aumento_atividade_objetivo=self.__get_as_int_or_none('aumento_atividade_objetivo'),
            agitacao_psicomotora=self.__get_as_int_or_none('agitacao_psicomotora'),
            reducao_sono=self.__get_as_int_or_none('reducao_sono'),
            distrabilidade=self.__get_as_int_or_none('distrabilidade'),
            envolvimento_atividade_risco=self.__get_as_int_or_none('envolvimento_atividade_risco')
        )

    def __get_as_int_or_none(self, param):
        value = self.parameters.get(param)
        return int(value) if value != 'undefined' else None
