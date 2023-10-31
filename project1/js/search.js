// Function to search and display results
function searchOnePiece(searchTerm, jsonData) {
    var inputData = searchTerm.toLowerCase();
    var encodedData = encodeURIComponent(inputData);
    
    // Create the URL for the new page with the data as a query parameter
    var newPageURL = "movie-detail.html?data=" + encodedData;
    
    // Open the new page with the data as a query parameter
    window.location.replace(newPageURL, "_blank");


}
// Event listener for search button click
$('#searchButton').on('click', function () {
    var searchTerm = $('#searchInput').val();
    $.getJSON('../data/data.json', function (jsonData) {
        searchOnePiece(searchTerm, jsonData);
    });
});
