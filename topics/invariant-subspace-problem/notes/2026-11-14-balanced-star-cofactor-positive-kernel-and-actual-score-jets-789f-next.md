# 平衡 star 配分多项式的全部 cofactor 正核与真实 score jets

日期：2026-11-14；作者工作标识：789f。

## 0. 范围与结论

本稿处理平衡 star 的真实配分多项式
\[
 P_Q(z)=\sum_{I\subset[Q]}\binom Q{|I|}^{-1}z_I
       =(Q+1)\int_0^1\prod_{i=1}^Q(1-t+z_it)\,dt.                 \tag{0.1}
\]
先将每个小组拆成单个位；重复权再给任意组大小。全文的正核系数有显式有限和证明，不以一般对称稳定多仿射多项式的 Agler 猜想为前提。

新的正性结论是：每个 cofactor \(a_i=P_Q|_{z_i=0}\) 都有显式、严格正定系数 Gram 的 Agler 分解。把该分解代入同一真实配分多项式后，得到真实坐标 score \(1-2m_i\) 的正核恒等式；其一阶 jets 正是整个真实协方差 \(G\)，并由已知 score 恒等式恢复完整 \(H,L\)。

这里没有证明
\[
 J^*L^{-1}J\leq \kappa H,\qquad
 J=HG^{-1}L-2G-(2m-\mathbf1)(2m-\mathbf1)^* .                    \tag{0.2}
\]
尤其在混合正权下，核本身正，但其前面的 \(1-z_j\overline w_j\) 可变号；不能把 polydisk 收缩直接当作 (0.2)。

## 1. 真实多项式与 cofactor

对含 \(d\) 个变量的多仿射多项式，记全反射为
\[
 \widetilde a(z)=z_1\cdots z_d\,\overline{a(1/\overline z)}.
\]
对 \(d\geq1\)，定义
\[
 a_d(z)=\sum_{A\subset[d]}\binom{d+1}{|A|}^{-1}z_A,\qquad
 b_d(z)=\widetilde a_d(z)
       =\sum_{A\subset[d]}\binom{d+1}{|A|+1}^{-1}z_A.             \tag{1.1}
\]
因此 \(P_Q=a_i+z_i b_i\)，其中 \(a_i=a_{Q-1}\)、\(b_i=b_{Q-1}\)，变量是除去 \(i\) 的其余位。对 \(Q=1\)，约定 \(a_i=b_i=1\)。

\(P_Q\) 本身全反射不变。因此 \(\widetilde P_Q/P_Q=1\)，这一个平凡商不会产生所需预算。本稿使用的是每个真正非平凡的 cofactor 对 \((a_i,b_i)\)。

为核对文献中 closed-polydisk stable 的术语，对角多项式满足
\[
 a_d(\zeta,\ldots,\zeta)=\sum_{k=0}^d\frac{d+1-k}{d+1}\zeta^k,
\quad
 (1-\zeta)a_d(\zeta,\ldots,\zeta)
 =1-\frac{\zeta+\cdots+\zeta^{d+1}}{d+1}.
\]
若其在 \(|\zeta|\le1\) 为零，则 \(\zeta=1\) 时直接矛盾；其余点由三角不等式等号强迫全部 \(\zeta^k=1\)，仍矛盾。故对角多项式在闭盘无零。由下引 Knese Theorem 1.2 的 Grace–Walsh–Szegő 定理，其多仿射对称化 \(a_d\) 在闭多圆盘无零。这只用于术语，后面的全部正核系数由直接恒等式另证。

## 2. 显式严格正定的系数 Gram

固定 \(d\geq1\)。对 \(0\leq j\leq d\)，写
\[
 c_j=\binom d j^{-1},\qquad
 \gamma_d=\frac{d+2}{(d+1)^2};
\]
\((x)_\ell=x(x-1)\cdots(x-\ell+1)\)，\((x)_0=1\)。

对 \(A,B\subset[d-1]\)，令 \(j=|A|,\ k=|B|,\ i=|A\cap B|\)，定义
\[
 B^{(d)}_{A,B}
   =c_jc_k\sum_{\ell=0}^{i}
       \frac{(i)_\ell(d+1)_\ell}{(j)_\ell(k)_\ell}.              \tag{2.1}
\]
只有 \(\ell\leq i\leq \min(j,k)\) 的项出现，故分母均合法。该矩阵不是仅由低阶数值推测为正，而有完整 inclusion Gram：
\[
 B^{(d)}_{A,B}
  =\sum_{S\subset A\cap B}|S|!(d+1)_{|S|}
       \frac{c_{|A|}}{(|A|)_{|S|}}
       \frac{c_{|B|}}{(|B|)_{|S|}}.                            \tag{2.2}
\]
这是将 \((i)_\ell=\ell!\binom i\ell\) 按 \(S\) 展开。所有系数正；按包含偏序排列 \(S,A\) 后，特征矩阵为三角阵且对角非零。因此
\[
                         B^{(d)}>0.                          \tag{2.3}
\]

定义多项式特征
\[
 F^{(d)}_S(z)=
 \sum_{\substack{A\subset[d-1]\\A\supset S}}
       \frac{c_{|A|}}{(|A|)_{|S|}}z_A
       \quad (S\subset[d-1])
\]
以及正核
\[
 K_d(z,w)=\gamma_d\sum_{S\subset[d-1]}
       |S|!(d+1)_{|S|}
       F^{(d)}_S(z)\overline{F^{(d)}_S(w)}.                    \tag{2.4}
\]
故 \(K_d\) 在整个复空间上是正核；不需要对 \(z,w\) 限制在单位圆盘中。

## 3. 全系数恒等式，包括满并集的边界

主恒等式为
\[
 a_d(z)\overline{a_d(w)}
       -b_d(z)\overline{b_d(w)}
   =\sum_{r=1}^d(1-z_r\overline w_r)
        K_d(\widehat z_r,\widehat w_r).                       \tag{3.1}
\]
\(\widehat z_r\) 表示删去第 \(r\) 坐标；核在变量置换下不变，删除后任意一致顺序均可。

以下逐个核对全部 \(z_A\overline w_B\) 系数，特别不省略 \(|A\cup B|=d\)。

由
\[
 \binom{d+1}{j}^{-1}=c_j\frac{d+1-j}{d+1},\qquad
 \binom{d+1}{j+1}^{-1}=c_j\frac{j+1}{d+1},
\]
左侧相应系数为
\[
                  \gamma_d c_jc_k(d-j-k).                   \tag{3.2}
\]
右侧正项有 \(d-j-k+i\) 个删除位置，负项有 \(i\) 个，所以只须证明
\[
 c_jc_k(d-j-k)
  =(d-j-k+i)B^i_{j,k}-iB^{i-1}_{j-1,k-1}.                    \tag{3.3}
\]
这里 \(B^i_{j,k}\) 是 (2.1) 中只依赖三项基数的值；若首系数为零，则首项不使用实际的 \([d-1]\) 子集，也可用同一有限和作代数延拓。若 \(i=0\)，负项为零，结论立即成立。

令 \(t=d-j-k\)，并令
\[
 T_\ell=\frac{(i)_\ell(d+1)_\ell}{(j)_\ell(k)_\ell}.
\]
将 (3.3) 除以 \(c_jc_k\)，负项重编号后变为
\[
 (t+i)\sum_{\ell=0}^iT_\ell
 -(d-j+1)(d-k+1)\sum_{\ell=1}^i
                         \frac{T_\ell}{d+2-\ell}.             \tag{3.4}
\]
对 \(1\leq\ell\leq i\)，有精确望远镜身份
\[
 T_\ell\left(t+i-
       \frac{(d-j+1)(d-k+1)}{d+2-\ell}\right)
   =(i-\ell)T_\ell-(i-\ell+1)T_{\ell-1}.                      \tag{3.5}
\]
其验证只用
\[
 (t+\ell)(d+2-\ell)
   =(d-j+1)(d-k+1)-(j-\ell+1)(k-\ell+1).
\]
(3.5) 求和给 \(-i\)，再加 \(\ell=0\) 的 \(t+i\)，得到 \(t\)。这证明 (3.3)，包括 \(|A\cup B|=d\) 时首项系数恰为零的全部边界。因此 (3.1) 已对所有系数证明。

例如 \(d=1\) 时 \(K_1=3/4\)，恒等式就是
\[
 (1+z/2)(1+\overline w/2)
   -(1/2+z)(1/2+\overline w)
       =\tfrac34(1-z\overline w).
\]

## 4. 核特征有同源删位积分表示

若 \(|S|=\ell\)，则
\[
 F^{(d)}_S(z)
 =z_S\,\frac{(d-\ell+1)!}{d!}
      \int_0^1(1-t)
          \prod_{r\in[d-1]\setminus S}(1-t+z_rt)\,dt.          \tag{4.1}
\]
证明是对每个 \(A\supset S\) 使用 beta 积分：
\[
 \int_0^1t^{|A|-\ell}(1-t)^{d-|A|}\,dt
       =\frac{(|A|-\ell)!(d-|A|)!}{(d-\ell+1)!},
\]
并注意
\[
 \frac{c_{|A|}}{(|A|)_\ell}
       =\frac{(|A|-\ell)!(d-|A|)!}{d!}.
\]
所以该正核的特征仍由原乘积权删位后的积分给出；没有引入自由选择的抽象正块。

## 5. 真实坐标 score 的正核身份

令
\[
 m_i(z)=z_i\,\partial_i\log P_Q(z),\qquad
 f_i(z)=1-2m_i(z)=\frac{a_i(z)-z_i b_i(z)}
                            {a_i(z)+z_i b_i(z)}.              \tag{5.1}
\]
在 \(P_Q(z)P_Q(w)\neq0\) 处，(3.1) 给出
\[
 \begin{split}
 P_Q(z)\overline{P_Q(w)}
       [f_i(z)+\overline{f_i(w)}]
  ={}&2(1-z_i\overline w_i)b_i(z)\overline{b_i(w)}\\
    &+2\sum_{j\ne i}(1-z_j\overline w_j)
            K_{Q-1}(\widehat z_{i,j},\widehat w_{i,j}).        \tag{5.2}
 \end{split}
\]
当 \(Q=1\) 时和项为空；其余式按 \(a_i=b_i=1\) 理解。

证明只需将左侧展开为
\[
 2[a_i(z)\overline{a_i(w)}
       -z_i\overline w_i b_i(z)\overline{b_i(w)}]
\]
再加减 \(2b_i(z)\overline{b_i(w)}\)，然后用 (3.1)。

将每个核除以 \(P_Q(z)\overline{P_Q(w)}\) 仍得正核。在全部正实权处 \(P_Q>0\)，所以 (5.2) 及其任意有限阶 jets 都合法，包括同时存在 \(z_i<1\) 与 \(z_j>1\) 的情形。

但若在对角正实权上取值，则因子 \(1-z_j^2\) 具有不同符号。故这里得到的是完整同源正核身份，不是已经把右侧求和化成正矩阵的相位界。

## 6. 它确实连接完整物理 \(G,H,L\)

令随机子集 \(I\subset[Q]\) 的分布为
\[
 \mathbb P_z(I)=\frac{z_I}{P_Q(z)\binom Q{|I|}},
\]
\(X_i=\mathbf1_{\{i\in I\}}\)，则 \(m_i=\mathbb E X_i\)，且
\[
 G_{ij}=\operatorname{Cov}(X_i,X_j)
       =\partial_{\log z_j}m_i
       =-\tfrac12\partial_{\log z_j}f_i.                      \tag{6.1}
\]
注意普通 \(z\) 导数的对角项：
\[
 G_{ij}=z_i z_j\,\partial_i\partial_j\log P_Q
                          +\delta_{ij}m_i.                  \tag{6.2}
\]
因此 (5.2) 的全部坐标一阶 jets 给出的是整个真实 \(G\)，不是仅总数的一个标量方差。

写 \(n=\mathbf1-m\)、\(Z=\operatorname{diag}(z_i)\)。由真实 beta–Bernoulli score 恒等式，
\[
 \begin{split}
 H&=\operatorname{diag}(Zn)-ZG+(Zn)m^*,\\
 L&=\operatorname{diag}(Z^{-1}m)-GZ^{-1}+n(Z^{-1}m)^*.
 \end{split}                                                \tag{6.3}
\]
特别 \(H_{ii}=z_i n_i,\ L_{ii}=m_i/z_i\)。所以 (5.2) 的同一 jets 系统与 (6.3) 一起确切恢复 (0.2) 中的三个完整矩阵。

一般小组大小 \(q_g\) 由重复 \(q_g\) 个相等小位得到。若组变量仍记 \(z_g\)，则
\[
 m_g=\frac1{q_g}\partial_{\log z_g}\log P,\qquad
 G_{gh}=\frac1{q_gq_h}
        \partial_{\log z_g}\partial_{\log z_h}\log P.
\]
这正是 \(X_g=K_g/q_g\) 的均值与协方差；(6.3) 的对角噪声相应改为
\(\operatorname{diag}(z_gn_g/q_g)\) 与
\(\operatorname{diag}(m_g/(q_gz_g))\)。
故重复权没有丢掉实际组源度量。这里没有通过先压缩再取逆去替换真正的完整 \(G^{-1}\)。

为使上述 score 接口在本稿中可直接核对，可采用条件模型：
\(T\) 的密度正比于 \(\prod_i(1-t+z_it)\)，给定 \(T=t\) 后各 \(X_i\) 独立，
\(\mathbb P(X_i=1\mid t)=z_it/(1-t+z_it)\)。
对 \(i\ne j\)，直接按 \(X_i=1\) 的条件概率计算即得
\[
 H_{ij}=z_i\,\mathbb E[(1-X_i)X_j]
        =z_i(n_i m_j-G_{ij}).
\]
对角 \(X_i^2=X_i\) 给 \(H_{ii}=z_i n_i\)；倒数互补给 \(L\) 的式子。
组内二项方差则给前述 \(1/q_g\) 的噪声。这独立证明 (6.3)。

## 7. 与文献的关系及下一条真正缺失的预算

Knese 的 *Stable symmetric polynomials and the Schur–Agler class* 给出一般对称多仿射系数矩阵准则及其基数递推；本稿的 (3.3) 是该型递推在本课题真实 cofactor 上的显式解。一般命题“对称稳定多仿射多项式均为 Agler denominator”在其论文及 2024 年综述中作为未解决问题列出，不能用作本稿前提。

可核的一手来源：

- Greg Knese, *Stable symmetric polynomials and the Schur–Agler class*, arXiv:1008.4560，特别 Theorem 3.3 和 coefficient recurrence；官方全文：<https://arxiv.org/html/1008.4560v1>。
- Greg Knese, *Rational inner functions on the polydisk — a survey*, arXiv:2409.14604，Section 6 的 SOS 结构与 Problem 3；官方全文：<https://arxiv.org/html/2409.14604v1>。

本稿独立给出系数公式、严格正定 Gram、包括满并集的全部系数证明，以及真实 score/全协方差接口；这些不依赖该一般开放命题。

目前仍缺：从 (5.2) 的同一正核 jets，经合法的完整源 Schur 消去，控制
\[
 HG^{-1}L-2G-(2m-\mathbf1)(2m-\mathbf1)^*
\]
的两端 \(H,L\) 度量。单独的 cofactor Schur–Agler 性、单独的一阶协方差正性或将混合正权全部当作单位圆盘内点，都不支付该缺口。本稿不把正核本身登记为一般相位常数或 ISP 完成。

