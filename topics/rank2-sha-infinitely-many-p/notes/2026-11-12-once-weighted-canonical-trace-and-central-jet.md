# 一次微分权的实际 canonical 域迹、对偶格与中央 jet 比较

日期：2026-11-12。状态：真实域迹的整格、留数/trace-duality 公式、
任意有限精度输入界及两个小素数的完整算术证书均已证明。
这些式子尚未把该域迹的非零等同于中央 $J'_p(0)$ 的非零。

## 1. 真实对象及所求的带权迹

固定惰性 $p\ge7$，令 $d=p+1$、$D=pd$。
取足够大的有限未分歧域 $B$，并令
$L_p=B(\varpi)$、$\varpi^d=p$。
[真实邻点定理](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
证明，canonical 源曲线的全部 $p+1$ 个 $p$-同源商参数 $r_H$
恰是 $K$ 在半径 $\rho=p^{-1/d}$ 上的零点，
且每个 $B(r_H)=L_p$。

保留原实际函数

$$
I(t)=H_i(u(t)),\qquad
I'=\frac{M_eK}{sL^2},\qquad I(0)=0,\qquad
L=tJ,\quad s=1-4t^2.
\tag{1.1}
$$

这里 $L$ 是固定奇周期；$L_p$ 才是数域。
真实商微分为 $q_H^*\omega_H=\beta_pL(r_H)\omega_0$，
所以 root 所指定的一次微分权迹为

$$
\mathscr T_p
=\operatorname{Tr}_{L_p/B}
 \left(\frac{I(r_H)}{\beta_pL(r_H)}\right)
=\beta_p^{-1}S_p,\qquad
S_p=\operatorname{Tr}_{L_p/B}\left(\frac{I(r_H)}{L(r_H)}\right).
\tag{1.2}
$$

$\beta_p\in\mathbb Z_p^\times$ 为同一实际晶体常数。
以下先计算完全不含此周期单位的 $S_p$。

## 2. 完整 trace 格与留数公式

[三次权迹的完整 Gauss 证明](2026-11-12-actual-weighted-primitive-trace-unit.md)
给出

$$
\overline{\varpi^{-3}I(\varpi X)}
=\frac{X^3}{3}+\frac{\kappa_pX^{d+3}}4,\qquad
\overline{L(\varpi X)/\varpi}=X.
\tag{2.1}
$$

在 $K$ 零点 $\bar X^d=-\kappa_p^{-1}$ 上，

$$
\frac{I(r_H)}{L(r_H)}
\in\varpi^2\mathcal O_{L_p},\qquad
\overline{\varpi^{-2}I(r_H)/L(r_H)}
=\bar X_H^2/12.
\tag{2.2}
$$

但 (2.2) 的最低项 trace 为零，不能据它猜测 $S_p/p$。

本处可以把全部格准确写出。因为 $d$ 为 $p$ 单位，

$$
\operatorname{Tr}_{L_p/B}(\varpi^j\mathcal O_{L_p})
=p^{\lceil j/d\rceil}\mathcal O_B
\qquad(j\in\mathbb Z).
\tag{2.3}
$$

证明是写 $x=\sum_{a=0}^{d-1}x_a\varpi^a$：
其迹为 $d x_0$，而 $x\in\varpi^j\mathcal O_{L_p}$
正好要求 $v_p(x_a)\ge\lceil(j-a)/d\rceil$。
于是 (2.2) 严格给

$$
\boxed{S_p\in p\mathcal O_B,\qquad
\mathscr T_p\in p\mathcal O_B.}
\tag{2.4}
$$

令 $P_p(T)$ 为 $r_H$ 的 monic 最小多项式。
它是次数 $d$ 的 Eisenstein 多项式，
$\mathcal O_{L_p}=\mathcal O_B[r_H]$，
对偶格为 $P_p'(r_H)^{-1}\mathcal O_{L_p}$。
对任意在这些点收敛的 $F$，记
$\operatorname{rem}_{P_p}F$ 为 $F(r_H)$ 的次数 $<d$ 的唯一多项式表示。
则

$$
\boxed{\quad
\operatorname{Tr}_{L_p/B}F(r_H)
=[T^{d-1}]\operatorname{rem}_{P_p}\bigl(P_p'(T)F(T)\bigr).
\quad}
\tag{2.5}
$$

这由 Lagrange interpolation 直接证明：
对次数 $<d$ 的 $Q$，
$[T^{d-1}]Q=\sum_HQ(r_H)/P_p'(r_H)$；
取 $Q=\operatorname{rem}_{P_p}(P_p'F)$ 即得。

相同的量还有准确的 period-map 留数表达式：

$$
S_p=\sum_{K(r_H)=0}\operatorname{Res}_{t=r_H}
 \frac{I}{L}\frac{K'}K\,dt
=-\sum_{K(r_H)=0}\operatorname{Res}_{t=r_H}
 \frac{I\,s(K')^2}{K}\,dt.
\tag{2.6}
$$

第一式是简单零点的定义。第二式使用
$KL'-LK'=1/s$，特别 $K'(r_H)=-1/(s(r_H)L(r_H))$。
更强地，两被积式之差为
$I\,sK'L'/L\,dt$，在整条闭圆盘上解析，包括 $t=0$，
故没有隐藏额外的原点留数。

(2.5)–(2.6) 保留了实际邻点全部高阶项；
它们的极点除子是 $K=0$。
中央系数

$$
\Gamma_{i,p}=\frac{C_d}{p}
=\frac1p\operatorname{Res}_{t=0}
 \frac{M_eK^d}{sL^{d+1}}\,dt
\tag{2.7}
$$

则是 $L=0$ 处的另一个留数。
两种留数并未因同在一个圆盘内而自动相同。

## 3. 任意有限精度的短输入界

设 $F_q=I/L^q$，这里只取 $q=1$ 或 $3$。
前述完整 Gauss 笔记证明

$$
v_p([t^j]J^{-q})\ge-\lfloor j/D\rfloor,
\tag{3.1}
$$

以及对 $m\ge d+3$，

$$
v_p(I_m)\ge
-1-\left\lfloor\frac{m-d-3}{D}\right\rfloor-v_p(m).
\tag{3.2}
$$

小指标 $m<d+3$ 的 $I_m$ 全整：
唯一风险 $m=p$ 已用实际 $C_d\in p\mathbb Z_p$ 消去，
不是假设 $\Gamma_{i,p}$ 非零。

对卷积 $m+j=n+q$，(3.1)–(3.2) 因而给
$n\ge d+3-q$ 时的准确公共界

$$
v_p([t^n]F_q)\ge
-1-\left\lfloor\frac{n+q-d-3}{D}\right\rfloor
-\lfloor\log_p(n+q)\rfloor.
\tag{3.3}
$$

小 $m$ 的项也满足此界：因 $d<D$，
对应的 $\lfloor j/D\rfloor$ 至多多出一。
特别当 $n\ge8d$、$q\le3$ 时，

$$
\lfloor\log_p(n+q)\rfloor\le\frac n{4d}.
\tag{3.4}
$$

若左边不超过二，(3.4) 来自 $n\ge8d$；
若为 $\ell\ge3$，则
$n\ge p^\ell-3\ge4d\ell$。
最后一个不等式在 $p=7,\ell=3$ 已严格成立，
随后对 $p$ 及 $\ell$ 递增保持成立。

于是缩放系数满足

$$
v_p([t^n]F_q)+\frac nd
\ge\frac nd\left(\frac34-\frac1p\right)-1
\qquad(n\ge8d).
\tag{3.5}
$$

给定精度 $p^N$，取

$$
B_N=2d\max(N+1,4).
\tag{3.6}
$$

则全部次数 $n\ge B_N$ 的缩放系数估值严格大于 $N$。
这对 $N\le3$ 由
$8(3/4-1/7)-1=27/7>3$ 得到；
对 $N\ge3$，下界至少
$(17N+3)/14>N$。

因此 $F_q(r_H)\bmod p^N$、
以及其真实域迹模 $p^N$，只需次数 $<B_N$ 的系数。
构造这些系数时，$M_e,K,J$ 读到 $B_N+6$ 已足够。
这是准确 $O(p(N+1))$ 阶的有限输入，而不是把无限高项随意删去。

对 $K(\varpi X)$ 同样有更强尾界：
由 $K$ 的层数计数，
$v_p(k_n)\ge-1-\lfloor(n-d)/D\rfloor$；
在 $n\ge B_N$ 加上 $n/d$ 后也严格大于 $N$。
所以截断 $K$ 后，在
$\mathcal O_B[\varpi]/(p^N)$ 中作 Hensel–Newton
得到的根准确到此精度。
(2.1) 保证缩放导数为单位。
所有 $F_q(\varpi X)$ 的缩放系数整，
故替换近似根不会损失额外精度。

## 4. 完整实际计算与一个中央不变的高 jet 扰动

可执行证书为
[check-canonical-neighbor-primitive-traces.py](../scripts/check-canonical-neighbor-primitive-traces.py)。
它从固定整数 Hurwitz 流生成 $C_m$，
由 $\mathcal B_1(u)=KM_e$ 得实际 $M_e$，
然后在有限环

$$
(\mathbb Z/p^N\mathbb Z)[\varpi]/(\varpi^{p+1}-p)
$$

内求解 $K(\varpi X)=0$。
准确域迹就是 $d$ 倍 $\varpi^0$ 坐标。
选择一个剩余根可在 $\mathbb F_p$ 中完成：
由强整除矩阵
$F_{11}=s(\beta_pt^pL'-p\alpha_pK')+\cdots$
的 $t^p$ 系数模 $p$ 可得
$\kappa_p=\beta_p/\alpha_p$；
再用 $\alpha_p\beta_p=-1$，
得到 $-\kappa_p^{-1}=\beta_p^{-2}$ 是平方。
其余根不必逐个重算；数域 trace 已完整包含全部 $p+1$ 个共轭。

在 $N=3$，脚本准确给

| $p$ | $C_{p+1}/p\bmod p$ | $S_p\bmod p^3$ | $S_p/p\bmod p$ |
|---:|---:|---:|---:|
| 7 | 2 | 84 | 5 |
| 11 | 9 | 429 | 6 |

它还核定 $p=7$ 的
$\operatorname{Tr}(I/L^3)=325\bmod343$，即模七为 $3=1/12$；
$p=11$ 的同一三次权迹为 $771\bmod1331$。
这些是实际函数的算术值，不输入 CLS 表或新的 $L$ 值表。

为准确检验“这个一次权迹是否仅由中央 jet 决定”，
在固定该 $p$ 的比较中令

$$
\Delta M=t^{p+3},\qquad
\Delta I'=\frac{\Delta M\,K}{sL^2},\quad\Delta I(0)=0.
\tag{4.1}
$$

它没有改变 $M_e$ 的首项 $t^4$，
且由 (2.7) 立刻有 $\Delta C_{p+1}=0$。
因此 $M_e+\Delta M$ 的中央 $\Gamma_{i,p}$ 与原实际对象相同。
但上述完整有限环计算给

$$
\begin{array}{c|cc}
p&\operatorname{Tr}(\Delta I/L)\bmod p^3&
 \operatorname{Tr}(\Delta I/L)/p\bmod p\\ \hline
7&168&3\\
11&1012&4
\end{array}
\tag{4.2}
$$

全尾界对这个扰动同样适用：
$\Delta M/t^4$ 整，且 $\Delta I_p=0$，
所以没有撤掉 §3 所需的中央整性。
故 (4.2) 是严格的不同函数行比较，不是截断实验。

结论是：仅用周期方程、邻点几何、实际首项、
$p$-整性及 $C_{p+1}\in p\mathbb Z_p$，
不能把 $S_p/p$ 识别成 $\Gamma_{i,p}$ 的一个固定单位倍数，
也不能说它只读取中央 jet。
这个扰动并非本题实际模形式，
没有声称它保持实际 Hecke 特征或构成主问题的反例。

## 5. 保留的正面接口及准确缺口

一次权迹已经成为 (2.5) 的真实 tame field-trace 行，
有任意精度的完整输入界和无需周期单位的有限算法。
三次权迹则由完整 Gauss 证明处处为单位。
两者都在同一个实际邻点轨道上，不是任意换了一条曲线。

下一步若要把一次权迹用于主目标，必须利用本题的额外
Hecke/level 角色，证明它消去 (4.1) 所展示的高 jet 方向，
或构造一个准确的修正权，使所得迹控制完整 $J'_p(0)$。
目前未证明这种比较。
反过来，(4.2) 只排除“无需实际 Hecke 输入就自动相等”的捷径，
不排除对固定原 $M_e$ 建立更精细的正面关系。
