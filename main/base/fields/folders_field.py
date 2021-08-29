from main.base.fields.enpass_field import EnpassField


class GroupingField(EnpassField):
    enpass_field_name = "folders"
    lastpass_field_name = "grouping"

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
    def get_parsed_value(cls, input_value,enpass_folders_json_array) -> str:

        default_path = "EnpassImport"
        if cls.enpass_field_name in input_value.keys():
            folder_json_array = list(filter(lambda x:x["uuid"]==input_value[cls.enpass_field_name][0],enpass_folders_json_array))
            folder_name = "%s\%s" % (default_path, folder_json_array[0]['title'])
        return folder_name if cls.enpass_field_name in input_value else default_path

    @classmethod
    def is_applicable(cls, input_value) -> bool:
        return cls.enpass_field_name in input_value
