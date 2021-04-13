import React, { Component } from "react";
import { Link } from "react-router-dom";
import SoldierRiskScore from "./soldier-risk-score";

export default class Soldier extends Component {
  render() {
    return (
      <div className="row justify-content-center align-items-center">
        <div className="col justify-content-center align-items-center">
          <h3 style={{ margin: "10px 0", color: "gainsboro" }}>{this.props.soldier.name}</h3>
          <div className="row justify-content-center align-items-center">
            {/* <Link
              to={"/view/" + this.props.soldier.name}
              type="button"
              className="btn btn-secondary btn-lg"
              style={{ margin: "0 10px" }}
            >
              view
            </Link> */}
            <button
              type="button"
              className="btn btn-danger btn-lg"
              style={{ margin: "0 10px" }}
              onClick={() => {
                this.props.deleteSoldier(this.props.soldier.name);
              }}
            >
              delete
            </button>
          </div>
          <SoldierRiskScore soldier={this.props.soldier} pulseOx={this.props.pulseOx} />
        </div>
      </div>
    );
  }
}
