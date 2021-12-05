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

## Known issues

### No access to archive state errors

If you are using Ganache to fork a network, then you may have issues with the blockchain archive state every 30 minutes. This is due to your node provider (i.e. Infura) only allowing free users access to 30 minutes of archive state. To solve this, upgrade to a paid plan, or simply restart your ganache instance and redploy your contracts.

# Resources

- Yearn [Discord channel](https://discord.com/invite/6PNv2nF/)
- Brownie [Gitter channel](https://gitter.im/eth-brownie/community)
