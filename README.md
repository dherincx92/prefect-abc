# prefect-abc

## Inspiration
During my time at Gallup, I found myself automating a lot of manual processes and my journey like any other good ol' data engineer, I started with `cron`. While `cron` is a good ad-hoc solution when running some basic scripts, things can get complicated when you're running a ton of scripts attempting to accomplish different things. This makes it difficult to work within different Python environments and it really stagnated my ability to write modular code since the end goal was to "get the job done". While anyone's focus should be on accomplishing a specific goal, as a developer, I wanted to write code that others could understand and improve years down the road.

When discussing workflow tools, _Airflow_ was the obvious first choice to come up. A quick Google search for Airflow yielded lots of complaints about it's scheduler and somewhat complex nature...until we (shoutout to @mitchbregs) found *_Prefect_*

## Prefect
At it's core, Prefect's main selling point was that it was written in Python _for_ Python. Furthermore, its emphasis on being able to integrate seamlessly with an existing code base was what sold me. And let me mention, the Prefect docs are UNBELIEVEABLE -- full of examples and a great community group on Slack (check them out: https://docs.prefect.io/orchestration/)

## Why it Matters (to me)
This repo was inspired by a structure that @mitchbregs used at Gallup. We found ourselves building `flows` (i.e. or in Airflow terms, a DAGs) over and over, nesting them in arbitrary functions that had different names, so rather than try to figure out how to run each other's code, @mitchbregs devised a way to modularize the different `flow` methods, effectively "containerizing" the `flow` logic and the `run` method to actually run it. Also, the _Prefect_ repo was the first codebase I really dug into so I built this repo to prove to myself that I really understood what is going on under the hood when running a local flow on my device.

## What Matters (to you)
If you've made it this far, thanks for reading!
