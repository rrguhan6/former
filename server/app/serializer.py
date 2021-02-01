from app import ma

class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "Book", "Author")


class FormSchema(ma.Schema):
    class Meta:
        fields = ("id", "form_schema")
