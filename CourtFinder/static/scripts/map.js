var map;

function initMap(courts) {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 39.7088028,
      lng: -75.1188798
    },
    zoom: 12
  });
  var i;
  for(var key in courts){
    marker = new google.maps.Marker({
      position: courts[key].latlng,
      map: map,
      title: ("Pin" + i)
    });
    marker.setMap(map);
  }
}
