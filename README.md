# prefect-abc

## Inspiration
During my time at Gallup, I found myself automating a lot of manual processes and like any other good ol' data engineer, I started with `cron`. While `cron` is a good ad-hoc solution when running some basic scripts, things can get complicated when you're running a ton of scripts attempting to accomplish different things. This makes it difficult to work within different Python environments and it really stagnated my ability to write modular code since the end goal was to "get the job done". While your focus should be on accomplishing a specific goal, as a developer, I wanted to write code that others could understand and improve years down the road.

When discussing workflow tools, _Airflow_ was the obvious first choice to come up. A quick Google search for Airflow yielded lots of complaints about it's scheduler and somewhat complex nature...until we (shoutout to @mitchbregs) found *_Prefect_*

## Prefect
At it's core, Prefect's main selling point was that it was written in Python _for_ Python. Furthermore, its emphasis on being able to integrate seamlessly with an existing code base was what sold me. And let me mention, the Prefect docs are UNBELIEVEABLE -- full of examples and a great community group on Slack (check them out: https://docs.prefect.io/orchestration/)

## Why it Matters (to me)
This repo was inspired by a structure that @mitchbregs used at Gallup. We found ourselves building `flows` (i.e. or in Airflow terms, DAGs) over and over, nesting them in arbitrary functions that had different names, so rather than try to figure out how to run each other's code, @mitchbregs devised a way to modularize the different `flow` methods, effectively "containerizing" the `flow` logic and the `run` method to actually run it. Also, the _Prefect_ repo was the first codebase I really dug into, so I built this repo to prove to myself that I really understood what is going on under the hood when running a local flow on my device.

## What Matters (to you)
If you've made it this far, thanks for reading!

So what I've built here is what's called an Abstract Base Class (ABC). Python's `abc` module allows us to use abstract base classes and if you're like me, you're probably wondering what the heck they are. It's simple -- let's say you have an idea for a class and its methods and you want someone to simply come in and fill in the logic for the methods. If you attempt to return `None` from any method within a class of this sorts, you will get an error. Here's where ABC's come in -- if you want to build a class with methods returning `None`, you can have your class inherit from ABC and then wrap all methods that you want the user to fill in with the `@abstractmethod` decorator, which is exactly what the `AbstractFlow` class in this repo does. That's the tweet!

So in me and @mitchbregs' scenario, here's what's happening:

1. We know we need to build a `flow` that automates some sort of task; doesn't matter what the task is - we just want to get something done
2. We know that the `flow` needs to get built 
3. We know that the `flow` needs to `run` in order to be executed by Prefect and accomplish our task

Regardless of what we are trying to accomplish, you can see that the only step that really varies with the task is #1 - steps #2 and #3 do not vary because they are not dependent of the task; those are just things that needs to happen because Prefect said so :)

So ignoring the existence of Prefect Cloud, if we wanted to simply insert logic for a task all we would need to do is the following:


```python

class SampleFlow(AbstractFlow):

    def build(self):
        # this `build` overrides the `build` method from `AbstractFlow`
        sample_task = SampleTask()

        with Flow("sample flow") as flow:
            task_output = sample_task(some_param)

            (continued flow logic here...)

        return flow
```

Simply add the logic you want to run in your class' `build` method. In my case, `SampleFlow` has inherited from `AbstractFlow` (the ABC class). Because we are inheriting from `AbstractFlow`, that means we have the `build` and `run` methods available to us. Remember those 1,2,3 steps from above? Remember how I mentioned step #1 is the only one that varies depending on your task? Well in terms of the example above, `build` is the abstract method that we left open for the user. That means that in the class inheriting from `AbstractFlow`, you _must_ include the `build` method since it is used by steps #2 and #3 to execute your logic. So where are steps #2 and #3? Those are simply the `run` method...you don't need to worry about those since they are the same, _regardless of the task_.


So continuing from the example above, `SampleFlow` accomplishes something (doesn't matter what it is...just make sure it works). To run the flow locally then and see your task _accomplished_, run the following:

```python

flow = SampleFlow()
flow.run()
```
