# R1022：原小 index 标量的全方向常平方与 split 行的完整值

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：存在仅依赖 \(p\) 的非零平方
\(D_p\in(\mathbf F_p^\times)^2\)，使全部原范数负一方向满足
\(4\eta^6\mathcal C_N(\eta)^2=D_p\)。
对整个 \(p\equiv5\bmod12\) 行，准确有 \(D_p=1\)。**
证明使用原积分 torus lift、真实 principal theta pullback 的相对
Hermitian 范数和完整 addition 分布比较；没有将模 \(p\) 为零的
apolar 范数擅自除以 \(p\)。原 primitive/Legendre 同标签仍开放。

## 1. 原来源、常数与结论

保持 R1016、R1020：
\[
p=6N+5\ge41,\quad
E:y^2=x^3-1,\quad dz=dx/(2y),\quad
L_m=O(mO),
\]
\[
V=\sigma^2=z^2\sum_i a_i z^{6i},\qquad
\mathsf X=x\sigma^2,\qquad
\mathcal C_N(\eta)=\sum_{i+j=N}a_i a_j\eta^{6i}.
\]
sigma、\(B\)、实际 \(Q_m,\Omega_{\gamma,m}\)、原点 rigidification
与所选 \(p\) 处约化全不变。

对
\[
A=\begin{pmatrix}\alpha&-\overline\beta\\
\beta&\overline\alpha\end{pmatrix},\quad
N\alpha+N\beta=p,\quad
\gamma=-\overline\alpha/\beta,\quad \eta=\gamma^{-1},
\tag{1022.1}
\]
仍用实际标量
\[
\mathcal K_{A,1}(s_p\boxtimes s_p)
 =d_A(s_1\boxtimes s_1),\qquad
\mathcal K_{A,2}(V^p\boxtimes V^p)
 =c_A(\mathsf X\boxtimes\mathsf X).
\]
R1016 已证明二者非零，并有
\[
c_A=-\gamma^{-2}\mathcal C_N(\eta).
\tag{1022.2}
\]

**定理 1022.1。** 存在方向无关的
\(D_p\in(\mathbf F_p^\times)^2\)，使全部原表示满足
\[
\boxed{\qquad
d_A^2=D_p\gamma^2,\qquad
c_A^2=\frac{D_p}{4}\gamma^2,\qquad
4\eta^6\mathcal C_N(\eta)^2=D_p.
\qquad}
\tag{1022.3}
\]
定义 \(P(v)=\sum_{i+j=N}a_i a_jv^i\)，则同样有准确的有限多项式式
\[
\boxed{\quad
4vP(v)^2\equiv D_p\pmod{v^{N+1}+1},\qquad
D_p=-4\sum_{i=0}^N a_i^2a_{N-i}^2.
\quad}
\tag{1022.4}
\]
此外
\[
\boxed{\quad p\equiv5\pmod{12}\ \Longrightarrow\ D_p=1.\quad}
\tag{1022.5}
\]
对 \(p\equiv11\bmod12\) 本篇保留 (1022.4) 的实际共同单位，
不预称它等于一。

## 2. Index-one 的真实积分 torus lift 及其代数域

令 \(R=W(\mathbf F_{p^2})\)，
\(T=\ker(N:\mathbf F_{p^2}^\times\to\mathbf F_p^\times)\)，
\(n=p+1\)。在原 \(\mathcal H_1=H^0(E_R,L_p)\) 上复用
R881 §§1–2 的实际构造，只有 tame multiplicity 从六变成一：

原 CM 环作用使每个 \(t\in T\) 真正作用于有限平坦群概形
\(E[p]\)，并保持 Weil 配对。canonical 对称 section
\(\tau(u)=g\iota(g)^{-1}\)（\(g\) 位于 \(u/2\) 上）
给实际 theta-group automorphism。
相对 theta 等价使其 intertwiner 为可基变换的自由秩一 \(R\)-模。
将生成元的 \(n\) 次幂用 Hensel 单位根归一，得到唯一的积分作用
\[
M_tM_u=M_{tu},\qquad M_t^n=1.
\]
它在特殊纤维的 \(\ker D=k s_p\) 上为一，并在
\(Q_1^r\ker D\) 上为 \(t^{-r}\)，\(0\le r<p\)。
因此实际 characters 恰各出现一次，惟独缺少 tangent character
\(\widetilde\chi\)。特别
\[
\operatorname{tr}M_t=-\widetilde\chi(t)\quad(t\ne1).
\tag{1022.6}
\]
这里使用真实积分格和原 vacuum；不另选一个抽象 Weil 格。

接下来必须固定复共轭与原 \(p\) 处 Frobenius 的关系。
令 \(K_0=\mathbf Q(\zeta_3)\)。同一个 elliptic model、\(L_p\)
及上述 theta-group automorphism 都定义在 \(K_0\) 上：
\(t\) 是 \(\mathcal O/p\mathcal O\) 的元素，其作用来自原 CM
endomorphism，而非将 Teichmüller 根当成 \(E\) 的全局 automorphism。
有限 theta 的 absolute Schur 引理给一个一维的
\(K_0\)-intertwiner line。取其任一非零矩阵
\(L_t\in\mathrm{GL}_p(K_0)\)，使用原代数 section 基。

在原 \(p\) 嵌入下 \(L_t\) 与 \(M_t\) 成比例；由 (1022.6)
其 trace 非零。因此
\[
M_t=-\frac{\widetilde\chi(t)}{\operatorname{tr}L_t}\,L_t
\quad(t\ne1),\qquad M_1=I.
\tag{1022.7}
\]
故所有矩阵条目都在
\[
L=K_0(\mu_n)=\mathbf Q(\mu_n)
\]
中，因为 \(6\mid n\)。
这一步避免给一个任意 \(p\)-adic Hensel 根指定未核的复共轭。

\(p\nmid n\) 且 \(p\equiv-1\bmod n\)；
故在所选 \(p\) 素点，\(L\) 的 arithmetic Frobenius
就是复共轭 \(c\)，局部域为未分歧二次域，约化满足
\[
\overline{c(\lambda)}=\overline\lambda^{\,p}
\]
对所有该处整的 \(\lambda\in L\) 成立。

## 3. 同核线的真实运输及严格相对范数

令 \(\vartheta=s_1\boxtimes s_1\)，并记
\[
v_A=I_{A,1}A^*\vartheta
 \in H^0(E^2,L_p\boxtimes L_p).
\]
原实际下降式等价于
\[
\Omega_{\gamma,1}(s_p\boxtimes s_p)=d_Av_A
\tag{1022.8}
\]
在特殊纤维成立；\(v_A\) 本身来自同一特征零刚化模型。

固定一个原 \(A_0\) 及其核方向 \(\gamma_0\)。
任一其它方向为 \(\gamma=t\gamma_0,\ t\in T\)；
R1012 给实际 norm-\(p\) 矩阵 \(A\)。

在泛纤维，\(\ker A=\operatorname{graph}(\gamma)\subset E[p]^2\)
是 maximal isotropic。其 canonical 对称 splitting
也是原 \(A\) 下降的 splitting：两个对称 splitting 的差为
odd-\(p\) 群的 character，而 inversion 迫该 character 的平方为一，
故差只能平凡。
所以 \(v_A\) 张成这一真实 invariant line。
\(M_t\boxtimes1\) 精确运输两个 canonical splittings，遂有
\[
(M_t\boxtimes1)v_{A_0}=\lambda_t v_A,\qquad \lambda_t\in L^\times.
\tag{1022.9}
\]

\(\lambda_t\) 是原 \(p\) 处的单位：
\(M_t\) 积分且可逆；两 \(v_A\) 均 primitive，因为特殊纤维
\(A\) 仍有限满射，非零 \(\vartheta\) 的 pullback 不为零，
而 \(I_{A,1}\) 是整同构。
这不是由复绝对值推断 \(p\)-整性。

现在在 \(E(\mathbf C)\) 上给刚化 \(L_1\) 取曲率平移不变、
原点 frame 范数一的 Hermitian metric。
原 \(j=0\) quasiperiod 关系亦给显式构造：
在 \(\mathbf C/\Lambda\) 上，以对应正实常数 \(c_\Lambda\)
给 sigma 表示乘 Gaussian
\(\exp(-c_\Lambda|z|^2)\)，其 period multiplier 的绝对值恰抵消；
原点的 \(\sigma/z\) frame 固定尺度。
\(L_p\) 用其 \(p\) 次张量 metric，section 范数用 normalized Haar
积分定义。

每个 canonical odd-\(p\) theta lift \(\tau(u)\) 覆盖平移、
满足 \(\tau(u)^p=1\)，故是此 metric 的 isometry：
两个同曲率 metric 只差正常数，有限阶迫该常数为一。
p-Heisenberg 在 \(H^0(L_p)(\mathbf C)\) 上不可约；
\(M_t\) 正规化它，因而 \(M_t^\dagger M_t\) 是正常数。
\(M_t^n=1\) 再迫该常数为一。因此 \(M_t\) 是 unitary。

另一方面，\(A^\dagger A=pI\) 使 \(A^*\) 的曲率与
\(L_p\boxtimes L_p\) 的曲率相同。
实际 \(I_{A,1}\) 在原点纤维为一，故它严格保持这些 metrics。
isogeny 保 normalized Haar 积分，所以
\[
\|v_A\|^2=\|\vartheta\|^2
\]
对所有 \(A\) 相同。由 (1022.9)，准确得到
\[
\boxed{\qquad \lambda_t c(\lambda_t)=1.\qquad}
\tag{1022.10}
\]
这是 \(L\) 中的代数等式。
它没有约化一个为零的范数，也没有进行任何未付出的除 \(p\)。

在特殊纤维，原 \(Q_1^r\) 权为 \(t^{-r}\)，vacuum 权为一，故
\[
(M_t\boxtimes1)\Omega_{\gamma_0,1}(s_p\boxtimes s_p)
 =\Omega_{t\gamma_0,1}(s_p\boxtimes s_p).
\]
结合 (1022.8)–(1022.9)，
\[
d_A=\overline\lambda_t d_{A_0}.
\]
约化 (1022.10) 合法，遂得
\[
\boxed{\quad N_{\mathbf F_{p^2}/\mathbf F_p}(d_A)
       =N_{\mathbf F_{p^2}/\mathbf F_p}(d_{A_0}).\quad}
\tag{1022.11}
\]

## 4. 回文式将相对 norm 变成 principal 常平方

记原
\[
\sigma=z\sum b_i z^{6i},\qquad
\mathcal S_N(\eta)=\sum_{i+j=N}b_i b_j\eta^{6i}.
\]
R1016 的实际 \(J_{1,1}\) 比较为
\[
d_A=-\frac{B^2\gamma^{-2}\mathcal S_N(\eta)}{2N\alpha}.
\tag{1022.12}
\]
所有有限系数在 \(\mathbf F_p\) 中。
由 \(\eta^p=-\eta^{-1}\)、回文对称和 \(6N=p-5\)，
\[
\mathcal S_N(\eta)^p
 =\eta^{-6N}\mathcal S_N(\eta)
 =-\eta^6\mathcal S_N(\eta).
\]
\(\gamma^p=-\gamma^{-1}\)，且 (1022.12) 的其余因子在
\(\mathbf F_p^\times\)，所以
\[
d_A^p=-\gamma^{-2}d_A,\qquad
(d_A/\gamma)^p=d_A/\gamma.
\tag{1022.13}
\]
由 (1022.11)，
\[
D_p:=-N(d_A)=d_A^2/\gamma^2
\]
与方向无关；由 (1022.13) 它是 \(\mathbf F_p^\times\) 中的平方。
这证明 (1022.3) 第一式。

同一核的十二表示只把 \(d_A\) 变号：
左乘 \(\operatorname{diag}(u,\overline u)\) 对
\(\sigma\boxtimes\sigma\) 的角色为一，左乘
\(\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) 的角色为负一。
所以定义也不依赖代表的选择。

## 5. 真正 addition pullback 的完整分布比较

本节将 principal 结论接回同一个 \(c_A\)。
它不是将 \(\Omega\) 当成保持乘法的算子。

先在 R1012 的同核十二表示内，左乘一个实际 \(\mu_6\) 单位，
使 \(A\bmod2\) 为 \(I\) 或
\(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\)。
这只用模二的唯一非零 CM 乘子；不改变 \(\gamma\) 或 (1022.2)。
令
\[
H=\begin{pmatrix}1&-1\\1&1\end{pmatrix},
\qquad A'=HAH^{-1}.
\tag{1022.14}
\]
上述模二条件使 \(A'\) 的所有条目在 \(\mathcal O\) 中。
它仍有 (1022.1) 的 quaternion 形状，且
\(A'^\dagger A'=pI\)。其核方向为
\[
\gamma'=\frac{\gamma-1}{\gamma+1}.
\tag{1022.15}
\]
\(\gamma\ne\pm1\)，并且 \(N\gamma'=-1\)，所以所有式子有定义。

令
\[
j_H:H^*(L_1\boxtimes L_1)\simeq L_2\boxtimes L_2
\]
使用同一原点 rigidification。
原 sigma addition formula 准确给
\[
j_H\vartheta
 =V\boxtimes\mathsf X-\mathsf X\boxtimes V=:\mathcal A.
\tag{1022.16}
\]
其 \(p\) 次张量比较记为 \(j_H^{(p)}\)。

实际 theta translation 的 \(p\) 阶系数满足乘积公式；
其 cross 项均为
\[
\frac{D_1^aD_2^{p-a}}{a!(p-a)!},\qquad 1\le a<p.
\tag{1022.17}
\]
这来自 R889 的原 lower distributions \(D^r/r!\)，不是形式上
将 \(D^p/p!\) 约化。用
\(\Theta_{p,m}=-mB Q_m\)，在 \(j_H^{(p)}\) 上的 \(Q_2\)
线性部分准确为
\[
Q_{2,z}\longleftrightarrow\tfrac12(Q_{1,u}+Q_{1,v}),\qquad
Q_{2,t}\longleftrightarrow\tfrac12(-Q_{1,u}+Q_{1,v}).
\tag{1022.18}
\]
其余项全为 (1022.17) 型，总 \(D\) 次数是 \(p\)。

从 Frobenius vacuum 开始，构造总 \(Q\) 次数不超过 \(p-1\)
的向量时，每次应用一个 \(Q\) 之前的总次数不超过 \(p-2\)。
由 \([D_i,Q_i]=1\)、\(D_i\) 杀 vacuum，
(1022.17) 在这些向量上全为零。因此可在这个完整有限范围内，
逐次使用 (1022.18)，没有漏掉未审的 cross 项。

又
\[
\Omega_{\gamma,m}
 =(Q_{m,2}-\gamma^{-1}Q_{m,1})^{p-1}
\]
由 \(\binom{p-1}{r}=(-1)^r\) 精确成立。
(1022.18) 将括号送到
\[
\frac{1-\gamma^{-1}}2
 (Q_{1,v}-\gamma'^{-1}Q_{1,u}).
\]
其标量的 \(p-1\) 次幂是
\[
\left(\frac{1-\gamma^{-1}}2\right)^{p-1}
 =\frac{\gamma}{\gamma'}.
\]
故对原 vacuum \(w_1=s_p\boxtimes s_p\)，
\[
\boxed{\quad
\Omega_{\gamma,2}j_H^{(p)}w_1
 =\frac{\gamma}{\gamma'}\,
 j_H^{(p)}\Omega_{\gamma',1}w_1.
\quad}
\tag{1022.19}
\]

还须固定左侧下降源的标量。
R1020 §2 的原二-primary 列矩阵给，在目前
\(A\bmod2=I\) 的情形，
\[
\mathcal K_{A,2}(V^p\boxtimes\mathsf X^p)
 =-2c_A\,\mathsf X\boxtimes V,\qquad
\mathcal K_{A,2}(\mathsf X^p\boxtimes V^p)
 =-2c_A\,V\boxtimes\mathsf X.
\]
交换轴的 \(J\) 情形把两输出交换。因此
\[
\boxed{\quad
\mathcal K_{A,2}j_H^{(p)}w_1
 =2e_Ac_A\,\mathcal A,\qquad
e_A=\begin{cases}1,&A\bmod2=I,\\-1,&A\bmod2=J.\end{cases}
\quad}
\tag{1022.20}
\]
所有 CM residue 乘子此时都已归一为一；没有隐含的 tame 相位。

最后，\(A'H=HA\)，所有实际 line-bundle 比较在原点取一，
所以相应 pullback 方块严格交换。
将 (1022.20) 和 principal 的 (1022.8) 代入 (1022.19)，得
\[
\boxed{\quad
d_{A'}=2e_A\frac{\gamma'}{\gamma}\,c_A.
\quad}
\tag{1022.21}
\]
由已证 \(d_{A'}^2=D_p\gamma'^2\)，立即得到
\(c_A^2=D_p\gamma^2/4\)。与 (1022.2) 合并，完成 (1022.3)。

## 6. 原多项式式与 Gaussian 常数

\(T^-\) 在 \(\eta\mapsto v=\eta^6\) 下的像恰是
\(v^{N+1}=-1\) 的全部 \(N+1\) 个不同根。
因此 (1022.3) 等价于 (1022.4) 的多项式同余。

由于 \(4vP(v)^2\) 的次数不超过 \(2N+1<2(N+1)\)，约化后的常数项
只来自原 \(v^{N+1}\) 项，符号为负一。
所以
\[
D_p=-4[v^N]P(v)^2=-4\sum_{i=0}^N a_i^2a_{N-i}^2.
\]
这个有限和的非零及平方性来自前述完整相对证明，
不来自有限样本或未经证明的二次和非退化。

若 \(p\equiv5\bmod12\)，则 \(\iota^2=-1\) 的
\(\iota\in\mathbf F_p\) 属于 \(T^-\)，且 \(\iota^6=-1\)。
消费 R1016 §7.2 已核的同一原尺度值
\[
\mathcal C_N(\iota)
 =-\tfrac12(-432)^{(p-1)/4},\qquad
\mathcal C_N(\iota)^2=-\tfrac14.
\]
代入 (1022.3) 即给 \(D_p=1\)。
本篇未重做该 Gaussian 计算。

对一般 \(p\)，选一次 \(\delta_p\in\mathbf F_p^\times\)
满足 \(\delta_p^2=D_p\)，则所有方向准确满足
\[
\eta^3\mathcal C_N(\eta)\in\{\delta_p/2,-\delta_p/2\}.
\tag{1022.22}
\]
由 (1022.2)，这是原 \(c_A/\gamma\) 的同一个两值结论。
仍须保留实际方向上的正负号，不能把它们任意改成同号。

## 7. 原筛选边界、来源与复核

R1020 的完整 \(H_p/\mathcal C_N\) 比例现在可消费 (1022.22)：
原方向 scalar 已压成一个共同单位及实际符号函数。
但指定 Fourier/primitive/Legendre 投影会受这个符号函数影响。
本篇仍没有证明同一个原标签
\[
h=6i+7,\quad(h,p+1)=1,\quad
P_{h-1}(1/s)f_i g_{N-1-i}\ne0.
\]
两值单位函数不能自行替代其指定 Fourier 坐标的非零。
O2 的 bare \(A_r+BT_r\)、实际 global log 和 O0 全覆盖也继续开放。
**Serre 主目标仍 OPEN。**

依赖：

- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md) §§1–2：
  原有限平坦 theta automorphism、实际积分 linearization、
  Hensel 唯一性和完整角色；本篇明确复用于 index one。
- [R1016](R1016-original-small-index-theta-and-complete-convolution-units.md)：
  odd index 的实际刚化同构、principal / index-two 下降、
  \(J_{1,1}\)、原 period 比较及已成 Gaussian 精确值。
- [R1020](R1020-original-critical-convolution-complete-theta-scalar-bridge.md)：
  真实二-primary 矩阵及全部共同 scalar。
- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)：
  每个核方向的原 norm-\(p\) 表示及同核十二个单位。
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md)：
  原低阶分布和完整 \(Q\)-vacuum 关系。
- R881 已实读的 Shin, Propositions 2.12–2.13：
  相对有限 theta 等价及 base-change-compatible intertwiner line。

o1_theta 与 root 独立纸核实际积分格、trace 定标的全局代数域、
复共轭与原 \(p\) Frobenius、两种 \(p\)-单位/复范数论证的不同作用、
canonical kernel splitting、回文符号、\(H\) 的整性、
全部总阶 \(p\) cross 项、二-primary 的 \(2e_A\)、
以及多项式常数项。无数学程序执行，无旧窗口或矩阵枚举重跑。
