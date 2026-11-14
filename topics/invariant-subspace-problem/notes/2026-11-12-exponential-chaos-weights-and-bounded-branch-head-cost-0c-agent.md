# R207 附录：指数次数权给全零头的定量高尾次数约束

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：完整实际必要条件。承接 R207 的记号与已证域。它加强投影/延拓成本的速率，不由成本增长推出慢平方核为零。

## A. 固定指数权的真实尺度估计

对尾位 $j\ge m$，令 $\mathcal N_m$ 为 Walsh 次数算子，置
$$
\mathcal H_{m,t}=\operatorname{Dom}e^{t\mathcal N_m},\qquad
\|v\|_{m,t}=\|e^{t\mathcal N_m}v\|,\qquad 0\le t\le1.
$$
$\mathcal H_{m,0}=H_{\ge m}$。
令
$$
Z_m=\sum_{j\ge m}a_jV_j,\qquad g_m=\|a_{\ge m}\|_2.
$$

**引理 A.1。** 存在一个与 $m,t,\delta,a$ 无关的有限模型常数 $C$，
使每个 $0<\delta\le t\le1$ 都有
$$
\boxed{
\|Z_m:\mathcal H_{m,t}\to\mathcal H_{m,t-\delta}\|
\le Cg_m\delta^{-1/2}.
}
\tag{A.1}
$$
这里的映射由真实闭 $Z_m$ 限制得到；特别
$\mathcal H_{m,t}\subseteq\operatorname{Dom}Z_m$ 对 $t>0$ 成立。

证明先考虑纯算子
$$
Z_m^0=\sum_{j\ge m}a_j(c_j-c_j^*+2n_j).
$$
在次数 $q$ 到 $q+1,q-1,q$ 的三个块上，通常范数分别至多
$g_m\sqrt{q+1}$、$g_m\sqrt q$、$2g_m\sqrt q$。
加上两端指数权后，额外比值分别是
$$
e^{t-\delta}e^{-\delta q},\qquad
e^{-(t-\delta)}e^{-\delta q},\qquad e^{-\delta q}.
$$
对 $0<\delta\le1$，
$$
\sup_{q\ge0}\sqrt{q+1}\,e^{-\delta q}\le2\delta^{-1/2}.
$$
各单独移位块的输入、输出次数正交，再对三类使用三角不等式，
故纯部分可用常数16。

实际 carry 仍用 R171/R181 的局部级数
$$
K_m=Z_m-Z_m^0
=\sum_{j\ge m}\sum_{L\ge1}a_jB_{j,j+L},\qquad
\|B_{j,j+L}\|\le18\eta_j\eta_*^{L-1}.
$$
该局部项只作用 $L+1$ 位，所以对 $0\le s\le1$，
$$
\|e^{s\mathcal N_m}B_{j,j+L}e^{-s\mathcal N_m}\|
\le e^{s(L+1)}\|B_{j,j+L}\|.
$$
因为 $e\eta_*<1$，
$$
\|K_m:\mathcal H_{m,s}\to\mathcal H_{m,s}\|
\le
\frac{18e^2}{1-e\eta_*}
\sum_{j\ge m}|a_j|\eta_j
\le C_Kg_m,
$$
其中可取
$$
C_K=\frac{18e^2\|\eta\|_2}{1-e\eta_*}.
$$
从 $t$ 到 $t-\delta$ 的嵌入为收缩映射，且 $\delta^{-1/2}\ge1$，
所以 (A.1) 可取 $C=16+C_K$。

这些估计先在有限柱上成立。
有限柱在每个指数权空间中稠密；取其加权逼近，利用 $Z_m$ 及
$e^{(t-\delta)\mathcal N_m}$ 的闭性，得到所述真实域与映射。
因此没有把无界形式和直接当作指数权空间上的算子。证毕。

## B. 任意有限尾次数上的全部实际幂

对整数 $p\ge1$，把尺度 $1\to0$ 分成 $p$ 个步长 $1/p$。
反复使用 (A.1)，得到
$$
\boxed{
\|Z_m^p v\|\le(Cg_m\sqrt p)^p e^q\|v\|,
\qquad v\in H_{\ge m,\le q}.
}
\tag{B.1}
$$
每个中间输入在一个正指数权空间内，因而确在下一次 $Z_m$ 的域中。
所以 (B.1) 是自然幂界，而不是仅有形式的反复作用。

为统一二项式中的较低幂，置
$$
D_{m,p}=Cg_m\sqrt p.
$$
则对 $0\le r\le p$，
$$
\|Z_m^r v\|\le D_{m,p}^r e^q\|v\|.
\tag{B.2}
$$
$r=0$ 时该式只是 $1\le e^q$。

## C. 低头误差只付一次

沿用 R207 的
$$
s_m=a_*+\sum_{j<m}a_j,\quad
H_m=\sum_{j<m}a_j(V_j-I),\quad
L_m=6\sum_{j<m}|a_j|,\quad
h_m=6\alpha_m\sum_{j<m}|a_j|/\alpha_j.
$$
真实分解为 $X-s_mI=H_m+Z_m$。
对全1头柱投影 $\Pi_{1,m}$，
$$
\|H_m\|\le L_m,\qquad
\|H_m^k\Pi_{1,m}\|\le L_m^{k-1}h_m\quad(k\ge1).
$$
$Z_m$ 保持该物理头，$H_m$ 与其真实自然幂域交换。

因此对 $v\in H_{\ge m,\le q}$，二项式和 (B.2) 给
$$
\begin{aligned}
\|(X-s_mI)^p(e_1^{\otimes m}\otimes v)\|
&\le e^q\left[
D_{m,p}^p+
h_m\sum_{k=1}^p\binom pk L_m^{k-1}D_{m,p}^{p-k}
\right]\|v\|\\
&\le e^q\left[
D_{m,p}^p+
p h_m(L_m+D_{m,p})^{p-1}
\right]\|v\|.
\end{aligned}
\tag{C.1}
$$
最后一步是有限多项式的差商界，也适用于 $L_m=0$。

共同共轭 $C$ 把全1头变成全0头，并保持尾 Walsh 次数。
定义投影
$$
\mathcal E_{m,q}
=|e_0^{\otimes m}\rangle\langle e_0^{\otimes m}|
\otimes P_{\ge m,\le q}.
$$
由 $X^*=CXC$，(C.1) 给
$$
\boxed{
\|(X^*-\overline{s_m}I)^p\mathcal E_{m,q}\|
\le e^q\left[
D_{m,p}^p+
p h_m(L_m+D_{m,p})^{p-1}
\right].
}
\tag{C.2}
$$
$\operatorname{Ran}\mathcal E_{m,q}$ 虽可能无限维，但其中每个向量
确属于本式所需的全部有限自然幂域。

## D. 有界分支的统一指数投影界

设 $0\ne M$ 为闭 $A$ 不变子空间，
$M\subseteq\operatorname{Dom}X$ 且 $X_M$ 有界。
假设存在 $m_0$ 和 $R\ge1$，使
$$
s_m\in\rho(X_M),\qquad
\|(X_M-s_mI)^{-1}\|\le R\quad(m\ge m_0).
\tag{D.1}
$$
R207 的真实恒等式 $P_MX^*=X_M^*P_M$ 可在 (C.2) 的域中逐幂迭代。
所以
$$
\boxed{
\|P_M\mathcal E_{m,q}\|
\le e^q R^p\left[
D_{m,p}^p+
p h_m(L_m+D_{m,p})^{p-1}
\right].
}
\tag{D.2}
$$

对充分大的 $m$，$h_m>0$ 且 $h_m<1$。
记
$$
\theta_m=-\log h_m,\qquad
b_m=\log\bigl(R(2+L_m)\bigr).
$$
(D.1) 与 $M\ne0$ 已排除整行 $a=0$；所以充分大 $m$ 确有 $h_m>0$。
若 $g_m=0$，下面第一项上界按 $+\infty$ 理解。
选择
$$
p_m=
\left\lfloor
\min\left\{
\frac{e^{-4}}{C^2R^2g_m^2},
\frac{\theta_m}{4(b_m+2)}
\right\}
\right\rfloor,\qquad
q_m=\lfloor p_m/4\rfloor.
\tag{D.3}
$$
当 $m$ 足够大时，$p_m\ge1$。
因为 $R D_{m,p_m}\le e^{-2}$，
(D.2) 的第一项不超过 $e^{-7p_m/4}$。

第二项中 $D_{m,p_m}\le1$、$R\ge1$，从而
$$
R^{p_m}(L_m+D_{m,p_m})^{p_m-1}
\le e^{b_mp_m}.
$$
再用 $\log p_m\le p_m$、$q_m\le p_m/4$ 和
$\theta_m\ge4(b_m+2)p_m$，第二项至多为
$e^{-6p_m}$。
两项相加，对 $p_m\ge1$ 可得
$$
\boxed{\|P_M\mathcal E_{m,q_m}\|\le e^{-p_m}.}
\tag{D.4}
$$

最后，
$$
h_m\le\frac{6g\eta_{m-1}}{\sqrt{1-\eta_*^2}},\qquad
L_m\le6g\sqrt m.
$$
实际 $\eta_{m-1}$ 的双指数衰减保证
$\theta_m/(b_m+2)\to\infty$；同时 $g_m\to0$。
故 $p_m,q_m\to\infty$，所有选择均有意义。

## E. 交替慢幂尾的速率和准确的成本结论

在 R207 的交替幂尾
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad \tfrac12<\sigma\le1,
$$
及危险平方分支 $X_M=Y|_M$、$\chi(Y)=1$ 中，
部分和极限属于 $(0,1)$，故 (D.1) 成立。
积分比较给
$$
g_m^2\asymp m^{1-2\sigma}.
$$
(D.3) 的第一项为 $m^{2\sigma-1}$ 的固定常数倍，
第二项增长远快于它。因此存在 $c,c'>0$，使充分大 $m$ 时
$$
p_m\ge c m^{2\sigma-1},\qquad
q_m\ge c' m^{2\sigma-1}.
$$
于是
$$
\boxed{
\|P_M\mathcal E_{m,q_m}\|
\le\exp(-c m^{2\sigma-1}).
}
\tag{E.1}
$$

特别，$e_0^{\otimes m}\otimes\Omega_{\ge m}$ 属于 $\mathcal E_{m,q_m}$ 的像，故每个有限头右逆
$J_m:\mathcal F_m\to M$ 都满足
$$
\boxed{\|J_m\|\ge\exp(c m^{2\sigma-1}).}
\tag{E.2}
$$
对每个单位 $h\in M$，还可写成
$$
\|\mathcal E_{m,q_m}h\|\le e^{-p_m}.
$$
令 $\Pi_{0,m}=|e_0^{\otimes m}\rangle\langle e_0^{\otimes m}|\otimes I$。
所以若 $\rho=\|\Pi_{0,m}h\|$ 为 $h$ 在完整全零头柱中的范数，
其中尾次数大于 $q_m$ 的部分范数至少是
$\sqrt{\max(0,\rho^2-e^{-2p_m})}$。

没有给这个完整全零头柱质量一个统一正下界，也没有给
$\|J_m\|$ 一个能与 (E.2) 冲突的上界。
$\mathcal E_{m,q_m}$ 的头部随 $m$ 移向一个测度趋零的柱，
并不强趋恒等；因此 (D.4) 不能推出 $P_M=0$。
这正是当前仍需真正 M 特有控制的部分。
