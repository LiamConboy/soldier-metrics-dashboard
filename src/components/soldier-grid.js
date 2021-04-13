import React, { Component } from "react";
import axios from "axios";
import Soldier from "./soldier";

export default class SoldierGrid extends Component {
  constructor(props) {
    super(props);
    this.deleteSoldier = this.deleteSoldier.bind(this);
    this.updateSoldiers = this.updateSoldiers.bind(this);
    this.state = { soldiers: [], pulseOxValues: [96, 93, 90, 96, 94, 99, 99, 99] };
  }

  componentDidMount() {
    axios
      .get("http://localhost:5000/api/soldiers")
      .then((response) => {
        this.setState({ soldiers: response.data });
      })
      .catch((error) => {
        console.log(error);
      });

      

  }

  updateSoldiers() {
    axios
      .get("http://localhost:5000/api/soldiers")
      .then((response) => {
        this.setState({ soldiers: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
    
    this.setState({ pulseOxValues: this.state.pulseOxValues.map((value) => {return value-1}) })
  }

  deleteSoldier(name) {
    const soldier = { name: name };
    axios
      .post("http://localhost:5000/api/soldiers/delete", soldier)
      .then((res) => console.log(res.data));
    this.setState({
      soldiers: this.state.soldiers.filter((s) => s.name !== name),
    });
  }

  render() {
    return (
      <div className="container">
        <div
          className="row justify-content-center"
          style={{ marginBottom: "20px" }}
        >
          <div className="col-md-4">
            <h1 style={{ textAlign: "center", color:"gainsboro" }}>Soldier Pulse Ox Values</h1>
          </div>
          <div className="col-md-4" style={{ textAlign: "center" }}>
            <button
              type="button"
              className="btn btn-primary btn-lg"
              style={{ width: "75%", minHeight: "75%", color: "black" }}
              onClick={() => {
                this.updateSoldiers();
              }}
            >
              update
            </button>
          </div>
        </div>
        <div className="row justify-content-center">
          {this.state.soldiers.map((currentSoldier, i) => {
            return (
              <div
                className="col-md-6"
                style={{ textAlign: "center", marginBottom: "20px" }}
              >
                <Soldier
                  soldier={currentSoldier}
                  deleteSoldier={this.deleteSoldier}
                  key={currentSoldier.name}
                  pulseOx={this.state.pulseOxValues[i]}
                />
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}
