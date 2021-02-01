import axios from 'axios';
import React, { Component } from 'react'
import {Form} from 'react-formio';

export default class FormViewer extends Component {

    constructor(props){
        super(props);
        this.state = {
            form: null,
            submissionData : {},
            loading : "loading ..."
        }
    }

    componentDidMount(){
        const id = this.props.match.params.id;
        this.getForm(id);
    }
    
    getForm = async(id) => {
        try {
            let form = await axios.get(`/api/former/${id}`);
            form = JSON.parse(JSON.stringify(form.data["form_schema"]))
            this.setState({form });

        } catch(e) {
            console.log(e);
            this.setState({loading : e["message"] || "Something went wrong, please try again later!" })
        }
    }

    submitHandler = async(d) => {
        delete d['data']['submit']
        d = {"data":d['data']}
        let id = this.props.match.params.id
        try {
            let res = await axios.post(`/api/former/${id}`,d)
            this.setState({submissionData : {}})
        } catch(e) {
            console.log(e);
        }

        return true
    }

 

    render() {
        if(this.state.form == null) {
            return <> {this.state.loading} </>
        }
        return (
            <div>
                <Form
                    src={this.state.form}
                    onSubmit={this.submitHandler}
                    submission={{ data: this.state.submissionData }}
                   />
            </div>
        )
    }
}
