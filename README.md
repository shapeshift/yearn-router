# ShapeShift DAOs Yearn Affiliate Router

## Installation and Setup

You will need Python 3, [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), and [Ganache-CLI](https://github.com/trufflesuite/ganache-cli) installed. You will also need to sign up for [Infura](https://infura.io/) and get your own project ID.

```bash
# Check out the submodules
git submodule init && git submodule update --init --recursive
# Create new python virtualenv in the .virtualenv folder
virtualenv .virtualenv
# Activate the virtualenv
source ./.virtualenv/bin/activate
# Install python deps
pip install -r requirements-dev.txt
# Export environment variable with Infura project ID
export WEB3_INFURA_PROJECT_ID=<YourInfuraProjectIDHere>
```

Once you have the dependencies are installed and the infura project ID exported, compile with `brownie compile` and run tests with `brownie test`. Note that the virtualenv activation and infura project ID export need to be done in each shell you want to use Brownie in:

```bash
source ./.virtualenv/bin/activate
export WEB3_INFURA_PROJECT_ID=<YourInfuraProjectIDHere>
```

# Resources

- Yearn [Discord channel](https://discord.com/invite/6PNv2nF/)
- Brownie [Gitter channel](https://gitter.im/eth-brownie/community)

# Mainnet Deployment

Contract is currently deployed to mainnet at [0x6a1e73f12018D8e5f966ce794aa2921941feB17E](https://etherscan.io/address/0x6a1e73f12018d8e5f966ce794aa2921941feb17e)

Please see the security folder for the audit.
