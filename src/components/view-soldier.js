import React, { Component } from "react";
import axios from "axios";
import ViewSoldierTimeSeriesChart from "./view-soldier-time-series-chart";
import ViewSoldierNumberPanel from "./view-soldier-number-panel";

export default class ViewSoldier extends Component {
  constructor(props) {
    super(props);
    //this.deleteSoldier = this.deleteSoldier.bind(this);
    this.updateSoldier = this.updateSoldier.bind(this);
    this.state = { soldier: {} };
  }

  componentDidMount() {
    const name = this.props.match.params.name;
    axios
      .get("http://localhost:5000/api/soldiers/soldier/" + name)
      .then((response) => {
        this.setState({ soldier: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  updateSoldier() {
    const name = this.props.match.params.name;
    console.log(this.state.soldier);
    axios
      .get("http://localhost:5000/api/soldiers/soldier/" + name)
      .then((response) => {
        this.setState({ soldier: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  /*
  deleteSoldier(name) {
    const soldier = { name: name };
    axios
      .post("http://localhost:5000/api/soldiers/delete", soldier)
      .then((res) => console.log(res.data));
    this.setState({
      soldiers: this.state.soldiers.filter((s) => s.name !== name),
    });
  }
  */

  render() {
    return (
      <div className="container">
        <div
          className="row justify-content-center"
          style={{ marginBottom: "20px" }}
        >
          <div className="col-3">
            <h3 style={{ textAlign: "center" }}>
              Soldier {this.state.soldier.name} Metrics
            </h3>
          </div>
          <div className="col-2" style={{ textAlign: "center" }}>
            <button
              type="button"
              className="btn btn-primary btn-lg"
              onClick={() => {
                this.updateSoldier();
              }}
            >
              update
            </button>
          </div>
        </div>
        <div
          className="row justify-content-center"
          style={{ marginBottom: "20px" }}
        >
          <div className="col-4">
            <ViewSoldierTimeSeriesChart
              label={"Risk Score"}
              data={this.state.soldier.riskScore}
            />
          </div>
          <div className="col-4">
            <ViewSoldierTimeSeriesChart
              label={"Heart Rate"}
              data={this.state.soldier.heartRate}
            />
          </div>
          <div className="col-4">
            <ViewSoldierTimeSeriesChart
              label={"Water"}
              data={this.state.soldier.water}
            />
          </div>
        </div>
        <div
          className="row justify-content-center"
          style={{ marginBottom: "20px" }}
        >
          <div className="col-4">
            <ViewSoldierNumberPanel
              label={"BMI"}
              data={this.state.soldier.bmi || [{ time: 0, value: 0 }]}
            />
          </div>
          <div className="col-4">
            <ViewSoldierNumberPanel
              label={"Body Differential"}
              data={
                this.state.soldier.bodyDifferential || [{ time: 0, value: 0 }]
              }
            />
          </div>
        </div>
      </div>
    );
  }
}
