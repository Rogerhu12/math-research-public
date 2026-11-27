# R1011 — 同一个未 depletion 最高循环与全部普通素数的严格 Chow Euler 因子

日期：2026-11-27。会话：`Astra-rank2-Sha-0b097461-20261127`。

**已证明。** R1006 中随 $p$ 写出的三个同源图组合，在原最高
$P_-$、原 $\eta_j$ 投影和完整 corestriction 后，都等于一个
**与 $p$ 无关的固定循环**乘以明确非零代数数。
本篇在 Chow 层面证明这一点，保留原 full9 级结构、全部54图、
算术 Frobenius 方向和两次 $\mathfrak p$ 商。

因此 R817/R1006 的7993非零实际检测的是这一个固定未 depletion
循环；对每个其余好分裂 $p$，其原最高 AJ 非零恰等价于原
Katz 负二值非零。没有因此证明跨 $p$ 非零。

## 1. 固定对象及准确系数

记
$$
K=\mathbf Q(\omega),\quad\delta=1+2\omega,\quad
A=E_{27}:y^2+y=x^3,\quad\psi=\psi_{27}.
\tag{1}
$$
系数域记作 $E=\mathbf Q(\zeta_9)$，不与椭圆曲线 $A$ 混淆。
沿 R1006 取完整306级数据，其中9级基严格是
$$
\ell_9=((1+\omega)u_9,(\omega-1)u_9).
\tag{2}
$$
真实原 $K$ 分量及 $g=P h$ 不改变。

对 $i=(t,s)$ 遍历 $3\cdot18$ 个标签，令
$$
C_i=C_{2,t}+C_{17,s}\subset A[34],\qquad
q_i:A\longrightarrow A_i=A/C_i,
\tag{3}
$$
并将(2)沿 $q_i$ 运输到 $A_i$。忘至 R991/R997 的实际
$\Gamma$ 模问题后，得到 $b_i\in B$ 及同源
$\varphi_i:A\to S_{b_i}$。系数
$c_i=c_{2,t}c_{17,s}$ 完全是 R1006(18)–(20)的原系数。
每条图都保留，重复点仍按原重数出现。

取一个固定有限 Galois 扩张 $L/K$，包含 $H$、全部这些级点、
商同源及所需模型同构。所有 Chow 群均用 $E$ 系数，Galois
只作用几何数据并固定 $E$ 为标量。定义
$$
Z_{j,0,L}=\sum_i c_i\Delta_{\varphi_i},\qquad
Y_{j,0}=P_-e_{\eta_j}\operatorname{Cor}_{L/H}Z_{j,0,L},
\tag{4}
$$
$$
\Delta_{\varphi_i}
=\Gamma_{\varphi_i}-34(S_{b_i}\times O_A)-(O_{b_i}\times A),
\qquad
e_{\eta_j}=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
\eta_j(\sigma)^{-1}\sigma.
\tag{5}
$$
$Y_{j,0}$ 是一个固定的原 Artin 特征循环，按 R1006§11–12
下降到原 $K$ 表示。它没有在定义中使用任何普通素数。
严格 projector 与同调零性均由 R995/R997 保证。

以下取 R1006 允许的好素数 $p>3$，$p\nmid34$，在 $K$ 分裂，
且不分歧于固定数据域 $L$。这些排除只涉及一个固定有限集合。
固定与原普通方向相符的
$$
p=\mathfrak p\bar{\mathfrak p},\qquad
\pi=\psi(\mathfrak p),\quad\bar\pi=\psi(\bar{\mathfrak p}),
\quad\pi\bar\pi=p.
\tag{6}
$$
在指定 $p$-adic 嵌入中 $v_p(\pi)=1$、$v_p(\bar\pi)=0$。
$\pi$ 是 $A$ 的真实 CM Frobenius；不能把 $\psi_0$ 的 primary
生成元直接放入(6)而漏掉 $\psi_{27}/\psi_0$ 的有限三次扭曲。

设 $\sigma_{\mathfrak p}\in\operatorname{Gal}(L/K)$ 是一个
算术 Frobenius，并记
$$
e_j(p)=\eta_j(\sigma_{\mathfrak p}|_H)=\eta_j(\mathfrak p).
\tag{7}
$$
这里 Artin 方向采用 R1006(23)–(25)、(52)。
weight3 模形式 $f_{27}=\theta(\psi^2)$ 在 $p$ 的 Hecke 系数为
$$
\boxed{A_p=\pi^2+\bar\pi^2.}
\tag{8}
它不是椭圆曲线 $A$ 的 weight2 迹 $\pi+\bar\pi$。

## 2. 商对象的完整 full9 同构

取对应于所选素位的算术 Frobenius 提升；其在 $L$ 上的限制仍记为
$\sigma_{\mathfrak p}$。CM 主定理按(6)–(7)给
$$
\sigma_{\mathfrak p}|_{A[N]}=[\pi]
\quad\text{对每个 }N\mid306.
\tag{9}
$$
这是同一个算术 Frobenius 提升在 prime-to-$p$ Tate 模上的
标量等式在 $L$ 内级点的限制，尤其同时适用于 $N=34$ 与 $N=9$。因此
$$
\sigma_{\mathfrak p}C_i=\pi C_i,
\qquad\sigma_{\mathfrak p}\ell_9=\pi\ell_9.
\tag{10}
$$
在 $A_i$ 上取由 $q_i(A[\mathfrak p^k])$ 给出的 CM 商，$k=1,2$。
由于 $\deg q_i=34$ 素于 $p$，$q_i$ 运输所选普通形式方向；
这正是 R997(28)中 canonical $\mathfrak p^k$ 子群，不另选
另一素位。其合成商的核为
$$
D_{i,k}=C_i+A[\mathfrak p^k].
\tag{11}
$$
另一方面，(10)及 $\pi$ 在 $A[34]$ 上可逆给出有限群概形等式
$$
[\pi^k]^{-1}(\sigma_{\mathfrak p}^k C_i)
=[\pi^k]^{-1}(\pi^k C_i)
=C_i+A[\mathfrak p^k].
\tag{12}
$$
为明确(12)不是只比较点数：若 $P$ 在左侧，则存在
$Q\in C_i$ 使 $[\pi^k]P=[\pi^k]Q$，故
$P-Q\in A[\mathfrak p^k]$；反向直接。特征零下这些有限群
概形均 étale，故点上的此等式就是群概形等式。

由商的泛性质有唯一保零点的同构
$$
\iota_{i,k}:A/D_{i,k}\xrightarrow{\ \sim\ }
\sigma_{\mathfrak p}^k(A_i)
$$
使
$$
\iota_{i,k}\circ q_{D_{i,k}}
=(\sigma_{\mathfrak p}^kq_i)\circ[\pi^k].
\tag{13}
$$
两边都是次数 $34p^k$ 的同源，(13)是商映射的等式，非另加
一个未定的 CM 单位。

对(2)的**两个**9级基元 $P$，(9)和(13)给
$$
\iota_{i,k}\bigl(q_{D_{i,k}}(P)\bigr)
=(\sigma_{\mathfrak p}^kq_i)([\pi^k]P)
=\sigma_{\mathfrak p}^k(q_i(P)).
\tag{14}
$$
所以(13)保完整有序9级基，因而也保真实 $\Gamma$ 级结构。
Weil pairing 同时核合：商次数使 pairing 乘指数 $p^k$，
算术 Frobenius 在 $\mu_9$ 上也恰是 $\zeta\mapsto\zeta^{p^k}$。
若 $p\not\equiv1\pmod9$，两边都移动到同一个 full9 分量；
$p$ 在 $K$ 分裂保证 $p\equiv1\pmod3$，故忘到原 $K$ 上
的 $S$ 后分量仍准确。没有在此额外施一次 $h$ 或复共轭。

也可先在 fine full9 通用族上比较(13)–(14)，再忘至 $S$；
这样不需假设 coarse moduli 点自己消除了所有模型自同构。
任一保完整9级的自同构都是恒等，所以已固定的模型同构沿
(14)一致下降。

于是，将 R997 实际 $\mathfrak p^k$ 商的目标放回 $S$ 的上述
完整模问题后，有真正的同源等式
$$
\boxed{b_{i,k}=\sigma_{\mathfrak p}^k b_i,\qquad
\varphi_{i,k}=(\sigma_{\mathfrak p}^k\varphi_i)\circ[\pi^k].}
\tag{15}
$$
特别地，不要求 $[\pi]$ 是目标 $S_{b_i}$ 的自同态。其 CM
order 可有 conductor34；$[\pi]$ 在(15)只作用于具有完整
$\mathcal O_K$ 乘法的**外部源曲线** $A$。

## 3. 修正图的严格 pullback，包括 $p^2$

令 $u_k=1_S\times[\pi^k]:S\times A\to S\times A$。
这是有限平坦映射。在纤维积中，(15)逐个给
$$
u_k^*\Gamma_{\sigma_{\mathfrak p}^k\varphi_i}
=\Gamma_{\varphi_{i,k}}.
\tag{16}
$$
右侧是一条完整图，并非原图乘 $p^k$；它的投影到 $A$ 仍是
恒等。有限平坦 pullback 包含全部原像，这支付了所有分支。

对两个修正项则有
$$
u_k^*(S_{\sigma^k b_i}\times O_A)
=S_{\sigma^k b_i}\times[\pi^k]^*[O_A],
$$
$$
u_k^*(O_{\sigma^k b_i}\times A)
=O_{\sigma^k b_i}\times A.
\tag{17}
$$
$[\pi^k]^*[O_A]$ 是全部 $A[\mathfrak p^k]$ 的约化和。
其 degree 为 $p^k$，而群中点之和为0：$p$ 为奇数，除0外的点
成 $P,-P$ 对。椭圆曲线的 $\operatorname{Pic}^0\simeq A$ 因而给
$$
[\pi^k]^*[O_A]\sim p^k[O_A].
\tag{18}
$$
该等式定义在 $K$ 上；$O_A$ 是 $K$ 有理点，所以不产生
Picard 的下降障碍。

结合(16)–(18)，得到在 $\operatorname{CH}^2(S\times A)_E$ 中
$$
\boxed{\Delta_{\varphi_{i,k}}
=u_k^*\bigl(\sigma_{\mathfrak p}^k\Delta_{\varphi_i}\bigr),
\qquad k=1,2.}
\tag{19}
$$
次数修正项准确为 $34p^k(S_{\sigma^k b_i}\times O_A)$。
因此二次项是 $u_2^*\sigma^2$，不是只用一次 $u_1^*$ 后把
次数或 Frobenius 幂忘掉。

因为(6)的 $[\pi]$ 定义于 $K$，它与 $\sigma_{\mathfrak p}$
交换。故(19)也可由第一次恒等式迭代得到，两个证明给相同
$\pi^2$、$\sigma^2$ 和 $34p^2$。

## 4. 原最高线、有限投影和完整 trace

在 R995 的严格 $h_1(A)$ 上，$g=[\delta]^*$，
$e_A^-=(1-g/\delta)/2$。若 $\pi=a+b\omega$，则 $h_1$ 上
CM endomorphism 的加法性给
$$
[\pi]^*=(a-b/2)\,1+(b/2)g,
\qquad
e_A^-[\pi]^*=\bar\pi e_A^-.
\tag{20}
$$
这里加法性是 $\operatorname{Hom}(A,A)\otimes\mathbf Q$
到 $\operatorname{End}(h_1(A))$ 的标准对应等式，不只是上同调
特征值。$P_-=e_S^-\otimes e_A^-$，故
$$
P_-u_k^*=\bar\pi^kP_-.
\tag{21}
$$
$P_-$ 的所有对应定义于 $K$，与几何 Galois 作用交换。
这也是原 $V_j=\eta_j^{-1}\chi_{27}^3\varepsilon^{-1}$ 的那条
线；若错用 $P_+$，(21)会变成 $\pi^k$，不再是本篇原目标。

定义 $Z_{j,k,L}=\sum_i c_i\Delta_{\varphi_{i,k}}$。
(19)逐项成立，且 $c_i$ 固定为标量，所以
$$
Z_{j,k,L}=u_k^*\sigma_{\mathfrak p}^k Z_{j,0,L}.
\tag{22}
$$
没有要求 $\sigma$ 保持每一个子群标签；它按(10)真实置换
全部子群和目标，(22)保留了每项原 $c_i$。

有限 Galois 扩张的 corestriction 与 $\sigma$ 相容：若
$\sigma_H=\sigma|_H$，则
$$
\operatorname{Cor}_{L/H}\sigma^k
=\sigma_H^k\operatorname{Cor}_{L/H}.
\tag{23}
$$
这是对 $\operatorname{Gal}(L/H)$ 的共轭重排，不需删去稳定子
重数。原投影满足
$$
e_{\eta_j}\sigma_H^k=e_j(p)^k e_{\eta_j}.
\tag{24}
$$
例如将 $\tau=\rho\sigma_H^k$ 代入其完整18项和，正得到
$\eta_j(\sigma_H)^k$；这里没有逆号。

由(21)–(24)，在原 Artin Chow 对象中严格有
$$
\boxed{P_-e_{\eta_j}\operatorname{Cor}_{L/H}Z_{j,k,L}
=\bigl(e_j(p)\bar\pi\bigr)^kY_{j,0},\qquad k=0,1,2.}
\tag{25}
$$
式(25)没有除掉 $[L:H]$ 或18，也没有将原 corestriction 改成
平均：其两侧使用同一个完整算子。

## 5. 严格 Chow depletion 公式及非零

R1006 的原循环是
$$
Y_{j,p}^{[p]}=P_-e_{\eta_j}\operatorname{Cor}_{L/H}
\left(Z_{j,0,L}-\frac{A_p}{p^2}Z_{j,1,L}
+\frac1{p^2}Z_{j,2,L}\right).
\tag{26}
$$
代入(8)、(25)并用 $p=\pi\bar\pi$，得
$$
\boxed{Y_{j,p}^{[p]}=d_j(p)Y_{j,0},}
\tag{27}
$$
$$
\begin{aligned}
d_j(p)
&=1-\frac{\pi^2+\bar\pi^2}{p^2}e_j(p)\bar\pi
  +\frac{e_j(p)^2\bar\pi^2}{p^2}\\
&=\boxed{\left(1-\frac{e_j(p)}{\bar\pi}\right)
\left(1-\frac{e_j(p)\bar\pi}{\pi^2}\right).}
\end{aligned}
\tag{28}
$$
这与 R997 的 $p^{-2}$ 次数系数一致；若把(8)换成 weight2
迹或把(19)错用 pushforward，(28)均不成立。

$e_j(p)$ 是根单位，$\pi$ 的每个复嵌入绝对值为 $\sqrt p$。
于是(28)两项被减去的数的绝对值都为 $p^{-1/2}<1$。因此
$$
\boxed{d_j(p)\in E^\times\text{，且任一系数素位下均非零。}}
\tag{29}
$$
在指定 $p$ 方向，第二因子的 valuation 是 $-2$；第一因子
可以有正 valuation，故(29)不是统一整单位断言。全文在有理
Chow/有理 AJ 中使用它，未删去任何原整格条件。

角色还给另一种准确写法。由
$\eta_j(\bar{\mathfrak p})=\eta_j(\mathfrak p)^{-1}$、
$\nu_j=\eta_j\psi^{-1}\bar\psi^2$ 及 $\beta_j=\psi\eta_j$，
$$
\boxed{d_j(p)=
\left(1-\beta_j(\bar{\mathfrak p})^{-1}\right)
\left(1-\frac{\nu_j(\mathfrak p)}p\right).}
\tag{30}
$$
$\nu_j$ 在此仍等于原 $\eta_j\psi_0^{-1}\bar\psi_0^2$，因为
$\psi/\psi_0$ 的三次方为1。式(30)逐项对上两个 Katz 因子的
普通 Euler 项，不只比较最终绝对值。

## 6. 固定循环的全部实现与7993

式(27)是 $E$ 系数 Chow 等式，所以对**任意**实现素位
$\lambda\mid\ell$ 都有
$$
\operatorname{AJ}_{\lambda}(Y_{j,p}^{[p]})
=\iota_\lambda(d_j(p))\operatorname{AJ}_{\lambda}(Y_{j,0}).
\tag{31}
$$
这里甚至不要求 $\ell=p$。式(31)不是由不同 $p$ 的数值实验
归纳，而是一个固定有限代数对应的自然性。

记按 R1006 相同微分和原 $H$ 有限和求得的值为
$$
\mathcal J^0_{j,p}
=\operatorname{AJ}_{p}(Y_{j,0})(\Omega_S\omega_A).
$$
则 R1006(5)和(27)给
$$
\boxed{
(\mathcal J^0_{j,p})^2
=\frac{\iota_p(-486\omega34^2)[L:H]^2\Omega_p^2}
 {\iota_p(d_j(p))^2}
\mathscr K_{p,\mathfrak c}(\nu_j)
\mathscr K_{p,\mathfrak c}(\beta_j),
\quad\mathfrak c=34\delta^2.}
\tag{32}
$$
全部固定微分、CM period 和 full trace 与 R1006 相同。
指定 Artin de Rham 基仍须再乘 R1006(57)的
$a_{j,p}^{-1}$；原射线上平方倍率为 $1/17$。

还可直接消掉已知的 companion Euler。R1002(7)给固定非零
代数数 $\gamma_j=L(\beta_j,1)/\Omega$，并给
$$
\mathscr K_{p,\mathfrak c}(\beta_j)
=\Omega_p\,\iota_p(\gamma_j)
\left(1-\iota_p(\beta_j(\bar{\mathfrak p})^{-1})\right)^2.
$$
所以(32)等价于
$$
\boxed{
(\mathcal J^0_{j,p})^2
=\iota_p(-486\omega34^2\gamma_j)[L:H]^2\Omega_p^3
\frac{\mathscr K_{p,\mathfrak c}(\nu_j)}
 {\left(1-\iota_p(\nu_j(\mathfrak p)/p)\right)^2}.}
\tag{33}
$$
此处 $\gamma_j$ 使用 R1002 的 raw $\Omega$ 约定，不另添
$2\pi i$ 或任何无穷处因子；$\Omega_p^3$ 来自原(32)的平方
周期与 companion 的一次周期。

由 R1002 与(29)，对所有上述好分裂 $p$
$$
\boxed{\mathcal J^0_{j,p}\ne0
\quad\Longleftrightarrow\quad
\mathscr K_{p,\mathfrak c}(\nu_j)\ne0.}
\tag{34}
$$
因此原跨 $p$ 门槛现在确实位于**同一个**固定未 depletion
循环 $Y_{j,0}$，无需随 $p$ 重选一个新的 motivic 输入。

在 $p_*=7993$，R1009§1已经用 R817(23)→R806(33)→
R1002→R1006 严格得到
$\operatorname{AJ}_{p_*}(Y_{j,p_*}^{[p_*]})\ne0$。
由(27)–(29)
$$
\boxed{\operatorname{AJ}_{p_*}(Y_{j,0})\ne0
\qquad(j=4,10,16).}
\tag{35}
$$
R1009 固定的循环恰是 $d_j(p_*)Y_{j,0}$，两个非零扩张只差
核线上一个非零标量。因此其实际幺幂 Lie 模和1-motive
张量范畴排除也适用于 $Y_{j,0}$，无需重作7993计算。

式(34)仍不推其它 $p$ 非零；R1009 的兼容系统盲区仍存在。
本篇的推进是移除了“来源循环随 $p$ 改变”的额外问题，给出
一个可供真正混合 CM 比较定理直接使用的固定原最高类。

## 来源及范围

- R991、R995：实际 $S$、完整有限角色及严格 Chow projectors。
- R997(28)–(34)：canonical CM 商、实际三个图的次数、原
  $p^{-2}$ 系数和单线转置方向。
- R1002(7)、(13)、(16)：原 $\nu_j$、新 $\beta_j$、primitive
  Euler 和相同周期规范。
- R1006(13)–(20)、(23)–(28)、(52)–(57)：实际 full9 分量、
  54图、算术 Artin、CM Tate 作用及原 $P_-$ 平方公式。
- R817、R1009§1：唯一7993检测及已固定的实际最高扩张。

本文使用的 CM 主定理和 Chow $h_1$ 对应规范均为上述已支付
输入；其余(11)–(33)由商的泛性质、有限平坦 pullback、椭圆
曲线 Picard 群和完整有限群和逐项证明。没有新增数学程序运行，
没有重跑7993，也没有对原v9另启重复作业。
