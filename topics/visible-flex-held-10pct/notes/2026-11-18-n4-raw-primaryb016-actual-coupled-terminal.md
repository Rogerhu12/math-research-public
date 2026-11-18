# n4：宽主核下首个完整 raw 核—真尾联立有限解

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 结论与范围

固定既有物理轮廓、$\eta=0.1$、$a=0.147$、主核与控制过渡宽度均为 $0.16$，从已登记的 $M=20,\lambda=0.02$ 线性 DN 前缀接入真正非线性有限尾。本次原联立程序完整返回成功，保存了前缀、全部尾状态、边界 Jacobian、原尾审计和均值／非均值两阶接缝诊断。完整前缀采样 metric 为

$$
8.910232570314584\times10^{-7}<10^{-6}.
$$

这是正同伦参数下的一条实际联立有限解。$\lambda=0.02$ 是核心圆化的同伦参数，不是握持比例；只有 $\lambda=1$ 的指定端点才给目标精确圆弧。本条没有完成连续角度误差界、无限尾、全闭合族或 $10\%$ 握持目标。

## 输入和保持的物理定义

输入完整前缀为 `n4_work/raw-lam002-primaryb016-m20-v2.json.gz`，SHA-256 为 `c2a313809017c27872593db0edda0d2c5c230b273f08383dbae097f473f23677`。原物理参数仍为

$$
\delta=0.030158202455449618,\qquad
v_d=0.25018727173023186,\qquad
v_u=0.35.
$$

其余轮廓、真实 $w_{\rm cut}=0.16$ 端口、材料角图、完整 raw 控制定义和原低端锚 $J=16$ 均保持。全部 $19$ 个物理控制仍自由，包括独立 $c_8$；没有重新施加设计阶段的 $c_8=0$ 条件，也没有把基本模泄漏按新 $M$ 重新定义。规范幅值为 $q_{\rm gauge}=0.0125$，最后实际主幅值为

$$
q=0.012488348123231355.
$$

这里的 `fixed=True` 固定的是物理轮廓；$p_0=\log(q/q_{\rm gauge})$ 和全部控制仍为求解未知量。输入实际 $q$ 为 $0.012488347919833637$，本次漂移 $2.0339771880650837\times10^{-10}$。因此本条是轮廓固定的设计延续／有限联立证据，不能仅凭轮廓不变就称满足本课题 README 第 5 项要求的“度量、参数和 $t$ 范围全固定”的加密证据。

入口 `build_seed` 在 $1024$ 个材料角样本上给出的完整 $F,F_u,F_{uu}$ 身份误差均为零，完整材料图投影误差为 $2.220446049250313\times10^{-16}$。这些采样数值不是全角严格误差界。这里 $u$ 是材料角。核心误差、控制系数与图的保存定义不能由显示摘要代替。

初始尾取自已明确失败的 halfH 检查点 `ebae7190…`。它只作为未接受初值使用；本次直接请求完整真实 $H$，没有把 halfH 的未接受状态升级成 fullH 结论。

## 原程序实际返回了什么

运行目录为 `n4_work/native-raw-fullH-v1`，原始 observer session 为 `96568`。固定启动计划 SHA 为 `f724afba254a82f983805833a8877d3e99d67c82451be47a9e6f7aa1e40263b7`。原 coupler 源 `couple_raw_actual_tail.py` 的 SHA `00b63349…` 未变；本轮没有安装新的初值策略，也没有编辑运行中源文件。

四次实际请求分别承担完整 $H$ 预热审计、同态边界 Jacobian、内层前缀返回后的新 $H$ 检查、最终插值端点的 Jacobian 与审计。后两次的 $H$ 不冒称逐字相同：最终插值端点的若干高模有浮点末位差，原 worker 对其单独求解。

| 实际请求 | 返回内容 | 原 shooting 残差 |
|---|---|---:|
| call 1 | 完整 $H$，原 audit | $1.6177547370043463\times10^{-9}$ |
| call 2 | 同一完整状态，1240 项边界 Jacobian | $1.6177547370043463\times10^{-9}$ |
| call 3 | 新前缀真实 $H$，1240 项边界 Jacobian | $1.5848578240592022\times10^{-9}$ |
| call 4 | 最终端点真实 $H$，1240 项 Jacobian 与原 audit | $1.9810722800740028\times10^{-9}$ |

每次均实际通过原 $2\times10^{-9}$ 门。call 3 和 call 4 均由原 Newton／原线搜索自然接受，没有手工修改内部节点。call 3 返回后的原 outer 0 边界检验为 $1.3730941039141264\times10^{-9}<10^{-8}$，随后原程序完成完整前缀审计及接缝审计。

原 inner BVP 一次返回成功，保留 $2282$ 个节点，最大 RMS 为 $9.976431989219418\times10^{-9}$。其域 Newton 为两次全步接受、零域拒绝、零 merit 拒绝。真实 observer 于 `2026-11-18T05:12:55Z` 返回 child code 0；原 worker 也真实退出 0。不能仅用进程零码代替上述原数学返回，本条同时核对了保存的成功标志、残差与审计。

## 完整前缀和接缝诊断

| 量 | 先前线性 DN 输入 | 本次实际 DN 联立 |
|---|---:|---:|
| 完整前缀 metric | $8.910179473223694\times10^{-7}$ | $8.910232570314584\times10^{-7}$ |
| 完整前缀 Darboux $\ell^1$ | $0.0041566578$（此处略写） | $0.0041566825442881875$ |
| 原实际边界残差 | — | $1.3730941039141264\times10^{-9}$ |
| 物理一阶边界残差 | — | $1.3730941039141264\times10^{-11}$ |

本次 metric 和 Darboux 均有轻微上升；本条不声称单调改善。完整前缀审计使用 $4712$ 个子午采样位置、$1296$ 个角样本。Frenet 正根采样最小余量为 $0.015107428362802655$。这些数值仍按原数值审计／守卫范围解释，不新增严格连续区间认证。

最终均值一阶、二阶差分别为

$$
1.8575377347396227\times10^{-10},\qquad
-4.398950981254757\times10^{-9}.
$$

非均值一阶、二阶差分别为 $1.3730941041152967\times10^{-11}$、$3.1895891915834475\times10^{-7}$；接缝 metric 的 FFT $\ell^1$ 为 $4.056019011272523\times10^{-7}$，其 C¹ 诊断为 $2.9165344776511085\times10^{-5}$。这些量全部保留，不能因有限 DN／BVP 门通过就称任意精度的完整两阶接缝已经构造。

最后原尾审计返回 `actualMetric = 2.565745393923192e-10`、`fullD = 2.0259234938355968e-5`、`normalizedFullDefect = 6.946511128408057e-8`，以及正的 `minLeading = 0.9615529099615254`。没有为 `fullD` 另造验收阈值。尾审计使用原 JS 路径，完整 stage 求值采用已登记的 native long-double 字面算术与完整隐式 Jacobian；这两者的有限数值范围都不升级成真 ODE 或无限尾证书。

## 执行与完整保存身份

原尾仍为 $M=20$、spacing $4$、公共 $N=512$、physical depth $8$、parts $32$、RK $16$；全部 $2304$ 个实际分片和原 cusp 网格保持。37 次完整 native batch（14 次 fullJac、23 次 scalar）均真实成功；四路 wrapper 共完成 148 个原 CLI 子进程，退出码全部为零。wrapper 只分发独立 stage，未修改已冻结 C++ 数学核。

完整前缀 `seed.json.gz` 的 SHA 为 `db78f24808e87420a30faed2759c6a44f0980f6eefe872cc0a67cb51ca9a433c`。其两个完整 NumPy 系数分块由该 CP 内部清单绑定，另用既有 `record_fixed_actual.py::checkpoint_info` 逐文件核对：

- `seed_coeff_00.npy.gz`：`f0568d6e5bb7dfb64e10717fc27379f5975afa6a119212a4cac38f4543399ca5`。
- `seed_coeff_01.npy.gz`：`5c2c341629157b1bcea5afb5f62d7fb66795693ea0d38a0f72658d87b8e4e2ca`。

该纯读绑定保存在 `prefix-checkpoint-binding.json`，SHA `c7fe89fd4f24ba5a46027e1c904925ffe4d030c323cf4d70b600cfc9b54cadd3`，工具 chunk `0a20fb` 真实退出 0。最终尾文件 `seed-tail_0004.json.gz` 的 SHA 为 `c782c31c544bdc0839a8719f658b2919847c86c1f02bbcfa99bdc3ba66489138`。

独立纯读 collector `record_native_raw_coupled_terminal.py` 的 SHA 为 `2c251fc93715d8eb9fa33efe39d29fe7e476891f8dda006c2ac2b9ab22632d43`；实际 collection session `30756`、resource terminal 0。对应紧凑记录是 `scripts/resume_n4_tail/native_raw_fullH_coupled_terminal.json`，SHA `5807ac98c3f8e6f0b11ca30bfa2271344dfe7fd3dc809a5150e0318b3a1c21c5`。完整批输入、输出、源与四子进程身份保留在 scratch manifest；Git 中没有场、节点表、控制导数界表或残差排名。

collection 首次 observer 命令把 `--out` 误写为 `--resource`，chunk `762264` 在参数解析阶段退出 2，collector 子进程尚未开始。该工程记录保存在 `collector-launch-argument-error.json`（SHA `71e4f9f6e133511262070f2dcfc37dffc51f8b2adcdbca9e758dc64408015273`）；修正的仅是观察器参数，没有重跑任何数学求解。

本次 observer wall time 为 $2595.9077899210024$ 秒。其 namespace 采样峰 RSS 为 $902856$ KiB，`RUSAGE_CHILDREN.ru_maxrss` 为 $1355672$ KiB；二者分别按自身语义报告，不称全主机进程树峰值。
