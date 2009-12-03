#    This file is part of django-doubleoptin-contactform.

#    django-doubleoptin-contactform is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    django-doubleoptin-contactform is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.

#    You should have received a copy of the GNU Lesser General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template import RequestContext

from doptincf.models import ContactRequest
from doptincf.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = form.save(commit=False)

            #put a bit user agent information into the mail
            contact_request.question += '\n\n- - - - - - - - - - - - - - - - - - - - - - - -\n\n' + request.META['HTTP_USER_AGENT'] 
            contact_request.save() 
            
            #build the verify link that will be submitted to the user
            link = settings.WEB_URL+'contact/'+str(contact_request.pk)+'/verify/'
            
            subject = settings.DOPTINCF_MAIL_SUBJECT

            #standard messagetext of verification mail
            message = 'To proceed your contactrequest please visit the following link \n\n' + link

            #send the mail
            send_mail(subject, message, settings.DOPTINCF_MAIL_FROM,[contact_request.email], fail_silently=False)
            #redirect to the successpage
            return HttpResponseRedirect('./received/')

    else:
        form = ContactForm()
   	
	return render_to_response('contact/contact.html', {'form': form}, context_instance=RequestContext(request))


def verify(request, contact_id):
	contact_request = get_object_or_404(ContactRequest, pk=contact_id)
	contact_request.verification = True
	contact_request.save()

    #send mail to the users who are listed in the settings.py (DOPTINCF_MAIL_TO)
	send_mail('Contactrequest: '+contact_request.subject, contact_request.question, contact_request.email, settings.DOPTINCF_MAIL_TO, fail_silently=False)
	return render_to_response('contact/verified.html', context_instance=RequestContext(request))
	
