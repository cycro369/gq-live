
                                                                                                                                                                                                                                          
function myFunction() {
  var x = document.getElementById("myDIV");


                                                                                                                                                                                                                          
  if (x.style.display === "none") {                                                                                                                                                                                                                                               
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function toggleButton(ref,registerbtn){
    document.getElementById(registerbtn).disabled= ((ref.value !== ref.defaultValue) ? false : true);
}

function numberOnly(ref,registerbtn) {
  e = (e) ? e : window.event;
var clipboardData = e.clipboardData ? e.clipboardData : window.clipboardData;
var key = e.keyCode ? e.keyCode : e.which ? e.which : e.charCode;
var str = (e.type && e.type == "paste") ? clipboardData.getData('Text') : String.fromCharCode(key);

return (/^\d+$/.test(str));
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
  modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


