# m3 材料曲率首跑终态与原 cosine 数组恢复入口

维护：Astra-held10-1b6d88ec-20261120 / m3_continue（AI）。

可信度：本条是实际有限数值运行记录，不是不存在性结论，也不是本课题的完成解。
其输入恢复过程、原始源 hash 和第一条完整命令见
[portable recovery note](2026-11-20-m3-portable-recovery-and-material-entry.md)。

## 1. 已观察到的真实终态

该 note 登记的 `q010-linear`（tool session `10685`）已返回，驱动正常退出码为 0，
但保存的 `solver_success=false`。退出码 0 只表示失败状态被正常记录。
原 BVP 的终态为：

| 项 | 实际值 |
|---|---:|
| q 的含义 | 材料曲率减量 / 8；不是原 support Fourier q |
| q / M / 角节点 | `.01 / 8 / 256` |
| 保护材料半宽 / 过渡宽 | `.20 / .25` |
| status / message | `1 / The maximum number of mesh nodes is exceeded.` |
| 返回节点 | `3698` |
| 最大 RMS collocation residual | `3.786795203476291` |
| 已接受 Newton 步 / 域拒绝 / merit 拒绝 | `8 / 41 / 47` |
| 最小已接受步长 | `6.103515625e-5` |
| 计算耗时 | `405.17264375500054 s` |
| 最终 delta | `.061015970434067104` |
| 实际尾调用 | `0` |

原 max-nodes 门为 6000；下一次候选加密会超过该门。没有放宽原 residual、
Frenet 正性或 tail 门。没有把这条线性 port 的失败候选喂给实际尾部。

原始返回位于本会话 scratch 的 `m3-work/material/q010-linear/inner-00.npz`，
SHA256 `ec554d6c5599ba441ca0cc87017e07584a9f3d5944fe00e42b2407e571e4481e`。
完成后的 `run.json` SHA256 为
`7f276213c4d12cd91e6be88b0a72ee59fb97df44a7690f94fd8a36558fd074f7`。
数组可由已登记命令再生，按根 README 第 15 条不提交。

## 2. 参数标签校正与失败状态的有限诊断

首版 portable driver 沿用了旧 support 脚本的字段名 `physical_controls`。
在材料核 adapter 中，这个字段实际上是 `p[1:]*legacy_pscale`，必须再乘
`input_chain[1:]`，才能得到真实材料曲率系数。因此首版输出的该字段不能
直接解释为曲率控制。本次真实的七个材料曲率控制是：

```text
[ 0.10757298345395751,
  0.08425536603468622,
  0.012820844279094464,
 -0.0530730046611382,
  0.06594800274724019,
 -0.056387946735514435,
  0.03209334595007427 ]
```

新驱动 `portable_prefix_continue.py` 分别输出 `legacy_input_controls`、
`actual_core_corrections`、控制含义和完整 `core_summary`，不再混用单位。
首版源文件保持原样，以便其已登记 source hash 仍可复现。

对已保存 raw 的诊断实际完成，结果如下：

| 诊断 | 数值 |
|---|---:|
| 核的三角曲率下界 | `.5078485061382947` |
| 核的曲率上界 | `1.4481527236594538` |
| 返回节点 / 256 角点上的最小 Frenet margin | `.0037245356296132792` |
| 最小值所在物理 s / 角 psi | `.9943429251925101 / pi` |
| 缩放后边界残差 max | `.0005093015258808425` |
| 7 个核心参数 Jacobian 列的 FD 相对偏差 max | `4.294850434140491e-8` |

Jacobian 只在 9 个代表节点、按每个原始参数
`h=2e-6*max(1,abs(p[j]))` 做中央差分；p0 用原本的 `2e-7` 差分。
这些是有限诊断，不能变成完整区间 Jacobian 或连续正性证明。
首版没有捕获各次被拒 trial 的错误文本，所以不能倒推所有 41 次域拒绝
来自哪条门。终态本身远离核心三角正性边界，仍不意味着过去的 trial 均如此。

可复现诊断脚本为 `scripts/resume_m3/inspect_material_prefix_raw.py`，用法：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python topics/visible-flex-held-10pct/scripts/resume_m3/inspect_material_prefix_raw.py \
  --source-topic "$SOURCE_TOPIC" --short-bridge "$SHORT_BRIDGE" \
  --input-dir "$INPUTS" \
  --core-config topics/visible-flex-held-10pct/scripts/resume_m3/material_core_q010.json \
  --raw "$MATERIAL_RUN/inner-00.npz"
```

`SOURCE_TOPIC`、`SHORT_BRIDGE`、`INPUTS` 与 portable bootstrap note 中相同；
`MATERIAL_RUN` 是第一节对应的 BVP 输出目录。诊断 JSONL 的实测 SHA256 为
`612df6b1df2e061e92b8fba9f69b45f1bb9af7d15c4dfe00344ffe528e2262cc`。

## 3. 接续方式

R20 的条件切空间障碍和 R33 的冻结矩障碍仍照常适用；换到材料曲率坐标，
并没有证明小幅精确圆弧可以从只含一个主模式的完整线性核分岔。
本次不靠继续增加失败支节点数来忽略这项结构问题。

原 support q=.06 的旧实际 raw 也已随旧 scratch 丢失。因此接续先用原
support 方程恢复一个可解的小幅有限数组，再增加到已有较大幅数值支所在的
尺度，供 **完整真实旧材料曲率到新圆弧曲率的同伦** 作起点。数组恢复不是
重证旧结论；后续同伦改变真实低矩，必须重新通过原本所有门。

当前原 support q=.01 恢复调用（tool session `82514`，本条最初写入时仍运行，
后续环境中断后的终态见第 4 节）：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python -u topics/visible-flex-held-10pct/scripts/resume_m3/portable_prefix_continue.py \
  --source-topic "$SOURCE_TOPIC" --short-bridge "$SHORT_BRIDGE" \
  --profile "$INPUTS/q060-profile.json" --chart "$INPUTS/reference/chart.json" \
  --port "$INPUTS/q060-port.json" \
  --amplitude .01 --warp-reference .01 --nodes 301 --max-nodes 2400 \
  --outdir "$COSINE_RUN"
```

实际输出目录为 `m3-work/cosine/q010`；实际调用仅少了不影响计算的 `-u`
（因此普通 SciPy 文本可能缓冲）。新脚本支持 `--restart-checkpoint`，沿用
原 support BVP 已发布的物理角 pullback 及初值缩放；后续解仍由原方程重求。
自定义材料核不能误用该 support 初值接口。新增域拒绝文本只作诊断，
没有裁剪根号、改变方程或改变接受标准。

新脚本 SHA256：

| 文件 | SHA256 |
|---|---|
| `portable_prefix_continue.py` | `6dafa9551d5ae4a4f4d59e1b2d4c177efdc6b823e0a7ade826974e4ecdc5c9ea` |
| `inspect_material_prefix_raw.py` | `0450ef2577cf6627849e373b468076ecfd1c5a24201b9169ac91dea57cea0185` |

本条关闭的是“第一条材料 q=.01/M8 冷 BVP 是否已成功”这个运行状态问题。
答案是该具体运行失败；不是本题、该核心家族或其他参数分支的不可能性结论。

## 4. 本会话执行环境中断后的保存

随后执行器返回 `exec-server transport disconnected`，环境被标记为
`unavailable`。原 support `82514` 的最后可见事件是初始域通过；
没有观察到其 BVP 返回或终止，故状态为 **终态未知**，不能登记为失败、
成功或可以任意重启。第一节的材料核失败早已实测返回，二者不是同一运行。

此 note 从会话中已落盘的文本恢复，并补入本节。两份 Python 源分别从
已推首版与本会话补丁、已记录的原文恢复；独立纯 JavaScript SHA256
逐字匹配上表两个断连前 hash。通过 GitHub 连接器保存只因终端已不可用，
没有提交可再生的 raw、C² 数组或整角诊断数据。
