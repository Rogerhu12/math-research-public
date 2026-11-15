# 第82轮：真实 actual80 父状态的显式阻尼续接请求草稿

日期：2026-11-15。根代理已完整读取新源、源接口、工作流/请求与本接口，统一接入公开仓库；本接口记录发起前的冻结设计。源级与输入字节检查完成；没有本地科学调用，也没有假填未来 run、source commit、artifact 或结果 SHA。

## 可直接接入的两件

- workflow：`.github/workflows/visible-larger-public-small-core-resonance.yml`，草稿 `visible-larger-public-small-core-resonance.yml`，15209 B，SHA256 `00af44968eb98a06f81845922151e0eb52baf123f35a9f93ac4359747ae0dd4a`。
- request：`topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`，草稿 `public-small-core-resonance-request.json`，17649 B，SHA256 `d10fddcc60339921a418e70dbc1b51b7c1df505bf511d6aa435d664a81dea3f7`。

唯一触发仍为原 computations 目录内 request push；lane、job key、concurrency 和 artifact 名称模式仍为 `smallcoreresonance`。没有第二个触发请求或并发旁路。

## 源与父原件

新增第70个源：`geometry_20261115_small_core_damped_resume.py`，15452 B，SHA256 `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a`。原69件 pin 逐项保留，包含 `1691c7d9…` 实际方向引擎、`3b9c45ab…` 原 R259 model/checks、原78 source restore、完整 source-dependencies 和 publisher `22e640bb…`。

源接口：`2026-11-15-small-core-damped-resume-interface.md`，9715 B，SHA256 `439616d4594f767e7dae986e29fc856673b1833ba495a5aa01e2c935979c916f`。request `source_chain` 明确三层 producer；不会把新 resume source 称为未变原科学源。

父来源是已完成真实第80轮：run `43664043053`，source `5a17ad802c28a0a00f2776201cea4cef27f68da7`，job `132659392179`，artifact `14141985111`。只需要已公开的小 status：

`topics/visible-flex-larger-amplitude/notes/public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/damped-search-status.json`

52985 B / SHA256 `ebe5b50c6af5ec9cfbe201e4d19a1b24dc9357e28ac8fe89354d5c04fd13ee2a`。

checkout sparse 精确加入此文件，替换上一请求 actual78 immediate parent。四件数学输入、其 bytes/SHA、原 Python3.12.14 / NumPy2.3.5 / SciPy1.17.0 / python-flint0.9.0、BLAS 单线程保持实际80。没有新增 native 请求。

## 唯一实际参数候选

初始参数由父 `final.parameters` 原字面值给出：

`[0.09071772300091886,-0.13939413969182854,-0.12252606423015384]`。

请求显式选择 `damping="0.1"`、candidate steps8、backtracks20。原 Armijo、未加权 merit、真实 gdot、域异常、1e-8候选读出、FD三档、Arb160/depth14和完整圆参考都保留。该 η 候选基于实际80八次全步接受且低模残差仍大的事实；没有宣称根存在、唯一原因或必成功。

CLI 与原80相比只增加 `--parent-status-sha256`，换新 source、真实父文件、显式 damping 和输出路径；不传伪 `--parameters` 覆盖父值。全部70个 source 原字节、四输入和真实父状态先核来源，科学命令只有一次 subprocess 调用。

## 输出和失败范围

新的主要输出是 `small-core-damped-resume/damped-resume-status.json`，schema 为 `R259-original-three-equation-column-scaled-LM-resume-v1`。原父 bytes 在 `prior-candidate/actual80-damped-search-status.json` 和新入口自己的完整父副本中分别保留。原大最终 Arb/circle仍完整落盘，所有失败文件仍由原 `always()` artifact 上传覆盖。

`request82-input-and-source-identity.json` 记真实触发 commit、requestSHA、70源码、四原输入与 actual80 父身份。命令 receipt 记录 `source_chain` 与新 argv。只读输出阶段复制新 status 的原字段，另保 source/engine/parent 身份；不计算新科学量，不给 workflow success 赋予 candidate 或 native 成功含义。

作业60min、科学步45min及原全部 runtime 环境不改。token 仍只在原 publisher step 的环境中；科学 step 无 token 环境。原 public78 restore 和 publisher 普通 pull/rebase逻辑未改。

## 静态证据

21项 workflow/request/源字节核全部通过：70 source hashes，7个 shell 块 `bash -n`，4个 inline Python AST。原 checkout/actions pins、runtime install、public78 restore、artifact/publisher step 字典逐项未变。原四大数学输入只按实际80描述器保持，未本地重算或导入模型。

完整差异为 `workflow-from-actual80.diff`、`request-from-actual80.diff`；基线由真实80 source commit 的 Git 原件读取，分别保存为 `baseline80-workflow.yml`、`baseline80-request.json`。`source-only-static-check.json` 及 `check_request82.py` 保完整核验范围。此处只准备第82轮，任何新结果必须等待其真实 Actions 回执。

## 仓库内静态记录文件名

为避免覆盖既有通用文件名，源级 `source-only-check.json` 保存为 `2026-11-15-small-core-damped-resume-source-static.json`，源完整差异保存为 `2026-11-15-small-core-damped-resume-source.diff`。工作流原静态记录保存为 `2026-11-15-request82-source-static-check.json`；两差异分别为 `2026-11-15-request82-workflow.diff`、`2026-11-15-request82-request.diff`。上述原记录和差异均保持原字节；源码接口仍为原439616d4。root独立70源SHA/AST、7shell/4inline检查见 `2026-11-15-request82-root-static-check.json`。这些来源核验不新增科学门。
