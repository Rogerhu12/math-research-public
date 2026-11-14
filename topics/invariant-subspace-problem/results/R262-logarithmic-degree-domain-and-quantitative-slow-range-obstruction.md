# R262：对数次数权下的慢符号值域障碍与真实末端链预算

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：完整证明的中间结论；普通 Hilbert ISP 未完成。

本稿量化 [R253 的多项式次数附录](R253-appendix-polynomial-degree-smooth-domain-and-finite-resolvent-denominators.md) 的真实末端链。使用 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的有限逆芽系数，得到统一的四次链成本，再把慢符号值域障碍加强到一个明确的超多项式 Walsh 次数权。这里的 $4/3$ 是本证明得到的指数，不宣称它是最佳阈值。

## 1. 定理与准确量词

在原 Haar 空间上记
$$
\mathcal N\chi_F=|F|\chi_F,\qquad
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}Y_j.
$$
两个 $S$ 都是既有结果中的全空间单射有界算子。定义
$$
\phi(x)=(\log(2+x))^{4/3},\qquad
W_\sigma=\exp\{\sigma[\phi(\mathcal N)-\phi(0)]\},
\qquad \mathcal G_\sigma=\operatorname{Dom}W_\sigma,
\tag{1.1}
$$
并给 $\mathcal G_\sigma$ 范数 $\|f\|_\sigma=\|W_\sigma f\|$。
因 $W_\sigma\ge I$，这是 Banach（事实上 Hilbert）图范数。

**定理。** 取明确常数
$$
\boxed{\sigma_0=1/512.}
$$
对 $S=S_N$、$S_Y$ 分别有
$$
\boxed{\mathcal G_{\sigma_0}\not\subseteq\operatorname{Ran}S.}
\tag{1.2}
$$
更具体地，对每个足够大的整数物理头长度 $m$，存在实际向量 $z_m$，使
$$
\|z_m\|=1,\qquad z_m\in\bigcap_{\sigma>0}\mathcal G_\sigma,
\qquad
\|Sz_m\|_{\sigma_0}
\le4\exp\left[-\frac1{256}(\log m)^{4/3}\right].
\tag{1.3}
$$
阈值 $m$ 可以依赖固定模型及固定常数；不要求给一个小的数值阈值。

因此，对每个 $S$ 分别存在 $f\notin\operatorname{Ran}S$，而
$$
\exp\{t(\log(2+\mathcal N))^\alpha\}f\in H
\quad\text{对全部 }1<\alpha<4/3\text{ 和 }t>0.
\tag{1.4}
$$
该 $f$ 尤其具有全部多项式 Walsh 次数矩。没有声称同一个 $f$ 同时离开两个 $S$ 的值域。

## 2. 统一的单位步长真链

沿用真实边界的有限矩阵
$$
Be_n=\alpha_{v_2(n)}e_{n-1},\qquad Be_0=0,\qquad
W_n=\prod_{i=1}^n\alpha_{v_2(i)},\quad W_0=1.
$$
对头维数 $d=2^h\ge4$，两个真实截断均为
$$
T_h=f_h(B_h),\qquad f_h'(0)=\beta=e^{20},
\tag{2.1}
$$
其中
$$
f_{N,h}(z)=\sum_{j<h}(j+1)^{-2}\frac{z^{2^j}}{d_j},
\qquad
f_{Y,h}(z)=\sum_{j<h}(j+1)^{-2}\frac{z^{2^j}}{d_j+z^{2^j}}
\pmod {z^d}.
$$
第二式保留全部有限 Cayley 展开。

R249 §§2–4 已证明，设
$$
L_d=\frac{25}{2}\frac{d^4}{d-2},\qquad \rho=e^{-L_d},
\qquad \lambda_d=\beta\rho,
$$
则有实际上三角矩阵 $S_d$ 满足
$$
T_hS_d=S_d\lambda_dJ_d,\qquad
S_de_0=e_0,\qquad
\|S_d\|\le d6^d,
\tag{2.2}
$$
其中 $J_de_k=e_{k-1}$。准确构造为
$$
S_d=\operatorname{diag}(W_n^{-1}\rho^n)_{n<d}
C_{\widetilde h}^{\mathsf T},
\tag{2.3}
$$
$g=\beta^{-1}f_h$，$h=g^{-1}\pmod {z^d}$，
$\widetilde h(z)=\rho^{-1}h(\rho z)$；换元矩阵的第 $(k,n)$ 项为 $[z^k]\widetilde h(z)^n$。
这里使用转置，不是未经说明的伴随换元。

对 $0\le k<d$ 置
$$
\xi_k=\lambda_d^{-k}S_de_k.
\tag{2.4}
$$
它的第 $n$ 坐标准确为
$$
(\xi_k)_n=W_n^{-1}\beta^{-k}[z^k]h(z)^n
\quad(0\le n\le k),
\tag{2.5}
$$
其余坐标为零。式 (2.5) 表明 $\xi_k$ 不依赖所选的足够大 dyadic 维数 $d$：每个所用系数只依赖 $f_h$ 到 $k$ 阶的系数，而两个慢符号的这些系数随有限头相容。因此这是一条共同的实际有限支撑链，且
$$
\xi_0=e_0,\qquad T\xi_k=\xi_{k-1},\qquad
\operatorname{supp}\xi_k\subseteq\{0,\ldots,k\}.
\tag{2.6}
$$

现在按每个 $k\ge1$，选最小的 dyadic $d\ge4$ 且 $d>k$。于是 $d\le2(k+1)$，并且 $L_d\le25d^3$。由 (2.2)、(2.4)，
$$
\log\|\xi_k\|
\le\log d+d\log6+(L_d-20)k
\le512(k+1)^4.
\tag{2.7}
$$
最后的常数很宽松：$25d^3k\le200(k+1)^4$，其余两项小于 $4(k+1)^4$。
所以得到明确统一界
$$
\boxed{\|\xi_k\|\le e^{512(k+1)^4}\quad(k\ge1).}
\tag{2.8}
$$
不同 $k$ 选取不同有限头只用于证明界；相容性 (2.5) 保证最后用的是同一条链。

## 3. 对数次数权中的实际 carry

函数 $\phi$ 在 $[0,\infty)$ 上递增且凹，因为
$$
\phi''(x)=\frac{4}{3(2+x)^2[\log(2+x)]^{2/3}}
\left(\frac13-\log(2+x)\right)<0.
$$
令
$$
\mu_\sigma(L)=e^{\sigma[\phi(L)-\phi(0)]}.
$$
凹性给
$$
\mu_\sigma(q+L)\le\mu_\sigma(q)\mu_\sigma(L)
\quad(q,L\ge0).
\tag{3.1}
$$
若 $B$ 仅作用于 $L$ 个物理位，按块外 Walsh 次数分解，每一块内的次数在 $0$ 到 $L$ 之间，故
$$
\boxed{\|B\|_{\mathcal G_\sigma\to\mathcal G_\sigma}
\le\mu_\sigma(L)\|B\|.}
\tag{3.2}
$$
有限和的图范数极限用闭的 $W_\sigma$ 识别，故这是实际的域保持。

用 R171、R253 的实际有限头壳层
$$
N_j^{[m]}=\sum_{r=j}^{m-1}\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r,
$$
以及
$$
\|V_j^{[r+1]}-V_j^{[r]}\|
\le18\frac{\alpha_r}{\alpha_j},
\qquad Y_j=\frac{I-V_j}{2},
\tag{3.3}
$$
其中对应壳层只作用于 $[j,r]$。
结合 $\alpha_r/\alpha_j\le\eta_j\eta_*^{r-j-1}$、$\eta_*<1/4$，
以及 $\mu_\sigma(L)$ 比任意固定的 $e^{\epsilon L}$ 增长慢，得到
$$
\sup_j\left(\|N_j\|_{\mathcal G_\sigma\to\mathcal G_\sigma}
+\|Y_j\|_{\mathcal G_\sigma\to\mathcal G_\sigma}\right)
\le K_\sigma<\infty.
\tag{3.4}
$$
这对每个固定 $\sigma>0$ 成立；不要求对全部 $\sigma$ 有同一个常数。

按原 Haar 前 $m$ 个物理位分解，记 $T_m$ 为真实有限头，$U_m$ 为真实尾，并写
$$
\widetilde S_m=T_m\otimes I+I\otimes U_m,\qquad
R_m=S-\widetilde S_m.
$$
这里 $T_m$ 的下标表示物理头长度，头维数是 $2^m$。
对 $m\ge1$，(3.4) 与 $\sum_{j\ge m}(j+1)^{-2}\le1/m$ 给
$$
\|U_m\|_{\mathcal G_\sigma^{\rm tail}\to\mathcal G_\sigma^{\rm tail}}
\le K_\sigma/m.
\tag{3.5}
$$
对 $r\ge m>j$，真实权满足 $\alpha_r/\alpha_j\le e^{-770\,16^{r-1}}$。
所以两个 $S$ 共同满足
$$
\boxed{\|R_m\|_{\mathcal G_\sigma\to\mathcal G_\sigma}
\le\varepsilon_{m,\sigma}:=
9a_\Sigma\sum_{r\ge m}\mu_\sigma(r+1)e^{-770\,16^{r-1}},}
\quad a_\Sigma=\sum_{j\ge0}(j+1)^{-2}.
\tag{3.6}
$$
固定 $\sigma$ 时该误差为双指数小量。全部真实 carry 都保留在 (3.6) 中。

## 4. 同时增长的链长与物理头

将 §2 的 $e_n$ 倒序嵌入原 Haar 物理头的末端，记此等距嵌入为 $J_m$。R253 的准确末端权恒等式给
$$
T_mJ_m\xi_k=J_m\xi_{k-1}\quad(1\le k<2^m),\qquad
T_mJ_m\xi_0=0.
\tag{4.1}
$$
它不是将边界的无限核搬到原表示；这里只使用完全相同的有限矩阵。

令 $\Omega_m$ 为尾真空，取整数 $p<2^m$ 并定义
$$
v_{m,p}=\sum_{k=0}^{p-1}(-1)^k
J_m\xi_k\otimes U_m^k\Omega_m.
\tag{4.2}
$$
由 (3.4)–(3.5)，每个这样的有限和属于所有 $\mathcal G_\sigma$。
(4.1) 给准确望远镜式
$$
\widetilde S_mv_{m,p}
=(-1)^{p-1}J_m\xi_{p-1}\otimes U_m^p\Omega_m.
\tag{4.3}
$$
由 (3.1)，任意低头向量 $x$ 和尾向量 $y$ 满足
$$
\|x\otimes y\|_\sigma
\le\mu_\sigma(m)\|x\|\|y\|_\sigma.
\tag{4.4}
$$

固定 $\sigma=\sigma_0$，并令 $K=\max(1,K_0,K_{\sigma_0})$；$K_0$ 表示普通 Hilbert 范数中的对应常数。设
$$
L=\log m,\qquad p=p(m)=\left\lfloor\frac{L^{1/3}}{32}\right\rfloor.
\tag{4.5}
$$
充分大时 $p\ge2$、$p<2^m$ 且 $\log K\le L/4$。
对 $1\le k<p$，因为 $(k+1)^4\le16k^4$ 和 $p^3\le L/32768$，有
$$
\log\|\xi_k\|\le8192k^4\le Lk/4.
\tag{4.6}
$$
从而
$$
\|\xi_k\|(K/m)^k\le m^{-k/2}.
\tag{4.7}
$$
记 $u_m=J_m\xi_0\otimes\Omega_m$，则 $\|u_m\|=1$，并有
$$
\|v_{m,p}-u_m\|\le\sum_{k=1}^{p-1}m^{-k/2}\longrightarrow0,
\qquad
\|v_{m,p}\|_{\sigma_0}\le2\mu_{\sigma_0}(m)
\tag{4.8}
$$
对充分大的 $m$ 成立。

再次由 (4.6) 和 $\log K\le L/4$，
$$
\|\xi_{p-1}\|(K/m)^p\le e^{-Lp/2}.
$$
而充分大时 $p\ge L^{1/3}/64$，所以 (3.6)、(4.3)–(4.4) 给
$$
\boxed{\|Sv_{m,p}\|_{\sigma_0}
\le\mu_{\sigma_0}(m)
\left(e^{-L^{4/3}/128}+2\varepsilon_{m,\sigma_0}\right).}
\tag{4.9}
$$
充分大时 $\log\mu_{\sigma_0}(m)\le2\sigma_0L^{4/3}=L^{4/3}/256$。
双指数余项远小于第一项。因此右边至多
$2e^{-L^{4/3}/256}$。
最后置 $z_m=v_{m,p}/\|v_{m,p}\|$，并用 $\|v_{m,p}\|\ge1/2$，得到 (1.3)。

这里的 $p$ 随 $m$ 增长。统一链界 (2.8) 与对数次数域中的 (3.6) 正是为这一步补齐的两项预算；不能仅引用旧稿中“先固定 $p$”的估计替代。

## 5. 闭图反证与适用范围

假设 $\mathcal G_{\sigma_0}\subseteq\operatorname{Ran}S$。由于 $S$ 单射，$S^{-1}:\mathcal G_{\sigma_0}\to H$ 全域定义，且图闭：若 $f_n\to f$ 于 $\mathcal G_{\sigma_0}$、$S^{-1}f_n\to g$ 于 $H$，则有界 $S$ 给 $Sg=f$。Banach 闭图定理迫存在 $C<\infty$，使
$$
\|S^{-1}f\|\le C\|f\|_{\sigma_0}.
$$
代入 $f=Sz_m$ 与 (1.3) 矛盾，证明 (1.2)。

若 $1<\alpha<4/3$、$t>0$，则存在有限常数 $C_{\alpha,t}$，使
$$
e^{t(\log(2+n))^\alpha}\le C_{\alpha,t}
e^{\sigma_0[(\log(2+n))^{4/3}-(\log2)^{4/3}]}
\quad(n\ge0).
$$
因此 $\mathcal G_{\sigma_0}$ 连续嵌入 (1.4) 的每个域。由 (1.2) 选取的同一个 $f$ 对所有这些参数均满足 (1.4)。

作为直接推论，若有界算子 $R$ 满足
$\mathcal G_{\sigma_0}\subseteq\operatorname{Ran}R$，则
$$
\operatorname{Ran}R\not\subseteq\operatorname{Ran}S,
\qquad R\notin S B(H).
$$
这一推论只适用于已经证明该像包含的 $R$。
尤其不能用它排除只知包含 $\operatorname{Dom}e^{\epsilon\sqrt{1+\mathcal N}}$ 的无限正预解积：后一个域更小，包含方向不足以应用本结论。

本稿没有给出正正常慢理想湮灭态，也没有证明两个边界的 $N=M$，没有决定 R253 的 $q_m$ 是否非消失，更没有完成普通 ISP。
