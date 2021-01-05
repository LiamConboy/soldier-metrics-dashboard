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

const TimeSeriesChart = ({ chartData }) => (
  <ResponsiveContainer width="100%" height={280}>
    <AreaChart
      data={chartData}
      margin={{ top: 10, right: 45, left: 0, bottom: 0 }}
    >
      <CartesianGrid />
      <XAxis
        dataKey="time"
        domain={["auto", "auto"]}
        name="Time"
        tickFormatter={(unixTime) => moment(unixTime).format("HH:mm:ss")}
        type="number"
      />
      <YAxis dataKey="value" name="Value" />
      <Tooltip
        labelFormatter={(unixTime) => moment(unixTime).format("HH:mm:ss")}
      />
      <Area type="monotone" dataKey="value" stroke="#8884d8" fill="#8884d8" />
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
