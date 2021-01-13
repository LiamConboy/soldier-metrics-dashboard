import React from "react";
import TimeSeriesChart from "./time-series-chart";

function SoldierRiskScore(props) {
  return (
    <div>
      <TimeSeriesChart
        chartData={props.soldier.riskScore}
        yAxisTicks={[0, 20, 40, 60, 80, 100]}
      />
    </div>
  );
}

export default SoldierRiskScore;
