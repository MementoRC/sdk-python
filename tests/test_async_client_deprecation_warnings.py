from warnings import catch_warnings

import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb
from pyinjective.proto.exchange import injective_accounts_rpc_pb2 as exchange_accounts_pb
from pyinjective.proto.injective.types.v1beta1 import account_pb2 as account_pb
from tests.client.chain.grpc.configurable_auth_query_servicer import ConfigurableAuthQueryServicer
from tests.client.chain.grpc.configurable_autz_query_servicer import ConfigurableAuthZQueryServicer
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer
from tests.client.indexer.configurable_account_query_servicer import ConfigurableAccountQueryServicer


@pytest.fixture
def account_servicer():
    return ConfigurableAccountQueryServicer()


@pytest.fixture
def auth_servicer():
    return ConfigurableAuthQueryServicer()


@pytest.fixture
def authz_servicer():
    return ConfigurableAuthZQueryServicer()


@pytest.fixture
def bank_servicer():
    return ConfigurableBankQueryServicer()


class TestAsyncClientDeprecationWarnings:
    @pytest.mark.asyncio
    async def test_get_account_deprecation_warning(
        self,
        auth_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubAuth = auth_servicer
        auth_servicer.account_responses.append(account_pb.EthAccount())

        with catch_warnings(record=True) as all_warnings:
            await client.get_account(address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_account instead"

    @pytest.mark.asyncio
    async def test_get_bank_balance_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubBank = bank_servicer
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balance(address="", denom="inj")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_bank_balance instead"

    @pytest.mark.asyncio
    async def test_get_bank_balances_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubBank = bank_servicer
        bank_servicer.balances_responses.append(bank_query_pb.QueryAllBalancesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balances(address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_bank_balances instead"

    @pytest.mark.asyncio
    async def test_get_order_states_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.order_states_responses.append(exchange_accounts_pb.OrderStatesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_order_states(spot_order_hashes=["hash1"], derivative_order_hashes=["hash2"])

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_order_states instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccounts_list_responses.append(exchange_accounts_pb.SubaccountsListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_list(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccounts_list instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_balances_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balances_list_responses.append(
            exchange_accounts_pb.SubaccountBalancesListResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balances_list(subaccount_id="", denoms=[])

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_balances_list instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balance_responses.append(exchange_accounts_pb.SubaccountBalanceEndpointResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balance(subaccount_id="", denom="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_balance instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_history_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_history_responses.append(exchange_accounts_pb.SubaccountHistoryResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_history(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_history instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_order_summary_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_order_summary_responses.append(
            exchange_accounts_pb.SubaccountOrderSummaryResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_order_summary(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_order_summary instead"

    @pytest.mark.asyncio
    async def test_get_portfolio_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.portfolio_responses.append(exchange_accounts_pb.PortfolioResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_portfolio(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_portfolio instead"

    @pytest.mark.asyncio
    async def test_get_rewards_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.rewards_responses.append(exchange_accounts_pb.RewardsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_rewards(account_address="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_rewards instead"

    @pytest.mark.asyncio
    async def test_stream_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.stream_subaccount_balance_responses.append(
            exchange_accounts_pb.StreamSubaccountBalanceResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.stream_subaccount_balance(subaccount_id="")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert (
            str(all_warnings[0].message) == "This method is deprecated. Use listen_subaccount_balance_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_grants_deprecation_warning(
        self,
        authz_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
            insecure=False,
        )
        client.stubAuthz = authz_servicer
        authz_servicer.grants_responses.append(authz_query.QueryGrantsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_grants(granter="granter", grantee="grantee")

        assert len(all_warnings) == 1
        assert issubclass(all_warnings[0].category, DeprecationWarning)
        assert str(all_warnings[0].message) == "This method is deprecated. Use fetch_grants instead"
