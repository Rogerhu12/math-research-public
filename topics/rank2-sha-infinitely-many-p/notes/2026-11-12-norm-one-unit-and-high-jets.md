# 固定 norm-one 单位、分母的普通迹与实际高 jet

**可信度：本文恒等式与非挠性已证明；目标矩的额外比较尚未完成。** 日期：2026-11-12。本文继续 R31，准确计算固定 $w$ 的范数，去掉其普通迹中的有理分量，并说明原目标矩需要哪一种高 jet，而不能仅由 $D_p(\alpha)$ 的值直接代替。

## 1. 两个 2-torsion 值的精确常数

记
$$
E:y^2=x^3-17x,\quad \Delta=64\cdot17^3,\quad
\mathfrak a=(67),\quad A=\mathrm N\mathfrak a=4489,
$$
并沿用 R31 的 $P_f,T,Q_\pm,F,M,\alpha,D_p$。在 $Q_\pm$，
$$
x=\pm\sqrt{17},\qquad y=0,\qquad
(3x^2-17)=34.
$$

对任意非零 $2$-torsion 点 $Q=(e,0)$，令
$d=3e^2-17$。标准奇数 division polynomial 满足
$$
\boxed{\quad
\psi_n(Q)=(-1)^{(n-1)/2}
d^{(n^2-1)/4}\qquad(n\ge1\text{ 为奇数}).
\quad}
\tag{1}
$$
以下给出所需的完整归纳。$\psi_1(Q)=1$，而直接由
$\psi_3=3x^4-102x^2-289$ 得到 $\psi_3(Q)=-d^2$。
所有偶数 division polynomial 在 $Q$ 为零。使用标准递推
$$
\psi_{2m+1}
=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3,
$$
当 $m$ 为奇数时只剩第一项，当 $m$ 为偶数时只剩负的第二项。
第一种情形的指数为
$$
\frac{(m+2)^2-1+3(m^2-1)}4=m^2+m,
$$
符号为负；第二种情形的指数为
$$
\frac{(m-1)^2-1+3((m+1)^2-1)}4=m^2+m,
$$
计入外面的负号后符号为正。这分别与
$(-1)^m d^{((2m+1)^2-1)/4}$ 相同。除去已处理的 $n=1,3$ 基例，递推只涉及更小的奇数，故 (1) 成立。

R31 的 $\Theta_{\mathfrak a}$ 等于
$\Delta^{A-1}/\psi_{67}^{12}$；选 Hecke 生成元 $-67$ 与标准 $\psi_{67}$ 的符号差在十二次幂后消失。因此 (1) 给出
$$
\Theta_{\mathfrak a}(Q_\pm)
=\left(\frac{64\cdot17^3}{34^3}\right)^{A-1}
=2^{3(A-1)}=2^{13464}.
\tag{2}
$$
所以
$$
F_{\mathfrak a}(Q_+)
=\Theta_{\mathfrak a}(Q_+)\Theta_{\mathfrak a}(Q_-)
=2^{6(A-1)}=2^{26928}.
\tag{3}
$$

## 2. 一个固定的全局 norm-one 单位

定义
$$
u=F_{\mathfrak a}(P_f)
=\Theta_{\mathfrak a}(P_f)\Theta_{\mathfrak a}(P_f+T).
\tag{4}
$$
由 R31 的 $\tau$-不变性，$u\in M$。它其实是 $M$ 的全局单位。

准确的外部输入是 Rubin Theorem 7.4 的椭圆单位性：当非零 torsion 点的精确导子不是素理想幂，且与辅助理想互素时，相应 $\Theta$ 值为全局单位。这里 $P_f$ 为 primitive $\mathfrak f$-torsion；$\mathfrak f=(34(1+i))$ 同时含 $(1+i)$ 与 $17$ 上方的素理想。又
$$
P_f+T=[35]P_f,\qquad (35,\mathfrak f)=1,
$$
所以第二个点也具有相同精确导子。辅助理想 $(67)$ 与它们互素，因此两个值都为全局单位。它们的乘积在 $M$ 中，故为 $\mathcal O_M^\times$ 中的元素。

此外，
$$
A-1=4488=12\cdot374,
\qquad
\Theta_{\mathfrak a}(P_f)
=\left(\frac{\Delta^{374}}{\psi_{67}(P_f)}\right)^{12}.
$$
既然这个十二次幂是全局单位，括号中的代数数在每个有限素位的赋值也为零，故自身是 $F$ 的全局单位。其 $F/K$ 范数属于
$\mathcal O_K^\times=\mu_4$，十二次幂为一。因此
$$
\mathrm N_{F/K}\Theta_{\mathfrak a}(P_f)=1.
$$
$\Theta_{\mathfrak a}$ 为偶函数，且 $\tau P_f=T-P_f$，所以
$$
u=\mathrm N_{F/M}\Theta_{\mathfrak a}(P_f).
$$
综上，
$$
\boxed{\quad u\in\mathcal O_M^\times,\qquad
\mathrm N_{M/K}u=1,\qquad
w=u/2^{26928}.\quad}
\tag{5}
$$
这比仅称 $w$ 为某个固定 $S$-unit 更准确。

## 3. 分母的普通范数只留下底数 2

R31 给出
$$
D_p(\alpha)^C=\frac{\sigma_{\mathfrak p}w}{w^p},
\qquad C=53856=2\cdot26928.
$$
由 (5) 及 $[M:K]=128$，
$$
\mathrm N_{M/K}w=2^{-26928\cdot128}=2^{-64C}.
$$
因此
$$
\bigl(\mathrm N_{M/K}D_p(\alpha)\bigr)^C
=2^{64C(p-1)}.
$$
两个 $C$ 次幂相同的 $K^\times$ 元素之比属于 $K$ 的根单位群 $\mu_4$。又 $D_p(\alpha)\equiv1\bmod\mathfrak p$，
$2^{64(p-1)}\equiv1\bmod p$；在奇素数 $p\ge13$ 处，$\mu_4$ 的约化单射。故该根单位为一：
$$
\boxed{\quad
\mathrm N_{M/K}D_p(\alpha)=2^{64(p-1)}.
\quad}
\tag{6}
$$
取标准的单位群 $p$-进对数，
$$
\boxed{\quad
\operatorname{Tr}_{M/K}\log_pD_p(\alpha)
=64(p-1)\log_p2.
\quad}
\tag{7}
$$
所以未加权的普通迹没有保留一个新的高秩单位分量。不能用它来替代目标的 $\lambda_p$ 或 $\lambda_{2p-1}$。

令
$$
B_p=\left(\frac2p\right)2^{(p-1)/2}\in1+p\mathbb Z_p,
\qquad
\widetilde D_p=\frac{D_p(\alpha)}{B_p}.
$$
因为 $C$ 为偶数，$B_p^C=2^{C(p-1)/2}$，由 (5) 得到更干净的固定单位关系
$$
\boxed{\quad
\widetilde D_p^C
=\frac{\sigma_{\mathfrak p}u}{u^p},
\qquad
\widetilde D_p\in1+p\mathcal O_{M,\mathfrak p},
\qquad
\mathrm N_{M/K}\widetilde D_p=1.
\quad}
\tag{8}
$$

## 4. u 不是根单位，且每个 p 的归一化值确实非零

**命题。** (4) 的固定全局单位 $u$ 不是根单位；对每个目标 $p$，都有 $\widetilde D_p\ne1$。

**证明。** 若 $u$ 为根单位，因 $M$ 在目标 $p$ 处不分歧，根单位阶素于 $p$，算术 Frobenius 在它上面准确作用为 $p$ 次幂。因此 (8) 给
$\widetilde D_p^C=1$。$C$ 为 $p$-进单位，且 $\widetilde D_p$ 为主单位，故 $\widetilde D_p=1$。

现在只取 $p=13$。这会给出
$$
D_{13}(\alpha)=B_{13}\in K.
$$
但 $D_{13}$ 的次数准确为 $12$，而
$[K(\alpha):K]=128$。非零多项式 $D_{13}(X)-B_{13}$ 的次数为 $12$，不可能以 $\alpha$ 为根，矛盾。这里的次数来自 R31/R29 的真实同源分母，不依赖数值计算。

这证明 $u$ 非挠。如果某个目标 $p$ 满足 $\widetilde D_p=1$，(8) 又给
$\sigma_{\mathfrak p}u=u^p$。反复作用一个有限阶的 $\sigma_{\mathfrak p}$，得到 $u=u^{p^d}$，再次迫使 $u$ 为根单位，矛盾。$\square$

于是每个 $p$ 的 $v_{\mathfrak P}(\widetilde D_p-1)$ 都有限。但此论证没有给出一个统一的门槛，例如至多 $3$，也没有单凭非挠性证明满足该门槛的素数无穷。

## 5. 加权迹保留了什么

对任意固定 $\beta\in M$，(8) 给出
$$
\boxed{\quad
C\,\operatorname{Tr}_{M/K}
\bigl(\beta\log_p\widetilde D_p\bigr)
=
\operatorname{Tr}_{M/K}
\bigl((\sigma_{\mathfrak p}^{-1}\beta-p\beta)\log_pu\bigr).
\quad}
\tag{9}
$$
这是一个明确的、固定数域单位对数的加权线性式。其证明只是
$\operatorname{Tr}(\beta\sigma z)
=\operatorname{Tr}((\sigma^{-1}\beta)z)$。
当 $\beta=1$ 时，右边为 $(1-p)\log_p\mathrm N u=0$，与 (7) 去掉底数 $2$ 分量后完全一致。

式 (9) 为后续比较提供了准确对象；本文尚未证明原 $\Phi$ 的 $g_0$ 或 $g_1$ 等于其中某个固定 $\beta$ 的表达式，也没有用 Baker 型非零性代替所需的估值界。

## 6. 配对分母的高 jet 及一个自动为零的迹

令
$$
J_{k,p}=
\left.\delta^k\log D_p(X(P))\right|_{P=P_f},
\qquad
B_k=\left.\delta^k\log F_{\mathfrak a}(P)\right|_{P=P_f}
\quad(k\ge1).
$$
对每个固定 $k$，$B_k$ 是固定的代数数。微分 R31 的准确辅助交换式，并使用 $[-67]P_f=P_f$，得到
$$
\bigl((-67)^k-4489\bigr)
\left.\delta^k\log F_{(\pi)}\right|_{P_f}
=\pi^k\sigma_{\mathfrak p}(B_k)-pB_k.
$$
由 $12\log D_p$ 与 $-\log F_{(\pi)}$ 仅差常数，
$$
\boxed{\quad
J_{k,p}
=-\frac{\pi^k\sigma_{\mathfrak p}(B_k)-pB_k}
{12((-67)^k-4489)}
\quad(k\ne2).
\quad}
\tag{10}
$$
对于 $k\equiv1\pmod{p-1}$，
$$
(-67)^k-4489\equiv-4556=-4\cdot17\cdot67\pmod p.
$$
所以在全部目标素数处，这个分母（连同 $12$）为单位。但 $k=p$ 或 $2p-1$ 时，$B_k$ 的索引仍随 $p$ 增长，不能称为一个固定有限集合。

还有一个必须保留的对称性。$D_p(X(P))$ 与 $F_{\mathfrak a}(P)$ 都在 $P\mapsto T-P$ 下不变，而该映射把不变微分送到其负值。因此
$$
\tau J_{k,p}=(-1)^kJ_{k,p},\qquad
\tau B_k=(-1)^kB_k.
$$
特别地，
$$
\boxed{\quad
\operatorname{Tr}_{F/K}J_{k,p}=0
\qquad(k\text{ 为奇数}).
\quad}
\tag{11}
$$
所以直接对分母的 $p$ 阶或 $(2p-1)$ 阶不变微分取未加权 $F/K$ 迹，会得到恒等于零，而非原来需要检测的目标矩。

### 6.1 k=2 的零分母由单独恒等式解决

对任意 CM 理想 $\mathfrak b=(b)$，有准确有理函数恒等式
$$
\delta^2\log\Theta_{\mathfrak b}(P)
=12\bigl(b^2x([b]P)-\mathrm N\mathfrak b\,x(P)\bigr).
\tag{12}
$$
可直接比较极点证明：在非零核点，两边均有首部 $12/(z-z_0)^2$；在 $O$，均有首部
$-12(\mathrm N\mathfrak b-1)/z^2$，且没有简单极点。差是常数。由定义式在 $O$ 展开，左侧常数项为
$12\sum_{0\ne R\in E[\mathfrak b]}x(R)=0$，因为 $[i]$ 置换核并把 $x$ 送到 $-x$；右侧也没有常数项。故差为零。

用 $x(P+T)=-17/x(P)$ 及
$x(P)+x(P+T)=X(P)^2$，由 (12) 得
$$
\boxed{\quad
J_{2,p}=p\alpha^2-\pi^2(\sigma_{\mathfrak p}\alpha)^2.
\quad}
\tag{13}
$$
因此 (10) 在 $k=2$ 的形式零分母不代表一个遗漏的未知常数；但解决它仍未把高 $k$ 的索引改成固定低阶。

## 7. 原目标实际对应未配对 Theta 的高阶迹

对每个奇数 $m\ge3$，R6、R19 给出
$$
\lambda_m
=2\operatorname{Tr}_{F/K}
\bigl(\delta^{m-2}x(P_f)\bigr).
\tag{14}
$$
继续微分 (12)，并在 $P_f$ 使用 Frobenius 作用：
$$
\left.\delta^m\log\Theta_{(\pi)}\right|_{P_f}
=12\bigl(\pi^m\sigma_{\mathfrak p}-p\bigr)
\delta^{m-2}x(P_f).
$$
取迹得到准确比较
$$
\boxed{\quad
\lambda_m=
\frac{\operatorname{Tr}_{F/K}
\left(\delta^m\log\Theta_{(\pi)}(P_f)\right)}
{6(\pi^m-p)}.
\quad}
\tag{15}
$$
对于 $m=p,2p-1$，分母的 $p$-进赋值为一。

未配对的值本身也来自一个固定全局单位
$v=\Theta_{\mathfrak a}(P_f)$：
$$
\Theta_{(\pi)}(P_f)^{4488}
=\frac{v^p}{\sigma_{\mathfrak p}v}.
\tag{16}
$$
但是 (15) 使用的是函数在该点处的 $m$ 阶几何微分，不是 (16) 中一个代数值的 $p$-进对数。对一个已求值的固定数取对数，不能恢复原函数的全部高阶 jet。配对后再取普通迹更会由 (11) 把相应奇阶信息直接消去。

因此当前准确缺口是：需要把 (15) 中随 $p$ 增长的高阶、未配对迹，或 R24–R26 的相应 $g_0,g_1$ 组合，非循环地与 (9) 这样的固定有限个加权单位对数比较，并控制其估值。R31 的固定单位发现与本篇的 norm-one 化已经完成；这个额外的高 jet 比较仍未完成。

## 来源与依赖

- R31：Theta 规范、固定 $w$、辅助交换式、$D_p(\alpha)$ 的 Frobenius 商。
- R18、R29：$\alpha$ 的次数、真实分母次数及 CM 作用。
- R6、R19：式 (14) 的目标矩规范。
- K. Rubin，1999 CM/BSD 讲义，Theorem 7.4：复合导子 torsion 值的全局单位性；其具体输入已在 §2 核对。
- §1 已给出本次所用 2-torsion division-polynomial 公式的完整归纳；§6.1 已给出第二微分恒等式的独立证明。
