# R150：额外乘子后的九个全局原来源与无条件加权成本 8531

日期：2026-11-15 UTC。作者：Astra-ISP-789f / root；literature_audit 独立复核。AI-assisted，GPT-6 Astra Pro。

## 1. 已经成立的目标成员性

[完整射影确定因子与余乘子](R150-appendix-full-projective-divisor-degree381-and-residual-multiplier170.md)已经证明存在同一个非零 $R\in\mathbb Q[s]$，使
$$
\deg R\le170,\qquad R(s)h_0(s)t_\nu(s,m)\in\operatorname{im}_{\mathbb Q[s]}A
\quad(2\le\nu\le10),
\tag{1.1}
$$
其中 $A:\mathbb Q[s]^{6188}\to\mathbb Q[s]^{4367}$ 仍是原十七式的全部次数至多三来源，
$$
h_0=s^3(s-2)F_+^2F_-^2E_8,\qquad
t_\nu=\left(\sum_{k=0}^{\nu}\binom{\nu}{k}(-s)^{\nu-k}m_k\right)^2.
$$
取该定理所定义的 $R=\Delta_{\mathrm{aff}}/K_{158}$ 即可。下文不用 $R$ 的展开系数，不将它假定为常数。

原来源权及成本为
$$
a_{m^\alpha N_i}=20+10|\alpha|,\qquad
a_{m^\alpha\Gamma_i}=25+10|\alpha|,\qquad
\delta_\ell=a_\ell-10,\qquad |\alpha|\le3,
$$
$$
\operatorname{cost}(x)=\max_{x_\ell\ne0}\bigl(\deg x_\ell+\delta_\ell\bigr).
\tag{1.2}
$$

本篇证明以下无附加成员性条件的结论：
$$
\boxed{
\exists\,0\ne R,\ \deg R\le170,\quad
\exists\,x^{(2)},\ldots,x^{(10)}\in\mathbb Q[s]^{6188}:
\quad
Ax^{(\nu)}=Rh_0t_\nu,\quad
\operatorname{cost}(x^{(\nu)})\le8531.
}
\tag{1.3}
$$
同一个 $R$ 对全部九列使用。式 (1.3) 的来源仍只用原 $m$ 次数至多三的乘子，增加的参数乘子不改变原五次 Macaulay 空间。

## 2. 同一选定原子式的三个已付界

保持此前的 $I,J$、$B=A_{I,J}$、$D=\det B\ne0$ 和自然总权 $H=8770$。
[同选第四配对证明](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)已经付
$$
v_\infty D\ge130,\qquad
v_\infty(\text{全部原来源换列子式})\ge125,\qquad
v_\infty(\text{全部 cofactor})\ge125.
\tag{2.1}
$$
[同选完整模 31 无穷远计算](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md)给同一非零约化子式次数 $8527$；故
$$
8527\le\deg D\le8640.
\tag{2.2}
$$
[完整有限公共因子](R150-appendix-original-low-projection-double-linear-divisor-and-E8-local-target-membership.md) §8 给
$$
K=K_{158}=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4.
$$
它整除每个原最大子式，而不只是 $D$。置
$$
d_*=D/K,\qquad q=\deg d_*,
\qquad 8369\le q\le8482.
\tag{2.3}
$$
没有把 $K$ 当作完整 gcd，也没有将 $D$ 的模 31 最高项当作特征零最高项。

## 3. 保全部输出的准确余式整理

这里逐项使用[原公共因子余式引理](R150-appendix-common-minor-factor-conditional-source-cost8740.md) §§2–4，写明新的目标依赖。

对每个原来源列 $A_\ell$，定义
$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K.
$$
每个分子坐标是原最大换列子式，故 $P_\ell$ 是多项式，并且
$$
A_JP_\ell=d_*A_\ell
\tag{3.1}
$$
在全部 $4367$ 输出上成立。理由是所选输出限制在完整函数域像上单射；两边都是原多项式，不能遗失其余十三个输出。

由 (2.1) 的原来源换列界，
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-125-158.
\tag{3.2}
$$

固定 $\nu$，置 $b=Rh_0t_\nu$。现在 (1.1) 已经给出某个多项式解 $Ax=b$，所以
$$
T_b=\operatorname{adj}(B)b_I/K
=\sum_\ell P_\ell x_\ell
\in\mathbb Q[s]^{4354}.
\tag{3.3}
$$
此处多项式性使用已经证明的 $Rh_0$ 成员性，不使用原 $h_0$ 尚未证明的成员性。

对每个 $\ell\notin J$ 作 $x_\ell=d_*v_\ell+r_\ell$、$\deg r_\ell<q$，再置
$$
y_\ell=r_\ell\quad(\ell\notin J),\qquad
y_J=x_J+\sum_{\ell\notin J}P_\ell v_\ell.
$$
式 (3.1) 给 $Ay=b$，而基来源满足精确恒等式
$$
d_*y_j=(T_b)_j-\sum_{\ell\notin J}(P_\ell)_jr_\ell.
\tag{3.4}
$$
$y$ 已经是多项式向量；以下减去 $q$ 的次数是对这个真实整除使用，并非从函数域解猜测整除。

## 4. 额外参数乘子没有增加最终成本

目标 $b$ 仅有二次 $m$ 输出，这些输出的自然权为 $20$。因而
$$
\tau(b):=\max_i(\deg b_i+b_i^{\mathrm{wt}})
\le\deg R+24+2\nu+20\le234.
\tag{4.1}
$$
与原 $h_0t_\nu$ 的 $64$ 相比，唯一改变是至多增加 $170$。

由全部 cofactor 的 (2.1)，
$$
\deg(T_b)_j\le H-a_j+\tau(b)-125-158.
\tag{4.2}
$$
对非基来源，由 (2.3) 得
$$
\deg y_\ell+\delta_\ell\le q-1+45\le8526.
\tag{4.3}
$$
对基来源，将 (3.2)、(4.2) 代入 (3.4)，再加 $\delta_j=a_j-10$，得到两个分支
$$
\begin{aligned}
\text{原来源转移}&\le H+55-125-158-11=8531,\\
\text{目标伴随支路}&\le H+234-125-158-10-8369=342.
\end{aligned}
\tag{4.4}
$$
因此三个真实分支共同给
$$
\operatorname{cost}(y)\le\max\{8526,8531,342\}=8531.
$$
对九个目标分别执行同一整理即证明 (1.3)。先前的目标支路 $172$ 现在升至 $342$，但仍小于已经决定共同上界的原来源转移支路。

## 5. 已闭接口及尚未得到的系数信息

这是全局原来源的存在定理与具体参数次数界；它不再以原九个 $h_0t_\nu$ 的成员性为条件，因为目标已经明确换成同一个 $Rh_0t_\nu$。总乘子次数仍至多 $194$。

$R$ 的具体系数、九个来源的展开系数及系数高度没有在本篇计算。对任何选定的九个有理来源，当然存在一个有限非零整数同时清分母，且不增加成本；但本篇没有给出该整数、其大小或其素因子，也没有证明分母只含固定的 $31$ 次幂。

同一 $D$ 的最高系数是否为 $\mathbb Z_{(31)}$ 单位仍开。因此上述有理余式整理不自动给固定 $31$ 分母层的降度，不把有限模精度或原 $h_0$ 成员性视为已完成。普通 Hilbert 不变子空间问题也未由本条完成。
