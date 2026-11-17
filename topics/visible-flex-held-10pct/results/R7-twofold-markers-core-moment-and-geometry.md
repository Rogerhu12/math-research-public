# R7　二重对称闭族的固定双帽标记：二阶矩、核心矩及局部几何预算

会话：Astra-held10-f00f08c9-20261117；并行推导 literature_mechanisms，主会话独立复核矩积分、扰动有理界、双帽Hessian及通量公式。本条是**条件引理**：假定所需闭合等距族、圆平帽和中央接口已经存在，以下构造支付 `delta_E > 0`，并给出标记本身的 `C²`、曲率、法线支撑及幅度预算。它不构造仍未解决的非线性闭合尾，也不把开放 prefix 当作闭曲面。

## 1. 假设及需要证明的结论

设一族闭合、连通、嵌入的 `C²` 曲面围成有界体 `Omega_alpha^0`，其像满足

\[
\Omega_\alpha^0=R_\alpha\Omega_0,
\]

其中 `R_alpha` 为绕 `z` 轴的旋转，相位区间具有非空内部并包含 `0`。原体关于该轴的半转对称。各成员已用材料参数实现同一度量，并且上下两个平面圆盘帽以及邻接开平领全程逐点固定。圆盘帽的固定像位于 `z=+Z` 与 `z=-Z`；它们在材料参数下固定，与其作为圆盘的像在旋转下不变相容。

选取 `r_c` 严格小于两圆帽半径；标记的支撑因此离开帽与尾的接缝。令

\[
0<\eta<1,\qquad \varepsilon>0,\qquad
f(x,y)=\varepsilon\left(1-\frac{x^2+y^2}{r_c^2}\right)_+^3
       \bigl[x^2+y^2+\eta(x^2-y^2)\bigr].                       \tag{1}
\]

这里 `t_+^3=max(t,0)^3`。把两块平帽在支撑盘内分别改为

\[
z=Z+f(x,y),\qquad z=-Z-f(x,y).                              \tag{2}
\]

只要选择的 `varepsilon` 使新增两块体积不触碰原曲面的其它部分，这就是一个全程固定的标记。这个不相交条件可由原闭族的严格几何余量支付；不能从开放 prefix 推出。

新族依然对一个固定度量等距：修改的两块材料帽在所有相位完全相同，帽外沿用原等距族，标记支撑外还保留一个开平领。下面证明，适当选择一个任意短的中央直柱后，该新族有 `delta_E>0`，包括对全部反射取商。

## 2. 标记的正则性、大小与局部几何

写 `r²=x²+y²`、`t=r²/r_c²`、`p=1-t`、`c=1+eta`，并令

\[
B=\operatorname{diag}(1+\eta,1-\eta),\qquad q=(x,y)B(x,y)^T.
\]

在支撑盘内 `f=varepsilon q p³`，且 `0<=q<=c r²`。盘内它是多项式；在 `r=r_c`，`f`、一阶导数和二阶导数全为零，因此与盘外的零函数**严格 `C²` 拼接**。这里没有用“小的二阶跳跃”代替 `C²`。

由 `max_{0<=t<=1} t(1-t)^3=27/256`，

\[
0\le f\le d:=\frac{27}{256}\varepsilon c r_c^2.              \tag{3}
\]

其梯度和 Hessian 为

\[
\nabla f=2\varepsilon p^3 Bv-
         \frac{6\varepsilon q p^2}{r_c^2}v,\qquad v=(x,y)^T,
\]

\[
D^2f=2\varepsilon p^3 B
-\frac{12\varepsilon p^2}{r_c^2}
 [(Bv)v^T+v(Bv)^T]
-\frac{6\varepsilon q p^2}{r_c^2}I
+\frac{24\varepsilon q p}{r_c^4}vv^T.                       \tag{4}
\]

于是

\[
|\nabla f|\le 2\varepsilon c r_c\sqrt t\,p^2(1+2t)
             \le 2\varepsilon c r_c,                       \tag{5}
\]

因为 `sqrt(t)<=1` 且 `(1-t)^2(1+2t)=1-3t²+2t³<=1`。又因为

\[
\|D^2f\|_{\rm op}
\le\varepsilon c(2p^3+30tp^2+24t^2p)
\le\varepsilon c\left(2+\frac{120}{27}+\frac{96}{27}\right)
=10\varepsilon c.                                         \tag{6}
\]

最后一步使用 `max t(1-t)^2=max t²(1-t)=4/27`。图形的第一基本形式是 `I+grad f (grad f)^T`，第二基本形式是 `D²f/sqrt(1+|grad f|²)`；故两主曲率都满足

\[
|\kappa_i|\le 10\varepsilon c.                             \tag{7}
\]

上下图形的外向单位法线分别为

\[
n_+=\frac{(-\nabla f,1)}{\sqrt{1+|\nabla f|^2}},\qquad
n_-=\frac{(-\nabla f,-1)}{\sqrt{1+|\nabla f|^2}}.
\]

两者均给出 `X dot n=(Z+f-v dot grad f)/sqrt(1+|grad f|²)`。若
`Z>2 varepsilon c r_c²`，则

\[
X\cdot n\ge
\frac{Z-2\varepsilon c r_c^2}
 {\sqrt{1+4\varepsilon^2c^2r_c^2}}.                         \tag{8}
\]

这是标记图形上实际**曲面法线**的支撑界，未混同于平面截线的支持函数。曲率和法线支撑的局部预算均显式趋于原平帽的预算；全局 reach 仍需在拼接后的整个闭族上检查。

## 3. 双帽四极矩的精确积分

令 `B_+` 和 `B_-` 为新增上下两块体。因 `f>=0`，它们与原体内部不交；新体为

\[
\Omega_\alpha=R_\alpha\Omega_0\;\cup B_+\cup B_-.
\]

两块体固定、各自半转对称。以 `w=x+iy` 记横向复坐标，新增四极矩为

\[
B_2=\int_{B_+\cup B_-}w^2\,dV.
\]

每块体的竖直厚度均为 `f`，故

\[
\begin{aligned}
B_2
 &=2\varepsilon\int_0^{r_c}\int_0^{2\pi}
   r^5e^{2i\theta}(1-r^2/r_c^2)^3
   (1+\eta\cos2\theta)\,d\theta\,dr\\
 &=2\varepsilon\eta\pi\int_0^{r_c}
             r^5(1-r^2/r_c^2)^3\,dr\\
 &=\boxed{\frac{\pi\varepsilon\eta r_c^6}{60}}>0.             \tag{9}
\end{aligned}
\]

其中径向积分为 `r_c^6/120`；**单帽**贡献为 `pi varepsilon eta r_c^6/120`。若希望记号恰为 `pi epsilon r_c^6/60`，可把固定乘积 `varepsilon eta` 记为 `epsilon`；几何预算仍应保留原 `varepsilon(1+eta)`。

## 4. 全体欧氏运动下的不变量

以体积测度定义未归一的中心二阶矩阵

\[
C(\alpha)=\int_{\Omega_\alpha}(X-c_\alpha)(X-c_\alpha)^T\,dV.
\]

半转对称使重心的横向分量为零，且 `C_xz=C_yz=0`。旋转不改变原体的体积及所有只含 `z` 或 `x²+y²` 的矩；新增体又固定，因此重心高度、`C_zz` 和 `T=C_xx+C_yy` 都不随相位变化。

令

\[
A=\int_{\Omega_0}w^2\,dV.
\]

由于横向重心为零，中心化不改变横向复四极矩。于是

\[
Q(\alpha):=C_{xx}-C_{yy}+2iC_{xy}
           =Ae^{2i\alpha}+B_2,
\]

\[
I_2(\alpha):=\operatorname{tr}(C(\alpha)^2)
 =C_{zz}^2+\frac{T^2+|Ae^{2i\alpha}+B_2|^2}{2}.             \tag{10}
\]

若 `A!=0`，右侧在任何非空开相位区间都不恒定。对任意欧氏运动 `X -> U X+b`，其中 `U in O(3)` 允许反射，中心矩阵变为 `U C U^T`，故 `tr(C²)` 不变。因此其中某幅像不能通过任何欧氏刚体运动与参考像重合。

若相位包含 `pi/2` 并且 `Re A!=0`，更有明确差值

\[
I_2(\pi/2)-I_2(0)=-2B_2\operatorname{Re}A\ne0.              \tag{11}
\]

这可让非全等性证据发生在用于可见位移比较的同一个 `pi/2` 相位。

### 从不全等到严格正的 `delta_E`

设两个紧非空曲面像 `S,T` 不全等，但存在 `U_k in O(3)`、`b_k` 使
`d_H(U_k S+b_k,T)->0`。固定 `x_0 in S`，充分大的 `k` 满足
`|b_k|<=sup_{y in T}|y|+|x_0|+1`，故平移有界；`O(3)` 又紧。取收敛子列后，Hausdorff 连续性给出 `US+b=T`，矛盾。闭嵌入曲面重合也会将其有界内部对应，所以体积矩确实是曲面像的不变量。

因此所得到的严格结论是 `delta_E>0`，不是“尚未找到刚体对齐”。

## 5. 短中央直柱使 `A` 非零：不要求所有 upper 点均有正高度

设上下半曲面在中央凸初圈 `Gamma=boundary C` 的精确二阶接口为

\[
F_\pm(0,u)=\gamma(u),\quad
\partial_sF_\pm(0,u)=\pm e_z,\quad
\partial_s^2F_\pm(0,u)=0,                                  \tag{12}
\]

其中 `s>=0` 分别从初圈向两半曲面内部走。把上半整体上移 `ell/2`、下半整体下移 `ell/2`，中间插入 `Gamma times[-ell/2,ell/2]` 的直柱面。式 (12) 使拼接为 `C²`，共同度量也以常值 `a(s)=a(0)` 延长。足够小的 `ell>0` 的嵌入性需由原闭嵌入及接口的局部嵌入邻域保证；此步骤不要求远离接口的全部 upper 点都满足 `z>0`。

以下用 Stokes 通量证明矩的变化公式。令

\[
A_C=\int_C w^2\,dA.
\]

对于有向闭体边界，散度定理给出

\[
A=\int_{\partial\Omega}z\,w^2 n_z\,dS,
\]

因为 `div(z w² e_z)=w²`。另一方面，`div(w² e_z)=0`。将上半与中央平面域 `C` 按边界方向闭合，Stokes 定理给出

\[
\int_{S_+}w^2 n_z\,dS=A_C,\qquad
\int_{S_-}w^2 n_z\,dS=-A_C.
\]

这些是有向曲面的通量恒等式，和两半曲面是否整体位于 `z` 的同一侧无关。新直柱的 `n_z=0`；两半平移仅改变通量式中的 `z`。于是**精确地**

\[
\boxed{A(\ell)=A(0)+\ell A_C}.                             \tag{13}
\]

只要 `Re A_C>0`，至多一个实 `ell` 使 `Re A(ell)=0`。任意小的正长度区间内均可选择合法长度。若取两个允许的精确长度 `ell_0,2ell_0`，并已知 `Re A_C>.11`，则

\[
\max\{|\operatorname{Re}A(\ell_0)|,
       |\operatorname{Re}A(2\ell_0)|\}>.055\ell_0.           \tag{14}
\]

因此一个具有足够误差控制的体积矩计算可在两个显式候选中作出确定选择；无需把浮点数“看起来不为零”当作证明。

## 6. 当前二重对称 core 的完整 Fourier 积分与 `Re A_C>.11` 界

设初圈支持函数

\[
h(\phi)=1+q\cos2\phi+d(\phi)
\]

为 `pi` 周期，并满足

\[
.16\le q\le.21,\qquad
\|d\|_\infty\le.004,\quad
\|d'\|_\infty\le.018,\quad
\|d+d''\|_\infty\le.08.                                  \tag{15}
\]

则 `rho=h+h''>=1-3(.21)-.08=.29>0`，定义严格凸、中心对称的平面域。其边界的法线角表示是

\[
w(\phi)=(h+ih')e^{i\phi},\qquad ds=\rho\,d\phi.
\]

对齐次二次函数 `w²` 使用二维散度恒等式
`div((x,y) w²)=4w²`，得到完整积分公式

\[
\boxed{A_C=\frac14\int_0^{2\pi}
             (h+ih')^2e^{2i\phi}\,h(h+h'')\,d\phi}.         \tag{16}
\]

这也给出有限 Fourier 系数的完全代数算法：若
`h=sum_k h_k e^{ik phi}`，则 `(h+ih')_k=(1-k)h_k`、
`(h+h'')_k=(1-k²)h_k`。因此

\[
A_C=\frac\pi2
\sum_{k_1+k_2+k_3+k_4=-2}
 (1-k_1)(1-k_2)(1-k_4^2)
 h_{k_1}h_{k_2}h_{k_3}h_{k_4}.                             \tag{17}
\]

对于 `h_0=1+q cos2phi`，唯一非零系数为 `h_0=1,h_{±2}=q/2`；代入 (17)，或直接展开 (16)，恰得

\[
A_C^0=\pi q\left(1-\frac94q^2\right)>0.                    \tag{18}
\]

为避免仅以数值角向积分确认正性，下面给出保守的解析扰动界。取精确有理数

\[
v=.21,\quad D=.004,\quad E=.018,\quad F=.08,
\]

\[
K=(1+3v)D+(1+v)F+DF,\quad Z_1=D+E,\quad
W=2(1+v)Z_1+Z_1^2,\quad P=1+2v-3v^2.                     \tag{19}
\]

在此范围内 `|w_0|<=1+v`。例如
`|h_0+ih_0'|²=1+2q c+4q²-3q² c²`，`c=cos2phi`；因 `q<1/3`，其关于 `c in[-1,1]` 单调递增，最大值为 `(1+q)²`。又有

\[
0<h_0\rho_0\le P,\qquad
|h\rho-h_0\rho_0|\le K,\qquad
|w^2-w_0^2|\le W.
\]

将 (16) 的被积函数拆成
`w_0²(h rho-h_0 rho_0)+(w²-w_0²)h rho`，得

\[
|A_C-A_C^0|\le
\frac\pi2\big[(1+v)^2K+(P+K)W\big].                       \tag{20}
\]

函数 `q(1-9q²/4)` 在 `[.16,.21]` 递增；故由 (18)--(20)，

\[
\operatorname{Re}A_C\ge
\pi\left\{.16\left(1-\frac94(.16)^2\right)
-\frac12[(1+v)^2K+(P+K)W]\right\}.                         \tag{21}
\]

花括号内的精确有理数为

\[
\frac{938504073}{25000000000}.
\]

只使用 `pi>3`，已得到

\[
\boxed{\operatorname{Re}A_C>
\frac{2815512219}{25000000000}
=.11262048876>.11}.                                       \tag{22}
\]

若使用数值 `pi` 显示该解析下界，则为约 `.1179359000`；(22) 本身没有依赖浮点积分。

### 当前有限 core 的适用性

`fixed-r30-p20-q20-m24` 的实际主幅度约 `.20000109659082244`。其显式支持函数
`h=1+sum_{j=1}^{24} c_j cos(2j phi)` 满足以下三角和：

\[
\sum_{j\ge2}|c_j|=.003781221963518031,
\]
\[
\sum_{j\ge2}2j|c_j|=.016497143433080445,
\]
\[
\sum_{j\ge2}((2j)^2-1)|c_j|=.07303729193073488.
\]

这些严格落在 (15) 内，所以该有限 Fourier 输入的域矩具有 (22) 的解析正性。所列条件不自动覆盖所有更大 `q` 的新检查点；每个新 core 应重新核对三项有限三角和。这里也没有把有限输入的结论扩张为尚未构造的精确闭曲面极限。

## 7. 对可见比例、握持区与 reach 的影响

双帽标记的每幅像相对原像的 Hausdorff 改变量至多为 (3) 中的 `d`，因此

\[
D_{\rm new}\le D_{\rm old}+2d,\qquad
\delta_{\rm hold,new}\ge\delta_{\rm hold,old}-2d.            \tag{23}
\]

中央直柱长度趋于零时，两半的位移也趋于零；其可见比例影响应一同计入最终预算。固定帽的材料子域修改后依然逐点固定，且 `f(0,0)=0`，两帽中心的距离仍为 `2Z`。题目允许握持区不连通，因而可用包含两中心的两个固定闭子盘作为握持区；其内部非空，且直径至少为 `2Z`。只要最终完整直径预算满足 `2Z>=.2D_new` 即支付所需尺寸。

式 (7)、(8) 给出的只是两块新图形上的明确局部几何控制。原曲面的全部余量、中央直柱的加入、非局部近自接触，以及完整相位族的全局 reach，仍必须在已闭合的候选上支付。该引理的可发布结论是条件性的非全等性机制和标记预算，不能用来代替圆领、非线性尾、全局嵌入或 reach 的缺项。
