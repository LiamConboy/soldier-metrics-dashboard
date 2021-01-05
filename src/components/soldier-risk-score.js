import React from "react";
import TimeSeriesChart from "./time-series-chart";

function SoldierRiskScore(props) {
  return (
    <div>
      <TimeSeriesChart chartData={props.soldier.riskScore} />
    </div>
  );
}

export default SoldierRiskScore;
