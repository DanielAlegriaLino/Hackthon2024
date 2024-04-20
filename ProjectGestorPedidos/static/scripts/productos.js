let popularidadTotal = 0;
let arrayProductos = [];
const arrayPopularidad = [];

fetch('http://127.0.0.1:8000/get_best_n_products', {
    method: 'post',
    body: JSON.stringify({
        "query": "metales"
    })
})
    .then(data => data.json())
    .then(data => {
        arrayProductos = Object.values(data)

        arrayProductos.forEach(producto => {
            popularidadTotal += Number(producto.distance);
            arrayPopularidad.push(Number(producto.distance));
        })

        arrayProductos.forEach(producto => {
            producto.popularity = Math.trunc((1 - (producto.distance / popularidadTotal)) * 100) + '%';

            insertarNuevaFila(producto);
        })        
    })
    .catch(err => console.log(err))


function softmax(arr) {
    return arr.map(function (value, index) {
        return Math.exp(value) / arr.map(function (y /*value*/) { return Math.exp(y) }).reduce(function (a, b) { return a + b })
    })
}

function insertarNuevaFila(productoObj) {
    let tablaProducto = document.getElementById('tabla-productos');
    let filaProducto = tablaProducto.insertRow(-1);

    insertarCelda(filaProducto, productoObj["name"]);
    insertarCelda(filaProducto, productoObj["description"]);
    insertarCelda(filaProducto, productoObj["popularity"]);
}

function insertarCelda(nuevaFila, producto) {
    let nuevaCelda = nuevaFila.insertCell(-1);
    nuevaCelda.textContent = producto;
}