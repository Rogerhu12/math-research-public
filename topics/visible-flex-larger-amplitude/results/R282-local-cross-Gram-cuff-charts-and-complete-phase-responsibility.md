# R282　局部交叉 Gram 积分门、共同 cuff 图与完整相位责任

2026-11-15，geometry，AI 辅助研究。**状态：已证明的条件几何结论；当前只有源码和解析论证，没有实际接受场的新计算。**

本条补的是 [R241](R241-immersion-cover-embedding-and-normal-cones.md) 的一个可计算局部切向门及其跨 cuff 的真实坐标接口。该门处理**包含材料对角线的整个闭参数块 product**：同一个材料点按原粘合识别，不要求该点与自身具有正距离；对所有不同材料点则直接证明非零切向投影，从而同时排除相交和双法向。

它作为原门的一个额外 OR 分支。旧短路径、距离、法向锥、平帽以及完整静态基面加 R24 标记路线全部保留。这里没有替换原非线性方程、目标度量 $g$、$\tau$、接受容差或完成标准，也没有把某个尚未生成的场写成已接受。

## 1. 原局部责任的准确边界

R241 的短路径门先给实际诱导度量下的距离上界，再用**整个闭面**的主曲率界 $K$ 控制连接两点的长度极小测地线。一个显式参数路径只给距离上界；它通常有非零测地曲率，不能把表面主曲率界直接当作这条任意路径的空间曲率界。若只有某个图内的曲率界，也不能未经证明就假定全局极小测地线留在图内。

R241 的中心法向锥正余量能处理远离材料对角线的块对，但它是对整块的**绝对**切向长度下界。若闭 product 含 $x=y$，该下界不可能严格为正。把这个失败解释成几何失败，或直接删掉含对角线的整对，都不正确。

现有 geometry_20261114_continuous_cover_budget_v3.py 保留短路径、平帽、距离与中心法向锥，并对完整原候选计数；其导出的 worst 至多 128 项、每坏对的少量 child 是展示项，不是可直接移植到新闭 cell 布局的完整逐对责任账。现有 shared-field mixed 入口对可能跨 cuff 含零弦的 rank 明确记为未支付的 local responsibility，也没有宣称它已经通过。

本条的新增量是：用**随参数位移平方缩放的严格下界**支付局部 product，给实际 shared-B/collar 的全相位有效常数，并规定空间与相位共同细分后的责任单位。它不重复 R241 的全局 reach 消费定理或 R281 的严格相位球门。

## 2. 交叉 Gram 积分门

设 $D\subset\mathbb R^2$ 为凸闭集，包含于一个开坐标域。设

$$\chi:D\longrightarrow M$$

是实际抽象材料面中的一个单射坐标片的限制；其跨接缝和周期端点识别必须来自原材料图册。令

$$f=F\circ\chi,\qquad J(z)=Df(z)\in\mathbb R^{3\times2}.$$

只需 $f$ 在 $D$ 的邻域中为 $C^1$。此处不预先假定 $F$ 在整个 $M$ 上单射。记

$$\operatorname{Sym}A=\frac{A+A^T}{2}.$$

### 定理 282-A

若存在 $m>0$，使全部 $z,w\in D$ 都满足

$$
\operatorname{Sym}\!\bigl(J(z)^TJ(w)\bigr)\succeq m I_2, \tag{282.1}
$$

则对任何 $x,y\in D$、$x\ne y$，令 $v=y-x$，有

$$
\begin{aligned}
(f(y)-f(x))\cdot J(x)v&\ge m|v|^2>0,\\
(f(y)-f(x))\cdot J(y)v&\ge m|v|^2>0.
\end{aligned} \tag{282.2}
$$

因此 $f$ 在 $D$ 上单射；每个不同坐标点的弦在两个端点均有非零切向投影。特别地，该弦既不为零，也不可能是双法向弦。

**证明。** 凸性保证 $x+tv\in D$，$0\le t\le1$。微积分基本定理给

$$f(y)-f(x)=\int_0^1J(x+tv)v\,dt.$$

与 $J(x)v$ 作内积。对任何实方阵 $A$，$v^TAv=v^T\operatorname{Sym}(A)v$，故

$$
(f(y)-f(x))\cdot J(x)v
=\int_0^1v^TJ(x)^TJ(x+tv)v\,dt
\ge m|v|^2.
$$

把固定端点改为 $y$，同样得到第二式。在 (282.1) 中取 $z=w$，还得到 $J(z)^TJ(z)\succeq mI_2$，所以各点的微分秩为 2；$J(x)v,J(y)v$ 是相应真实切平面中的非零向量。严格正内积排除零弦和法向弦。若两个不同坐标点的像相同，第一式立即矛盾，单射性同时得到。□

若另有 $\sup_D\|J\|_{\rm op}\le L$，则

$$
\frac{m}{L}|y-x|\le |f(y)-f(x)|\le L|y-x|. \tag{282.3}
$$

上界由积分得到；下界由 (282.2) 和 $|J(x)v|\le L|v|$ 得到。这里没有对零位移作除法，(282.2) 对不同点的严格性来自 $m>0$ 与 $|v|>0$。

### 对角线、图册和取向

若两份参数字符串经原材料粘合代表同一个点，应先送入同一坐标图，得到 $x=y$。定理此时只给等式 $0=0$；该点不属于 R241 所要求排除的不同材料点对。

反过来，不能因为两个像坐标很近、相同，或某个球含零弦，就把两个材料点宣布为同一点。$\chi$ 的单射性来自材料图的构造，不来自待证明的像单射性。图中不同坐标即是不同材料点，再由定理证明其像不同。

该门只使用切向量和 Euclidean 内积。环境刚体变换、上下片反射，以及法向取反均不改变结论；不需要先选全局单位法向。一个图内的结论不排除该图与远处另一块相交，后者仍须完整块对覆盖。

## 3. 可由完整导数包围支付的充分条件

### 3.1 一般有理参考矩阵

取固定 $E\in\mathbb R^{3\times2}$，给出

$$E^TE\succeq \gamma I_2,\qquad \|E\|_{\rm op}\le L_0,\qquad
\sup_{z\in D}\|J(z)-E\|_{\rm op}\le\varepsilon,$$

其中 $\gamma>0$。若

$$m:=\gamma-2L_0\varepsilon-\varepsilon^2>0, \tag{282.4}$$

则 (282.1) 成立。

**证明。** 对任意 $v$ 写 $J(z)v=Ev+e_z$，其中 $|e_z|\le\varepsilon|v|$。于是

$$
\begin{aligned}
v^TJ(z)^TJ(w)v
&=|Ev|^2+(Ev)\cdot(e_z+e_w)+e_z\cdot e_w\\
&\ge\bigl(\gamma-2L_0\varepsilon-\varepsilon^2\bigr)|v|^2.
\end{aligned}
$$

该式同时是对应对称部分的二次型下界。□

若 $E$ 为有理矩阵，其 Gram 矩阵 $Q=E^TE$ 正定，可取

$$\gamma=\frac{\det Q}{\operatorname{tr}Q},\qquad
L_0\ge\sqrt{\operatorname{tr}Q}.$$

因为 $\lambda_{\max}(Q)\le\operatorname{tr}Q$，这确实给出 $\lambda_{\min}(Q)\ge\gamma$。这个局部标量 $\gamma$ 不是原目标度量 $g$。根号用 R62 的有理上界即可。若六个导数误差分量分别有绝对上界 $b_{ij}$，则

$$\varepsilon\ge\sqrt{\sum_{i,j}b_{ij}^2}$$

足以控制算子范数。所有下界和上界必须来自该闭域上的真实导数包围，不是只在中心的数值差。

### 3.2 正交参考列的简单特例

若 $E^TE=I_2$，则可直接使用

$$m=1-2\varepsilon-\varepsilon^2>0. \tag{282.5}$$

这是便于核查的充分条件，不是最优条件，也不是一个新的求解验收阈值。如果该充分条件未过，仍可以直接支付 (282.1)，或使用任意原有门。

例如直接包围 $H(z,w)=\operatorname{Sym}(J(z)^TJ(w))$ 时，应把 $z,w$ 当作两个独立变量。相同名字的导数区间相乘不能误用只允许同一实数平方的更窄区间。若能对全部 $(z,w)\in D^2$ 给出 $H_{11}\ge a>0$、$\det H\ge d>0$、$\operatorname{tr}H\le T$，则 $H$ 正定，且统一有 $H\succeq(d/T)I_2$。这些是可选的区间充分条件。

式 (282.4) 或 (282.5) 取等号只给半正定下界，不能据此宣布不同点的严格切向分量。未付严格余量表示该分支未决，不表示实际曲面相交。

## 4. 实际 collar 的物理角、材料角与全相位

以下绑定已冻 shared-field 解释器所定义的**准确有限函数**，而不是将浮点点值 jets 标签当作兼容导数。原共享节点中的值、一阶、二阶数值是 Hermite 多项式的定义数据；区间内所有导数由该多项式自身求出。

令 cuff 半径为 $R>0$，原 inner 半径为 $R+h$，$h>0$。上片在不含外端 cut patch 的 collar 内具有

$$
G_0(r,\phi)=r e_{\Phi(\phi)}+B(r)e_z+Q\,U(r,\Phi(\phi)),
\qquad Q=\operatorname{diag}(1,1,-1), \tag{282.6}
$$

其中 $e_\theta=(\cos\theta,\sin\theta,0)$，$U$ 包含全部实际 Cartesian FFT 系数和完整均值。原解释器以 $q\in[0,1]$、$\phi=2\pi q$ 为输入，且

$$
\Phi(\phi)=\phi+\sum_{m=1}^{k}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\qquad \rho(\phi)=\Phi'(\phi)>0. \tag{282.7}
$$

使用完整实际 core 以及其已有完整圆上的严格正密度输入。由 $\Phi(\phi+2\pi)=\Phi(\phi)+2\pi$、连续严格正导数，$\Phi$ 给材料圆的微分同胚。这里没有把该非线性角映射延伸到帽极点。

R248 的原活动族是 $F_\alpha(r,\theta)=R_\alpha F_0(r,\theta-\alpha)$。对于新活动球中一个基态物理角 $\phi$，旋转后的点 $R_\alpha G_0(r,\phi)$ 的**当前共同材料角**恰为

$$\theta=\Phi(\phi)+\alpha\pmod{2\pi}. \tag{282.8}$$

因此在共同材料角中准确写为

$$
F_\alpha^+(r,\theta)
=r e_\theta+B(r)e_z+R_\alpha Q\,U(r,\theta-\alpha). \tag{282.9}
$$

在 marker-free 的上帽邻 cuff 环带，实际帽是

$$F_\alpha^+(r,\theta)=r e_\theta+H e_z,\qquad r\le R, \tag{282.10}$$

且不随相位变化。下片是全部 $z$ 分量反射后的相同表达，帽高为 $-H$。高度 $H$ 只作平移，对本条局部导数门无正性要求；这不撤销原闭组装中为别的责任设置的实际输入条件。

公式 (282.9) 直接使用已经具有材料角变量的完整 $U$，所以局部 owner 不必数值求 $\Phi^{-1}$。若另一个实现要从原 $(r,q)$ 六 jet 转到 $(r,\theta)$，必须使用真正的链式法则。以下右侧的 $F_q,F_{rq},F_{qq}$ 明确指**已经乘同一个 $R_\alpha$** 的函数 $R_\alpha G_0(r,2\pi q)$ 的 jet，下片还保原反射；$\rho'$ 指关于 $\phi$ 的导数。例如固定 $\alpha$ 时

$$
\begin{aligned}
F_\theta&=\frac{F_q}{2\pi\rho},\\
F_{r\theta}&=\frac{F_{rq}}{2\pi\rho},\\
F_{\theta\theta}
&=\frac{F_{qq}}{4\pi^2\rho^2}
  -\frac{F_q\rho'}{2\pi\rho^3}.
\end{aligned} \tag{282.11}
$$

右侧均在正确的 $\phi=\Phi^{-1}(\theta-\alpha)$ 处取值；全部 $\rho,\rho'$ 与逆像区间都须真实包围。不能令 $\theta=\phi$，不能只改 jet 的标签，也不能以有限材料角带宽替代非线性复合。当前可直接使用 (282.9) 的方案没有这项额外反解费用。

## 5. 真实共同 cuff 图与准确接缝

选择 $0<\delta<R$、$0<\omega<\pi$ 和一个圆周中心角 $\theta_c$，令

$$D=[-\delta,\delta]\times[-R\omega,R\omega],\qquad
r=R+u,\quad \theta=\theta_c+v/R. \tag{282.12}$$

在 $u\le0$ 使用该帽的 Cartesian 极坐标图，在 $u\ge0$ 使用原活动 collar 的材料图，沿 $u=0$ 用原 cuff 身份粘合。由于 $r>0$，且角提升区间的长度 $2\omega<2\pi$，这是抽象材料面上的单射坐标图，不经过极点。相同侧 cuff 的两份边界表示只有在相同材料角模 $2\pi$ 时才识别。上、下两个 cuff 分别处理，不能凭空间位置相同把它们互相识别。

$v=R(\theta-\theta_c)$ 只是该材料图的坐标选择，不对空间中的场作缩放，也不修改原目标度量、曲率或 reach 的物理单位。

原完整 collar 在 $r=R$ 的非轴 $0/1/2$ 径向 jet 都为零；共享背景在该端的准确数据为

$$B(R)=H,\qquad B'(R)=B''(R)=0.$$

故 (282.9) 与 (282.10) 的完整 Cartesian 两阶 jet 相同。角和混合迹由准确有限函数求导得到，因零径向迹是对整个材料角函数的恒等式，并非有限角样本相等。于是该分片图为 $C^2$，特别满足定理 282-A 的 $C^1$ 前提。

此处只使用同场 collar/shared-B 的准确有限多项式接缝。它不声称原有限 Gauss 算式的 $a$ 与返回的 ap 已被证明互为导数，也不借此支付远端 prefix/cut 或中央反射缝。那些责任继续由 R249/R279 和原闭组装分别承担。

## 6. 完整系数给出的统一全相位常数

在实际 collar 宽度 $h$ 上写完整有限表达

$$
U(r,\vartheta)=
\sum_{j=3}^{5}
\left(\sum_{k=0}^{N/2}\operatorname{Re}\!\bigl(C_{jk}e^{ik\vartheta}\bigr)\right)
\left(\frac{r-R}{h}\right)^j,
\qquad C_{jk}\in\mathbb C^3. \tag{282.13}
$$

$C_{jk}$ 是原 tail_coefficients(-1) 的实、虚三坐标幂系数，不增加或删除 RFFT 归一化因子。所有 $0,\ldots,N/2$ 模、零模的三坐标和实际 Nyquist 均保留。$j=0,1,2$ 精确消失来自原零端点 jet。

设共享背景第一个 cell 的宽度为 $h_B>0$，写

$$B(r)=H+\sum_{j=3}^5 b_j\left(\frac{r-R}{h_B}\right)^j. \tag{282.14}$$

选有理上界

$$\nu_{jk}\ge\sqrt{\sum_{\ell=1}^3
\bigl((\operatorname{Re}C_{jk,\ell})^2+
      (\operatorname{Im}C_{jk,\ell})^2\bigr)},$$

并令

$$L_j=\sum_{k=0}^{N/2}\nu_{jk},\qquad
T_j=\sum_{k=0}^{N/2}k\nu_{jk}.$$

取 $0<\delta<\min(h,h_B)$，定义

$$
M_r(\delta)=
\sum_{j=3}^5\frac{jL_j\delta^{j-1}}{h^j}
+\sum_{j=3}^5\frac{j|b_j|\delta^{j-1}}{h_B^j},
\qquad
M_\theta(\delta)=
\sum_{j=3}^5\frac{T_j\delta^j}{h^j}. \tag{282.15}
$$

对于 $R\le r\le R+\delta$、全部 $\vartheta$，有

$$|U_r|+|B'|\le M_r,\qquad |U_\vartheta|\le M_\theta. \tag{282.16}$$

证明逐模用 $|\operatorname{Re}(C e^{ik\vartheta})|\le|C|$，求导时角模得到 $k$、径向幂得到 $j/h$，再用三角不等式。该估计支付完整向量，不把每个坐标的上界误当向量范数，也不使用有限角采样。

### 6.1 实际无标记环带

对该侧帽的每个紧支撑 marker，读取原中心 $c_\ell\in\mathbb R^2$、半径 $s_\ell>0$。若

$$|c_\ell|+s_\ell<R,$$

取有理上界 $r_*^+\ge\max_\ell(|c_\ell|+s_\ell)$ 且 $r_*^+<R$；无 marker 时可取 $r_*^+=0$。再要求

$$0<\delta<R-r_*^+.$$

则 $R-\delta\le r\le R$ 的帽部分准确平坦，全部 marker 及其导数为零。上界可以用原 R62 有理平方根逐个形成；若原严格支撑条件成立，提高根号精度会在有限步得到 $r_*^+<R$。若实际支撑没有这项余量，本节方案未付，不能硬称帽环带平坦。

### 6.2 图中的导数误差

对 (282.12) 的图，使用 $R_{-\theta_c}$ 的固定环境旋转；下片可以再反射。令

$$E=(e_x,e_y)\in\mathbb R^{3\times2},\qquad E^TE=I_2.$$

在帽侧导数来自原圆盘；在活动侧由 (282.9) 求导。因为

$$|e_\theta-e_{\theta_c}|\le|\theta-\theta_c|\le\omega,$$

且 $\partial_v=R^{-1}\partial_\theta$，两列误差分别满足

$$
\begin{aligned}
|f_u-e_x|&\le E_u:=\omega+M_r(\delta),\\
|f_v-e_y|&\le E_v:=\delta/R+\omega+M_\theta(\delta)/R.
\end{aligned} \tag{282.17}
$$

第二式的圆项准确分解为

$$\frac rR e_\theta^\perp-e_{\theta_c}^\perp
=\left(\frac rR-1\right)e_\theta^\perp
+(e_\theta^\perp-e_{\theta_c}^\perp).$$

所以无需额外误写一个不受控制的角径乘积。帽内侧的 $|r/R-1|\le\delta/R$，扰动项为零，仍由同一上界覆盖。$R_\alpha,Q$ 和上下反射均为正交变换，故 (282.17) **同时适用于全部相位**，而不是只在 $\alpha=0$。

取有理

$$\varepsilon\ge\sqrt{E_u^2+E_v^2}.$$

若实际有理比较给

$$1-2\varepsilon-\varepsilon^2>0, \tag{282.18}$$

定理 282-A 就对该共同图和全部相位成立。$|f_u-e_x|,|f_v-e_y|$ 指上述固定旋转后坐标中的误差。$E_u,E_v$ 是两列向量范数上界，其平方和控制 Frobenius 范数，继而控制算子范数。

### 6.3 有效的严格余量终止

对于实际已绑定的有限系数，$L_j,T_j,|b_j|$ 均为有限数，且 $h,h_B,R>0$。因此

$$M_r(\delta)=O(\delta^2),\qquad M_\theta(\delta)=O(\delta^3).$$

从任一满足上述几何宽度和支撑严格条件的正有理 $\delta_0$、$0<\omega_0<1/4$ 出发，令 $\delta_n=\delta_0 2^{-n}$、$\omega_n=\omega_0 2^{-n}$。R62 平方根上界以随 $n$ 增大的精度形成，其绝对向上误差趋零。故 $\varepsilon_n\to0$，而 (282.18) 的左边趋于 1，有限层必严格通过。

这是从**具体有限系数和真实支撑余量**推出的终止，不是从“场是 $C^2$”标签推测一个可计算余量。系数可能很大，所需层数也可能很大；没有给实际未生成场指定 $\delta,\omega$ 或运行时间。若资源预算先结束，只记尚未支付，不推出几何反例。

## 7. 实际闭 cell 的共同材料图 membership

一个小 cuff 图的导数门对全相位有效，并不意味着某个完整 mixed rank 在所有相位都落入该图。原 rank 中的活动基态物理角随 $\alpha$ 旋转遍历材料圆，固定帽块不动；必须把 membership 与相位一起分。

考虑一个责任子块

$$P=I_r\times I_q\times Q_{\rm cap}\times I_\zeta,$$

其中 $I_r,I_q$ 是原活动闭参数 cell 的闭子区间，$Q_{\rm cap}$ 是原帽 Cartesian 闭 box 与原闭圆盘相交所得集合的闭子块，$\zeta$ 是下述一个 RP1 相位图中的坐标。只有以下输入全部成立，才能将 $P$ 交给局部门：

1. 活动与帽属于同一真实 cuff、同一上下侧、同一场和固定轴。
2. $I_r\subset[R,R+\delta]$；帽块所有点满足 $R-\delta\le\sqrt{x^2+y^2}\le R$。
3. 对所有 $q\in I_q,\zeta\in I_\zeta$，活动的**材料圆方向**
   $e_{\Phi(2\pi q)+\alpha(\zeta)}$ 落在选定的共同角图。
4. 对帽块所有 $(x,y)$，其材料方向 $(x,y)/\sqrt{x^2+y^2}$ 落在同一个角图。
5. 这两个方向有同一不绕满圈的提升区间，包含于 (282.12) 的角范围；原粘合身份和完整闭端点均保留。

条件 3 的方向不是变形后活动点的 $F_{xy}/|F_{xy}|$；后者受到完整 $U_{xy}$ 影响，通常不是材料角。条件 4 则使用原帽的实际 Cartesian 参数，图 marker 不改变其 XY 坐标。不能把 $q$ 或 $\phi$ 直接当帽极角。

### 7.1 不需要浮点 atan2 的充分 membership

可选一个有理单位向量 $e=(a,b)$，$a^2+b^2=1$，作为图中心方向，令 $e^\perp=(-b,a)$。对于 $0<\eta<1/4$，若某个非零平面向量 $z$ 的全部允许值满足

$$
e\cdot z>0,\qquad
\eta(e\cdot z)-e^\perp\cdot z>0,\qquad
\eta(e\cdot z)+e^\perp\cdot z>0, \tag{282.19}
$$

则它有唯一的相对角提升 $|\theta-\theta_c|<\arctan\eta<\eta$。取 (282.12) 的 $\omega=\eta$ 即有带余量的共同图 membership。帽侧可直接对 $z=(x,y)$ 检查这些线性式；活动侧用 $z=R_\alpha e_{\Phi(2\pi q)}$。径向下界保证帽侧 $z\ne0$。

原 R281 的两张相位图可继续使用：

$$
\begin{array}{ll}
t\in[-1,1]:&
\cos\alpha=\dfrac{1-t^2}{1+t^2},\quad
\sin\alpha=\dfrac{2t}{1+t^2},\\
u\in[-1,1]:&
\cos\alpha=\dfrac{u^2-1}{u^2+1},\quad
\sin\alpha=\dfrac{2u}{u^2+1}.
\end{array} \tag{282.20}
$$

对应连续提升分别可取 $\alpha=2\arctan t$ 和 $\alpha=\pi-2\arctan u$。检查 (282.19) 不必真的计算这两个反三角函数：用 (282.20) 和完整 $\Phi$ 的三角函数即可。两图的闭端点重复覆盖是允许的，$\alpha=\pi$ 在第二图内部；不能漏掉该相位或只用单个 tan-half 图。

有理单位向量由有理圆参数给出一个稠密集合；对任意固定 $\eta>0$，以它们为中心的开扇区覆盖圆周，紧性给有限子覆盖。实际消费者须保该有限 atlas 的完整覆盖证据，而非取若干角样点就宣布覆盖。圆周扇区可在两 RP1 图上转为有理多项式不等式，用已付的严格区间/Sturm 门或有余量的完整区间细分核查。中心角符号 $\theta_c$ 本身不必以浮点 atan2 形式保存。

## 8. 完整 rank × 空间 × phase 责任，而非整 rank 豁免

令原活动闭 cell 编号为 $i$、帽闭 cell 编号为 $j$，保

$$\operatorname{rank}=iN_C+j.$$

每个 rank 的起始责任是两个完整相位图上，原活动 cell 与原帽 cell 的全部 Cartesian product。允许在原活动的 $r,q$、帽的 Cartesian box、相位的 $t$ 或 $u$ 上作闭区间二分。父域必须等于子域之并；公共端点重复无害，空域只能凭准确的空交证明剔除。

每个叶责任可由下列一个或多个原义分支支付：

- R241 的原已付局部路径、平帽、距离或切向门；
- R281 的原距离、两单端和 joint OR，相位范围限制到该叶的真实闭相位区间；
- 本条 282-A 的共同图 membership 与严格交叉 Gram 下界。

采用新局部分支的叶，必须记录本叶的全部空间区间、相位图和区间、共同 cuff/side、材料角图、有限表达式身份及实际 $m>0$。它支付的是该叶全部**不同材料点**，不是把一个包含相同点的球对丢掉。

例如，一个 rank 包含零弦相位，并不意味着该 rank 的其他相位或空间部分都近邻。近角的相位片可以由共同 cuff 图支付；角度远离的片仍交 R281 或其他原门。不得因 known_cuff_local_responsibility 为真就将整 rank 改为通过。已冻 mixed 入口目前恰好只把它记为未决，本条没有改写那个已有结果。

### 定理 282-B：完整组合的合法性

若每个 rank 在两 RP1 图上的原完整 product 都是有限已付闭叶之并，并且每个叶的所选门都针对**同一实际相位、同一实际场**支付相应全域，则这些叶共同支付所有活动—固定点对的原 R241 点对排除责任，包括 cuff 的不同点对；同一材料点只按既定商识别免于“不同点”责任。

**证明。** 固定任意相位、活动材料点与帽材料点。两相位图至少一张包含该相位，原两个完整 cell 覆盖至少一对原编号。完整子域覆盖给一个包含该三元组的叶。在局部叶中，共同图的单射材料坐标把不同材料点送成不同坐标，282-A 给非零切向投影及非零弦；其他叶使用各自已证明的原门。因此没有未经支付的点对。公共边界或重复表示只会提供多份合法覆盖，不会产生遗漏。□

### 8.1 关于细分终止能声明什么

对同侧 cuff 的材料对角集合，即活动点 $r=R$ 与帽边界同角点在该相位下相同的三元组，(282.17)—(282.18) 给全相位统一的小图。选择有重叠余量的有限角 atlas 后，每个对角三元组在原空间—相位参数域中都有一个邻域，其整个 product 落入某个严格共同图；径向条件在 $r=R$ 两侧也有余量。

这个对角集合是有限闭参数域中的紧集。有限 atlas、连续的真实材料方向映射以及严格余量给正的局部覆盖尺度。因此足够细的 dyadic 空间—相位子块中，所有接触该对角集合的子块都能由某个局部叶支付。对于固定有限 Hermite/Fourier 表达式，随空间及相位宽度缩小、Arb 精度提高，所用自然区间包围收缩；(282.19) 的真实严格余量最终可被有限计算识别。

这只消除了**由正确粘合造成的局部零弦障碍**。对角集合以外可能还有未支付的真实几何责任；不保证任意输入场的 R281 球门或所有旧门必过，也不保证所有 rank 都在有限预算内完成。该方向的全局终止仍需所有剩余点对各有适用门及严格余量等真实条件。

账本须分别保：完整计划 rank 数、每 rank 的两图根域、已付叶、未决叶、未访问 rank 后缀、预算退出原因。仅导出 worst 至多 128 项或每坏对四个 children 不满足此完整性要求。

## 9. 与原曲率、短路径和全局结论的衔接

局部交叉 Gram 门不需要预先输入 $K$。若同时已有 $L=\sup_D\|Df\|_{\rm op}$，图中的直线路径还给

$$d_{F^*e}(\chi(x),\chi(y))\le L|x-y|.$$

只有在原整个闭面的曲率界 $K$ 已付、且对所需 product 有 $L|x-y|<\pi/K$ 的统一上界时，才能进一步把这条显式路径用作 R241 的短路径门。这里仍是用路径估计内蕴距离，再由全局 $K$ 控制极小测地线；不是对这条参数线假定空间曲率不超过 $K$。

在全局使用时，仍需原闭 $C^2$ 正则浸入、全部其它接缝、active-active 与 fixed-fixed 的完整空间责任、原曲率 $K\tau\le1$ 及剩余 mixed 责任。局部门与这些原输入一起，才可按 R241 的原顺序先得嵌入，再得 reach。R279 提供同一准确有限场上的可计算曲率充分条件，但不因本条证明而自动生成一个实际 $K$。

本条没有把整个 marked 面当作静态基面一起旋转。共同图中的 (282.9) 是原 R248 活动表达，(282.10) 是实际固定帽；只在已证明无 marker 的环带内使用平帽公式。远处固定 marker 的几何、原 static+R24 传递、完整目标像上的 held/Hausdorff、同一个 $g$、两帽非平面和刚体商等责任均不改变。

## 10. 现有源可供给的最小输入与尚缺的生产者

对已冻的准确有限表达式，局部常数无需重新求解 BVP，也无需重建全部 native Jacobian。真实运行时可在同一 ExactFiniteField 对象中读取：

| 必要对象 | 已有准确来源 | 本条使用 |
|---|---|---|
| $R,h$、原上下侧/轴 | ExactFiniteField.cuff/inner、真实 plan/assembly | 共同材料图的半径与身份 |
| collar 全部 $C_{jk}$ | ExactFiniteField.tail_coefficients(-1)，含 node(0) 全部三个 jet、全部 FFT 模 | (282.13)—(282.16)，不截断均值或 Nyquist |
| $h_B,b_3,b_4,b_5,H$ | 同一 B.radii、B.coefficients[0] 与准确 cuff 节点 | 真实有限背景，不换原 $g$ |
| 完整 $\Phi,\rho>0$ | 实际全部 core、已有密度证据 | 活动物理角到共同材料角 membership |
| marker 中心/半径/side | 同场原 plan 与固定帽 producer 的完整 binding | marker-free 环带及原 cap Cartesian 域 |
| 原完整活动/帽 cell | 两个已冻 producer 的完整 cell 定义与 rank 规则 | 空间—相位完整子域覆盖 |
| 原 $\tau$ 与其它 owner | 同场原 cover、原 R241/R281/R24 合同 | 保原责任与 OR，不选择新目标 |

活动 producer 当前导出完整 FFT 节点的身份和区间球，但没有把完整 collar 系数 payload 另存为局部 owner 的输出。一个 hash 不能恢复这些系数。最薄接线是在同一 Actions 运行的已绑定表达式对象中调用上述准确方法，或由相同原 loader 和原完整节点输入重建同一有限表达式；二者都保原表达式与 source 身份，不能从球中心倒造系数，也不能从 renderer 的点值 jet 拼出连续导数。

当前真正缺少的是**完整空间—相位局部责任生产者及其组合账本**：它须生成本条的真实常数、membership、细分树和每叶 owner，才能把已冻 mixed 入口的未支付 local responsibility 连接起来。原聚合 cover 不是这个账本；本证明也不冒充实际运行。

可在独立后继实现中复用已冻 field 与 R281 内核。现有两源不改、旧结论不换标签；新 owner 的输入/output identity 需明确区分。大型可重算 cell/leaf payload 只在 runner 临时保留，按 README 第 15 条仅将源码、参数、真实 run、输出 SHA 与紧凑结论保入库。

## 11. 本条的证明范围

本次完成了源级读取、准确公式推导与条件证明，没有执行系数求值、Arb、Sturm、FFT、几何采样或任何本地科学计算，也没有创建合成 fixture。当前没有真实接受的闭场，故没有实际 $\delta,\omega,m$ 或 local-paid rank 数可报告。

与已有结果的区别是：

- R241 给完整浸入覆盖如何合法推出嵌入与 reach；本条给它新增一个能容纳材料对角线的真实局部切向门。
- R248 给共同材料角的全相位族与接缝责任；本条把物理 $\phi$、材料 $\Phi(\phi)$、当前相位和帽 Cartesian 图在 cuff 处精确接上。
- R249/R279 规定准确有限 Hermite/共享背景表达式及同场导数；本条使用该表达式的完整 collar 系数获得有效局部余量，而不假定原 scalar 返回导数兼容。
- R281 给正确连续球上的全相位 OR 覆盖；本条只补它不能整块严格支付的正确粘合近邻，并要求同一 rank 内按真实空间—相位 membership 分责任。

证明可以独立登记。未来是否在一个真实场上产生全局证书，仍由原科学流程和原全部责任决定，不以新增 fixture、机器 jet 门或额外审批为前提。

## 12. 直接引用

- [R241：浸入覆盖与法向锥](R241-immersion-cover-embedding-and-normal-cones.md)、[R37：双法向瓶颈](R37-double-normal-bottleneck-and-distance-cover.md)。
- [R248：有限 C² 全相位族](R248-finite-C2-phase-family-and-global-reductions.md)、[R24：固定弱标记余量](R24-weak-markers-with-explicit-reach-margin.md)。
- [R249：共有节点 inlet 规范形](R249-shared-node-inlet-parity-normal-form.md)、[R279：准确有限场曲率证书](R279-finite-field-direct-continuous-curvature-certificate.md)。
- [R62：连续相位球门](R62-continuous-all-phase-mixed-normal-balls.md)、[R281：两 RP1 图完整相位覆盖](R281-exact-rational-phase-disjunction-and-finite-cover.md)。
- [已冻活动有限表达式](../computations/geometry_20261115_shared_active_interval_balls.py)、[已冻两固定帽球](../computations/geometry_20261115_fixed_cap_rational_balls.py)、[已冻完整 mixed 责任入口](../computations/geometry_20261115_complete_mixed_phase_component.py)。
