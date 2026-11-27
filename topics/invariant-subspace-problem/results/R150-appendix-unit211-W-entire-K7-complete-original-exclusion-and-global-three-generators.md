# R150：整个 K7 原权曲线排除与全余 W 的物理 λ 三生成规则

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 完整结论与原域

在当前一般 LS、$\Delta=0$、$W=0$、原单值互异的既有物理单位域中，整个权曲线

$$
K_7(e,k)=12e^2k^2-ek^3+8ek^2-k^3-4k^2-16k-16=0
\tag{1}
$$

没有完整原点。以后可以在**这个完整 W 原图**支付 $K_7$。

由此前实际四头因式，这同时使三条固定原均值 $E_1,E_{Be},E_{Bo}$ 在物理 $\lambda$ 坐标下的 $x^2,xy,y^2$ 头处处可逆。相应原多项式商在仅按权量局部化的 $\mathbb Q[e,k][\lambda]$ 上由 $1,x,y$ 生成。每个固定 $(e,k,\lambda)$ 的有限原几何纤维长度至多 3。

这里不把三生成元称为自由基底，不把关于 $\lambda$ 的三生成性改写成权环上的三点界，也不把任意后续几何局部化未经论证称为全局有限模。$\Phi=0$ 和 $h_U=k_U$ 碰撞图不在本定理的范围内；整个 W 仍须继续原方程返回。

## 2. 已完成的整 K7 覆盖

[完整参数定理](R150-appendix-unit211-W-entire-K7-rational-parameter-and-original-rho-cover.md)已经保两支和所有允许退化点，给出

$$
A=m^2-6m+6,\quad
B=m^2-4m+6,\quad
C=m^3-10m^2+36m-36,
$$

$$
k=\frac{2A}{m},\qquad e=\frac C{6A},\qquad
u=e+1,\quad Q=ek,\quad V=uk+2,
$$

$$
\ell=\frac{u((k+2)^2-2ek)}{kV}.
\tag{2}
$$

$m,A,B$ 已由完整反向身份支付。每个有限原 $K_7$ 点都落入 (2)，没有只取一个有理开集或一个判别式分支。

随后[原理想三次平方定理](R150-appendix-unit211-W-entire-K7-original-cubic-square-cover-and-finite-environment.md)实际证明

$$
C_3(m)^2\in I_6,\qquad
C_3(m)=m^3-4m^2-6m+18,
\tag{3}
$$

其中

$$
I_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S)
$$

在同一原权单位局部化环中取值。该次实际原六项组合、全部主元零纤维和已付分母均已登记。本次不重算其 242 次行列式、107 次残式或大 Bézout。

因此剩下的准确输入是**整个**

$$
K=\mathbb Q[m]/(C_3),
\tag{4}
$$

而不是一个浮点根。其三维正规表示保留全部三个复嵌入。

## 3. 整三维常数代数中的原 Gram

新源从 (2)、(4) 直接构造原常数代数。每次降幂都核商余乘回，每次逆都用完整 QQ 一元 Bézout 并核乘积为 1。程序保留真正非单位的两整个因子；本次实际没有发生分裂。

置 $d=1-Q$、$\rho^2=d$，并取原形式

$$
b=\frac\ell2+\frac{u-\ell}{2d}\rho,\quad
c=\frac\ell2-\frac{u-\ell}{2d}\rho,\quad
p=1+\rho,\quad q=1-\rho.
$$

在独立变量 $x,y,t$ 中，$X=x+y\rho$、$Y=x-y\rho$。令

$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,
$$

$$
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,\quad
P_f=T_0(J-Q).
$$

$f,\lambda,T$ 由原 $E_0,N_0,P_1$ 恢复：

$$
f=\frac{ux+(u-\ell Q)y-T_0/2}{2u},
$$

$$
\lambda=
\frac{V_2x+(2u-uQ-\ell Q)y-uT_0-(V_2+2u^2)f+bcQt}{P_{02}},
$$

$$
T=
\frac{[\lambda P_{02}-(1-u)T_0]T_0-P_ff-\Phi bcQt}{QP_{02}}
-\ell.
\tag{5}
$$

原 Gram 四行、原迹与六式定义采用[整 C9 原系统正文](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md)第 3 节；新源完整写入并实际重建这些定义。它核回原 $E_0$、$N_0$、$P_1$、四个原二次以及两个加权原三次。

尤其本次没有使用 $J_{19}$、$G_{36}$ 的泛型头来代替有限纤维验证，也没有用模素数证据或数值抽样判空。

## 4. 原 48×35 恒等式直接返回 D

令

$$
A_2=2\lambda^2-2\lambda+1,\qquad
D=\ell A_2-T^2.
\tag{6}
$$

取 $x,y,t$ 总次数至多 4 的全部 35 个单项式。四个原二次分别乘总次数至多 2 的十个单项式，两个原三次分别乘总次数至多 1 的四个单项式，得到**固定原 48×35 矩阵**。

所有系数始终在整个 (4) 中，所有行均是字面上的原式乘单项式。实际行秩为 **33**；这里没有宣称矩阵满列秩或原六式在 (4) 中直接给常数 1。

实际返回的是

$$
D=\sum_{j=0}^5 a_j(m,x,y,t)F_j
\quad\text{in }K[x,y,t],
\tag{7}
$$

$$
(F_0,\ldots,F_5)=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
$$

程序将 (7) 的全部 35 列乘回，随后又把原多项式组合直接乘回到 $D$。本次共 62 次真逆、94382 次有限降幂乘回；组合证书编码 6827 字节，SHA256 为

850562a0ef9955744a9bfeb313a5ee1c15538b219f1c0ab6ae61f3758f2f97c1。

故每一个允许的三次权点上的原解都满足 $D=0$。没有剩余共轭根、未付范数零支或被跳过的常数主元分量。

源码还准备了仅在此输入未返回时才使用的完整 $HA/HB$ 六次后果和 181×84 新输入；**本次没有执行该分支，也不把它写成已完成证据**。

## 5. 物理 D 与整个 K7 的矛盾

本稿沿用原互异单值图的准确身份

$$
D+\frac{\ell}{u^2}HA=bc\,(h_U-k_U)^2.
\tag{8}
$$

在完整原点，$HA=0$；原 $b,c,h_U-k_U$ 均非零。因此这个原图上

$$
D\ne0.
$$

这与 (7) 矛盾。$D$ 的支付来自同一个原物理图，不从其它碰撞支外推，也不把 $D$ 的多项式范数误当作已付量。

还可以直接说明非约化层面没有遗漏：将 (7) 从 (4) 提回原权单位局部化环，给

$$
D\in I_6+(C_3).
$$

于是

$$
D^2\in I_6+(C_3^2)=I_6
\tag{9}
$$

由 (3) 成立。在当前物理 $D$ 局部化后，(9) 给单位理想。因而原三次平方的幂零层也不留下合法分量。

完整参数 (2) 覆盖整条 (1)，而 (3) 已穷尽所有可能 $m$，所以整 $K_7=0$ 原支关闭。

## 6. 三条固定均值头在全余 W 上支付

[物理 λ 四头定理](R150-appendix-unit211-W-physical-lambda-four-heads-global-affine-and-finite-rank-defect.md)已经实际核出全域可逆坐标

$$
\lambda=\alpha_0+\alpha_xx+\alpha_yy+
\frac{bcQ}{P_{02}}t,
\qquad
t=\frac{\lambda-\alpha_0-\alpha_xx-\alpha_yy}{bcQ/P_{02}}.
\tag{10}
$$

系数 $bcQ/P_{02}$ 是原权单位。对每条完整原式，正反代换均已实际回乘。

记变换后 $E_1,E_{Be},E_{Bo}$ 的 $(x^2,xy,y^2)$ 头矩阵为 $H_3$。此前完整 QQ 因式和原乘回给

$$
\det H_3=U(e,k)\,K_7(e,k),
\tag{11}
$$

$U$ 为此前已付权量的乘积乘非零 QQ 常数；该头没有其它未付因子。由本稿第 5 节，(11) 现在在整个余 W 原图上非零。

因此用真正 $\operatorname{adj}(H_3)/\det H_3$，三条原均值给出

$$
\begin{aligned}
x^2&=a_0(\lambda)+a_1(\lambda)x+a_2(\lambda)y,\\
xy&=b_0(\lambda)+b_1(\lambda)x+b_2(\lambda)y,\\
y^2&=c_0(\lambda)+c_1(\lambda)x+c_2(\lambda)y.
\end{aligned}
\tag{12}
$$

这些是三条原均值的准确线性组合，分母只含已付权量。由原总次数至多 2 和头矩阵与 $\lambda$ 无关，

$$
\deg_\lambda a_0,\deg_\lambda b_0,\deg_\lambda c_0\le2,
$$

$$
\deg_\lambda a_i,\deg_\lambda b_i,\deg_\lambda c_i\le1
\quad(i=1,2).
\tag{13}
$$

第 (13) 式是多项式次数的直接保持结论，不依赖另一次大矩阵运行。

任一 $x,y$ 总次数至少 2 的单项式，都可用 (12) 降低 $x,y$ 总次数。因此对当前权单位环 $A_W$，三原均值的多项式商以及再加其它原多项式关系的商，都由

$$
1,\ x,\ y
$$

作为 $A_W[\lambda]$ 模生成。不要求三规则构成自由商的 Gröbner 基，也不要求重写余式唯一；重叠产生的剩余原关系仍须保留。

原 $\lambda$ 单位的局部化是系数环的局部化，可以相应基变换。对于依赖 $x,y$ 的其它几何量，例如 $D$，本稿只把原点放入上述有限多项式环境的局部化，不另宣称该局部化仍在未经扩大的 $A_W[\lambda]$ 上三生成。每个固定 $(e,k,\lambda)$ 后，环境是至多三维的 Artin 代数，此时再局部化只删分量，所以各有限原几何纤维长度至多 3。

完整 $N_1,N_S,P_S$、个别原值和原理想相容条件继续保留。原四头共同降秩支也因此关闭，因为它此前必落入 $K_7=0$；这不等于排空所有余 W 原方程。

## 7. 真实证据与入口失败分离

正常首次科学运行的自含源：

[2026-11-28-unit211-W-entire-K7-last-cubic-original-QQ-return-8542.py](../notes/2026-11-28-unit211-W-entire-K7-last-cubic-original-QQ-return-8542.py)

对应小回执：

[2026-11-28-unit211-W-entire-K7-last-cubic-original-QQ-return-receipt-8542.json](../notes/2026-11-28-unit211-W-entire-K7-last-cubic-original-QQ-return-receipt-8542.json)

源 Git blob 941897e3d0996360314f22dd30f4eefdc7558acf，15124 字节，SHA256：

7d0855230abc8f16a0c965e62f75cede3a66a1dbea64fd9b484801ef8241e822。

真实 run 46076745817 / job 140766143584，source commit 22e753773375efc483000ff580592e173f000583。源最终数学标记 0.234906910 秒；驱动 0.299187631 秒、峰值子进程 RSS 37528 KiB、内层 exit 0。上限 180 秒、4 GiB。没有需要追加的运行门。

stdout 2391 字节，SHA256：

20ba617f58b42de9f15573cf61ee8d4df10f243c32f7ce6a35856af62f691610。

真实 pull 在 2026-11-27 22:27:37.610680 UTC，从 22e753773375efc483000ff580592e173f000583 到 f001ca62c1081b7e542c842d14c198ce16b6bee5，两个 README 均无差异。

更早的 run 46076646594 / job 140765817594 使用 f16d9c5915e362d828c50d6feb43e49bb24c6b0b；文件当时误置课题根目录，工作流在读取 notes 路径时 git exit 128。该次没有启动 Python 数学源，没有科学阶段或科学回执；它是入口打包失败，不算数学排除或数学算法失败。修复仅把相同原 blob 放到正确 notes 路径，科学源没有更改。两次状态均原样保留。

本稿关闭整个 K7 并把固定三均值头全域化；后续使用 (12) 返回全部原行，继续余 W。
