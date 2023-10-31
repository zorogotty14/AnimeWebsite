$(document).ready(function(){
    // on click the check boxes can be selected only one at a time
    $('.checkoptionCategory').click(function() {
         $('.checkoptionCategory').not(this).prop('checked', false);
         const x =  $('.checkoptionCategory:checked').val();
         var encodedData = encodeURIComponent(x);
         
         // Create the URL for the new page with the data as a query parameter
         var newPageURL = "/" + encodedData;
         console.log(newPageURL);
         
         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });

    $('.checkoptionFormat').click(function() {
        $('.checkoptionFormat').not(this).prop('checked', false);
        const y =  $('.checkoptionCategory:checked').val();
   });
    // when clear button is clicked it will clear the checked boxes 
   $('.clear').click(function (e) { 
    $('.checkoptionCategory').prop('checked', false);
    $('.checkoptionFormat').prop('checked', false);
   });
});