function myGeeks() {
    var x1 = document.querySelector("label[for='id_city'");
    var x2 = document.querySelector("label[for='id_firstName'");
    var x3 = document.querySelector("label[for='id_lastName'");
    var x4 = document.querySelector("label[for='id_state'");
    var x5 = document.querySelector("label[for='id_password1'");
    var x6 = document.querySelector("label[for='id_password2'");
    x1.innerHTML = "Ciudad"
    x2.innerHTML = "Nombre"
    x3.innerHTML = "Apellido"
    x4.innerHTML = "Estado"
    x5.innerHTML = "Contraseña"
    x6.innerHTML = "Confirmar Contraseña"
    console.log("Hello world2");

    //Second
    var arr = document.getElementById("hint_id_password2");
    let msg = "Ingresa la contraseña nuevamente, por favor";
    arr.innerHTML = msg;

    //Third
    var li = document.querySelector("#hint_id_password1 ul");

    
    li.childNodes[0].childNodes[0].nodeValue = "Tu contraseña no puede ser similar a tu informacion personal";
    li.childNodes[1].childNodes[0].nodeValue = "Tu contraseña debe tener al menos 8 caracteres";
    li.childNodes[2].childNodes[0].nodeValue = "Tu contraseña no puede ser generica";
    li.childNodes[3].childNodes[0].nodeValue = "Tu contraseña debe tener numeros y letras";

    /*
    Tu contraseña no puede ser similar a tu informacion personal
    Tu contraseña debe tener al menos 8 caracteres
    Tu contraseña no puede ser generica
    Tu contraseña debe tener numeros y letras

    */
}
myGeeks();
