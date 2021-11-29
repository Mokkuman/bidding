function myGeeks() {
    var x1 = document.getElementById('yeetCondition')
    var x2 = document.querySelector("label[for='id_currentBid'");
    var sheesh = String(x1.innerHTML);
    if(sheesh === ' bad') {
        x1.innerHTML = "malo";
    }
    if(sheesh === ' BAD') {
        x1.innerHTML = "MALO";
    }
    if(sheesh === ' good') {
        x1.innerHTML = "bueno";
    }
    if(sheesh === ' GOOD') {
        x1.innerHTML = "BUENO";
    }
    if(sheesh === ' like new') {
        x1.innerHTML = "como nuevo";
    }
    if(sheesh === ' LIKE NEW') {
        x1.innerHTML = "COMO NUEVO";
    }
    if(sheesh === ' new') {
        x1.innerHTML = "nuevo";
    }
    if(sheesh == ' NEW') {
        x1.innerHTML = "NUEVO";
    }
    x2.innerHTML = "Puja actual: "
}
myGeeks();