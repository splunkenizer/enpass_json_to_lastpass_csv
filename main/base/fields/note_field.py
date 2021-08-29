from main.base.fields.enpass_field import EnpassField


class NoteField(EnpassField):
    enpass_field_name = "note"
    lastpass_field_name = "extra"

    def __init__(self, value) -> None:
        self.field_value = value

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.field_value == other.field_value

    @classmethod
    def get_lastpass_field_name(cls):
        return cls.lastpass_field_name

    @classmethod
    def get_enpass_field_name(cls) -> str:
        return cls.enpass_field_name

    @classmethod
    def get_parsed_value(cls, input_value) -> str:

        return ("%s\n" % input_value[cls.enpass_field_name]) if cls.enpass_field_name in input_value else ""

    @classmethod
    def is_applicable(cls, input_value) -> bool:
        return cls.enpass_field_name in input_value
