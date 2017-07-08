var map;
function initMap(){
    var kamoorcorner = {lat: 26.174498, lng: 91.765068};
    var map = new google.maps.Map(document.getElementById('map'), {
          center: kamoorcorner,
          zoom: 10
        });
    var marker = new google.maps.Marker({
          position: kamoorcorner,
          map: map
        });
}
