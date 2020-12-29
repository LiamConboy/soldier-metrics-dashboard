import React, { Component } from "react";
import axios from "axios";

export default class Soldier extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <tr>
        <td>{props.soldier.name}</td>
        <td>
          <Link to={"/view/"+props.soldier.name}>view</Link> | <button onClick={() => { props.deleteSoldier(props.soldier.name) }}>delete</button>
        </td>
      </tr>
    );
  }
}
