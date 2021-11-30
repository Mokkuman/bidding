function myGeeks() {
    var x1 = document.querySelector("label[for='id_productName'");
    var x2 = document.querySelector("label[for='id_description'");
    var x3 = document.querySelector("label[for='id_category'");
    var x4 = document.querySelector("label[for='id_price'");
    var x5 = document.querySelector("label[for='id_isActive");
    var x6 = document.querySelector("label[for='inventory'");
    x1.innerHTML = "Nombre del producto: ";
    x2.innerHTML = "Descripción: ";
    x3.innerHTML = "Categoría: ";
    x4.innerHTML = "Precio: ";
    x5.innerHTML = "Activo: ";
    x6.innerHTML = "Inventario: ";
}
myGeeks();