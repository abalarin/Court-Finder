function myMap() {

  var mapProp = {
    center:new google.maps.LatLng({{Court.latitude}},{{Court.longitude}}),
    zoom:14,
  };
  var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
  var marker = new google.maps.Marker({
    map: map,
    position: new google.maps.LatLng({{Court.latitude}},{{Court.longitude}}),
    map: map,
    title:"Hello World!"
  });
  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
  var contentString =
    '<div id="content">'+
    '<h1 id="firstHeading" class="firstHeading">{{Court.name}}</h1>'+
    '</div>';

  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });
}
