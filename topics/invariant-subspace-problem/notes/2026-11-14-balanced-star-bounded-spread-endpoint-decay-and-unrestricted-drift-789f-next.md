# 平衡 star 的有界平方偏差端峰：全源一致衰减与去掉总漂移限制

日期：2026-11-14；工作标识：789f。

## 0. 结论及量词

沿用真实平衡 star 的完整二值源：
\[
 F(t)=\prod_{i=1}^Q(1-t+z_it),\qquad
 \rho(t)=F(t)/\int_0^1F,\qquad
 X_i\mid T=t\ \text{独立 Bernoulli}\left(\frac{z_it}{1-t+z_it}\right).
\]
记
\[
 m=\mathbb EX,\quad y=2m-\mathbf1,\quad
 G=\operatorname{Cov}(X),\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*,
\]
\[
                         J=HG^{-1}L-2G-yy^*.
\]
只假设固定常数
\[
 0<a\leq z_i\leq b<\infty,\qquad
                   \sum_{i=1}^Q(z_i-1)^2\leq S_0.        \tag{0.1}
\]
不固定 \(Q\)、组数、各组比例或总漂移。

定义实际右端漂移
\[
 R=\sum_i(1-z_i^{-1})
   =\sum_i(z_i-1)-\sum_i\frac{(z_i-1)^2}{z_i}.             \tag{0.2}
\]
**定理。** 存在只依赖 \(a,b,S_0\) 的有限常数 \(R_0,C\)，使每个满足 (0.1) 且 \(R\geq R_0\) 的完整有限行都有
\[
 \boxed{
 J^*L^{-1}J\preceq\frac C R H.}                           \tag{0.3}
\]
所有余项在完整 \(Q\) 维源上按算子范数一致；没有先固定组数或先取逐源极限。因此 \(R\to+\infty\) 时，整个真实相位一致趋于零。

本稿给出这一一致衰减的完整证明，但不将 \(C,R_0\) 的保守数值逐项最优化或汇总成一个数字。下文每个余项的常数均只由明确的固定参数界及有限阶矩控制；它们可由所列估计直接取成有限数。与已经给出全显式常数的中央窗口定理拼接后，得到：

**推论。** 对每个固定 \(a,b,S_0\)，存在一个有限
\(\kappa(a,b,S_0)\)，使 (0.1) 下所有有限 \(Q\) 都满足
\[
                         J^*L^{-1}J\preceq\kappa H.       \tag{0.4}
\]
这里不再要求总漂移有界。它仍不是任意正权的绝对统一常数，也不自动关闭原 graph 的跨出生接口。

## 1. 真实端峰尺度和统一矩估计

置
\[
 \alpha_i=z_i^{-1},\qquad d_i=1-\alpha_i,\qquad
 M^2=S_0/a^2.
\]
于是
\[
 1/b\leq\alpha_i\leq1/a,\qquad
 \sum_i d_i^2\leq M^2,\qquad
 R=\sum_i d_i.
\]
本节取 \(R\geq1\)，并记
\[
 \varepsilon=R^{-1},\qquad
 \theta=R/\sqrt Q,\qquad
                 0<\theta\leq M.                         \tag{1.1}
\]
最后一个不等式是 Cauchy–Schwarz。若 \(S_0=0\)，则 \(R=0\)，本端峰范围为空；此时中央定理已经覆盖该行。

令 \(x=1-T\)。除去不影响密度的常数 \(\prod_i z_i\)，其真实密度正比于
\[
                       g(x)=\prod_i(1-d_ix),\quad 0<x<1.
\]
设 \(u=\max\{1,b\}\)。对每个 \(0\leq x\leq1\)，有
\[
 -Rx-\frac{u^2M^2}{2}x^2
                   \leq\log g(x)\leq-Rx.                \tag{1.2}
\]
因为 \(1-d_ix\geq1/u\)，这是 \(\log\) 的真实二阶余项界，允许 \(d_i\) 同时有正、负号。

记 \(\beta_k=\mathbb Ex^k\)。对任意固定非负整数 \(k\)，(1.2) 给
\[
 \boxed{\beta_k=k!\varepsilon^k+
                  O_{a,b,S_0,k}(\varepsilon^{k+2})}
                  \quad(k\geq1).                         \tag{1.3}
\]
这一估计对 \(Q\) 和所有允许权一致。为明确其依据，
\[
 0\leq e^{-Rx}-g(x)
       \leq\frac{u^2M^2}{2}x^2e^{-Rx}.
\]
因此未归一化的第 \(k\) 矩与
\(\int_0^\infty x^ke^{-Rx}dx=k!\varepsilon^{k+1}\)
的差，由一个明确的 \((k+2)!\varepsilon^{k+3}\) 项及
\(\int_1^\infty x^ke^{-Rx}dx\) 控制。后者在 \(R\geq1\) 上也不超过一个只依赖 \(k\) 的常数乘 \(\varepsilon^{k+3}\)。归一化分母为
\(\varepsilon+O_{a,b,S_0}(\varepsilon^3)\)，在统一的充分大 \(R\) 上至少为 \(\varepsilon/2\)，得到 (1.3)。

以后只用到有限个这样的矩，例如 \(k\leq10\)。特别
\[
 \beta_1=\varepsilon+O(\varepsilon^3),\quad
 \beta_2=2\varepsilon^2+O(\varepsilon^4),\quad
 \beta_3=6\varepsilon^3+O(\varepsilon^5),
\]
\[
 \operatorname{Var}(x)=\varepsilon^2+O(\varepsilon^4),
 \qquad
 \operatorname{Cov}(x,x^2)=4\varepsilon^3+O(\varepsilon^5).
                                                               \tag{1.4}
\]

## 2. 完整源的一个集体方向与整个正交补

令
\[
 e=Q^{-1/2}\mathbf1,\qquad P=I-ee^*,\qquad
 \mathcal V=e^\perp.
\]
以下 \(P\) 后的矩阵都限制在完整的 \(\mathcal V\)，不是选取一个小的对称试探源。置
\[
 A=P\operatorname{diag}(\alpha_i)P|_{\mathcal V},\qquad
 B=P\operatorname{diag}(\alpha_i d_i)P|_{\mathcal V},
\]
\[
 b_1=Pd,\qquad b_2=P(d_i^2)_i.
\]
有
\[
 b^{-1}I_{\mathcal V}\preceq A\preceq a^{-1}I_{\mathcal V},
 \qquad
 \|b_1\|\leq M,\qquad
 \|b_2\|\leq \max_i|d_i|\,M.                              \tag{2.1}
\]
这里右侧的 \(a,b\) 是 (0.1) 的参数。

以下性质使所有余项与维数无关。记
\(D_\infty=\max\{|1-a^{-1}|,|1-b^{-1}|\}\)。对 \(j\geq1\)，
\[
 \|P(d_i^j)_i\|\leq D_\infty^{j-1}M,
 \qquad e^*d=\theta.
\]
对 \(j\geq2\)，更有
\[
 |e^*(d_i^j)_i|
 \leq D_\infty^{j-2}M^2/\sqrt Q
 =D_\infty^{j-2}M^2\varepsilon\theta.                     \tag{2.2}
\]
只有 \(d\) 的一次和为 \(R\)；所有更高次和都有共同界。

以 \(\mathbb Ce\oplus\mathcal V\) 为同一个物理正交分解，定义三个不同但明确的正合同
\[
 \mathcal B_H=
 \begin{pmatrix}\sqrt\varepsilon\,\theta&0\\0&\varepsilon^{-1}I\end{pmatrix},
 \qquad
 \mathcal B_L=
 \begin{pmatrix}\sqrt\varepsilon\,\theta&0\\0&I\end{pmatrix},
\]
\[
 \mathcal B_G=\varepsilon^{-1/2}\mathcal B_L
       =\begin{pmatrix}\theta&0\\0&\varepsilon^{-1/2}I\end{pmatrix}.
                                                               \tag{2.3}
\]
记
\[
 \widehat H=\mathcal B_HH\mathcal B_H,\quad
 \widehat L=\mathcal B_LL\mathcal B_L,\quad
 \widehat G=\mathcal B_GG\mathcal B_G.
\]
每个 \(\theta>0\)，所以这些合同在每一有限行都可逆。以下估计允许
\(\theta\to0\)，不会把 \(1/\theta\) 藏进误差常数。

## 3. 保留真实噪声的全块展开

给定 \(x\)，缺位概率为
\[
 \pi_i(x)=1-p_i(1-x)
        =\frac{\alpha_i x}{1-d_ix}.
\]
令 \(v_i(x)=(1-d_ix)^{-1}\)。原完整条件矩严格写成
\[
 H=\mathbb E x(1-x)v(x)v(x)^*
        +\operatorname{diag}\mathbb E[\alpha_i x^2v_i(x)^2],
                                                               \tag{3.1}
\]
\[
 L=\mathbb E x(1-x)
       [\operatorname{diag}(\alpha_i)v(x)]
       [\operatorname{diag}(\alpha_i)v(x)]^*
        +\operatorname{diag}\mathbb E[
                   \alpha_i(1-x)^2v_i(x)^2],              \tag{3.2}
\]
\[
 G=\operatorname{Cov}(\pi(x))
        +\operatorname{diag}\mathbb E[
                   \alpha_i x(1-x)v_i(x)^2].              \tag{3.3}
\]
尤其 (3.3) 的噪声分子是 \(\alpha_i x(1-x)\)。若错删其中的
\(1-x\)，下文危险的交叉抵消会被破坏。

使用 (1.3)–(1.4)、(2.2)，将
\[
 v_i(x)=1+d_ix+d_i^2x^2+
                  \frac{d_i^3x^3}{1-d_ix}
\]
代入 (3.1)–(3.3)，得到以下完整块展开：
\[
 \begin{array}{c|c|c|c}
 &00&01&11\\ \hline
 \widehat H
 &1-2\varepsilon+O(\varepsilon^2)
 &2\sqrt\varepsilon\,b_1^*+O(\varepsilon^{3/2})
 &2A+O(\varepsilon)\\[1mm]
 \widehat G
 &1-\varepsilon\theta^2+O(\varepsilon^2)
 &-\sqrt\varepsilon\,b_1^*
       +4\varepsilon^{3/2}(b_1-b_2)^*
       +O(\varepsilon^{5/2})
 &A+\varepsilon(4B-2A+b_1b_1^*)+O(\varepsilon^2)\\[1mm]
 \widehat L
 &1-\varepsilon(2+\theta^2)+O(\varepsilon^2)
 &-\sqrt\varepsilon\,b_1^*
       +\varepsilon^{3/2}(4b_1-2b_2)^*
       +O(\varepsilon^{5/2})
 &A+\varepsilon(2B-2A+b_1b_1^*)+O(\varepsilon^2).
 \end{array}                                             \tag{3.4}
\]
10 块是相应的伴随。

为使 (3.4) 的系数和余项可直接重建，列出所需的原条件展开：
\[
 \begin{aligned}
 \operatorname{diag}\mathbb E[\alpha_i x^2v_i^2]
       &=2\varepsilon^2\operatorname{diag}(\alpha_i)
          +12\varepsilon^3\operatorname{diag}(\alpha_i d_i)
          +O(\varepsilon^4),\\
 \operatorname{diag}\mathbb E[\alpha_i(1-x)^2v_i^2]
       &=\operatorname{diag}(\alpha_i)
          +\varepsilon\operatorname{diag}(2\alpha_i d_i-2\alpha_i)
          +O(\varepsilon^2),\\
 \operatorname{diag}\mathbb E[\alpha_i x(1-x)v_i^2]
       &=\varepsilon\operatorname{diag}(\alpha_i)
          +2\varepsilon^2\operatorname{diag}(2\alpha_i d_i-\alpha_i)
          +O(\varepsilon^3),                              \tag{3.5}\\
 \pi(x)&=\alpha x+(\alpha_i d_i)_i x^2+
                        (\alpha_i d_i^2)_i x^3+O_{\ell^2}(x^4).
 \end{aligned}
\]
在最后一个式子中，从二次项开始的所有系数向量都有统一
\(\ell^2\) 界；余项也有此界，因为 \(1-d_ix\geq1/\max\{1,b\}\)。
第一系数 \(\alpha=\mathbf1-d\) 的大分量始终按
\(\mathbf1-d\) 保留。

外积部分使用
\[
 \mathbb Ex(1-x)=\varepsilon-2\varepsilon^2+O(\varepsilon^3),
\quad
 \mathbb Ex^2(1-x)=2\varepsilon^2-6\varepsilon^3+O(\varepsilon^4)
\]
及 (1.4)。例如 \(G\) 的外积首两项为
\[
 \varepsilon^2\alpha\alpha^*
  +4\varepsilon^3[
        \alpha(\alpha_i d_i)_i^*
         +(\alpha_i d_i)_i\alpha^*]
\]
加上由四阶及更高矩控制的项。对 01 块作 (2.3) 合同后，
\(\sqrt Q\) 因子总与
\(\theta\sqrt Q=\varepsilon^{-1}\) 配对；对含
\(\sum d_i^j\)、\(j\geq2\) 的项，再使用 (2.2)。
这给出 (3.4) 所标的算子范数余项，常数仅依赖 \(a,b,S_0\)。
特别，表中三个 01 块保留了同一个完整集体方向和同一个
\(\mathcal V\)，不能分别换成各自的有利源。

由 (2.1)、(3.4)，在统一的充分大 \(R\) 上，存在只依赖
\(a,b,S_0\) 的 \(c_0,C_0>0\)，使
\[
 c_0I\preceq\widehat H,\widehat G,\widehat L\preceq C_0I.  \tag{3.6}
\]

## 4. 危险上右反馈的逐坐标消去

写 \(\mathcal T=\widehat G^{-1}\widehat L\)。从 (3.4) 直接有
\[
 \widehat L-\widehat G=
 \begin{pmatrix}
  -2\varepsilon+O(\varepsilon^2)
       &2\varepsilon^{3/2}b_2^*+O(\varepsilon^{5/2})\\
  2\varepsilon^{3/2}b_2+O(\varepsilon^{5/2})
       &-2\varepsilon B+O(\varepsilon^2)
 \end{pmatrix}.                                          \tag{4.1}
\]
完整逆的 01 块是
\[
 (\widehat G^{-1})_{01}
       =\sqrt\varepsilon\,b_1^*A^{-1}
                           +O(\varepsilon^{3/2}).
\]
因此，若只按三角不等式估计，\(\mathcal T_{01}\) 会留下一个
\(O(\varepsilon^{3/2})\) 项；之后真实相位的非对称源尺度会把它放大。
必须保留
\[
 (\mathcal T-I)_{01}
   =2\varepsilon^{3/2}
          [b_2^*-b_1^*A^{-1}B]+O(\varepsilon^{5/2}).       \tag{4.2}
\]

这一差有逐坐标的准确恒等式。令
\(D_\perp=P\operatorname{diag}(d_i)P|_{\mathcal V}\)。
由 \(\alpha_i=1-d_i\)、\(e^*d=\theta\)、\(Q^{-1/2}=\varepsilon\theta\)，
\[
 P\operatorname{diag}(\alpha_i)e=-\varepsilon\theta\,b_1,
 \qquad
 e^*\operatorname{diag}(d_i)P=\varepsilon\theta\,b_1^*.
\]
于是
\[
                 B=A D_\perp-\varepsilon^2\theta^2b_1b_1^*,
\]
\[
 b_1^*D_\perp=b_2^*-\varepsilon\theta^2b_1^*,
\]
从而
\[
 \boxed{
 b_2^*-b_1^*A^{-1}B
   =\varepsilon\theta^2b_1^*
     +\varepsilon^2\theta^2
           (b_1^*A^{-1}b_1)b_1^*.}                       \tag{4.3}
\]
两项的系数和向量都有统一界。因此 (4.2) 实际提高为
\(O(\varepsilon^{5/2})\)。同时，其余块由 (4.1) 给
\[
 \boxed{
 \mathcal T=
 \begin{pmatrix}
  1-2\varepsilon+O(\varepsilon^2)
                  &O(\varepsilon^{5/2})\\
  O(\varepsilon^{3/2})
                  &I-2\varepsilon A^{-1}B+O(\varepsilon^2)
 \end{pmatrix}.}                                         \tag{4.4}
\]
这是完整逆之后的非交换乘积。右上和左下的阶数不同，不能用普通
转置或两边各自的范数把它们混同。

## 5. 原有序 \(J\) 的三个大项共同抵消

令
\[
 \mathcal R=\begin{pmatrix}1&0\\0&\varepsilon I\end{pmatrix}
             =\mathcal B_L\mathcal B_H^{-1}.
\]
由 (2.3) 严格得到
\[
 \mathcal B_L HG^{-1}L\mathcal B_H
    =\varepsilon^{-1}
         \mathcal R\widehat H\mathcal R
                 \mathcal T\mathcal R^{-1}.              \tag{5.1}
\]
将 (3.4)、(4.4) 保持原次序相乘，得
\[
 \mathcal B_L HG^{-1}L\mathcal B_H
   =
 \begin{pmatrix}
  \varepsilon^{-1}-4+O(\varepsilon)
      &2\varepsilon^{-1/2}b_1^*+O(\sqrt\varepsilon)\\
  2\sqrt\varepsilon\,b_1+O(\varepsilon^{3/2})
      &2A+O(\varepsilon)
 \end{pmatrix}.                                          \tag{5.2}
\]
例如，(4.4) 的右上 \(O(\varepsilon^{5/2})\) 在这里恰变为
\(O(\sqrt\varepsilon)\)，这说明 (4.3) 不是可省的技术余项。

另一方面，由
\[
 \mathbb E\pi(x)
       =\beta_1\alpha
         +2\varepsilon^2(\alpha_i d_i)_i
         +O_{\ell^2}(\varepsilon^3),
 \qquad \beta_1=\varepsilon+O(\varepsilon^3)
\]
并将第一项的大集体分量按 (1.3) 保留，得到
\[
 (\mathcal B_Ly)_0=(\mathcal B_Hy)_0
          =\varepsilon^{-1/2}-2\sqrt\varepsilon
                                  +O(\varepsilon^{3/2}),
\]
\[
 (\mathcal B_Ly)_1=2\varepsilon b_1+O(\varepsilon^2),
 \qquad
 (\mathcal B_Hy)_1=2b_1+O(\varepsilon).                    \tag{5.3}
\]
最后
\[
                   \mathcal B_LG\mathcal B_H
                       =\varepsilon\widehat G\mathcal R^{-1}.
\]
因此 (5.2) 的 \(\varepsilon^{-1}-4\)、危险
\(2\varepsilon^{-1/2}b_1^*\)、左下
\(2\sqrt\varepsilon b_1\) 分别与同一个硬源平方抵消，而右下 \(2A\)
与 \(2G\) 抵消。最终
\[
 \boxed{
 \widetilde J:=\mathcal B_LJ\mathcal B_H
   =
 \begin{pmatrix}
       O(\varepsilon)&O(\sqrt\varepsilon)\\
       O(\varepsilon^{3/2})&O(\varepsilon)
 \end{pmatrix},\qquad
                         \|\widetilde J\|\leq C_1\sqrt\varepsilon.}
                                                               \tag{5.4}
\]
所有常数依然与 \(Q\) 和 \(\theta^{-1}\) 无关。

注意 (5.3) 的短写法中，沿 \(\alpha\) 的大向量误差必须保留为
\((\beta_1-\varepsilon)\alpha\)，不能把它免费称为维数无关的普通
\(\ell^2\) 误差。其系数是 \(O(\varepsilon^3)\)；
作 00 合同后是 \(O(\varepsilon^{5/2})\)，在正交补上则因
\(P\alpha=-b_1\) 而有真正统一的 \(\ell^2\) 界。这与第 3 节处理
大向量 \(\alpha\) 的规范相同。

(3.6)、(5.4) 给
\[
 \widetilde J^*\widehat L^{-1}\widetilde J
                 \preceq C_2\varepsilon\,\widehat H.
\]
由于 \(\widetilde J=\mathcal B_LJ\mathcal B_H\)，这恰等价于
(0.3)，不是一个更换了源或度量的相位。

## 6. 反端、全部总漂移与分组

将权平方改成 \(z_i'=z_i^{-1}\)，并同时作
\(T'=1-T,\ X'=\mathbf1-X\)，是真正的同模型变换：
\[
 H'=L,\quad L'=H,\quad G'=G,\quad y'=-y,\quad J'=J^*.
\]
因此
\[
 J'^*L'^{-1}J'\preceq\kappa H'
\quad\Longleftrightarrow\quad
 J^*L^{-1}J\preceq\kappa H
\]
由两个标准化交叉算子互为伴随而严格等价。倒数权仍满足固定正
上下界，并且
\[
 \sum_i(z_i^{-1}-1)^2\leq S_0/a^2.
\]
其右端漂移恰为
\[
                  \sum_i(1-z_i)=-\sum_i(z_i-1).
\]
于是总漂移 \(\sum_i(z_i-1)\to-\infty\) 的另一端也有全源一致衰减。

设原总漂移为 \(A_{\rm tot}\)。由 (0.2)，
\[
            A_{\rm tot}-S_0/a\leq R\leq A_{\rm tot}.
\]
当 \(A_{\rm tot}\) 足够大时，(0.3) 给相位不超过 \(1\)；当
\(A_{\rm tot}\) 足够负时，倒数权的同一结论也给相位不超过 \(1\)。
剩余的 \(|A_{\rm tot}|\leq D_*\) 是一个共同有限区间，其中
\(D_*\) 只依赖 \(a,b,S_0\)。在这个区间，应用已经完整证明的
[有限中央退化窗口定理](2026-11-14-balanced-star-finite-central-degenerate-window-uniform-phase-bound-789f-next.md)
及其显式常数，便得 (0.4)。

对于任意分组 \(q_i\)，先按重数展开全部二值源；条件为
\(\sum_iq_i(z_i-1)^2\leq S_0\)。本稿已经对完整源一致成立，再通过
真实组内置换的共同 reducing 子空间及原组平均源合同限制回去。
不会产生组数或 \(q_i\) 的额外损失。

本稿解决的是有界正权且累计平方偏差有共同界的整个平衡 star 类。
它没有证明任意 \(S_0\) 都能使用同一个常数，也没有将此模型类直接
等同于原无限尾的 moving-birth graph 接口。
