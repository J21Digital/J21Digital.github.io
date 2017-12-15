//HTML should include <script src="http://www.myersdaily.org/joseph/javascript/md5.js"</script>
//And should include <meta charset="utf-8">
//WARNING! WHEN USING HTML INPUTS, DON'T FORGET TO SANITISE!
//Also, call this encryption method again serverside for further security.
function j2encrypt(mergeValues){
    var encodedData = "";  
    for(var i in mergeValues){
        var initValue = mergeValues[i];
        encodedData = encodedData + btoa(initValue);
    }  
    hashedData = md5(encodedData);
    return hashedData;
}   
