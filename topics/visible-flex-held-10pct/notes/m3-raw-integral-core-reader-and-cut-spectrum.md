# raw 积分 core 的真实读取与单个切口频谱

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 1. 显式区分 raw 与 canonical

生产读取器 `resume_closed/m3_integral_prefix.py` 已按 checkpoint 的完整协议分派：

| `config.core_kind` | `core_control_path` | 使用库与控制含义 |
|---|---|---|
| `exact_m3_local_circle_integral_lift` | 缺省 | `round_core_lib`，canonical 高支撑矩 |
| `exact_m3_raw_local_circle_integral_lift` | `raw-mean-primary-compact-v1` | `round_raw_lib`，仅投影 mean/primary，不乘高矩 Schur 逆 |

不匹配的 kind/path 组合直接拒绝；显式提供的库也必须通过 checkpoint 中
`core_round_sources` 的逐文件 hash 核对。每个进程只装载一个源定义，拒绝与
另一 core 库重名的已加载模块。库 manifest hash 同时记入输出来源。

当前审过的 m3 raw wrapper 把完整控制 `parameters[1:]*central_correction_scales`
传入 core，故 `J=len(controls)+1=M`。读取器核对参数、scale、basis 维数和真实
raw basis 的 `control_path`；没有因为某个字段叫 `coefficients` 就将它解释成
支撑函数的 Fourier 系数。
实际例子的 `M=J=8`、`q=.04`、`lambda=.02`、半宽 `.21`、flatten transition
`.08`、control transition `.16`，均来自原记录，未在导出层另选。

同一原物理输入的幅值也按 source 区分：设计 checkpoint 使用已经冻结的最终
profile，读取时只将原 `delta` 设计参数换成固定读取对象的零幅值参数；要求
`actual_q=gauge_q`。真正的 fixed-g checkpoint 则保留其原 logarithmic amplitude
参数，避免 `exp(log(q/q_gauge))` 往返引入 ulp 改变。两种情况最后都逐值核
`obj.support_amplitude==record.actual_primary_amplitude`。

## 2. 实际 raw checkpoint 的端到端接口核验

输入为 `m3_work/beta4625-q040-raw-lam002/seed.json.gz`，保留原
`accepted_anchor`、物理 profile/port、全部 source hash 和原分块系数读取器。
此次未接尾 lift、未求解 BVP、未做闭图区间盒。

实际 `N=256`、径向诊断点 2070，退出码 `0`，运行约 `4.84` 秒。
源 `Flow.geo` 中 reference 项与新导出器独立展开的七种 jet，最大差
`6.290409e-15`；中心 `X=Gamma,Fs=e_z,Fss=0` 的数值恒等式最大差
`1.776357e-15`。证明 raw 来源的对象确实进入了原先单次 `H` 导出链。

新有限前缀的完整 metric 采样量为 `8.300395301657644e-5`，仍超过 `1e-6`。
这与 source 记录约 `8.30e-5` 一致；不同采样和中心补缝造成的末位变化不能称作
固定 `g` 收敛或精度改善。

raw finite 相对 source 的位置、一阶、二阶径向差分别约
`1.22e-15,8.77e-9,2.86e-8`；中心补缝的径向二阶缺口约 `2.93519e-4`，
其角一阶/二阶导数约 `.00898179/.275416`。
这些量仍只是数值接口诊断，不领取旧 R31 的连续界。

## 3. 已有数组的一个指定切口，未重新扫全域

原生产 audit 当时没有保存最大误差对应的径向位置，source 原 audit 也只存
全局最大标量。不能把旧 cosine 分支的最坏位置借给这个 raw 图。

因此新增 `diagnose_integral_cut_spectrum.py` 只使用本次已经导出的共享数组，
在唯一指定切口

`s=1.3603133321372538`

取三分量有限 DFT。此处 reference 和中心 lift 为零，角图二阶 jet 为零，
使用 nominal physical `rCut=.3`。它不声称是全域最坏切片。
按当前 state cutoff `3M=24`，把三重标量频率分成带内和带外：

| 分量 | 有限 FFT 总 l1 | 带内 `|k|<=24` | 带外三重频率 `|k|>=27` |
|---|---:|---:|---:|
| `E-1` | `3.8773090046e-9` | `4.1097515557e-10` | `3.4663324571e-9` |
| `F/a` | `3.2830792165e-10` | `9.6273745390e-11` | `2.3203337602e-10` |
| `G/a^2-1` | `1.8006337654e-6` | `1.8000726243e-6` | `5.6113891244e-10` |

这个切口的主导分量是 `G/a^2-1`，其中主导为 `k=+-24`，单边幅值约
`5.46385455e-7`，其次为 `k=+-21`，单边幅值约 `2.07520537e-7`。
以明确的 `1e-14` 系数门计算，三分量的带外最高可见频率均为 `|k|=48`。
非三重 bins 的数值 l1 约 `1e-15`，也原样记录。

这里“带外”只是相对 state 模态上限的诊断分组。metric 是乘积量，本来就能
含 state 上限以外的频率；原完整 FFT audit 没有丢掉这些 bins。
本切口主要误差在带内，也不排除它由较低 state 截断间接造成；提高 `M` 同样
可能改变旧带内系数。此切片不能判定全域 `8.3e-5` 最大缺口的频谱归因。

## 4. 证据与尚未支付的界

执行命令、真实 source 协议、输出/数组 hash 和单片谱摘要在
`scripts/resume_closed/raw_integral_prefix_interface_execution.json`。
新共享数组留作可再生 scratch 数据；没有提交几何大数组。

这些结果补齐 raw 生产读取和一个明确切片的谱诊断。真积分 core、反函数误差、
共同固定物理 atlas、全角连续 metric 及实际全闭几何仍须另付。
canonical/raw 的设计变化与后续固定 `g` 精化继续明确区分。
