var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 39.7088028,
      lng: -75.1188798
    },
    zoom: 8
  });
}
