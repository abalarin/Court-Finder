import React from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

import Navbar from './Navbars/NavBar'
import ObjectStorage from './ObjectStorage'

const useStyles = makeStyles(theme => ({
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(8, 0, 6),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
}));

export default function Album() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Navbar />
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
              Find Some Pickup Games
            </Typography>
            <Typography variant="h5" align="center" color="textSecondary" paragraph>
              With our application you will never have to drive around your neigborhood looking for pickup games! Just join exsisting games or create a local game...
            </Typography>
            <div className={classes.heroButtons}>
              <Grid container spacing={2} justify="center">
                <Grid item>
                  <Button href="/courts" variant="contained" color="primary">
                    View Courts
                  </Button>
                </Grid>
                <Grid item>
                  <Button href="/map" variant="outlined" color="primary">
                    View Map
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
      </main>
      <ObjectStorage/>
    </React.Fragment>
  );
}
