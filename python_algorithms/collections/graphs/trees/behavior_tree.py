class Selector(Task):
    """
        Runs each task in order until one succeeds, at which point it returns
        SUCCESS. If all tasks fail, a FAILURE status is returned.  If a subtask
        is still RUNNING, then a RUNNING status is returned and processing
        continues until either SUCCESS or FAILURE is returned from the subtask.
    """

    def __init__(self, name, *args, **kwargs):
        super(Selector, self).__init__(name, *args, **kwargs)

    def run(self):
        for c in self.children:
            status = c.run()

            if status != TaskStatus.FAILURE:
                return status

        return TaskStatus.FAILURE


class Sequence(Task):
    """
        Runs each task in order until one fails, at which point it returns
        FAILURE. If all tasks succeed, a SUCCESS status is returned.  If a
        subtask is still RUNNING, then a RUNNING status is returned and
        processing continues until either SUCCESS or FAILURE is returned from
        the subtask.
    """

    def __init__(self, name, *args, **kwargs):
        super(Sequence, self).__init__(name, *args, **kwargs)

    def run(self):
        for c in self.children:
            status = c.run()

            if status != TaskStatus.SUCCESS:
                return status

        return TaskStatus.SUCCESS
