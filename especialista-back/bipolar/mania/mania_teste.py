from bipolar.mania.mania_engine import Mania
from bipolar.sintomas import Sintomas


def testa_todos_falsos():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=0,
        prejuizo_social=0,
        prejuiso_profissional=0,
        psicose=0,
        autoestima_inflada=0,
        grandiosidade=0,
        loquaz=0,
        pressao_continuar_falando=0,
        fuga_ideias=0,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=0,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == ":0"


def testa_todos_verdadeiros():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=1,
        prejuiso_profissional=1,
        psicose=1,
        autoestima_inflada=1,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=1,
        fuga_ideias=1,
        pensamento_acelerado=1,
        aumento_atividade_objetivo=1,
        agitacao_psicomotora=1,
        reducao_sono=1,
        distrabilidade=1,
        envolvimento_atividade_risco=1
    ))
    engine.run()
    return engine.result['answer'] == "mania:1"


def testa_todos_verdadeiros_exceto_psicose():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=1,
        prejuiso_profissional=1,
        psicose=0,
        autoestima_inflada=1,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=1,
        fuga_ideias=1,
        pensamento_acelerado=1,
        aumento_atividade_objetivo=1,
        agitacao_psicomotora=1,
        reducao_sono=1,
        distrabilidade=1,
        envolvimento_atividade_risco=1
    ))
    engine.run()
    return engine.result['answer'] == "hipomania:1"


def testa_todos_verdadeiros_exceto_fisiologico():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=0,
        prejuizo_social=1,
        prejuiso_profissional=1,
        psicose=1,
        autoestima_inflada=1,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=1,
        fuga_ideias=1,
        pensamento_acelerado=1,
        aumento_atividade_objetivo=1,
        agitacao_psicomotora=1,
        reducao_sono=1,
        distrabilidade=1,
        envolvimento_atividade_risco=1
    ))
    engine.run()
    return engine.result['answer'] == ":0"


def testa_menos_que_3_mudanca_comportamento():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=1,
        prejuiso_profissional=0,
        psicose=1,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=0,
        pressao_continuar_falando=0,
        fuga_ideias=0,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=0,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == ":0"


def testa_igual_a_3_mudanca_comportamento():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=0,
        prejuiso_profissional=0,
        psicose=1,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=0,
        fuga_ideias=1,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=0,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == "mania:1"


def testa_maior_que_3_mudanca_comportamento():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=0,
        prejuiso_profissional=0,
        psicose=1,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=0,
        fuga_ideias=1,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=1,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == "mania:1"


def testa_menos_que_3_mudanca_comportamento_psicose_falso():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=1,
        prejuiso_profissional=0,
        psicose=0,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=0,
        pressao_continuar_falando=0,
        fuga_ideias=0,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=0,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == ":0"


def testa_igual_a_3_mudanca_comportamento_psicose_false():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=0,
        prejuiso_profissional=0,
        psicose=0,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=0,
        fuga_ideias=1,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=0,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == "hipomania:1"


def testa_maior_que_3_mudanca_comportamento_psicose_false():
    engine = Mania()
    engine.reset()
    engine.declare(Sintomas(
        fisiologico=1,
        prejuizo_social=0,
        prejuiso_profissional=0,
        psicose=0,
        autoestima_inflada=0,
        grandiosidade=1,
        loquaz=1,
        pressao_continuar_falando=0,
        fuga_ideias=1,
        pensamento_acelerado=0,
        aumento_atividade_objetivo=1,
        agitacao_psicomotora=0,
        reducao_sono=0,
        distrabilidade=0,
        envolvimento_atividade_risco=0
    ))
    engine.run()
    return engine.result['answer'] == "hipomania:1"


if __name__ == '__main__':
    print(testa_todos_falsos())
    print(testa_todos_verdadeiros())
    print(testa_todos_verdadeiros_exceto_psicose())
    print(testa_todos_verdadeiros_exceto_fisiologico())
    print(testa_menos_que_3_mudanca_comportamento())
    print(testa_igual_a_3_mudanca_comportamento())
    print(testa_maior_que_3_mudanca_comportamento())
    print(testa_menos_que_3_mudanca_comportamento_psicose_falso())
    print(testa_igual_a_3_mudanca_comportamento_psicose_false())
    print(testa_maior_que_3_mudanca_comportamento_psicose_false())
