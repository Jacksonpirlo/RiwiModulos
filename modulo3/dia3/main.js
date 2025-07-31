let enviar = document.getElementById('enviar');
let lista_notas = [];
let notasTotal = 0;
let cambios = document.getElementById('cambios')

enviar.addEventListener('click', (e) => {
    let notas = parseFloat(document.getElementById('notas').value);
    let apruebaOnO = document.getElementById('apruebaOnO')
    lista_notas.push(notas);
    notasTotal += notas;
    let total = notasTotal / lista_notas.length

    console.log(lista_notas);
    let notasTotal = 0;
    console.log(notasTotal);

    console.log(total)

    cambios.addEventListener('click', (e) => {
    let promedio = document.getElementById('promedio');
    promedio.innerHTML = total

    if (total >= 3) {
        apruebaOnO.innerHTML = 'Aprobaste'
    } else {
        apruebaOnO.innerHTML = 'Reprobaste'
        console.log(promedio.value)
    } 
})

});