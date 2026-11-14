# R19：极小向量误差端点与任意标量归一化

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态与范围。** §§1–6 是已证明的具体模型中间结论。它们处理 [R14](R14-backward-minimal-images-all-exponents.md) 尚留下的误差趋于零或一：固定非零目标的极小像经任意标量重标度后，非零强极限只可能来自误差趋于零，且只能是原目标的标量倍；在这一端点，归一化预像及残差均弱趋零。误差趋于一的 dyadic 情形反而产生两个非零弱极限，但其零阶配对不消失。这没有构造普通不变子空间，也没有排除其他极小向量或紧交织机制；主问题仍未完成，不主张文献新颖性。全部推理依赖仓库内已证明的 R9、R12、R14，不依赖尚未取得全文的文献。

## 1. 设定与极小向量公式

仍用 R9 的 $H=L^2(\mathbb Z_2,\mu)$、$(Uf)(y)=f(y-1)$ 及

$$
A=M_wU,\qquad w(y)=a_{v_2(y)},\qquad a_j=e^{-b_j},
$$

$$
b_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad 16^j\le b_j\le400\,16^j.
\tag{1.1}
$$

权在零点定义为零。设 $f\ne0$ 固定，$F=\|f\|^2$，并允许任意 $\beta_n\in(0,1)$。令 $x_n$ 为约束

$$
\|A^nx-f\|\le\beta_n\|f\|
\tag{1.2}
$$

下范数最小的向量，$z_n=A^nx_n$，$u_n=f-z_n$。置

$$
W_n(y)=\prod_{j=0}^{n-1}w(y-j),
\quad q_\lambda(v)=\frac1{1+\lambda v^2},
\quad m_\lambda(v)=\frac{\lambda v^2}{1+\lambda v^2}.
\tag{1.3}
$$

R14 §3 已自含证明：存在唯一 $\lambda_n>0$ 使

$$
\int q_{\lambda_n}(W_n)^2|f|^2\,d\mu=\beta_n^2F,
\tag{1.4}
$$

并且

$$
u_n=q_{\lambda_n}(W_n)f,\qquad
z_n=m_{\lambda_n}(W_n)f,\qquad
x_n=\lambda_nU^{-n}\left[\frac{W_n}{1+\lambda_nW_n^2}f\right].
\tag{1.5}
$$

特别地 $\|u_n\|=\beta_n\|f\|$，$z_n\ne0$，且所有乘子都取实非负值。以下单位向量记作 $\widehat z_n=z_n/\|z_n\|$、$\widehat x_n=x_n/\|x_n\|$、$\widehat u_n=u_n/\|u_n\|$。

## 2. 可平移模区间的渐近独立性

对于 $Q=2^s$、$1\le n<Q$ 及任意整数 $a$，定义

$$
E_a(n,Q)=\{y:y\bmod Q\in\{a,a+1,\ldots,a+n-1\}\bmod Q\}.
\tag{2.1}
$$

其测度等于 $n/Q$。当 $Q\to\infty$，允许 $n,a$ 任意变化，则每个固定 $h\in L^1(\mu)$ 都有

$$
\int_{E_a(n,Q)}h\,d\mu-\frac nQ\int h\,d\mu\longrightarrow0.
\tag{2.2}
$$

**证明。** 固定最低 $d$ 位的柱集合。长度 $n$ 的连续整数区间中，某个模 $2^d$ 剩余类的元素个数与 $n/2^d$ 相差至多 $1$，与起点 $a$ 无关。因此交测度与乘积测度之差绝对值至多 $1/Q$。先对柱函数求有限和，再以柱函数在 $L^1$ 中逼近 $h$，总逼近误差至多 $2\|h-h_d\|_1$。这给出 (2.2)。证毕。

以下简写 $E(n,Q)=E_0(n,Q)$。这项结论只是在极限中成立；没有把一般 $L^2$ 向量与高位当成精确独立。

## 3. 任意误差序列下极小像的强收敛分类

**定理 3.1。** 对任何趋于无穷的指数子列 $n_j$，有：

1. $z_{n_j}$ 强收敛，当且仅当 $\beta_{n_j}\to0$ 或 $\beta_{n_j}\to1$；对应极限分别为 $f$ 和 $0$。
2. $\widehat z_{n_j}$ 强收敛，当且仅当 $\beta_{n_j}\to0$；对应极限为 $f/\|f\|$。
3. 若存在复数 $c_j$ 使 $c_jz_{n_j}$ 强收敛到非零向量，则必有 $\beta_{n_j}\to0$，且 $c_j\to c\ne0$，极限为 $cf$。反向显然成立。

### 3.1 归一化后仍存在固定正测度的消失层

先证明比 R14 更强的估计。假设沿所研究的指数，$\beta_n\ge\beta_0>0$。选

$$
r=\left\lceil\log_2\frac{16}{\beta_0^2}\right\rceil,
\quad 2^k\le n<2^{k+1},\quad m=k+r-1,
\quad G_n=E(n,2^{m+1})^c.
\tag{3.1}
$$

R14 §3 的逐项计数（仅用 (1.1)）给

$$
W_n\ge L_n:=e^{-1400\,16^m}\quad\hbox{于 }G_n.
\tag{3.2}
$$

又由 (2.2)，当 $n$ 足够大时，

$$
\int_{G_n^c}|f|^2\,d\mu\le\frac{\beta_0^2}{4}F,
\qquad \int_{G_n}|f|^2\,d\mu\ge\frac F2.
\tag{3.3}
$$

将 (3.2)—(3.3) 代入 (1.4)，并用 $\beta_n\ge\beta_0$，得到

$$
\beta_0^2F\le\frac{F}{(1+\lambda_nL_n^2)^2}+\frac{\beta_0^2F}{4},
\qquad
\lambda_nL_n^2\le C_0:=\frac2{\sqrt3\,\beta_0}-1.
\tag{3.4}
$$

定义更深层

$$
D_n=E(n,2^{m+3}),\qquad
p_0=2^{-r-2}.
\tag{3.5}
$$

由整数段至少经过一个 $2^{m+3}$ 的倍数，

$$
W_n\le V_n:=e^{-4096\,16^m}\quad\hbox{于 }D_n,
\qquad \mu(D_n)\ge p_0>0.
\tag{3.6}
$$

注意与 R14 不同，现需在 $\|z_n\|$ 可能趋零时估计比例。乘子 $m_\lambda(v)$ 随 $v$ 递增，故由 (3.3)

$$
\|z_n\|\ge m_{\lambda_n}(L_n)\sqrt{F/2}.
$$

因 $\lambda_n>0$，分母非零。因此

$$
\begin{aligned}
\|\mathbf1_{D_n}\widehat z_n\|
&\le\sqrt2\frac{m_{\lambda_n}(V_n)}{m_{\lambda_n}(L_n)}\\
&=\sqrt2\left(\frac{V_n}{L_n}\right)^2
\frac{1+\lambda_nL_n^2}{1+\lambda_nV_n^2}\\
&\le\sqrt2(1+C_0)e^{-5392\,16^m}\longrightarrow0.
\end{aligned}
\tag{3.7}
$$

对任意固定 $z\in H$，(2.2)、(3.5)—(3.7) 给

$$
\liminf_n\|\widehat z_n-z\|\ge\sqrt{p_0}\|z\|.
\tag{3.8}
$$

同时 $\|\widehat z_n-z\|\ge1-\|z\|$，因此

$$
\boxed{\liminf_n\|\widehat z_n-z\|
\ge\frac{\sqrt{p_0}}{1+\sqrt{p_0}}>0.}
\tag{3.9}
$$

这里不需要误差远离 $1$。

更一般地，若复数 $d_n$ 满足 $\sup_n\|d_nz_n\|<\infty$，则 (3.7) 也给 $\|\mathbf1_{D_n}d_nz_n\|\to0$。若 $d_nz_n\to z$ 强收敛，由 (2.2) 必有 $z=0$。故在 $\beta_n\ge\beta_0$ 时，**任意标量重标度的极小像都不可能有非零强极限**。

### 3.2 分类的其余步骤

若 $\beta_n\to0$，则 $\|f-z_n\|=\beta_n\|f\|\to0$，故 $z_n\to f$ 及 $\widehat z_n\to f/\|f\|$。

若 $\beta_n\to1$，令 $m=m_{\lambda_n}(W_n)\in[0,1]$。由 $m^2\le2m-m^2$ 及 (1.4)，

$$
\|z_n\|^2=\int m^2|f|^2
\le\int(2m-m^2)|f|^2
=(1-\beta_n^2)F\longrightarrow0.
\tag{3.10}
$$

反过来，若 $z_n\to z$ 强收敛，则 $\beta_n=\|f-z_n\|/\|f\|$ 必收敛到某个 $b\in[0,1]$。若 $b\in(0,1)$，则 $\|z_n\|\ge(1-\beta_n)\|f\|$ 远离零；§3.1 的标量结论（取 $d_n=1$）给矛盾。故 $b$ 是端点，极限如上。

若 $\widehat z_n$ 强收敛但 $\beta_n$ 不趋零，取子列 $\beta_n\ge\beta_0>0$，与 (3.9) 冲突。若 $c_nz_n\to z\ne0$，同一子列论证迫使 $\beta_n\to0$。于是 $z_n\to f$；由 $\langle z_n,f\rangle\to F\ne0$ 得

$$
c_n=\frac{\langle c_nz_n,f\rangle}{\langle z_n,f\rangle}
\longrightarrow\frac{\langle z,f\rangle}{F}=:c.
$$

所以 $z=cf$，且 $c\ne0$。所有论证对任意子列 $n_j\to\infty$ 原样成立，证明定理。证毕。

## 4. 误差趋零时归一化残差弱趋零

**定理 4.1。** 若 $\beta_n\to0$，则对全部整数指数

$$
\widehat u_n\rightharpoonup0.
\tag{4.1}
$$

**证明。** 任取固定整数 $r\ge1$。写 $2^k\le n<2^{k+1}$，现在置 $m=k+r$，并定义

$$
E_n=E(n,2^{m+1}),\quad
D_n=E(n,2^{m+3}),\quad
L_n=e^{-1400\,16^m},\quad V_n=e^{-4096\,16^m}.
\tag{4.2}
$$

如前，$W_n\ge L_n$ 于 $E_n^c$，$W_n\le V_n$ 于 $D_n$，并且

$$
\mu(E_n)<2^{-r},\qquad\mu(D_n)\ge2^{-r-3}.
\tag{4.3}
$$

由 (2.2)，充分大 $n$ 时

$$
\int_{D_n}|f|^2\,d\mu\ge2^{-r-4}F.
\tag{4.4}
$$

因 $q_\lambda$ 递减，(1.4) 给

$$
\beta_n^2F\ge q_{\lambda_n}(V_n)^2\,2^{-r-4}F.
$$

因此 $q_{\lambda_n}(V_n)\to0$，即 $\lambda_nV_n^2\to\infty$。由 (4.4)

$$
\begin{aligned}
\|\mathbf1_{E_n^c}\widehat u_n\|
&\le2^{(r+4)/2}\frac{q_{\lambda_n}(L_n)}{q_{\lambda_n}(V_n)}\\
&=2^{(r+4)/2}\frac{1+\lambda_nV_n^2}{1+\lambda_nL_n^2}
\longrightarrow0,
\end{aligned}
\tag{4.5}
$$

因为 $V_n/L_n\to0$ 且 $\lambda_nV_n^2\to\infty$。

任取固定 $g\in H$。单位范数及 Cauchy–Schwarz 不等式给

$$
|\langle\widehat u_n,g\rangle|
\le\|\mathbf1_{E_n^c}\widehat u_n\|\|g\|
+\|\mathbf1_{E_n}g\|.
$$

由 (2.2)、(4.3)、(4.5)，

$$
\limsup_n|\langle\widehat u_n,g\rangle|
\le2^{-r/2}\|g\|.
$$

先固定 $r$ 取上极限，再令 $r\to\infty$，得到 (4.1)。证毕。

## 5. 误差趋零时归一化极小预像也弱趋零

**定理 5.1。** 若 $\beta_n\to0$，则对全部整数指数

$$
\widehat x_n\rightharpoonup0.
\tag{5.1}
$$

**证明。** 固定 $r\ge1$，仍取 $m=k+r$，以及 §4 的 $E_n,L_n,V_n$。记

$$
h_n(v)=\frac{v}{1+\lambda_nv^2},\qquad
\xi_n=h_n(W_n)f.
\tag{5.2}
$$

由 (1.5)，$\widehat x_n=U^{-n}\xi_n/\|\xi_n\|$。函数 $h_n$ 并非全局单调，故不能把 §4 的单调性论证直接搬来；需要一个上下权界都成立的环带。

定义

$$
H_n=E(n,2^{m+3})\setminus E(n,2^{m+4}).
\tag{5.3}
$$

在此环带上，长度 $n$ 的整数段包含一个 $2^{m+3}$ 的倍数，却不含 $2^{m+4}$ 的倍数；其最大 $2$-进赋值恰为 $m+3$。因此与 (3.2) 相同的计数给

$$
T_n:=e^{-1400\,16^{m+3}}\le W_n\le V_n
\quad\hbox{于 }H_n.
\tag{5.4}
$$

这里应用上界计数时 $n/2^{m+3}\le2$，所以常数 $1400$ 仍适用。又

$$
\mu(H_n)=\frac n{2^{m+4}}\ge2^{-r-4}.
$$

对两个嵌套模区间分别应用 (2.2) 并相减，得到充分大 $n$ 时

$$
\int_{H_n}|f|^2\,d\mu\ge2^{-r-5}F.
\tag{5.5}
$$

进一步取

$$
J_n=E(n,2^{m+6}),\qquad R_n=e^{-16^{m+6}}.
$$

在 $J_n$ 上 $W_n\le R_n$，且 $\mu(J_n)\ge2^{-r-6}$。因 $\beta_n\to0$，重复 (4.4) 的推理，得到 $\lambda_nR_n^2\to\infty$。而

$$
R_n/T_n=\exp\bigl(-(4096-1400)16^{m+3}\bigr)\to0,
$$

故也有 $\lambda_nT_n^2\to\infty$。由 (5.4)，在 $H_n$ 上最终 $\lambda_nW_n^2\ge1$，于是

$$
h_n(W_n)\ge\frac1{2\lambda_nW_n}
\ge\frac1{2\lambda_nV_n}.
\tag{5.6}
$$

另一方面，在 $E_n^c$ 上 $W_n\ge L_n$，恒有

$$
h_n(W_n)\le\frac1{\lambda_nW_n}\le\frac1{\lambda_nL_n}.
\tag{5.7}
$$

(5.5)—(5.7) 给

$$
\frac{\|\mathbf1_{E_n^c}\xi_n\|}{\|\xi_n\|}
\le2^{1+(r+5)/2}\frac{V_n}{L_n}\longrightarrow0.
\tag{5.8}
$$

平移 $U^{-n}$ 把 $E_n$ 变为

$$
E_n-n=E_{-n}(n,2^{m+1}).
$$

因此 $\widehat x_n$ 在其补集上的范数趋零，而该集合的测度小于 $2^{-r}$，并满足 §2 的渐近独立性。对任意固定 $g$，与 §4 末尾相同的估计给

$$
\limsup_n|\langle\widehat x_n,g\rangle|
\le2^{-r/2}\|g\|.
$$

令 $r\to\infty$，证明 (5.1)。证毕。

**紧算子推论。** 若 $K$ 是任意固定紧算子，$\beta_n\to0$ 时

$$
\|K\widehat x_n\|\to0,\qquad \|K\widehat u_n\|\to0.
\tag{5.9}
$$

这是紧算子将有界弱零列送到范数零列的直接结论。因此该误差端点虽有 $z_n\to f\ne0$，其单位预像或单位残差不能经某个固定紧算子提取非零范数极限。这里没有排除变化紧算子、无界重标度、逃逸目标或别的交织关系。

## 6. 误差趋一的 dyadic 精确极限：非零弱向量及其非零配对

本节只取指数 $n=2^k$，相对误差简写为 $\gamma_k=\beta_{2^k}\to1$。写

$$
B_k=\|A^{2^k}\|=C_ka_k,\quad
D_k=W_{2^k}/B_k,\quad t_k=\lambda_{2^k}B_k^2.
\tag{6.1}
$$

R9/R12 的精确公式给：$D_k=1$ 于第 $k$ 位 $b_k=1$；于 $b_k=0$ 有 $0\le D_k\le\eta_k=a_{k+1}/a_k\to0$。设 $P_{k,\epsilon}=M_{\mathbf1_{\{b_k=\epsilon\}}}$。

**命题 6.1。** 在本节条件下，

$$
\frac{t_k}{1-\gamma_k^2}\longrightarrow1,
\tag{6.2}
$$

$$
\widehat z_{2^k}-\frac{\sqrt2}{\|f\|}P_{k,1}f\longrightarrow0,
\qquad
\widehat x_{2^k}-\frac{\sqrt2}{\|f\|}P_{k,0}f\longrightarrow0
\quad\hbox{于范数}.
\tag{6.3}
$$

故两单位向量均弱趋于 $f/(\sqrt2\|f\|)$，而到该弱极限的距离均趋于 $1/\sqrt2$。同时 $\widehat u_{2^k}\to f/\|f\|$ 强收敛，因此

$$
\langle\widehat x_{2^k},\widehat u_{2^k}\rangle
\longrightarrow\frac1{\sqrt2}\ne0.
\tag{6.4}
$$

**证明。** 由 (3.10)，$z_{2^k}\to0$。另一方面

$$
\|z_{2^k}\|\ge\frac{t_k}{1+t_k}\|P_{k,1}f\|,
\qquad \|P_{k,1}f\|\to\frac{\|f\|}{\sqrt2}.
$$

故 $t_k\to0$。由

$$
\frac{z_{2^k}}{t_k}=\frac{D_k^2}{1+t_kD_k^2}f
$$

可得

$$
\left\|\frac{z_{2^k}}{t_k}-P_{k,1}f\right\|
\le(t_k+\eta_k^2)\|f\|\longrightarrow0.
\tag{6.5}
$$

这证明 (6.3) 的第一项。误差方程还给

$$
\frac{1-\gamma_k^2}{t_k}
=\frac1F\int\frac{2D_k^2+t_kD_k^4}{(1+t_kD_k^2)^2}|f|^2\,d\mu.
$$

因 $0\le D_k\le1$，右端与 $2F^{-1}\int D_k^2|f|^2$ 之差趋零；后者趋于 $1$，证明 (6.2)。

令 $F_k=A^{2^k}/B_k$，并用 R12 的高位矩阵单位 $E_k$，其满足 $\|F_k-E_k\|\to0$。由 (1.5)，

$$
\frac{B_k}{t_k}x_{2^k}=F_k^*u_{2^k}.
$$

因为 $u_{2^k}=f-z_{2^k}\to f$，得

$$
\frac{B_k}{t_k}x_{2^k}-E_k^*f\longrightarrow0.
\tag{6.6}
$$

对固定低位柱函数 $f_d$ 及 $k\ge d$，恰有 $E_k^*f_d=P_{k,0}f_d$。两个算子范数都不超过 $1$，柱函数稠密遂给 $E_k^*f-P_{k,0}f\to0$。结合 $\|P_{k,0}f\|\to\|f\|/\sqrt2$，得到第二个 (6.3)。

高位投影 $P_{k,\epsilon}\to I/2$ 于 WOT，故两个弱极限如述。每个单位向量的弱极限范数为 $1/\sqrt2$，展开平方距离可得其距离趋于 $1/\sqrt2$。最后 $\|u_{2^k}\|=\gamma_k\|f\|\to\|f\|$，所以单位残差强趋 $f/\|f\|$；强弱配对给 (6.4)。证毕。

**含义的准确界限。** 误差趋于一确实给出归一化预像的非零弱极限，但上述自然残差配对连零阶矩都不为零。它本身不满足 R15 所需的全部矩消失条件。证明不能把“得到非零弱向量”直接升级成不变子空间。

## 7. 尚待推进的构造

以上结果固定了目标 $f\ne0$。强收敛变化目标可以沿用相同的 $L^1$ 逼近估计，但不应把这些结论扩张到任意逃逸目标。真正尚剩的是有控制的变化目标、不同的两个向量序列，或复对称双线性矩的构造。下一项研究将专门检查 $Cf(y)=\overline{f(-1-y)}$ 的双线性对称性是否能提供非零矩消失向量；仅仅把条件重写为无限个二次方程不算构造。
