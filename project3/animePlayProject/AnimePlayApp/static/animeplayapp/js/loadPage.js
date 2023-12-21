// function to load the content from json
function mload(resultItem) {    
        $.each(json.category[0], function (key, value) {
            if(key == resultItem){
            $.each(value, function (index, item) {
                // creating the div cards
                        var resultItemCard = document.createElement('div');
                        $(resultItemCard).addClass('arrivals_card');

                        var resultItemImg = document.createElement('div');
                        $(resultItemImg).addClass('arrivals_image');

                        var resultItemA = document.createElement('a');
                        // load the content when clicked
                        var newPageURL = "movie-detail.html?data=" + item.name;
                        $(resultItemA).addClass('img-click').attr('href', '../html/'+newPageURL);

                        var resultItemImgsrc = document.createElement('img');
                        $(resultItemImgsrc).addClass('content-img').attr('src', item.img);

                        $(resultItemA).append(resultItemImgsrc);
                        $(resultItemImg).append(resultItemA);

                        var resultItemTag = document.createElement('div');
                        $(resultItemTag).addClass('arrivals_tag');

                        // Create a result item and append it to the results container
                        var resultItemH5name = document.createElement('h5');
                        $(resultItemH5name).text(item.name);
                        var resultItemH5aired = document.createElement('h5');
                        $(resultItemH5aired).text(item.aired);
                        var resultItemH5studios = document.createElement('h5');
                        $(resultItemH5studios).text('Studios: ' + item.studios);

                        resultItemTag.append(resultItemH5name);
                        resultItemTag.append(resultItemH5aired);
                        resultItemTag.append(resultItemH5studios);
                        $(resultItemCard).append(resultItemImg);
                        $(resultItemCard).append(resultItemTag);

                        var resultItembtn = document.createElement('button');
                        $(resultItembtn).addClass('offer-btn').text('ADD to WATCHLIST');
                        $(resultItemCard).append(resultItembtn);

                        $('.arrivals_box').append(resultItemCard);
                        
            });
        }
        });
    

}
// get the url from the website, to load the content of the index page
var content= window.location.pathname;
const myArray = content.split("/");
const result = myArray[myArray.length -1].split(".");
// spliting the url and storing the desired value
var resultItem = result[0];
// checking if result is watchlist, we ned to load the recommendations
if(resultItem == 'watchlist'){
    resultItem="recommendations";
}
window.addEventListener('load', function (){
    mload(resultItem);
});
