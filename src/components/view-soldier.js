import React, { Component } from "react";
import axios from "axios";
import ViewSoldierTimeSeriesChart from "./view-soldier-time-series-chart";
import ViewSoldierNumberPanel from "./view-soldier-number-panel";
import RadialChart from "./radial-chart"

export default class ViewSoldier extends Component {
  constructor(props) {
    super(props);
    //this.deleteSoldier = this.deleteSoldier.bind(this);
    this.updateSoldier = this.updateSoldier.bind(this);
    this.state = { soldier: {}, pulseOxValue: 95 };
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
          <div className="col-md-5">
            <h1 style={{ textAlign: "center" }}>
              Soldier {this.state.soldier.name} Metrics
            </h1>
          </div>
          <div className="col-md-5" style={{ textAlign: "center" }}>
            <button
              type="button"
              className="btn btn-primary btn-lg"
              style={{ width: "75%", minHeight: "75%" }}
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
          <div className="col-lg-6">
            {/* <ViewSoldierTimeSeriesChart
              label={"Risk Score"}
              data={this.state.soldier.riskScore}
              yAxisTicks={[0, 20, 40, 60, 80, 100]}
              pulseOx={this.state.pulseOxValue}
            /> */}
            <div className="col justify-content-center align-items-center">
              <h5 style={{ margin: "10px 0", textAlign: "center" }}>
                {"Current PulseOx"}
              </h5>
              <h5 style={{ textAlign: "center" }}>
                {this.state.pulseOxValue}
              </h5>
              <RadialChart value={this.state.pulseOxValue-85} />
              
            </div>
            
          </div>
          <div className="col-lg-6">
            <ViewSoldierTimeSeriesChart
              label={"Heart Rate"}
              data={this.state.soldier.heartRate}
              yAxisTicks={[0, 40, 80, 120, 160, 200]}
            />
          </div>
          {/* <div className="col-lg-4">
            <ViewSoldierTimeSeriesChart
              label={"Water"}
              data={this.state.soldier.water}
              yAxisTicks={[0, 20, 40, 60, 80, 100]}
            />
          </div> */}
        </div>
        {/* <div
          className="row justify-content-center"
          style={{ marginBottom: "20px" }}
        >
          <div className="col-md-4">
            <ViewSoldierNumberPanel
              label={"BMI"}
              data={this.state.soldier.bmi || [{ time: 0, value: 0 }]}
            />
          </div>
          <div className="col-md-4">
            <ViewSoldierNumberPanel
              label={"Body Differential"}
              data={
                this.state.soldier.bodyDifferential || [{ time: 0, value: 0 }]
              }
            />
          </div>
        </div> */}
      </div>
    );
  }
}
