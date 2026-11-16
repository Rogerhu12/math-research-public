# R852 — 原 Schoen 对应的精确九倍自复合与 Chow 逆

日期：2026-11-16。**状态：以下对应恒等式、目标幂等元、双向 Chow 同构及原循环的逆运输已证明。**

本篇使用 R850–R851 的同一个原模型、完整图形对应及最高投影。
新结论是精确的
$$
{}^t\Gamma\circ\Gamma=9\Pi,\qquad
\Gamma^{-1}=\frac19\,{}^t\Gamma
$$
（逆的目标为下文实际构造的直和因子）。
证明先在 Chow 范畴中支付两个 CM 因子的可逆性，再用一个明确的三阶自同构排掉交叉块；
最后才以原微分读取两个已经知道是标量的对角块。
因此没有把“Betti 秩一”当成任意 Chow 对应的标量性，
也不需要一个未确定的幂零修正。

## 1. 原对应与完整图形约定

保持
$$
E_0:Y^2=X^3+1,\qquad
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\qquad A=E_0^3,
$$
$$
\Omega_A=\bigwedge_{i=1}^3\frac{dX_i}{2Y_i}.
\tag{1}
$$
令 $\Pi$ 为 R839、R850 的原最高 Chow 投影。
先在含 $K$ 的固定系数域 $\mathcal E$ 上证明；所有最终合并的对应均可在有理系数上定义。

R850 的两个实际态射及对应为
$$
b:\widetilde A\to A,\qquad q:\widetilde A\to Z,\qquad
\alpha=q_*b^*\Pi,\qquad \beta=\frac13\Pi b_*q^*.
$$
准确有
$$
\beta\alpha=\Pi,\qquad \alpha\beta=\Pi_Z,\qquad
{}^t\alpha=3\beta,\qquad q^*\Omega_Z=b^*\Omega_A.
\tag{2}
$$
这里 $\widetilde A$ 仅指 R850 对27点的吹起。

在 R851 允许的光滑射影解消中，固定第3节的等变选择 $W_9$。
对同一有理映射 $\mathcal F_Z:Z\dashrightarrow W_9$ 取完整图形解消
$$
b_9:T_9\longrightarrow Z,\qquad f_9:T_9\longrightarrow W_9,\qquad
\mathscr G=f_{9,*}b_9^*.
$$
$b_9$ 双有理，$f_9$ 的泛型次数为3。定义
$$
\boxed{\Gamma=\mathscr G\alpha\in CH^3(A\times W_9)_{\mathbf Q}.}
\tag{3}
$$
因而 $\Gamma=\Gamma\Pi$，$\,{}^t\Gamma=\Pi\,{}^t\Gamma$。
式(3)正是 R851 运输原循环的对应，不以一个只在开集上定义的图形替代它。
$b_9^*$、$\Pi_Z$、原曲线的异常交数和所有有限系数始终保留。
本文的 $T_9$ 也不与 R850 的 $\widetilde A$ 混用。

对应按循环推前方向组合；对于对应 $C$，
写 $C_*$ 表示其对循环或上同调的作用，写 $C^*=({}^tC)_*$
表示 Abel–Jacobi 对偶中的反向作用。此约定用于第5–7节的倍率。

## 2. 两个原最高 CM 因子确为可逆 Chow 线

令 $\mathbf L=\mathbf1(-1)=h^2(E_0)$。
在 $K$ 上取 $[\omega]^*$ 的两个实际 Chow 特征幂等元，写
$$
h^1(E_0)_{\mathcal E}=C_+\oplus C_-,\qquad
[\omega]^*|C_+=\omega,\quad [\omega]^*|C_-=\omega^2.
\tag{4}
$$
这些幂等元来自 $h^1$ 上的严格关系
$[\omega]^{*2}+[\omega]^*+1=0$；不是先在实现中分解后假定可提升。

使用阿贝尔 Chow 动机的标准代数结构：
乘法给自然同构
$$
\operatorname{Sym}^2 h^1(E_0)\ \xrightarrow{\ \sim\ }\ h^2(E_0)=\mathbf L.
\tag{5}
$$
这里 $\operatorname{Sym}$ 使用未改变交换约束的 Chow 范畴；
实现函子的目标是带 Koszul 符号的分次向量空间，因此 (5)
实现为通常的 $\bigwedge^2H^1$。
该同构是有理等价意义的同构，见 Künnemann 的阿贝尔动机定理，
以及 Vial 作者稿 Theorem 3、Appendix A.3 式(24)；
后者还给出逆为相应分量上的
$\frac1{2!}\Sigma_2^*$，$\Sigma_2:E_0^2\to E_0$ 为和映射。

把 (4) 代入 (5)，在 Chow 范畴内得到直和
$$
\operatorname{Sym}^2 C_+
\ \oplus\ (C_+\otimes C_-)
\ \oplus\ \operatorname{Sym}^2 C_-
\ \simeq\ \mathbf L.
\tag{6}
$$
$[\omega]^*$ 在左侧三个因子上的特征依次为
$\omega^2,1,\omega$，而在 $\mathbf L$ 上为 $\deg[\omega]=1$。
(5) 由对角乘法及和映射构成，严格与 $[\omega]$ 交换。
所以限制到各特征幂等元，准确有
$$
\boxed{
\operatorname{Sym}^2 C_\pm=0,\qquad C_+\otimes C_-\simeq\mathbf L.
}
\tag{7}
$$
第二个同构的逆就是 (5) 的逆限制到特征1部分；它已在 Chow 范畴中给出。
因此
$$
C_+^{-1}=C_-\,\mathbf L^{-1},\qquad C_-^{-1}=C_+\,\mathbf L^{-1}.
\tag{8}
$$
这也与椭圆 Poincaré 对偶
$C_\pm^\vee\simeq C_\mp\mathbf L^{-1}$ 相同。
(7) 说明两者是 Kimura 意义的奇线；(8) 支付的是实际张量逆，
并不只报告它们的实现维数。

置
$$
M_+=C_+^{\otimes3},\qquad M_-=C_-^{\otimes3}.
$$
于是
$$
(A,\Pi)_{\mathcal E}=M_+\oplus M_-,\qquad
M_\pm^{-1}=M_\mp\mathbf L^{-3}.
\tag{9}
$$
张量逆使张量 $M_\pm$ 成为范畴自等价。因此对原基域及其任意固定扩域，
$$
\boxed{\operatorname{End}(M_\pm)
\simeq\operatorname{End}(\mathbf1)=\mathcal E.}
\tag{10}
$$
这正是后文能够从两个标量实现确定对应的理由。
没有声称任意高余维 Chow 对应的实现都忠实；
也不需要预先确定 $\operatorname{Hom}(M_+,M_-)$。

椭圆极化把两 CM 投影的转置互换，故
$$
{}^t\Pi=\Pi.
\tag{11}
$$
式(2)–(3)因而是自对偶的同一最高因子规范。

## 3. 原显式映射的三阶等变性及等变解消

令
$$
u=([\omega],1,1):A\longrightarrow A.
\tag{12}
$$
它与 R850 的对角三阶作用交换，保持27点中心，
故提升到 $\widetilde A$ 并下降为 $u_Z$。

使用 R851 完全固定的目标坐标
$$
x=r_0/r_2,\quad y=r_1/r_2,\quad r=s_0/s_2,\quad s=s_1/s_2,
$$
$$
P=(x^2+xy^2+y)rs-(r^2+rs^2+s)xy.
$$
在这个双三次模型上定义
$$
\sigma(x,y,r,s)=(\omega x,\omega^2y,\omega r,\omega^2s).
\tag{13}
$$
这来自两份 $\mathbf P^2$ 上的同一个对角矩阵
$\operatorname{diag}(\omega,\omega^2,1)$，所以是全射影模型上的自同构。
直接代入得 $P\circ\sigma=\omega^2P$；共同底参数满足
$$
\tau\circ\sigma=\omega^2\tau,\qquad \tau=x/y+y+1/x.
\tag{14}
$$

R851 映射使用
$$
a_i=(Y_i+1)/2,\quad b_i=(Y_i-1)/2,\quad T=X_1X_2X_3/4,
$$
$$
(x,y,r,s)=
\left(-T/b_1,-a_1a_3b_2/T,-T/b_2,-T^2/(a_1b_2b_3)\right).
$$
$u$ 固定全部 $a_i,b_i$，使 $T\mapsto\omega T$。
因而逐项准确有
$$
\mathcal F_0u=\sigma\mathcal F_0,\qquad
\mathcal F_Zu_Z=\sigma\mathcal F_Z.
\tag{15}
$$

选用特征零函子性解消及主化，使 $W_9$ 和 $T_9$ 上的作用都正则。
具体可先对原射影双三次作函子性解消，再对完整图形作同样解消；
所有吹起中心在自同构下稳定，且吹起保持射影性。
Bierstone–Milman–Temkin 的 Theorem 1.1、1.3 及其对域扩张的相容性
保证此选择同时与 $K/\mathbf Q$ 下降相容。
$\sigma$ 的生成元虽在 $K$ 上写出，其 $\mu_3$ 群概形和原模型在
$\mathbf Q$ 上定义，所以这些解消及合并对应可在 $\mathbf Q$ 上取。
此处仅固定 R851 已允许的解消选择，未删去任何图形异常项。

由等变的实际推拉，(15)提升为完整 Chow 对应恒等式
$$
\boxed{\Gamma u^*=\sigma^*\Gamma.}
\tag{16}
$$
对转置使用自同构拉回与推前互逆，再把三阶生成元取逆，得到
$$
{}^t\Gamma\,\sigma^*=u^*\,{}^t\Gamma.
\tag{17}
$$
因此
$$
Q:={}^t\Gamma\Gamma=\Pi Q\Pi,\qquad Qu^*=u^*Q.
\tag{18}
$$

## 4. 交叉块在 Chow 中严格为零

在 (9) 的两个因子上，$u^*$ 只作用第一份 CM 线，
所以其特征准确为 $\omega,\omega^2$，不是二者的三次幂。
把 (18) 写成两个因子的矩阵。
对任意交叉块 $Q_{+-}$ 或 $Q_{-+}$，
交换关系给出
$$
(\omega-\omega^2)Q_{+-}=0,\qquad
(\omega-\omega^2)Q_{-+}=0.
$$
系数域中特征零，故两块严格为零。
结合 (10)，存在唯一 $a_+,a_-\in\mathcal E$ 使
$$
Q=a_+\,1_{M_+}\oplus a_-\,1_{M_-}.
\tag{19}
$$
到此为止全部都是 Chow 范畴中的推理。
第5节的实现计算只用来读 (19) 已知的两个标量。

## 5. 以原 $-18$ 微分倍率确定两个标量

R851 的 residue 规范为
$$
\Omega_W=\frac{dx\wedge dy\wedge dr}{P_s}.
$$
由 (13)，$P_s\circ\sigma=P_s$，所以
$\sigma^*\Omega_W=\omega\Omega_W$，与原最高线一致。

R850–R851 已支付
$$
q^*\Omega_Z=b^*\Omega_A,\qquad
\mathcal F_Z^*\Omega_W=-18\Omega_Z,\qquad \deg f_9=3.
\tag{20}
$$
在图形解消上第二式准确为
$$
f_9^*\Omega_W=-18\,b_9^*\Omega_Z.
$$
推前并用 $f_{9,*}f_9^*=3$，得到
$$
\mathscr G_*\Omega_Z=-\frac16\Omega_W,\qquad
({}^t\mathscr G)_*\Omega_W=-18\Omega_Z.
\tag{21}
$$
双有理 $b_9$ 的推拉无额外次数；形式全纯，因此这里也不把异常部分删成一个未说明的开集计算。

另一方面，(2)给
$$
\alpha_*\Omega_A=3\Omega_Z,\qquad
({}^t\alpha)_*\Omega_Z=\Omega_A.
$$
故 (3) 的完整对应准确满足
$$
\boxed{
\Gamma_*\Omega_A=-\frac12\Omega_W,\qquad
({}^t\Gamma)_*\Omega_W=-18\Omega_A.
}
\tag{22}
$$
两式复合为 $Q_*\Omega_A=9\Omega_A$。
在一个固定复嵌入下，其共轭三微分也同样乘9。
两条分别实现 $M_+,M_-$，所以 (19) 的两个标量均为9。
由此得到有理等价意义的精确恒等式
$$
\boxed{{}^t\Gamma\Gamma=9\Pi.}
\tag{23}
$$
证明先在含 $K$ 的域上进行。两边本来为有理对应，
有限域扩张的限制—核限制及系数标量扩张的单射性把等式降回原域。
没有以 Kimura 幂零定理把一个未知误差悄悄设为零。

## 6. 目标上的实际投影与双向逆

定义
$$
\boxed{
P_9=\frac19\Gamma\,{}^t\Gamma,\qquad
\Lambda=\frac19\,{}^t\Gamma.
}
\tag{24}
$$
由 (23)、$\Gamma\Pi=\Gamma$、$\Pi{}^t\Gamma={}^t\Gamma$，
$$
P_9^2=P_9,\quad {}^tP_9=P_9,\quad
P_9\Gamma=\Gamma,\quad \Lambda P_9=\Lambda,
$$
$$
\boxed{\Lambda\Gamma=\Pi,\qquad \Gamma\Lambda=P_9.}
\tag{25}
$$
于是得到明确的 Chow 动机同构
$$
\boxed{
(A,\Pi)\ \underset{\frac19{}^t\Gamma}{\stackrel{\Gamma}{\rightleftarrows}}\
(W_9,P_9).
}
\tag{26}
$$
也可完全用 R850–R851 的原对应写
$$
P_9=\frac13\,\mathscr G\Pi_Z\,{}^t\mathscr G,
\tag{27}
$$
因为 $\alpha{}^t\alpha=3\Pi_Z$。
这不是任选一个实现相同的目标幂等元；
它是由原完整图形构造出的那个特定幂等元。
不需要声称它与另一解消上预先选定的某个 Chow–Künneth 投影相等。

## 7. 同一原循环、有限角色与 AJ 的精确逆运输

保持 R839、R841、R851 的全部固定 Hom 系数、实际
$q_0(z)=z,q_2(z)=4z$、finite Artin trace 和原端点循环
$\mathcal Z_{\rm orig}=\Pi\mathcal Z_{\rm orig}$。
R851 的定义就是
$$
\mathcal Z_9=\mathscr G\alpha\mathcal Z_{\rm orig}
           =\Gamma\mathcal Z_{\rm orig}.
$$
现在得到反向的实际 Chow 等式
$$
\boxed{
\mathcal Z_{\rm orig}=\frac19\,{}^t\Gamma\,\mathcal Z_9.
}
\tag{28}
$$
因此原端点与其这个指定 Schoen 像在 Chow 群中同时为零或同时非零。
相同结论对各固定有限域及每个原 Artin 幂等元成立：
$\Gamma,\Lambda$ 在 $\mathbf Q$ 上定义，故与循环因子的 Galois 作用交换；
系数保持标量，不另外作半线性共轭。
特别，原三个 $\eta_j$ 的 order18、2/3/17 局部数据没有被 order9 几何商抹去。

原 source quotient 的3仍在 R851 的
$3\sum c_i f_{9,*}b_9^*\Pi_Z\phi_{Z,i,*}[X_0(3468)]$ 中。
(28)不重选原 $6^{-2}$、$12^{-2}$、$D_X=1632,D_C=816$，
也不把 ambient 泛型 degree9 当作某条原曲线的次数。

注意 (22)的推前与 AJ 的反向读数不同。
按第1节的约定，准确为
$$
\Gamma^*\Omega_W=-18\Omega_A,\qquad
\Lambda^*\Omega_A=-\frac1{18}\Omega_W.
\tag{29}
$$
故对 $z=\Pi z$ 及 $y=P_9y$，
$$
\begin{aligned}
\operatorname{AJ}_{W_9}(\Gamma z)(\Omega_W)
 &=-18\,\operatorname{AJ}_{A}(z)(\Omega_A),\\
\operatorname{AJ}_{A}(\Lambda y)(\Omega_A)
 &=-\frac1{18}\operatorname{AJ}_{W_9}(y)(\Omega_W).
\end{aligned}
\tag{30}
$$
使用 R851 的
$\Omega_9^{\rm orig}=-\Omega_W/18$，双向归一读数均为倍率1。
各个适用的 $p$-adic 或复 AJ 函子都遵守这些实际对应等式；
这只对同一个 $p$ 运输其完整投影，不给跨 $p$ 非零定理。

式(26)–(30)支付了 ambient 对应的精确可逆性。
R814 的 canonical 类仍来自其固定非 Dirichlet good pair 与指定 CM cycle；
本文未把该类等同于 $\mathcal Z_9$，未证明原端点或指定 regulator 非零。
同一最高动机可以承载不同的同调平凡类，不能从本篇的逆推出它们成比例。

无新增数值运行、素数扫描或可重算数据。

## 8. 原文依据与所用范围

- [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原最高 Chow 投影与真实 Hom/曲线组合。
- [R850](R850-original-smooth-cubic-quotient-and-exact-top-cycle-transport.md)：
  $\alpha,\beta,\Pi_Z$、严格推拉及原 $\Omega_Z$。
- [R851](R851-original-schoen-map-and-horizontal-cycle-transport.md)：
  固定坐标、degree9/3、$-18$、完整图形及原 Artin 运输。
- K. Künnemann, *On the Chow motive of an abelian scheme*,
  Proc. Sympos. Pure Math. 55, Part 1 (1994), 189–205,
  [DOI](https://doi.org/10.1090/pspum/055.1/1265530)。
  本篇使用其阿贝尔 Chow 动机代数结构；
  已直接读取的完整表述及显式逆见 C. Vial,
  *On the birational motive of hyper-Kähler varieties*,
  J. Math. Pures Appl. 163 (2022), 577–624，
  [作者稿](https://www.math.uni-bielefeld.de/~vial/biratmotiveHK.pdf)
  Theorem 3、Appendix A.3，式(24)及其后的 $\frac1{k!}\Sigma_k^*$。
  这里使用的是有理等价范畴的定理，不是只有数值动机的结构。
- E. Bierstone, P. D. Milman, M. Temkin,
  *Q-universal desingularization*,
  [作者原文](https://math.huji.ac.il/~temkin/papers/Q-universal_Desingularization.pdf)，
  Theorem 1.1、1.3（printed pp.1、3）及 §§5–6。
  所需仅是特征零函子性解消/主化对自同构和域扩张相容；
  因而可保原全 $\mu_3$ 作用及射影图形。
