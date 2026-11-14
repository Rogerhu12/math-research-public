# 真实邻点上的 Hermite 中央行：首个导数、整格成本与完整深度

日期：2026-11-12。状态：首层中央系数的精确 Hermite 留数公式、
所需一阶导数的必要性、整 jet 格指数、有限精度重构及完整深度的
$M_e$ 输入替换均已证明。没有证明该中央行在无穷多个 $p$ 上非零。

## 1. 固定对象、真实邻点与中央系数

仍取惰性 $p\ge7$，$d=p+1$，以及
[真实 canonical 邻点](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
的有限未分歧域 $B$、$L_p=B(\varpi)$、$\varpi^d=p$。
取任一实际商参数 $r$，则 $B(r)=L_p$；
它的 monic 最小多项式记为

$$
\mathscr P_p(t)=t^d+pA_p(t),\qquad
A_p\in\mathcal O_B[t],\quad\deg A_p<d,\quad A_p(0)\in\mathcal O_B^\times.
\tag{1.1}
$$

它的全部根正是 $K$ 的最近 $p+1$ 个零点。
本文中的 $\mathscr P_p$ 是这个真实邻点多项式，
不是任意选的 Eisenstein 多项式。

令

$$
m(t)=M_e(t)/t^4\in\mathcal O_B[[t]],\quad m(0)=1,\qquad
q=d-4=p-3,
$$

并取明确的有限周期核

$$
R_p(t)=\left[\frac{K(t)^d}{s(t)J(t)^{d+1}}\right]_{\le q}
\in\mathbb Z_p[t],\qquad R_p(0)=1.
\tag{1.2}
$$

其整性由 $K,J$ 在次数 $\le q<p$ 的整性直接得到。
准确有

$$
C_d=[t^q]\bigl(R_pm\bigr),\qquad
\Gamma_{i,p}=C_d/p\in\mathbb Z_p.
\tag{1.3}
$$

最后的整性是本题已证明的 $C_{p+1}\in p\mathbb Z_p$，
未假设 $\Gamma_{i,p}$ 非零。

## 2. 整形式级数的 $\mathscr P_p^e$ 除法及低 jet 精度

对任意 $e,N\ge1$ 及 $f\in\mathcal O_B[[t]]$，存在唯一表示

$$
f=\mathscr P_p^eQ+f_e,\qquad
Q\in\mathcal O_B[[t]],\quad
f_e\in\mathcal O_B[t],\quad\deg f_e<ed.
\tag{2.1}
$$

这是本处的整 Weierstrass 除法。可直接逐 $p$ 构造：
模 $p$ 时 $\mathscr P_p^e=t^{ed}$，所以把低于 $ed$ 的系数放入
$f_e$，其余移入 $Q$，给出唯一解。
减去该提升后除以 $p$，重复同一步；
完备性给 (2.1)，逐层唯一性也给其唯一性。

有限精度还有明确的截断式：

$$
t^{d(e+N-1)}\in(\mathscr P_p^e,p^N).
\tag{2.2}
$$

因为 $t^d=\mathscr P_p-pA_p$，
展开 $(\mathscr P_p-pA_p)^{e+N-1}$：
含 $\mathscr P_p^j$ 且 $j\ge e$ 的项属于第一理想，
其余项的 $p$ 次数至少 $N$。
因此模 $(\mathscr P_p^e,p^N)$ 的余式完全由
$f$ 的前 $d(e+N-1)$ 个系数决定，不涉及无限形式除法的不受控尾项。

反过来，若只关心次数 $\le D'$ 的低 jet，
则任何 $\mathscr P_p^eQ$ 的这些系数均属于

$$
p^{\,e-\lfloor D'/d\rfloor}\mathcal O_B
\quad\text{当 }e\ge\lfloor D'/d\rfloor.
\tag{2.3}
$$

证明是展开
$\mathscr P_p^e=\sum_j\binom ej t^{dj}p^{e-j}A_p^{e-j}$。
能贡献次数 $\le D'$ 的项必须 $j\le\lfloor D'/d\rfloor$；
再乘整的 $Q$ 不改变这个结论。

特别，$f\bmod(\mathscr P_p^e,p^N)$ 在

$$
e\ge N+\lfloor D'/d\rfloor
\tag{2.4}
$$

时决定 $f\bmod(p^N,t^{D'+1})$。
本篇稍后明确使用这个界，不把在邻点求值当成免费的原点 jet 识别。

## 3. 首层恰由 first Hermite 数据给出

因为 $q<d$，
$\mathscr P_p^2$ 的次数 $\le q$ 的系数全部被 $p^2$ 整除。
对 $m$ 作 (2.1) 的 $e=2$ 除法，

$$
m=m_2+\mathscr P_p^2Q,\qquad\deg m_2<2d,
$$

得到

$$
C_d\equiv[t^q](R_pm_2)\pmod{p^2}.
\tag{3.1}
$$

这里先取 $m=M_e/t^4$ 很重要。
若直接对 $M_e$ 忽略四阶零点，$\mathscr P_p^2$ 的第 $t^d$ 项
可以只被一个 $p$ 整除，不能得到 (3.1)。

$\mathscr P_p$ 的所有根都简单，且 (2.1) 在 $|t|<1$ 收敛，
所以

$$
m_2(r_H)=m(r_H),\qquad
m_2'(r_H)=m'(r_H)
\tag{3.2}
$$

对每一个真实邻点成立。
因此 $m_2$ 正是这些值与一阶导数的唯一 Hermite 插值多项式。
这些是同一固定实际 $m$ 的数据，没有更换成另一个模形式。

令 $(\cdot)_+$ 表示 Laurent 多项式的非负次幂部分，定义

$$
\boxed{\quad
W_p(t)=\left(\frac{\mathscr P_p(t)^2R_p(t)}{t^{q+1}}\right)_+
\in\mathcal O_B[t],\qquad \deg W_p<2d.
\quad}
\tag{3.3}
$$

则首层中央值的准确邻点公式为

$$
\boxed{\quad
C_d\equiv
\operatorname{Tr}_{L_p/B}
\left(
 \frac{(W_pm)'(r)}{\mathscr P_p'(r)^2}
-\frac{W_p(r)m(r)\mathscr P_p''(r)}
       {\mathscr P_p'(r)^3}
\right)\pmod{p^2}.
\quad}
\tag{3.4}
$$

所以把 (3.4) 的完整迹除以 $p$ 再模 $p$，
准确得到 $\Gamma_{i,p}$。
特别非零仍是已证的惰性初级有限充分条件。

**完整证明。**
在无穷远，

$$
\frac{W_p}{\mathscr P_p^2}
-\frac{R_p}{t^{q+1}}=O(t^{-2d-1}).
$$

乘以 $\deg m_2<2d$ 的多项式后，不改变 $t^{-1}$ 系数。
因此

$$
[t^q](R_pm_2)
=\sum_H\operatorname{Res}_{t=r_H}
 \frac{W_p(t)m_2(t)}{\mathscr P_p(t)^2}\,dt.
\tag{3.5}
$$

在简单根 $r_H$ 展开分母，每个二阶极点的留数为

$$
\frac{(W_pm_2)'(r_H)}{\mathscr P_p'(r_H)^2}
-\frac{W_p(r_H)m_2(r_H)\mathscr P_p''(r_H)}
       {\mathscr P_p'(r_H)^3}.
$$

由 (3.2) 替换成实际 $m,m'$，再用同一 Galois 轨道求迹，
最后用 (3.1)，即得 (3.4)。
完整迹为整，且模 $p$ 为零来自 (1.3)；
没有分别宣称带 $\mathscr P_p'$ 分母的每一项整。

还有一个方便的有限权表示：

$$
W_p\equiv t^3R_p(t)\bigl(t^d+2pA_p(t)\bigr)\pmod{p^2}.
\tag{3.6}
$$

这是把 (1.1) 平方后代入 (3.3)。
(3.6) 若用于 (3.4)，必须对整个 Hermite 留数泛函一起使用：
其整性来自 (3.5) 的整多项式余式，
不能逐个忽略分母后宣称单项误差仍在 $p^2$。

## 4. 仅邻点值不够：一个准确的必要性证明

这一步不是猜测 trace 权不合适，而是给出评价映射的真实核。
对固定当前 $p$，令

$$
\Delta M(t)=t^d\mathscr P_p(t),\qquad
\Delta m=t^q\mathscr P_p(t).
\tag{4.1}
$$

$\Delta M$ 在每个实际邻点都为零，
是整函数，阶数为 $d\ge8$，所以不改原来的 $t^4$ 首项。
但由 (1.3)，

$$
\Delta C_d=\mathscr P_p(0),\qquad
\boxed{\ \Delta\Gamma_{i,p}=\mathscr P_p(0)/p
                    \in\mathcal O_B^\times.\ }
\tag{4.2}
$$

因此，无论怎样选择只乘 $M_e(r_H)$ 的 trace-dual 权，
仅靠这些点值都不能在这一整函数空间上提取中央 $\Gamma_{i,p}$。
这同样保留了 $C_d\in p\mathcal O_B$ 的已知整性。
第一导数恰看见丢失的信息：

$$
\Delta m'(r_H)=r_H^q\mathscr P_p'(r_H)\ne0.
$$

(4.1) 不是本题原模形式，也没有声称保持其实际 Hecke 关系；
它证明的是在上述普遍整性与分支几何假设下，
一阶 Hermite 数据确有必要，$e=1$ 不能代替 §3 的 $e=2$。

## 5. Hermite 的真实整格及准确指数

用 Hasse 导数
$f^{[j]}=f^{(j)}/j!$；对整级数，它仍是整级数。
考虑实际整映射

$$
\mathcal J_e:\quad
\mathcal O_B[t]/(\mathscr P_p^e)
\longrightarrow \mathcal O_{L_p}^{\,e},
\qquad
f\longmapsto
\bigl(f(r),f^{[1]}(r),\ldots,f^{[e-1]}(r)\bigr).
\tag{5.1}
$$

反转 $p$ 后它是同构，但一般不是整同构。
其 image 的准确 $\mathcal O_B$ 长度指数是

$$
\boxed{\quad
\operatorname{length}_{\mathcal O_B}
 \operatorname{coker}\mathcal J_e
=\binom e2(d-1).
\quad}
\tag{5.2}
$$

证明采用整基
$\{\mathscr P_p^kt^a:0\le k<e,\ 0\le a<d\}$。
它与通常单项式基的变换为 monic 的整三角变换，行列式一。
在 $j$ 阶 jet 中，$k>j$ 时为零；在 $j=k$ 的对角块，
映射是 $x\mapsto\mathscr P_p'(r)^k x$。
因此 determinant ideal 是

$$
\prod_{k=0}^{e-1}
 \operatorname{Norm}_{L_p/B}(\mathscr P_p'(r))^k.
$$

$L_p/B$ 是 tame、完全分歧、次数 $d$ 的扩张，
其不同理想为 $\varpi^{d-1}\mathcal O_{L_p}$。
这里也可从 $\varpi^d-p$ 的导数直接核算；
改变到另一均一化元 $r$ 不改变不同理想。
故 $v_p\operatorname{Norm}\mathscr P_p'(r)=d-1$，
得到 (5.2)。

特别首层 $e=2$ 的指数长度就是 $p$。
所以 §3 不是把两个任意整值/导数向量都免费放入原整格；
实际数据来自固定 $m$，自动满足这个非平凡的兼容条件。

对 $e=2$，兼容性还可以完全写出。
把 $a=m(r)$ 表示成唯一的次数 $<d$ 整多项式 $a_0(r)$。
则

$$
b(r)=\frac{m'(r)-a_0'(r)}{\mathscr P_p'(r)}
\in\mathcal O_{L_p}.
\tag{5.3}
$$

若 $b_0$ 是 $b(r)$ 的次数 $<d$ 整表示，则

$$
m_2(t)=a_0(t)+\mathscr P_p(t)b_0(t).
\tag{5.4}
$$

(5.3) 是真实的一次除不同理想，不是预先假设
$m'(r)$ 能独立指定。它也给一种可直接计算 (3.1) 的版本。

例如，把 $m(r),m'(r)$ 和 $\mathscr P_p$ 计算到模 $p^3$，
足以恢复 $m_2\bmod p^2$，再得到 $\Gamma_{i,p}\bmod p$：
这里的数据须在同一个已经固定的
$\mathcal O_{L_p}=\mathcal O_B[r]$ 整基或相容有限环中给出；
仅知道 $\mathscr P_p\bmod p^3$ 不意味着已经获得根 $r$ 的同精度表示。
因 $v_p(\mathscr P_p'(r))=(d-1)/d<1$，
其逆乘法把整格至多移入 $p^{-1}\mathcal O_{L_p}$。
源点值的整多项式表示与各阶 Hasse 导数均不额外损失整性。

一般 $e$ 也有明确的安全精度界。
按上述块三角式逐步解，
第 $k$ 步的逆对角块至多除 $p^k$，
所以模 $p^{N+\binom e2}$ 的实际 jet 数据足以恢复
$\mathcal O_B[t]/\mathscr P_p^e$ 中模 $p^N$ 的余式。
这只是一个可直接证明的上界，不声称最优；
也没有用其 determinant 长度代替每一所选行的范数。

## 6. 完整惰性深度的 $M_e$ 输入可用同一真实邻点的高 jets 替换

在 [R81 的短输入证书](2026-11-12-weighted-two-step-frobenius-and-kummer-iteration.md)
中，对 $n\ge0$ 定义

$$
m_n=(p+1)p^n,\qquad Q_n=4n+4,\qquad N_n=Q_n-1,
$$

$$
D_n=\min\bigl(m_n,\ 2(p+1)N_n+4\bigr),\qquad D'_n=D_n-4.
\tag{6.1}
$$

该证书计算

$$
p^{p^n}C_{m_n}\bmod p^{Q_n},
$$

所需的实际 $M_e$ 输入是次数 $\le D_n$、精度 $p^{N_n}$。
置

$$
e_n=N_n+\left\lfloor\frac{D'_n}{p+1}\right\rfloor
\le3N_n.
\tag{6.2}
$$

由 §2，$m=M_e/t^4$ 的整余类

$$
m\bmod(\mathscr P_p^{e_n},p^{N_n})
\tag{6.3}
$$

决定 R81 所需的全部 $M_e$ 输入。
而反转 $p$ 后，这一余类由实际邻点的 Hasse jets

$$
m^{[j]}(r_H),\qquad 0\le j<e_n
\tag{6.4}
$$

唯一决定；其整格与足够重构精度由 §5 明确给出。
因此可把完整中央深度的这部分输入，
准确放在同一真实 level-one quasi-canonical 轨道的非约化增厚上，
所需 jet 阶只随检测深度线性增长。

这里没有改变 R81 的另外两个输入/运算：
实际二次 GM Frobenius 矩阵
$G_p=-pY(t^{p^2})Y(t)^{-1}$ 仍需它规定的 jet 与 $p^{Q_n}$ 精度；
最终高权系数提取也仍按原公式执行。
没有声称这些周期输入或指数大的目标权
自动下降成 (6.3) 的同一个有限代数。

## 7. 这一接口已经做到什么，尚未做到什么

首层 (3.4) 是实际中央 $\Gamma_{i,p}$ 的准确
CM 邻点值与第一导数公式；其非零充分得到本题惰性初级有限性。
完整深度则由 (6.3)–(6.4) 保留此前完备检测所需的实际模函数输入。
值、导数、不同理想以及额外的中央除 $p$ 均已逐一保留。

$M_e$ 是固定代数模函数，所以其这些 derivatives 可以在同一个
固定 prime-to-$p$ level 覆盖上计算；并非新选的任意解析原函数。
但邻点本身、$\mathscr P_p$、核 $R_p$ 和 Hermite 权均随 $p$ 变化。
真实 Hecke trace 还使用运输后的 level 与奇偶角色；
不能把 (3.4) 直接认作未经核对的无权 Hecke 特征值。

尚需利用实际 Hecke/同源关系，对 (3.4) 或其完整深度形式
证明跨素数的非零。§4 说明这个比较必须包含 infinitesimal 信息；
只保留 reduced CM 邻点值确实丢失了中央方向。
