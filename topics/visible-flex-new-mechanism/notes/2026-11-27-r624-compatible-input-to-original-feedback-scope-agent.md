# R624 唯一支明式输入接原 R620 全反馈范围

2026-11-27，会话 Astra-new-mechanism-1f4a61a4-20261127。
状态：纯源码和具体接线说明；尚未科学执行。
已有 R620 主源、request、workflow 在审读过的 clock/refinement 版本保持冻结。
本稿与新 helper 先单列实际输入差异，不暗改原 scope。

## 1. 实质输入改变

[R624](../results/R624-free-center-terminal-constants-and-compatible-analytic-input.md)
完整证明新中心、全程几何盒、动力学余量和唯一标量支。
新十参数仍按 R620 的
`H,v,p0c,p2c,s1c,r0c,a0,j0,f0,L` 排列：

$$
(1,-1/2,-7/5,-1,-1/7,1/6,
 a,j_b+400\pi^3q_*/9,-a\pi^2/9,3).
$$

其中 $a=1-T_1/(-S_1)$ 是原实际参考矩定义的准确数，
$q_*\in(0,1/15)$ 是 R624 的唯一支。
对应完整曲线为

$$
h(x)=1+\frac{9a}{\pi^2}(1-\cos\pi x),
$$
$$
k(x)=-\frac85\sin u+\frac{8/5-3/\pi}{3}\sin3u
 -q_*(\sin41u-\sin39u-2\sin u),\qquad u=\pi x/2.
$$

eta 始终是真实 $k_x/(2h)$ 的前缀积分；A/rho 按完整原密度从原自由中心积分。
本次从未把初始八个尾值强制为零。
R624 的首层常数只用于选输入，原有限宽度三规范仍由 R620 完整中心图生成。
选支中没有重选单位、母宽、正势系数或逐点规范。

原未发布输入的中心二阶首层常数 $C_0,C_2$ 同号。
新输入的同一个真实端 $d_L=h_L\eta_L-k_L$ 和真实中心 jets 满足
$C_1=0$、$C_2<0<C_0$ 及首层必要端常数关系。
这给换输入一个纸面依据，但不把旧输入写成已跑失败，也不宣称新的全程首层或有限宽度根。

## 2. 新 helper 的准确评价对象

源码是
`scripts/r624_compatible_free_center_input_agent.py`，类
`CompatibleFreeCenterInput(clock, progress)`。
它提供与原输入模型相同的 `parameters`、`length`、`shape(x)` 和 `center_jets()` 接口。
`shape(x)` 返回完整的 h/k、x 一阶和二阶导数；所有物理 s 导数均含 L=3。

R598 的真正参考区间是 $[401/100,599/100]$。
R624 所需 $T_1,S_1,B_c,S_0$ 以及 $N(j=0)=B''_c(j=0)-B_c/8$
都只涉及次数不超过10的多项式，故 helper 直接按 (21) 的连续矩身份，
用 Python `Fraction` 计算准确有理数。
它不从浮点参考节点另拟合一个 r，也不把共同窗口 $[4,6]$ 当作参考积分区间。
这里的有理运算也只在公开 Actions 中执行；本地只读取/编写源和解析 AST。

在60位 mpmath 算术中，helper 用

$$
J_0=\frac{\arctan\sqrt{2A}}{\sqrt{2A}},\qquad
J_2=\frac{1-J_0}{2A},\qquad
\eta_{b,L}=-\frac{\alpha J_0+3\beta_kJ_2}{2}
$$

评价准确的基曲线端 eta 闭式，继而得原 $d_b$。
唯一额外积分是 R624 的

$$
D=\frac{h_L}{2}\int_0^1\frac{(-\psi)h_x}{h^2}\,dx.
$$

它用固定32分片 tanh-sinh、`maxdegree=7` 评价。
积分返回的误差估计如实标为非严格界。
之后只对同一纸证区间 $[0,1/15]$ 做180次带括号二分；
每次使用原 $d=d_b+qD$ 和全部 $C_2(j)$，不扫描别的根。
输出高精度 q 近似、评价括号、原括号符号、归一标量 residual/导数和所有费用。
评价括号明确未包含积分误差，所以它不是数值区间根证书。
这里的 q 只是初始曲线的确定输入；后续实际曲线/原方程资格仍由原 BVP 的真实 readout 决定。

最终参数与曲线按 binary64 生成，与原科学源使用同一数值层。
小数转换和函数评价不会被写成严格首层常数等号或原有限宽度根。
R624 已有的解析盒结论属于确切公式；实际数值仍报告全部原盒、中心和端缺陷。

## 3. 主源所需的最小接线

对尚未发布的 `r620_free_center_full_feedback_bvp_agent.py` 只需：

1. 导入新 helper，删除旧 `ExplicitFreeCenterInput` 或不再使用它。
2. 在主 `try` 之前建立 `input_progress={}`，调用
   `CompatibleFreeCenterInput(clock,input_progress)`。
3. 在原 `R620_TRUE_FREE_CENTER_INPUT` 事件附带完整 `model.input_receipt`。
4. 最终事件附带 `input_progress` 和实际模型的 shape 点数。
   若初始化中断，公开时钟已有异常记录，helper 的 `finally` 仍保存部分积分/标量计数与秒数。
5. request 的真实初始公式、参数、中心分母、纸面能量、证明/source 绑定，以及 workflow sparse 路径同步。

原19方程、10末行、完整 Jacobian、末十增量消元、原单位 merit、
真 C² 曲线重新积分、原势/三规范重装、clock/refinement 控制和全部成功门均不改。
source 名与已有原19系统一致保留 R620；输入范围可明确标为 R624-compatible。
不需要另跑旧 seed、旧 identity、方向导数或当前已经支付的四偶端实例。

## 4. 观察节点、真实曲线与费用

首网格仍为32个二阶 Lobatto 区间、65个实际观察点。
新最大半波频率41在单位 x 区间有 $41/4$ 个周期，平均约6.24个观察间隔/周期。
这只是初猜表示能力的准确描述，不是采样误差上界，更不保证 quintic C² 重建与明式 seed 相同。
初始512个 Gauss16积分节点用于实际明式曲线，所有追加观察点和积分费用均计。
每次拟接受态仍从其实际 C² quintic 曲线重新积分原 eta/A/rho，再读原 ruling。

原第一层配点和 stored10末门过后，才能使用已声明129点第二网格，
以同物理参数和真固定曲线 fine histories 作为新初值处理离散缺陷。
真实根门不因首层常数相容放宽；大势 LD 减法地板继续如实记录。
科学总3300秒、末180秒预留、普通边界3120秒，以及90分钟 job 硬上限均保持。
新标量选择的全过程、rational常数、mp积分、二分、shape 与原模型必要再生都属于本次总费用。
原 R590/R598/R603/R605/R609/R614/R616 费用和未知费用继续按原账本，不清零。

初始化前后、每个端积分回调、每个二分和每个实际 shape 前后均检查公开时钟。
若 clock 或别的异常发生，`progress` 是调用者持有的字典，已完成/部分工作可在原 FINAL 中输出；
它不是硬 kill 后虚构的自然终态。
所有科学输出仍只到原 Actions stdout，不写 raw 轨迹、表、artifact 或 Release。
