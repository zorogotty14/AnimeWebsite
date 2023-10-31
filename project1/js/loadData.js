function mload() {
    // fetching the url from browsers to know which page we are currently on.
    //this will be used to display the content of the page
    var urlParams = new URLSearchParams(window.location.search);
    var data = urlParams.get("data");
    // Display the data on the new page
    // Create a flag to check if any results were found
    var resultsFound = false;
    // fetching the data from data.json to display on the site
    $.getJSON('../data/data.json', function (jsonData) {
        $.each(jsonData.category[0], function (key, value) {
            $.each(value, function (index, item) {
                if (item.name.toLowerCase().includes(data.toLowerCase())) {
                        // Create a result item and append it to the results container
                        // this will create the div cards for the content to be loaded
                        $('.detailHead').append(item.name);
                        var resultItem = $('<div>').addClass('detail_tag');
                        resultItem.append($('<h5>').text(item.name));
                        $('.detail_image').append($('<img>').attr('src', item.img));
                        resultItem.append($('<h5>').text(item.aired));
                        resultItem.append($('<h5>').text('Studios: ' + item.studios));
                        resultItem.append($('<h5>').text('desc: ' + item.description));
                        $('.detail_card').append(resultItem);
                        
                        $('.video').attr('src', item.video);
                        resultsFound = true;
                }
                
            });
        });
        // if search result is not found, it will print no result found
        if (!resultsFound) {
            $('.detail_box').remove();
            $('.video').remove();
            $('.arrivals').remove();
            $('.detailHead').append("No search result found");
        }
    });
    // Display "No Results Found" message if no results were found
    

}
// fundtion to load the recommendations on the page
function mload1(resultItem) {    
    $.getJSON('../data/data.json', function (jsonData) {
        $.each(jsonData.category[0], function (key, value) {
            if(key == resultItem){
            $.each(value, function (index, item) {
                        resultItemCard = document.createElement('div');
                        $(resultItemCard).addClass('arrivals_card');

                        resultItemImg = document.createElement('div');
                        $(resultItemImg).addClass('arrivals_image');

                        resultItemA = document.createElement('a');
                        // load the content when clicked
                        var newPageURL = "movie-detail.html?data=" + item.name;
                        $(resultItemA).addClass('img-click').attr('href', '../html/'+newPageURL);

                        resultItemImgsrc = document.createElement('img');
                        $(resultItemImgsrc).addClass('content-img').attr('src', item.img);

                        $(resultItemA).append(resultItemImgsrc);
                        $(resultItemImg).append(resultItemA);

                        resultItemTag = document.createElement('div');
                        $(resultItemTag).addClass('arrivals_tag');

                        // Create a result item and append it to the results container
                        resultItemH5name = document.createElement('h5');
                        $(resultItemH5name).text(item.name);
                        resultItemH5aired = document.createElement('h5');
                        $(resultItemH5aired).text(item.aired);
                        resultItemH5studios = document.createElement('h5');
                        $(resultItemH5studios).text('Studios: ' + item.studios);

                        resultItemTag.append(resultItemH5name);
                        resultItemTag.append(resultItemH5aired);
                        resultItemTag.append(resultItemH5studios);
                        $(resultItemCard).append(resultItemImg);
                        $(resultItemCard).append(resultItemTag);

                        resultItembtn = document.createElement('button');
                        $(resultItembtn).addClass('offer-btn').text('ADD to WATCHLIST');
                        $(resultItemCard).append(resultItembtn);

                        $('.arrivals_box').append(resultItemCard);
                        
            });
        }
        });
    });
    

}
// on window loading the js functions are getting invoked
window.addEventListener('load', function (){
    mload();
    mload1("recommendations");
});