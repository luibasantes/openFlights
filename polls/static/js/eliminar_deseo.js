$(document).ready(function(){
    cargar();

    $('#myTable').DataTable( {
		
    } );



});

function cargar(){

    $.get( "http://127.0.0.1:8000/api/lista_deseos/", function( data ) {

        for( i=0; i<data.length;i++){
            $trow= $("<tr></tr>")
            $trow.append("<td>"+data[i].nombres+"</td>");
            $trow.append("<td>"+data[i].celular+"</td>");
            $trow.append("<td>"+data[i].f_partida+"</td>");
            $trow.append("<td>"+data[i].f_retorno+"</td>");
            $trow.append("<td>"+data[i].ciudad_partida+"</td>");
            $trow.append("<td>"+data[i].ciudad_llegada+"</td>");
            if(data[i].escala){
                $trow.append("<td><input type= 'checkbox' class='escala' checked></input></td>");
            }else{
                $trow.append("<td><input type= 'checkbox' class='escala' ></input></td>");
            }
			$button=$("<td><button class='eraseButton', type='button'>eliminar</button></td>");
			$trow.append($button);
            $("#cuerpo").append($trow);
        }
		
		$(".eraseButton").click(function(){
				$tr=$(this).parent().parent()
				$td_name=$(this).parent().parent().children()
				var user_name= $td_name.html()
				$.ajax({
					url: "http://127.0.0.1:8000/api/borrar_deseo/" + user_name,
					type: 'DELETE',
					success: function(result) {
						alert("GIFT DELETED")
						$tr.remove()
					}
				});
				
		});
    });
}