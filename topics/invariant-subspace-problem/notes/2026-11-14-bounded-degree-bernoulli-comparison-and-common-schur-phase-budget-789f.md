# 有限次数 Bernoulli 多项式的维数无关比较与完整 Schur 相位预算

日期：2026-11-14；工作标识789f。本稿先证明一个不依赖位数的完整多项式 Gram 比较，再给同一 nuisance 空间下的相位推论。物理模型的来源识别和等权标定须准确满足第5节条件，不能仅凭形式相似套用。

## 1. 平方自由系数空间上的移位

对 \(N\) 个变量，令 \({\cal P}_{\le k}\) 是次数至多 \(k\) 的多线性多项式空间；若 \(k>N\) 可将 \(k\) 换成 \(N\)。以平方自由单项式 \(Z_I=\prod_{i\in I}Z_i\) 的系数平方和作为范数。不同次数层相互正交。

给定 \(\delta\in\mathbb R^N\)，定义降次算子
\[
 (A_\delta c)_{I}=\sum_{j\notin I}\delta_j c_{I\cup\{j\}}.
\]
对齐次 \(r\) 层，Cauchy–Schwarz 给
\[
 \sum_{|I|=r-1}\left|\sum_{j\notin I}\delta_jc_{I\cup\{j\}}\right|^2
 \le \|\delta\|_2^2
       \sum_{|I|=r-1}\sum_{j\notin I}|c_{I\cup\{j\}}|^2
 =r\|\delta\|_2^2\sum_{|J|=r}|c_J|^2.
\]
因此
\[
 \|A_\delta\|_{{\cal P}_{\le k}}\le\sqrt k\,\|\delta\|_2,
 \qquad
 \|\exp A_\delta\|\le e^{\sqrt k\,\|\delta\|_2}.          \tag{1.1}
\]
有限多项式指数 \(\exp A_\delta\) 正是代入 \(Z_i\mapsto Z_i+\delta_i\)：每个被删除指标出现一次，\(r!\) 个排列由指数的 \(r!\) 抵消。

若再作 \(Z_i\mapsto \sigma_i Z_i\)，其系数对角算子在第 \(r\) 层乘
\(\prod_{i\in I}\sigma_i\)。若 \(0<\sigma_-\le\sigma_i\le\sigma_+\)，则
\[
 \|\Gamma_\sigma\|\le\max(1,\sigma_+)^k.                 \tag{1.2}
\]
这些估计完全按系数空间算子范数取得，没有乘上单项式个数或位数。

## 2. 两个乘积 Bernoulli 度量

取 \(0<t<1\)，令 \(\mu_t\) 是各位参数均为 \(t\) 的乘积 Bernoulli 测度；令 \(\mu_p\) 是各位参数 \(p_i\in(0,1)\) 的乘积测度。置
\[
 Z_i=\frac{X_i-t}{\sqrt{t(1-t)}},\qquad
 Y_i=\frac{X_i-p_i}{\sqrt{p_i(1-p_i)}},
\]
\[
 \delta_i=\frac{p_i-t}{\sqrt{t(1-t)}},\qquad
 \sigma_i=\sqrt{\frac{p_i(1-p_i)}{t(1-t)}}.
\]
\(\{Z_I\}\) 与 \(\{Y_I\}\) 分别是两个乘积测度下的正交归一基，且准确有
\[
                          Z_i=\delta_i+\sigma_iY_i.
\]
故任意 \(f\in{\cal P}_{\le k}\) 的范数满足
\[
 \|f\|_{L^2(\mu_p)}
 \le M_+\|f\|_{L^2(\mu_t)},\qquad
 M_+=\max(1,\sigma_+)^k e^{\sqrt k\|\delta\|_2}.          \tag{2.1}
\]
逆代入是 \(Y_i=-\delta_i/\sigma_i+Z_i/\sigma_i\)，因此
\[
 \|f\|_{L^2(\mu_t)}
 \le M_-\|f\|_{L^2(\mu_p)},\qquad
 M_-=\max(1,\sigma_-^{-1})^k
              e^{\sqrt k\|(\delta_i/\sigma_i)_i\|_2}.   \tag{2.2}
\]
这是所有低次数多项式的共同双边比较，不仅比较单个均值或协方差条目。

## 3. 实际加权 Boolean 条件概率与全部积分权

取 \(a\le z_i\le b\)，\(0<a\le b<\infty\)，并令
\[
 p_i(t)=\frac{z_it}{1+t(z_i-1)},\quad
 D=\sum_i(z_i-1),\quad S=\sum_i(z_i-1)^2.
\]
设 \(|D|\le D_0,\ S\le S_0\)，记
\[
 \ell=\min(1,a),\qquad v=\max(1,b),\qquad
 r=\exp[-2D_0-S_0/(2\ell^2)].
\]
直接计算
\[
 \delta_i=\frac{(z_i-1)\sqrt{t(1-t)}}{1+t(z_i-1)},\qquad
 \sigma_i=\frac{\sqrt{z_i}}{1+t(z_i-1)},
\]
所以可在全部 \(t\in(0,1)\) 同时取
\[
 \|\delta\|_2\le\frac{\sqrt{S_0}}{2\ell},\qquad
 \|(\delta_i/\sigma_i)_i\|_2\le\frac{\sqrt{S_0}}{2\sqrt a},
\]
\[
 \frac{\sqrt a}{v}\le\sigma_i\le\frac{\sqrt b}{\ell}.
\]
定义明确常数
\[
 {\cal M}_+
 =\max(1,\sqrt b/\ell)^k
               \exp\!\left(\frac{\sqrt{kS_0}}{2\ell}\right),
\]
\[
 {\cal M}_-
 =\max(1,v/\sqrt a)^k
               \exp\!\left(\frac{\sqrt{kS_0}}{2\sqrt a}\right).
                                                               \tag{3.1}
\]

实际混合密度是
\[
 \rho_z(t)=\frac{\prod_i(1+t(z_i-1))}
                 {\int_0^1\prod_i(1+s(z_i-1))\,ds}.
\]
Taylor 的真实二阶余项给
\[
 Dt-\frac{t^2S}{2\ell^2}
 \le \log\prod_i(1+t(z_i-1))\le Dt,
\]
从而
\[
                           r\le\rho_z(t)\le r^{-1}.    \tag{3.2}
\]
等权 \(z_i=1\) 的参考密度为1。

令 \(w(t)\ge0\) 为任意共同可测积分权，允许在端点发散。对任何固定多项式族
\(f_1,\ldots,f_n\in{\cal P}_{\le k}\)，只要参考积分有限，定义
\[
 (K_z)_{ij}=\int_0^1w(t)\rho_z(t)
          \mathbb E_{\mu_{p(t)}}[\overline{f_i(X)}f_j(X)]\,dt,
\]
\[
 (K_0)_{ij}=\int_0^1w(t)
          \mathbb E_{\mu_t}[\overline{f_i(X)}f_j(X)]\,dt.
\]
则所有加权积分也有限，且
\[
                    \boxed{\alpha K_0\preceq K_z\preceq\beta K_0,}
                                                               \tag{3.3}
\]
其中
\[
                         \alpha=r/{\cal M}_-^2,\qquad
                         \beta={\cal M}_+^2/r.          \tag{3.4}
\]
证明是在每个 \(t\) 对任意共同线性组合 \(\sum c_if_i\) 应用
(2.1)–(2.2)，再乘正权并积分。反射特征 \(f_i(1-X)\) 仍是次数至多 \(k\) 的多线性多项式，所以同样适用。

## 4. 必须在完整共同空间内取 Schur

取固定目标空间和固定 nuisance 空间，将它们的全部特征一起代入 (3.3)，得到
\[
 K_z=\begin{pmatrix}M_z&C_z\\C_z^*&Q_z\end{pmatrix},
 \qquad \alpha K_0\preceq K_z\preceq\beta K_0.
\]
假设 \(M_0,M_z>0\)。定义
\[
 S_z=Q_z-C_z^*M_z^{-1}C_z,\qquad R_z=C_z^*M_z^{-1}C_z.
\]
对每个同一目标系数 \(c\)，
\[
 c^*S_zc=\inf_\eta
   \left\langle\binom{\eta}{c},
                  K_z\binom{\eta}{c}\right\rangle.
\]
在**同一个** nuisance 空间中取上下界的 infimum，准确给
\[
                     \alpha S_0\preceq S_z\preceq\beta S_0.
                                                               \tag{4.1}
\]
也有 \(0\preceq R_z\preceq Q_z\)。本稿没有从各块的分离比较推出
\(R_z\preceq\beta R_0\)；即使 \(R_0=0\)，倾斜后 \(R_z\) 仍可能非零。

## 5. 一个可直接代入物理来源的相位推论

假设某个已准确识别的源模型具有：
\[
 G_z=S_z/4,\qquad
 J_z=H_zG_z^{-1}L_z-2G_z-R_z,
\]
其中 \(H_z,L_z\) 也分别由次数至多 \(k\) 的同一固定来源和共同正积分权取得，因而满足 (3.3)。进一步假设其等权标定准确为
\[
 H_0=L_0=B>0,\quad C_0=0,\quad Q_0=2B.
                                                               \tag{5.1}
\]
那么 \(G_0=B/2\)。由 (3.3)、(4.1)，
\[
 \alpha B\preceq H_z,L_z\preceq\beta B,\qquad
 \tfrac\alpha2B\preceq G_z\preceq\tfrac\beta2B,\qquad
 0\preceq R_z\preceq2\beta B.
\]
作所有矩阵相同的 \(B^{-1/2}\) 合同，原乘法次序保持，因此
\[
 \|B^{-1/2}J_zB^{-1/2}\|
                \le 2\beta^2/\alpha+3\beta.
\]
再以真实 \(H_z,L_z\) 的同源下界归一，得到
\[
 \boxed{J_z^*L_z^{-1}J_z\preceq
          (2\Theta^2+3\Theta)^2H_z,\qquad
           \Theta=\beta/\alpha
                  =r^{-2}({\cal M}_+{\cal M}_-)^2.}     \tag{5.2}
\]
常数不依赖位数或来源维数，但显式依赖次数 \(k\)。不允许先删 nuisance、换成不同物理来源、或省略 (5.1) 再使用它。

## 6. 次数增长时仍可统一的极平坦区

设 \(k\ge1\)，并有固定 \(0<\eta\le1/2\)、\(C_0,D_0<\infty\)，满足
\[
 |z_i-1|\le\eta/k,\qquad
 k\sum_i(z_i-1)^2\le C_0,\qquad
 \left|\sum_i(z_i-1)\right|\le D_0.
\]
取 \(a=1-\eta/k,b=1+\eta/k,S_0=C_0/k\)。因为
\[
 k\log\!\left(\frac{1+\eta/k}{1-\eta/k}\right)\le4\eta,
\]
(3.1)–(3.4) 给
\[
 \Theta\le
 \exp\{4D_0+4C_0+12\eta+(2+\sqrt2)\sqrt{C_0}\}.          \tag{6.1}
\]
所以满足第5节准确来源条件的模型，在这个区域有不依赖 \(k,N\) 的统一有限相位预算。

该结论是共同多项式 Gram 与完整 Schur 的定理。其作用在于给更高次数的物理源一个可付接口；不把任意非线性来源都当作固定低次数，也不将未验证的等权标定或原 graph 的两侧费用当作已完成。
