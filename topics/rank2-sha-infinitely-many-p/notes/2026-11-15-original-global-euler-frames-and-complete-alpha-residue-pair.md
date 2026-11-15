# 原十九角 Euler 框与 α 转置的完整交概形配对

日期：2026-11-15。**状态：以下全局截面、原框及联合配对恒等式已证明；指定 ramification trace 是否属于该实际像仍未解决。**

本注接 R495、R524、R550、R822 以及
[对数主部接口](2026-11-15-mirror-trace-logarithmic-principal-part-and-thirteen-tail.md)。
它把真正 $\alpha_\eta^*$ 的法向部分统一放在原完整
$Z=(F,\mathcal EF)$ 上；这一步必须先支付十九角的 Euler lift。
所得有限对偶是 Gorenstein 留数配对，不是非约化代数上退化的普通乘法迹。

## 1. 原十九角上 E 确实保持全截面格

沿用
$$
\mathcal E=Y\partial_Y,\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad e=\mathcal EF.
$$
原曲面来自 $\mathbb F_4$，其负截面是 $Y=0$，
正截面是 $Y=\infty$。
R495 的中心只位于这些截面与固定底纤维的交点，
以及各链随后产生的固定交点：
三个四步负角、一个三步负角、两个两步正角，共十九次普通吹起。
并没有在任意非零有限 $Y$ 点另作一次不受该作用保持的吹起。

### 负角的完整局部算子

取 $z=t-a$、$x=Y^{-1}$，第 $j$ 图为 $z=x^jz_j$。
固定底变量的原 Euler lift 为
$$
\boxed{\mathcal E_j=-x\partial_x+jz_j\partial_{z_j}.}
\tag{1}
$$
它正则，且保持下一中心的理想 $(x,z_j)$。
设 $V_j$ 为 R495 的原累计重数，
$$
F_j=x^{-V_j}\,x^bF(a+x^jz_j,x^{-1}).
$$
这是原线束的真实正则局部系数。
由原函数 $F=x^{V_j-b}F_j$ 精确得到
$$
\boxed{
e_j=\mathcal E_jF_j+(b-V_j)F_j.
}
\tag{2}
$$
对任何原 $H\in\mathcal H_m$，同一框给
$$
\boxed{
(\mathcal EH)_j
=\mathcal E_jH_j+m(b-V_j)H_j.
}
\tag{3}
$$
这里的零阶项不因写了一个正则向量场而消失。

### 正角及底无穷远

有限正角取 $x=Y$，仍写 $z=x^jz_j$；
底无穷远按原 $T=1/t,\ Z=t^4Y$ 取 $z=T,x=Z$。
两处均有
$$
\boxed{\mathcal E_j=x\partial_x-jz_j\partial_{z_j}.}
\tag{4}
$$
有限正角 $F=x^{V_j}F_j$；
无穷远先取原方程 $T^uF(T^{-1},T^4Z)$，
其中 $T^u$ 的 Euler 权为零，再除 $x^{V_j}$。
故两处同样准确有
$$
\boxed{
e_j=\mathcal E_jF_j+V_jF_j,\qquad
(\mathcal EH)_j=\mathcal E_jH_j+mV_jH_j.
}
\tag{5}
$$

(1)–(5) 保每一个实际累计帽。
在别的吹起图上是同一正则 lift 的坐标表示；
远离中心没有改变原局部理想。
也可直接在原 Gauss 基上核验：
$\mathcal E$ 只把 $Y^n$ 的系数乘 $n$，
不会降低任何一条原系数整除或次数帽。

因此这里得到真正全局结论
$$
\boxed{
\mathcal E\mathcal H_m\subseteq\mathcal H_m,\qquad
e\in\mathcal H_1,\quad
\mathcal EH\in\mathcal H_2\ (H\in\mathcal H_2).
}
\tag{6}
$$
这只说同一线束的完整原来源被保持；
它不说原物理 $M$ 的核或像被 $\mathcal E$ 保持。

## 2. 全部十九角的真实 canonical 框

取原有理二形式
$$
\Omega_{\log}=\frac{dt\wedge dY}{Y}.
$$
记 $H_-,H_+$ 为两个截面的严格变换，
$f_\infty$ 为底无穷远纤维的严格变换，
$E_{i,j}$ 为相应第 $j$ 个例外曲线的严格变换。
有限链包括 $0$、两个 $h_7$ 根、$1$ 和 $d=0$；
无穷远链单列。

其全除子准确为
$$
\boxed{
\operatorname{div}_X\Omega_{\log}
=-H_- -H_+ -2f_\infty
+\sum_{\text{有限链 }i}\sum_j(j-1)E_{i,j}
-\sum_{j=1}^{2}(j+1)E_{\infty,j}.
}
\tag{7}
$$
这是 $K_X$ 的一个明确代表。

证明只用同一吹起坐标。
有限链上
$dz\wedge dx/x=x^{j-1}dz_j\wedge dx$，给 $j-1$。
底无穷远
$$
\Omega_{\log}=-T^{-2}\,dT\wedge dZ/Z,
$$
代 $T=x^jz_j$ 后为
$-x^{-j-1}z_j^{-2}dz_j\wedge dx$，给 $-(j+1)$。
两个水平框各有简单极，底无穷远严格纤维有二阶极。
这些项已列尽；在原域上不分裂的 $h_7$ 点按闭点下降读取。

对真正
$$
\omega\in H^0(C,\omega_C\otimes N^{-1}(qP))
=H^0(C,K_X|_C(qP)),
$$
可用唯一的 $B\in k(C)$ 写
$$
\boxed{\omega_F=B\,dt/e}
\tag{8}
$$
作为原有限 $F$ 框中的微分系数。
这就是将 $B\Omega_{\log}|_C$ 经原伴随同构读取。

式 (7) 给 $B$ 的真实全局零极条件，而非裸 $B\,dt/e$ 的表观极条件。
例如正水平要求相应局部 canonical 框正则，
正是前注中必须保的 $N^{-1}$ 框变换。
在光滑点，各相交边界项的局部阶相加后要求非负，
在 $P$ 则只允许所给 $q$ 阶极。

若 $C$ 奇异，不能仅用正规化上各阶非负替代下降。
具体地，取 $K_X$ 的局部单位框 $\Omega_U$，
写 $\Omega_{\log}=g_U\Omega_U$，
则应要求 $g_U B$ 属于原 $\widehat{\mathcal O}_{C,Q}$。
在正规化上正则后，还须其模 conductor 的类落在
$\mathcal O_C/\mathfrak f\subset\widetilde{\mathcal O}_C/\mathfrak f$ 中。
这给有限而准确的奇点相容条件；本注没有把所有正规化截面免费加入。

## 3. 原交概形上的真实一阶算子

令
$$
Z=V(F,e)\subset X.
$$
按 R550，$Z$ 在 $C$ 上是 $e|_C$ 的 Cartier 零除子，
$\mathcal O_C(Z)=N$、$\operatorname{length}Z=\kappa$，并且 $P\notin Z$。
所有固定角、水平交点、重数和非约化结构均在这个同一个 $Z$ 内。

原限制 $\mathcal H_2\to H^0(C,N^2)$ 满射。
对 $B_0\in H^0(C,N^2)$，取任一真实提升 $H\in\mathcal H_2$，定义
$$
\boxed{
D_{\mathcal E}(B_0)=(\mathcal EH)|_Z
\in H^0(Z,N^2|_Z).
}
\tag{9}
$$
这是良定义的：
改变提升 $H\mapsto H+FL$，$L\in\mathcal H_1$，则
$$
\mathcal E(H+FL)-\mathcal EH=eL+F\mathcal EL
$$
在 $Z$ 上为零。

该算子读取 $B_0$ 的真正一阶 jet，包含 (2)、(5) 的线束零阶项。
它一般不由 $B_0|_Z$ 的值决定；
$\mathcal E$ 不必保持 $Z$ 的理想。
不过它因子化于 $B_0|_{2Z}$：
对局部被 $e^2$ 整除的截面，导数模 $e$ 为零。
因此不能把 (9) 的值和 $B_0|_Z$ 分别当作两个可自由选择的来源向量。

## 4. 完整 Z 的完美配对与全部 conductor

$Z$ 为原零维 Gorenstein 交概形，准确有
$$
\omega_Z=(\omega_C\otimes N)|_Z.
$$
所以
$$
(\omega_C\otimes N^{-1})|_Z
=\omega_Z\otimes(N^2|_Z)^{-1}.
$$
由此得到真完美配对
$$
\boxed{
\langle\ ,\ \rangle_Z:
H^0(Z,N^2|_Z)\times
H^0(Z,(\omega_C N^{-1})|_Z)\longrightarrow k.
}
\tag{10}
$$
其规范是完整 Gorenstein 留数迹：
若 $B_1$、$\omega$ 是相应局部提升，
$$
\langle B_1|_Z,\omega|_Z\rangle_Z
=\sum_{Q\in Z}\operatorname{Tr}_{k(Q)/k}
\operatorname{Res}_Q(B_1\omega/e).
\tag{11}
$$
奇点处 $\operatorname{Res}_Q$ 指所有正规化分支的和，
并保各支至 $k(Q)$ 的迹。
这也可用同一个完全交的 Grothendieck 系数留数定义。

(10) 不是局部 Artin 代数上普通乘法算子的迹。
后者在非约化代数上通常退化；
R822 的普通有限迹是乘以所需 Jacobian 后才进入这样的完美配对。

## 5. α 转置的实际全局联合式

保原强窗 $T\le2h$、$q=T-h>\kappa$、$h>\kappa$，
以及同一个实际 $\eta=\log(g/\psi)$。
R524 的连接源为
$$
\mathcal B_h=H^0(C,N^2(-hP)),
$$
其对偶空间为
$$
\mathcal D_q=H^0(C,\omega_C N^{-1}(qP)).
$$
对 $B_0\in\mathcal B_h$ 和其原提升 $H\in\mathcal H_2$，
原 Serre 转置准确为
$$
\alpha_\eta^*\omega(B_0)
=
\operatorname{Res}_P
\left[
\left(\frac{B_0}{2\eta}+(\mathcal EH)|_C\right)
\frac{\omega}{e}
\right].
\tag{12}
$$
这是与 R524(15) 一致的正号规范。

由已付 (6)，微分
$$
\frac{(\mathcal EH)|_C}{e}\,\omega
$$
是原 $C$ 上的亚纯对偶化截面，其可能的非正则支撑仅在 $Z\cup\{P\}$。
在正规化上，别的奇点仍可出现 conductor 极；
但在原 $\omega_C$ 中正则，Rosenlicht 条件使这些点的全部分支残数和为零。
没有逐支删掉 conductor 极。

对这个同一个微分使用全局留数定理及 (9)–(11)，得到
$$
\boxed{
\alpha_\eta^*\omega(B_0)
=
\operatorname{Res}_P\frac{B_0\omega}{2\eta e}
-
\left\langle
D_{\mathcal E}(B_0),\ \omega|_Z
\right\rangle_Z.
}
\tag{13}
$$
这支付了全十九边界的联合性。
那些边界若不属于完整 $Z$，其表观极必须在真实框中抵消；
若属于 $Z$，则已在 (10)–(13) 的同一个配对内，不能另外删去。
尤其正水平的 $2b$ 项是 (9) 的组成部分，并未在 (13) 中消失。

于是对每个真正 $B_0\in\ker\alpha_\eta$，有实际约束
$$
\boxed{
\left\langle D_{\mathcal E}(B_0),\omega|_Z\right\rangle_Z
=
\operatorname{Res}_P\frac{B_0\omega}{2\eta e}
\qquad(\omega\in\mathcal D_q).
}
\tag{14}
$$
两边由同一个全局 $\omega$ 产生；
不能分别选择一个有限 $Z$ 对偶向量和一个原点主部。

## 6. 指定 trace 尚须经过哪个真实像

R822 在非固定有限 $Z^\circ$ 上给原零阶行
$$
\mathcal T(B_0)=
\sum_{Q\in Z^\circ}
\operatorname{Tr}_{\mathcal O_{Z_Q}/k}
(W_sF_tq_{\rm src}t^r B_0).
$$
它只读取同一个 $B_0$ 的值，不等于 (9) 的切向一阶算子。
经 (10) 可将该有限零阶行写成一个确定的 $Z$ 对偶向量，
但这不使它自动成为某个允许全局 $\omega$ 的限制。

精确待判条件是：是否存在一个满足 (7) 的原框条件、
所有 conductor 下降条件及同一 $qP$ 帽的
$\omega\in\mathcal D_q$，使
$$
\mathcal T(B_0)
=
\operatorname{Res}_P\frac{B_0\omega}{2\eta e}
-
\langle D_{\mathcal E}(B_0),\omega|_Z\rangle_Z
\quad\text{对全部 }B_0\in\mathcal B_h.
\tag{15}
$$
(15) 的确等价于指定行属于 $\operatorname{im}\alpha_\eta^*$；
本注没有证明它成立或不成立。
新支付的是原十九角上的全局截面及有限完全交转置，
而不是凭一个局部对数主部宣布 (15)。

相对 $J$ 用 $T=s-r$，原较短 $M$ 用 $T=s-r-13$；
仅在 R808 已付 primitive 第三精度时可使用相应的长窗口。
前注 $r\le11$ 的十三尾、低行右逆高尾、
原 $P_{134}/U_0$、同一个 $R$ 和全部其余 normal/carry 都仍保留。
本注不增加中央零，不扩原来源，也未宣称主目标完成。

依赖：
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R524](../results/R524-original-three-layer-boundary-kernel-and-first-escape-window.md)；
[R550](../results/R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[正水平全 jet](2026-11-15-mirror-trace-positive-horizontal-jets-and-t1-fiber.md)。
