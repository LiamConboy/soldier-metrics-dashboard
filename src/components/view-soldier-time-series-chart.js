import React, { Component } from "react";
import TimeSeriesChart from "./time-series-chart";

export default class ViewSoldierTimeSeriesChart extends Component {
  render() {
    return (
      <div className="col justify-content-center align-items-center">
        <h5 style={{ margin: "10px 0", textAlign: "center" }}>
          {this.props.label}
        </h5>
        <TimeSeriesChart
          chartData={this.props.data}
          yAxisTicks={this.props.yAxisTicks}
        />
      </div>
    );
  }
}
