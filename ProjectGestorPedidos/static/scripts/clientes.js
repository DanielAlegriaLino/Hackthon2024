const arrScore = [];

const cliente = {
    "name": "Juan",
    "email": "juan@gmail.com",
    "phone": "442940249",
    "shopping": 0,
    "mensajes": [
        {
            "query": "me interesan mucho sus productos",
            "date": 1708473620
        },
        {
            "query": "hola, no he podido comprarles pero lo hare",
            "date": 1710979220
        },
        {
            "query": "tengo varias dudas antes de comprar",
            "date": 1713657620
        },
        {
            "query": "perdon ya no me interesa",
            "date": 1713636420
        }
    ]
}

async function obtenerScore() {
    for (const mensaje of cliente.mensajes) {
        fetch('http://127.0.0.1:8000/get_user_score', {
            method: 'post',
            body: JSON.stringify({
                "query": mensaje.query
            })
        })
            .then(data => data.json())
            .then(data => {
                arrScore.push(data.score);
            })
            .catch(err => console.log(err))
    }
}

(async function () {
    try {
        await obtenerScore();

        const arrayScore = [9, 10, 7, 3];

        cliente.mensajes.forEach((mensaje, index) => {
            mensaje.score = arrayScore[index];
        })

        let scoreTotal = 0;
        arrayScore.forEach(score => {
            scoreTotal += score;
        })

        scoreTotal = scoreTotal / arrayScore.length;

        cliente.score = scoreTotal;

        let tablaClientes = document.getElementById('tabla-clientes');
        let nuevaFila = tablaClientes.insertRow(-1);
        let nuevaCelda = nuevaFila.insertCell(-1);
        nuevaCelda.textContent = cliente.name;

        nuevaCelda = nuevaFila.insertCell(-1);
        nuevaCelda.textContent = cliente.email;

        nuevaCelda = nuevaFila.insertCell(-1);
        nuevaCelda.textContent = cliente.shopping;

        nuevaCelda = nuevaFila.insertCell(-1);
        nuevaCelda.textContent = cliente.score;

        // document.getElementById('correo').textContent = cliente.email;
        // document.getElementById('numero').textContent = cliente.phone;
        // document.getElementById('compras').textContent = `${cliente.shopping} compras`;

        cliente.mensajes.forEach(mensaje => {
            insertarNuevaFila(mensaje, 'tabla-adicional')
        })

        graficar(arrayScore);
    } catch (err) {
        console.log(err)
    }
})();

function insertarNuevaFila(objeto) {
    let tabla = document.getElementById('tabla-adicionales');
    let fila = tabla.insertRow(-1);

    let fechaMensaje = new Date(objeto["date"]);

    insertarCelda(fila, objeto["query"]);
    insertarCelda(fila, `${fechaMensaje.getDay()}/${fechaMensaje.getMonth()}/${fechaMensaje.getFullYear()}`);
    insertarCelda(fila, objeto["score"]);
}

function insertarCelda(nuevaFila, producto) {
    let nuevaCelda = nuevaFila.insertCell(-1);
    nuevaCelda.textContent = producto;
}


function graficar(data) {

    const xValues = [1, 2, 3, 4];

    new Chart("myChart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                data: data,
                borderColor: "green",
                fill: false
            }]
        },
        options: {
            legend: { display: false }
        }
    });
}