import pytest
from brownie import accounts, config, Contract
from eth_account import Account
from eth_account.messages import encode_structured_data


@pytest.fixture
def gov(accounts):
    yield accounts[0]


@pytest.fixture
def affiliate(accounts):
    yield accounts[1]


@pytest.fixture
def guardian(accounts):
    yield accounts[2]


@pytest.fixture
def management(accounts):
    yield accounts[2]


@pytest.fixture
def rewards(accounts):
    yield accounts[3]


@pytest.fixture
def rando(accounts):
    yield accounts[3]

@pytest.fixture
def rando2(accounts):
    yield accounts[4]

@pytest.fixture
def token(pm, gov):
    Token = pm(config["dependencies"][0]).Token
    yield gov.deploy(Token, 18)

@pytest.fixture
def shape_shift_router(affiliate, registry,  ShapeShiftDAORouter):
  yield affiliate.deploy(
    ShapeShiftDAORouter,
    registry
  )

@pytest.fixture
def vault(create_vault, token):
    yield create_vault(token=token)


@pytest.fixture
def create_vault(pm, gov, rewards, guardian, management):
    def create_vault(token, releaseDelta=0, governance=gov):
        liveRegistry = Contract("0x50c1a2eA0a861A967D9d0FFE2AE4012c2E053804")
        Vault = pm(config["dependencies"][0]).Vault

        tx = liveRegistry.newExperimentalVault(
            token,
            governance,
            guardian,
            rewards,
            "vault",
            "token",
            releaseDelta,
            {"from": governance},
        )
        vault = Vault.at(tx.return_value)

        vault.setDepositLimit(2 ** 256 - 1, {"from": governance})
        return vault

    yield create_vault


@pytest.fixture
def registry(pm, gov):
    Registry = pm(config["dependencies"][0]).Registry
    yield gov.deploy(Registry)


@pytest.fixture
def new_registry(pm, gov):
    Registry = pm(config["dependencies"][0]).Registry
    yield gov.deploy(Registry)

@pytest.fixture
def live_token(live_vault):
    token_address = live_vault.token()  # this will be the address of the Curve LP token
    yield Contract(token_address)


@pytest.fixture
def live_vault():
    yield Contract("0x986b4aff588a109c09b50a03f42e4110e29d353f")  # yvseth

@pytest.fixture
def live_shape_shift_router(ShapeShiftDAORouter, affiliate, live_registry):
    yield affiliate.deploy(
        ShapeShiftDAORouter,
        live_registry
    )

@pytest.fixture
def live_registry():
    yield Contract("v2.registry.ychad.eth")


@pytest.fixture
def live_whale(accounts):
    whale = accounts.at(
        "0x3c0ffff15ea30c35d7a85b85c0782d6c94e1d238", force=True
    )  # make sure this address holds big bags of want()
    yield whale


@pytest.fixture
def live_gov(live_registry):
    yield accounts.at(live_registry.governance(), force=True)
