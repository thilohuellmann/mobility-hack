M.AutoInit();

var inputs = document.getElementsByClassName('query');

var options = {
  types: ['(cities)'],
};

var autocompletes = [];

for (var i = 0; i < inputs.length; i++) {
  var autocomplete = new google.maps.places.Autocomplete(inputs[i], options);
  autocomplete.inputId = inputs[i].id;
  autocomplete.addListener('place_changed', fillIn);
  autocompletes.push(autocomplete);
}

function fillIn() {
  // console.log(this.inputId);
  var place = this.getPlace();

  var lat = place.geometry.location.lat();
  var lng = place.geometry.location.lng();

  if (this.inputId == 'start_location') {
    console.log('start')
    $('#start_lat').val(lat);
    $('#start_lng').val(lng);
  }

  if (this.inputId == 'end_location') {
    $('#end_lat').val(lat);
    $('#end_lng').val(lng);
  }

  if (this.inputId == 'home_location') {
    $('#home_lat').val(lat);
    $('#home_lng').val(lng);
  }



}
