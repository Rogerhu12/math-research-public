# R827：用一个真实剩余域的两图全局满射认证原导数层终止

日期：2026-11-15。状态：**完整充分条件与源适配证明；尚未得到任何新的模多项式满射、终止层数或原D。**
本篇证明一种正向证书：只要在同一个合法DVR约化中，
两张图上的完整多项式列像都等于原cusp格，就能推出特征零原层已经终止。
它不把一个底点的rank272当作全图满射，也不从预期的低重数填入结果。

本篇接
[R814](R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)、
[R817](R817-original-normal-derivation-without-separate-h-multiplier.md)、
[R820](R820-original-cusp-finite-algebra-and-two-chart-Hermite-ideals.md)、
[R824](R824-original-pole-module-generators-in-weights-five-to-seven.md)与
[R825](R825-original-logarithmic-ratio-and-multiplicity-preimages.md)。
与[R822](R822-original-polar-lattices-certified-by-global-colength.md)的“原特征零包含加全局余长”判据不同，
这里利用整的全球source与proper支撑，把**整个特殊纤维上的满射**提升为原特征零等式。

## 1. 原特征零对象、层与坐标

固定原 $L=\mathbf Q(b,\zeta)$、$s=1+2\zeta$、原 $Y_L$，
以及原无基点铅笔
$$
\tau=e_0,\qquad \sigma=e_1+e_{73},\qquad
z=\sigma/\tau,\quad t=1/z,\qquad N=272.
\tag{827.1}
$$
原正规基与次数为
$$
\beta_{\tau,i}=d_i/\tau^{\epsilon_i},\qquad
\beta_{\sigma,i}=d_i/\sigma^{\epsilon_i},\qquad
\epsilon=(0,1^{144},2^{127}).
\tag{827.2}
$$
同一函数的坐标从第一图变到第二图乘
$$
D(t)=\operatorname{diag}(t^{-\epsilon_i}).
\tag{827.3}
$$
记 $\mathscr E_L=\pi_*\mathcal O_{Y_L}$；
原分裂是 $\mathscr E_L=\bigoplus_i\mathcal O_{\mathbf P^1_L}(-\epsilon_i)$。
“底空间向量丛”与“原正规代数”仍分开使用。

令原 $y=y_{f_4}$、$E=(y)_\infty$，并令
$$
I_0=\mathcal O_Y(-E),\qquad
I_{n+1}=I_n+\delta_v(I_n)\quad\hbox{在 }U_v,\ v=\tau,\sigma.
\tag{827.4}
$$
其中
$$
\delta_\tau=\tau^{-1}D_0,\qquad
\delta_\sigma=t\delta_\tau,\qquad
D_0=(q_Y/82)d/dq_Y.
\tag{827.5}
$$
两图重叠处 $t$ 为单位，R814已经证明(827.4)是完整理想，并且两个定义相容。
记
$$
\mathscr I_n=\pi_*I_n,\qquad
\mathscr C_L=\pi_*\mathcal O_Y(-\mathcal D_{\rm cusp}).
\tag{827.6}
$$
R825的原局部重数公式给
$\mathscr I_n\subseteq\mathscr C_L\subseteq\mathscr E_L$；
本篇不改成含 $P_0$ 的21点除子。

原导子矩阵满足
$$
\operatorname{coord}(\delta_\tau(\beta_\tau v))
=\Gamma_\tau v+G_\tau v',\qquad G_\tau=M_{g,\tau},
\tag{827.7}
$$
而在第二图写
$$
\operatorname{coord}(\delta_\sigma(\beta_\sigma v))
=\Gamma_\sigma v+G_\sigma^{\rm deriv}v',\qquad
G_\sigma^{\rm deriv}=-t^3D(t)G_\tau(1/t)D(t)^{-1}.
\tag{827.8}
$$
R815输出的positive regular g-sigma矩阵要乘(827.8)中的负号。
原weighted界为
$$
\deg(\Gamma_v)_{ij}\le2+\epsilon_j-\epsilon_i,\qquad
\deg(G_v^{\rm deriv})_{ij}\le3+\epsilon_j-\epsilon_i,
\tag{827.9}
$$
第一图的 $G_\tau^{\rm deriv}$ 就是 $G_\tau$。
实际使用的矩阵必须来自同一原R815完成输入，或下文§7.5的新完成单位节点构造。
仅有g/h向量、尚未完成该构造时，不能称这些矩阵已经取得。

## 2. proper支撑引理及为何必须覆盖两个图

**引理827.1。**
设 $A$ 是DVR，分式域 $F$，剩余域 $k$。
设 $X$ 是 $A$ 上proper的Noetherian概形，
$\Phi:\mathscr V\to\mathscr C$ 为有限型拟凝聚层之间的态射。
若 $\Phi_k$ 在整个 $X_k$ 上满射，则 $\Phi$ 在整个 $X$ 上满射。

**证明。**
令 $\mathscr Q=\operatorname{coker}\Phi$，它有限型且支撑闭。
拉回右正合，所以 $\mathscr Q\otimes_Ak=0$。
对每个特殊纤维点 $x$，其有限局部模满足
$\mathscr Q_x/\mathfrak m_A\mathscr Q_x=0$；
$\mathfrak m_A\mathcal O_{X,x}$ 包含于局部环的Jacobson radical，
Nakayama给 $\mathscr Q_x=0$。
因此闭支撑 $Z=\operatorname{Supp}\mathscr Q$ 不遇特殊纤维。

$Z\to\operatorname{Spec}A$ 是proper，像是闭集。
若 $Z$ 非空，其像是 $\operatorname{Spec}A$ 中非空闭集，必含闭点；
这与不遇特殊纤维矛盾。因此 $\mathscr Q=0$。$\square$

这里不要求余商 $\mathscr Q$ 平坦。
本题要求target格平坦，是为了证明所约化的确是原完整C，
并防止用错误特殊纤维替代它，不是为Nakayama另加假设。

不能在单个仿射图直接作同样推论：
$$
A[z]/(\varpi z-1)
\tag{827.10}
$$
的模 $\varpi$ 约化为零，而generic fiber非零。
它的支撑在仿射图上逃向无穷远；在proper闭包中会遇第二图的特殊纤维。
同样，某个 $z_0$ 的非零minor只排除那一个点上的余商，
无法排除其它有限点或无穷远点。
本篇的模证书必须是两个完整多项式模的满射。

## 3. 原C给出的一个可明确核整性的proper目标

取 $A=\mathcal O_{L,\mathfrak p}$，或其完成；
若使用完成，最后用 $L\hookrightarrow\operatorname{Frac}A$ 的忠实域扩张下降。
在 $\mathbf P^1_A$ 上固定
$$
\mathscr E_A=\bigoplus_i\mathcal O(-\epsilon_i).
\tag{827.11}
$$
它的两图过渡仍为原(827.3)，没有换原normal基。

R820的实际两图完整C基是
$$
C_{v,j}=e_j-q_{v,j}(x_v)e_{271}\quad(j<271),\qquad
C_{v,271}=P_v(x_v)e_{271},
\tag{827.12}
$$
其中 $x_\tau=z,x_\sigma=t$，$P_v$ 首一20次，$\deg q_{v,j}<20$。
直接读取实际stage；不重新生成20维cusp代数或其核。
原run为43721747750，source
7890fde180ffabee056de2ce8dd241b189a893a2，
certificate SHA256为
a2e629d05d561e1144e6989612213b33990075400a21f7c1c2f0c2eb825152b4。

下列是可逐源系数检查的充分整性条件：

- 所有 $q_{v,j},P_v$ 的原有理系数属于 $A$；
- $P_\tau(0)$ 与 $P_\sigma(0)$ 是 $A$ 的单位；
- 保留原R820的两图同一cusp字段与完整过渡认证；
  不替换为平方自由部分或新的根。

这些条件已经使(827.12)在两个图定义一个完整的flat目标子丛
$\mathscr C_A\subset\mathscr E_A$，generic fiber为原 $\mathscr C_L$。
下面给出整的拼接理由，避免只在分式域中说“它们相同”。

写 $n=271$，$\epsilon_n=2$。
从原两个C基计算出的坐标过渡
$$
U(t)=C_\sigma(t)^{-1}D(t)C_\tau(1/t)
\tag{827.13}
$$
是下三角：前271个对角为 $t^{-\epsilon_j}$，末对角为
$$
U_{nn}(t)=t^{-2}P_\tau(1/t)/P_\sigma(t).
\tag{827.14}
$$
R820实际最后一条20次first-dependence及20条独立链向量说明，
$P_\tau$ 是原 $\alpha=z(\mathrm{cusp})$ 的20次最小多项式，
$P_\sigma$ 是 $\alpha^{-1}$ 的20次最小多项式。
因此，令 $c=P_\tau(0)\ne0$，
$$
P_\tau(1/t)=c\,t^{-20}P_\sigma(t),\qquad
U_{nn}=c\,t^{-22}.
\tag{827.15}
$$
不是假设 $\alpha$ primitive；此处使用的是原实际20条独立链见证。

第j列的另一个可能非零项为
$$
U_{nj}(t)=
\frac{t^{-\epsilon_j}q_{\sigma,j}(t)-t^{-2}q_{\tau,j}(1/t)}
     {P_\sigma(t)}.
\tag{827.16}
$$
原两图完整C身份先保证它在 $L[t,t^{-1}]$ 内。
分子最低幂至少为 $-21$；$P_\sigma(0)$ 为单位。
把分子乘 $t^{21}$，再对首一 $P_\sigma$ 作多项式除法，
整系数长除法的余数在 $L[t]$ 为零，故在 $A[t]$ 也为零。
所以 $U_{nj}\in A[t,t^{-1}]$。
交换两个图得到相同结论，且(827.15)的 $c$ 是单位，
故 $U^{-1}$ 也在 $A[t,t^{-1}]$。
这就是一个有限可核的整拼接，不要求展开272阶有理逆。

每个图上还有准确同构
$$
A[x_v]^{272}/C_vA[x_v]^{272}\simeq A[x_v]/(P_v).
\tag{827.17}
$$
首一性使右端为自由秩20的A模。
因此 $\mathscr E_A/\mathscr C_A$ 对A平坦，
$\mathscr C_A$ 的两个框架确为原完整C格。
本论证不要求特殊纤维的 $P_v$ 无重根；
即使发生根合并，也必须保留整个首一20次商及重数。

## 4. 从原齐次列构造全球source，不预设导数列自己齐次

取有限多条原截面
$$
B_j\in H^0(Y_L,a_jH-E),\qquad a_j\ge0.
\tag{827.18}
$$
允许使用R824准确认证的272条权5/6生成元，
也允许使用较小但已经准确证明属于(827.18)的集合。
本定理只需要其包含，不先要求它们生成整个 $I_E$。

在两个图写
$$
h_{j,\tau}=B_j/\tau^{a_j},\qquad
h_{j,\sigma}=B_j/\sigma^{a_j},
\qquad
F_{0,\sigma,j}=t^{a_j}D(t)F_{0,\tau,j}(1/t).
\tag{827.19}
$$
假设原两图 $F_0,\Gamma,G^{\rm deriv}$ 的全部系数在同一个A内，
且实际原同次尺度、字段嵌入及原负号均已绑定。

仅在纸面定义准确列
$$
F_{k+1,v,j}
=\Gamma_vF_{k,v,j}+G_v^{\rm deriv}F'_{k,v,j}.
\tag{827.20}
$$
由(827.9)归纳得到
$$
\deg(F_{k,v,j})_i\le a_j+2k-\epsilon_i.
\tag{827.21}
$$
所有系数在A中；普通多项式求导只乘整数，没有除以 $k!$。
因此可直接在剩余域递推(827.20)，其结果就是这些原特征零列的真实约化，
无需先物化巨大的特征零 $F_k$。

导数列本身不满足一个简单的齐次过渡。
为得到全球source，分别对每张图的列按
$d_{j,k}=a_j+2k$ 齐次化：
$$
\widehat F^{\,\tau}_{j,k}:
\quad F_{k,\tau,j}(z)\ \hbox{在第一图},\qquad
t^{d_{j,k}}D(t)F_{k,\tau,j}(1/t)\ \hbox{在第二图}.
\tag{827.22}
$$
它是 $\mathcal O(-d_{j,k})\to\mathscr E_A$ 的态射；
次数界保证第二图没有负幂。
同样定义以 $F_{k,\sigma,j}$ 为起始的
$\widehat F^{\,\sigma}_{j,k}$。

**引理827.2。**
对于 $k\le q$，上述两族在generic fiber的像均包含于 $\mathscr I_q$。

**证明。**
在起始图，$F_{k,v,j}$ 对应 $\delta_v^kh_{j,v}$，
由(827.4)和 $h_{j,v}\in I_0$，它属于 $I_k$。
需要另核延至另一图后的函数，不能只用重叠区包含。

以τ起始为例，在σ图定义
$$
T_k=t^{a_j+2k}\delta_\tau^k(t^{-a_j}h_{j,\sigma}).
$$
$T_0=h_{j,\sigma}\in I_0$。
由于 $\delta_\tau=t^{-1}\delta_\sigma$，
准确递推是
$$
T_{k+1}
=t\,\delta_\sigma T_k-(a_j+2k)(\delta_\sigma t)T_k.
\tag{827.23}
$$
$t$ 和 $\delta_\sigma t$ 在σ图都正则。
若 $T_k\in I_k$，则 $\delta_\sigma T_k\in I_{k+1}$，
而 $I_k$ 是完整环理想且包含于 $I_{k+1}$，
故(827.23)属于 $I_{k+1}$。
归纳得到另一图的包含。交换两图同理。$\square$

特别地，这些generic像都在 $\mathscr C_L$。
由于(827.17)使 $\mathscr E_A/\mathscr C_A$ 无A挠，
每个整态射(827.22)自动因子化经过 $\mathscr C_A$：
其到余商的像在generic fiber为零，故本身为零。
于是取两族之和得到一个真正定义在 $\mathbf P^1_A$ 上的有限source
$$
\Phi_q:
\bigoplus_{\substack{j,\ 0\le k\le q\\v=\tau,\sigma}}
\mathcal O(-a_j-2k)
\longrightarrow\mathscr C_A.
\tag{827.24}
$$
$k=0$ 的重复列可只保留一次。
这个构造避免先假定两张图的原导数矩形矩阵已经整地拼接成同一个像。

## 5. 两个完整模多项式证书足以终止原层

在剩余域 $k$ 中，按原C坐标形成
$$
\overline{\mathcal F}_{v,q}
=\overline C_v^{-1}
 [\,\overline F_{0,v},\overline F_{1,v},\ldots,\overline F_{q,v}\,].
\tag{827.25}
$$
(827.12)给逐列准确公式
$$
(\overline C_v^{-1}w)_j=w_j\quad(j<271),\qquad
(\overline C_v^{-1}w)_{271}
=\frac{w_{271}+\sum_{j<271}\overline q_{v,j}w_j}{\overline P_v}.
\tag{827.26}
$$
要求完整首一多项式整除和乘回。
这里是底环自由模换基，不是整理想商。

**定理827.3。**
在§3、§4的原源与整性条件下，
若在同一个真实剩余域中实际得到多项式矩阵 $X_\tau,X_\sigma$，
并完整核实
$$
\overline{\mathcal F}_{\tau,q}(z)X_\tau(z)=I_{272},\qquad
\overline{\mathcal F}_{\sigma,q}(t)X_\sigma(t)=I_{272},
\tag{827.27}
$$
则特征零原完整层满足
$$
\boxed{\mathscr I_q=\mathscr C_L.}
\tag{827.28}
$$
等价地，可用保有完整生成/包含见证的两图多项式HNF为单位矩阵来认证(827.27)。
仅在 $k(z)$ 中满秩，或只在一批点上rank272，都不是(827.27)。

**证明。**
(827.25)中的每个列是全球态射(827.24)在该图上的一个原列。
所以(827.27)使 $\Phi_q\otimes_Ak$ 在特殊纤维的两个标准图都满射，
因而在整个 $\mathbf P^1_k$ 满射。
$\mathbf P^1_A\to\operatorname{Spec}A$ proper，
由引理827.1，$\Phi_q$ 全局满射。
取generic fiber并用引理827.2，得到
$$
\mathscr C_L=\operatorname{im}\Phi_{q,L}
\subseteq\mathscr I_q\subseteq\mathscr C_L.
$$
两端相同即得(827.28)。若先在完成域上论证，再由忠实域扩张下降。$\square$

因此模上的两个Bézout矩阵无需做特征零CRT或有理重构。
它们也不需要是某一特征零canonical HNF的约化：
所需的是对**真实约化列**的完整多项式右逆。
(827.27)只是一条正向充分证书；某个素点或某个q失败，不能登记相反的特征零结论。

## 6. 一个剩余域分支就足够，及实际小q意味着什么

本篇不同于重构原14个字段系数。
只需一个真实地方 $\mathfrak p$，因为其DVR的分式域仍是原L，
或完成后的分式域包含L且为忠实扩张。

可执行的一个选法是避开原模型的分母与判别式，
使原
$$
\mathbf Z_{(\ell)}[b,\zeta]
$$
在 $\ell$ 处为étale的同一原次数14 order。
实际分解原 $m_b\bmod\ell$，并选择原
$\zeta^2+\zeta+1$ 的一个相容不可约分支；
保存所选最大理想、真实有限剩余域、原b与ζ的像和全部分母单位检查。
不要求一个任意14次多项式模ℓ仍不可约，
也不允许随意挑一个与原域无关的14维乘法表。
若取 $\ell\equiv1\bmod3$，可用原两个ζ根之一及一个真正的 $m_b$ 因子，
得到R822已经写清的真实地方。

这里没有用特征p的“导数降一阶”结论。
所有重数推导都在特征零；模计算只验证(827.27)。
因此不必额外假设 $\ell$ 大于原极点重数；
导数首系数在模ℓ偶然消失只可能使此次充分证书失败。

一旦实际认证(827.28)，原R825给每个非cusp极点
$$
\operatorname{mult}_P E\le q.
\tag{827.29}
$$
原同余是 $m=3d$ 或 $3d+1$，所以可取安全界
$$
K=\lfloor q/3\rfloor
\quad\text{满足}\quad K\ge\max_P\operatorname{mult}_P D.
\tag{827.30}
$$
若没有证明q最小，不把q或K登记为实际最大重数。

例如，**若将来实际通过q=4的两图证书**，则原D约化，
R825逆递推只需 $K=1$：
$$
I_D=\mathcal R\cap(I_1+r\mathcal R),\qquad r=y/\delta y.
\tag{827.31}
$$
这是条件推论；本篇没有运行q=4，也没有宣称D已经约化或坐标已求得。
即使得到(827.28)，(827.31)的完整原坐标、主函数常数与刚性化仍须实际消费。

## 7. 不等待全kernel有理重构的一个进一步入口

本节只给另一组**可核的充分输入条件**。
它不把任意模kernel候选当成特征零函数，也不重跑R787/R809已成阶段。

### 7.1 同一unit-minor chart的原特征零lift

原R787的Schur系统是1326行、1214未知量，原结构界给rank至多1186。
若一个真实、来源完整的1186阶minor在所选地方为单位，
则原特征零rank恰为1186，kernel维数28。

要作DVR结论，还必须把原消元链全部放在同一个A：
原20阶B0块、1234阶A块、Schur构造、原κ与字段尺度中实际使用的每个逆，
以及全部已清分母输入，都须在该地方有单位/整性见证。
不能只检查最终1186阶minor而漏掉前级逆。

固定该真实chart的一组pivot列与28个free列。
指定一个free列为1，其余free列为0，使用同一个单位minor解pivot坐标，
就在A中定义一个确切特征零向量。
rank上界保证所选方程的解满足完整Schur系统；
恢复前级变量后满足原129阶完整关系。
R786/R787的短注入定理遂给一对原全局截面
$$
(A_B,B)\in V_5^2,\qquad A_B=yB,\quad B\ne0.
\tag{827.32}
$$
这个向量无需先做有理重构，其存在、唯一规范与模约化已由单位线性系统确定。
若选择的是另一free方向，必须给独立source标签，
不能将它冒充R787或R809已经输出的那一条A/B。

### 7.2 原S5单位坐标块给p整normal向量

若原S5准确坐标矩阵的某个1234阶minor在同一A为单位，
且(827.32)在原V5基的系数及全部原 $82^{10}$ 尺度都整，
则
$$
b_B=B/\tau^5=\beta_\tau v_B(z),\qquad
\deg(v_B)_i\le5-\epsilon_i
\tag{827.33}
$$
的真实normal系数都在A中。

理由是原S5确为同一个V5的基。
单位minor上的线性系统在A中有唯一解；
它在分式域中只能是原完整normal坐标，
故解自动满足全部1380个原短坐标行。
实际模适配仍应完整代回这些行以绑定来源。
已有R809相同矩阵、相同prime的完成minor/逆和mod转换必须直接消费，
不能因为本节另起标签而重算。

### 7.3 八个单位cyclic节点证明真实 $M_{b_B}$ 整

记原primitive乘法矩阵为 $W=M_w$。
假设它及 $v_B$ 的系数在A，且取到八个
$z_1,\ldots,z_8\in A$，它们的剩余值两两不同，并且每个
$$
K_i=[\,e_0,W(z_i)e_0,\ldots,W(z_i)^{271}e_0\,]
\tag{827.34}
$$
都有实际模单位determinant。
则真实 $M_{b_B}(z)$ 的全部系数都在A中，其模多项式可完全用八个有限域节点恢复。

**证明。**
真正的乘法矩阵已经由原函数(827.33)定义，
并有精确weighted界
$$
\deg(M_{b_B})_{uv}\le5+\epsilon_v-\epsilon_u\le7.
\tag{827.35}
$$
在每个节点，环内乘法与W交换，故
$$
M_{b_B}(z_i)K_i
=[\,v_B(z_i),W(z_i)v_B(z_i),\ldots,W(z_i)^{271}v_B(z_i)\,].
\tag{827.36}
$$
右侧在A，$K_i^{-1}$ 在A，故全部节点值在A。
八个节点的Vandermonde determinant是单位；
对次数至多7的每个真实条目插值，迫其全部系数在A。
约化(827.36)和同一单位Vandermonde求解，
就是原矩阵系数的真实约化。$\square$

此处不构造特征零272阶Krylov逆，不做全矩阵char0 CRT，
也不从八个节点猜一个任意多项式。
充分性使用了原函数已存在、(827.35)的原全局次数界以及全部节点单位性。
任何坏节点只能更换/记录，不能擅自按预期填满秩。

第二图无需再求八套节点；直接用
$$
M_{b_B,\sigma}
=t^5D(t)M_{b_B,\tau}(1/t)D(t)^{-1}
\tag{827.37}
$$
准确运输，(827.35)保证每项非负幂且系数整。
同prime、同原W、同normal基的R806/R815既有cyclic点缓存可按原SHA消费，
不改tag伪装成新producer；缺少的合法节点才是新计算。

### 7.4 从一条B产生足够多的原齐次source

$M_{b_B,\tau}$ 的第i列是原
$$
B\,d_i\in H^0(Y_L,(5+\epsilon_i)H-E)
\tag{827.38}
$$
在第一图的normal向量。
第二图第i列正按权 $5+\epsilon_i$ 运输。
所以这一个lift B就给272条满足§4的原source，
权分布为 $5,6^{144},7^{127}$。

其初始像通常是比 $I_E$ 更小的主截面零理想；
不把它称为R824的完整极点模。
然而定理827.3只要求原包含，因此若它的模导数列在两图真的满射到C，
仍足以强制原 $I_q=C$。
若不通过，原因可能是B的附加零、坏约化或实际高重数，
不能据此否定完整 $I_q$ 的终止。

仅有28个原weight5 kernel方向而不乘这些 $d_i$ 时，
q=4最多只有140个底环列，不能从它们直接得到rank272。
本节保留了这项必要的实际source规模。

### 7.5 原R806/R813也可给导子的真实约化

还可把导子入口与R815尚未完成的特征零CRT分开。
此入口只在下列原对象及单位节点已经真实具备后使用：

- R806的准确 $W(z)=M_w$，包括原normal基与实际 $w=e_2/\tau$；
- R813的原准确 $v_g(z),v_h(z)$，分别表示 $g=\delta_\tau z$、
  $h=\delta_\tau w$；两个原target rational scale实际都是 $6724$，
  在恢复normal向量时只施一次；
- 它们的全部系数在同一个A，原六个节点的 $K_i$ 单位，
  且节点剩余值两两不同。

R813/R817已经证明原真正 $M_g$ 与 $\Gamma$ 存在，
并有(827.9)的weighted界。
在节点令
$$
K_g=[\,v_g,Wv_g,\ldots,W^{271}v_g\,].
$$
原环内乘法给
$$
M_g(z_i)=K_g(z_i)K_i^{-1}.
\tag{827.39}
$$
右侧在A。$M_g$条目最高次数5，
所以六个单位Vandermonde节点使它的全部真实系数在A，
并从模(827.39)得到真实约化；不需要先做R815的char0重构。

对Γ，令 $K'(z)$ 为(827.34)中原多项式K关于底变量z的普通导数，
不要把它误换成 $D_0$ 或原δ。
写
$$
T_h(z)=
[\,0,\ v_h(z),\ 2W(z)v_h(z),\ldots,271W(z)^{270}v_h(z)\,].
\tag{827.40}
$$
由于 $\delta_\tau(w^j)=j w^{j-1}h$，
$$
\Gamma(z)K(z)+M_g(z)K'(z)=T_h(z).
\tag{827.41}
$$
因此在任一单位节点，
$$
\Gamma(z_i)=\bigl(T_h(z_i)-M_g(z_i)K'(z_i)\bigr)K_i^{-1}\in\operatorname{Mat}_{272}(A).
\tag{827.42}
$$
这里无需物化 $M_h$。
$K'$的节点列也无需构造高次特征零K：
若 $c_0=e_0,d_0=0$，则在每个节点递推
$$
c_{j+1}=Wc_j,\qquad d_{j+1}=W'c_j+Wd_j
\tag{827.43}
$$
恰得K和K'的列。
$W'$只对原已经完成的低次W系数求导。

Γ条目最高次数4，故任选五个上述不同单位节点，
同一插值论证证明其全部真实系数在A，模(827.42)给真实约化。
本节给的是对既已存在且有全局次数界的原算子的整性证明，
不是把少量点值宣称为一个任意矩阵多项式的特征零证明。

σ侧按原完整式运输：
$$
\Gamma_\sigma
=tD\Gamma_\tau(1/t)D^{-1}
-t^2DG_\tau(1/t)D^{-1}\operatorname{diag}(\epsilon),
\qquad
G_\sigma^{\rm deriv}=-t^3DG_\tau(1/t)D^{-1}.
\tag{827.44}
$$
这些Laurent表达的系数整；其负幂在原特征零中由R813/R817证明为零，
故在A中也为零。实际模消费者仍须准确检查所有负幂相消、weighted支撑和原负号。

可以给§7.3的八个节点共用一张source-bound表：
六点足以给g、五点足以给Γ、八点足以给 $M_{b_B}$。
不先假设这八个小整数都好；真实单位minor决定可用节点。
相同prime/节点/原W/normal基的已完成R815有限域stage须原样复用；
只有实际缺少且必要的节点或不同合法素点才是新算术。
若旧运行尚未发布可读完成stage，不伪造cache已被消费。

所以这条可选入口在全部条件真正满足时只需要原mod kernel chart、
R806、R813、R820及必要的S5单位转换，
不逻辑上等待三项巨大char0 CRT。
这不宣称其中任何尚在运行的原矩阵已经完成，
也不预称新的模满射或原终止层已经得到。

## 8. 可执行证书边界与新增算术

最终一个正向终止证书必须保存：

1. 原Γ、两图正确 $G^{\rm deriv}$的完成来源（或§7.5的原向量加新单位节点证明）、
   normal基、C的完整producer/run/file SHA，
   原b/ζ模型及所选真实地方；
2. source齐次列的原包含证明及权：
   完整R824输入，或§7的所有unit-minor lift与真实mod转换见证；
3. §3全部系数整性、两图C的单位常数及同一原过渡来源；
4. 实际模递推到q的全部完成阶段与原(827.26)整除/乘回；
5. 两个整个多项式模的Bézout右逆/等价完整HNF证书，
   及(827.27)每项系数的实际乘回。

不需要char0全Bézout，不需要把每个 $F_k$ 重构为巨大有理系数，
不需要先证明特殊纤维曲线光滑，
也不需要先分解原E的几何闭点。
这些省略都由本文明确的proper丛、flat C和真实源证明承担。

新增模递推、有限域多项式HNF/Bézout及未成的source适配仍有真实成本。
应先按需求尝试小q并逐层续接，保已成阶段；
不因为理论上界395就预跑395层。
本篇没有得到任何实际q、D、η或高度。
所有新算术只在公开仓库Actions；一日artifact仅传紧接消费者，
仓库只存证明、脚本、参数、run与SHA。

## 来源与查重

- 本仓库R814、R817、R820、R824、R825（2026）：原导子、真实C、原齐次关系及局部重数。
  R822/R824的已登记结论用真实特征零包含和余长；本篇不重做该结论。
- The Stacks Project，2026访问版，
  [Tag 00DV, Lemma 10.20.1](https://stacks.math.columbia.edu/tag/00DV)：
  有限局部模的Nakayama消失。
- The Stacks Project，2026访问版，
  [Tag 01BA, Lemma 17.9.6](https://stacks.math.columbia.edu/tag/01BA)：
  有限型层的支撑闭。
- The Stacks Project，2026访问版，
  [Tag 01WC, Lemma 29.44.5](https://stacks.math.columbia.edu/tag/01WC)、
  [Tag 01W0, Definition 29.42.1](https://stacks.math.columbia.edu/tag/01W0)：
  projective空间proper及其闭像性质。

已对照当前R814/R822/R824全文，并搜索旧Nakayama、proper特殊纤维及模全局满射记录；
未把旧整格单位minor结论另列为新结果。
本文新增的是原导数滤过的两图全球source、flat C和模满射的完整连接。
