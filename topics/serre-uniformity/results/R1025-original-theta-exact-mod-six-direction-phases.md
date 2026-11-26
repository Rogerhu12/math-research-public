# R1025：原 theta 标量的全部方向符号由模六数据准确确定

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：R1022 留下的每个方向的正负号，可以在原
Eisenstein norm-\(p\) 矩阵的模六数据中准确读出。**
保留同一 principal theta、原点 rigidification、积分 torus、
原 \(H_p\) 和完整卷积 \(\mathcal C_N\)。没有换归一、取绝对值，
或把方向非零当成 primitive/Legendre 同标签非零。

## 1. 原记号和结论

沿 R1016、R1020、R1022，设
\[
p=6N+5\ge41,\quad \mathcal O=\mathbf Z[\zeta],\quad
s=\zeta-\zeta^2,\quad E:y^2=x^3-1,
\]
\[
A=\begin{pmatrix}\alpha&-\bar\beta\\
                  \beta&\bar\alpha\end{pmatrix},
\qquad N\alpha+N\beta=p,\qquad
\gamma=-\bar\alpha/\beta,\quad \eta=\gamma^{-1}.
\]
实际标量仍由
\[
\mathcal K_{A,1}(s_p\boxtimes s_p)=d_A(s_1\boxtimes s_1),\qquad
\mathcal K_{A,2}(V^p\boxtimes V^p)=c_A(\mathsf X\boxtimes\mathsf X)
\]
定义，且 \(c_A=-\gamma^{-2}\mathcal C_N(\eta)\)。

在 \(\mathcal O/(s)\simeq\mathbf F_3\) 记
\[
a=\alpha\bmod s,\qquad b=\beta\bmod s.
\]
由 \(N\alpha+N\beta=p\equiv2\bmod3\)，两者都属于
\(\{1,-1\}\)。以其唯一整数符号提升理解下面的 \(ab\)。
模二恰有 \(\alpha,\beta\) 中的一个非零，定义
\[
e_A=\begin{cases}
+1,&\alpha\bmod2\ne0,\\
-1,&\beta\bmod2\ne0.
\end{cases}
\tag{1025.1}
\]

**定理 1025.1。** 存在只依赖原 \(p\) 归一的共同单位
\(\delta'_p\in\mathbf F_p^\times\)，满足
\((\delta'_p)^2=D_p\)，且对全部原方向、全部原表示，
\[
\boxed{\quad
d_A=\delta'_p\,ab\,\gamma,\qquad
\frac{2c_A}{\gamma}=\delta'_p\,e_Aab,\qquad
\eta^3\mathcal C_N(\eta)=-\frac{\delta'_p}{2}e_Aab.
\quad}
\tag{1025.2}
\]
这里 \(D_p\) 正是 R1022 的共同常平方；没有为
\(p\equiv11\bmod12\) 擅自令它等于一。

R1020 中
\(\epsilon=(3/p)\)、\(t^3=4\) 的原 \(t\in\mathbf F_p\)、
\(\chi=\operatorname{lift}_{\mu_6}(\alpha/\beta\bmod3)\)
以及原 \(B\) 全部不变。因此原临界值还准确满足
\[
\boxed{\quad
\eta^3H_p(\eta)=
-\frac{60\epsilon t\delta'_p}{(6B)^5}
 e_A b\chi\,(N\alpha)^2(\chi\bar\alpha+\bar\beta).
\quad}
\tag{1025.3}
\]
此式保留实际符号；下一步仍须对同一值函数施加原
primitive 和 Legendre 两个 mask。

## 2. 相对 norm-one 标量其实只有真实的两个相位

消费 R1022 的实际构造。令 \(n=p+1\)、\(T=\ker N_{\mathbf F_{p^2}/\mathbf F_p}\)、
\(L=\mathbf Q(\mu_n)\)，\(\widetilde\chi(t)\) 为原 tangent character
的 Teichmüller lift。原 integral torus 作用 \(M_t\) 满足
\(M_t^n=1\)，其 character 为除 \(\widetilde\chi\) 外的全部
\(T\) characters 各一次。

记
\[
v_A=I_{A,1}A^*(s_1\boxtimes s_1)
       \in H^0(E^2,L_p\boxtimes L_p).
\]
当 \(t=\gamma/\gamma_0\) 时，R1022 已给
\[
(M_t\boxtimes1)v_{A_0}=\lambda_t v_A,\qquad
\lambda_t\in L^\times,\quad
\lambda_t c(\lambda_t)=1,\quad
\bar\lambda_t=d_A/d_{A_0}.
\tag{1025.4}
\]
其中 \(c\) 为复共轭，原 \(p\) 处其约化为 Frobenius。

还须支付所有有限处的整性，不能只从复绝对值一猜根单位。
对 \(L\) 任一有限处，经有限扩张使原 \(j=0\) 曲线有好约化；
CM endomorphisms 及 \(L_p=O(pO)\) 均延拓。
在剩余特征不为 \(p\) 的地方，实际 odd-\(p\) theta splitting
仍存在：\(u/2\) 是在 \(E[p]\) 上乘二的逆，不要求底环有 \(1/2\)。
相对 theta 等价给可逆的整 intertwiner \(J_t\)。
它的 \(n\) 次幂中央化不可约 Heisenberg 作用，故
\[
J_t^n=c_t I,\qquad c_t\in R_\ell^\times.
\]
写 \(M_t=a_tJ_t\)，由 \(M_t^n=1\) 得
\(a_t^n=c_t^{-1}\)，所以 \(a_t\) 是单位，\(M_t\) 整且可逆。
此论证不要求剩余特征不整除 \(n\)。
在 \(p\) 处直接使用 R881/R1022 已证明的 integral \(M_t\)。

同一好模型上的每个 \(v_A\) 都 primitive：\(A\) 是 finite flat
isogeny，原非零 theta section 的特殊纤维拉回非零，而刚化
\(I_{A,1}\) 是整同构。更换原模型及原点 frame 只把全部 \(v_A\)
同乘一个依赖 \(p\)、不依赖 \(A\) 的尺度，因为源与靶线丛
分别固定为 \(L_1\boxtimes L_1\)、\(L_p\boxtimes L_p\)。
所以比较中的 \(\lambda_t\) 不变，且在每个有限处均为单位。

\(L\) 为 abelian 数域，复共轭与所有嵌入交换；
\(\lambda_tc(\lambda_t)=1\) 因而给其全部复共轭绝对值为一。
Kronecker 定理遂使 \(\lambda_t\) 为根单位。
\(L\) 在 \(p\) 未分歧，故其根单位的阶与 \(p\) 互素。
由 R1022 的常平方，
\(\bar\lambda_t^2=t^2\)；prime-to-\(p\) 根单位的约化单射，于是
\[
\lambda_t=\varepsilon_t\widetilde\chi(t),\qquad
\varepsilon_t\in\{1,-1\}.
\tag{1025.5}
\]
置 \(\widetilde M_t=M_t/\widetilde\chi(t)\)，则
\[
(\widetilde M_t\boxtimes1)v_{A_0}=\varepsilon_t v_A.
\tag{1025.6}
\]
其 character 准确为 \(T\) 的全部非平凡 characters 各一次。
下面在真实的三处好约化读出 \(\varepsilon_t\)。

## 3. 三处真实好模型与唯一非 projective Jordan 块

先核准 torus 中 \(\zeta\) 与几何自同构的准确关系。
在原 sigma frame 中令 \(J_\zeta f(z)=f(\zeta z)\)。
它在 theta translations 上诱导 \(\zeta^{-1}\)，不是 \(\zeta\)。
原代数基为
\[
\sigma^p\{1,x,\ldots,x^{3N+2},
                  y,xy,\ldots,x^{3N+1}y\}.
\]
由 \(x(\zeta z)=\zeta x(z)\)、\(y(\zeta z)=y(z)\)、
\(\sigma(\zeta z)=\zeta\sigma(z)\)，直接求 character 得
\(\operatorname{tr}J_\zeta=-\zeta\)。
对实际 torus 作同一 trace 归一后，
\[
M_\zeta=\zeta^{-1}J_{\zeta^{-1}},\qquad
\widetilde M_\zeta=\zeta J_{\zeta^{-1}}.
\tag{1025.7}
\]
因此模三后它就是以下几何 \(g^{-1}\)，无需删去一个未核相位。

取 \(u^2=\zeta-1\)，作实际坐标更换
\[
x_{\rm old}=1+u^2X,\qquad y_{\rm old}=u^3Y.
\]
方程变为
\[
Y^2=X^3+(3/u^2)X^2+(3/u^4)X,
\]
在三处有好约化
\[
\bar E:\ Y^2=X^3-X.
\]
原 \(\zeta\) 作用为 \(X\mapsto1+\zeta X,\ Y\mapsto Y\)，约化为
\[
g:X\mapsto X+1,\quad Y\mapsto Y.
\]

在 \(H=H^0(\bar E,L_p)\) 中用 rational-function 基
\(1,X,\ldots,X^{3N+2}\) 和
\(Y,YX,\ldots,YX^{3N+1}\)，乘同一 canonical divisor section。
令 \(U=X^3-X=Y^2\)，可分解为
\[
\bigoplus_{j=0}^{N}U^j\langle1,X,X^2\rangle
\quad\oplus\quad
\bigoplus_{j=0}^{N-1}YU^j\langle1,X,X^2\rangle
\quad\oplus\quad YU^N\langle1,X\rangle.
\]
所以，若 \(J_r\) 表示一个 \(r\) 阶单 Jordan 块，
\[
H\simeq J_3^{\,2N+1}\oplus J_2.
\tag{1025.8}
\]
没有 \(J_1\)，且只有一个 \(J_2\)。

对 diagonal \(g\) 的 \(H\otimes H\)，含 \(J_3\) 的 tensor
summand 都 projective；而
\[
J_2\otimes J_2\simeq J_3\oplus J_1.
\]
例如 \(ge_1=e_1+e_0\) 时，
\((g-1)^2(e_1\otimes e_1)=2e_0\otimes e_0\ne0\)，
并且 \(g-1\) 秩为二，准确给该分解。
故实际 Tate 空间
\[
\mathcal T=
\frac{\ker(g-1:H\otimes H\to H\otimes H)}
     {\operatorname{im}(1+g+g^2)}
=\frac{\ker(g-1)}{\operatorname{im}(g-1)^2}
\tag{1025.9}
\]
恰为一维。

## 4. Torus 在这条 Tate 线上平凡

写 \(n=3^e n_0\)，\(3\nmid n_0\)。
§2 给 \(\widetilde M\) 在三处的真实整作用，§3 使它与 \(g\)
交换。对 prime-to-three 子群 \(T_{n_0}\) 作整 character
projectors，char-zero 中的准确秩在约化后保持：

- trivial eigenspace 的维数是 \(3^e-1\)；
- 其余每个 eigenspace 的维数是 \(3^e\)。

这些都是 \(C_3\)-module 的 direct summands。
由 (1025.8) 只有一个 \(J_2\) 且无 \(J_1\)，维数模三迫使
唯一的 \(J_2\) 位于 trivial \(T_{n_0}\) eigenspace；
其余 eigenspaces 都 projective。因此
\(\widetilde M_t\otimes1\) 在 (1025.9) 上对 \(T_{n_0}\) 平凡。
余下的三次幂阶子群在特征三的一维空间上也只能平凡。
于是
\[
(\widetilde M_t\otimes1)|_{\mathcal T}=1
\quad\text{对全部 }t\in T.
\tag{1025.10}
\]

## 5. 原二阶 jet 在 Tate 线上准确读出 \(ab\)

在好模型原点取局部参数 \(z=-X/Y\)，有
\(g(z)=z+O(z^3)\)。
刚化 \(L_p\) frame 的 multiplier 为 \(1+O(z^2)\)；
canonical divisor section 的几何 character 模三为一，
frame 比值可写成 \((z/gz)^p\)。
因此 diagonal \(g-1\) 对任意局部 section 的总消失阶提高至少二；
\((g-1)^2\) 的像在 \(O^2\) 总消失阶至少四。
二阶 jet 从而下降为 \(\mathcal T\) 上的线性读数。

在同一好模型的原点刚化规范中仍记全部向量为 \(v_A\)；
§2 的共同尺度不改变 (1025.6)。
这些向量在 diagonal \(g\) 下 invariant：char-zero 原 diagonal
\(\zeta\) 的 theta character 为 \(\zeta^2\)，模三为一，
且原 \(I_{A,1}\) 与 CM 作用交换。
由于 \(s=\zeta-\zeta^2\) 的微分在剩余特征三为零，原矩阵微分为
\[
dA=\begin{pmatrix}a&-b\\b&a\end{pmatrix},\qquad a^2=b^2=1.
\]
原 \(s_1\boxtimes s_1\) 的首项为 \(zw\)，而刚化常数为一，
故
\[
v_A=ab(z^2-w^2)+(a^2-b^2)zw+O(\text{总次数}\ge3)
    =ab(z^2-w^2)+O(\text{总次数}\ge3).
\tag{1025.11}
\]
它的二阶 jet 非零，故其 Tate 类非零。
取 \(z^2\) 系数的读数就是 \(ab\)。

将 (1025.6) 约化至三处，利用 (1025.10)，得到
\[
a_0b_0=\varepsilon_t ab\quad\text{于 }\mathbf F_3.
\]
两个整数符号在 \(\mathbf F_3\) 仍不同，所以这是实际符号等式
\[
\varepsilon_t=\frac{a_0b_0}{ab}.
\tag{1025.12}
\]
这一步使用真正的 mod-three theta module 及原 section 的 jet，
不是从一组有限方向值猜出相位。

## 6. 回到原 \(p\) 处，并与 addition、原 \(H_p\) 接合

令
\[
\delta'_p=(d_{A_0}/\gamma_0)a_0b_0.
\]
R1022 的回文关系使 \(d_{A_0}/\gamma_0\in\mathbf F_p^\times\)，
且平方为 \(D_p\)。
由 (1025.4)–(1025.5)、(1025.12) 和
\(t=\gamma/\gamma_0\)，立刻得
\[
d_A=\delta'_p ab\gamma.
\]

再用 R1022 §5 的真实 addition 比较。
以同核 \(\mu_6\) 左乘把 \(A\bmod2\) 归一为 \(I\) 或
\(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\)。
这种左乘不改 \(ab\)。
令
\[
H=I+J,\quad A'=HAH^{-1},\qquad
\gamma'=(\gamma-1)/(\gamma+1).
\]
这是同一整 norm-\(p\) 矩阵问题。模 \(s\) 时
\(A=aI+bJ\) 与 \(H\) 交换，所以 \(a'=a,b'=b\)。
R1022 已保留全部 degree-\(p\) cross terms 后给
\[
d_{A'}=2e_A(\gamma'/\gamma)c_A.
\]
代入刚证明的 principal 值，得到 (1025.2) 的第二、三式。

还须保同核全部十二代表。
左乘 \(\operatorname{diag}(u,\bar u)\)、\(u\in\mu_6\) 时，
\(a,b\) 同乘 \(u\bmod s=\pm1\)，故 \(ab\) 不变；
\(j\) 代表则使 \(ab,d_A\) 同时反号，并使 \(e_A\) 反号。
所以 \(e_Aab\) 对全部同核代表不变，与原 \(c_A\)、
\(\mathcal C_N(\eta)\) 的来源相容。
最后将 (1025.2) 代入 R1020 的完整比例，得到 (1025.3)；
其中 \(a^2=1\) 只消去原式的两个 \(a\)，没有删除方向符号。

## 7. 准确完成的接口与继续范围

本篇把原方向相位完全化为 \(A\bmod6\) 的数据，
共同的 \(\delta'_p\) 仍是一个保留的原单位。
即使在 R1022 已有 \(D_p=1\) 的 \(p\equiv5\bmod12\) 行，
也没有任意选择 \(\delta'_p=1\)。

(1025.3) 是原带符号的 degree-five quaternion norm-sphere
值函数。原 primitive Fourier 标签 \(h=6i+7\) 和 Legendre
mask 必须继续作用在这个同一函数上；值处处非零或符号已知
都不自动保证某个共同保留标签非零。
它也没有把 R1015 的 bare 高坐标完整余项删去。

依赖：

- [R1022](R1022-original-theta-all-direction-constant-square.md)：实际 integral torus、trace 定义的 cyclotomic 域、相对 Hermitian norm、全部方向常平方及完整 addition 分布。
- [R1020](R1020-original-critical-convolution-complete-theta-scalar-bridge.md)：原 \(H_p/\mathcal C_N\) 的全部 tame-two/three 相位与共同尺度。
- [R1016](R1016-original-small-index-theta-and-complete-convolution-units.md)：原 \(d_A,c_A,\gamma,\eta\) 和 sigma 归一、同核十二代表。
- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md)：实际 theta group 与可基变换的相对 intertwiner line；本篇只在原 principal index-one 表示中使用。

o1_theta 与 root 纸面核准所有有限处整性、共同模型尺度、
准确 \(\zeta\) trace 方向、真实三处好模型、全部 Jordan summands、
Tate 线上的 torus 作用、原二阶 jet、同核符号及 addition 常数。
本证明不使用数学程序或有限数值结果作为依据。主目标仍 OPEN。


## 后继：全部行的绝对常平方现为一

[R1027](R1027-original-level-p-squared-theta-distribution-and-constant-one.md)
用实际 \(L_{p^2}\) 的 genuine 第 \(p\) 个 theta distribution、
\(A^\dagger A=[p]\) 的刚化复合及 R1025 的实际 dagger 符号，
证明全部 \(p\ge41,\ p\equiv5\bmod6\) 都有 \(D_p=1\)。
共同 \(\delta'_p\) 仍保其 \(\pm1\) 符号；原 primitive/Legendre
同标签和 bare 完整余项不因此自动关闭。
