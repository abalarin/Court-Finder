function initialize() {
    var defaultBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(39.7098595, -75.1211365)
    );

    var input = document.getElementById('address-input');
    var options = {
         bounds: defaultBounds,
         types: ['geocode']
    };

    autocomplete = new google.maps.places.Autocomplete(input, options);
    autocomplete.setFields(['geometry']);

    autocomplete.addListener('place_changed', fillInAddress);

}
function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  if(!place.geometry) {
    window.alert("No details available for input: '" + place.name + "'");
    return;
  }
  var lat = place.geometry.location.lat();
  var lon = place.geometry.location.lng();
  document.getElementById('lat').value = lat;
  document.getElementById('lng').value = lon;
}


// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle(
          {center: geolocation, radius: position.coords.accuracy});
      autocomplete.setBounds(circle.getBounds());
    });
  }
}

