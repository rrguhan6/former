import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import FormBuilder from "./components/FormBuilder";
import FormViewer from "./components/FormViewer";
import Table from "./components/Table";

export default class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/" exact component={FormBuilder} />
          <Route path="/former/:id" exact component={FormViewer} />
          <Route path="/former/records/:id" exact component={Table} />
        </Switch>
      </Router>
    );
  }
}
