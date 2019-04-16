export default class QuestionsService {

    questions = [
        {
            variable: "fisiologico",
            variableStatus: undefined,
            question: "fisiologico ?",
            isAnswered: false
        }, {
            variable: "prejuizo_social",
            variableStatus: undefined,
            question: "prejuizo social?",
            isAnswered: false
        }, {
            variable: "prejuiso_profissional",
            variableStatus: undefined,
            question: "prejuiso profissional?",
            isAnswered: false
        }, {
            variable: "psicose",
            variableStatus: undefined,
            question: "psicose?",
            isAnswered: false
        }, {
            variable: "autoestima_inflada",
            variableStatus: undefined,
            question: "autoestima inflada?",
            isAnswered: false
        }, {
            variable: "grandiosidade",
            variableStatus: undefined,
            question: "grandiosidade?",
            isAnswered: false
        }, {
            variable: "loquaz",
            variableStatus: undefined,
            question: "loquaz?",
            isAnswered: false
        }, {
            variable: "pressao_continuar_falando",
            variableStatus: undefined,
            question: "pressao continuar falando?",
            isAnswered: false
        }, {
            variable: "fuga_ideias",
            variableStatus: undefined,
            question: "fuga ideias?",
            isAnswered: false
        }, {
            variable: "pensamento_acelerado",
            variableStatus: undefined,
            question: "pensamento acelerado?",
            isAnswered: false
        }, {
            variable: "agitacao_psicomotora",
            variableStatus: undefined,
            question: "agitacao psicomotora?",
            isAnswered: false
        },{
            variable: "aumento_atividade_objetivo",
            variableStatus: undefined,
            question: "aumento atividade objetivo?",
            isAnswered: false
        }, {
            variable: "reducao_sono",
            variableStatus: undefined,
            question: "reducao sono?",
            isAnswered: false
        }, {
            variable: "distrabilidade",
            variableStatus: undefined,
            question: "distrabilidade?",
            isAnswered: false
        }, {
            variable: "envolvimento_atividade_risco",
            variableStatus: undefined,
            question: "envolvimento atividade risco?",
            isAnswered: false
        }
    ];

    getQuestions() {
        return this.questions;
    }

    getQuestionsAsQueryString() {
        return this.questions.map(makeParameter).reduce(makeQueryString, "");

        function makeParameter(question) {
            return question.variable + "=" + question.variableStatus;
        }

        function makeQueryString(acumulator, question) {
            return acumulator + question + "&";
        }
    }

    getQuestion(variable) {
        return this.questions[this.findIndexByVariable(variable)].question;
    }

    setQuestionStatus(variable, variableStatus) {
        return this.questions[this.findIndexByVariable(variable)].variableStatus = variableStatus;
    }

    findIndexByVariable(variable) {
        return this.questions.findIndex(question => question.variable === variable);
    }
}
