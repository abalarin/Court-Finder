import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Login, PrivateRoute} from './components/Login'
import HomePage from './components/HomePage'
import Courts from './components/Courts'
import CourtProfile from './components/CourtProfile'
import Map from './components/Map'

import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";

ReactDOM.render(
  <Router>
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route path="/courts" component={Courts} />
      <Route path="/map" component={Map} />
      <Route path="/login" component={Login} />
      <Route path="/court/:id" key=":id" component={CourtProfile} />
      <PrivateRoute path="/app" component={App} />
    </Switch>
  </Router>,
  document.getElementById('root')
);
