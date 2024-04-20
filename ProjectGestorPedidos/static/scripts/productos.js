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

        graficar();
    })
    .catch(err => console.log(err))

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

function graficar() {
    const xValues = ["Alambre recocido", "Arena a granel", "Cemento gris", "Pala cuadrada", "Carretilla 4.5 Ft3"];
    const yValues = [81, 80, 79, 79, 78, 75];

    new Chart("myChart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: "green",
                data: yValues
            }]
        },
        options: {
            legend: {display: false},
            title: {
              display: true,
              text: "Productos"
            }
        }
    });
}