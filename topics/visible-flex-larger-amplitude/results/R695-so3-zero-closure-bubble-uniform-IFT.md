# R695. 零闭合差分支的双 bubble 端点校正：定量 Jacobian、统一 IFT 与完整隐式转置

日期：2026-11-26。本文新增一个局部、全变量、保单位 meridian 的准确端点校正定理及其完整导数。它只解决当前 SO3 表示的 Delta=0 闭合分支；不是 R692 的连接重建，不证明其余两条 Gram 方程、非平凡幅度、embedding、reach 或课题完成。本文没有科学运行、没有生成校正后的候选，也不宣称数值入口已经实现。所有用来验证下述条件的实际数据必须另在公有 Actions 产生。

## 1. 准确对象、变量及左乘约定

保留同一固定准确 scalar metric、同一 symbolic S/径向节点、同一固定父材料图 theta0(phi) 和同一真实 T0。记 y 为全部当前自由变量：全部原 free core、全部旋转系数和最后 H。它们不是几个选定模；前三 core 仅按既有条件固定。令

$
T_y(s,\phi)=\exp(\omega_y(s,\phi)\times)T_0(s,\phi),\qquad |T_y|=1,
$

$
P_y(\phi)=R e_r(\theta_0(\phi))+H e_z,\qquad
\Delta_y(\phi)=\Gamma_y(\phi)-P_y(\phi)+\int_0^S T_y(s,\phi)\,ds .
$

当前 Gamma_y 用完整当前 core 和隐式角
Theta_c(phi_c)=theta0(phi) 定义。要求这条实际 core 图的 rho_c>0，且使用同一 unwrapped 分支。R、theta0 和 T0 均是固定输入；H 与全部 free core 继续变化。

所有校正都**左乘在 world 坐标**：

$
\widehat T_{y,z}(s,\phi)
=\exp((W(s,\phi)z(\phi))\times)\,T_y(s,\phi). \tag{1}
$

这里 W 是预先固定的 3×3 矩阵场，z(phi) 是由准确闭合方程隐式确定的三维 endpoint 校正。不得把下面 world 轴的积分 Jacobian 无声用到右乘局部 frame 校正中；右乘时必须把相应旋转放回积分。

定义完整端点映射

$
\mathcal C(y,z)(\phi)
=\Gamma_y-P_y+\int_0^S\widehat T_{y,z}(s,\phi)\,ds. \tag{2}
$

解 C=0 后直接取

$
\widehat F_y(s,\phi)
=P_y(\phi)+\int_S^s\widehat T_{y,z(y)}(v,\phi)\,dv. \tag{3}
$

于是 core 端为 Gamma_y，cap 端为 P_y，且径向 Gram 准确为 1。这一次 (3) 没有 hDelta 项，因为完整 Delta 已由 (2) 准确消去；不是把尚未消去的项删出残差。

## 2. 两个真正 C² 的局部 bubble

取两个互不相交、紧含于 (0,S) 的支撑区间 [a_i,b_i]，各有中间结点 c_i。令
S5(t)=10t³−15t⁴+6t⁵，定义

$
b_i(s)=
\begin{cases}
S_5((s-a_i)/(c_i-a_i)),&a_i\le s\le c_i,\\
1-S_5((s-c_i)/(b_i-c_i)),&c_i\le s\le b_i,\\
0,&\text{其它}.
\end{cases} \tag{4}
$

每个 bubble 在外端 value/slope/second jet 全为零，在中间结点 value=1 且一、二导数为零。因此它是共享节点的分段 quintic C² 函数；不需要凭空假定一段五次多项式能在两个端点都消去前三 jet 而仍非零。可以选已有三个连续径向节点，或在同一固定数学域内显式加入节点。

有 0≤b_i≤1，且准确质量及平方质量为

$
m_i:=\int_0^S b_i\,ds=\frac{b_i-a_i}{2},\qquad
n_i:=\int_0^S b_i^2\,ds=\frac{181}{462}(b_i-a_i). \tag{5}
$

第二个等式来自准确积分
$\int_0^1(10t^3-15t^4+6t^5)^2dt=181/462$；
升降两段用 S5(1−t)=1−S5(t)。这些只是解析有理常数，没有对当前科学数据做本地运算。

bubble 在 core/cap 邻域完全为零，所以校正保持 T 与 T_s 的实际端 jet。只要原单位 meridian 的端口条件成立，core 的反射 C² 接合及固定 cap 接合不会因该端点校正被破坏。

## 3. 为什么单个三轴 bubble 不够，两个够用

先在一个固定 phi 上使用六个 world 控制量
a=(a_1,a_2)，令校正角为 b_1 a_1+b_2 a_2。对固定单位基底 Tbar，零校正处的端点 Jacobian 为

$
J a=\sum_{i=1}^2\int_0^S b_i(a_i\times\overline T)\,ds
=-[v_1]_\times a_1-[v_2]_\times a_2,\qquad
v_i=\int_0^S b_i\overline T\,ds. \tag{6}
$

只有一个 b 时，J=−[v]× 的秩至多为 2，不能校正一般三维闭合误差。三轴自由并不自动等于三个独立 endpoint 方向。

两个 bubble 给

$
JJ^T=(|v_1|^2+|v_2|^2)I-v_1v_1^T-v_2v_2^T. \tag{7}
$

对任意 q，

$
q^TJJ^Tq=|v_1\times q|^2+|v_2\times q|^2.
$

因此 J 满秩当且仅当 v1、v2 不平行。设它们的夹面内两个非零特征值为 lambda_minus、lambda_plus，则和为 |v1|²+|v2|²、积为 |v1×v2|²，法向特征值为该和。因此

$
\sigma_{\min}(J)
\ge\frac{|v_1\times v_2|}
          {\sqrt{|v_1|^2+|v_2|^2}}. \tag{8}
$

若在全部 phi 上该右端至少为 sigma>0，取固定

$
Q_0(\phi)=J(\phi)^T(J(\phi)J(\phi)^T)^{-1},\qquad
W=b_1(Q_0)_1+b_2(Q_0)_2. \tag{9}
$

则对固定基底，在 z=0 处 C_z=I，且 ||Q0||≤1/sigma。这一写法没有选择可能不连续的特征向量 frame；只要 Tbar 的角导数和统一秩界存在，Q0 自动周期且光滑。

“固定”很关键：Q0、Tbar 及 bubble 的准确数学定义作为此校正入口的来源冻结；不在每个 trial 中重算 Q0 却省掉它的参数导数。

### 3.1 从正确端 jet 得到可检查的统一秩界

若第一个支撑上
$|\overline T-e_z|\le\eta_1$，第二个支撑上
$|\overline T+e_r(\theta_0)|\le\eta_2$，则

$
|v_1\times v_2|
\ge m_1m_2(1-\eta_1-\eta_2-\eta_1\eta_2),
$

$
|v_1|^2+|v_2|^2
\le m_1^2(1+\eta_1)^2+m_2^2(1+\eta_2)^2. \tag{10}
$

第一式只需展开
$v_1=m_1(e_z+\epsilon_1)$、
$v_2=m_2(-e_r+\epsilon_2)$
并用三角不等式。若其括号严格正，(8) 给统一正 sigma。又如已在相应端邻域有完整
$|\overline T_s|\le L_i$，支撑距端点不超过 delta_i，则可取 eta_i≤L_i delta_i。

正确端 jet 和紧致角圈保证足够小的支撑存在某个正秩界，但这**不保证当前实际 Delta 小到满足后面的闭合球条件**。支撑缩小也会使 endpoint 校正的条件数变差；不能把一个定性秩事实说成当前大幅候选必可校正。

## 4. 更易真正实现的固定端轴右逆

还可完全避免先求精确 v_i 的逆矩阵：用理想端方向
u1=e_z、u2=−e_r(theta0)，定义

$
J_{\rm end}=[-m_1[e_z]_\times,\quad m_2[e_r]_\times].
$

在正交基 (er,e_theta,ez) 中，

$
G_{\rm end}:=J_{\rm end}J_{\rm end}^T
=m_1^2e_re_r^T+(m_1^2+m_2^2)e_\theta e_\theta^T+m_2^2e_ze_z^T.
$

所以其准确逆显式为

$
G_{\rm end}^{-1}
=\frac{e_re_r^T}{m_1^2}
 +\frac{e_\theta e_\theta^T}{m_1^2+m_2^2}
 +\frac{e_ze_z^T}{m_2^2},
$

$
Q_1=m_1[e_z]_\times G_{\rm end}^{-1},\qquad
Q_2=-m_2[e_r]_\times G_{\rm end}^{-1},\qquad
W=b_1Q_1+b_2Q_2. \tag{11}
$

这里 Q1、Q2 只依准确 bubble 质量和固定 theta0；全部当前 core/H/omega 仍可变。直接在上述正交基作用即可核
||Q1||=1/m1、||Q2||=1/m2。由于支撑互不相交，

$
\beta_1:=\sup_\phi\int_0^S\|W\|ds=2,\quad
\beta_2:=\sup_\phi\int_0^S\|W\|^2ds
=\frac{181}{231}\left(\frac1{m_1}+\frac1{m_2}\right). \tag{12}
$

若当前实际 Ty 在这两个支撑上分别距对应端轴不超过 eta1、eta2，则

$
\|C_z(y,0)-I\|\le\eta_1+\eta_2. \tag{13}
$

证明是分别积分
$[Wz]_\times(T_y-u_i)$，每段贡献不超过
$m_i\|Q_i\|\eta_i|z|=\eta_i|z|$。
这直接给统一可逆性，不需要把完整闭合方程化成一个未验证的数值 3×3 逆。

(11) 是一个明确可实现的新固定选择，不是现有 Actions 已采用的选择。准确 theta0、symbolic m_i 与全部积分误差仍须实际支付。

## 5. 不带指数损失的统一收缩定理

以下同时覆盖 (9) 和 (11)。假设在一个当前全变量参数域 U 上、所有 phi 有

$
\|C_z(y,0)-I\|\le a_0,\qquad
|\Delta_y(\phi)|\le d,\qquad
\int_0^S\|W\|^2ds\le L.
$

对 (9)，可取
$a_0\le\beta_1\sup|T_y-\overline T|$；
对 (11)，可取 a0≤eta1+eta2。选择 r>0 满足严格余量

$
\boxed{\kappa:=a_0+Lr<1,\qquad d<(1-\kappa)r.} \tag{14}
$

则对每个 y∈U、每个 phi，存在唯一 |z|≤r 的准确解 C(y,z)=0，且

$
|z|\le\frac{d}{1-\kappa},\qquad
\|C_z(y,z)^{-1}\|\le\frac1{1-\kappa}. \tag{15}
$

### 证明

对实反对称 X、H1、H2，矩阵指数的时间有序 simplex 公式及各指数因子的正交性给

$
\|D\exp(X)[H_1]\|\le\|H_1\|,\qquad
\|D^2\exp(X)[H_1,H_2]\|\le\|H_1\|\|H_2\|.
$

第二式是两个次序的 simplex 积分；每个 simplex 质量为 1/2，总质量为 1，不出现 exp(||X||) 或额外因子 2。叉积矩阵满足 ||[w]×||=|w|，Ty 是单位向量，故

$
\|C_{zz}(y,z)\|\le\int_0^S\|W\|^2ds\le L.
$

沿线段积分得 $\|C_z(y,z)-I\|\le a_0+L|z|\le\kappa$。令
$\Psi_y(z)=z-C(y,z)$，则其在闭球的 Lipschitz 常数≤kappa，且
$|\Psi_y(z)|\le d+\kappa r<r$。
Banach 收缩定理给唯一根与第一条 (15)；第二条由 Neumann 级数得。证毕。

严格余量使根在开球内，也使满足条件的参数可以有开邻域。因此后面的 C²/参数 IFT 不只是在一个边界闭球上声称可微。即使某一表述只取闭球条件等号，实际根处可逆时仍可局部用普通 IFT；这里直接采用严格版本以避免混淆。

若 Ty=Exp(omega_y×)T0，则同一真实 T0 上

$
|T_y-\overline T|\le|\omega_y-\overline\omega|
$

也由 Dexp 的积分式得到，非交换旋转不需先相减成一个错误的角度。若连接两 core 的参数线段上 rho_c>0，则固定材料角的完整 core 导数每个 free 系数的向量范数≤1，从而可用

$
\sup|\Delta_y|
\le\sup|\Delta_{\bar y}|+
 \|\delta c_{\rm free}\|_1+|\delta H|+
 S\sup|\delta\omega|. \tag{16}
$

(16) 是一个保全全部变量的保守球界，不是实际候选已通过的数值判据。

## 6. 周期、反射、C² 与正则性

假设 C 在 (y,z,phi) 的所用变量上具有连续的相应导数，至少在 phi 上 C²；Ty 在 s 上 C¹、phi 上 C²，并满足构造 F 所需混合连续性。bubble C²、Q0 或 Qend C²，且 (14) 统一成立。点态 IFT 与根唯一性给同一个周期 C² 的 z(y,phi)，不存在逐角任意挑根的 seam。

固定 y 后记 A=C_z，偏 theta/phi 导数以下均在**固定 z**时取。完整角 jet 是

$
z_\phi=-A^{-1}C_\phi,\qquad
z_{\phi\phi}
=-A^{-1}\{C_{\phi\phi}+2C_{\phi z}z_\phi
                    +C_{zz}[z_\phi,z_\phi]\}. \tag{17}
$

W 的所有角导数均在 C_phi 等项内；不能只对 Ty 求角导而冻结随角变化的 Q。比如

$
C_\phi=\Gamma_\phi-P_\phi+
\int_0^S\{D\exp(Wz)[W_\phi z]T_y+\exp(Wz)T_{y,\phi}\}\,ds.
$

矩阵符号中的 Wz 均指对应叉积矩阵。由 (15)，若整球上
||C_phi||≤M1、||C_phiphi||≤M2、||C_phiz||≤L1，则

$
|z_\phi|\le M_1/(1-\kappa),
$

$
|z_{\phi\phi}|
\le\frac{M_2+2L_1M_1/(1-\kappa)+L M_1^2/(1-\kappa)^2}
         {1-\kappa}. \tag{18}
$

这些常数可由同场完整 jet 和积分包围给出；没有使用有限角采样代替完整角域。

对空间反射 S、det(S)=−1，校正角是轴向量：
w(gphi)=det(S)S w(phi)。若基底、Gamma、P 服从既有完整反射，(9) 的准确伪逆满足相应
$Q(g\phi)=\operatorname{diag}(\det S\,S,\det S\,S)\,Q(\phi)\,S^T$；
(11) 也由显式端轴式满足它。因此
$C(y,Sz,g\phi)=S C(y,z,\phi)$，唯一性迫使 z(gphi)=Sz(phi)。完整校正保留 quarter 反射结构，不能拿有限节点的近似对称充这个结论。

由于 bubble 在两个端邻域完全为零，T、Ts 端 jet 保持。C=0 使 core 位置准确为当前 Gamma。由单位 T 的 core 端值 ez 可得 Ts,z=0，故中平面反射的二阶 jet 条件保留。它仍不证明全表面的嵌入或 reach。

## 7. 全变量的隐式 J

固定 W 的数学定义。对任意原全变量方向 v，包括每个 free core、每个 omega 系数和 H，令

$
C_y[v]
=D\Gamma_y[v]-DH[v]e_z+
 \int_0^S R_c\,DT_y[v]\,ds,\qquad
R_c=\exp((Wz)\times), \tag{19}
$

其中这一偏导是在固定 z 下取。于是

$
Dz[y][v]=-A^{-1}C_y[v]. \tag{20}
$

完整当前 core 固定材料角的微分是

$
D\Gamma_c[\delta c]
=\sum_{\rm free}\delta c_j
 \left(\cos(\nu_j\phi_c)e_r(\phi_c)
       -\frac{\sin(\nu_j\phi_c)}{\nu_j}e_\theta(\phi_c)\right). \tag{21}
$

(21) 包含隐式 phi_c 的变化；不能换成固定 normal-angle 的 support 微分。前三固定项的微分为零，但它们仍在当前 phi_c/rho_c 的值中。DTy 是原全部 omega 场的完整 Dexp；H 的直接 cap 导数也没有删去。

定义点态线性算子

$
B(s)w=D\exp((Wz)\times)[(Ww)\times]T_y(s).
$

则 A=∫B(s)ds，而且

$
D\widehat T[v]
=R_c DT_y[v]-B(s)A^{-1}C_y[v], \tag{22}
$

$
D\widehat F(s)[v]
=DH[v]e_z+\int_S^s D\widehat T(v') [v]\,dv'. \tag{23}
$

在 s=0 代入 A 的定义，(23) 恰等于 DΓy[v]；在 s=S 恰为 DH[v]ez。这是完整端点变分的直接核对，不是把 core 或 H 当固定值来使端点残差消失。

全变量空间仍保留。某些 bubble 方向会成为校正参数化的冗余方向；原正定 H²/阻尼可以稳定它们，但不能冒称已消掉 gauge 或保证良态。对已经准确闭合的裸 Ty，z=0 是球内唯一根，所以该校正保留这个已有闭合场；它不是对全部 C² 等距浸入的双射参数化。

## 8. 完整 J*，包括 z 的一、二角 jet

先不显式展开角 jet。对任一依校正场的残差/观察算子 L(y,z)，完整 reduced Jacobian 为

$
J=L_y-L_z A^{-1}C_y.
$

在同一个声明的角配对与径向测度下，给残差协向量 r，先解

$
A^T\lambda=L_z^*r,
$

再返回

$
\boxed{J^*r=L_y^*r-C_y^*\lambda.} \tag{24}
$

A 的转置方程必须解在实际当前根上。不能反传有限次 Newton 的迭代图并声称那就是准确 implicit J；也不能只对原裸 Ty 回传。

对完整六 jet，z、z_phi、z_phiphi 都影响物理场。可以使用一个明确的下三角隐式系统，避免把 z_phi/z_phiphi 当独立自由场或漏掉其参数变化。记 Z=(z0,z1,z2)，定义

$
R_0=C(y,z_0)=0,
$

$
R_1=C_\phi+A z_1=0,
$

$
R_2=C_{\phi\phi}+2C_{\phi z}z_1+C_{zz}[z_1,z_1]+A z_2=0. \tag{25}
$

在准确根上 z1、z2 就是 (17)。定义两个 3×3 线性算子

$
B_1u=C_{\phi z}u+C_{zz}[u,z_1],
$

$
B_2u=C_{\phi\phi z}u+2C_{\phi zz}[u,z_1]
      +C_{zzz}[u,z_1,z_1]+C_{zz}[u,z_2].
$

直接逐项微分 (25) 给

$
R_Z=
\begin{pmatrix}
A&0&0\\
B_1&A&0\\
B_2&2B_1&A
\end{pmatrix}. \tag{26}
$

因此前向只需依次解三个同一 A 系统：

$
\delta z_0=-A^{-1}R_{0,y}v,
$

$
\delta z_1=-A^{-1}(R_{1,y}v+B_1\delta z_0),
$

$
\delta z_2=-A^{-1}(R_{2,y}v+B_2\delta z_0+2B_1\delta z_1). \tag{27}
$

转置按反顺序解。若 $q_i=L_{z_i}^*r$，则

$
\lambda_2=A^{-T}q_2,\quad
\lambda_1=A^{-T}(q_1-2B_1^T\lambda_2),
$

$
\lambda_0=A^{-T}(q_0-B_1^T\lambda_1-B_2^T\lambda_2),
$

$
\boxed{J^*r=L_y^*r-\sum_{i=0}^2R_{i,y}^*\lambda_i.} \tag{28}
$

所有偏导都来自同一个 C；R_i,y 包含原 core/H/omega 的全部角 jet 和积分分支。曲率 covector 所需 Fss、Fsphi、Fphiphi 因而也有完整隐式回传。最终才经过原全 H² 坐标转置；不能先切掉某个变量块。

### 若改用随 y 重算的右逆

本文推荐固定 W。若将 (9) 中的 J/Q 每个 trial 都重算，则必须付

$
\delta Q=(\delta J)^T G^{-1}
-J^TG^{-1}\{(\delta J)J^T+J(\delta J)^T\}G^{-1},
\quad G=JJ^T,
$

并在 (19) 加入
$\int D\exp(Wz)[(\delta W)z]T_y\,ds$，角 jet 中也相应增加。没有这些项就不是全变量 J/J*。更换固定 Q/基底也需要明确的新表示输入与真实转移重读，不能把旧 Phi 或几何值原样继承。

## 9. 几何量级、实际实现责任与下一方向

局部校正的旋转量满足 |Wz|≤||W||r，位置变化相对裸帽锚定 G 满足

$
|\widehat F-G|\le r\int_s^S\|W(v)\|dv\le r\beta_1.
$

但 $|\widehat T_s|$ 可增加到
$|T_{y,s}|+r\|W_s\|$。过窄 bubble 可能恶化曲率；满秩、闭合和 E=1 都不替代实际 K/reach/幅度。这也解释为何不能只不断缩支撑而忽略 (14) 和完整几何。

实际下一实现可以采用 (11) 的显式端轴 W，把当前原全变量与三个准确 implicit endpoint 参数接到一份独立物理场；真实读取其 closure、两个剩余 Gram 分量、全部原 C/幅度/永久点，按 (25)–(28) 做完整 J/J*。准确积分、root 残差、bubble 质量/域载体、implicit root 的角 jet 与全部浮点误差，须由同场连续核另行支付。有限每角 root 可作数值候选，但不是这个统一连续 IFT 的实际验证。

原 R692 解决的是不同连接系统的完整兼容/重建；本文只是在已经声明的单位 meridian trial 空间内消去一个三维 endpoint 缺口。没有重复它，也没有由条件 IFT 得出非圆闭合 isometry 存在。当前候选是否满足 (14)、是否应该选零 Delta 分支、校正后是否改善真正剩余 Gram，都仍要看真实新输入和 Actions 返回；不以“条件尚未验证”收尾停工，而以这些明确接口继续构造和求解。

来源：本证明由本会话静态推导并由两位代理及root独立审阅；未执行科学计算。原审阅全文SHA256 `58680a770a9b7a7611b88490fe046ef817e1263c5713e35db5e66e3fdfac6d07`，本文只增加结果编号、此来源行并规范数学定界符。实际闭合根、统一IFT条件、剩余Gram及同场全几何均待真实Actions输入验证；完整隐式实现正在接续。
