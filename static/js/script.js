 // Get the section-2 element
 var section2 = document.querySelector('.section-2');

 // Function to check if section is in view
 function isScrolledIntoView(el) {
   var rect = el.getBoundingClientRect();
   var elemTop = rect.top;
   var elemBottom = rect.bottom;

   // Only check for the top part of the section to be in view
   var isVisible = (elemTop >= 0) && (elemTop <= window.innerHeight);
   return isVisible;
 }

 // Add scroll event listener
 window.addEventListener('scroll', function() {
   if (isScrolledIntoView(section2)) {
     // If section-2 is in view, set opacity to 1
     section2.style.opacity = 1;
   }
 });

//  sidebar javascript
function toggleDropdown() {
  var dropdown = document.getElementById("myDropdown");
  if (dropdown.style.display === "block") {
    dropdown.style.display = "none";
  } else {
    dropdown.style.display = "block";
  }
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.style.display === "block") {
        openDropdown.style.display = "none";
      }
    }
  }
}



