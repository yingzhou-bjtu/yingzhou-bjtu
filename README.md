<div align="center">

<img src="https://yingzhou-bjtu.github.io/images/avatar.webp" width="148" style="border-radius: 50%;" alt="Ying Zhou">

# Ying Zhou (周瀛)

**AI Infrastructure Engineer @ Moore Threads** · Ph.D., BJTU

Networking systems → efficient AI serving · MUSA runtime, model enablement,
graph-safe execution, and reproducible performance work.

[![Homepage](https://img.shields.io/badge/Homepage-Academic_Profile-224b8d?style=flat-square&logo=googlechrome&logoColor=white)](https://yingzhou-bjtu.github.io/)
[![Contributions](https://img.shields.io/badge/Open_Source-Contribution_Map-0e7490?style=flat-square&logo=git&logoColor=white)](https://yingzhou-bjtu.github.io/contributions/)
[![IEEE Xplore](https://img.shields.io/badge/IEEE_Xplore-Author_Profile-00629B?style=flat-square&logo=ieee&logoColor=white)](https://ieeexplore.ieee.org/author/37087009843)
[![Email](https://img.shields.io/badge/Email-22110019@bjtu.edu.cn-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:22110019@bjtu.edu.cn)

</div>

<table>
<tr>
<td width="33%" valign="top"><strong>NOW</strong><br>Inference Optimization Engineer<br><sub>Moore Threads · Beijing</sub></td>
<td width="33%" valign="top"><strong>BUILD</strong><br>MUSA runtime and AI serving<br><sub>Graph-safe execution · measured performance</sub></td>
<td width="33%" valign="top"><strong>RESEARCH</strong><br>Distributed systems and networks<br><sub>Federated learning · data-center infrastructure</sub></td>
</tr>
</table>

## At a Glance

- **Current**: AI Infrastructure Engineer at **Moore Threads** (摩尔线程)
- **Education**: Ph.D. @ BJTU (2026) · B.E. @ China University of Petroleum (Beijing), GPA **1/60**
- **Focus**: MUSA backend enablement, LLM/audio-model serving, graph-safe execution, and measured performance

## Highlights

| Area | Details |
|------|---------|
| Publications | TCE, ToN (CCF-A), ICASSP (CCF-B), INFOCOM/CCS under review |
| Awards | CUMCM National First Prize, Huawei Cup National 2nd/3rd Prize |
| Industry | AI Infra @ Qingcheng Zhiji, Algorithm @ China Mobile, Research @ SUAT |

## Selected Upstream Contributions

Authored pull requests across the production systems I work on. Open proposals and
merged changes are labeled separately; the links point to the upstream evidence.

| Project | Contribution | Status | PR |
|---|---|---|:---:|
| **SGLang** | Public MUSA JIT compilation through `mcc` | Open | [#51491](https://github.com/sgl-project/sglang/pull/51491) |
| **SGLang** | Shared `store_cache` contract for MUSA KV cache | Open | [#50916](https://github.com/sgl-project/sglang/pull/50916) |
| **SGLang-Omni** | MUSA audio and vocoder paths for MOSS-TTS | Open | [#3833](https://github.com/sgl-project/sglang-omni/pull/3833) |
| **SGLang-Omni** | FAST attention reuse for FishAudio S2-Pro | Merged | [#3829](https://github.com/sgl-project/sglang-omni/pull/3829) |
| **SGLang** | Portable breakable-capture status | Merged | [#47034](https://github.com/sgl-project/sglang/pull/47034) |
| **torchada** | Joint in-place RoPE provider | Merged | [#138](https://github.com/MooreThreads/torchada/pull/138) |
| **FlagTensor** | Initial MUSA backend support | Merged | [#14](https://github.com/flagos-ai/FlagTensor/pull/14) |

<sub>Status snapshot: 2026-11-19. Full contribution map:
[yingzhou-bjtu.github.io/contributions](https://yingzhou-bjtu.github.io/contributions/).</sub>

## Links

- **[Academic Homepage](https://yingzhou-bjtu.github.io/)** — full CV, publications & projects
- **[Open-Source Contributions](https://yingzhou-bjtu.github.io/contributions/)** — selected upstream PRs and systems work
- **[LoongX](https://github.com/jhlxp/loongx)** — SimAI communication layer extension

## Selected Public Repositories

| Repository | Scope |
| --- | --- |
| [FlowFish Streaming Clustering](https://github.com/yingzhou-bjtu/flowfish-streaming-clustering) | Streaming speaker clustering artifact with reproducible benchmarks |
| [PIFCA](https://github.com/yingzhou-bjtu/PIFCA) | Federated clustering method for non-IID client distributions |
| [Containerized Routing Network Simulator](https://github.com/yingzhou-bjtu/containerized-routing-simulator) | Docker-based OSPF/LISP network simulation |
| [Multipath Delay Measurements](https://github.com/yingzhou-bjtu/multipath-delay-measurements) | Relative-delay measurement dataset with DNS-derived IP metadata and packet captures |
| [paper-agent](https://github.com/yingzhou-bjtu/paper-agent) | Local Overleaf writing workspace tools and reproducible paper workflows |

<details>
<summary><strong>Profile scope and repository standards</strong></summary>

### Project Identity

See [docs/PROJECT_IDENTITY.md](docs/PROJECT_IDENTITY.md) for the profile repository scope and public project boundary.
See [docs/OPEN_SOURCE_STANDARD.md](docs/OPEN_SOURCE_STANDARD.md) for the repository hygiene and validation contract.

### Repository Notes

This profile repository is intentionally small. Project code, datasets, and
paper artifacts live in their own repositories; this README only keeps public
identity, current work, and stable links.

### Validation

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
Missing or unreadable README files are reported through the same
`PROFILE_README_CHECK_FAIL` contract instead of escaping as tracebacks.
Direct `ProfileReadmeSpec` construction accepts path strings, normalizes them to
`Path`, and rejects malformed, empty, or duplicate name sequences before any
filesystem access.

The validator also checks that the profile repository keeps its public support
files: `.editorconfig`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`,
`CODE_OF_CONDUCT.md`, and `CITATION.cff`. The selected repository table keeps
both the expected GitHub repository slugs and the expected display names under
validation so public links cannot drift silently.

</details>
