# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2
from injective.tokenfactory.v1beta1 import genesis_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_genesis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*injective/tokenfactory/v1beta1/query.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a+injective/tokenfactory/v1beta1/params.proto\x1a,injective/tokenfactory/v1beta1/genesis.proto\"\x14\n\x12QueryParamsRequest\"S\n\x13QueryParamsResponse\x12<\n\x06params\x18\x01 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"p\n\"QueryDenomAuthorityMetadataRequest\x12!\n\x07\x63reator\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"\x12\'\n\tsub_denom\x18\x02 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"sub_denom\"\"\x9c\x01\n#QueryDenomAuthorityMetadataResponse\x12u\n\x12\x61uthority_metadata\x18\x01 \x01(\x0b\x32\x36.injective.tokenfactory.v1beta1.DenomAuthorityMetadataB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"authority_metadata\"\"D\n\x1dQueryDenomsFromCreatorRequest\x12#\n\x07\x63reator\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"creator\"\"C\n\x1eQueryDenomsFromCreatorResponse\x12!\n\x06\x64\x65noms\x18\x01 \x03(\tB\x11\xf2\xde\x1f\ryaml:\"denoms\"\"\x19\n\x17QueryModuleStateRequest\"W\n\x18QueryModuleStateResponse\x12;\n\x05state\x18\x01 \x01(\x0b\x32,.injective.tokenfactory.v1beta1.GenesisState2\xc9\x06\n\x05Query\x12\xa1\x01\n\x06Params\x12\x32.injective.tokenfactory.v1beta1.QueryParamsRequest\x1a\x33.injective.tokenfactory.v1beta1.QueryParamsResponse\".\x82\xd3\xe4\x93\x02(\x12&/injective/tokenfactory/v1beta1/params\x12\xfa\x01\n\x16\x44\x65nomAuthorityMetadata\x12\x42.injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataRequest\x1a\x43.injective.tokenfactory.v1beta1.QueryDenomAuthorityMetadataResponse\"W\x82\xd3\xe4\x93\x02Q\x12O/injective/tokenfactory/v1beta1/denoms/{creator}/{sub_denom}/authority_metadata\x12\xd9\x01\n\x11\x44\x65nomsFromCreator\x12=.injective.tokenfactory.v1beta1.QueryDenomsFromCreatorRequest\x1a>.injective.tokenfactory.v1beta1.QueryDenomsFromCreatorResponse\"E\x82\xd3\xe4\x93\x02?\x12=/injective/tokenfactory/v1beta1/denoms_from_creator/{creator}\x12\xc2\x01\n\x17TokenfactoryModuleState\x12\x37.injective.tokenfactory.v1beta1.QueryModuleStateRequest\x1a\x38.injective.tokenfactory.v1beta1.QueryModuleStateResponse\"4\x82\xd3\xe4\x93\x02.\x12,/injective/tokenfactory/v1beta1/module_stateBTZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['creator']._options = None
  _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['creator']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['sub_denom']._options = None
  _QUERYDENOMAUTHORITYMETADATAREQUEST.fields_by_name['sub_denom']._serialized_options = b'\362\336\037\020yaml:\"sub_denom\"'
  _QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata']._options = None
  _QUERYDENOMAUTHORITYMETADATARESPONSE.fields_by_name['authority_metadata']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"authority_metadata\"'
  _QUERYDENOMSFROMCREATORREQUEST.fields_by_name['creator']._options = None
  _QUERYDENOMSFROMCREATORREQUEST.fields_by_name['creator']._serialized_options = b'\362\336\037\016yaml:\"creator\"'
  _QUERYDENOMSFROMCREATORRESPONSE.fields_by_name['denoms']._options = None
  _QUERYDENOMSFROMCREATORRESPONSE.fields_by_name['denoms']._serialized_options = b'\362\336\037\ryaml:\"denoms\"'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002(\022&/injective/tokenfactory/v1beta1/params'
  _QUERY.methods_by_name['DenomAuthorityMetadata']._options = None
  _QUERY.methods_by_name['DenomAuthorityMetadata']._serialized_options = b'\202\323\344\223\002Q\022O/injective/tokenfactory/v1beta1/denoms/{creator}/{sub_denom}/authority_metadata'
  _QUERY.methods_by_name['DenomsFromCreator']._options = None
  _QUERY.methods_by_name['DenomsFromCreator']._serialized_options = b'\202\323\344\223\002?\022=/injective/tokenfactory/v1beta1/denoms_from_creator/{creator}'
  _QUERY.methods_by_name['TokenfactoryModuleState']._options = None
  _QUERY.methods_by_name['TokenfactoryModuleState']._serialized_options = b'\202\323\344\223\002.\022,/injective/tokenfactory/v1beta1/module_state'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=321
  _globals['_QUERYPARAMSREQUEST']._serialized_end=341
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=343
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=426
  _globals['_QUERYDENOMAUTHORITYMETADATAREQUEST']._serialized_start=428
  _globals['_QUERYDENOMAUTHORITYMETADATAREQUEST']._serialized_end=540
  _globals['_QUERYDENOMAUTHORITYMETADATARESPONSE']._serialized_start=543
  _globals['_QUERYDENOMAUTHORITYMETADATARESPONSE']._serialized_end=699
  _globals['_QUERYDENOMSFROMCREATORREQUEST']._serialized_start=701
  _globals['_QUERYDENOMSFROMCREATORREQUEST']._serialized_end=769
  _globals['_QUERYDENOMSFROMCREATORRESPONSE']._serialized_start=771
  _globals['_QUERYDENOMSFROMCREATORRESPONSE']._serialized_end=838
  _globals['_QUERYMODULESTATEREQUEST']._serialized_start=840
  _globals['_QUERYMODULESTATEREQUEST']._serialized_end=865
  _globals['_QUERYMODULESTATERESPONSE']._serialized_start=867
  _globals['_QUERYMODULESTATERESPONSE']._serialized_end=954
  _globals['_QUERY']._serialized_start=957
  _globals['_QUERY']._serialized_end=1798
# @@protoc_insertion_point(module_scope)
