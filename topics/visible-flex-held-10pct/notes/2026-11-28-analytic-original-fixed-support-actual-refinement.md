# 原 R53 support 族：首个同 λ、同 g 的实际径向精化

## 结论与边界

2026-11-28，真实已接受的原 R53 `lambda002_m24` 作为唯一锚，冻结它的物理
`delta=0.06413464112662924`、完整 profile、线性 Robin tail、`lambda=.002`、
gauge `q=.06`、`warp_reference_q=.06`（实际 `warp_e=.48`）和字面 `mean1168`
后，原 `fixed=True` support 族实际完成一次更严格的径向 BVP：`M24/nt768`，
`tol=2e-7`，879 个源节点增至 1032 个节点，所有原接受门通过。

这一步支付的是**原线性 Robin 前缀在同 λ、同 g 下的实际数值精化**。它没有
调用实际 nonlinear/full-H tail，没有给出连续 C² 收敛、精确等距极限、闭图、
reach 或 held10 最终完成证明。不能把它表述为旧 phase v2–v5 失败链的成功，
也不能把改变 delta 的 design 续接表述为固定 g 的收敛。

本次原始 `run.json` 已逐字复制为
[`2026-11-28-analytic-fixed-support-m24-observed.json`](2026-11-28-analytic-fixed-support-m24-observed.json)，
不是重新计算或手写的摘要。

## 为什么这次确实固定了原问题

沿用 Nov26 已有的 `fixed_m3_branch_model.py` 和
`fixed_m3_branch_refinement.py`，不另造 support 模型。参数零从 design 的
加性 delta 改为原模型已有的

\[
p_0=\log(q_{\rm actual}/q_{\rm seed}),\qquad q_{\rm seed}=.06.
\]

高 support 控制仍使用原物理系数和原 `pscale`，完整 exact lift 系数仍为 1。
物理 profile、domain、tail 参数/切口、BC normalization `.02` 与非零分支
`[.055,.065]` 全部固定。这个 q 参数与前一条完整非线性 delta/log-q Schur
实验中的参数相同；它没有改变 gauge q 或 warp reference。

窄入口声明独立且诚实的
`model_kind=original_r53_fixed_support_literal_chart_v1`。它恢复真实 design
锚的 `chart_join`、`chart_reference_prefix`、`chart_breaks`，避免旧 fixed
入口重建另一张计算径向图。真实源全部 879 个 adaptive 节点保留；源节点上的
`s(t)` 与 `ds/dt` 逐位相同。初始 RHS 与源保存 cubic 的节点导数最大差仅
`2.6020852139652106e-18`；不是把源插值到 401 个均匀点后重新开始。

七个跨全径向节点还实际核验了原 fixed q-log 列。改变 `p0` 时，同一个物理
Flow 对象和完整 frozen profile 保持不变。中心差分步长 `1e-3, 5e-4, 1e-4`
与原解析列的最大差分别为 `4.1578392e-8, 1.0366714e-8, 7.6924424e-10`；
前两项呈二阶缩小。此检查不是区间误差证明。

## 实际返回

| 项目 | 实际值 |
|---|---:|
| Galerkin modes / RHS angular | 24 / 768 |
| 固定物理 mean | 1168 |
| 原 RMS 容差 | `2e-7` |
| 原 scaled BC / physical BC 容差 | `1e-7` / `2e-9` |
| 原 metric component FFT / sample operator 容差 | `1e-6` / `1e-6` |
| adaptive 节点 | 879 → 1030 → 1032 |
| 返回最大 RMS | `1.996289845769345e-7` |
| 返回 `q_actual` | `0.06000009614419792` |
| 返回 `p0=log(q_actual/.06)` | `1.6024020148219968e-6` |
| 返回 scaled BC | `1.3100631690576847e-14` |
| 返回 physical linear-DN BC | `1.885889210908546e-18` |
| `N=2048` component FFT l1 | `6.532516806828173e-7` |
| `N=4096` component FFT l1 | `6.532516840081911e-7` |
| 两组 sample operator 最大值 | `5.507155164628707e-7` |
| 实际 Newton 接受步 | 2，均 `alpha=1` |
| domain / merit 拒绝次数 | 0 / 0 |
| 总 wall seconds（包括准备/资源门等待/完整 audit） | `314.55723567900077` |

完整 collocation Jacobian 的所有 state、全部 24 个 parameter 和全部端点
方程都保留。两次 complete block QR 分解对应 75214 与 75360 维原系统；没有
截掉低模、高模或坏方向。每次解都仍对原完整矩阵做残差修正。原实现记录的
最大 normwise backward error 分别为 `1.2677675589497278e-25` 与
`4.8138262828833675e-26`；`maximum_componentwise_backward_error=1` 也原样
保留，不能隐去后宣称逐分量误差很小，更不能把这些浮点统计当作无限维逆界。
单进程峰 RSS 为 1131820 KiB。

## 入口与 provenance

实际目录：

`/workspace/scratch/7c4e33ee17de/held10-analytic-work/fixed-lambda002-m24-radial-v2`

原锚：

`/workspace/scratch/7c4e33ee17de/held10-design-work/design-material-recovery-20261128/lambda002_m24/run.json`

| 文件 | SHA256 |
|---|---|
| actual design 锚 run | `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891` |
| 本次 fixed-g run / repo 中逐字 observed 副本 | `1516564940efc197b43881be4c6dee1c44adef42f9b108308f36eb659c637d94` |
| `inner-00.npz` | `16e9240557207c50bde90c55e4db74671c9a21adde936afcc68402d02620e385` |
| `physical.npz` | `e5aba07d52b2526d70bcff43fe87aa84ebdb14a391075cda72fdec4344585460` |
| `analytic/fixed_support_literal_driver.py` | `6ca29978b422201e9312b30205de91d4abf3f9ac5c0ca78c627470c7df41a06e` |
| `analytic/fixed_support_literal_model.py` | `41fb25ca0d92f936f747cfd74066806c0a114d54ee920c4a8d82e081870ba1cf` |
| 原 Nov26 fixed refinement entry | `fa71d41534d17e543a27fa22fb8637d1b3ff08ef13b6d0c7db323ef2ea907297` |
| 原 main 字面源码 | `60169cde213fb0f8b7df8440b03f594898188c5abbd2f0f6926076a66f94c297` |
| 实际窄适配后 main 字面源码 | `bbb8e226f3c0cefbc52604d55b4e1ff1cf24835275a3d923eaae7f1217ef28e8` |

完整命令、frozen profile、源/port 哈希、全部返回参数、domain/Newton 统计和
audit 均在真实 run 副本。`literal-adapter.json` 与两份 event JSONL 在实际目录。
已有 R53 Fourier table 只读缓存用于组装；没有缓存可变物理响应、没有改方程。

曾有一个 `v1` 仅准备阶段误填 `angular=584`；发现真实锚是 768 后，在资源门
前明确终止，`actual_solve_invoked=False`。它没有运行 BVP，也没有任何接受结论。
这里所有数值都来自随后保留原 768 的 `v2` 实解。

## 紧接的工作

此实际固定-g 返回接入同一原 support 族的 M32 谱精化，并比较完整 Cartesian
六组 C² jets 与原字面 core 系数差。比较必须保持同一 mean1168 原函数，且将
有限采样/有限加密与连续收敛证明区分。主 design 链、实际 full-H tail 和闭图
几何证书继续各自推进，不能用本条代替。
