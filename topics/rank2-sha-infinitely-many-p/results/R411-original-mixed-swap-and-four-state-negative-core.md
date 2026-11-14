# R411 — 原 mixed 来源的准确交换、共同二挠平均与四态负谱返回

日期：2026-11-14。**状态：已证明。** 在 R407 的同一个固定无穷 ray 上，
本篇求出两条实际 mixed 来源在有限 core 群中的准确关系：第一轴算子与
第二轴四次算子都交换它们。全十六项不变投影因此各为原乘积的一半；
差来源是非零的负谱，完整正则化只需四条来源。
没有把该负谱的中央值、导数或任意单项预赋为零；主目标仍未完成。

## 1. 同一来源和结论

全部曲线、周期、半特征、真实 trace 算子与 R404、R407 相同。
特别地，$\delta^2=-3$、$\omega=(-1+\delta)/2$，
$$
\mathcal C(Z)=\sigma(\delta Z)\sigma(2\delta Z)
                 \sigma(\gamma_7Z)\sigma(\bar\gamma_7Z),
\qquad \gamma_7=(5+\delta)/2,
$$
$$
S(Z)=-\frac{\mathcal C(Z)\sigma(Z)\sigma(2Z)}{84},\qquad
T(W)=-\frac{\mathcal C(W)\sigma(3\delta W)\sigma(4W)}{504\delta}.
\tag{1}
$$
用 R404 的两个实际十二 sigma 来源 $B_2,B_3$，置
$$
F_2(z,w)=B_2(2z,2w),\quad F_3(z,w)=B_3(2z,2w),\quad
F_0=S(2z)T(2w)=F_2+F_3,\quad D=F_2-F_3.
\tag{2}
$$
保持真正的二覆盖空间
$\mathcal S_{136}\otimes\mathcal S_{288}$，不先将单项下降。
令 $K_1=K_{136}\otimes I$、$K_2=I\otimes K_{288}$。

**定理。** 对 R407 的固定 ray：
$$
\boxed{
K_1F_2=F_3,\quad K_1F_3=F_2,\qquad
K_2^4F_2=F_3,\quad K_2^4F_3=F_2.
}
\tag{3}
$$
因而 $K_1D=K_2^4D=-D$，而 $K_1F_0=K_2F_0=F_0$。
在整个固定空间上的群平均
$$
P=\frac1{16}\sum_{a=0}^{1}\sum_{b=0}^{7}K_1^aK_2^b
$$
满足准确的实际来源身份
$$
\boxed{PF_2=PF_3=\tfrac12F_0,\qquad PD=0.}
\tag{4}
$$
此外，差来源不是零：
$$
\boxed{[z^8w^4]D=64\delta.}
\tag{5}
$$
在这里的 $p>19$ 普通整模型中，$\delta$、$2$ 和原普通周期均为单位，
故该差来源仍然 primitive。它不能作为一条额外 rank-two 曲线来源。

## 2. 包含中心的有限 theta 计算

取 $\Lambda=\Omega(\mathbf Z+\omega\mathbf Z)$。
R407 的原对称 lift 为
$$
\mathsf T_vF(z)=e^{-N\eta_v(z+v/2)}F(z+v).
$$
对偶数 $N$，若 $v=(a+b\omega)\Omega/N$、
$\ell=(A+B\omega)\Omega\in\Lambda$，准周期公式直接给
$$
\mathsf T_{v+\ell}=(-1)^{Ab-Ba}\mathsf T_v.
\tag{6}
$$
这是下文所需的中心符号，不能只把 $gv$ 模 $N$ 化简。

记
$$
U_N=\mathsf T_{\Omega/N},\quad V_N=\mathsf T_{\omega\Omega/N},
\quad A_N=U_N^{N/2},\quad B_N=V_N^{N/2},\quad RF(z)=F(-z).
$$
在 $N=136,288$ 两种情形，$A_N,B_N$ 是可交换的二阶算子。
其中 $B_N$ 与 $U_N$ 反交换，$A_N$ 与 $V_N$ 反交换，
另外两对交换。置
$$
Q_N=\frac{A_N+B_N+A_NB_N-I}{2},\qquad
\mathcal E_N=\frac{I+A_N+B_N+A_NB_N}{4}.
\tag{7}
$$
在 $(A_N,B_N)$ 的四个共同特征空间上，$Q_N$ 的特征值分别为
$+1,-1,-1,-1$，故
$$
Q_N^2=I,\quad Q_N=2\mathcal E_N-I,
\quad Q_NU_NQ_N=-U_N^{1+N/2},
\quad Q_NV_NQ_N=-V_N^{1+N/2}.
\tag{8}
$$
$\mathcal E_N$ 正是原四个二挠平移的平均。

R407 已给出第一轴的真实有限比例
$g\equiv203+136\omega\pmod{272}$。
对 $\Omega/136$，其像的坐标是 $(203,136)$；
对 $\omega\Omega/136$，其像的坐标是 $(-136,67)$。
用 (6) 分别化到 $(67,0)$、$(0,67)$，两个符号都是 $-1$。
因此 $K_{136}$ 对两个生成元的共轭为
$U_{136}\mapsto-U_{136}^{67}$、$V_{136}\mapsto-V_{136}^{67}$。
由 (8)，$RQ_{136}$ 给同一个**含中心**的自同构。
R407 已证原 theta 表示不可约，故两算子只差标量。

非零来源 $S(2z)$ 被 $K_{136}$ 固定；它是偶函数，且被所有
二挠 lift 固定，因为它确实从 degree34 来源作 $[2]$ 拉回。
于是 $RQ_{136}S(2z)=S(2z)$，准确锁定标量为一：
$$
\boxed{K_{136}=RQ_{136}.}
\tag{9}
$$

第二轴 R407 的比例为 $g\equiv91+72\omega\pmod{576}$。
在 $\omega^2+\omega+1=0$ 中直接平方得到
$$
g^2\equiv217+432\omega,\qquad
g^4\equiv433+288\omega\pmod{576}.
$$
两个生成元的坐标分别化为 $(145,0)$、$(0,145)$，中心符号仍各为
$-1$。因 $145=1+288/2$，$K_{288}^4$ 与 $Q_{288}$ 诱导相同
自同构；以实际非零 $T(2w)$ 锁定标量，得到
$$
\boxed{K_{288}^4=Q_{288}=2\mathcal E_{288}-I.}
\tag{10}
$$
这些计算用的是 R407 的固定 $g$ 及实际锚，不是任选 metaplectic lift。

## 3. 原第一轴的精确倍点 trace

下面直接计算实际 $F_2$ 的二挠平均。
写 $Z=2z$、$W=2w$，并置
$$
y_0=(4+3\delta)W/2,\qquad v_0=(-4+3\delta)W/2.
$$
原式准确为
$$
F_2(z,w)=\frac{\mathcal C(2z)\mathcal C(W)}{42336\delta}
\sigma(3z+v_0)\sigma(3z-v_0)
\sigma(y_0-z)\sigma(y_0+z).
\tag{11}
$$
在 $E_b:y^2=x^3+b$ 上，令 $x=x(z),y=y(z)$、
$X=x(2z),Y=y(2z)$，并记 $x_3=x(3z)$。
定义真正的椭圆函数
$$
r(z)=\frac{\sigma(3z)^2\sigma(z)^2}{\sigma(2z)^5}
     =-\frac{\psi_3(x)^2}{32y^5}
     =-\frac{(x-X)^2}{2y},
\quad \psi_3(x)=3x(x^3+4b).
\tag{12}
$$
这里 $\sigma(2z)=-2y\sigma(z)^4$，
$\sigma(3z)=\psi_3(x)\sigma(z)^9$，而
$x-X=\psi_3(x)/(4y^2)$，故 (12) 包括整体符号。

**倍点 trace 引理。** 对完整的四个 $[2]$ 原像，
$$
\boxed{
\operatorname{Tr}_{[2]}r=0,\quad
\operatorname{Tr}_{[2]}(rx)=-4Y,\quad
\operatorname{Tr}_{[2]}(rx_3)=4Y,\quad
\operatorname{Tr}_{[2]}(rxx_3)=0.
}
\tag{13}
$$

**证明。** 四个横坐标是首一四次多项式
$$
f(X_0)=X_0^4-4XX_0^3-8bX_0-4bX
\tag{14}
$$
的根。倍点纵坐标式为
$$
Y=\frac{x^6+20bx^3-8b^2}{8y^3}.
$$
代入 (14) 得 $f'(x)=8Yy$，所以 (12) 等于
$-4Y(x-X)^2/f'(x)$。
对首一可分四次多项式，Lagrange 插值给
$\sum_i h(x_i)/f'(x_i)=[X_0^3](h\bmod f)$。
对 $h=(X_0-X)^2,X_0(X_0-X)^2,X_0^2(X_0-X)^2$，
三个系数准确为 $0,1,2X$；因而
$$
\operatorname{Tr}r=0,\quad\operatorname{Tr}(rx)=-4Y,
\quad\operatorname{Tr}(rx^2)=-8XY.
$$
另外三倍点公式
$x_3=x-8y^2(x^6+20bx^3-8b^2)/\psi_3(x)^2$
与 (12) 给 $r(x_3-x)=2Y$。
再用 (14) 的 $\operatorname{Tr}x=4X$，即得 (13) 的后两式。
在泛点上的证明给出有理函数身份，故不受个别分支坐标或极点限制。
证毕。

令 $H(Z)=\mathcal C(Z)\sigma(Z)^5$。
由 (1) 和倍点式，$H=42S/y$ 是同一 degree34 线丛的全纯截面。
其 $[2]$ 拉回 $H(2z)$ 被原二挠 lift 固定。
两次使用原 sigma 加法公式，将 (11) 写成
$$
\frac{H(2z)\mathcal C(W)\sigma(y_0)^2\sigma(v_0)^2}
     {42336\delta}
\;r(z)\bigl(x(v_0)-x_3\bigr)\bigl(x-x(y_0)\bigr).
\tag{15}
$$
因此第一轴二挠平均恰为括号后椭圆函数的完整 $[2]$ trace 除以四，
不缺中心相位。由 (13)，该平均为
$Y\bigl(x(y_0)-x(v_0)\bigr)$。
而
$$
\sigma(y_0)^2\sigma(v_0)^2
 \bigl(x(y_0)-x(v_0)\bigr)
=-\sigma(3\delta W)\sigma(4W).
$$
结合 $S(Z)=YH(Z)/42$，完整常数给
$$
\boxed{(\mathcal E_{136}\otimes I)F_2=\tfrac12F_0.}
\tag{16}
$$
由于 $F_2+F_3=F_0$，$F_3$ 的同一平均也是 $F_0/2$。
这一步实际用了全部四个倍点原像，不是从维数或少数展开项猜标量。

## 4. 同一二挠对角使第二轴平均相等

两个 $F_j$ 各自在第一轴是偶函数：$\mathcal C$ 为偶函数，
四个 active sigma 成两对，改变 $z$ 的符号只交换每对并产生偶数个负号。
于是 (9)、(16) 已给 (3) 的第一轴两式。

为计算第二轴，不需要一个新的高次 trace。
对每个 $\ell\in\Lambda$，考虑完整二变量 lift 的平移
$$
h=(\ell/2,-\ell/2).
$$
共同八个 sigma 的增量成 $+c\ell,-c\ell$ 四对，半特征乘积为一。
在 $F_2$ 的四个 active 因子上，增量分别为
$$
(2-3\omega)\ell,\quad(1+3\omega)\ell,\quad
(-4-3\omega)\ell,\quad(-3-3\omega)\ell.
$$
模 $2\Lambda$，它们依次为
$\omega\ell,(1+\omega)\ell,\omega\ell,(1+\omega)\ell$。
所以半特征的乘积也是一。
对 $F_3$，四个系数为
$$
-2-3\omega,\quad5+3\omega,\quad-3\omega,\quad-1+3\omega,
$$
得到相同的模二列表和相同结论。

全部线性、二次指数由 R404 已付的 Gram
$\operatorname{diag}(136,288)$ 及零交叉项准确成为本二变量 lift 的
正规化指数。因此以上半特征计算给的是实际身份
$$
\boxed{\mathsf T^{136}_{\ell/2}\mathsf T^{288}_{-\ell/2}F_j=F_j.}
\tag{17}
$$
也可直接使用 equianharmonic 准周期式
$\eta_{a\ell}=\bar a\eta_\ell$ 展开各因子；Gram 等式消去全部
$z,w$ 项，剩余的正是上列四对半特征。

每个半周期 lift 的平方为一，故 (17) 等价于
第一轴和第二轴的对应二挠平移在 $F_j$ 上相等。
四项平均得到
$$
(I\otimes\mathcal E_{288})F_j
=(\mathcal E_{136}\otimes I)F_j=\tfrac12F_0.
\tag{18}
$$
现在 (10) 给出 (3) 的第二轴两式。
再平均第二轴八个算子，利用 $K_2F_0=F_0$，得到 (4)。

## 5. 负谱确实存在，原十六列缩为四条差来源

$\mathcal C(z)=-42z^4+O(z^{10})$。
R404 未拉回的 $B_2$ 在 $w^4$ 项中的四个 active sigma 首项为
$-(9/16)z^4$，$B_3$ 为相反号。
因此
$$
[z^8w^4](B_2-B_3)=-\frac3{64\delta}.
$$
双 $[2]$ 将此项乘以 $2^{12}$，得到 (5)。
特别地，这个负谱来源对固定无限 ray 上每个普通好素数都仍存在。

还有一个直接处于两轴 $\mu_6$ 不变部分的系数。
原四个 active sigma 的最低齐次项，对 $B_2,B_3$ 的
$z^2w^2$ 系数分别是 $-55/8+12\delta$、$55/8+12\delta$。
乘共同首项 $z^4w^4/(24\delta)$，再作双 $[2]$，得到
$$
\boxed{[z^6w^6]D=\frac{7040\delta}{9}.}
\tag{18a}
$$
此数在所有当前 $p>19$ 都是单位。
若 $\Pi_6$ 表示两轴各自六次单位旋转的平均，
则 $z^6w^6$ 项被保留，故 $\Pi_6D\ne0$。
因此也不能仅用两轴的 $\mu_6$ 角度零投影删去实际负谱；
这里没有把有限 $\mu_6$ 投影当成整个随 $p$ 变化的 tame 投影。

由 (3) 及交换性，
$$
K_1K_2^bF_j=K_2^{b+4}F_j,\qquad
K_2^{b+4}D=-K_2^bD.
\tag{19}
$$
所以原十六个形式列在这两个实际来源上至多有八个不同列，
而除去共同的 $F_0/2$ 后只需四条带符号返回的差来源。
其第二轴谱满足 $X^4+1$，并不含特征一。

### 5.1 四条差来源恰好独立

这里还可以确定实际循环块的维数。令 $K=\mathbf Q(\delta)$。
同一 theta 空间有原 $K$-模型
$\mathcal S_N(K)=\sigma^N L(NO)(K)$。
两个 $F_j$ 都属于这两个 $K$-模型的张量积：
例如 (15) 先用两次 sigma 加法，再把每个
$\sigma(az)^2/\sigma(z)^{2Na}$ 写成 CM division 函数，
以及把 $x(az)$ 写成原 CM 同源有理函数，即得到 $K$ 系数。
这里平方已消除可能的二挠半特征，原分母 $42336\delta$ 也在 $K$ 中。
共同因子 $\mathcal C(2z),\mathcal C(2w)$ 的各个乘子都是 $2c$，
其 division 函数同样在 $K$ 上；标准首项锁定常数，没有任选代数根。

$K_{288}$ 也保持此 $K$-模型。
在 R407 (7)–(8) 中，原 $\pi\equiv1\pmod{2\mathcal O_K}$，
$r_\pi,r_{\bar\pi}$ 的除子、CM 同源和完整函数域 trace 都在 $K$ 上，
且 division 函数首项为 $\pi,\bar\pi$。
其规范化标量 $\bar\pi/p$ 仍在 $K$ 中。
因此此处不是仅在含全部 theta 常数的未定扩域上讨论线性独立。

多项式 $X^4+1=\Phi_8(X)$ 在 $K$ 上不可约：
$\mathbf Q(\zeta_8)$ 的三个二次子域为
$\mathbf Q(i),\mathbf Q(\sqrt2),\mathbf Q(\sqrt{-2})$，均不是 $K$，
故 $[K(\zeta_8):K]=4$。
由 $D\ne0$、$\Phi_8(K_2)D=0$，循环向量 $D$ 的最小多项式
是 $\Phi_8$ 的非恒定因子，所以只能是 $\Phi_8$ 本身。
因此
$$
\boxed{D,\ K_2D,\ K_2^2D,\ K_2^3D
       \text{ 在 }K\text{ 上线性独立}.}
\tag{19a}
$$
有限维向量空间的域扩张保线性独立，故该结论在每个相关完成后仍成立。
扩到包含八次根单位的系数域时，四个 primitive 八次特征的投影各自非零。
这不声称某个指定投影在模 $p$ 后还是单位，也不涉及中央泛函的非零性。

## 6. 两个单项的完整正则化

使用 R407 (24) 的同一完整 unit-cell 泛函 $\mathcal J_G(u,v)$，
并先在 $|q_1|,|q_2|<1$ 使用该篇的 $A_1,A_2$。
将 (19) 代入原十六列公式，两个真实因子准确相消：
$$
\boxed{
\mathcal R_D(q_1,q_2;u,v)
=\frac{\displaystyle\sum_{b=0}^{3}A_2^b
                    \mathcal J_{K_2^bD}(u,v)}
       {(1+A_1)(1+A_2^4)}.
}
\tag{20}
$$
其推导是分子中的 $(1-A_1)(1-A_2^4)$
分别抵消分母 $(1-A_1^2)(1-A_2^8)$；
每条 unit-cell 泛函仍保留两个实际输出及全部碰撞补域。

同时
$$
\mathcal R_{F_0}
=\frac{\mathcal J_{F_0}(u,v)}{(1-A_1)(1-A_2)},\qquad
\boxed{\mathcal R_{F_2}=\tfrac12(\mathcal R_{F_0}+\mathcal R_D),\quad
       \mathcal R_{F_3}=\tfrac12(\mathcal R_{F_0}-\mathcal R_D).}
\tag{21}
$$
principal 分支取 $q_1=q_2=1$，R407 的
$1-\lambda^2,1-\lambda^8$ 为单位，故
$1+\lambda,1+\lambda^4$ 也各为单位。
所以 (20) 给同一个整 Tate 环正则化，未引入额外的有限部选择。
返回未拉回 $B_j$ 时仍须乘 R407 (28) 的准确 $[2,2]$ Mellin 因子。

若两条实际曲线中央导数同时为零，已知的是 (21) 的共同正谱项
具有双轴二重零。式 (20) 的四条差来源没有因此各自变成中央零。
本篇支付了实际有限群分解和全部差项的准确返回分母，
但仍须新的算术输入来约束该差项，或直接证明原 $J_S',J_T'$ 联合非零。

直接依赖：[R404](R404-two-original-ranktwo-riemann-joint-and-complete-two-axis-central-transport.md)、
[R407](R407-original-riemann-cover-finite-cores-and-integral-regularization.md)。
倍点 trace (13)、二挠交换 (17) 及包含中心的 (9)、(10) 在本文完整证明。
