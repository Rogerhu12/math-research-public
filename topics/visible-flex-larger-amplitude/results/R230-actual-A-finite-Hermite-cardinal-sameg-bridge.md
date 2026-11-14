# R230 — 真实 A 节点接口的有限 Cartesian 场、非均匀 Hermite 拼接与同一度量精化差

## 0. 结论、状态与适用对象

本结果给出一个准确有限场的定义、一套共享二阶数据规则，以及在同一固定度量和同一材料坐标下比较两个有限场的连续误差公式。全部结论均为以下明确输入条件下的代数或分析命题；没有新的 577 节点数值结果。

新节点 reader 的目标对象是原已接受 A：primary SHA256 为 917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf，最终尾包为 018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9，完整 flow manifest 为 3f63c69738fc171709a4cba47baeaf70c40778876e03f93436db56b302578e1f，保存均值主包为 59717e6b83c009671781054b7042624fa30ef39b9f8f9660e9511b1481092e14。reader 使用原 M32、577 个 shooting 节点及每节点 512 个角采样；新源码 SHA256 为 32ffba06fd84d325afa1d9eda7c5391057733f281ba12036c80d54f4661ee1db。

这里“没有新的 Newton”不能泛指全部内部算法。该 reader 不做新的 shooting/BVP Newton、RK/ODE 或变分 flow，但仍实际调用原点根 Newton 及其根矩阵求解。源码就绪不等于点根或节点读取已执行。

2026-11-14 的专用 CI run 43549334621 / job 132307907542 实际以 failure 结束，记录为 runner_id=0、steps=[]，无 artifacts，日志读取为 BlobNotFound。因此本结果不登记任何由该次 CI 产生的科学节点、实际 pull 或成功执行。

以下有限场是对未来真实读出数据的一个新定义。它与原真实尾部、原浮点求值程序、既有接缝场之间的误差，都必须另行支付。R227 的固定度量补丁估计及 R223 的非平面标记接口可消费本结果；本结果不替代其前提。

## 1. 实际径向网格、准确角插值和节点一阶数据

### 1.1 径向顺序

设 reader 的原编号为 $j=0,\ldots,n$，其中 $n=576$，保存半径为 $\widehat r_j$。原编号从外向内；必须由实际保存的数值核实

$$
\widehat r_0>\widehat r_1>\cdots>\widehat r_n>0.
\tag{1.1}
$$

所有保存的有限 binary64 数在本构造中都作为其准确有理值。若两个保存半径相等，不能将零差当作一个严格区间，也不能借理想背景的单调性免费代替 (1.1)。

在 (1.1) 成立后，反序定义

$$
r_i=\widehat r_{n-i},\qquad
a=r_0<r_1<\cdots<r_n=b,\qquad
h_i=r_{i+1}-r_i>0\quad(0\le i<n).
\tag{1.2}
$$

全部节点数组同时按这一反序重排；以下 $Y_i,V_i,W_i$ 均对应半径 $r_i$。相邻差 $h_i$ 用准确有理减法定义，不先作浮点相减再视为准确长度。

### 1.2 偶数角网格的实 cardinal 定义

令 $N=512$、$\theta_\ell=2\pi\ell/N$。对实标量或实向量样本 $f_\ell$，定义

$$
\mathcal I_N f(\theta)
=\frac1N\sum_{\ell=0}^{N-1}f_\ell
\left[
1+2\sum_{k=1}^{N/2-1}\cos\bigl(k(\theta-\theta_\ell)\bigr)
+\cos\bigl((N/2)(\theta-\theta_\ell)\bigr)
\right].
\tag{1.3}
$$

它准确插值全部 $N$ 个样本，是一个明确定义的实有限三角多项式。最后一个 Nyquist 余弦项完整保留。该项的一阶角导在所有采样节点为零，并不表示其全圆周导数为零。

式 (1.3) 中的角是准确的 $\theta_\ell=2\pi\ell/N$。原程序以浮点角和 libm 求值所得的样本被用作这个新多项式的系数数据；两种角求值的差没有被宣布为零。

### 1.3 位置与径向一阶数据

令节点 $i$ 的保存相对圆框样本为 $\delta X_i,\delta Y_i,Z_i^{\rm osc}$，径向一阶样本为 $\delta X_{r,i},\delta Y_{r,i},Z_{r,i}$，保存均值锚为 $H_i$。定义

$$
Y_i(\theta)=
\begin{pmatrix}
r_i\cos\theta\\ r_i\sin\theta\\ H_i
\end{pmatrix}
+
\begin{pmatrix}
\mathcal I_N\delta X_i\\
\mathcal I_N\delta Y_i\\
\mathcal I_N Z_i^{\rm osc}
\end{pmatrix},
\qquad
V_i(\theta)=
\begin{pmatrix}
\cos\theta\\ \sin\theta\\ 0
\end{pmatrix}
+
\begin{pmatrix}
\mathcal I_N\delta X_{r,i}\\
\mathcal I_N\delta Y_{r,i}\\
\mathcal I_N Z_{r,i}
\end{pmatrix}.
\tag{1.4}
$$

保存的 $Z_{r,i}$ 是完整高度径向导数；不得再加一次背景 $w$。$H_i$ 使用 reader 原 stage 正序求和的保存值。新节点场的准确平均高度为

$$
\langle (Y_i)_z\rangle
=H_i+\frac1N\sum_{\ell=0}^{N-1}(Z_i^{\rm osc})_\ell.
\tag{1.5}
$$

浮点样本中可能残留的小零模不能免费删除。

全部角导数必须对 (1.4) 的有限三角多项式求导。原独立保存的角 jet 列可以用于误差比较，但一般不逐数等于此多项式的准确角导，不能在不同公式中交替使用后仍声称它们来自同一个场。准确圆框、准确加法与原 libm/浮点重构之间的差，也属于接回原程序时的费用。

## 2. 非均匀网格上的共享二阶数据

### 2.1 一个无需新 ODE 的明确选择

令

$$
P_i(\theta)=
\begin{pmatrix}
\mathcal I_N\delta X_{r,i}(\theta)\\
\mathcal I_N\delta Y_{r,i}(\theta)
\end{pmatrix}.
$$

对内部节点 $1\le i<n$，记 $h_-=h_{i-1}=r_i-r_{i-1}$、$h_+=h_i=r_{i+1}-r_i$，定义

$$
A_i=
\frac{h_+}{h_-+h_+}\frac{P_i-P_{i-1}}{h_-}
+
\frac{h_-}{h_-+h_+}\frac{P_{i+1}-P_i}{h_+}.
\tag{2.1}
$$

一个完整的端点选择是

$$
A_0=\frac{P_1-P_0}{h_0},
\qquad
A_n=\frac{P_n-P_{n-1}}{h_{n-1}}.
\tag{2.2}
$$

取

$$
W_i^{xy}=A_i,\qquad
(W_i)_z=\mathcal I_N Z_{rr,i}.
\tag{2.3}
$$

由于准确圆框关于 $r$ 为仿射，(2.3) 的水平部分不需再加圆框的径向二阶项。

也可以在构造开始前明确将 $W_0$、$W_n$ 固定为外部接缝给定的完整角函数。采用此选择时必须保存其完整定义及来源，并将 (2.2) 标为未采用。既有有限四 RK 微步的端点 $rr$ 数据若要复用，只能作为这样明确指定的数据；它不是原尾部真实 $rr$ 的区间证书，且仍须核相同坐标、刚体框架、均值锚和全部角函数的匹配。

### 2.2 条件误差公式

式 (2.1) 本身只定义新有限场的二阶数据。若另有同一个准确函数 $P(r,\theta)$，且所用节点值等于它的节点值，则对每个固定 $\theta$，以及统一向量范数，成立

$$
\left|A_i-\partial_rP(r_i,\theta)\right|
\le
\frac{h_-h_+}{h_-+h_+}
\sup_{[r_{i-1},r_{i+1}]}|\partial_r^2P|.
\tag{2.4}
$$

若 $P$ 具有连续三阶径向导数，则还有

$$
\left|A_i-\partial_rP(r_i,\theta)\right|
\le
\frac{h_-h_+}{6}
\sup_{[r_{i-1},r_{i+1}]}|\partial_r^3P|.
\tag{2.5}
$$

端点单侧规则仅给相应的

$$
\frac{h_0}{2}\sup_{[r_0,r_1]}|\partial_r^2P|,
\qquad
\frac{h_{n-1}}{2}\sup_{[r_{n-1},r_n]}|\partial_r^2P|.
\tag{2.6}
$$

不能将内部公式 (2.5) 的二阶精度移给端点。

若节点数据另有误差帽 $\varepsilon_j$，则内部还须加

$$
\frac{h_+}{h_-+h_+}\frac{\varepsilon_i+\varepsilon_{i-1}}{h_-}
+
\frac{h_-}{h_-+h_+}\frac{\varepsilon_i+\varepsilon_{i+1}}{h_+};
\tag{2.7}
$$

端点分别加 $(\varepsilon_0+\varepsilon_1)/h_0$ 与 $(\varepsilon_{n-1}+\varepsilon_n)/h_{n-1}$。因此短区间会放大数据误差。保存相对圆框的径向扰动可避免先加入圆框再相减，但不能免去 (2.7)。

**证明。** 左、右单侧差相对 $P'(r_i)$ 的二阶余项分别不超过 $h_-\sup|P''|/2$ 与 $h_+\sup|P''|/2$；按 (2.1) 加权即得 (2.4)。展开至 $P''$ 项时，两个系数准确抵销；三阶余项的加权系数为

$$
\frac{h_+h_-^2+h_-h_+^2}{6(h_-+h_+)}
=\frac{h_-h_+}{6},
$$

得到 (2.5)。数据误差由线性规则和三角不等式给出。以上导数帽均是额外前提，不能由有限差分结果倒推。

## 3. 五次 Hermite 场及准确 C² 拼接

在 $I_i=[r_i,r_{i+1}]$ 上令 $u=(r-r_i)/h_i$，使用六个完整向量三角多项式控制点

$$
\begin{aligned}
B_{i,0}&=Y_i,\\
B_{i,1}&=Y_i+\frac{h_i}{5}V_i,\\
B_{i,2}&=Y_i+\frac{2h_i}{5}V_i+\frac{h_i^2}{20}W_i,\\
B_{i,3}&=Y_{i+1}-\frac{2h_i}{5}V_{i+1}
                    +\frac{h_i^2}{20}W_{i+1},\\
B_{i,4}&=Y_{i+1}-\frac{h_i}{5}V_{i+1},\\
B_{i,5}&=Y_{i+1}.
\end{aligned}
\tag{3.1}
$$

令 $b_a^d(u)=\binom da u^a(1-u)^{d-a}$。定义

$$
Y^{(N)}(r,\theta)=
\sum_{a=0}^{5}b_a^5(u)\,B_{i,a}(\theta),
\qquad r\in I_i.
\tag{3.2}
$$

(3.1) 中右端数据的下标均为 $i+1$；特别是 $B_{i,3}$ 的二阶项为 $h_i^2W_{i+1}/20$。

Bernstein 端点公式给出

$$
\begin{aligned}
Y^{(N)}(r_i,\theta)&=Y_i(\theta),&
\partial_rY^{(N)}(r_i,\theta)&=V_i(\theta),&
\partial_r^2Y^{(N)}(r_i,\theta)&=W_i(\theta),
\end{aligned}
\tag{3.3}
$$

在右端同样成立。位置、一阶和二阶数据作为完整角函数被相邻片共享，因此总阶不超过二的角导和混合导也一致。由此得到整个闭径向区间上的 $C^2$ 场。每个开径向片上的场是有限多项式与有限三角多项式的组合，因而实解析。

此构造不要求原独立角 jet 列逐数等于插值导数，也不证明 $Y^{(N)}$ 等距于目标度量。其平均高度及径向导数可由有限三角多项式的零模准确计算；这个平均是新 Cartesian 场的平均，不是原非线性 Frenet 速度均值泛函的免费替代。

## 4. 同一固定度量下两级有限场的连续差

### 4.1 准确共同细分

设粗、细两级场都已经实际构造，具有相同闭区间 $[a,b]$、相同材料角 $\theta$ 和相同固定目标度量 $g$。取两径向网格的准确共同细分。对每个共同区间，将两级五次 Bernstein 多项式准确限制到该区间，并将角表示提升到共同有限频带；缺失频率补零。此步骤不通过重新采样或未经误差支付的 FFT 改写函数。

若两级端点、坐标或目标度量不同，必须先明确支付相应桥；不能仅因它们属于同一候选名称就直接使用以下公式。

在长度 $h>0$ 的共同区间 $I$ 上写

$$
E(r,\theta)=Y_f(r,\theta)-Y_c(r,\theta)
=\sum_{a=0}^{5}b_a^5(u)e_a(\theta).
\tag{4.1}
$$

令 $\Delta$ 表示控制点下标的前向差分，$(5)_p=5!/(5-p)!$ 且 $(5)_0=1$。对 $p,q\ge0$、$p+q\le2$，

$$
\partial_r^p\partial_\theta^q E
=
(5)_p h^{-p}
\sum_{a=0}^{5-p}b_a^{5-p}(u)
\,\partial_\theta^q\Delta^p e_a.
\tag{4.2}
$$

### 4.2 有限 Fourier 的混合 jet 帽

对向量三角多项式

$$
v(\theta)=c_0+\sum_{k=1}^{K}
\bigl(a_k\cos k\theta+b_k\sin k\theta\bigr),
$$

取任一已指定的向量范数，定义

$$
\begin{aligned}
\mathcal L_0(v)&=|c_0|+\sum_{k=1}^{K}(|a_k|+|b_k|),\\
\mathcal L_q(v)&=\sum_{k=1}^{K}k^q(|a_k|+|b_k|),\qquad q>0.
\end{aligned}
\tag{4.3}
$$

Bernstein 基非负且和为一，所以

$$
\sup_{I\times S^1}|\partial_r^p\partial_\theta^q E|
\le
(5)_p h^{-p}
\max_{0\le a\le5-p}\mathcal L_q(\Delta^p e_a).
\tag{4.4}
$$

这直接消费两个场的系数差，不将两个大场的范数分别相加。所有实际存在的 Nyquist 系数仍按其所定义的实多项式纳入。若 Fourier 系数含准确角代数数，可用向外区间包住；普通浮点 FFT 的输出本身不是准确系数证书。

同式也适用于一个场与其显式对称投影之差。

### 4.3 供 R227 使用的固定度量一阶与 Hessian 费用

若同一材料坐标中的目标度量确为

$$
g=E_g(r)\,dr^2+r^2\,d\theta^2,
$$

并有

$$
r\ge r_{\min}>0,\qquad
E_g\ge E_{\min}>0,\qquad
\sup\frac{|E_g'|}{2E_g^2}\le C_g,
\tag{4.5}
$$

在 (4.6)–(4.7) 中，$T_{pq}$ 必须是目标 $\mathbb R^3$ 的 Euclidean 范数全域帽；若 (4.3) 采用其他向量范数，须先乘已证明的范数比较常数，不能直接代入诱导度量或 Euclidean Hessian 预算。以这样的 $T_{pq}$ 表示 (4.4) 的全域帽。对正交基
$e_1=E_g^{-1/2}\partial_r$、$e_2=r^{-1}\partial_\theta$，成立

$$
\|dE\|_g\le
\eta:=
\sqrt{\frac{T_{10}^2}{E_{\min}}
      +\frac{T_{01}^2}{r_{\min}^2}}.
\tag{4.6}
$$

相应协变 Hessian 的三个独立分量满足

$$
\begin{aligned}
Z_{11}&=\frac{T_{20}}{E_{\min}}+C_gT_{10},\\
Z_{12}&=\frac{T_{11}+T_{01}/r_{\min}}
                   {r_{\min}\sqrt{E_{\min}}},\\
Z_{22}&=\frac{T_{02}}{r_{\min}^2}
                   +\frac{T_{10}}{r_{\min}E_{\min}},\\
\|\operatorname{Hess}_g E\|&\le
\zeta:=\sqrt{Z_{11}^2+2Z_{12}^2+Z_{22}^2}.
\end{aligned}
\tag{4.7}
$$

证明使用

$$
\Gamma^r_{rr}=\frac{E_g'}{2E_g},\qquad
\Gamma^\theta_{r\theta}=\frac1r,\qquad
\Gamma^r_{\theta\theta}=-\frac r{E_g};
$$

因而 (4.7) 已包括径向坐标联络项。这里以 Frobenius 范数上包所需算子或对角二次范数。

$\eta,\zeta$ 可直接作为 R227 的扰动输入。若被比较的底面只是近似等距，仍须保留 R227 的完整旧 Hessian 帽，或其旧法向曲率与切向 Hessian 分账；不能仅由小 metric 误差删除切向 Hessian。

(4.4)–(4.7) 只有在两个同 $g$ 的实际有限场齐备后才给数值精化证据。单级场、源码准备或只比较若干节点，不等于题目要求的固定 $g$ 连续精化。

## 5. 显式 π 投影与其费用

若需要准确半转对称，可在节点定义时明确使用

$$
(\Pi_{xy}f)(\theta)=\frac{f(\theta)-f(\theta+\pi)}2,
\qquad
(\Pi_zf)(\theta)=\frac{f(\theta)+f(\theta+\pi)}2.
\tag{5.1}
$$

对位置、一阶和二阶数据统一使用这一分量投影。准确圆框已经具有所需水平反对称性，均值锚已经具有所需竖直偶性。

该线性投影与角求导、径向 Hermite 拼接及同步相位运输交换，所以投影后仍为同样的 $C^2$ 有限场。原始场与投影场是两个不同对象；其完整值、一阶、二阶差须用 (4.4) 或另一明确上界支付。不能因为浮点样本看起来对称就将投影费用设为零，也不能将原始场的正性或误差结论直接转给投影场。

## 6. 四个准确 cardinal 点的非平面判据

### 6.1 节点 determinant 的准确有理消费

取 $\theta=0,\pi/2,\pi,3\pi/2$。由于 (1.3) 准确插值这些网格点，其圆框坐标分别为 $(r,0),(0,r),(-r,0),(0,-r)$。将同一节点均值高度从四点同时减去，不改变点差 determinant。

设四个样本扰动为 $(dX_\ell,dY_\ell,z_\ell)$，$\ell=0,1,2,3$，则新原始场的四个点可准确写为

$$
\begin{aligned}
p_0&=(r+dX_0,\ dY_0,\ z_0),\\
p_1&=(dX_1,\ r+dY_1,\ z_1),\\
p_2&=(-r+dX_2,\ dY_2,\ z_2),\\
p_3&=(dX_3,\ -r+dY_3,\ z_3).
\end{aligned}
\tag{6.1}
$$

全部右端量都是准确 binary64 有理值，不需调用三角函数。定义

$$
D=\det
\begin{pmatrix}
(p_1-p_0)^{\mathsf T}\\
(p_2-p_0)^{\mathsf T}\\
(p_3-p_0)^{\mathsf T}
\end{pmatrix}.
\tag{6.2}
$$

公共高度锚在此准确抵销，不需要假设振荡高度的离散零模恰好为零。

对显式 π 投影后的四点，令

$$
a=\frac{(p_0)_{xy}-(p_2)_{xy}}2,\qquad
b=\frac{(p_1)_{xy}-(p_3)_{xy}}2,
\qquad
z_a=\frac{(p_0)_z+(p_2)_z}2,\qquad
z_b=\frac{(p_1)_z+(p_3)_z}2.
$$

四点成为 $(a,z_a),(b,z_b),(-a,z_a),(-b,z_b)$，且按 (6.2) 的行顺序有准确恒等式

$$
D_\pi=4(z_b-z_a)(a_xb_y-a_yb_x).
\tag{6.3}
$$

原始 $D$ 与投影 $D_\pi$ 分别计算、分别报告。它们非零时各自证明相应四点不共面；其数值不能混用。

### 6.2 径向区间的覆盖

对某个径向区间 $I_i$，如果其至少一个端点的 $D$ 严格非零，则对应原始有限 Hermite 场在开片 $I_i^\circ\times S^1$ 上不存在被映入一个平面的非空参数开集。对 $D_\pi$ 同理，但结论属于投影场。

**证明。** 如果某个非空参数开集被映入平面 $n\cdot x=c$，则实解析函数 $n\cdot Y^{(N)}-c$ 在该开集为零。连通开片上的实解析恒等原理使它在整片为零；连续延至端点后，端点整圆周均落在此平面，与该端点四点 determinant 非零矛盾。

如果两个端点的 determinant 都为零，本判据只给“尚未覆盖”，不推出整片平面。后续可以采用其他准确见证。有限条径向接缝本身没有二维参数内部；若全部径向片都被上述判据覆盖，接缝不会留下仅藏于接缝的开平面片。沉浸与像的几何性质仍由各自的证书支付。

## 7. 有限消费者的输出与解释

另备的纯 Python Fraction 消费者只读取真实完整 reader 结果及其实际 owned exit 0 资源，核各节点压缩与解压字节 SHA，使用 (6.1)–(6.3) 产生 577 个节点的准确分数和 576 个区间的覆盖记录。它不补算点根、ODE、变分流或缺失节点。

消费者分别保存：

- 原始与 π 投影 determinant、符号及严格非零节点；
- 实际准确半径差、径向顺序失败索引；
- 每个区间的原始覆盖和投影覆盖、所用端点见证及未覆盖索引；
- 四个 cardinal 点处的准确投影改变量，同时明确它不是完整圆周或一二 jet 的投影误差帽。

完整读取和准确算术正常完成可以得到进程 exit 0，即使某些区间仍未覆盖；必须读取各覆盖布尔量，不能将进程退出码改称数学全通过。输入不完整或 SHA 不符则属于数据消费失败，不能造补值。

## 8. 本结果没有支付的事项

本结果定义并分析有限场，不宣称它已是原连续尾部。它没有支付原浮点节点到准确 cardinal 场的全部求值误差、真实水平 $rr$、原场与 Hermite 场的全径向差、外 cut 与内 collar 的同框架 $C^2$ 接合、完整目标 metric、曲率、嵌入、reach、全闭面直径，以及固定帽和全族的 Hausdorff 幅度。

这些事项在未来实际数据齐备时按各自接口继续完成。当前没有新的 577 节点数值断言，也没有由 CI 准备推出任何原题完成结论。
