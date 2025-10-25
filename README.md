# Thermodynamic Neural Networks (TNN) — Research Starter

Monorepo for **Thermodynamic Neural Networks (TNN)** research and early **TASP core** development.

## 🧠 Quick Start (with Conda)

```bash
# 1) Create environment
conda env create -f environment.yml
conda activate tnn

# 2) (Optional) register Jupyter kernel
python -m ipykernel install --user --name tnn --display-name "TNN Environment"

# 3) Run tests
pytest -q
```

Launch JupyterLab:
```bash
jupyter lab
```

## Layout
```
src/
  tnn/         # research models, equations, analyses
  tasp_core/   # early simulator API that will become TASP
docs/
notebooks/
tests/
assets/figures/
```

## Week 1 Checklist
- [ ] Literature survey in `docs/literature_survey.md`
- [ ] Conceptual mapping figure in `assets/figures/`
- [ ] Symbolic notebook `notebooks/thermodynamic_mapping.ipynb`
- [ ] Minimal simulator + one test

## Split Later
```bash
pip install git-filter-repo
git clone --mirror <YOUR_MONOREPO_URL> tnn-mirror
cd tnn-mirror
git filter-repo --path src/tasp_core --to-subdirectory-filter tasp
git remote add tasp <NEW_TASP_REPO_URL>
git push tasp HEAD:main
```