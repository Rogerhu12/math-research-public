# R1013：原临界多项式的实际 theta 下降与统一零点界

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：未经 primitive/Legendre 筛选的原临界多项式，在范数 −1 圆上的零点数有绝对常数上界。** 证明使用原有限平坦 theta 作用、每个方向的实际 \(p\)-同源，以及一个四维源的真实第五阶 jet。它不证明原筛选后的同 \(h\) 非零，不解决 O0，也不将整个非整 sigma 级数约化。

## 1. 原数据与结论

保持
\[
p=6N+5\ge41,\qquad k=\mathbf F_{p^2},\qquad
E_0:y^2=x^3-1,\qquad \omega=dx/(2y)=dz,
\]
\[
F=x\sigma^6=\sum_{i\ge0}f_i z^{6i+4},\qquad
G=-xy\sigma^6=\sum_{j\ge0}g_j z^{6j+1},
\]
以及原六水平标记、sigma 规范和普通 Taylor 系数。以下临界系数全部在 R702 已证的整范围内。记
\[
T^-=\{\eta\in k^\times:\eta^{p+1}=-1\},\qquad
H_p(\eta)=\sum_{i+j=N-1}\overline f_i\overline g_j\,\eta^{6i+4}.
\tag{1013.1}
\]
系数 \(\overline f_i,\overline g_j\) 在 \(\mathbf F_p\) 中。

**定理。** 置
\[
M=6^4\left|\operatorname{Sp}_4(\mathbf Z/6)\right|
  =6^4\cdot720\cdot51840.
\]
则
\[
\boxed{\quad
\#\{\eta\in T^-:H_p(\eta)=0\}\le3M<10^{12}.
\quad}
\tag{1013.2}
\]
特别地，\(p+1>3M\) 时 \(H_p\) 非零；取 \(p>10^{12}\) 是一个宽松的充分条件。因此在该范围至少有一对原 \(i+j=N-1\) 满足 \(f_i g_j\not\equiv0\)。

这里尚未要求 \(h=6i+7\) 本原，也未乘 \(P_{h-1}(1/s)\)。这两个条件保留为后继问题，不能由本定理删去。

## 2. 实际同源与两个不同的方向

R1012 已证明：对每个 \(\kappa\in T^-\)，恰有十二个有序向量
\[
v=(\alpha,\beta)\in\mathbf Z[\zeta]^2,\qquad
N\alpha+N\beta=p,\qquad \alpha/\beta\equiv\kappa\pmod p.
\tag{1013.3}
\]
\(\alpha,\beta\) 都是 \(p\)-单位。矩阵
\[
A=A_v=
\begin{pmatrix}
\alpha&-\overline\beta\\
\beta&\overline\alpha
\end{pmatrix},
\qquad A^\dagger A=pI,\qquad\det A=p
\tag{1013.4}
\]
定义原 \(E_0^2\) 的实际同源，次数为 \(p^2\)。

以下两个参数必须分开：
\[
\kappa_{\rm out}=\alpha/\beta\bmod p,\qquad
\gamma=-\overline\alpha/\beta\bmod p.
\tag{1013.5}
\]
微分像的方程是 \(U=\kappa_{\rm out}V\)，实际核则为
\[
K_\gamma=\{(\gamma P,P):P\in E_0[p]\}.
\tag{1013.6}
\]
确切地，\(A^\dagger A=pI\) 给 \(\ker A\subset E_0[p]^2\)，第二行和 \(\beta\) 的可逆性给 (1013.6)；第一行由范数等式自动成立。两参数均有范数 −1，但一般不同。

令 \(L_m=O(mO)\) 且 \(\mathcal L=L_6\boxtimes L_6\)。有实际线丛同构
\[
I_A:A^*\mathcal L\xrightarrow{\sim} L_{6p}\boxtimes L_{6p}.
\tag{1013.7}
\]
它可在原良好整模型上构造，并在 \(O^2\) 的纤维 rigidify 为一。理由是：对 \(\mathcal L_1=L_1\boxtimes L_1\)，(1013.4) 先给
\(A^*\mathcal L_1\) 与 \(\mathcal L_1^p\) 代数等价；它们的商是对称的 \(\operatorname{Pic}^0\) 元素，故为二挠。取六次幂消去这个商。基底上的线丛因子由原点 rigidification 消去。

尤其不能仅凭极化等式丢掉二挠歧义。本篇使用六次幂后的实际 (1013.7)，并在 §6 仍计入全部 tame theta characters。

## 3. 原有限平坦核的不变向量

设
\[
\mathcal H=H^0(E_0,L_{6p}),\quad
V=H^0(E_0,L_6),\quad
\mathcal H_0=\ker D
 =\{f^p s_{6p}:f s_6\in V\}.
\]
R889 的原 theta 算子满足
\[
Q=q-\frac{d_p}{6B}=-\frac{\Theta_p}{6B},
\qquad [D,Q]=1,\qquad D^p=Q^p=0,
\]
\[
\mathcal H=\bigoplus_{r=0}^{p-1}Q^r\mathcal H_0,\qquad
\dim\mathcal H_0=6.
\tag{1013.8}
\]
这里 \(d_p\) 是真正的第 \(p\) 个平移分布，绝非 \(D^p/p!\)；
\(B\in\mathbf F_p^\times\) 是 R574/R889 的原单位。\(D,Q\) 均与实际六-primary theta 群交换。

### 3.1 核上的 splitting 和全部分布条件

使用 R589 (589.6) 的原参数 \(Y\)。该参数对全部 Teichmüller
\(\mu_{p^2-1}\) 线性，而不仅对范数一子群线性。因此
\[
E_0[p]=\operatorname{Spec}k[Y]/(Y^{p^2}),\qquad
[\gamma]^*Y=\gamma Y.
\]
其形式群律由 Teichmüller 等变性在总次数严格小于 \(p^2\) 时等于 \(X+Y\)。不声称整个截断 Hopf 代数是加法群；总次数 \(p^2\) 的项仍可能存在。

原对称 theta section \(\tau\) 的乘法式为
\[
\tau(u)\tau(v)=e(u,v)^{1/2}\tau(u+v).
\]
在 (1013.6) 上，乘积交换子因
\(N\gamma+1=0\) 而平凡，故 \(\tau\boxtimes\tau\) 限制为群 splitting。
这个 splitting 在 \(k\) 上唯一：其差属于
\[
\operatorname{Hom}_k(E_0[p],\mathbf G_m)=E_0[p]^D(k)=0,
\]
因为原超奇异 \(E_0[p]\) 及其 Cartier 对偶都是 local-local。由实际 \(A^*\) 下降得到的 splitting 因而就是这个 splitting。

其 \(Y\) 系数给
\[
L=\gamma D_1+D_2.
\]
其 \(Y^p\) 系数准确为
\[
\gamma^p\Theta_{p,1}+\Theta_{p,2}
 +\sum_{r=1}^{p-1}
 \frac{\gamma^rD_1^rD_2^{p-r}}{r!(p-r)!}.
\]
在 \(\ker L\) 上，每个混合项都变为 \(D_1^p\) 的倍数，故为零。因此不变条件化为
\[
(\gamma D_1+D_2)v=0,\qquad
(\gamma^pQ_1+Q_2)v=0.
\tag{1013.9}
\]

这是完整核不变条件。令 \(\delta_n\) 为参数 \(Y\) 的分布基；由上述严格低于 \(p^2\) 的加法律，
\[
\delta_1^a\delta_p^b=a!b!\delta_{a+pb},
\qquad0\le a,b<p.
\]
这些乘积组成整个分布代数的向量空间基，故两个正生成元作用为零等价于全部 augmentation 作用为零。证明没有将 \(E_0[p]\) 写成 \(\alpha_p\times\alpha_p\)，也不使用对 étale \(p\)-核的求和或除以核阶。

### 3.2 显式不变空间

由 (1013.8)，可将 \(\mathcal H\otimes\mathcal H\) 写成
\[
k[X,Y]/(X^p,Y^p)\otimes(\mathcal H_0\otimes\mathcal H_0),
\]
其中 \(Q_1,Q_2\) 是乘 \(X,Y\)，而 \(D_1,D_2\) 是相应偏导。
置 \(Z=Y-\gamma^{-1}X\)，使用 \(\gamma^p=-\gamma^{-1}\)。
于是 (1013.9) 分别为 \(\gamma\partial_X|_Z\) 和乘 \(Z\)。
同时被它们杀掉的空间恰为
\[
Z^{p-1}\otimes(\mathcal H_0\otimes\mathcal H_0).
\]
展开
\[
\Omega_\gamma(w):=
\sum_{r=0}^{p-1}
 \gamma^{-r}Q_1^rQ_2^{p-1-r}w.
\tag{1013.10}
\]
这里 \(\binom{p-1}{r}(-1)^r=1\)，所以 (1013.10) 正是乘 \(Z^{p-1}\)。
它给出实际同构
\[
\Omega_\gamma:\mathcal H_0\otimes\mathcal H_0
 \xrightarrow{\sim}(\mathcal H\otimes\mathcal H)^{K_\gamma}.
\tag{1013.11}
\]

令 \(W=H^0(E_0^2,\mathcal L)=V\otimes V\)，维数为三十六。
有限平坦下降和 (1013.7) 给
\[
I_A A^*(W)=(\mathcal H\otimes\mathcal H)^{K_\gamma}.
\]
因此存在唯一实际同构
\[
T_A:W\xrightarrow{\sim}\mathcal H_0\otimes\mathcal H_0,\qquad
I_A A^*=\Omega_\gamma T_A.
\tag{1013.12}
\]
这是同一个原 theta 源的比较，而不是另选一个具有相同维数的模型。

## 4. 原 μ6 角色迫使首五阶 jet 非零

取指定的 Frobenius 源
\[
w_0=(x^p s_{6p})\boxtimes((-xy)^p s_{6p}),\qquad
s_A=T_A^{-1}w_0\ne0.
\tag{1013.13}
\]
考虑真正的全局对角 CM \(\epsilon\in\mu_6\)；它不同于 R889 的 vacuum 归一化 \(M_\epsilon\)。
原作用下 \(Q\) 的权为一，而 \(w_0\) 的权为 \(5p\)。所以
\(\Omega_\gamma w_0\) 的权为
\[
5p+(p-1)=6p-1\equiv5\pmod6.
\]
矩阵 \(A\) 与全局对角 CM 交换，(1013.7) 的 rigidification 也使线丛同构交换：
其交换子是全局标量，原点纤维上为一。因此
\[
s_A\in W_5.
\tag{1013.14}
\]

在原点单位 local frame \(s_6/Y^6\) 中，原六维有理基的角色和首阶为
\[
\begin{array}{c|rrrrrr}
\text{section}&s_6&x^3s_6&-xys_6&x^2s_6&ys_6&xs_6\\ \hline
\mu_6\text{ weight}&0&0&1&2&3&4\\
\text{首阶}&6&0&1&2&3&4
\end{array}
\]
各首项系数非零。故 \(W_5\) 恰为四维，由
\[
G\boxtimes F,\quad
(x^2\sigma^6)\boxtimes(y\sigma^6),\quad
(y\sigma^6)\boxtimes(x^2\sigma^6),\quad
F\boxtimes G
\tag{1013.15}
\]
给出。这里 sigma 只是标识原 section，局部计算始终在整 local frame 中进行。

这四个 section 的首项是不同的五次单项式。因此每个非零 \(s_A\) 的首齐次项都是
\[
\boxed{\quad
P_A(U,V)=aUV^4+bU^2V^3+cU^3V^2+dU^4V\ne0.
\quad}
\tag{1013.16}
\]
没有低于五的项。特别地 \(P_A(U,1)\) 是 \(U\) 乘一个非零的至多三次多项式，在非零 \(U\) 上至多三个根。

## 5. 精确对接原临界多项式

在 \(\mathcal H\otimes\mathcal H\) 的两个原 local frame
\(s_{6p}/Y^{6p}\) 中，令 \(J_{2,3}\) 取 \(Y^2T^3\) 系数。

R889 (889.35)、(889.45) 已在同一个原 frame 中给出
\[
J_{2,3}
 (Q_1^{6i+6}Q_2^{6j+4}w_0)
 =\frac{(6B)^5}{12}(f_i g_j)^p,\qquad i+j=N-1.
\]
其余指数因原 \(\mu_6\) 支撑不贡献这个 jet。因此
\[
\boxed{\quad
J_{2,3}(\Omega_\gamma w_0)
 =\frac{(6B)^5}{12}\gamma^{-2}H_p(\gamma^{-1}).
\quad}
\tag{1013.17}
\]
使用了 \(f_i,g_j\in\mathbf F_p\)，以及
\(\gamma^{-(6i+6)}=\gamma^{-2}(\gamma^{-1})^{6i+4}\)。

另一方面，因 \(s_A\) 首阶恰五，任一 line-frame 的单位变化只以常数影响五阶齐次项；(1013.7) 的 rigidification 将该常数固定为一。同理，实际形式群同态 \(A\) 的高阶项不影响这个首 jet。由其微分
\[
U=\alpha Y-\overline\beta T=\kappa_{\rm out}V,\qquad
V=\beta Y+\overline\alpha T,
\]
得到
\[
J_{2,3}(I_A A^*s_A)
 =10\beta^2\overline\alpha^{\,3}P_A(\kappa_{\rm out},1).
\tag{1013.18}
\]
所有外乘因子均为单位。结合 (1013.12)、(1013.13)，有准确的零条件等价
\[
\boxed{\quad
H_p(\gamma^{-1})=0
\iff P_A(\kappa_{\rm out},1)=0.
\quad}
\tag{1013.19}
\]
若使用未 rigidify 的整 frame，(1013.18) 仅多一个非零常数，(1013.19) 不变。这里不需要声称整个 sigma quotient 整，也不需要把两个不同方向强行视为同一个方向。

## 6. 保全部 tame 相位的有限类型界

必要时扩到 \(\overline k\) 固定 tame theta structures；零点仍只在原 \(T^-\) 中计数。
源端六-primary theta 群作用在
\(\mathcal H_0\otimes\mathcal H_0\) 上，目标 theta 群作用在 \(W\) 上；两者都是三十六维、中心权一的绝对不可约表示。

因 \(Q_1,Q_2\) 与源端 tame theta 群交换，所有 \(\Omega_\gamma\) 都是该群的 intertwiners。实际 \(A^*\) 则通过 (1013.7) 诱导源、目标两个固定 tame theta 群之间的同构；底层是
\[
A:E_0[6]^2\longrightarrow E_0[6]^2.
\]
它可逆，因为 \(p\) 与六互素。底层对原固定 pairing 的 multiplier 是 \(p\)，但对各自实际线丛 pairing 的比较保持交换子与中心。故 (1013.12) 的 \(T_A\) 正是两固定表示经这个实际 lift 的 intertwiner。

固定任意一个 \(A_0\)。相对于 \(A_0\)，所有 lift 属于同一 tame Heisenberg 群的中心固定自同构群。底层有限模
\[
K_6=E_0[6]^2\simeq(\mathbf Z/6)^4
\]
有完美交替 pairing。每个中心固定自同构诱导
\(\operatorname{Sp}(K_6)\) 中的元素；同一底层元素的两个 lift 之差是
\(\operatorname{Hom}(K_6,\mathbf G_m)\)，个数为 \(6^4\)。
所以实际 projective \(T_A\) 类型数至多
\[
6^4|\operatorname{Sp}_4(\mathbf Z/6)|=M.
\tag{1013.20}
\]
不需要断言每个辛元素都能提升；上界已足够。中国剩余定理和标准辛基计数给
\[
|\operatorname{Sp}_4(\mathbf Z/6)|
=|\operatorname{Sp}_4(\mathbf F_2)|
 |\operatorname{Sp}_4(\mathbf F_3)|
=720\cdot51840;
\]
其中 \(|\operatorname{Sp}_4(\mathbf F_q)|=q^4(q^2-1)(q^4-1)\)。

若两个 \(A\) 具有相同实际 lift 类型，Schur 引理使其 \(T_A\) 相差一个非零标量；于是 \(s_A\) 和 \(P_A\) 也只差一个非零标量。

这一论证保留了全部 character，尤其六水平的二挠相位。它没有把“底层辛矩阵相同”擅自替换成“theta lift 相同”。也不要求不同 \(p\) 的矩阵可在同一个特征零模型中统一归一化；只需对每个固定 \(p\) 的类型数有同一个常数界。

## 7. 从向量计数到统一零点界

对一个固定类型，(1013.16) 在 \(\kappa_{\rm out}\ne0\) 上至多有三个零方向。R1012 的逐方向十二表示结论表明，该类型至多有
\(3\cdot12=36\) 个 bad 向量。全部类型遂至多有 \(36M\) 个 bad 向量。

另一方面，映射
\[
(\alpha,\beta)\longmapsto(\overline\alpha,-\beta)
\]
是所有 norm-\(p\) 有序向量的一个双射；其 image 方向正是
\(-\overline\alpha/\beta=\gamma\)。再取逆仍排列 \(T^-\)。故每一个
\(\eta=\gamma^{-1}\in T^-\) 也恰对应十二个向量。

由 (1013.19)，当 \(H_p(\eta)=0\) 时，这十二个向量全部 bad；
不为零时，它们全部不 bad。因此
\[
12\,\#\{\eta:H_p(\eta)=0\}\le36M.
\]
约去十二，即为 (1013.2)。全部计数为纸面有限群和格计数，没有枚举矩阵、素数窗口或执行数值试验。

## 8. 原目标的边界与准确后继

本篇对 R1012 的实际桥给出了新的非零信息：对全部充分大的 \(p\)，未经筛选的原 critical \(H_p\) 必非零，而且在 \(T^-\) 上几乎处处非零。因此 R1012 的原导数平衡系数也在至多 \(3M\) 个方向之外非零。

原 O1 则要求至少一个
\[
h=6i+7,\quad i+j=N-1,\quad
(h,p+1)=1,\quad P_{h-1}(1/s)f_i g_j\ne0.
\]
有限值零点界不自动控制这些 Fourier 系数。一个只含非本原指数的单项式可以在所有非零点都非零，已经说明为何不能由 (1013.2) 省掉 primitive 条件；同理不能省掉 Legendre 因子。这里没有把该单项式冒称为本篇实际 \(H_p\) 的反例，只说明尚需关于实际谱支撑的额外证明。

后继应对同一个 \(\Omega_\gamma w_0\)、实际有限类型或其投影证明保留标签非零。R1012 左端与 O2 的 bare \(c_{p-r}^{\pm}\) 之间也仍没有已证单位等价。原主目标的全部 O0 分支继续开放。

## 9. 依赖、原始来源与核准

- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md) §§1–2：每方向十二表示、原实际 \(A_v\) 和 \(H_p\)；本篇不重算这些输入。
- [R589](R589-specified-type-three-coefficient-and-actual-CM-unit-criterion.md) (589.6)–(589.10)：同一个全 Teichmüller 等变参数和合法有限微分范围。
- [R878](R878-original-finite-theta-action-and-section-projections.md) §§2–4：原对称 theta section、有限平坦 splitting、tame 中央化与 Frobenius vacuum。
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md) §§2–7：原 \(Q\)、Weyl 分解、实际 local frame 和精确第五阶读数；正文使用其证明内容而非仅维数类比。
- B. Moonen, [The Theta Group of a Line Bundle](https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf), Theorem 8.10、Proposition 8.15：忠实平坦下降与下降后 theta 群的中央化商。这些命题不要求核 étale。
- S. W. Shin, [Abelian Varieties and Weil Representations](https://math.berkeley.edu/~swshin/AV-Weil.pdf), Propositions 2.12–2.13：任意特征的 theta 表示唯一性、Schur 结论及上同调基变换。
- D. Robert, [Efficient Algorithms for Abelian Varieties and Their Moduli Spaces](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/academic/hdr_details.pdf), §§2.5–2.6：实际 theta compatibility、rigidification 与偶水平 lift 的二挠歧义；本篇用更宽的全部 character 上界保留它，不使用仅对 étale 核的算法。

o1_theta 与 root 独立核准实际核/像两方向、完整分布条件、四维角色空间、五阶 unit-frame 比较及每方向十二的两次计数。root 实读上述原始下降和表示定理。没有数学程序执行，也没有重跑任何已登记窗口。
