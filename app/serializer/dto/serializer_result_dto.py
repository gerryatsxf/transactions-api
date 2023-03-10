from flask_restx import fields, Model
from app.serializer.dto.serialized_record_dto import serializedRecordDto
serializerResultDto = Model(
    'serializerResultDto', 
    {
        'serialized': fields.List(cls_or_instance=fields.Nested(serializedRecordDto),required=True, description='The parsed list of serialized records')
    }
)
