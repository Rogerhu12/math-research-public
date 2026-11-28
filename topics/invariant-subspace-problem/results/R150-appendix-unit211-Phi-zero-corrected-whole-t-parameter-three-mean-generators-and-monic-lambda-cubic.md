# R150：正确 Phi 全图的 t 参数真均值三生成与原 lambda 首一三次

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面证明，无新执行。** 在当前正确 Phi、distinct singleton、物理 $D\ne0$ 的原规范上，已证的整个 $\ell=1/2$ 排除支付 $2\ell-1$。利用这一新单位，将真正的三个均值改写为 $(f,V)$ 的二次式、保留原 $t$ 为参数，其共同二次头可在全图直接求逆：
$$
\boxed{\det H_{f,V}=\frac{32uQ(2\ell-1)}{M^2}.}
\tag{1}
$$
因此原三均值商在已付权环的 $t$ 多项式环上由 $1,f,V$ 生成。原 $\lambda$ 的乘法随即给一个首一三次式，系数是 $t$ 的多项式。这不要求三生成元自由，不宣布原图有限或空。

## 1. 原量、支付范围与两个仿射图

记
$$
p+q=2,\quad pq=Q,\quad \rho=(p-q)/2,\quad \delta=\rho^2=1-Q,
$$
$$
u=bp+cq,\quad \ell=b+c,\quad m=u-\ell,\quad
M=4bc\delta,\quad V=bX+cY.
$$
原 $Q\delta bcP_{02}$ 均为单位。$u$ 来自独立真原零 base-mean 排除；$2\ell-1$ 来自
[正确 Phi 整个 ell-half 排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)。
所有支付只用于当前原图，不移入 $h=k$ 碰撞、任意 $D=0$ 或 W 图。

沿用 Phi 权量
$$
T_0=2u-\ell Q-2u^2,\qquad
J=2u(1-u)+\ell Q,\qquad
P_f=T_0(J-Q),\quad s=u-1.
$$
原 $P_f\ne0$ 图的 $E_0,N_0,P_1$ 恢复是
$$
W_1=bpX+cqY=T_0/2+2uf,\qquad
QV=Jf-\lambda P_{02}-sT_0+bcQt.
\tag{2}
$$
完整原双点条目为
$$
A_1=2f-2V+2bct.
$$
将 (2) 代入已刊 $P_ff+QP_{02}(\ell+T)-(\lambda P_{02}+sT_0)T_0=0$，直接得到
$$
\boxed{
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},\qquad
T=-\ell+\frac{T_0}{P_{02}}(f-V+bct),\qquad z=Qt .
}
\tag{3}
$$
固定 $t$ 时，$(f,V)\mapsto(\lambda,T)$ 的线性行列式为
$$
-\frac{P_f}{P_{02}^2}.
\tag{4}
$$
它是原已付权单位，所以 (3) 是整个当前图的双向仿射变换。这里不倒 $t,f-u,\alpha,\lambda$ 或任何新的几何首项。还原到 $(\lambda,T,z)$ 时的 $f$ 正是原 $-P_c/P_f$，不是另选分支。

$X,Y$ 也由 (2) 唯一恢复：
$$
X=\frac{W_1-qV}{b(p-q)},\qquad
Y=\frac{pV-W_1}{c(p-q)}.
\tag{5}
$$
所有分母只含已经支付的 $b,c,\rho$。在不引入单个 $\rho$ 根的偶奇原环中，等价公式为
$$
X=x+\rho y,\quad Y=x-\rho y,\quad
x=\frac{(u-\ell Q)V-mW_1}{M},\quad
y=\frac{\ell W_1-uV}{M}.
\tag{6}
$$

## 2. 正确三个均值与固定 t 的二次头

在已恢复 $E_0=0$ 的原 Gram 上，正确的均值差是
$$
\mathcal R=
4(f-u)(V-f)+bct^2+
t\left(4bcu-\ell V+
 \frac{m}{2\delta}(T_0+4uf-2V)\right).
\tag{7}
$$
其完整真原身份为
$$
2\mathcal R+E_1-bE_B-cE_C=0.
\tag{8}
$$
(8) 使用双点乘法 $(d^2)_1=2d_0d_1$。原已更正来源及 (7) 的自由权推导见
[原 alpha/chi 坐标](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md) §2 的 (4)–(7)；这些身份在代入 W 权关系之前成立。本条只引用该自由恒等式，不借用 W 的任何单位。

设
$$
E_{Be}=(E_B+E_C)/2,\qquad
E_{Bo}=(E_B-E_C)/(2\rho).
$$
由 (8) 及 $bE_B+cE_C=\ell E_{Be}+mE_{Bo}$，
$$
(E_1,E_B,E_C)=(\mathcal R,E_{Be},E_{Bo})
\tag{9}
$$
作为已付权环的 $\rho^2=\delta$ 二次扩张中的理想。右侧三个偶奇表达及其系数都在原权环中；由 (6) 也可直接在原环写出它们。整个首一规则都来自真正三个均值，不需要原 $N_1$ 来补头。

固定 $t$、只给 $f,V$ 次数一。令
$$
X^{[1]}=af+\beta V,\qquad Y^{[1]}=\gamma f+\eta V,
$$
其中 $a,\beta,\gamma,\eta$ 只是临时线性系数：
$$
a=\frac{2u}{b(p-q)},\quad
\beta=-\frac q{b(p-q)},\quad
\gamma=-\frac{2u}{c(p-q)},\quad
\eta=\frac p{c(p-q)}.
\tag{10}
$$
这些系数的分母都已在原环中支付。

直接由真原 meanB 公式
$$
E_B=(1-\ell)p^2+2pr+ct^2
 -2\bigl((1-\ell)pu+pd_1+ru+ctY\bigr)
 -2X^2+4fX
$$
可见，前三括号项在 $f,V$ 上至多一次，因此
$$
\mathcal R^{[2]}=4f(V-f),\quad
E_B^{[2]}=-2(af+\beta V)^2+4f(af+\beta V),
$$
$$
E_C^{[2]}=-2(\gamma f+\eta V)^2+4f(\gamma f+\eta V).
\tag{11}
$$
与总几何最高函子不同，这里 $t$ 留作系数参数；没有把原 $t$ 设零或只研究边界纤维。

## 3. 行列式的完整代数计算

令 $d=p-q=2\rho$，并置
$$
S=a+\beta=\frac{2u-q}{bd},\qquad
U=\gamma+\eta=\frac{p-2u}{cd}.
$$
(11) 对列 $(f^2,fV,V^2)$ 的前三行分别为
$$
(-4,4,0),
$$
$$
(-2a^2+4a,\,-4a\beta+4\beta,\,-2\beta^2),
$$
$$
(-2\gamma^2+4\gamma,\,-4\gamma\eta+4\eta,\,-2\eta^2).
$$
沿第一行展开，得到
$$
\det H_{\mathcal R,B,C}
=-16\left[\beta^2U(2-U)-\eta^2S(2-S)\right].
\tag{12}
$$
原 $u=bp+cq$ 给
$$
2cd-p+2u=p(2\ell-1),\qquad
2bd-2u+q=-q(2\ell-1).
$$
所以方括号的共同分子为
$$
\begin{aligned}
&q^2(p-2u)(2cd-p+2u)\\
&\qquad-p^2(2u-q)(2bd-2u+q)
=2upq(2\ell-1)d .
\end{aligned}
$$
因而
$$
\det H_{\mathcal R,B,C}
=-\frac{32uQ(2\ell-1)}{b^2c^2d^3}.
\tag{13}
$$
从 $(E_B,E_C)$ 换成 $(E_{Be},E_{Bo})$ 的行变换行列式为 $-1/(2\rho)$。用 $d=2\rho$ 和 $M=4bc\delta$，(13) 变成
$$
\det H_{f,V}
=\frac{2uQ(2\ell-1)}{b^2c^2\delta^2}
=\frac{32uQ(2\ell-1)}{M^2},
$$
这证明 (1)。计算没有任何未付因子或漏掉的权零支。

## 4. 整原均值商的三生成

将三原均值写成
$$
\begin{pmatrix}\mathcal R\\E_{Be}\\E_{Bo}\end{pmatrix}
=
H_{f,V}
\begin{pmatrix}f^2\\fV\\V^2\end{pmatrix}
+
L(t)\begin{pmatrix}1\\f\\V\end{pmatrix}.
$$
(1) 给原环中的完整伴随矩阵身份，因而
$$
\begin{pmatrix}f^2\\fV\\V^2\end{pmatrix}
=-H_{f,V}^{-1}L(t)\begin{pmatrix}1\\f\\V\end{pmatrix}
\pmod{(\mathcal R,E_{Be},E_{Bo})}.
\tag{14}
$$
右侧三个常数系数的 $t$ 次数至多二，$f,V$ 系数的 $t$ 次数至多一。分母只在既有权单位中，尤其没有 $t$ 分母。

每次使用 (14) 都严格降低 $(f,V)$ 的总次数。因此，若 $A$ 为第 1 节的已付权环，
$$
A[t,f,V]/(\mathcal R,E_{Be},E_{Bo})
$$
由 $1,f,V$ 三元生成为 $A[t]$ 模。任意再加入原 $N_1$、加权 NS/PS、个别 N/P 或完整 NV 的商，仍由这三元生成。它们可能有非平凡 $A[t]$ 线性关系；本条不假设自由，也不把三个裸余式矩阵当作无关系结合代数。

## 5. 原 lambda 首一三次与次数

令 $M_f,M_V$ 的列分别是 $f$、$V$ 乘 $1,f,V$ 后按 (14) 得到的三个真实余式坐标。由 (3) 设
$$
M_\lambda=
\frac{bcQt-sT_0}{P_{02}}I
+\frac J{P_{02}}M_f-\frac Q{P_{02}}M_V.
\tag{15}
$$
每一列都有原均值来源，故在原商中 $M_\lambda$ 确实表示同一个 $\lambda$ 的作用。即使原商不是自由模，仍可先在自由三坐标上使用 Cayley–Hamilton，再通过三元生成映射返回原商，得到
$$
\boxed{\chi_\lambda(\lambda,t)=\det(\lambda I-M_\lambda)=0.}
\tag{16}
$$
这是原均值理想的完整来源定义；(16) 对 $\lambda$ 首一三次，不需要展开其大系数。

给基元权 $d_0=0,d_f=d_V=1$，(14)–(15) 有
$$
\deg_t(M_\lambda)_{ij}\le1+d_j-d_i.
$$
每个行列式乘积的基权望远镜消去，所以 $\chi_\lambda$ 的 $(\lambda,t)$ 总次数至多三，且 $\lambda^3$ 系数为一。也可以用相同来源定义原 $T$ 的首一三次，但本条不另记一份重复推论。

必要代数在 $A[t]$ 上有限三生成并不意味着对 $A$ 有限，更不意味着原系统为空。物理 $D\ne0$ 等几何局部化也不能自动保留对 $A[t]$ 的有限模结构；这里的整三生成与 (16) 先在未反演这些几何量的必要代数中成立，随后原物理点必满足它们。

## 6. 本条与下一新输入的边界

本条完全由既有正确原定义与 §3 的显示恒等计算证明，没有调用或重跑旧 f62 头门、f73 原十五列、05c1 个别值、任何失败线性门或旧 ell-half 证明。

下一真正新输入可以在这个整三生成环境里计算完整原 $N_1$ 的 $t$ 参数线性余式、其原斜率与完整 NS/PS 来源。那些尚未执行、尚未证明的首项支付不属于本条。已经撤回的 wrong-Rbar 消元链继续保持撤回。
