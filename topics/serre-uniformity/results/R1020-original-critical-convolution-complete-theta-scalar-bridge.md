# R1020：原 \(H_p\) 与小 index 卷积的完整标量桥

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：原 \(H_p(\eta)/\mathcal C_N(\eta)\) 等于一个明确的五次
quaternion 表达式，保留共同 theta scalar、二挠符号与全部三挠相位。**
本篇继续 R1016、R1017 的同一来源。它没有将共同 scalar 归一为一，
也没有把未经筛选的单位结论改称原 primitive/Legendre 同标签非零。

## 1. 原数据与精确公式

固定
\[
p=6N+5\ge41,\quad E_0:y^2=x^3-1,\quad dz=dx/(2y),\quad
s=\zeta-\zeta^2,\quad s^2=-3.
\]
原 sigma、\(B\in\mathbf F_p^\times\)、\(Q_m\)、\(\Omega_{\gamma,m}\)、
\(I_{A,m}\) 与 \(\mathcal K_{A,m}=T_{A,m}^{-1}\)
全保持 R889/R1013/R1016 的规范。记
\[
V=\sigma^2,\quad \mathsf X=x\sigma^2,\quad
U=x^2\sigma^6,\quad Y_6=y\sigma^6,\quad R_-=(x^3-4)\sigma^6,
\]
\[
F=x\sigma^6,\qquad G=-xy\sigma^6.
\]
原 \(\mathcal C_N\) 与 \(H_p\) 分别为
\[
\mathcal C_N(\eta)=\sum_{i+j=N}a_i a_j\eta^{6i},
\quad V=z^2\sum_i a_i z^{6i},
\qquad
H_p(\eta)=\sum_{i+j=N-1}f_i g_j\eta^{6i+4}.
\]

取同一个 Eisenstein norm-\(p\) 表示
\[
A=\begin{pmatrix}\alpha&-\overline\beta\\
\beta&\overline\alpha\end{pmatrix},\quad
N\alpha+N\beta=p,\quad
\gamma=-\overline\alpha/\beta,\quad
\kappa=\alpha/\beta,\quad \eta=\gamma^{-1}\in T^-.
\tag{1020.1}
\]
所有含 \(\alpha,\beta\) 的最终公式在所选 \(p\) 上约化；二者 norm
均严格介于零和 \(p\) 之间，故有关外因子均非零。

令 \(r^2=3,\ i=s/r,\ \epsilon=(3/p)\)，并取唯一的
\(t\in\mathbf F_p\) 满足 \(t^3=4\)。写
\[
\alpha\equiv a+a's,\qquad \beta\equiv b+b's\pmod3,
\quad a,b\in\{1,-1\},\quad a',b'\in\mathbf F_3.
\]
这里 \(a,b\ne0\) 来自 \(a^2+b^2=p=-1\bmod3\)。
约化 \(\mu_6\to(\mathbf Z[\zeta]/3)^\times\) 是双射，故可定义
\[
\chi=\operatorname{lift}_{\mu_6}(\alpha/\beta\bmod3)
 =ab\,\zeta^{-(aa'-bb')}.
\tag{1020.2}
\]
它不是另选的可丢相位；它由原 \(\alpha,\beta\) 唯一确定。

**定理 1020.1。** 原实际下降源准确为
\[
\boxed{\quad
\mathcal K_{A,6}(F^p\boxtimes G^p)
 =\epsilon t\,a\chi\,c_A
   \bigl(\chi U\boxtimes Y_6-Y_6\boxtimes U\bigr),
\qquad c_A=-\gamma^{-2}\mathcal C_N(\eta).
\quad}
\tag{1020.3}
\]
因此
\[
\boxed{\quad
\frac{H_p(\eta)}{\mathcal C_N(\eta)}
 =\frac{120\epsilon t}{(6B)^5}\,
 a\chi\,(N\alpha)^2
 \bigl(\chi\overline\alpha+\overline\beta\bigr).
\quad}
\tag{1020.4}
\]
同一核方向的十二个原表示给同一个右侧。公式不是仅在选定
Gaussian 方向上的比较；它适用于全部 \(T^-\)。

## 2. Index two 的另一真空及其共同 scalar

R1016 已证明
\[
\mathcal K_{A,2}(V^p\boxtimes V^p)
 =c_A\,\mathsf X\boxtimes\mathsf X,\qquad
c_A=-\gamma^{-2}\mathcal C_N(\eta)\ne0.
\tag{1020.5}
\]
这里须在同一实际算子内确定 \(\mathsf X^p\boxtimes\mathsf X^p\)
的像，不能为它另取一个自由 scalar。

对 \(e^3=1\)，index-two 的实际半周期 lift 是
\[
\rho_e f(Q)=\frac{x(Q)-e}{er}\,f(Q+(e,0)).
\]
在有序基 \((V,\mathsf X)\) 的列系数上，其矩阵为
\[
C_e=\frac1r
\begin{pmatrix}-1&2e\\e^{-1}&1\end{pmatrix}.
\tag{1020.6}
\]
加法公式直接给
\[
C_e^2=I,\quad C_1C_\zeta=iC_{\zeta^2},\quad
\sum_{e^3=1}C_e=\operatorname{diag}(-r,r).
\]
这里是列系数矩阵；它与 R1016 §7.2 使用的行作用矩阵互为转置，
不可混用复合次序。

因二在原 CM 环中惰性，\(A\bmod2\) 是 monomial。
它的两个非零乘子在 \(x(P_e)\) 上诱导
\(e\mapsto u_1e,\ e\mapsto u_2e\)，其中
\(u_1,u_2\in\mu_3,\ u_1u_2=1\)：不交换轴时来自
\(\alpha,\overline\alpha\)，交换时来自
\(-\overline\beta,\beta\)，两种的非零 norm 均为一模二。

实际对称 lifts 的 Frobenius 运输相位为
\(\delta=(-1/p)\)。确实，比较 \(C_1C_\zeta=iC_{\zeta^2}\)
与其 Frobenius，且用 CM 循环相容性使每轴的三个符号相同，
得到唯一相位 \(\delta=i^{p-1}\)。
逐轴 intertwiner 因而满足
\[
K_j C_e^{(p)}=\delta C_{u_je}K_j.
\tag{1020.7}
\]
\(r^p=\epsilon r\) 且 \(\delta\epsilon=(-3/p)=-1\)。
对 (1020.7) 求和，迫使 \(K_j\) 反对角。写
\[
K_jV^p=c_j\mathsf X,\qquad K_j\mathsf X^p=d_jV.
\]
再代 \(e=1\)，准确给
\[
d_j=2\delta\epsilon u_jc_j=-2u_jc_j.
\]
两个二维 Heisenberg 因子各不可约，故整个实际
\(\mathcal K_{A,2}\) 是这两个 intertwiner 的张量积（可能交换轴）
乘同一个 scalar。用 (1020.5) 固定该 scalar 后，
\[
\boxed{\quad
\mathcal K_{A,2}(\mathsf X^p\boxtimes\mathsf X^p)
 =4c_A\,V\boxtimes V.
\quad}
\tag{1020.8}
\]
没有删除二-primary 的符号或把两个未知尺度独立归一。

## 3. Norm-three 拉回及真实分布的符号

令 \(J_m:[s]^*L_m\simeq L_{3m}\) 为原点纤维取一的比较，
并以 \(j_m=J_m[s]^*\) 记 section 拉回。原 sigma 乘法式及
同一椭圆曲线的 norm-three 加法式为
\[
\sigma(sz)=s\,x\sigma^3,\qquad
x(sz)=-\frac{x^3-4}{3x^2}.
\]
因此
\[
j_2V=-3U,\qquad j_2\mathsf X=R_-.
\tag{1020.9}
\]
第二式原点值为一，固定了实际 rigidification；且
\(J_{2p}=J_2^{\otimes p}\)，所以 \(j_{2p}(f^p)=(j_2f)^p\)。

还要比较分布，不能把拉回误当成保持 \(Q\) 的同一个 index。
canonical 对称 theta section 对这些实际线丛拉回自然。
R889 的原参数满足
\([s]^*Y=sY\bmod Y^{p^2}\)，故取该 theta section 的 \(Y^p\)
系数得到
\[
\Theta_{p,6}j_{2p}=s^p j_{2p}\Theta_{p,2}.
\]
所用参数关系也可由
\(\omega=dY\bmod Y^{p^2-1}\)、\([s]^*\omega=s\omega\)
及其与原 norm-one 作用交换核定：低于 \(p^2\) 的非线性候选次数
须为 \(1\bmod p+1\)，且其中没有可被导数漏掉的 \(p\) 倍次数。
由于 \(\Theta_{p,m}=-mB Q_m\)，遂有
\[
Q_6j_{2p}=\frac{s^p}{3}\,j_{2p}Q_2=s^{-1}j_{2p}Q_2.
\tag{1020.10}
\]
这里使用 \(s^p=-s,\ s^2=-3\)，符号不可省。

双轴 \(\Omega\) 的总分布次数为 \(p-1\)，所以
\[
\Omega_{\gamma,6}(j_{2p}\boxtimes j_{2p})
 =-\,(j_{2p}\boxtimes j_{2p})\Omega_{\gamma,2}.
\tag{1020.11}
\]
\(A\) 与对角 \([s]\) 交换，两个 line-bundle 方块又有同一原点
rigidification，故严格交换，没有另一个全局 scalar。
由实际 \(I_AA^*=\Omega_\gamma T_A\)，
(1020.8)–(1020.11) 得
\[
\boxed{\quad
\mathcal K_{A,6}(R_-^p\boxtimes R_-^p)
 =-36c_A\,U\boxtimes U.
\quad}
\tag{1020.12}
\]
这固定 R1017 三-primary 基运输的共同 \(d_0=-36c_A\)；
它来自真实分布相容性，没有假定 \(\Omega\) 保乘法。

## 4. 实际三挠点、基尺度与 Weyl 相位

使用同一
\[
P=(0,i),\qquad Q=(t,-r),\qquad t^3=4.
\]
原 canonical lifts 是
\[
Rf=-\frac{(y+i)^2}{4}f(\,\cdot+P),\qquad
\tau_Qf=\frac{\ell^2}{12}f(\,\cdot+Q),\quad
\ell=y-\frac{rt^2}{2}x+r.
\tag{1020.13}
\]
它们与 R1017/R812 的实际 Miller 乘数相同，均三次为一且在
\([-1]\) 下送到自己的逆。直接比较乘数给
\[
R\tau_Q=\zeta\tau_QR,\qquad [s]Q=-P.
\tag{1020.14}
\]
具体地，commutator 在原点的值为
\[
\left(\frac{i+r}{i-r}\right)^2=\zeta.
\]
第二式可用
\[
y(sz)=-\frac{x^3+8}{3s x^3}y(z)
\]
在 \(Q\) 处核定。故这里的 \(P,Q\) 顺序和相位已经固定，不靠
一个未定的 Weil-pairing 符号。

仍按 R1017 定义
\[
\delta_0^-=R_-,\quad \delta_\nu^-=\tau_Q^\nu R_-,
\qquad
\delta_0^+=U,\quad \delta_\nu^+=\tau_Q^\nu U.
\]
由其实际 eigenspaces 与 (1020.13)，基尺度准确为
\[
k_-=\frac{3t^2}{2},\qquad k_+=\frac{t^2}{12},
\]
\[
\begin{aligned}
\delta_1^-&=k_-(F-G/r),&
\delta_{-1}^-&=k_-(F+G/r),\\
\delta_1^+&=k_+(R_+-6Y_6/r),&
\delta_{-1}^+&=k_+(R_++6Y_6/r).
\end{aligned}
\tag{1020.15}
\]
这两个常数不需要新的高阶计算。例如
\(\ell(z)^2\sigma(z)^6=1+O(z)\)，而
\(D(x^3-4)(Q)=-6rt^2\)，故 \(\delta_1^-\) 的首项为
\(-rt^2z/2\)，给 \(k_-\)；\(\delta_1^+(0)=t^2/12\)
给 \(k_+\)。两相反标签共用一个尺度由 canonical 对称性保证。

置
\[
A_0=\begin{pmatrix}a&-b\\b&a\end{pmatrix},
\quad A_1=\begin{pmatrix}a'&b'\\b'&-a'\end{pmatrix},
\quad S=A_0^{\mathsf T}A_1
 =\begin{pmatrix}d&e\\e&-d\end{pmatrix},
\]
\[
d=aa'+bb',\qquad e=ab'-ba'.
\tag{1020.16}
\]
由 \([s]Q=-P\)，原 \(A\) 把 \(Q\)-坐标向量 \(\nu\) 送到
\(P\)-坐标 \(-A_1\nu\)、\(Q\)-坐标 \(A_0\nu\)。
对任意坐标 \(z,y\in\mathbf F_3^2\)，其 canonical Weyl lift 为
\[
W(z,y)=\zeta^{-z^{\mathsf T}y/2}R^z\tau_Q^y.
\tag{1020.17}
\]
这式由 (1020.14) 与 inversion 条件直接确定，所有 \(1/2\)
在 \(\mathbf F_3\) 解释。

记
\[
\Delta_\nu^-=(\delta_{\nu_1}^-)^p
 \boxtimes(\delta_{\nu_2}^-)^p,\qquad
\Delta_y^+=\delta_{y_1}^+\boxtimes\delta_{y_2}^+.
\]
R1017 已逐项核定原 Frobenius 标签运输为 \(y=A_0\nu\)：
\(A_0^{\mathsf T}y=p\nu=-\nu\)，而
\(A_0^{\mathsf T}A_0=-I\)。现在 (1020.12)、(1020.17)
进一步给准确 scalar
\[
\boxed{\quad
\mathcal K_{A,6}\Delta_\nu^-
 =d_0\,\zeta^{-\nu^{\mathsf T}S\nu/2}\Delta_{A_0\nu}^+,
\qquad d_0=-36c_A.
\quad}
\tag{1020.18}
\]
确实，\(W(z,y)\Delta_0^+=\zeta^{z^{\mathsf T}y/2}\Delta_y^+\)，
代 \(z=-A_1\nu,y=A_0\nu\) 即得所示相位。
canonical 奇阶 lifts 的唯一性排除了另加 affine character。

## 5. 四个原角点的完整求和

把 (1020.15) 写成
\[
F=A_F(\delta_1^-+\delta_{-1}^-),\quad
G=B_G(\delta_{-1}^--\delta_1^-),\quad
Y_6=D_Y(\delta_{-1}^+-\delta_1^+),
\]
\[
A_F=\frac1{3t^2},\qquad B_G=\frac r{3t^2},\qquad D_Y=\frac r{t^2}.
\tag{1020.19}
\]
原 \(F^p\boxtimes G^p\) 在四个
\(\nu_1,\nu_2\in\{1,-1\}\) 上的系数是
\(-\nu_2 A_F^p B_G^p\)。在这些角点上，
\[
-\nu^{\mathsf T}S\nu/2=-e\nu_1\nu_2.
\]
故所有四项和相位都可显式保留。

在目标第二轴 \((0,y_2)\) 上，
\(\nu_1=-b y_2,\ \nu_2=-a y_2\)，相位为
\(\zeta^{-eab}\)，源符号为 \(a y_2\)。
在目标第一轴 \((y_1,0)\) 上，
\(\nu_1=-a y_1,\ \nu_2=b y_1\)，相位为
\(\zeta^{eab}\)，源符号为 \(-b y_1\)。
用 (1020.19) 换回 \(U,Y_6\)，得到两个系数
\[
-\Lambda a\zeta^{-eab}c_A,\qquad
 \Lambda b\zeta^{eab}c_A,\qquad
\Lambda=\frac{-36A_F^pB_G^p}{D_Y}.
\]
\(t\in\mathbf F_p\)、\(r^p=\epsilon r\) 与 \(t^3=4\) 准确给
\[
\Lambda=-\frac{4\epsilon}{t^2}=-\epsilon t.
\tag{1020.20}
\]
再令 \(d'=aa'-bb'\)。由
\(eab=-d'\)、\(\chi=ab\zeta^{-d'}\)，两个系数就是
\[
\epsilon t a\chi^2c_A,\qquad -\epsilon t a\chi c_A.
\]
这证明 (1020.3)，包括其共同 scalar 与两个符号。

## 6. 原第五阶读数及十二表示的不变性

在原整 frame，
\(U=z^2+O(z^8)\)、\(Y_6=-z^3+O(z^9)\)。
令 \(q_A=\epsilon t a\chi c_A\)，则 (1020.3) 的首齐次项为
\[
P_A(u,v)=-q_A u^2v^2(\chi v-u).
\]
R1017 的同一个实际第五阶 jet 给
\[
\frac{(6B)^5}{12}\gamma^{-2}H_p(\eta)
 =10\beta^2\overline\alpha^{\,3}P_A(\kappa,1).
\]
将 \(c_A=-\gamma^{-2}\mathcal C_N(\eta)\) 代入，并用
\[
\beta^2\kappa^2\overline\alpha^{\,3}
 =(N\alpha)^2\overline\alpha,\qquad
\overline\alpha(\chi-\kappa)=\chi\overline\alpha+\overline\beta,
\]
便准确得到 (1020.4)。第二式使用
\(N\alpha+N\beta=0\bmod p\)，没有把整数 norm 等式误写为零。

R1012 的十二表示由
\[
(\alpha,\beta)\longmapsto(u\alpha,\overline u\beta)
\quad(u\in\mu_6),\qquad
(\alpha,\beta)\longmapsto(-\beta,\alpha)
\tag{1020.21}
\]
生成，均保持核方向 \(\gamma\)。
第一种变换下
\[
a\mapsto u^3a,\quad \chi\mapsto u^2\chi,\quad
\chi\overline\alpha+\overline\beta
 \mapsto u(\chi\overline\alpha+\overline\beta),
\]
所以右侧总因子为 \(u^6=1\)。
第二种变换下
\[
a\mapsto-b,\quad\chi\mapsto-\chi^{-1},\quad
N\alpha\mapsto N\beta=-N\alpha\bmod p.
\]
用 \(\chi^3=ab\)，同样保持
\(a\chi(N\alpha)^2(\chi\overline\alpha+\overline\beta)\)。
因此它是原方向上的真正值，不依赖任意选择一个 norm-\(p\) 代表。

此外，\(\chi\) 的 norm 为一、\(\kappa\) 的 norm 为负一，
故 \(\chi-\kappa\ne0\)；式中其余因子亦均为单位。这与
R1016/R1017 的全方向单位定理一致，但本篇保留了它们之间原先
尚未确定的精确比例。

## 7. 保留的原问题与全文核准

这条桥允许后续在原方向函数上保留共同
\(\mathcal C_N(\eta)\)、实际三挠角色 \(\chi\) 与 norm 权重，
再处理 Fourier/primitive/Legendre 筛选。
目前尚未证明同一个原保留标签
\[
h=6i+7,\quad (h,p+1)=1,\quad
P_{h-1}(1/s)f_i g_{N-1-i}\ne0.
\]
不能因 (1020.4) 的每个值非零，就断言它的这些指定 Fourier
坐标非零。R1016 §7.2 的 Gaussian 精确值仍只在已证方向使用；
后继 [R1022](R1022-original-theta-all-direction-constant-square.md) 已证明
全方向常平方，5mod12 行常数为一；实际方向上的正负号继续保留。
原 O2 的 bare \(A_r+BT_r\)、全局对数和 O0 覆盖继续开放。
**Serre 主目标仍 OPEN。**

依赖：

- [R1016](R1016-original-small-index-theta-and-complete-convolution-units.md)：
  实际 index-two 下降、原 \(\mathcal C_N\)、共同 \(c_A\) 与 norm-three sigma 式。
- [R1017](R1017-original-tame-two-three-phases-and-every-direction-critical-unit.md)：
  实际二、三-primary 运输、canonical lifts、原第五阶 jet。
- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)：
  每核方向的十二个原 norm-\(p\) 表示。
- [R812](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md) §6：
  同一原三挠点 \(Q=(t,-r)\) 及 Miller 乘数的准确常数。
- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md)：
  原参数、实际 \(\Theta_{p,m}=-mB Q_m\) 与有限整 jet 范围。

o1_theta 与 root 分别纸审了二-primary 列矩阵的复合次序、
\(\delta\epsilon=-1\)、两个 CM residue 单位乘积、
norm-three 的实际 rigidification 与 \(\Omega\) 负号、
\([s]Q=-P\)、Weyl 的 \(1/2\) 相位、四点完整求和、
\(\Lambda=-\epsilon t\)、第五阶常数120及十二表示不变性。
无数学程序执行，无有限扫描或旧窗口重跑。
