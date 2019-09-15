import axios from 'axios';
import React from 'react';
import Container from '@material-ui/core/Container';

import CourtCard from '../components/CourtCard'
import Navbar from '../components/Navbars/NavBar'

function DisplayCourts(props) {
  if(props.courts){
    return (
      props.courts.map(court =>(
        <CourtCard key={court.id} court={court}/>
      ))
    );
  }
  else {
    return(
      <div>
      Loading...
      </div>
    )
  }
}
class CourtsPage extends React.Component {
  state = {
    courts: []
  }

  componentDidMount() {
    axios.get(`https://api.findthecourt.com/courts`)
      .then(res => {
        const courts = [];
        for (var key in res.data) {
          if (res.data.hasOwnProperty(key)) {
            courts.push({"id": key, "data" : res.data[key]})
          }
        }
        this.setState({ courts });
      })
  }

  render(){
    return (
      <React.Fragment>
        <Navbar/>
        <Container maxWidth="md">
        <DisplayCourts courts={this.state.courts} />
        </Container>
      </React.Fragment>
    );
  }
}

export default CourtsPage;
