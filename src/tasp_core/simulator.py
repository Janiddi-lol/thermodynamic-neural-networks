from dataclasses import dataclass
from typing import Callable, Dict

State = Dict[str, float]

@dataclass
class ThermodynamicSimulator:
    state: State
    free_energy: Callable[[State], float]
    grad_free_energy: Callable[[State], State]
    L: float = 1.0

    def step(self, dt: float = 1e-2) -> State:
        gradF = self.grad_free_energy(self.state)
        for k, v in gradF.items():
            self.state[k] = self.state.get(k, 0.0) - dt * self.L * v
        return self.state

    def F(self) -> float:
        return self.free_energy(self.state)
