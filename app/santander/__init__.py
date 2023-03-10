from app.santander.namespace import ns
from app.santander.di.bootstrap import bootstrap_di

bootstrap_di()

from app.santander.dto.santander_request_dto import santanderRequestDto
from app.santander.dto.santander_response_dto import santanderResponseDto
from app.santander.dto.santander_result_dto import santanderResultDto
from app.santander.dto.santander_record_dto import santanderRecordDto

ns.models[santanderRequestDto.name] = santanderRequestDto
ns.models[santanderResponseDto.name] = santanderResponseDto
ns.models[santanderResultDto.name] = santanderResultDto
ns.models[santanderRecordDto.name] = santanderRecordDto

