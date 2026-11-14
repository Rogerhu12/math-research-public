# R111：强幅度标记的完整固定帽与保持 reach 的真实拼接

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

**状态：本文全部构造与注明输入的拼接定理已证明。**
本文实际接成 R107 的固定帽，给出同一个 C² 帽的全部空间范围、六个标记、真实两 jet、平面补全的 reach，以及与已有平圆盘活动核拼接的跨片 reach。
它不再只用相离圆顶或 C¹,¹ 胶囊代替帽。
**尚未得到所需的短 n2 活动核；所以本文不是本课题的完成解。**
当前 flat17 原 g 的数值加密不改变。本构造是另一新几何的固定部分。

## 1. 明确参数与一个完整光滑凸体

以下长度均使用 R100 的中央圈周长 $2\pi$ 归一。
取准确有理数

$$
R=\frac1{10},\quad \lambda=\frac1{40},\quad
a=\frac{11}{50},\quad a_c=\frac8{25},\quad
\epsilon=10^{-4},\quad \delta=10^{-6},\quad A=\frac{21}{50}+2\delta,
\tag{1}
$$

$$
h=\frac{89}{125},\quad L=\frac{573}{500},\quad
Z=\frac{1349}{1000},\quad b=L+R=\frac{623}{500},\quad H=Z+R=\frac{1449}{1000}.
\tag{2}
$$

令 $P_0$ 为下面七个点的凸包：

$$
(\pm A,\pm A,h),\qquad (0,\pm L,h),\qquad (0,0,Z).
\tag{3}
$$

四个双符号点独立取号。底面为平面 $z=h$ 中的一个六边形，包含闭圆盘 $D_A$；顶点在 $z=Z>h$，所以 $P_0$ 有内点。
这已经是有限显式的凸多面体。

选定标准径向偶核

$$
\eta(u)=c\exp\!\left(-\frac1{1-|u|^2}\right)\boldsymbol1_{|u|<1},
\qquad \int_{\mathbb R^3}\eta=1,
$$

并令 $\eta_\delta(u)=\delta^{-3}\eta(u/\delta)$。写 $d_0(x)=\operatorname{dist}(x,P_0)$，定义

$$
f(x)=(d_0*\eta_\delta)(x),\qquad P=\{f\le\epsilon\},\qquad K=P+\overline B_R.
\tag{4}
$$

这些是有限维凸距离、一个明确紧支撑积分和一个固定平行体，不涉及非线性 PDE 或无限层极限。

### 引理 1：$P$ 和 $K$ 的准确正则性

$P$ 是有内点的紧凸体，边界为 $C^\infty$；且

$$
P_0\subset P\subset P_0+\overline B_\epsilon.
\tag{5}
$$

其最低平面为 $z=h-\epsilon$，这个平面中的底面包含 $D_{A-\delta}$。
$K$ 也是 $C^\infty$ 凸体；其最低平面

$$z=z_0:=h-\epsilon-R=\frac{6119}{10000}$$

的底面包含同一个 $D_{A-\delta}$。$K$ 的每个边界点均有半径 $R$ 的内切球，外侧任意半径的切球不进入 $K$。

**证明。** 到凸集的距离是凸函数。与非负核卷积后仍凸且为 $C^\infty$；$d_0$ 的 1-Lipschitz 性、核支撑及 Jensen 不等式给

$$d_0(x)\le f(x)\le d_0(x)+\delta.$$

因 $\delta<\epsilon$，得 (5) 和紧性、有内点。
若 $f(x)=\epsilon$，取 $q\in P_0$，则 $f(q)\le\delta$，凸性给

$$\nabla f(x)\cdot(x-q)\ge f(x)-f(q)\ge\epsilon-\delta>0.$$

所以这个水平集的梯度处处非零，边界光滑。
在 $z=h-\epsilon$、$|(x,y)|\le A-\delta$ 处，卷积核范围内的全部点都在 $P_0$ 底面的正下方，投影仍落在底面；在那里 $d_0=h-z$。核的均值为零，故卷积也恰为 $h-z$。
又 $d_0(x)\ge h-z$，所以整个 $P$ 都在 $z\ge h-\epsilon$ 内。这证明准确平底，不是小误差平底。

对光滑凸体 $P$，法向平移 $p\mapsto p+Rn(p)$ 给 $\partial K$。
凸性使所有主曲率非负，平移的切向微分为 $I+RS$，处处可逆；唯一最近点投影使它全局一一。因此 $K$ 边界 $C^\infty$。
在 $p+Rn(p)$，球 $\overline B_R(p)$ 包含于 $K$，并在该点相切。外切球位于凸体支持平面的外侧。
平底的位置和盘由同一平移直接得到。证毕。

本文后续只需下列保守事实：

$$D_{a+R}\times\{z_0+R\}\subset P,
\qquad D_{a+R}\times[z_0,z_0+2R]\subset K.
\tag{6}
$$

因为 $A-\delta=.420001>a+R=.32$，(6) 已由引理 1 支付。

## 2. 从平 cuff 接到凸体底面的真实 C² 喉

令

$$
q(\theta)=R\left(1+\frac{\lambda}{\sqrt{\sin\theta}}\right),\quad
d=\int_0^\pi q(\theta)\sin\theta\,d\theta
=2R+\lambda R\int_0^\pi\sqrt{\sin\theta}\,d\theta,
\quad z_c=z_0-d.
\tag{7}
$$

对 $0\le\theta\le\pi$ 定义母线

$$
\begin{aligned}
r(\theta)&=a-R\sin\theta-2\lambda R\sqrt{\sin\theta},\\
z(\theta)&=z_c+R(1-\cos\theta)
+\lambda R\int_0^\theta\sqrt{\sin u}\,du.
\end{aligned}
\tag{8}
$$

在开区间，$(r',z')=q(-\cos\theta,\sin\theta)$。
旋转 (8) 得一个嵌入环带，底圈 $(r,z)=(a,z_c)$，顶圈 $(a,z_0)$；中央最细处为

$$r_{\min}=a-R(1+2\lambda)=\frac{23}{200}=.115>R.$$

将它的底圈外接到 $z=z_c$ 的平面，顶圈外接到 $K$ 的平底（删去该平底内 $r<a$ 的盘）。再在底部保留完整平环 $a\le r\le a_c$。
得到一个边界为 $r=a_c,z=z_c$ 的真正嵌入圆盘帽 $C_+$。
它在外边界附近有宽 $.10$ 的开平环。

### 引理 2：没有隐藏的球柱折缝

$C_+$ 为 $C^2$。以母线弧长参数计，两个主曲率绝对值为

$$|\kappa_m|=q(\theta)^{-1}\le R^{-1},\qquad
|\kappa_\varphi|=\frac{\sin\theta}{r(\theta)}<R^{-1}.$$

在两个端圈，两主曲率都趋零，完整 Cartesian 两 jet 与相接平面一致。

**证明。** 令弧长 $s=\int q(\theta)d\theta$。两端 $q$ 虽发散，但仅为可积的 $O(\theta^{-1/2})$；故弧长有限。
在底端 $s=2\lambda R\sqrt\theta+O(\theta)$，所以 $\theta=O(s^2)$，切向角为 C¹ 且 $d\theta/ds\to0$。
顶端由对称性相同。母线的一阶导连续且单位长，二阶导趋零，正好能 C² 接平线。
旋转半径始终正，角向和混合导数也连续；端点 $\sin\theta=0$ 使环向曲率趋零。
公式即由旋转面第一、二基本形式得到。因 $r\ge.115>.1=R$，环向界成立。
上端在 $K$ 的真实开平底中，故这里也没有曲率跳跃。证毕。

下面只用有理范围，不依赖求积小数：$2\le\int_0^\pi\sqrt{\sin\theta}\,d\theta<22/7$，所以

$$
.205\le d<\frac{291}{1400},\qquad
.404<z_c<.407,\qquad d>2R.
\tag{9}
$$

数值读数为 $d\approx.205990701173678$、$z_c\approx.405909298826322$。

## 3. 平面补全帽的全局 reach

将 $C_+$ 的边界外接整张平面 $z=z_c,r\ge a_c$，记非紧曲面为 $\widehat C_+$。
其内侧实体是下半空间、喉内侧及 $K$ 的并。

### 引理 3：二维转弯的完整滚动圆

将高度平移为 $z_c=0$。母线 (8) 在 $0<z<d$ 是凸函数 $r=f_*(z)$ 的图。
令

$$X(\theta)=(r(\theta),z(\theta)),\quad
T=(-\cos\theta,\sin\theta),\quad N=(\sin\theta,\cos\theta).$$

平面凸集 $E=\{0\le z\le d, r\ge f_*(z)\}$ 在 $X(\theta)$ 的内法向是 $N$。
圆盘 $\overline B_R(X+RN)$ 包含于 $E$；圆盘 $\overline B_R(X-RN)$ 不交 $E$ 的内部。

**证明。** $dr/dz=-\cot\theta$ 随 $z$ 递增，所以 $f_*$ 凸。
它连同两条水平边界射线的所有支持半平面是
$N(\phi)\cdot(Y-X(\phi))\ge0$，$0\le\phi\le\pi$。
对任意 $\theta,\phi$，由 $q\ge R$ 和两角差不超过 $\pi$，直接积分得

$$
(X(\theta)-X(\phi))\cdot N(\phi)
\ge R\{1-\cos(\theta-\phi)\}.
$$

因此 $N(\phi)\cdot(X(\theta)+RN(\theta)-X(\phi))\ge R$；半径 R 圆盘满足全部支持不等式。
另一个圆盘位于当前支持线的相反闭半平面，故不交凸集内部。证毕。

### 命题 4

$$\boxed{\operatorname{reach}(\widehat C_+)\ge R=.1.}\tag{10}$$

**证明。** 给每个边界点明确的内外切球。

喉上外球中心为 $(r+R\sin\theta)e_\varphi+(z+R\cos\theta)e_z$。
引理 3 保证它在二维中落于 $E$；旋转后的球在同一高度的最小柱半径由经过球心的母线截面取得，故整个三维球都在喉外侧。
此外
$R\le z+R\cos\theta\le d-R$，所以外球不进入下半空间或位于 $z\ge d$ 的 $K$。

喉上内球中心为 $(r-R\sin\theta)e_\varphi+(z-R\cos\theta)e_z$，其柱半径非负，因为 $r_{\min}>R$。
同一高度的最大柱半径也在球心母线平面取得；引理 3 使位于 $0\le z\le d$ 的部分留在喉内。
球在 $z<0$ 的部分属于下半空间；在 $z>d$ 的部分满足柱半径 $\le a+R$、高度 $\le d+2R$，故由 (6) 属于 $K$。

下平面所有点的内球显然在下半空间；外球在接点的外球基础上向径向外侧平移，仍在 $E$ 或在喉、$K$ 外。上平底 $r\ge a$ 的外球同理，使用引理 3 的 $\theta=\pi$ 端点；内球在 $K$ 中。

最后看 $K$ 的其余边界点 $p$，外法向为 $n$。内球已由引理 1 给出。
外球中心 $c=p+Rn$ 在凸体外，且 $c_z\ge d-R\ge R$，所以球不进下半空间。
若 $c_z\ge d+R$，它也在喉上方。否则设 $s=|n_{xy}|$。
当 $s>0$，用 $K$ 包含 $D_{a+R}\times\{d+R\}+\overline B_R$ 的支持不等式，得

$$
p_{xy}\cdot\frac{n_{xy}}s
\ge a+R+\frac{(d+R-p_z)n_z+R}{s}.
\tag{11}
$$

若 $n_z<0$，因 $p_z\ge d$，最后的分子至少 $R(1+n_z)>0$；若 $n_z\ge0$，由 $p_z+Rn_z<d+R$，分子也为正。
故 $|c_{xy}|>a+R$，整个外球留在柱半径 $>a$，不进喉。
$s=0,n_z=1$ 属于上方情形；$s=0,n_z=-1$ 正是已经处理的平底。
于是每一点都有不碰另一边界点内侧的半径 R 双侧切球。

这些球对任意两点 $x,y\in\widehat C_+$ 给

$$|n(x)\cdot(y-x)|\le\frac{|x-y|^2}{2R}.$$

若 $p=x+t n(x)$、$|t|<R$，则对 $y\ne x$，

$$|p-y|^2\ge t^2+(1-|t|/R)|x-y|^2>t^2.$$

最近点必在法线上，所以距离小于 R 的点有唯一最近点。这就是 (10)，包含非局部点对。证毕。

## 4. 帽的全部范围和真实标记

所有 $K$ 中点由 (5) 满足 $K\subset P_0+\overline B_{R+\epsilon}$。
七个顶点中最大模长在两个侧顶点或顶点处；以下准确数检验侧顶点的球余量：

$$
\left(\frac{29}{20}-R-\epsilon\right)^2-L^2-h^2
=\frac{197001}{10^8}>0.
\tag{12}
$$

顶点 $Z+R+\epsilon=1.4491<1.45$，方形角点更在球内。
因此整个 $K\subset B_{29/20}$。喉及平环位于 $r\le.32$、$.404<z\le.6119$，也在这个球内。
另外

$$C_+\subset\{|x|\le A+R+\epsilon=.520102<3/4\}.$$

$P_0+\overline B_R$ 包含 $(0,\pm b,h)$ 和 $(0,0,H)$，且它们是各自 $\pm e_y,e_z$ 支持方向上的边界点。
沿相应支持法线射线，$K$ 的边界必在距离不超过 $\epsilon$ 处：内包含给射线的内端，$K\subset P_0+\overline B_{R+\epsilon}$ 给外端。
故 $C_+$ 真正包含这三个目标点的 $10^{-4}$ 近点。
它们远离被删的底盘，因此都仍在帽上。

取关于 $z=0$ 的反射帽 $C_-$，得到 R107 §5.1 所需六个固定标记，误差比其 $10^{-3}$ 输入更小。
两个帽的轴向标记距离至少 $2H=2.898$。

最后，帽在 $|z|\le3/5$ 的全部点只能来自喉/平环，均有 $|y|\le.32$。
所以帽完整满足 R100 的握持保护条件

$$y\le\frac7{10}+\frac56z^2\qquad(|z|\le3/5).\tag{13}$$

不是只核对六个标记点。

## 5. 同实际活动闭核拼接时的跨片 reach

下面不把平面补全 reach 直接转授闭面；另证明跨片球不相交。

### 定理 5：真实 grafting

设 $\Sigma_A$ 是闭 C² 嵌入曲面，其有界内侧 $\Omega_A$ 包含于 $|z|\le z_c$，且

$$\operatorname{reach}(\Sigma_A)\ge\rho:=9/100.$$

假设在两平面 $z=\pm z_c$ 上，$\Sigma_A$ 各含一个半径 $a_c=.32$ 的真实平圆盘，并在其外边界保持 C²。
将两个盘换成 $C_\pm$，得到 $\Sigma$。则

$$\boxed{\operatorname{reach}(\Sigma)\ge\rho=.09.}\tag{14}$$

新曲面仍闭、嵌入、C²；更换的都是拓扑圆盘，所以连通性和亏格保持。

**证明。** 新实体是 $\Omega_A$ 与上下两个喉内体及凸体的并；新部分分别在 slab 的上、下方。
外边界宽 $.10$ 的平环使空间两 jet 直接一致。
沿平盘外法线的旧内切 $\rho$ 球给

$$D_{a_c}\times[z_c-2\rho,z_c]\subset\overline\Omega_A.$$

因为每个水平点均可作为球心的水平坐标。上帽喉的内切 $\rho$ 球若有部分落在 $z<z_c$，那部分的柱半径至多
$a+\rho=.31<a_c$，最低高度至少 $z_c-2\rho$，因此已在旧实体内。
它在 slab 上方的部分按命题 4 的相同证明位于喉或 $K$ 中；这里 $q\ge R>\rho$，且 (6) 对较小半径仍充分。
新帽外切 $\rho$ 球的最低高度至少 $z_c$，所以不进入旧实体。
凸体上的内球留在凸体内。下帽由反射得到同样结论，且两帽相距超过 $.8>2\rho$。

旧保留曲面点的内球留在 $\Omega_A$，只须排除其外球碰到新帽。
对上帽，把 $z_c$ 平移到零，令这个旧外球中心为 $c$，则 $c_z\le\rho$。
凸体最低高度 $d>2R>2\rho$，所以外球不会碰凸体。
若 $c_z\le-\rho$，球也不会进入上半空间；只剩 $-\rho<c_z\le\rho$。
旧外球不能进入旧平盘，故当 $|c_z|<\rho$ 时必有

$$|c_{xy}|\ge a_c+\sqrt{\rho^2-c_z^2}.\tag{15}$$

$c_z=\rho$ 时，若柱半径小于 $a_c$，球与旧 slab 的唯一可能切点就在被删盘内部，不能是保留点；所以这一端点也有相应的界。
在高度 $0\le z\le2\rho$，该球任何点的柱半径至少

$$a_c+\sqrt{\rho^2-c_z^2}-\sqrt{\rho^2-(z-c_z)^2}
\ge a_c-\sqrt{2\rho z-z^2}.\tag{16}$$

最后一个不等式来自凹函数 $u\mapsto\sqrt{\rho^2-u^2}$：固定 $z\ge0$，两值的差随 $c_z$ 递减，最小值在 $c_z=\rho$。
无实根的高度不与球相交。
另一方面，引理 3 用半径 $\rho$ 的底端外圆给

$$f_*(z)\le a-\sqrt{2\rho z-z^2}\qquad(0\le z\le2\rho).$$

因 $a_c>a$，(16) 严格在喉外。更高部分不在这个旧外球内。
这排除全部旧片—新喉、新凸体点对；不是有限云检查。
对下帽反射同证。故新闭面仍有双侧 $\rho$ 滚动球，命题 4 末尾的弦不等式即给 (14)。证毕。

## 6. 可组合为两个强幅度目标的完整条件定理

现设同一个活动闭核有一族 $\Sigma_{A,\alpha}$，满足定理 5 全部条件和以下输入：

1. 参数为同一个闭曲面，族在 C² 中连续，全部对共同 g 等距；两平盘逐材料点固定。
2. 删去两平盘后的活动像集为 $R_\alpha A$，相位含 $\alpha=\pi/2$。
3. $A$ 含 R100 的准确 $q=.3$ 中央支撑核；$A\subset B_{29/20}\cap\{|y|\le3/4\}$。
4. 初始活动部分在 $|z|\le3/5$ 上满足 (13)。

把两个平盘替换为本文的固定 $C_\pm$，在帽上取固定诱导度量。
平环使新目标 g 与旧活动 g 在接合处一致；所有相位逐点固定平环、整帽，因而等距性和 C² 连续性直接保持。
定理 5 给全部时间的嵌入性和 reach，不需要时间采样。
全图都在 $B_{29/20}$，所以 $D\le2.9$。
R100 命题 2、本文 (13) 给 $\delta_{hold}\ge.6$；R107 §5.1 的八点内球—窄板论证应用于实际六个帽标记，给 $\delta_E/D>37/725$，包含反射。
因此

$$
\boxed{
\frac{\delta_{hold}}D\ge\frac6{29}>.2,\qquad
\frac{\delta_E}D>\frac{37}{725}>.05,\qquad
\frac{\operatorname{reach}}D\ge\frac9{290}>.03.
}
\tag{17}
$$

握持区取两个完整帽，具有相对曲面的非空内部，直径至少 $2.898>.2D$。
它们虽不连通，仍符合本题 README。

**真实剩余缺口。** 本文没有构造以上活动核：尤其需要它在高度
$|z|\le z_c\approx.4059093$ 内由 n2 中央圈接到半径 $.32$ 的平盘，并有全时 reach $.09$、共同 g 和真实数值加密。
旧 flat17 的帽高度约 $1.8$，不能剪去高度或做轴向压缩后引用本定理。
R100 的线性深尾也不支付这个非线性短核。
不过，一旦获得这样的核，固定大帽本身及全部跨片 reach 已在这里接清，无须再把 R107 的分离圆顶当作未知连接。

## 7. 复现

脚本 `scripts/fd2d_large_fixed_caps.py` 固定全部有理参数，输出公式 (7) 的求积读数、准确有理范围/球余量与明确的未完成标签。
可选网格使用 $(P_0+B_R)-\epsilon e_z$ 作为 $K$ 的参考凸体，与准确光滑 $K$ 的 Hausdorff 距离不超过 $2\epsilon$；喉和开平环使用 (8) 的同一公式。
该三角网格仅为本固定帽的展示/装配输入，另有离散网格误差；不是完整活动闭面，也不将三角面叫作 C² 曲面。
真正 C² 帽是 (4)、(8) 的固定几何，其存在、所有比例窗和 reach 不依赖网格试验。

## 8. 允许更高活动核的第二个完整帽

还有一个实用的改进：保持中央核 $q=.3$、完整活动半宽 $.75$、内喉半径 $.22$、cuff 半径 $.32$、$A,\epsilon,\delta$，改取

$$
R=\rho=\frac{91}{1000},\quad\lambda=\frac1{100},\quad
b=\frac54,\quad h=\frac45,\quad H=\frac{1499}{1000},\quad
L=b-R=\frac{1159}{1000},\quad Z=H-R=\frac{176}{125}.
\tag{18}
$$

此时目标球半径为 $3/2$，所以整图直径上界放宽为 $D\le3$。
这恰好仍保住强握持目标 $.6/D\ge.2$，并非放宽本题条件。
用同一个 (3)–(8) 重建完整帽。
喉最细半径为 $.12718>R$；$a+\rho=.311<a_c$；凸体底面的半径余量也保留。
所以 §§1–5 的全部 C²、双侧滚动球及真实 grafting 证明原样适用。

所有尺寸用准确数支付：

$$
\left(\frac32-R-\epsilon\right)^2-L^2-h^2
=\frac{171821}{10^8}>0,\qquad
H+\epsilon=1.4991<1.5,
$$

$$
H^2-(H-h)^2-b^2=\frac{1959}{10000}>0.
\tag{19}
$$

第一行把整个凸体放进 $B_{3/2}$；方形角点与喉的球界有更大余量。
第二行正是 R107 六边形包含半径 b 平面圆盘的条件。
两活动轴点仍在 $\pm13/10$，所以八点凸包的内球半径 r 满足

$$
r^2=\frac{4225}{5204},\qquad
r^2-\left(\frac{901}{1000}\right)^2=\frac{96899}{1301000000}>0.
\tag{20}
$$

真实六个固定标记误差仍不超过 $10^{-4}$。另一相位完整半宽仍为 $.75$，因此不必把误差放宽到 R107 的 $10^{-3}$：

$$
\delta_E\ge r-10^{-4}-.75>.1509,\qquad
\frac{\delta_E}D>\frac{503}{10000}=.0503.
\tag{21}
$$

新凸体最低高度 $.7089>.6$，喉在低高度部分仍有 $|y|\le.32$，所以整个帽仍支付 (13)。
其平 cuff 高度现为

$$
z_c=.7089-\left(.182+.00091\int_0^\pi\sqrt{\sin\theta}\,d\theta\right)
\approx .5247193847727811.
\tag{22}
$$

活动核允许高度比第一方案增加约 $.11881$，且完整活动半宽要求没有收紧。
若实际活动核在这个 slab 内满足 §6 的其余输入并有 reach $\ge.091$，则相同真实拼接给

$$
\boxed{
\delta_{hold}/D\ge1/5,\quad
\delta_E/D>503/10000,\quad
\operatorname{reach}/D\ge91/3000>3/100.
}
\tag{23}
$$

脚本选项 `--variant diameter3` 生成这一套明确参数和参考帽网格。
第二方案仍缺自己的短非线性活动核；不是现有 fixed-g 图的精修，也不把任一旧图高度改成 (22)。

## 9. 可选的 C∞ 平接公式

固定帽还可直接升级为 C∞，不需新增求解或网格检查。保持任一上述参数，把 (7) 的曲率半径改为

$$q_\infty(\theta)=R\left(1+\frac{\lambda}{\sin\theta\,(1-\log\sin\theta)^2}\right).$$

它在两端可积、处处不小于 R。对应的母线是

$$
r_\infty(\theta)=a-R\sin\theta-\frac{R\lambda}{1-\log\sin\theta},
$$

$$
z_\infty(\theta)=z_{c,\infty}+R(1-\cos\theta)
+R\lambda\int_0^\theta\frac{du}{(1-\log\sin u)^2},
$$

其中 $z_{c,\infty}$ 选择成使顶端仍位于同一个 $z_0$。
在底端用 $v=(1-\log\sin\theta)^{-1}$ 作参数，
$\sin\theta=e^{1-1/v}$ 在 $v=0$ 的全部阶导数为零；
$r_\infty=a-R\lambda v$ 加一个平坦函数，所以 $dr_\infty/dv\to-R\lambda\ne0$。
而

$$
\frac{dz_\infty}{dv}
=\frac{R\sin^2\theta}{v^2\cos\theta}
+\frac{R\lambda\sin\theta}{\cos\theta}
$$

也在 $v=0$ 平坦。因此 $z_\infty$ 是 $r_\infty$ 的 C∞ 函数，并以所有阶导数零接到平面；顶端由反射相同。
中间原 θ 参数正则。最细半径改为 $a-R(1+\lambda)>R$，所以全部双侧滚动球和嫁接证明仍成立。
高度增量在 $2R$ 与 $2R+\pi R\lambda$ 之间；空间球/板/标记和强幅度预算保持，但活动核应使用这一次新算出的 cuff 高度。
本节不改变脚本默认的 C² profile，也不将这个不同帽参数称作当前主线的同 g 加密。
