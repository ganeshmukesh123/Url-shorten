
$('document').ready(function(){
    console.log("init");

    $(getId(URL_INPUT_ID)).on('keyup',function(){
        var url = getUrl();
        if(urlValid(url)){
            $(getClass(ENTER_BTN_CLASS)).removeClass(BTN_DISABLE_CLASS);
        }else{
            $(getClass(ENTER_BTN_CLASS)).addClass(BTN_DISABLE_CLASS); 
        }
    })

    $(getId(ENTER_BTN_ID)).on('click',function(e){
        e.preventDefault();
        var url = getUrl();
        // console.log(url);
        // makeApiRequest.endPoint;
        var formData = {
            url : url,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        };
        makeApiRequest.makeRequest(
            {
                method : 'post',
                endPoint : makeApiRequest.endPoint.createShortenUrl,
                postData : formData
            },
            function(data){
                console.log(data);
            },
            function(err){
                console.log(err);
            }
        )
    })

    function getUrl(){
        var url = $(getId(URL_INPUT_ID)).val().trim();
        return url;
    }

    function urlValid(url){
        url = url.trim();
        return !!url && url.length >= MINMUM_URL_LENGTH  && httpExist(url);
    }

    function httpExist(string) {
        string = string+"";
        return /(http(s?)):\/\//i.test(string);
    }

    function getId(id){
        return '#'+id;
    }
    function getClass(classname){
        return '.'+classname;
    }

});