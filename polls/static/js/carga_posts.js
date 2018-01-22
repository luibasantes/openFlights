/*$(document).ready(function(){
    cargar();

    $('#myTable').DataTable( {

    } );



});*/


$.ajax({
    'url': "http://127.0.0.1:8000/api/lista_deseos/",
    'method': "GET",
    'contentType': 'application/json'
}).done( function(data) {
    $('#myTable').dataTable( {
        "language": {
            "lengthMenu": "Mostrando _MENU_ registros por pagina",
            "zeroRecords": "No pudimos encontrar registros. Lo sentimos",
            "info": "Mostrando pagina  _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros",
            "deferLoading": 0,
            "infoFiltered": "(filtrado desde _MAX_ el total de registros)",
            "paginate": {
                "first":      "Primero",
                "last":       "Ultimo",
                "next":       "Siguiente",
                "previous":   "Anterior"
            }
        },
        "aaData": data,
        "columns": [
            { "data": "nombres" },
            { "data": "celular" },
            { "data": "f_partida" },
            { "data": "f_retorno" },
            { "data": "ciudad_partida" },
            { "data": "ciudad_llegada" },
            { "data": "escala" }
        ]
    })
});

function cargar(){

    $.get( "http://127.0.0.1:8000/api/lista_deseos/", function( data ) {

        for( i=0; i<data.length;i++){

            $("#cuerpo").append("<tr>");
            $("#cuerpo").append("<td>"+data[i].nombres+"</td>");
            $("#cuerpo").append("<td>"+data[i].celular+"</td>");
            $("#cuerpo").append("<td>"+data[i].f_partida+"</td>");
            $("#cuerpo").append("<td>"+data[i].f_retorno+"</td>");
            $("#cuerpo").append("<td>"+data[i].ciudad_partida+"</td>");
            $("#cuerpo").append("<td>"+data[i].ciudad_llegada+"</td>");
            if(data[i].escala){
                $("#cuerpo").append("<td><input type= 'checkbox' class='escala' checked></input></td>");
            }else{
                $("#cuerpo").append("<td><input type= 'checkbox' class='escala' ></input></td>");
            }
            $("#cuerpo").append("</tr>");
        }
    });
}