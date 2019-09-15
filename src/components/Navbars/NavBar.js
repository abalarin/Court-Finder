import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Link from '@material-ui/core/Link';
import { Auth } from '../Login';

import { makeStyles } from '@material-ui/core/styles';
import Toolbar from '@material-ui/core/Toolbar';

const useStyles = makeStyles(theme => ({
  root: {
    marginBottom: 30,
  },
  title: {
    flexGrow: 1,
    textDecoration: "none",
  },
}));

export default function Navbar() {
  const classes = useStyles();

  function Navver() {
    if(Auth.isAuthenticated){
      return(
        <Button
        color="inherit"
        href="/login"
        onClick={Auth.signout}
        >
        Logout
        </Button>
      )
    }
    else {
      return(
        <Button color="inherit" href="/login">Login</Button>
      )
    }
  }

  return(
    <AppBar className={classes.root} position="static">
      <Toolbar>
        <Link variant="h6" color="inherit" href="/" className={classes.title}>
          CourtFinder
        </Link>
        <Navver />
      </Toolbar>
    </AppBar>
  )
}
