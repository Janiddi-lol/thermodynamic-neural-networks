from typing import Dict

def quadratic_free_energy(state: Dict[str, float], a: float = 1.0) -> float:
    return 0.5 * a * sum(v*v for v in state.values())

def grad_quadratic_free_energy(state: Dict[str, float], a: float = 1.0) -> Dict[str, float]:
    return {k: a * v for k, v in state.items()}
