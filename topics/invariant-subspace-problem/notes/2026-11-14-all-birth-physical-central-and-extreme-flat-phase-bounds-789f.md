# 全出生物理源的中央区与极平坦区完整相位界

日期：2026-11-14；工作标识789f。本稿把已经证明的完整物理来源公式与低次数多项式比较准确接合，处理整个硬源空间及真实 Moore–Penrose 逆。其结论适用于下述有限 Boolean 模型；原无限尾 graph 的跨段、裸项、负前缀及普通完整右费仍须另外支付。

依赖：[全部出生物理特征公式](2026-11-14-deficient-main-pool-all-birth-feature-grams-and-full-hard-regression-789f-next.md)；[共同多项式 Gram 与完整 Schur 比较](2026-11-14-bounded-degree-bernoulli-comparison-and-common-schur-phase-budget-789f.md)。

## 1. 同一个完整物理模型

取整数 \(Q\ge1\)、\(0\le d\le Q/2\)，主等权池长度
\[
 q_0=Q-2d,\qquad s=Q-d.
\]
主池删除权为1，另有 \(Q\) 个外部 Boolean 位，其删除权是 \(\sqrt{z_i}>0\)。在主池的完整对称 spin 模块与外部全 Boolean 张量上，取
\[
 V=\ker D\cap{\cal H}_{s-1},\qquad
 U=\ker D\cap{\cal H}_s.
\]
这里的低源 \(V\) 和硬源 \(U\) 均完整保留。令 \({\cal P}_r\) 为 \(Q\) 变量的齐次平方自由次数 \(r\) 多项式空间，\(\partial=\sum_i\partial_i\)。已经证明的、与权无关的系数空间为
\[
 E_d=\ker\partial^3\cap{\cal P}_{d+1},\qquad
 {\cal U}_d=\ker\partial\cap{\cal P}_d.                   \tag{1.1}
\]
它们分别参数化整个 \(V,U\)。若 \(q_0=0\)，则 \(Q=2d\)，模型就是原来的完整 \(Q\) 位 Boolean 空间，没有添加主池；这一点使结论能直接用于原连续尾的有限偶数位段。

给定 \(\phi\in E_d\)，置
\[
 \psi_\phi=\partial\phi-2\phi.
\]
使用真实条件概率
\[
 p_i(t)=\frac{z_it}{1+t(z_i-1)},\quad
 F_z(t)=\prod_i(1+t(z_i-1)),\quad
 \rho_z(t)=F_z(t)/\int_0^1F_z,
\]
以及 \(w_d(t)=[t(1-t)]^{-d}\)。下文期望先取 \(T\sim\rho_z\)，再在给定 \(T=t\) 时取独立 \(X_i\sim\operatorname{Bernoulli}(p_i(t))\)。

整个低源上的真实三个 Gram 及完整硬回归准确为
\[
 H_z[\phi]=\mathbb E\,w_d(T)\frac{1-T}{T}|\phi(X)|^2,
\]
\[
 L_z[\phi]=\mathbb E\,w_d(T)\frac{T}{1-T}|\phi(1-X)|^2,
\]
\[
 B_z[\phi]=\mathbb E\,w_d(T)|\psi_\phi(X)|^2,             \tag{1.2}
\]
\[
 M_z[\chi]=\mathbb E\,w_d(T)|\chi(X)|^2,\qquad
 C_z(\chi,\phi)=\mathbb E\,w_d(T)\overline{\chi(X)}
                                      \psi_\phi(X),
\]
\[
 R_z=C_z^*M_z^{-1}C_z,\qquad
 G_z=\tfrac14(B_z-R_z),\qquad
 J_z=H_zG_z^{-1}L_z-2G_z-R_z.                            \tag{1.3}
\]
其中 \(\chi\) 遍历整个 \({\cal U}_d\)。这些矩阵在同一个 \(E_d\) 坐标中取值，不替换为单侧均值、固定出生子块或删去硬源后的模型。

物理 Gram 与 (1.2)–(1.3) 只差同一个正标量
\[
 c_z=\frac{(q_0+1)\int_0^1F_z(t)\,dt}{\prod_i z_i}.
\]
特别真实物理相位矩阵是 \(c_zJ_z\)。若
\(J_z^*L_z^{-1}J_z\preceq\kappa H_z\)，乘此同一标量便是物理源上的原不等式。不能在不同 Gram 上分别丢掉不同归一化。

## 2. 中央区的显式全源界

**定理1。** 固定
\[
 0<a\le b<\infty,\qquad D_0,S_0<\infty,
\]
并设实际权满足
\[
 a\le z_i\le b,\quad
 \left|\sum_{i=1}^Q(z_i-1)\right|\le D_0,\quad
 \sum_{i=1}^Q(z_i-1)^2\le S_0.                           \tag{2.1}
\]
置 \(k=d+1\)、\(\ell=\min(1,a)\)、\(v=\max(1,b)\)，定义
\[
 r=\exp[-2D_0-S_0/(2\ell^2)],
\]
\[
 M_+=\max(1,\sqrt b/\ell)^k
          \exp\!\left(\frac{\sqrt{kS_0}}{2\ell}\right),
\quad
 M_-=\max(1,v/\sqrt a)^k
          \exp\!\left(\frac{\sqrt{kS_0}}{2\sqrt a}\right),
\]
\[
 \Theta=r^{-2}(M_+M_-)^2,\qquad
 \kappa=(2\Theta^2+3\Theta)^2.                           \tag{2.2}
\]
则在整个真实低源 \(V\) 上
\[
                 \boxed{J_z^*L_z^{-1}J_z\preceq
                                      \kappa H_z.}      \tag{2.3}
\]
对于固定 \(d,a,b,D_0,S_0\)，此界不依赖 \(Q\)、低源维数或硬源维数。

### 2.1 端点积分与共同次数

所有特征 \(\phi,\phi(1-X),\psi_\phi,\chi\) 都是次数至多 \(k=d+1\) 的多线性多项式。虽然 (1.2) 的积分权在端点可以发散，原特征满足
\[
 \chi(1-X)=(-1)^d\chi(X),\qquad
 \psi_\phi(1-X)=(-1)^{d+1}\psi_\phi(X),                  \tag{2.4}
\]
\[
 \phi(1-X)=(-1)^{d+1}
       \left(\phi(X)-\partial\phi(X)
                           +\tfrac12\partial^2\phi(X)\right).
                                                               \tag{2.5}
\]
因此 \(\chi,\psi_\phi\) 在两个端点的最低非零次数均至少为 \(d\)；
\(\phi\) 在左端的次数为 \(d+1\)，右端反射后的最低次数至少
\(\max(d-1,0)\)。这些次数分别支付 \(w_d\) 和 \(w_d(1-t)/t\) 的端点因子；\(L_z\) 由反射得到同样结论。\(d=0\) 时直接使用非负最低次数，积分也有限。

所以可以对 \(H,L\) 的各自共同权，以及联合硬源与 \(\psi\) 的共同权 \(w_d\)，使用同一个多项式比较常数。端点可积性来自整个物理来源条件，而不是把发散权截断后省略极限。

### 2.2 完整硬源 Schur 和等权标定

令
\[
 {\cal K}_z=
 \begin{pmatrix}M_z&C_z\\ C_z^*&B_z\end{pmatrix},\qquad
 \alpha=r/M_-^2,\quad\beta=M_+^2/r .
\]
共同 Gram 定理给
\[
 \alpha{\cal K}_0\preceq{\cal K}_z\preceq\beta{\cal K}_0,
\quad
 \alpha H_0\preceq H_z\preceq\beta H_0,\quad
 \alpha L_0\preceq L_z\preceq\beta L_0.                  \tag{2.6}
\]
这里下标0表示相同 \(Q,d,E_d,{\cal U}_d\) 在 \(z_i=1\) 时的度量。真实等权 spin1 标定已经证明
\[
 H_0=L_0=:B_0>0,\qquad G_0=B_0/2,\qquad
 C_0=R_0=0,\qquad B_{\text{feature},0}=2B_0.             \tag{2.7}
\]
在同一个完整硬源空间上对联合形式取下确界，
\[
 4G_z[\phi]=
 \inf_{\chi\in{\cal U}_d}
      \mathbb E\,w_d(T)|\psi_\phi(X)-\chi(X)|^2,
\]
从 (2.6) 得
\[
 \tfrac{\alpha}{2}B_0\preceq G_z\preceq
                  \tfrac{\beta}{2}B_0,\qquad
 0\preceq R_z\preceq2\beta B_0.                          \tag{2.8}
\]
这里没有错误地从 \(R_0=0\) 推断 \(R_z=0\)；倾斜后的整个硬回归由 (2.8) 支付。

共同作 \(B_0^{-1/2}\) 合同且保持原乘法次序，
\[
 \|B_0^{-1/2}J_zB_0^{-1/2}\|
              \le 2\beta^2/\alpha+3\beta.
\]
再用 \(H_z,L_z\succeq\alpha B_0\) 归一，正好给 (2.3) 与 (2.2)。证明包括真正的 \(G_z^{-1}\)，没有用不同子空间的最小逆替换它。

## 3. 出生也增长时的统一极平坦界

**定理2。** 固定 \(0<\eta\le1/2\)、\(C_0,D_0<\infty\)。允许 \(d,Q\) 同时变化，仍置 \(k=d+1\)。如果实际外场满足
\[
 \max_i|z_i-1|\le\eta/k,\qquad
 k\sum_i(z_i-1)^2\le C_0,\qquad
 \left|\sum_i(z_i-1)\right|\le D_0,                      \tag{3.1}
\]
那么 (2.3) 成立，且可以统一取
\[
 \Theta_*=\exp\{4D_0+4C_0+12\eta+
                               (2+\sqrt2)\sqrt{C_0}\},
\]
\[
             \boxed{\kappa_*=(2\Theta_*^2+3\Theta_*)^2.} \tag{3.2}
\]
常数同时不依赖 \(d,Q\) 和两个物理源空间的维数。

证明是在定理1中取
\[
 a=1-\eta/k,\quad b=1+\eta/k,\quad S_0=C_0/k.
\]
由 \(\ell=a\ge1/2\)、\(v=b\) 以及
\[
 k\log\frac{1+\eta/k}{1-\eta/k}\le4\eta
\]
可按共同 Gram 定理第6节直接得到
\(\Theta\le\Theta_*\)。完整来源、端点和硬源 Schur 已在第2节付清，因此这一代入是物理模型上的定理，不再只是等待来源识别的抽象接口。

## 4. 对原偶数位尾段的准确用途

当 \(Q=2d\) 时主池为空，定理1–2直接作用于原有限全 Boolean 的中央低 primitive 与中央硬源。此时可将全部删除权同时乘一个正标量，以便选择方便的平方权归一化；完整相位比在这一共同缩放下不变。原连续尾 \(b_j=j^{-2}\) 的短段，经共同归一后可检验 (2.1) 或 (3.1)，从而取得全中央源界。

这不提供原无限尾的 reducing 分解。也没有证明所有高度、所有未受控出生、实际 \(Z_q^{-1}\) 所产生的尾标签局部化或整个 graph 接合 Gram 的统一预算。接下来直接对原连续权段计算可用窗口和增长率，再在同一实际来源上接原左右、裸项与负前缀费用。
