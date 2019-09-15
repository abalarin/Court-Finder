import axios from 'axios';
import React from 'react';
import Container from '@material-ui/core/Container';
import Navbar from '../components/Navbars/NavBar'
import Box from '@material-ui/core/Box';

import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import Typography from '@material-ui/core/Typography';
import image from './basketball.png';

const useStyles = makeStyles(theme => ({
  root: {
    marginTop: 50,
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
  },
  gridList: {
    width: 500,
    height: 450,
  },
}));

function CourtTitle(props) {

  if(props.court){
    return(
      <React.Fragment>
      <Box textAlign="center">
        <Typography variant="h2" gutterBottom>
            {props.court.name}
        </Typography>
        <Typography variant="h6" gutterBottom>
          {props.court.address}
        </Typography>
      </Box>
      </React.Fragment>
    )
  }
  else {
    return(
      <h1>loading..</h1>
    )
  }
}

function CourtGallery(props) {
  const classes = useStyles();

  if(props.court && props.court.image_urls.length){
    return (
      <div className={classes.root}>
        <GridList cellHeight={160} className={classes.gridList} cols={2}>
          {props.court.image_urls.map(tile => (
            <GridListTile key={tile} cols={1}>
              <img src={tile} alt="broken img" />
            </GridListTile>
          ))}
        </GridList>
      </div>
  );}
  else{
    return (
      <div/>
    );
  }
}

function CourtReviews(props) {
  const classes = useStyles();

  if(props.reviews && props.reviews.length){
    return(
      <div className={classes.root}>
      <React.Fragment>
      <Container maxWidth="sm">
        <Typography variant="h4">
          <Box textAlign="center">
            Reviews:
          </Box>
        </Typography>
        {props.reviews.map(review => (
          <List key={review.id}>
            <ListItem alignItems="flex-start">
              <ListItemAvatar>
                <Avatar alt="Remy Sharp" src={image} />
              </ListItemAvatar>
              <ListItemText
                primary={review.data.username}
                secondary={
                  <React.Fragment>
                    <Typography
                      component="span"
                      variant="body2"
                      className={classes.inline}
                      color="textPrimary"
                    >
                      {review.data.date}
                    </Typography>
                    {" - " + review.data.review}
                  </React.Fragment>
                }
              />
            </ListItem>
            <Divider variant="inset" component="li" />
          </List>
        ))}
      </Container>
      </React.Fragment>
      </div>
    )
  }
  else{
    return(
      <div/>
    )
  }
}

class CourtProfile extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      court_id: props.match.params.id,
    };
  }

  state = {
    court_name: '',
    court_id: '',
    court: [],
    court_reviews: []
  }

  componentDidMount() {
    axios.get('https://api.findthecourt.com/court/' + this.state.court_id)
      .then(res => {
        // console.log(res.data)
        const court = res.data;
        const court_name = res.data.name;

        const court_reviews = []
        for (var key in res.data.reviews) {
          if (res.data.reviews.hasOwnProperty(key)) {
            court_reviews.push({"id": key, "data" : res.data.reviews[key]})
          }
        }

        this.setState({ court, court_name, court_reviews });
      })
  }

  render(){
    return (
      <React.Fragment>
        <Navbar/>
        <Container maxWidth="md">
        <CourtTitle court={this.state.court}/>
        <CourtGallery court={this.state.court}/>
        <CourtReviews reviews={this.state.court_reviews}/>
        </Container>
      </React.Fragment>
    );
  }
}

export default CourtProfile;
