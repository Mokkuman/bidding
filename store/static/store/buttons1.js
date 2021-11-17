function myGeeks() {
    //alert(location)
    var x1 = document.querySelector("label[for='id_productName'");
    var x2 = document.querySelector("label[for='id_description'");
    var x3 = document.querySelector("label[for='id_category'");
    var x4 = document.querySelector("label[for='id_isActive'");
    var x5 = document.querySelector("label[for='id_image'");
    var poop = window.location.pathname;
    //alert(poop)
    if(poop == "/products/uploadStockProduct") {
        console.log("Entro");
        var x8 = document.querySelector("label[for='id_price'");
        var x9 = document.querySelector("label[for='id_inventory'");    
        x1.innerHTML = "Nombre del producto"
        x2.innerHTML = "Descripción: "
        x3.innerHTML = "Categoria: "
        x4.innerHTML = "¿Desear que se muestre el producto?"
        x5.innerHTML = "Imagen:"
        x8.innerHTML = "Precio: "
        x9.innerHTML = "Inventario: "
    } 
    if(poop == "/products/uploadBidProduct") {
        var x6 = document.querySelector("label[for='id_minBid'");
        var x7 = document.querySelector("label[for='id_condition'");
        x1.innerHTML = "Nombre del producto"
        x2.innerHTML = "Descripción: "
        x3.innerHTML = "Categoria: "
        x4.innerHTML = "¿Desear que se muestre el producto?"
        x5.innerHTML = "Imagen:"
        x6.innerHTML = "Puja mínima: "
        x7.innerHTML = "Condición del producto: "
    } 
    
    console.log(poop);
    console.log("Hello world2");
}
myGeeks();