from django_filters import filters


def ArrayFilter(filter):
    class ArrayFilter(filters.BaseCSVFilter, filter):
        pass
    return ArrayFilter
