function check_del() {
	// Fonction requete json de vérification de suppression
 	var x=document.getElementsByName("delete");
 	var res = '';
 	var j = 0;
	for (var i = 0; i < x.length; i++) {
		if(x[i].checked) {
			if (j > 0 ) {
				res = res + ",";
			}
			j = j + 1; 
			res = res + x[i].value;
		}
	}
	if (j > 0) {
	   	$.ajax({
	        url: '/gestion/ajax_member_list_delete/',
	        data: {'res': res},
	        dataType: 'json',
	        async: false,
	        success: function (data) {
	        	if (data.val) {
	    			var rep = confirm("Souhaitez vraiment supprimer les éléments selectionnés ?\n" + data.val);	
					if (!rep) {
					 	var x=document.getElementsByName("delete");
						for (var i = 0; i < x.length; i++) {
							if(x[i].checked) {
								x[i].checked = false;
							} 
				        }
				    }
				}.
			}
	    });
	}
	return true;
}

$("#search")
    .autocomplete({
		minLength: 2,
		appendTo: "#autocomplete",
		source: "/gestion/ajax_search/",
        select: function( event, ui ) { 
    		window.location.href = ui.item.url;
    	}
    })
	.data( "autocomplete" )._renderItem = function( ul, item ) {
		return $( "<li></li>" )
			.data( "item.autocomplete", item )
			.append(  item.label )
			.appendTo( ul );
	};