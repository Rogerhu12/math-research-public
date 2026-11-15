# Actual89：26 查询完整原件读回入口与接线

作者：geometry；日期：2026-11-15。状态：独立源码、请求及工作流草稿已冻结；仅作源文本、AST、shell 语法及已有 JSON/文件 SHA 核对。尚未执行本入口、未下载原大包、未导入数学模块，也没有新的科学结果。

本入口补齐 actual89 尚未在本地取得的导出数组证据。原 actual89 的 warm、所有 trial、QP 与 FD 结论已经从公开原件读出，不以本次 byte audit 作为这些结果或 request94 的前置门。本入口不重新解释原 success 标志，不改原方程、方向、预算、容差或验收。

## 1. 为什么需要独立 26 reader

已亲读冻结 shared25 reader `root_20261114_read_completed_twenty_five_prefix.py`：50,404 B，SHA256 `9239b31016fde72f55961bc33e36dd014d8cf051df8aaca1fb3f475f8494e8cb`。其传输和绝大多数数组检查已通用，但不能把它直接标为 26-query reader：`audit_domain` 明写 51,200 行、三个 `range(25)`、八个 MID、25 schema/source pins，以及“新增 LEFT465/endpoint465”的来源说明。

新独立文件为 `root_20261114_read_completed_twenty_six_prefix.py`：50,510 B，SHA256 `36743c90d689525b975cec0acc66cdfa8051588ff8ce38f61e52120ad94c8527`。新文件只改下列来源或有限布局元数据：

| 项目 | 冻结 25 reader | 本独立 26 reader |
|---|---|---|
| warm 目录 | `twenty-five-condensed-warm` | `twenty-six-condensed-warm` |
| reader schema | `completed-twenty-five-prefix-artifact-readback-and-byte-audit-v1` | `completed-twenty-six-prefix-artifact-readback-and-byte-audit-v1` |
| 数学 producer schema | `exact-constraint-twenty-five-query-condensed-complete-H-warm-v1` | `exact-constraint-twenty-six-query-condensed-complete-H-warm-v1` |
| 全角行数 | 51,200 | 53,248 |
| typed groups | 25 | 26 |
| MID 列表 | 八组 | 在原顺序中加入 MID479，九组 |
| 全局/局部列数 | 236,036 / 7,439 | 原值保留，仍须实际 payload 核对 |
| 捕获节点 | 465…486 | 同一节点集合；不增加 endpoint |
| reader 来源 | shared24 | 完整绑定上述 shared25 SHA |

35 个顶层类/函数定义中，34 个 AST 与冻结 shared25 原样相同。唯一变化的定义是 `audit_domain`；全部文本差异可精确反向还原成原 50,404 字节。`readout`、`source_audit`、NPZ 解码/拼块、condensed 检查、14 raw 检查、observer 检查、下载器接线和 `main` 均保持原 AST。完整 diff 与源级检查随稿，不导入新 reader 来作该比较。

## 2. 绑定的唯一实际大 artifact

本请求只允许 actual89 这一份完整 artifact：

| 字段 | 实际值 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| original request | `89` |
| run | `43671882961` |
| source commit | `032c513ab5db8aff98a6efca2070375418846098` |
| job（来源记录） | `132683564697` |
| artifact | `14145231618` |
| artifact name | `visible-followup-condensedqp-43671882961-1` |
| ZIP bytes | `687750414` |
| ZIP SHA256 | `e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583` |

这组值来自 root 已核的官方 metadata，并与已有 actual89 primary identity JSON 逐字段相等。本地仅核既有小 JSON 和源文本，没有取得该 ZIP。artifact 名称沿 actual89 原 condensed 工作流的 first-attempt 上传约定；运行时仍由冻结下载器核官方名称、run、id、size、SHA 和 head SHA。

实际父件从**同一 actual89 extraction 内的 `parent86/`**读取，不再次请求 actual86 或任何更旧 artifact：

| 原父件 | 绑定 |
|---|---|
| `parent86/warm-001.json.gz` | `d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e` |
| `parent86/driver-status.json` 的原 decoded bytes；兼容透明 `.gz` | `7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235` |

reader 核父 warm/status 成对关系、完整 `resume_producer`、actual89 新 warm/status producer，以及 FD 的 prepared SHA 和完整 producer。它不会把 parent86 改名为 parent84，也不会把历史 zero-tail provenance 改写成本轮真实非零 native 响应。

## 3. 26 个 typed queries 与来源

行序必须等于原 producer 保存的顺序：先全部 LEFT，再全部 MID；各组仍为原完整 2,048 个物理角。查询列表如下。

```
LEFT = (465, 466, 467, 468, 469, 470, 471, 472, 473,
        475, 477, 479, 480, 481, 482, 484, 485)
MID  = (473, 475, 477, 479, 480, 481, 482, 484, 485)
```

LEFT 的原 fraction 为 `0.17267316464601146`；MID 的原 fraction 为 `0.5`。这是身份声明，入口不会重新计算查询状态、Hermite 中点、角度、曲率或 beta。已作纯 JSON 核对：上述 26 项与 actual89 原 `model-000.json`、原 status 和原 `domain_operator_export.query_specs` 逐字相同。MID479 在本轮内，MID487 不在本轮内。

`audit_domain` 检查每个 block、query、gradient 和其每个 NPZ part 的 index/kind/interval/fraction/station；完整 rows、Gamma、Pi 分块按原顺序核 SHA，再核全部 beta 字节串。实际列映射必须为原 465…486 节点与三个 global-p 列；每一 block 的 global-to-local 整数映射、实际列并集和显式空 zero layout 均从保存整数数组核对。已有 `unchanged_left_component_model_sha256` 字段保持原名和原 canonical 规则；这里不冒用 request94 的新布局或新字段。

四个 actual26 数学/observer 入口来源独立锁为：

| 原 basename | SHA256 |
|---|---|
| `geometry_20261114_twenty_six_query_domain_operator.py` | `b5b72fde97ece27c034a5f1ae3c81f0c0288b4092050f63e96296f764e7068c8` |
| `geometry_20261114_twenty_six_query_condensed_warm.py` | `b9954eb5caffca7e3e001e66b07b0628a8275a22139ca3000cf527e258023197` |
| `geometry_20261114_twenty_six_query_condensed_response.py` | `17908d4cb301f2073ce6539a8fcdc218a434529586722f013202c69378933b01` |
| `geometry_20261114_twenty_six_query_collocation_observer_warm.py` | `e10055b6e6d5604d247ecfbe637f8ca01b2b1337a7a528da8e25cbe48e6b8b25` |

`source_audit` 还遍历原 status/FD 中的全部嵌套 Python/MJS SHA 声明，逐一核 checkout 中实际文件；同 basename 的冲突声明明确失败。未在本次 checkout 中出现的历史文件明确记为未独立文件核，不冒全部通过；四个本轮入口必须存在且逐 SHA 相同。完整 source count 由本次真实输出产生，不把 primary 的 62 数学 producer、66 FD source 数误当成包括所有历史/observer 声明的恒定数目。

## 4. 原件字节检查和导出范围

下载器仍为 `exact_20261114_fetch_pinned_public_artifact.py`，SHA256 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。只在内存中替实际 tuple、metadata head 绑定和 adapter schema；安全提取、完整 ZIP 验证、每个 member CRC/size/SHA、readonly 原件发布与 receipt 逻辑不变。

检查按以下顺序进行，原 outcome 与 trial/FD 小报告先写，随后才核完整导出字节：

1. 原 status/model、全部原 trials、accepted 和 nearest 标量视图；原 QP、C 比较、actual full-model evidence；原 FD。原值只复制，不重算任一 merit、norm、失败角、最坏行或误差。
2. `domain-operator/manifest.json` 的全部 NPZ。每个 archive 的完整 member 集合、dtype/shape/byte count、原 identity SHA、可用 raw SHA 均核；全 rows/Gamma/Pi/beta 分块再按原顺序核完整数组身份。
3. `condensed-array-manifest.json` 的全部声明文件与结果引用。完整 parts 清单必须逐 descriptor 一致，重复完整数组按相同 identity 去重记录，所有引用数仍记录。不会运行 H/B/BT、QR、CG 或任何 model action。
4. `condensed-root/status.json` 声明的全部 14 个原 raw 输出，逐文件 SHA/size/dtype/shape 核。仅靠这些导出件不能审原 RAM-only 完整 factor；输出保持 `full_factor_files_independently_audited=False`，不把它改成真。
5. 所有 `collocation-observer/evaluate-*.json` 和原 run summary，核保存的返回值/残差字节未改变标志，并复制原 argmax 读数。遍历原 model 中所有 midpoint NPZ 引用，核文件和各 member 身份；分别导出 present/matched 列表，是否覆盖全部保存 midpoint 文件使用实际 equality 结果，不凭期待写真。

NumPy 仅用于读取 NPY/NPZ、dtype/shape、C-order bytes、原父 JSON 数组到其声明 dtype 的字节比对和整数索引列表。没有数值模型 import、RHS、Jacobian、ODE、FD、QR、求根、矩阵作用、范数计算或新增区间算术。

`large-arrays/complete-original-byte-audit.json` 导出每项原 payload/数组身份及完整拼块报告；`large-arrays/complete-transport-receipt.json` 导出完整原 archive member 收据。五件原报告（status/model/FD/C-comparison/QP-summary）直接复制到 `large-arrays/original-reports/` 并核复制前后 SHA；不重序列化。

**读回 artifact 不再次复制数百 MB 的 NPZ/raw 数值 payload。** 它保存完整验证明细与原来源索引；完整 raw 原件仍由已锁 actual89 artifact 保持。这个范围与 shared25/已完成 actual86 reader 相同。本稿没有把未运行的新 reader 或未取得的 payload 写成 PASS。

## 5. 唯一 completed-reader 工作流接线

基线为 root 指定的 `visible-larger-public-completed-readback.yml`，20,778 B，SHA256 `8953f0c350fab99d1a1dedf73374c1b3414ffa9be80b2ada6412f62c3d5ab1de`。草稿不创建第二条并发入口；仍只有原 request path push trigger、同一 concurrency group，`cancel-in-progress: false`。

工作流文本只加四处 `prefix26`：source reader map、CLI reader map、prefix CLI family tuple，以及已有 publication-recovery allowlist。其余 step 正文、固定 setup、token scope、artifact/publisher、所有旧路由均逐字保持。实际 request 中 `recover_original_publication=false`；未请求 R276，所以两个通用条件 step 只正常退出，不能在回执中冒称执行了 R276 或恢复出版。

新 request 只锁三件可执行来源：本 reader、上述 512247 下载器、原 publisher `root_20261114_publish_actions.py` SHA256 `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。四个 actual26 科学入口只被读取 SHA，不导入执行。

runtime 沿原 Python 3.12.14、NumPy 2.3.5、固定 checkout/setup/upload SHA；原 job 120 分钟及 4 GiB 原件读取空间声明不变。这是 storage budget，不是数学门。仅 original-byte fetch step 与已有 publisher/recovery step 获 token；本请求不激活任何科学 step。原件中保存的父86已足够，无第二次 fetch。

实际 CLI 由工作流生成，等价于：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261114_read_completed_twenty_six_prefix.py" \
  --request-number 89 \
  --run-id 43671882961 \
  --artifact-id 14145231618 \
  --artifact-name visible-followup-condensedqp-43671882961-1 \
  --expected-size 687750414 \
  --expected-sha256 e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583 \
  --source-commit 032c513ab5db8aff98a6efca2070375418846098 \
  --parent-directory parent86 \
  --parent-warm-sha256 d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e \
  --parent-status-sha256 7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235 \
  --download-out "$RUNNER_TEMP/original-completed-43671882961" \
  --out "$VISIBLE_OUT/request89-readback" \
  --repository-root "$GITHUB_WORKSPACE"
```

唯一 request 目标仍为 `topics/visible-flex-larger-amplitude/computations/public-completed-readback-request.json`；lane 仍 `receipts`，上传名字仍 `visible-completed-readback-${run}-${attempt}`。科学 run89、后续 reader run 以及 request94 三者身份分开。本地没有 dispatch。

## 6. 失败保全和实际回执判读

原 scalar/status/trial/FD/QP 报告在 full payload audit 前保存。若后续检查失败，保留已读原值和独立 traceback，记录实际 failed stage；`original_successful_scientific_run_not_reclassified=True`，不把 byte/transport 错当原求解失败。

全部数组核完成时，实际 report 才设置 `completed=True`、`byte_audit_completed=True`。这些是本次读取工作完成标志，不是原 `success`、coupled/native/closed field 接受，也不是连续曲率、metric、reach 或 δE 证明。

完整 derived report 无论大小均留 artifact；有界 public summary 超过原 90,000 字节阈值时仅缩小公开视图，完整内容保留原 artifact 路径。这一文件传输机制不删 scientific arrays、不降低数值门。

## 7. 本地已完成的静态证据与冻结清单

独立文件目录：`/tmp/visible-larger-twenty-six-readback/`。请求目录：`/tmp/visible-larger-request89-readback/`。reader 全 diff、四处 workflow diff、86→89 request 全 diff 均在相应目录。

已完成：新 reader AST/compile-only；34/35 顶层定义 AST 不变；全部源修改可逆；既有四个26入口和三request pins 的原 bytes SHA；actual89 原 model/status/query metadata 的一致性；唯一 trigger/concurrency/三项变动 step 的结构比较；8 段 shell `bash -n` 与 5 段 inline Python AST/compile。上述检查程序不导入 reader，不执行 workflow 命令。

| 文件 | bytes | SHA256 |
|---|---:|---|
| 新 reader | 50,510 | `36743c90d689525b975cec0acc66cdfa8051588ff8ce38f61e52120ad94c8527` |
| completed-reader workflow 草稿 | 见冻结清单 | `0b11f0796b268e98812b18e167f2862336093ea983df5fd036dd1162499be720` |
| actual89 request 草稿 | 见冻结清单 | `3ac6ac20b7f993b9a71900283738f3dcf1758056823e88450e8bfc569345dca9` |
| request89 静态检查 JSON | 14,801 | `91e9d445e284ed55dbe098596f08c7242fcb4d47c16c2d2e25b905cb75f44b1f` |

source 及 workflow 没有待填科学 SHA，也没有新数学结果占位；未来 actual reader run/artifact tuple 必须等真实运行产生。root 统一审读、复制和普通 Git 发布，本稿不要求另设审核门，也不阻 request94。
