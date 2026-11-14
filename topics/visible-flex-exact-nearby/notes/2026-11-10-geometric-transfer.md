# 可见精确化的几何转移：全局 reach、握持与结构性非全等

2026-11-10，visible-exact-astra-76e8 / geometry_transfer。

**状态：以下转移命题及显式预算已证明；仍为主问题的中间结论。** 它们不证明精确等距校正存在。其作用是把真正待付的解析估计明确收敛到一个修正范数范围，并说明不必把欧氏取商 Hausdorff 距离直接估到微小的矩差尺度。

本文沿用本题 README 以及相邻课题 R21、R25 的同一 M12 有限闭图。用 $\widetilde F_t$ 表示这个参考族，$d=\operatorname{diam}\widetilde F_0(M)$。**$d$ 是实际参考直径，不是其包围球上界。** 相邻 R21/R25 已给

$$
d<3.787021,\qquad
\widetilde\delta_{\rm hold}>0.05278d,\qquad
\operatorname{reach}(\widetilde F_t(M))>0.0312d,
\tag{0.1}
$$

$$
\operatorname{diam}\widetilde F_0(H)>0.9354d,
\qquad |\widetilde F_t|<1.894,\qquad
\widetilde F_t\cdot\widetilde n_t>0.737.
\tag{0.2}
$$

参考对象是 R21 第一档 critical M12，不将其他 M14/M15 图的量混入。R21 已给公共两 jet 的真正 $C^2$ 有限闭图；仅逐段解释、接缝 jet 不相等的原始数值曲线不能直接作为本引理的输入。

## 1. 范数和主要可用结论

在参考曲面 $S_t=\widetilde F_t(M)$ 上，把修正写成

$$
V_t= (F_t-\widetilde F_t)\circ\widetilde F_t^{-1}.
$$

$\nabla V_t$、$\nabla^2V_t$ 使用 $S_t$ 的诱导 Levi--Civita 联络，值域使用 $\mathbb R^3$ 的平坦联络。范数取对单位切向量的算子范数；例如

$$
\nabla^2V(u,v)=D_u(dV(v))-dV(\nabla^S_u v).
$$

因此本文的二阶界既不是坐标二阶导数的裸上界，也不是只控制法向分量。

**命题 1（M12 的显式保余量范围）。** 假设校正族空间上为 $C^2$、对 $t$ 在 $C^2$ 中连续，并在所有 $t$ 满足

$$
\boxed{\quad
\|V_t\|_\infty\le10^{-4}d,\qquad
\|\nabla V_t\|_\infty\le10^{-2},\qquad
\|\nabla^2V_t\|_\infty\le\frac{1}{10d}.
\quad}
\tag{1.1}
$$

若 $V_t|_{\widetilde F_t(H)}$ 在公共材料点上不随 $t$ 改变，则 $H$ 仍是固定握持区。每个 $F_t$ 是闭嵌入，且对于**新直径** $D=\operatorname{diam}F_0(M)$，

$$
\frac{\delta_{\rm hold}}D\ge\frac{2629}{50010}
>0.0525694,
\tag{1.2}
$$

$$
\frac{\operatorname{diam}F_0(H)}D
\ge\frac{4676}{5001}>0.9350>0.2,
\tag{1.3}
$$

$$
\frac{\operatorname{reach}(F_t(M))}D
\ge\frac{637065}{20902513}>0.0304779>0.03
\qquad(0\le t\le1).
\tag{1.4}
$$

如果还采用第 5 节的相位族、保持三重旋转对称并令修正在完整两帽上为零，则还严格有 $\delta_E>0$。这最后一步不需要把任意校正的 $C^0$ 大小压到原三阶矩不变量差 $10^{-10}$ 的尺度。

这里只是校正**若已得到**时的定理。精确的等距方程、真实无限尾、给出满足 (1.1) 的校正以及公共帽两 jet，仍由解析存在部分负责。

## 2. Hausdorff、直径和握持的直接转移

设 $\sup_{p,t}|F_t(p)-\widetilde F_t(p)|\le a$。逐点配对立即给

$$
d_H(F_t(M),\widetilde F_t(M))\le a,
\qquad |D-d|\le2a.
\tag{2.1}
$$

Hausdorff 距离的三角不等式给

$$
|\delta_{\rm hold}-\widetilde\delta_{\rm hold}|\le2a.
\tag{2.2}
$$

同理，对每个刚体 $A\in E(3)$，两项 Hausdorff 距离之差至多 $2a$；先对 $A$ 取下确界，再对 $t$ 取上确界，得到

$$
|\delta_E-\widetilde\delta_E|\le2a.
\tag{2.3}
$$

包括反射不会改变这一论证。(2.3) 是一般转移式，但若只有一个很小的正不变量差，直接经此式量化往往浪费余量；第 5 节使用同一构造的结构。

握持的**相等条件**不能由小范数推出。必须另有 $F_t|_H=F_0|_H$，例如 $V_t=0$ 于两完整帽；只有这样才能解释 (2.2) 为本题要求的握持变化。$H$ 的闭性和内部非空是固定参数子集的性质，修正不会改变。

取 $a=d/10000$，将 (0.1) 和 (0.2) 代入，得到

$$
\frac{\delta_{\rm hold}}D
\ge\frac{0.05278-0.0002}{1.0002}=\frac{2629}{50010},
$$

$$
\frac{\operatorname{diam}F_0(H)}D
\ge\frac{0.9354-0.0002}{1.0002}=\frac{4676}{5001}.
$$

如果修正在 $H$ 上为零，第二式还可以去掉分子的 $0.0002$，但无须使用此改进。

## 3. 正支撑曲面的 reach 转移：适用于本 M12 的较宽预算

### 3.1 正支撑和主曲率给全局法向管

**引理 3.1。** 设 $X:M\to\mathbb R^3$ 是连通紧致无边界 $C^2$ 浸入，有连续单位法向 $n$，并有

$$
X\cdot n\ge\sigma>0,\qquad |\kappa_i|\le K.
$$

则 $X$ 实际为嵌入，且

$$
\operatorname{reach}(X(M))\ge\min\{\sigma,K^{-1}\}.
\tag{3.1}
$$

**证明。** 先固定 $|s|<\min\{\sigma,K^{-1}\}$，考虑平行曲面
$X_s=X+sn$。因为 $1-s\kappa_i\ne0$，它仍为浸入，且法向仍可取 $n$。又有
$X_s\cdot n\ge\sigma-|s|>0$。所以径向投影

$$
p\longmapsto\frac{X_s(p)}{|X_s(p)|}
$$

是到 $S^2$ 的局部微分同胚。紧性使其成为覆盖；$M$ 连通而 $S^2$ 单连通，故覆盖只有一层。于是每个 $X_s(M)$ 都是正径向图，特别是 $s=0$ 时 $X$ 嵌入。

把同一方向 $u\in S^2$ 上的点写成 $r_s(u)u=X_s(p_s(u))$。逆函数定理给其对 $s$ 的 $C^1$ 依赖。对 $s$ 求导，再与 $n(p_s(u))$ 内积，切向项消失，得到

$$
\partial_s r_s(u)=\frac1{u\cdot n(p_s(u))}>0.
$$

所以不同 $s$ 的平行曲面互不相交，同一个 $s$ 上也无重合。法向管映射 $(p,s)\mapsto X(p)+sn(p)$ 在上述开区间上全局单射。任一点到 $X(M)$ 的距离小于该区间半径时有最近点，且到最近点的位移垂直于切平面；因此该点必在这条法向管内，单射性保证最近点唯一。令管半径趋于 $\min\{\sigma,K^{-1}\}$ 即得 (3.1)。证毕。

这正是相邻 R10 的星形法向管机制，确实同时处理了远处曲面部分接近的问题，而非仅以局部曲率冒充 reach。

### 3.2 一般向量校正下的曲率与支撑

设 $S$ 为参考曲面，$G(x)=x+V(x)$，并记

$$
\|V\|\le a,\qquad\|\nabla V\|\le b<1,\qquad
\|\nabla^2V\|\le c.
$$

对于 $u\in T_xS$，

$$
|dG(u)|\ge(1-b)|u|.
\tag{3.2}
$$

所以 $G$ 为浸入。沿直线同伦 $G_s=x+sV$ 选取与参考法向连续一致的法向 $n_s$。由 $n_s\perp u+s\,dV(u)$，对所有单位切向量 $u$ 都有
$|n_s\cdot u|\le sb$。连续性排除法向翻转，因此

$$
n_s\cdot n\ge\sqrt{1-s^2b^2},\qquad
|n_s-n|\le\sqrt2\,sb\le2sb.
\tag{3.3}
$$

若参考有 $|x|\le R$、$x\cdot n\ge\sigma$，则

$$
G_s\cdot n_s\ge\sigma-2sRb-sa.
\tag{3.4}
$$

当 $\sigma-2Rb-a>0$ 时，上述径向覆盖论证保证整个同伦都是嵌入。此处仅用一阶界，不需二阶或曲率导数。

二阶基本形式满足精确等式

$$
\mathrm{II}_{G}(dG(u),dG(v))
=n_G\cdot\bigl(\mathrm{II}_S(u,v)n+\nabla^2V(u,v)\bigr).
\tag{3.5}
$$

这是因为用参考联络减去的 $dG(\nabla^S_uv)$ 在新曲面的切空间内。令 $v=u$ 并用 (3.2)，可得

$$
|\kappa_i(G)|\le\frac{K+c}{(1-b)^2}.
\tag{3.6}
$$

联合引理 3.1：

$$
\boxed{\quad
\operatorname{reach}(G(S))\ge
\min\left\{\sigma-2Rb-a,
\frac{(1-b)^2}{K+c}\right\}.
\quad}
\tag{3.7}
$$

### 3.3 M12 的显式数值余量

由 (0.1) 的 reach 界可取 $Kd\le1/0.0312=1250/39$。在 (1.1) 下，

$$
a\le d/10000<0.000379,\quad b\le1/100,\quad cd\le1/10.
$$

支撑项严格大于

$$
\frac{737}{1000}-2\frac{947}{500}\frac1{100}
-\frac{379}{10^6}
=0.698741.
$$

曲率给出的统一下界为

$$
\frac{(99/100)^2}{1250/39+1/10}\,d.
$$

这个下界小于 $0.031d<0.118$，故上述支撑项远大于它。再用 $D\le(5001/5000)d$，得到

$$
\frac{\operatorname{reach}(F_t(M))}D
\ge\frac{(99/100)^2}
{(1250/39+1/10)(5001/5000)}
=\frac{637065}{20902513}>0.0304779.
$$

这些比较可直接在有理数中完成，所有十进数在此均为明确的有限十进有理数。

## 4. 不依赖正支撑的普适双点 reach 转移

下面的独立版本可用于未来不再星形的候选。它不借助 $C^3$ 正则性，也不需要延拓 $V$ 到环境空间再估计延拓的二阶导数。

**命题 4。** 设 $S\subset\mathbb R^3$ 为紧致无边界 $C^2$ 嵌入曲面，$\operatorname{reach}(S)\ge\rho>0$，并有

$$
\|V\|\le a<\rho/2,\qquad
\|\nabla V\|\le b<1/2,\qquad
\|\nabla^2V\|\le c.
$$

则 $G=\mathrm{id}+V$ 为嵌入，且

$$
\boxed{\quad
\operatorname{reach}(G(S))\ge\rho\min\left\{
\frac{(1-2b)^2}{1+4b+4\rho c},
\frac{(1-2a/\rho)^2}{1+4a/\rho+2b}
\right\}.
\quad}
\tag{4.1}
$$

**证明。** Federer 的双点刻画给出

$$
\operatorname{dist}(q-p,T_pS)\le\frac{|q-p|^2}{2\rho}
\quad(p,q\in S).
\tag{4.2}
$$

它也给 $|\kappa_i|\le1/\rho$。写 $d_{pq}=|q-p|$、$P_p$ 为切平面的正交投影，$A_p=dV_p\circ P_p$。沿 $S$ 中单位速度曲线 $\gamma$，对固定环境向量 $w$ 有

$$
\frac d{ds}(A_{\gamma(s)}w)
=\nabla^2V(\dot\gamma,Pw)
+dV\bigl(P\tfrac d{ds}P\,w\bigr).
$$

若局部取法向 $n$，则 $P=I-n\otimes n$，故
$P P'w=-n'\langle n,w\rangle$。于是

$$
\left\|\frac d{ds}A_{\gamma(s)}\right\|
\le c+b/\rho=:L.
\tag{4.3}
$$

这里仅出现第二基本形式，未出现它的导数。

先设 $d_{pq}\le\rho$。连接 $p,q$ 的环境线段距离 $S$ 至多 $d_{pq}/2\le\rho/2$。最近点投影在该管内的 Lipschitz 常数至多 $2$，故投影线段是一条连接 $p,q$、长度 $\ell\le2d_{pq}$ 的曲面路径。该投影界来自 Federer Theorem 4.8(8)，也可从 $D\pi=(I-s\mathcal S)^{-1}P$ 直接得出。沿此路径积分得

$$
|V(q)-V(p)|\le b\ell\le2b,d_{pq},
$$

$$
|V(q)-V(p)-A_p(q-p)|\le\frac L2\ell^2
\le2L,d_{pq}^2.
\tag{4.4}
$$

以 $dG_p(P_p(q-p))$ 作为新切平面的比较向量，(4.2)、(4.4) 给

$$
\operatorname{dist}(G(q)-G(p),T_{G(p)}G(S))
\le\frac{d_{pq}^2}{2\rho}+2L,d_{pq}^2,
$$

而 $|G(q)-G(p)|\ge(1-2b)d_{pq}>0$。因此这类双点的 reach 比值至少为 (4.1) 的第一项。

再设 $d_{pq}\ge\rho$。直接用 $|V(q)-V(p)|\le2a$ 及 $\|A_p\|\le b$ 得

$$
|G(q)-G(p)|\ge d_{pq}-2a\ge(1-2a/\rho)d_{pq}>0,
$$

$$
\operatorname{dist}(G(q)-G(p),T_{G(p)}G(S))
\le\frac{d_{pq}^2}{2\rho}+2a+b,d_{pq}.
$$

用 $d_{pq}\ge\rho$ 后，双点比值至少为 (4.1) 的第二项。两类双点均不重合，加上 $b<1$ 保证浸入，紧性给 $G$ 为嵌入。对新嵌入使用 Federer 双点刻画，得到 (4.1)。证毕。

例如在 (0.1) 下采用更严格的一阶要求 $b\le10^{-3}$，其余仍取 $a\le10^{-4}d$、$c\le1/(10d)$，则 (4.1) 给

$$
\operatorname{reach}(G(S))/D
\ge\frac{3003125}{98964789}>0.0303453.
$$

这一普适版本的第二项明确控制了相距较远的参数点；不把局部曲率界当成全局管半径。

## 5. 固定三凸起帽的结构性非全等转移

### 5.1 需要保留的结构

令 $\widetilde\Omega$ 为参考图**去掉上帽三个凸起**后的有界实体。R17/R21 给出它的三重轴旋转对称性，正支撑和球界仍满足 (0.2)，且

$$
\operatorname{Re}\widetilde A_3
=\operatorname{Re}\int_{\widetilde\Omega}(x+iy)^3\,dV
>0.4401644538270965>0.44.
\tag{5.1}
$$

设校正后去凸起实体 $\Omega$ 仍有三重轴旋转对称性，完整两平帽不变。活动部分以轴旋转相位生成，平帽作为集合旋转不变；再加回完全固定的三个上帽凸起。因此整个相位族的未标记实体为 $R_\alpha\Omega$，标记部分固定。

三重对称可以通过在不变函数空间中求解保留。下面不需要额外的水平镜像对称：只要 (5.1) 的实部在校正后仍为正即可。

### 5.2 用一般向量校正控制主体三阶矩

去凸起只改变固定帽内部，校正于完整帽上为零，所以 $V$ 在未标记曲面上仍满足同样范数界。设

$$
R=\frac{947}{500},\quad\sigma=\frac{737}{1000},\quad
\eta=\frac{379}{10^6},\quad b=\frac1{100}.
$$

由 $d<3.787021$ 及 (1.1)，$\|V\|\le\eta$。第 3 节证明直线同伦 $G_s=x+sV$ 全程为正支撑嵌入，其有界域记为 $\Omega_s$。

参考曲面面积用散度定理直接估计：

$$
\sigma\,\operatorname{Area}(\partial\widetilde\Omega)
\le\int_{\partial\widetilde\Omega}x\cdot n\,dA
=3\operatorname{Vol}(\widetilde\Omega)
\le4\pi R^3.
$$

所以用 $\pi<22/7$ 得

$$
\operatorname{Area}(\partial\widetilde\Omega)
\le\frac{4\pi R^3}{\sigma}<116.
\tag{5.2}
$$

Reynolds 公式（亦可由沿同伦的散度公式推导）给

$$
\frac d{ds}\int_{\Omega_s}(x+iy)^3\,dV
=\int_{\partial\widetilde\Omega}
\bigl(G_{s,1}+iG_{s,2}\bigr)^3
\,(V\cdot n_s)\,J_s\,dA.
$$

这里 $J_s\le(1+sb)^2$，$|G_s|\le R+\eta$。故

$$
|A_3-\widetilde A_3|
\le\eta(R+\eta)^3(1+b)^2\frac{4\pi R^3}{\sigma}
<0.305.
\tag{5.3}
$$

最后一个比较完全可以用 $\pi<22/7$ 和上述有限十进有理数完成；其精确有理上界为 $22321969311850019326971530329810963/73281250000000000000000000000000000<0.304607$。于是

$$
\boxed{\operatorname{Re}A_3>0.135.}
\tag{5.4}
$$

这不需要先把校正改写成法向图。如已知是法向图 $x+h(x)n(x)$，还可用法向管体积元得到更紧的

$$
|A_3-\widetilde A_3|
\le\eta(R+\eta)^3(1+8.463\eta)^2\frac{4\pi R^3}{\sigma}
<0.302,
$$

但该改进并非后续结论所需。

### 5.3 包括反射在内的非全等证明

固定三凸起采用 R16 的参数：中心半径 $c_0=2/25$、每个凸起的支撑圆盘半径 $a_0=3/100$、高度 $h_0=1/2000$，每个高度为径向函数

$$
h_0\left(1-\frac{|z-z_j|^2}{a_0^2}\right)_+^3,
\qquad z_j=c_0e^{2\pi ij/3},\quad j=0,1,2.
$$

圆对称积分消去 $z-z_j$ 的所有非零纯复幂，故三个凸起的水平三阶体积矩为

$$
B_3=\frac{3\pi c_0^3a_0^2h_0}{4}
=\frac{27\pi}{156250000000}>0.
\tag{5.5}
$$

考虑完整有界实体的中心三阶矩张量

$$
T_{ijk}(\alpha)=\int_{\Omega^{\rm marked}_\alpha}
(x_i-\bar x_i)(x_j-\bar x_j)(x_k-\bar x_k)\,dV,
\qquad I(\alpha)=\sum_{i,j,k}T_{ijk}(\alpha)^2.
$$

它在全部 $E(3)$（包括反射）下不变。三重旋转对称使水平质心为零，$z$ 质心不随相位改变。三阶对称张量在绕轴旋转下只有权 $0$ 与权 $3$ 的部分可能保留；权 $0$ 的部分不随相位改变。水平三阶张量满足

$$
T_{111}+T_{122}=T_{112}+T_{222}=0,
$$

所以其平方范数为 $\frac14|\int(x+iy)^3dV|^2$。其余非零分量均为绕轴不变部分。因此

$$
I(\alpha)=C+\frac14|A_3e^{3i\alpha}+B_3|^2,
\tag{5.6}
$$

其中 $C$ 不随相位改变。凸起矩的加法可由相邻 R16 的散度论证，或在固定帽上把凸起高度从 $0$ 连续增加至 $h_0$ 后积分得到；整个加帽同伦保持正支撑。

由 (5.4)--(5.6)，

$$
I(0)-I(\pi/3)=B_3\operatorname{Re}A_3
>\frac{27}{200}\frac{27\pi}{156250000000}
>6.9984\times10^{-11}>0.
\tag{5.7}
$$

所以这两个时刻的像不可能由任何刚体（含反射）相互得到。若它们的刚体对齐 Hausdorff 下确界为零，可选逼近该下确界的刚体序列。紧非空像集使平移部分有界，$O(3)$ 紧使正交部分有收敛子列，其极限刚体会使两像真正相等，矛盾。因此 $\delta_E>0$。

### 5.4 不必对全部时间重新求解

如果精确种子 $F_0$ 的活动区诱导度量对材料角平移不变，且它与固定帽匹配公共两 jet，则

$$
F_\alpha=R_\alpha F_0\circ\tau_{-\alpha}
$$

在活动区、固定帽上不变，给全时间的精确等距族。其修正与参考相位族之差是同一 $V$ 经旋转和材料换元所得；空间范数及参考诱导联络的范数保持，所以种子的 (1.1) 控制自动推广到全部相位。此观察只是几何生成机制，**不证明该精确种子存在**。

## 6. 对后验分析的精确接口

本 note 已付清以下几何端条件：

1. 对相邻 R21/R25 的具体有限 $C^2$ 图，(1.1) 足以保留定量握持、reach、闭嵌入；不需要 $C^3$ 界。
2. 校正在帽上为零、保留三重旋转对称和相位构造时，同一 $C^0$ 范围还严格保留非全等，主体三阶矩有明确正余量 $0.135$。
3. 相位生成使一次种子的空间估计可覆盖全时间。直接的 Hausdorff 分离见证转移使用像集而非材料点位移。

仍需真正得到：固定帽两 jet 的精确种子；对同一目标度量的无限维精确等距性；相对于此具体 M12 参考图的 (1.1)；求解时保留三重旋转对称。任何有限 Galerkin 解、只控制残差而没有解误差、或只证明条件性右逆，都尚未支付这些条件。

## 7. 允许输出径向度量时，固定 H 的准确函数空间接口

本节只处理支持和接缝，避免重复自由平均的非线性代数。令活动环带靠近 cuff 的公共材料坐标为 $(x,\theta)$，活动侧 $x\ge0$，固定帽侧 $x\le0$。$x=0$ 是原轴对称平领的边界，修正用 Cartesian 向量表示。

**零延拓引理。** 若 $U$ 在活动闭侧为 $C^2$，则把它在帽上置为零得到全局 $C^2$ 校正，当且仅当其零、第一和第二阶坐标 jet 在 $x=0$ 全为零。

必要性来自帽侧导数均为零及连续性。充分性可逐阶检查差商：$U(0,\theta)=0$ 保证连续，一阶法向差商由 $U_x$ 的连续延零给出，二阶差商同理；切向和混合导数也由其零迹及连续性拼接。此陈述不要求 $C^3$，也不要求任何固定正 Hölder 指数。

一个可用于无限 Fourier 尾的显式充分条件如下。取任意非负模函数 $\omega(x)\to0$，写

$$U(x,\theta)=\sum_{n\in\mathbb Z}u_n(x)e^{in\theta}.$$

若存在非负数 $a_n$ 满足

$$
\sum_n(1+|n|)^2a_n<\infty,\qquad
|u_n^{(j)}(x)|\le a_n x^{2-j}\omega(x),
\quad j=0,1,2,
\tag{7.1}
$$

则所有总阶数至多二的 Fourier 导数均一致收敛。对 $j+k\le2$，

$$
|\partial_x^j\partial_\theta^kU(x,\theta)|
\le x^{2-j}\omega(x)\sum_n|n|^k a_n\longrightarrow0.
$$

所以 (7.1) 确实给全 $C^2$ 零延拓。可选 $\omega(x)=x^\beta$（$\beta>0$），但这只是方便的充分条件，不是添加在本题上的 Hölder 完成门。

若同时要求三重旋转等变，Cartesian 水平复分量满足
$U_h(x,\theta+2\pi/3)=e^{2\pi i/3}U_h(x,\theta)$，故其频率属于 $1+3\mathbb Z$；垂直分量频率属于 $3\mathbb Z$。若改用旋转标架，则三个分量都可用 $3\mathbb Z$，但角微分须保留标架导数。不能将 Cartesian 水平分量也直接限制到 $3\mathbb Z$。

现在令 $F=\widetilde F+U$，把活动区的度量系数记成

$$g_{ij}(x,\theta)=\partial_iF\cdot\partial_jF.$$

欲输出一个径向度量，真实方程是

$$P_{\ne0}g_{ij}=0,\qquad i,j\in\{x,\theta\},\tag{7.2}$$

其中 $P_{\ne0}$ 去掉角平均。一旦 (7.2) 真正成立，便可定义输出系数
$\bar g_{ij}(x)=\langle g_{ij}(x,\cdot)\rangle$；帽上继续取固定帽诱导度量。

零二 jet 自动支付这个新度量与固定帽的一阶拼接。事实上

$$
g_{ij}-\widetilde g_{ij}
=\partial_i\widetilde F\cdot\partial_jU
+\partial_j\widetilde F\cdot\partial_iU
+\partial_iU\cdot\partial_jU.
\tag{7.3}
$$

在 seam 上，$DU=D^2U=0$ 使 (7.3) 及其全部一阶导数为零。取角平均仍保持该性质，故输出径向度量与帽的值和第一 jet 相同。允许改变平均度量因此**不要求**改变帽或握持区。

同一观察也说明参考角向非均值残差在 seam 处具有零一 jet：原参考图与轴对称平帽本来就匹配二 jet。因此 (7.2) 的强迫项在这些边界迹上是兼容的，不会仅因固定帽而产生一个非零的 seam 残差。

这只关闭了支持与拼接的几何接口。仍须证明实际线性化或非线性求解在零二 jet 空间内可解，并给其无限 Fourier 尾如 (7.1) 的有效控制。零平均自由度不自动提供非零角模的右逆、端口兼容或无限尾收敛。

## 文献与仓库来源

- Herbert Federer, *Curvature measures*, Transactions of the American Mathematical Society **93** (1959), 418--491；Theorem 4.8(8)（最近点投影 Lipschitz 界）、Theorem 4.18（reach 双点刻画）、Theorem 4.19（环境变换下的 reach）。[AMS 原文](https://www.ams.org/tran/1959-093-03/S0002-9947-1959-0110078-1/S0002-9947-1959-0110078-1.pdf)。第 4 节的具体曲面内在校正估计为本文推导，不以 Theorem 4.19 代替缺失的环境延拓。
- `topics/visible-flexible-closed-surface/results/R10-positive-support-offset-reach.md`：正支撑法向管；第 3 节给出所用结论的完整证明。
- `topics/visible-flexible-closed-surface/results/R16-fixed-cap-volume-moment-noncongruence.md`：固定帽中心三阶矩机制；第 5 节明确重述使用结构和转移余量。
- `topics/visible-flexible-closed-surface/results/R17-exact-finite-visible-closed-geometry.md`：同一公共材料闭图、两帽及三凸起定义。
- `topics/visible-flexible-closed-surface/results/R21-m12-whole-map-and-actual-metric-decrease.md`：具体第一档 critical M12 的全图、曲率、正支撑、握持与三阶矩。
- `topics/visible-flexible-closed-surface/results/R25-m12-sharper-enclosing-ball.md`：同一图的更紧包围球、直径归一化比例。
