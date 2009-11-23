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

urlpatterns = patterns(
    (r'^$', 'aceton.contact.views.contact'),
    (r'^received/$', direct_to_template, {'template': 'contact/received.html'}),
    (r'^(?P<contact_id>\d+)/verify/$', 'aceton.contact.views.verify'),
    (r'^received/$', direct_to_template, {'template': 'contact/verified.html'}),
)

