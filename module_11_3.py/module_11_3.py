def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj,"attr",[method]))]
    module = obj.__class__.__module__
    info = {"type": obj_type,"attributes": attributes,"methods": methods,"module": module,"name":__name__}
    return info
number_info = introspection_info(42)
print(number_info)







