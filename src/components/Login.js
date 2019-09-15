import axios from 'axios';
import Navbar from './Navbars/NavBar'
import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

import * as Cookies from 'js-cookie';


import {
  Route,
  Redirect
} from "react-router-dom";

const useStyles = makeStyles(theme => ({
  '@global': {
    body: {
      backgroundColor: theme.palette.common.white,
    },
  },
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export function SignIn(props) {
  const classes = useStyles();

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <form onSubmit={props.handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            label="Username"
            name="username"
            autoFocus
            onChange={props.handleChange}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={props.handleChange}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign In
          </Button>
        </form>
      </div>
    </Container>
  );
}

export const Auth = {
  isAuthenticated: Cookies.get('authToken'),
  authenticate(cb) {
    Cookies.set('authToken', 'value', { expires: 1 })
    setTimeout(cb, 100); // fake async
  },
  signout(cb) {
    Cookies.remove('authToken');
    setTimeout(cb, 100);
  }
};

export function PrivateRoute({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={props =>
        Auth.isAuthenticated ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: props.location }
            }}
          />
        )
      }
    />
  );
}

function Navver(props) {
  if(Auth.isAuthenticated){
    return(
      <Redirect to="/" />
    )
  }
  else {
    return(
      <SignIn
      login={props.login}
      handleSubmit={props.handleSubmit}
      handleChange={props.handleChange}
      />
    )
  }
}

export class Login extends React.Component {
  state = {
    redirectToReferrer: false,
    username: '',
    password: ''
  };

  login = () => {
    Auth.authenticate();
  };

  handleChange = event => {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit = event => {
    event.preventDefault();

    const user = {
      username: this.state.username,
      password: this.state.password
    };

    axios.post('https://api.findthecourt.com/login', { user })
      .then(res => {
        if(res.data["msg"] === "success"){
          this.login()
          console.log("fucking redirect")
          window.location.reload();
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  render() {

    return (
      <React.Fragment>
        <Navbar />
        <Navver
        login={this.login}
        handleSubmit={this.handleSubmit}
        handleChange={this.handleChange}
        />
      </React.Fragment>
    );
  }
}
