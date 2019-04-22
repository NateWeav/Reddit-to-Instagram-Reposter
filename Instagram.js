var instagram_username = "YOUR IG USERNAME"
var instagram_password = "YOUR IG PASSWORD"



var Client = require('instagram-private-api').V1;
var device = new Client.Device(instagram_username);
var storage = new Client.CookieFileStorage(__dirname + '/cookies/'+instagram_username+'.json');
var fs = require('fs');
var text = fs.readFileSync('Memory/Caption.txt','utf8');
var text2 = fs.readFileSync('Memory/Caption2.txt','utf8');
var caption = text+text2

// And go for login
Client.Session.create(device, storage, instagram_username, instagram_password)
	.then(function(session) {
        Client.Upload.photo(session, './'+text+'.jpg')
	    .then(function(upload) {
	        // upload instanceof Client.Upload
	        // nothing more than just keeping upload id
	        //console.log(upload.params.uploadId);
	        return Client.Media.configurePhoto(session, upload.params.uploadId, caption);
	    })
	    .then(function(medium) {
	        // we configure medium, it is now visible with caption
	        //console.log(medium.params)
			console.log("It is posted on instagram")
	    })
	})
