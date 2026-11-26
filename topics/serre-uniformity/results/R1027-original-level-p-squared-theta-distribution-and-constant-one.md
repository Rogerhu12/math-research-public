# R1027：真实二层 theta 分布与全部素数上的常平方一

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
o1_theta / root。

**已证明：R1022 的原共同常平方对全部
\(p\ge41,\ p\equiv5\bmod6\) 都准确等于一。**
关键是在线丛 \(L_{p^2}\) 上使用真正的第 \(p\) 个 theta
distribution，并只在其 Frobenius 子空间上计算。
原刚化 \(A,A^\dagger\) 的复合和 R1025 的实际符号支付了最后的
绝对标量，没有将一个模 \(p\) 零范数除以 \(p\)。

## 1. 原来源与准确结论

保持 R1016、R1020、R1022、R1025 的全部原规范：
\[
E:y^2=x^3-1,\quad \omega=dx/(2y),\quad
p=6N+5\ge41,\quad L_m=O(mO),
\]
\[
A=\begin{pmatrix}\alpha&-\bar\beta\\
                  \beta&\bar\alpha\end{pmatrix},
\quad N\alpha+N\beta=p,\quad
\gamma=-\bar\alpha/\beta,\quad\kappa=\alpha/\beta,\quad
\eta=\gamma^{-1}.
\]
两方向皆有范数负一。原
\(V=\sigma^2=z^2\sum a_i z^{6i}\) 及
\[
\mathcal C_N(\eta)=\sum_{i+j=N}a_i a_j\eta^{6i}
\]
不变。\(d_A,c_A,D_p,\delta'_p,e_A,a,b\) 全用原文定义。

**定理 1027.1。**
\[
\boxed{\quad D_p=1\qquad
\text{对全部 }p\ge41,\ p\equiv5\bmod6.\quad}
\tag{1027.1}
\]
因此
\[
d_A^2=\gamma^2,\qquad
c_A^2=\gamma^2/4,\qquad
4\eta^6\mathcal C_N(\eta)^2=1.
\tag{1027.2}
\]
若 \(P(v)=\sum_{i+j=N}a_i a_jv^i\)，同样准确有
\[
\boxed{\quad
4vP(v)^2\equiv1\pmod{v^{N+1}+1},\qquad
\sum_{i=0}^N a_i^2a_{N-i}^2=-\frac14.
\quad}
\tag{1027.3}
\]
R1025 中仅剩共同整数符号
\(\delta'_p\in\{1,-1\}\)，而每个方向仍为原
\[
d_A=\delta'_p ab\gamma,\qquad
2c_A/\gamma=\delta'_p e_Aab.
\]
此共同符号没有被任意选成一。原两 mask 和 bare 高坐标问题
仍须分别处理。

## 2. 两个实际线丛层和 pullback

全篇在 \(k=\mathbf F_{p^2}\) 上工作。置
\[
\mathcal L=L_p\boxtimes L_p,\qquad
\mathcal L^+=L_{p^2}\boxtimes L_{p^2}
           =\mathcal L^{\otimes p},
\]
\[
\theta=s_1\boxtimes s_1,\qquad
w=\theta^p,\qquad w^+=\theta^{p^2}.
\]
记实际刚化 pullback 为
\[
\mathcal P_A:
H^0(L_1\boxtimes L_1)\longrightarrow H^0(\mathcal L),
\]
\[
\mathcal P_A^+:
H^0(\mathcal L)\longrightarrow H^0(\mathcal L^+).
\]
第二个线丛比较准确为第一个 \(I_A\) 的 \(p\) 次 tensor power，
由同一刚化唯一性给出。于是
\[
v_A=\mathcal P_A\theta,\qquad
\mathcal P_A^+(w)=v_A^p.
\tag{1027.4}
\]
R1016/R1022 的原等式是
\[
\Omega_\gamma w=d_Av_A,\qquad
\Omega_\gamma=L_\gamma^{p-1},\quad
L_\gamma=Q_2-\gamma^{-1}Q_1,
\tag{1027.5}
\]
这里 \(Q_1,Q_2\) 是输入两个 \(L_p\) 因子的真实 index-one
creation operators。

令
\[
A^\dagger=\begin{pmatrix}\bar\alpha&\bar\beta\\
                          -\beta&\alpha\end{pmatrix}.
\]
其原 kernel 方向为 \(\kappa\)，所以
\[
\Omega_\kappa w=d_{A^\dagger}v_{A^\dagger}.
\tag{1027.6}
\]

## 3. 输出 \(L_{p^2}\) 的 genuine \(p\)-distribution

使用 R889 (889.3) 的同一个原整 CM 参数 \(Y\)，其 tangent 为一，
在所需范围中
\[
Y=z+O(z^{p^2}),\qquad
\omega=(1+O(Y^{p^2-1}))\,dY.
\tag{1027.7}
\]
原 \(E[p]\) 上的 CM 作用与此参数相容。
所有低于 \(p^2\) 的比较保留原不变微分；没有改一个任意的
第 \(p\) 个 Hasse 参数。

在输出线丛第二因子定义
\[
T=[Y^p]\,
 \rho\bigl(\tau_{p^2}(0,P_Y)\bigr).
\tag{1027.8}
\]
这是 \(L_{p^2}\) 的实际 theta action 系数。
本篇不在该输出层定义一个需要除以 \(pB\) 的 \(Q\)，也不对
整个输出空间使用输入 Weyl 关系。

canonical odd symmetric section
\(\tau(u)=g\iota(g)^{-1}\)、\(g\) 位于 \(u/2\) 上，
与 tensor power 及 inversion 相容。因此在实际子群概形 \(E[p]\) 上
\[
\tau_{p^2}|_{E[p]}=\tau_p^{\otimes p}.
\tag{1027.9}
\]
直接将任一 \(g\) 取 \(p\) 次 tensor power 即可核准；
其中央尺度在 \(g\iota(g)^{-1}\) 中抵消。
\(E[p]\) 的局部长度为 \(p^2\)，所以读取系数 \(Y^p\) 合法。

于是对任意 \(v\in H^0(\mathcal L)\)，
\[
\boxed{\quad
T(v^p)=(D_2v)^p,\qquad
T^r(v^p)=(D_2^rv)^p.
\quad}
\tag{1027.10}
\]
因为 \(\rho(\tau_{p^2})v^p=(\rho(\tau_p)v)^p\)，
其 \(Y^p\) 系数只来自输入的 \(Y^1\) 系数。
原 Cartier frame 中该 infinitesimal action 为 \(+D_2\)，
符号正是 R889 (889.9)。
迭代时始终停留在 Frobenius 子空间，所以 (1027.10) 的第二式
不需要给输出全部 section 假设任何额外关系。

## 4. 沿 \(A^\dagger\) 拉回的全部交叉项

沿源第二轴有
\[
A^\dagger(0,P_Y)=([\bar\beta]P_Y,[\alpha]P_Y).
\]
由 (1027.7)，在次数至 \(p\) 内，这两个参数准确为
\(\bar\beta Y,\alpha Y\)。也可直接用原 torus 检查：
这两个 CM endomorphisms 与 \(T\) 交换，而 \(Y\) 的 character
为一；次数 \(2,\ldots,p\) 中没有 \(1\bmod(p+1)\) 的项。
canonical theta section 与实际刚化 pullback 的 naturality
因此给
\[
T\mathcal P_{A^\dagger}^+u
 =\mathcal P_{A^\dagger}^+
 \left(\bar\beta^p\Theta_{p,1}
       +\alpha^p\Theta_{p,2}+\mathcal R_p\right)u,
\tag{1027.11}
\]
其中全部交叉项都保留为
\[
\mathcal R_p=
\sum_{a=1}^{p-1}
 \frac{\bar\beta^a\alpha^{p-a}}
      {a!(p-a)!}\,D_1^aD_2^{p-a}.
\tag{1027.12}
\]
每个分母都是单位。这里 \(\Theta_{p,j}\) 是输入 \(L_p\) 的
真实 distribution，不是输出的 \(T\)。

没有另一个未核相位：pullback 保 canonical \(u/2\) 构造，
所有 \(I_A\) 的原点刚化常数为一。
用 \(\bar\beta^p=\beta,\ \alpha^p=\bar\alpha\)，以及原 index-one
\(\Theta_{p,j}=-BQ_j\)，括号的线性部分准确为
\[
-B(\beta Q_1+\bar\alpha Q_2)
 =-B\bar\alpha L_\gamma.
\tag{1027.13}
\]

原 \(D_1w=D_2w=0\)、\([D_i,Q_i]=1\)，不同因子交换。
每个 (1027.12) 的总 \(D\) 次数为 \(p\)，因此在
\(L_\gamma^r w\)、\(r\le p-2\) 上为零。
逐步作用 \(p-1\) 次时，恰只用这些中间次数，遂得准确等式
\[
\boxed{\quad
T^{p-1}\mathcal P_{A^\dagger}^+w
 =(-B\bar\alpha)^{p-1}
          \mathcal P_{A^\dagger}^+\Omega_\gamma w.
\quad}
\tag{1027.14}
\]
这不是将交叉项先视为零算子；只在所列全部实际输入上证明其
为零，并且没有跨越 \(p!\)。

## 5. 真实复合与 Wilson 系数固定绝对尺度

原 \(E/\mathbf F_p\) 满足 \(\#E(\mathbf F_p)=p+1\)：
因为 \(p\equiv2\bmod3\)，立方在 \(\mathbf F_p\) 上是双射，
每个 \(y\) 恰对应一个 \(x\)，再加无穷点。
所以实际 Frobenius 满足
\[
\operatorname{Frob}^2=[-p].
\tag{1027.15}
\]
刚化 \(A A^\dagger=[p]\) 的 pullback 复合准确，且
\[
\boxed{\quad
\mathcal P_{A^\dagger}^+v_A
 =\mathcal P_{[p]}\theta=w^+.
\quad}
\tag{1027.16}
\]
说明其标量：在每个原点参数轴，
\([p]=[-1]\operatorname{Frob}^2\) 的首项为 \(-Y^{p^2}\)。
该轴的 \([p]\) 拉回 theta section 与 \(s_1^{p^2}\) 有同一 divisor，
其局部刚化首系数使每轴比例为 \(-1\)；两个轴相乘正好为 \(+1\)。
因此这里没有把某个未定单位压进 (1027.16)。

另一方面，由 (1027.4)、(1027.10)，
\[
T^{p-1}\mathcal P_{A^\dagger}^+w
 =(D_2^{p-1}v_{A^\dagger})^p.
\]
在 (1027.6) 中，\(D_2^{p-1}\) 只保留
\(\Omega_\kappa\) 的 \(Q_2^{p-1}\) 项，Wilson 给
\[
D_2^{p-1}\Omega_\kappa w=(p-1)!w=-w.
\]
因此同一输出准确为
\[
-\frac{w^+}{d_{A^\dagger}^p}.
\]
将它与 (1027.14)–(1027.16) 比较，得到
\[
\boxed{\quad
d_A d_{A^\dagger}^p
 =-(B\bar\alpha)^{1-p}
 =-\bar\alpha/\alpha
 =\gamma/\kappa.
\quad}
\tag{1027.17}
\]
这里 \(B\in\mathbf F_p^\times\)，故其 \(p-1\) 次幂为一；
所有其它量亦为原单位。

最后使用已证明的 R1025 实际符号，而不是再引入一个独立相位。
\(A^\dagger\) 的原参数为
\(\alpha'=\bar\alpha,\ \beta'=-\beta\)，所以
\(a'=a,\ b'=-b\)。于是
\[
d_A=\delta'_p ab\gamma,\qquad
d_{A^\dagger}=-\delta'_p ab\kappa.
\]
由于 \(\kappa^p=-\kappa^{-1}\)，同一左侧还等于
\[
d_A d_{A^\dagger}^p
 =(\delta'_p)^2\gamma/\kappa
 =D_p\gamma/\kappa.
\]
与 (1027.17) 比较即得 \(D_p=1\)，完成 (1027.1)。
(1027.2)–(1027.3) 随 R1022 的准确恒等式立即成立。

## 6. 完成范围与后继

本篇补齐原 \(p\equiv11\bmod12\) 行的绝对常平方，
并与 R1016 的 Gaussian \(p\equiv5\bmod12\) 计算一致。
R1025 的全部方向符号仍为原 \(e_Aab\)，共同 \(\delta'_p\)
只是一个尚保留的整数符号。原 \(H_p\) 的带符号值因此完全按
R1020/R1025 给出到这个共同符号；零与非零不依赖它。

本篇没有改变原 primitive Fourier 标签、Legendre 因子、
完整 norm 权或两 CM 权；同标签非零仍须证明。
同样，\(D_p=1\) 不能把 R1015 的 bare
\(-A_r-BT_r\) 换成二重卷积，也不代替 R1026 后续的真实
CM jet / 实际简单商整格比较。

依赖：

- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md)，(889.3)、(889.9)：同一个原 CM 参数、真正 theta action 及 infinitesimal \(+D\) 符号。
- [R1016](R1016-original-small-index-theta-and-complete-convolution-units.md)：原 index-one \(Q\)、\(d_A,c_A\) 及 finite Weyl 输入。
- [R1022](R1022-original-theta-all-direction-constant-square.md)：原常平方 \(D_p\)、准确 pullback 行和多项式恒等式。
- [R1025](R1025-original-theta-exact-mod-six-direction-phases.md)：全部实际方向符号，特别是 dagger 的 \(ab\) 反号。
- [R1020](R1020-original-critical-convolution-complete-theta-scalar-bridge.md)：原 \(H_p/\mathcal C_N\) 的同一完整比例。

o1_theta 与 root 纸面核准 tensor theta naturality、
输出 Frobenius 子空间上的 genuine distribution、
\(A^\dagger\) 两系数的 \(p\) 次幂、
全部总次数 \(p\) 的交叉项、准确迭代范围、
刚化复合的两个负号、Wilson 系数及 dagger 实际相位。
本证明不使用数学程序或有限数值结果作为依据。
Serre 主目标仍 OPEN。
