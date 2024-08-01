Package to compute property tests over data present on Materials Project. 

KIM models and arbitrarty ASE Calculators are supported.

Currently, only tests to compute elastic constants/bulk modulus (with equilibrium crystal structure) are implemented.

Functionality exists to compute elastic constants (and equilibrium crystal structures) for all structures on MP with reference elastic properties. 

This data has been downloaded and preprocessed to speed up testing process.

Installation:

    pip install git+https://github.com/EFuem/mp_tests.git

NOTE: If KIM models are to be used, the kimpy package and the KIM-API must also be installed.

Example Usage:
```python
from mp_tests import Elasticity

test = Elasticity(
    "SW_StillingerWeber_1985_Si__MO_405512056662_006",
    )

test.mp_tests()
```


Note: It's often the case for MLIPs that convergence criteria and optimization strategies adopted from the original KIM tests may be too tight/inappropriate. Work is still needed here.
