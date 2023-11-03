# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from exchange import injective_campaign_rpc_pb2 as exchange_dot_injective__campaign__rpc__pb2


class InjectiveCampaignRPCStub(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ranking = channel.unary_unary(
                '/injective_campaign_rpc.InjectiveCampaignRPC/Ranking',
                request_serializer=exchange_dot_injective__campaign__rpc__pb2.RankingRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__campaign__rpc__pb2.RankingResponse.FromString,
                )


class InjectiveCampaignRPCServicer(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    def Ranking(self, request, context):
        """Lists all participants in campaign
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveCampaignRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ranking': grpc.unary_unary_rpc_method_handler(
                    servicer.Ranking,
                    request_deserializer=exchange_dot_injective__campaign__rpc__pb2.RankingRequest.FromString,
                    response_serializer=exchange_dot_injective__campaign__rpc__pb2.RankingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_campaign_rpc.InjectiveCampaignRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveCampaignRPC(object):
    """InjectiveCampaignRPC defined a gRPC service for Injective Campaigns.
    """

    @staticmethod
    def Ranking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_campaign_rpc.InjectiveCampaignRPC/Ranking',
            exchange_dot_injective__campaign__rpc__pb2.RankingRequest.SerializeToString,
            exchange_dot_injective__campaign__rpc__pb2.RankingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
