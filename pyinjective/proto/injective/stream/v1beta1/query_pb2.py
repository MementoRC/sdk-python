# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/stream/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.exchange.v1beta1 import events_pb2 as injective_dot_exchange_dot_v1beta1_dot_events__pb2
from injective.exchange.v1beta1 import exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$injective/stream/v1beta1/query.proto\x12\x18injective.stream.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\'injective/exchange/v1beta1/events.proto\x1a)injective/exchange/v1beta1/exchange.proto\"\xb6\x06\n\rStreamRequest\x12P\n\x14\x62\x61nk_balances_filter\x18\x01 \x01(\x0b\x32,.injective.stream.v1beta1.BankBalancesFilterB\x04\xc8\xde\x1f\x01\x12\\\n\x1asubaccount_deposits_filter\x18\x02 \x01(\x0b\x32\x32.injective.stream.v1beta1.SubaccountDepositsFilterB\x04\xc8\xde\x1f\x01\x12H\n\x12spot_trades_filter\x18\x03 \x01(\x0b\x32&.injective.stream.v1beta1.TradesFilterB\x04\xc8\xde\x1f\x01\x12N\n\x18\x64\x65rivative_trades_filter\x18\x04 \x01(\x0b\x32&.injective.stream.v1beta1.TradesFilterB\x04\xc8\xde\x1f\x01\x12H\n\x12spot_orders_filter\x18\x05 \x01(\x0b\x32&.injective.stream.v1beta1.OrdersFilterB\x04\xc8\xde\x1f\x01\x12N\n\x18\x64\x65rivative_orders_filter\x18\x06 \x01(\x0b\x32&.injective.stream.v1beta1.OrdersFilterB\x04\xc8\xde\x1f\x01\x12O\n\x16spot_orderbooks_filter\x18\x07 \x01(\x0b\x32).injective.stream.v1beta1.OrderbookFilterB\x04\xc8\xde\x1f\x01\x12U\n\x1c\x64\x65rivative_orderbooks_filter\x18\x08 \x01(\x0b\x32).injective.stream.v1beta1.OrderbookFilterB\x04\xc8\xde\x1f\x01\x12I\n\x10positions_filter\x18\t \x01(\x0b\x32).injective.stream.v1beta1.PositionsFilterB\x04\xc8\xde\x1f\x01\x12N\n\x13oracle_price_filter\x18\n \x01(\x0b\x32+.injective.stream.v1beta1.OraclePriceFilterB\x04\xc8\xde\x1f\x01\"\xc0\x05\n\x0eStreamResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04\x12<\n\rbank_balances\x18\x02 \x03(\x0b\x32%.injective.stream.v1beta1.BankBalance\x12I\n\x13subaccount_deposits\x18\x03 \x03(\x0b\x32,.injective.stream.v1beta1.SubaccountDeposits\x12\x38\n\x0bspot_trades\x18\x04 \x03(\x0b\x32#.injective.stream.v1beta1.SpotTrade\x12\x44\n\x11\x64\x65rivative_trades\x18\x05 \x03(\x0b\x32).injective.stream.v1beta1.DerivativeTrade\x12\x38\n\x0bspot_orders\x18\x06 \x03(\x0b\x32#.injective.stream.v1beta1.SpotOrder\x12\x44\n\x11\x64\x65rivative_orders\x18\x07 \x03(\x0b\x32).injective.stream.v1beta1.DerivativeOrder\x12I\n\x16spot_orderbook_updates\x18\x08 \x03(\x0b\x32).injective.stream.v1beta1.OrderbookUpdate\x12O\n\x1c\x64\x65rivative_orderbook_updates\x18\t \x03(\x0b\x32).injective.stream.v1beta1.OrderbookUpdate\x12\x35\n\tpositions\x18\n \x03(\x0b\x32\".injective.stream.v1beta1.Position\x12<\n\roracle_prices\x18\x0b \x03(\x0b\x32%.injective.stream.v1beta1.OraclePrice\"V\n\x0fOrderbookUpdate\x12\x0b\n\x03seq\x18\x01 \x01(\x04\x12\x36\n\torderbook\x18\x02 \x01(\x0b\x32#.injective.stream.v1beta1.Orderbook\"\x8d\x01\n\tOrderbook\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x35\n\nbuy_levels\x18\x02 \x03(\x0b\x32!.injective.exchange.v1beta1.Level\x12\x36\n\x0bsell_levels\x18\x03 \x03(\x0b\x32!.injective.exchange.v1beta1.Level\"}\n\x0b\x42\x61nkBalance\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12]\n\x08\x62\x61lances\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"p\n\x12SubaccountDeposits\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x43\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32+.injective.stream.v1beta1.SubaccountDepositB\x04\xc8\xde\x1f\x00\"^\n\x11SubaccountDeposit\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12:\n\x07\x64\x65posit\x18\x02 \x01(\x0b\x32#.injective.exchange.v1beta1.DepositB\x04\xc8\xde\x1f\x00\"_\n\tSpotOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12?\n\x05order\x18\x02 \x01(\x0b\x32*.injective.exchange.v1beta1.SpotLimitOrderB\x04\xc8\xde\x1f\x00\"~\n\x0f\x44\x65rivativeOrder\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x45\n\x05order\x18\x02 \x01(\x0b\x32\x30.injective.exchange.v1beta1.DerivativeLimitOrderB\x04\xc8\xde\x1f\x00\x12\x11\n\tis_market\x18\x03 \x01(\x08\"\xdd\x02\n\x08Position\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\t\x12\x0e\n\x06isLong\x18\x03 \x01(\x08\x12@\n\x08quantity\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x43\n\x0b\x65ntry_price\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12>\n\x06margin\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12P\n\x18\x63umulative_funding_entry\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\"j\n\x0bOraclePrice\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12=\n\x05price\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x0c\n\x04type\x18\x03 \x01(\t\"\xd3\x02\n\tSpotTrade\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0e\n\x06is_buy\x18\x02 \x01(\x08\x12\x15\n\rexecutionType\x18\x03 \x01(\t\x12@\n\x08quantity\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12=\n\x05price\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x15\n\rsubaccount_id\x18\x06 \x01(\t\x12;\n\x03\x66\x65\x65\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x12\n\norder_hash\x18\x08 \x01(\t\x12#\n\x15\x66\x65\x65_recipient_address\x18\t \x01(\tB\x04\xc8\xde\x1f\x01\"\xdb\x02\n\x0f\x44\x65rivativeTrade\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0e\n\x06is_buy\x18\x02 \x01(\x08\x12\x15\n\rexecutionType\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x41\n\x0eposition_delta\x18\x05 \x01(\x0b\x32).injective.exchange.v1beta1.PositionDelta\x12>\n\x06payout\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12;\n\x03\x66\x65\x65\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x12\n\norder_hash\x18\x08 \x01(\t\x12#\n\x15\x66\x65\x65_recipient_address\x18\t \x01(\tB\x04\xc8\xde\x1f\x01\":\n\x0cTradesFilter\x12\x16\n\x0esubaccount_ids\x18\x01 \x03(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t\"=\n\x0fPositionsFilter\x12\x16\n\x0esubaccount_ids\x18\x01 \x03(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t\":\n\x0cOrdersFilter\x12\x16\n\x0esubaccount_ids\x18\x01 \x03(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t\"%\n\x0fOrderbookFilter\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"&\n\x12\x42\x61nkBalancesFilter\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"2\n\x18SubaccountDepositsFilter\x12\x16\n\x0esubaccount_ids\x18\x01 \x03(\t\"#\n\x11OraclePriceFilter\x12\x0e\n\x06symbol\x18\x01 \x03(\t2g\n\x06Stream\x12]\n\x06Stream\x12\'.injective.stream.v1beta1.StreamRequest\x1a(.injective.stream.v1beta1.StreamResponse0\x01\x42\x46ZDgithub.com/InjectiveLabs/injective-core/injective-chain/stream/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.stream.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/InjectiveLabs/injective-core/injective-chain/stream/types'
  _STREAMREQUEST.fields_by_name['bank_balances_filter']._options = None
  _STREAMREQUEST.fields_by_name['bank_balances_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['subaccount_deposits_filter']._options = None
  _STREAMREQUEST.fields_by_name['subaccount_deposits_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['spot_trades_filter']._options = None
  _STREAMREQUEST.fields_by_name['spot_trades_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['derivative_trades_filter']._options = None
  _STREAMREQUEST.fields_by_name['derivative_trades_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['spot_orders_filter']._options = None
  _STREAMREQUEST.fields_by_name['spot_orders_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['derivative_orders_filter']._options = None
  _STREAMREQUEST.fields_by_name['derivative_orders_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['spot_orderbooks_filter']._options = None
  _STREAMREQUEST.fields_by_name['spot_orderbooks_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['derivative_orderbooks_filter']._options = None
  _STREAMREQUEST.fields_by_name['derivative_orderbooks_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['positions_filter']._options = None
  _STREAMREQUEST.fields_by_name['positions_filter']._serialized_options = b'\310\336\037\001'
  _STREAMREQUEST.fields_by_name['oracle_price_filter']._options = None
  _STREAMREQUEST.fields_by_name['oracle_price_filter']._serialized_options = b'\310\336\037\001'
  _BANKBALANCE.fields_by_name['balances']._options = None
  _BANKBALANCE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _SUBACCOUNTDEPOSITS.fields_by_name['deposits']._options = None
  _SUBACCOUNTDEPOSITS.fields_by_name['deposits']._serialized_options = b'\310\336\037\000'
  _SUBACCOUNTDEPOSIT.fields_by_name['deposit']._options = None
  _SUBACCOUNTDEPOSIT.fields_by_name['deposit']._serialized_options = b'\310\336\037\000'
  _SPOTORDER.fields_by_name['order']._options = None
  _SPOTORDER.fields_by_name['order']._serialized_options = b'\310\336\037\000'
  _DERIVATIVEORDER.fields_by_name['order']._options = None
  _DERIVATIVEORDER.fields_by_name['order']._serialized_options = b'\310\336\037\000'
  _POSITION.fields_by_name['quantity']._options = None
  _POSITION.fields_by_name['quantity']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['entry_price']._options = None
  _POSITION.fields_by_name['entry_price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['margin']._options = None
  _POSITION.fields_by_name['margin']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _POSITION.fields_by_name['cumulative_funding_entry']._options = None
  _POSITION.fields_by_name['cumulative_funding_entry']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _ORACLEPRICE.fields_by_name['price']._options = None
  _ORACLEPRICE.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _SPOTTRADE.fields_by_name['quantity']._options = None
  _SPOTTRADE.fields_by_name['quantity']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _SPOTTRADE.fields_by_name['price']._options = None
  _SPOTTRADE.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _SPOTTRADE.fields_by_name['fee']._options = None
  _SPOTTRADE.fields_by_name['fee']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _SPOTTRADE.fields_by_name['fee_recipient_address']._options = None
  _SPOTTRADE.fields_by_name['fee_recipient_address']._serialized_options = b'\310\336\037\001'
  _DERIVATIVETRADE.fields_by_name['payout']._options = None
  _DERIVATIVETRADE.fields_by_name['payout']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _DERIVATIVETRADE.fields_by_name['fee']._options = None
  _DERIVATIVETRADE.fields_by_name['fee']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _DERIVATIVETRADE.fields_by_name['fee_recipient_address']._options = None
  _DERIVATIVETRADE.fields_by_name['fee_recipient_address']._serialized_options = b'\310\336\037\001'
  _globals['_STREAMREQUEST']._serialized_start=205
  _globals['_STREAMREQUEST']._serialized_end=1027
  _globals['_STREAMRESPONSE']._serialized_start=1030
  _globals['_STREAMRESPONSE']._serialized_end=1734
  _globals['_ORDERBOOKUPDATE']._serialized_start=1736
  _globals['_ORDERBOOKUPDATE']._serialized_end=1822
  _globals['_ORDERBOOK']._serialized_start=1825
  _globals['_ORDERBOOK']._serialized_end=1966
  _globals['_BANKBALANCE']._serialized_start=1968
  _globals['_BANKBALANCE']._serialized_end=2093
  _globals['_SUBACCOUNTDEPOSITS']._serialized_start=2095
  _globals['_SUBACCOUNTDEPOSITS']._serialized_end=2207
  _globals['_SUBACCOUNTDEPOSIT']._serialized_start=2209
  _globals['_SUBACCOUNTDEPOSIT']._serialized_end=2303
  _globals['_SPOTORDER']._serialized_start=2305
  _globals['_SPOTORDER']._serialized_end=2400
  _globals['_DERIVATIVEORDER']._serialized_start=2402
  _globals['_DERIVATIVEORDER']._serialized_end=2528
  _globals['_POSITION']._serialized_start=2531
  _globals['_POSITION']._serialized_end=2880
  _globals['_ORACLEPRICE']._serialized_start=2882
  _globals['_ORACLEPRICE']._serialized_end=2988
  _globals['_SPOTTRADE']._serialized_start=2991
  _globals['_SPOTTRADE']._serialized_end=3330
  _globals['_DERIVATIVETRADE']._serialized_start=3333
  _globals['_DERIVATIVETRADE']._serialized_end=3680
  _globals['_TRADESFILTER']._serialized_start=3682
  _globals['_TRADESFILTER']._serialized_end=3740
  _globals['_POSITIONSFILTER']._serialized_start=3742
  _globals['_POSITIONSFILTER']._serialized_end=3803
  _globals['_ORDERSFILTER']._serialized_start=3805
  _globals['_ORDERSFILTER']._serialized_end=3863
  _globals['_ORDERBOOKFILTER']._serialized_start=3865
  _globals['_ORDERBOOKFILTER']._serialized_end=3902
  _globals['_BANKBALANCESFILTER']._serialized_start=3904
  _globals['_BANKBALANCESFILTER']._serialized_end=3942
  _globals['_SUBACCOUNTDEPOSITSFILTER']._serialized_start=3944
  _globals['_SUBACCOUNTDEPOSITSFILTER']._serialized_end=3994
  _globals['_ORACLEPRICEFILTER']._serialized_start=3996
  _globals['_ORACLEPRICEFILTER']._serialized_end=4031
  _globals['_STREAM']._serialized_start=4033
  _globals['_STREAM']._serialized_end=4136
# @@protoc_insertion_point(module_scope)
