$(document).ready(function(){
    // on click the buttons function can be seleted
    $('#addAnimebtn').click(function() {

         // Create the URL for the new page with the data as a query parameter
         var newPageURL = "/addanime";
         console.log(newPageURL);

         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });

    $('#addToWatchlist').click(function() {
        var inputData = $('#addToWatchlist').val();
        console.log(inputData)
        var encodedData = encodeURIComponent(inputData);
         // Create the URL for the new page with the data as a query parameter
         var newPageURL = "/watchlist/"+encodedData.toString();
         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });
    $('#editAnime').click(function() {
        var inputData = $('#editAnime').val();
        var encodedData = encodeURIComponent(inputData);

        // Create the URL for the new page with the data as a query parameter
        var newPageURL = "/editanime/" + encodedData.toString();
         console.log(newPageURL);
         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });
    $('#editProfile').click(function() {
        var inputData = $('#editProfile').val();
        var encodedData = encodeURIComponent(inputData);

        // Create the URL for the new page with the data as a query parameter
        var newPageURL = encodedData.toString()+ "/edit";
         console.log(newPageURL);
         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });
    $('#delAnime').click(function() {
        var inputData = $('#delAnime').val();
        var encodedData = encodeURIComponent(inputData);

        var xhr = $.ajax( {
        url : 'http://127.0.0.1:8000/deleteanime/'+ encodedData.toString(),
        type : 'DELETE',
        success : function ( data ) {
            var newPageURL = "/" ;
             // Open the new page with the data as a query parameter
             window.location.replace(newPageURL, "_blank");
        },
        error : function ( jqXhr, textStatus, errorMessage ) {
        $( "p" ).append( "Delete request is Fail.");
        }
        });

    });


    $('#sortNameASC').click(function() {
        var inputData = $('#sortNameASC').val();
        var encodedData = encodeURIComponent(inputData);
        var newPageURL = "/sorted_list/" + encodedData.toString()+"/ASC";

         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });
    $('#sortNameDESC').click(function() {
        var inputData = $('#sortNameDESC').val();
        var encodedData = encodeURIComponent(inputData);
        var newPageURL = "/sorted_list/" + encodedData.toString()+"/DESC";
         // Open the new page with the data as a query parameter
         window.location.replace(newPageURL, "_blank");
    });
});