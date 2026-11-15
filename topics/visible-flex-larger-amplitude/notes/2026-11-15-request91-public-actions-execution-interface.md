# Request91：四行精确贡献诊断的独立公开 Actions 接线

类型：已实现的执行接口与静态源码事实；新科学读数尚未产生。  
作者：ChatGPT，`exact_refinement`。  
日期：2026-11-15 UTC。

本文件配合[四行完整贡献与相邻词算术接口](2026-11-15-request91-four-row-attribution-and-word-spacing-interface.md)。该算术源与运输源保持原冻结字节。本文件只说明独立 workflow、固定实际输入、产物路径、资源与发布范围；没有派发 job、产生未来 run/result 身份或本地执行科学。

## 1. 独立文件与触发范围

| 建议仓库路径 | 字节 | SHA256 |
|---|---:|---|
| `.github/workflows/visible-larger-public-native-four-row-attribution.yml` | 13264 | `a43bfa7353749caeb1b11e2fcd0ae6247238d096afe785a278f6fc3f35c6b410` |
| `topics/visible-flex-larger-amplitude/computations/public-native-four-row-attribution-request.json` | 4701 | `96aa71a7e56588ff28885236bf036b3465fddf5e62c7802414887b78a5078a23` |

这两个文件目前只在 `/tmp/request91-workflow-draft/`。root 负责把它们与两份已冻结新源一起正常提交；本交付不修改旧83 workflow/request 或任何分支。

唯一 trigger 是 `main` 上新的 `public-native-four-row-attribution-request.json` 路径。独立 concurrency 为 `visible-larger-public-native-four-row-attribution`，`cancel-in-progress: false`，不取消83、73或其他当前计算。job 与现有 publisher lane 使用 `modelresponse`；研究身份始终是 request91 四行诊断，不借 lane 名冒称83重跑或原 native 成功。

请求 schema 为 `public-actual83-four-original-row-attribution-request-v1`。它把两个真实 artifact、原 J chunk、四行顺序、源 SHA、资源和新算术范围完整写出；未填写未来 run、artifact、数值结果或接受标志。

## 2. 完整运行源闭包

| 文件 | 字节 | SHA256 | 本次用途 |
|---|---:|---|---|
| `exact_20261115_actual83_four_row_state_formation.py` | 41270 | `17659d25b5f24d21843c188f845247ce3a132a7462e28d7b4fbcdf59db17bc8c` | 独立新的四行精确贡献与相邻词算术 |
| `exact_20261115_fetch_actual83_four_row_inputs.py` | 10726 | `e3dae97ae649dadd46cf77508e84b8573daaff30a77c14cc6f7c0a77a3bc6c92` | 固定83全包或73一块的纯字节取入 |
| `exact_20261114_fetch_pinned_public_artifact.py` | 28006 | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` | 不变的公开 HTTPS／完整 ZIP／安全提取内核 |
| `root_20261114_publish_actions.py` | 14455 | `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` | 原既有 bounded publisher、普通 pull/rebase/push |

Python 为固定 `3.12.14`。科学与运输都是标准库；不安装 numpy/scipy，不启动 Node，不恢复78源，不 import 原 native、RHS、J、QR或求解模块。checkout 仍是固定 `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`，setup-python 仍是 `a26af69be951a213d495a4c3e4e4022e16d87065`，upload-artifact 仍是 `ea165f8d65b6e75b540449e92b4886f43607fa02`。

原83科学源及全部原 source 身份在已经固定的83 result/input-binding中保留。本次科学源读取该来源，但不再次执行原83全系统作用、原73 QR或原 noJ。

## 3. 两个实际 artifact 与必要单块

| 输入 | 完整固定 tuple |
|---|---|
| 实际83 | run `43668743706`，source `8d199eda5c1f1df162ded244e8dfd012e0c8d127`；artifact `14143009723`，name `visible-mainline-modelresponse-43668743706-1`；ZIP 48375172 B，SHA `9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c` |
| 原73 | run `43657001633`，source `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`；artifact `14141540502`，name `visible-mainline-nojprimalnative-43657001633-1`；完整 ZIP 1752742419 B，SHA `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9` |

83完整提取。原73下载、完整流式大小／SHA验证后，只提取：

```text
native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le
```

该实际原件为1605632 B，SHA `fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677`，`<f8`／C／shape `[4,224,224]`，`chunk_index=2`、`row_start=8`、`row_stop=12`。其 descriptor 与83原 input-binding交叉绑定。

原73运输只对这一个选中成员逐字解压／CRC／SHA；其他成员做中央目录路径、重复、符号链接、特殊文件等安全检查，但**不声称对未提取成员做过单独解压或CRC**。完整原 ZIP SHA仍全部核完，不能把网络范围写成“只下载1.6MB”。两个临时ZIP按冻结内核在完成后删除，不删除任何科学输出。

## 4. 按真实执行顺序的路径与 CLI

### 4.1 输出和检查

工作目录维持触发 `GITHUB_SHA` 的 sparse checkout；不会让运输或新算术改该源 checkout。读取根README、题README、HANDOFF和本题computations，关闭自动gc／maintenance。

`VISIBLE_OUT` 设为：

```text
$RUNNER_TEMP/visible-actual83-four-row/modelresponse
```

前置step读取请求，核四源完整SHA并只用AST解析源；核固定两个artifact tuple、chunk、四行及Python版本。只记录实际 `git rev-parse HEAD`，要求与当前 `GITHUB_SHA`相同。双README沿实际已读blob：根`6183b7f3eaa5edf22cd1a62fa19d84bf4ab3ba09`，题`bff8aea253a9e6a7a4fac28d810ac454c5499fec`。若新规则改变，会停止这个旧规则下尚未开始的请求，供root读取真实变化；不是新科学接受门。

实际identity写`request91-input-and-source-identity.json`。空间检查写`request91-input-storage.json`，明确两完整ZIP、单块选择与保存范围。

### 4.2 两次取入

```bash
python -u "$VISIBLE_COMPUTATIONS/exact_20261115_fetch_actual83_four_row_inputs.py" \
  --input actual83 \
  --out "$RUNNER_TEMP/request91-actual83"

python -u "$VISIBLE_COMPUTATIONS/exact_20261115_fetch_actual83_four_row_inputs.py" \
  --input original73-j-chunk \
  --out "$RUNNER_TEMP/request91-original73-Jchunk"
```

每次helper自己给原512247内核完整五个固定artifact CLI flags，workflow不另维护不完整的旧parser参数。新目录必须不存在；完整取件receipt仍为`_pinned_public_artifact_receipt.json`。API元数据还核原source commit，不靠目录名推原来源。

`GITHUB_TOKEN`仅放在这两个取件step的环境，由原内核使用；没有PAT、签名URL或token进入request／源／日志。跨host重定向剥离Authorization与HTTPS要求保持冻结内核实现。

两步日志分别为`actual83-complete-fetch.log`和`original73-one-J-chunk-fetch.log`。后续`always()`字节保全step复制实际存在的两份完整receipt；若单J已取入且SHA正确，先把该原件保到：

```text
$VISIBLE_OUT/large-arrays/request91-pre-arithmetic-inputs/
  native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le
```

因此即使新的算术失败，这一确实支付了完整大包运输的原块仍进入产物。该step仅复制／hash字节，记录`request91-available-transport-and-J-receipts.json`，不宣称诊断已经完成。

### 4.3 单独的新科学step

```bash
python -u "$VISIBLE_COMPUTATIONS/exact_20261115_actual83_four_row_state_formation.py" \
  --actual83-directory "$RUNNER_TEMP/request91-actual83" \
  --original73-chunk-directory "$RUNNER_TEMP/request91-original73-Jchunk" \
  --out "$VISIBLE_OUT/actual83-four-row-attribution"
```

这是**新的科学算术**，不是byte-only读者。step名称明确写`Compute new exact contributions...`，没有凭据环境。它只对以下原行计算全部224入列和出端直接负项，按原83八向量行账核总和；相邻词／精确比例／最近偶数舍入同样只在此Actions step运行。

| global row | stage／local row | 入端节点 | 出端节点 |
|---:|---|---:|---:|
| 2539 | 10／187，Pi76 | 11 | 10 |
| 2536 | 10／184，Pi73 | 11 | 10 |
| 2762 | 11／186，Pi75 | 12 | 11 |
| 2128 | 9／0，Q1 | 10 | 9 |

完整896个相关状态坐标、全部列、原sigma、实际flow输出／目标词与已经归一的norm标量分开保全。它不再把norm除一次sigma。原alpha仍1/512；没有新RHS/J/ODE、QR、solve或trial，没有改变eta、容差、原方向或接受规则。

## 5. 资源、失败与发布

运行节点为原`ubuntu-latest`，job timeout保持120分钟。两取件step明确15分钟／30分钟；新算术step30分钟。这里是执行资源上限，不是新的数学阈值或对预计耗时的数值结果。

最低空闲为4294967296 B（4GiB），取件顺序执行。主要临时对象是原73的1752742419 B完整ZIP；83约48MB的完整ZIP和约49MB解包、一个1.6MB J块以及诊断输出另保。它不是多轮native的存储上界，不缩减任何原科学预算。BLAS线程环境保持1，但本次没有BLAS调用。

`always()`upload先保存所有实际输出与部分失败，artifact名称仍使用既有lane格式：

```text
visible-mainline-modelresponse-${run_id}-${run_attempt}
```

名称中的真实run与attempt只由Actions注入；本稿没有未来实际值。upload压缩级别1、保留30日、无文件则warn，使用固定官方actionSHA。

随后既有`22e640...`publisher以`--lane modelresponse`正常Git发布有界小件。`GH_TOKEN`只放在该发布step，保持真`pull --rebase`、双README变化检查、NFF立即重试、不force及HANDOFF规则行专用合并。全部路径含`large-arrays`的原件、完整有理结果／逐列账只在artifact；publisher保其哈希和小summary，不需要改共享白名单。

科学源成功后还会在自己的`large-arrays/original-inputs/`保完整J块和原15数组。这与前置1.6MB保全有一个小原件副本重复，目的分别是诊断完整自包含来源和失败时先保运输所得；没有删除或覆盖原证据。

任何前置失败不会继续新的科学step。`always()`保全和发布仍尝试记录实际已有文件。独立诊断是否完成不改83/73 outcome，完整输出不会被当作未来native派发的新增门。

## 6. 相对已实际执行83的完整差异

比较基准固定为实际83源提交`8d199eda5c1f1df162ded244e8dfd012e0c8d127`：

| 比较文件 | 字节 | SHA256 |
|---|---:|---|
| 原83 workflow | 14152 | `54e24e4527e58a5b4c2f67f32be89f3ff9de5c5af0adb1d8a8aa22f2e6936bf4` |
| 原83 request | 5120 | `90da387ca0e9fa57b22e89bce34a8692f1e4e1ffa993542d5b38be9f175c68b8` |
| `request91-workflow-versus-published83.diff` | 24711 | `e0ca709ba7ec5486769a144ab24cc517ee94503f41d5889f4c37aed1668987e3` |
| `request91-request-versus-published83.diff` | 9817 | `6342837b17c1577620a5cc718b4aea45f0686aba2d965dcc00ee1292297d306f` |

保留原checkout/setup/upload版本、公共repository、普通publisher、lane和partial evidence规则。新trigger、concurrency、输出根和请求独立；原一次noJ+全系统exact步被两个原件取入与四行诊断替换。原20源闭包收为真正调用的3源加publisher；Node、numpy/scipy、原78恢复以及83的R276小参考输入都不再是运行依赖。原R276/83科学事实通过83实际固定result和input-binding读取，不再复算。

## 7. 已完成的本地静态事实

`2026-11-15-request91-workflow-static-check.json`为6623 B，SHA `7bc23af6b0b07dc1c699310f2c83c63f0fcfdd00bb4a0450f34d5e294383f3f2`。

它实际记录：四份源SHA与AST通过、8段Shell逐段`bash -n`通过、3段内嵌Python的AST通过、固定输入tuple/chunk/四行与两源常量匹配、完整CLI flags匹配、两个取件token与一个publisher token的独立范围、独立trigger/concurrency、`always()`保全，以及`large-arrays`沿现publisher仅artifact。

检查器只读源码／YAML／JSON并调用`bash -n`。没有运行任何workflow内嵌Python、运输模块、科学函数、Fraction、矩阵、norm、相邻词、RHS/J/QR，也没有下载原artifact、Git修改或dispatch。它证明接线已进行静态检查，不是假造运行成功或新数学结果。
