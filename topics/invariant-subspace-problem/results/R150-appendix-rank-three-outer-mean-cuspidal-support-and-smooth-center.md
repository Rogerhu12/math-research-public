# R150 附录：外均值降秩截面的尖点三次与光滑二次曲面中心

日期：2026-11-13（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明的完整降秩归约。** 在原非割线均值、第三矩本质维数三且均值位于其外的完整临界截面中，若 $H$ 不满秩，则其秩准确为三。唯一长度四支撑中，$\lambda$ 只能在一个简单支点为零；剩余长度三支撑上的原中央二元三次必须有一个二重根和一个单根。三重剩余支点全部排除；另外两型必须有指定单点权等于 $1/2$。原三维物理像是不可约尖点三次曲线，且完整二阶梯度给出的四维二次曲面仍非零、中心仍光滑。以下均为原完整临界点的必要条件，尚未把剩余两型判为存在或不存在。

## 1. 从原有限支撑证明局部乘法的秩

本稿始终假设
$$
\nabla\mathcal Q_3=0,\qquad
\operatorname{rank}(y_{j+k})_{0\le j\le3,\ 0\le k\le2}=3,\qquad
\operatorname{ess}(T_3)=W,\quad\dim W=3,\quad y\notin W,
\tag{1.1}
$$
其中 $T_3(r)=y(r)^3-6y(r)H(r,r)+4V(r,r,r)$。由[原四 jets 支撑归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)，有唯一准确长度四的物理除子 $g$，其 jet 空间
$$
E=W\oplus\mathbb Cy
$$
同时支撑 $y,H,V$，并有唯一 $\lambda\in E^*$ 满足
$$
\lambda|_W=0,\quad\lambda(y)=1,\qquad
H=2V\lambda,\quad y=8V\lambda\lambda,\quad V(\lambda,\lambda,\lambda)=1/8.
\tag{1.2}
$$
每个局部块的最高 $V$ jet 系数均非零。

设各支点局部长度为 $n_i$，令
$$
\mathcal A=\bigoplus_i\mathbb C[\varepsilon_i]/(\varepsilon_i^{n_i}),
\qquad\sum_i n_i=4.
$$
选择每个物理曲线点附近的非零齐次代表和局部参数；这包括无穷远，不改变原 $K$ 或任何张量。次数五的线性坐标限制到长度四除子是满射，因此 $E^*$ 与 $\mathcal A$ 识别。原 $V$ 准确由一个泛函 $\Lambda$ 表示：
$$
V(f_1,f_2,f_3)=\Lambda(f_1f_2f_3).
\tag{1.3}
$$
各局部最高系数非零说明 $(f,h)\mapsto\Lambda(fh)$ 非退化：在长度 $n$ 块，按 $1,\varepsilon,\ldots,\varepsilon^{n-1}$ 排列，其配对矩阵的反对角线均为非零的 $\Lambda(\varepsilon^{n-1})$，高侧为零。故 $\Lambda$ 是这里的 Frobenius 泛函；没有正性假设。

把 $\lambda$ 也视为 $\mathcal A$ 的一个元素，并令 $a_i$ 为其在第 $i$ 块的消失阶；零元素取 $a_i=n_i$。由 (1.2)、(1.3)，
$$
H(f,h)=2\Lambda(\lambda fh),\qquad y(f)=8\Lambda(\lambda^2f).
$$
乘以非退化的 Frobenius 配对矩阵可见
$$
\operatorname{rank}H=\operatorname{rank}M_\lambda
=\sum_i\max(n_i-a_i,0).
\tag{1.4}
$$
同理，$y$ 在这个已固定的 $g$ 内部的有效物理 jet 长度准确为
$$
d_y=\sum_i\max(n_i-2a_i,0).
\tag{1.5}
$$
后一准确性也可逐块检查：若 $2a_i<n_i$，$y$ 的最高剩余 jet 系数是原最高系数乘以 $\lambda$ 首个非零系数的平方，因而非零；若 $2a_i\ge n_i$，该块全消失。总长度至多四的物理 jets 在 $\mathbb C^6$ 中独立，不能发生该固定支撑内部的跨块消去。这里不预先断言它是所有其他可能支撑中的最小长度；后面只使用这个有效支撑给出的上界。

(1.1) 的 Hankel 秩三排除长度至多二的均值支撑。因此 $d_y\ge3$。若 $H$ 不满秩，至少一个 $a_i>0$；(1.5) 又给
$$
\sum_i\min(2a_i,n_i)\le1.
$$
所以恰有一个块满足 $a_i>0$，该块长度只能是一，其他块的 $\lambda$ 都是单位。于是
$$
\boxed{
g=s_0+D,\quad s_0\notin\operatorname{supp}D,\quad\deg D=3,\quad
\lambda(v(s_0))=0,\quad\lambda\text{ 在 }D\text{ 上可逆},\quad
\operatorname{rank}H=3.
}
\tag{1.6}
$$
这里 $s_0$ 是一个简单支点，$D$ 可暂时包含重 jets。令 $u_0$ 为其非零物理代表，$U=E_D$，则
$$
E=U\oplus\mathbb Cu_0,\qquad
y,H\text{ 支持于 }U,\quad H|_U\text{ 秩三},\qquad
V=V_D+c\,u_0^3,\quad c\ne0.
\tag{1.7}
$$

## 2. 剩余长度三上的原中央二元三次

在 $D$ 上按同一个 $\lambda$ 归一。具体地，若原坐标限制为 $f$，令 $X=f/\lambda$，并定义
$$
\tau(X)=8\Lambda_D(\lambda^3X).
$$
$\lambda$ 为单位且 $\Lambda_D$ 的最高系数非零，所以 $\tau$ 的乘积配对仍非退化；(1.2) 给 $\tau(1)=1$。逐项从原矩得到
$$
y(f)=\tau(X),\qquad H(f,f)=\frac14\tau(X^2),\qquad
V_D(f,f,f)=\frac18\tau(X^3).
$$
因此
$$
\boxed{
T_3=C_D+4c\,u_0^3,\qquad
C_D(X)=\frac12\tau\bigl((X-\tau(X)1)^3\bigr).
}
\tag{2.1}
$$
$C_D$ 对常数平移不变，是二维商 $\mathcal A_D/\mathbb C1$ 上的二元三次式。由于 $u_0\notin U$，且 $T_3$ 的本质维数准确为三，$C_D$ 的本质维数准确为二。

在独立坐标中，$T_3$ 是 $4cZ^3+C_D(X_1,X_2)$。它不可约：若其在 $\mathbb C(X_1,X_2)[Z]$ 上可约，三次多项式必有一个根，使 $-C_D/(4c)$ 成为有理函数的立方；二元多项式唯一分解于是迫 $C_D$ 为一次式的立方，违背本质维数二。

原最高梯度使三维物理曲线落在该不可约三次上。光滑平面三次不能被 $\mathbb P^1$ 非恒定参数化，前述支撑归约 §5 已给出正则微分的直接证明。因此该三次必须奇异。其 $Z$ 偏导迫奇点满足 $Z=0$，另两偏导说明 $C_D$ 有重根。因为它不是一个立方，只能准确有一个二重根和一个单根：
$$
\boxed{C_D=\gamma L^2R,\qquad \gamma\ne0,\quad L,R\text{ 独立}.}
\tag{2.2}
$$
所以原三维物理像准确是不可约尖点三次曲线 $4cZ^3+\gamma L^2R=0$，而非节点三次。

## 3. 三种长度三支撑的全部中央必要条件

下面令 $\kappa_3=2C_D$。各权均是复数，所有公式均是原归一后的代数身份。

### 3.1 一个三重支点不可能

取 $\mathcal A_D=\mathbb C[\varepsilon]/(\varepsilon^3)$，记
$$
\tau(1)=1,\quad\tau(\varepsilon)=\alpha,\quad
\tau(\varepsilon^2)=\beta\ne0.
$$
减去常数后取 $X=x\varepsilon+u\varepsilon^2$，置 $\mu=\alpha x+\beta u$。则
$$
\tau(X^2)=\beta x^2,\quad\tau(X^3)=0,\qquad
C_D=\mu\left(\mu^2-\frac32\beta x^2\right).
\tag{3.1}
$$
$\mu,x$ 独立且 $\beta\ne0$，所以这是三个不同一次因子的乘积，与 (2.2) 冲突。故原 $H$ 降秩截面不可能具有 $g=3s+s_0$。

### 3.2 双支点加单点：单点权必须为一半

取 $\mathcal A_D=\mathbb C[\varepsilon]/(\varepsilon^2)\oplus\mathbb C$，双点总权为 $a$，$\tau(\varepsilon)=b\ne0$，单点权为 $1-a\ne0$。减去单点常数后取 $X=(x+u\varepsilon,0)$。直接展开得
$$
\begin{aligned}
\kappa_3={}&a(1-a)(1-2a)x^3
+3b(1-a)(1-2a)x^2u\\
&-6b^2(1-a)xu^2+2b^3u^3.
\end{aligned}
\tag{3.2}
$$
普通二元三次判别式准确为
$$
\operatorname{disc}\kappa_3=108b^6(1-a)^2(1-2a).
\tag{3.3}
$$
由于 $b(1-a)\ne0$，重根准确迫 $a=1/2$，即剩余单点的权为 $1/2$。此时
$$
\boxed{\kappa_3=b^2u^2(-3x+2bu),}
\tag{3.4}
$$
二重与单根确实不同。原总支撑只能是 $2s+t+s_0$，其中缺失点 $s_0$ 与另两个点不同，且活跃单点 $t$ 的归一权为 $1/2$。

### 3.3 三个不同支点：恰一个权为一半

取三个非零权 $a,b,c$，其中 $a+b+c=1$。在 $X=(x,u,0)$ 的商坐标中，
$$
\begin{aligned}
\kappa_3={}&a(1-a)(1-2a)x^3
+3ab(2a-1)x^2u\\
&+3ab(2b-1)xu^2+b(1-b)(1-2b)u^3.
\end{aligned}
\tag{3.5}
$$
精确判别式是
$$
\boxed{\operatorname{disc}\kappa_3
=27a^2b^2c^2(1-2a)(1-2b)(1-2c).}
\tag{3.6}
$$
因此至少一个权等于 $1/2$；两个权同时为一半会迫第三权为零，故准确只有一个。若 $a=1/2$，则
$$
\kappa_3=b(1-2b)u^2
\left(-\frac32x+(1-b)u\right),
\tag{3.7}
$$
其二重、单根不同，因为 $b,c\ne0$。式 (3.3)、(3.6) 可直接将显示的四个系数代入
$B^2C^2-4AC^3-4B^3D-27A^2D^2+18ABCD$ 展开；无未付的数值或一般位置假设。

综上，降秩只剩总支撑重数 $2+1+1$ 与 $1+1+1+1$ 两型，且活跃长度三部分具有上述准确半权条件。

## 4. 二次关系仍非零，且中心仍光滑

继续使用[原完整低梯度](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)的记号
$$
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky,\quad
M=H-\tfrac14yy^{\mathsf T},\qquad
N=T_{3,p}-FT_2+4HKH.
$$
其已证身份为
$$
\operatorname{tr}(KM)=-F/2,\qquad
N=T_{3,p}+2FM+4MKM+y(Mp)^{\mathsf T}+(Mp)y^{\mathsf T},
\tag{4.1}
$$
而原二阶临界性给
$$
v(z)^{\mathsf T}KNKv(z)\equiv0.
\tag{4.2}
$$

由 $H|_U$ 秩三、$H\lambda=y/4$ 及 $\lambda(y)=1$，$M$ 的秩准确为二，且
$$
\operatorname{Ran}M=U_0:=U\cap\ker\lambda,\qquad
W=U_0\oplus\mathbb Cu_0,\quad U=\mathbb Cy\oplus U_0.
\tag{4.3}
$$
$M$ 在 $U_0$ 的二阶张量块可逆，$C_D$ 的本质支撑正是 $U_0$。

反设 $N=0$。式 (4.1) 的前三项在 $\operatorname{Sym}^2W$ 中，$y\notin W$，故跨项迫 $Mp=0$。因此 $p$ 湮灭 $U_0$，并由 (2.1) 得
$$
T_{3,p}=4c(y^{\mathsf T}Ku_0)u_0^2.
$$
比较 $u_0^2$ 与 $\operatorname{Sym}^2U_0$ 两块，得到
$$
y^{\mathsf T}Ku_0=0,\qquad MKM=-FM/2.
\tag{4.4}
$$
在可逆的二维 $M$ 块中取迹，后式给 $\operatorname{tr}(KM)=-F$，与 (4.1) 比较迫 $F=0$。继而 $K|_{U_0}=0$、$y\perp_K U_0$、$y^{\mathsf T}Ky=0$，即整个三维 $U$ 全等向。

设 $D$ 的齐次三次方程为 $G_D$。因为 $U=E_D$ 全等向，全部 $U$ 极线 $u^{\mathsf T}Kv(z)$ 都被 $G_D$ 整除，且包括每个重 jet 的重数。最高条件
$$
C_D(Kv(z))+4c\bigl(u_0^{\mathsf T}Kv(z)\bigr)^3=0
$$
于是迫 $G_D^3$ 整除第二项，也就是 $G_D$ 整除 $u_0^{\mathsf T}Kv(z)$。这准确说 $u_0\perp_K U$。六维非退化 $K$ 的三维全等向空间满足 $U^{\perp_K}=U$，所以 $u_0\in U$，与 (1.7) 冲突。因此
$$
\boxed{N\ne0.}
\tag{4.5}
$$

若仅假设 $Mp=0$，则 (4.1) 已使 $N\in\operatorname{Sym}^2W$。但 §2 已证明三维物理像是不可约三次曲线；它不能满足非零二次方程，故 (4.2) 迫 $N=0$，又与 (4.5) 冲突。因此
$$
\boxed{Mp\ne0.}
\tag{4.6}
$$
(4.1) 收缩 $\lambda$ 给 $N\lambda=Mp$、$\lambda^{\mathsf T}N\lambda=0$，所以原投影中心 $[\lambda]$ 位于该非零二次曲面上，且为光滑点。原四维物理曲线张成 $\mathbb P(E^*)$，故该二次关系不能是两个平面的并；其秩至少三。

这证明[满秩情形的光滑中心结论](R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md)在本稿准确降秩类中仍成立；这里用了降秩类的原尖点三次与最高条件，没有直接挪用满秩证明。

## 5. 原极线的尖点除子与中心支撑限制

不可约三次像的参数化由三个五次式给出。若其公共因子次数为 $\delta_W$、覆盖次数为 $d$，拉回一条一般直线给
$$
5-\delta_W=3d.
$$
因此 $\delta_W=2,d=1$。记公共二次因子为 $G$。令 $L,R$ 为 (2.2) 的物理向量，并设
$$
p_0=u_0^{\mathsf T}Kv,\quad \ell=L^{\mathsf T}Kv,\quad r=R^{\mathsf T}Kv.
$$
除去 $G$ 后三个二元三次式无共同因子，且满足
$$
4c(p_0/G)^3+\gamma(\ell/G)^2(r/G)=0.
$$
若 $\ell/G,r/G$ 有公共根，则 $p_0/G$ 也有该根，矛盾。唯一分解于是迫存在两个独立一次式 $a,b$ 与非零常数，使
$$
\boxed{
\ell/G=\alpha a^3,\qquad r/G=\beta b^3,\qquad
p_0/G=\rho a^2b.
}
\tag{5.1}
$$
这是原缺失支点极线的准确尖点因式，不仅是抽象平面曲线的名称。

[任意长度四投影的单基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)给四维公共因子次数 $\delta_E\le1$。故投影到 $W$ 所增加的中心除子长度为 $2-\delta_E$，即二或一。它不能经过 $D$ 的任何支持点。证明如下：在 $\sigma\in D$，$\lambda(v(\sigma))\ne0$；若四维投影在 $\sigma$ 无基点，其值作为 $E$ 上的泛函在 $v(\sigma)$ 上为 $v(\sigma)^{\mathsf T}Kv(\sigma)=0$。若有基点，只有一个简单基点，除去后投影值在该向量上为 $v(\sigma)^{\mathsf T}Kv'(\sigma)=0$。两种情形都不可能正比于 $\lambda$。因此中心除子与原 $g$ 相交时，只可能经过缺失的简单支点 $s_0$；没有宣称该点本身也已被排除。

## 6. 缺失点上的完整一次条件

本稿还保留一个必须与上述几何同时使用的低阶条件。原一次梯度为
$$
\frac13K^{-1}\nabla_y\mathcal Q_3
=(F^2-2b+2\tau_2)y-4FHp+8HKHp
 +4V(p,p,\cdot)-8V:(KHK).
$$
除 $V$ 的 $c u_0^3$ 块外，右边全部位于 $U$ 中；该块在 $u_0$ 方向的系数准确为
$$
4c\left((y^{\mathsf T}Ku_0)^2-2u_0^{\mathsf T}KHK u_0\right).
$$
由 $c\ne0$ 及 $u_0\notin U$，完整一次临界性迫
$$
\boxed{T_{2,D}(Ku_0)=0.}
\tag{6.1}
$$
原物理点本身有 $u_0^{\mathsf T}Ku_0=0$；最高恒等式在该点又给
$$
\boxed{C_D(Ku_0)=0.}
\tag{6.2}
$$
此外原平方的完整标量值 $F^2-2b+2\tau_2=0$ 仍由同一 $\lambda$ 收缩一次梯度得到。以上条件来自同一组原矩，不能自由挑选相互独立的中央权或尖点参数。

剩余任务是：对总支撑 $2+1+1$ 与四不同点的上述准确半权、尖点、光滑二次中心类型，同时解原极化核及全部低梯度。本稿已排除其余所有降秩支撑，但没有将剩余必要条件当作充分条件，也未给全局自然幂证书或实际算子逆。
