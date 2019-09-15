import React from 'react';
import image from './objectstorage.png'
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles(theme => ({
  root: {
    marginTop: 50,
  },
  image: {
    padding: 30,
    width: 635,
    height: 504,
  },
  title: {
    textAlign: "center",
    marginTop: 100,
  },
  description: {
    textAlign: "center",
    marginTop: 20,
  }

}));

export default function ObjectStorage() {
  const classes = useStyles();

  return(
    <Container>
      <Grid container className={classes.root} spacing={2}>
        <Grid item xs={6}>
          <a href="https://welcome.linode.com/object-storage/">
            <img src={image} alt="whyyy" className={classes.image}/>
          </a>
        </Grid>
        <Grid item xs={6}>
          <Typography variant="h5" component="h3" className={classes.title}>
            Featuring Linode's Object Storage!
          </Typography>
          <Typography className={classes.description}>
            This Application is now using Linode's Beta Object Storage to serve its static assest!
          </Typography>
        </Grid>
      </Grid>
    </Container>
  )
}
