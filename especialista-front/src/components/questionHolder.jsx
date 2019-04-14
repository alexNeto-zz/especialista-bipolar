import React, { Component } from 'react';

export default class QuestionHolder extends Component {
    render() {
        return (
            <div>
                <h1 className="title">{this.props.question}</h1>
                <div className="columns is-gapless">
                    <div className="column">
                        <button className="button is-medium" onClick={() => this.props.answer(1)}>Sim</button>
                    </div>
                    <div className="column">
                        <button className="button is-medium" onClick={() => this.props.answer(0)}>Não</button>
                    </div>
                </div>
            </div>
        )
    }
}
