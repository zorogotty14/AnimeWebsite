function mload() {    
    // reading the data.json
    
        $.each(json.category[0], function (key, value) {
            // creating h1 tag to be added as category and adding class
            resultItemH1name = document.createElement('h1');
            $(resultItemH1name).addClass("home-h1");
            $(resultItemH1name).text(key);
            // adding the h1 tag to div
            $('.arrivals').append(resultItemH1name);
            //creating the div box for all the div cards and adding class
            resultItembox = document.createElement('div');
            $(resultItembox).addClass('arrivals_box');

            $.each(value, function (index, item) {
                        //creating each div card and adding class 
                        
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

                        $(resultItembox).append(resultItemCard);
                        
                        
            });
            $('.arrivals').append(resultItembox);
            
            
        });
    

}
// get the url from the website, to load the content of the index page
var content= window.location.pathname;
const myArray = content.split("/");
const result = myArray[myArray.length -1].split(".");
// spliting the url and storing the desired value
var resultItem = result[0];
// checking if the result is index
if(resultItem == 'index'){
    window.addEventListener('load', function (){
        mload();
    });
}
