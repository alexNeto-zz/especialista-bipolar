import React, { Component } from 'react';
import './App.css';
import 'bulma/css/bulma.min.css';

import QuestionHolder from './components/questionHolder';
import QuestionsService from './services/questions';

export default class App extends Component {

  state = {
    endpoint: "localhost:5000/mania",
    variable: "",
    question: "Iniciar questionário?",
    isFinalAnswer: false,
    finalAnswer: "",
    questionsService: new QuestionsService()
  }

  render() {
    return (
      <div className="App">
        {this.showContentWhenLoaded()}
      </div>
    );
  }

  showContentWhenLoaded() {
    if (this.state.question !== "" && this.state.isFinalAnswer === false) {
      return (<section className="section">
        <div className="container">
          <QuestionHolder question={this.state.question} answer={this.takeAnswer.bind(this)} />
        </div>
      </section>);
    } else if (this.state.isFinalAnswer === false) {
      return (<section className="section">
        <div className="container">
          Carregando...
      </div>
      </section>);
    } else {
      return <h1 className="title">{this.state.finalAnswer}</h1>
    }
  }

  takeAnswer(answer) {
    if (answer !== undefined)
      this.state.questionsService.setQuestionStatus(this.state.variable, answer);
    this.onFetch(answer);
  }

  onFetch(answer) {
    this.setState({
      question: "",
      isFinalAnswer: false
    });
    fetch("http://127.0.0.1:5000/mania" + this.getQueryString())
      .then(res => res.json())
      .then((result) => this.onFetchSuccess(result, answer), this.onFetchError)
  }

  onFetchSuccess(result, answer) {
    if (result.isFinalAnswer) {
      this.onFinalAnswer(result);
    } else {
      this.onNormalAnswer(result, answer);
    }
  }

  onFinalAnswer(result) {
    this.setState({
      variable: "",
      isFinalAnswer: true,
      finalAnswer: result.answer,
    });
  }

  onNormalAnswer(result) {
    this.setState({
      isFinalAnswer: result.isFinalAnswer,
      variable: result.variable,
      finalAnswer: result.answer,
      question: this.state.questionsService.getQuestion(result.variable)
    });
  }

  onFetchError(error) {
    console.log(error);
  }

  getQueryString() {
    return "?" + this.state.questionsService.getQuestionsAsQueryString();
  }

}
