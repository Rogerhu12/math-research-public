# R14：任意目标、非退化误差及全部整数指数的极小像非紧性

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94；并行推导：centered_literature。

**状态：已证明的中间结论。** 对 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的具体加权 odometer，完整排除固定非零目标、固定非退化相对误差下 backward-minimal-vector images 的强紧性，覆盖全部整数指数。也给出 dyadic 指数的精确弱极限。没有解决该模型或一般 ISP，不主张文献新颖性。来源条件核查另见[本轮文献笔记](../notes/2026-11-12-centered-literature-e2.md)。

## 1. 全指数极小像非紧性定理

以下仅用 R9 已定义的系数：

$$
a_j=e^{-b_j},\qquad
b_j=10+\frac{1400}{15}(16^j-1)-90\,8^j+300\,2^j-200
=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$

令 $H=L^2(\mathbb Z_2,\mu)$，$\mu$ 为 Haar 概率测度，$w(y)=a_{v_2(y)}$，$w(0)=0$，$A=M_wU$。

**定理。** 固定 $f\in H\setminus\{0\}$ 以及 $0<\beta<1$。对每个 $n\ge1$，令 $x_n$ 为闭凸集合

$$
\mathcal C_n=\{x\in H:\|A^nx-f\|\le\beta\|f\|\}
\tag{1.2}
$$

中范数最小的唯一向量，并置 $z_n=A^nx_n$。则 $(z_n)_{n\ge1}$ **没有任何范数收敛子列**。

更定量地，取

$$
r=\left\lceil\log_2\frac{16}{\beta^2}\right\rceil,
\qquad p_\beta=2^{-r-2}>\frac{\beta^2}{128}.
\tag{1.3}
$$

对任意固定 $z\in H$，有

$$
\liminf_{n\to\infty}\|z_n-z\|\ge \sqrt{p_\beta}\,\|z\|,
\tag{1.4}
$$

同时

$$
\|z_n\|\ge(1-\beta)\|f\|.
\tag{1.5}
$$

因而所有固定 $z$ 还满足统一正下界

$$
\liminf_n\|z_n-z\|
\ge \frac{\sqrt{p_\beta}}{1+\sqrt{p_\beta}}(1-\beta)\|f\|>0.
\tag{1.6}
$$

结论对任何 $n_j\to\infty$ 都成立，并非仅对 $n=2^k$。

## 2. 两个基本引理

### 2.1 系数界

对每个 $j\ge0$，

$$
16^j\le b_j\le400\,16^j.
\tag{2.1}
$$

上界由 (1.1) 舍去负项、并用 $2^j\le16^j$ 得到，因为 $280/3+300=1180/3<400$。下界在 $j=0,1$ 分别由 $b_0=20$、$b_1=1090$ 验证。当 $j\ge2$ 时，$8^j\le16^j$ 给

$$
b_j\ge\frac{10}{3}16^j-\frac{850}{3}\ge16^j,
$$

最后一步等价于 $7\cdot16^j\ge850$，对 $j\ge2$ 成立。

### 2.2 长模区间与固定函数渐近独立

给正整数 $n<Q$，其中 $Q$ 为 $2$ 的幂，定义

$$
E(n,Q)=\{y\in\mathbb Z_2:y\bmod Q\in\{0,1,\dots,n-1\}\}.
\tag{2.2}
$$

显然 $\mu(E(n,Q))=n/Q$。若 $Q\to\infty$ 且 $n<Q$ 任意变化，则对每个固定 $h\in L^1(\mu)$，

$$
\int_{E(n,Q)}h\,d\mu-\frac nQ\int h\,d\mu\longrightarrow0.
\tag{2.3}
$$

**证明。** 先取 $h$ 为只依赖最低 $d$ 位的柱函数。对每个 $t\in\{0,\dots,2^d-1\}$，整数 $0\le j<n$ 中满足 $j\equiv t\pmod{2^d}$ 的个数与 $n/2^d$ 相差至多 $1$。因此该柱集合与 $E(n,Q)$ 的交测度和乘积测度相差至多 $1/Q$；有限线性组合给 (2.3)。一般 $h$ 用柱函数在 $L^1$ 中逼近，两个积分项产生的总误差至多 $2\|h-h_d\|_1$。先令 $Q\to\infty$，再令逼近误差趋零即可。此论证允许 $n/Q$ 不收敛。证毕。

## 3. 极小向量公式及标量参数上界

令

$$
W_n(y)=\prod_{j=0}^{n-1}w(y-j).
\tag{3.1}
$$

则

$$
A^n=M_{W_n}U^n,\qquad
A^nA^{*n}=M_{W_n^2}.
\tag{3.2}
$$

$W_n>0$ 几乎处处，所以 $A^n$ 单射且值域稠密，(1.2) 非空。闭凸投影定理保证最小范数元存在且唯一。也可直接构造它：存在唯一 $\lambda_n>0$ 使

$$
\int\frac{|f(y)|^2}{(1+\lambda_n W_n(y)^2)^2}\,d\mu(y)
=\beta^2\|f\|^2.
\tag{3.3}
$$

左端是关于 $\lambda\ge0$ 连续严格递减的函数，从 $\|f\|^2$ 趋于 $0$；这证明存在与唯一性。置

$$
u_n=(I+\lambda_n A^nA^{*n})^{-1}f,
\quad x_n=\lambda_n A^{*n}u_n,
\quad z_n=f-u_n
=\frac{\lambda_n W_n^2}{1+\lambda_n W_n^2}f.
\tag{3.4}
$$

式 (3.3) 给 $\|u_n\|=\beta\|f\|$。若 $x_n+d\in\mathcal C_n$，展开 $\|u_n-A^nd\|^2\le\|u_n\|^2$ 得

$$
\operatorname{Re}\langle d,x_n\rangle
=\lambda_n\operatorname{Re}\langle A^nd,u_n\rangle
\ge\frac{\lambda_n}{2}\|A^nd\|^2\ge0.
$$

故 $\|x_n+d\|^2\ge\|x_n\|^2+\|d\|^2$，验证公式给出的确是唯一最小元。此处 $u_n$ 是残差。

现在写 $2^k\le n<2^{k+1}$，并令

$$
m=k+r-1,\qquad G_n=\mathbb Z_2\setminus E(n,2^{m+1}).
\tag{3.5}
$$

点 $y\in G_n$ 的整数段 $y,y-1,\dots,y-n+1$ 不含 $2^{m+1}$ 的倍数。因此该段所有 $v_2$ 值至多为 $m$。对每个 $j\le m$，其中 $v_2=j$ 的项数至多 $n/2^j+1$，于是由 (2.1)

$$
\begin{aligned}
-\log W_n(y)
&\le400\sum_{j=0}^{m}(n2^{-j}+1)16^j\\
&\le400\left(\frac87 n8^m+\frac{16}{15}16^m\right)\\
&=400\left(\frac87\frac n{2^m}+\frac{16}{15}\right)16^m
\le1400\,16^m.
\end{aligned}
\tag{3.6}
$$

最后用了 $n/2^m<2^{2-r}\le2$；事实上 (1.3) 给 $r\ge5$，所以常数有富余。置

$$
L_n=e^{-1400\,16^m};\qquad W_n\ge L_n\quad\text{于 }G_n.
\tag{3.7}
$$

另一方面，

$$
\mu(G_n^c)=\frac n{2^{m+1}}<2^{1-r}\le\frac{\beta^2}{8}.
\tag{3.8}
$$

对 $h=|f|^2$ 使用 (2.3)，得到对充分大 $n$，

$$
\int_{G_n^c}|f|^2\,d\mu\le\frac{\beta^2}{4}\|f\|^2.
\tag{3.9}
$$

由 (3.3)、(3.7)、(3.9)，

$$
\beta^2\|f\|^2
\le\frac{\|f\|^2}{(1+\lambda_n L_n^2)^2}
+\frac{\beta^2}{4}\|f\|^2.
$$

因此

$$
\boxed{\lambda_nL_n^2\le C_\beta:=\frac2{\sqrt3\,\beta}-1.}
\tag{3.10}
$$

$C_\beta>0$，因为 $0<\beta<1$。这里没有把一般 $f$ 当成高位独立随机变量；(3.9) 只是在 $n\to\infty$ 的极限中利用柱函数逼近。

## 4. 正测度移动稀疏层迫使所有候选强极限为零

定义

$$
E_n=E(n,2^{m+3}).
\tag{4.1}
$$

对 $y\in E_n$，段 $y,y-1,\dots,y-n+1$ 含一个 $2^{m+3}$ 的倍数。因此至少一个因子具有 $v_2\ge m+3$。由 (2.1) 且其余权不超过 $1$，

$$
W_n(y)\le e^{-16^{m+3}}=e^{-4096\,16^m}=:U_n.
\tag{4.2}
$$

在恰好碰到 $0$ 的有限个点，$W_n=0$，同一不等式仍成立。联合 (3.10)，于 $E_n$ 有

$$
0\le\frac{\lambda_n W_n(y)^2}{1+\lambda_n W_n(y)^2}
\le C_\beta\left(\frac{U_n}{L_n}\right)^2
=C_\beta e^{-5392\,16^m}\longrightarrow0.
\tag{4.3}
$$

于是

$$
\|\mathbf1_{E_n}z_n\|\le
C_\beta e^{-5392\,16^m}\|f\|\longrightarrow0.
\tag{4.4}
$$

而

$$
\mu(E_n)=\frac n{2^{m+3}}
=\frac n{2^{k+r+2}}
\ge2^{-r-2}=p_\beta>0.
\tag{4.5}
$$

给任意固定 $z\in H$，再次由 (2.3)，

$$
\|\mathbf1_{E_n}z\|^2-\mu(E_n)\|z\|^2\longrightarrow0.
\tag{4.6}
$$

所以三角不等式给

$$
\begin{aligned}
\liminf_n\|z_n-z\|
&\ge\liminf_n\bigl(\|\mathbf1_{E_n}z\|-\|\mathbf1_{E_n}z_n\|\bigr)\\
&\ge\sqrt{p_\beta}\|z\|.
\end{aligned}
$$

这就是 (1.4)。式 (1.5) 来自 $\|f-z_n\|=\beta\|f\|$。另外

$$
\|z_n-z\|\ge(1-\beta)\|f\|-\|z\|.
$$

对 $s=\|z\|$ 使用

$$
\max\{\sqrt{p_\beta}s,(1-\beta)\|f\|-s\}
\ge\frac{\sqrt{p_\beta}}{1+\sqrt{p_\beta}}(1-\beta)\|f\|
$$

便得 (1.6)。若一个子列强收敛到 $z$，(1.4) 迫使 $z=0$，而 (1.5) 排除这个强极限。因此无强收敛子列。证毕。

**稳健形式。** 相同论证适用于变化误差 $\beta_n\in[\beta_0,\beta_1]\subset(0,1)$：在 (1.3)、(3.8) 选 $\beta_0$，在参数上界选 $C_{\beta_0}$，在非零范数下界选 $(1-\beta_1)\|f\|$。若目标 $f_n\to f\ne0$ 于 $L^2$，也同样成立，因为 $|f_n|^2\to|f|^2$ 于 $L^1$，§2.2 的逼近误差和范数界仍统一。

## 5. Dyadic 精确弱极限与强缺口

全指数结论不需要本节；本节给更精确的 dyadic 数值并核实所有阈值边界。

令 $n=2^k$，$s_k(y)=v_2(\lfloor y/2^k\rfloor)$（删去最低 $k$ 位后尾部的 $2$-进赋值），并置

$$
C_k=\prod_{j=0}^{k-1}a_j^{2^{k-j-1}}.
$$

R9 的段乘积恒等式给

$$
W_{2^k}(y)=C_k a_{k+s_k(y)}.
\tag{5.1}
$$

取整数 $\ell\ge0$ 满足

$$
2^{-\ell-1}\le\beta^2\le2^{-\ell},
\quad p=2^{-\ell-1},
\quad c=\sqrt{2^{\ell+1}\beta^2-1}\in[0,1],
\quad M=p(1+c).
\tag{5.2}
$$

定义序列

$$
q_s=\begin{cases}
0,&s<\ell,\\
c,&s=\ell,\\
1,&s>\ell.
\end{cases}
\tag{5.3}
$$

则

$$
\boxed{u_{2^k}\rightharpoonup Mf,\qquad
z_{2^k}\rightharpoonup(1-M)f,}
\tag{5.4}
$$

以及

$$
\boxed{\|z_{2^k}-(1-M)f\|^2
\longrightarrow(\beta^2-M^2)\|f\|^2>0.}
\tag{5.5}
$$

**证明。** 用 (3.4) 记

$$
q_{k,s}=\frac1{1+t_k(a_{k+s}/a_k)^2},
\qquad t_k=\lambda_{2^k}C_k^2a_k^2.
$$

则 $u_{2^k}=q_{k,s_k(\cdot)}f$。对固定 $s$，

$$
\frac{a_{k+s+1}}{a_{k+s}}\longrightarrow0,
\tag{5.6}
$$

由 (1.1) 直接得出。每列 $q_{k,s}$ 关于 $s$ 单调不减，取任意子列，可再次选子列使每个 $s$ 上都有极限 $q'_s\in[0,1]$。若 $q'_s>0$，则 $t_k(a_{k+s}/a_k)^2$ 有界，故 (5.6) 迫使 $q'_{s+1}=1$。等价地，若 $q'_{s+1}<1$，则 $q'_s=0$。

对任意高位尾部可测且有界的函数 $h_k$，低位柱函数逼近给

$$
\int |f|^2h_k\,d\mu-\|f\|^2\int h_k\,d\mu\longrightarrow0
\tag{5.7}
$$

且误差对 $\|h_k\|_\infty\le1$ 一致。确切地，对任意低 $d$ 位柱函数 $g_d$ 逼近 $|f|^2$，当 $k\ge d$ 时独立性使 $g_d$ 的两积分相同，而余项至多 $2\||f|^2-g_d\|_1$。

因 $\mu\{s_k=s\}=2^{-s-1}$，将 (5.7) 用于 $q_{k,s_k}^2$，再用离散支配收敛，得到

$$
\sum_{s\ge0}2^{-s-1}(q'_s)^2=\beta^2.
\tag{5.8}
$$

前述相邻关系表明 $q'_s$ 必为“若干个零、至多一个处于 $(0,1)$ 的值、其余全一”；全零与全一由 $0<\beta<1$ 排除。式 (5.8) 唯一确定该序列为 (5.3)。因为任何子列都有这个唯一极限，所以 $q_{k,s}\to q_s$ 对每个 $s$ 成立。再用离散支配收敛和 (5.7)，

$$
\|u_{2^k}-q_{s_k(\cdot)}f\|\longrightarrow0.
\tag{5.9}
$$

对固定 $g\in H$，用相同柱逼近处理 $f\overline g\in L^1$，得到 $q_{s_k(\cdot)}f\rightharpoonup(\sum_s2^{-s-1}q_s)f=Mf$。同理

$$
\|(q_{s_k(\cdot)}-M)f\|^2
\longrightarrow
\left(\sum_s2^{-s-1}q_s^2-M^2\right)\|f\|^2
=(\beta^2-M^2)\|f\|^2.
$$

联合 (5.9) 即得 (5.4)–(5.5)。严格正性是非恒定随机变量 $q_s$ 的方差为正；也可直接代入 (5.2)。当 $\ell=0$ 时该方差是 $(1-c)^2/4>0$，因为 $\beta<1$；当 $\ell\ge1$ 时，由 $(1+c)^2\le2(1+c^2)$ 得到

$$
\beta^2-M^2\ge(1-2p)\beta^2\ge\frac12\beta^2>0.
$$

**阈值边界。** 若 $\beta^2=2^{-\ell}$，则 (5.2) 可取 $c=1$，也可在前一层取 $c=0$；两种表示给完全相同的序列 $q_s$、相同 $M=\beta^2$，且方差为 $\beta^2(1-\beta^2)$。因此没有遗漏误差恰为二进阈值的情形。证毕。

## 6. 剩余范围

本文证明只排除了在当前 $A$ 上采用固定非零目标和非退化误差、要求 backward-minimal images 强紧的方案，且排除已经覆盖所有整数指数。它没有排除误差趋于 $0$ 或 $1$、目标逃逸且无强收敛子列、其他重新归一化、或不依赖像强紧性的方法。最主要的非零向量对全部矩消失问题仍没有解决。
