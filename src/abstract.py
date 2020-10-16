'''
Abstract class to be inherited in order to build
and run a prefect `flow` object.

author: Derek Herincx
last_updated: 10/15/2020
'''
from abc import ABC, abstractmethod

from croniter import croniter
import prefect

class AbstractFlow(ABC):
  """
  An abstract class for a prefect `flow`. If this class is instantiated,
  you will receive a TypeError since the `build` method has no actual
  implementation. Rather, this class must be inherited by another class that
  overrides and implements the actual flow logic.

  class SampleFlow(AbstractFlow):
    def build(self):
      sample_task = SampleTask()

      with Flow("sample flow") as flow:
        task_output = sample_task(some_param)

        (continued flow logic here...)

      return flow

  Args:
    - cron (str): a valid cron string
  """
  def __init__(self, cron):
    # validates if cron is a valid string
    if not croniter.is_valid(cron):
      raise ValueError(f"Invalid cron string: `{cron}`")
    self.cron = cron

  @abstractmethod
  def build(self):
    pass

  def run(self):
    flow = self.build()
    self.run()

