class TriggerOutput:
    """Safe trigger interface. Simulation must be the default implementation."""

    def send(self, code, label):
        raise NotImplementedError("Approve trigger codes and simulation behavior before implementation")
