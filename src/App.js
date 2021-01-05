import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

import Navbar from "./components/navbar";
import SoldierGrid from "./components/soldier-grid";
import ViewSoldier from "./components/view-soldier";
import CreateSoldier from "./components/create-soldier";

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <br />
        <Route path="/" exact component={SoldierGrid} />
        <Route path="/view/:name" component={ViewSoldier} />
        <Route path="/soldier" component={CreateSoldier} />
      </div>
    </Router>
  );
}

export default App;
