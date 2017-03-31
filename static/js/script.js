function check_del(model_name,app_name) {
	// Fonction requete json de vérification de suppression
 	var x=document.getElementsByName("delete");
 	var res = '';
 	var j = 0;
 	var ans = 1;
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
	        url: '/ajax_list_delete/',
	        data: {'res': res,'model_name':model_name,'app_name':app_name},
	        dataType: 'json',
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
				    } else {
				    	$('#form_delete').submit();
				    }
				}
			}
	    });
	}
}

function quick_connect() {
	login = document.getElementById("c_login").value;
	password = document.getElementById("c_password").value;
	if (login.length > 0 && password.length > 0) { 
	   	$.ajax({
	        url: '/gestion/ajax_member_connect/',
	        data: {'login': login, 'password': password},
	        dataType: 'json',
	        success: function (data) {
	        	if (!data.error) {
	        		if (data.url != "none") {
	        			window.location.href = data.url;
	        		} else {
		        		window.location.reload();
	        		}
	        	} else {	        		
	        		$("#c_connection_error").remove();
	        		$("#c_connection_table").append(data.error);
	        	}
	        }
		});
	}
}

$("#c_login").mouseenter(function() {
	if ($("#c_login").val() == "Login") {
		$("#c_login").val("");
	}
});
$("#c_login").mouseleave(function() {
	if ($("#c_login").val() == "") {
		$("#c_login").val("Login");
	}
});
$("#c_password").mouseenter(function() {
	if ($("#c_password").val() == "*****") {
		$("#c_password").val("");
	}
});
$("#c_password").mouseleave(function() {
	if ($("#c_password").val() == "") {
		$("#c_password").val("*****");
	}
});

// $("#search")
//     .autocomplete({
// 		minLength: 2,
// 		appendTo: "#autocomplete",
// 		source: "/gestion/ajax_search/",
//         select: function( event, ui ) { 
//     		window.location.href = ui.item.url;
//     	}
//     })
// 	.data( "autocomplete" )._renderItem = function( ul, item ) {
// 		return $( "<li></li>" )
// 			.data( "item.autocomplete", item )
// 			.append(  item.label )
// 			.appendTo( ul );
// 	};