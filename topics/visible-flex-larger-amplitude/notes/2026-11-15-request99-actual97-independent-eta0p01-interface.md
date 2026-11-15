# Request99：实际 97 末点的独立 η=0.01 续接入口

类型：可执行源码接口与静态核对；包含原 Actions 字面读数，不包含新的数值结果。  
作者：exact_refinement（协作代理）；主控负责发布与实际调度。  
日期：2026-11-15（UTC）。

## 1. 已交付的改变

本请求从实际 request97 的最后一个 **完整三方程 merit 已接受点**继续，执行一次明确的 η=0.01 试验。旧 `geometry_20261115_small_core_inexact_p3_restoration.py` 的 SHA 为 `ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e`，其 `main()` 把阻尼固定为 `.1`。直接给这个旧入口传 `--damping 0.01` 会在科学模型开始前报错。因此，本次创建独立入口和新 schema；旧源保持全部原字节，也不作为第二个求解器执行。

新入口是 `geometry_20261115_small_core_inexact_p3_eta_0p01.py`，46,126 B，SHA256 为：

`f43c20ea6b8a5616b4330870897a1d0b6bd2c157435544366af1fe70dcdff7bd`。

它固定检查有限的 `damping == .01`。复制的原 Schur 方向、内层恢复、完整原三方程 merit、实际完整 J 斜率、`.2 Armijo`、全部外层及内层回溯、原最终诊断，保持原函数正文。新的来源、父件及阻尼声明不能标成“同一 ce93 源仅改 CLI 参数”。

源码内的新输出 schema 为：

`R278-original-three-equation-inexact-p3-restoration-LM-eta0p01-v1`。

输出相对目录仍是 `small-core-inexact-p3-restoration`，主文件仍是 `inexact-p3-restoration-status.json`。因此既有完整输出保全与字面读回可以继续使用；实际 JSON 的 schema、producer SHA 和 source closure 都是新的。

## 2. 实际父件与本次动机的范围

唯一初始父件来自实际公开 run `43676647334`，source commit `15b2028e039d2b93ea01b3bf6ef8c1fed8db15ed`，job `132698148882`。原 artifact 为 `14146527398`，478,758 B，ZIP SHA256：

`f041c43023cd5d431d5cb44e7991ed8345050859baf7e228c894c9a71b3fd06b`。

本次不重新下载该 artifact。主控已经唯一下载并验证完整包；本地准备只读取其中已存在的原 JSON/字节。

工作流稀疏取入的公开父件路径是：

`topics/visible-flex-larger-amplitude/notes/public-actions-43676647334-1-smallcoreresonance/small-core-inexact-p3-restoration/inexact-p3-restoration-status.json`。

文件大小 **233,256 B**，SHA256：

`d55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331`。

只复用它的 `final.parameters`：

```json
[0.5050366803948241, -0.3310221447104421, 0.5931424079355273]
```

实际 97 的八个外层方向都在首个 `alpha=1` 试探接受，停止原因是原字符串 `explicit outer direction budget completed`，没有顶层 exception。原 merit 从 `16791.96200276451` 变为 `15400.321596660777`；最终单位缺陷为 `[-175.4927978505483, 1.7091213848475404, -5.313809937131531e-08]`。单位停止标志和完整 112 行候选标志均为 false，native/nonzero/BVP 解也没有被取得。

原最后一个方向模型记录的弱奇异分量 retention 为 `0.9956458018520519`，该模型的 η 为 `0.1`。**这是最后一次试探前的方向基点，不是最终接受态。** 它的参数为 `[0.5051360438036447, -0.33246925937903155, 0.5930685269229757]`。本请求不把该谱改贴到最终点，不在本地重新计算 η=0.01 的方向或预测，也不从该值推出 η 是唯一原因、单行或整体单调改善。

η=0.01 是主控明确选定的一次算法试验。它没有扫描值列，没有减少原约束，也没有提前宣称更好的实际 merit、共振根或原非线性接受。下一次科学结果由原完整模型与原判据决定。

完整原父件按字节复制在本交付目录 `actual97-original/inexact-p3-restoration-status.json`。`actual97-parent-literal-readout.json` 保存实际原字段、最后方向模型及 literal parameter bits；它只做 JSON/字节读取。

## 3. 13、14、73 三个来源范围

| 范围 | 数目 | 精确含义 |
|---|---:|---|
| 实际 97 producer closure | 13 | 原 ce93 加其十二个冻结依赖；这就是父 status 的 `consumed_source_sha256` |
| 新 producer closure | 14 | 上述十三源加本次新的 η=0.01 入口 |
| Request99 全工作流 pins | 73 | request97 的全部 72 个 source pins 原样保留，再加新入口一项 |

新入口的 `FROZEN` 恰好等于实际 97 的完整十三源字典。`checked_sources()` 再加入新入口自己的真实文件 SHA，形成新的十四源身份。没有将父十三源冒成新 producer 的完整闭包。

原 ce93、3b48 内层根入口、ec9 恢复入口、1691 原方向入口是不可变的来源/算法基线；本次不会依次执行这些入口。新入口只按原路径 import 冻结 `geometry_20261114_small_core_resonance.py`（`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`），用其原 CircleReference、方程、完整参数 J、setup 与最终检查。原数学依赖和原公开 78 源恢复保留。

首次父件分支要求：

1. CLI 指定的完整文件 SHA 与实际文件字节相同；如果文件是 gzip，另外保留压缩和解压身份。
2. 解压后的内容必须是上述实际 97 的 233,256 B / `d55b…`，不是另一个同 schema 文件。
3. 原 schema、ce93 producer SHA、完整十三源、四数学输入、完成标志、未声称 native/nonzero 解的标志，以及最后接受点语义均匹配。
4. 三个初猜参数直接来自 `final.parameters`；不采用最后一个未接受内层 probe。

后续 own-schema 分支保留，但它要求 **新 schema、新入口实际 SHA、新十四源全部相同**，并要求原最后接受点语义。它不会把旧 ce93 输出泛化成新入口输出。父件保存的 damping 作为元数据如实记录；不会错误地要求旧父的 η=0.1 等于新入口的 η=0.01。

工作流另外保存完整 `request99-input-and-source-identity.json`，其中区分 `parent_source_closure` 和 `current_producer_source_closure`。原父件按字节另存 `prior-candidate/actual97-inexact-p3-restoration-status.json`；producer 自己亦保留 `parent-status.json` 原字节。

## 4. 原模型、预算和判据

四个原数学输入保持原路径和原 SHA：

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| actual accepted M96 | 2,614,352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| complete prepared112 | 4,220,043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| true T112 zero heightJetJacobian anchor | 6,815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| original T112 config | 2,161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

完整相对路径都在 request 的 `inputs`。当前 sparse 本地树缺少的输入，只与已保存实际 97 的真实输入 receipt 对照；静态回执逐项区分是否实际存在、是否本地重哈希。这里不冒称重新取得了缺失 payload。Actions checkout 后仍对四份完整输入逐字节数/SHA 验证。

预算和原规则保持：外层最多 8 个方向，每个最多 20 档；内层最多 12 次更新，每次最多 20 档；原单位目标 `1e-8`；最终 Arb `160 bits`、深度 `14`；完整原 699 节点、112 模态、原角度网格和一个原 RHS worker。job 仍 60 分钟，科学步骤仍 45 分钟。Python `3.12.14`、NumPy `2.3.5`、SciPy `1.17.0`、python-flint `0.9.0`、BLAS 单线程原样保留。

完整当前残差 `r3` 仍进入原 `n3=-r3/J33` 和 normal-plus-Schur 构造；从未覆盖为零。完整实际 J 必须在当前实际点形成。内层达到 `1e-8` 仍是原努力目标，其未达值不是新增外层禁行条件；最后实际有限候选点与自己的完整 J，仍交给原完整三方程 merit、实际 `r·Jv` 和 `.2 Armijo`。实际恢复位移继续与 `alpha*v` 分开保存。

单位方程的迭代停止阈值和完整 112 行候选标志是不同对象，均保持原定义。完整原 FD、scalar Arb 和 zero-core circle 检查全部仍执行。绿色 job 或 `diagnostic_completed=true` 不表示这两个数值标志已真，也不表示高 109 非共振、原 BVP、非零 native 或最终几何目标已完成。

## 5. CLI 与 Actions 接线

新入口 CLI 保持原参数集合，仅新文件名与固定 damping 值变化：

```text
python -u geometry_20261115_small_core_inexact_p3_eta_0p01.py
  --accepted <原 accepted M96>
  --prepared <原 complete prepared112>
  --tail-anchor <原真实 T112 anchor>
  --tail-config <原 T112 config>
  --parent-status <上述实际97完整status>
  --parent-status-sha256 d55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331
  --damping 0.01
  --candidate-steps 8 --backtracks 20
  --inner-newton-steps 12 --inner-backtracks 20
  --candidate-resonance-tolerance 1e-8
  --interval-bits 160 --interval-depth 14
  --out <fresh>/small-core-inexact-p3-restoration
```

只有 `Rogerhu12/math-research-public` 的 Actions 可以执行科学入口。本地没有 import 新/旧数学源，也未创建科学输出。

交付工作流仍对应 `.github/workflows/visible-larger-public-small-core-resonance.yml`，唯一 push trigger 仍为 `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`。既有 smallcoreresonance concurrency、`cancel-in-progress=false`、公开仓库限制、checkout/setup/upload 的固定版本、自动 gc/maintenance 关闭和 token 范围保持。

科学子进程没有新增 token；`GH_TOKEN` 仍只在最后 publisher 步骤提供。publisher 保持 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` 和既有 smallcoreresonance lane。原完整日志、trace、inner 报告、circle/Arb 输出及失败 partial 都走 `always()` artifact 保全。`large-arrays` 仍只存 artifact，不把数值大对象写入 Git。

实际科学入口的参数由 request 动态组成，所以 `PYDIAGNOSTIC` 的正文逐字同 request97。恢复原 78 源的 `PYSOURCE` 和仅复制原结果的 `PYREAD` 也逐字同 request97。状态文件的原完整 schema 会透传为新值，不改贴成 ce93。

## 6. 差异与已实际完成的静态核对

同目录包含：

- `producer-from-ce93.diff`：新 producer 对 ce93 的全部差异。
- `workflow-from-actual97.diff`：工作流全部差异。
- `request-from-actual97.diff`：请求全部差异。
- `request99-producer-source-only-check.json`：逐项字面编辑、完整逆变换、函数正文/AST 和来源闭包核对。
- `request99-static-check.json`：所有 source pins、父件/输入 receipts、工作流及 shell/inline 静态核对。
- 两个 source-only builder 与独立静态 checker：可复核创建过程；没有调用科学函数。

实际完成而非预期的检查为：

1. 新源全 AST/compile-only 通过；全部声明改动逆变换后，完整 45,133 B 原 ce93 逐字恢复。
2. 顶层 12 个未修改函数/类的完整正文及 AST 都相同。仅 `checked_parent` 与 `main` 的声明、父件、固定 damping 检查和状态 provenance 发生明确变化。
3. 从 `start = time.monotonic()` 起的整个 try/search/final-diagnostics/finally 主体逐字同 ce93，包括所有原数学和最终输出过程。
4. 全部 73 源逐 SHA 核对，原 72 项字典逐项相同；所有 Python 源只做 AST/compile，不 import。
5. 实际 97 完整父件及新目录复制件逐字相同；父十三源、新十四源与四输入均精确核对。literal 三参数只 pack 成 binary64 检查对应位，不做任何新模型运算。
6. 7 个 shell 段 `bash -n` 通过；4 个 inline Python AST/compile 通过。除 PYPINS 外三个 inline 正文全部逐字同原。
7. 工作流变动只在 checkout 父路径、来源绑定步骤和科学步骤标签；科学调用正文及原资源预算未变。

这些检查没有执行工作流命令，没有本地科学计算、Git 写入、网络下载或 dispatch。它们不构成新增数值接受条件。

## 7. 冻结文件与待实际结果

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| 新 producer | 46,126 | `f43c20ea6b8a5616b4330870897a1d0b6bd2c157435544366af1fe70dcdff7bd` |
| shared workflow 草稿 | 27,537 | `5a562ff17f0c202fd918ccb9208609938091ff9150619698305b7ef6b834926e` |
| request99 草稿 | 32,927 | `05d12abc4134f508d4682d8deece2ce857ad989d70de16ccc1ed4d133f724daa` |
| producer source-only receipt | 11,461 | `42f2763eaf814919ba996565b2d68020fc3ba5b1ce5044756e54f35b907b341c` |
| 完整静态 receipt | 35,589 | `9fdcfdee4f110f1f54a730617a6cbec4beb1efe75c25519016800f8d1cb43a32` |

实际 request99 run、source commit、artifact、参数更新、merit、单位/full112 标志、FD/Arb/circle 结果现在都尚未产生；没有填入未来身份。主控收到本完整可执行交付后负责唯一发布、调度和下载。后续原输出应先读科学状态和实际接受，再独立记录源/字节身份，不让字节附记阻止原算法推进。
