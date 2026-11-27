# 原三变量向量场的正特征截断森林、立方界与原薄窗二次界

日期：2026-11-27 UTC。**状态：以下截断局部比较、统一最小方程退出、原低轴立方界及§§11–14的薄X二次混合界与真秩返回已证明。常数只给存在性，未计算有效最小值；原 canonical 主目标及临界完整核仍未排除。**

本文接同日《原三变量 Theta 向量场的全稳定素簇、截断 D-property 与小长度根理想》及其第8节。保持
$$
V=6t(1-t)\partial_t+
 \left((1+2t)X+\frac23t\right)\partial_X+
 6(1-t)XY\partial_Y.
\tag{1}
$$
原实际低轴是
$$
\gamma_s(t)=(t,x(t),\theta(t))\pmod{t^s},\qquad
p=6s-1,\quad x(0)=0,\ \theta(0)=1.
$$
只使用已付的截断关系
$$
\operatorname{ev}_s(VF)
 =6t(1-t)\partial_t\operatorname{ev}_s(F)\pmod{t^s}.
\tag{2}
$$
不把 $\gamma_s$ 延成一条满足 $(1)$ 的无限特征 $p$ 解。

方法沿 Binyamini 的重数森林结构，但本文逐项替换其特征零局部轨道步骤：局部比较用正规化赋值而非 Puiseux；一般点只作长度小于 $p$ 的有限流；原奇点直接保 $(2)$ 的误差与截断。下述定理不是对复解析定理作未经证明的换特征引用。

## 1. 固定常数与待证上界

沿前注第8节，固定
$$
d_0=864.
$$
在通用系数环上，对所有次数不超过 $d_0$ 的多项式同时考虑
$(P,VP,\ldots,V^jP)$ 的升链，取其一个固定稳定指标 $M\ge1$。定义
$$
L=864+3M,\qquad
B=\max\{M,288\},\qquad
A=3B.
\tag{3}
$$
本文所有特征均要求
$$
\boxed{p>\max\{83,L^3,2B+3\}.}
\tag{4}
$$
这是一个固定的有限排除，独立于待测多项式 $P$、其系数及次数。没有把未计算的 $M$ 称作有效数值。

**定理。** 对任意非零 $P\in\Bbbk[t,X,Y]$、总次数 $D\ge1$，在同一个原截断评价中，
$$
\boxed{
\min\{s,\operatorname{ord}_tP(t,x(t),\theta(t))\}
 \le (D+A)^3+(D+A)^2+(D+A).
}
\tag{5}
$$
评价为零模 $t^s$ 时，左边按 $s$ 解释。常数多项式的评价阶为0。

稍强的森林记账给
$$
\min\{s,\operatorname{ord}_tP(\gamma_s)\}
 \le D+D(D+A)+D(D+A)^2,
\tag{6}
$$
但本文后续只使用 $(5)$，不优化常数。若右边至少为 $s$，结论本身不排除任何截断零；不可将一个立方估计当作二次临界的自动排核。

## 2. 截断重数的准确局部定义

在光滑三维形式邻域中，取一条光滑形式曲线 $\gamma$，以 $u$ 为参数。它只须满足某个有限精度 $N$ 的切向条件。将曲线拉直后写坐标 $(u,w_1,w_2)$，其理想为 $(w_1,w_2)$，并假设
$$
V|_\gamma
 =a(u)\partial_u+b_1(u)\partial_{w_1}
                      +b_2(u)\partial_{w_2},
\qquad b_1,b_2\in(u^N).
\tag{7}
$$
称 $a(0)=0$ 的情形为本节的奇点情形。实际原点的 $(2)$ 正属于此情形，且可取 $N=s$。

对不可约簇 $W$ 的局部 germ，若 $\gamma$ 不包含于 $W$，令
$$
m_\gamma(W)
 =e(I_\gamma,\mathcal O_{W,0})
$$
为 Samuel 重数。对有限个待处理簇，可任意选择 $\gamma_s$ 的足够一般的高尾，使 $\gamma$ 不包含于它们；这只选择计算局部交数的辅助曲线，保持原 $s$-jet 与 $(7)$，不声称它为无限轨道。对给定的有限森林，这样的延拓可以一次选定。

给正循环 $\Gamma=\sum n_i[W_i]$，定义**线性加权的截断函数**
$$
\mathcal M_c(\Gamma)=\sum_i n_i\min\{c,m_\gamma(W_i)\},
\qquad 1\le c\le N.
\tag{8}
$$
这里没有将 $\min\{c,\sum n_i m_i\}$ 认成 $(8)$。实际始终只使用
$$
\min\{c,\sum_i n_i m_i\}
 \le\sum_i n_i\min\{c,m_i\}.
\tag{9}
$$

### 2.1 正规化枝与横截参数

用足够一般、包含 $\gamma$ 的形式超平面把 $W$ 切到曲线。保留交循环的全部正整数权重；不需要断言曲线约化。对各正规化枝，设其赋值为 $\nu_i$。可把第一坐标换成
$$
\widetilde u=u+\ell(w_1,w_2),
$$
其中 $\ell$ 为一般线性式，使它同时横截有限个枝；在 $\gamma$ 上仍有 $\widetilde u=u$，且 $(7)$ 的误差阶不变。于是
$$
e_i=\nu_i(\widetilde u)\ge1,\qquad
a_i=\min\{\nu_i(w_1),\nu_i(w_2)\}\ge e_i.
\tag{10}
$$
泛线性式 $\ell'(w_1,w_2)$ 在该枝上的阶准确为 $a_i$。标准局部交数与正规化公式给
$$
m_\gamma(W)=\sum_i n_i a_i,\qquad
\operatorname{mult}_0W=\sum_i n_i e_i.
\tag{11}
$$
这些是整数赋值等式；没有在特征域内除以 $e_i$，也没有要求分歧指数与 $p$ 互素。

## 3. 保全部cap与枝权的局部 Rolle 引理

**引理1。** 设 $f$ 在 $W$ 上恒零，而 $g=Vf$ 不在 $W$ 上恒零，令
$$
\Gamma'= [W]\cdot\operatorname{div}(g)
$$
为实际适当交循环。对 $(7)$ 与 $1\le c\le N$，有
$$
\boxed{
\min\{c,m_\gamma(W)\}
 \le \operatorname{mult}_0W+\mathcal M_c(\Gamma').
}
\tag{12}
$$
若 $a(0)=0$，则可去掉第一项：
$$
\boxed{
\min\{c,m_\gamma(W)\}\le\mathcal M_c(\Gamma').
}
\tag{13}
$$

证明：沿第2节的某个正规化枝，因 $f$ 在该枝上为零，$f(\widetilde u,0)$ 的拉回阶至少为 $a_i$，即其 $\widetilde u$ 阶至少为 $\lceil a_i/e_i\rceil$。由 $(7)$，再将 $g(\widetilde u,0)$ 拉回该枝，得到
$$
\nu_i g\ge \min\{a_i-e_i,Ne_i\}
$$
的一般界；奇点时切向导数不降低阶，故加强为
$$
\nu_i g\ge \min\{a_i,Ne_i\}.
\tag{14}
$$
从 $\gamma$ 移回该枝的差在 $(w_1,w_2)$ 内，阶至少为 $a_i$，所以不削弱上述界。$a_i\ge e_i$ 保一般界右边非负。

奇点时，由 $e_i\ge1$、$c\le N$ 及全部正权，
$$
\min\{c,\sum_i n_i a_i\}
 \le\sum_i n_i\min\{a_i,Ne_i\}
 \le\sum_i n_i\nu_i g.
\tag{15}
$$
一般情形则先加回 $\sum_i n_i e_i$，得到同样的比较。最右边是沿同一泛截曲线的 $g$ 交数，也就是 $m_\gamma(\Gamma')$ 的线性总和。把这一总和再用 $(9)$ 截断，得到 $(12)$、$(13)$。更明确地，左边不超过 $c$，故先可把右边总交数取 $\min(c,\cdot)$，随后才用 $(9)$ 分解到各子循环；没有把 cap 当作线性运算。

若采用一般情形的 $\operatorname{mult}_0W$ 项，使用整数不等式
$$
\min(c,\mu+q)\le\mu+\min(c,q)
$$
即可作同一分解。引理证毕。

这个证明只用正规化上的整数赋值、局部交数与普通求导的阶界。特别，它在不可分投影的枝上仍成立；所需横截坐标已由 $(10)$ 单独选择。

## 4. 一般点处的有限流与实际导数检测

令 $q$ 为 $V$ 的一个非奇异点。因 $(4)$，所有 $j!\ (j\le2B)$ 均可逆，故可以取长度 $2B+1$ 的真实有限流
$$
\gamma_q(u)=
\left(
 \sum_{j=0}^{2B}\frac{V^jt(q)}{j!}u^j,\
 \sum_{j=0}^{2B}\frac{V^jX(q)}{j!}u^j,\
 \sum_{j=0}^{2B}\frac{V^jY(q)}{j!}u^j
\right)
 \pmod{u^{2B+1}}.
\tag{16}
$$
Leibniz 公式在这些次数内准确给
$$
F(\gamma_q(u))
 =\sum_{j=0}^{2B}\frac{V^jF(q)}{j!}u^j
 \pmod{u^{2B+1}},
\qquad
\gamma_q'(u)-V(\gamma_q(u))=O(u^{2B}).
\tag{17}
$$
因 $V(q)\ne0$，这是一条光滑曲线的有限 jet。任意保持该 jet 的一般高尾都满足第2节条件，取 $N=2B$。以下统一用
$$
c=B+1<2B.
\tag{18}
$$
不需要存在无限特征 $p$ 流。

对不可约簇 $Z$，在其一般非奇异点取 $(16)$。则
$$
\min\{c,\operatorname{ord}_uF(\gamma_q(u))\}
 =\min\bigl(\{c\}\cup
       \{j<c:V^jF\notin I(Z)\}\bigr).
\tag{19}
$$
这只由有限代数条件决定。在下面的循环论证中，各局部比较对每个满足 $(16)$ 的一般高尾都成立，因此不需要给不存在的无限流定义唯一轨道重数。

若 $Z$ 不包含于任何非零真稳定素簇，它的每个包含簇也不稳定，且其一般点不在 $V$ 的奇异集。对一个不稳定不可约 $W$，在其一般光滑点 $V$ 横截 $W$，故
$$
m_{\gamma_q}(W)=1.
\tag{20}
$$
这是一次切向检测：存在 $h\in I(W)$ 而 $Vh\notin I(W)$；第一阶 jet 已付横截性，未用高阶或无限轨道。

## 5. 三维的纯代数次数下界

需要的 Hilbert 步骤可以在三维中直接支付，不依赖复解析几何。

**引理2。** 设 $d>6$，$Z\subset\mathbf A^3_{\overline{\Bbbk}}$ 不可约，$P$ 为 $I(Z)$ 中非零最小总次数的多项式，$\deg P=d$。若 $Z\subset W$、$W$ 不可约且余维为 $j$，则
$$
\boxed{\deg W>d^j/12.}
\tag{21}
$$

余维1时，$W$ 的不可约定义方程次数为 $\deg W$，且属于 $I(Z)$，故实际上 $\deg W\ge d>d/12$。

余维2时，取 $W$ 的射影闭包及正规化。次数至多 $d-1$ 的仿射多项式限制空间，注入次数为 $(d-1)\deg W$ 的线丛截面空间。一个次数为 $e\ge0$ 的线丛的截面维数至多 $e+1$：在 $e+1$ 个一般点取值即为单射，否则非零截面有超过 $e$ 个零。因此该限制空间维数至多
$$
(d-1)\deg W+1.
$$
若 $\deg W\le d^2/12$，它严格小于
$$
\binom{d+2}{3}=\dim\overline{\Bbbk}[t,X,Y]_{\le d-1}.
$$
于是有一个非零次数小于 $d$ 的多项式在 $W$、从而在 $Z$ 上恒零，矛盾。

余维3时 $W$ 为一点，其理想已有非零线性式，与 $d>6$ 不相容。因而这种包含在本引理假设下不会发生。以上证明在任意特征中成立。

## 6. 高次数最小方程在288阶内退出

**命题3。** 设 $Z$ 不包含于任何非零真 $V$ 稳定素簇，$P$ 为 $I(Z)$ 中非零最小次数方程。若
$$
d=\deg P>864,
$$
则
$$
\boxed{\text{存在 }1\le j\le288\text{ 使 }V^jP\notin I(Z).}
\tag{22}
$$
证明不先假定退出阶有限。

反设 $V^jP\in I(Z)$ 对 $0\le j\le288$ 全成立。最小性使 $P$ 不可约：否则其某个较低次数因子在不可约 $Z$ 上恒零。构造最多三层正循环
$$
\Gamma^1=\operatorname{div}(P),\quad \Gamma^2,\quad \Gamma^3,
$$
每个保留的分量均包含 $Z$，并满足
$$
\operatorname{codim}\Gamma^j=j,\qquad
\deg\Gamma^j\le(2d)^j.
\tag{23}
$$

同时保留下列完整局部归纳。对 $Z\subset W\subset\operatorname{supp}\Gamma^j$，在 $W$ 的一般点取第4节有限流及任一一般高尾，设 $\mu_W$ 为普通局部重数，则
$$
\boxed{
\min\{c,\operatorname{ord}_{\gamma_q}P\}
 \le (j-1)\mu_W(\Gamma^j)+\mathcal M_c(\Gamma^j).
}
\tag{24}
$$
$j=1$ 由除子因子分解与 $(9)$ 成立。

假设第 $j$ 层已构成，写
$$
\Gamma^j=\sum_i m_i[W_i].
$$
由 $(21)$、$(23)$，
$$
m_i<12\cdot2^j.
\tag{25}
$$
在 $W_i$ 一般点，其它分量不经过该点，而 $(20)$ 给 $\mathcal M_c(\Gamma^j)=m_i$。所以 $(24)$ 迫
$$
\min\{c,\operatorname{ord}_{\gamma_q}P\}
 \le j m_i<12\cdot2^j j\le288<c.
\tag{26}
$$
因此原实际导数已有一个首退出阶 $\ell_i\le288$：
$$
Q_i=V^{\ell_i}P\notin I(W_i),\qquad
V^{\ell_i-1}P\in I(W_i).
$$
这是从截断不等式推出的有限退出，不是先假定有限后引用轨道阶。反设保证 $Q_i\in I(Z)$。

对每个 $i$ 作适当交
$$
[W_i]\cdot\operatorname{div}(Q_i),
$$
保留其中包含 $Z$ 的分量，并乘回原权 $m_i$；所有这些循环之和定义 $\Gamma^{j+1}$。因为
$$
\deg Q_i\le d+3\ell_i\le d+864<2d,
\tag{27}
$$
Bézout 给 $(23)$ 的下一层。

为核 $(24)$，对下一层中包含 $Z$ 的任意 $W$，在它的一般点应用引理1。未保留的分量不包含 $Z$，故不包含 $W$，不会经过 $W$ 的一般点。实际交数的单调性给
$$
\mu_W([W_i])\le
 \mu_W([W_i]\cdot\operatorname{div}(Q_i)).
$$
引理1把每个旧分量的 $\mathcal M_c$ 上界为其普通重数加新循环的 $\mathcal M_c$。将这些不等式乘原 $m_i$ 求和，旧式 $(24)$ 便变成
$$
j\,\mu_W(\Gamma^{j+1})+\mathcal M_c(\Gamma^{j+1}),
$$
正是下一层的 $(24)$。全过程中 $\mathcal M_c$ 按 $(8)$ 线性使用；只在单个多项式的左边取 cap。

当 $j=3-\dim Z$ 时，所有保留分量都等于 $Z$。$(26)$ 此时使截断阶至多 $288$，而反设使它至少为 $289$（$c=B+1\ge289$），矛盾。命题证毕。

由前注第8节的低次数命题及 $(4)$，$\deg P\le864$ 时退出阶至多 $M$。合并得到对全部最小次数方程的统一结论：
$$
\boxed{
0\ne P\in I(Z)\text{ 最小次数},\
Z\text{ 不包含于真稳定素簇}
\Longrightarrow
\exists\,1\le j\le B,\quad V^jP\notin I(Z).
}
\tag{28}
$$
这里小次数步骤真正使用局部 primary 长度 $<p$；高次数步骤使用的是 $(16)$–$(27)$ 的有限流和交循环，两者的逻辑没有混合。

## 7. 原任意多项式的三层实际森林

现在令 $0\ne P$、$\deg P=D$。以 $\operatorname{div}(P)$ 的不可约分量及其**实际因子重数**为根，递归如下。

若节点 $n[W]$ 为一点，或 $W$ 包含于某个非零真稳定素簇，则把它作为叶。否则在 $I(W)$ 中选最小次数方程 $\widetilde P$。因原 $P$ 在 $W$ 上恒零，
$$
\deg\widetilde P\le D.
$$
由 $(28)$，取首退出阶 $j\le B$，令
$$
f=V^{j-1}\widetilde P,\qquad
g=V^j\widetilde P,\qquad
f|_W=0,\quad g|_W\ne0.
$$
该节点的子节点是实际交循环
$$
n[W]\cdot\operatorname{div}(g)
$$
的所有不可约分量及其正整数交重数。因为
$$
\deg g\le D+A,
$$
深度 $j=1,2,3$ 的循环总次数分别满足
$$
\boxed{
\deg\mathcal T^1\le D,\quad
\deg\mathcal T^2\le D(D+A),\quad
\deg\mathcal T^3\le D(D+A)^2.
}
\tag{29}
$$
每次为适当交，余维增加1，因此最多三层。这里没有丢掉 embedded 问题后猜 multiplicity；节点使用实际素分量的交循环权。

此森林完全由代数多项式、导数及交数构成，与原截断弧的高尾选择无关。构成后，可一次选原 $\gamma_s$ 的一般形式高尾，避开有限全部节点，并保持 $(2)$。

## 8. 在原奇点上的加权cap归纳

原 $(0,0,1)$ 是 $V$ 的奇点；$(2)$ 在拉直坐标后给第2节条件 $N=s$ 与 $a(0)=0$。所以沿森林每一条边使用的是引理1的**奇点式** $(13)$，没有额外普通重数损失。

根处，若 $P=\prod P_i^{e_i}$，
$$
\min\{s,\operatorname{ord}P(\gamma_s)\}
 \le\sum_i e_i\min\{s,\operatorname{ord}P_i(\gamma_s)\}.
\tag{30}
$$
每个根因子的评价阶等于相应除子沿 $\gamma$ 的重数。将 $(13)$ 对每个节点乘其原正整数权，逐层用 $(8)$ 求和，得到
$$
\min\{s,\operatorname{ord}P(\gamma_s)\}
 \le\sum_{\text{叶 }n[W]}
 n\,\min\{s,m_\gamma(W)\}.
\tag{31}
$$
这就是需要的加权 cap 归纳，而不是把 $\min$ 从和式中交换出去。

叶若为原点，其沿曲线重数为1；其它点对原点的局部贡献为0。叶若为正维且通过原点，前注的全稳定素簇分类迫它包含于 $t=0$。此时在 $\mathcal O_{W,0}$ 中，曲线的理想等于极大理想：因为 $t=0$，其余两个拉直坐标已经生成全部极大理想。因此准确有
$$
m_\gamma(W)=\operatorname{mult}_0W.
\tag{32}
$$
若它在 $Y=0$ 或 $t=1$ 等不经过原点的稳定边界内，则局部贡献为0。于是 $(31)$ 不超过全部叶在原点的普通重数总和，再不超过其次数总和。由 $(29)$ 得到 $(6)$，从而得到 $(5)$。

至此已完整支付原奇点、所有分量重数、截断误差和正特征导数。既没有在 $\Bbbk[[t]]$ 中制造 $(1)$ 的无限解，也没有用复 Puiseux 参数或遗漏 $p$ 次非约化分量。

## 9. 回到同一个原完整M的准确范围

R525 §4 对原完整 $M=c_*U_0m_{13}J$ 已给必要低轴
$$
\bar M P_{\rm source}=0
\Longrightarrow
F(t,\theta)=\sum_{m\le N}\theta^m
 a(t)^{\lceil m/68\rceil}f_m(t)=0\pmod{t^{H}},
$$
$$
a(t)=t(t-1)(7+4t+16t^2),\qquad
H=s-13-r_c.
\tag{33}
$$
所有原 Gaussian、进位、固定 conductor 及原来源格仍属于该必要式的前提。本文只对这个完整返回多项式使用 $(5)$；不反向由低轴核制造原完整核。

若 $F(t,Y)\ne0$，其实际总次数为 $D_F$，且
$$
H>(D_F+A)^3+(D_F+A)^2+(D_F+A),
\tag{34}
$$
则 $(33)$ 与本文定理矛盾。因此 $(34)$ 在原已付返回范围内排除该完整核。若 $(34)$ 不成立，本文没有排核结论。

特别，原二次临界 $N\asymp\sqrt p$ 下，单靠一个含未知固定常数的立方上界不能排除核。后继若进一步利用原 $F$ 不含 $X$ 的 Newton 多面体厚度，仍须重新付相应 mixed-degree 消元，而不能把本文纯次数常数直接删掉一维。本文不增加任何独立中央条件，也未改变同一 ordered scalar kernel 的预算。

## 10. 原文定位与依赖

- [前注：全稳定素簇、截断 D-property、Artin 根理想与固定低次数退出](2026-11-27-original-three-variable-vector-field-prime-d-property.md)，尤其 §6、§8。
- [R525：真实低轴与完整 M 必要投影](../results/R525-original-multiweight-wronskian-and-growing-kernel-support.md)，§1–2、§4。
- G. Binyamini, *Multiplicity estimates, analytic cycles and Newton polytopes*, [arXiv:1407.1183v2](https://arxiv.org/pdf/1407.1183)：§2 Lemma8、§3 Lemma13 与 Theorem3 提供原特征零循环结构。本文使用其结构，但正特征的有限流、截断 Rolle、全部 cap 与原奇点应用均在上文另证，未直接套其复解析定理。

全文为符号证明；没有执行数学脚本或产生新的数值回执。


## 11. 保原X薄度的矩形版本：不用复解析多面体定理

本节另立固定常数；不把第1节的未知 $M$ 自动视为较大固定次数的同一个稳定指标。最后得到对原 $P(t,Y)$ 的二次混合界。

先作整平移
$$
u=t+1,\qquad z=X+1,
$$
使原点变为三维 torus 内的 $(u,z,Y)=(1,1,1)$。导子变为
$$
\widehat V
=6(u-1)(2-u)\partial_u
 +\left((2u-1)(z-1)+\frac23(u-1)\right)\partial_z
 +6(2-u)(z-1)Y\partial_Y.
\tag{35}
$$
按“系数单项式减去所微分坐标的一个指数”计支撑，准确有
$$
\boxed{\Delta_{\widehat V}
 \subset[-1,1]_u\times[-1,1]_z\times\{0\}_Y.}
\tag{36}
$$
因此一次导数至多把 Laurent 支撑的每个方向各增厚1；实际 $Y$ 厚度甚至不增加。本节用单位立方体作保守增厚，不丢掉任何导数项。

在此 torus 的稳定素理想收缩到多项式环后仍稳定，随后平移回原坐标。因此前注的稳定素簇分类在该开集继续成立。通过 $(1,1,1)$ 的稳定叶仍包含原 $t=u-1$，沿原弧其阶为1。

### 11.1 新的固定小次数费用

置
$$
h_0=24\cdot2^3\cdot3=576,\qquad d_{\square}=6h_0=3456.
$$
对总次数不超过 $d_{\square}$ 的多项式，重新用前注第8节的通用 Noetherian 升链，取一个固定稳定指标 $M_{\square}\ge1$。定义
$$
L_{\square}=d_{\square}+3M_{\square},\qquad
B_{\square}=\max\{M_{\square},h_0\},\qquad
C=h_0+B_{\square}.
\tag{37}
$$
本节额外要求
$$
\boxed{
p>\max\{83,L_{\square}^3,2B_{\square}+3\}.
}
\tag{38}
$$
这些均为固定存在常数，不是已计算的有效数字。

若一个 Laurent 多项式的支撑在 $[-h_0,h_0]^3$，乘以
$(uzY)^{h_0}$ 后变成总次数至多 $6h_0$ 的多项式。在 torus 上该乘子是单位。对于任一素簇，首导数退出阶不变：若前 $\ell$ 个导数都在其理想内，则 Leibniz 公式给
$$
\widehat V^\ell\big((uzY)^{h_0}P\big)
 \equiv(uzY)^{h_0}\widehat V^\ell P
 \pmod{I(Z)}.
\tag{39}
$$
因而小 Laurent 次数的退出由 $M_{\square}$ 支付。整平移不增总次数，所以这个 Noetherian 步骤仍是同一个原导子的通用步骤。

## 12. 完整矩形的Hilbert比较与576阶退出

给整数 $A_1,A_2,A_3\ge h_0$，记
$$
\Delta=\prod_{i=1}^3[-A_i,A_i],\qquad
\Delta_d=\Delta\cap[-d,d]^3,\qquad
a_i(d)=\min(A_i,d).
$$
$L_\Delta$ 表示由该矩形**全部**整数单项式组成的 Laurent 线性空间，不是任取的稀疏列。对非零 Laurent 多项式，$\deg_\infty$ 是其支撑最小中心立方体的半边长。

### 12.1 任意特征的限制空间维数界

将 torus 紧化为 $(\mathbf P^1)^3$，记三个超平面类为 $H_1,H_2,H_3$。矩形 $\Delta_d$ 的完整单项式，在乘一个单位单项式后给出线丛
$$
\mathscr L_d=2a_1(d)H_1+2a_2(d)H_2+2a_3(d)H_3
\tag{40}
$$
的全部截面。各边长为正时，这是实际 Segre–Veronese 嵌入，任意特征下均为闭嵌入；这里没有仅由少数单项式构造可能不可分的映射。

对 $k$ 维不可约 $W$，该嵌入下的限制空间维数满足
$$
\boxed{
\dim(L_{\Delta_d}|_W)
 \le [\overline W]\cdot\mathscr L_d^k+k.
}
\tag{41}
$$
理由是其像在自己的线性包中非退化，而一个 $k$ 维非退化射影簇的次数至少为其余维加1。这个纯代数次数界可由一般超平面旗标降到零维截面得到：最终截面仍张成相应线性包，其长度至少为包的向量空间维数。度数使用实际嵌入，所以等于右边的交数；不需要特征零或可分投影假设。

设 $d>h_0$。此时 $a_i(d)\ge h_0$，并有
$$
\begin{aligned}
\#(\Delta_{d-1}\cap\mathbf Z^3)
 &=\prod_i(2a_i(d-1)+1)\\
 &> (1-1/d)^3\,\operatorname{Vol}(\Delta_d)
 >\frac12\operatorname{Vol}(\Delta_d),\\
\mathscr L_d^3&=6\operatorname{Vol}(\Delta_d).
\end{aligned}
\tag{42}
$$
若某个 $k\le2$ 维 $W$ 满足
$$
[\overline W]\cdot\mathscr L_d^k
 \le\mathscr L_d^3/24,
$$
则由 $\mathscr L_{d-1}\le\mathscr L_d$、$(41)$，
$$
\dim(L_{\Delta_{d-1}}|_W)
 \le \tfrac14\operatorname{Vol}(\Delta_d)+2
 <\tfrac12\operatorname{Vol}(\Delta_d).
$$
结合 $(42)$，便有一个非零 $Q\in I(W)\cap L_\Delta$、$\deg_\infty Q<d$。

因此，若 $P$ 是 $I(Z)\cap L_\Delta$ 中最小 $\deg_\infty$ 的非零元素，$d=\deg_\infty P>h_0$，则每个 $Z\subset W$ 都满足
$$
\boxed{
[\overline W]\cdot\mathscr L_d^{\dim W}>
 \mathscr L_d^3/24.
}
\tag{43}
$$

### 12.2 保完整支撑的退出构造

设 $Z$ 不包含于任何真稳定素簇。使用长度 $2B_{\square}+1$ 的有限流及 cap $B_{\square}+1$，重复第6节的局部归纳，但把总次数界改为
$$
[\overline{\Gamma^j}]\cdot\mathscr L_d^{3-j}
 \le2^j\mathscr L_d^3.
\tag{44}
$$
初始循环为 $P$ 的除子中包含 $Z$ 的分量，保全部因子重数。其它分量在每个包含 $Z$ 的簇的一般点都是单位，故不贡献所用局部重数。这里不要求 $P$ 的单个因子仍属于原矩形。

由 $(43)$、$(44)$，每个分量的权准确受限为
$$
m_i<24\cdot2^j.
$$
第6节的同一个加权 cap 归纳与一次横截性于是给首退出阶
$$
\ell_i<24\cdot2^j j\le576=h_0.
\tag{45}
$$
若这些导数仍全在 $I(Z)$ 内，就用第一个退出该分量的导数作适当交，并保留包含 $Z$ 的分量。由 $(36)$，
$$
\Delta(\widehat V^{\ell_i}P)
 \subset\Delta_d+\ell_i[-1,1]^3
 \subset2\Delta_d,
\tag{46}
$$
因为 $\Delta_d$ 含 $[-h_0,h_0]^3$。其闭包的有效除子属于 $2\mathscr L_d$；可能的边界分量全部保为有效费用，丢弃它们只降低与 nef 类的交数。因此 $(44)$ 逐层保持。

最多三层后到达 $Z$，与“所有 $\le576$ 阶导数均未退出”矛盾。全部局部步骤正是第3–6节已付的截断版本，不另借无限流。小 $\deg_\infty\le h_0$ 的情形则由 $(39)$ 与固定 $M_{\square}$ 支付。得到
$$
\boxed{
P\in I(Z)\cap L_\Delta\text{ 最小 }\deg_\infty
\Longrightarrow
\exists\,1\le j\le B_{\square},\
 \widehat V^jP\notin I(Z).
}
\tag{47}
$$

## 13. 原无X多项式的明确二次混合界

现在取
$$
0\ne P(t,Y),\qquad
a=\deg_tP,\quad b=\deg_YP.
$$
平移后 $P(u-1,Y)$ 的支撑仍在
$[0,a]\times\{0\}\times[0,b]$。选择
$$
\Delta=[-(a+h_0),a+h_0]\times[-h_0,h_0]
       \times[-(b+h_0),b+h_0].
$$
原 $P$ 属于这个完整矩形。在每个森林节点的理想中，依 $(47)$ 选择这个固定矩形内最小 $\deg_\infty$ 的方程，再以其首退出导数相交。因此每个新交方程的支撑均在同一个固定增厚
$$
\Delta^*=[-(a+C),a+C]\times[-C,C]
          \times[-(b+C),b+C].
\tag{48}
$$
$X$（即平移后的 $z$）厚度确为固定 $C$，不随 $a,b$ 增长。

置
$$
U=a+C,\qquad W=b+C,\qquad
\mathscr L=2U H_1+2C H_2+2W H_3,\qquad
\mathscr H=H_1+H_2+H_3.
$$
每层闭包循环与任何所需 nef 类的交数，由实际有效除子和适当交，分别上界为 $\mathscr L^j$ 的相应交数。每个叶在原点的普通重数不超过它与 $\dim W$ 个一般 $\mathscr H$ 截面的全交数；这些截面的原点一次 jet 足够一般，故确实比较同一个局部重数。

第8节奇点 cap 与叶阶1的证明完全保持。利用
$H_i^2=0$、$H_1H_2H_3=1$，得到
$$
\boxed{
\begin{aligned}
\min\{s,\operatorname{ord}_tP(t,\theta(t))\}
&\le \mathscr L^3+\mathscr L^2\mathscr H+\mathscr L\mathscr H^2\\
&=48UCW+8(UC+UW+CW)+4(U+C+W).
\end{aligned}
}
\tag{49}
$$
这是完整的二次混合界：
$$
\boxed{\min\{s,\operatorname{ord}P(t,\theta)\}
       =O_V((a+1)(b+1)).}
\tag{50}
$$
其固定常数由 $(37)$ 指定的存在常数控制，仍未声称数值有效。Laurent 清分母仅在原点为单位的三维 torus 中使用；没有将 $t=0$ 的真实消失因子除掉。

## 14. 同一个原M中的可用二次范围

对第9节的原完整返回，
$$
F(t,Y)=\sum_{m\le N}Y^m
 a(t)^{\lceil m/68\rceil}f_m(t),
$$
原帽
$$
\deg f_m\le\lfloor11m/34\rfloor-4\lceil m/68\rceil
$$
给
$$
\deg_t F\le a_N:=\lfloor11N/34\rfloor,\qquad
\deg_YF\le N.
\tag{51}
$$
把 $(49)$ 的右边记为 $\mathcal B_V(a,b)$。在原来源返回、固定坏素数、$(38)$ 及 conductor 全部条件下，
$$
\boxed{
H=s-13-r_c>\mathcal B_V(a_N,N)
\quad\Longrightarrow\quad
\text{原完整 }\bar M\text{ 没有非零且返回 }F\ne0\text{ 的核}.
}
\tag{52}
$$
这消费的是原实际矩阵的同一必要低轴，而不是自由环境列。若原规范化来源已付 primitive 返回非零，则 $(52)$ 直接排除该来源中的完整核。

例如充分的数值形式为
$$
p>6\mathcal B_V(a_N,N)+77+6r_c,
\tag{53}
$$
再同时保 $(38)$ 与原返回范围。这里 $(53)$ 只是存在常数控制的二次 cutoff。

原二次临界中 $s$ 与 $N^2$ 的比例已经固定；$(49)$ 的首系数含尚未计算的 $C$。因此本文仍没有证明临界核消失、同一 ordered scalar kernel 的严格预算改善，或任一 canonical 中央非零。二次指数本身也不能替代原需要严格改善的常数或全精度返回。后续须对这个实际低轴与原其余块继续联立，不能把已付的固定厚度换成零厚度。

### 14.1 同一个实际低轴的真秩下界

保持原规范化来源的独立列与已付 conductor 返回；不得为本推论添自由环境列。定义
$$
n_H=\max\bigl(\{0\}\cup
 \{1\le n\le N:\mathcal B_V(\lfloor11n/34\rfloor,n)<H\}\bigr).
\tag{54}
$$
在原独立低权子格 $\mathcal B_{\le n_H}$ 上，任何非零约化列组合都给非零 $F(t,Y)$，所以 $(49)$ 使其不能在全部 $H$ 个原低轴位置消失。因此，若该子格已由原固定 conductor 整返回到当前实际来源，
$$
\boxed{
\operatorname{rank}_{\Bbbk}(\text{原第一块})
 \ge \dim_{\Bbbk}\mathcal B_{\le n_H}.
}
\tag{55}
$$
有 conductor 的源权平移与固定原点阶仍分别记在实际预算和 $H=s-13-r_c$ 内，不从矩阵中删除。

原已付维数为 $\dim\mathcal B_{\le n}=9n^2/68+O(n)$，而
$$
\mathcal B_V(\lfloor11n/34\rfloor,n)
 =\frac{44(6C+1)}{17}n^2+O_C(n).
$$
故在 $N$ 足以容纳 $(54)$ 且 $H\to\infty$ 的范围，
$$
\boxed{
\operatorname{rank}(\text{原第一块})
 \ge\left(\frac9{176(6C+1)}+o(1)\right)H.
}
\tag{56}
$$
这是一个由同一实际来源与同一低轴读者得到的正比例秩下界，常数存在但未知。它远小于 $H$，不会越过行数，也不声称原临界全部列独立。第二、第三块、同一首提升与真正 Schur 返回仍须另外联立。


## 15. 与已登记二维接触界的准确关系

本节核对在本稿之前已经登记的 [R467 原 Theta 补充](2026-11-14-r467-mixed-j-original-theta-extension.md)及 [R637](../results/R637-original-short-three-block-square-root-surjectivity.md)。**二维 $P(t,Y)$ 的二次指数并非本次首次得到，应优先调用旧文更强且显式的实际接触界；§§11–14仅记录本次三变量森林方法的薄窗推论，不把它另计为新的临界排核或主预算改善。**

具体地，R467 补充已经在同一个实际 $\Theta$ 上证明：不可约 $F(t,Y)$ 经过 $(0,1)$，$a=\deg_tF$、$b=\deg_YF<p$、$c=\operatorname{mult}_{Y=1}F(0,Y)$ 时，
$$
\min\{\operatorname{ord}_tF(t,\theta),s\}
 \le a(6b-1)-2c+3.
\tag{57}
$$
该文同时保全部真实因子和权重，见其(6)–(9)。原 $b=1$ 分支还有 $4a+1$ 的显式界。临界 $N\asymp\sqrt p$ 时 $N<p$ 最终成立，故这些旧界适用，不能以本稿未知且较大的 $C$ 取代它们。

R637 还在原 $\rho=(1+8t)\Theta^{17}$、全角帽和真正短三块上，用原 ODE、完整分支判别式及可提升自由异常链，给已登记的平方根量级整满射范围；它明确没有覆盖真实临界区。该来源包含、全部 Gaussian 高尾及完整 carry 条件继续按原文使用。

本稿独立支付的是含对数变量 $X$ 的三变量全稳定素簇之后，真正正特征、有限截断轨道上的局部 cap、统一最小方程退出和完整交循环论证。下一工作须消费原第二、第三块与同一首次修正的真实像，而不是重复二维接触界或把低轴单位秩直接当作所需全位行列式收益。


## 16. 原两长一短行的完整垂直厚理想

本节消费 R534(38)–(49) 已付的同一个实际三块，不把第14.1节的秩下界复制三次。记
$$
E=Y\partial_Y,\qquad
P(t,Y)=\sum_m a(t)^{c_m}f_m(t)Y^m,\qquad
a(t)=t(t-1)(7+4t+16t^2).
$$
保原独立来源、conductor 整返回、共同目标单位及全部固定坏素数。原首核必要长度为
$$
H=s-d_0,\qquad K=\ell_+-d_0,\qquad 0<K\le H<s,
\quad d_0=13+r_c.
$$
通常目标 $\ell_+=\ell+d_0$ 时，$K=\ell$。相同来源的 primitive 模 $p^2$ 右核约化，则由 R534(48) 的两条实际进位逐坐标得到内层全长
$$
H=s,\qquad K=\ell.
$$
这项加强只使用 $m_{d_0}$ 的真实 Smith 因子，不删除下一位的 carry，也不是首核向第二核的充分条件。

在两种范围，实际必要式都是
$$
P(t,\theta),\quad (EP)(t,\theta)\in t^Hk[[t]],
\qquad (E^2P)(t,\theta)\in t^Kk[[t]].
\tag{58}
$$
这里 $\theta$ 只需原有限 regularized 轴的相应 jet；任取与它相容的形式延拓，以下条件及结论都不依赖未读取尾。设置
$$
h=Y-\theta(t),\qquad
P(t,\theta+h)=c_0(t)+c_1(t)h+c_2(t)h^2+h^3Q(t,h).
$$
因为 $\theta$ 是单位且 $2$ 可逆，
$$
c_0=P(t,\theta),\qquad
c_1=\theta^{-1}(EP)(t,\theta),\qquad
c_2=\frac{(E^2-E)P(t,\theta)}{2\theta^2}.
$$
故 $(58)$ 精确等价于
$$
\boxed{
P(t,\theta+h)\in(t^H,\ t^Kh^2,\ h^3)
\subset k[[t]][h].
}
\tag{59}
$$
特别，第二行不是另一条曲线；它是同一原曲线的第一垂直 jet。第三短行则是同一厚理想中 $h^2$ 的真实截断。上式没有把这个非约化理想误认作一个完整可积闭簇理想。

原向量场还准确满足
$$
[V,E]=0.
$$
这只表示在环境多项式环中两个算子对易；它不给 $VP$ 或某个来源连接新的 canonical 零。需要跨 $t^s$ 时仍须使用 R534(23)、(31)、(36) 对原 ODE 缺陷的完整支付，不能由 $(59)$ 延长一个不存在的无限特征 $p$ 解。

### 16.1 去掉的只是显示分类因子，不是新来源

直接对整个 $P$ 取 $Y$ 判别式一般没有意义：正权来源常共同含高次 $Y$，它在原点 $Y=\theta$ 是单位，却会使全局判别式恒零。必须先写实际唯一的分解
$$
P=t^rY^{m_0}P^\circ,\qquad
t\nmid P^\circ,\quad Y\nmid P^\circ,
$$
其中 $m_0$ 是出现的最小权，$r$ 是各 $Y$ 系数共同的准确 $t$ 阶。这里只在函数域中分类这个已给出的向量，绝不把 $P^\circ$ 免费加入原来源格。

令
$$
H'=\max(H-r,0),\qquad K'=\max(K-r,0).
$$
由于
$$
E^j(Y^{-m_0}P)=Y^{-m_0}(E-m_0)^jP
\quad(j=0,1,2),
$$
且 $K\le H$，同一原必要式给
$$
\boxed{
P^\circ(t,\theta+h)\in
(t^{H'},\ t^{K'}h^2,\ h^3).
}
\tag{60}
$$
这一步同时保留两次 Euler 的下三角项 $-m_0P$、$-2m_0EP+m_0^2P$。没有仅在第一块提出 $Y^{m_0}$，再在另两块遗漏电荷。

若 $H'=0$，本节不声称有额外接触约束。以下设 $H'>0$，记
$$
b=\deg_YP^\circ.
$$
$t\nmid P^\circ$ 立刻排除 $b=0,1$：其平移后的全部系数都会被 $t^{H'}$ 整除。若 $K'>0$，同理还排除 $b=2$。所以真正的第三短行进入时必有 $b\ge3$；$K'=0,b=2$ 则是原低角二重边界，不能偷偷按三重分支处理。

## 17. 两长一短条件的同一个判别式费用

下面的身份在整数系数环中成立，不需要原 ODE。令
$$
F(h)=c_0+c_1h+h^2Q_2(h),\qquad \deg F=b\ge3,
\quad Q_2(0)=c_2.
$$
所有判别式都采用实际最高次系数的通常多项式判别式，未先把非单位最高系数除掉。则
$$
\boxed{
\operatorname{Disc}_h(F)
\equiv
-4c_0c_2^3\operatorname{Disc}_h(Q_2)
\pmod{(c_0,c_1)^2}.
}
\tag{61}
$$

**完整证明。** 判别式的常数项在 $c_0=c_1=0$ 时为零。置 $c_0=0$，由
$F=h(hQ_2+c_1)$ 及判别式的乘积公式，得到
$$
\operatorname{Disc}F=c_1^2\operatorname{Disc}(hQ_2+c_1).
$$
因此没有单独的一次 $c_1$ 项。

为求一次 $c_0$ 项，可在通用系数分式域中令 $c_1=0$、$c_0=\varepsilon$。先取 $c_2$、最高系数及 $\operatorname{Disc}Q_2$ 都非零的通用点。原双根 $0$ 分裂的根差平方的一次项是 $-4\varepsilon/c_2$。与其余根的全部交叉根差平方给 $(c_2/A)^4$；其余根之间的根差平方给 $\operatorname{Disc}Q_2/A^{2b-6}$，其中 $A$ 是实际最高系数。再乘 $\operatorname{Disc}F$ 中的 $A^{2b-2}$，所有 $A$ 完全相消，留下
$-4\varepsilon c_2^3\operatorname{Disc}Q_2$。

两边均是通用整数系数多项式，因此这个一次系数身份从通用点延拓到整个系数环；没有给特化后的 $c_2$、$A$ 或判别式施加单位假设。这证明 $(61)$，也保留它在原特征 $p>3$ 的全部特化。证毕。

将 $(60)$ 代入 $(61)$。所有二次 $(c_0,c_1)$ 项至少为 $2H'$ 阶，一次项至少为 $H'+3K'$ 阶。判别式不随 $Y$ 的平移而改变，故得到
$$
\boxed{
\operatorname{ord}_{t=0}\operatorname{Disc}_Y(P^\circ)
\ge T(H',K'):=\min(2H',\,H'+3K').
}
\tag{62}
$$
这里允许判别式恒零，按无限阶理解。若 $b=2$，前节已迫 $K'=0$；此时
$\operatorname{Disc}F=c_1^2-4c_0c_2$ 仍给 $(62)$，其右边为 $H'$。

因此，只要 $P^\circ$ 在 $k(t)[Y]$ 中平方自由，且
$a^\circ=\deg_tP^\circ$，便有准确必要式
$$
\boxed{
T(H',K')\le(2b-2)a^\circ.
}
\tag{63}
$$
这是同一完整多项式的判别式次数界，不是把三个秩相加。它无需对单个分支取根，也未逐支除 $P^\circ_Y$。当 $(63)$ 失败时，得到的是实际 $P^\circ$ 有重复非边界因子，而非原核已被排除。

特别，不能在 $\operatorname{Disc}P^\circ=0$ 时继续把 $(62)$ 的右边同一个有限次数比较；这种情形正是必须返回原因子、同一修正 $R$ 与 Bockstein 的范围。

## 18. 原全部角帽给更准确的判别式预算

本节不将原来源换成自由双次数矩形。仍取
$$
c_m=\lceil m/68\rceil,\qquad
\deg f_m\le\lfloor11m/34\rfloor-4c_m.
$$
令实际最高权为 $m_1=m_0+b$，并置
$$
W=(b-1)(b+2m_0).
$$
在 $P^\circ=\sum_{i=0}^b A_i(t)Y^i$ 中，每个实际非零系数满足
$$
\deg_t A_i\le\left\lfloor\frac{11(m_0+i)}{34}\right\rfloor-r.
$$
通常次数 $b$ 的判别式对全部系数齐次次数为 $2b-2$，对第 $i$ 系数赋权 $i$ 时加权次数为 $b(b-1)$。所以其中每个非零单项式的原来源权总和严格等于
$$
m_0(2b-2)+b(b-1)=W.
$$
于是
$$
\boxed{
\deg_t\operatorname{Disc}_Y(P^\circ)
\le\left\lfloor\frac{11W}{34}\right\rfloor-r(2b-2).
}
\tag{64}
$$
最高系数可以在角点消失；此齐次计算没有先作首一化。

原角多项式 $a(t)$ 在 $t=1$ 和 $7+4t+16t^2=0$ 的两个根都有单零。$p>83$ 保这三点互异、非零，并与原点分离。除以 $t^r$ 在这些点是单位，所以
$$
\operatorname{ord}_{t=\alpha}A_i\ge
\left\lceil\frac{m_0+i}{68}\right\rceil
\quad
\left(\alpha=1\text{ 或 }7+4\alpha+16\alpha^2=0\right).
$$
同一个齐次权计算给每点的完整必消阶至少为
$\lceil W/68\rceil$。可先在代数闭剩余域分别计算再下降；两个共轭角不能合并成只付一次。

若 $\operatorname{Disc}_YP^\circ\ne0$，结合这三个真实角及原点的 $(62)$ 得
$$
\boxed{
\min(2H',\,H'+3K')
+3\left\lceil\frac{W}{68}\right\rceil
\le
\left\lfloor\frac{11W}{34}\right\rfloor-r(2b-2).
}
\tag{65}
$$
这是原实际三块、原 $68$ 类 ceiling、全部三个外角及显示原点含量共同给出的必要条件。没有删除 $m_0$ 的电荷，也没有把高次数共同 $Y$ 因子误当成非边界重因子。

若 $(65)$ 失败，则实际 $P^\circ$ 在 $k(t)[Y]$ 有重复因子。若同时保原 $N<p$，它在 $Y$ 中的正次数严格小于 $p$，故这不是单独的不可分 $p$ 次幂伪影；确有某个非边界不可约因子以至少二重出现。它是否三重、在原曲线上的接触多深，以及其乘法和角帽是否允许同预算修正，都仍须在原多项式上检查。

### 18.1 同一首次修正及真正第二余核保持

本节只缩小真实首核或真实模 $p^2$ 核约化的形状。对于原 $M$ 的下一位，仍必须由同一个允许修正 $R$ 实现 R479(3)：
$$
\bar J\bar R+\overline{J(P^0)/p}
=t^{s-d_0}B_0+\epsilon_t t^{s-d_0}B_1,
$$
两条 $B_0,B_1$ 是这个 $R$ 的真实图形输出，不是可以独立选择的来源。显示写法按一般 $d_0$ 的进位带理解；不用 conductor 时恰为原两条十三行。

采用 R481 的完整高轴规范形后，相对首提升仍先解
$$
\bar K_z\bar R_z
=-\overline{\mu_z+\mathcal A_zP^{\rm base}},
$$
再由这个同一 $R_z$ 计算
$$
\boxed{
\Xi_z(P,R_z)=
\overline{
\frac{\mu_z+K_zR_z+\mathcal A_zP^{\rm base}}p
+\mathcal A_zR_z+\mathcal B_zP^{\rm base}}.
}
\tag{66}
$$
最后只在原真实 $G_{2,z}$ 中取类。$(65)$ 没有删掉其中的低行高尾、Miller 乘子、两个 carry 或共同 charge；也没有把单位 $5$、$-2$ 的 normal 项单独当作非零余核。

现有第14.1节的单位秩下界与 $(65)$ 的重复因子必要性，均是同一矩阵的有限信息。原全局严格斜率仍按
[固定深度预算说明](2026-11-14-deep-fixed-depth-tame-average-budget.md)
的同一饱和旗标及全 Smith 指数和读取：固定三块只覆盖 $p$ 与相应 jet 同量级的一段，不能单凭这里的单位比例改写 $a_I+2b_I<3$。后续真正需要的是重复因子范围内的同一 $(66)$ 强迫，或增长块数与全部原跳跃的完整估值。这里未把任一有限判别式约束升级为 canonical 中央非零。
