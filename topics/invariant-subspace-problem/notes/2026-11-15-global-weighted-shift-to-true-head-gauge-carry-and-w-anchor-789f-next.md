# 原全局后移与有限头正向 gauge 的定量 carry 锚

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文支付有限头正向 gauge 与同一全局后移多项式之间的真实 carry 误差，进而在原 \(W=M\ominus N\) 上得到完整物理自配对锚。不把该锚免费移到孔截断或原左最小代表；高孔自配对和带 gauge 的真实投影误差仍须支付。

## 1. 原算子、权与同一有限多项式

沿用 [R195 §1](../results/R195-slow-boundary-module-types-and-fast-ideal-separation.md) 的两个原模型及定义
\[
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
\tag{1.1}
\]
因为 \(T\) 与原有界后移 \(B\) 交换，\(M\) 对 \(B\) 不变，故
\[
B^kM\subseteq N\qquad(k\ge1).
\tag{1.2}
\]

固定 \(m\ge10,d=2^m\)。原物理权为
\[
Be_n=\frac{W_n}{W_{n-1}}e_{n-1},\quad
W_n=\prod_{i\in{\rm bits}(n)}d_i,\quad
d_i=e^{-\Lambda_i},
\]
\[
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\qquad d_0=e^{-20}.
\tag{1.3}
\]
记 \(B_m=B|_{\operatorname{span}\{e_0,\ldots,e_{d-1}\}}\)，并在完整二进物理空间中写
\[
\widehat B_m=B_m\otimes I.
\]
这是只在低 \(m\) 位作后移的原有限头，不是全 \(B\)。

原实际头满足 \(A_m=F_m(B_m)\)。对 \(N\) 模型和 \(Y\) 模型分别有
\[
F_{N,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i},
\qquad
F_{Y,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i+z^{2^i}},
\quad b_i=(i+1)^{-2}.
\]
定义 \(f_{0,m}(z)=F_m(z)/z\)，其零点处按解析延拓，满足
\(f_{0,m}(0)=d_0^{-1}\)。

[真逆芽稿](2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)
在
\[
\rho_m=\exp(-25d^3/2)
\]
上证明
\[
\sup_{|z|\le\rho_m}|f_{0,m}(z)-d_0^{-1}|
\le e^{-d^3/4}.
\tag{1.4}
\]
因而 \(f_{0,m}^{-1}\) 在该圆盘解析，并有
\[
|f_{0,m}(z)^{-1}|\le2d_0.
\]
取它的同一 Taylor 截断
\[
p_m(z)=\sum_{k=0}^{d-1}p_{m,k}z^k,\qquad
p_{m,0}=d_0,\qquad
|p_{m,k}|\le2d_0\rho_m^{-k}.
\tag{1.5}
\]
由 \(B_m^d=0\)，真正有限头正向 gauge 准确为
\[
G_{1,m}:=f_{0,m}(B_m)^{-1}\otimes I=p_m(\widehat B_m).
\tag{1.6}
\]
以下比较的是 \(p_m(B)\) 与 (1.6)；不会在全 \(B\) 上代入一个未经证明收敛的无限逆级数。

## 2. 每个原权位置上的 carry 界

记
\[
\alpha_j=\frac{d_j}{\prod_{i<j}d_i}.
\]
由原 \(\Lambda_i\) 显式求和，
\[
-\log\alpha_j=
\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{2.1}
\]
其相邻差为
\[
1400\,16^j-630\,8^j+300\,2^j>0,
\]
故 \(\alpha_j\) 递减。

对 \(1\le k<d\)，将任意整数输入写成 \(n=d\ell+r\)，
\(0\le r<d\)。
若 \(r\ge k\)，低头不发生借位，原两算子在 \(e_n\) 上完全相同：
\[
B^ke_n=\widehat B_m^ke_n
=\frac{W_r}{W_{r-k}}\,e_{n-k}.
\]
若 \(r<k\)，则 \(\widehat B_m^ke_n=0\)。在 \(\ell=0\) 时 \(B^ke_n\) 也为零；
在 \(\ell\ge1\) 时，设 \(j=m+v_2(\ell)\)，原全部借位权准确为
\[
B^ke_n=
\left(\frac{d_j}{\prod_{i=m}^{j-1}d_i}\right)
\frac{W_r}{W_{d+r-k}}\,e_{n-k}.
\tag{2.2}
\]
第一个括号等于
\(\alpha_jW_{d-1}\le\alpha_mW_{d-1}=d_m\)。
同时 \(0<d_i<1\) 给 \(W_r\le1\) 及
\(W_{d+r-k}\ge W_{d-1}\)。
不同输入在这一 \(k\) 下仍送到不同输出，所以算子范数就是这些实际权的上确界。因此
\[
\boxed{\|B^k-\widehat B_m^k\|
\le\frac{d_m}{W_{d-1}}=\alpha_m
\qquad(1\le k<d).}
\tag{2.3}
\]
这里已经包括所有 \(j\ge m\) 的更远借位；没有只核首个 \(d\)-块。

结合 (1.5)、(2.3)，
\[
\|p_m(B)-G_{1,m}\|
\le2dd_0\alpha_m\rho_m^{-(d-1)}.
\tag{2.4}
\]
右边的对数至多
\[
-\frac{485}{6}d^4+\frac{155}{2}d^3
-300d+\frac{850}{3}+\log(2dd_0).
\]
对 \(d\ge1024\) 此数不大于 \(-80d^4\)：只需用
\((155/2)/d\le155/2048<5/6\)，其余线性项和对数项更小。
于是
\[
\boxed{\|p_m(B)-G_{1,m}\|\le\eta_m,\qquad
\eta_m:=e^{-80d^4}.}
\tag{2.5}
\]

## 3. 原 \(W\) 上的完整自配对锚

由 (1.2)，对任意 \(x\in M\)，
\[
(p_m(B)-d_0I)x\in N.
\]
故对 \(w\in W\)，在整个 \(M\) 上有准确伴随恒等
\[
P_Mp_m(B)^*w=d_0w.
\tag{3.1}
\]
与 (2.5) 合并给出真正向量估计
\[
\boxed{\|P_MG_{1,m}^*w-d_0w\|
\le\eta_m\|w\|\qquad(w\in W).}
\tag{3.2}
\]
尤其
\[
\boxed{\|P_WG_{1,m}|_W-d_0I_W\|\le\eta_m,}
\tag{3.3}
\]
\[
\boxed{
|\langle w,G_{1,m}w\rangle-d_0\|w\|^2|
\le\eta_m\|w\|^2.}
\tag{3.4}
\]
因此完整自配对的实部至少为
\((d_0-\eta_m)\|w\|^2\)。
这没有估计全环境的 \(\|G_{1,m}\|\)，也没有将
\(G_{1,m}w\) 中可能很大的 \(N\) 分量删成一个范数小量。

相同证明还适用于任意正整数 \(a\)：
令 \(p_{a,m}\) 为 \(f_{0,m}^{-a}\) 的 \(<d\) Taylor 截断，则
\[
\|p_{a,m}(B)-f_{0,m}(B_m)^{-a}\otimes I\|
\le d(2d_0)^a\alpha_m\rho_m^{-(d-1)}
\le\eta_m.
\tag{3.5}
\]
相应压缩常数为 \(d_0^a\)。这是绝对误差；若 \(a\) 随 \(m\) 增长，
不得不经比较便把它写成相对 \(d_0^a\) 的小误差。

## 4. 孔截断与原最小代表仍需共同支付

令 \(P_{\le q}^{(m)}\) 是原尾孔截断。有限头 \(G_{1,m}\) 与该截断交换，
所以
\[
\langle w,G_{1,m}w\rangle
=\langle P_{\le q}^{(m)}w,G_{1,m}P_{\le q}^{(m)}w\rangle
+\langle P_{>q}^{(m)}w,G_{1,m}P_{>q}^{(m)}w\rangle.
\tag{4.1}
\]
(3.4) 只支付左边的完整锚；尚未支付 (4.1) 第二项。
不能以未知速率的 \(\|P_{>q}^{(m)}w\|\to0\)
乘一个可能有四次指数增长的 \(\|G_{1,m}\|\) 后声称它消失。

同样，
[c26 的实际母顶部](2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)
给真正左最小代表在原 Hilbert 范数中的逼近；
本稿没有证明该逼近在带 \(G_{1,m}\) 的二次型或投影反馈中仍为小误差。
将 (3.4) 移到同一 \(U_qr_q\) 之前，必须支付这一真实最小化误差，
不能只用大环境范数乘母误差。

原同源代数 \(G_{1,m}A_m=B_m\) 仍允许把所需普通右费写为
\(\lambda_q(B_m(u_Q)_q)\)，而原 flat 费保持不变。
但它的完整未来候选、末端封口和高返回也没有由 (2.5) 自动构造出来。
因此本稿支付的是全局 carry 和原 \(W\) 的完整锚；
原左截断、普通右费以及 \(N=M\) 仍未闭合。
