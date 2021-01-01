import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const Soldier = props => (
    <tr>
      <td>{props.soldier.name}</td>
      <td>
        <Link to={"/view/"+props.soldier.name}>view</Link> | <button onClick={() => { props.deleteSoldier(props.soldier.name) }}>delete</button>
      </td>
    </tr>
  )

export default class SoldierGrid extends Component {
  constructor(props) {
    super(props);
    this.deleteSoldier = this.deleteSoldier.bind(this);
    this.updateSoldiers = this.updateSoldiers.bind(this);
    this.state = { soldiers: [] };
  }

  componentDidMount() {
    axios
      .get('http://localhost:5000/api/soldiers')
      .then((response) => {
        this.setState({ soldiers: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  updateSoldiers() {
    axios
      .get('http://localhost:5000/api/soldiers')
      .then((response) => {
        this.setState({ soldiers: response.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  deleteSoldier(name) {
    const soldier = { name: name };
    axios
      .post('http://localhost:5000/api/soldiers/delete', soldier)
      .then((res) => console.log(res.data));
    this.setState({
      soldiers: this.state.soldiers.filter((s) => s.name !== name),
    });
  }

  soldierList() {
    return this.state.soldiers.map((currentSoldier) => {
      return (
        <Soldier
          soldier={currentSoldier}
          deleteSoldier={this.deleteSoldier}
          key={currentSoldier}
        />
      );
    });
  }

  render() {
    return (
      <div>
        <h3>Soldiers</h3>
        <button type="button" class="btn btn-primary btn-lg" onClick={() => { this.updateSoldiers() }}>update</button>
        <table className="table">
          <thead className="thead-light">
            <tr>
              <th>Username</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>{this.soldierList()}</tbody>
        </table>
      </div>
    );
  }
}
