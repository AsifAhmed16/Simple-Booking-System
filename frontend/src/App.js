import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      output: "",
      start_date: null,
      end_date: null
    };

    this.submit = this.submit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  async call_api(from_date, to_date) {
    const config = {
      headers: {
          'Content-Type': 'application/json'
      }
    };

    const body = JSON.stringify({ from_date, to_date });

    try {
      const res = await axios.post(`${process.env.REACT_APP_API_URL}/api/booking/`, body, config);
      this.handleChange({ output: (res.data.msg) });
      console.log(this.state.output);
    } catch(error) {
      console.log(error.response);
      this.handleChange({ output: (error.response.data.msg) });
      console.log(this.state.output);
    };
  }

  submit(e) {
    e.preventDefault();

    const from_date = this.state.start_date;
    const to_date = this.state.end_date;
    this.call_api(from_date, to_date);
  }

  handleChange(changeObject) {
    this.setState(changeObject)
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <form>
            <label> - - - - - SIMPLE BOOKING SYSTEM - - - - - </label>
            <br/>
            <br/>
            <label>Start Date . . .  
            <input 
              type="date" 
              name="start_date"
              id="start_date"
              className="form-control"
              value={this.state.start_date}
              onChange={(e) => this.handleChange({ start_date: e.target.value })}
              required
            />
            </label>
              <br/>
              <br/>
            <label>End Date . . . . 
            <input 
              type="date" 
              name="end_date"
              id="end_date"
              className="form-control"
              value={this.state.end_date}
              onChange={(e) => this.handleChange({ end_date: e.target.value })}
              required
            />
            </label>
              <br/>
              <br/>
            <button className="btn btn-primary" type='button' onClick={(e) => this.submit(e)}>
              Submit
            </button>
            <br/>
            <br/>
            <p>{ this.state.output }</p>
          </form>
        </header>
      </div>
    );
  }
}

export default App;
