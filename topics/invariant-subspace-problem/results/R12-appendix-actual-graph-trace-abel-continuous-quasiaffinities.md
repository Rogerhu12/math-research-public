# 原整数图迹的 Abel 连续来源与稠密迹类交织

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 固定原 Haar 尾 $C=A^{(m)}$ 及任意 Walsh 块根的图空间 $E$。
依赖[实际整数迹与采样](R12-appendix-actual-walsh-graph-domain-integer-traces-sampling-and-single-boundary-chain.md)。
本篇给 $E$ 到原 $H$ 的实际单射稠值迹类来源，同时准确支付为何它不能被当作 $H$ 上的闭缩放交织。

## 1. 原全部幂的同一规范

写
$$
\beta_n=\prod_{a=1}^n\alpha_{m+v_2(a)},\qquad \beta_0=1.
$$
原[全部尾幂规范](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md) (1.3) 给
$$
\|C^n\|=\beta_n,\qquad
\|C^n\Omega\|_\infty=\beta_n.
\tag{1}
$$
第二式也可直接核：任意长度 $n$ 的原连续权积中，
被 $2^j$ 整除的项至少有 $\lfloor n/2^j\rfloor$ 个；
原权逐层下降，故积至多 $\beta_n$。
整数目标点 $n$ 对应 $1,\ldots,n$，准确达到该最大值。
若积中出现原点 $0$，积为零，也不破坏上界。
所有 $C^n\Omega$ 都是同一原连续函数。

前稿给真实图连续迹 $\ell_n$，且
$$
|\ell_nf|\le\sqrt{K_0+8n}\,\|f\|_E,\qquad K_0=2^{20}+9.
\tag{2}
$$
它们分离 $E$，并满足
$\ell_0C_E=0$、$\ell_nC_E=\alpha_{m+v_2(n)}\ell_{n-1}$。

## 2. 一个完整正向构造

固定 $0<\rho<1$，定义
$$
\boxed{\quad
X_\rho f=\sum_{n=0}^{\infty}
\rho^n\frac{\ell_n(f)}{\beta_n}C^n\Omega.
\quad}
\tag{3}
$$
由 (1)--(2)，级数在 $C(\mathbb Z_2)$ 的范数中绝对收敛，
并在 $E\to H$ 的迹范数中收敛：
$$
\|X_\rho\|_{E\to C(\mathbb Z_2)}
\le M_\rho,\qquad
\|X_\rho\|_1\le M_\rho,\qquad
M_\rho=\sum_{n\ge0}\rho^n\sqrt{K_0+8n}<\infty.
\tag{4}
$$
所以它是真正处处定义于 $E$ 的紧算子，且输出有原连续代表。

保留同一个 $\beta_n$，逐项用原递推得到
$$
\boxed{\quad X_\rho C_E=\rho\,C X_\rho.\quad}
\tag{5}
$$
确因 $\beta_n=\alpha_{m+v_2(n)}\beta_{n-1}$；
重编号后的级数仍由 (4) 绝对收敛。
这不是换权后的形式等式。

### 单射

若 $X_\rho f=0$ 于 $H$，连续性使它在所有原整数点都为零。
对整数 $k\ge0$，$C^n\Omega(k)=0$ 当 $n>k$，
而 $C^k\Omega(k)=\beta_k$。
因此 (3) 在这些点是准确有限下三角式：
$$
0=(X_\rho f)(k)
=\sum_{n=0}^k\rho^n\frac{\ell_n(f)}{\beta_n}
(C^n\Omega)(k).
\tag{6}
$$
从 $k=0$ 起归纳，得到 $\ell_k(f)=0$ 对全部 $k$。
前稿的均方采样分离性于是给 $f=0$。

### 原 $H$ 中稠密像

固定 $k$，对 $2^L>k$ 取真实柱指标
$p_{k,L}=\mathbf1_{\{x\equiv k\pmod{2^L}\}}\in E$。
其全部整数迹恰为对应的 $0/1$ 周期序列。
(1)、(3) 给
$$
\left\|X_\rho p_{k,L}
-\rho^k\beta_k^{-1}C^k\Omega\right\|_\infty
\le\frac{\rho^{k+2^L}}{1-\rho^{2^L}}\longrightarrow0.
\tag{7}
$$
原 $\Omega$ 循环，故 (7) 给
$$
\boxed{\quad \ker X_\rho=0,\qquad
\overline{\operatorname{Ran}X_\rho}^{\,H}=H.\quad}
\tag{8}
$$
为明确这里所用的原循环来源，可用既有归一化幂
$N_j=E_j+\eta_jE_j^*N_{j+1}$ 的准确 Cayley 式：
$$
N_j(I+N_j)^{-1}\Omega=E_j\Omega.
$$
每个 Cayley 因子属于 $C$ 的多项式范数闭包。
按位数递增施加，前面的低位事件保持不变，便产生全部有限柱指标；
这些指标在 $H$ 中稠密。这里没有假设任意非零输入都循环。

## 3. 同一向量的有界原交换子来源

(3) 还给一个 $E$ 到原多项式范数闭包的有界线性映射
$$
\Phi_\rho(f)
=\sum_{n\ge0}\rho^n\frac{\ell_n(f)}{\beta_n}C^n,\qquad
\|\Phi_\rho(f)\|\le M_\rho\|f\|_E.
\tag{9}
$$
它满足
$$
X_\rho f=\Phi_\rho(f)\Omega,\qquad
\Phi_\rho(C_Ef)=\rho C\Phi_\rho(f).
$$
若 $\ell_0(f)\ne0$，则 $\Phi_\rho(f)$ 在该含单位交换 Banach 代数中可逆：
每个连续字符都把拟幂零生成元 $C$ 送到零，
所以其在 (9) 上的值恒为非零的 $\ell_0(f)$。
于是这种输入的 $X_\rho f$ 确对原 $C$ 循环。
对于 $\ell_0(f)=0$ 的一般非零输入，本篇只使用 (8)，
没有据有限首项或稠密像倒置出所需原范围或循环性。

## 4. 忘掉图范数后，闭关系恰为整个双空间

把同一 $X_\rho$ 暂视为 $H$ 上、域为 $\mathcal D$ 的算子，
令
$$
\mathcal L=\overline{\{(f,X_\rho f):f\in\mathcal D\}}^{\,H\oplus H}.
$$
由于 (5)，原图及其闭包都被 $\operatorname{diag}(C,\rho C)$ 保持。

取原 dyadic 幂规范 $d_j=\|C^{2^j}\|$、
$N_j=C^{2^j}/d_j$。原实际高位身份给
$$
N_j\longrightarrow\tfrac12I\quad\text{弱},\qquad
\|N_j\|=1.
$$
因此对任意 $(x,y)\in\mathcal L$，
$$
(N_jx,\rho^{2^j}N_jy)\in\mathcal L,\qquad
(N_jx,\rho^{2^j}N_jy)\rightharpoonup(x/2,0).
$$
闭线性子空间也弱闭，故 $(x,0)\in\mathcal L$，继而 $(0,y)\in\mathcal L$。
原域在 $H$ 中稠密，而 (8) 给像稠密，所以
$$
\boxed{\quad\mathcal L=H\oplus H.\quad}
\tag{10}
$$
即该同一来源具有最大的垂直闭关系部分；
它不是 $H$ 上的可闭缩放交织，更不是一个闭平方根或可直接拉回的图。

新增正向内容为 (3)--(8) 的实际全域于 $E$、迹类、连续输出、单射稠值来源，
以及精确同权交织；(10) 保留了改变来源拓扑的全部费用边界。
后续原闭域构造仍需其它相容来源，不从此稠密像升级为普通 ISP 完成。
