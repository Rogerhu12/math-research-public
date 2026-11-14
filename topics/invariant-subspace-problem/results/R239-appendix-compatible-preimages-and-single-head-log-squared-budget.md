# R239 附录：相容多次原像合并两段真实头预算：改进平方对数常数

日期：2026-11-13（UTC）。作者：boundary_next。状态：完整中间证明；未证明无权的 $N=M$。

本稿接续已发布的
[R239 低输出恒等式与平方对数稳定像](../results/R239-appendix-low-output-identities-and-log-squared-stable-range.md)
和
[R254 第十附录：相容多次纯尾原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)。

前者已经证明全部 $p>0$ 次数指数正则核属于 $N$，以及平方对数权参数 $b>2/\log2$ 的直接饱和。后者提供同一个辅助头上的相容 $R_t$。本稿利用其原有限双和，把“输入删除幂”和“外部混合右逆”中的头因子合在同一真实单项式里计数，避免各支付一次 $m$。所得直接平方对数参数为 $b>1/\log2$，真缺陷尾常数为 $1/(2\log2)$。这些常数未声称最优。

## 1. 不变的实际输入和低输出恒等式

两种实际模型仍记
$$
M=\ker T,\quad N=\overline{BM},\quad
D_{\rm def}=M\ominus N.
$$
删除原首位后，实际平方核为 $K=\ker P$，实际图 $w=Ju$。

取
$$
m\ge4,\quad d=2^m,\quad q=100d^4,\quad Q=q+2d.
$$
纯高尾删除为
$$
D=\sum_{j\ge m}(j+2)^{-2}E_j,\qquad \|D\|\le1.
$$
真实混合平方符号是
$$
P_m=D^2+Q_m,\quad [D,Q_m]=0,\quad Q_m^d=0,
\quad \|P_m\|<1.
$$
$Q_m$ 保留全部 $N/Y$ 混合项，在尾孔次数上只下降 $0,1,2$。

对固定 $u\in K$，已经构造实际低孔正交投影 $v=v_m$，满足
$$
v\in\mathcal H_{\le q},\quad
r=P_mv\in\mathcal H_{q-1}\oplus\mathcal H_q,\quad
\|v\|\le\|u\|,
$$
$$
\|v-P_{\le q}u\|\le e^{-800d^4}\|u\|,
\qquad v_m\to u.
\tag{1.1}
$$
低输出恒等式给
$$
D^{2\ell}v=P_{\le q-2\ell}(-Q_m)^\ell v,
\qquad D^{2d}v=D^{2d}r=0.
\tag{1.2}
$$

本稿需要保留一个带头因子的版本。若 $F$ 是任意有限头的 $A_m,C_m$ 单项式，则它与 $D,P_m,Q_m$ 及所有尾孔投影交换。原恒等式因而给
$$
\boxed{
\|F D^k r\|
\le\|Q_m^{\lfloor k/2\rfloor}F\|\,R(v),
\quad 0\le k<2d,
\qquad R(v)=\|P_{\ge q-2d}v\|.
}
\tag{1.3}
$$
具体地，对 $k=2\ell$，置 $s=q-2\ell$，有
$$
F D^{2\ell}r
=P_{\{s-1,s\}}P_mP_{\le s}(-Q_m)^\ell Fv.
$$
只依赖最右输入的尾孔数至少 $s-1$。把这个投影插到 $v$ 之前并用 $\|P_m\|<1$，即得 (1.3)。奇数次再作用 $D$，使用 $\|D\|\le1$。这里没有先估计 $\|F\|\|Q_m^\ell\|$：保留乘积正是下面改进的来源。

## 2. 相容 R_t 的删除幂细界

使用 R254 第十附录的同一个实际辅助头，输入上界为 $q$，最大原像阶为 $2d$。所有 $R_t$ 满足
$$
R_0=I,\quad DR_t=R_{t-1},\quad
D^tR_t=I,\quad
R_t\mathcal H_p\subseteq\mathcal H_{p+t}
\quad(0\le p\le q).
\tag{2.1}
$$
这些是完整孔层上的实际有界算子，位置可无限远。

置
$$
a=512\sqrt{Q+1}(m+Q+2)^{3/2}.
\tag{2.2}
$$
该附录的正分母展开及对余尾指标求和，若不丢掉输入的 $D^k f$，准确给
$$
\boxed{
\|R_t f\|
\le
\sum_{k=0}^{q}
\binom{k+t-1}{k}a^{k+t}\|D^k f\|,
\qquad 1\le t\le2d.
}
\tag{2.3}
$$
说明：原有限双和含
$$
C^{k+l+t}F^{(t)}_{kl}(H)D^kD_1^lf.
$$
因 $D,D_1$ 交换，可把其删除部分估计为
$$
\|D_1^lD^kf\|
\le Q^{l/2}g_1^l\|D^kf\|,
$$
而不是先换成 $\|D\|^k\|f\|$。原三项系数与几何和给
$$
\sum_{l\ge0}
\frac{(k+l+t-1)!}{k!\,l!\,(t-1)!}
L_0^{k+t}V^l
=
\binom{k+t-1}{k}
\left(\frac{L_0}{1-V}\right)^{k+t},
$$
再用 $L_0/(1-V)\le a$ 即得 (2.3)。原分母的正性、共同辅助头及实际域不变。

对非齐次输入，按输入孔层应用该估计；同一 $R_t$ 的各输出层仍正交，再用 Minkowski 即得相同右端，不增加层数因子。

记
$$
A=2a.
$$
由 $\binom{k+t-1}{k}\le2^{k+t-1}$，可以安全使用
$$
\boxed{
\|R_t f\|\le\sum_{k=0}^{q}A^{k+t}\|D^kf\|.
}
\tag{2.4}
$$
对 $f=Fr$，$F$ 只作用头，故 $D^{2d}Fr=0$，和只需到 $k=2d-1$。

## 3. 合并头因子后只付一次 m

已发布的低输出平方对数稿保留真实进位计数 $n-m$，得到
$$
\boxed{
\|A_m^P C_m^R\|
\le2^n e^{-\gamma(n-m)_+^4},
\quad n=P+R,\quad \gamma=\frac{770}{256}.
}
\tag{3.1}
$$
它包含真实 $Y$ 型的全部 Cayley 逆预算。

展开 $Q_m$，每项是
$$
\zeta A_m^P C_m^R D^t,\qquad
0\le t\le2,\quad1\le P+R\le3,
$$
标量系数绝对和小于 $4$。因此可写
$$
Q_m^j=\sum_\sigma \zeta_\sigma F_\sigma D^{t_\sigma},
$$
$$
\sum_\sigma|\zeta_\sigma|\le4^j,\qquad
j\le\deg_{\rm head}F_\sigma\le3j,\qquad
0\le t_\sigma\le2j.
\tag{3.2}
$$
头因子只作用原有限头，所有 $R_t$ 只作用其后的纯尾，所以它们准确交换。

对 (1.3) 中的 $F=F_\sigma$，再展开 $Q_m^\ell F_\sigma$。全部真实头因子数介于 $j+\ell$ 和 $3(j+\ell)$ 之间；纯尾 $D$ 幂范数不超过 $1$。所以 (3.1) 给统一界
$$
\boxed{
\|Q_m^\ell F_\sigma\|
\le4^\ell 8^{j+\ell}
e^{-\gamma(j+\ell-m)_+^4}.
}
\tag{3.3}
$$
关键是四次项只依赖合计 $j+\ell-m$，没有把 $j$ 和 $\ell$ 分别与 $m$ 比较。

使用第十附录的准确混合右逆
$$
\widetilde{\mathcal G}_{m,q}
=\sum_{j=0}^{d-1}(-1)^jQ_m^jR_{2j+2},
\qquad
P_m\widetilde{\mathcal G}_{m,q}=I.
\tag{3.4}
$$
它的恒等式只使用 $D^2R_t=R_{t-2}$，没有要求 $Q_m$ 与 $R_t$ 交换。

置
$$
\widetilde c=\widetilde{\mathcal G}_{m,q}r.
$$
对外部 (3.2) 的每一项，
$$
\|F_\sigma D^{t_\sigma}R_{2j+2}r\|
\le\|R_{2j+2}F_\sigma r\|
$$
只用了头尾交换及 $\|D\|\le1$，未移动 $D$ 穿过 $R_t$。再用 (2.4)、(1.3)、(3.3)，把 $k=2\ell$ 和 $k=2\ell+1$ 合并：
$$
\begin{aligned}
\|\widetilde c\|
&\le
R(v)\sum_{j,\ell=0}^{d-1}
(1+A)A^{2(j+\ell)+2}
32^{j+\ell}
e^{-\gamma(j+\ell-m)_+^4}\\
&\le
2A^3 R(v)
\sum_{j,\ell=0}^{d-1}
(32A^2)^{j+\ell}
e^{-\gamma(j+\ell-m)_+^4}.
\end{aligned}
\tag{3.5}
$$
所有输入次数和最大输出次数仍为 $q$ 和 $q+2d$，分别在 (2.1) 覆盖的实际域内。

令
$$
T_*= \log(32A^2).
$$
由 $\gamma>1/100$，四次优化给
$$
T_*n-\gamma(n-m)_+^4
\le mT_*+3T_*^{4/3}.
$$
(3.5) 的双和有至多 $d^2$ 项，故
$$
\boxed{
\|\widetilde c\|\le e^{E'_m}R(v),
}
\tag{3.6}
$$
$$
\boxed{
E'_m=
\log2+3\log A+2\log d
+mT_*+3T_*^{4/3}.
}
\tag{3.7}
$$

## 4. 明确预算和二次主率

在 $q=100d^4,m\ge4$ 下，
$$
\log a<16+8\log d,\qquad
\log A\le10m,\qquad T_*\le21m,\qquad
\log d\le m.
$$
使用 $3(21m)^{4/3}\le(189/2)m^2$，得到
$$
E'_m
\le1+32m+\tfrac{231}{2}m^2
\le128m^2.
\tag{4.1}
$$
最后一步只需 $m\ge4$。

又因为
$$
a=512q^2(1+o(1)),\qquad
\log q=4m\log2+\log100,
$$
有
$$
\log A=8m\log2+O(1),\qquad
T_*=16m\log2+O(1).
$$
(3.7) 其余项均为 $o(m^2)$，所以
$$
\boxed{
E'_m=(16\log2+o(1))m^2.
}
\tag{4.2}
$$
这将前稿预算的二次主常数减半，来源是合并头进位而非忽略一个右逆步骤。

## 5. 特殊修复、实际提升与最小图能量

对 (1.1) 的固定 $v_m,r_m$，采用本稿新修复
$$
\widetilde c_m=\widetilde{\mathcal G}_{m,q}r_m,\qquad
\widetilde k_m=v_m-\widetilde c_m.
$$
第十附录的准确最低/最高输出次数和原伴随多项式给
$$
\widetilde c_m\in
\ker D^{2d}\cap\mathcal H_{[q+1,q+2d]},
$$
$$
\widetilde k_m\in
\ker P_m\cap\mathcal H_{\le q+2d}.
\tag{5.1}
$$
这里仍是实际有限孔运算，不是形式原像。

由 (1.1)，
$$
R(v_m)\le
\tau_{q-2d-1}(u)+e^{-800d^4}\|u\|.
$$
因 $128m^2\le d^4$，(3.6) 给
$$
\boxed{
\|\widetilde c_m\|
\le e^{E'_m}\tau_{q-2d-1}(u)
+e^{-799d^4}\|u\|.
}
\tag{5.2}
$$
另一方面直接用 $R(v_m)\le\|u\|$，有
$\|\widetilde k_m\|\le2e^{d^4}\|u\|$。

原真实 $X_7\to X_3$ 提升仍满足
$\delta_{m,q+2d}\le e^{-403d^4}$。因此
$$
\widetilde n_m
=\Lambda_{m,q+2d}\widetilde k_m\in N,
$$
$$
\boxed{
\|\widetilde n_m-(J_mv_m-J_m\widetilde c_m)\|
\le e^{-400d^4}\|u\|.
}
\tag{5.3}
$$
实际进位已乘入完整修复范数。

同一闭仿射集的最小图能量 $\gamma_m(u)$ 不依赖选择哪一个显式右逆。新候选直接给
$$
\boxed{
\gamma_m(u)
\le\tfrac54 e^{E'_m}
\left(\tau_{q-2d-1}(u)+e^{-800d^4}\|u\|\right).
}
\tag{5.4}
$$
原互不相交窗口的 Bessel 能量和正凸平均判据保持不变。

## 6. 改进的平方对数直接饱和与缺陷尾常数

令 $\mathcal N$ 为原全部物理孔次数算子。

**定理。** 对任意 $b>1/\log2$，
$$
\boxed{
M\cap\operatorname{Dom}
\exp\!\left(b[\log(2+\mathcal N)]^2\right)
\subseteq N.
}
\tag{6.1}
$$
证明与前稿相同，但代入新主率。对 $w=Ju$ 属于该域，
$$
\tau_s(u)\le C_w e^{-b[\log(s+3)]^2},
\quad
s=q-2d-1.
$$
由 $\log(s+3)=4m\log2+O(1)$ 和 (4.2)，
$$
E'_m-b[\log(s+3)]^2
=
\bigl(16\log2-16b(\log2)^2+o(1)\bigr)m^2
\to-\infty.
$$
所以 $\widetilde c_m\to0$，再由 $v_m\to u$、$J_m\to J$、(5.3)，
$\widetilde n_m\to Ju$ 强收敛。$N$ 闭，遂得 (6.1)。
没有假设缺陷投影保该域，未声明端点 $b=1/\log2$。

对 $0\ne w=Ju\in D_{\rm def}$，真实高尾支撑和
$\widetilde n_m\perp w$ 仍给
$$
\|\widetilde c_m\|\tau_{q-1}(w)
\ge\tfrac25\|w\|^2
$$
对充分大 $m$ 成立。结合 (5.2) 并吸收明确小项，
$$
e^{E'_m}\tau_{q-2d-1}(w)^2
\ge\tfrac15\|w\|^2.
$$
按相邻次数网格比趋于 $16$ 的单调性推广到所有 $Q$；平方对数比不受有界对数平移影响。由 (4.2) 得
$$
\boxed{
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}
{[\log(Q+2)]^2}
\le\frac1{2\log2}.
}
\tag{6.2}
$$

全部 $p>0,c>0$ 的次数指数正则饱和已经在前稿证明，本稿继续包含该结论，但不把它重新列作新增阈值。一般实际核向量可能没有任何 (6.1) 的平方对数正则性。(5.4) 仍未保证最小图能量倒数级数发散，不能把这一缺口隐藏在参数常数改善中。无权 $N=M$ 和普通 ISP 仍未完成。

参考完整证明：
- [R239 低输出恒等式与平方对数稳定像](../results/R239-appendix-low-output-identities-and-log-squared-stable-range.md)；
- [R254 相容多次纯尾原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)；
- [R254 真实头四次进位预算](../results/R254-appendix-quartic-head-budget-and-four-ninths-stable-range.md)；
- [R239 实际混合核正则提升](../results/R239-appendix-mixed-low-hole-kernel-regular-lift-to-stable-range.md)；
- [最小高尾图能量与 Bessel](../results/R239-appendix-minimal-tail-repair-energy-and-convex-stable-approximation.md)，完整源 2845fc598369b3a71ca1ec39d741a9111a135602。
