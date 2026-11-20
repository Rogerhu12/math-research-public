# R656：完整解析 lift 的连续几何向外界与同一父的三个真实胞

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：已证明的连续包围算法及三胞应用，明确 IEEE 向外算术模型。** 对下述准确 fullclosed 场，在三个完整闭径向胞和全部角度上，已同时包围真实欧氏主曲率、$A_{1/4}$ 支持、位置半径与固定握持见证距离。未覆盖其余919胞，因此本条尚不登记全局 D、reach、held 或整域度量结论。它直接推进 [R650](R650-positive-definite-flow-support-reach.md) 所需输入，不重复原 pulse 前缀或旧归一化 $\lambda$ 证书。

## 1. 准确数学对象，区别于数值 carrier

固定本次 Gauss 曲率受约束六步父 `curvature-qp-gauss-six-step.npz`，SHA-256

`2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`。

J923、M160、n482。全部自由的节点三 jet、自由 core 系数和 H 按各自准确 binary64 数定义；固定前三个 core 系数仍是原同一数据。节点不是把数值 `mesh` 当作新的准确目标，而是原报告所定义的

$$s_i=\alpha_iS+\beta_i,\qquad \alpha_i,\beta_i\in\mathbb Q.$$

S、R 是原同一个准确 Hold 轮廓的末端与半径，消费 [原 FullHold 完整积分证明](../notes/2026-11-17-parallel-model-fullclosed-hold-warm-and-oracle.md) 已给出的有理盒：

$$
S\in\left[
{296412483966226858607817\over125000000000000000000000},
{2371299871729836522645511\over1000000000000000000000000}
\right],
$$

$$
R\in\left[
{564734175386577761774707\over1000000000000000000000000},
{282367087693515366508543\over500000000000000000000000}
\right]. \tag{1}
$$

本候选的准确高度与 lift 宽度为

$$H={4304066185253405\over2251799813685248},\qquad
w={3602879701896397\over72057594037927936}.$$

派生端口按原准确仿射 `unpack` 重建：入口 R 系数为 core c，T 系数为 $-\nu_jc_j$，$\nu_j=2j$；$U_0=e_z$、$A_{0,Z}=0$，末端残差的完整三 jet 为零。特别地，存盘时已舍入的派生 T 槽不是另一个自由实参数。本核先确认输入属于原字面仿射接口，再用向外乘法包围准确 $-\nu_jc_j$，没有改变任何自由系数。其余实际自由三 jet 保持全部角模。

q 是这些三 jet 在准确节点上的共享 quintic Hermite 场。在旋转 $\phi$ 正交架中写

$$
\delta(\phi)=\sum_{j=1}^{M}{1-\nu_j^2\over\nu_j}c_j\sin(\nu_j\phi),
\quad \Theta=\phi+\delta,\quad \rho=\Theta_\phi=1+\delta_\phi,
$$

$$
e_r=(\cos\delta,\sin\delta,0),\qquad
e_\theta=(-\sin\delta,\cos\delta,0).
$$

完整物理场是

$$
F=q+f e_r+\chi H e_z,\qquad
f=\chi(R+S-s), \tag{2}
$$

其中 $\chi=0$ 于 $s\le S-w$，之后为 $10r^3-15r^4+6r^5$，$r=(s-S+w)/w$。本核没有对 $\cos\delta,\sin\delta$ 截频。几何完全由 (2) 求得，不以 a 样值或目标第一基本形式代替真实几何，也不使用旧 pulse 的 $\lambda=a/b$。

即使 (1) 中的 S/R 相关，以下独立区间运算仍覆盖其真实组合；丢失相关性只会放宽界。对应原 `fullclosed-hold-warm.json` 的 SHA-256 为 `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692`。

## 2. 径向全部位置：Hermite、Bernstein 与 piece 连接

对一个准确胞宽 $h>0$，端点三 jet 为 $(Y_0,U_0,A_0)$、$(Y_1,U_1,A_1)$。其 quintic 的六个 Bernstein 控制点准确为

$$
\begin{aligned}
B_0&=Y_0,& B_1&=Y_0+hU_0/5,\\
B_2&=Y_0+2hU_0/5+h^2A_0/20,&
B_3&=Y_1-2hU_1/5+h^2A_1/20,\\
B_4&=Y_1-hU_1/5,&B_5&=Y_1.
\end{aligned} \tag{3}
$$

由 Bernstein 基的准确求导恒等式，物理一导控制点为 $5(B_{j+1}-B_j)/h$，二导再求相应差分。原胞宽直接以
$(\alpha_{i+1}-\alpha_i)S+(\beta_{i+1}-\beta_i)$ 形成有理／S 区间，保留可立即消去的 S 相关性。导数在原胞上形成后再限制到子片，避免把原导数误当子片单位参数导数。

若胞穿过 $S-w$，在该准确符号位置切为两个闭 piece；De Casteljau 的每一步

$$B_j^{\rm new}=(1-u)B_j+uB_{j+1}$$

是准确线性恒等式。把准确切分参数的有理式包围后，用向外区间计算同一恒等式，包围真实被限制的所有控制点。本次节点894准确为 $(\alpha,\beta)=(1,-w)$，所读三胞均不穿界，但代码保留真正穿界的两片处理。

在活动 lift 区间，$\chi$ 在全 $r\in[0,1]$ 的 Bernstein 控制点恰为 $(0,0,0,1,1,1)$。其物理一／二导先按全宽 w 求差分，再限制到真实 piece。若 $P$ 是 d 次 Bernstein 多项式、b 为线性多项式，b 的两端值为 $b_0,b_1$，则乘积的控制点准确为

$$
(Pb)_k={d+1-k\over d+1}P_kb_0+{k\over d+1}P_{k-1}b_1, \tag{4}
$$

越界下标项省略。取 $b=R+S-s$，由此形成

$$f=\chi b,\quad f_s=\chi_s b-\chi,\quad
f_{ss}=\chi_{ss}b-2\chi_s.$$

所以 X/V/T/AA/VT/EE 所需的全部径向分量次数至多六。各项先准确升阶到 degree6，按同一控制点组合 q 与 lift，再作径向细分；不是先分别取 q 与 lift 的大凸包后相加。升阶公式是

$$\widetilde B_j={j\over d+1}B_{j-1}+{d+1-j\over d+1}B_j.$$

Bernstein 基在闭单位区间非负且和为1，故每个连续分量都位于其控制点最小下界与最大上界之间。这支付整个径向 piece，包括所有节点、中点和 Gauss 点之间的位置。共享端点的二 jet 属于同一 C² 场，闭胞并集没有遗漏接缝。

## 3. 有限角多项式的全角余项

本节只对 q 的真实旋转架分量及 core 的 $\delta,\rho,\rho_\phi$ 使用有限带宽，不对完整解析 lift 使用此假设。它们的普通角频率至多 $m=2M$。固定 Q 个均匀角节点，令 $\Delta=\pi/Q$。

对任一个真实径向 Bernstein 控制点对应的实三角多项式 p，设 $B_2=\|p''\|_\infty$。在 $|p''|$ 取最大值的点，导数为零；取距离至多 Δ 的角节点，并用三角多项式 Bernstein 不等式 $\|p^{(4)}\|_\infty\le m^2\|p''\|_\infty$，得到

$$
B_2\le\max_j|p''(\phi_j)|+\frac{m^2\Delta^2}{2}B_2.
$$

因此在 $d=1-m^2\Delta^2/2>0$ 时，

$$B_2\le {\max_j|p''(\phi_j)|\over d}. \tag{5}$$

这里使用的是 [R641 第6–7式](R641-continuous-Gram-certificate-for-one-pulse-cell.md) 已支付的三角 Bernstein／过采样不等式；不是依靠某个 FFT 的经验误差。每个控制点分别取其网格上界，因而亦覆盖由 S/R 盒产生的全部控制点参数族。

在以 $\phi_j$ 为中心的闭角段 $|\eta|\le\Delta$，普通 Taylor 公式给

$$
p(\phi_j+\eta)\in p(\phi_j)+[-L_j,L_j],\quad
L_j=\Delta|p'(\phi_j)|+\tfrac12\Delta^2B_2. \tag{6}
$$

网格上的 p、p′、p″ 由原严格区间 radix-two 变换包围，(5)、(6) 也逐运算向外。因此这是真正角区间覆盖，不是增加角样点后把离散最大值称为连续界。

对旋转架系数 $R_j\cos\nu\phi,T_j\sin\nu\phi,Z_j\cos\nu\phi$，物理角一导的三个分量系数是

$$(-\nu R-T)\sin\nu\phi,\quad(R+\nu T)\cos\nu\phi,\quad-\nu Z\sin\nu\phi,$$

二导系数是

$$
(-(\nu^2+1)R-2\nu T)\cos\nu\phi,\quad
(-(\nu^2+1)T-2\nu R)\sin\nu\phi,\quad
-\nu^2Z\cos\nu\phi. \tag{7}
$$

零模按同一公式处理，T 零槽为零。式 (7) 已包含旋转架连接项；之后 (6) 只对这些实际分量函数作普通角变化包围，不能再次将它们当作未求物理导数的系数。

## 4. 完整 $\cos\delta,\sin\delta$ 的向外包围

先对有限 core 三角多项式使用 (5)、(6)，得到每个整个角段上的 $\delta,\rho,\rho_\phi$ 区间。对其中任意 $x\in[-B,B]$，源码采用

$$
C_{24}(x)=\sum_{k=0}^{24}{(-1)^kx^{2k}\over(2k)!},\qquad
S_{24}(x)=\sum_{k=0}^{24}{(-1)^kx^{2k+1}\over(2k+1)!}.
$$

Taylor 定理和正弦／余弦的每阶导数绝对值至多1给

$$
|\cos x-C_{24}(x)|\le {B^{50}\over50!},\qquad
|\sin x-S_{24}(x)|\le {B^{51}\over51!}. \tag{8}
$$

余弦可将零的49次项也计入 Taylor 多项式，正弦可将零的50次项计入，故 (8) 的阶数准确。所有系数先以 Fraction 定义；Horner 运算、余项与最终已知范围 $[-1,1]$ 的交均向外进行。B 取区间最大绝对端点，余项用该准确 binary 上界的有理幂／阶乘计算并向上转为 double。此操作包围完整非线性解析函数，不把其无限 Fourier 展开截断。

于是完整六 jet 准确为

$$
\begin{aligned}
X&=q+f e_r+\chi H e_z,&
V&=q_s+f_s e_r+\chi_s H e_z,\\
T&=q_\phi+f\rho e_\theta,&
AA&=q_{ss}+f_{ss}e_r+\chi_{ss}H e_z,\\
VT&=q_{s\phi}+f_s\rho e_\theta,&
EE&=q_{\phi\phi}+f(\rho_\phi e_\theta-\rho^2e_r).
\end{aligned} \tag{9}
$$

每个乘积都用同一个真实 (2) 的参数范围，保留所有模、所有 core 及完整解析 lift。区间间可能失去相关性，但包围不会因此缩小。每一径向子胞／闭角段上的 (9) 由前两节的 Bernstein 凸包及 (8) 同时包围。

## 5. 实际欧氏形算子，不使用目标度量

取连续外向接口

$$N=T\times V=F_\phi\times F_s,\quad W=|N|.$$

定义真实第一基本形式 $E=V\cdot V,F_1=V\cdot T,G=T\cdot T$；精确有

$$W^2=EG-F_1^2=|T\times V|^2.$$

源码分别计算右侧两种区间并取交，两者都包含同一个准确值。若某盒不能证明 E>0、W²>0，源码如实登记未付盒，不在该盒除以零或输出虚构的曲率界。位置界仍独立有效。本次三个胞未出现未付盒。

记 $e=N\cdot AA,f_1=N\cdot VT,g=N\cdot EE$。以 V 作 Gram–Schmidt 第一向量，真实对称形算子矩阵为

$$
B_{11}={e\over WE},\qquad
B_{12}={f_1-(F_1/E)e\over W^2},
$$

$$
B_{22}={E\{g-2(F_1/E)f_1+(F_1/E)^2e\}\over W^3}. \tag{10}
$$

这是将第二基本形式除以单位法向长度并变到真实正交切标架后的矩阵；没有假设 E=1、F₁=0 或 G=a²ρ²。它的特征值就是实际欧氏主曲率，取向反转只同时改变符号。

对任何真实对称 $2\times2$ 矩阵，

$$
\|B\|_{\rm op}={|B_{11}+B_{22}|+
\sqrt{(B_{11}-B_{22})^2+4B_{12}^2}\over2}. \tag{11}
$$

直接以 (10) 的区间代入 (11) 得上界。另令 $a,d,b$ 分别包围三个矩阵元的最大绝对值，二次型三角不等式给

$$\|B\|_{\rm op}\le\lambda_{\max}\begin{pmatrix}a&b\\b&d\end{pmatrix}.$$

源码取两种有效向外上界的较小者。因此输出的是整盒上两条实际主曲率绝对值的共同上界，而非以离散特征值填充连续区域。

## 6. 同一次覆盖的位置、支持及 witness

### 位置与 $A_\beta$ 支持

位置盒 X 直接给 $|F|^2$ 的上界。对固定 $\beta>0$、中心0，

$$S_\beta={X_RN_R+X_TN_T+\beta X_ZN_Z\over W}. \tag{12}$$

旋转架正交，所以这是实际 Cartesian $A_\beta F\cdot n$。分子可正可负，源码使用完整区间除法，未在负分子时错误地只除以分母上界。$\beta=1/4$ 是本次固定工具参数，未改变候选或其 g。

### 角四分之一域及取向

所有 even R/Z、odd T 系数及 $\delta$ 的奇对称，使 $F(s,-\phi)$ 等于 Cartesian y 反射后的 $F(s,\phi)$，而 $F(s,\phi+\pi)$ 是其水平半转。对反射，$F_\phi$ 还带来自参数反转的负号，故所选 $N=F_\phi\times F_s$ 准确按同一个空间反射变换；(12)、半径及绝对主曲率保持。因此 $[0,\pi/2]$ 的闭角覆盖给整圆覆盖。每个节点仍覆盖两侧半步，端点处额外覆盖只会使区间更宽。

### 固定握持见证

令 $r_0=1+\sum_jc_j$，则 $F(0,0)=(r_0,0,0)$，本题所需固定见证为

$$p=\operatorname{Rot}_{\pi/2}F(0,0)=(0,r_0,0).$$

在旋转 $\phi$ 架中，p 的分量为 $(r_0\sin\phi,r_0\cos\phi,0)$。基础 $\sin\phi,\cos\phi$ 的严格网格值来自同一整数 twiddle；各角段的 Taylor 余量分别可取
$\Delta|\cos\phi_j|+\Delta^2/2$、$\Delta|\sin\phi_j|+\Delta^2/2$。

距离到固定 p 本身不具有所有上述角对称性，不能只在四分之一域对一个 p 求最小值。p 在这些反射／半转下的轨道是 $\{p,-p\}$，故源码对两个符号都计算

$$|X\mp p(\phi)|^2=\sum_{k=1}^3(X_k\mp p_k(\phi))^2$$

的区间下界，再取最小值。这准确覆盖全圆。上下水平镜像不动 p，故距离界也传给另一半，不需再计算整场。平方区间过零时下界取0，未用分量端点绝对值误作距离下界。

所有半径、支持、曲率和 witness 都消费同一份 (9) 位置／导数区间。没有为 witness 重新扫一遍旧场；将来结合 R248 的活动相位消元时，仍须使用其准确同一 witness 与固定握持区关系。

## 7. 帽、镜像与未来全域 R650 合并

上平盘 $z=H,|x|\le R$ 的外法向为 $e_z$，下镜像盘为 $-e_z$。各盘准确满足

$$|F|^2\le R^2+H^2,\qquad S_\beta=\beta H,\qquad K=0.$$

盘到 p 的准确平方距离是 $H^2+\max(|r_0|-R,0)^2$；源码使用其始终有效的弱下界 $H^2+\max(r_0-R,0)^2$。当前 $r_0>0$ 时两者相同。

入口的 $U_{0,xy}=0,Y_{0,z}=0,A_{0,z}=0$ 给完整 C² 水平镜像接合。末端 q 的三 jet 全为零，使 (9) 在 S 准确给

$$F=R e_r(\Theta)+H e_z,\quad F_s=-e_r(\Theta),\quad F_{ss}=0,$$

恰匹配向内平盘。core 的 $\rho>0$ 给 $\Theta$ 的圆周微分同胚，帽中心用 Cartesian 图；由上下两片与两个圆盘组成闭参数球面。此结构未预先假定像嵌入。相位旋转若按已付材料接口生成，轴对称 $A_\beta$、半径和欧氏曲率界保持；固定非轴标记另用 R650 附录C。

若以后同一候选的全部922胞都已覆盖，令

$$
B_*\ge\max\{\sup_{\rm band}|F|^2,R^2+H^2\},\quad
\sigma_*\le\min\{\inf_{\rm band}S_\beta,\beta H\},\quad
K_*\ge\sup_{\rm band}|\kappa_i|.
$$

且全域浸入、$\sigma_*>0$ 已付，则

$$
D\le2\sqrt{B_*},\qquad
\operatorname{reach}\ge\min\left\{{\sigma_*\over\max(1,\beta)},\,{1\over K_*}\right\}. \tag{13}
$$

第一式只用任意两点经同一中心0的三角不等式；第二式直接使用 R650，已包括全局嵌入和正常管唯一性，不需要另造新的点对验收程序。两式可组合成 reach/D 下界。全域 witness 距离下界同样取全部胞与帽的最小值；若再满足 R248 的握持构造条件，可除以同一个 D 上界。局部三胞结果尚不满足这里的“全部922胞”前提。

## 8. 明确算术模型与实现复用

完整新源码：[fullclosed_geometry_interval.py](../scripts/resume_20261120/fullclosed_geometry_interval.py)，SHA-256

`2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377`。

复用 [原 f512 区间核](../scripts/parallel_20261117_arclength_interval_positive.py)，SHA-256 `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。与 R643/R651 同样，声明的算术模型是标准 IEEE binary64 加、减、乘、除、平方根及逐运算一个 `nextafter` 向外；subnormal 不作 flush-to-zero。精确有理输入转换后以 Fraction 比较确保向外。矩阵／向量内积按明确三项区间运算，不假设普通 BLAS 点积误差。

有限三角求值使用原自制 radix-two 区间变换。π 来自 Machin 有理 arctan 交错余项；twiddle 来自原整数 Taylor 及显式截断余量，不把普通 FFT 或 libm 正弦当作严格包围。新的非线性 sin/cos(delta) 则由 (8) 支付。径向控制点、角余项、lift、正交形算子、支持除法及距离平方全部使用同一向外核，未在最后才把一个普通浮点最大值加 eps。

对不满足正则性盒条件的区域，程序返回 `unpaid_metric_boxes` 并将完整支持／曲率界置空；不将该候选不可解与当前区间过宽混同。无需新 fixture 或重复旧审计才能使用本已完成证明。读取旧有 S/R 盒是消费已刊准确积分证据；本程序未重新执行其标量证书，也不包含旧 pulse 归一化对象。

## 9. 同一2038父的三个完整胞实算

固定 Q8192、每准确 piece 的16个闭 dyadic 径向子胞、$\beta=1/4$、全部模式、全部自由二 jet 及完整 lift。按第6节对2049个闭角盒覆盖四分之一域，连同对称性覆盖全角。三个胞都返回0未付盒、完整连续位置／角覆盖。

下面数字是将原报告的 binary 上／下界向外放宽后的准确十进制有理数：

| 原胞 | 全域 $|\kappa_i|$ 上界 | $S_{1/4}$ 下界 | $|F|^2$ 上界 | 到 witness 的平方距离下界 |
|---|---:|---:|---:|---:|
| 821 | 8.077131 | 0.448878 | 2.971076 | 0.972632 |
| 881 | 6.482645 | 0.724714 | 4.178650 | 3.493963 |
| 895 | 6.591227 | 0.500459 | 4.023809 | 4.273405 |

胞821覆盖 `[1.01275,1.017]` 的准确原符号端点，位于当前点曲率峰附近；881含最大半径点附近；895位于真实非零 χ 区间。后三者并未把三个代表冒充全部922胞。已证三个胞共同满足 $E\ge0.963308$、$|N|^2\ge0.010261$。core 单独的全角 $\rho\ge0.165954$，故材料角保持正向。

本候选的上下平帽另外给

$$
|F|^2\le3.972334,\quad S_{1/4}\ge0.477847,\quad K=0,
\quad \operatorname{dist}(p,\text{caps})^2\ge4.374868.
$$

胞821报告原曲率上界为 `8.077130177083832`。同期另一个实际局部数值极值读取找到了该胞中 $K\approx7.991357693366$，高于其原六个 Gauss 点最大值；连续上界确实覆盖了它。该局部读数不是本证明的依据，也不是上界。报告的“最坏盒地址”只定位区间最大上界，不声称曲率在盒中心达到此值。

实际局部 session78423 自然返回0，单胞总耗时4.84秒；session19024 对881/895自然返回0，总耗时9.90秒。每胞核心时间约4.0–4.6秒是本机这次读数，不能冒称全922胞总成本或其他并行环境的时限。没有再读后继父来替换任何2038结果。

| scratch 证据 | SHA-256 |
|---|---|
| `continuous-2038-cell821-q8192-r16.json` | `7e97770e949aef8da6bef301c2aff63c127cde236599ad9da46e3d8ca9f1eaf0` |
| `continuous-2038-cells881-895-q8192-r16.json` | `8a67ebde02ad43c220a59c4bf9af108ada897a5bc8fa356e0ec2c2430ddcac08` |

完整 source 和参数保留；可重生 raw 不入库。实际 CLI 在工作根 `/workspace/scratch/24b2ab87057a` 为：

```bash
python -u work/recover_evidence/fullclosed_geometry_interval.py \
  --bundle work/geometry_path/curvature-qp-gauss-six-step.npz \
  --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
  --interval-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --out work/recover_evidence/continuous-2038-cell821-q8192-r16.json \
  --cells 821 --angles 8192 --radial-subdivisions 16 --beta 1/4
```

第二次仅将 `--cells` 改为 `881 895`、输出改为第二个报告名，其余输入／source／参数相同。原2038及符号节点报告沿已刊恢复与 Gauss QP 小源码生成，绑定上文各自身份。

## 10. 当前边界

本条首次把当前完整闭端口 q+解析 lift 的真实新候选推进到严格连续几何盒，含真 χ 分片、完整未截频角链、实际 Euclidean 形算子和同遍 witness。它没有复用另一曲面的旧 K／支持结论，没有使用目标 a 作为几何答案，也没有通过缩小检查范围声称全局证书。其余919胞、全域 witness 最小值、最终固定标记、整域同 g 度量求解精化及 README 的完整闭族指标仍由实际后续结果支付。
