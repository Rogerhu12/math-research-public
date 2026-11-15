# R656 — 同一整数 jet 证书的四次高度与保留全部例外的九格强制非整

日期：2026-11-15。**状态：已证明。**

R658 已把 R644 原五来源辅助空间的真实 jet 最大行号降到二次量。
本篇用 R652 的**同一个**正则整微分系统和确定选行规则，把原整数证书的对数高度同步降为
$O(D^4\log(D+1))$。证书的分子坏素数全部保留。

随后在 R581 的同一个九坐标格、全部真实饱和层上求和，证明这些坏素数不能吸收所有大惰性素位的非整现象：
对任意固定 $C>0$ 和 $4<\vartheta<7$，每个充分大 $D$ 都有
$p>CD^\vartheta$、$p\nmid A_D$ 及一个真实非整 jet。
这仍不是原中央非零；最后明确写出尚缺的实际传播。

## 1. 原空间、确定行与同一个整数

保持 R644/R652 的 $b=17$、$u=x^{-1/2}$、$h=\sigma/z$，令
$$
K=66D,\qquad M=72D,\qquad d_*=K+2M=210D,\qquad
N_D^*=K(M+1).
\tag{1}
$$
原辅助列始终为
$$
B_{a,\beta,m}(u)=u^Kx(u)^ay(u)^\beta h(z(u))^m,
$$
$$
\beta\in\{0,1\},\quad2a+3\beta\le K,\quad0\le m\le M.
\tag{2}
$$
取 $q_D$ 为大于 $\max(72D,101)$ 的最小素数 $5\bmod6$，置
$$
J_D^\sharp=K+M(q_D+1),\qquad
L_D=J_D^\sharp+M=K+M(q_D+2).
\tag{3}
$$
R658 已证明 (2) 在原连续行 $0,\ldots,J_D^\sharp$ 上满列秩，并付清所有原 $H=z/u$、sigma 和椭圆因子高尾。
固定模数六的素数定理给
$$
q_D=(72+o(1))D,\qquad J_D^\sharp,L_D=(5184+o(1))D^2.
\tag{4}
$$
无需某个增长模数或未付的短区间结论。

使用 R652 的整向量场及原初值
$$
\mathscr V=R^3\partial_U+3bU^5R^2\partial_R+3bU^4\partial_V
 +(VR^2-bU^5R)A\partial_A+R^2\partial_Z,\qquad
q_0=(0,1,0,1,0).
\tag{5}
$$
准确换时是
$$
\tau(U)=\int_0^U(1+bt^6)^{-3/2}dt,\qquad
U=\tau+O(\tau^2),\quad Z=\tau+O(\tau^2).
$$
对每个 (2) 定义同一整单项式
$$
P_{a,\beta,m}
=(-1)^\beta U^{K-2a-3\beta+m}R^\beta A^m Z^{M-m},
\quad \deg P_{a,\beta,m}\le d_*.
\tag{6}
$$
沿原轨迹准确有
$$
C_{a,\beta,m}(\tau):=\tau^{-M}P_{a,\beta,m}(q(\tau))
=\left(\frac{Z(\tau)}{\tau}\right)^M B_{a,\beta,m}(U(\tau)).
\tag{7}
$$
共同因子与换时的切线均为一，故 (7) 的连续前缀也在
$0,\ldots,J_D^\sharp$ 上满列秩。

按 $n=0,1,2,\ldots$ 对 (7) 的有理系数矩阵逐行消元，只保留提高秩的行，在满列秩时停止；设所选行号为
$n_1,\ldots,n_{N_D^*}$。这正是 R652 的规则，没有另选一个随最终素数 $p$ 变化的子式。由 R658，
$$
n_i\le J_D^\sharp,\qquad n_i+M\le L_D.
\tag{8}
$$
于是原整数
$$
\boxed{
A_D=\det\bigl((\mathscr V^{\,n_i+M}P_{a,\beta,m})(q_0)\bigr)
\in\mathbf Z\setminus\{0\}
}
\tag{9}
$$
仍是 R652 的同一个 $A_D$。
行因子 $(n_i+M)!$ 非零，故其非零性由 (7) 的满秩给出。
所有构造只用有理运算和整多项式微分，因而是确定、有效的；不需要实际展开一个巨大矩阵才使定理成立。

## 2. 四次对数高度及真正的整 jet 运输

(5) 的每个分量的系数 $\ell^1$ 范数至多 $51$，总次数至多七。
因此
$$
\|\mathscr VP\|_1\le51\deg(P)\|P\|_1,\qquad
\deg(\mathscr VP)\le\deg(P)+6.
$$
(6) 各有系数范数一，初值的每个坐标绝对值不超过一。
对每个 $0\le k\le L_D$，
$$
|(\mathscr V^kP_{a,\beta,m})(q_0)|
\le51^k\prod_{j=0}^{k-1}(d_*+6j)
\le\{51(d_*+6L_D)\}^{L_D}.
\tag{10}
$$
Hadamard 不等式给
$$
\boxed{
\log|A_D|\le H_D^\sharp:=
\frac{N_D^*}{2}\log N_D^*
+N_D^*L_D\log\!\bigl(51(d_*+6L_D)\bigr)
=O(D^4\log(D+1)).
}
\tag{11}
$$
$|A_D|=1$ 时左边为零。显示界 (11) 只用 (3) 的明确辅助素数；渐近记号只用于说明增长次数。

若最终好惰性素数满足
$$
p>L_D,\qquad p\nmid A_D,
\tag{12}
$$
则 (9) 中所有阶乘在 $p$ 处都是单位。故 (7) 的完整有限 jet 含一个整单位子式。

这里还须回到原参数，不能以特征零可逆代替整可逆。
$\tau(U)$ 的第 $6j+1$ 个系数是
$\binom{-3/2}{j}b^j/(6j+1)$；所需次数小于 $p$，故在 $p$ 处整，切线为一，其同阶逆亦整。
(5) 的整递推使 $U(\tau)$、$Z(\tau)$ 到所需 $L_D$ 阶的系数仅有相应阶乘分母，因此也整。
于是 (7) 在 $0,\ldots,J_D^\sharp$ 的整个原 Taylor 前缀上是整可逆的下三角行变换。

R644 的原 $T_{\rm g}$ 规范满足
$$
B^{(p)}_{a,\beta,m}(u)\in\mathcal O[[u]],\qquad
B^{(p)}_{a,\beta,m}-B_{a,\beta,m}\in u^{p+1}K_p[[u]].
$$
因为 $J_D^\sharp<p$，这些前缀逐项相同。
因此 R644 的原 Gauss 最大项论证与全部 $p^2-1$ 个边界简单零点给：

**定理 1。** 对 (12) 的全部 $p$，
$$
\boxed{
\mathcal A_{D,p}\cap\mathbf C_p\langle z/R_E\rangle=\mathbf C_p,
}
\tag{13}
$$
其中 $\mathcal A_{D,p}$ 是 R644 的整个原五来源 degree$\le D$ 多项式空间，允许系数依赖 $p$，保全部原代数关系。
这没有改用 $\tau$ 作算术参数。

特别本篇缩小的是 R652 所需长度及同一证书的已付高度；
(12) 中 $p\nmid A_D$ 没有被省略。

## 3. 所有大坏素数的准确成本

对任意实数 $X\ge2$，定义真实有限例外集
$$
\mathcal E_D(X)=\{p:X<p,\ p\mid A_D\}.
$$
(11) 给
$$
\boxed{
\sum_{p\in\mathcal E_D(X)}
\frac{v_p(A_D)\log p}{p}
\le\frac{\log|A_D|}{X}
\le\frac{H_D^\sharp}{X}.
}
\tag{14}
$$
这是整数分解的直接不等式，保留了所有坏素数及其重数。
仅限制到好惰性素数仍成立。

现在回到 R581 的原九坐标格。
其全部好惰性素位、全部 $D,k\ge1$ 的实际算子范数满足
$$
\log\|\varphi_D^k\|_p
\le
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor\log p+
\Gamma_p(6k,\min(D,k))\log p,
$$
$$
\Gamma_p(n,K)=\sum_{a\ge1}
\min\!\left(K,\left\lfloor n/p^a\right\rfloor\right).
\tag{15}
$$
此处 $\varphi_D^k$ 是原单项式格的真实饱和前缀 quotient 上的 jet，不是辅助空间 (2) 的评价。

对每个 $p\ge2$，
$$
\frac{6p}{p^2-1}\le\frac8p,\qquad
\Gamma_p(6k,\min(D,k))
\le\frac{6k}{p-1}\le\frac{12k}{p}.
$$
因此在全部例外素数上，
$$
\boxed{
\sum_{\substack{p\in\mathcal E_D(X)\\p\ {\rm good\ inert}}}
\log\|\varphi_D^k\|_p
\le\frac{20kH_D^\sharp}{X}.
}
\tag{16}
$$
若某项实际为负，此式仍是合法上界；没有将其改为一个虚构的非负贡献。
这同时支付所有 $k$，并保留短积分分母的全部 $p^a$ 项。
不需要把例外集合视为固定坏集，也没有把它的素数个数当作固定常数。

## 4. 原九格的大素位非整仍不能被这些例外吸收

继续使用 R581 的原九坐标
$$
\mathbf G=(S,T,V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5})
$$
及同一源格
$$
E_D=\bigoplus_{|\mathbf a|\le D}\mathbf Z\mathbf X^{\mathbf a},
\qquad N_D=\binom{D+9}{9}.
\tag{17}
$$
全部前缀、有限位最大系数范数、实位 Euclidean 范数及固定坏集不变。
九者的代数独立保证恰有 $N_D$ 个秩一跳跃
$$
0=k_1<k_2<\cdots<k_{N_D},\qquad k_i\ge i-1.
$$
R581 的同格饱和恒等式为
$$
\sum_{i=1}^{N_D}
\left(\log\|\varphi_D^{k_i}\|_\infty+
\sum_p\log\|\varphi_D^{k_i}\|_p\right)=0.
\tag{18}
$$

固定 $C>0$、$4<\vartheta<7$，置
$X_D=\max(2,CD^\vartheta)$。
假设对某个 $D$ 有
$$
\|\varphi_D^k\|_p\le1
\quad\text{对全部 }k\ge1
\text{ 和全部好惰性 }p>X_D,\ p\nmid A_D.
\tag{19}
$$
R581 对 $p\le X_D$ 的准确截断分母界为
$$
\sum_{\substack{p\le X_D\\p\ {\rm good\ inert}}}
\log\|\varphi_D^k\|_p
\le3k\log X_D+O(k+DX_D).
$$
对剩下的 $p>X_D,p\mid A_D$ 使用 (16)，对 (19) 的素位保留非正贡献。
结合原全部普通位、固定坏位与复侧估计，得到
$$
\begin{aligned}
\log\|\varphi_D^k\|_\infty+
\sum_p\log\|\varphi_D^k\|_p
\le{}&-3k\log k+(6+3\vartheta)k\log D\\
&+O(k+D+D^{\vartheta+1})
+\frac{20kH_D^\sharp}{X_D}.
\end{aligned}
\tag{20}
$$
所有常数只依赖固定 $C,\vartheta$ 和原格，与 $D,k$ 无关。

由 $\vartheta>4$ 和 (11)，
$$
\frac{H_D^\sharp}{X_D}
=O(D^{4-\vartheta}\log(D+1))=o(\log D).
$$
选任意固定
$$
0<\varepsilon<3(7-\vartheta).
$$
当 $D$ 充分大时，(20) 最后一项不超过
$\varepsilon k\log D$。因此把
$$
G_D(t)=-3t\log t+
(6+3\vartheta+\varepsilon)t\log D+O(t)
$$
中的 $O(t)$ 固定为同一个上界，可得
$$
\sup_{t\ge0}G_D(t)
=O(D^{\vartheta+2+\varepsilon/3}),\qquad
\vartheta+2+\varepsilon/3<9.
\tag{21}
$$
前半跳跃的总贡献至多
$O(N_DD^{\vartheta+2+\varepsilon/3})=o(N_D^2)$。
后半跳跃满足 $k_i\ge N_D/2-1\gg D^9$，
故其 $G_D(k_i)$ 的总和至多
$$
-cN_D^2\log D
$$
其中 $c>0$ 与 $D$ 无关。
(20) 其余附加项在全部层上的和为
$$
O\!\left(N_D(D+D^{\vartheta+1})\right)=o(N_D^2),
$$
因为 $\vartheta+1<8<9$。
常数层为零；全部早期跳跃与任意大的真实接触阶均已支付。
于是 (18) 的右边严格小于零，矛盾。

得到无条件结论：

**定理 2。** 对任意固定 $C>0$、$4<\vartheta<7$，
每个充分大的 $D$ 都有
$$
\boxed{
p\equiv5\pmod6,\quad p\notin\mathcal S,\quad
p>CD^\vartheta,\quad p\nmid A_D,\quad
\|\varphi_D^k\|_p>1
}
\tag{22}
$$
对某个实际秩一跳跃 $k$ 成立。
可在同一个全局整数格中取原始 quotient 生成元的提升
$P\in E_D$，使
$$
[w^j]P(\mathbf G(w))=0\quad(j<k),\qquad
v_p([w^k]P(\mathbf G(w)))<0.
\tag{23}
$$
R581 的短分母包络还给
$$
k\ge(p+1)/6.
\tag{24}
$$

因为 $L_D=O(D^2)$ 而 $\vartheta>4$，
(22) 的 $p$ 对充分大 $D$ 同时满足 (12)，所以也是原五来源闭边界结论 (13) 的一个合法素位。
这里陈述两个同一素位的结论，没有将九格的 (23) 与五来源的 (13) 认成同一个函数。

## 5. 准确的新接口与尚缺的算术传播

(16)–(22) 说明：R644/R652 整数子式的有限分子例外即使随 $D$ 增长，也不能把 R581 的全部大惰性非整现象容纳进去。
所以若某个后续原算术论证只在
$$
p>CD^\vartheta,\quad p\nmid A_D,\qquad4<\vartheta<7
$$
证明原九格的所有真实层整，仍足以与定理 2 矛盾。
不必先删除这些例外或把它们归入一个固定集合。

但是本篇没有证明原完整中央失败
$J'_S(0)=J'_T(0)=0$ 会蕴含 (19)。
R639 所付的是每个严格 $R<R_E$ 盘上的正规零初值解；
R644/R658/(13) 使用的是闭 $R_E$ Tate 条件。
也没有给七原函数的全部任意乘积新增中央零。

因此实际中央到全部九格真层的传播、旧十九角/帽/同一个 $R$ 的第二余类，以及全部普通补域仍保持原量词。
(22) 给无穷个适用于 (13) 的好惰性素位及真实非整层，不给固定曲线的 $\Sha[p^\infty]$ 有限性。
主目标尚未完成。

依赖：
[R658](R658-original-auxiliary-gaussian-minor-and-quadratic-jet-bound.md)；
[R652](R652-original-regular-polynomial-flow-and-quantitative-jet-bound.md)；
[R644](R644-bounded-degree-original-polynomials-and-full-boundary-obstruction.md)；
[R581](R581-nine-coordinate-truncated-denominators-and-forced-large-inert-jets.md)；
[R579](R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md)；
[R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)。
