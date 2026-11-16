# R847 — 原二处的完整 \(S_3\) 作用与实际曲线像的亏格七下界

日期：2026-11-16。**状态：下述实际态射、群作用及亏格下界已证明。**

本篇继续 R841 附录 B 的同一份原端点表达，并使用 R846 已付的属四排除。
新增结论是：该表达中任何生成整个 \(E_0^3\) 的实际曲线像，其正规化的亏格至少为七。
证明直接使用原 \(S\)、partial \(W_4\) 及三阶 \(R\) 的完整曲线作用；
不增加算术中央零，不更换原 \(q/q^4\)，也不由下界推断原最高 Chow 类为零。

## 1. 同一原 Hom 表达

沿
[R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)
附录 A、B，固定
$$
K=\mathbf Q(\omega),\qquad
M=2601,\qquad N=4M=10404,
$$
$$
X=X_0(N),\qquad C=X_0(M),\qquad A=E_0^3.
$$
\(E_0\) 上的 \([\omega]\) 规范为
\([\omega]^*\omega_{E_0}=\omega\,\omega_{E_0}\)。

原三个有序 CM 来源、全部 Galois–Artin 系数以及完整权一对应，
经 R841 的实际 Hom 平均与对称 polarization 后，给同一原最高类的有限表达
$$
\widetilde Z
 =\sum_\alpha c_\alpha\,
   \Pi\,(\Phi_\alpha)_*[X],
\qquad
\Phi_\alpha=(F_\alpha,a_\alpha q_0,a_\alpha q_2).
\tag{1}
$$
这里
$$
q_0(z)=z,\qquad q_2(z)=4z,\qquad
\deg q_0=\deg q_2=6,
$$
\(F_\alpha\) 通过原有理新形式
\(f=\theta(\psi_{17})\) 的完整权一因子；
\(a_\alpha\) 通过原
\(g_4,g_{10},g_{16}\) 的完整有理 Hecke packet。
所有态射以原 cusp \(\infty\) 为零点，且
$$
\Phi_\alpha R_N=[\omega]^{\times3}\Phi_\alpha,
\qquad R_N(z)=z+\tfrac13.
\tag{2}
$$
系数 \(c_\alpha\) 继续保留原两个 \(\Gamma\) 因子的交叉项；
不要求每个单项已经单独具有指定的 \(\lambda_\nu\) 角色。

以下固定一个 \(\Phi=(F,aq_0,aq_2)\)。
令 \(D\) 为其像的正规化，
$$
X\xrightarrow{\vartheta}D\xrightarrow{\iota}A.
\tag{3}
$$
真实推前次数仍是
\(\Phi_*[X]=\deg(\vartheta)\,\iota_*[D]\)。
若像位于真阿贝尔子簇的平移中，
R839 的原最高投影已经消去该项。
本篇只讨论像生成整个 \(A\) 的情形。

## 2. 原两个二阶自同构与 \(W_4\) 的常值项

取原有理矩阵
$$
s=\begin{pmatrix}1&1/2\\0&1\end{pmatrix},
\qquad
\mathcal W=
\begin{pmatrix}4&-1\\4M&1-M\end{pmatrix}.
\tag{4}
$$
它们在 \(X\) 上分别给
\(S:z\mapsto z+1/2\) 和 R831 的 partial \(w_4\)。
二者均定义于 \(\mathbf Q\)，且
$$
S^2=w_4^2=1.
\tag{5}
$$
R841 已在原整个有理 packet 上证明
$$
FS=-F,\qquad aq_0S=-aq_0-aq_2,\qquad aq_2S=aq_2.
\tag{6}
$$
其中 \(q_2^*\omega_g=4g(Q^4)dQ/Q\) 的真实倍率已计入；
不能把它改成裸 \(g(Q^4)dQ/Q\)。

R831 的实际退化恒等式与新向量绝对符号为
$$
q_0w_4=q_2,\qquad q_2w_4=q_0,\qquad
e_f(w_4)_*=-e_f.
\tag{7}
$$
最后一式先给 \(Fw_4=-F+\text{常值}\)。
这里必须准确消去常值，不能只引用有理 Chow 系数下的 cusp torsion。

令 \(E_f/\mathbf Q\) 为原 \(f\) 的 optimal elliptic quotient，
\(\varphi_f:X\to E_f\) 仍以 \(\infty\) 为零点。
因为 \(F\) 的完整 Jacobian 同态只经原 \(f\)-isotypic 因子，
它在 \(\ker(J(X)\to E_f)^0\) 上的微分为零，
故在这个连通阿贝尔子簇上为零。
因此每个实际 \(F\) 都因子化为
$$
F=\lambda_f\varphi_f
\tag{8}
$$
，其中 \(\lambda_f:E_f\to E_0\) 是原固定有限定义域上的真实同态。
这一步不把清分母后的任意 Hom 误认成某个预选有理商的整数倍。

\(E_f\) 与 \(E_{17}:y^2=x^3+17\) 在 \(\mathbf Q\) 上同源。
在良好位 \(5,7\) 上，直接计数为
$$
\#E_{17}(\mathbf F_5)=6,\qquad
\#E_{17}(\mathbf F_7)=13.
\tag{9}
$$
第一式中 \(x=2,3,4\) 分别给 \(1,2,2\) 个仿射点；
第二式中六个非零 \(x\) 各给两个仿射点，\(x=0\) 不给点；
两式均另加无穷远点。
同源曲线 \(E_f\) 在两位同样良好且点数相同。
良好约化对素于剩余特征的 torsion 单射，
而 \(6,13\) 互素；对 \(5\)-或 \(7\)-primary torsion 使用另一位。
所以
$$
E_f(\mathbf Q)_{\rm tors}=0.
\tag{10}
$$

实际 \(w_4\infty=1/M\) 是 \(\mathbf Q\)-有理 cusp：
其 cusp 定义域由
\(\gcd(M,N/M)=\gcd(M,4)=1\) 给出。
Manin–Drinfeld 使
\(\varphi_f(w_4\infty)\) 为有理 torsion，故由(10)恰为零。
结合(8)，原常值 \(F(w_4\infty)\) 准确为零。
因此
$$
\boxed{
\Phi S=L\Phi,\qquad
\Phi w_4=W\Phi,
}
\tag{11}
$$
其中
$$
L=
\begin{pmatrix}
-1&0&0\\
0&-1&-1\\
0&0&1
\end{pmatrix},
\qquad
W=
\begin{pmatrix}
-1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}.
\tag{12}
$$
这是真实曲线映射等式，无剩余平移、有限阶修正或未定常数。
后两坐标的常值也由(7)及 \(q_i(\infty)=\infty\) 逐式为零。

## 3. 原层级上的完整 \(S_3\)，及其与 \(R\) 的交换

为不只在目标矩阵上检查关系，先核原源。
置 \(B=s\mathcal W\)。有
$$
B=
\begin{pmatrix}
4+2M&-(M+1)/2\\
4M&1-M
\end{pmatrix},
\qquad
\det B=4,\quad \operatorname{tr}B=M+5.
$$
Cayley–Hamilton 给
$$
\boxed{
\frac{B^3}{8}
=
\frac{(M+3)(M+7)}8\,B-\frac{M+5}{2}I
\in\Gamma_0(4M).
}
\tag{13}
$$
确因 \(M\equiv1\bmod4\)，右侧两系数均为整数；
下左项被 \(4M\) 整除，行列式为1。
中心标量 \(8\) 不改变 Möbius 作用，
因此原 \(X\) 上
$$
(Sw_4)^3=1.
\tag{14}
$$

再令 \(r=\left(\begin{smallmatrix}1&1/3\\0&1\end{smallmatrix}\right)\)。
\(r\) 与 \(s\) 直接交换；同时
$$
\boxed{
r\mathcal W r^{-1}\mathcal W^{-1}
=
\begin{pmatrix}
1+4M/3+4M^2/9&-1-4M/9\\
4M^2/3&1-4M/3
\end{pmatrix}
\in\Gamma_0(4M).
}
\tag{15}
$$
这里使用原 \(9\mid M\)；
下左项除以 \(4M\) 后为整数 \(M/3\)。
故
$$
R_NS=SR_N,\qquad R_Nw_4=w_4R_N
\quad\text{于 }X.
\tag{16}
$$
没有添加层级、ray 或新的 normalizer。

目标矩阵满足
$$
L^2=W^2=I,\qquad
LW=
\begin{pmatrix}
1&0&0\\
0&-1&-1\\
0&1&0
\end{pmatrix},
\qquad (LW)^3=I,
\tag{17}
$$
并给忠实的 \(S_3\) 表示：
第一坐标为 sign，后两坐标为标准二维表示。
式(13)–(17)遂同时支付源关系与目标关系。

由(11)，这些作用保持原像并唯一提升到正规化 \(D\)。
由于像生成整个 \(A\)，若一个目标群元素在原像上逐点恒等，
它在该像所生成的阿贝尔簇上也恒等。
故所诱导的
$$
G=\langle S_D,(w_4)_D\rangle\simeq S_3
\tag{18}
$$
在 \(D\) 上忠实。
(2)同样给阶准确为3的 \(v\in\operatorname{Aut}(D)\)，
它与 \(G\) 交换。
于是这份原实际来源保一个忠实的 \(C_3\times S_3\) 作用，
而不仅保某个微分空间的三个矩阵。

## 4. \(S_3\) 在原三阶商上仍然忠实

令
$$
B_0=D/\langle v\rangle,\qquad g_0=g(B_0).
\tag{19}
$$
这里 \(B_0\) 仅表示本篇的商曲线，与旧六变量分布符号无关。
因 \(G\) 与 \(v\) 交换，它作用于 \(B_0\)。

这个作用的核落在函数域覆盖
\(K(D)/K(B_0)\) 的完整 deck 群 \(\langle v\rangle\) 中。
但该群与 \(G\) 交换，
所以核也落在 \(Z(G)\) 中；
\(Z(S_3)=1\)。因此
$$
\boxed{G\longrightarrow\operatorname{Aut}(B_0)\text{ 单射}.}
\tag{20}
$$

每个分支点的局部 monodromy 是 \(v\) 或 \(v^2\)。
记这两种点的数目为 \(r_1,r_2\)。
由于这里是与 \(v\) **交换**的作用，两个分支除子分别由
\(G\) 保持，不能将它们互换。
这一点会使下面的轨道计数强于只控制总分支数。

## 5. 亏格五、六的全部可能分支数据

原 \(\iota:D\to A\) 生成整个三维 \(A\)，
故其 Jacobian 满同态使微分拉回单射。
由(2)，
$$
d_\omega:=\dim H^0(D,\Omega^1)_\omega\ge3.
\tag{21}
$$
R841 附录 A 已从实际循环覆盖线丛给出
$$
g(D)=3g_0-2+r_1+r_2,
\tag{22}
$$
$$
d_\omega=g_0-1+\frac{2r_1+r_2}{3},
\qquad
d_{\omega^2}=g_0-1+\frac{r_1+2r_2}{3}.
\tag{23}
$$
以下 \(g=5,6\) 的所有候选均有分支；
相应正次数线丛的 \(H^1\) 为零，
所以(23)没有遗漏一个未分歧 degree-zero 扭曲修正。

结合(21)–(23)，完整候选表为

| \(g(D)\) | \(g_0\) | \((r_1,r_2)\) | \((d_1,d_\omega,d_{\omega^2})\) |
|---|---:|---:|---:|
| \(5\) | \(0\) | \((5,2)\) | \((0,3,2)\) |
| \(6\) | \(0\) | \((4,4)\) | \((0,3,3)\) |
| \(6\) | \(0\) | \((7,1)\) | \((0,4,2)\) |
| \(6\) | \(1\) | \((4,1)\) | \((1,3,2)\) |

逐项说明如下。
当 \(g=5\) 时，\(r_1+r_2=7-3g_0\)；
若 \(g_0\ge1\)，(23)给 \(d_\omega<3\)。
故 \(g_0=0\)，再由整性与(21)得到唯一 \((5,2)\)。
当 \(g=6\) 时，总数为 \(8-3g_0\)；
\(g_0\ge2\) 同样被(21)排除。
\(g_0=0\) 的整性只留 \((4,4),(7,1)\)，
\(g_0=1\) 只留 \((4,1)\)。
这份表未假设 \(J(D)\) 的其余因子仍为 CM，
也未使用原层级的任何未枚举新形式。

## 6. 有理商上的唯一二点轨道排除前三种候选

在代数闭包上，忠实 \(S_3\subset\operatorname{Aut}(\mathbf P^1)\)
可自含规范为
$$
c:x\longmapsto\omega x,\qquad
t:x\longmapsto1/x.
\tag{24}
$$
证明是先令阶3元素的两个固定点为 \(0,\infty\)；
共轭它到其逆的二阶元素必须交换这两点，因而为 \(a/x\)，
再缩放坐标消去非零 \(a\)。

所以恰有一个大小2的轨道 \(\{0,\infty\}\)，
两个大小3的轨道
$$
\{1,\omega,\omega^2\},\qquad
\{-1,-\omega,-\omega^2\},
$$
其余轨道全为大小6。
特别，没有单点轨道；
任何大小4的 \(G\)-不变约化点集都不存在；
任何大小5的不变约化点集必须包含那个唯一大小2轨道。

现分别应用于本篇两个互不相交的 monodromy 分支除子：

- \((r_1,r_2)=(5,2)\)：大小5除子和大小2除子都须包含唯一二点轨道，违反不相交。
- \((r_1,r_2)=(4,4)\)：连单个大小4的不变约化除子都不存在。
- \((r_1,r_2)=(7,1)\)：大小1除子不存在。

因此全部 \(g_0=0\) 候选均被同一个实际 \(S_3\) 作用排除。
为计数而在代数闭包上选择(24)，不改变原 \(\Phi\) 的定义域、
Artin 系数或原 Chow 表达。

## 7. 椭圆商上的三阶平移排除最后一种候选

最后设 \(g_0=1\)。
在代数闭包上选择 \(B_0\) 的任一点作原点，
有
$$
1\longrightarrow B_0
\longrightarrow\operatorname{Aut}(B_0)
\longrightarrow\operatorname{Aut}(B_0,0)
\longrightarrow1.
\tag{25}
$$
特征零中右端是循环群。
因此忠实 \(S_3\) 的交换子群 \(A_3\) 在右端像为1，
必须作用为平移。
由(20)，其非恒等元素是非零三阶点的平移，
所以在椭圆曲线上无固定点。

故任何 \(G\)-不变有限约化点集都是自由 \(A_3\) 轨道的并，
其大小被3整除。
然而第5节最后一种候选总分支数为5，
甚至两种分支数分别为4与1，均不满足这一要求。
得到矛盾。
这里没有把带非平凡线性部分的某个 order-three 椭圆自同构
误认为平移；正是 \(A_3=[S_3,S_3]\) 及循环商(25)
强制了平移性质。

## 8. 原端点的实际结论及保留范围

R841 已排除所有生成项的亏格小于四；
[R846](R846-original-full-hom-and-genus-four-exclusion.md)
在原全部 Hom 与真实定义域上排除属四。
本篇第5–7节再排除属五、属六。
因此对(1)中的每个实际生成项有
$$
\boxed{g(D)\ge7.}
\tag{26}
$$

这是原 polarization 后的**同一份有限曲线表达**的结论。
没有替换 \(F\)、\(a\)、\(q_0\)、\(q_2\)，没有删掉全部
Galois–Artin 系数，也没有增加一个额外平均因子。
在(1)中，原 \(1/3\) 的 Hom 平均、\(1/2\) 的 polarization
和原有限推前次数都照旧保留。

全部源群作用先在真实 \(X_0\) 曲线上证明。
返回 R831 的 old 副本仍是 \(6^{-2}\) 的原拉回；
返回 \(X_1\) 仍保
$$
D_X=1632,\qquad D_C=816,\qquad
A_*Z_{02}^{(1)}=D_XZ_{02},\qquad
Z_{02}^{(1)}=D_C^{-2}A^*Z_{02},
$$
以及原单副本的 \(12^{-2}\)。
本篇不声称 \(s\) 或 \(\mathcal W\) 直接正规化所有原
\(\Gamma_1\) 层级；一切按这些既有真实遗忘映射运输。

(26)不排除亏格至少七的实际来源，不证明其中存在非零项，
也不证明原指定线性组合、其临界 Abel–Jacobi 值或 R814
canonical 特殊化之间的非零比例。
原三条中央同时零的主缺口仍在。
本篇无新增数值计算或目标素数扫描；(9)是显示的有限手算，
全部群、轨道与亏格论证均为符号证明。

## 9. 依据

- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原 partial \(W_4\)、\(q_a w_4=q_{2-a}\)、第一新向量的绝对负号、
  完整共同目标及 \(X_0/X_1\) 次数。
- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  原整个 Hom 的 \(R\)-等变平均、同 \(a\) 的实际 polarization、
  \(S\) 的完整微分和态射作用、循环覆盖维数式。
- [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原最高投影、实际有限曲线表达及真阿贝尔子簇平移项的消失。
- [R846](R846-original-full-hom-and-genus-four-exclusion.md)：
  原完整 Hom 与 Galois 角色给出的实际属四排除。
- [R829](R829-same-degeneracy-diagonal-chow-vanishing.md)：
  原 modular cusps 上的 Manin–Drinfeld 与真实 CK 相容。
  本篇第2节另用(9)–(10)消去曲线映射的实际常值，
  因而没有把仅有理 Chow 意义的 torsion 零误当成点恒等式。
