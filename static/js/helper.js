var makeApiRequest = (function(){
    var endPoint = {
        createShortenUrl : '/create'
    }
    var makeRequest = function(data,callback,handleError){
        var {method,endPoint,postData} = data;
        if (method === "get") {
            $.ajax({
                url: endPoint,
                type: "GET",
                success: function(results) {
                    console.log(results);
                    callback(results);
                },
                error: function(err) {
                    handleError(err);
                }
            });
        } else if (method == "post") {
            $.ajax({
                url: endPoint,
                type: "POST",
                data: postData,
                success: function(results) {
                    console.log(results);
                    callback(results);
                },
                error: function(err) {
                    console.log(err);
                    handleError(err);
                }
            });
        }
    }

    return {
        endPoint : endPoint,
        makeRequest : makeRequest
    }
})();