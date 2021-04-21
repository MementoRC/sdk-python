# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import injective_spot_markets_rpc_pb2 as injective__spot__markets__rpc__pb2


class InjectiveSpotMarketsRPCStub(object):
    """InjectiveSpotMarketsRPC defines gRPC API of Spot Markets provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MarketList = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketList',
                request_serializer=injective__spot__markets__rpc__pb2.MarketListRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.MarketListResponse.FromString,
                )
        self.MarketDetails = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketDetails',
                request_serializer=injective__spot__markets__rpc__pb2.MarketDetailsRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.MarketDetailsResponse.FromString,
                )
        self.StreamMarketDetails = channel.unary_stream(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketDetails',
                request_serializer=injective__spot__markets__rpc__pb2.StreamMarketDetailsRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.StreamMarketDetailsResponse.FromString,
                )
        self.MarketOrderbook = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketOrderbook',
                request_serializer=injective__spot__markets__rpc__pb2.MarketOrderbookRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.MarketOrderbookResponse.FromString,
                )
        self.StreamMarketOrderbook = channel.unary_stream(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketOrderbook',
                request_serializer=injective__spot__markets__rpc__pb2.StreamMarketOrderbookRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.StreamMarketOrderbookResponse.FromString,
                )
        self.MarketOrders = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketOrders',
                request_serializer=injective__spot__markets__rpc__pb2.MarketOrdersRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.MarketOrdersResponse.FromString,
                )
        self.StreamMarketOrders = channel.unary_stream(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketOrders',
                request_serializer=injective__spot__markets__rpc__pb2.StreamMarketOrdersRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.StreamMarketOrdersResponse.FromString,
                )
        self.MarketTrades = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketTrades',
                request_serializer=injective__spot__markets__rpc__pb2.MarketTradesRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.MarketTradesResponse.FromString,
                )
        self.StreamMarketTrades = channel.unary_stream(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketTrades',
                request_serializer=injective__spot__markets__rpc__pb2.StreamMarketTradesRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.StreamMarketTradesResponse.FromString,
                )
        self.SubaccountsList = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountsList',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountsListRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountsListResponse.FromString,
                )
        self.SubaccountOrdersList = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountOrdersList',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountOrdersListResponse.FromString,
                )
        self.SubaccountTradesList = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountTradesList',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountTradesListResponse.FromString,
                )
        self.SubaccountBalancesList = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountBalancesList',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountBalancesListRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountBalancesListResponse.FromString,
                )
        self.SubaccountBalanceEndpoint = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountBalanceEndpoint',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountBalanceRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountBalanceResponse.FromString,
                )
        self.SubaccountHistory = channel.unary_unary(
                '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountHistory',
                request_serializer=injective__spot__markets__rpc__pb2.SubaccountHistoryRequest.SerializeToString,
                response_deserializer=injective__spot__markets__rpc__pb2.SubaccountHistoryResponse.FromString,
                )


class InjectiveSpotMarketsRPCServicer(object):
    """InjectiveSpotMarketsRPC defines gRPC API of Spot Markets provider.
    """

    def MarketList(self, request, context):
        """Get a list of Spot Markets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketDetails(self, request, context):
        """Get details of a single spot market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMarketDetails(self, request, context):
        """Stream live updates of selected spot markets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketOrderbook(self, request, context):
        """Orderbook of a Spot Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMarketOrderbook(self, request, context):
        """Stream live updates of selected spot market orderbook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketOrders(self, request, context):
        """Orders of a Spot Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMarketOrders(self, request, context):
        """Stream updates to individual orders of a Spot Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketTrades(self, request, context):
        """Trades of a Spot Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMarketTrades(self, request, context):
        """Stream newly executed trades from Spot Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountsList(self, request, context):
        """List all subaccounts IDs of an account address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountOrdersList(self, request, context):
        """List orders posted from this subaccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountTradesList(self, request, context):
        """List trades executed by this subaccount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountBalancesList(self, request, context):
        """List all subaccount balances
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountBalanceEndpoint(self, request, context):
        """Gets a balance for specific coin denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountHistory(self, request, context):
        """Get subaccount's deposits and withdrawals history
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveSpotMarketsRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MarketList': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketList,
                    request_deserializer=injective__spot__markets__rpc__pb2.MarketListRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.MarketListResponse.SerializeToString,
            ),
            'MarketDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketDetails,
                    request_deserializer=injective__spot__markets__rpc__pb2.MarketDetailsRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.MarketDetailsResponse.SerializeToString,
            ),
            'StreamMarketDetails': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMarketDetails,
                    request_deserializer=injective__spot__markets__rpc__pb2.StreamMarketDetailsRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.StreamMarketDetailsResponse.SerializeToString,
            ),
            'MarketOrderbook': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketOrderbook,
                    request_deserializer=injective__spot__markets__rpc__pb2.MarketOrderbookRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.MarketOrderbookResponse.SerializeToString,
            ),
            'StreamMarketOrderbook': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMarketOrderbook,
                    request_deserializer=injective__spot__markets__rpc__pb2.StreamMarketOrderbookRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.StreamMarketOrderbookResponse.SerializeToString,
            ),
            'MarketOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketOrders,
                    request_deserializer=injective__spot__markets__rpc__pb2.MarketOrdersRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.MarketOrdersResponse.SerializeToString,
            ),
            'StreamMarketOrders': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMarketOrders,
                    request_deserializer=injective__spot__markets__rpc__pb2.StreamMarketOrdersRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.StreamMarketOrdersResponse.SerializeToString,
            ),
            'MarketTrades': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketTrades,
                    request_deserializer=injective__spot__markets__rpc__pb2.MarketTradesRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.MarketTradesResponse.SerializeToString,
            ),
            'StreamMarketTrades': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMarketTrades,
                    request_deserializer=injective__spot__markets__rpc__pb2.StreamMarketTradesRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.StreamMarketTradesResponse.SerializeToString,
            ),
            'SubaccountsList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountsList,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountsListRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountsListResponse.SerializeToString,
            ),
            'SubaccountOrdersList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountOrdersList,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountOrdersListRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountOrdersListResponse.SerializeToString,
            ),
            'SubaccountTradesList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountTradesList,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountTradesListRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountTradesListResponse.SerializeToString,
            ),
            'SubaccountBalancesList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountBalancesList,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountBalancesListRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountBalancesListResponse.SerializeToString,
            ),
            'SubaccountBalanceEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountBalanceEndpoint,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountBalanceRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountBalanceResponse.SerializeToString,
            ),
            'SubaccountHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountHistory,
                    request_deserializer=injective__spot__markets__rpc__pb2.SubaccountHistoryRequest.FromString,
                    response_serializer=injective__spot__markets__rpc__pb2.SubaccountHistoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_spot_markets_rpc.InjectiveSpotMarketsRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveSpotMarketsRPC(object):
    """InjectiveSpotMarketsRPC defines gRPC API of Spot Markets provider.
    """

    @staticmethod
    def MarketList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketList',
            injective__spot__markets__rpc__pb2.MarketListRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.MarketListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketDetails',
            injective__spot__markets__rpc__pb2.MarketDetailsRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.MarketDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMarketDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketDetails',
            injective__spot__markets__rpc__pb2.StreamMarketDetailsRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.StreamMarketDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketOrderbook',
            injective__spot__markets__rpc__pb2.MarketOrderbookRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.MarketOrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMarketOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketOrderbook',
            injective__spot__markets__rpc__pb2.StreamMarketOrderbookRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.StreamMarketOrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketOrders',
            injective__spot__markets__rpc__pb2.MarketOrdersRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.MarketOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMarketOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketOrders',
            injective__spot__markets__rpc__pb2.StreamMarketOrdersRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.StreamMarketOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/MarketTrades',
            injective__spot__markets__rpc__pb2.MarketTradesRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.MarketTradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMarketTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/StreamMarketTrades',
            injective__spot__markets__rpc__pb2.StreamMarketTradesRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.StreamMarketTradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountsList',
            injective__spot__markets__rpc__pb2.SubaccountsListRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountsListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountOrdersList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountOrdersList',
            injective__spot__markets__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountOrdersListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountTradesList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountTradesList',
            injective__spot__markets__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountTradesListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountBalancesList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountBalancesList',
            injective__spot__markets__rpc__pb2.SubaccountBalancesListRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountBalancesListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountBalanceEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountBalanceEndpoint',
            injective__spot__markets__rpc__pb2.SubaccountBalanceRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_spot_markets_rpc.InjectiveSpotMarketsRPC/SubaccountHistory',
            injective__spot__markets__rpc__pb2.SubaccountHistoryRequest.SerializeToString,
            injective__spot__markets__rpc__pb2.SubaccountHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
