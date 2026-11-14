# R49：正角向曲率的实际固定 H 环带及有限平坦延拓

**已证明；完整未参与者独立审查通过。** 这是仍有两条边界的精确等距族，未达到本题闭曲面、可见幅度和目标 reach 的全部完成标准。

作者 independent-geometry-continued-2；root 提供四约束/材料固定区路线中的部分论证、全 E(3) 路线及 J 多项式比较建议，不担任这些部分的独立审查人。独立审查为 tail-review-continued-2。root 于 2026-11-09 全文读取作者稿及完整独审后登记。

固定作者稿 commit `ec5093a6d7c368dfaf80855d03c5c0f19ac51afe`，blob `34ba5cd303512e203a22501db57b11dd4e844470`，见 [完整作者稿](../notes/2026-11-09-db6f-positive-epicycle-bump-fixed-h-v1.md)。完整独审 commit `ab158761cb5fc844d8e2da18abdca4313aed79e6`，blob `de89ad838b6adcc0462952ca8950873c24c3bb56`，见 [完整独立审查](../notes/2026-11-09-db6f-tail-review-positive-epicycle-bump-fixed-h-v1.md)。独立有理门实际重放 13 PASS 的固定回执为 `fae71b065bdfa178271169e9f6c9fe6e5c019893`，见 [独立小回执](../notes/2026-11-09-db6f-tail-review-positive-epicycle-fixed-h-rational-replay.md)。这是 JavaScript 隔离运行时，不是终端；0 PDE、隐函数数值求值或主求解器运行。

四个首扇区积分约束及可逆 Gram 给实际光滑局部族。固定 c(0) 与共同材料弧长使同一有内部的闭集 H 逐点固定；对含新增平坦领的整个初态，diam(H)/D>9/13。整个共同材料域全时间嵌入，有本构造自己的正 reach 下界；每个充分小非零时间的完整像与初态在含反射的 E(3) 下不全等。

作者稿 §9 当时以待审单调 Q 定理为条件；该定理现已作为 [R48](R48-monotone-flat-collar-smooth-data.md) 全文独审通过，本次独审又逐项核过实际初值的正性、共同 Sobolev 界、周期位置、开重叠、弦长、曲率识别等全部组合假设。因此有限平坦领部分也已接受。旧冻结稿的待审措辞保留为历史，不代表本登记仍有该项逻辑缺口。

仍缺实际闭合、有效时间半径和 .05D 像变化、全图 .03D reach。新正 C 种子不继承 R45 的 b/5。平坦出口仍是小锥角、非零秩一第二形式，尚未接到 R43 或固定帽。

下文保留冻结作者稿全部十一节及检查源码。

---

# 正 C epicycle 的实际局部 bump 族：固定握持区与有限平坦领

**状态：完整作者推导，待全文独立审查。** 2026-11-09，独立几何分工。
本稿不修改任何冻结的旧稿；不读取主优化数组，不运行 BVP、tail、RK 或几何网格。
§§2–8 给一个实际的光滑、闭合、正宽有边环带族，其共同度量、固定材料 H、
全时间嵌入及全 E(3) 非全等均在本文核清。
§9 的新领延拓明确引用尚待独审的单调 Q 光滑数据定理；该定理未采纳前，
本文的有限平坦领部分是依赖该固定定理的条件结论，不能预记为已证明结果。

这里的“闭合”只指角向位置与标架周期。材料曲面始终有两条边界，不是闭曲面。
没有有效非零参数半径、0.05D 像位移或 0.03D reach 结论。
本文的固定 H 是新正 C 种子的实际材料集合，不是把旧 R44/R45 的数值移过来。

## 1. 固定来源与分工

1. 正 C epicycle 作者稿：
   [固定 0239fffd6e5206dfadb778db4ba5a057e01cfc5a](https://github.com/Rogerhu12/math-research/blob/0239fffd6e5206dfadb778db4ba5a057e01cfc5a/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-finite-flat-collar-v1.md)，
   blob 24c70487248a1766119cb06d1299d9686901205c，27,156 B。
   本文只引用其显式基础曲线恒等式和基础有理界；它的原角解析扰动没有固定开 H。
2. 上项的未参与者完整独审：
   [固定 e927f688421290880733e8de0ddc2d017ef8c574](https://github.com/Rogerhu12/math-research/blob/e927f688421290880733e8de0ddc2d017ef8c574/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-positive-epicycle-finite-flat-collar-v1.md)；
   独立常数检查脚本另冻 d47fd0029bf17cba10e3c50bfe41497914bdedb7。
   这不是本文新族的独立审查或程序重跑。
3. 根作者的光滑角数据延拓：
   [固定 9daa8aba8a341855811d2f1c164bfb3ca7eab0bc](https://github.com/Rogerhu12/math-research/blob/9daa8aba8a341855811d2f1c164bfb3ca7eab0bc/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-monotone-flat-collar-smooth-data-v1.md)，
   blob bfd25b66bc985f22eb350b8c99d045bf3b1388a0，17,171 B。
   该稿用 Q>=0、Q'<=0 的混合能量给实际光滑解；本文不把它用于从 Q=0 向正 Q 起步。
4. 四个扇区约束与固定弧材料 gauge 的模式来自已独审的 R44 恢复正文
   [固定 456c246b252e102e5a3d29c45b9d4dde7146dcea](https://github.com/Rogerhu12/math-research/blob/456c246b252e102e5a3d29c45b9d4dde7146dcea/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-geometry-explicit-ruled-saddle-annulus-recovered-v2.md)。
   **全 E(3) 的“内在等距分类 + 固定开片 + 仅基础图解析”的证明途径由 root 提出。**
   本文把该途径应用于新的正 C 种子；参与该途径的 root 审阅不计作这部分的独立来源。
   §3 的 J 多项式平方检验也由 root 建议，下面给出完整计算。

以下所有新参数、材料区与度量均另行固定，不属于旧 flat17 的加密序列。

## 2. 显式正 C 基础曲线

令 b>0 为固定尺度，omega=2pi/3，并记

$$
\eta=1/\sqrt2,\qquad
p^2=\frac{2(1-\eta^2)}{1+6\eta-3\eta^2},\qquad q=\sqrt{1-p^2},\quad p>0.
\tag{1}
$$

为免与场方程 Q 混淆，本文的小写 q 始终只是 (1) 的正常数。
取

$$
\bar d(\theta)=R_z(\theta)R_y(\pi/4)
                (p\cos3\theta,-p\sin3\theta,q),\qquad d_0=-\bar d.
\tag{2}
$$

这里 R_z、R_y 是通常的右手正交旋转。用复数记水平分量 W=x+iy，

$$
\bar d_W=\eta q e^{i\theta}
+\frac{p(\eta-1)}2e^{4i\theta}
+\frac{p(\eta+1)}2e^{-2i\theta},\qquad
(d_0)_z=\eta(p\cos3\theta-q).
\tag{3}
$$

令

$$
J=(\eta-3)q-\eta p\cos3\theta,\qquad
W_*=10-6\eta,\qquad A_*=19-9\eta.
\tag{4}
$$

注意 W_* 是实常数，和复水平分量下标 W 无关。精确恒等式为

$$
k_0^2:=|d_0'|^2=W_*-J^2,\qquad
(d_0)_z=-J-3q,
$$

$$
\kappa_0=
\frac{J^3-A_*J-3W_*q}{(W_*-J^2)^{3/2}}>1/15.
\tag{5}
$$

这里 \kappa_0 是以球面弧长定向的测地曲率；
若 T_0=d_0'/k_0、n_0=d_0\times T_0，则
(T_0)_u=-d_0+\kappa_0 n_0，(n_0)_u=-\kappa_0T_0。
冻结来源 1–2 已完整证明

$$
3/10<k_0^2<6,\qquad |d_0''|\le16,
\qquad \int_0^{2\pi}d_0\times d_0'\,d\theta=0.
\tag{6}
$$

下面把该周期原函数的积分常数写死。设

$$
\begin{aligned}
R&=\tfrac12+(3\eta-\tfrac34)p^2,&
P&=\tfrac12pq(\tfrac32+\eta),&
A&=\tfrac14pq(1-\eta)^2,\\
B&=\eta p^2(1-\eta)/28,&
C&=\eta p^2(1+\eta)/20,&
U&=\eta pq(3-2\eta)/3,\quad V=p^2/24 .
\end{aligned}
\tag{7}
$$

定义

$$
(c_0)_W=i b\{R e^{i\theta}+A e^{4i\theta}
                  +P e^{-2i\theta}+B e^{7i\theta}+C e^{-5i\theta}\},
\qquad
(c_0)_z=-b(U\sin3\theta+V\sin6\theta).
\tag{8}
$$

则 c_0'=b d_0\times d_0'，c_0(theta+omega)=R_z(omega)c_0(theta)。
已审基础界是

$$
.86<R<.88,\quad .48<P<.50,\quad
0<A<.01,\quad0<B<.003,\quad0<C<.017,
\quad 0<U<.17,\quad0<V<.012,
\tag{9}
$$

以及对最短角差 Delta_theta，

$$
|c_0(\theta)-c_0(\phi)|\ge (b/32)\Delta_\theta,\qquad |c_0''|\le16b .
\tag{10}
$$

(9) 的 U<.17 也直接由
eta<.708、p<.518、q<.857、eta>.707 给出，见文末有理核查。
特别是 c_0 真正单射，非只因三次对称而猜测闭合。

## 3. 四函数 Gram 严格正定

令

$$
g(\theta)=((d_0)_x,(d_0)_y,(d_0)_z,\kappa_0)^T .
\tag{11}
$$

**断言：四个实解析函数在任一非空开弧上线性无关。**
先设某个线性关系在一开弧成立。实解析延拓使它在整圆成立。
对 theta、theta+omega、theta+2omega 三式求和，水平分量消去，
于是得到 a_z(d_0)_z+c\kappa_0=0。

若 c不为0，就有 \kappa_0=lambda(d_0)_z，lambda为实常数。
由 (5)，在 J 取到的一个非退化实区间上

$$
(J^3-A_*J-3W_*q)^2
=\lambda^2(J+3q)^2(W_*-J^2)^3.
\tag{12}
$$

因此它是多项式恒等式。左边恰为六次、首项系数1；lambda不为0时
右边恰为八次、首项系数-lambda^2，矛盾。
lambda=0 又与 \kappa_0>0 矛盾。因此 c=0，
并由 (d_0)_z<0 得 a_z=0。

剩余关系 a_x(d_0)_x+a_y(d_0)_y=0。
(3) 的实 Fourier 展开中，水平复数 e^{i theta} 系数为 -eta q不为0，
而 d_{0,W} 没有 e^{-i theta} 项。
取上述实关系的频率 +1 系数便得 a_x-i a_y=0。
所以 a_x=a_y=0，断言得证。

现在取任何在一个开子弧严格正的光滑非负 chi。
由 k_0>0 和上述独立性，

$$
G=\int_0^\omega \chi(\theta)k_0(\theta)
                 g(\theta)g(\theta)^T\,d\theta
\tag{13}
$$

严格正定：若 z^T G z=0，非负连续被积函数迫使 z·g
在 chi>0 的开弧恒零，继而 z=0。
这里没有把正定性寄托于采样或浮点行列式。

## 4. 真正满足全部约束的局部 bump 族

在第一扇区 (0,omega) 取两个不相交区间

$$
I_f=(\omega/8,\omega/4),\qquad
I_c=(3\omega/8,5\omega/8).
\tag{14}
$$

对开区间 (a,c) 定义标准归一光滑 bump

$$
\mathcal B_{a,c}(\theta)=
\begin{cases}
\exp\{4/(c-a)^2-1/[(\theta-a)(c-\theta)]\},&a<\theta<c,\\
0,&\text{其余}.
\end{cases}
\tag{15}
$$

它的最大值为1，全部边界 jet 为0。
令 h=B_{I_f}，chi=B_{I_c}，先在第一扇区定义
f_j=chi g_j，j=1,...,4，再把 h、每个 f_j 分别作为**标量**
以 omega 为周期复制。因为支集远离扇区边界，复制后的函数全为 C-infinity。
这里不是把 d_x、d_y 本身误当成 omega 周期函数。

令

$$
f_{\tau,\alpha}=\tau h+\sum_{j=1}^4\alpha_j f_j,\qquad
d_{\tau,\alpha}=\cos f_{\tau,\alpha}\,d_0+
                 \sin f_{\tau,\alpha}\,n_0 .
\tag{16}
$$

这是精确单位向量场，且
d_{\tau,\alpha}(theta+omega)=R_z(omega)d_{\tau,\alpha}(theta)。
设

$$
\mathcal A_0=\int_0^\omega d_0\times d_0'\,d\theta,\qquad
\ell=\int_0^{2\pi}k_0\,d\theta .
$$

要求以下四个实约束：

$$
\int_0^\omega d_{\tau,\alpha}\times d_{\tau,\alpha}'\,d\theta
=\mathcal A_0,\qquad
\int_0^\omega|d_{\tau,\alpha}'|\,d\theta=\ell/3 .
\tag{17}
$$

对首扇区的任意支集内部变分 delta d=f n_0，
分部积分没有边界项，得到

$$
\delta\!\int_0^\omega d\times d'\,d\theta
=-2\int_0^\omega f k_0 d_0\,d\theta,\qquad
\delta\!\int_0^\omega|d'|\,d\theta
=-\int_0^\omega f k_0\kappa_0\,d\theta .
\tag{18}
$$

因此 (17) 对 alpha 的 Jacobian 恰为
-diag(2,2,2,1)G，由 (13) 可逆。
有限维光滑隐函数定理给真实的 alpha(tau)，alpha(0)=0，
使 (17) 对全部 |tau|<tau_* 精确成立。
这是一个由显式有限积分和唯一局部隐函数定义的族，不是只求一阶核。

记 d_tau=d_{tau,alpha(tau)}、k_tau=|d_tau'|。
缩小同一个正参数半径，使对所有时间

$$
k_\tau\ge1/2,\qquad |d_\tau'|\le4,\qquad
|d_\tau''|\le17,\qquad
1/30<\kappa_\tau\le68.
\tag{19}
$$

前面三个界由 C2 连续性及 (6) 得到；
曲率下界也由连续性，曲率上界则由
|kappa_tau|<=|d_tau''|/k_tau^2<=68。
以一个固定的充分小正数 tau_1<=tau_* 取 tau=t tau_1，t在[0,1]，
便得到整个闭时间区间上的共同族。本文没有计算 tau_1 的有效数值下界。

## 5. 积分锚点、位置闭合与共同材料坐标

定义真正的中心线

$$
c_\tau(\theta)=c_0(0)+b\int_0^\theta
                                  d_\tau(x)\times d_\tau'(x)\,dx .
\tag{20}
$$

**积分常数始终是同一个 c_0(0)。**
这与旧角解析族按时间重置零平均的规则不同。

由首扇区向量约束，

$$
c_\tau(\omega)-c_\tau(0)
=b\mathcal A_0
=(R_z(\omega)-I)c_0(0).
$$

被积函数的 C3 等变性因此给全局恒等式

$$
c_\tau(\theta+\omega)=R_z(\omega)c_\tau(\theta).
\tag{21}
$$

三次迭代即给真实位置周期。等价地，完整向量面积是
(I+R_z(omega)+R_z(2omega))A_0=0。
这不仅消去竖直平均，还固定了用于锚点对称的首扇区水平位移。

令

$$
u_\tau(\theta)=\int_0^\theta k_\tau(x)\,dx,\qquad
u\in\mathbb T_\ell,\qquad \theta=\theta_\tau(u).
\tag{22}
$$

(17) 与 C3 给每个扇区长度精确相同，故
u_tau(theta+omega)=u_tau(theta)+ell/3。
全部时间使用同一个材料圆周 T_ell，不随时间改变周期。
严格正速度保证逆函数及其时间依赖联合 C-infinity。

在每个 j omega 的两侧至少 omega/32 的开邻域内，所有 bump 恒零。
由 (20)、完整首扇区面积约束及邻域内相同的被积函数，有

$$
d_\tau(\theta)=d_0(\theta),\quad c_\tau(\theta)=c_0(\theta),
\quad u_\tau(\theta)=u_0(\theta)
\quad\text{当 }|\theta-j\omega|\le\omega/32 .
\tag{23}
$$

对左侧邻域，先用完整扇区积分相同，再倒积分最后一段，得到同一结论。
所以 (23) 是固定材料坐标的等式，不能以“角向支集不变”代替这一步。

定义

$$
B_\tau(v,u)=c_\tau(\theta_\tau(u))
                          +v\,d_\tau(\theta_\tau(u)),\qquad
-w\le v\le w,\qquad w=b/10^6.
\tag{24}
$$

以球面弧长导数记 T=d_u、n=d×T，则 c_u=bn，故

$$
g=dv^2+(b^2+v^2)du^2 .
\tag{25}
$$

选 N=(v n-bT)/sqrt(b^2+v^2)，第二基本形式为

$$
L=0,\qquad M=-b/\sqrt{b^2+v^2},\qquad
C_{\!II}=\sqrt{b^2+v^2}\,\kappa_\tau(u)>0,\qquad
K=-b^2/(b^2+v^2)^2.
\tag{26}
$$

这给整个新族的精确共同第一基本形式。
所有符号 C_{II} 都表示二次型分量，不与 (7) 的小常数 C 混淆。

## 6. 全时间嵌入、空间弦长与有边 reach

再缩小同一个参数区间，使

$$
\|c_\tau'-c_0'\|_\infty\le b/64,\qquad
\|c_\tau''-c_0''\|_\infty\le b .
\tag{27}
$$

沿最短角弧积分第一式，并用 (10)，得到

$$
|c_\tau(\theta)-c_\tau(\phi)|
\ge (b/64)\Delta_\theta,\qquad |c_\tau''|\le17b .
\tag{28}
$$

因此中心线是光滑嵌入闭曲线。对任一单位法向 nu，
最短参数弧 Taylor 式给

$$
2|\nu\cdot(c_\tau(\phi)-c_\tau(\theta))|
\le 17b\,\Delta_\theta^2
\le \frac{69632}{b}|c_\tau(\phi)-c_\tau(\theta)|^2 .
\tag{29}
$$

紧曲线最近点的法向极小条件和距离平方比较遂给

$$
\operatorname{reach}(c_\tau)\ge \rho:=b/69632.
\tag{30}
$$

因为 c_tau' 与 d_tau 正交，(24) 是其正常管的一条子带。
2w<rho，故在更宽的 |v|<=2w 上也全部嵌入。
确切地，(29) 给任何正常位移 x=p+v d 与另一中心点 q 的距离平方差
至少 (1-|v|/rho)|p-q|^2；所以 p 确为 x 的唯一中心线足点，
不同中心足点的两条纤维不能相交。

还需要实际空间弦长下界。对带上两点 x=p+v d_theta、
y=q+vhat d_phi，(29) 和 |v|,|vhat|<=2w 给

$$
(x-y)\cdot(p-q)\ge(1-2w/\rho)|p-q|^2,
\quad\text{从而}\quad |p-q|\le(5/4)|x-y|.
\tag{31}
$$

结合 (28) 得 b Delta_theta<=80|x-y|。
又由 |d_theta-d_phi|<=4Delta_theta，

$$
|v-\widehat v|
\le |x-y|+|p-q|+2w|d_\theta-d_\phi|
<3|x-y|.
$$

最短材料角差满足 Delta_u<=4Delta_theta，因而

$$
\sqrt{(v-\widehat v)^2+b^2\Delta_u^2}<321|x-y|.
\tag{32}
$$

这是全局空间弦长，不是只在切空间比较长度。

还可给一个不追求最优的带边界 reach。使用欧氏参数 (v,z)=(v,b u)，
有 B_vv=0、|B_vz|=1/b，以及由 (19)

$$
|B_{zz}|
\le b^{-1}\{68+2\cdot10^{-6}(1+68)\}<69/b.
$$

因此 Hessian 双线性算子范数可以统一取 H_0=71/b。
设空间点 y 的一个最近点是 B(p)，取通向任一另一参数 q
的可行最短角 lift 直线段。即使 p 位于 v=±w 的边界，
单侧极小条件仍给

$$
(y-B(p))\cdot DB(p)(q-p)\le0 .
$$

Taylor 余项和 (32) 于是给

$$
(y-B(p))\cdot(B(q)-B(p))
\le |y-B(p)|\,\frac{71}{2b}\,321^2\,|B(q)-B(p)|^2 .
$$

当 |y-B(p)|<b/(71·321^2) 时，展开到 B(q) 的距离平方，
其值严格大于到 B(p) 的值，除非两像点相同。因此

$$
\operatorname{reach}(B_\tau([-w,w]\times\mathbb T_\ell))
\ge \frac{b}{71\cdot321^2}>0.
\tag{33}
$$

这里使用整个有边盘带的最近点条件，包含边界的法锥方向；
没有把无边曲面的 reach 公式直接套到边界上。
co-Lipschitz 常数必须平方，(33) 已保留这一因子。
该小下界绝非 R45 的 b/5，也不达成本题 3% 指标。

## 7. 固定材料 H 及其真实尺寸

令 H 是以下材料闭集：

$$
H=\bigcup_{j=0}^2
\left\{(v,u_0(\theta)):
|v|\le w/2,\quad|\theta-j\omega|\le\omega/32\right\},
\tag{34}
$$

角区间按周期解释。它有非空内部。
由 (23)，B_tau|H=B_0|H，逐点固定且不靠后续刚体对齐。

在 v=0、theta=0 与 theta=omega 处，由 (8)，

$$
|c_0(\omega)-c_0(0)|
=\sqrt3\,b(R+P+A+B+C)
>\sqrt3\,b(67/50)>9b/4.
\tag{35}
$$

另一方面，(8)–(9) 给

$$
|c_0(\theta)|
\le |(c_0)_W|+|(c_0)_z|
< b(1.41+.17+.012)<8b/5.
\tag{36}
$$

旧环带初态全像因而包含在半径 8b/5+w 的球内。
后文若加上长度 delta<=w 的新领，F_r 是单位向量，
其初态任一点到 c_0(u) 的距离仍至多 2w。
两种情形均有

$$
D:=\operatorname{diam}F_0<13b/4,\qquad
\frac{\operatorname{diam}F_0(H)}{D}>9/13>1/5.
\tag{37}
$$

(37) 的分母是实际完整有边环带（含后来小领）的初态直径，
不是中心曲线直径，也不是环宽。没有用材料点位移冒充像 Hausdorff 位移。

## 8. 含反射的全 E(3) 非全等

本节使用 §1 明确归属 root 的证明途径。

先在任意对称中央子带 |v|<a<w 上分类 (25) 的全部内在自等距。
K 严格确定 |v|，所以其第一坐标必为 epsilon v；
在 v=0 两侧的符号必须由光滑可逆性一致连接，epsilon=±1。
若第二坐标为 h(v,u)，比较 dv^2 系数得 h_v=0，
再比较 du^2 得 h_u^2=1。连通性最终给

$$
(v,u)\longmapsto(\epsilon v,\zeta u+\beta),
\qquad \epsilon,\zeta\in\{1,-1\},\quad\beta\in\mathbb T_\ell.
\tag{38}
$$

这里已经包括所有可能的材料翻向。

假设某个欧氏等距 A 把 B_tau 的这个中央子带像映到 B_0 的像。
嵌入性使诱导材料映射是 (38) 中某个 psi，因此
A B_tau=B_0 psi。在 H 的一个内部矩形上 B_tau=B_0，遂有

$$
A B_0=B_0\psi .
\tag{39}
$$

基础图 B_0 在整个连通中央带实解析：
(2)、(8) 解析，k_0>0，其弧长逆函数解析；psi 也是解析。
故 (39) 的解析恒等定理把等式延至整个中央带。
这只要求**基础图**解析；新 bump 图无需解析。
由 A B_tau=B_0 psi=A B_0 得 B_tau=B_0。

最后说明这种逐点相等对所有充分小的非零 tau 不可能。
记 D_tau(u)=d_tau(theta_tau(u))。
取自由支集内的中点 theta_*，有 h(theta_*)=1，而全部控制 f_j
在该点邻域恒零。令 u_*=u_0(theta_*)。
球面法向分量不受一阶弧长重参数化的切向项影响，所以

$$
\left.\frac d{d\tau}
d_\tau(\theta_\tau(u_*))\cdot n_0(\theta_*)\right|_{\tau=0}=1.
\tag{40}
$$

(40) 的标量在 tau=0 为0，因而在一个更小的正参数区间内
对每个非零 tau 都不为0。于是 D_tau不等于D_0，继而 B_tau不等于B_0，
与上面矛盾。故所有充分小非零 tau 的中央环带像与初态不全等。

这个论证允许 A 的正交部分行列式为-1，不漏掉反射。
本文只声称各非零 tau 与基础像不全等，不额外声称任意两非零参数像彼此不全等。

对两个固定紧像，刚体商 Hausdorff 距离的下确界如果为0，
取逼近刚体时其平移有界、正交部分紧，便有子列收敛到真正的全等。
因此上述非全等确实给每个非零 tau 的严格正 delta_E，
并给正的握持 Hausdorff 变化；没有提供其有效比例下界。

## 9. 应用待审单调 Q 定理：完整保 H 的有限平坦领

本节暂以来源 3 的定理成立为条件。先归一 b=1，最后整体缩放恢复 b。
取 (24) 的 w=10^{-6}，在 r=w 的真实位置、框架和 (26) 处起步。
此时 Q=aa''=(1+r^2)^{-1}>0，满足该定理要求的正侧入口。

取来源 3 中的固定非增光滑 psi，定义

$$
Q_\delta(r)=\frac1{1+r^2}\,
                 \psi\!\left(\frac{r-w}{\delta}\right),\qquad
a_\delta''=Q_\delta/a_\delta,\quad
a_\delta(w)=\sqrt{1+w^2},\quad
a_\delta'(w)=w/\sqrt{1+w^2}.
\tag{41}
$$

Q_delta>=0 且 Q_delta'<=0；a,a',a'' 有与 delta 无关的统一界。
(19) 及固定紧时间区间给初值 C=a kappa 的统一正下界，
并给所有所需低阶 Sobolev 范数界。故来源 3 的结论先给
**同一个与 delta 无关的 T>0**，之后才选择
0<delta<min(w,T/2)。没有以更尖截止反过来假设同一寿命。

所得第二形式与真实径向标架重构给一个共同材料域

$$
M_\delta=[-w,w+\delta]\times\mathbb T_\ell,\qquad
g_\delta=dr^2+a_\delta(r)^2du^2
\tag{42}
$$

上的实际 C-infinity 族；在 r<=w 仍使用原 (25)。
在 [w,w+delta/4]，(41) 恰与旧 a=sqrt(1+r^2) 相同，
光滑 Cauchy 唯一性和实际位置初值给开重叠上的同一个 B_tau。
于是接缝全部 jet 相等。原区域中的 H 完整保留。

为明确位置而不是只解第二形式，重构方程是

$$
F_r=e_1,\quad (e_1)_r=LN,\quad
(e_2)_r=(M/a)N,\quad N_r=-Le_1-(M/a)e_2 .
\tag{43}
$$

Gauss–Codazzi 保持角向等式
F_u=ae_2、(e_1)_u=a'e_2+MN、
(e_2)_u=-a'e_1+(C/a)N、N_u=-Me_1-(C/a)e_2；
这些误差具有零初值并满足齐次径向方程。
实际周期初值及周期系数的 ODE 唯一性使位置、标架一起周期，
也保持 C3。这里没有漏掉平移 monodromy 或另行选择出口高度。

(32) 的统一全局常数 gamma=1/321 在 |r|<=2w 上有效。
来源 3 的低阶界给统一 L_max、M_max。
令 delta 进一步满足

$$
\delta(L_{\max}+3/2+M_{\max})<\gamma/2 .
\tag{44}
$$

由 (43) 及角方程，新增图与原 B_tau 的一阶导数差
沿 r 积分不超过 (44) 左边，旧域差为0。
沿两个材料点间的可行直线段积分，
得到整个 (42) 的全局弦长下界 gamma/2，从而全时间嵌入。
同样的有限 Hessian 界 H_* 与 §6 的边界单侧论证给
reach>=gamma^2/(4H_*)>0。这个界不继承 R45，不承诺 0.03D。
§7 的单位径向速度估计给完整新域的 (37)。

还须排除新领加入后出现全像全等。在新领中，

$$
|K|=Q_\delta/a_\delta^2\le(1+w^2)^{-2},
$$

而在保留的旧区域 K=-(1+r^2)^{-2}。
因此内在条件

$$
K<-(1+w^2/4)^{-2}
\tag{45}
$$

恰选出中央 |r|<w/2。任何完整像之间的欧氏全等
都必须把这一中央子图映到对应中央子图，与 §8 矛盾。
故严格全 E(3) 非平凡性传给完整新领，同时固定 H 与其尺寸仍保留。

在 r>=w+3delta/4 上，a_delta 为正斜率仿射函数，
所以这里是有限宽的真正平坦领。
由于 C>0，其第二基本形式仍为非零秩一。
此外 a_delta'<=w+delta<=2w，而 ell<2pi sqrt6<16，
所以内禀展开的总角 a_delta' ell<32·10^{-6}，不是2pi。
这些事实不等于抵达 R43 或固定的平圆环。

## 10. 正确的完成边界

本文实际补上的步骤是：正 C 显式闭中心线具有四个独立首扇区约束，
可产生精确共同周长、位置闭合、固定材料开片、全时间正宽嵌入
且全 E(3) 非全等的真实光滑 bump 族。
原固定积分常数和共同弧长 gauge 使 H 真正逐点固定；
对整个小领初态的 diam(H)/D>9/13 有明确证明。

待来源 3 完整独审通过后，§9 把这些性质延到有限平坦领。
仍未提供闭曲面、指定出口位置或全两 jet、
有效可见幅度、所需归一 reach、网格或最终独立完整运行。
原本角解析的 R46 不提供固定 H；本文不把非解析 bump 偷换入其 CK 假设。
水平核心的 Q=0 正向进入鞍领也不属于本稿单调 Q 用法。

文末只有新增简单有理常数的可复核检查源；它不计算中心线数组，
不求 PDE，也不能代替上述几何及存在证明。

## 11. 冻结的纯有理检查源与运行身份

以下 JavaScript 只核本文新增的 13 个简单有理不等式。
它不构造 d、c 的数组，不评价隐函数、不运行场方程。
正文冻结时不预报执行成功；实际执行结果、时间及所绑定的本正文 commit/blob
另存独立小回执，且不能冒充未参与者独跑。

```javascript
(() => {
  "use strict";
  const gcd = (x,y) => { x=x<0n?-x:x; y=y<0n?-y:y;
    while(y!==0n){ const r=x%y; x=y; y=r; } return x; };
  const Q = (n,d=1n) => { n=BigInt(n); d=BigInt(d);
    if(d===0n) throw Error("zero denominator");
    if(d<0n){n=-n;d=-d;} const g=gcd(n,d); return [n/g,d/g]; };
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>add(a,Q(-b[0],b[1]));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const sq=a=>mul(a,a);
  const fmt=a=>String(a[0])+"/"+String(a[1]);
  const rows=[];
  const pass=(name,a,b)=>{if(!lt(a,b))throw Error(name);
    rows.push({name,left:fmt(a),right:fmt(b),result:"PASS"});};
  const w=Q(1n,1000000n);
  const U=div(mul(mul(mul(Q(708n,1000n),Q(518n,1000n)),
       Q(857n,1000n)),sub(Q(3n),mul(Q(2n),Q(707n,1000n)))),Q(3n));
  pass("U upper",U,Q(17n,100n));
  pass("center norm",add(Q(141n,100n),add(Q(17n,100n),Q(12n,1000n))),Q(8n,5n));
  pass("H distance squared",sq(Q(9n,4n)),mul(Q(3n),sq(Q(67n,50n))));
  pass("whole initial radius",add(Q(8n,5n),mul(Q(2n),w)),Q(13n,8n));
  pass("H diameter fraction",Q(1n,5n),Q(9n,13n));
  pass("normal tube margin",mul(Q(2n*69632n),w),Q(1n,5n));
  pass("v difference coefficient",add(add(Q(1n),Q(5n,4n)),mul(Q(640n),w)),Q(3n));
  pass("parameter chord squared",add(sq(Q(3n)),sq(Q(320n))),sq(Q(321n)));
  pass("u second derivative",add(Q(68n),mul(Q(138n),w)),Q(69n));
  pass("full Hessian",add(Q(70n),mul(Q(138n),w)),Q(71n));
  pass("sqrt six majorant",Q(6n),sq(Q(5n,2n)));
  pass("sphere length majorant",Q(110n,7n),Q(16n));
  pass("nonstandard cone angle",mul(Q(32n),w),Q(6n));
  return {kind:"exact BigInt rational inequalities",count:rows.length,rows,
    geometry_arrays:false,pde_solver:false,terminal_execution:false};
})()
```
