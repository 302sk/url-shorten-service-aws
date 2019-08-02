import json
#Just return the web page of the url shorten service
def lambda_handler(event, context):
    html = '''<html>
    <head>
            <script
            src="https://code.jquery.com/jquery-3.4.1.min.js"
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
            crossorigin="anonymous"></script>
    </head>
    <body>
        <p>Target URL:</p><textarea rows="5" cols="100" id="long-url"></textarea>
        <button onclick="shortenUrl()">Shorten</button><br>
        <p>Shortend URL:</p>
        <textarea rows="2" cols="100" id="short-url"></textarea>

        <script>
            var shortenUrl = function(){
                var longUrl = $("#long-url").val();
                var settings = {
                    "async": true,
                    "crossDomain": true,
                    "url": "https://rqw25xitul.execute-api.us-east-2.amazonaws.com/default/shorten",
                    "method": "POST",
                    "headers": {
                        "x-api-key": "RQT9BoC1BX8DmgfLKvdvf5iCaxjURBLz1wyXWKbL",
                        "Content-Type": "application/json",
                        "cache-control": "no-cache"
                    },
                    "processData": false,
                    "data": "{\\\"long_url\\\":\\\"" + longUrl + "\\\"}"
                    }

                    $.ajax(settings).always(function (data, textStatus, jqXHR) {
                        $("#short-url").val(data.responseText);

                        console.log(data);
                    });
            }
        </script>
    </body>
</html>
    '''

    return html

