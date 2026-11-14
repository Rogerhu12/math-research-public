# R112：不缩小平帽的局部兼容修复与轴向平移迭代接口

2026-11-13，visible-exact-astra-f6a2。

**状态：完整证明的局部重构、有限导阶延拓与平帽保持定理。**
本文补足 R71 的一个尺度问题：兼容源只在极小平帽中为零时，仍可
在整个同一平帽上准确消掉应变误差，而修复的 $C^2$ 费用不含平帽
半径的倒数。构造不逐轮缩小握持材料区域，也不要求其外面的固定
球面大帽继续精确等距。

第二个结论区分两种时间：构造一个精确曲面的迭代步，与最终等距族
的相位参数。前者允许平帽作受控轴向刚体平移；最终相位族仍可逐点
固定最终平帽，并可在其内部插入共同固定的标记模块。这里使用的是
R74 保留 regular 均值及其通量的真实实现，不是把均值行删去。
完整强逆、其邻域估计、尾源可解性和非线性收敛仍须分别支付；本文
没有称本课题的主目标完成。

## 1. 准确变量和局部条件

沿用 R32/R37/R71 的球面变量
$$
 F(u)=u/\rho(u),\quad B=\nabla_\sigma^2\rho+\rho\sigma,\quad
 V=\rho^{-1}(q+w\nabla\rho)+wu,
$$
$$
 \rho^2Dg_F[V]=\mathcal L_q\sigma+2wB,\qquad
 \mathcal C T=\operatorname{div}\operatorname{div}T
             -\Delta\operatorname{tr}T-\operatorname{tr}T.
 \tag{112.1}
$$
R71 的准确分解为
$$
 e=\mathcal L_{\mathcal Qe}\sigma+T,\qquad
 T=\mathcal Pe=\mathcal C^\dagger\mathcal Ce.
 \tag{112.2}
$$
本文给定同一个真实 $e$，不把另一个截断残差代入 (112.2)。

北极使用固定图
$$
 \Phi(x)=(x_1,x_2,\sqrt{1-|x|^2}),\qquad |x|<R,\quad R=1/4.
 \tag{112.3}
$$
南极取第三坐标的负号。设 $0<r\le1/8$，并假设 $T$ 在闭小帽
$\Phi(\overline B_r)$ 上为 $C^2$，且 $\mathcal CT=0$ 在其内部。
两极图支撑不相交。局部条件不要求 $\mathcal CT$ 在
$\Phi(B_R\setminus B_r)$ 中为零。

对球面场，$\|\,\cdot\,\|_{C^k}$ 表示各协变导数的 Hilbert–Schmidt
点范数上确界的最大值；对图上的 $\mathbb R^2$ 值函数，使用
Fréchet 各阶导数的算子范数。所有后续常数均按这两个明确规范给出。

## 2. 局部 Killing 原函数的导数增益

令 $E=T/2$。R71 (71.13)–(71.16) 的准确积分给
$$
 \eta_i=J(E_i{}^\sharp)+\beta_i u,\quad
 \beta_i=\varepsilon^{jk}\nabla_jE_{ik},\quad
 \Omega(p)=0,\quad D_i\Omega=\eta_i,\quad q_T=\Omega\times u.
$$
因为 $d\eta=-(\mathcal CE)u\,dA_\sigma=0$，它在闭小帽中由径向积分
定义，并与路径无关。准确有
$$
 \mathcal L_{q_T}\sigma=T,\qquad
 \nabla_iq_T=E_i{}^\sharp+\alpha Je_i,\quad \alpha=\Omega\cdot u.
 \tag{112.4}
$$
需要控制三阶导数时，不能把 $\Omega$ 的三次 ambient 微分直接估成
未支付的三阶 $T$。应使用闭合的一阶系统
$$
 \nabla\alpha=\beta+(Jq_T)^\flat,\qquad \nabla J=0.
 \tag{112.5}
$$
第一式由 $D_i\Omega=\eta_i$ 与 $\Omega^\top=u\times q_T$ 得到。

置 $A=\|T\|_{C^2(\Phi(\overline B_r))}$。测地半径
$\arcsin r<1/4$，因此
$$
 \|\Omega\|_\infty
 \le \tfrac14(\|E\|_\infty+\sqrt2\|\nabla E\|_\infty)<A/2.
$$
依次用 (112.4)–(112.5) 得
$$
 \begin{split}
 \|q_T\|_\infty&<A/2,\\
 \|\nabla q_T\|_\infty
   &\le\|E\|_\infty+\sqrt2\|\alpha\|_\infty<2A,\\
 \|\nabla^2q_T\|_\infty
   &\le3\|\nabla E\|_\infty+\sqrt2\|q_T\|_\infty<3A,\\
 \|\nabla^3q_T\|_\infty
   &\le3\|\nabla^2E\|_\infty+\sqrt2\|\nabla q_T\|_\infty<5A .
 \end{split}                                                    \tag{112.6}
$$
这些不等式也由一阶系统逐次证明 $q_T\in C^3$；不假设 $T\in C^3$。
在边界按连续延拓取值即可。

记 $Q=(q_T^1,q_T^2)$ 为图上的向量分量，故
$q_T(\Phi(x))=d\Phi_xQ(x)$，且 $Q(0)=0$。
在 $|x|\le1/4$，直接微分平方根给
$$
 \|d\Phi\|,\ \|D^2\Phi\|,\ \|D^3\Phi\|\le2 .
$$
从 ambient/球面 Gauss 公式，球面向量场 $q$ 的三阶图导数被
$$
 8\|\nabla^3q\|+36\|\nabla^2q\|
       +56\|\nabla q\|+28\|q\|
$$
控制，低阶界更小。为核对这一常数：把 ambient 值、球面协变输入的
第 $j$ 阶导数记为 $A_j$，则
$|A_j|\le\sum_{\ell=0}^j{j\choose\ell}|\nabla^\ell q|$，$j\le3$；
图的前三个协变导数分别不超过 $2,2,8$，链式法则给
$8A_3+12A_2+8A_1$。前两个 ambient 分量就是 $Q$。
结合 (112.6)，得到方便的统一界
$$
 \boxed{\quad \|Q\|_{C^3(\overline B_r)}\le2^{10}A.\quad}
 \tag{112.7}
$$
这里没有 $r^{-1}$。

## 3. 保持整个闭小帽的明确 $C^2$ 延拓

若只将 $q_T$ 乘一个在 $B_{r/2}$ 为1的截止，每次迭代只能保证较小帽
不变。反复使用会使材料开集缩至极点。因此本节要求在整个
$\overline B_r$ 准确相等。

令
$$
 P(x)=DQ(0)x+\tfrac12D^2Q(0)[x,x],\qquad Z(x)=Q(x)-P(x).
$$
置 $N_j=\max_{0\le i\le j}\|D^iQ\|_\infty$。Taylor 积分公式给
$$
 \|D^jZ(x)\|\le
       \frac{r^{3-j}}{(3-j)!}N_3,\qquad j=0,1,2,\quad |x|\le r.
 \tag{112.8}
$$
所有低次 jet 已从 $Z$ 中准确减去。

对 $r\le s=|x|\le7r/6$，令
$$
 \psi_j(x)=\big((j+1)r-js\big)\frac{x}{s},\qquad j=1,2,3,
$$
$$
 {\cal E}Z(x)=6Z(\psi_1(x))-8Z(\psi_2(x))+3Z(\psi_3(x)).
 \tag{112.9}
$$
所有 $\psi_j(x)$ 都在 $r/2\le|\psi_j(x)|\le r$ 中，故未使用帽外的
$Q$。系数准确满足
$$
 6-8+3=1,\quad -6+16-9=1,\quad 6-32+27=1.
 \tag{112.10}
$$
在极坐标中，它们分别匹配边界的0、1、2阶径向导数；再作切向微分，
所有总阶不超过2的混合导数也匹配。

取 $S_5(v)=10v^3-15v^4+6v^5$，并定义
$$
 \zeta_r(s)=1-S_5(6(s/r-1)),\qquad r\le s\le7r/6 .
$$
定义全平面函数
$$
 \widetilde Z(x)=
 \begin{cases}
 Z(x),&|x|\le r,\\
 \zeta_r(|x|){\cal E}Z(x),&r<|x|<7r/6,\\
 0,&|x|\ge7r/6 .
 \end{cases}                                                   \tag{112.11}
$$
$S_5$ 在两端的一、二阶导数为零。由 (112.10)，
$\widetilde Z\in C^2$，且在整个闭小盘上就是 $Z$，没有损失半径。

以下给足够的明确费用。因为
$\|D\psi_j\|\le3$、$\|D^2\psi_j\|\le12/r$，且系数绝对值之和为17，
(112.8) 给
$$
 \|{\cal E}Z\|\le17r^3N_3/6,\quad
 \|D{\cal E}Z\|\le51r^2N_3/2,\quad
 \|D^2{\cal E}Z\|\le255rN_3.
$$
平方根图不参与这一步；这是平面向量函数的准确延拓。
由 $\max|S_5'|=15/8$、$\max|S_5''|<6$，
$$
 |D\zeta_r|\le45/(4r),\qquad
 |D^2\zeta_r|\le225/r^2.
$$
第二个界包括径向与切向 Hessian。Leibniz 公式于是给
$$
 \|\widetilde Z\|_{C^2}\le1500rN_3 .
 \tag{112.12}
$$
例如二阶系数的和为
$255+45\cdot51/4+225\cdot17/6=1466.25<1500$；
低阶项在 $r\le1/8$ 时更小。截止的负次幂已与 Taylor 余项的正次幂
配对，留下的是 $r$，不是 $r^{-1}$。

令 $\chi_R=1$ 于 $|x|\le R/2$，在 $R/2\le s\le R$ 取
$1-S_5(2s/R-1)$，在外面取0。准确有
$$
 |D\chi_R|\le15/(4R),\qquad |D^2\chi_R|\le32/R^2 .
$$
因为 $Q(0)=0$，在 $R=1/4$ 上
$$
 \|\chi_RP\|_{C^2}\le183N_2.
$$
二阶常数为 $1+2\cdot15\cdot(5/4)+512\cdot(9/32)=182.5$。

最后置
$$
 B_{\rm ext}=\chi_RP+\widetilde Z,\qquad
 b(\Phi(x))=d\Phi_xB_{\rm ext}(x),
 \tag{112.13}
$$
并在该固定图外取0。由于 $r\le R/2$，在整个 $\Phi(\overline B_r)$
准确有 $b=q_T$。支撑在固定的 $\Phi(B_R)$ 中。
(112.7)、(112.12) 给
$$
 \|B_{\rm ext}\|_{C^2}
 \le(183+1500r)2^{10}A<2^{19}A.
$$
从图向量分量到球面向量场的 $C^2$ 范数转换小于64。一个直接核对是
$\|d\Phi B\|\le2\|B\|$、一阶协变算子范数不超过
$4\|B\|_{C^1}$；二阶坐标表达
$\Pi\partial_i(\Pi\partial_j b)-\Gamma^k_{ij}\Pi\partial_kb$
的三项分别不超过 $8,8,4$ 倍 $\|B\|_{C^2}$。
这里 $\|\Gamma\|\le R/(1-R^2)<1$，由
$\Gamma^k_{ij}=x_k(\delta_{ij}+x_ix_j/(1-|x|^2))$ 得出。
二阶 Hilbert–Schmidt 换算再乘2，仍小于64。
故有完整的半径无关界
$$
 \boxed{\quad
 \|b\|_{C^2(S^2)}
 \le2^{25}\|T\|_{C^2(\Phi(\overline B_r))}.
 \quad}                                                       \tag{112.14}
$$
南北两帽支撑不相交，合并时这个最大值范数不另乘2。

## 4. 兼容源、群作用和更高有限档

对两帽分别作上述构造并相加，定义
$$
 q=\mathcal Qe+b,\qquad T_{\rm cap}=T-\mathcal L_b\sigma .
$$
准确得到
$$
 \boxed{
 e=\mathcal L_q\sigma+T_{\rm cap},\quad
 \mathcal CT_{\rm cap}=\mathcal Ce,\quad
 T_{\rm cap}=0\text{ 在两个完整小帽上}.
 }                                                            \tag{112.15}
$$
中间等式使用恒等式 $\mathcal C\mathcal L_b\sigma=0$；
$C^2$ 延拓时按分布理解，全局应变等式本身是 $C^1$ 等式。
对更高档延拓则可按相应经典导数解释。
没有在兼容性不成立的外环上积分 $\eta$，也没有要求
$\operatorname{div}T_{\rm cap}=0$。由 (112.14)，
$$
 \|T_{\rm cap}\|_{C^1}
 \le\|T\|_{C^1}+2^{26}
       \|T\|_{C^2(\text{两闭小帽})}.                         \tag{112.16}
$$

R71 的二面体 $G_0=\langle R_z(\pi/2),\operatorname{diag}(1,-1,1)\rangle$
在图 (112.3) 中线性作用于 $x$ 和向量分量 $Q$。
以极点零初值取局部原函数、在原点取 Taylor jet、所有径向反射与截止
均与此作用交换。南北使用互为腰反射的图和公式，故保持完整 $G$。
这里不是将 ambient 三分量各自截断后冒充切向场；切向性由
$d\Phi B_{\rm ext}$ 精确保留。

任意指定有限阶 $k\ge1$ 也有同样构造。减去 $Q$ 的 $k$ 阶 Taylor
多项式，并在 $r\le s\le r+r/(2(k+1))$ 使用
$$
 \psi_j(x)=((j+1)r-js)x/s,\quad
 a_j=(-1)^{j-1}j{k+2\choose j+1},\quad j=1,\ldots,k+1.
$$
Lagrange 插值在节点 $-1,\ldots,-k-1$ 处给
$\sum a_j(-j)^m=1$，$0\le m\le k$。
取两端有 $k$ 阶零 jet 的固定 smoothstep，按 (112.11) 延拓。
Taylor 积分及链式法则给
$$
 \|b\|_{C^k}\le C_k\|T\|_{C^k(\text{两小帽})},
 \tag{112.17}
$$
其中 $C_k$ 只依赖上述固定图、阶数和明确截止，不依赖 $r$。
局部原函数所需的 $C^{k+1}$ 由 (112.4)–(112.5) 归纳从 $T$ 的
$C^k$ 得到。这里每个高阶 $C_k$ 可由有限 Leibniz 和计算；
(112.14) 是已在本文展开支付的 $k=2$ 数值。
此结论只逐个有限档使用，不声称现有有限 $C^4$ 样条背景为 $C^\infty$。

## 5. 平帽上的条件自动兼容，但法向实现仍保留

设当前曲面在一个材料开盘 $O$ 上为平面 $z=h$，$h\ne0$，且当前
度量修正源 $f$ 在 $O$ 上准确为零。对任意给定的真实标量 $w$，取
$$
 e=\rho^2f-2wB.
$$
平面上 $\rho=u_z/h$，因此 $B=0$，于是
$$
 e=0,\qquad \mathcal Ce=0\quad\text{在该开平帽上}.            \tag{112.18}
$$
这是当前真实几何的恒等式：此处不需要先证明外围大环上的
$\mathcal Ew-r_{\rm sc}$ 为零。若全局分解足够正则，
$T=\mathcal Pe$ 满足 §1 的小帽条件，故可使用 (112.15)。

在平帽上，(112.15) 与 (112.18) 给 $\mathcal L_q\sigma=0$。
保持 $G_0$ 的构造使每个帽的局部 Killing 场分别为零，见 R71
命题71.2；所以 $q=0$。真实物理位移为
$$
 V=\frac{w}{u_z}e_z.                                      \tag{112.19}
$$
这一步仍没有推出 $w/u_z$ 是常数。所需的准确法向实现是
$$
 \boxed{\quad w=\lambda_\pm u_z
              \quad\text{在各自完整平帽上}.\quad}           \tag{112.20}
$$
在此条件下 $V=\lambda_\pm e_z$，所以 $dV=0$；
一次更新 $F+V$ 在平帽上的完整诱导度量准确不变，二次项
$dV\cdot dV$ 也准确为零。

R74 的真实 grounded 变量是 $w=Y_zv$，其中
$Y_z=z/|F|=u_z$。齐次尾的 regular 零模常通量为0，并可有常值 $v_0$；
当允许平帽移动时，这个常值正是物理轴向平移。非均值必须通过
R15/R72/R74 的完整强尾实现取得 $C^2$ 零延拓，不能从某有限 cut 的
Robin 线或仅仅 $w\to0$ 推出 (112.20)。
对非齐次普通尾源，必须使用其真实加权收敛和完整两迹；本文没有把
齐次尾线转授给任意源。

若 regular 采用单位 $L^2(d\theta)$ 常数
$\phi_0=(2\pi)^{-1/2}$，坐标 $\xi$ 对应
$\lambda=\xi/\sqrt{2\pi}$；当前 R105/R111 帽矩阵采用平均角 norm、
常数基1时，$\lambda=\xi$。regular 均值仍是未知量，平均通量仍是
联立输出行；允许轴移不意味着删除这两个槽。腰反射要求
$\lambda_-=-\lambda_+$，不是把它们各自设成零。

## 6. 一个固定材料平帽如何逐轮保持

设材料开盘 $O_\pm$ 和其平面参数 $X$ 已固定，
$$
 F_n|_{O_\pm}=(X,h_{n,\pm}),\qquad
 h_{n+1,\pm}=h_{n,\pm}+\lambda_{n,\pm}.
$$
假设每步输入 $f_n$ 在这些开盘为零，标量输出满足 (112.20)，并在
真实星形坐标中使用 §3 的整个闭帽延拓。则归纳给
$$
 F_{n+1}|_{O_\pm}=(X,h_{n+1,\pm}),\qquad
 g_{F_{n+1}}|_{O_\pm}=dX\cdot dX .
 \tag{112.21}
$$
若目标在这些开盘上固定为原平面度量，下一步仍有 $f_{n+1}=0$。
不要求其外面的固定球面大帽诱导度量不变。

这里材料域不随 $n$ 缩小。若物理平盘半径为 $a$，则其在当前图
$x=u_{xy}$ 中的半径准确为
$$
 r_n=a/\sqrt{a^2+h_{n,\pm}^2}.
$$
只要 $|h_{n,\pm}|\ge h_{\min}>0$ 且 $a/h_{\min}\le1/8$，
每一步都可应用同一个固定大图。§3 在整个 $B_{r_n}$ 上匹配，
不是只在 $B_{r_n/2}$ 上匹配，因此不会出现逐轮半径损失。
该小帽可取在原平开盘内的一个固定闭子盘；兼容性在其内部成立，
边界 jets 从全局连续场取得，外延不要求更大的兼容开帽。

若完整修正级数在材料 $C^2$ 中收敛，且
$\sum|\lambda_{n,\pm}|<|h_{0,\pm}|-h_{\min}$，则极限仍在同一材料
开盘上为平面，轴向高度是准确的收敛和。这只是保持性质的定理；
不以这一假设代替实际收敛证明。

(112.14) 控制的是球面切向修复。额外物理位移为
$\rho^{-1}b$，故 R37 所用的真实乘子 $\rho^{-1}$ 的导数、材料/星形
坐标转换以及全局高阶源 norm 仍须计入。特别不能把球面 $2^{25}$
直接称为整个物理 $C^2$ 右逆常数。

## 7. 最终相位族仍准确固定握持区

设上述程序最终给出一个真实闭曲面 $F_\infty$，其目标度量在材料
角作用 $\tau_t$ 下不变，且在 $O_\pm$ 上为旋转平盘。则 R3 的
$$
 F_t=R_{-t}\circ F_\infty\circ\tau_t
$$
在 $O_\pm$ 上对所有 $t$ 逐材料点相同。平盘的最终高度不影响这个
恒等式；$R_t$ 保持轴向平移。这说明构造阶段的 (112.21) 与最终
固定 $H$ 要求相容。

单独这条相位族的全曲面像仍由整体旋转相联系，不能据此宣称
$\delta_E>0$。若在两个最终平开盘内部插入与原平盘在开环上相等的
固定标记模块，则在外面使用 $F_t$、在模块内使用同一个固定嵌入。
两定义在开重叠上完全相同，故每个 $t$ 都是同一公共度量的 $C^2$
嵌入；相位连续性也保持。固定标记后的非全等、全时 reach 和可见
位移必须沿 R17/R78/R79 的同一最终对象预算核验。
本文仅证明这一拼接机制不要求在构造精确零解的每一步冻结原帽高度。

## 8. 对当前接口的实际改变与尚未支付的量

R69/R74 的平盘半径极小，但高度有正下界。本文的修复因此不会引入
平盘半径的逆幂，也不依赖较大外环继续满足 $g_F=g_0$。
R71 §8 列出的两种较强外区闭合条件不是唯一选择；新增可用路线为：

1. 在固定材料平盘上保持平面度量，允许 regular 轴向平移；
2. 从当前真实 $e=\rho^2f-2wB$ 作全局分解；
3. 用整个小帽的 Taylor/反射延拓修复切向部分；
4. 由完整强尾实现给 (112.20)，在非线性更新后保持同一材料平盘。

这四条中的局部重构和保持恒等式已在本文全部证明。对当前实际问题，
仍需实际完整逆在所用邻域和普通源类中提供第4条；还需真实的
core/cap/return 强 Schur、平滑或有限档迭代、误差缩减和累积
$C^2$ 几何预算。固定型别误差、所有高频、均值/regular 反馈和
物理坐标费用都不能由本文的局部公式删除。

依赖：[R32](R32-exact-darboux-and-full-scattering-interface.md) / [R37](R37-fixed-type-metric-defect-newton-interface.md) 的准确星形分解，[R71](R71-dihedral-reconstruction-and-local-compatible-cap-repair.md) 的兼容原函数与局部 Killing
消去，[R74](R74-actual-full-tail-robin-and-augmented-positive-cap.md) 的 grounded/regular 归一，[R3](R3-free-metric-finite-fourier-equations.md) 的相位作用。全部新增延拓
公式、常数与保持证明已在上文展开；没有依赖新的数值节点实验。
