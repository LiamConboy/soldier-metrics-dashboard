import React from "react";
import TimeSeriesChart from "./time-series-chart"

function SoldierRiskScore(props) {
    const testChartData = [
        { value: 14, time: 1503617297689 },
        { value: 15, time: 1503616962277 },
        { value: 15, time: 1503616882654 },
        { value: 20, time: 1503613184594 },
        { value: 15, time: 1503611308914 },
      ]

  return (
      
    <div>
      <TimeSeriesChart
        chartData={props.soldier.riskScore}
      />
    </div>
  );
}

export default SoldierRiskScore;
