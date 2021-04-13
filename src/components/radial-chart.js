import { React, Component } from "react";
import { RadialBarChart, RadialBar, Label, ResponsiveContainer } from "recharts";
import PropTypes from "prop-types";
import { Tooltip } from "recharts";


  
  


const RadialChart = ({ value }) => {

  const data = [
    {
      name: "Base",
      uv: 15,
      fill: "#000000",
    },
    {
      name: "PulseOx",
      uv: ( value ? value : 10 ),
      fill: ( value > 7 ? "#009900" : "#ff0000" ),
    },
  ];

  var labelValue = value + 85

  class CustomLabel extends Component { 
    constructor(props) {
      super(props);
      //this.deleteSoldier = this.deleteSoldier.bind(this);
      this.labelValue = labelValue
      
    }
    render() {  
      
          return (
            <g>
              <foreignObject x={100} y={101} width={100} height={100}>
                <div>
                  <h2 style={{color: "white"}}>{this.labelValue}</h2>
                  
                </div>
              </foreignObject>
            </g>
          );
    }
  };

  return (
  
  <div className="chart align-items-center justify-content-center">
    <ResponsiveContainer width="100%" height={280}>
      <RadialBarChart
        width={500}
        height={280}
        cx={150}
        cy={120}
        innerRadius={20}
        outerRadius={140}
        barSize={40}
        data={data}
      >
        
        <RadialBar
          minAngle={360}
          //label={{ position: "insideStart", fill: "#fff" }}
          background
          clockWise
          dataKey="uv"
          label={CustomLabel}
        />
        
      </RadialBarChart>
    </ResponsiveContainer>
  </div>
);}

RadialChart.propTypes = {
  value: PropTypes.number
};

export default RadialChart;