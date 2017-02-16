def get_verbose(obj,field_title):
	return obj._meta.get_field(field_title).verbose_name
