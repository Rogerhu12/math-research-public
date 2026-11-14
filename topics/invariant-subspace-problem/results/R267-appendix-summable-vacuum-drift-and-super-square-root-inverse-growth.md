# R267 第一附录：可和真空漂移的增生块与超过平方根次数型的真实逆

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf8c51d 复核。

状态：以下实际非零正则器及逆增长下界均已证明，属于中间结论。它构造一个带收缩强单位的 $P\in\{A\}'$，但其逆在有限柱上的增长超过每个固定的平方根次数指数。因而 R261 的结论不能扩大到全部增生块乘积。本稿不构造慢理想湮灭者，也未证明新正则器可以完成任意见证的配对。

## 1. 纯有限块及一个收缩 Cayley 逆词

先在一个含 $q\ge4$ 个位的有限纯块上计算，始终明确区分后面要构造的实际算子。令
$$
D_q=\sum_{j=1}^q E_j,\qquad
T_q=\frac{2D_q}{q+2},\qquad
U_q^0=2(I+T_q)^{-1},\qquad
L_q^0=U_q^0-I.
\tag{1.1}
$$
在物理 $r$ 孔层，$D_q$ 的每列有 $r$ 个1，每行有 $q-r+1$ 个1。Schur 界给
$$
\|D_q\|\le\max_r\sqrt{r(q-r+1)}\le\frac{q+1}{2}.
$$
所以
$$
\|T_q\|\le\frac{q+1}{q+2}<1,\qquad
\|U_q^0\|\le2(q+2).
\tag{1.2}
$$

准确有
$$
L_q^0=(I-T_q)(I+T_q)^{-1},
$$
因此
$$
\operatorname{Re}L_q^0
=(I+T_q^*)^{-1}(I-T_q^*T_q)(I+T_q)^{-1}\ge0.
\tag{1.3}
$$
其预解式反而是简单的收缩
$$
(I+L_q^0)^{-1}=\frac{I+T_q}{2}.
\tag{1.4}
$$

取块 Haar 真空 $\Omega=\Omega_+^{\otimes q}$，记
$$
g_q=U_q^0\Omega,\qquad \alpha_q=\langle g_q,\Omega\rangle.
$$
下面支付它的全部积分尾及方差；不能只用 $\|U_q^0\|=O(q)$ 来估计真空列。

## 2. 真空列的统一积分界

有限维 Bochner 积分给
$$
g_q=2\int_0^\infty e^{-s}e^{-sT_q}\Omega\,ds.
\tag{2.1}
$$
令 $a=s/(q+2)$。在每一位上，
$$
e^{-2aE}\Omega_+=(1-a)\Omega_++a\chi.
$$
于是
$$
v_q(s):=e^{-sT_q}\Omega
=\bigotimes_{j=1}^q((1-a)\Omega_++a\chi),
$$
$$
h_q(s):=\langle v_q(s),\Omega\rangle=(1-a)^q,\qquad
\|v_q(s)\|^2=(1-2a+2a^2)^q.
\tag{2.2}
$$

### 2.1 对全部 $s$ 有效的支配

对全部 $a\ge0$，
$$
1-2a+2a^2\le e^a.
\tag{2.3}
$$
证明：$f(a)=e^a-1+2a-2a^2$ 满足 $f(0)=0$；
$f'(a)=e^a+2-4a$ 的最小值在 $a=\log4$，等于
$6-4\log4>0$。故 $f(a)\ge0$。

因此
$$
\boxed{e^{-s}\|v_q(s)\|\le e^{-s/2}\quad(s\ge0),\qquad
\|g_q\|\le4.}
\tag{2.4}
$$
该界保留了 $s$ 超过 $q$ 后 $(1-a)^q$ 的符号变化和多项式增长，没有在大 $s$ 区域使用错误的小参数展开。

### 2.2 均值及正交部分

当 $0\le s\le(q+2)/4$，$0\le a\le1/4$。由二项式差分，
$$
\begin{aligned}
\|v_q(s)-h_q(s)\Omega\|^2
&=((1-a)^2+a^2)^q-(1-a)^{2q}\\
&\le q a^2(1-2a+2a^2)^{q-1}.
\end{aligned}
$$
因为 $1-2a+2a^2\le1-\tfrac32a$、$q\ge4$，得到
$$
\boxed{\|v_q(s)-h_q(s)\Omega\|
\le\frac{s}{\sqrt q}e^{-3s/8}.}
\tag{2.5}
$$

在同一区间，
$$
|q\log(1-a)+s|
\le\frac{2s+s^2}{q},\qquad
q\log(1-a)\le-\frac23s.
$$
对实指数用中值估计可得
$$
\boxed{|h_q(s)-e^{-s}|
\le\frac{2s+s^2}{q}e^{-2s/3}.}
\tag{2.6}
$$
在余下区间，(2.4) 同时控制 $v_q(s)$ 和 $|h_q(s)|$。

把 (2.5)—(2.6) 代入 (2.1)，并在 $s=(q+2)/4$ 分段。初等指数积分给以下安全常数：
$$
|\alpha_q-1|\le\frac{16}{q},\qquad
\|g_q-\alpha_q\Omega\|\le\frac9{\sqrt q},
\qquad
\|g_q-\Omega\|\le\frac{20}{\sqrt q}.
\tag{2.7}
$$
例如均值的小区间误差至多
$$
\frac2q\int_0^\infty(2s+s^2)e^{-5s/3}ds<\frac3q,
$$
其尾至多 $5e^{-(q+2)/8}\le12/q$。
正交部分的小区间至多
$2q^{-1/2}\int_0^\infty s e^{-11s/8}ds<2q^{-1/2}$，
尾至多 $8e^{-(q+2)/8}<8q^{-1/2}$；直接保留前一积分的准确值即得 (2.7) 中的9，最后一个20也覆盖较粗常数。

由于 (1.3)，$\alpha_q-1=\langle L_q^0\Omega,\Omega\rangle$ 为非负实数。因此
$$
\boxed{
0\le\alpha_q-1\le\frac{16}{q},\qquad
0\le\|g_q\|^2-1
=2(\alpha_q-1)+\|g_q-\Omega\|^2
\le\frac{432}{q}.
}
\tag{2.8}
$$

## 3. 反向全块向量上的大逆矩

令 $\chi_{[q]}=\chi_1\cdots\chi_q$。同一积分中，每位有
$\langle E\chi,\chi\rangle=-1/2$，所以
$$
\boxed{
\langle U_q^0\chi_{[q]},\chi_{[q]}\rangle
=2\int_0^\infty e^{-s}
\left(1+\frac{s}{q+2}\right)^q ds.
}
\tag{3.1}
$$
该积分全部非负。

在 $0\le s\le\sqrt q$ 上，$\log(1+x)\ge x-x^2/2$ 给
$$
q\log\left(1+\frac{s}{q+2}\right)-s
\ge-\frac{2s}{q+2}
-\frac{q s^2}{2(q+2)^2}
\ge-\frac32.
$$
因此
$$
\boxed{
\langle U_q^0\chi_{[q]},\chi_{[q]}\rangle
\ge2e^{-3/2}\sqrt q\ge\frac{\sqrt q}{4}.
}
\tag{3.2}
$$
真空列的平方偏差只有 $O(q^{-1})$，而另一个完整有限柱上的逆矩至少为 $\sqrt q/4$。二者不矛盾，因为输入不同。

## 4. 用有限 Walsh 符号提升到真实代数并支付 carry

现取原 Haar 空间中一个任意有限位块 $F$，$|F|=q$、$m=\min F$。
将纯 $g_q$ 放在这些位上，仍记作 $g_F$。它是一个有限 Walsh 多项式，
$$
g_F=\sum_{J\subseteq F}c_J\chi_J.
$$
定义实际有界乘子
$$
X_{g_F}=\sum_{J\subseteq F}c_JV_J\in\mathcal A.
$$
与之比较的纯算子准确为
$$
U_F^0=\sum_{J\subseteq F}c_JV_J^0
=2\left(I+\frac2{q+2}\sum_{j\in F}E_j\right)^{-1},
\qquad V_j^0=I-2E_j.
\tag{4.1}
$$
等式只在纯有限代数内使用；其理由是两边作用于纯循环真空后同为 $g_F$。

已有实际估计
$$
\|V_j-V_j^0\|\le8\eta_j,\qquad
\|V_j\|,\|V_j^0\|\le6
$$
给
$$
\|V_J-V_J^0\|
\le8q6^{q-1}\eta_m.
$$
又 (2.4) 和 Cauchy--Schwarz 给
$$
\sum_{J\subseteq F}|c_J|\le2^{q/2}\|g_F\|\le4\cdot2^{q/2}.
$$
所以
$$
\boxed{
\|X_{g_F}-U_F^0\|
\le32q9^q e^{-77016^m}
=:\varepsilon(F).
}
\tag{4.2}
$$

定义
$$
\widetilde g_F=g_F+\varepsilon(F)1,\qquad
\widetilde U_F=X_{\widetilde g_F},\qquad
\widetilde L_F=\widetilde U_F-I.
$$
由 (1.3) 和 (4.2)，
$$
\boxed{\operatorname{Re}\widetilde L_F\ge0.}
\tag{4.3}
$$
因此 $\widetilde R_F=\widetilde U_F^{-1}$ 是实际收缩交换子。

本附录允许每块有非零、可和的真空均值漂移，所以 (4.2) 的小正标量可以合法加入。这里没有沿用 R267 奇数零真空块所要求的严格零均值。

若 $\varepsilon(F)\le q^{-2}$，由 (2.4)、(2.8)，
$$
\boxed{
1\le\langle\widetilde g_F,1\rangle\le1+\frac{17}{q},
\qquad
1\le\|\widetilde g_F\|^2\le1+\frac{500}{q}.
}
\tag{4.4}
$$

## 5. 选择块大小和物理位置

令
$$
q_\nu=4096+
\left\lceil(\nu+2)(\log(\nu+2))^{3/2}\right\rceil
\qquad(\nu\ge1).
\tag{5.1}
$$
则
$$
\sum_{\nu\ge1}\frac1{q_\nu}
\le\sum_{k\ge3}\frac1{k(\log k)^{3/2}}
\le\int_2^\infty\frac{dx}{x(\log x)^{3/2}}
=\frac2{\sqrt{\log2}}<3.
\tag{5.2}
$$
记
$$
Q_n=\sum_{\nu=n}^{2n}q_\nu.
$$

递归选择整数 $m_\nu$，使各连续块
$$
F_\nu=[m_\nu,m_\nu+q_\nu)
$$
两两不交且从低位到高位排列，并同时满足
$$
32q_\nu9^{q_\nu}e^{-77016^{m_\nu}}
\le2^{-\nu}q_\nu^{-2},
\tag{5.3}
$$
$$
8Q_\nu6^{Q_\nu-1}e^{-77016^{m_\nu}}
\le2^{-\nu}e^{-1000}.
\tag{5.4}
$$
每一步只有有限个已知数，且左侧随 $m_\nu\to\infty$ 趋零，所以这样的递归明确定义且总能继续。它不依赖尚未构造的见证向量或任何未知尾速率。

对每个 $F_\nu$ 应用第4节，记
$$
\widetilde g_\nu=\widetilde g_{F_\nu},\quad
\widetilde U_\nu=X_{\widetilde g_\nu},\quad
\widetilde R_\nu=\widetilde U_\nu^{-1}.
$$
由 (4.4)—(5.3)，这些源列满足
$$
\alpha_\nu:=\langle\widetilde g_\nu,1\rangle\ge1,\qquad
\sum_\nu(\|\widetilde g_\nu\|^2-1)<\infty,
\qquad
\sum_\nu|\alpha_\nu-1|<\infty.
\tag{5.5}
$$

## 6. 可和均值版本的真实乘积引理

定义实际算子
$$
P_n=\prod_{\nu=1}^n\widetilde R_\nu,\qquad
U_n=\prod_{\nu=1}^n\widetilde U_\nu.
$$
每个 $\widetilde R_\nu$ 为收缩，全部因子交换，且 $P_nU_n=I$。

由于符号位块互不交，R267 中的准确真空展开仍给
$$
g_n:=U_n1=\prod_{\nu=1}^n\widetilde g_\nu
\tag{6.1}
$$
作为通常 Walsh 函数乘积。常数项现在不必为1；不同块仍独立。

对尾乘积 $g_{n,m}=\prod_{\nu=n+1}^m\widetilde g_\nu$，
$$
\|g_{n,m}-1\|^2
=\prod_{\nu=n+1}^m\|\widetilde g_\nu\|^2
+1-2\prod_{\nu=n+1}^m\alpha_\nu
\le
\prod_{\nu=n+1}^m\|\widetilde g_\nu\|^2-1.
\tag{6.2}
$$
由 (5.5)，右侧随 $n\to\infty$ 一致于 $m>n$ 趋零；全部正标量均值尾积也趋于1。于是 $g_n$ 在 $H$ 收敛到真正向量 $g$。由 (4.4)、(5.2)，
$$
\boxed{\|g\|\le
\exp\!\left(250\sum_\nu q_\nu^{-1}\right)<e^{750}<e^{1000}.}
\tag{6.3}
$$

令 $Q_{n,m}=\prod_{\nu=n+1}^m\widetilde R_\nu$。
准确有 $Q_{n,m}g_{n,m}=1$，故
$$
\|(Q_{n,m}-I)1\|
\le\|g_{n,m}-1\|\longrightarrow0.
\tag{6.4}
$$
尾积均收缩，交换性和 $1$ 的循环性把该结论延伸到全 $H$。

与 R267 相同的实际论证现在给
$$
\boxed{
P_n\longrightarrow P\ne0\quad\mathrm{SOT},\qquad
Pg=1,\qquad
\|PU_n\|\le1,\qquad PU_n\longrightarrow I\quad\mathrm{SOT}.
}
\tag{6.5}
$$
例如对固定 $n$，$P_mU_n=Q_{n,m}$；先令 $m\to\infty$ 得 $PU_n$ 为收缩尾积极限，再用 (6.4) 令 $n\to\infty$。因此始终是同一组 $U_n$。

于是 $P$ 单射、稠密像，并在所有有限放大不变旗子商上具有同样性质。[R244 聚合附录](R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md) 又给
$$
G:=P^{-1}=X_g,\qquad
G(V_J1)=V_Jg.
\tag{6.6}
$$
全部有限 Walsh 柱都是其真实图核心。这是后面实际逆测试的依据。

## 7. 高窗口的真实逆增长

令
$$
J_n=\bigcup_{\nu=n}^{2n}F_\nu,\qquad
x_n=\chi_{J_n}.
$$
则 $\|x_n\|=1$、其次数准确为 $Q_n$。由 (6.6)，
$$
Gx_n=V_{J_n}g.
\tag{7.1}
$$

先比较纯 $V_{J_n}^0$。由于 $g$ 是完整的互不交块乘积，
$$
\|V_{J_n}^0g\|
=
\left[\prod_{\nu=n}^{2n}
\|V_{F_\nu}^0\widetilde g_\nu\|\right]
\left[\prod_{\nu\notin[n,2n]}
\|\widetilde g_\nu\|\right].
\tag{7.2}
$$
未选块的范数均至少为1。选中块内部只有纯有限代数在运算，由 (4.1) 的交换性，
$$
V_{F_\nu}^0\widetilde g_\nu
=(U_{F_\nu}^0+\varepsilon(F_\nu)I)\chi_{F_\nu}.
$$
用 (3.2) 的正对角矩，得到
$$
\|V_{F_\nu}^0\widetilde g_\nu\|
\ge\frac{\sqrt{q_\nu}}4.
$$
因此
$$
\boxed{\|V_{J_n}^0g\|
\ge\prod_{\nu=n}^{2n}\frac{\sqrt{q_\nu}}4.}
\tag{7.3}
$$

现在完整支付实际测试误差。所有被测试的位都不小于 $m_n$，所以
$$
\|V_{J_n}-V_{J_n}^0\|
\le8Q_n6^{Q_n-1}e^{-77016^{m_n}}
\le2^{-n}e^{-1000}.
$$
结合 (6.3)，
$$
\boxed{\|Gx_n-V_{J_n}^0g\|\le2^{-n}.}
\tag{7.4}
$$
选取高窗口是必要的：这里没有让固定的最早 carry 误差乘上无限增大的测试次数。低块只作为 $g$ 的未选张量因子保留。

由于 $q_\nu\ge4096$，(7.3) 的每个因子至少为16。由 (7.3)—(7.4)，例如对全部 $n\ge1$，
$$
\boxed{
\|Gx_n\|\ge
\frac12\prod_{\nu=n}^{2n}\frac{\sqrt{q_\nu}}4.
}
\tag{7.5}
$$

由 (5.1)，存在固定正常数 $c_1,c_2,c_3$，对充分大的 $n$，
$$
c_1n^2(\log n)^{3/2}\le Q_n
\le c_2n^2(\log n)^{3/2},
$$
$$
\log\|Gx_n\|
\ge\frac12\sum_{\nu=n}^{2n}\log q_\nu
-(n+1)\log4-\log2
\ge c_3n\log n.
$$
于是
$$
\boxed{
\frac{\log\|Gx_n\|}{\sqrt{Q_n+1}}
\longrightarrow+\infty.
}
\tag{7.6}
$$

若将有限次数逆成本定义为
$$
M_P(q)=
\sup\{\|Gu\|:\ u\text{ 为有限 Walsh 柱},\
\deg u\le q,\ \|u\|=1\},
$$
则 (7.6) 也给
$$
\limsup_{q\to\infty}
\frac{\log M_P(q)}{\sqrt{q+1}}=+\infty.
$$
该定义允许上确界为无穷；未擅称整个无限维次数层都属于 $\operatorname{Dom}G$ 或已有有限算子范数上界。

## 8. 每个平方根域及其共同 Fréchet 域的真实像障碍

对 $\epsilon>0$，令
$$
\mathcal H_{\epsilon,\sqrt{\ }}=
\operatorname{Dom}e^{\epsilon\sqrt{1+\mathcal N}}
$$
配其通常 Hilbert 图范数。

若 $\mathcal H_{\epsilon,\sqrt{\ }}\subseteq\operatorname{Ran}P$，
则闭算子 $G=P^{-1}$ 在这个 Hilbert 空间上全域定义，且其图闭；
闭图定理给
$$
\|Gu\|\le C_\epsilon
\|e^{\epsilon\sqrt{1+\mathcal N}}u\|.
$$
代入 $x_n$，右端为
$C_\epsilon e^{\epsilon\sqrt{1+Q_n}}$，与 (7.6) 矛盾。因此
$$
\boxed{
\mathcal H_{\epsilon,\sqrt{\ }}\not\subseteq\operatorname{Ran}P
\qquad\text{对每个 }\epsilon>0.
}
\tag{8.1}
$$

还存在同一个 $f$ 同时具有全部平方根指数矩，却不在 $\operatorname{Ran}P$。确切地，令
$$
\mathcal E=\bigcap_{k\ge1}
\operatorname{Dom}e^{k\sqrt{1+\mathcal N}}
$$
配递增 Hilbert 图范数生成的 Fréchet 拓扑。若 $\mathcal E\subseteq\operatorname{Ran}P$，
Fréchet 到 Banach 的闭图定理使 $G:\mathcal E\to H$ 连续。
连续性必由某个有限指标 $k$ 的图范数控制，再次与 (7.6) 矛盾。
故
$$
\boxed{
\exists f\in\bigcap_{\epsilon>0}
\operatorname{Dom}e^{\epsilon\sqrt{1+\mathcal N}},
\qquad f\notin\operatorname{Ran}P.
}
\tag{8.2}
$$
这里是同一个向量，不是对每个权另选一个坏向量。

[R261](R261-infinite-positive-resolvent-inverses-zero-type-degree-domains.md) 已证明每个非零规范正一阶无穷预解式积，以及其中列明的有限混合附加因子，都包含每个上述平方根域。因此本稿的 $P$ 不属于该类；(8.1) 是严格的实际区分，不是仅从生成元形式不同作推测。

## 9. 对见证专属正则化的意义和边界

本稿提供一类仍有真正收缩强单位、却突破 R261 平方根逆增长限制的实际交换正则器。新增长来自大块上的收缩 Cayley 结构；可和的正真空漂移没有使乘积极限消失，真实 carry 已由有限 Walsh 提升及高窗口分别支付。

R244 聚合判据适用于这个 $P$。若对一个假想正正常慢湮灭者能证明
$$
|\phi(X_u)|\le C_\phi\|P^{-1}u\|
$$
在全部有限柱上一致成立，就得到矛盾。但 (7.6) 只是某些测试方向的逆下界，不给这个对所有 $u$ 的聚合控制。

同样，(8.1)—(8.2) 不说明 $P$ 已属于 $S\mathcal A'$ 或 $S B(H)$，也不求得 R253 的完整尾理想范数。这里只证明先前一阶类的零型障碍不是所有合法收缩强单位的普遍障碍；一般见证配对与普通 ISP 仍需继续。
