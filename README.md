<div align="center">

<img src="https://yingzhou-bjtu.github.io/images/avatar.png" width="180" style="border-radius: 50%;" alt="Ying Zhou">

# Ying Zhou (周瀛)

**AI Infrastructure Engineer** @ Moore Threads · Ph.D., BJTU

[![Homepage](https://img.shields.io/badge/Homepage-yingzhou--bjtu.github.io-blue?style=flat&logo=googlechrome)](https://yingzhou-bjtu.github.io/)
[![IEEE Xplore](https://img.shields.io/badge/IEEE_Xplore-Author_Profile-00629B?style=flat&logo=ieee&logoColor=white)](https://ieeexplore.ieee.org/author/37087009843)
[![Email](https://img.shields.io/badge/Email-22110019@bjtu.edu.cn-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:22110019@bjtu.edu.cn)
[![GitHub](https://img.shields.io/badge/GitHub-yingzhou--bjtu-181717?style=flat&logo=github)](https://github.com/yingzhou-bjtu)

</div>

## About Me

- **Current**: Joining **Moore Threads** (摩尔线程) as AI Infrastructure Engineer
- **Research**: Distributed networks, data center networks, federated learning, AI infrastructure
- **Education**: Ph.D. @ BJTU (2026) | B.E. @ China University of Petroleum (Beijing) (GPA **1/60**)
- **Contact**: 22110019@bjtu.edu.cn

## Highlights

| Area | Details |
|------|---------|
| Publications | TCE, ToN (CCF-A), ICASSP (CCF-B), INFOCOM/CCS under review |
| Awards | CUMCM National First Prize (Top 0.3%), Huawei Cup National 2nd/3rd Prize |
| Industry | AI Infra @ Qingcheng Zhiji, Algorithm @ China Mobile, Research @ SUAT |

## Links

- **[Academic Homepage](https://yingzhou-bjtu.github.io/)** — full CV, publications & projects
- **[LoongX](https://github.com/jhlxp/loongx)** — SimAI communication layer extension

## Selected Public Repositories

| Repository | Scope |
| --- | --- |
| [FlowFish Streaming Clustering](https://github.com/yingzhou-bjtu/flowfish-streaming-clustering) | Streaming speaker clustering artifact with reproducible benchmarks |
| [PIFCA](https://github.com/yingzhou-bjtu/PIFCA) | Federated clustering method for non-IID client distributions |
| [Containerized Routing Network Simulator](https://github.com/yingzhou-bjtu/containerized-routing-simulator) | Docker-based OSPF/LISP network simulation |
| [Multipath Delay Measurements](https://github.com/yingzhou-bjtu/multipath-delay-measurements) | Relative-delay measurement dataset with DNS-derived IP metadata and packet captures |
| [paper-agent](https://github.com/yingzhou-bjtu/paper-agent) | Local Overleaf writing workspace tools and reproducible paper workflows |

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=yingzhou-bjtu&color=blueviolet&style=flat-square" alt="Profile views" />
</div>

## Project Identity

See [docs/PROJECT_IDENTITY.md](docs/PROJECT_IDENTITY.md) for the profile repository scope and public project boundary.
See [docs/OPEN_SOURCE_STANDARD.md](docs/OPEN_SOURCE_STANDARD.md) for the repository hygiene and validation contract.

## Repository Notes

This profile repository is intentionally small. Project code, datasets, and
paper artifacts live in their own repositories; this README only keeps public
identity, current work, and stable links.

## Validation

Before updating the profile README, run:

```bash
python3 scripts/test_validate_profile_readme.py
python3 scripts/validate_profile_readme.py
git diff --check
```

To validate a staged or copied profile tree without editing the script, pass
the target paths explicitly:

```bash
python3 scripts/validate_profile_readme.py \
  --readme /path/to/README.md \
  --repo-root /path/to/profile-repo \
  --json-out /tmp/profile_readme_check.json
```

`--json-out` must be a `.json` file. If it is inside the profile repository, it
must live under `logs/` or `reports/`; otherwise, write it to `/tmp` or another
external artifact directory. Reports are written through a same-directory
temporary file and atomically replaced.

The validator also checks that the profile repository keeps its public support
files: `.editorconfig`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`,
`CODE_OF_CONDUCT.md`, and `CITATION.cff`.
