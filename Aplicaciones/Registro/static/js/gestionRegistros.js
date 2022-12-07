(function () {
    const btnEliminiar = document.querySelectorAll(".btnEliminar")

    btnEliminiar.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Está seguro de eliminar el registro?')
            if (!confirmacion){
                e.preventDefault()
            }
        })
    })
})()

// function disable(){
//     const listaDependencias = document.getElementById('idOficina');
//     listaDependencias.addEventListener('click', (e) => {
//         let dependencias = document.getElementById('dependencias');
//         let checked = e.toElement.checked
//     })
// }

// window.onload = function (){
//     dependencias = document.forms['formularioRegistro'].elements;
//     for (var i=0; i< dependencias.length; i++){
//         if(dependencias[i].type == 'select'){
//             dependencias[i].disabled = true;
//         }
//         else {
//             console.log('hola')
//         }
//     }
// }

// window.onload = function (){
//     dependenciasSelect = document.forms['formularioRegistro'].elements['idOficina'];
//     for (i=0; i<dependenciasSelect.length; i++){
//         if (dependenciasSelect[i].value == '6'){
//             dependenciasSelect[i].disabled = true;
//         }
//     }
// }

function desactivar(){
    document.getElementById('dependencias').disabled=true;
}