# R182：标量有理 C(X) 的最大闭分式场与完整谱分类

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R182。

状态：完整证明。本稿只处理一个实际闭一阶乘子的标量有理函数。全空间得到忠实闭分式场；未知不变限制上只保留明确的最大闭关系及既约参数图核心，不预设其定义域稠密。

## 1. 设置

设

$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad 0\ne a\in\ell^2,
$$

$X=X_u$ 为 R125 的实际闭一阶乘子。

R172、R176 已证明：

1. 所有自然幂及非零标量多项式 $p(X)$ 闭、稠密定义，准确域为 $\operatorname{Dom}X^{\deg p}$。
2. 每个非零标量多项式 $p(X)$ 在全 $H$ 上单射、值域稠密，且 $C$ 自伴。
3. R128/R140 的固定共同正则器 $R(t)\in\mathfrak C=\{A\}'$ 是单射稠密的收缩，$R(t)\to I$ 强，并满足

$$
S(t)=XR(t)\in\mathfrak C,\qquad
X^kR(t)^d=S(t)^kR(t)^{d-k}\quad(0\le k\le d).
\tag{1.1}
$$

4. 对 $s,t>0$，

$$
R(s)=R(t)U(s,t),
\tag{1.2}
$$

其中 $U(s,t)\in\mathfrak C$ 是有界单位。它及其逆保持全部闭 $A$ 不变空间及其有限放大。
5. $\mathfrak C$ 交换，其元素均 $C$ 对称，并且 $\mathfrak C$ 是 $\mathbb C[A]$ 的强算子闭包。

以下所有标量有理函数都以实际 $X$ 为变量。它们不是点态符号 $u$ 的普通有理函数乘法。

## 2. 固定共同正则器具有强主理想单位

固定 $t>0$ 及整数 $N\ge0$。由 (1.2)，

$$
R(s)^N=R(t)^NU(s,t)^N.
$$

对固定 $s$，用 $\mathbb C[A]$ 在 $\mathfrak C$ 中的强稠密性逼近 $U(s,t)^N$。因此 $R(s)^N$ 属于 $R(t)^N\mathbb C[A]$ 的强闭包。再令 $s\downarrow0$，得到

$$
\boxed{I\in\overline{R(t)^N\mathbb C[A]}^{\rm SOT}.}
\tag{2.1}
$$

等价地，对任意有限个向量及任意误差，可以先固定一个小 $s$，再选一个实际多项式，完成两层逼近。

所以，对每个有限放大中的闭 $A$ 不变空间 $\mathcal M$，

$$
\boxed{\overline{R(t)^{N\,\oplus d}\mathcal M}=\mathcal M.}
\tag{2.2}
$$

因为多项式保持 $\mathcal M$，(2.1) 在每个向量上直接给稠密性。

这是本稿参数闭图的通用分母。它没有断言任意 $p(X)R(t)^d$ 都有同样的强主理想性质。

## 3. 一个既约有理函数的最大闭实现

取非零标量多项式 $p,q$，先假设它们互素。设

$$
r(z)=\frac{p(z)}{q(z)},\qquad
d=\max(\deg p,\deg q),\qquad R=R(t),\quad S=XR.
$$

定义真正有界算子

$$
F=p(X)R^d=\sum_kp_kS^kR^{d-k},\qquad
G=q(X)R^d=\sum_kq_kS^kR^{d-k}.
\tag{3.1}
$$

它们属于 $\mathfrak C$，因而交换且 $C$ 对称。两者均单射、值域稠密。

为核对最后的稠密性：若 $n=\deg p\le d$，对任意 $x\in\operatorname{Dom}X^n$，

$$
R(s)^dx\to x,\qquad
p(X)R(s)^dx=R(s)^dp(X)x\to p(X)x.
$$

而所有 $R(s)^dH$ 都等于固定 $R(t)^dH$。因此 $R^dH$ 是 $p(X)$ 的图核心，$\overline{\operatorname{Ran}F}=H$。$G$ 同理。

定义

$$
\boxed{
\operatorname{Graph}T_r
=\{(x,y)\in H\oplus H:Fx=Gy\}.
}
\tag{3.2}
$$

$G$ 单射，故这是一张单值闭图。因为有界因子交换，

$$
(Gh,Fh)\in\operatorname{Graph}T_r\qquad(h\in H).
\tag{3.3}
$$

于是定义域包含 $\operatorname{Ran}G$，像包含 $\operatorname{Ran}F$。两者均稠密。又 $F$ 单射，所以

$$
\ker T_r=0.
\tag{3.4}
$$

对 $r=0$，另定义 $T_0=0$ 于全 $H$；常数有理函数按常数算子处理。

## 4. 实际 Bézout 证书与原参数图核心

互素标量多项式给

$$
a(z)q(z)+b(z)p(z)=1
$$

的标量多项式解。取 $e=\max(\deg a,\deg b)$，并定义

$$
L=a(X)R^e,\qquad K=b(X)R^e.
$$

它们是有界交换子，真实自然域计算给

$$
\boxed{LG+KF=R^{d+e}=:D.}
\tag{4.1}
$$

取任意 $(x,y)$ 满足 $Fx=Gy$。令

$$
h=Lx+Ky.
$$

利用交换性，

$$
Gh=LGx+KGy=LGx+KFx=Dx,
$$

$$
Fh=LFx+KFy=LGy+KFy=Dy.
$$

因此

$$
(Dx,Dy)\in\{(Gh,Fh):h\in H\}.
\tag{4.2}
$$

最大图 (3.2) 是闭 $A\oplus A$ 不变空间。由 (2.2)，$D\oplus D$ 在该图上的像稠密。结合 (4.2)，

$$
\boxed{
\operatorname{Graph}T_r
=\overline{\{(Gh,Fh):h\in H\}}.
}
\tag{4.3}
$$

这明确证明原分母参数图是最大闭分式图的核心，不只给形式商。

还可以使用未归一化的真实自然参数：

$$
\boxed{
\operatorname{Graph}T_r
=
\overline{
\{(q(X)v,p(X)v):v\in\operatorname{Dom}X^d\}
}.
}
\tag{4.4}
$$

一方面 (3.3) 是 (4.4) 的子集。另一方面，对 $v\in\operatorname{Dom}X^d$，用 $R(s)^dv$ 作自然幂图逼近；其 $p(X)$、$q(X)$ 像分别趋于 $p(X)v$、$q(X)v$，并且逼近对都属于 (3.3) 的参数图。最大图闭，得到反向包含。

## 5. 分式表示、次数与正则器的独立性

### 5.1 增大归一化次数

把 $d$ 换成 $d+k$ 时，$F,G$ 同时乘以单射 $R^k$。于是

$$
R^kFx=R^kGy\Longleftrightarrow Fx=Gy.
$$

最大图不变。因 $\operatorname{Ran}R^k$ 稠密，新的原参数图也在旧原参数图中稠密，所以其闭包不变。

### 5.2 更换 $t$

由 (1.2)，新 $F,G$ 同时乘以有界单位 $U(s,t)^d$；它与全部因子交换。因此最大图和原参数图闭包均不变。

### 5.3 非既约表示

若将 $p,q$ 同乘非零标量多项式 $h$，把归一化次数取为 $d+\deg h$，则新的有界对是

$$
F'=[h(X)R^{\deg h}]F,\qquad
G'=[h(X)R^{\deg h}]G.
$$

方括号算子在全 $H$ 上单射稠密。因此可以在最大图方程中实际消去这个共同有界因子，所得最大图仍为 (3.2)。

原参数图方面，$\operatorname{Ran}[h(X)R^{\deg h}]$ 在 $H$ 稠密；有界列映射 $v\mapsto(Gv,Fv)$ 把其稠密像送成原参数图中的稠密子集。所以全空间原参数图闭包仍相等。

任意两个表示同一标量有理函数的多项式对，经约分和共同倍数均可连接，故

$$
\boxed{T_r\text{ 只依赖 }r\in\mathbb C(z).}
\tag{5.1}
$$

全空间稠密性在这一段有实质作用；§8 将明确不把它无条件传到限制。

## 6. C 自伴、定义域交换与实际闭场运算

### 6.1 整个通常伴随域

由 (4.3)，向量 $z$ 属于 $\operatorname{Dom}T_r^*$ 且 $T_r^*z=w$，当且仅当

$$
F^*z=G^*w.
$$

$F^*=CFC$、$G^*=CGC$，因此该条件等价于

$$
F(Cz)=G(Cw),
$$

即 $(Cz,Cw)\in\operatorname{Graph}T_r$。所以

$$
\boxed{T_r^*=CT_rC.}
\tag{6.1}
$$

对任意 $B\in\mathfrak C$，若 $Fx=Gy$，则

$$
F(Bx)=B(Fx)=B(Gy)=G(By).
$$

故

$$
\boxed{
B\operatorname{Dom}T_r\subseteq\operatorname{Dom}T_r,\qquad
T_rBx=BT_rx.
}
\tag{6.2}
$$

### 6.2 加法与乘法取闭包

设 $r_i=p_i/q_i$，对应有界对为 $F_i,G_i$。则交域上的自然和包含参数图

$$
(G_1G_2h,\ (F_1G_2+F_2G_1)h).
$$

这正是 $r_1+r_2$ 的一个实际归一化表示的原参数图。由 §5，其全空间闭包是最大图。另一方面，在自然交域上乘以 $G_1G_2$，可直接验证自然和包含于同一最大图。因此

$$
\boxed{\overline{T_{r_1}+T_{r_2}}=T_{r_1+r_2}.}
\tag{6.3}
$$

自然乘积的域包含 $\operatorname{Ran}(G_1G_2)$，因为

$$
T_{r_2}G_1G_2h=F_2G_1h\in\operatorname{Ran}G_1.
$$

在那里乘积值为 $F_1F_2h$。一般自然乘积域中的向量同样满足最大方程

$$
G_1G_2(T_{r_1}T_{r_2}x)=F_1F_2x.
$$

再用原参数图核心，得到

$$
\boxed{\overline{T_{r_1}T_{r_2}}=T_{r_1r_2}.}
\tag{6.4}
$$

这些自然和、乘积的域都稠密，因为包含相应有界单射稠密分母的像。

非零 $r$ 的最大图翻转给

$$
\boxed{T_r^{-1}=T_{1/r}}
\tag{6.5}
$$

于准确逆域 $\operatorname{Ran}T_r$ 上。每个非零 $T_r$ 都单射稠密，因此这里确为稠密定义的闭逆。

常数函数与自然多项式得到其原来的实际算子；多项式的识别也可直接用 R176 的最大图。若 $r\ne0$，$T_r$ 单射，故不可能为零算子。因此

$$
r\longmapsto T_r
$$

是忠实的 $\mathbb C(z)$ 闭分式场实现。这里“场运算”是 (6.3)—(6.5) 的真实图闭包运算，不表示所有自然乘积本来已经闭。

### 6.3 所有标量移位

若 $r$ 非恒定，则对每个 $\lambda$，$r-\lambda\ne0$。由于闭算子加有界标量已闭，

$$
\boxed{T_r-\lambda I=T_{r-\lambda}}
\tag{6.6}
$$

且域不变。所以每个标量移位都单射、值域稠密。任意非空谱均只能是连续谱。

## 7. 原空间谱的完整分类

以下 $r=p/q$ 始终约为互素，且非恒定。

### 7.1 第一阶有全复平面谱

假设 $a\notin\ell^1$ 且没有可和相位缺陷方向。由 R138，$\sigma(X)=\mathbb C$；R181 更给：对每个 $\mu$，存在有限柱单位向量 $x_m$，使

$$
\|(X-\mu I)^kx_m\|\to0
\quad\text{对全部固定 }k.
\tag{7.1}
$$

固定任意 $\lambda$，设

$$
h_\lambda(z)=p(z)-\lambda q(z).
$$

如果 $T_r-\lambda I$ 有全域有界逆，则由 (6.5)—(6.6)，这个逆准确为

$$
T_{q/h_\lambda}.
\tag{7.2}
$$

若 $h_\lambda$ 非常数，取一个根 $\mu$。互素性给 $q(\mu)\ne0$。对 (7.1) 的序列，

$$
\|h_\lambda(X)x_m\|\to0,\qquad
\|q(X)x_m-q(\mu)x_m\|\to0.
$$

原参数图保证真实等式

$$
T_{q/h_\lambda}\,h_\lambda(X)x_m=q(X)x_m
$$

成立；所有输入都是有限柱，属于所需的全部自然幂域。有界逆假设遂产生

$$
|q(\mu)|+o(1)
\le\|T_{q/h_\lambda}\|\,
\|h_\lambda(X)x_m\|\longrightarrow0,
$$

矛盾。

若 $h_\lambda$ 为非零常数，则 (7.2) 是非恒定标量多项式 $q(X)/h_\lambda$。$q$ 必须非常数，否则 $r$ 也恒定。R171 已证明这类自然多项式无界，仍与有界逆矛盾。

因此

$$
\boxed{
\sigma(T_r)=\mathbb C,
\quad\mathbb C\text{ 全部为连续谱}.
}
\tag{7.3}
$$

特别，这个分支中 $\mathbb C(X)$ 的有界成员只有常数。没有把有理函数的极点跳过，也没有只用形式谱映射。

### 7.2 第一阶空谱

假设 $a\notin\ell^1$ 且存在可和相位缺陷方向。令

$$
R_0=X^{-1}.
$$

由 R138/R134，$R_0$ 是有界拟幂零交换子。设 $m=\deg p$、$n=\deg q$，并定义逆向多项式

$$
\widetilde p(z)=z^mp(1/z),\qquad
\widetilde q(z)=z^nq(1/z).
$$

两者在0处非零，故 $\widetilde p(R_0)$、$\widetilde q(R_0)$ 都是实际有界单位。由闭场恒等式，

$$
T_r=X^{m-n}U(R_0),\qquad
U=\widetilde p/\widetilde q,
\tag{7.4}
$$

其中当 $m<n$ 时 $X^{m-n}=R_0^{n-m}$。有界单位与 $X$ 域交换，所以正幂情形 (7.4) 是准确自然闭域上的等式。

若 $m\le n$，即 $r$ 在无穷远点有限，则 $T_r$ 有界，且拟幂零算子的通常全纯演算给

$$
\boxed{\sigma(T_r)=\{r(\infty)\}.}
\tag{7.5}
$$

由于 $r$ 非恒定，§6.3 给这个唯一谱点是连续谱。

若 $m>n$，令 $k=m-n\ge1$。对任意 $\lambda$，

$$
T_r-\lambda I=[U(R_0)-\lambda R_0^k]X^k.
$$

方括号在0处的标量值为 $p_m/q_n\ne0$，所以实际可逆。逆为

$$
R_0^k[U(R_0)-\lambda R_0^k]^{-1}.
$$

故

$$
\boxed{
r\text{ 在 }\infty\text{ 有极点}
\ \Longrightarrow\
T_r\text{ 无界且 }\sigma(T_r)=\varnothing.
}
\tag{7.6}
$$

“无界”也由非零 Hilbert 空间上的有界算子必有非空谱得到；这里同时已有准确的正自然幂形式。

### 7.3 第一阶有界、单点谱

假设 $a\in\ell^1$，置

$$
c=a_*+\sum_ja_j,\qquad N=X-cI.
$$

则 $N\in\mathcal A$ 是非零、单射稠密的拟幂零算子。

若 $q(c)\ne0$，$r$ 在 $c$ 正则，通常全纯演算给

$$
\boxed{T_r=r(X)\in\mathcal A,\qquad\sigma(T_r)=\{r(c)\}.}
\tag{7.7}
$$

非恒定时该谱点仍为连续谱。

若 $q(c)=0$，互素性保证 $p(c)\ne0$。设 $q$ 在 $c$ 的零阶为 $k\ge1$。则

$$
T_r=N^{-k}V(N),
\tag{7.8}
$$

其中 $V$ 是在0附近解析、$V(0)\ne0$ 的实际单位函数。最大闭域为

$$
\operatorname{Dom}T_r=\operatorname{Ran}N^k.
$$

这是因为 $V(N)$ 及其有界逆都与 $N$ 交换，故保持 $\operatorname{Ran}N^k$。对任意 $\lambda$，

$$
(T_r-\lambda I)^{-1}
=N^k[V(N)-\lambda N^k]^{-1}
$$

是有界全域逆。因此

$$
\boxed{
r\text{ 在 }c\text{ 有极点}
\ \Longrightarrow\
T_r\text{ 无界且 }\sigma(T_r)=\varnothing.
}
\tag{7.9}
$$

该分支并不需要慢 $N$ 属于 $\mathcal G$；它只用单点谱、真实有界因子和完整最大图。

### 7.4 汇总

对非恒定标量有理函数，全部情况是：

| 第一阶 $X$ | $r$ 的相关极点 | $T_r$ 有界性 | 谱 |
|---|---|---|---|
| $\sigma(X)=\mathbb C$ | 任意 | 无界 | $\mathbb C$，全连续谱 |
| $\sigma(X)=\varnothing$ | 在 $\infty$ 有极点 | 无界 | 空 |
| $\sigma(X)=\varnothing$ | 在 $\infty$ 有限 | 有界 | $\{r(\infty)\}$，连续谱 |
| $X\in\mathcal A,\ \sigma(X)=\{c\}$ | 在 $c$ 有极点 | 无界 | 空 |
| $X\in\mathcal A,\ \sigma(X)=\{c\}$ | 在 $c$ 正则 | 有界 | $\{r(c)\}$，连续谱 |

例如在 full-plane 第一阶分支，$X^{-1}$、$(X-I)(X+I)^{-1}$ 的最大闭实现也都具有全复平面的连续谱；在 empty-spectrum 第一阶分支，$X^{-1}$ 则是有界拟幂零算子。

## 8. 未知不变空间上保留的准确闭关系

令 $M$ 为任意闭 $A$ 不变空间。对一个既约表示 $r=p/q$，仍以 (3.1) 的有界 $F,G$ 定义

$$
\mathcal R_{r,M}
=\{(x,y)\in M\oplus M:Fx=Gy\}.
\tag{8.1}
$$

它是单值闭关系，等于全空间最大图与 $M\oplus M$ 的交。没有预先断言其定义域稠密，也没有断言全空间 $T_r$ 将全部 $\operatorname{Dom}T_r\cap M$ 送回 $M$。

既约 Bézout 证书 (4.1) 以及 (2.2) 在此图上仍适用，所以

$$
\boxed{
\mathcal R_{r,M}
=\overline{\{(Gh,Fh):h\in M\}}.
}
\tag{8.2}
$$

因此其定义域与像的闭包准确为

$$
\boxed{
\overline{\operatorname{Dom}\mathcal R_{r,M}}
=\overline{GM},\qquad
\overline{\operatorname{Ran}\mathcal R_{r,M}}
=\overline{FM}.
}
\tag{8.3}
$$

第一式的反向包含来自每个图向量都是参数图极限，第二式相同。不能把全 $H$ 上 $G,F$ 稠密值域无条件传给 $M$。

更换 $t$、增大归一化次数不会改变最大关系。最大方程中的非零共同标量多项式因子也仍可消去，因为对应有界算子在原 $H$ 单射。但非既约表示的原参数图在 $M$ 上不一定已经知道是核心：

例如恒等有理函数 $1=h/h$ 的最大图是整个对角 $M$，而该非既约原参数图的闭包首先只是

$$
\{(x,x):x\in\overline{h(X)R^dM}\}.
$$

它等于全部对角图需要相应限制稠密性，当前一般情形未知。

所以本稿不宣称全部限制上已经得到一个稠密定义的分式场，也不在这些限制上自动搬用 §6 的闭场加乘。全空间的域、原参数核心及场运算均已完整证明。

## 9. 与已有有界分式场及主核问题的区分

本稿的变量 $X$ 可以是真正无界的一阶乘子，其共同有界正则器通常在 $\mathcal A$ 和 UHF 之外。它不同于 R153 的 $\operatorname{Frac}\mathcal G$，也不同于仅以有界慢方向为变量的闭分式场。

R170 已说明：无界一阶 $X$ 不可能本身成为非零 $\mathcal A$ 分母的实际最大闭商。本稿没有与此冲突；这里的 $G=q(X)R(t)^d$ 一般只是 $\{A\}'$ 中的有界分母，不能自动放入 $\mathcal A$。

全部 $p,q$ 都是标量多项式，所以 R172 给的单射稠密性确实适用于分子分母。若换成 Bell 或一般 $\mathcal A$ 系数多项式，其核可能未知，不能照搬 §3 的单值闭分式及 §6 的场结论。

本稿也没有把 $r(X)$ 当成点态 $r(u)$ 的乘子。一般点态 Bell 核、慢平方共振和完整 Hilbert 不变子空间问题仍未解决。
