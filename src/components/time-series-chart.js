import React from "react";
import PropTypes from "prop-types";
import moment from "moment";

import {
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  AreaChart,
  Area,
  XAxis,
  YAxis,
} from "recharts";

const TimeSeriesChart = ({ chartData, yAxisTicks }) => (
  <ResponsiveContainer width="100%" height={280}>
    <AreaChart
      data={chartData}
      margin={{ top: 10, right: 45, left: 0, bottom: 0 }}
    >
      <CartesianGrid />
      <XAxis
        dataKey="time"
        domain={
          [
            chartData ? chartData.slice(-1)[0].time - 300000 : "dataMin",
            "dataMax",
          ] /* The x-axis domain goes from exactly 5 minutes (300000 milleseconds) before the latest time with data, up to latest time with data */
        }
        allowDataOverflow={true}
        name="Time"
        tickFormatter={(unixTime) => moment(unixTime).format("HH:mm:ss")}
        type="number"
      />
      <YAxis dataKey="value" ticks={yAxisTicks} name="Value" />
      <Tooltip
        labelFormatter={(unixTime) => moment(unixTime).format("HH:mm:ss")}
      />
      <Area type="monotone" dataKey="value" stroke="#461D7C" fill="#461D7C" />
    </AreaChart>
  </ResponsiveContainer>
);

TimeSeriesChart.propTypes = {
  chartData: PropTypes.arrayOf(
    PropTypes.shape({
      time: PropTypes.number,
      value: PropTypes.number,
    })
  ).isRequired,
};

export default TimeSeriesChart;
