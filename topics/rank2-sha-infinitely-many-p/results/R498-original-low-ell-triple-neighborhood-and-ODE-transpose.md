# R498 — 低 ell 的整个原首像、真实三厚化与 ODE 转置

日期：2026-11-14。**状态：已证明。** 本篇在 R495 的同一实际曲面和来源中，将比较从两条必要分支 jet 推进到**整个原相对 $\bar J$ 的首像**。高块准确是 $3C$ 上由真实 $\eta$ 确定的有限子概形，全部低行由原两/三相邻 charge 支付。其对偶使用 $K_X|_{3C}$，并保其余原列的消元。

在 $\ell\le r$，特别 $\ell=1$ 时，几何真行的局部条件化为
$A-2\eta B$ 正则。它给一个真正代数的 Padé 比值及原 ODE 转置，且准确显示当前截断始终低于首共振。没有将这一局部条件称为已证非零，也没有把 $\bar J$ 首像当原 $M$ 的二阶像。

## 1. 原实际立方、曲面与完整有限目标

保 R495 的所有条件：
$$
d^{C_D}\bar P=t^rF^3Q,\quad
\bar P\in\overline{\mathcal W}_D,\quad
F(0,1)=0,\quad F_Y(0,1)Q(0,1)\ne0,
$$
$$
h=\operatorname{ord}_wF(t(w),\bar g(w)),\quad
r+2h\ge s,\quad r+h\ge\ell,\quad
1\le r<s,\quad 1\le h<s.
\tag{1}
$$
$X$ 是同一十九次固定吹起面，$C$ 是 $F=0$ 的严格变换，$P=(0,1)$ 不动。
$\psi(t)$ 是这条正规分支；$\mathcal E=Y\partial_Y$。
原物理评价为
$$
Y_{\rm phys}=g(w)e_2(a\epsilon),\qquad
a=p\kappa\in\mathcal O^\times,\qquad
w^s=p\epsilon.
$$
因此整个相对目标的约化为
$$
\bar\Gamma=k[w,\epsilon]/(w^s,\epsilon^3,w^\ell\epsilon^2).
\tag{2}
$$
$t(w)=-w+\cdots$ 是原整参数的单位倍，将 (2) 换成 $t$ 变量不改变任一行长。所有 $g$ 均指原 Gaussian 已删的 regularized 轴，不另选形式参数。

## 2. 原整来源中的完整 3C 子格

R495 已给
$$
d^{-C_D}t^rQ\,H^0(X,\mathcal O_X(3C))
\subset\overline{\mathcal W}_D,\qquad
H^1(X,\mathcal O_X(mC))=0\quad(m\ge0).
\tag{3}
$$
还可保一个整来源表示。按 R491 引理逐系数保持所有有限角阶和系数次数提升 $F,Q$。这不只保持每条链的最后 Gauss 值，也保持 R495 (5) 的每个中间值，所以保持全部十九个重数。

在同一整吹起面上，$\mathcal O(3C)$ 的截面仍由逐 charge 的固定角整除及次数帽描述；其显示系数格有限自由，约化准确等于 (3) 的截面空间。乘
$d^{-C_D}t^r\widetilde Q$ 后仍在原 $\mathcal W_D$。
这个包含是 $p$ 饱和的来源包含：若乘积在原格被 $p$ 整除，模 $p$ 多项式域中
$t^rQ\ne0$ 迫截面本身约化为零；显示格的约化核是 $p$ 倍。这里不声称物理评价的像因此饱和。

限制到 $3C$ 的序列
$$
0\to\mathcal O_X\to\mathcal O_X(3C)
\to\mathcal O_{3C}(3C)\to0
$$
给
$$
\boxed{H^0(X,\mathcal O_X(3C))
\twoheadrightarrow H^0(3C,\mathcal O_{3C}(3C)),}
\tag{4}
$$
核为原 $F^3$ 的常数倍，并且
$H^1(3C,\mathcal O_{3C}(3C))=0$。不是只使用 $F^2$ 的限制。

## 3. 真实 normal 坐标与准确高块

令
$$
S=s-r>0,\qquad E=\max(\ell-r,0).
\tag{5}
$$
乘 $t^r$ 的目标像在 (2) 中准确有 $2S+E$ 条行，除去这个已知像因子后为
$$
\mathcal A_{S,E}
=k[[t]][\epsilon]/(t^S,\epsilon^3,t^E\epsilon^2).
\tag{6}
$$
$E=0$ 时 $\epsilon^2=0$；第三块整段消失在这个高块中，而非从原目标删掉。

在 $C$ 的完成邻域上用
$$
\zeta=\log(Y/\psi(t))\pmod{F^3}.
\tag{7}
$$
这里只用 $\log(1+x)=x-x^2/2\bmod x^3$，所以是实际的二次正规坐标，未调用正特征完整 log 级数。$F/\zeta$ 是单位。

定义同一原轴的截断
$$
\eta(t)=\log(g/\psi)\pmod{t^S}.
\tag{8}
$$
(1) 给 $2h\ge S$，因此 $(g/\psi-1)^2=0\bmod t^S$，(8) 也只需已付的低次 log。
它的阶为 $h$（若 $h\ge S$ 则在本目标为零），并有 $h\ge E$。
在 (6) 中准确有
$$
\boxed{\zeta\longmapsto\eta+a\epsilon.}
\tag{9}
$$
因为 $\eta^2\in(t^S)$、$\eta\in(t^E)$，
$(\eta+a\epsilon)^3=0$；所有被正规坐标截去的三次项在**同一**高块均零。
$d^{-C_D}Q(t,Y)$ 及 $t(w)^r/w^r$ 给完整目标单位，必须整项运输；其中的径向项并未删除。

因此原高块的有限子概形准确由
$$
\boxed{\mathscr I_\eta=(t^S,\ t^E(\zeta-\eta)^2)
\quad\text{于 }k[[t]][\zeta]/(\zeta^3)}
\tag{10}
$$
定义，在 $P$ 外为整个结构层。其商准确同构于 (6)，长度 $2S+E$。
证明可取逆 $\epsilon=a^{-1}(\zeta-\eta)$：
$\eta^2\in(t^S)$、$\eta\in(t^E)$ 使
$(\zeta-\eta)^3$ 已属于 (10)，不需另加一条缺失关系。
这是实际 $g$ 所决定的子概形，$\eta$ 不是自由 Padé 参数。

## 4. 原低行一条也不省

R495 已证真立方的最低角层至少有四条 charge，故
$r\le\mathsf B_{D-3}$，其中 $\mathsf B_n=A_n+e_{n+1}$。
对 $0\le j<r$，在 $j<\ell$ 时使用原三个相邻 charge，在 $j\ge\ell$ 时使用两个。
准确源列仍为
$Y^nq_nt^{j-A_n}$。
R412 的范围条件和上述界保证所有列都存在。

按原 (2) 评价，其首三向量为
$$
c_n(1,\ an,\ a^2n^2/2).
$$
三列的 Vandermonde 行列式为单位；两列亦然。依 $j$ 块三角消元，填入
$$
2r+\min(r,\ell)
\tag{11}
$$
个真实低行，产生的高尾完整保留。
(11) 与 (5) 的高块长度相加恰为 $2s+\ell$，即原整个 $\bar J$ 目标。

因此可先用这个实际低行右逆消元，再在余目标按
$t^r$、原 $Q/d^{C_D}$ 全单位和 (9) 规范化到 (10)。
这些操作均可追踪到原有限矩阵，不改变来源预算。

## 5. 整个首像的几何真左行

由 (4) 和 Gorenstein 对偶，显示高子格的余核对偶准确为
$$
\boxed{
\mathscr D_\eta=
H^0\!\left(3C,\operatorname{Hom}
(\mathscr I_\eta,\omega_{3C}\otimes\mathcal O_{3C}(-3C))\right)
=
H^0(3C,\operatorname{Hom}(\mathscr I_\eta,K_X|_{3C})).
}
\tag{12}
$$
最后一个等号是实际伴随公式。没有剩余的全局正则对偶商，因为
$H^1(3C,\mathcal O_{3C}(3C))=0$。

保第4节低行的全高尾，令 $\widehat{\bar J R}$ 表示其消元及第3节规范化。
则整个原相对 $\bar J$ 的真左行空间准确为
$$
\boxed{
\mathscr D_\eta^{\rm actual}
=\{\Phi\in\mathscr D_\eta:
\lambda_\Phi(\widehat{\bar J R})=0
\text{ 对所有原基列 }R\in\mathcal W_D\}.}
\tag{13}
$$
只须检查显示高子格及所选低列之外的列。
反向理由与 R489 一样完整：每条原左行先杀低列，故在高目标因子化；
又杀 (3)，故唯一来自 (12)。因此 (13) 是等号。
此时比较的是**整个原首像**，不再只是两个分支必要 jet。

## 6. 低 ell 的准确三层主部条件

在原线束平凡化中，将 (12) 的行写成
$$
\Phi=(A(t)+B(t)\zeta+C(t)\zeta^2)
\frac{dt\wedge d\zeta}{\zeta^3}.
\tag{14}
$$
这里省写与 $\mathcal O_{3C}(3C)$ 平凡化互为对偶的线束框；
配对时始终使用同一框。三个系数还须满足 (12) 的全部全局正则条件，不能独立任取。

由乘 $t^S$ 正则，三个系数极阶都不超过 $S$。
再乘 (10) 的另一生成元，利用 $\eta^2\in(t^S)$，正则条件准确化为
$$
\boxed{
A,B,C\in t^{-S}k[[t]],\qquad
A-2\eta B\in t^{-E}k[[t]].}
\tag{15}
$$
计算中还出现 $t^E\eta A$，但它由第二式自动正则：
$t^E\eta A=t^E\eta(A-2\eta B)+2t^E\eta^2B$。
因此没有漏掉另一条独立主部方程。

对 $G=q_0+\zeta q_1+\zeta^2q_2$，准确剩余配对为
$$
\lambda_\Phi(G)
=\operatorname{Res}_{t=0}(Aq_2+Bq_1+Cq_0)\,dt.
\tag{16}
$$
当 $\ell\le r$，特别 $\ell=1$ 时，$E=0$，所以
$$
\boxed{A-2\eta B\text{ 正则}.}
\tag{17}
$$
若 $B$ 的实际极阶为 $q>h$，则 $A$ 的极阶准确为 $q-h$，
最高极系数等于 $2\eta_h$ 乘 $B$ 的最高极系数。
这不等同于 R489 的两层极系数关系：这里还有第三层 $C$、不同的行长、
原全局 $K_X$ 条件和 (13) 的实际列测试。

## 7. 原 ODE 的真实 Padé 转置及首共振边界

三个系数可在泛点用原 $t,Y$ 与 $\zeta$ 作正规展开，因此属于同一 $k(C)$ 中的有理系数；
因为 $b<p$ 且 $F_Y\ne0$，这由泛点处对 $k(t)$ 的可分 Hensel 展开给出。
有限二次正规展开不引入新的自由函数。

若 (17) 中 $B$ 有正极阶 $q$，定义
$$
R_\Phi=\frac{A}{2B}\in k(C).
$$
则在同一个 $P$ 上准确有
$$
\boxed{R_\Phi-\eta=O(t^q).}
\tag{18}
$$
只有通过 (12)、(13) 的行才给这个真实有理近似。

R467 已保原 theta 的方程。为免与行系数混同，记
$$
\mathsf A=6t(1-t)d^2,\qquad
\mathsf B=(5-8t)d^2,\qquad
\mathsf C=(154+160t+1792t^2)/3,
$$
$$
\mathscr L=\mathsf A\partial_t^2+\mathsf B\partial_t.
$$
原 regularized 低轴满足
$\mathscr L\log g=\mathsf C\bmod t^{s-1}$。
因此 (8) 给
$$
\boxed{
\mathscr L\eta
=\mathcal R_F\pmod{t^{S-1}},\qquad
\mathcal R_F=
\mathsf C-\mathsf A\,\partial_t(\psi'/\psi)
-\mathsf B\,\psi'/\psi\in k(C).}
\tag{19}
$$
这里 $\psi'/\psi=-F_t/(YF_Y)$ 于 $C$ 上，故右端完全是同一实际代数曲线的有理 forcing。
$\log$ 在 (19) 只指上述截断的导数身份，不声称有正特征完整 log 函数。

从 (18) 得真正的转置必要式
$$
\boxed{\mathscr L R_\Phi-\mathcal R_F=O(t^{q-1}).}
\tag{20}
$$
若原接触首项为 $\eta_h\ne0$，则
$$
[t^{h-1}]\mathcal R_F=h(6h-1)\eta_h\ne0.
\tag{21}
$$
因为 $1\le h<s$、$p=6s-1$，此系数确为单位。
但 (20) 并不把 $\mathcal R_F$ 置零：它允许同一有理 $R_\Phi$ 支付该首项。

尤须保其准确长度：
$$
q\le S=s-r\le s-1,\qquad q-1\le s-r-1\le s-2.
\tag{22}
$$
R467 原整数递推的首共振位于 $t^{s-1}$。**当前真行条件没有到达这一位。**
因此不能把 (20) 说成一个跨越首共振的全方程，继而用单位共振立即排除该行。
这里明确定位了低 $\ell$ 转置仍未支付的边界；补它必须使用真实下一精度及 carry，而非延长形式等号。

## 8. 三高轴的作用保在原主部内

本节只描述 (15) 的实际变化，未增加中央条件。
若原高轴将 $g$ 改为 $g\exp(H)$，$\operatorname{ord}_tH\ge s-3$，
则本高块 $\eta$ 改为 $\eta+H\bmod t^S$。
所以 $r\ge3$ 时它在本高块完全不变；
$r=2$ 时仅 $s-3$ 一项能进入；
$r=1$ 时仅 $s-3,s-2$ 两项能进入。

在 $E=0$ 的 (17) 中，变化只通过 $2HB$：
$r=1$ 时最多影响 $A$ 的 $t^{-2},t^{-1}$ 主部，
$r=2$ 时最多影响 $t^{-1}$ 主部。
真正行仍须满足全局 (12) 和原列测试 (13)；
小秩主部变化并不保证最高极空间、真左核维数或 Schur 标量不变。
第三完整中央的全部真实参数照 R468 保留，不能把它们换成任意可调数。

## 9. 原 M 与下一精度

本篇 (12)–(22) 已是整个相对 $\bar J$ 首像的准确描述。
它尚未识别可提升到模 $p^2$ 的全部左行，也未计算原 $d_2^J$ 在这些行上的值。

恢复原物理矩阵时继续使用
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
$$
$P_{134}/U_0$、十三自由行、两条十三行 carry 及 R481 的同一修正第三精度公式均保留。
第3节对 $t^rQ$ 的单位运输和取像除法只在指定的 $\bar J$ 高块进行，
不能直接提升成模 $p^2$ 的目标单位并抹掉跨块进位。

R491 的因子化实际基准只消掉分支双 jet 的来源偏移；
原 $J(P^{\rm fact})/p$、$\xi$ 以及 (22) 缺少的共振边界都还在。
下一步必须把这个真实几何行提升与 R481 的同一首次修正及原 carry 相接。
完整中央跨 $p$ 非零仍未得到。

