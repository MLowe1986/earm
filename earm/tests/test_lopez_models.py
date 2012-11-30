"""
Checks the MOMP-only versions of the Lopez models, that is

- earm.mito.lopez_embedded
- earm.mito.lopez_direct
- earm.mito.lopez_indirect

against a previously validated and serialized state. Each test in the module
uses the function pysb.testing.check_model_against_component_list to perform
the comparison.
"""

from earm.mito import lopez_embedded
from earm.mito import lopez_direct
from earm.mito import lopez_indirect

from pysb.testing import *
import pickle

def test_lopez_embedded():
    """Test the earm.mito.lopez_embedded model against a serialized state."""
    f = open('lopez_embedded_validated.pickle', 'r')
    component_list = pickle.load(f)
    check_model_against_component_list(lopez_embedded.model, component_list)

def test_lopez_direct():
    """Test the earm.mito.lopez_direct model against a serialized state."""
    f = open('lopez_direct_validated.pickle', 'r')
    component_list = pickle.load(f)
    check_model_against_component_list(lopez_direct.model, component_list)

def test_lopez_indirect():
    """Test the earm.mito.lopez_indirect model against a serialized state."""
    f = open('lopez_indirect_validated.pickle', 'r')
    component_list = pickle.load(f)
    check_model_against_component_list(lopez_indirect.model, component_list)

def pickle_lopez_models():
    """The pickling procedure that was used to serialize the components
    of the Lopez models in a validated state.
    """
    serialize_component_list(lopez_embedded.model,
                             'lopez_embedded_validated.pickle')
    serialize_component_list(lopez_direct.model,
                             'lopez_direct_validated.pickle')
    serialize_component_list(lopez_indirect.model,
                             'lopez_indirect_validated.pickle')
