import React, { Component } from "react";
import { FormBuilder } from "react-formio";
import { Link } from "react-router-dom";
import axios from "axios";
import "../styles.css";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      form: {},
      urlId: "",
    };
  }

  formBuilderHandler = (schema) => {
    this.setState({ form: schema });
  };

  saveForm = async () => {
    let data = { form: this.state.form };
    try {
      const response = await axios.post("/api/form/", data);
      let urlId = "http://localhost:3000/former/" + response.data.id;
      this.setState({ urlId });
    } catch (error) {
      console.error(error);
    }
  };

  render() {
    return (
      <div>
        <div className="App">
          <FormBuilder
            form={{ display: "form" }}
            onChange={(schema) => this.formBuilderHandler(schema)}
          />

          <button
            type="button"
            className="btn btn-success"
            onClick={this.saveForm}
          >
            Save form
          </button>
          <div>
            <a href={this.state.urlId} target="_blank">
              {this.state.urlId}
            </a>
          </div>
        </div>
      </div>
    );
  }
}
