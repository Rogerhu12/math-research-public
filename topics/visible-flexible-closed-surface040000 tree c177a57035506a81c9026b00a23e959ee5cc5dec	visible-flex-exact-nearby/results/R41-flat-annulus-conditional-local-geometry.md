# R41：固定水平平环的条件局部几何

状态：**已证明，全文独立审查通过。** 作者 `/root/independent_geometry_continued`；独审 `/root/tail_review_continued`；root于2026-11-09全文读取原证明与独审后正式采纳。

只支付指定分离保留片的共同包围、径向必要条件、全角两点核及所有保留片法向点对半径383/5000。未解达到指定高度的共同度量连接，未知片不在量词内。 本结论不支付G5。

原证明 [冻结稿](../notes/2026-11-09-db6f-audit-flat058-geometric-template.md)，SHA256 `f962bee606ba0a2cc03b08bb9e4669bf43056dfd6f983cfa24d6c3d990a7c805`；[独立全文审稿](../notes/2026-11-09-db6f-tail-review-flat058-geometric-template.md)，SHA256 `16d0eb80746246c5bf84a33326055705931f7248e55cf82342927a0c2ab2dd0e`，含实际独立精确复跑和另一实现。

以下第1节起数学正文逐字保留；新前言只更新可信度和采用范围。

## 1. 保留同一核心和帽，只另指定两个固定平环

Poisson 核、双帽、辅助包围沿用 R27、R34、R36 及已审双帽账本。记核心支持极大值、极小值分别为 $H,m_0$。固定参数为

$$
b=.01,\quad B=.09,\quad P_\pm=(-H,0,\pm.3),\quad
a_{\rm cap}=.1,\quad\chi=.01,
$$

$$
L_b=\sqrt{4H^2+.31^2},\quad
v_\pm=(-2H,0,\pm.31)/L_b,
\quad
\widehat C_\pm=\{P_\pm+.1\omega:|\omega|=1,\ |\omega-v_\pm|\le.01\}.
\tag{1}
$$

本稿不移动帽的轴、球心、材料标记或相位。只指定新的保留平环

$$
\mathcal A_\pm=
\{(r\cos\theta,r\sin\theta,\pm z):c_-\le r\le c_+\},
\qquad
c_-=\frac{577}{1000},\quad c_+=\frac{579}{1000},\quad
z=\frac{47}{500}.
\tag{2}
$$

“固定”要求未来材料图在这些二维片上逐点不变。平环与活动片、帽仍为分离的保留片，不是已经构造的闭曲面。

局部 CK 引理允许选择同一尚未量化的正宽度，使活动片与原竖直柱基准满足

$$
\epsilon\le .005,\qquad
\|F-F_{\rm base}\|_{C^0}\le\delta=10^{-6},\qquad
\|\nu-\nu_{\rm base}\|_{C^0}\le e=10^{-4},
\tag{3}
$$

并具有自身法向点对半径 $.09$。这是有限多个严格要求的共同存在性选择；不是认证宽度 $.005$ 本身可用。因而活动片满足

$$
|F_z|\le .015001,\qquad |F_{xy}|\ge m_{0,\rm lo}-10^{-6}.
\tag{4}
$$

所有数值比较使用旧账本的精确有理端点。显示 $m_{0,\rm lo}\approx .655688007298$ 仅便于阅读。

## 2. 全平环在所有相位的共同包围内

同一上帽轴点写成 $q_0=(-X,0,Z)$，其中

$$
X=H+\frac{H}{5L_b},\qquad Z=.3+\frac{.031}{L_b}.
\tag{5}
$$

各旋转核心的填充凸体包含 $D_{m_0}$。因此
$D_{m_0}\times\{B\}$ 与 $q_0$ 都在每个旧包围 $E^B_\alpha$ 内。
在高度 $z$ 处取两者的凸组合，其权为

$$
\lambda=\frac{z-B}{Z-B}\le
\lambda_*:=\frac{z-B}{Z_{\rm lo}-B}\in(0,1).
$$

组合圆盘的水平中心为 $(-\lambda X,0)$，半径为 $(1-\lambda)m_0$。
故它包含以原点为中心、半径至少

$$
r_{\rm host,lo}=(1-\lambda_*)m_{0,\rm lo}-\lambda_*X_{\rm hi}
>.62>.579
\tag{6}
$$

的圆盘。精确账本给 (6) 的显示值 $.620854884070008$。这包含整个上平环；下平环由完整 $z$ 反射同证。

上小帽的全部点满足旧精确包围

$$
R_{\rm lo}\le |q_{xy}|\le R_{\rm hi},\qquad
V_{\rm lo}\le q_z\le V_{\rm hi},
\tag{7}
$$

其端点由 (5) 的轴点区间向外扩大 $.001=a_{\rm cap}\chi$ 得到。
精确比较另给

$$
\frac{.015001}{m_{0,\rm lo}-10^{-6}}
<\frac{z}{c_+}\le\frac{z}{r}\le\frac{z}{c_-}
<\frac{V_{\rm lo}}{R_{\rm hi}}.
\tag{8}
$$

所以活动片、平环、上帽的径向纬度依次增大。先前 $c=z_c=.1$ 圆柱的具体纬圈分隔反例不适用于本位置。但 (8) 没有填入未知连接，更没有证明整体正支持。

## 3. 所有涉及平环的两点支持核必要门

这一节检查 R37 的换中心两点必要条件，不能反过来当作全局正支持的充分条件。目标仍为 $\rho_*=.03(2.52)=.0756$。

### 3.1 同侧平环与帽：全角、全半径、全帽点

给定平环点 $p=(c\cos\theta,c\sin\theta,z)$、帽点 $q=(-R,0,V)$，绕轴改变计算坐标不改变整个平环。对于固定 $c,R,V$，原点到直线 $pq$ 的平方距离由凹二次分子/正仿射分母引理下界为

$$
\min\left\{
\frac{(zR-cV)^2}{(R-c)^2+(V-z)^2},\quad
\frac{(zR+cV)^2}{(R+c)^2+(V-z)^2}
\right\}.
\tag{9}
$$

为明确覆盖 $c\in[c_-,c_+]$，取

$$
C_-=c_-V_{\rm lo}-zR_{\rm hi}>0,\qquad
C_+=zR_{\rm lo}+c_-V_{\rm lo}>0.
$$

则 (9) 两项分别至少为

$$
Q_-:=\frac{C_-^2}{(R_{\rm hi}-c_-)^2+(V_{\rm hi}-z)^2},\qquad
Q_+:=\frac{C_+^2}{(R_{\rm hi}+c_+)^2+(V_{\rm hi}-z)^2}.
\tag{10}
$$

这里使用 $R_{\rm lo}>c_+$、$V_{\rm lo}>z$，所以各分母所取的上界方向正确。
纯 Fraction 计算得

$$
\min(Q_-,Q_+)>(79/1000)^2>\rho_*^2.
\tag{11}
$$

最小平方下界显示为 $.006310455925311917$。整条直线下界同时覆盖以任一端点为起点的反向射线。

### 3.2 异侧及其他保留点对

若 $q=(-R,0,-V)$，沿 $p+t(p-q)$ 判断最小范数。起点导数非负时，最小值在 $p$，其范数至少 $c_-$；否则在允许的 $\cos\theta$ 子区间上仍用凹分子/正仿射分母引理，端点下界为

$$
\min\left\{c_-^2,
\frac{C_+^2}{(R_{\rm hi}-c_-)^2+(V_{\rm hi}+z)^2}\right\}
>(7/20)^2>\rho_*^2.
\tag{12}
$$

以帽为起点的反向射线满足

$$
q\cdot(q-p)\ge
R_{\rm lo}^2+V_{\rm lo}^2-c_+R_{\rm hi}-zV_{\rm hi}>0,
\tag{13}
$$

故范数在起点已最小。对平环—活动片，以平环点为起点的反向射线，其高度绝对值至少为 $z>\rho_*$；以活动点为起点，在该点水平径向单位向量上的投影不减，至少为 $m_{0,\rm lo}-\delta>c_+>\rho_*$。

同一平环的两个点位于同一高度，反向射线的高度绝对值恒为 $z$；异侧平环时沿反向射线高度绝对值增加。因此所有涉及新平环的保留点对都不会通过上述必要条件排除目标 $\rho_*$。

## 4. 完整保留点对的法向半径 .0766

法向点对条件为

$$
2|(Q-P)\cdot\nu_P|\le\frac{|Q-P|^2}{\tau}.
\tag{14}
$$

它必须在两个有向端点分别检查。平环法向竖直，活动柱基准法向水平；不能只用共同的粗距离下界略过这个近点对。

### 4.1 平环端：利用水平间距

实际活动点 $P$ 与平环点 $Q$ 的水平间距至少

$$
d_h=m_{0,\rm lo}-\delta-c_+>.07668
>\frac{383}{5000}=.0766.
\tag{15}
$$

精确门使用有理 $m_{0,\rm lo}$，$d_h$ 的近似显示为 $.076687007298$。写弦为 $(v,w)$。在平环端 $\nu_Q=\pm e_z$，从 $|v|\ge d_h$ 得

$$
|P-Q|^2=|v|^2+w^2\ge 2d_h|w|
=2d_h|(P-Q)\cdot\nu_Q|.
\tag{16}
$$

所以平环端已有半径 $d_h$，不需要限制这个点对的竖直间距。

### 4.2 活动端：利用竖直间距及真实法向误差

活动柱基准与任一平环的竖直间距至少

$$
g=z-(b+.005)=.079.
$$

对基准弦 $\bar d$ 与水平基准法向，AM–GM 给
$2|\bar d\cdot\bar\nu|\le |\bar d|^2/g$。
实际点移动至多 $\delta$，单位法向移动至多 $e$。
若 $r=|d|$，则 $r\ge g-\delta$、$|\bar d|\le r+\delta$，从而

$$
2|d\cdot\nu_P|\le\frac{(r+\delta)^2}{g}+2\delta+2re.
$$

除以 $r^2$ 得

$$
\frac{2|d\cdot\nu_P|}{|d|^2}\le
C_*:=\frac1g+
\frac{2\delta/g+2e}{g-\delta}+
\frac{\delta^2/g+2\delta}{(g-\delta)^2}.
\tag{17}
$$

精确账本证明 $1/C_*>.07898>.0766$；其显示值为 $.07898020467282107$。
这涵盖上下片的所有角度及全部活动高度，没有仅检查最接近的两点。

### 4.3 其余所有片内和跨片点对

活动片自身的点对半径为 $.09$；球面帽为 $.1$；单个平环内法向点对分子恒为零。
其余跨片距离下界为

$$
\begin{array}{c|c}
\text{两类片}&\text{距离下界}\\\hline
\text{活动片与帽}&.3-.1-.015001=.184999\\
\text{平环与帽}&H_{\rm lo}-.1-.579\\
\text{上下平环}&2(.094)=.188\\
\text{上下帽}&.4
\end{array}
\tag{18}
$$

这些精确下界都大于 $2(.0766)$，于是可用
$2|d\cdot\nu|\le2|d|\le |d|^2/.0766$。
结合 (15)–(18)，活动片、两个固定平环、两个固定小帽上的任意点对，在两个端点法向及全部相位上统一满足 (14)，其中

$$
\boxed{\tau=383/5000=.0766>.0756.}
\tag{19}
$$

(19) 只是这些分离保留片之间的全部法向点对证书。未知活动连接、固定外桥以及它们的混合点对都不在证明范围内。也不把平环作为带边集合的 reach 与未来闭面的 reach 混用。

## 5. 真正退化的两阶入口与仍待求解的条件

以上平环外沿 $r_0=c_+$ 为入口，水平参数化的完整 Cartesian 两阶数据为

$$
F=r_0e_r+ze_z,\quad F_r=e_r,\quad F_{rr}=0,\quad
F_\theta=r_0e_\theta,\quad F_{r\theta}=e_\theta,\quad
F_{\theta\theta}=-r_0e_r.
\tag{20}
$$

在 inward 经线取向 $r_s=-1/\sqrt E$ 下，$n=F_s\times F_\theta/r=-e_z$，
所以 $A=F_{rr}\cdot n=B=F_{r\theta}\cdot n=C=F_{\theta\theta}\cdot n=0$。
共同度量应在入口满足 $E\to1,E'\to0$。若采用旋转背景 $E=1+w^2$、$h_r=-w$，完整平面两jet还要求 $w,w_r\to0$，不能只检查 $E'\to0$。

相位作用 $F_\alpha(r,\theta)=R_\alpha F(r,\theta-\alpha)$ 使 (20) 逐点不变，因此一个实际满足它的活动连接可与同一固定平环 $C^2$ 接合。退化接口的 Gauss–Codazzi 系统及可核验的平圆领极限条件另写在 `audit-degenerate-flat-endpoint-interface`；本节没有预设这个边值问题已有解。

由于 (2) 位于旧共同包围内，若未来完整连接仍满足旧单向包围与实际支持/远点见证，则 R36 原条件比例可继续使用：$D_0<2.51518578393841$、$\delta_E/D_0>.05109026903944$、$\delta_{\rm hold}/D_0>.20712850442174$。这些只是原有条件命题；本稿没有构造新的实际闭图，也没有证明活动连接真能在核心相对高度 $.094$ 处达到平环。

## 6. 复现与来源

标量脚本为 `scripts/db6f-audit-flat058-geometric-template.py`。它只读取并核 SHA 的两个旧精确 JSON：

- `notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json`；
- `notes/2026-11-09-db6f-audit-positive-collar-budget.json`。

输出以独占创建模式写入，重复运行须给新输出路径。程序的结论明确保留 `common_metric_exit_solved=false`、`connected_connection_constructed=false`、`whole_positive_support_or_reach_proved=false`。

完整推导来源包括 R27、R34、R36、R37、R38，以及旧 cylindrical-cuff 和 cylinder058 两份接口稿；精确身份随独立来源清单记录。新脚本和正文属于作者核验，必须另由未参与者全文审查，不能因已有圆柱稿独审而省略平环法向与新半径的审核。
