# R44. 偶三重圆弧相容控制空间的两维补全

状态：**已证明**。本条只给出控制函数空间的精确分解、两列明确函数和项目坐标下的圆半径/圆心作用。它不证明非线性 BVP 可解、正曲率、完整 metric 或本题比例；既有 R38/R41 的具体几何数值不随新列自动继承。

## 1. 圆弧条件比“支撑增量在弧上为零”多两个自由度

取

$$
T=\frac{2\pi}{3},\qquad L=\frac\pi3,\qquad\phi_0=L,
\qquad0<a<a+b<L.
$$

记 $d(\phi)$ 为 $\phi-\phi_0$ 在 $[-L,L)$ 的周期代表。保护弧及其三重重复记为
$I=\{|d|\le a\}$。所有函数都为实值、$2\pi$ 周期，以下 $C^4$ 指全圆周的正则性。
使用归一化内积

$$
\langle f,g\rangle=\frac1{2\pi}\int_0^{2\pi}f(\phi)g(\phi)\,d\phi,
\qquad e_0=1,\quad e_1=\cos3\phi.
$$

定义

$$
\mathcal X=\{f\in C^4:\ f(\phi+T)=f(\phi),\
 f(2\phi_0-\phi)=f(\phi),\
 \langle f,1\rangle=\langle f,\cos3\phi\rangle=0\},
$$

$$
\mathcal X_0=\{f\in\mathcal X:f|_I=0\},\qquad
\mathcal X_{\rm circ}=\{f\in\mathcal X:(f+f'')|_I\text{ 为常数}\}.
$$

三重周期保证三个保护弧上的常数相同。$\mathcal X_0$ 是**全 $C^4$ 空间中**满足上述条件的弧上零函数空间；这里没有要求 $f/W$ 存在或属于某个光滑空间，也没有把它等同有限 raw 列的张成空间或其闭包。

**定理。** 存在下文明确构造的 $S_A,S_B\in\mathcal X_{\rm circ}$，使

$$
\boxed{\mathcal X_{\rm circ}=\mathcal X_0
 \ \oplus\ \operatorname{span}\{S_A,S_B\}.}
$$

在保护弧上，它们分别等于 $1$ 和 $\cos d$。对任何 $f\in\mathcal X_{\rm circ}$，唯一分解为

$$
f=f_0+A(f)S_A+B(f)S_B,\qquad f_0\in\mathcal X_0,
$$

$$
A(f)=f(\phi_0)+f''(\phi_0),\qquad B(f)=-f''(\phi_0).
$$

因此，在固定主核后，原先把全部控制限制为弧上恒零，恰好额外固定了圆弧的两个局部几何参数。

## 2. 与现有低两矩定义一致的显式两列

取原控制窗口的九次 C4 smoothstep

$$
P(t)=126t^5-420t^6+540t^7-315t^8+70t^9.
$$

令 $\chi$ 在 $|d|\le a$ 上为 1，在 $|d|\ge a+b$ 上为 0，在中间为

$$
\chi(\phi)=1-P\!\left(\frac{|d(\phi)|-a}{b}\right),\qquad W=1-\chi.
$$

$P(0)=0,P(1)=1$，且两端一至四阶导数均为零，所以 $\chi,W$ 全局为 $C^4$、偶对称且三重周期。
由于 $a+b<L$，$\chi$ 在周期代表接缝 $d=\pm L$ 的一个邻域上恒零。

定义两个种子

$$
u_A=\chi,\qquad u_B=\chi\cos d.
$$

**$\cos d$ 是局部角差的余弦，不是全局谐波 $\cos3\phi$。**
这里先将它乘以在接缝邻域恒零的 $\chi$，再作三重周期重复，故 $u_B$ 仍为全局偶/C3 的 $C^4$ 函数。

取同一低两矩 Gram

$$
G_{ij}=\langle W e_i,e_j\rangle,\qquad i,j=0,1,
$$

并将两个右端按**列**排成 $V_{iA}=\langle u_A,e_i\rangle$、
$V_{iB}=\langle u_B,e_i\rangle$。令 $D=G^{-1}V$，其中 $D$ 的行对应
$e_0,e_1$，列对应 $A,B$。设

$$
S_A=u_A-W(D_{0A}+D_{1A}\cos3\phi),\qquad
S_B=u_B-W(D_{0B}+D_{1B}\cos3\phi).
$$

对任意非零 $(z_0,z_1)$，

$$
z^\mathsf TGz=\langle W(z_0+z_1\cos3\phi)^2\rangle>0.
$$

理由是 $W>0$ 的补弧含开区间，$\cos3\phi$ 在其中不恒定，非零一次多项式不可能在整个该区间上为零。因此 $G$ 严格正定，两个列都唯一确定。
矩方程 $GD=V$ 给出

$$
\langle S_A,1\rangle=\langle S_A,\cos3\phi\rangle
=\langle S_B,1\rangle=\langle S_B,\cos3\phi\rangle=0.
$$

在闭保护弧上 $W=0,\chi=1$，且所需端点导数相合，于是

$$
S_A=1,\quad S_A+S_A''=1,\qquad
S_B=\cos d,\quad S_B+S_B''=0.
$$

为把符号与实际 $\phi_0=\pi/3$ 源定义锁定，记

$$
I(\omega)=\frac2T\int_0^{a+b}\chi(d)\cos(\omega d)\,dd.
$$

在这一扇区 $\cos3\phi=-\cos3d$，所以明确地

$$
G=\begin{pmatrix}
1-I(0)&I(3)\\
I(3)&\tfrac12[1-I(0)-I(6)]
\end{pmatrix},\qquad
V=\begin{pmatrix}
I(0)&I(1)\\
-I(3)&-\tfrac12[I(2)+I(4)]
\end{pmatrix}.
$$

这与当前 raw 基的 $\langle W e_i,e_j\rangle$ 使用同一归一化和符号。
源码 `circle_trace_controls.py` 按这些积分及 $2\times2$ 逆定义两个新列，数值求值另标精度。

## 3. 直和证明及其确切范围

设 $f\in\mathcal X_{\rm circ}$，在 $I$ 上 $f+f''=A$。偶对称给
$f'(\phi_0)=0$。常系数方程的一般解以及这个初值说明

$$
f(\phi_0+d)=A+B\cos d,
\quad B=f(\phi_0)-A=-f''(\phi_0),\quad |d|\le a.
$$

因而 $f-A S_A-B S_B$ 在 $I$ 上恒零，且仍满足全局 C4、偶/C3 和低两矩条件，即属于 $\mathcal X_0$。
若 $A S_A+B S_B\in\mathcal X_0$，在非空开弧上有 $A+B\cos d=0$；
求二阶导数并取 $d=0$ 得 $B=0$，再得 $A=0$，所以分解唯一。

等价地，连续线性映射

$$
\operatorname{Tr}_{\rm circ}(f)
 =\big(f(\phi_0)+f''(\phi_0),-f''(\phi_0)\big)
$$

在 $\mathcal X_{\rm circ}$ 上满射到 $\mathbb R^2$，核恰为 $\mathcal X_0$，
两个新列分别给 $(1,0)$ 与 $(0,1)$ 的明确右逆。
整个证明不对 $W$ 作除法，因此没有使用其在弧边的平坦阶数来偷换全 C4 零迹空间。

对目前有限 raw 空间，另外令

$$
V_M=\operatorname{span}\{B_j:2\le j\le M\}\subset\mathcal X_0,
\quad
B_j=W(\cos(3j\phi)-c_{0j}-c_{1j}\cos3\phi).
$$

这些列线性独立：任何线性组合为零时，在 $W>0$ 的开区间上，
相应有限三角多项式恒零，继而其所有高次余弦系数为零。因此
$\dim V_M=M-1$，并且

$$
V_M\oplus\operatorname{span}\{S_A,S_B\}
\quad\text{维数为 }M+1.
$$

这只是有限空间的两维扩张，不声称 $V_M$ 穷尽 $\mathcal X_0$。
若为保持原参数个数而在 $M\ge3$ 时用两新列替换原最高两列，例如

$$
\widetilde V_M=\operatorname{span}\{B_2,\ldots,B_{M-2},S_A,S_B\},
$$

则 $\dim\widetilde V_M=M-1$，而

$$
V_M\cap\widetilde V_M=\operatorname{span}\{B_2,\ldots,B_{M-2}\}.
$$

故这是**改变有限控制空间**，不是原 $V_M$ 的可逆坐标变换。参数计数也不证明新 BVP Jacobian 满秩或存在性；新增两列而不替换时，则须明确处理新增的两个未知量。

## 4. 从项目实际法向约定推导半径与圆心

项目使用

$$
e_r=(\cos\phi,\sin\phi),\quad e_\theta=(-\sin\phi,\cos\phi),
\quad\Gamma=h e_r+h'e_\theta,\quad\rho=h+h''.
$$

令 $\nu_0=e_r(\phi_0)$。对支撑增量 $f=A S_A+B S_B$，在保护弧上
$f=A+B\cos d$、$f'=-B\sin d$，所以

$$
\begin{aligned}
\Delta\Gamma
 &= A e_r+B(\cos d\,e_r-\sin d\,e_\theta)\\
 &=\boxed{A e_r+B\nu_0},\qquad \Delta\rho=A.
\end{aligned}
$$

因此若旧圆弧写为 $\Gamma=O+R e_r$，新弧为

$$
\Gamma_{\rm new}=(O+B\nu_0)+(R+A)e_r.
$$

**实际圆心向 $+B\nu_0$ 移动，半径增量为 $A$。**
在本项目大半径轴的另一种记号 $O=-c\nu_0$ 下，才是
$c_{\rm new}=c-B$。不能把这个 $c$ 的符号当成实际圆心向量的符号。
几何圆弧还须 $R+A>0$；本线性构造本身不保证整个新核心的 $\rho$ 正性。

低均值与偶/C3 条件也保留原弧中心的材料原点：若 $u(0)=0$、$u'=h+h''$，
则 $\int_0^{\phi_0}(f+f'')=0$。这是因为半扇区积分为零，且反射对称给
$f'(0)=f'(\phi_0)=0$。所以 $u(\phi_0)$ 不变，但弧内材料角尺度会随 $R+A$ 改变。

## 5. 可复现定义与没有继承的结论

`scripts/resume_m3/circle_trace_controls.py` 是独立定义原型，提供两列的支撑函数一至四阶 jet、$\rho$ 至二阶 jet 及实际 $\Delta\Gamma$；没有被当前运行的核心或 BVP 导入。
`probe_circle_trace_controls.py` 用有限全圆求和核低矩、与当前 raw 低 Gram 的身份，并直接核圆心符号。数值检查只检验实现，不作为上述证明的依据；复现参数与输出哈希见 `circle_trace_controls_probe_record.json`。

这些列允许局部圆半径/圆心变化，故既有 R38 的固定圆弧/握持/特征窗常数和 R41 的某个实际全控制界均不能直接搬用。后续若进入生产求解，必须明确有限空间选择、初值、核心正性和完整几何参数，并继续原 BVP、真实尾、全域 metric、闭合和 reach 验收。本条不从函数空间维数或有限初猜推出任何解的存在。
