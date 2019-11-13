import bases

def generate(data):
	pass

class Resource:
	def __init__(self, url, session, jql, fields=None, expand=None):
		self.url = url
		self.session = session
		self.jql = jql
		self.fields = fields
		self.expand = expand

		self.content = self.get_raw()

	def get_raw(self):
		items = []
		raw = self.session.get(bases.bases[0],
		params={'jql': self.jql,
			'maxResults': 1,
			'fields': '',
			'expand': ''}).json()

		futures = []
		for page in range(0, raw['total'], 100):
			futures.append(
				raw = self.session.get(bases.bases[0],
				params={'jql': self.jql,
					'maxResults': 100,
					'startAt': page,
					'fields': self.fields,
					'expand': self.expand}).json())

		for future in futures:
			response = future.result().json()
			items.extend(response['issues'])

		return items