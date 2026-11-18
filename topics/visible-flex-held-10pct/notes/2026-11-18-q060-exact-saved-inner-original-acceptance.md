# q060：从原 cubic 精确续接，原联立问题得到有限接受终态

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 结论与范围

**原余弦支撑核的有限数值接受，非连续证明。**
session 41319 从原 session 91135 保存的 inner0 三次插值直接续接，
没有调用旧 restart、warmup 或重算 inner0。
原 actual-DN 边界检查要求继续校正后，只增加了一轮原 inner1；
原联立问题最终 `solver_success=true`，实际边界残差为
$9.178791778917617\times10^{-12}$，低于原 $10^{-7}$ 门。
全部三个实际尾请求均通过原 $2\times10^{-9}$ 门，末次包含完整 Jacobian 和 audit。

最终 prefix checkpoint 是
`closed_work/q060-saved-inner-resume-v1/seed.json.gz`，SHA-256
`4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9`；
系数块 `seed_coeff_00.npy.gz` 的 SHA-256 为
`a3434077ca4b42effcfdb80ce196f6e3bb52f37501f8d5319674ad66e2dc8249`。
这是完整的原 native chunk 格式输出，不是只含参数的手造 checkpoint。

| 原后处理项目 | 实际值 |
|---|---:|
| 前缀有限 FFT metric $l^1$ | $3.791250828333143\times10^{-8}$ |
| 前缀 flow defect | $1.4392190674471765\times10^{-7}$ |
| 前缀 Cartesian Darboux $l^1$ | $0.0016239119589907414$ |
| 原 physical BC | $1.8357583557835234\times10^{-13}$ |
| 原最大 collocation RMS | $9.977585233061552\times10^{-7}$ |
| 最后实际尾 shooting residual | $1.8339313038213144\times10^{-9}$ |
| 尾 audit actual metric | $4.624401106489984\times10^{-8}$ |
| 尾 audit full Darboux defect | $0.0003267809764476424$ |

前缀后处理使用 4016 个径向样本及 512 个角样本。
上述 metric 小于 $10^{-6}$ 是有限采样事实，不是全部角域或全部径向的严格上界。
Darboux、接缝及连续闭合问题仍单独保留；本条没有全闭曲面、持握比例或固定 $g$ 收敛结论。

## 精确保存点与原控制流

输入 raw inner0 的 SHA-256 为
`67112318acde56cf1c797267b2069885e50567f4b5052db008acda64cf70d84d`，
其 actual-DN 锚点 sidecar 为
`ec23c070f93692835d400a5f0eae60ba24669c862c1045e5184a465483877715`。
原字段包含 1934 个节点、25 个状态分量、
$4\times1933\times25$ 个 cubic 系数、breaks 和 axis 1。
恢复使用这些字面 binary64 系数；不由物理 quintic 反推原 cubic。
求值限于保存区间，原先未保存的 extrapolation 属性没有补造。

原 projected inner0 最大 RMS 为
$9.977585220921287\times10^{-7}$。
原 message、逐区间 RMS 向量与旧 Newton 计数未保存。
恢复入口以 `null` 表示缺失 message，仅引用原最大 RMS 标量，不制造 RMS 向量。
最终结果来自真实新 inner1，因此其 message 和 RMS 则保留新 `solve_bvp` 的真实诊断。
本次进程只记录一次原 Newton 调用、一次全步接受；不把新计数充作旧累计计数。

owned preparer 只改变 main 的状态载入、缺失诊断序列化及其来源字段。
修改位置有字面检查，逆向移除后须恢复上一 owned coupler 的全部原字节。
独立 runner 保留原方程、`solve_bvp` 选项、`TailMixin`、BC、C2 导出及
完整 metric/seam 后处理。控制流逐项对应原 `solve_with_actual_tail`：

1. 在 actual client 下真正求解保存的 candidate height，再执行原 BC。
2. BC 未过门时，才把 `o.tail` 换为该真实响应的 affine DN，执行下一 inner。
3. 在 `finally` 中恢复 actual client，保存新 raw cubic 和其 affine 锚点，
   再对新完整高度调用原 worker。
4. 总 outer 索引仍为 $0,\ldots,7$。已用 inner0 计入预算，
   不因恢复另加八轮；实际只执行到 outer1。

新客户端 call 从 0 起，来源另记原进程已有 3 次 call；没有伪接一个 worker 调用序列。
native ready/checkpoint 的 IO 字段按各自配置映射，只有 initializer/trace 路径改变。
其余配置、原 native 源、全部物理输入和原接受门保持。
JavaScript 原算术复核 reload 比值为 1、全部左端补正为正零。

## 两轮原边界检查与三个真实尾请求

| 检查 | inner 来源 | actual BC | 对应尾 residual |
|---|---|---:|---:|
| outer0 | 保存的原 cubic | $4.414534236067417\times10^{-6}$ | $1.8339826971781208\times10^{-9}$ |
| outer1 | 一次新原内层求解 | $9.178791778917617\times10^{-12}$ | $1.8339313038213144\times10^{-9}$ |

call1 真实再次接受原保存高度，Jacobian 的 208 个元素有限且 audit 存在；
其 $1153\times16$ 个 shooting 状态与已经原生接受的 initializer 逐位相同。
call2 接受新 inner1 的完整高度，仍按原 outer 请求 `jacobian=true,audit=false`。
call3 是原 C2 导出后处理重新形成的完整物理高度，再由原 worker 真正接受，
请求为 `jacobian=true,audit=true`。
call3 相对 call2 有三个分量各差一个 binary64 ULP；这些字面差别记录完整，
没有把两次 request 宣称逐位相同，也没有将 call2 响应替作 call3 的验收。

新 outer1 raw 的 SHA-256 为
`ca546af794bdbaca2247961d9b0e2132067ea8674be5476b9ef5898de057347a`；
锚点 SHA-256 为
`8206bfb14475ecafbc8f16cb344def62216113c52b410837b5fc7e0948d1bb23`。
它在提交新高度之前落盘，引用本次真实 call1 响应及完整 request/config/source。
response/config 的规范 JSON payload 哈希与文件哈希分别保留。

末次原接缝后处理给出 mean 一阶差
$-2.8313462685503055\times10^{-12}$、mean 二阶差
$6.644151895329742\times10^{-11}$，非 mean 一阶差
$1.8357537712176963\times10^{-13}$、二阶差
$9.572317916830916\times10^{-8}$。
cut metric 和其一阶有限 FFT 指标分别为
$1.6923316718824245\times10^{-9}$ 与
$3.2340959494359975\times10^{-8}$。
这些数值不隐去非 mean 二阶残差，也不自动证明两个完整 Cartesian 图已精确拼接。

## 新候选的完整物理身份

这是原 `adaptive_warped_support`、base mode 3、$M=8$ 的设计求解，
`fixed_metric=false`；原可解设计变量仍由原方程更新。
实际和 gauge 幅值均为 $.06$，最终
$\delta=.06104275721220832$，$v_u=.45$、$v_d=.5$、ramp $.4$、
flat ramp 的 $\eta_r=.05$，ShortBridge 的 $K=4$、peak fraction $.2$。
记录的材料长度 binary64 值为 $1.3602524132788236$。

固定此候选用于未来同 $g$ 加密时，必须同时冻结完整 profile、全支撑核、
warp reference $.06$、完整 spline chart、物理 port 和全部尾参数。
不能只固定标量 $.06$。紧凑记录保留全部 8 个原参数和 7 个 scales，
并逐项核对实际控制量为 `parameters[1:] * scales`：

$$
(c_6,c_9,c_{12},c_{15},c_{18},c_{21},c_{24})=
(0.00046456731984427426,
-0.00003764304940447063,
0.0000006440454234806906,
-0.0000001728968363766654,
-0.00000009226970580802433,
-0.000000005925313956530067,
0.0000000007680657966726738).
$$

`frozen_candidate_metric_identity` 同时保存完整物理尾参数与 cut、
chart 的规范 payload 哈希及原 chart 文件身份、port SHA-256
`359b5727cee3d7f7e842ba2d1f357df3f34b75374ceebd0ad06380969ad95846`。
这些是本次有限候选的完整定义来源；它们不替代真积分、atlas 与导出舍入的连续误差预算。
该核仍是余弦支撑核，不是 R44 的新圆弧 trace 空间，也不能领取 R38 的圆弧持握比例。

## 执行与复现

observer 在 `2026-11-18 01:02:31 UTC` 观察到真实 exit 0，elapsed 为
$238.33915508$ 秒。原 checkpoint、summary 和 runner 分别记录自己的计时；
checkpoint 的 $237.0458183$ 秒与 summary 的 $237.3548470$ 秒相差序列化时间，
并未冒充逐字段完全一致。其余 summary 字段逐项核对原 checkpoint。
采样 namespace RSS 与 `RUSAGE_CHILDREN` 高水位各自保留，不称全主机峰值。

冻结 launch-plan SHA-256 为
`d81942fd9ad73cac4787e4a48390cfb4698549aace2613a5c888d9ad0d0f25f7`。
入口两源 `prepare_saved_inner_resume_source.py` 和 `resume_q060_saved_inner.py`
在启动前由 root 与 m3 独立审读。
只读抽取器 `record_q060_saved_inner_terminal.py` 核对全部源、真实输出、chunk、
三次 request/response、原 gate 及接缝，不重跑 flow、BVP 或 audit。
完整命令、45 个源身份、全部物理定义、输出和日志哈希见
[`q060_exact_saved_inner_resume_terminal.json`](../scripts/resume_transfer/q060_exact_saved_inner_resume_terminal.json)。
完整 mesh、cubic/quintic、shooting 状态和 Jacobian 留在 scratch 原文件中。

这条新真实锚点可用于后续圆弧空间或更大幅值的设计入口；
任何新核或新幅值都须重新联立并经过原全部门，不能当成本条已完成的几何结论。
