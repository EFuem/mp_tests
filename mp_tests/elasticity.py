from test_driver import TestDriver
from mp_mixin import MPMixin

class Elasticity(TestDriver,MPMixin):

    def __init__(self, model, supported_species, db_name):
        TestDriver.__init__(self, model)
        MPMixin.__init__(self, supported_species, db_name)

    def post_process(self):
        results = self.property_instances

if __name__ == "__main__":
    from mace.calculators import mace_mp
    from utils import mp_species
    model = mace_mp(default_dtype="float64")
    test = Elasticity(model, supported_species=mp_species, db_name='mp.json' )
    test.mp_tests(job_n=0, n_calcs=10, method="energy-condensed", optimize=True)

