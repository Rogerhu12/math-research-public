# R133 补篇：完整物理两迹匹配后的周期继承与腰反射

2026-11-13，visible-exact-astra-ac0d。

**已证明的拼接定理。** 若真实 body 的完整 Gauss–Codazzi 解在外圈
与一个已经构造的、单值周期的实际端帽匹配全部物理曲率迹 $B,C$，
则 body 自动继承该端帽的完整 Euclidean 周期框架。再满足腰上的
$B=0$ 和径向度量偶性，即可作 $C^2$ 镜像接合。

本条明确仍须解出的方程：真实 body PDE、与实际端帽的完整 $B,C$
匹配、安装长尾的真实 residual 和最终全域嵌入/reach。一个周期
高度函数、一条驱动帽的局部曲率解或很小的匹配残差都不满足这里
的全部假设。本条不把它们提前升级为闭面。

## 1. 采用同一实际材料坐标和物理标架

设 $I=[0,R]$ 上的固定径向度量为
$$
g=E(r)\,dr^2+a(r)^2\,d\theta^2,\qquad E>0,\quad a>0.
$$
记 $e=\sqrt E$、$b=a'/e$、$\beta=a'/a$、$\gamma=e/a$。
假设系数具有 R126 重建所需的连续一阶度量 jet；在各实际光滑
片上满足完整 Gauss–Codazzi 方程，接缝处相关 metric jet 和第二
形式连续。下面可先对光滑片证明，再由连续端值拼接；不会忽略
尚未支付的 PPoly 跳跃。

第二形式采用同一实际正交标架
$$
X=F_r/e,\qquad Y=F_\theta/a,\qquad \nu=Y\times X,
\qquad \mathrm{II}_{(X,Y)}=
\begin{pmatrix}A&B\\B&C\end{pmatrix}.
\tag{M.1}
$$
$A,B,C$ 是完整实周期函数，满足
$$
AC-B^2=K_g,\qquad
B_r=\gamma A_\theta-2\beta B,\qquad
C_r=\gamma B_\theta+\beta(A-C).
\tag{M.2}
$$
在两场图中 $C\ne0$ 时使用 $A=(K_g+B^2)/C$；此处的 $B,C$
包含所有 Fourier 模和两个 mean。

设实际外帽 $G$ 至少在 $r=R$ 的外侧 collar 上是单值周期的
$C^2$ 等距浸入，使用同一度量和相同方向，并且准确有
$$
B(R,\theta)=B_G(R,\theta),\qquad
C(R,\theta)=C_G(R,\theta),\qquad C_G(R,\theta)\ne0.
\tag{M.3}
$$
Gauss 恒等式立即给 $A(R,\theta)=A_G(R,\theta)$。这里不允许
只匹配非零模，也不允许把完整非线性 regular 关系替换为其线性
中心。真实长尾的高度和通量先按
[完整 Codazzi 边界转换](R119-supplement-Codazzi-boundary-from-actual-regular-tail.md)
产生这些物理迹。

## 2. 从实际帽直接向内重建，周期性无需另猜

以帽在 $R$ 上的实际 $G,X_G,Y_G,\nu_G$ 为边值，逐个角度向内
解完整径向系统
$$
\begin{aligned}
F_r&=eX,& X_r&=eA\nu,\\
Y_r&=eB\nu,& \nu_r&=-e(AX+BY).
\end{aligned}
\tag{M.4}
$$
这是连续系数的有限维线性标架系统和位置积分。正交性由其反对称
连接保持；$\nu=Y\times X$ 的方向也保持。

数据、系数均为 $2\pi$ 周期，故 ODE 唯一性直接给
$$
(F,X,Y,\nu)(r,\theta+2\pi)=(F,X,Y,\nu)(r,\theta).
\tag{M.5}
$$
这同时证明旋转和位置的周期性；不是只验证一个高度分量的周期。

还须验证径向积分确实解决整个二维重建，而不只是逐射线给出曲面。
完整角向标架方程为
$$
\begin{aligned}
X_\theta&=bY+aB\nu,\\
Y_\theta&=-bX+aC\nu,\\
\nu_\theta&=-a(BX+CY).
\end{aligned}
\tag{M.6}
$$
令 $\mathcal O=(X,Y,\nu)$；其行列式为 $-1$，连接矩阵仍反对称。
将 (M.4)、(M.6) 写为 $\mathcal O_r=\mathcal O\Omega_r$、
$\mathcal O_\theta=\mathcal O\Omega_\theta$。完整 (M.2) 正是
这两个矩阵的平坦相容条件。

角向缺陷 $Q=\mathcal O_\theta-\mathcal O\Omega_\theta$ 因而
满足齐次径向方程 $Q_r=Q\Omega_r$。在 $R$，实际帽给 $Q=0$，
故整个 $I$ 上 $Q=0$。位置缺陷 $S=F_\theta-aY$ 则满足
$S_r=eQ_X=0$，且 $S(R)=0$，所以
$$
F_\theta=aY
\tag{M.7}
$$
准确成立。于是 (M.4) 所得 $F$ 的第一、第二形式确实为指定的
$g$ 和 $(A,B,C)$。它是单值周期 $C^2$ 浸入。

这也可表述为完整 Euclidean holonomy 沿平坦连接共轭传递：
实际帽的 holonomy 是恒等，body 因而也是恒等。结论的前提是
(M.3) 已经准确成立；在未匹配的驱动帽上不能提前使用它。

## 3. 外圈实际 $C^2$ 接合与位置常数

在 $R$ 两侧，$F$ 和完整标架由构造一致，metric jet 一致。
一阶导数 $F_r=eX,F_\theta=aY$ 因而一致。二阶导数准确为
$$
\begin{aligned}
F_{rr}&=e'X+e^2A\nu,\\
F_{r\theta}&=a'Y+eaB\nu,\\
F_{\theta\theta}&=a(-bX+aC\nu).
\end{aligned}
\tag{M.8}
$$
由 (M.3) 和 Gauss 给出的 $A$ 一致，这三个二阶导数逐点相同。
因此拼接确实为 $C^2$，不是只拼到第一阶或只匹配法向的一部分。

本构造从实际帽的位置出发，保留其实际 mean 高度。若另一个
body 已用任意初始点重建，可以用一个整体 Euclidean 刚体作用
在一个角点匹配位置和框架；沿 $R$ 的完整角方程唯一性使整个
边界都匹配。只允许这一次整体对齐，不能在不同角度或接缝上
各自调整平移来掩盖未解出的周期条件。

因而，一旦完整物理迹匹配和实际帽本身的安装成立，位置常数
不再产生一个新的函数方程。若两个端帽被预先独立固定在不同
位置，仍须满足那两份额外位置数据；下节使用同一正半面及其
镜像，不引入第二份任意位置约束。

## 4. 腰条件给真实平面和 $C^2$ 镜像

假设腰上准确有
$$
a'(0)=0,\qquad E'(0)=0,\qquad B(0,\theta)=0
\quad\hbox{对所有 }\theta.
\tag{M.9}
$$
第一、第三式代入 (M.6) 给 $X_\theta(0,\theta)=0$，所以
$X(0,\theta)=X_0$ 是固定单位向量。由 $F_\theta=aY\perp X_0$，
腰圈落在某一个固定平面
$$
\Pi=\{x:x\cdot X_0=d_0\}.
\tag{M.10}
$$
(M.5) 已给腰圈实际闭合，未由局部曲率周期性单独猜测闭合。

令 $\mathcal R_\Pi$ 是这个平面的仿射反射，定义
$$
\widetilde F(r,\theta)=
\begin{cases}
F(r,\theta),&r\ge0,\\
\mathcal R_\Pi F(-r,\theta),&r\le0.
\end{cases}
\tag{M.11}
$$
负半侧度量取同一正半侧的偶延拓。其一阶导数在腰匹配：
$F_r=eX_0$ 垂直于平面，反射和 $r\mapsto-r$ 的两个负号抵消；
$F_\theta$ 位于平面且被反射固定。

二阶导数由 (M.8) 检查。在腰 $e'=0$，所以 $F_{rr}=e^2A\nu$
位于 $\Pi$ 的切平面；$F_{r\theta}=0$；$F_{\theta\theta}$ 也
位于该平面。它们分别满足反射接缝所需的偶、奇、偶关系。
因此 (M.11) 为 $C^2$ 精确等距浸入，腰上的第二形式延拓为
$A,C$ 偶、$B$ 奇。

若正半面外侧已由实际端帽封成一个拓扑圆盘，则该圆盘沿腰边界
与自身镜像粘合，得到连通闭曲面；在此圆盘假设下拓扑为球面。
这一闭浸入结论没有自动给全局单射。

## 5. 均值、四重对称与嵌入仍应准确区分

在腰平面选择定向后，(M.6) 给切向转角
$\psi'=-a(0)C(0,\theta)$。故某个整数 $k$ 满足
$$
\langle C(0,\cdot)\rangle=-k/a(0).
\tag{M.12}
$$
完整周期继承本身不允许把这个整数直接写成1。若进一步验证
$|a(0)\langle C\rangle+1|<1/2$，整数性才准确给 $k=1$。
也可由实际腰曲线的定向嵌入证明其转角数。有限 BVP 输出接近1
只是选择这一分支的数值依据，仍须真实误差界。

如果实际帽具有固定轴的四重 Euclidean 等变性，而 body 系数也
有相同四重材料周期，(M.4) 的唯一性将这一等变性传到腰。
$X_0$ 因而沿该轴，腰反射面垂直于该轴。这里使用实际几何
等变性；仅有某个有限 Fourier 文件的频率命名不替代它。

若另证正半圆盘是嵌入、其内部严格位于 $\Pi$ 的一侧、腰边界
嵌入且仅在腰与 $\Pi$ 相交，则两侧镜像除腰外不相交。
结合上述接缝浸入和紧性，整个闭面是 $C^2$ 嵌入。
曲率有界与这一拓扑单射仍不单独给 README 的定量 reach；
全域自距离、可见位移和固定握持区还须在同一最终族上支付。

## 6. 与真实 tail 高度规范的精确对接

一般固定 ambient 高度 $Z$ 满足
$\nabla_g^2Z=(\nu\cdot e_z)\mathrm{II}$。令
$W=\nu\cdot e_z>0$，则在物理 $r$ 方向
$$
B=\frac{Z_{r\theta}-\beta Z_\theta}{aeW},\qquad
C=\frac{Z_{\theta\theta}/a^2+a'Z_r/(aE)}W.
\tag{M.13}
$$
这里
$W^2=1-Z_r^2/E-Z_\theta^2/a^2$，分母必须在真实完整角圈上保持
正值。平均曲率由这两个完整商求平均，不能从导数项平均为零
就把整个非线性 mean 清零。

R119 实际尾的固定 ambient 高度是 $Z=Z_{\rm ref}-v$，其半径
坐标满足 $(Z_{\rm ref})_a=-w_{\rm ref}$；物理 $r$ 向北帽时
$a_r<0$。按前引接口的
$P=v_\theta/(aw_{\rm ref})$、$\mathcal K=v_a/w_{\rm ref}$、
$U=P_\theta$、$V=\mathcal K_\theta$，(M.13) 恰给
$$
B=\frac{w_{\rm ref}}a\,\frac{V-P}{\sqrt D},\qquad
C=-\frac{w_{\rm ref}}a\,
\frac{1+\mathcal K+(1+w_{\rm ref}^2)U}
{\sqrt{1+w_{\rm ref}^2}\sqrt D},
\tag{M.14}
$$
$$
D=1-w_{\rm ref}^2
\bigl(2\mathcal K+\mathcal K^2+(1+w_{\rm ref}^2)P^2\bigr).
$$
这是同一物理向内标架的符号，$B$ 相对于向外半径标架变号，
$C$ 不变。固定 $\Gamma$ 的 raw Jacobi 高度 $h=\delta v$ 对应
$\delta Z=-h$；改变 $\Gamma$ 时还必须保留实际参考高度、尺度
和移动切口列。独立 mean 高度也保留这个负号和实际积分常数。

因此可以把真正尾端的完整高度两迹先转为 (M.14)，再与 R133
曲率端口图联立。$f_B$、实际 labels、两 bump 和真实
$\mathfrak F=0$ 未解决时，只得到局部接口，不能冒称本定理的
实际周期封闭端帽假设已经满足。

## 7. 连续依赖

在同一紧材料圆盘上，若真实 metric jet、完整 $A,B,C$ 和实际
帽的 $C^2$ 数据连续依赖参数，且上述正性条件统一成立，则
(M.4) 的连续系数 ODE、(M.6) 和 (M.8) 给 $F$ 的 $C^2$ 连续
依赖。腰平面和反射也连续依赖，所以镜像闭浸入连续。

这一结论只传递已经给定数据的连续性。不同参数若改变 $g$，
仍不成为公共度量弯曲族；最终相位构造必须在选定的一张真实
闭嵌入及一个固定径向度量上进行。
