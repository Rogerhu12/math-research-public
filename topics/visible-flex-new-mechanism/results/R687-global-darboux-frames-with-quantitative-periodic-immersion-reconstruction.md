# R687：一般正交纬圈的全局 Darboux 帧、真厚锚点与周期浸入重建

2026-11-28。固定 [R680](R680-smaller-tilt-offset-cap-and-positive-hoop-curvature-phase-input.md) 的真实整壳、内倾角 $\vartheta=\arcsin(.27)$ 和刚圈 $a=.075,b=.22$。这里直接求材料标架的一阶兼容，并由它重建实际浸入。源点的纬向尺度含完整材料角依赖。只有在终点角依赖消失且实际重建满足同一度量时，才得到 R655/R680 的完整相位。

## 一般正交度量与端圈

设 $F_r=eP$, $F_\varphi=rT$, $n=P\times T$，其中 $(P,T,n)\in SO(3)$，$e=e(r,\varphi)>0$。令 $h=1/e$。混合导数相等和标架正交性给
$$
 P_\varphi=hT+\ell n,\quad T_\varphi=-hP+kn,\quad
 P_r=vT+an,\quad T_r=-vP+cn,\quad v=-e_\varphi/r,\quad c=e\ell/r .       \tag{1}
$$
对 $P_{r\varphi}=P_{\varphi r}$ 分别取 $T,n$ 分量，再对 $T_{r\varphi}=T_{\varphi r}$ 取 $n$ 分量，得到**一般**相容式
$$
 h_r=c\ell+v_\varphi-ak,\qquad k_r=ha+c_\varphi-v\ell,\qquad
 (r\ell)_r=r(vk+a_\varphi).                                          \tag{2}
$$
例如 $P_{\varphi r}\cdot T=h_r-c\ell$，$P_{r\varphi}\cdot T=v_\varphi-ak$；$P_{\varphi r}\cdot n=hc+\ell_r$，$P_{r\varphi}\cdot n=vk+a_\varphi$。$T_{\varphi r}\cdot n=-ha+k_r$，$T_{r\varphi}\cdot n=c_\varphi-v\ell$。这里保持 $ak$ 的乘积，在 $k=0$（包括真实平接圈）也有定义。给定这些平坦联络可在单连通覆盖上解标架；若仅给抽象联络，还须支付绕环单值、位置闭合和真实内帽姿态。

R680 令 $Q=R_y(\omega)$，$p=r\omega'$，$z=-p(1.01+\cos\varphi)$，$e_0=\sqrt{1+z^2}$。其真实标架及系数为
$$
 P_0=Q(e_r+ze_z)/e_0,\quad T_0=Qe_\varphi,\quad n_0=Q(e_z-ze_r)/e_0,
$$
$$
 k=z/e_0,\quad \ell=p\sin\varphi/e_0^2,\quad c=p\sin\varphi/(re_0),
 \quad v=-p z\sin\varphi/(re_0),\quad a=z_r/e_0^2-(p/r)\cos\varphi .
$$
直接微分上述物理标架即给 (1)。开环带 $k>0$，接圈处这些 $k,\ell,a,c,v$ 全零，$e_0=1$；在 $\varphi=0$，$\int_a^b a(r,0)dr=[\arctan z]_a^b-\int_a^b(p/r)dr=\vartheta$。各标架和位置绕完整材料圆准确回返。真实外圈为 $(be_r,e_r,e_\varphi,e_z)$，内圈为 $(C(a)+aQ_ae_r,Q_ae_r,Q_ae_\varphi,Q_ae_z)$。

## 全局标架与一个可以逐点检验的重建误差

以真实全域周期 $(P,T,n)$ 为未知，另外取标量 $e>0$ 和中心 $C(r)$。设 $I$ 为零均值周期原函数，$\partial_\varphi I f=f-\bar f$，横线为等角均值。完整输入与实际位置定义为
$$
 G=(eP)_\varphi-T-rT_r,\quad d=C'-\overline{eP},\qquad F=C+rIT .        \tag{3}
$$
于是有精确恒等式
$$
 F_r-eP=d-IG,\qquad F_\varphi/r-T=-\bar T,\qquad
 r\bar T(r)=\int_r^b\bar G(s)\,ds                                       \tag{4}
$$
（最后一式用真实外圈 $\bar T(b)=0$）。故 $G=d=0$ 自动给实际度量 $e^2dr^2+r^2d\varphi^2$、位置闭合及 (1)–(2)，原函数无任何非周期积分常数。全域 $SO(3)$ 标架自身的绕圈矩阵乘积准确为单位；这与未解时 $T$ 的均值可能非零是不同条件。执行中保留 $\bar T_y$ 的独立行。位置 $F$ 对任意候选都周期。

有定量无导数损失界。若 $\delta=\sup_r\langle |G|^2\rangle^{1/2},\gamma=\sup_r|d|$, $e_* =\inf e>0$，则由 Fourier Cauchy–Schwarz 和 $\sum_{n\ne0}n^{-2}=\pi^2/3$ 有
$$
 \|(F_r-eP)/e\|_\infty\le(\gamma+\pi\delta/\sqrt3)/e_*,\qquad
 \|F_\varphi/r-T\|_\infty\le(b-a)\delta/a .
$$
把右侧两个数的平方和开根记为 $B$。在目标度量的单位基，真实两列等于正交对加算子范数至多 $B$ 的扰动，故相对度量算子最大误差至多 $2B+B^2$。结论要求全连续域的界。用有限节点计算的数只作独立读数；FFT 原函数与非带限 $eP$ 的真实连续角导数另列混叠误差。

## 不破坏真实接圈正则性的参数化

从 $Q(e_r,e_\varphi,e_z)$ 依次右乘三次绕当前体坐标轴的转动 $R_1(A)R_2(B)R_3(C_1)$，最后右乘 $R_2(-\arctan z)$。$A,C_1$ 为材料角奇函数，$B$ 为偶函数，符合 $y$ 反射；$T$ 为沿材料角的单位切向，只有 $\bar T_y$ 可能不为零。最后的转动围绕当前 $T$，因此描写 $T$ 的两径向导数时无需 $z_{rr}$。这个顺序有实质作用：R680 的真坡 $k(r)$ 是 $C^1$，$\omega$ 是 $C^2$，由此 $T$ 在真坡分段点仍为 $C^2$，$eP$ 为 $C^1$，(3) 的实际 $F$ 为 $C^2$。体角的五次样条在两端去三列，中心斜率与标量径向自由量去两列，真实两阶接圈无变化。

令 $\mu_0(r)=\tfrac12\log[1+p^2(1.01^2+1/2)]$，取
$$
 \log e=(1-\lambda)\log e_0+\lambda\mu_0+u(r),\qquad
 C'= -1.01pQe_z+C'_{\rm free},\quad C(b)=0 .
$$
$\lambda=0$ 的全部未知为零时 (3) 精确满足并恢复 R680。$u$、三张体角和两个自由中心斜率在新实际输入上同时优化。$\lambda=1$ 的 $e$ 是严格径向函数，仍须 (3) 及实际 $F$ 等距检验通过；设计参数到一不授此结论。基相位满足目标时，正向材料角平移和空间刚体给整族 $F_\alpha$，两端位移支撑及真实远刚帽沿用 R680 的几何门。

## 完整解析导数和实际几何门

体角某列的空间无穷小旋转记 $Z=fV$，$V$ 是转动之前的实际那根体轴。于是
$$
 \delta G=Z\times G+Z_\varphi\times(eP)-rZ_r\times T,\quad
 \delta d=-\langle e Z\times P\rangle,
 \quad \delta \bar T=\langle Z\times T\rangle .
$$
径向对数列给 $\delta G=f(eP)_\varphi,\delta d=-f\overline{eP}$。两个自由中心斜率直接进入 $d$。实际求解还保全相反两母线全角端切向长度、中央位置微分与两侧光滑曲率保护。一般未解候选的标架二基读数为
$$
 A=P_r\cdot n/e,\quad B=(P_\varphi\cdot n/r+T_r\cdot n/e)/2,
 \quad K=T_\varphi\cdot n/r .
$$
在准确解处就是正交单位基上的真实二基；任一候选都另从 (3) 重建实际 $F_{ij}$ 和主曲率，不能用这三个保护量替代。体旋转微分中共同刚转项相消，例如 $\delta A=(Z_r\times P)\cdot n/e$，其余两项分别用 $Z_r,Z_\varphi$。以两侧 $I\pm .03\begin{psmallmatrix}A&B\\B&K\end{psmallmatrix}$ 的迹与行列式以及双轴法向构成光滑保护。每个可接受步须通过工作及独立细网的真实 $F$ 曲率、双轴正法向、远帽净空、支撑和整像直径。以后要赋全点资格仍须在连续域封闭相应不等式。

在有限角网 $N$ 上，周期原函数采用 $I_N$。其插值面有 $(F_N)_{\varphi\varphi}=rD_N T$；连续定义 (3) 则为 $F_{\varphi\varphi}=rT_\varphi$。运行用同一候选的两种角二阶分别计算曲率门，并分列两者峰值与位置，后一种仍含其余原函数及均值的数值近似。独立读数比较 $N,3N$ 对同一 $T,T_r,T_{rr}$ 的三个均值及三个原函数。两端完整位置、中心、$F_r,F_\varphi,F_{rr},F_{r\varphi},F_{\varphi\varphi}$ 的刚圈误差逐项记录；正反射母线另读材料帧 $\int P_r\cdot n$ 与实际曲线 $\int (F_{rr}\cdot n_F)/|F_r|$，未解时两者应分列。
