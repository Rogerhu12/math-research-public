# R150 附录：完全去中心的临界幂、真实梯度尾相消与非零参数的全部指数权

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：已证明。

本稿接续[增长头与临界幂稿](R150-appendix-growing-head-multiscale-columns-and-critical-power-bell-units.md)，处理该稿保留的完全去中心分支。结论覆盖全部非零谱参数、全部固定点态幂和任意复第一阶指数权；零参数仍不由本稿排除。

关键有两项。第一，真实线性梯度的尾发生额外相消。第二，完整 Bell 系数的有限头保留显式 $N_j$ 因子，而其补集在所需对数幂放大后仍趋零。因此不必将零字符 Bell 常数误当成有界单位。

## 1. 原行、固定常数与结论

固定整数 $k\ge2$，令
$$
a_j=\frac1{j+2},\qquad
b_j=\frac1{k(j+2)(\log(j+2))^{\,1-1/k}}.
\tag{1.1}
$$
两行均属于 $\ell^2\setminus\ell^1$。置
$$
T_n=(\log(n+2))^{1/k}.
$$
积分比较给固定实常数 $\kappa_a,\kappa_b$，使
$$
\sum_{j<n}a_j=T_n^k+\kappa_a+O(n^{-1}),\qquad
\sum_{j<n}b_j=T_n+\kappa_b+
O((nT_n^{k-1})^{-1}).
\tag{1.2}
$$
这里的常数来自求和与积分之差的收敛，误差不超过相应递减被积函数在第 $n$ 位的常数倍。

取固定原函数
$$
\boxed{
u=-\kappa_a+\sum_ja_j\chi_j,\qquad
z=-\kappa_b+\sum_jb_j\chi_j,
}
\tag{1.3}
$$
及其实际 first $X=X_u$、$Y=X_z$。前 $n$ 个物理位的准确中心是
$$
s_{1n}=T_n^k+O(n^{-1}),\qquad
s_{2n}=T_n+O((nT_n^{k-1})^{-1}),
\tag{1.4}
$$
所以
$$
q_n=s_{2n}^k-s_{1n}=O(n^{-1})\to0.
\tag{1.5}
$$
原函数的常数不随 $n$ 改动。

**定理 1。** 对每个 $\lambda\in\mathbb C\setminus\{0\}$、整数 $r\ge1$ 和任意
$$
w=w_*+\sum_jw_j\chi_j,\qquad (w_j)\in\ell^2,
$$
都有
$$
\boxed{[z^k-u-\lambda]^r e^w\text{ 对实际 }A\text{ 循环}.}
\tag{1.6}
$$

证明只在已付的原共同深词域和整个有限柱上运算，不把某个自然无界差的定义域默认等同于两个最大定义域的交。

## 2. 两个实际变化方向与梯度尾相消

下文略写 $T=T_n$，并在原共同深域上定义
$$
U_n=(X-s_{1n})-kT^{k-1}(Y-s_{2n}),\qquad
V_n=T^{(k-2)/2}(Y-s_{2n}).
\tag{2.1}
$$
这些是实际有限线性组合。每个固定 $n$ 的有限词恒等式由 R186 的同一共同正则器及 R251 的全柱域支付；无需声明其自然差在最大交域上已经闭。

置 $h_n=T^{-(k-2)/2}$，则
$$
Y=s_{2n}+h_nV_n,\qquad
X=s_{1n}+U_n+kT^{k/2}V_n.
\tag{2.2}
$$
因此原标量多项式在两个形式变量中的准确改写为
$$
\begin{aligned}
\mathcal Q_n(U,V)
&=(s_{2n}+h_nV)^k-(s_{1n}+U+kT^{k/2}V)-\lambda\\
&=q_n-\lambda-U
+k(s_{2n}^{k-1}-T^{k-1})h_nV
+\sum_{j=2}^k\binom kj s_{2n}^{k-j}h_n^jV^j.
\end{aligned}
\tag{2.3}
$$
其一次 $V$ 系数是 $O((nT^{k/2})^{-1})$；第 $j\ge2$ 次系数为
$O(T^{k(1-j/2)})$。故逐系数有
$$
\boxed{\mathcal Q_n(U,V)\longrightarrow-\lambda-U+\binom{k}{2}V^2.}
\tag{2.4}
$$
特别，固定 $r$ 时 $\mathcal Q_n^r$ 的全部系数一致有界，其常数趋于 $(-\lambda)^r$。

令 $F_n=\{0,\ldots,n-1\}$。$U_n$ 的补集行是
$$
d_j(n)=a_j-kT^{k-1}b_j
=\frac1{j+2}\left[
1-\left(\frac{\log(n+2)}{\log(j+2)}\right)^{(k-1)/k}
\right],\qquad j\ge n.
\tag{2.5}
$$
利用 $1-(1+x)^{-\alpha}\le\alpha x$（$x\ge0,\ 0<\alpha<1$），
$$
|d_j(n)|\le
\frac{C}{(j+2)\log(n+2)}
\log\frac{j+2}{n+2}.
$$
又
$$
\sum_{j\ge n}\frac{\log^2((j+2)/(n+2))}{(j+2)^2}
=O(n^{-1}),
$$
可由二进区间求和或 $\int_1^\infty t^{-2}\log^2t\,dt=2$ 得到。因此
$$
g_{U,n}:=\|d_{\ge n}(n)\|_2
=O((\sqrt n\,T^k)^{-1}).
\tag{2.6}
$$
$V_n$ 的补集行为 $T^{(k-2)/2}b_j$，直接积分比较给
$$
g_{V,n}=O((\sqrt n\,T^{k/2})^{-1}).
\tag{2.7}
$$
所以两个实际补集方向的总预算满足
$$
\boxed{
\varepsilon_n=g_{U,n}+g_{V,n}
=O((\sqrt n\,T^{k/2})^{-1})
=O((n\log(n+2))^{-1/2}).
}
\tag{2.8}
$$

两方向有限头的绝对系数和分别不超过
$$
\sum_{j<n}|a_j-kT^{k-1}b_j|=O(T^k),\qquad
T^{(k-2)/2}\sum_{j<n}b_j=O(T^{k/2}).
\tag{2.9}
$$
这里保留了真实梯度行；若只分别估计 $X$、$Y$ 的尾再相加，就失去 (2.6)。

## 3. 带任意交换有界因子的真实有限头

以下直接延伸 [R251 §2](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) 的实际进位估计。

设固定有限个头字母为
$$
H_{\ell n}=\sum_{j<n}N_j B_{\ell j,n},
\qquad B_{\ell j,n}\in A',
\qquad
A_n\ge\max\left(1,\sum_{\ell,j<n}\|B_{\ell j,n}\|\right).
\tag{3.1}
$$
所有实际有界因子彼此交换。允许 $B_{\ell j,n}$ 随 $n$ 变化，且不要求它们在物理上只作用于前 $n$ 位。

任意总长度 $h$ 的混合头词满足
$$
\|H_{\ell_1n}\cdots H_{\ell_hn}\|\le A_n^h.
\tag{3.2}
$$
若 $h\ge\max(2n,16)$，则进一步有
$$
\boxed{
\|H_{\ell_1n}\cdots H_{\ell_hn}\|
\le A_n^h e^{-\gamma h^4},
\qquad \gamma=770/16^4.
}
\tag{3.3}
$$

证明时逐项展开，利用交换性将所有 $B$ 因子移开。每个实际 $N_j$ 产品仍准确满足
$$
N_j^2=\eta_jN_{j+1},\qquad \eta_j\le e^{-770\,16^j},
\qquad \|N_j\|\le1.
$$
R251 的进位计数本来就是对这个 $N$ 产品给出的：
总进位至少 $(h-n)/2$，且当 $h\ge2n$ 时，
$\sum_j16^jc_j\ge(h/16)^4$。
因此该产品的范数至多 $e^{-\gamma h^4}$。
对剩余因子只用 $\prod\|B\|$ 并求和，得到 (3.3)。
各 $B$ 的物理尾不会取消这个已经显式保留的 $N_j$ 因子。

(3.2)—(3.3) 对伴随头词同样成立。
由 $V_j-I=-2N_j(I+N_j)^{-1}$、$\|(I+N_j)^{-1}\|\le3$，
(2.9) 的两个实际头恰属于 (3.1)。

## 4. 完整 Bell 对数与真正的 $N_j$ 商

记
$$
H(\xi,V)=e^{-\xi V}(\cosh\xi\,I+V\sinh\xi),\qquad
L_j(\xi)=\log H(\xi,V_j),
$$
并用字符为零的规范对数。令
$$
B_w=\prod_jH(w_j,V_j),\qquad
\mathcal B_w(s,t)=
\prod_jH(w_j+sa_j+tb_j,V_j)H(w_j,V_j)^{-1}.
\tag{4.1}
$$
这些是实际交换算子。把 $w$ 加为 R145 的第三个真实模式并在其参数1处取值，已付
$$
\xi_w=B_w^{-1}e^w
$$
的全部原 $X,Y$ 混合域、循环性和原指数图核心。

### 4.1 一阶导数的额外 $w_j$ 因子

[R154 §3](R154-supercubic-modes-all-polynomials-exponential-weights.md) 给每个固定 $h\ge1$ 的真实商
$$
L_j^{(h)}(w_j)=N_j U_{hj},\qquad
\sup_j\|U_{hj}\|<\infty.
\tag{4.2}
$$
它由实际参数积分与 Cauchy 估计构造，不能只由字符为零推出。

本稿还需要一阶的加强：
$$
\boxed{
L_j'(w_j)=w_jN_jW_j,\qquad \sup_j\|W_j\|<\infty.
}
\tag{4.3}
$$
对高位，R154 的同一小圆盘计算给 $L_j''(\xi)=N_jU_{2j}(\xi)$，
其中商在固定小圆盘内一致有界。
因为 $L_j'(0)=0$，对线段积分即得
$$
L_j'(w_j)
=w_jN_j\int_0^1U_{2j}(\tau w_j)\,d\tau.
$$
所有充分高的 $w_j$ 都落在该圆盘中。
余下有限低位，当 $w_j\ne0$ 时用 (4.2) 的真实商除以这个非零标量；
当 $w_j=0$ 时取 $W_j=0$。有限次取最大值得到 (4.3)。
商仍属于实际 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。

### 4.2 不可和两行的对数求和

这里的 $a,b$ 不可和，不能直接借 R154 快模式部分的 $\ell^1$ 收敛论证。
高位统一小圆盘上，由 $L_j'(0)=0$ 和二阶导数界，
$$
\|L_j(w_j+\xi)-L_j(w_j)\|
\le C(|w_j||\xi|+|\xi|^2).
$$
令 $\xi=sa_j+tb_j$。两行和 $w$ 都在 $\ell^2$，
所以右侧在固定小参数闭盘上可和。
有限低位分别取共同小邻域。因此局部一致绝对范数收敛地有
$$
\log\mathcal B_w(s,t)
=\sum_j[L_j(w_j+sa_j+tb_j)-L_j(w_j)].
\tag{4.4}
$$
可以逐项求任意固定阶参数导数。

对 $\delta=(i,j)\ne(0,0)$、$h=i+j$，置
$$
\kappa_\delta
=\partial_s^i\partial_t^j\log\mathcal B_w(0,0).
$$
则
$$
\kappa_{ij}=\sum_{\ell\ge0}a_\ell^i b_\ell^j
L_\ell^{(h)}(w_\ell).
\tag{4.5}
$$
当 $h\ge2$ 时，使用 (4.2)；当 $h=1$ 时，使用 (4.3)。
故每个 $\kappa_\delta$ 都是带显式 $N_\ell$ 因子的绝对范数收敛和。
一阶的绝对系数和用 $\sum |a_\ell w_\ell|$ 或
$\sum |b_\ell w_\ell|$ 的 Cauchy–Schwarz 界支付。

完整 Bell 系数
$$
C_\alpha^w=\partial^\alpha\mathcal B_w(0,0),\qquad C_0^w=I,
$$
对每个 $\alpha\ne0$，都是有限个 $\kappa_\delta$ 的固定有限多项式，
且没有常数项。这是 $\exp(\log\mathcal B_w)$ 的有限阶 Leibniz 公式。

## 5. 放大累积量的有限头与小补集

固定 $\lambda\ne0,r,w$，令
$$
K(x,y)=(y^k-x-\lambda)^r,\qquad D=kr,\qquad M=D.
$$
只需使用 $1\le|\delta|\le D$ 的有限个累积量。对每个这样的 $\delta$，按真实物理前缀拆分
$$
\boxed{T^M\kappa_\delta=H_{\delta n}+E_{\delta n}.}
\tag{5.1}
$$
由 (4.5)、(4.2)—(4.3)，有限头有真实表示
$$
H_{\delta n}=\sum_{\ell<n}N_\ell B_{\delta\ell,n},
\qquad
\sum_{\delta,\ell<n}\|B_{\delta\ell,n}\|\le C T^M.
\tag{5.2}
$$

对 $|\delta|\ge2$，因 $a_\ell,b_\ell\le C/(\ell+2)$，
补集绝对系数和为 $O(n^{-1})$。对 $|\delta|=1$，(4.3) 和
Cauchy–Schwarz 给 $O(n^{-1/2}\|w_{\ge n}\|_2)$。
因此
$$
\boxed{
\max_{1\le|\delta|\le D}\|E_{\delta n}\|
\le C T^M\left(n^{-1}+n^{-1/2}\|w_{\ge n}\|_2\right)\to0.
}
\tag{5.3}
$$
任意固定对数幂都小于这里的 $\sqrt n$；不要求 $w$ 的尾具有额外速度。
全部 $H_{\delta n}$、$E_{\delta n}$ 属于实际 $\mathcal A$，保持每个所用的原混合词域。

完整原 Bell 多项式是
$$
P_K(X,Y)=
\sum_{\alpha}\frac{C_\alpha^w}{\alpha!}
(\partial^\alpha K)(X,Y).
\tag{5.4}
$$
把 (2.2) 代入，作有限多项式系数比较：

- $\alpha=0$ 项准确为 $\mathcal Q_n(U,V)^r$，由 (2.4) 系数一致有界；
- 对任意 $\alpha$，$(\partial^\alpha K)(s_1+U+kT^{k/2}V,s_2+h_nV)$
  的每个系数为 $O(T^{kr})$。

第二点只用原 $K$ 的权次数：赋 $x$ 权 $k$、$y$ 权1，
所有单项式的权至多 $kr$；代入中 $x$ 的各系数为 $O(T^k)$，
$y$ 的各系数为 $O(T)$，固定阶偏导不增加该界。

对于 $\alpha\ne0$，$C_\alpha^w$ 的每个单项式含 $\ell\ge1$ 个累积量。
使用 (5.1) 把每个 $\kappa_\delta$ 替换为
$T^{-M}(H_{\delta n}+E_{\delta n})$ 后，其数值系数最多是
$$
C T^{kr-M\ell}\le C.
\tag{5.5}
$$
因此 (5.4) 已成为固定次数、固定个数字母的多项式，所有标量系数一致有界；
字母是 $U_n,V_n$、有限个实际头 $H_{\delta n}$ 和小有界算子 $E_{\delta n}$。
这一改写准确保留每个完整 Bell 修正。

将 $E_{\delta n}$ 吸收进有界交换系数；它们的一致小范数保证这些系数仍一致有界。
再将 $U_n,V_n$ 分成各自实际有限头与补集 first。
由 (2.9)、(5.2)，所有显式头字母共同满足 §3，且可取
$$
\boxed{A_n\le C T^{kr}.}
\tag{5.6}
$$
两个无界补集字母的总行范数是 (2.8) 的 $\varepsilon_n$。

若把全部显式头字母及无界补集字母形式上置零，则 (5.4) 的常数系数为
$$
\boxed{(q_n-\lambda)^rI+o(1)\longrightarrow(-\lambda)^rI.}
\tag{5.7}
$$
理由是每个 Bell 修正都含至少一个 $H_{\delta n}$ 或 $E_{\delta n}$；
置零后只剩含至少一个 $E_{\delta n}$ 的项，(5.3)、(5.5) 使其范数趋零。
这里没有声称原 Bell 常数本身为零或可逆。

## 6. 小算子常数、增长头与真实全柱根界

令 $Q_n=Q_{F_n}$ 为实际前 $n$ 位的整柱投影。
[R251 §3](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md)
的同一补集次数尺度适用于 (2.5)、(2.7) 的两个补集行：
任何总长度 $j$ 的混合补集自然词，在整个 $Q_nH$ 上都有界，并满足
$$
\|\text{该混合词}\,Q_n\|\le(C\varepsilon_n\sqrt j)^j.
\tag{6.1}
$$
这是共同尺度上的逐步估计，亦支付所有需要的迭代定义域；
无需逐词引入一个不同的图闭包。
其伴随版本由原 $C$ 对称结构与 $CQ_n=Q_nC$ 得到。

设 $\mathscr T_n$ 是上述伴随头、伴随补集字母的一个固定次数多项式，
全部有界交换系数一致有界，其算子常数项为 $\Delta_{0n}$，
并且 $\|\Delta_{0n}\|\to0$。
每个系数保持全部实际伴随词域。假设头预算为 (5.6)、尾预算为 (2.8)。
取显式整数
$$
\boxed{p_n=\lceil nT^{k/2}\rceil.}
\tag{6.2}
$$
则
$$
p_n/n\to\infty,\qquad
\varepsilon_n\sqrt{p_n}=O(T^{-k/4})\to0,\qquad
(n/p_n)\log A_n=O(T^{-k/2}\log T)\to0.
\tag{6.3}
$$

令 $D'$ 为一个固定的展开次数上界，置
$$
\Delta_n=A_n e^{-\gamma(2n)^3}\to0,\qquad
E_n=\|\Delta_{0n}\|+C\varepsilon_n\sqrt{D'p_n}\to0.
$$
在 $\mathscr T_n^{p_n}$ 的每个展开项中，把一个常数项
$\Delta_{0n}$ 也视为一个有界尾字母。
若头次数、无界尾次数、常数字母次数分别为 $h,j,c$，则
$$
p_n\le h+j+c\le D'p_n.
$$
固定次数和一致系数界使总系数成本不超过 $C_0^{p_n}$。

若 $h\ge2n$，由 §3，
头范数不超过 $\Delta_n^h$。配合 (6.1) 与小常数字母，
这部分总和不超过
$$
C_0^{p_n}(\Delta_n+E_n)^{p_n}
$$
（充分大时 $\Delta_n+E_n<1$）。
若 $h<2n$，则 $j+c\ge p_n-2n$，这部分不超过
$$
C_0^{p_n}A_n^{2n}E_n^{p_n-2n}.
$$
所有有界因子通过原交换关系移到真实尾词的左侧；只在原共同词域上进行，
从未要求这些因子保持补集的加权范数。

所以
$$
\boxed{
\|\mathscr T_n^{p_n}Q_n\|^{1/p_n}
\le C_0\left[
\Delta_n+E_n+
A_n^{2n/p_n}E_n^{\,1-2n/p_n}
\right]\to0.
}
\tag{6.4}
$$
当 $E_n=0$ 时，低头部分没有非零项，按零解释。

此处只要求 $\|\Delta_{0n}\|\to0$，不要求
$p_n\|\Delta_{0n}\|\to0$。小常数是逐因子计算的尾字母，不能用一个未经支付的长迭代误差代替它。

## 7. 准确作用于未知核与循环性

令 $\mathcal P_K$ 为完整原 Bell 多项式 (5.4) 的规范最大实现。
R186 已付其 $C$ 自伴性、原指数图核心，以及所有有界 $A'$ 系数
对全部原有限混合域的保持。

若 $\ker\mathcal P_K\ne0$，令 $\Pi$ 为其正交投影。
在原共同伴随深域上，准确有
$$
\Pi P_K^*=0.
\tag{7.1}
$$
取
$$
\boxed{\mathscr T_n=I-\frac{P_K^*}{(-\overline\lambda)^r}.}
\tag{7.2}
$$
按 §5 的真实变化字母展开，它的常数项由 (5.7) 趋于零；
其余全部系数一致有界，头尾预算正是 (5.6)、(2.8)。
故 (6.4) 适用。

每个整柱 $Q_nH$ 都属于原 first 的全部所需混合伴随词域；
固定 $n$ 时，各变化字母和系数保持这些域。
因此对有限整数 $p_n$ 可逐步迭代 (7.1)，得到
$$
\boxed{\Pi Q_n=\Pi\mathscr T_n^{p_n}Q_n.}
\tag{7.3}
$$
未知的 $\Pi$ 始终在左侧。
没有将 $n$ 依赖系数、有限头或 Bell 因子穿过 $\Pi$，
也没有要求它们与该正交投影交换。

由 (6.4)，右侧算子范数趋于零。
而 $Q_n\to I$ 强，故 $\Pi=0$，矛盾。
所以 $\ker\mathcal P_K=0$。

最后，原真实生成恒等式给
$$
[z^k-u-\lambda]^re^w=B_wP_K(X,Y)\xi_w.
$$
$C$ 自伴性使无核等价于稠密像，原指数图核心使
$P_K(X,Y)\xi_w$ 的多项式 $A$ 轨道在该像中稠密；
$B_w$ 是有界交换单位。因此目标向量循环，证明定理1。

## 8. 有限多项式推论与准确剩余

同一证明还给：任意标量多项式 $q$ 满足 $q(0)\ne0$ 时，
$$
\boxed{q(z^k-u)e^w\text{ 循环}.}
\tag{8.1}
$$
对非常数 $q$，取 $K(x,y)=q(y^k-x)$、$M=k\deg q$。
在 (2.3) 的有限标量恒等式中先取 $\lambda=0$，再复合 $q$，
所得基础多项式逐系数趋于 $q(-U+\binom{k}{2}V^2)$。
其常数趋于 $q(0)\ne0$，所有导数权次数和累积量预算完全相同，
(7.2) 的分母改为 $\overline{q(0)}$ 即可。
非零常数 $q$ 的结论由原指数循环性直接给出。
这不是由分别循环的向量相乘推出，而是对整个原多项式重新应用完整 Bell 证明。

可再加回任意固定线性混合 $v=\beta u+z$。
[多尺度稿 §5](R150-appendix-multiscale-column-budgets-bell-covariance-and-full-plane-joint-polynomials.md)
已付原生成函数的准确线性协变和规范图的双向识别，
所以 (1.6) 也可写成
$$
[(v-\beta u)^k-u-\lambda]^re^w\text{ 循环},
\qquad\lambda\ne0.
$$

本稿依赖真实梯度尾 (2.6)、全部 $N_j$ 商和 (5.3) 的完整 Bell 尾预算。
它没有把零字符因子当成有界单位，没有丢弃一阶指数项，
也没有把一般 $A'$ 当作一个局部代数。

对于完全去中心且 $\lambda=0$，(5.7) 的极限为零，
当前未知核测试缺少非零标量分母；本稿不据此声称该向量无核或循环。
一般更慢共振、任意向量循环性、真正常见证的源上界及普通复 Hilbert ISP 仍开放。

## 9. 所有合法梯度柱的完全居中值仍趋于零

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明。本节不扩大已证循环性范围。

本节保持固定整数 $k\ge2$ 和原两条正行
$$
a_j=\frac1{j+2},\qquad
b_j=\frac1{k(j+2)(\log(j+2))^{1-1/k}}.
$$
常数 $\kappa_a,\kappa_b$ 由原前缀求和唯一确定：
$$
\sum_{j<n}a_j=T_n^k+\kappa_a+O(n^{-1}),\qquad
\sum_{j<n}b_j=T_n+\kappa_b+O((nT_n^{k-1})^{-1}),
\quad T_n=(\log(n+2))^{1/k}.
$$
采用完全居中的同一原函数
$$
u=-\kappa_a+\sum_ja_j\chi_j,\qquad
z=-\kappa_b+\sum_jb_j\chi_j.
$$
对任意具有恰好 $n$ 个物理位的集合 $F$，写其实际中心
$$
s_u(F)=-\kappa_a+\sum_{j\in F}a_j,\qquad
s_z(F)=-\kappa_b+\sum_{j\in F}b_j.
$$
这里 $n=|F|$ 是实际位数，不是辅助排序指标。

定义变化的真实梯度行
$$
\omega_{n,j}=a_j-kT_n^{k-1}b_j
=\frac1{j+2}
\left[1-
\left(\frac{\log(n+2)}{\log(j+2)}\right)^{(k-1)/k}
\right].
$$

**命题。** 设 $F_\ell$ 为任意有限位集，$n_\ell=|F_\ell|\to\infty$。若
$$
\eta_\ell=\sqrt{n_\ell}\,
\|\omega_{n_\ell,F_\ell^c}\|_2\longrightarrow0,
\qquad
\theta_\ell=\sqrt{n_\ell}\,T_{n_\ell}^{(k-2)/2}
\|b_{F_\ell^c}\|_2\longrightarrow0,
\tag{B.1}
$$
则
$$
\boxed{s_z(F_\ell)^k-s_u(F_\ell)\longrightarrow0.}
\tag{B.2}
$$
这个结论不要求这些集合递增或穷尽；实际全柱应用另外保留原递增穷尽条件。

### 证明

省略 $\ell$，记 $I_n=\{0,\ldots,n-1\}$，并置
$$
M=I_n\setminus F,\qquad E=F\setminus I_n.
$$
两者位数相同且不超过 $n$。记 $\alpha=(k-1)/k$、$L=\log(n+2)$。

对 $j<n$，$\omega_{n,j}<0$；对 $j\ge n$，$\omega_{n,j}\ge0$。
在后一范围，置 $x=\log((j+2)/(n+2))\ge0$。由
$1-(1+y)^{-\alpha}\le\alpha y$，
$$
0\le\omega_{n,j}
=\frac{1-(1+x/L)^{-\alpha}}{(n+2)e^x}
\le\frac{\alpha x e^{-x}}{(n+2)L}
\le\frac{\alpha}{e(n+2)L}.
\tag{B.3}
$$
因此缺失与新增梯度总和分别满足
$$
\left|\sum_{j\in M}\omega_{n,j}\right|
\le\sqrt n\,\|\omega_{n,F^c}\|_2=\eta_\ell,
\qquad
0\le\sum_{j\in E}\omega_{n,j}
\le\frac{\alpha}{eL}.
\tag{B.4}
$$

令
$$
\Delta_b=s_z(F)-s_z(I_n),\qquad
\Delta_a=s_u(F)-s_u(I_n).
$$
$b_j$ 正且递减，$I_n$ 是前 $n$ 个最大项，所以
$$
\Delta_b=\sum_Eb_j-\sum_Mb_j\le0,\qquad
|\Delta_b|\le\sum_Mb_j
\le\sqrt n\,\|b_{F^c}\|_2
=\theta_\ell T_n^{-(k-2)/2}.
\tag{B.5}
$$
特别 $\Delta_b=o(1)$，包括 $k=2$。准确的线性中心差为
$$
kT_n^{k-1}\Delta_b-\Delta_a
=\sum_M\omega_{n,j}-\sum_E\omega_{n,j},
$$
故由 (B.4)
$$
|kT_n^{k-1}\Delta_b-\Delta_a|
\le\eta_\ell+\frac{\alpha}{eL}\longrightarrow0.
\tag{B.6}
$$

原前缀中心满足
$$
s_z(I_n)=T_n+e_n,\quad
e_n=O((nT_n^{k-1})^{-1}),\qquad
s_z(I_n)^k-s_u(I_n)=O(n^{-1}).
\tag{B.7}
$$
对固定次数 $k$ 作完整有限 Taylor 展开。因 $|\Delta_b|=o(1)$、$T_n\to\infty$，
$$
\begin{aligned}
&s_z(F)^k-s_u(F)
-\bigl[s_z(I_n)^k-s_u(I_n)\bigr]\\
&\qquad=kT_n^{k-1}\Delta_b-\Delta_a+\mathcal R_\ell,
\end{aligned}
$$
其中
$$
|\mathcal R_\ell|
\le C_k T_n^{k-2}|\Delta_b|^2
 +C_k T_n^{k-2}|e_n|\,|\Delta_b|
\le C_k\theta_\ell^2
 +O\!\left(\frac{|\Delta_b|}{nT_n}\right)
\longrightarrow0.
\tag{B.8}
$$
高于二阶的项由 $|\Delta_b|/T_n\to0$ 吸收到第一项；$k=2$ 时同一式直接成立。
合并 (B.6)—(B.8)，得到 (B.2)。证毕。

### 以该列自身中心选梯度也不能改变结论

实际使用时也可以令 $\tau_\ell=s_z(F_\ell)$，并直接假设
$$
\sqrt n\,\|a-k\tau_\ell^{k-1}b\|_{2,F_\ell^c}\to0,\qquad
\sqrt n\,|\tau_\ell|^{(k-2)/2}\|b_{F_\ell^c}\|_2\to0,
\tag{B.9}
$$
其中 $F_\ell$ 递增穷尽。正的不可和 $b$ 使 $\tau_\ell\to+\infty$。
第二式先给 $\sqrt n\|b_{F_\ell^c}\|_2\to0$，再由 (B.5)、(B.7) 得
$\tau_\ell=T_n+o(1)$，因此 $|\tau_\ell|/T_n\to1$，且 (B.1) 的第二式成立。

第一梯度的替换误差满足
$$
\begin{aligned}
&\sqrt n\,k|\tau_\ell^{k-1}-T_n^{k-1}|
\|b_{F_\ell^c}\|_2\\
&\quad\le C_k T_n^{k-2}
\bigl(|\Delta_b|+|e_n|\bigr)
\sqrt n\,\|b_{F_\ell^c}\|_2\\
&\quad\le C_k nT_n^{k-2}\|b_{F_\ell^c}\|_2^2+o(1)
\longrightarrow0.
\end{aligned}
$$
故 (B.1) 的第一式也成立，仍得 (B.2)。

### 准确范围

主稿增长头测试所需的对数尾预算，比 (B.1) 更强。因此在这些原两行不变、采用同一种梯度和二阶变化尺度的全柱族内，任意重新选择物理位都不能把完全居中零参数的标量中心改成一个非零极限。更不能仅凭允许任意有限位集，就把零参数并入已证的非零参数单位准则。

这只是一条该预算下的准确中心约束。不排除改变真实测试结构、使用更深尺度、原核上的额外关系，或另一种实际非零字符以外的排核方法；也没有声称零参数向量不循环。

## 10. 临界曲线附近的 Newton 度数范围与全部点态幂

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。
状态：已证明。

本节保持主稿完全去中心的同一对原函数 $u,z$、固定整数 $k\ge2$，
以及前缀中心 $s_{1n},s_{2n}$ 和 $T_n=(\log(n+2))^{1/k}$。
没有改动原常数，也没有改选一个具有不同非零中心的输入函数。

### 10.1. 原多项式的准确条件

写
$$
g(x,y)=y^k-x.
$$
因为 $(x,y)\mapsto(g,y)$ 是多项式坐标变换，
每个 $F\in\mathbb C[x,y]$ 都唯一写作
$$
\boxed{F(x,y)=\sum_{j=0}^{J}f_j(y)\,g(x,y)^j.}
\tag{N.1}
$$
要求
$$
f_0\ne0.
\tag{N.2}
$$
对非零 $f_j$，记 $\ell_j=\deg f_j$；略去为零的项。
假设
$$
\boxed{
\max_{\substack{j\ge1\\ f_j\ne0}}
\frac{\ell_j-\ell_0}{j}<k.
}
\tag{N.3}
$$
若没有 $j\ge1$ 的项，将最大值解释为 $-\infty$。

等价地，存在一个固定实数 $s$，使
$$
\boxed{
0\le s<k,\qquad \ell_j-sj\le\ell_0
\quad\text{对所有非零 }f_j.
}
\tag{N.4}
$$
$s$ 不必为整数；它只用于实际正实缩放 $T_n^s$，不涉及无界算子的分数幂。

**定理。** 在 (N.2)—(N.3) 下，对全部整数 $r\ge1$ 和全部复
$\ell^2$ 第一阶指数 $w$，
$$
\boxed{F(u,z)^r e^w\text{ 对实际 }A\text{ 循环}.}
\tag{N.5}
$$
证明对整个原标量多项式 $K=F^r$ 作完整 Bell 展开，
不把点态乘积误换为某个自然算子幂，也不由各因子的循环性推出乘积循环性。

### 10.2. 更深的真实梯度缩放

使用主稿 §2 的实际变化方向
$$
U_n=(X-s_{1n})-kT_n^{k-1}(Y-s_{2n}),\qquad
V_n=T_n^{(k-2)/2}(Y-s_{2n}).
$$
再置
$$
\boxed{
U_n'=T_n^sU_n,\qquad V_n'=T_n^{s/2}V_n.
}
\tag{N.6}
$$
这些仍是原共同深域上的有限线性组合；
每个固定 $n$ 的实际自然词域继续由同一 R186/R251 接口支付。

略写 $T=T_n$。在有限形式变量 $U',V'$ 中准确有
$$
x=s_{1n}+T^{-s}U'+kT^{(k-s)/2}V',
\qquad
y=s_{2n}+T^{-(k+s-2)/2}V'.
\tag{N.7}
$$
令 $\mathcal G_n(U',V')$ 为把 (N.7) 代入 $T^s g(x,y)$ 后的有限多项式。
主稿 (2.3) 逐项给
$$
\begin{aligned}
\mathcal G_n(U',V')
={}&T^s q_n-U'\\
&+k(s_{2n}^{k-1}-T^{k-1})T^{(s-k+2)/2}V'\\
&+\sum_{h=2}^{k}\binom kh
s_{2n}^{k-h}T^{\,s-h(k+s-2)/2}(V')^h.
\end{aligned}
\tag{N.8}
$$
其中 $q_n=s_{2n}^k-s_{1n}=O(n^{-1})$。

常数为 $O(T^s/n)\to0$，一次 $V'$ 系数为
$O((nT^{(k-s)/2})^{-1})\to0$。
第 $h\ge2$ 次系数的数量级为
$$
T^{(k+s)(1-h/2)};
$$
二次系数趋于 $\binom{k}{2}$，更高次系数趋零。
因此
$$
\boxed{
\mathcal G_n(U',V')\longrightarrow
-U'+\binom{k}{2}(V')^2
}
\tag{N.9}
$$
逐系数成立。

同时，令
$$
\mathcal Z_n(V')=\frac{s_{2n}}{T}
+T^{-(k+s)/2}V'.
$$
则 $y=T\mathcal Z_n(V')$，且
$$
\mathcal Z_n(V')\longrightarrow1
\tag{N.10}
$$
逐系数成立；这里保留了准确的 $s_{2n}/T=1+o(1)$，没有用形式中心代替实际中心。

### 10.3. 归一原多项式的全部系数与非零常数

对非零 $f_j$，记
$$
\widetilde f_{j,n}(v)=T^{-\ell_j}f_j(Tv).
$$
其系数一致有界，并趋于 $\operatorname{lc}(f_j)v^{\ell_j}$。
把 (N.7) 代入 (N.1)，得到准确有限恒等式
$$
\boxed{
T^{-\ell_0}F(x,y)
=\sum_{j=0}^{J}
T^{\ell_j-sj-\ell_0}
\widetilde f_{j,n}(\mathcal Z_n(V'))
\,\mathcal G_n(U',V')^j.
}
\tag{N.11}
$$
由 (N.4)，每个前面的实幂因子不超过1。
结合 (N.9)—(N.10)，(N.11) 的全部系数一致有界。

取常数项时，$j\ge1$ 的项都含
$\mathcal G_n(0,0)^j=(T^s q_n)^j\to0$，
而 $j=0$ 项趋于
$$
c_0=\operatorname{lc}(f_0)\ne0.
$$
故
$$
\boxed{
[T^{-\ell_0}F]_{\mathrm{constant}}\longrightarrow c_0.
}
\tag{N.12}
$$
(N.11) 可能含非零的极限 $U',V'$ 项；本证明不要求整个归一多项式趋于常数。

固定 $r\ge1$ 后，取 $K=F^r$。
直接对 (N.11) 作有限多项式乘方可知，
$T^{-r\ell_0}K$ 的全部系数一致有界，其常数趋于 $c_0^r\ne0$。

条件本身也对幂稳定：在 $F^r$ 的一个 $g^h$ 系数中，
任一乘积来自 $j_1+\cdots+j_r=h$，其次数至多
$$
\sum_{\nu=1}^r\ell_{j_\nu}
\le r\ell_0+s h.
$$
常数系数为 $f_0^r$，次数恰为 $r\ell_0$。
系数间相消只会降低次数，所以同一 $s<k$ 仍满足 (N.4)。

### 10.4. 真实头尾预算与严格上界 $s<k$

主稿已付
$$
g_{U,n}=O((\sqrt n\,T^k)^{-1}),\qquad
g_{V,n}=O((\sqrt n\,T^{k/2})^{-1}).
$$
由 (N.6)，两个新补集字母的总行范数满足
$$
\begin{aligned}
\varepsilon_n'
&=T^s g_{U,n}+T^{s/2}g_{V,n}\\
&=O((\sqrt n\,T^{k-s})^{-1})
+O((\sqrt n\,T^{(k-s)/2})^{-1})\\
&=\boxed{O((\sqrt n\,T^{(k-s)/2})^{-1}).}
\end{aligned}
\tag{N.13}
$$
两新有限头的绝对系数预算分别为
$O(T^{k+s})$ 和 $O(T^{(k+s)/2})$。
它们仍显式为 $\sum_{j<n}N_j B_{j,n}$，所以主稿 §3 的真实进位界适用。

$s<k$ 是这里实际用到的严格不等式。
在未另付新尾预算的情况下，不能把端点 $s=k$ 并入定理。

### 10.5. 原完整 Bell 修正没有丢失

固定原 $w$，使用主稿 §4 的同一对数累积量 $\kappa_\delta$：
它们只依赖原 $a,b,w$，不因为 (N.6) 改用另一组未经识别的最大图。

原完整 Bell 多项式为
$$
P_K(X,Y)=
\sum_\alpha\frac{C_\alpha^w}{\alpha!}
(\partial^\alpha K)(X,Y),\qquad K=F^r.
\tag{N.14}
$$
$\alpha=0$ 项除以 $T^{r\ell_0}$ 后，
已经由 §10.3 准确支付，不能用一个只看总次数的粗界替代其相消。

对其余有限个原偏导，赋 $x$ 权 $k$、$y$ 权1。
例如可取
$$
W=r\max_{f_j\ne0}(\ell_j+k j).
$$
$K$ 的每个原单项式权次数不超过 $W$。
(N.7) 中 $x$ 的各系数为 $O(T^k)$，
$y$ 的各系数为 $O(T)$；因为 $s\ge0,k\ge2$，其中负幂系数也一致有界。
因此所有偏导代入后的系数均为 $O(T^W)$。
再除以 $T^{r\ell_0}$ 只会改善这个上界。

取一个固定整数
$$
M\ge W+1.
$$
只对 (N.14) 涉及的有限个 $\delta$ 使用主稿 (5.1)—(5.3)：
$$
T^M\kappa_\delta=H_{\delta n}+E_{\delta n},
$$
$$
H_{\delta n}=\sum_{j<n}N_jB_{\delta j,n},
\qquad
\sum_{\delta,j<n}\|B_{\delta j,n}\|=O(T^M),
$$
$$
\max_\delta\|E_{\delta n}\|
\le C T^M\left(n^{-1}+n^{-1/2}\|w_{\ge n}\|_2\right)\to0.
\tag{N.15}
$$
每个 $C_\alpha^w$（$\alpha\ne0$）的单项式含至少一个累积量。
若含 $\ell\ge1$ 个，则代入 (N.15) 后的数值系数至多
$$
C T^{W-r\ell_0-M\ell}\le C.
$$
所以整个归一多项式 $T^{-r\ell_0}P_K$ 在以下字母中具有一致有界系数：

- 两个新的真实有限头及其补集 first；
- 有限个实际 $H_{\delta n}$；
- 小有界交换算子 $E_{\delta n}$。

把 $E_{\delta n}$ 吸收进有界系数，再将所有显式头和无界尾置零，
所得常数按算子范数趋于
$$
\boxed{c_0^rI.}
\tag{N.16}
$$
所有 Bell 修正含一个显式头或小 $E_{\delta n}$，故主稿 §5 的论证逐项适用。
任意复指数权的一阶 $w_jN_j$ 项和高阶项都保留在 (N.15) 内。

全部头的统一预算可取
$$
A_n\le C T^{M+k+s},
\qquad \log A_n=O(\log T).
\tag{N.17}
$$
只需这个固定对数幂上界，不要求新缩放满足上一稿的 $t_\nu\ge1$ 条件。

### 10.6. 实际核测试与幂次数

取
$$
\boxed{p_n=\lceil nT^{(k-s)/2}\rceil.}
\tag{N.18}
$$
由 (N.13)、(N.17) 得
$$
p_n/n\to\infty,\qquad
\varepsilon_n'\sqrt{p_n}=O(T^{-(k-s)/4})\to0,
\qquad
(n/p_n)\log A_n=O(T^{-(k-s)/2}\log T)\to0.
\tag{N.19}
$$
且 $A_n e^{-\gamma(2n)^3}\to0$。

设 $\Pi$ 为规范完整 $\mathcal P_K$ 的核投影。
在原共同伴随深域上令
$$
\mathscr T_n
=I-\frac{P_K^*}{T^{r\ell_0}\overline{c_0}^{\,r}}.
\tag{N.20}
$$
由 (N.16)，其算子常数项趋于零；其余系数一致有界。
原整柱 $Q_nH$ 支付任意有限次迭代，
而 $\Pi P_K^*=0$ 给
$$
\Pi Q_n=\Pi\mathscr T_n^{p_n}Q_n.
$$
全部 $n$ 依赖系数保持原混合伴随域，但没有被移过未知的 $\Pi$。

主稿 §6 的根界只使用
$p_n/n\to\infty$、$\varepsilon_n'\sqrt{p_n}\to0$、
$(n/p_n)\log A_n\to0$ 和高头进位。
把 (N.19) 代入，同样得到
$$
\|\mathscr T_n^{p_n}Q_n\|^{1/p_n}\to0.
$$
于是 $\Pi=0$。原 $C$ 自伴性、指数图核心及 $B_w$ 单位给 (N.5)。

### 10.7. 移位、有限标量复合与乘积

这些范围可以直接在原多项式的同一个有限过滤中验证。
对固定 $s$，令
$$
\mathcal V_d(s)
=\left\{\sum_j h_j(y)g^j:
\deg h_j-sj\le d\text{ 对每个非零系数成立}\right\}.
$$
有限多项式的逐项乘法给
$$
\mathcal V_d(s)\,\mathcal V_e(s)\subset\mathcal V_{d+e}(s).
\tag{N.21}
$$
这只是实际有限多项式的次数不等式，不涉及无界算子的乘法定义域。
定理要求 $F\in\mathcal V_{\ell_0}(s)$，并且其曲线限制
$F(y^k,y)=f_0(y)$ 的次数恰为 $\ell_0$。

若 $\ell_0>0$，任意非零标量多项式 $Q$ 都满足
$$
Q(F)\in\mathcal V_{(\deg Q)\ell_0}(s),
\qquad
\deg Q(f_0)=(\deg Q)\ell_0.
$$
因此直接对整个原多项式 $Q(F)$ 使用定理，得到
$$
\boxed{Q(F(u,z))e^w\text{ 对任意非零 }Q\text{ 循环}.}
\tag{N.22}
$$
非零常数 $Q$ 仍按原指数循环性解释。

若 $\ell_0=0$、$f_0=c\ne0$，则每个 $F$ 的幂都在
$\mathcal V_0(s)$ 中。只要 $Q(c)\ne0$，原多项式 $Q(F)$ 的曲线限制
就是该非零常数，故直接得到 $Q(F(u,z))e^w$ 循环。
这里不包含 $Q(c)=0$ 的情况。

于是 $\ell_0>0$ 时可取 $Q(t)=(t-\lambda)^r$，
得到全部 $\lambda\in\mathbb C$ 的移位和点态幂；
$f_0=c\ne0$ 时得到全部 $\lambda\ne c$。

有限若干原多项式 $F_i$ 分别满足本节条件时，可以共用
$s=\max_i s_i<k$。其乘积属于
$\mathcal V_{\sum_i\ell_{0,i}}(s)$，曲线限制
$\prod_i f_{0,i}(y)$ 非零且次数恰为 $\sum_i\ell_{0,i}$。
所以该乘积也直接满足定理及上述复合范围。
这些结论全由原有限系数检验后重新应用完整 Bell 证明，
不是将循环向量相乘。

### 10.8. 具体新增范围与端点

取
$$
F(x,y)=y^{k-1}(y^k-x)-\lambda,\qquad\lambda\ne0.
$$
此时 $\ell_0=0,\ell_1=k-1$，可取 $s=k-1<k$，
故
$$
\boxed{
[z^{k-1}(z^k-u)-\lambda]^r e^w
\text{ 对所有 }\lambda\ne0,\ r\ge1,\ w\text{ 循环}.
}
\tag{N.23}
$$
更一般，$y^L(y^k-x)^m-\lambda$ 在
$L\ge0,m\ge1,L<km,\lambda\ne0$ 时满足条件，
同样得到全部固定点态幂和指数权。
这些结论不是主稿 $q(z^k-u)$ 的单变量重述。

端点例 $y^k(y^k-x)-\lambda$ 需要 $s\ge k$，
本节没有相应的趋零尾预算。
对于 $f_0=0$，特别是完全去中心的 $z^k-u$ 本身，
(N.16) 仍缺少非零常数。本节继续保留该分支，
也未解决一般复杂慢行的共振或普通复 Hilbert ISP。

