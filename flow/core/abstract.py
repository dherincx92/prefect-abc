'''
Abstract class to be inherited in order to build
and run a prefect `flow`

author: Derek Herincx
last_updated: 10/22/2020
'''

from abc import ABC, abstractmethod
from functools import wraps

from croniter import croniter
from prefect import Flow

def _validate_build_output(build_method):
  """
  Decorator that validates if the output of the `build` method is a
  prefect `flow` object. If it is not, a `TypeError` is raised.

  Args:
    - build_method (Callable): `build` method overwriting `AbstractFlow`

  Returns:
    - Callable: the decorated `AbstractFlow.build` method

  Raises:
    - TypeError: if the output of `build` is not a prefect `flow`
  """
  @wraps(build_method)
  def wrapper(*args, **kwargs):
    if not isinstance(build_method(*args, **kwargs), Flow):
      raise TypeError("You must return a prefect `flow` object from `build`")
    else:
      return build_method(*args, **kwargs)
  return wrapper


class AbstractFlow(ABC):
  """
  An abstract class for a prefect `flow`. If this class is instantiated,
  you will receive a TypeError since the `build` method has no actual
  implementation. Rather, this class must be inherited by another class that
  overrides and implements the actual flow logic.

  What this means is that any user can import `AbstractFlow` and simply
  override the abstract `build` method with their specific `flow` logic.

  Note: for this version of the class, we are only supporting prefect's
  `cron` scheduler. If an invalid `cron` string is used, a `ValueError` will
  be raised during instantiation. For help on forming cron strings, I recommend
  `crontab.guru.com`.

  class SampleFlow(AbstractFlow):

    # this `build` overrides the `build` method from `AbstractFlow`
    def build(self):
      sample_task = SampleTask()

      with Flow("sample flow") as flow:
        task_output = sample_task(some_param)

        (continued flow logic here...)

      return flow

  Args:
    - cron (str, optional): a valid cron string
  """

  def __new__(cls, *args, **kwargs):
    """
    If user tries to instantiate this class, we prevent that with __new__
    (i.e. before class instantiation).
    """
    if cls.__name__ == 'AbstractFlow':
      raise NotImplementedError(f'''
        Abstract class `{cls.__name__}` should not be instantiated. Rather, it
        should be inherited by another class that implements a `build` method
        that returns a prefect `flow`
        '''
      )
    # if `AbstractFlow` is inherited by a new `cls` object, proceed...
    else:
      # cannot have any args since super() references the `object` class
      return super(AbstractFlow, cls).__new__(cls)

  def __init__(self, cron: str = None):
    # validates if cron is a valid string
    if cron and not croniter.is_valid(cron):
      raise ValueError(f'''
        Invalid cron string: `{cron}`. For help, consult `crontab.guru.com`
        '''
      )
    self.cron = cron

  def __getattribute__(self, name):
    # prevents recursion error; in Python3, all classes inherit from `object`
    method = object.__getattribute__(self, name)

    # decoration for any user created build method
    if name == 'build':
      return _validate_build_output(method)
    else:
      return method

  @abstractmethod
  def build(self):
    pass

  def run(self):
    flow = self.build()
    flow.run()

