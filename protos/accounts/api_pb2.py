# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/accounts/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.accounts import account_pb2 as protos_dot_accounts_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protos/accounts/api.proto\x12\x0fprotos.accounts\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x11protos/base.proto\x1a\x1dprotos/accounts/account.proto\"8\n\x1aGetAccountApiTokensRequest\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\"w\n\x1bGetAccountApiTokensResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12<\n\x12\x61\x63\x63ount_api_tokens\x18\x02 \x03(\x0b\x32 .protos.accounts.AccountApiToken\"\x1e\n\x1c\x43reateAccountApiTokenRequest\"\x89\x01\n\x1d\x43reateAccountApiTokenResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x11\x61\x63\x63ount_api_token\x18\x02 \x01(\x0b\x32 .protos.accounts.AccountApiToken\"=\n\x1c\x44\x65leteAccountApiTokenRequest\x12\x1d\n\x15\x61\x63\x63ount_api_token_key\x18\x01 \x01(\t\"L\n\x1d\x44\x65leteAccountApiTokenResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x10\n\x0eGetUserRequest\"6\n\x0fGetUserResponse\x12#\n\x04user\x18\x01 \x01(\x0b\x32\x15.protos.accounts.User\"z\n\x16GetVersionInfoResponse\x12\x17\n\x0f\x63urrent_version\x18\x01 \x01(\t\x12\x16\n\x0elatest_version\x18\x02 \x01(\t\x12\x16\n\x0eshould_upgrade\x18\x03 \x01(\x08\x12\x17\n\x0fupgrade_message\x18\x04 \x01(\t\";\n\x12InviteUsersRequest\x12\x0e\n\x06\x65mails\x18\x01 \x03(\t\x12\x15\n\rsignup_domain\x18\x02 \x01(\t\"7\n\x13InviteUsersResponse\x12 \n\x07message\x18\x01 \x01(\x0b\x32\x0f.protos.Message\"b\n\x1eGetCurrentAccountUsersResponse\x12\x1a\n\x04meta\x18\x01 \x01(\x0b\x32\x0c.protos.Meta\x12$\n\x05users\x18\x02 \x03(\x0b\x32\x15.protos.accounts.User\"%\n\x14ResetPasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"J\n\x15ResetPasswordResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"Q\n\x1bResetPasswordConfirmRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cnew_password\x18\x03 \x01(\t\"Q\n\x1cResetPasswordConfirmResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\xf9\x01\n\x0cOktaAuthData\x12(\n\x02pk\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12+\n\x05\x65mail\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nfirst_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tlast_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bis_new_user\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xa8\x01\n\x10OktaAuthResponse\x12\x32\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rrefresh_token\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x04user\x18\x05 \x01(\x0b\x32\x1d.protos.accounts.OktaAuthDatab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.accounts.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETACCOUNTAPITOKENSREQUEST._serialized_start=158
  _GETACCOUNTAPITOKENSREQUEST._serialized_end=214
  _GETACCOUNTAPITOKENSRESPONSE._serialized_start=216
  _GETACCOUNTAPITOKENSRESPONSE._serialized_end=335
  _CREATEACCOUNTAPITOKENREQUEST._serialized_start=337
  _CREATEACCOUNTAPITOKENREQUEST._serialized_end=367
  _CREATEACCOUNTAPITOKENRESPONSE._serialized_start=370
  _CREATEACCOUNTAPITOKENRESPONSE._serialized_end=507
  _DELETEACCOUNTAPITOKENREQUEST._serialized_start=509
  _DELETEACCOUNTAPITOKENREQUEST._serialized_end=570
  _DELETEACCOUNTAPITOKENRESPONSE._serialized_start=572
  _DELETEACCOUNTAPITOKENRESPONSE._serialized_end=648
  _GETUSERREQUEST._serialized_start=650
  _GETUSERREQUEST._serialized_end=666
  _GETUSERRESPONSE._serialized_start=668
  _GETUSERRESPONSE._serialized_end=722
  _GETVERSIONINFORESPONSE._serialized_start=724
  _GETVERSIONINFORESPONSE._serialized_end=846
  _INVITEUSERSREQUEST._serialized_start=848
  _INVITEUSERSREQUEST._serialized_end=907
  _INVITEUSERSRESPONSE._serialized_start=909
  _INVITEUSERSRESPONSE._serialized_end=964
  _GETCURRENTACCOUNTUSERSRESPONSE._serialized_start=966
  _GETCURRENTACCOUNTUSERSRESPONSE._serialized_end=1064
  _RESETPASSWORDREQUEST._serialized_start=1066
  _RESETPASSWORDREQUEST._serialized_end=1103
  _RESETPASSWORDRESPONSE._serialized_start=1105
  _RESETPASSWORDRESPONSE._serialized_end=1179
  _RESETPASSWORDCONFIRMREQUEST._serialized_start=1181
  _RESETPASSWORDCONFIRMREQUEST._serialized_end=1262
  _RESETPASSWORDCONFIRMRESPONSE._serialized_start=1264
  _RESETPASSWORDCONFIRMRESPONSE._serialized_end=1345
  _OKTAAUTHDATA._serialized_start=1348
  _OKTAAUTHDATA._serialized_end=1597
  _OKTAAUTHRESPONSE._serialized_start=1600
  _OKTAAUTHRESPONSE._serialized_end=1768
# @@protoc_insertion_point(module_scope)
