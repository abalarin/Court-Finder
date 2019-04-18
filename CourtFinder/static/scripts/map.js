var map;

function initMap(coords) {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 39.7088028,
      lng: -75.1188798
    },
    zoom: 8
  });
    var myLatLng = [{lat: 39.7050303, lng: -75.0995315}, {lat: 39.7148264, lng: -75.1314857}, {lat: 39.699367, lng: -75.1161549}, {lat: 39.7256851, lng: -75.1172171}];
    var marker, i;
        for(i = 0; i < myLatLng.length; i++) {
            marker = new google.maps.Marker({
                position: myLatLng[i],
                map: map,
                title: ("Pin" + i)
            });
            marker.setMap(map);
        }
}
