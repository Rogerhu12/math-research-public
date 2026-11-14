# R291 附录：真实固定头距离证书、有限矩预算与尾谱病态下界

2026-11-14，normal-annihilator / 789f。**状态：本稿各恒等式与界已证明；所有距离常数保留固定头、原态矩及实际逆元费用，不给移动头的一致下界。**

继续 [R291](R291-normal-moment-module-independence-and-exponential-support-rank-growth.md)。本稿先记录同一有限秩正链的必然谱病态，再把 R291 的代数独立性化为原有界算子中的准确距离证书。最后得到由有限个实际矩控制的谱尾质量下界。它仍未排除一般有限秩正常湮灭者。

## 1. 同一有限秩正链的最小特征值上界

设原正正常湮灭密度满足

$$
\rho\ge0,\qquad \operatorname{Tr}\rho=1,\qquad
\operatorname{rank}\rho=r<\infty.
$$

取 [R253](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) 的同一相容尾边缘

$$
\nu_m=\operatorname{Tr}_{<m}\rho,
\qquad
\delta_m=1-\langle\nu_m\Omega_m,\Omega_m\rangle\longrightarrow0.
$$

写 $d_m=\operatorname{rank}\nu_m$。R291 及有限头部分迹给

$$
D_m:=\left\lceil2^{m/2}\right\rceil\le d_m\le r2^m.
\tag{1.1}
$$

对 $m\ge1$，有 $D_m\ge2$，所以 $\delta_m>0$：若 $\delta_m=0$，正性与迹为一迫 $\nu_m=|\Omega_m\rangle\langle\Omega_m|$，其秩为一，与 (1.1) 矛盾。

把 $\nu_m$ 的正特征值递减排列为 $\lambda_1\ge\cdots\ge\lambda_{d_m}>0$。Rayleigh 商给 $\lambda_1\ge1-\delta_m$，故

$$
\sum_{i=2}^{d_m}\lambda_i\le\delta_m,
\qquad
\boxed{\lambda_{d_m}\le\frac{\delta_m}{d_m-1}
\le\frac{\delta_m}{D_m-1}.}
\tag{1.2}
$$

在真实支撑 $E_m=\operatorname{ran}\nu_m$ 上，因 $d_m<\infty$，逆平方根是有界算子，并且

$$
\boxed{
\|\nu_m^{-1/2}\|_{E_m\to E_m}
\ge\sqrt{\frac{D_m-1}{\delta_m}}.
}
\tag{1.3}
$$

这里有限原秩用于保证每个尾边缘有限秩。没有在整个尾空间上定义有界逆平方根。(1.3) 说明用密度逆平方根归一化 R276 的共同列 Gram 时至少须支付这项费用；它没有给出熵下界。大支撑上的极小正特征值仍可与 [R289](R289-finite-rank-tail-entropy-density-and-compatible-arbitrarily-slow-rank-two-chains.md) 的 $\mathsf S(\nu_m)=o(m)$ 相容。

## 2. 低算子 Schmidt 秩比较项给出有限次数的真实多项式关系

下文固定一个原 Haar 模型或真实尾，沿用 R291 的记号

$$
H=\mathbb C^q\otimes H_{\rm far},\qquad q=2^M,\ M\ge1,
$$

$$
T=J(z)=\sum_{i=1}^{q-1}c_i e_{i,i-1}\otimes I
+\beta^{-1}e_{0,q-1}\otimes z,
\qquad \beta=\prod_{i=1}^{q-1}c_i>0,
\qquad T^q=I_q\otimes z,
\tag{2.1}
$$

$$
R=\overline{\mathbb C[I,z]}^{\|\cdot\|},\qquad
\mathcal B=\overline{\mathbb C[I,T]}^{\|\cdot\|}
=\bigoplus_{j=0}^{q-1}T^jR.
$$

这里的 $c_i$ 全是原物理头权；$z$ 是原远尾生成元的正标量倍数。取首形式阶为一的实际符号

$$
S=\sum_{j=0}^{q-1}T^jb_j,\qquad b_j\in R,
\qquad \chi(S)=0,\quad \chi(b_1)\ne0,
\tag{2.2}
$$

以及实际迹类湮灭者

$$
\operatorname{Tr}\rho=\tau\ne0,
\qquad \operatorname{Tr}(\rho SG)=0\quad(G\in\mathcal B).
\tag{2.3}
$$

本节至第 5 节不要求 $\rho$ 正。

设一个比较迹类算子有表示

$$
\sigma=\sum_{\ell=1}^{k}A_\ell\otimes\omega_\ell,
\qquad A_\ell\in M_q(\mathbb C),\quad
\omega_\ell\in\mathcal S_1(H_{\rm far}),\qquad k<q.
\tag{2.4}
$$

定义实际矩泛函

$$
\psi_j^\rho(F)=\operatorname{Tr}\bigl[\rho T^j(I_q\otimes F)\bigr],
\qquad
\psi_j^\sigma(F)=\operatorname{Tr}\bigl[\sigma T^j(I_q\otimes F)\bigr]
\quad(F\in R).
$$

对 $0\le j<q$，

$$
\psi_j^\sigma=\sum_{\ell=1}^k m_{\ell j}(z)\varphi_{\omega_\ell},
\qquad
m_{\ell j}(z)=\operatorname{Tr}(A_\ell J(z)^j).
\tag{2.5}
$$

每个 $m_{\ell j}$ 都至多一次：$j<q$ 的每条循环路径至多经过一次含 $z$ 的进位边。

因此存在不全为零的多项式 $a_0,\ldots,a_{q-1}\in\mathbb C[z]$，使

$$
\sum_{j=0}^{q-1}a_j(z)m_{\ell j}(z)=0\quad(1\le\ell\le k),
\qquad
\boxed{\sum_{j=0}^{q-1}a_j\psi_j^\sigma=0\text{ 于 }R.}
\tag{2.6}
$$

还可取

$$
\deg a_j\le k.
\tag{2.7}
$$

为说明此次数界，在 $\mathbb C(z)$ 上取 (2.5) 系数矩阵的秩 $s\le k$。若 $s=0$，取任一标准坐标行即可。否则选取一个非零 $s$ 阶子式，再加一个未选取的列；这 $s+1$ 列上的带符号 $s$ 阶余子式给非零核向量。其各项次数至多 $s$。它先消去所选 $s$ 行，再因这些行张成全行空间而消去所有行。所得恒等式均在 $\mathbb C[z]$ 中成立。

令

$$
P(t)=\sum_{j=0}^{q-1}t^j a_j(t^q)\in\mathbb C[t].
\tag{2.8}
$$

不同余数的指数不重叠，故 $P\ne0$，且可取

$$
\deg P\le D:=qk+q-1.
\tag{2.9}
$$

其实际代入满足

$$
P(T)=\sum_{j=0}^{q-1}T^j(I_q\otimes a_j(z))\in\mathcal B,
\qquad
\operatorname{Tr}\bigl[\sigma P(T)(I_q\otimes F)\bigr]=0
\quad(F\in R).
\tag{2.10}
$$

这没有把尾系数 $b_j$ 当成有理函数；只对有限个物理头矩的仿射多项式做消元。

## 3. 原有界算子中的准确距离恒等式

令 $C=C_q\in M_q(R)$ 是矩递推 companion：

$$
(Cv)_j=v_{j+1}\ (0\le j<q-1),\qquad (Cv)_{q-1}=zv_0,
\qquad C^q=zI_q.
\tag{3.1}
$$

记

$$
s(C)=\sum_{j=0}^{q-1}b_j C^j,
\qquad \psi^\rho=(\psi_0^\rho,\ldots,\psi_{q-1}^\rho)^{\mathsf T}.
$$

R291 的原右源方程准确给

$$
s(C)\psi^\rho=0.
\tag{3.2}
$$

定义 $U\in M_q(R)$ 的第 $j$ 行为 $S^j$ 在 $1,T,\ldots,T^{q-1}$ 中的实际余数系数：

$$
S^j=\sum_{r=0}^{q-1}T^rU_{jr},\qquad 0\le j<q.
\tag{3.3}
$$

**这个 $U$ 是原尾 Banach 代数中的真实单位矩阵。** 事实上，常数字符下 $\chi(U)$ 是三角矩阵，对角元为 $\chi(b_1)^j\ne0$。$R$ 由拟幂零元生成，只有常数字符，所以 $\det U\in R^\times$；伴随矩阵公式给 $U^{-1}\in M_q(R)$。这也是 [R274 §1](R274-full-commutant-basis-and-last-raw-moment-obstruction.md) 的固定 $S$ 幂基在本记号中的版本。没有任何随 $q$ 一致的逆元范数断言。

写 $a=(a_0,\ldots,a_{q-1})$，并令

$$
\mathscr P=P(C)=\sum_{j=0}^{q-1}a_j(z)C^j,
\qquad p(z)=\det\mathscr P.
\tag{3.4}
$$

有 $p\in\mathbb C[z]\setminus\{0\}$：在 $K=\mathbb C(z)$ 上，$t^q-z$ 不可约，而次数小于 $q$ 的 $\sum a_j(z)t^j$ 非零；因此它在域 $K[t]/(t^q-z)$ 中为单位，乘法矩阵 $\mathscr P$ 的行列式非零。

令 $O$ 的第 $j$ 行是 $a\,s(C)^j$，$0\le j<q$。因为 $e_0^{\mathsf T}C^r=e_r^{\mathsf T}$（$r<q$），又因所有系数交换，(3.3) 给

$$
\boxed{O=U\mathscr P.}
\tag{3.5}
$$

这是 $R$ 内的有限矩阵恒等式。若

$$
\eta^\rho=\sum_{j=0}^{q-1}a_j\psi_j^\rho,
$$

则 (3.2) 给 $O\psi^\rho=(\eta^\rho,0,\ldots,0)^{\mathsf T}$。定义

$$
B=\operatorname{adj}(\mathscr P)U^{-1}\in M_q(R),
\qquad c=B_{00}\in R.
\tag{3.6}
$$

由 $BO=pI_q$ 取第一行，得到 $p\psi_0^\rho=c\eta^\rho$。再用 (2.6)，对于每个实际 $F\in R$，有

$$
\boxed{
\operatorname{Tr}\bigl[\rho(I_q\otimes p(z)F)\bigr]
=\operatorname{Tr}\bigl[(\rho-\sigma)P(T)(I_q\otimes cF)\bigr].
}
\tag{3.7}
$$

于是，只要左端非零，就有原迹范数的定量界

$$
\boxed{
\|\rho-\sigma\|_1\ge
\frac{\left|\operatorname{Tr}[\rho(I_q\otimes pF)]\right|}
{\|P(T)(I_q\otimes cF)\|}.
}
\tag{3.8}
$$

非零锚自动保证分母非零。一个较粗但完全有界的预算是

$$
\|P(T)(I_q\otimes cF)\|
\le\|P(T)\|\,\|\operatorname{adj}(\mathscr P)\|\,
\|U^{-1}\|\,\|F\|.
\tag{3.9}
$$

矩阵范数在 $\mathbb C^q\otimes H_{\rm far}$ 上取。物理头 $T$ 与矩递推 $C$ 的范数在这里分别保留，没有通过未运输的相似把二者等同。

## 4. 两种完全明确的非零锚，保留正常阈值与来源范数

写唯一的多项式分解

$$
p(z)=z^d u(z),\qquad d\ge0,\quad u(0)\ne0.
\tag{4.1}
$$

$u(z)^{-1}$ 是原 $R$ 中的实际有界单位逆。

若 $d=0$，取 $F=p(z)^{-1}$，则 (3.7) 左端正是 $\tau$，从而

$$
\boxed{
\|\rho-\sigma\|_1\ge
\frac{|\tau|}{\|P(T)(I_q\otimes cp(z)^{-1})\|}>0.
}
\tag{4.2}
$$

若 $d>0$，对每个满足 $2^n\ge d$ 的 $n$ 定义真实来源

$$
F_n=u(z)^{-1}\frac{z^{2^n-d}}{\|z^{2^n}\|}\in R.
\tag{4.3}
$$

其费用保留为

$$
\|F_n\|\le
\|u(z)^{-1}\|\frac{\|z^{2^n-d}\|}{\|z^{2^n}\|}.
\tag{4.4}
$$

没有给这个比值一致上界。[R12 的真实归一化幂](R12-normalized-powers-and-compact-commutant.md) 给

$$
L_n:=\operatorname{Tr}\left[\rho\left(I_q\otimes
\frac{z^{2^n}}{\|z^{2^n}\|}\right)\right]
\longrightarrow\tau/2.
\tag{4.5}
$$

这里使用的是固定正常 $\rho$ 与一致有界的输出。具体地，选取一个实际依赖于 $\rho,z,d$ 的有限阈值 $n_0$，使所有 $n\ge n_0$ 同时满足

$$
2^n\ge d,\qquad |L_n-\tau/2|\le|\tau|/4.
\tag{4.6}
$$

对每个这样的 $n$，(3.8) 给

$$
\boxed{
\|\rho-\sigma\|_1\ge
\frac{|\tau|}{4\|P(T)(I_q\otimes cF_n)\|}.
}
\tag{4.7}
$$

特别，分母可用 (3.9)、(4.4) 原样估计。$n_0$ 不是对所有正常态一致的阈值，$\|u^{-1}\|$、$\|U^{-1}\|$、$c$、$P(T)$ 和来源幂的范数比都没有被丢掉。这是 R291 无挠性证明的有预算版本。

## 5. 对全部固定低张量秩比较项共同的有限矩证书

本节固定 $q$、$1\le k<q$ 和 $D=qk+q-1$。可以把第 3 节对比较项 $\sigma$ 的多项式依赖收进一个公共常数，但该常数仍依赖原态的实际有限矩。

### 5.1 一组实际归一化幂测试

令 $\varphi_0(F)=\operatorname{Tr}[\rho(I_q\otimes F)]$。R291 §2 的正常无挠性表明

$$
p\varphi_0=0,\quad p\in\mathbb C[z]
\quad\Longrightarrow\quad p=0,
\tag{5.1}
$$

因为 $\varphi_0(I)=\tau\ne0$。因此存在有限个非负整数 $n_0,\ldots,n_D$，使矩阵

$$
H_{ir}=\varphi_0(z^rF_i),\qquad
F_i=\frac{z^{n_i}}{\|z^{n_i}\|},\qquad 0\le i,r\le D,
\tag{5.2}
$$

可逆。证明是：若全部行向量 $(\varphi_0(z^{n+r}))_{r=0}^D$ 的张成维数小于 $D+1$，就有非零次数至多 $D$ 的多项式 $p$，满足 $\varphi_0(pz^n)=0$ 对所有 $n\ge0$ 成立。多项式在 $R$ 中范数稠密，于是 $p\varphi_0=0$，违反 (5.1)。选取有限基行，再按各行对应的非零范数归一化即可。

以后固定一组这样的整数，记

$$
h=\sigma_{\min}(H)>0.
\tag{5.3}
$$

这些整数及 $h$ 都是原正常态的有限矩数据，尚无对移动头或全部正常态的统一控制。

### 5.2 有限多项式的行列式不会无预算消失

把第 2 节的 $P(t)=\sum_{n=0}^D\alpha_nt^n$ 乘一个非零标量，令

$$
\sum_{n=0}^D|\alpha_n|^2=1.
\tag{5.4}
$$

若 $p(z)=\det P(C)$，则

$$
\deg p\le D,\qquad
\|\operatorname{coeff}p\|_2\ge\binom{2D}{D}^{-q/2}.
\tag{5.5}
$$

为给出这个粗而显式的界，记多项式 $f$ 的根乘积量为

$$
\mathcal M(f)=|\operatorname{lead}(f)|
\prod_{f(r)=0}\max(1,|r|).
$$

对实际次数 $d\le D$ 的 $P$，逐项展开根乘积给
$|\alpha_n|\le\binom{d}{n}\mathcal M(P)$。于是由 $\sum_{n=0}^d\binom{d}{n}^2=\binom{2d}{d}\le\binom{2D}{D}$ 及 (5.4)，得到
$\mathcal M(P)\ge\binom{2D}{D}^{-1/2}$。
在 $\lambda^q=z$ 的代数扩张中，

$$
p(z)=\prod_{\zeta^q=1}P(\zeta\lambda).
$$

每个根 $r$ 被送为 $r^q$，首项系数的模取 $q$ 次方，所以 $\mathcal M(p)=\mathcal M(P)^q\ge\binom{2D}{D}^{-q/2}$。最后，圆周上 $\log|e^{it}-r|$ 的均值为 $\log\max(1,|r|)$；对根乘积相加，并用几何均值不超过平方均值和 Parseval，得到 $\mathcal M(p)\le\|\operatorname{coeff}p\|_2$。这证明 (5.5)，也覆盖常数多项式。

### 5.3 真实来源的公共范数预算

定义有限常数

$$
L_T(D)=\left(\sum_{n=0}^{D}\|T^n\|^2\right)^{1/2},
\qquad
L_C(D)=\left(\sum_{n=0}^{D}\|C^n\|^2\right)^{1/2}.
\tag{5.6}
$$

由 (5.4) 及 Cauchy–Schwarz，$\|P(T)\|\le L_T(D)$、$\|\mathscr P\|\le L_C(D)$。
每个 $(q-1)$ 阶子式是 $(q-1)!$ 项的和，各矩阵块范数均不超过 $L_C(D)$；再用 $q\times q$ 块矩阵范数不超过 $q$ 倍最大块范数，得到

$$
\|\operatorname{adj}(\mathscr P)\|
\le q! L_C(D)^{q-1}.
\tag{5.7}
$$

因此对于第 5.1 节每个 $\|F_i\|=1$ 的来源，

$$
\|P(T)(I_q\otimes cF_i)\|
\le K_{q,k}(S,T):=
L_T(D)\,q!L_C(D)^{q-1}\|U^{-1}\|.
\tag{5.8}
$$

这个预算直接采用原有界矩阵 $U^{-1}$，没有把抽象分裂域中的倒数当成新算子。

### 5.4 固定 q 的公共距离下界

令 $v$ 为 $p$ 的系数列，补零到长 $D+1$。由 (5.2)、(5.3)、(5.5)，

$$
\left(\sum_{i=0}^D|\varphi_0(pF_i)|^2\right)^{1/2}
=\|Hv\|_2\ge h\binom{2D}{D}^{-q/2}.
$$

至少一个 $i$ 满足 $|\varphi_0(pF_i)|\ge h\binom{2D}{D}^{-q/2}/\sqrt{D+1}$。应用 (3.8)、(5.8)，对于**每个**算子 Schmidt 秩至多 $k$ 的比较迹类 $\sigma$，得到

$$
\boxed{
\|\rho-\sigma\|_1\ge
\Gamma_{q,k}(\rho,S,T):=
\frac{h\binom{2D}{D}^{-q/2}}
{\sqrt{D+1}\,L_T(D)\,q!L_C(D)^{q-1}\|U^{-1}\|}>0.
}
\tag{5.9}
$$

这里同一个 $H$、同一个 $U$、同一个 $\Gamma$ 对固定 $q,k,\rho,S,T$ 下的全部比较项共同有效。固定有限头下，算子 Schmidt 秩至多 $k$ 的集合本来就是迹范数闭集，故 R291 排除该集合后定性正距离也已存在。本节新增的是仅依赖有限实际矩与有限真实逆元预算的明确证书，及第 6 节的谱质量表达。其大小包含原态的 $h$，且 $D$、$U^{-1}$ 与所有范数都随头改变；(5.9) 不是移动 $q$ 的一致分离。

## 6. 正态真实谱尾质量的定量后果及尚缺费用

设再有 $\rho\ge0$、$\operatorname{Tr}\rho=1$，并记本节固定切分的真实远尾边缘为 $\nu=\operatorname{Tr}_{\mathbb C^q}\rho$。
给定 $d\ge1$ 满足 $d^2<q$，令 $E$ 是 $\nu$ 前 $d$ 个特征向量的张成，$P_E$ 为其投影，

$$
\epsilon_d=\operatorname{Tr}\nu(I-P_E)
=\sum_{j>d}\lambda_j(\nu),
\qquad
\sigma_E=(I_q\otimes P_E)\rho(I_q\otimes P_E).
\tag{6.1}
$$

谱重数处任选 $d$ 维最大特征子空间即可。若尾秩小于 $d$，则已与 R291 矛盾。按 $E$ 的矩阵单位展开，$\sigma_E$ 的算子 Schmidt 秩至多 $d^2$。

正性的直接 Hilbert–Schmidt 因式估计给

$$
\begin{aligned}
\|\rho-\sigma_E\|_1
&\le\|(I-P)\rho\|_1+\|P\rho(I-P)\|_1\\
&\le\sqrt{\epsilon_d}
+\sqrt{(1-\epsilon_d)\epsilon_d}
\le2\sqrt{\epsilon_d},
\qquad P=I_q\otimes P_E.
\end{aligned}
\tag{6.2}
$$

在 (5.9) 取 $k=d^2$，于是

$$
\boxed{
\sum_{j>d}\lambda_j(\nu)
\ge\frac14\Gamma_{q,d^2}(\rho,S,T)^2>0
\qquad(d^2<q).
}
\tag{6.3}
$$

同样，把 $P$ 取为头边缘前 $d$ 个特征向量投影，就得到头边缘的同式下界；使用的实际 $\rho,S,T,H,U$ 不变。

对 R253 的同一链，可在任意 $j\ge0$、任意块长 $M\ge1$，把当前态取为 $\nu_j$、当前首阶一符号取为 $Q_j$、当前生成元取为真实 $\widehat N_j$，逐次应用 (6.3)。每次都是原同一链的实际谱质量约束。

目前尚缺的是对这些常数的跨层控制。尤其：

- $U$ 是 $1,S,\ldots,S^{q-1}$ 与 $1,T,\ldots,T^{q-1}$ 的真实换基，不能只保留它的非零常数字符而漏掉 $\|U^{-1}\|$；
- 第 5.1 节可逆矩阵的测试幂和最小奇异值 $h$ 依赖同一正常态的实际矩，没有从正常性取得统一速度；
- 第 4 节的替代证书直接暴露 $\|u^{-1}\|\,\|z^{2^n-d}\|/\|z^{2^n}\|$ 以及正常阈值；
- $q$ 增长时连显式系数因子 $\binom{2D}{D}^{-q/2}$ 也迅速缩小。

因此 (6.3) 是一条真实的有限矩谱质量证书，并没有推出与 R289 的 $o(m)$ 熵上界矛盾的质量下界。下一接口是将这些具体费用与原 $Q_j$ 的实际系数和同一 $\nu_j$ 的矩联系起来，而不是用支撑秩或定性正常性替代该比较。
