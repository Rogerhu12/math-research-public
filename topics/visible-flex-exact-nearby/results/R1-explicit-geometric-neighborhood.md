# R1：M12 周围的显式几何邻域与结构性非全等

2026-11-10，visible-exact-astra-76e8 / geometry_transfer。

**状态：已证明。** 本结果付清精确化之后所需的全部几何转移常数。它没有证明精确等距校正存在，故仍为本题中间结果。

## 1. 固定参考对象、范数及结论

参考对象唯一取相邻课题 `visible-flexible-closed-surface` 的 R21 第一档 critical M12 闭族，记为 $\widetilde F_\alpha:S^2\to\mathbb R^3$，$0\le\alpha\le2\pi/3$。其两完整固定帽记为 $H$，其实际初始直径记为

$$d=\operatorname{diam}\widetilde F_0(S^2).$$

不是用包围球上界代替 $d$。相邻 R21 §§1、3、5 及 R25 §1 已证明

$$
d<3.787021,\quad
\widetilde\delta_{\rm hold}>0.05278d,\quad
\operatorname{diam}\widetilde F_0(H)>0.9354d,
\tag{1.1}
$$

$$
\operatorname{reach}(\widetilde F_\alpha(S^2))>0.0312d,
\quad |\widetilde F_\alpha|<1.894,
\quad\widetilde F_\alpha\cdot\widetilde n_\alpha>0.737.
\tag{1.2}
$$

这是公共两 jet 精确拼接的真实 $C^2$ 闭图，不是将原始分段数值曲线的接缝跳跃忽略后得到的对象。

设 $F_0:S^2\to\mathbb R^3$ 是一个 $C^2$ 校正种子，$F_0=\widetilde F_0$ 于 $H$。在参考像 $S=\widetilde F_0(S^2)$ 上定义 Cartesian 向量校正

$$V=(F_0-\widetilde F_0)\circ\widetilde F_0^{-1}.$$

导数 $\nabla V,\nabla^2V$ 用 $S$ 的诱导 Levi--Civita 联络及值域的平坦联络；范数为对单位切向量的算子范数。假设

$$
\boxed{
\|V\|_\infty\le\frac d{10000},\qquad
\|\nabla V\|_\infty\le\frac1{100},\qquad
\|\nabla^2V\|_\infty\le\frac1{10d}.}
\tag{1.3}
$$

在活动环带上令

$$F_\alpha=R_\alpha F_0\circ\tau_{-\alpha},\tag{1.4}$$

其中 $R_\alpha$ 绕原 $z$ 轴旋转，$\tau$ 为原公共材料角平移；在两帽上令 $F_\alpha=F_0$。参考两 jet 在 cuff 是轴对称的。因为 $V$ 全局 $C^2$ 且在完整帽上为零，其边界两 jet 也为零，故 (1.4) 与帽全相位精确 $C^2$ 拼接，并且 $\alpha\mapsto F_\alpha$ 在 $C^2$ 中连续。

**定理。** 在以上假设下，$F_\alpha$ 是连通闭 $C^2$ 嵌入族，$H$ 是固定握持区。记新初始直径 $D=\operatorname{diam}F_0(S^2)$，则

$$
\frac{\delta_{\rm hold}}D\ge\frac{2629}{50010}>0.0525694,
\qquad
\frac{\operatorname{diam}F_0(H)}D>0.9350>0.2,
\tag{1.5}
$$

$$
\frac{\operatorname{reach}(F_\alpha(S^2))}D
\ge\frac{637065}{20902513}>0.0304779>0.03
\quad\text{对每个 }\alpha.
\tag{1.6}
$$

若去掉固定上帽三凸起后的校正种子保留绕轴 $2\pi/3$ 旋转对称，则还有

$$\delta_E>0\qquad\text{（包括排除反射全等）}.\tag{1.7}$$

若活动区的种子诱导度量 $F_0^*e$ 对 $\tau$ 不变，则这个族对固定度量 $g=F_0^*e$ **精确等距**。这最后一个角向不变条件是待构造的解析条件，不由 (1.3) 的小范数推出。

## 2. 全相位范数与握持量

参考族采用同一相位公式，因此在活动区

$$F_\alpha-\widetilde F_\alpha
=R_\alpha(F_0-\widetilde F_0)\circ\tau_{-\alpha}.$$

旋转和材料换元保持相应参考诱导联络范数，故 (1.3) 对全相位成立。两帽上的修正为零。于是

$$
d_H(F_\alpha(S^2),\widetilde F_\alpha(S^2))\le d/10000,
\qquad D\le(1+2/10000)d.
\tag{2.1}
$$

Hausdorff 距离的三角不等式给

$$\delta_{\rm hold}\ge\widetilde\delta_{\rm hold}-2d/10000.$$

代入 (1.1)、(2.1)，

$$\frac{\delta_{\rm hold}}D
\ge\frac{0.05278-0.0002}{1.0002}
=\frac{2629}{50010}.$$

两帽固定，所以 $H$ 仍为闭且内部非空的握持区，其直径实际上未变。即使使用更松的通用两端误差也有

$$\frac{\operatorname{diam}F_0(H)}D
\ge\frac{0.9354-0.0002}{1.0002}
=\frac{4676}{5001}>0.9350.$$

这里比较的是**像集**，没有把材料点沿像集移动的距离算成握持变化。

## 3. 支撑、主曲率及全局 reach

### 3.1 校正的直接微分估计

暂记 $G(x)=x+V(x)$，并设

$$\|V\|\le a,\quad\|\nabla V\|\le b<1,
\quad\|\nabla^2V\|\le c.$$

对 $u\in T_xS$，有

$$|dG(u)|\ge(1-b)|u|.\tag{3.1}$$

所以 $G$ 为浸入。沿 $G_s=x+sV$ 连续选择与参考法向 $n$ 一致的法向 $n_s$。因为对每个单位切向量 $u$ 都有
$n_s\cdot(u+s,dV(u))=0$，所以 $|P_{T_xS}n_s|\le sb$。由连续性取正向分支，

$$n_s\cdot n\ge\sqrt{1-s^2b^2},\qquad
|n_s-n|\le\sqrt2\,sb\le2sb.$$

若 $|x|\le R$、$x\cdot n\ge\sigma$，则

$$G_s\cdot n_s\ge\sigma-2sRb-sa.\tag{3.2}$$

二阶基本形式的精确变换为

$$
\mathrm{II}_{G}(dG(u),dG(v))
=n_G\cdot\bigl(\mathrm{II}_S(u,v)n+\nabla^2V(u,v)\bigr).
\tag{3.3}
$$

因为从二阶导数减去的 $dG(\nabla^S_uv)$ 是新切向量，点乘 $n_G$ 后消失。若参考 $|\kappa_i|\le K$，(3.1)--(3.3) 给

$$|\kappa_i(G)|\le\frac{K+c}{(1-b)^2}.\tag{3.4}$$

全程只用 $C^2$ 正则性，没有求曲率导数。

### 3.2 正支撑确实给全局法向管

相邻 R10 的直接论证如下。若闭连通 $C^2$ 浸入 $X$ 有
$X\cdot n\ge\sigma_*>0$、$|\kappa_i|\le K_*$，则对于
$|s|<\min\{\sigma_*,1/K_*\}$，平行面 $X_s=X+sn$ 仍是 $C^1$ 浸入，法向为 $n$，并有 $X_s\cdot n>0$。

径向投影 $X_s/|X_s|$ 是局部微分同胚。紧性、连通性及目标球面单连通使其为一层覆盖，所以每个 $X_s$ 为径向嵌入。写同一方向的交点为
$X_s(p(s,u))=r(s,u)u$。联合反函数定理保证它对 $(s,u)$ 为 $C^1$；对 $s$ 求导并点乘 $n$ 得

$$\partial_s r(s,u)=1/(u\cdot n)>0.$$

所以不同平行面严格嵌套，整个法向管全局单射。距离原曲面小于该管半径的点都有最近点，最近点的一阶条件给法向表示，单射性使最近点唯一。故

$$\operatorname{reach}(X(M))\ge\min\{\sigma_*,1/K_*\}.\tag{3.5}$$

这一证明控制远处不同部分的接近，不能缩写为“曲率有界所以 reach 有界”。

### 3.3 将 M12 余量代入

参考 reach $>0.0312d$ 蕴含 $Kd\le1250/39$。用 (1.3) 的

$$a\le d/10000<379/10^6,\quad b\le1/100,\quad cd\le1/10,$$

(3.2) 的支撑下界大于

$$0.737-2(1.894)(0.01)-0.000379=0.698741>0.$$

因此 $G_s$ 的每个像都为径向图，特别是校正种子嵌入。由 (3.4)、(3.5)，校正后的 reach 至少为

$$r_*:=\frac{(99/100)^2}{1250/39+1/10}\,d.$$

这里 $r_*<0.031d<0.118<0.698741$，所以支撑项不限制这个下界。再除以 (2.1) 的新直径上界，即得

$$\frac{r_*}D\ge
\frac{(99/100)^2}{(1250/39+1/10)(5001/5000)}
=\frac{637065}{20902513}>0.0304779.$$

同样的范数和支撑计算对全相位成立，故完成 (1.6)。

## 4. 校正后主体三阶矩仍有明确正余量

去掉上帽三个固定凸起，得到参考未标记实体 $\widetilde\Omega$。相邻 R17 §B.4、R21 §3 给

$$\operatorname{Re}\widetilde A_3
:=\operatorname{Re}\int_{\widetilde\Omega}(x+iy)^3,dV
>0.4401644538270965>0.44.\tag{4.1}$$

两平帽仍满足同一球界和正支撑界。校正于完整帽上为零，所以在去凸起的曲面上仍可用同一 $V$ 和 (1.3)。记校正后的未标记域为 $\Omega$。

取安全有理数

$$R=947/500,\quad\sigma=737/1000,\quad
\eta=379/10^6,\quad b=1/100.$$

上节证明 $x+sV$ 全程为正支撑嵌入，记它围成的域为 $\Omega_s$。散度定理和球包围给

$$
\sigma\operatorname{Area}(\partial\widetilde\Omega)
\le3\operatorname{Vol}(\widetilde\Omega)
\le4\pi R^3,
$$

$$\operatorname{Area}(\partial\widetilde\Omega)
\le4\pi R^3/\sigma<116.\tag{4.2}$$

沿直线同伦的体积积分变分公式为

$$
\frac d{ds}\int_{\Omega_s}(x+iy)^3,dV
=\int_{\partial\widetilde\Omega}
(G_{s,1}+iG_{s,2})^3(V\cdot n_s)J_s,dA.
$$

这里 $|G_s|\le R+\eta$、$J_s\le(1+sb)^2$，所以

$$
|A_3-\widetilde A_3|
\le\eta(R+\eta)^3(1+b)^2\frac{4\pi R^3}{\sigma}<0.305.
\tag{4.3}
$$

最后的严格不等式只需 $\pi<22/7$：所得精确有理上界是

$$
\frac{22321969311850019326971530329810963}
{73281250000000000000000000000000000}<\frac{305}{1000}.
$$

因此

$$\boxed{\operatorname{Re}A_3>0.135.}\tag{4.4}$$

这适用于一般 Cartesian 向量校正，不要求先化为法向图，也没有引入 $C^3$ 假设。

## 5. 固定三凸起给包括反射的非全等

两帽固定，三凸起使用相邻 R16 §1 的同一参数和同一函数：中心半径 $c_0=2/25$，局部半径 $a_0=3/100$，高度 $h_0=1/2000$，三个中心等角分布，每个高度函数为

$$h_0(1-|z-z_j|^2/a_0^2)_+^3.$$

圆对称积分消去非零纯复幂，故凸起的水平三阶体积矩为

$$B_3=\frac{3\pi c_0^3a_0^2h_0}{4}
=\frac{27\pi}{156250000000}>0.\tag{5.1}$$

校正未标记体的 reach 由上一节的同一正支撑、曲率计算控制，远大于凸起高度 $1/2000$。所以凸起位于固定平帽的外侧法向管中，可按 R16 §1 作体积矩加法。亦可直接用 R17 §B.5 的正支撑加帽同伦及散度公式，无须此额外解释。

假设未标记体具有三重旋转对称。所有标记实体也如此，故水平质心为零；体积、$z$ 一阶矩和 $z$ 质心不随相位改变。对完整实体定义中心三阶矩张量

$$T_{ijk}(\alpha)=\int(X_i-\bar X_i)(X_j-\bar X_j)(X_k-\bar X_k),dV.$$

相邻 R16 §3 的计算可以直接复述：三重对称给

$$
T_{xxx}+T_{xyy}=T_{xxy}+T_{yyy}=0,
\qquad T_{xxz}=T_{yyz},
\qquad T_{xyz}=T_{xzz}=T_{yzz}=0.
$$

$T_{xxz},T_{zzz}$ 不随绕轴相位改变。置 $u=T_{xxx}=-T_{xyy}$、$v=T_{xxy}=-T_{yyy}$，则水平复矩为 $4(u+iv)$，水平张量平方范数为 $4(u^2+v^2)$。故

$$
I(\alpha):=\|T(\alpha)\|_F^2
=C+\frac14|A_3e^{3i\alpha}+B_3|^2,
\tag{5.2}
$$

其中 $C$ 不随相位改变。此公式不要求水平镜像对称，允许 $A_3$ 为复数。

$I$ 在全部欧氏刚体下不变，因为平移由中心化消去，$Q\in O(3)$ 对张量的作用 $Q^{\otimes3}$ 保持 Frobenius 范数。由 (4.4)、(5.1)、(5.2)，

$$
I(0)-I(\pi/3)=B_3\operatorname{Re}A_3
>\frac{27}{200}\frac{27\pi}{156250000000}
>6.9984\times10^{-11}>0.
\tag{5.3}
$$

所以这两个时刻的完整像不全等，反射亦被排除。若刚体对齐 Hausdorff 下确界为零，取趋近该下确界的刚体列。紧非空像集使平移部分有界，$O(3)$ 紧使正交部分有收敛子列，其极限刚体会使两像真正相等，矛盾。这证明 $\delta_E>0$。

## 6. 精确度量的接口及尚未解决的条件

若活动种子 $F_0^*e$ 对材料角平移 $\tau$ 不变，则

$$F_\alpha^*e=\tau_{-\alpha}^*(F_0^*e)=F_0^*e$$

于活动区成立；帽固定，其度量不变；公共两 jet 保证全局为同一诱导度量。因此完全可以把最终 $g$ **定义为校正种子的输出度量**，并不需要预先锁定为旧数值图的目标 $g$。但必须真正解出角向非均值的度量缺陷，不能把取角平均后的张量当成已经诱导出来的度量。

本 R1 把几何端收敛为 (1.3)、固定帽零二 jet 和三重对称三个可执行条件。主目标仍缺：具有轴对称活动诱导度量的精确种子，以及相对于本参考图的全域校正界 (1.3)。有限模解、小度量残差、仅形式校正或未付常数的右逆，均不满足这个缺口。

## 来源

所用相邻结果均在 `topics/visible-flexible-closed-surface/results/`：

- R10 `R10-positive-support-offset-reach.md` §§1--3：直接全局法向管。
- R16 `R16-fixed-cap-volume-moment-noncongruence.md` §§1--3：固定帽与全欧氏群的中心三阶矩。
- R17 `R17-exact-finite-visible-closed-geometry.md` §A.4、§B.4--B.5：公共闭图、去凸起实体和加帽。
- R21 `R21-m12-whole-map-and-actual-metric-decrease.md` §§1、3、5：本 M12 对象、主体矩及全图几何。
- R25 `R25-m12-sharper-enclosing-ball.md` §1：同图直径包围及严格归一化比例。

更一般、无需正支撑的 reach 双点转移已完整写在本题 `notes/2026-11-10-geometric-transfer.md` §4；本 R1 的结论不依赖那个较弱版本。
