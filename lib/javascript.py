class libJava:
	def autocomplete(self,idkey,idres,view,minLength="2"):
		"""
			Script d'autocompletion
		"""
		s = '$("#' + idkey + '")'
		s += """.autocomplete({"""
		s += 'minLength: ' + minLength + ','
		s += 'appendTo: "#' + idres + '",'
		s += 'source: "' + view + '",'		
		s +=  """select: function( event, ui ) { 
		    		window.location.href = ui.item.url;
		    	}
		    })
			.data( "autocomplete" )._renderItem = function( ul, item ) {
				return $( "<li></li>" )
					.data( "item.autocomplete", item )
					.append(  item.label )
					.appendTo( ul );
			};"""
		s = '<script type="text/javascript">' + s + '</script>' 
		return s