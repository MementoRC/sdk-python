# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: injective/auction/v1beta1/auction.proto, injective/auction/v1beta1/tx.proto, injective/auction/v1beta1/genesis.proto, injective/auction/v1beta1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib

from .cosmos.base import v1beta1


@dataclass
class Params(betterproto.Message):
    # auction_period_duration defines the auction period duration
    auction_period: int = betterproto.int64_field(1)
    # min_next_bid_increment_rate defines the minimum increment rate for new bids
    min_next_bid_increment_rate: str = betterproto.string_field(2)


@dataclass
class Bid(betterproto.Message):
    bidder: str = betterproto.string_field(1)
    amount: str = betterproto.string_field(2)


@dataclass
class EventBid(betterproto.Message):
    bidder: str = betterproto.string_field(1)
    amount: str = betterproto.string_field(2)
    round: int = betterproto.uint64_field(3)


@dataclass
class EventAuctionResult(betterproto.Message):
    winner: str = betterproto.string_field(1)
    amount: str = betterproto.string_field(2)
    round: int = betterproto.uint64_field(3)


@dataclass
class MsgBid(betterproto.Message):
    """Bid defines a SDK message for placing a bid for an auction"""

    sender: str = betterproto.string_field(1)
    # amount of the bid in INJ tokens
    bid_amount: v1beta1.Coin = betterproto.message_field(2)
    # the current auction round being bid on
    round: int = betterproto.uint64_field(3)


@dataclass
class MsgBidResponse(betterproto.Message):
    pass


@dataclass
class GenesisState(betterproto.Message):
    """GenesisState defines the auction module's genesis state."""

    # params defines all the parameters of related to auction.
    params: "Params" = betterproto.message_field(1)
    # current auction round
    auction_round: int = betterproto.uint64_field(2)
    # current highest bid
    highest_bid: "Bid" = betterproto.message_field(3)
    auction_ending_timestamp: int = betterproto.int64_field(4)


@dataclass
class QueryAuctionParamsRequest(betterproto.Message):
    """
    QueryAuctionParamsRequest is the request type for the Query/AuctionParams
    RPC method.
    """

    pass


@dataclass
class QueryAuctionParamsResponse(betterproto.Message):
    """
    QueryAuctionParamsRequest is the response type for the Query/AuctionParams
    RPC method.
    """

    params: "Params" = betterproto.message_field(1)


@dataclass
class QueryCurrentAuctionBasketRequest(betterproto.Message):
    """
    QueryCurrentAuctionBasketRequest is the request type for the
    Query/CurrentAuctionBasket RPC method.
    """

    pass


@dataclass
class QueryCurrentAuctionBasketResponse(betterproto.Message):
    """
    QueryCurrentAuctionBasketResponse is the response type for the
    Query/CurrentAuctionBasket RPC method.
    """

    amount: List[v1beta1.Coin] = betterproto.message_field(1)
    auction_round: int = betterproto.uint64_field(2)
    auction_closing_time: int = betterproto.int64_field(3)
    highest_bidder: str = betterproto.string_field(4)
    highest_bid_amount: str = betterproto.string_field(5)


@dataclass
class QueryModuleStateRequest(betterproto.Message):
    """
    QueryModuleStateRequest is the request type for the
    Query/AuctionModuleState RPC method.
    """

    pass


@dataclass
class QueryModuleStateResponse(betterproto.Message):
    """
    QueryModuleStateResponse is the response type for the
    Query/AuctionModuleState RPC method.
    """

    state: "GenesisState" = betterproto.message_field(1)


class MsgStub(betterproto.ServiceStub):
    """Msg defines the auction Msg service."""

    async def bid(
        self,
        *,
        sender: str = "",
        bid_amount: Optional[v1beta1.Coin] = None,
        round: int = 0,
    ) -> MsgBidResponse:
        """Bid defines a method for placing a bid for an auction"""

        request = MsgBid()
        request.sender = sender
        if bid_amount is not None:
            request.bid_amount = bid_amount
        request.round = round

        return await self._unary_unary(
            "/injective.auction.v1beta1.Msg/Bid",
            request,
            MsgBidResponse,
        )


class QueryStub(betterproto.ServiceStub):
    """Query defines the gRPC querier service."""

    async def auction_params(self) -> QueryAuctionParamsResponse:
        """Retrieves auction params"""

        request = QueryAuctionParamsRequest()

        return await self._unary_unary(
            "/injective.auction.v1beta1.Query/AuctionParams",
            request,
            QueryAuctionParamsResponse,
        )

    async def current_auction_basket(self) -> QueryCurrentAuctionBasketResponse:
        """
        Retrieves current auction basket with current highest bid and bidder
        """

        request = QueryCurrentAuctionBasketRequest()

        return await self._unary_unary(
            "/injective.auction.v1beta1.Query/CurrentAuctionBasket",
            request,
            QueryCurrentAuctionBasketResponse,
        )

    async def auction_module_state(self) -> QueryModuleStateResponse:
        """Retrieves the entire auction module's state"""

        request = QueryModuleStateRequest()

        return await self._unary_unary(
            "/injective.auction.v1beta1.Query/AuctionModuleState",
            request,
            QueryModuleStateResponse,
        )