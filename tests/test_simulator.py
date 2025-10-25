from tasp_core.simulator import ThermodynamicSimulator
from tnn.dynamics import quadratic_free_energy, grad_quadratic_free_energy

def test_energy_decreases():
    sim = ThermodynamicSimulator(
        state={"x": 1.0, "y": -0.5},
        free_energy=lambda s: quadratic_free_energy(s, a=1.0),
        grad_free_energy=lambda s: grad_quadratic_free_energy(s, a=1.0),
        L=1.0,
    )
    F0 = sim.F()
    for _ in range(100):
        sim.step(dt=0.05)
    F1 = sim.F()
    assert F1 < F0, f"Free energy did not decrease: {F0} -> {F1}"
