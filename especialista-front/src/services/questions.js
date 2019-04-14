export default class QuestionsService {

    questions = [
        {
            variable: "fisiologico",
            variableStatus: undefined,
            question: "fisiologico",
            isAnswered: false
        }, {
            variable: "prejuizo_social",
            variableStatus: undefined,
            question: "prejuizo_social",
            isAnswered: false
        }, {
            variable: "prejuiso_profissional",
            variableStatus: undefined,
            question: "prejuiso_profissional",
            isAnswered: false
        }, {
            variable: "psicose",
            variableStatus: undefined,
            question: "psicose",
            isAnswered: false
        }, {
            variable: "autoestima_inflada",
            variableStatus: undefined,
            question: "autoestima_inflada",
            isAnswered: false
        }, {
            variable: "grandiosidade",
            variableStatus: undefined,
            question: "grandiosidade",
            isAnswered: false
        }, {
            variable: "loquaz",
            variableStatus: undefined,
            question: "loquaz",
            isAnswered: false
        }, {
            variable: "pressao_continuar_falando",
            variableStatus: undefined,
            question: "pressao_continuar_falando",
            isAnswered: false
        }, {
            variable: "fuga_ideias",
            variableStatus: undefined,
            question: "fuga_ideias",
            isAnswered: false
        }, {
            variable: "pensamento_acelerado",
            variableStatus: undefined,
            question: "pensamento_acelerado",
            isAnswered: false
        }, {
            variable: "agitacao_psicomotora",
            variableStatus: undefined,
            question: "agitacao_psicomotora",
            isAnswered: false
        },{
            variable: "aumento_atividade_objetivo",
            variableStatus: undefined,
            question: "aumento_atividade_objetivo",
            isAnswered: false
        }, {
            variable: "reducao_sono",
            variableStatus: undefined,
            question: "reducao_sono",
            isAnswered: false
        }, {
            variable: "distrabilidade",
            variableStatus: undefined,
            question: "distrabilidade",
            isAnswered: false
        }, {
            variable: "envolvimento_atividade_risco",
            variableStatus: undefined,
            question: "envolvimento_atividade_risco",
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
