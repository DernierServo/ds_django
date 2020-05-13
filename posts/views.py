"""Posts views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
	{
		'name': 'Escribiendo Pensamientos',
		'user': 'kpaiva',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://i.picsum.photos/id/4/200/300.jpg?grayscale',
	},
	{
		'name': 'Perrito cochino',
		'user': 'dservo',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://i.picsum.photos/id/237/200/300.jpg',
	},
	{
		'name': 'Nieve en las rocas',
		'user': 'jperezoso',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://i.picsum.photos/id/866/200/300.jpg',
	},	
]

def list_posts(requests):
	"""List existing posts."""
	content = []
	for post in posts:
		content.append("""
			<p><strong>{name}</strong></p>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}"/></figure>
		""".format(**post))

	return HttpResponse('<br>'.join(content))