import inspect
import pytest
from prefect import Flow

from flow import AbstractFlow


class FlowTest(AbstractFlow):
  """Just need to ensure we return a flow object"""
  def build(self):
    with Flow("Empty Flow test") as flow:
      pass
    return flow

class TestAbstractFlow:
    """Test the `AbstractFlow` class"""

  def test_abstract_instance_error(self):
    """`AbstractFlow` should not be able to be instantiated"""
    with pytest.raises(NotImplementedError):
      AbstractFlow()

  def test_create_flow_no_cron(self):
    """Should be able to create a class without a `cron` string"""
    assert FlowTest()

  def test_assert_invalid_cron_exception(self):
    """An invalid cron string should raise an error in __init__"""
    sample_cron = "* c x 3"
    with pytest.raises(ValueError):
      FlowTest(sample_cron)

  def test_build_output_type(self):
    """Asserts that `build` method returns a `flow`"""
    mock = FlowTest()
    assert isinstance(mock.build(), Flow)