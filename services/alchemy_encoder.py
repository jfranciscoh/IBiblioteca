from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.exc import DetachedInstanceError
import json

"""
From StackOverFlow
"""

class AlchemyEncoder(json.JSONEncoder):
	def default(self, obj):
		fields = {}
		if isinstance(obj.__class__, DeclarativeMeta):
			for field in [x for x in dir(obj) if not x.startswith('_') and  x != 'metadata']:
				try:
					data = obj.__getattribute__(field)
					filed_type = type(getattr(obj, field))

					if filed_type is datetime:
						fields[field] = str(data.date())
					else:
						fields[field] = data
				except TypeError:
					fields[field] = None
				except DetachedInstanceError:
					""" Lazy reference loading """
					fields[field] = None

			# a json-encodable dict
			return fields
