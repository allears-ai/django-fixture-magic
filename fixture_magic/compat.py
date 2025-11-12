def get_all_related_objects(model, exclude_fields, include_related_fields):
    if include_related_fields:
        return [
            f
            for f in model._meta.get_fields()
            if (f.one_to_many or f.one_to_one)
            and f.auto_created
            and not f.concrete
            and f.name in include_related_fields
            and f.name not in exclude_fields
        ]
    return [
        f
        for f in model._meta.get_fields()
        if (f.one_to_many or f.one_to_one)
        and f.auto_created
        and not f.concrete
        and f.name not in exclude_fields
    ]
