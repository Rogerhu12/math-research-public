# 条件全三阶径向帽：完整独立审查

2026-11-10；Astra-visible-flex-78718bd0 / independent_audit。

**结论：原稿全部十节在明确的条件性、有限阶范围内通过完整独立审查。**
本审者未参与原稿构造或浮点参数搜索。已独立重推中心源的准确幂次、
两条 Euler 积分式、真正 Cartesian 二次型、Green 充分性、非共振 3n 模、
真实闭柱边以及三阶标架和位置积分。没有发现阻断证明的缺口。

结论是：在四个严格假设 $D_n=0,D_{2n}\ne0,D_{3n}\ne0,\mathfrak C_n=0$
都成立时，三阶形式等距帽和真实柱边三阶匹配可解。
本稿及本审查没有支付这些假设在某个具体剖面上的联合存在，也没有把浮点零
当成精确零；它仍不构造精确非线性等距族或本题闭面。

## 1. 冻结对象和依赖

本次全文审查：

- `notes/2026-11-10-78718-geometry-third-order-cap-v1.md`，10313 字节，
  SHA256 `7a2928fb33ff78a0d4038202a3c1540705791d2da21f979b5e45774418c6ca45`。
- 二阶输入是已由 root 全文独审、登记 R60 的
  `notes/2026-11-10-78718-geometry-second-order-cap-v2.md`，16919 字节，
  SHA256 `05e86cb4cfedef178316bdfb50bc2519ef663fff013add771b1720b769dbe9f7`。
- 三阶源与必要积分使用
  `notes/2026-11-10-78718-geometry-cubic-cap-v1.md`，8656 字节，
  SHA256 `bae8d9f081f85d08cf81539bcb01cb93b2125a1e774aee302abdf5ae86f9cbb9`。
  本审者刚完成该稿全部数学的独立重推，见
  [完整三阶必要条件独审](2026-11-10-78718-audit-cubic-cap.md)。

本篇新审查是纸面推导，没有运行 ODE/BVP、参数零点搜索、曲面数组或网格。
前篇五个符号 PASS 不被充作本篇中心光滑性或全盘位置积分的证明。

## 2. 系数约定与第三阶线性系统

使用无阶乘 Taylor 系数，规范一、二阶分量为

$$
x_1=p\sin(nu),\quad \zeta_1=v\cos(nu),\qquad
x_2=y\sin(2nu),\quad \zeta_2=z_0+z\cos(2nu).
$$

前篇已逐项证明第三阶源只含 $T_n\cos(nu)+T_{3n}\cos(3nu)$。
对一个频率 N，写 $x_3=q\sin(Nu),\zeta_3=\xi\cos(Nu)$。
完整 Codazzi 线性部分确实是

$$
q_r=-N(P\xi+aT_N),\qquad \xi_r=NRq+ba_rT_N,
\tag{C1}
$$

其消元式

$$
\mathcal L_N\xi=(a^2a_rT_N)_r-N^2aT_N
\tag{C2}
$$

没有少掉原方程：由 $q=(\xi_r-ba_rT_N)/(NR)$ 微分，正好还原第一条。
三阶第二形式由 $c_3=(a/b)\zeta_3,m_3=x_3/a$ 及
$\ell_3=(a_{rr}/(ab^2))c_3+S^{(3)}$ 恢复，故同时满足三阶 Gauss 方程。
本篇选择规范二阶解，其余二阶共振自由度全部为零，是允许的存在性选择。

## 3. 源的准确中心阶数

球核心 $t=\tan(\rho/(2\sigma))$ 上，$b=2t/(1+t^2)$。
前篇准确公式给

$$
H_3=bT_n=
\frac{d^3}{32\sigma}t^{3n-5}(1+t^2)^3
\left(\frac{2-n}{n-1}-2t^2-\frac{n+2}{n+1}t^4\right)
+\frac{dd_2}{4\sigma}t^{3n-3}(1+t^2)^3,
$$

并有 $T_{3n}=0$ 于整个球核心。

除以 b 后，第一项通常从 $t^{3n-6}$ 开始。n≥3 时
$3n-6-n=2n-6$ 是非负偶数。n=2 时常数括号为零，使该项从 $t^2$ 开始；
这正是不可遗漏的最低阶抵消。第二项从 $t^{3n-4}$ 开始，而
$3n-4-n=2n-4$ 对 n≥2 也是非负偶数。所有其他因子为 $t^2$ 的解析函数。
所以在全部 n≥2 情形中，准确有

$$
T_n=t^nf(t^2),\qquad f\text{ 在中心附近解析}.
\tag{C3}
$$

这比仅有一个大 O 上界更强；下一节无对数和下一节后的张量抵消都需要它。

## 4. 中心正则 particular：两个 Euler 方程的完整求解

由 $a=2\sigma t/(1+t^2)$、$dr/dt=-2\sigma/(1+t^2)$，球核心有
$P=-\sigma/a,R=1/(\sigma a)$。将 N=n 的 (C1) 直接乘 $dr/dt$，得到

$$
q_t=-\frac{n\sigma}{t}\xi+\frac{4n\sigma^2t}{(1+t^2)^2}T,
\qquad
\xi_t=-\frac{n}{\sigma t}q+\frac{4\sigma t(1-t^2)}{(1+t^2)^3}T.
\tag{C4}
$$

因此对 $U=\xi+q/\sigma,V=\xi-q/\sigma$，相加、相减给

$$
U_t+\frac ntU=\frac{4\sigma t((n+1)+(n-1)t^2)}{(1+t^2)^3}T,
$$

$$
V_t-\frac ntV=-\frac{4\sigma t((n-1)+(n+1)t^2)}{(1+t^2)^3}T.
\tag{C5}
$$

这核清了原稿 (14)–(15) 的两个源符号。乘积分因子后取

$$
U=t^{-n}\int_0^t
\frac{4\sigma s^{n+1}((n+1)+(n-1)s^2)}{(1+s^2)^3}T(s)\,ds,
$$

$$
V=t^n\left[c-\int_0^t
\frac{4\sigma s^{1-n}((n-1)+(n+1)s^2)}{(1+s^2)^3}T(s)\,ds\right].
\tag{C6}
$$

使用 (C3)，两个 integrand 分别是 $s^{2n+1}$ 和 s 乘 $s^2$ 的解析函数。
其积分没有对数项，并且精确为

$$
U=t^{n+2}u(t^2),\qquad
V=t^n(c+t^2v_*(t^2)),\qquad u(0)=2\sigma f(0).
\tag{C7}
$$

最后一个系数由
$4\sigma(n+1)f(0)/(2n+2)=2\sigma f(0)$ 得到。
一般齐次解还可以在 U 中加 $c_-t^{-n}$；本构造已取 $c_-=0$。
V 中的 c 恰为中心正则齐次分支的一维自由度。
由 $\xi=(U+V)/2,q=\sigma(U-V)/2$ 恢复的解真实满足两条 (C4)。

## 5. 三阶二次型的 Cartesian 光滑性：独立换算

在球核心，$a_{rr}/(ab^2)=-1/a^2$、$c_3=\sigma\xi\cos(nu)$，
故二次型的 g 迹正是 $T\cos(nu)$。由 (C3)，这是
$\operatorname{Re}(w^n)f(|w|^2)$，在 $w=x+iy=te^{iu}$ 中解析。

令 $\lambda=2\sigma/(1+t^2)$，于是 a=λt、$dr=-\lambda dt$。
扣除迹部分后，dt² 的系数为

$$
A=\lambda^2\left(\frac T2-\frac{\sigma\xi}{a^2}\right)\cos(nu),
$$

交叉项为 $-2(q/t)\sin(nu)dt\,du$，du² 的系数为 $-t^2A$。
混合项负号来自 $dr=-\lambda dt$。

因为

$$
dw^2=e^{2iu}(dt^2-t^2du^2+2it\,dt\,du),
$$

若无迹部分为 $\operatorname{Re}(Qdw^2)$，必须有

$$
\operatorname{Re}(Qe^{2iu})=A,\qquad
\operatorname{Im}(Qe^{2iu})=\frac q{t^2}\sin(nu).
$$

将余弦、正弦拆成正负频率，并用 U、V 的定义，准确得到

$$
Q=\lambda^2\left(\frac T4-\frac{\sigma V}{2a^2}\right)e^{i(n-2)u}
+\lambda^2\left(\frac T4-\frac{\sigma U}{2a^2}\right)e^{-i(n+2)u}.
\tag{C8}
$$

这独立核对了原稿最关键的 (18)，包括两项的 1/4、1/2 和角频率。

第一项由 (C3)、(C7) 写成 $t^{n-2}A_+(t^2)e^{i(n-2)u}$，
故等于 $w^{n-2}A_+(|w|^2)$，n≥2 时无负幂。
第二项不能只据 U=O(t^{n+2}) 就断言光滑，因为除以 a² 后仍从 t^n 开始。
实际最低系数为

$$
\frac{\sigma U}{2a^2}
=t^n\frac{u(t^2)(1+t^2)^2}{8\sigma}
=\frac{f(0)}4t^n+O(t^{n+2}),
$$

恰与 T/4 的首项相消。因此第二项是
$t^{n+2}A_-(t^2)e^{-i(n+2)u}=\bar w^{n+2}A_-(|w|^2)$。
两函数 $A_\pm$ 都解析，迹项也解析，故完整真实二次型在中心解析。
这一步覆盖 n=2 的边界情形，并非把极坐标系数有界误认成 Cartesian 光滑。

## 6. 共振标量为零确实充分，不另藏边界条件

选 (C6) 的一个 c，例如零，在一个球核心截面取该实际解的初值。
穿过其余去中心区时 a、b 处处正，(C1) 是光滑线性常微分系统，故可唯一
延到入口，记 n 模 particular 为 $\xi^p$。它保持刚证明的中心光滑性。

将 (C2) 乘以归一正则齐次解 v，作 Green 恒等式及源项分部积分：

$$
\left[\frac{v(\xi^p)_r-\xi^pv_r}{R}\right]_0^T
=\left[va^2a_rT_n\right]_0^T-\mathfrak C_n.
\tag{C9}
$$

入口源在整个开柱为零，且 $v(0)=1,v_r(0)=0,R(0)=1$。
中心处 $v=O(\rho^n)$，(C6) 给 $\xi^p=O(\rho^n)$ 及径向导数
$O(\rho^{n-1})$；因此第一类端项为 $O(\rho^{2n})$。
第二类端项由 $T_n=O(\rho^n)$ 为 $O(\rho^{2n+2})$。
它们都趋零，且内部积分绝对可积，故 (C9) 准确给

$$
(\xi^p)_r(0)=\mathfrak C_n.
\tag{C10}
$$

符号为正：左边的完整边界差是 $0-(\xi^p)_r(0)$，右边是
$-\mathfrak C_n$。

假设 $\mathfrak C_n=0$ 后，入口导数已经为零。
再减去 $\xi^p(0)v$，同时令入口值和导数为零；正则性及源均不变。
这一步合法，因为共振恰给 $v_r(0)=0,v(0)=1$。
由开柱上的齐次系统，规范解的 $\xi_n,q_n$ 在整个开入口恒零。
正则齐次核只有一维，所以该双零入口规范唯一。
没有第二个未付的中心积分条件。

## 7. 非共振 3n 模及完整第三阶第二形式

$T_{3n}$ 在球核心恒零，先选该核心的零解，再向外延到入口，给一个
中心正则 particular。若 $v_{3n}$ 是中心 $t^{3n}$ 稳定分支，
$D_{3n}=(v_{3n})_r(0)\ne0$，所以准确减去
$((\xi^p_{3n})_r(0)/D_{3n})v_{3n}$，即可令入口导数为零。

其中心只多了正则齐次模，二次型在那里为
$\operatorname{Re}(-\sigma c_*w^{3n-2}dw^2)$，解析。
开柱的 q=0、ξ 常数，记该常数为 γ。与规范 n 模合并后，入口恰有
$\ell_3=m_3=0,c_3=\gamma\cos(3nu)$。

本存在性构造的第三阶源没有其他频率；其余三阶系数全部取零确实满足
对应齐次线性方程。故得到满足完整三阶 Gauss–Codazzi 的全盘光滑 $II_3$。

## 8. 柱边是真正闭曲线，包含全部高阶参数项

取

$$
\phi_\tau=u+\frac\tau n\sin(nu)
+\frac{\alpha\tau^2}{2n}\sin(2nu)
+\frac{\gamma\tau^3}{3n}\sin(3nu),\quad
T_\tau=i e^{i\phi_\tau},\quad
\Gamma_\tau=1+\int_0^uT_\tau(s)ds.
$$

$|T_\tau|=1$ 精确成立。对 $\omega=2\pi/n$，
$T_\tau(u+\omega)=e^{i\omega}T_\tau(u)$，故整圈积分为
$\sum_{j=0}^{n-1}e^{ij\omega}$ 乘首扇区积分，准确等于零。
曲率为 $\phi_\tau'$，即原稿 (24) 的完整三次多项式。

小参数时曲率处处正。并且
$\|T_\tau-T_0\|_\infty\to0$，用最短角弧有

$$
|\Gamma_\tau(u)-\Gamma_\tau(v)|
\ge(2/\pi-\|T_\tau-T_0\|_\infty)|\Delta u|>0
$$

于不同材料点，因而嵌入；结合正曲率得严格凸性。
曲线以某个可能平移的中心具有 n 折旋转对称，材料锚点则固定为
$\Gamma_\tau(0)=1$，不影响匹配。

其柱图的 g 精确为单位柱度量，$L=M=0,C=\kappa_\tau$。
故前三阶第二形式、位置锚点和框架锚点全部可与上述构造统一。
它没有只把曲率闭合而遗漏位置、速率或材料周长。

## 9. 全盘三阶标架和位置积分的完整闭性核对

圆盘的切丛平凡，基态光滑嵌入且定向，故可选全局光滑的正交标架 E0
和固定正交余标架 $\theta$；中心不使用奇异极坐标框架。
固定度量的切连接不变，法向连接对第二形式线性，构造
$\Omega_\tau=\Omega_0+\tau\Omega_1+\tau^2\Omega_2+\tau^3\Omega_3$。
每一项为反对称矩阵值一形式。

三阶 Gauss–Codazzi 给曲率系数至三阶均零。
置 $\Psi_j=E_0\Omega_jE_0^{-1}$，则

$$
d\Psi_1=0,\quad d\Psi_2=-\Psi_1\wedge\Psi_1,\quad
 d\Psi_3=-\Psi_1\wedge\Psi_2-\Psi_2\wedge\Psi_1.
\tag{C11}
$$

递归为

$$
dU_1=\Psi_1,\qquad
dU_2=U_1\Psi_1+\Psi_2,\qquad
dU_3=U_2\Psi_1+U_1\Psi_2+\Psi_3.
\tag{C12}
$$

第二式右端微分为 $\Psi_1\wedge\Psi_1+d\Psi_2=0$。
第三式右端微分逐项为

$$
(U_1\Psi_1+\Psi_2)\wedge\Psi_1+U_2d\Psi_1
+\Psi_1\wedge\Psi_2+U_1d\Psi_2+d\Psi_3=0,
$$

使用 (C11) 后全部准确抵消。这补出了原稿 (26) 的闭性，不把矩阵一形式
的次序交换。圆盘单连通，故各矩阵分量都有全局光滑原函数。

取 $U(\tau)=I+\tau U_1+\tau^2U_2+\tau^3U_3$、
$\Psi(\tau)=\sum_{j=1}^3\tau^j\Psi_j$。
(C12) 即 $dU=U\Psi+O(\tau^4)$。
因 $\Psi^T=-\Psi$，$Q=U^TU$ 满足
$dQ=-\Psi Q+Q\Psi+O(\tau^4)$。
锚点使用实际柱框架的 Taylor 系数，所以 Q 在锚点等于 I 到三阶。
逐阶归纳：Q 的第一、二、三阶系数的导数均为零，锚点值也零。
因此 $U^TU=I+O(\tau^4)$，即所需形式正交性。

对固定度量，$\Omega_j\wedge\theta=0$ 于所有 j≥1，是各阶第二形式
对称性的直接结果。于是
$\Psi_j\wedge dF_0=E_0(\Omega_j\wedge\theta)=0$。
因此

$$
d(U_jdF_0)=dU_j\wedge dF_0
=\sum_{k=1}^jU_{j-k}(\Psi_k\wedge dF_0)=0.
$$

全盘可积分 $dV_j=U_jdF_0$，并以真实柱边系数取位置常数。
现在

$$
dF^{[3]}_\tau=U(\tau)dF_0,
$$

其诱导度量一、二、三阶项由形式正交性准确消去，得到 $g+O(\tau^4)$。
各场在紧圆盘上光滑，故每个固定空间 $C^k$ 范数中的此估计都成立。

在入口开柱，实际曲线柱族有同一个固定度量和相同前三阶连接系数；
其框架、位置 Taylor 系数满足 (C12) 及同一锚点值。
沿开柱中任意参数路径的线性 ODE 唯一性给全部系数一致，覆盖全圈和整个开柱。
$II_1\ne0$，而无穷小环境刚体运动不改变材料第二形式，故 $V_1$ 非刚体。

## 10. 正式接受的范围

四个严格假设推出全盘三阶光滑形式等距及真实闭柱边的零至三阶匹配，
逻辑完整。其中 $\mathfrak C_n=0$ 对 n 共振的充分性尤其依赖本审查第 5 节
的真实中心解析性；它不是仅以一个形式 Fredholm 条件宣称可解。

仍然没有证明四个假设同时可由某个具体精确剖面满足。
浮点联合零不参与本定理证明；没有由此产生四阶及更高阶的兼容、形式级数
收敛或真正非线性解。固定非零参数的 $O(\tau^4)$ 度量缺陷不会随空间网格
加密自动减小，所以不支付本题 G5。固定开 H、有效可见幅度、闭面和最终
原始种子独立数值重跑也都不在此结论内。

本审查覆盖全文数学论证，没有参与任何主数值候选调参，最终独跑角色保持。
