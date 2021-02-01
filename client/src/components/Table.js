import React, { Component } from "react";
import axios from "axios";

export default class Table extends Component {
  constructor(props) {
    super(props);
    this.state = {
      headers: null,
      body: null,
      loading: "Loading",
    };
  }

  componentDidMount() {
    const id = this.props.match.params.id;
    this.setHeader(id);
    this.setBody(id);
  }

  setHeader = async (id) => {
    try {
      let form = await axios.get(`/api/former/${id}`);
      form = JSON.parse(JSON.stringify(form.data["form_schema"]));
      let headers = [];
      for (let i of form["components"]) {
        if (i["type"] != "button") {
          headers.push(i);
        }
      }
      this.setState({ headers });
    } catch (e) {
      console.log(e);
      this.setState({
        loading:
          e["message"] || "Something went wrong, please try again later!",
      });
    }
  };

  setBody = async (id) => {
    try {
      let form = await axios.get(`/api/records/${id}`);
      console.log(form.data);
      this.setState({body : form.data});  
    } catch (e) {
      console.log(e);
      this.setState({
        loading:
          e["message"] || "Something went wrong, please try again later!",
      });
    }
  };

  render() {
    if (this.state.body == null) {
      return <>{this.state.loading}</>;
    }
    return (
      <div>
        <table className="table">
          <thead className="thead-dark">
            <tr>
              <th scope="col">#</th>
              {(this.state.headers || []).map((data, k) => {
                return <th scope="col">{data["label"]}</th>;
              })}
            </tr>
          </thead>
          <tbody>
            
              {(this.state.body.data || []).map((row)=>{
                return <tr>
                  {(row || []).map((d,k)=><td key={k}>{d}</td>)}
                </tr>
              })}
              
            
          </tbody>
        </table>
      </div>
    );
  }
}
