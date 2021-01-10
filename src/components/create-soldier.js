import React, { Component } from "react";
import axios from 'axios';

export default class CreateSoldier extends Component {
  constructor(props) {
    super(props);

    this.onChangeName = this.onChangeName.bind(this);
    this.onChangeBmi = this.onChangeBmi.bind(this);
    this.onChangeBodyDifferential = this.onChangeBodyDifferential.bind(this);
    this.onSubmit = this.onSubmit.bind(this);

    this.state = {
      name: "",
      bmi: undefined,
      bodyDifferential: 1,
    };
  }

  onChangeName(e) {
    this.setState({
      name: e.target.value,
    });
  }

  onChangeBmi(e) {
    this.setState({
      bmi: e.target.value,
    });
  }

  onChangeBodyDifferential(e) {
    this.setState({
      bodyDifferential: e.target.value,
    });
  }

  onSubmit(e) {
    e.preventDefault();

    const newSoldier = {
      name: this.state.name,
      bmi: this.state.bmi,
      bodyDifferential: this.state.bodyDifferential,
    };

    axios
      .post('http://localhost:5000/api/soldiers/add', newSoldier)
      .then((res) => console.log(res.data));

    window.location = "/";
  }

  render() {
    return (
      <div>
        <h3>Create New Soldier</h3>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>name: </label>
            <input
              type="text"
              required
              className="form-control"
              value={this.state.name}
              onChange={this.onChangeName}
            />
          </div>
          <div className="form-group">
            <label>BMI: </label>
            <input
              type="number"
              required
              className="form-control"
              value={this.state.bmi}
              onChange={this.onChangeBmi}
            />
          </div>
          <div className="form-group">
            <label>Body Differential: </label>
            <input
              type="number"
              required
              className="form-control"
              value={this.state.bodyDifferential}
              onChange={this.onChangeBodyDifferential}
            />
          </div>
          <div className="form-group">
            <label>Garmin Watch Number: </label>
            <input
              type="number"
              
              className="form-control"
              
            />
          </div>

          <div className="form-group">
            <input
              type="submit"
              value="Create Soldier"
              className="btn btn-primary"
            />
          </div>
        </form>
      </div>
    );
  }
}
