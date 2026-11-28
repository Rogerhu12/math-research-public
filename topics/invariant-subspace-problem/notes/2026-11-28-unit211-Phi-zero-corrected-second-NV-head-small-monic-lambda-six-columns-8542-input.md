# 新输入：正确 Phi 第二 NV 头的原首一 lambda 三次、六列与两固定三原 cofactor

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：未执行的新原目标。** 只处理第二完整 NV t 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0.
$$
两个原矩的固定组合给首一 lambda 三次；新幂等元极化小式给完整原 NV。首次在这一个真实三元环境内形成六条同点列及两组事前固定的三阶 cofactor。没有旧二十列或八条奇部列的重放，没有第一头输入、泛域 scalar gcd、选点、素数、因式、新头逆或排空预报。

源码：2026-11-28-unit211-Phi-zero-corrected-second-NV-head-small-monic-lambda-six-columns-8542.py。

源码 SHA256：11521b5532c7202582c3419dcb0a3b4283c8f72c092ad95422317b5d8512ec57。

零依赖；绝对 **120 秒 / 1 GiB**，外层最多 135 秒。两组目标在执行前固定，不增限、换组或在失败后续轮。

## 1. 原范围与最小系数环

沿[第二头原矩与四列纸证](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-original-monic-sigma-and-four-columns.md)及新[幂等元极化完整小三次](../results/R150-appendix-unit211-Phi-zero-corrected-second-NV-head-idempotent-polarization-and-small-complete-cubic.md)，置
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell.
$$
本次所有实际分母仅需
$$
A_0=\mathbb Q[u,Q,(Q sK_w)^{-1}].
\tag{1}
$$
原物理解释仍限已经付清坐标恢复的正确 Phi 图；(1) 不把原 Gram 延伸到其未定义的 M 零图。只是本次原小多项式及实际证书不需要 M 逆。

设
$$
a=\lambda-\frac32,\qquad T=\ell a-m\sigma,
$$
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1.
$$
两个完整原矩为
$$
E_2=\ell\delta\sigma^2-2ma\sigma+\ell a^2-A_\lambda,
$$
$$
E_3=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2
 -m\delta\sigma^3-B_\lambda.
\tag{2}
$$
它们来自同一个原
$h=\lambda-\tfrac12-\rho\sigma$、$k=\lambda-\tfrac12+\rho\sigma$，保全部复根和非约化纤维。

## 2. 不需要新头的原首一 lambda 三次

直接从 (2) 相减得
$$
E_3-aE_2
=-ma^2\sigma+2\ell\delta a\sigma^2-m\delta\sigma^3
 +aA_\lambda-B_\lambda,
$$
$$
aA_\lambda-B_\lambda=-2\lambda^3+\lambda^2+\lambda-\frac12.
$$
因此
$$
\boxed{
\begin{aligned}
q_\lambda
&=-\frac12(E_3-aE_2)\\
&=\lambda^3+\frac{m\sigma-1}{2}\lambda^2
 -\frac{1+3m\sigma+2\ell\delta\sigma^2}{2}\lambda\\
&\quad+\frac14+\frac{9m}{8}\sigma
 +\frac{3\ell\delta}{2}\sigma^2+\frac{m\delta}{2}\sigma^3 .
\end{aligned}}
\tag{3}
$$
特别，等价显示式中的 $a^2\sigma$ 系数是 **$m/2$**。源码使用展开的 (3)，并完整返回其与两个原矩的身份。

(3) 的 lambda 首项恒为一，所有系数分母仅含 Q。它在 $m=0$、$\ell=2$、$\ell=4$ 等零面上仍是同一多项式身份；不选择这些面之外的泛型图。总几何次数不超过三。

于是
$$
B=A_0[\sigma][\lambda]/(q_\lambda)
\tag{4}
$$
确为以 $(1,\lambda,\lambda^2)$ 为基的自由三元代数。这里仅声明 (4) 的自由性；加原条件后的真实商不必自由。也不从另一个 sigma 首一二次与 (3) 同时存在，擅自宣称某个六维自由商。

## 3. 新完整 NV 的紧凑原定义

取新极化稿的显示量
$$
\beta=\frac32-\lambda-\sigma,\qquad T_0=-K_w,\qquad
J-Q=-4s^2,\qquad P_{02}=2sL,
$$
$$
e=L(1-\beta)-uQ\sigma,\quad
D_0=(J-Q)T_0=4s^2K_w,\quad
F=P_{02}T_0\lambda-P_{02}e+sT_0^2.
$$
其普通原恢复为
$$
f=F/D_0,\qquad E=P_{02}e/(QT_0).
$$
记
$$
\begin{aligned}
C_f&=-1+2(1-\ell)\beta^2-4s\beta\sigma+4s^2\sigma^2,\\
C_u&=(1-2(1-\ell)\beta+2s\sigma)(\beta-2s\sigma),\\
P&=fC_f+uC_u+2E\beta(\beta+2\sigma)
 -T_0\sigma(1-2(1-\ell)\beta)+2\lambda P_{02}\sigma^2 .
\end{aligned}
$$
根据已付完整原极化身份，
$$
P=N_4(\mathbf V),\qquad
C=QD_0P=4Qs^2K_w N_4(\mathbf V)
\in\mathbb Q[u,Q,\lambda,\sigma].
\tag{5}
$$
源码采用极化稿的五项短式定义 C，并核 (5) 的普通多项式清分母。原完整 NV 不以某个范数、最高项或单独分量替换。其原 t 系数在本头支精确为零；没有施加物理 $t=0$，其余均值、N1、个别 N/P 条件仍在同一点保留。

由于 $QD_0$ 在 (1) 中是单位，本次原子系统准确为
$$
I=(E_2,E_3,N_4(\mathbf V))=(E_2,E_3,C).
$$
又由 (3)，
$$
\boxed{I=(q_\lambda,E_2,C).}
\tag{6}
$$
这只是这三个完整条件的准确子系统，不声称等于完整原物理系统。

## 4. 六条新原列与精确呈示

在 (4) 中，按如下固定次序取余：
$$
E_2,\quad \lambda E_2,\quad \lambda^2E_2,\quad
C,\quad \lambda C,\quad \lambda^2C.
\tag{7}
$$
每次仅按首一 (3) 作普通 lambda 除法。若
$v=r+Q_vq_\lambda$，则以 (3) 的完整两原矩来源反传，得到 r 对
$(E_2,E_3,C)$ 的真实普通多项式组合。

源实际核验每条的三个基坐标及三原身份。原分子形式、分母尺度和 (5) 的完整 NV 尺度同时保存为定义，不读取任何旧列或 cofactor 证书。

这些六条列构成 $A_0[\sigma]$ 上的矩阵 $\mathcal M$。因为 (4) 是真实单首一多项式商，一个理想生成元及其 $1,\lambda,\lambda^2$ 倍生成其整个底环模。因此
$$
\boxed{A_0[\lambda,\sigma]/I\simeq\operatorname{coker}\mathcal M,}
\tag{8}
$$
其中 $\mathcal M$ 是本次的准确三行六列呈示。全部重数都保留；这不需要对真实原值商另加自由或无根重合假设。

首一规则保持总几何次数。若基坐标按 $(1,\lambda,\lambda^2)$ 排列，六条列的 sigma 次数上界为
$$
\begin{array}{c|ccc}
\text{原列}&1&\lambda&\lambda^2\\ \hline
E_2&2&1&0\\
\lambda E_2&3&2&1\\
\lambda^2E_2&4&3&2\\
C&3&2&1\\
\lambda C&4&3&2\\
\lambda^2C&5&4&3
\end{array}
\tag{9}
$$
源逐坐标核这些上界，不预报实际次数或非零。

## 5. 事前固定的两组原 cofactor

只形成两组零起始索引：
$$
[0,1,3],\qquad [0,3,4].
\tag{10}
$$
分别对应 $(E_2,\lambda E_2,C)$ 和
$(E_2,C,\lambda C)$ 的三列。

设所选三阶矩阵为 M，取真实
$\operatorname{adj}(M)e_0$。完整返回
$$
M\operatorname{adj}(M)e_0=(\det M)e_0
\tag{11}
$$
的三个坐标，再把三个列来源合并到三个原多项式，便得
$$
\det M=\Omega_2E_2+\Omega_3E_3+\Omega_V N_4(\mathbf V).
\tag{12}
$$
(9) 给两者的 sigma 次数上界分别为
$$
2+3+3-(0+1+2)=5,\qquad
2+3+4-(0+1+2)=6.
\tag{13}
$$

源码先统一三个实际原分子乘子的权分母，再取全部三个乘子的共同多项式因子；只有共同精除并完整乘回之后才取消。此过程从普通原身份推出新的原身份，保共同因子的零面，不以裸行列式的内容约分冒充原来源。

随后只删除 (1) 中 Q、s、Kw 的旧付支持，并将这些除数运输到全部最终乘子。最后重新返回 (12) 的全部原多项式系数，其中第三乘子已经乘入 (5) 的 $QD_0$。三个最终分母都须逐项只含上述旧支持。

若某固定 scalar 恒为零，只如实记录该组没有给出非零支持，仍保全部纤维；不会改选其它列。若新 sigma 头有零点，整零面继续保留。没有先倒这些头后再声称全图结论。

## 6. 与已成门的区别和结论边界

本次唯一新工作是：

- 原两矩的固定组合 (3) 与新完整小 NV，共同建立新的 lambda 首一三元环境；
- 形成 (7) 的六条新同点列及真实三原反传；
- 形成 (10) 的两个固定三阶原 cofactor，统一实际乘子后取消共同因子。

源码自含，不读旧二十列或八条奇部列源码，不再生旧四阶 cofactors，也不调用第一头被冻的三 scalar gcd。这里换用一个新原首一关系，不是把失败的泛域消元换算法续算。

所有输出只含 profiles、实际次数、来源返回和统计；不输出或保存系数载荷。没有执行前不称任何 scalar 非零、头为单位、子系统排空或完整 Phi 排空。本次不计算两个 scalar 的 gcd、resultant、因式、模点或共同零集；这些也不在此预算内自适应追加。

如果任何实现、资源或数学断言触界，只登记最后完整返回的原身份，保未完成范围，不增加限额或换序重跑。
