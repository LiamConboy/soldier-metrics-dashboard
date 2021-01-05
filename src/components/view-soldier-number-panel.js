import React, { Component } from "react";

export default class ViewSoldierNumberPanel extends Component {
  render() {
    return (
      <div className="col justify-content-center align-items-center">
        <h5 style={{ margin: "10px 0", textAlign: "center" }}>
          {this.props.label}
        </h5>
        <h1 style={{ margin: "10px 0", textAlign: "center" }}>
          {this.props.data.slice(-1)[0].value}
        </h1>
      </div>
    );
  }
}
