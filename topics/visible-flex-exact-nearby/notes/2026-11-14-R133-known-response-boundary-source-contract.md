# 完整已知响应的腰部与真实正帽切面源合同

本合同只对固定物理 $\eta_0$、原 $\nu$、精确连续中心
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
成立；“仿射参数偏移 $\eta=0$”不表示物理 $\eta=0$。
所有新数值在公开仓库自己的 Actions 中执行。本文件尚不宣布任何新数值门通过。

## 1. 已知准解、内段和单侧迹

原完整物理响应索引为
`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`，
$193=96+97$ 个实槽均保留。它没有再乘原中心的幅度 $\alpha$。
实际完整标量均值修正给

$$
q_*=q_{\rm raw}+e_z e_2.
\tag{B.1}
$$

实际原主体/均值 native 为
`a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870`。
本次取其在 $[0,L]$、$L=9/10$ 上的内段准解。
腰部取 $q_*(0+)$，切面取 $q_*(L-)$；若 $L$ 恰为原节点，
准确选择左侧原立方片与左侧已证完整均值区间。
这使内段所有原跳跃恰位于 $0<r<L$，不会漏付切面单侧差。

每个原立方系数都是保存的 binary64 精确 dyadic 数。
在精确有理半径以 $320$ bit Arb Horner 运算评估全部槽，
仅在均值槽加上原 native 的完整 $e_z$ 包络。
原均值流已证连续；本消费者不重算它。

令 $h$ 为物理实振幅，$\widehat h$ 为角测度归一化的正交槽。
所有非均值振幅除以 $\sqrt2$，均值保持原值，故

$$
\|\widehat h\|_{\ell^2}
=\|h\|_{L^2_\phi},\qquad
\widehat h=(\widehat h_{\rm odd},\widehat h_{\rm even}),
\quad\dim\widehat h_{\rm even}=97.
\tag{B.2}
$$

## 2. 全部腰部行

在固定幅度的 $\nu$ 响应中，腰部全部 $96$ 个 odd Dirichlet 行为零。
对误差 $h=q_\nu-q_*$，因此完整已知腰部源为

$$
g_0=-\widehat q_{*,{\rm odd}}(0+).
\tag{B.3}
$$

它不是从有限 solve 的名义边界推定为零，而是从全部已存立方槽实际评估。
不新增腰 mean 约束，也不删除响应中的独立 even mean。

已证的完整腰部边界提升为

$$
p(0-)\le D_0q(0-)+L_0\|g_0\|.
\tag{B.4}
$$

原虚接口 $0-\to0+$ 的完整 projector 角跳仍由 Green 链消费，
不能将原 $D_0$ 直接配到内格 $0+$ 的 cone 上。

## 3. 真正 homogeneous cap 的完整低行

参数列使用紧支撑权
$w=4096[t(1-t)]^6$，支撑为 $[1/20,9/50]$。
在整个 $[L,25/8]$ 上 $w=w_r=0$，从完整参数列公式得到
$F_\nu=0$，其中心修正差也准确为零。
因此 $q_\nu$ 的正帽延拓属于真正 homogeneous cap 的 regular 子空间。
只为内段误差求界时，准解 $q_*$ 可以在 $L$ 截断；
没有必要强迫旧外帽 trial 本身成为该延拓。

实际完整 cap-cut native 为
`36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104`，
其全部 $14$ 门已由原公开运行 $43587619797$ 通过。
原 cut 原始矩阵 native 为
`528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba`。
完整名义低边界为

$$
B_{\rm nom}
=
\begin{pmatrix}
I_{96}&J\\
0&M
\end{pmatrix}.
\tag{B.5}
$$

这里 $J$ 是 $96\times97$，$M$ 是完整 $1\times97$ 独立 mean 行。
它们直接由原 native 保存的全部十六进制 binary64 数恢复为精确 dyadic。
对 $\widehat q_*=(o,v)$，名义已知源为

$$
g_{R,\rm nom}=-\binom{o+Jv}{Mv}.
\tag{B.6}
$$

真 cap 已给完整三个误差门 $\varepsilon_{\rm odd}$、
$\varepsilon_{\rm mean}$、$\varepsilon_{97}$，所有未知矩阵误差仅作用于
完整 even 输入 $v$。于是

$$
\|g_R\|
\le
\|(o+Jv,Mv)\|+\varepsilon_{97}\|v\|,
\tag{B.7}
$$

也可保留独立均值，取另一个完整上界

$$
\|g_R\|
\le
\sqrt{
(\|o+Jv\|+\varepsilon_{\rm odd}\|v\|)^2+
(|Mv|+\varepsilon_{\rm mean}\|v\|)^2}.
\tag{B.8}
$$

消费者取两种已证上界中较小者，并保存各项，避免丢失均值行或把
$\varepsilon_{97}$ 当成只作用于非均值 $96$ 列。

## 4. 径向权的准确取消

完整内段使用 $Y=R\widehat h$，
$R=\operatorname{diag}(I_{96},\rho I_{97})$。
实际 weighted-boundary native 为
`56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25`，
原公开 prepare $43594139132$ 的全部 $10$ 门已经通过。
其边界定义是 $B_R=B_{\rm true}R^{-1}$，因此

$$
B_R(R\widehat q_*)=B_{\rm true}\widehat q_*,
\qquad U(R\widehat q_*)=U\widehat q_*.
\tag{B.9}
$$

所以 (B.3)、(B.7) 的源范数直接配原

$$
q(L)\le D_Lp(L)+L_R\|g_R\|;
\tag{B.10}
$$

没有额外的 $\rho$ 或 $\rho^{-1}$ 因子。
完整 native 同时保存原 $\rho(0)$、$\rho(L)$、
$D_0,L_0,D_L,L_R$ 与精确边界单位公式。

## 5. 不能丢掉的高输出和未知反馈

原完整 cap 给

$$
\|(I-\Pi_{96})S(HB_{\rm even}-K_{\rm actual}HC)v\|
\le \varepsilon_{\rm high}\|v\|.
\tag{B.11}
$$

本次保存右端已知 high 源
$\varepsilon_{\rm high}\|\widehat q_{*,{\rm even}}(L-)\|$，
其范数与原 cap-cut 的完整 high-output 合同完全一致。
它不是未知 high 输入的反馈界，不意味着低 $97$ 行的核消掉了高输出。

若分解 $q_\nu$ 的 low/high 槽，完整边界中的未知 high 输入项
仍必须作为独立反馈端口送回低系统；完整高输出方程、外 regular 源、
所有 interior mean、根区和负区的 high 耦合仍保留。
在这些步骤完成前，(B.7) 只是完整低投影内已知源的一部分。

内段 source 应使用已经付清中心修正的 $q_*$ 残差、
全部 $0<r<L$ 原非均值跳跃、(B.3)、(B.7)。
真 homogeneous cap 决定 $q_\nu$ 的右边界，所以不再额外传播
旧外帽 trial 残差；这种节省没有取消真 cap 自身或未知 high 输入。

## 6. 公开可复算输入与输出

新 producer 为
`scripts/fourfold_codazzi_known_response_true_boundary_sources.py`，
新 wrapper 为
`scripts/fourfold_codazzi_known_boundary_source_CI.py`，
workflow 为
`.github/workflows/visible-exact-known-response-boundaries.yml`。

wrapper 只消费原已成 prepared bundle、完整 mean artifact、
完整 cap-cut artifact、weighted prepare artifact。
原 prepared manifest
`fd7594990ecc126e63a79198e00bbaf5912537ff1db480ade8ac82ff8917c893`
的全部文件逐字节检查；旧方法只用于 SHA 审计和准确 canonical alias 恢复。
不再运行旧 reconstruction、旧 mean、旧 residual 行或旧 cap 矩阵格。

新 native 将保存全部单侧原槽、均值修正槽、正交槽、完整腰部和名义切面源、
真实 low/mean/high 范数与原实际 process 身份。
另输出小型 UTF-8 JSON 摘要，以便仅集成可用时直接审查真实结果，
无需经集成传输或展开二进制。
失败时保留实际 process、stdout 和全部已产出的 native。
