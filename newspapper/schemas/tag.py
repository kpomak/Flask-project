from marshmallow_jsonapi import Schema, fields
from marshmallow import pre_load


class TagSchema(Schema):
    class Meta:
        type_ = "tag"
        self_url = "tag_detail"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "tag_list"

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)

    @pre_load
    def remove_id_before_deserializing(self, data, **kwargs):
        if id in data:
            del data["id"]
        return data
