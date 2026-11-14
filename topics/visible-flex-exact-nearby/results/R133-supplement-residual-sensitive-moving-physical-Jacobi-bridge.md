# R133：moving 与物理 Jacobi 的完整互逆及真实残差接线

**已证明（全 Fourier、完整平均、近似中心的准确恒等式）。** 这里解决一个
实际接口问题：moving 系统的大幅简化可以用于真实主体能量，但把该能量
接到原物理角的根块时，近似中心的残差不能设为零。两种 Jacobi 算子之间
除准确变分换角外，还有一个明确的二阶坐标变分项。本篇把它分成真实小
残差引起的共同输运及有界零阶项，并保留其完整平均。

这些恒等式不需要状态变分是有限 Fourier 多项式，也不要求中心的角斜率
很小。只要求实际 $v$ 与0分离、反射归一成立以及所写系数具有所需正则性。

## 1. 状态变换和完整变分互逆

沿用 moving 系统的定义。基场 $Q=(u,v)$ 已写在计算角 $\phi$ 上，
$v<0$，$u$ 奇、$v$ 偶，周期 $\pi/2$；$m=\langle v\rangle_\phi<0$。
反向物理角为

$$\theta_\phi=v/m,\qquad \theta(r,0)=0.$$

$I=\partial_\phi^{-1}P_0$ 是零均值周期原函数。设 $k$ 为**固定物理角**
的变分拉回当前 $\phi$ 圆后的函数，$h$ 为固定 $\phi$ 的 moving 变分，
$z=\langle h_2\rangle_\phi$。那么

$$
\boxed{h=T_Qk=k+Q_\phi I(k_2/v),\qquad
z=m\langle k_2/v\rangle_\phi.}\tag{B.1}
$$

准确逆为

$$
\boxed{k=h-Q_\phi\chi,
\qquad \chi=\frac1v I\left(h_2-\frac zmv\right).}\tag{B.2}
$$

证明可直接微分 $\theta_\phi=v/m$。对 (B.2)，令
$J=I(h_2-zv/m)$，则 $\chi=J/v$ 是奇函数，且

$$\frac{k_2}{v}=\chi_\phi+z/m.$$

所以 $I(k_2/v)=\chi$，代回 (B.1) 便得到 $h$；其平均也准确给 $z$。
反向将 (B.1) 代入 (B.2) 同样成立。这个证明不使用 Neumann 小量条件，
也没有以 $z=0$ 删除平均列。

### 完整有界端口变换

在某个实径向端口任取权 $q>0$，记

$$\mathcal E=\|\operatorname{diag}(1,q)h\|_2,\quad M=|z|,
\quad g\le|v|,\quad V_2=\|v\|_2,\quad
L=\|\operatorname{diag}(1,q)Q_\phi\|_\infty.$$

由四重原函数的完整范数 $\|I\|_{2\to2}=1/4$，有

$$\|\chi\|_2\le\frac1{4g}
\left(\frac{\mathcal E}{q}+\frac{V_2}{|m|}M\right).
\tag{B.3}$$

于是逆变换的完整能量满足

$$\|\operatorname{diag}(1,q)k\|_2
\le\left(1+\frac{L}{4gq}\right)\mathcal E
+\frac{LV_2}{4g|m|}M.\tag{B.4}$$

若 $F=\|\operatorname{diag}(1,q)k\|_2$，正向变换给

$$
\binom{\|\operatorname{diag}(1,q)T_Qk\|_2}
{|\langle(T_Qk)_2\rangle|}
\le
\binom{1+L/(4gq)}{|m|/(gq)}F.
\tag{B.5}$$

这些是完整允许奇偶空间上的端口界。负型能量中取 $q=\sqrt{-K}$；在根
点本身可改取普通正权 $q=1$，因为 (B.1)–(B.5) 不含任何 $1/K$。不能把
退化的 $q=0$ 能量当作根端完整二维范数。

## 2. 近似中心的准确 Jacobi 恒等式

将物理状态换成 moving 状态的非线性映射记为 $\mathcal H$。它本身不
显含 $r$ 或度量参数；其对物理场的导数正是 $T_Q$（并包括把物理函数
拉回当前 $\phi$ 圆）。设物理方程为 $Q^{\rm phys}_r=G(Q^{\rm phys})$，
moving 方程为 $Q_r=F(Q)$。完整等价性给

$$F(\mathcal H(Q^{\rm phys}))=
D\mathcal H(Q^{\rm phys})G(Q^{\rm phys}).$$

对一个实际近似中心，令 $R$ 为其物理残差
$Q^{\rm phys}_r-G(Q^{\rm phys})$ 拉回 $\phi$ 后的两分量。定义

$$\mathcal J_{\rm phys}k=k_r-DG[k],\qquad
\mathcal J_{\rm mov}h=h_r-DF[h].$$

第一式的径向导数在固定物理 $\theta$ 下先计算，再把结果拉回；第二式在
固定 $\phi$ 下计算。不能把第一式误读成拉回函数的固定 $\phi$ 径向导数。

链式法则及 $D^2\mathcal H$ 的对称性给准确关系

$$
\boxed{\mathcal J_{\rm mov}(T_Qk)
=T_Q\mathcal J_{\rm phys}k+D^2\mathcal H[R,k].}
\tag{B.6}$$

确实，沿近似中心求 $T_Qk$ 的径向导数时，中心速度为 $G+R$；其中 $G$
部分与 $DF$ 中的同一二阶项相消，剩下的恰为 $D^2\mathcal H[R,k]$。
只有真实 $R=0$ 时，才可删除这一项。

## 3. 二阶项的完整公式与平均

设

$$b=R_2/v,\qquad e=Ib,\qquad
a=k_2/v,\qquad \psi=Ia.$$

直接微分 (B.1)，用反射使 $\langle\psi b\rangle=0$，得到对称式

$$\begin{aligned}
D^2\mathcal H[R,k]={}&R_\phi\psi+k_\phi e
+Q_{\phi\phi}\psi e\\
&+Q_\phi\{ae+b\psi-2I(ab)\}.
\end{aligned}\tag{B.7}$$

这里的 $a,b$ 包含其实际平均；只有明确写出的 $I$ 才作用零均值投影。
代入 $k=h-Q_\phi\chi$、$\psi=\chi$ 与
$a=\chi_\phi+z/m$，再做一次准确周期分部积分，得到更适合能量的形式

$$
\boxed{D^2\mathcal H[R,k]
=e h_\phi+R_\phi\chi
+Q_\phi\left\{-b\chi+2I(b_\phi\chi)-\frac zm e\right\}.}
\tag{B.8}
$$

因此唯一含 $h_\phi$ 的新增项是一个**共同实输运速度** $e$，并非裸
$\gamma u_\theta$ 或一般高阶耦合。余项在 $L^2$ 上为有界零阶或有界
原函数算子，只需要真实残差的一阶角导。不能把尚未分离输运项的整个
$D^2\mathcal H[R,\cdot]$ 称作 $L^2$ 上的有界零阶算子。

其第二分量的完整平均进一步准确化简为

$$\boxed{\left\langle(D^2\mathcal H[R,k])_2\right\rangle
=2m\langle b_\phi\chi\rangle.}\tag{B.9}$$

一种独立核对是对 $m=\langle1/v^{\rm phys}\rangle_\theta^{-1}$ 求两次
变分：二阶平均等于 $2m(\langle a\rangle\langle b\rangle-\langle ab\rangle)$。
代 $a=\chi_\phi+z/m$ 后即为 (B.9)。故这里没有把某个真实平均残差
误当成零；恰是相关的两项准确相消。

## 4. 可直接消费的二维残差费用

只在严格负区间上取 $q=\sqrt{-K}$，沿用 moving 定理的 $L,g,V_2,m$。
记完整实际量

$$
B_0=\|b\|_\infty,\quad B_1=\|b_\phi\|_\infty,\quad
E_0=\|e\|_\infty,\quad E_1=\|e_\phi\|_\infty,\quad
L_R=\|\operatorname{diag}(1,q)R_\phi\|_\infty,
$$

以及 $Z_R=L_R+L(B_0+B_1/2)$。由于 $I$ 的完整 $L^2$ 范数为 $1/4$，
(B.8) 中零阶部分的能量至多

$$Z_R\|\chi\|_2+(LE_0/|m|)M.$$

共同速度 $e h_\phi$ 的能量分部积分只付 $E_1/2$。结合 (B.3)、(B.9)，
在原 moving 二维比较矩阵上加如下完整非负矩阵即可：

$$
\boxed{
\Delta\mathcal A_R=
\begin{pmatrix}
E_1/2+Z_R/(4gq)&Z_RV_2/(4g|m|)+LE_0/|m|\\
|m|B_1/(2gq)&V_2B_1/(2g)
\end{pmatrix}.}\tag{B.10}
$$

实际物理源 $f$ 先拉回当前 $\phi$，再按 (B.5) 给完整两行源费用。
精确地，$\langle(T_Qf)_2\rangle=m\langle f_2/v\rangle$。若只知道
原物理角的 $L^2_\theta$ 范数，还须支付密度
$d\phi=(m/v)d\theta$；若已知全角上确界或完整 $A_0$，则直接控制该
拉回的 $L^2_\phi$，因为真实平均密度为1。

可用的粗替代为 $E_1\le2B_0$；零均值原函数的周期 Green 核给
$E_0\le(\pi/8)B_0$。实际数值若更紧，应直接使用真实 $e,e_\phi$ 的界。
$B_1$ 及 $L_R$ 不能只用无角导的残差上界代替。

这给一个实用区别：完整 moving 方程自身的 Jacobi 直接使用原二维比较；
若要把它作为**同一近似中心的物理 Jacobi**常数，则必须进一步支付
(B.10)。本篇没有用“残差很小”省略该门。

## 5. 端口、接缝和参数范围

在共同实解析片内，(B.6) 可以逐点使用；因此可把严格负段的 moving
输入与原物理角的根块两迹准确接线。参数源不另设为零：对 unnormalized
物理 $(u,v)$ 的全部目标源先保留，再由同一个 $T_Q$ 转换。若从归一化
$(U,V,\alpha,\nu)$ 出发，必须先用
$\delta u=\alpha\delta U+U\delta\alpha$、
$\delta v=\alpha\delta V+V\delta\alpha+\delta s$。

对于径向分片中心，需要区分所选择的完整方程。若在 moving 区域直接
解 moving 方程，则其真实仿射接缝仍是 M.16–M.17 的
$-[\widehat Q]$，齐次未知量在共同 $\phi$ 圆上连续。若从一个已有的
**物理** Jacobi 接缝变换而来，则齐次接线准确为
$T_+\mathcal P T_-^{-1}$，其中 $\mathcal P$ 是两侧曲率角之间对同一
物理函数的复合；不能因为 PPoly 跳很小就把这个无限维接线默认为恒等。
本篇没有删除它。当前真实根盒已严格落在候选同一片内部，故可选择根
外接切口避开这类分片歧义。

实际闭合仍需消费完整连续的普通源及其一阶角导、上述两端口和真实帽
边界，并继续处理返回小除数。本篇提供准确全频接口，未预先宣称这些
尚未执行的数值费用已闭合。
