# 2026-11-14：R251 完整 prefix 的可执行区间证书入口

状态：**新增源与可复核接口，尚无本入口的 Actions 数值结果**。环境不可用后按根 README Rule 8，通过 GitHub 小文本接口保存新 blob。没有在本地执行科学数值，没有修改原求解、尾部、读出或接受门。三个新文件均待公开仓库自己的 Actions 做 compile/import 与实际运行。

## 1. 原件与范围

| 文件 | Git blob | SHA256 |
|---|---|---|
| [单 cell 原语](../computations/geometry_20261114_direct_operator_cell.py) | `4b3731027eb3b23c2c89fb8e4d52ac6b0522033c` | `1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce` |
| [完整 prefix 与 scalar exporter](../computations/geometry_20261114_full_prefix_operator.py) | `84200aeb18a507b5b7482b966a80c61d989992f3` | `a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703` |
| [三个解析场接口核验](../computations/geometry_20261114_operator_interface_check.py) | `231a4e9473039016772e5f48b9f9002922b2cde7` | `ae58f455992523327991a784bb935012121be3850bc0da33bb40f46c197f389f` |

文件大小依次为 20,431、40,466、11,341 bytes。单 cell 文件是故障后重新构建的 v2 身份，不能冒作故障前未推送的 `60600e...` 文件。

数学对象沿用 [R251](../results/R251-direct-relative-operator-metric-certificate.md) 和 [同源 scalar 分片包络说明](2026-11-14-complete-scalar-piecewise-envelopes.md)：

- 输入必须是原完整 saved reader 真正接受的 v3/v4 全 DN 场；prepared 或 failed 输出不能进入消费者。
- 物理场是全部共享 binary 节点及 0/1/2 径向 jet 定义的实五次 Hermite 场。整个 `z0` 和所有模均保留。
- 默认调用 R249 的 `read_saved(..., normalize=True)`，直接检查第一单元的入口规范形。三 nodal SHA 使用与原 normalizer 相同的 `str(shape)+NUL+little-endian f8 C-order bytes` 约定。
- 标量 prefix 采用原精确 scalar Hermite 定义，保留全部三个 `p*` 和各 bump 的实际 stored width。连接段仍为原 48/64 点 finite-Gauss 实表达式，没有换成精确积分或新拟合多项式。
- 完整材料密度继续由原 saved reader 的 R237 有理界证明为正，并绑定本次全部 core 系数 hash。

单 cell 原语始终注明 `scalar_envelopes_verified_here=False`。完整消费者才从同源表达式建立 scalar 包络，再与该原语组合；任意外给两串系数不能直接当作已经证明的上下界。

## 2. 四正性、全角与全径向

旋转框架中用 `JT=iT` 的实反对称 Laurent 系数，则

$
E=R_s^2-(iT_s)^2+Z_s^2,\qquad J_B=iB.
$

R251 两个行列式中的 `-B²` 因而写成 `+J_B²`。所有系数做完整卷积，没有截掉带宽。径向乘积使用 Bernstein 权重，子区间用 de Casteljau，求导除以真实子区间宽度。

角求值在 Arb/Acb 球中做 Bluestein 多项式卷积；它同时求值全部已知系数，不通过普通 FFT 从样值恢复系数。每个径向 Bernstein 控制函数另支付

$
p(\phi_j)-\Delta |p'(\phi_j)|-\frac{\Delta^2}{2}
\sum_k (2k)^2|\widehat p_k|
$

的全角余项。Gram 和四正性函数为 π 周期，`full_circle_points=N` 对应 N/2 个不同节点，最近格点距离为 `π/N`。通过的是全径向、全角下界，不是样点正性。

默认 160-bit 工作精度、角网格 2048 至最多 32768；`eta` 以精确有理数读取，不调宽门限。API 依据 [python-flint 0.9.0 arb 文档](https://python-flint.readthedocs.io/en/latest/arb.html)、[arb_series 文档](https://python-flint.readthedocs.io/en/latest/arb_series.html) 和 [arb_poly 文档](https://python-flint.readthedocs.io/en/latest/arb_poly.html)。使用区间库本身不表示证书已经运行或通过。

## 3. 同源 scalar 包络

检查分片是物理节点、scalar 节点、控制实际边界、phase panel、clip 边界和原 `Pieces.profile` mask 容差边界的精确有理并集。每块使用一个固定实表达式分支，左右块都按闭区间检查；这不把 tiny 接口差说成精确 C² 零。

在 `[a,b]` 上令 `c=(a+b)/2`、`h=b-a`。Arb series 给出中心 Taylor 系数与全区间第 `d+1` 阶导数除以阶乘的外包。若后者模上界为 B，则

$
|a(s)-q(s)|\le B(h/2)^{d+1}=e.
$

用 q 的 Bernstein 凸包得到 `|q|≤A` 后，使用

$
q^2-(2Ae+e^2)\le a^2\le q^2+(2Ae+e^2).
$

自动微分作用于原 finite-Gauss 半径，未使用另行返回的 `ap/app`。prefix 按真实次数至多 5/6 展开，余项应严格为零；非多项式默认四阶并按需二分。series precision/cap 显式保留到余项阶，避免误把已截断系数当零导数。源码另核定 `a>0`。

一次包络或 Bernstein 失败只记“未证”。程序另在真实径向中点、真实 scalar 值上求四个量；只有实际点值的**上端点为负**才登记反例。负 Bernstein 控制值本身不是反例。

## 4. 原运行常量 sidecar

`export_scalar_descriptor` 顶层只有标准库依赖，可由新外层 wrapper 调用，不向冻结 BVP 数值路径添加 flint：

~~~python
from geometry_20261114_full_prefix_operator import export_scalar_descriptor, write

descriptor = export_scalar_descriptor(
    captured_actual_profile,
    completed_result["fixed_scalar_profile"]["geometry"],
    producer_checkpoint_sha256=sha(completed_actual_path),
    origin="actual-live-profile",
)
write(sidecar_path, descriptor)
~~~

必须捕获本次构造的实际 profile 对象。`continuation.main` 会覆盖 `original.CompleteProfile`，所以新 wrapper 应捕获 `continuation.LiftedModesPrefixProfile` 返回的实际实例或同等真实 FrozenCompleteProfile 对象；不能仅在会被覆盖的旧全局上挂捕获。应在最终 checkpoint 的全部 writer 完成后写 sidecar，避免循环 hash。

导出只复制原 Gauss 数组、构造器常量、完整 segment 列表及 frozen parameters，不再次调用 `leggauss`。v3 从已完成 spec 取三个 `p*`，v4 从 FrozenCompleteProfile 取原三个冻结参数，不传其空 active vector。跨运行同 g 精化仍须比较真实 parent 与新运行的 `mathematical_identity_sha256`。

消费者重建 descriptor 并逐项比较 supplied sidecar。没有 actual-live sidecar，或者它未绑定当前 checkpoint，仍可证明**当前重建且明确声明的实表达式**，但 `actual_live_runtime_constants_verified=False`。在真实 readout 的同一对象上导出亦可诚实固定本次 g，不能伪装成已完成历史运行的逐位 Gauss-table 记录。当前正在运行的任务不因 sidecar 而要求重复求解。

## 5. 最短 Actions 核验

依赖明确使用 `python-flint==0.9.0`。先 compile 三文件，再执行：

~~~bash
python "$C/geometry_20261114_operator_interface_check.py" \
  --out "$OUT/operator-interface.json"
~~~

此入口仅包含三个解析场，并明确不是研究候选：

1. M=1、c=0、a=2、R=2、T=0、Z=s：全单元 E=1、B=0、C=4，四量为 `eta,eta,4eta²,4eta²`，应通过。
2. 同一场改 Z=(101/100)s：E=(101/100)²，真实点的上主元为负，应失败。
3. 改 T=(s/10000)sin(2φ)、Z=s。在 s=1/2、φ=π/4，两个归一化对角误差均小于 eta=10⁻⁶，但 `|B|/a=10⁻⁴`；U± 都正而 D± 都负。该例防止忽略 mixed term。

φ=π/4 另用四次单位根直接求完整 Laurent 点值，与 Arb/Bluestein 独立取点相核；实际 E/B/C 同独立解析微分结果核对。另只检查原 scalar 余项所需的 `arb_series.sin` 六个已知 Taylor 系数 API。全部严格球、失败点与异常写入小 report。它不声称完整 finite-Gauss scalar 消费者已经端到端通过。

## 6. 实际接受输入后的命令

取得真正接受的完整场后，可先对一个共同 cell 量实际成本、保存可重放 packet：

~~~bash
python "$C/geometry_20261114_full_prefix_operator.py" \
  --checkpoint "$ACTUAL_FULL" \
  --scalar-descriptor "$SCALAR_LIVE" \
  --out "$OUT/operator-first.json" \
  --eta 1/1000000 --precision 160 \
  --angular-points 2048 --max-angular-points 32768 \
  --cell-start 0 --cell-stop 1 \
  --first-cell-packet "$OUT/operator-first-cell.json"
~~~

无 sidecar 时省略相应参数，照实保留身份缺口。全 prefix 省略 cell-start/stop；也可按共同分片分给独立 Actions jobs。单 shard 不宣称完整覆盖，合并仍须核身份相同及精确无洞覆盖。

主 JSON 给出完整输入/源身份、叶 cell 状态、覆盖及 whole-prefix 布尔值。每叶完整证据追加到 `.cells.jsonl.gz` 的独立完整 gzip members，保留先前已刷新的结果。scalar descriptor 和首 cell packet 单独保全。

内存按一个物理 cell 流式处理。主要成本为 Bernstein-Laurent 卷积、严格角网格及原求积的 Taylor 包络；没有给未经 Actions 实测的耗时承诺。

## 7. 未付部分

本 note 没有登记本入口运行结果。源码明确未证明 literal rounded evaluator 的误差、finite-Gauss 半径与返回 ap/app 的严格同源 jet、所有 scalar 接口 C²，亦未覆盖 tail/cap/collar 的完整 operator、reach、保持位移或全相位。

这些义务不能以改换 scalar、删 mean、重标 failed 输入或新增九 jet 机器门替代。本入口 `closed_surface_standard4_certified` 与 `task_completed` 始终为 false。
