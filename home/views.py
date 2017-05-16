from django.shortcuts import render
from lib.html import libHtml


# Create your views here.

def home(request):

	content = """<div class="icotest2"><ul>
  <li><a href="#"><img class="ico ico1"><p>qdqs</p></a></li>
  <li><a href="#"><img class="ico ico2"><p>qdqs</p></a></li>
  <li><a href="#"><img class="ico ico1"><p>qdqs</p></a></li>
  <li><a href="#"><img class="ico ico1"><p>qdqs</p></a></li>
  <li><a href="#"><img class="ico ico2"><p>qdqs</p></a></li>
  <li><a href="#"><img class="ico ico1"><p>wwwwwwwqdqs</p></a></li>
  </ul></div>"""

	s = libHtml()
	content = s.section('Création de membre',content,"stdsection")
	content = s.container(content,'div','col-md-6 col-md-offset-1')
	return render(request, 'gestion/template/form.html', locals())

