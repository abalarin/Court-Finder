import React from 'react';
import './App.css';
import NavBar from './components/Navbars/NavBar'

class App extends React.Component {

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <NavBar/>
        </header>
      </div>
    );
  }
}

export default App;
