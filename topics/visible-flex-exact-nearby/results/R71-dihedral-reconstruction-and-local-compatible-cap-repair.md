# R71：实际二面体等变重建与两极帽的局部兼容修复

2026-11-12，independent-audit。

**状态：完整证明的重建与局部修复结论，含当前 R69 背景上的实际区域。**
本文证明当前四重旋转、角反射和腰反射与 R32–R37 的全部球面重建
交换；四重旋转加角反射已足以分别消掉每个不相连帽上的球面 Killing
场。对兼容缺陷源在极帽为零的修正标量解，还给出一个准确局部修复，
使真实应变误差在较小极帽严格为零。修复支撑可取在球面半径
$2^{-19}$ 与 $2^{-18}$ 之间，与 R69 平盘的极小半径无关。

本文没有用对称性代替法向零迹，也没有把基态上的外区精确性自动
转授给整个 Newton 迭代。最后一节明确列出保持固定 $H$ 时仍需的
实际外区条件。这些条件未被本文称为已构造的全局强逆。

## 1. 当前对象的准确群作用

设
$$
R=R_z(\pi/2),\qquad S=\operatorname{diag}(1,-1,1),\qquad
Z=\operatorname{diag}(1,1,-1).
\tag{71.1}
$$
$G_0=\langle R,S\rangle$ 是八元二面体群，
$G=\langle R,S,Z\rangle=G_0\times\{I,Z\}$ 有十六元。
材料作用分别为 $(r,\theta)\mapsto(r,\theta+\pi/2)$、
$(r,-\theta)$ 和 $(-r,\theta)$。

当前 exact affine 标量数据和 R33 原函数规范准确满足
$$
F(r,\theta+\pi/2)=RF(r,\theta),\quad
F(r,-\theta)=SF(r,\theta),\quad F(-r,\theta)=ZF(r,\theta).
\tag{71.2}
$$
这是实际函数的恒等式，包含无限位置 Fourier 尾。证明可直接从
旋转柱坐标中的单位切向
$$
T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma)
$$
核算：$\beta,\gamma$ 均为 $\sin(4k\theta)$ 和；$a,\beta$ 关于
$r$ 偶，$Z,\gamma$ 关于 $r$ 奇。四重旋转和角反射使实际 Cartesian
切向的平均为零，唯一零均值周期原函数继承这两个作用；准确高度
均值固定剩余积分常数。腰反射同理。R66 以相同奇偶定义负侧 graft；
R69 的径向段、connector、完整 R72 尾和两个平盘也保持 (71.2)。

在 R69 已证明的星形坐标中，写
$$
F(u)=\frac{u}{\rho(u)},\qquad u\in S^2,\quad \rho>0.
$$
则 $\rho(Au)=\rho(u)$，$A\in G$。向量场、标量和张量的作用均取
真实球面等距推前；例如
$$
(A_*q)(u)=Aq(A^{-1}u),\qquad (A_*w)(u)=w(A^{-1}u).
\tag{71.3}
$$
对位移 $V=v+wu$，R32 的准确变量为
$$
q=\rho v-w\nabla_\sigma\rho,\qquad
\rho^2Dg_F[V]=\mathcal L_q\sigma+2wB,\qquad
B=\nabla_\sigma^2\rho+\rho\sigma.
\tag{71.4}
$$
因此 $V$ 的物理等变性恰对应 $w$ 的标量不变性与 $q$ 的向量等变性。

真实目标度量和 R37 固定型别修正也须取同一作用。实际使用的径向
目标、径向 cutoff 及
$\ell=\partial_\theta\log(Y_z/r)$ 均满足所需奇偶；后者关于
$\theta$ 奇、关于 $r$ 偶。在角反射下
$Q_\ell=\partial_\theta-\ell$ 变号，而
$Q_\ell^*(\chi\omega)Q_\ell$ 不变。故当前准确选择的
$\widehat{\mathcal D}$ 与 $G$ 交换。若以后更换零阶修正或 cutoff，
必须保持这一准确性质，不能只检查主符号。

## 2. 全局兼容重建与群作用交换

固定 R32–R37 的归一：
$$
\mathcal C e=\operatorname{div}\operatorname{div}e
 -\Delta\operatorname{tr}e-\operatorname{tr}e,
\qquad
\mathcal C^*\phi=\nabla^2\phi-(\Delta\phi+\phi)\sigma.
\tag{71.5}
$$
R37 已证明
$$
\mathcal C\mathcal C^*=(\Delta+1)(\Delta+2),\qquad
\mathcal C^\dagger=\mathcal C^*
 [(\Delta+1)(\Delta+2)]^\dagger,
\tag{71.6}
$$
其中只去掉一次球谐，零次球谐保留。定义
$$
\mathcal Pe=\mathcal C^\dagger\mathcal Ce,\qquad
\mathcal Qe\perp\mathscr K,\qquad
\operatorname{div}\mathcal L_{\mathcal Qe}\sigma
 =\operatorname{div}e,
\tag{71.7}
$$
$\mathscr K=\{\Omega\times u:\Omega\in\mathbb R^3\}$。
于是有全局准确分解
$$
e=\mathcal L_{\mathcal Qe}\sigma+\mathcal Pe.
\tag{71.8}
$$

**命题 71.1。** $\mathcal C,\mathcal C^*,\mathcal C^\dagger,
\mathcal P,\mathcal Q$ 与每个 $A\in O(3)$ 的对应作用交换。

**证明。** 球面 Levi-Civita 联络、缩并和 $\Delta$ 与每个球面等距
作用交换；不要求保持定向。球谐一次空间是 $O(3)$ 不变子空间，故
(71.6) 的准确谱伪逆也交换。$\mathscr K$ 不变；若 $q=\mathcal Qe$，
则 $A_*q$ 解 $A_*e$ 的同一个方程，并仍与 $\mathscr K$ 正交。
R32 的唯一性给 $A_*q=\mathcal Q(A_*e)$。证毕。

这也给实际范数控制。R37 的旋转 Casimir 范数满足
$$
\|\mathcal C^\dagger h\|_{\mathcal H^s}
 \le\frac7{\sqrt{20}}\|h\|_{H^{s-2}_\sigma},
\qquad \|\mathcal Pe\|_{\mathcal H^s}\le\|e\|_{\mathcal H^s},
\tag{71.9}
$$
而 $\mathcal Q$ 增一阶。本文的局部修复另付 §5 的截断费用；
不能把其 norm 继续称为正交投影 norm。

对任意已给的线性右逆或修正逆 $\mathcal B$，可定义
$$
\mathcal B_G=|G|^{-1}\sum_{A\in G}A_*\mathcal B A_*^{-1}.
\tag{71.10}
$$
若算子 $L$ 和已指定的有限维投影 $\Pi$ 均交换，且
$L\mathcal B=I-\Pi+\mathcal R$，则
$L\mathcal B_G=I-\Pi+|G|^{-1}\sum A_*\mathcal R A_*^{-1}$。
在群作用为等距的范数中，此平均不增加 $\mathcal B$ 或误差的 norm。
本题球面 Sobolev、同一角权的 Fourier 范数和自然几何 $C^k$ 范数
具有此性质。一般非对称 norm 须另乘作用常数。这个平均不构造
原来缺失的右逆，也不消掉非刚体的实际核或反馈条件。

完整 $G$ 不变标量的一次球谐投影为零：$R$ 只保留 $u_z$，而 $Z$
将其变号。因此等变求解可自动去掉三个全局平移的一次球谐增广项。
零次球谐、第四模和更高实际核不由此消失。

## 3. 每个帽上的 Killing 场分别为零

**命题 71.2。** 设 $U\subset S^2$ 是连通、开、$G_0$ 不变的极帽
或环带。若 $q$ 在 $U$ 上为球面 Killing 场且 $G_0$ 等变，则 $q=0$。

**证明。** 先给局部 Killing 的准确形式。对任何切向场定义
$E=\tfrac12\mathcal L_q\sigma$、
$\alpha=\tfrac12\varepsilon^{ij}\nabla_iq_j$ 及
$\Omega(q)=u\times q+\alpha u$。直接微分并交换球面协变导数，
如 R37 (8.1)–(8.2)，得到
$D_i\Omega=J(E_i{}^\sharp)+\varepsilon^{jk}\nabla_jE_{ik}\,u$。
所以 $E=0$ 时 $\Omega$ 在每个连通分支上为常向量，且
$q=\Omega\times u$。对任意正交矩阵，
$$
A_*(\Omega\times u)=\det(A)(A\Omega)\times u.
\tag{71.11}
$$
相同 Killing 场在开集相同使其轴向量相同。$R$ 不变性迫使
$\Omega$ 平行 $e_z$；$S$ 不变性再给
$\Omega=\det(S)S\Omega=-\Omega$，故 $\Omega=0$。证毕。

两个不相连帽各自都保持 $G_0$，所以本命题分别应用，不需要先假设
两帽的轴向量相同，也不需要用一个整体 rotation 同时规范两帽。
腰反射只是把这两次结论相互对应。

**法向条件不能省。** 平面 $z=h$ 上
$\rho=u_z/h$、$B=0$。若 $q=0$，(71.4) 的逆式给
$$
V=\rho^{-1}(q+w\nabla\rho)+wu=\frac{w}{u_z}e_z.
\tag{71.12}
$$
故该帽上任意适当正则的 $w$ 都可以有零一阶应变；例如
$w=c u_z$ 对应帽的竖直平移。上下帽取相反的物理竖直平移，还可
同时保持完整 $G$。因此固定 $H$ 必须另有 $w|_H=0$。即使全部
切向 Killing 已消，不能从 $f|_H=0$ 推出这个条件。

## 4. 帽上的准确兼容积分：符号和二倍归一

以下 $E$ 是球面上的对称二张量，使用
$\tfrac12\mathcal L_q\sigma=E$ 的归一。定向取单位外法向 $u$，
$$
Jv=u\times v,\qquad
\beta_i=\varepsilon^{jk}\nabla_jE_{ik},\qquad
\eta_i=J(E_i{}^\sharp)+\beta_i u.
\tag{71.13}
$$
$\eta$ 是取值于固定 $\mathbb R^3$ 的一形式，其外微分使用 ambient
平凡联络。准确恒等式为
$$
\boxed{\quad d\eta=-(\mathcal CE)u\,dA_\sigma.\quad}
\tag{71.14}
$$

**逐项证明。** 在一点取定向测地正交标架 $e_1,e_2$，
$Je_1=e_2,Je_2=-e_1$，且 $D_i e_j=-\delta_{ij}u$。于是
$$
\eta_1=E_{11}e_2-E_{12}e_1+\beta_1u,\quad
\eta_2=E_{12}e_2-E_{22}e_1+\beta_2u,
$$
$$
\beta_1=\nabla_1E_{12}-\nabla_2E_{11},\qquad
\beta_2=\nabla_1E_{22}-\nabla_2E_{12}.
$$
$D_1\eta_2-D_2\eta_1$ 的切向系数由这两式恰抵消；法向系数为
$$
\nabla_1\beta_2-\nabla_2\beta_1+\operatorname{tr}E
 =\nabla_1\nabla_1E_{22}+\nabla_2\nabla_2E_{11}
  -\nabla_1\nabla_2E_{12}-\nabla_2\nabla_1E_{12}
  +\operatorname{tr}E=-\mathcal CE.
$$
这也核对了曲率项的负号；不能遗漏 $-\operatorname{tr}E$。

设 $U$ 是半径小于 $\pi$ 的开测地极帽，$\mathcal CE=0$。
因 $U$ 单连通，准确设
$$
\Omega(p)=0,\qquad \Omega(u)=\int_{p}^{u}\eta,
\qquad q_E=\Omega\times u,
\tag{71.15}
$$
其中 $p$ 是帽中心，路径可取径向测地线；闭性保证与路径无关。
由 $D_i\Omega=\eta_i$，切向投影给
$$
\nabla_iq_E=E_i{}^\sharp+(\Omega\cdot u)Je_i,
\qquad \tfrac12\mathcal L_{q_E}\sigma=E.
\tag{71.16}
$$
所以没有额外的点值 strain 条件。改变 $\Omega(p)$ 只加一个局部
Killing 场。

对反射也保持正确规范。若 $E$ 是 $G_0$ 不变张量，则
$$
\eta(Au)\circ A=\det(A)A\eta(u).
$$
中心 $p$ 被 $G_0$ 固定，零初值和径向路径给
$\Omega(Au)=\det(A)A\Omega(u)$；再取叉积得
$q_E(Au)=Aq_E(u)$。上下帽采用由 $Z$ 对应的定义即保持完整 $G$。

以上先对 $C^2$ 张量逐点证明，对低正则可按分布外微分解释。
下文实际使用的 $T=\mathcal C^\dagger h$ 在源 $h$ 消失的开帽内
光滑：写 $T=\mathcal C^*\phi$，则该处
$(\Delta+1)(\Delta+2)\phi=0$，这是光滑椭圆算子的局部齐次方程。
这只保证局部正则，不给未支付的高阶 norm；以下每个范数仍保留。

## 5. 不改变兼容源的局部修复与明确球面费用

设两帽 $U_\pm$ 不相交，半径均为 $r_c<\pi/4$，并设
$$
T=\mathcal Pe,\qquad \mathcal CT=\mathcal Ce=0
\quad\hbox{在 }U_+\cup U_-.
\tag{71.17}
$$
在每帽应用 §4 于 $E=T/2$，记所得向量场为 $q_T$。准确得到
$\mathcal L_{q_T}\sigma=T$，这里的二倍已包含在 $E=T/2$ 中。

取径向 $0\le\chi_\pm\le1$，在半径 $r_c/2$ 内为1，帽外为0。
记 $b=\chi_+q_{T,+}+\chi_-q_{T,-}$，定义
$$
q=\mathcal Qe+b,\qquad T_{\rm loc}=T-\mathcal L_b\sigma.
\tag{71.18}
$$
则准确有
$$
e=\mathcal L_q\sigma+T_{\rm loc},\quad
\mathcal CT_{\rm loc}=\mathcal Ce,\quad
T_{\rm loc}=0\ \hbox{在两个半径 }r_c/2\hbox{ 的内帽}.
\tag{71.19}
$$
最后一个等式为开区域上的恒等式，不只是小量估计。修复不要求
$T$ 原来局部为零，也不要求 $\operatorname{div}T_{\rm loc}=0$。
全部构造保持 $G$。

给出可计算的低层费用。球面张量使用 Hilbert–Schmidt 点范数。
设
$$
S_E=\|E\|_{L^\infty(U)}+\sqrt2\|\nabla E\|_{L^\infty(U)}.
$$
由 (71.13)，$|D\Omega|^2\le|E|^2+2|\nabla E|^2$，所以
$$
\|q_T\|_\infty\le r_cS_E,\qquad
\|\nabla q_T\|_\infty
 \le\|E\|_\infty+\sqrt2r_cS_E.
\tag{71.20}
$$
这里积分使用帽内长度不超过 $r_c$ 的测地线，范数不是材料柱坐标
分量 norm。

一个 $C^2$ 的明确选择是 $s=d_\sigma(u,p)$，
$$
\chi(s)=1-S_5(2s/r_c-1),\qquad
S_5(v)=10v^3-15v^4+6v^5
\tag{71.21}
$$
用于 $r_c/2<s<r_c$，两端分别接1和0。由
$\max|S_5'|=15/8$、$\max|S_5''|<6$，及
$\nabla^2s=\cot s(\sigma-ds^2)$，有
$$
\|d\chi\|_\infty\le\frac{15}{4r_c},\qquad
\|\nabla^2\chi\|_\infty\le\frac{32}{r_c^2}.
\tag{71.22}
$$
第二式用 $\cot s\le1/s\le2/r_c$，并对两个正交主方向分别估计。

帽内准确展开是
$$
T_{\rm loc}=(1-\chi)T-d\chi\otimes q_T^\flat
                              -q_T^\flat\otimes d\chi.
\tag{71.23}
$$
结合 $E=T/2$ 得
$$
\boxed{\quad
\|T_{\rm loc}\|_{C^0(S^2)}
\le\frac{19}{4}\|T\|_{C^0(S^2)}
 +\frac{15\sqrt2}{4}\|\nabla T\|_{C^0(U_+\cup U_-)}.
\quad}
\tag{71.24}
$$
两个支撑不相交，故最大值范数不另乘2。这个零阶张量界没有
$r_c^{-1}$。一阶的准确费用可取
$$
\begin{split}
\|\nabla T_{\rm loc}\|_{C^0(U)}\le{}&
 \|\nabla T\|_\infty+
 \frac{15}{4r_c}\|T\|_\infty+
 \frac{64}{r_c^2}\|q_T\|_\infty
 +\frac{15}{2r_c}\|\nabla q_T\|_\infty .
\end{split}
\tag{71.25}
$$
以 (71.20) 代入即为 $T,\nabla T$ 的明确界。位移 $C^2$ 范数还
须使用 $\nabla^2q_T$ 和真实 $\rho$ 的相应导数。更高有限档可选
端点有相应多阶零 jet 的高阶 smoothstep，并按 Leibniz 公式收费；
本文没有把 (71.24) 称作全档无损估计。

## 6. 接到真实修正标量方程：固定两帽的准确结论

令 $\widehat{\mathcal D}=\mathcal D_\rho+\mathcal E$，并保留实际
标量残差：
$$
\widehat{\mathcal D}w=-\tfrac12\mathcal C(\rho^2f)+r_{\rm sc},
\qquad e=\rho^2f-2wB.
\tag{71.26}
$$
由 $\mathcal C(wB)=-\mathcal D_\rho w$，准确有
$$
\boxed{\quad \mathcal Ce=-2\mathcal Ew+2r_{\rm sc}.\quad}
\tag{71.27}
$$
因此若 $\mathcal E=0$ 且 $r_{\rm sc}=0$ 在两外帽，(71.17) 成立。
按 (71.18) 修复后，以真实逆变量
$$
V=\rho^{-1}(q+w\nabla\rho)+wu
$$
重建，得到
$$
\boxed{\quad Dg_F[V]=f-\rho^{-2}T_{\rm loc}.\quad}
\tag{71.28}
$$
真实一阶误差在两个内帽严格为零，其余区域有 (71.24)–(71.25)
和实际乘子 $\rho^{-2}$ 的相应费用。

设 $H$ 包含在两个内帽内的平区，$f=0$、$w=0$ 在 $H$ 的一个开
邻域。则该处 $e=0$、$T_{\rm loc}=0$，故
$\mathcal L_q\sigma=0$。如果每个相应开帽区域为 $G_0$ 不变且连通，
命题 71.2 给 $q=0$，从而
$$
\boxed{\quad V=0\quad\hbox{在 }H\hbox{ 的该邻域。}\quad}
\tag{71.29}
$$
实际应用可直接取上下完整平开盘；R69 的闭子盘 $H$ 严格位于其内。
若只给闭 $H$ 上的迹，则先在内部应用同一结论，再按连续性延伸到
边界。需要的是实际 $w$ 的零迹，不能用尾部某个截断标签为零替代。

完整 $G$ 平均使一次球谐标量残差消失，但一般的局部
$r_{\rm sc}$ 仍须保留。只知道全局 norm 很小不足以使用 (71.29)
作为严格零迹结论；必须给它在外帽准确为零，或另解对应外区缺陷。

## 7. 当前 R69 对象已经支付的固定球面区域

本节沿用 R66/R69 的同一准确 affine 族
$$
\delta\in
\left[-\frac{7789866024620307}{4611686018427387904}
       -\frac1{2000000},\quad
      -\frac{7789866024620307}{4611686018427387904}
       +\frac1{2000000}\right].
\tag{71.30}
$$
这里的 $\delta$ 是近似背景的准确参数；每次选定 $\delta$ 后固定其
目标度量。没有断言不同 $\delta$ 的背景已经相互等距。
R66 完整 graft 报告的准确末端区间直接蕴含
$$
6.563\,10^{-6}<a_*<6.564\,10^{-6},\qquad
0.966<Z_*<0.967.
\tag{71.31}
$$
R69 后续全部径向外区的高度仍小于 $0.967$，半径单调递减。
故 graft 末端的球面余纬满足
$$
\vartheta_* =\arctan(a_*/Z_*)>6.7\,10^{-6}>2^{-18}.
\tag{71.32}
$$
这可以只用有理界验证：$a_*/Z_*>6.563\,10^{-6}/0.967$，
而 $\arctan x\ge x-x^3/3$；同时本区间的 $x<7\,10^{-6}$。

因真实星形投影为全局同胚，两个球面极帽
$$
U_\pm=\{u:d_\sigma(u,\pm e_z)<r_c\},\qquad r_c=2^{-18},
\tag{71.33}
$$
全部对应于 graft 之后的准确径向外区。R69 的长指数段有
$a_T<7\,10^{-6}e^{-(7/5)2^{24}}<2^{-30}$，其后半径继续递减、
高度大于 $0.966$。所以两个真实平开盘以及所选闭子盘 $H$ 均严格
包含于半径 $r_c/2=2^{-19}$ 的内帽。

修复 annulus 位于指数径向段的初段，而不是无限层的平坦极限附近。
在整个外帽上
$$
\rho^{-2}=|F|^2\le(0.967)^2+(6.564\,10^{-6})^2<0.936.
\tag{71.34}
$$
因此 (71.28) 的 $C^0$ 误差可再乘 $0.936$。高阶乘子常数仍用
该对象的真实球面导数，不从 (71.34) 免费推出。

**基态的算子相等。** R69 的目标度量在这一整段准确定义为实际
径向外延的诱导度量，故 $g_F=g_0$ 在 $U_\pm$。R37 的修正系数
$$
\omega=\frac{K(g_F)-K(g_0)}{\zeta^4\mathsf A^{rr}}
$$
在非平区按 R37 的真实正法向系数 $\mathsf A^{rr}$ 定义，准确为零；
这里 $\mathsf A^{rr}$ 不是物理半径 $a$。向平盘直接作零延拓，不在
其退化系数上计算 $0/0$。对应完整零阶修正也为零。因此在共同真实坐标与
密度中 $\widehat P=P$，等价于 $\mathcal E=0$。在极点等式按球面
张量解释，不需对退化的材料角坐标除法。只要标量求解使用外区的
准确齐次源、而非留下局部截断残差，就有 (71.27) 的帽内兼容性。

本节的实际区间来源为：

- [R66 真 graft 报告](../notes/2026-11-12-positive-family-natural-graft.json)，
  SHA256 `d56b7229439ade268b647f17a10f84ba662e02bcb9597f983d2c604fe765fa27`；
- [R69 完整闭近似背景报告](../notes/2026-11-12-actual-closed-approximate-exterior.json)，
  SHA256 `2d9dd3fec38a1f6b75bd41d858f9ef2cd0b7205a57ad9a5f6ee66996404aebbf`。

这里只对这些真实区间作宽松有理推论，没有新用浮点节点替代连续界。

## 8. 迭代中哪些条件真的保持，哪些仍须支付

若每次输入和算子取同一群作用，(71.10)、(71.18) 保持 $G$，且
$F+V$ 继续等变。若每次完整外区求解给 $w=0$ 于实际 $H$，并满足
外帽兼容源为零，则 (71.29) 使每次 $V|_H=0$；任何收敛的 $C^2$
增量级数均准确保持同一材料 $H$。

但这两句话不能反过来推出外帽源为零。只固定 $H$ 不会使整个
$U_\pm$ 的几何保持不变；即使本次 $Dg_F[V]=0$ 在该处，下次仍有
真实二次项 $dV\cdot dV$。于是下一步的 $g_F-g_0$、$\mathcal E$
和局部源可能重新出现。

每轮重新使用星形坐标时，也须将固定目标度量和材料 $H$ 按同一
实际坐标变换运输，并保持 (71.33) 的帽包含关系。基态的余纬间隔
给稳定性余量，但本文没有用它免费代付后续位移的坐标预算。

足够的闭合输入有以下两种准确形式，选择其一须由实际求解完成：

1. 在全局迭代中，把整个 $U_\pm$ 的几何准确固定，并对真实标量
   / 切向输出施加对应零条件。这比仅固定 $H$ 更强，不能默认它与
   所需非平凡弯曲相容。
2. 使用完整外区非线性解算子，使每次外区仍准确满足同一个 $g_0$，
   保持 $H$，并把其完整两迹、普通源、mean 和标签同核心联立。
   这样 $g_F=g_0$ 真正保持，R37 残差型修正在该处仍为零；重建用
   的源和标量解算缺陷也须与这一准确外区模块一致。

R15、R69 给出的完整尾标签/源接口是第二种路线的组成部分，但
当前尚未把该非线性外区模块、有限低块和中央反馈一起构造为满射
强逆。本文不把它们列为已支付输入。若只有
$\mathcal E w-r_{\rm sc}$ 很小而不为零，则 (71.14) 的一形式一般
不闭，不能继续使用路径无关积分；该非零项必须进入后续缺陷估计。

因此本文已严格消除的是两帽的相对切向 Killing 障碍，并给出实际
固定尺度的兼容误差局部化。实际法向零迹、完整外区方程和全局反馈
仍是同一精确族构造中的真实条件，未因对称性或尺度选择被删除。

## 9. 依赖与范围

使用的本课题已证结论为 R32 的星形变量与球面兼容、R33 的真实
单位切向原函数、R37 的完整固定型别误差及正交重建、R66 的实际
族 graft、R69 的闭背景与两个平盘。§§3–5 的 Killing 消去、
$d\eta$ 恒等式、局部原函数和明确 cutoff 费用均已在本文自证。
本文没有声称已证明可见幅度、reach 或 README 的全部完成条件。
