import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Hidden from '@material-ui/core/Hidden';

const useStyles = makeStyles(theme => ({
  card: {
    marginBottom: 25,
    display: 'flex',
  },
  cardDetails: {
    flex: 1,
  },
  cardMedia: {
    width: 160,
  },

}));

export default function CourtCard(props) {
  const classes = useStyles();

  return (
    <CardActionArea href={"/court/" + props.court.id}>
      <Card className={classes.card}>
        <Hidden xsDown>
          <CardMedia
            className={classes.cardMedia}
            image={props.court.data.image_urls[0] || "https://source.unsplash.com/random"}
            title="Image title"
          />
        </Hidden>
        <div className={classes.cardDetails}>
          <CardContent>
            <Typography component="h2" variant="h5">
              {props.court.data.name}
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
              {props.court.data.address}
            </Typography>
            <Typography variant="subtitle1" paragraph>
              {props.court.data.description}
            </Typography>
            <Typography variant="subtitle1" color="primary">
              Continue reading...
            </Typography>
          </CardContent>
        </div>
      </Card>
    </CardActionArea>
  );
}
