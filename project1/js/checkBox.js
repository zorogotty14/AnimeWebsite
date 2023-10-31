$(document).ready(function(){
    // on click the check boxes can be selected only one at a time
    $('.checkoptionCategory').click(function() {
         $('.checkoptionCategory').not(this).prop('checked', false);
         const x =  $('.checkoptionCategory:checked').val();
         console.log(x);
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