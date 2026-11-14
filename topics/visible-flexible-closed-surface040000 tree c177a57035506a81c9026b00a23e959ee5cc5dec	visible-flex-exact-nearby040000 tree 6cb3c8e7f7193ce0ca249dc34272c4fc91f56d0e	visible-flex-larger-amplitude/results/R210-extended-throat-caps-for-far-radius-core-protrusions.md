# R210：延长平接喉部后允许远径核心越过领口平面的完整固定帽

2026-11-13，constructive_geometry。**完整条件定理。**

本文修改 [R204](R204-complete-fixed-caps-for-cuff-height-point-four-to-point-six-three.md) 的真实固定帽，保留其凸体、标记、球包与三个强比例预算。喉的总高度增加准确的 $\Delta=1/50$，实际 cuff 仍位于 $z=\pm Z$，其中 $Z\in[.40,.61]$。相对于 R204，新允许整个原闭核位于 $|z|\le Z+\Delta$；但所有满足 $|z|>Z$ 的原核点必须有柱半径至少 $.514$。后一条件针对**完整超高集合**，不能用一个峰值样本代替。

本稿证明帽自身及帽—核之间的全部双侧法球。原平盘闭核的全局 reach、实际 metric、球包、窄板和 held 排球仍是输入。没有把当前有限拟合场声明为合格，也没有更改正在运行的数值目标。

## 1. 精确几何定义

沿用 R204 的准确有理参数：

$$
B=\frac85,\quad R=\rho=\frac{97}{1000},\quad
a=\frac3{10},\quad a_c=\frac8{25},\quad
\lambda=\frac1{100},\quad
\epsilon=\frac1{10000},\quad\delta=\frac1{1000000},
$$
$$
c=\frac34,\quad b=\frac{1011}{1000},\quad
h=\frac{37}{40},\quad H=\frac{31}{20},\quad
W=\frac{17}{20},\quad A_*=\frac{13}{10},\quad g_*=\frac{16}{25}.
\tag{1}
$$

令 $\eta_\delta$ 为 R111/R168 中已经固定的径向、偶、非负、单位质量光滑核，并定义同一个完整三维凸体

$$
P_0=\operatorname{conv}\{(\pm c,\pm(b-R),h),(0,0,H-R)\},
$$
$$
P=\{d_{P_0}*\eta_\delta\le\epsilon\},\qquad K=P+\overline B_R.
\tag{2}
$$

两组正负号独立。R111 的凸距离证明给 $C^\infty$ 凸体 $K$、准确平底和

$$
P_0+\overline B_R\subset K\subset P_0+\overline B_{R+\epsilon}.
\tag{3}
$$

记

$$
I=\int_0^\pi\sqrt{\sin v}\,dv,\qquad
d_0=2R+\lambda RI,\qquad
z_c=h-\epsilon-3R-\lambda RI,
$$
$$
\Delta=\frac1{50},\qquad L=\frac{8\Delta}{3\pi}.
\tag{4}
$$

因此 $d_0+z_c=h-\epsilon-R$。本文将凸体 $K$ 平移
$(Z+\Delta-z_c)e_z$，记所得凸体为 $K_{Z,\Delta}$。它最低处恰在
$z=Z+d_0+\Delta$。这是 R204 对有效高度 $Z+\Delta$ 放置的原凸体；连接到实际高度 $Z$ 的喉则按下式重新构造。

在整个 $\theta\in[0,\pi]$ 上令

$$
q_\Delta(\theta)
=R\left(1+\frac{\lambda}{\sqrt{\sin\theta}}\right)+L\sin^3\theta
\quad(0<\theta<\pi),
$$
$$
r_\Delta(\theta)
=a-R\sin\theta-2\lambda R\sqrt{\sin\theta}
-\frac L4\sin^4\theta,
$$
$$
z_\Delta(\theta)
=Z+R(1-\cos\theta)
+\lambda R\int_0^\theta\sqrt{\sin v}\,dv
+L\int_0^\theta\sin^4v\,dv.
\tag{5}
$$

旋转参数 $\varphi$ 取完整 $[0,2\pi]$。在开区间，

$$
(r_\Delta',z_\Delta')
=q_\Delta(-\cos\theta,\sin\theta).
\tag{6}
$$

因为 $\int_0^\pi\sin^4v\,dv=3\pi/8$，两端准确为

$$
(r_\Delta(0),z_\Delta(0))=(a,Z),\qquad
(r_\Delta(\pi),z_\Delta(\pi))=(a,Z+d_0+\Delta).
\tag{7}
$$

特别是半径在上端回到原凸帽的接点 $a$，没有把新喉接到另一条未证明的圆上。上端接 $K_{Z,\Delta}$ 的平底，删去其中 $r<a$ 的开盘；下端外接 $a\le r\le a_c$、$z=Z$ 的完整平环。所得上帽为 $C_+$；下帽为关于 $z=0$ 的反射 $C_-$。

这是完整圆盘帽。实际 cuff 是 $r=a_c,z=\pm Z$，不是有效高度 $Z+\Delta$。固定帽被选择后，对全部相位逐材料点不动。

## 2. 两个端口的完整两 jet 与帽自身法球

### 2.1 正则性

$q_\Delta\ge R$，且两端的奇性仍只有原来的可积 $O(\theta^{-1/2})$。若 $\ell$ 为从下端计算的母线弧长，则

$$
\ell=2\lambda R\sqrt\theta+O(\theta),\qquad
\theta=O(\ell^2),\qquad \frac{d\theta}{d\ell}\longrightarrow0.
\tag{8}
$$

新增的 $L\sin^3\theta$ 在这里不改变首项；上端令 $\vartheta=\pi-\theta$ 后相同。母线单位切向连续，二阶弧长导数趋零。因此两个端口都以准确零曲率接平。等价地，端部可写成平面的法向图，其值、一阶和二阶导数与平面完全一致。

$r_\Delta$ 在 $\pi/2$ 取最小值。由 $\pi>8/3$，

$$
\frac L4=\frac{2\Delta}{3\pi}<\frac{\Delta}{4},\qquad
r_{\min}>
a-R(1+2\lambda)-\frac{\Delta}{4}
=\frac{9803}{50000}=.19606>R.
\tag{9}
$$

旋转半径全程正。母线与环向主曲率为
$|{\kappa_m}|=1/q_\Delta$ 和
$|{\kappa_\varphi}|=\sin\theta/r_\Delta$，均不超过 $1/R$，且在两端同时趋零。由旋转参数的直接微分，混合及角向 Cartesian 二导也与平面一致。这支付完整空间两 jet，不只母线位置与法向。

凸体平底盘的余量

$$
\min(c,b-R)-\delta-(a+R)=.352999>0
\tag{10}
$$

保证上端位于真实开平底内。下端 $a_c-a=.02>0$ 是真实开平环，可与原核的开 collar 接合。

### 2.2 完整滚动圆与三维球

把下接平面平移为 $z=0$，并记 $d=d_0+\Delta$。母线是凸图 $r=f(z)$，因为 $dr/dz=-\cot\theta$ 随高度递增。令

$$
X=(r_\Delta,z_\Delta-Z),\quad
T=(-\cos\theta,\sin\theta),\quad N=(\sin\theta,\cos\theta).
$$

对任意 $\theta,\phi\in[0,\pi]$，由 (6)、$q_\Delta\ge R$ 及角差不超过 $\pi$，

$$
(X(\theta)-X(\phi))\cdot N(\phi)
\ge R\{1-\cos(\theta-\phi)\}.
\tag{11}
$$

所以半径 $R$ 的圆盘 $\overline B_R(X+RN)$ 满足凸区
$E=\{0\le z\le d,\ r\ge f(z)\}$ 的每个支持半平面；另一个圆盘
$\overline B_R(X-RN)$ 位于当前支持线的相反侧，不交 $E$ 的内部。这是 [R111 §3](R111-large-fixed-caps-and-reach-preserving-grafting.md) 的完整滚动圆证明，新增项只提高了 $q$。

外球中心的高度满足

$$
z_\Delta-Z+R\cos\theta
=R+\lambda R\int_0^\theta\sqrt{\sin v}\,dv
+L\int_0^\theta\sin^4v\,dv\in[R,d-R].
\tag{12}
$$

故外球不进入下半空间，也不到凸体最低处 $d$。内球中心的柱半径非负，因为 (9)。在任何水平截面，球的最小、最大柱半径由经过球心的母线平面取得；(11) 因此支付旋转后完整三维球的相应侧。

内球伸到 $z>d$ 的部分柱半径不超过 $a+R$、高度不超过 $d+2R$，而

$$
D_{a+R}\times[d,d+2R]\subset K_{Z,\Delta}-Ze_z
\tag{13}
$$

由准确平底及 $K=P+\overline B_R$ 得到。凸体内球仍在凸体内。对凸体外球，R111 的支持平面比较只使用 (13)、$d>2R$ 和喉半径不超过 $a$：若外球不完全高于喉，则其水平球心半径大于 $a+R$，故整个球在 $r>a$ 外侧，不撞喉。下平面、上平底的球由 $\theta=0,\pi$ 的滚动圆及径向平移支付。

因此将 $C_+$ 向外补成整张平面得到的完整非紧曲面具有双侧半径 $R$ 法球。这里使用了全部点对的球，不是由局部曲率界推断 reach。$C_-$ 同理。

## 3. 新的核心输入与全部帽—核双向点对

设 $\Sigma_0$ 是连通、闭、嵌入的 $C^2$ 曲面，含位于 $z=\pm Z$ 的准确闭平盘 $D_{a_c}$，并在外边界有相容开 collar。假设

$$
\operatorname{reach}(\Sigma_0)\ge R,\qquad
|z|\le Z+\Delta\quad\hbox{于整个 }\Sigma_0,
$$
$$
|z|>Z\quad\Longrightarrow\quad
r=\sqrt{x^2+y^2}\ge a_c+2R=\frac{257}{500}=.514.
\tag{14}
$$

删除两个平盘的相对内部并接上 $C_\pm$。证明新闭面全部双侧半径 $R$ 法球。由于原实体不再假定在 $|z|\le Z$ 内，下面不沿用“旧内球留在扩大实体”作为未经证明的捷径，而是直接处理两个球方向。

### 3.1 高于上平面的所有旧点

若旧保留点 $p$ 满足 $p_z>Z$，则其柱半径至少 $a_c+2R$。新上喉和平环的半径最多 $a_c$，故点距至少 $2R$。新凸体点的高度至少 $Z+d_0+\Delta$，而 $p_z\le Z+\Delta$，所以到新凸体的竖直距离至少 $d_0>2R$。

任何距离至少 $2R$ 的点对 $p,q$，对任意两点处的单位法向，均有

$$
|q-(p\pm R\nu_p)|\ge |q-p|-R\ge R,\qquad
|p-(q\pm R\nu_q)|\ge R.
\tag{15}
$$

因此上述比较同时支付以旧点为心向和以新点为心向的两侧法球。它覆盖整个超高集合，并且没有假设其法向朝向。

### 3.2 低于或等于上平面的旧点：旧点的两个球

把上平面设为 $z=0$，取旧保留点 $p_z\le0$。它的任一半径 $R$ 切球中心 $c$ 满足 $c_z\le R$，且该开球避开全部旧平盘。若 $c_z\le-R$，球不进入 $z>0$。当 $-R<c_z<R$ 时，避开旧平盘意味着

$$
|c_{xy}|\ge a_c+\sqrt{R^2-c_z^2}.
\tag{16}
$$

当 $c_z=R$，等式只能由 $p_z=0$ 且球心方向为 $+e_z$ 达到。因 $p$ 是保留点，其柱半径不小于 $a_c$，故仍有 (16) 的端点形式。这个推理对旧内球、外球都适用，只用全局 reach 和平盘，没有用旧实体的 slab 包含。

令 $h_R(w)=\sqrt{R^2-w^2}$。在球与 $0\le y=z\le2R$ 相交的每层，所有球内点的柱半径至少为

$$
a_c+h_R(c_z)-h_R(y-c_z)
\ge a_c-\sqrt{2Ry-y^2}.
\tag{17}
$$

最后一步由 $h_R$ 的凹性得到：固定 $y\ge0$，两项之差在共同定义域随 $c_z$ 不增，最小值在 $c_z=R$。母线下接点的外切圆属于 $E$，故

$$
f(y)\le a-\sqrt{2Ry-y^2}\qquad(0\le y\le2R).
\tag{18}
$$

$a_c>a$ 使 (17) 严格在新喉之外；新凸体开始于 $d>2R$，旧球到不了。平环原本就是旧平盘的一部分，所以也不在旧开切球内。于是**旧点的两侧球**均不碰新帽。

### 3.3 新帽的两个球：低于平面的旧点

新喉外球由 (12) 完全处于 $z\ge0$，开球不含 $z\le0$ 的旧点。凸体内球处于凸体内；其外球球心高度至少 $d-R$，最低高度至少 $d-2R>0$。只须处理新喉向下伸出的内球。

将其球心写成 $(c_r,c_z)=(a-u,-R+v)$。由 (5)，

$$
u=2R\sin\theta+2\lambda R\sqrt{\sin\theta}
+\frac L4\sin^4\theta\ge0,
$$
$$
v=2R(1-\cos\theta)+\lambda R\int_0^\theta\sqrt{\sin t}\,dt
+L\int_0^\theta\sin^4t\,dt\ge0.
\tag{19}
$$

$c_r\ge0$ 已由 (9) 支付。滚动圆不包含下接点 $(a,0)$，因此当 $0\le v\le2R$，

$$
u\ge\sqrt{2Rv-v^2}.
\tag{20}
$$

对该球任何 $z\le0$ 截面，写 $w=z+R$。凹性给

$$
h_R(w-v)-h_R(w)
\le h_R(R-v)-h_R(R)
=\sqrt{2Rv-v^2}\le u.
$$

故这个球在下平面以下的截面完全包含于

$$
r<a_c+h_R(z+R),\qquad -2R<z<0.
\tag{21}
$$

(21) 是所有旧平盘点向下的开半径 $R$ 切球的并；这些球因原全局 reach 均避开旧曲面，不管哪个方向叫作实体内侧。于是新内球不会碰任何低于平面的旧点。在 $z=0$，同一估计给球截面的最外半径不超过 $a<a_c$，也不会碰保留的旧点。当 $v>2R$ 时新球已经全在 $z>0$，端点由开球和连续性处理。新平环的向下球本身就是旧平盘的球，向上球不碰低点。

这正是 [R113 §1](R113-thin-cuff-grafting-and-elliptic-core-window.md) 的凹截面比较；新增项在 (19) 中均非负，且下接点的滚动圆证明仍成立。没有添加 $a+R\le a_c$ 或平坦半径 $.514$ 的条件。

### 3.4 反射、嵌入与全局 reach

对下帽反射 §§3.1–3.3。上下新帽间距至少 $2Z\ge.8>2R$。原保留核内部点对来自原 reach；同一个新帽内部来自 §2；全部双向帽—核点对及跨帽点对已全部覆盖。

新帽与旧保留核也没有额外交点：超高点由 §3.1 分离，低点与新帽只可能在规定的平圈及其共同平面部分接合。新的两端开平环与旧 collar 两 jet 相同，因此新面闭、嵌入、$C^2$，以圆盘替换圆盘保持连接性和拓扑。

所有点对满足

$$
|n(p)\cdot(q-p)|\le \frac{|p-q|^2}{2R}.
\tag{22}
$$

若 $x=p+t n(p)$、$|t|<R$，则 $q\ne p$ 时

$$
|x-q|^2\ge t^2+(1-|t|/R)|p-q|^2>t^2.
$$

最近点必在法线上，所以距离小于 $R$ 的点具有唯一最近点。新完整闭面的全局 reach 至少 $R$。这是双侧法球的全点对结论。

## 4. 全部有理参数预算

对 $\Delta=.02$、$Z\in[.40,.61]$，有效高度
$Z+\Delta\in[.42,.63]$。解析界 $2<I<22/7$ 给

$$
z_c>\frac{110399}{175000},\qquad
z_c-(Z+\Delta)>\frac{149}{175000}>0.
\tag{23}
$$

因此凸体仅从参考位置向内平移，所有正高度都减小。由 (3)，完整凸体球包的准确余量是

$$
(B-R-\epsilon)^2-c^2-(b-R)^2-h^2
=\frac{518741}{10^8}>0,\qquad
B-H-\epsilon=\frac{499}{10000}>0.
\tag{24}
$$

新喉和平环满足 $r\le a_c$，且其最高处不超过参考凸体最低高度
$h-\epsilon-R=.8279$。于是

$$
B^2-a_c^2-(h-\epsilon-R)^2
=\frac{177218159}{10^8}>0.
\tag{25}
$$

整个帽在 $B_{1.6}(0)$ 内。帽的完整 $x$ 半宽仍不超过

$$
c+R+\epsilon=.8471<W,\qquad W-(c+R+\epsilon)=.0029.
\tag{26}
$$

新喉比旧喉更细，故不增加该半宽。

其余法球数值余量为

$$
r_{\min}-R>\frac{4953}{50000}=.09906,\qquad
a_c-a=.02,\qquad
d_0-2R>\frac{97}{50000}=.00194,
$$
$$
2Z-2R\ge.606,\qquad
(a_c+2R)-a_c=2R.
\tag{27}
$$

最后一项允许等号，因为证明使用开切球；实际消费可选更大的径向阈值保留区间余量。

## 5. 真实标记、held 与全部强比例

凸体没有变形，只作有效高度 $Z+\Delta$ 的原平移。支持射线仍给八个距
$(\pm c,\pm b,\pm h_{Z,\Delta})$ 不超过 $\epsilon$ 的真实点，以及两个距
$(0,0,\pm H_{Z,\Delta})$ 不超过 $\epsilon$ 的真实点，其中

$$
h_{Z,\Delta}=Z+\Delta+\epsilon+3R+\lambda RI,\qquad
H_{Z,\Delta}=H-h+h_{Z,\Delta}.
\tag{28}
$$

它们远离被删的底孔。准确下界为

$$
h_{Z,\Delta}>\frac{8913}{12500}=.71304,\qquad
H_{Z,\Delta}>\frac{33451}{25000}=1.33804.
\tag{29}
$$

它们均比 R204 完整八极点证明使用的 $.69304$ 和 $1.31804$ 高 $.02$。对独立反射的角标记，支持函数的这两个系数只增加，因此 R204 的完整极体顶点枚举仍给：加上准确中央点 $(\pm A_q,0,0)$、$A_q\ge1.30$，理想十二点凸包含 $B_b$；标记误差后实际初态凸包含 $B_{b-\epsilon}$。

若相位零整个活动核满足 $|y|\le W$，其 $\pi/2$ 旋转像位于 $|x|\le W$，固定帽由 (26) 也在该窄板。任意含反射的刚体运动将此窄板搬成同宽窄板。完整无标签像集的 Hausdorff 距离因此至少

$$
\delta_E\ge b-\epsilon-W=.1609.
\tag{30}
$$

held 的见证仍取 $p=(0,A_q,0)$。新喉和平环的水平距离至少 $A_q-a_c\ge.98$，平方余量为

$$
(.98)^2-(.64)^2=.5508>0.
$$

凸帽点有 $y\le b+\epsilon$ 及 $|z|\ge Z+d_0+\Delta>Z+2R+\Delta$，故全部凸帽点的 held 距离平方余量至少

$$
(.2889)^2+(.614)^2-(.64)^2
=\frac{5085921}{10^8}>0.
\tag{31}
$$

若原相位零**整个核心**已排除 $B_{.64}(p)$，新帽不会破坏排球。中央长轴点在 $\pi/2$ 相位到达 $p$，故 $\delta_{\rm hold}\ge.64$。固定握持集合取两片完整帽，其相对内部非空，真实轴向标记间距大于
$2(1.33804)-2\epsilon=2.67588>.64$。

综合球包、§3 的全局 reach、(30) 和 whole-core held 输入，得到

$$
\boxed{
D\le\frac{16}{5},\qquad
\frac{\delta_{\rm hold}}D\ge\frac15,\qquad
\frac{\delta_E}D\ge\frac{1609}{32000}>\frac1{20},\qquad
\frac{\operatorname{reach}}D\ge\frac{97}{3200}>\frac3{100}.
}
\tag{32}
$$

## 6. 完整相位族定理与适用边界

在 §3 的核条件之外，要求整个原核位于 $B_{1.6}(0)$，相位零全活动核位于 $|y|\le.85$，准确中央支持 $A_q\ge1.30$，并支付 §5 的 whole-core 排球。取与原中央及尾一致的单一轴对称材料度量，准确平 collar 两 jet 固定，原族为 R199 的 $R_\alpha Y(s,u-\alpha)$。

(14)、球包和 reach 对绕轴旋转不变，所以同一个固定帽适用于全部相位。新帽上取其固定诱导度量，平 collar 使它和原核度量准确拼接；得到共同度量的 $C^2$ 闭族，并有 (32)。数值消费时仍须给原核实际全域误差及同一几何的加密证据。

这是一个新的完整帽设计。不能把旧 R204 的帽保持不动而只删掉其高度罚项。本定理也没有把核心 reach 由帽补付；尤其前缀—尾、前缀—补盘、上下活动片以及任何其他原核点对仍属于原核 reach 输入。

在已闭 R205 消费域 $0\le A_{\rm tail}\le1.2$、$Z\ge.40$ 内，弯环的下降不超过 $.23A_{\rm tail}\le.276$，连同平盘本来位于 $|z|\le Z$；故新增远径条件只可能约束超高的前缀部分。其准确平 collar 只需到 $.34$，并不需要平到 $.514$；$.514$ 在本文是**所有超高点的径向分离阈值**，角色不同。

下一实际消费应检查一个明确完整字段上 (14) 的全部点，而不是只读最大高度见证。现有若干有限态约 $.015$ 的越高量只说明本窗口可能有用，不支付 (14)、global reach 或任何完成标准。

## 7. 准确标量消费者

[scripts/fd2d-extended-throat-cap-budget-R210.cjs](../scripts/fd2d-extended-throat-cap-budget-R210.cjs) 通过显式参数接入未改的 R199/R204 有理消费者，核 (9)、(10)、(23)–(31) 与全部比例。它只使用 BigInt 有理数以及本稿明确证明的 $I,\pi$ 界，不作几何采样。

本次纯 V8 实际执行完成，完整有理报告另存；没有 OS 进程、OS exit、F/J、normal、LM 或 whole-body 求值。正的标量预算是上述条件定理的一部分，不是某个有限核心已通过的声明。
