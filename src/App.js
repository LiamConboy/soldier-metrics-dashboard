import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

import Navbar from "./components/navbar";
import SoldierGrid from "./components/soldier-grid";
import ViewSoldier from "./components/view-soldier";
import CreateSoldier from "./components/create-soldier";
import RadialChart from "./components/radial-chart";

function App() {
  return (
    <Router>
      <div className="container bg-dark">
        <Navbar className="bg-secondary" />
        <br />
        <Route path="/" exact component={SoldierGrid} />
        <Route path="/view/:name" component={ViewSoldier} />
        <Route path="/soldier" component={CreateSoldier} />
        <Route path="/test" render={() => (<RadialChart value={90-85}/>)} />
      </div>
    </Router>
  );
}

export default App;
