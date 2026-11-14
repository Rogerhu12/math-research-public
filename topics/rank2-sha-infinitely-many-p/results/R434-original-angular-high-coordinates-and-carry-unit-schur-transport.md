# R434：原角高轴的全素数固定坐标与 carry 单位 Schur 运输

日期：2026-11-14。**状态：已证明。** 本篇把 R425/R428 的两条高轴坐标恢复为原 $t$ 角中的固定系数。它们模 $p$ 只由实际 Gaussian 常数和 $(2/p)$ 决定，模 $p^3$ 则由同一个原 Miller 常数及 $2$ 的 Fermat 商准确给出。$t$ 到 $w$ 的全部高尾仍进入完整中央 Hensel 条件；但对真正方阵，该高尾在模 $p^2$ 行列式上只乘一个明确整单位，所以 R428 唯一掉秩线上的 $\eta_p$ 不增加新的高尾项。没有由这段有限矩阵运输断言两个完整中央不能同时为零。

## 1. 同一原模型与两个固定的角系数

采用共同 $E_1$ 模型及
$$
p=6s-1>83,\quad1\le\ell<s-13,\quad L=2s+\ell,
\quad a=p\kappa\in\mathcal O^\times,\quad\alpha=36/17.
$$
仍用原 $w=z^6$、$t=-1/x^3$、$\Theta=x\sigma^2$，并写
$$
\rho=(1+8t)\Theta^{17},\qquad g=e^{-\kappa w^s}\rho.
\tag{1}
$$
R305/R338 的固定系数为
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n},
\qquad A_p=p\ell_s\in\mathcal O^\times.
\tag{2}
$$
令 $e=(-1)^s$、$\chi=(2/p)$。原 Miller 常数仍是
$$
d_p=\ell_s-e\kappa\in\mathcal O,
\qquad eA_p=a+epd_p.
\tag{3}
$$
本篇不把 $A_p,a,d_p$ 当作可选参数。

因为 $w(t)^s$ 的 $t$ 阶恰为 $s$，原 $\log g$ 的下列两项不受 (1) 的 Gaussian 去除影响：
$$
\begin{aligned}
U_*&=[t^{s-2}]\log g
 =\ell_{s-2}-e\frac{8^{s-2}}{s-2},\\
V_*&=[t^{s-1}]\log g
 =\ell_{s-1}+e\frac{8^{s-1}}{s-1}.
\end{aligned}
\tag{4}
$$
定义同一实际对象的参考分解
$$
g_\circ=g\exp(-U_*t^{s-2}-V_*t^{s-1}),\qquad
g_{U,V}=g_\circ\exp(h_{U,V}),\quad
h_{U,V}=Ut^{s-2}+Vt^{s-1}.
\tag{5}
$$
只有 $(U,V)=(U_*,V_*)$ 是原算术来源。其他参数只用于同一个有限评价的坐标计算。

## 2. 原 theta 高系数的准确反向递推

**定理 1。** 对全部 $1\le k<s$，有
$$
\boxed{\ell_{s-k}\equiv
A_p\frac{4^k}{6k(6k-1)\binom{2k}{k}}\pmod p.}
\tag{6}
$$
特别，以下是特征零的准确恒等式，而非仅模 $p$ 近似：
$$
\boxed{\ell_{s-1}=A_pr_1(p),\qquad
\ell_{s-2}=A_pr_2(p),}
\tag{7}
$$
$$
r_1(p)=\frac{p+1}{(p-5)(p-3)},\qquad
r_2(p)=\frac{(p+1)(p-6)}{(p-3)(p-11)(p-9)}.
$$
所有分母在当前范围内均为 $p$ 单位。此外
$$
\boxed{\bar a=68e\,4^{-(s-1)}\binom{2s-2}{s-1}\quad\text{于 }k.}
\tag{8}
$$

**证明。** (2) 给
$$
\frac{\ell_n}{\ell_{n-1}}
=\frac{(n-1)(n-2/3)}{n(n-1/6)}.
$$
先将 $n=s$ 的唯一分母 $p/6$ 单独取出，再代入 $6s=p+1$，立即得到 (7)。向后再走 $k-1$ 步并模 $p$ 约化，得到
$$
\frac{\ell_{s-k}}{A_p}
\equiv\frac1{15}\prod_{r=1}^{k-1}
\frac{r(r-1/6)}{(r+5/6)(r+1/2)}
=\frac1{3(6k-1)}\frac{(k-1)!}{(3/2)_{k-1}}.
$$
以 $(3/2)_{k-1}=2(1/2)_k$ 化简即为 (6)。$2k<p$、$6k-1<p$ 保证这一整段递推中的所有约化合法。最后取 $k=s-1$，使用 $\ell_1=34/15$、$6(s-1)\equiv-5$、$6s-7\equiv-6$，得到 $A_p\equiv68\binom{2s-2}{s-1}/4^{s-1}$；再用 (3) 即得 (8)。$\square$

## 3. 物理坐标的首两项及完整高尾

原换参为
$$
t=-w-\frac37w^2-\frac{75}{637}w^3+\cdots.
\tag{9}
$$
所以准确写成
$$
h_{U,V}=u w^{s-2}+v w^{s-1}+w^sH_{U,V}(w),
\tag{10}
$$
其中
$$
\boxed{u=eU,\qquad v=e\left(\frac{3(s-2)}7U-V\right).}
\tag{11}
$$
这个整线性变换的行列式是 $-1$。若 $A=(t/w)^{s-2}$、$B=(t/w)^{s-1}$，则全部高尾为
$$
\boxed{H_{U,V}=
U\frac{A-e-e\frac{3(s-2)}7w}{w^2}
 +V\frac{B+e}{w}.}
\tag{12}
$$
两个商均整；这保留原换参产生的全部高项，没有用两个纯 $w$ 单项式替代 (5)。例如
$$
H_{U,V}(0)=\frac{3(s-1)}7v
 +(s-2)\left(\frac{75}{637}-\frac{9(s+1)}{98}\right)u,
\tag{13}
$$
故模 $p$ 为 $-5v/14-99u/5096$。

**定理 2（实际坐标的全素数公式）。** 令 $u_*,v_*$ 是 (4) 经 (11) 的像，则
$$
\boxed{\bar u_* =\frac{2\bar a}{99}+\frac{3\chi}{176},\qquad
\bar v_*=-\frac{26\bar a}{315}+\frac{321\chi}{1120}.}
\tag{14}
$$
若要保留模 $p^3$，令 $B_p=8^s$、$\beta_p=a+epd_p=eA_p$，则准确有
$$
\boxed{\begin{aligned}
u_*&=\beta_pr_2(p)-\frac{B_p}{64(s-2)},\\
v_*&=\beta_p\left(\frac{3(s-2)}7r_2(p)-r_1(p)\right)
             -\frac{3B_p}{448}-\frac{B_p}{8(s-1)}.
\end{aligned}}
\tag{15}
$$
这里 $B_p$ 也可以用同一个固定整数 $2$ 的实际 Fermat 商
$q_p(2)=(2^{p-1}-1)/p$ 计算：
$$
\boxed{B_p\equiv2\chi\left(1+\frac p2q_p(2)
                 -\frac{p^2}{8}q_p(2)^2\right)\pmod{p^3}.}
\tag{16}
$$

**证明。** (15) 是 (4)、(7)、(11) 的直接代入。模 $p$ 时 $s\equiv1/6$、$\beta_p\equiv a$，而
$B_p=2^{(p+1)/2}\equiv2\chi$；化简给 (14)。对于 (16)，$2^{(p-1)/2}$ 的平方是 $1+pq_p(2)$，其模 $p$ 值为 $\chi$。在这个固定单位根分支作二项式展开即得。$\square$

(8)、(14) 也给不含未计算 Gaussian 符号的有限二项式表达；它们没有主张这些数值中的某个组合跨素数非零。

## 4. 两条完整中央仍读取全部 t 高尾

令 $S_\circ,T_\circ$ 是 (5) 的参考 regularized 原来源，$S_{U,V}=S_\circ e^h$、$T_{U,V}=T_\circ e^{\alpha h}$。对 $k=1,2,3$ 定义
$$
c_k(U,V)=[w^{ks}]S_\circ\sum_{m=0}^{k}\frac{h^m}{m!},\qquad
d_k(U,V)=[w^{ks}]T_\circ\sum_{m=0}^{k}\frac{\alpha^mh^m}{m!}.
\tag{17}
$$
这是全部系数公式：$S_\circ,T_\circ$ 均从 $w$ 起，$s\ge15$ 使 $m>k$ 的项高于所读次数。式中 $h$ 是整个 (10)，所以第二、第三中央权中的所有高 wrap 均保留。

R403/R425 的完整三权归一仍是
$$
F_S=c_1-\frac pa c_2+\frac{2p^2}{a^2}c_3,\qquad
F_T=\frac{d_1}{\alpha}-\frac{p}{\alpha^2a}d_2
                           +\frac{2p^2}{\alpha^3a^2}d_3.
\tag{18}
$$
其模 $p$ Jacobian 是
$$
\begin{pmatrix}s_2&1\\t_2&1\end{pmatrix}
\begin{pmatrix}e&0\\3e(s-2)/7&-e\end{pmatrix},\quad
s_2=-988/105,\quad t_2=-2938/35,
\tag{19}
$$
行列式为 $t_2-s_2=-1118/15$，在当前惰性范围是单位。因此 (18) 有唯一解 $(U^\dagger,V^\dagger)\bmod p^3$；逐位 Hensel 的每一步均使用整个 (17)。原两完整中央失败必迫
$$
(U_*,V_*)\equiv(U^\dagger,V^\dagger)\pmod{p^3}.
\tag{20}
$$
反向只恢复这里的三权精度，不能用来断言原完整中央函数为零。

例如令 $b_S=F_S(0,0)\bmod p$、$b_T=F_T(0,0)\bmod p$。原同时失败的首位必要条件现在成为两条固定等式
$$
\boxed{\begin{aligned}
b_S&=\frac{2834}{10395}\bar a-\frac{311}{2464}\chi,\\
b_T&=\frac{2054}{1155}\bar a+\frac{14097}{12320}\chi.
\end{aligned}}
\tag{21}
$$
它们是 $b_S+s_2u_*+v_*=b_T+t_2u_*+v_*=0$ 及 (14) 的化简，不是把两个完整基准 $b_S,b_T$ 删除。

## 5. 高尾在真实方阵上的整单位运输

取 R406/R408 原有限自由来源 $\mathcal W_{D,J}$，$0\le J\le16$，以及相对 Euler
$$
\mathcal E_{\rm rel}(\mathscr R^nq_n(t)t^kT^j)
=(n+\alpha j)\mathscr R^nq_n(t)t^kT^j.
$$
记 $J_t(U,V)$ 为 (5) 的真实相对三块评价，$J_w(u,v)$ 为同一参考 $g_\circ$ 只乘 $\exp(uw^{s-2}+vw^{s-1})$ 的辅助评价。两者使用同一来源、同一 $t$、同一 $a$，差恰为 (12) 的高尾。

在 $\bar\Gamma_L$ 上令 $E_\epsilon=\epsilon\partial_\epsilon$，即三块的对角权 $0,1,2$。任意整提升给出下式中同一个模 $p^2$ 算子。

**定理 3。** 对整个原来源逐列有
$$
\boxed{J_t\equiv
\left(I+\frac pa\,\bar H_{U,V}E_\epsilon\right)J_w
\pmod{p^2}.}
\tag{22}
$$
特别，若原来源维数 $N=L$，则无需预设可逆性就有
$$
\boxed{\det J_t\equiv
\left(1+\frac pa(s+2\ell)H_{U,V}(0)\right)\det J_w
\pmod{p^2}.}
\tag{23}
$$

**证明。** 在原整目标中 $w^s=p\epsilon$，所以完整指数恒等式给
$$
J_t=J_w+pH\epsilon J_w\mathcal E_{\rm rel}
       +\frac{p^2H^2\epsilon^2}{2}J_w\mathcal E_{\rm rel}^2.
$$
一列模 $p$ 是 $A(w)e_2(aq\epsilon)$，$q=n+\alpha j$，因此
$$
\epsilon\bar J_w\mathcal E_{\rm rel}
=a^{-1}E_\epsilon\bar J_w.
$$
代回即得 (22)。乘 $\bar H$ 的矩阵按每块局部 $w$ 次数为三角形，其对角均为 $H(0)$，所以
$\operatorname{tr}(\bar H E_\epsilon)=(s+2\ell)H(0)$。恒等式
$\det(I+pK)\equiv1+p\operatorname{tr}K\bmod p^2$ 给 (23)。这同时证明 (22) 的目标变换是整单位。$\square$

整个原评价始终是
$$
\boxed{M_t^{\rm orig}=c_*U_{0,t}\,m_{13}J_t.}
\tag{24}
$$
公共 $G_0=\mathscr R^{40}h_0(t)$ 中的 $P_{134}$ 保留不动，$U_{0,t}$ 的高轴差是乘 $e^{40p\epsilon H}$。它在原饱和像格上为对角一的三角单位；没有将原总 charge 四十删掉。$m_{13}$ 的两个完整十三行 carry 带仍准确贡献二十六个 $p$。因此 (23) 可用于 R428 的同一个原有限首提升及第二次提升。

## 6. 唯一 carry 线上的实际标量与完整第二位

取 $\ell=1,N=L$。设 $J_\circ=J_t(0,0)=J_w(0,0)$，并记
$$
\vartheta(P)=a[w]\{\mathcal E_{\rm rel}^{\,2}P\}_{\rm reg,\circ},
\qquad r=2s-1.
$$
R428 的原行加法给 $\bar J_w\sim\bar J_\circ+u e_r\vartheta$。故即使参考矩阵奇异，也有无分母恒等式
$$
\boxed{\det\bar J_t(U,V)=A_0+uA_1,\quad
A_0=\det\bar J_\circ,\quad
A_1=\vartheta\operatorname{adj}(\bar J_\circ)e_r.}
\tag{25}
$$
原实际行列式因而准确为
$$
\boxed{\det\bar J_{\rm actual}
=A_0+\left(\frac{2\bar a}{99}+\frac{3\chi}{176}\right)A_1.}
\tag{26}
$$
这三个量全由固定原来源确定；没有自由高轴参数。

若 $A_0\ne0$，置 $\tau_p=A_1/A_0$，则真正首提升的实际相容值是
$$
\Delta_p=1+\tau_p\left(\frac{2\bar a}{99}+\frac{3\chi}{176}\right).
\tag{27}
$$
只有在原完整中央失败时，(27) 同时是其唯一中央 Hensel 解指定的相容值。$\Delta_p\ne0$ 仍只说明这段来源的真正 $C_2$ 没有额外有限方向，不是中央非零结论。

若 $\Delta_p=0$，将 (20) 经整线性式 (11) 转为 $u^\dagger,v^\dagger\bmod p^2$，并令
$$
D_t=\det J_t/\det J_\circ,\qquad D_w=\det J_w/\det J_\circ.
$$
(23) 的单位因子在 $D_w\in p\mathcal O$ 时不改变其除 $p$ 剩余值。因此唯一真实第二障碍准确满足
$$
\boxed{\eta_p
=\overline{D_t(U^\dagger,V^\dagger)/p}
=\overline{D_w(u^\dagger,v^\dagger)/p}.}
\tag{28}
$$
$H$ 必须用于 (17) 的第二 Hensel 位；(28) 证明的是它不再额外修正这个矩阵标量。第二位可以直接用原固定式 (15) 代入，但仅在 (20) 已知时才把该实际值认作中央条件值。若 $\eta_p\ne0$，同一个原 $M$ 的 Smith 因子仍是 R428 的 $L-26$ 个单位、二十五个 $p$、一个 $p^2$；若 $\eta_p=0$，唯一方向继续进入第三精度。第三 Hensel 位及完整中央基准仍必须另保，不能因 (28) 而省略。

## 7. 有限核验与尚待证明的量

伴随脚本 `scripts/check-r434-angular-high-coordinates.py` 检查 (6) 的整段反向系数、(7)/(14)/(16) 的固定参数，以及 (22) 在原三块全部真实列上的等式；另直接计算完整 $P_{134}$ 与 charge 四十，核对 $t$ 高轴和纯 $w$ 两项加完整 $H$ 产生同一个模 $p^3$ 原矩阵。核验只检查公式，没有把有限实例作为跨素数非零输入。

余下的主线数量已没有可调高轴：它是 (25) 的同一原有限矩阵 $A_0,A_1$、(21) 的两完整参考基准，以及掉秩时 (28) 的固定第二位。证明这些实际量的跨素数相容性或得到真正非零中央，仍是开放步骤。
