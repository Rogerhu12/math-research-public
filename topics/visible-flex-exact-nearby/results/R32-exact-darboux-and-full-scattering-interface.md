# R32：严格星形图的完整 Darboux 标量化与全传输接口

2026-11-12，independent-audit。

**状态：已证明的中间结论。** 对严格星形的真实浸入，本文把完整度量
线性化（包括全部低阶项）精确化为一个全局、散度自伴的标量算子，并给
反向重建、刚体自由度和持握条件。这里不要求真实诱导度量已为径向。
随后给严格双曲切口之间的完整传输、振幅及两通道散射接口；转折外端
响应的存在性与定量界必须从实际算子另行证明，不能由射线返回映射
或 Maslov 符号替代。

所有经典计算先在充分光滑对象上作出；例如 $\rho,w\in C^4$、源张量
$f\in C^2$。较低正则版本按本文散度式和分布恒等式解释。本文没有把
最终闭面只要求 $C^2$ 自动升级成全局光滑，也没有证明当前数值候选的
全频右逆或 README 的有限可见位移结论。

## 1. 实际严格星形面及坐标的范围

记 $\sigma$ 为单位球面 $S^2$ 的圆度量，$\nabla,\Delta,\operatorname{div}$
均相对于 $\sigma$，约定 $\Delta Y_\ell=-\ell(\ell+1)Y_\ell$。
设一个闭的连通浸入满足某个固定原点下的严格支撑条件
$$
\langle F,n\rangle>0.
\tag{1.1}
$$
径向投影 $F/|F|$ 的微分可逆：其核若含一个非零切向量，就会使该
切向量的像平行于 $F$，与 (1.1) 矛盾。紧性使投影为覆盖映射；
因 $S^2$ 单连通，它在连通的定义域上是微分同胚。因此可以用真实的
径向方向 $u\in S^2$ 作材料坐标，写成
$$
F(u)=r(u)u=\frac{u}{\rho(u)},\qquad \rho>0.
\tag{1.2}
$$
这不是将当前近似度量替换成某个平均度量。坐标改变后，实际应变源、
均值列、投影和持握集合都须一并拉回。

设
$$
Q=\rho^2+|\nabla\rho|^2,\qquad
B=\nabla^2\rho+\rho\sigma,\qquad A=\operatorname{cof}_\sigma B
=(\operatorname{tr}_\sigma B)\sigma-B.
\tag{1.3}
$$
作为张量收缩算子时，将 $A$ 的两个指标用 $\sigma$ 升起。实际诱导
度量和外法向为
$$
g=\rho^{-2}\sigma+\rho^{-4}d\rho^2,\qquad
n=\frac{\rho u+\nabla\rho}{\sqrt Q},\qquad
\langle F,n\rangle=\frac1{\sqrt Q}.
\tag{1.4}
$$
采用 $\mathrm{II}_{ij}=\langle F_{ij},n\rangle$ 的约定，
$$
\boxed{\quad
\mathrm{II}=-\frac{B}{\rho\sqrt Q},\qquad
K_g=\frac{\rho^4\det_\sigma B}{Q^2}.
\quad}
\tag{1.5}
$$
对球面的协变二阶导数直接展开 $F=u/\rho$ 即得第一式：
法向分量中两个 $2\rho_i\rho_j/\rho^2$ 项恰相消。
又 $\det_\sigma g=Q/\rho^6$，给第二式。
所以 $B$ 的行列式精确记录当前实际图的曲率变号；其系数不包含
$K_g^{-1}$ 或 $\sqrt{|K_g|}^{-1}$。

## 2. 完整线性化的代数恒等式

令 $V$ 是一个真实环境变分，分解为
$$
V=v+w u,\qquad v(u)\in T_uS^2,\qquad w=\langle V,u\rangle.
\tag{2.1}
$$
这里 $w$ 是沿真实径向方向的分量，不是沿曲面法向的分量。
令 $f=D(F^*e)V$ 为完整应变，定义球面切向场
$$
q=\rho v-w\nabla\rho.
\tag{2.2}
$$
则有逐点准确恒等式
$$
\boxed{\qquad
\rho^2 f=\mathcal L_q\sigma+2wB.
\qquad}
\tag{2.3}
$$

**证明。** 先置 $r=1/\rho$，记 $v_i=\langle v,\partial_i u\rangle$。
从
$$
F_i=r_i u+r\,\partial_i u,\qquad
D_iV=(w_i-v_i)u+\nabla_i v+w\,\partial_i u
$$
得到
$$
f_{ij}
=r_i(w_j-v_j)+r_j(w_i-v_i)
+r(\nabla_i v_j+\nabla_j v_i)+2rw\sigma_{ij}.
\tag{2.4}
$$
置 $p=v/r$、$\eta=w/r$。将 (2.4) 除以 $r^2$，再把
$p+\eta\nabla\log r$ 合为一个切向场，其对称梯度正好收去 $w$ 的
一阶导数。余项是
$$
2\eta\bigl(\sigma+d\log r\otimes d\log r-\nabla^2\log r\bigr)
=2w(\nabla^2\rho+\rho\sigma).
$$
而 $p+\eta\nabla\log r=\rho v-w\nabla\rho=q$，证明 (2.3)。

反过来，由任意满足 (2.3) 的 $w,q$，按
$$
\boxed{\quad V=\rho^{-1}(q+w\nabla\rho)+w u\quad}
\tag{2.5}
$$
重建的真实环境变分精确满足 $D(F^*e)V=f$。
所以没有删掉切向未知量；它们被显式地保留在 $q$ 中。

## 3. 球面完整兼容算子及 Darboux 方程

对球面上的对称二张量 $e$，定义
$$
\mathcal C e
=\nabla^i\nabla^j e_{ij}-\Delta(\operatorname{tr}e)
-\operatorname{tr}e.
\tag{3.1}
$$
这是单位球面高斯曲率线性化的两倍。可直接验证
$$
\mathcal C(\mathcal L_q\sigma)=0.
\tag{3.2}
$$
例如对 $q=\nabla\phi+J\nabla\psi$ 分别代入，使用球面
$\operatorname{Ric}=\sigma$ 和协变微分交换公式即可；它也来自
$K_{\Phi_t^*\sigma}\equiv1$ 的微分。

张量 $B$ 满足 Codazzi 恒等式
$$
\nabla_iB_{jk}=\nabla_jB_{ik},\qquad
\operatorname{div}A=0.
\tag{3.3}
$$
第一式中 $\nabla^3\rho$ 的曲率交换项被 $\nabla(\rho\sigma)$ 的项
准确抵消；缩并得到第二式。二维的 cofactor 对张量为线性算子，故
$$
\begin{aligned}
\mathcal C(wB)
&=-\operatorname{div}\operatorname{div}(wA)
 -w\operatorname{tr}B\\
&=-A:\nabla^2w-w\operatorname{tr}B.
\end{aligned}
\tag{3.4}
$$
因此定义完整标量算子
$$
\boxed{\quad
\mathcal D_\rho w
=A:\nabla^2w+(\operatorname{tr}B)w
=\operatorname{div}(A\nabla w)+(\operatorname{tr}B)w,
\quad}
\tag{3.5}
$$
(2.3) 的必要条件就是
$$
\boxed{\qquad
\mathcal D_\rho w=-\frac12\mathcal C(\rho^2f).
\qquad}
\tag{3.6}
$$
此式包括所有低阶项；尤其 $(\operatorname{tr}B)w$ 不能省略。
在 $B$ 的某一特征值过零时，(3.5) 本身仍为光滑系数方程。

在闭球面上，
$$
\int \overline v\,\mathcal D_\rho w
=-\int A(\nabla\overline v,\nabla w)
 +\int(\operatorname{tr}B)\overline v w,
\tag{3.7}
$$
故 $\mathcal D_\rho$ 严格形式自伴。这里没有断言它在混合型区域
椭圆、强制，或具有一个自动可用的闭算子逆。

若 $\rho\equiv1$，则 $\mathcal D_\rho=\Delta+2$；这同时检查
(3.5) 的零阶项和 (3.6) 的符号。

## 4. 球面兼容条件也是充分条件

### 命题 4.1

对充分光滑的球面对称张量 $e$，
$$
\boxed{\quad
\mathcal C e=0
\quad\Longleftrightarrow\quad
e=\mathcal L_q\sigma
\text{ 对某个球面切向场 }q.
\quad}
\tag{4.1}
$$
$q$ 的全部不唯一性恰为三个球面 Killing 场 $\omega\times u$。
因此，在整个闭球面上，(3.6) 与完整应变方程双向等价。

**证明。** 必要性已证。为证明充分性，先解
$$
\operatorname{div}\mathcal L_q\sigma=\operatorname{div}e
\tag{4.2}
$$
并令 $q$ 与 Killing 场正交。下面的球谐分解同时证明该解存在。

写 $\operatorname{div}e=\nabla a+J\nabla b$，其中 $a,b$ 均取零均值。
由于每个 $\omega\times u$ 都是 Killing 场，分部积分给
$\operatorname{div}e$ 与它们正交；所以 $b$ 的一次球谐分量为零。
若 $q=\nabla\phi+J\nabla\psi$，则
$$
\begin{aligned}
\operatorname{div}\mathcal L_{\nabla\phi}\sigma
 &=2\nabla(\Delta\phi+\phi),\\
\operatorname{div}\mathcal L_{J\nabla\psi}\sigma
 &=J\nabla(\Delta\psi+2\psi).
\end{aligned}
\tag{4.3}
$$
故在零均值空间解 $2(\Delta+1)\phi=a$，并在去掉零次及一次球谐的
空间解 $(\Delta+2)\psi=b$，就得到 (4.2)。这些标量分母分别为
$2(1-\ell(\ell+1))$ 及 $2-\ell(\ell+1)$，在规定空间中均不为零。

置 $T=e-\mathcal L_q\sigma$，则 $\operatorname{div}T=0$ 且
$\mathcal CT=0$。令 $\tau=\operatorname{tr}T$，即得
$(\Delta+1)\tau=0$。其球谐分解或球面第一非零特征值为 $2$ 的
Poincaré 不等式给 $\tau=0$。

最后，一个二维无迹、无散度对称张量自动满足 Codazzi 恒等式。
这一点可在一点的正交正常坐标写
$T_{22}=-T_{11}$，并用两条散度方程逐项核对。
在单位球面上，Codazzi 和无迹又给
$$
\nabla^k\nabla_kT_{ij}=2T_{ij}.
\tag{4.4}
$$
将协变导数交换并用 $\operatorname{Ric}=\sigma$ 即得 (4.4)；
与 $T$ 配对积分为
$-\|\nabla T\|_2^2=2\|T\|_2^2$，故 $T=0$。

若 $\mathcal L_q\sigma=0$，(4.3) 显示梯度部分为零，余下恰为一次
球谐的旋转梯度，即三个 Killing 场。证毕。

### 一个明确重建范数

对与 Killing 场正交的解，有
$$
\boxed{\quad
\|q\|_{L^2}\le\frac12\|e\|_{L^2},\qquad
\bigl(\|q\|_2^2+\|\nabla q\|_2^2\bigr)^{1/2}
\le\frac{\sqrt3}{2}\|e\|_2.
\quad}
\tag{4.5}
$$
证明可完全在上述向量球谐上作出。置
$Kq=\tfrac12\mathcal L_q\sigma$、$\lambda=\ell(\ell+1)$。
梯度型模式满足
$$
\|Kq\|_2^2=(\lambda-1)\|q\|_2^2,\qquad
\|q\|_2^2+\|\nabla q\|_2^2=\lambda\|q\|_2^2.
$$
旋转梯度型、除去 $\ell=1$ 后满足
$$
\|Kq\|_2^2=\tfrac12(\lambda-2)\|q\|_2^2,\qquad \lambda\ge6.
$$
两种模式在 $K^*K$ 下相互正交。第一种的第二比值最多 $1/2$，
第二种最多 $3/4$，给 (4.5)。

还可得到任意阶的一个精确球面对称范数。令
$\mathscr C=-\sum_{j=1}^3\mathcal L_{\Omega_j}^2$ 为旋转 Casimir
算子，作用于切向场或张量，其中 $\Omega_j=e_j\times u$。
置 $\|v\|_{\mathcal H^s}=\|(1+\mathscr C)^{s/2}v\|_2$。
旋转等变性使 $K$ 与该算子交换，逐模同样得到
$$
\boxed{\quad
\|q\|_{\mathcal H^{s+1}}
\le\sqrt{\frac78}\,\|e\|_{\mathcal H^s},\qquad s\ge0.
\quad}
\tag{4.6}
$$
最大比值是旋转梯度 $\ell=2$ 时的
$(1+\lambda)/(2(\lambda-2))=7/8$。这些是标准 Sobolev 范数的
等价范数；使用时应保持所声明的范数，不把等价常数默认为一。

## 5. 精确重建、六个刚体自由度及持握

给定完整源 $f$，若已求得 (3.6) 的一个解 $w$，置
$$
e=\rho^2 f-2wB.
\tag{5.1}
$$
由 (3.4) 得 $\mathcal Ce=0$。命题 4.1 重建 $q$，再用 (2.5)
重建 $V$。反过来，每个真实的 $V$ 都按 (2.1)--(2.2) 给出这样
的 $w,q$。这就是完整线性方程的双向对应。

对每个一次球谐 $Y(u)=a\cdot u$，有 $\nabla^2Y=-Y\sigma$，因而
$$
\mathcal D_\rho Y=0.
\tag{5.2}
$$
它们正是环境平移的径向分量。实际平移 $V=a$ 对应
$q=\rho(a-(a\cdot u)u)-(a\cdot u)\nabla\rho$。
三个球面 Killing 场对应 $w=0$、$V=\rho^{-1}(\omega\times u)
=\omega\times F$，正是环境旋转。

这六个模式并不排除 $\mathcal D_\rho$ 还存在真正的额外弯曲核；
所有这类额外核、振幅条件和自由均值约束仍须另行处理。仅仅删去
六个刚体模式不能被叫作完整可逆性。

任何源的右端已自动与三个 $Y$ 正交，因为
$$
\mathcal C^*Y=\nabla^2Y-(\Delta Y+Y)\sigma=0.
\tag{5.3}
$$
所以平移造成的三个标量 Fredholm 条件对真实应变源不额外设限。

**持握。** 若某个连通开集 $H$ 上 $f=0$ 且要求 $w=0$，则 (5.1)
在 $H$ 为零，重建的 $q|_H$ 是一个局部球面 Killing 场。
局部 Killing 场由一点的值和反对称一阶导数唯一决定，延伸为
唯一的全局 $\omega\times u$。减去这个全局旋转后，$q=0$、$V=0$
在 $H$ 精确成立。若要同时固定多个不相连的开帽，各帽得到的
Killing 场必须相同；这些相对匹配条件不能省略。

式 (4.5)--(4.6) 表明，完整 PDE 逆的主要难点确实集中在
$\mathcal D_\rho$：求出 $w$ 后，切向重建是一个明确的球面椭圆步骤，
不是另一份未知的全频混合型逆。仍须为 (3.6) 的二阶源、
乘法系数 $\rho,B$、端口和所选强范数支付实际费用。

## 6. 局部平面图的独立检查与周期条件

若在某一真实 Monge 图中 $F(x,y)=(x,y,z(x,y))$，写
$V=(v_1,v_2,w)$，置 $p=(v_1,v_2)+w\nabla z$。同样精确得到
$$
\operatorname{sym}\nabla p=\frac12f+w\nabla^2z=:E,
$$
并且
$$
\boxed{\quad
z_{yy}w_{xx}-2z_{xy}w_{xy}+z_{xx}w_{yy}
=-\frac12(f_{11,yy}+f_{22,xx}-2f_{12,xy}).
\quad}
\tag{6.1}
$$
三阶及四阶的 $z$ 项在展开时全部相消，且
$\operatorname{div}(\operatorname{cof}\nabla^2z)=0$。
这给 (3.5) 的局部平面版本，但单独一个这样的图未必覆盖腰部。

对非单连通的平面图，Saint-Venant 方程仅给局部重建。
令
$$
\beta=(E_{12,x}-E_{11,y})\,dx+
(E_{22,x}-E_{12,y})\,dy.
$$
它闭合。要有全局单值的平面旋转量 $r$，必须且只须每个闭曲线的
$\int\beta=0$；取 $dr=\beta$ 后，还必须且只须两个闭一形式
$$
\alpha_1=E_{11}\,dx+(E_{12}-r)\,dy,\qquad
\alpha_2=(E_{12}+r)\,dx+E_{22}\,dy
$$
各自的周期为零，才能积分成 $p_1,p_2$。$r$ 的常数变化不改变这些
周期，因为 $dx,dy$ 在平面图上为恰当形式。
这些是一个圆环上的三个真实周期条件。全局球面版本的充分性已经由
命题 4.1 解决，无需把局部周期条件假装成自动消失。


## 7. 转折帽上的精确 ground-state 变换

(3.5) 也恰为球面 Monge--Ampère 映射
$\rho\mapsto\det_\sigma(\nabla^2\rho+\rho\sigma)$ 的线性化，因为
$$
\operatorname{cof}B:(\nabla^2w+w\sigma)
=\mathcal D_\rho w.
\tag{7.1}
$$
但本文只用这一准确恒等式，不把非线性 Monge--Ampère 的可解性
当作等距问题的现成结论。

任取一次球谐 $Y=a\cdot u$。在 $Y$ 不为零的区域，置 $w=YU$。
由 $\mathcal D_\rho Y=0$，有
$$
\boxed{\quad
Y\,\mathcal D_\rho(YU)
=\operatorname{div}\bigl(Y^2A\nabla U\bigr).
\quad}
\tag{7.2}
$$
直接展开两边即证：交叉一阶项是
$2Y A(\nabla Y,\nabla U)$，余下 $U$ 项为 $YU\mathcal D_\rho Y=0$。
因此任何紧含于一个开半球内的实际转折帽，都可以选 $Y>0$，
把完整零阶项精确消去，得到真实散度式系数
$$
\widehat A=Y^2 A,\qquad
\widehat f=Y f_\rho,\qquad f_\rho=\mathcal D_\rho w.
\tag{7.3}
$$
其实际转折集不变，因为 $\det\widehat A=Y^4\det A$。
这一步没有冻结某个 Fourier 模、删除非径向系数或改用平均曲率。

设在任一横截曲线上，以同一个真实面密度和同一个定向定义
$p_v$ 为 $A\nabla v$ 的 conormal density。变换后的完整端口是
$$
\boxed{\quad
U=Y^{-1}w,\qquad p_U=Yp_w-wp_Y.
\quad}
\tag{7.4}
$$
这里 $p_U$ 使用 $\widehat A$，不是原 $A$。
故
$$
p_w=Y^{-1}p_U+(p_Y/Y)w,\qquad
\operatorname{Im}\int p_U\overline U
=\operatorname{Im}\int p_w\overline w.
\tag{7.5}
$$
第二项是必须保留的真实 normal shear。它是实乘子，因此保持通量；
它并不是零。一般源还给准确 charge 恒等式
$$
\int_{\partial\Omega}(Yp_w-wp_Y)
=\int_\Omega Y f_\rho .
\tag{7.6}
$$
所以变换后所谓“常数”是原变量中的 $Y$，而非原 Fourier mean。

如果某一开帽是真正平面片 $n_0\cdot F=d\ne0$，则在星形坐标中
$\rho=(n_0\cdot u)/d$，故 $B=A=0$ 在该帽。
此时 $\mathcal D_\rho w=0$ 本身对该帽的 $w$ 不加约束：
固定帽必须另行施加 $w=0$ 及第 5 节的 $q=0$ 匹配。
特别，多个帽的相对 Killing 场不是该退化方程自动消除的量。

(7.2) 不能在 $Y=0$ 处继续除以 $Y$。对环绕腰部的整个圆柱，
通常不存在一个处处正的一次球谐；该核心仍使用完整 (3.5)。
将一个帽变成散度式，也没有自动证明其实际弱域上的 Dirichlet、
Robin、持握或强范数门。它提供的是可逐项送入真实 cap form/Airy
构造的算子和端口。

## 8. 完整标量算子的切口通量

取一个真实圆柱坐标 $(s,\theta)$，其中 $\theta$ 周期为 $2\pi$。
令 $j=\sqrt{\det\sigma}$。将 (3.5) 乘以真实密度 $j$，得到
$$
P w=\partial_s(a w_s+b w_\theta)
+\partial_\theta(b w_s+c w_\theta)+d w,
\tag{8.1}
$$
其中
$$
a=jA^{ss},\quad b=jA^{s\theta},\quad
c=jA^{\theta\theta},\quad d=j\operatorname{tr}B.
\tag{8.2}
$$
完整 momentum 是
$$p_w=a w_s+b w_\theta.$$
对任意两个齐次解 $u,v$，分部积分给
$$
\partial_s\int
\bigl(p_u\overline v-u\overline{p_v}\bigr)\,d\theta=0.
\tag{8.3}
$$
对一个解，$\operatorname{Im}\int p_u\overline u$ 因而守恒。
零阶 $d$ 因为实且对称而相消；交叉二阶项 $b$ 已包含在完整
momentum 中。这是全部方程的通量恒等式，不只是 eikonal 结论。

在每个固定严格双曲切口，选同一个明确正自伴角算子，例如
$$K=(1-\partial_\theta^2)^{1/2}.$$
定义两个复端口
$$
z^+=\frac{K^{1/2}u-iK^{-1/2}p_u}{\sqrt2},\qquad
z^-=\frac{K^{1/2}u+iK^{-1/2}p_u}{\sqrt2}.
\tag{8.4}
$$
它们在 $u\in H^{1/2}$、$p_u\in H^{-1/2}$ 时属于 $L^2$，
且
$$
\|z^+\|_2^2-\|z^-\|_2^2
=2\operatorname{Im}\langle p_u,u\rangle.
\tag{8.5}
$$
$K$ 含 $1$，所以零角模仍在端口里；没有通过端口定义删除 mean。

实际改角时，高度作普通 pullback，conormal 作对偶密度 pullback。
若 $\theta=\psi(\eta)$，就是
$u\mapsto u\circ\psi$、$p\mapsto\psi'(p\circ\psi)$。
它们共同保持 (8.3)。只变高度而保留旧 momentum 会破坏通量和
后面的真实散射恒等式。

## 9. 严格双曲核心的完整传输确实有界

设固定两个切口间
$$
a>0,\qquad \gamma=b^2/a-c>0
\tag{9.1}
$$
有共同正下界，全部所用系数足够光滑。若 $a<0$ 而不变号，
可先把整个方程乘 $-1$。令
$\alpha=1/a$、$\beta=b/a$、$Z=(u,u_\theta,p_u)^t$。
(8.1) 的完整方程 $Pu=f$ 等价于
$$
Z_s=\mathsf A Z_\theta+\mathsf B Z+(0,0,f)^t,
\tag{9.2}
$$
其中
$$
\mathsf A=
\begin{pmatrix}
0&0&0\\
0&-\beta&\alpha\\
0&\gamma&-\beta
\end{pmatrix},\qquad
\mathsf B=
\begin{pmatrix}
0&-\beta&\alpha\\
0&-\beta_\theta&\alpha_\theta\\
-d&\gamma_\theta&-\beta_\theta
\end{pmatrix}.
\tag{9.3}
$$
初值约束 $Z_2=\partial_\theta Z_1$ 由这两行方程精确传播。

令 $\mathsf H=\operatorname{diag}(1,\gamma,\alpha)$。
则 $\mathsf H\mathsf A$ 对称。定义
$$
\mathsf M=\mathsf H_s-(\mathsf H\mathsf A)_\theta
+\mathsf H\mathsf B+\mathsf B^*\mathsf H,\qquad
\Gamma(s)=\frac12\sup_\theta
\|\mathsf H^{-1/2}\mathsf M\mathsf H^{-1/2}\|_{\rm op}.
\tag{9.4}
$$
若 $E=\int Z^*\mathsf H Z$，准确分部积分给
$$
\left|\frac{d}{ds}\sqrt E\right|
\le \Gamma(s)\sqrt E+\|\sqrt\alpha f(s,\cdot)\|_2
\tag{9.5}
$$
（在 $E=0$ 时用常规的 $E+\varepsilon$ 正则化）。
因此两个方向的 Cauchy 传播及完整 ordinary-source Duhamel 积分
都有有限的明确能量界，例如正向为
$$
\sqrt{E(s)}
\le e^{\int_t^s\Gamma}\sqrt{E(t)}
+\int_t^s e^{\int_r^s\Gamma}\|\sqrt\alpha f(r)\|_2\,dr.
\tag{9.6}
$$
所有低阶项和振幅费用都在同一个矩阵 (9.3)--(9.4) 内。
存在性可由周期 Friedrichs 截断、(9.5) 的统一能量界和弱极限得到；
差的能量界给唯一性。逐阶角微分给预选有限阶 Sobolev 窗口，
所用系数阶也相应明确增加。

(9.6) 先给 $H^1\oplus L^2$ 的 Cauchy 界。
用 (8.3) 和反向传播得到其通量对偶空间
$L^2\oplus H^{-1}$ 的界，再插值，得到
$H^{1/2}\oplus H^{-1/2}$ 的双向有界传播。
故 (8.4) 中的完整端口传输
$$
\binom{z_R^+}{z_R^-}
=T\binom{z_L^+}{z_L^-}+\mathfrak g,\qquad
T=\begin{pmatrix}A_T&B_T\\C_T&D_T\end{pmatrix}
\tag{9.7}
$$
是 $L^2\oplus L^2$ 上的真实有界同构，$\mathfrak g$ 来自同一个
zero-left-full-Cauchy particular。由 (8.3)，
$$
T^*JT=J,\qquad TJT^*=J,\qquad J=\operatorname{diag}(I,-I).
\tag{9.8}
$$
这里切口固定并满足 (9.1)。若令切口趋近转折，$\gamma$ 的下界消失，
(9.4) 会支付实际发散费用；本节没有借形式光滑性免费越过转折。

## 10. 从完整传输到精确两通道散射

由 (9.8)，
$$
D_T^*D_T-B_T^*B_T=I,\qquad
D_TD_T^*-C_TC_T^*=I.
\tag{10.1}
$$
第一式给单射和闭值域，第二式给满射；因此
$D_T^{-1}$ 确实存在且 $\|D_T^{-1}\|\le1$。
取 incoming 和 outgoing 数据分别为
$$
x=(z_L^+,z_R^-)^t,\qquad y=(z_L^-,z_R^+)^t.
$$
完整传输精确等价于
$$
\boxed{\quad y=Sx+\mathfrak s,\quad}
\tag{10.2}
$$
其中
$$
S=
\begin{pmatrix}
-D_T^{-1}C_T&D_T^{-1}\\
A_T-B_TD_T^{-1}C_T&B_TD_T^{-1}
\end{pmatrix},
\qquad
\mathfrak s=
\binom{-D_T^{-1}\mathfrak g_-}
{\mathfrak g_+-B_TD_T^{-1}\mathfrak g_-}.
\tag{10.3}
$$
(8.5) 给 $\|Sx\|=\|x\|$。同样由 (9.8) 有
$A_T^*A_T-C_T^*C_T=I$ 及 $A_TA_T^*-B_TB_T^*=I$，
故 $A_T$ 亦双向可逆。对给定 $y=(z_L^-,z_R^+)$，先由
$z_R^+=A_Tz_L^++B_Tz_L^-$ 解 $z_L^+$，再取
$z_R^-=C_Tz_L^++D_Tz_L^-$，就给 $S$ 的满射。因此
$$
\boxed{S^*S=SS^*=I.}
\tag{10.4}
$$
还由 (10.1) 得 $\|B_TD_T^{-1}\|\le1$，从而例如
$\|\mathfrak s\|\le2\|\mathfrak g\|$。
这些是完整算子的恒等式，包含两支之间的所有低阶耦合和振幅。
$S$ 的两个对角块一般不为零；不能只因几何光线有两支就删除它们。
另一方面，$L^2$ unitary 本身不提供强 Wiener、解析或高 Sobolev
范数的界；这些须从实际传输和所用坐标另外取得。

## 11. 真实转折帽、source contact 和最终边界方程

将两侧实际转折、椭圆区域、极点和持握条件全部放入外部组件。
它们在固定严格双曲切口上给出的完整齐次 Cauchy 关系，由 Green
恒等式为 isotropic。要把它写为一个处处定义的反射算子，还须证明
相应 Robin realization 的存在性、唯一性和正反向满射。
**isotropic 不等于 maximal；这一步是本节明确保留的输入。**

一个可核验的充分实现是：在同一真实弱域上已构造自伴的 full DN
$\Lambda$，并有完整源通量 $k$，使
$$p_{\rm out}=\Lambda u+k.$$
在一个预选正角算子 $K$ 下，若
$L=K^{-1/2}\Lambda K^{-1/2}$ 为同一真实自伴 realization，则以
(8.4) 的该侧 outward conormal 定义端口，有
$$
z^-=\mathcal R z^+
+i\sqrt2(I-iL)^{-1}K^{-1/2}k,\qquad
\mathcal R=(I+iL)(I-iL)^{-1}.
\tag{11.1}
$$
自伴谱演算给 $\|(I-iL)^{-1}\|\le1$，以及
$\mathcal R^*\mathcal R=\mathcal R\mathcal R^*=I$。
在全核心的 left/right 定向中，按需要使用此关系或它的逆；
相应 affine source 必须同时反向，不能只翻转齐次矩阵。

式 (11.1) 是一种充分表示。若 Dirichlet 图在某频率有极点，
也可直接用已证的非实 Robin 响应给出同一最大中性关系，
不要求一个不存在的处处有界 DN。反之，没有 Robin 存在性证明时，
不把 (11.1) 仅当作符号公式使用。

源通量必须包括 contact 项。具体地，若 (7.2) 后采用
$P_{\rm cap}=-\operatorname{div}\widehat A\nabla$，
右端是 $F_{\rm cap}=-Yf_\rho$，弱 form 为
$\mathfrak e(U,V)=\int\widehat A(\nabla U,\nabla\overline V)$，
$G$ 为同域零 Dirichlet inverse，$E$ 为真实边界延拓，则
$$
\boxed{\quad
\langle k,h\rangle
=\mathfrak e(GF_{\rm cap},Eh)-\langle F_{\rm cap},Eh\rangle.
\quad}
\tag{11.2}
$$
它来自对完整方程积分，不是一个可删的边界修饰。
若固定帽使自然域改变，应使用改变后的同一个 $G,E$；
不能从另一 realization 移植源通量。

假设这些实际外部组件已经给出完整反射及源
$$
x=R_{\rm cap}y+\mathfrak h.
\tag{11.3}
$$
若两帽确实是互不相连的两个组件，$R_{\rm cap}$ 是其反射的直和。
若一个外组件连接两个端，必须保留其 full two-end matrix 和 cross
项；本文不通过记号将它块对角化。
与 (10.2) 联立，整个实际边值问题精确化为
$$
\boxed{\quad
(I-R_{\rm cap}S)x
=\mathfrak h+R_{\rm cap}\mathfrak s.
\quad}
\tag{11.4}
$$

在已规定的 cap 唯一重建域和核心 Cauchy 域中，(11.4) 的解与原
全 PDE 的解双向一一对应：由 $x$ 得 $y$，分别重建核心及外部场，
相同的高度和完整 momentum 首先给真实的分布接合；在所声明的
强迹和源匹配条件下，由切口的 $a\ne0$ 和同一 PDE 递推恢复该域
要求的强接合。极端帽及极点的 $C^2$ 极限仍须另付。
反向取迹即得 (11.4)。
额外的刚体 gauge、标量弯曲核、多个帽的相对 Killing 条件及幅度
条件应作为同一个增广系统保留。隐藏的零全 Cauchy cap 解若没有
被域条件排除，也必须作为额外核块加入，不能宣称自动唯一。

若已证明 $(I-R_{\rm cap}S)^{-1}:H^{s+\ell}\to H^s$ 有常数 $M_s$，
且上述源、重建和接合映射有各自明确的范数，则完整标量 PDE 逆
由这些映射的组合得到；再由 §§4--5 恢复真实环境场。
这给准确的双向接口。它本身没有证明 (11.4) 的小除数门。
尤其一条射线返回图的旋转数只描述其主 canonical graph，
不能决定 $S,R_{\rm cap}$ 的完整振幅、有限低模和负阶相位。

## 12. 当前可用范围与必须另付的部分

本文已经独立证明：

1. 当前真实严格星形图的完整度量线性化，等价于全局自伴
   $\mathcal D_\rho$ 加一个有明确范数的球面切向重建。
2. 转折帽只要落在开半球内，就有准确的散度式变换、真实 source、
   normal shear 和 charge；实际转折集及型别保持。
3. 固定严格双曲切口之间，完整 source/Cauchy/两通道散射均来自
   同一实际方程，且通量代数准确保留全部低阶项。
4. 一旦实际外部 Robin 响应和 (11.4) 的强逆得到认证，便有明确的
   反向 PDE 重建；多个持握帽的相对刚体条件仍在同一增广系统内。

当前候选还须验证严格星形和所有实际类型门，并为其真实转折
realization、全频边界缺陷、源/强范数及固定帽条件给出定量证书。
R30/R31 的圆周共轭只能作用于实际证明等价的主返回图；不能直接
替代 (11.4) 的完整算子。低阶相位与 smoothing 余项是否能进入
已有正常形、以及是否满足其小量和除数门，仍是具体算子问题。

**来源与适配范围。** 写作中已逐节核对邻题的
[R513](../../continuous-flexibility-swarm/results/R513-direct-log-physical-local.md)
§§4--6、9、12--13，重点是完整 conormal/source contact、真实 cap
Robin、负段传输、共同通量归一与完整 feedback。本文 §§1--11 的
恒等式及接口证明独立给出；R513 的原固定型别、材料、小量、source
域、角权和累计增量前提没有因此自动授给本题。式 (7.2)--(7.5)
只提供了开始逐项验证那些前提的真实算子变换。


