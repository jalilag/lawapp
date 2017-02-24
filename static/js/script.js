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
				}
			}
	    });
	}
	return true;
}
// $('#search').autocomplete({
// 	source : function(requete, reponse){ // les deux arguments représentent les données nécessaires au plugin
// 		$.ajax({
// 	        url : '/gestion/ajax_search/', // on appelle le script JSON
// 	        dataType : 'json', // on spécifie bien que le type de données est en JSON
// 	        data : {
// 	            sh_txt : $('#search').val() // on donne la chaîne de caractère tapée dans le champ de recherche
// 	        },
// 	        success : function(objet){
// 	        		alert("ca marche");
// 	            	return objet.firstname + ', ' + objet.lastname; // on retourne cette forme de suggestion
// 	    		}));
// 	        }
// 	    });
// 	},
// 	minLength : 2
// });
$('#search').autocomplete({
	source: "/gestion/ajax_search/",
	minLength: 2,
	// position: {my: "center", at: "center", collision: "fit"},
	appendTo: "#autocomplete",
});
//  	var x=document.getElementsByName("delete");
//  	var res = '';
//  	j=0
// 	for (var i = 0; i < x.length; i++) {
// 		if(x[i].checked) {
// 			if (j > 0 ) {
// 				res = res + ",";
// 			}
// 			j = j + 1; 
// 			res = res + x[i].value;
// 		}
// 	}

//    	$.ajax({
//         url: '/gestion/sh_delete/',
//         data: {'res': res},
//         dataType: 'json',
//         success: function (data) {
//         	if (data.val) {
//         		alert(data.val);
//         	} else {
//         		alert("Erreur");
//         	}
//         }
//     });
// });
