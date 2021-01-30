'''
Tests for our `AbstractFlow` class

author: derek_herincx@gallup.com
last_updated: 10/28/2020
'''

import pytest
from prefect import task, Flow

from src import AbstractFlow

@task
def say_abc_hello():
    """Basic task to ensure flow has a finished state"""
    print("Testing ABC flow!")

class FlowTest(AbstractFlow):
    """Mock class to test with"""

    def __init__(self, fail=False, **kwargs):
        super().__init__(**kwargs)
        # set to True to return a string from `build` to test decorator
        self.fail = fail

    def build(self):
        """Purposely returns a `str` when `fail=True`"""
        if not self.fail:
            with Flow("Empty Flow test") as flow:
                h = say_abc_hello()
            return flow
        return "fail"

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
            FlowTest(cron=sample_cron)

    def test_build_output_type(self):
        """Asserts that `build` method returns a `flow`"""
        mock = FlowTest()
        assert isinstance(mock.build(), Flow)

    def test_validator_decorator(self):
        """Asserts build method decorator returns a TypeError"""
        mock = FlowTest(fail=True)
        with pytest.raises(TypeError):
            mock.build()

    def test_runner_finishes(self):
        """
        Asserts that `run` completes flow. It's up to the user to implement
        flow logic. We just want to test that even the simplest of logic is
        completed.
        """
        mock = FlowTest()
        state = mock.run()
        assert state.is_finished() == True
