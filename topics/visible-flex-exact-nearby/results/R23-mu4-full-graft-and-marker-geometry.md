# R23：$\mu=4\sqrt2$ 实际接尾、双 bump 与低峰标记的统一几何

2026-11-10，geometry-transfer。

**状态：已证明；主课题的中间结论。** 本文采用
[R22](R22-mu4-true-tail-and-source-conversion.md) 的实际
$\mu=4\sqrt2$ 接尾对象，并从
[R21](R21-mu4-global-geometric-certificate.md) 的整数区间主干证书
支付整个闭背景的几何。全程保留物理关系 $u=4x$、
$z_u=h^{-2}/4$；没有把 $u$ 错当成原来的 canonical $x$。
真 R72 尾的全部过渡层由实际 $\lambda/\rho^2$ 缩放控制。

所得背景和无穷小场包括两个具有内点的固定帽及四个低峰标记。
本结果不认证任何有限幅 Newton 候选，也不构造有限幅公共精确度量族。

## 1. 同一个实际对象及结论

原物理主干为
$$
h_{xx}=\left[32-(32+\sqrt2)\operatorname{sech}^2x\right]h,
\qquad h(0)=1,\ h_x(0)=0,\qquad z_x=h^{-2}.
$$
使用 R22 的统一变量
$$
u=4x,\qquad a=h^{-1},\qquad \omega=h_u/h,\qquad
q=\omega_u/\omega^2,
$$
$$
\boxed{z_u=\frac1{4h^2}=\frac{a^2}{4}.}
\tag{1.1}
$$
固定共同参数
$$
u_b=80\quad(\text{物理 }x_b=20),\qquad
u_T=2^{24},\qquad \Omega=2^{360}.
\tag{1.2}
$$
R22 的两段宽 $\ell\le1/16$ 的 bump 都在 $u$ 坐标中，
总占用长度 $L=3+2\ell\le25/8$，位于 $[u_T-L,u_T]$。
其整个参数矩形由
$$\zeta=s\phi_1+v\phi_2,\qquad
|s|\le\gamma_0,\quad0\le v\le\gamma_0,\quad
\gamma_0=\ell^2/512$$
给出；本文的 $v$ 只是第二个 bump 参数，不是 $h_x$。
取 R22 保持第四模的真实匹配曲线及其共同好参数。
有限 connector、实际 R72 尾与两端平盘均按 R22 构造。

该完整未标记背景满足
$$
\boxed{
\sup|X|<\frac{23}{20},\qquad D<\frac{23}{10},\qquad
K:=\sup\max_i|\kappa_i|<4,\qquad
\sigma:=\inf X\cdot n>\frac45,\qquad G<4.}
\tag{1.3}
$$
再加上第 7 节的四个低峰标记，仍有
$$
\boxed{
D_{\rm mark}<\frac{23}{10},\quad K_{\rm mark}<4,\quad
\sigma_{\rm mark}>\frac45,\quad
\operatorname{reach}(X^{\rm mark})>\frac14,\quad
\frac{\operatorname{reach}(X^{\rm mark})}{D_{\rm mark}}>\frac5{46}.}
\tag{1.4}
$$
并有闭握持集 $H$，内部非空，满足
$$
\boxed{\frac{\operatorname{diam}X^{\rm mark}(H)}
 {D_{\rm mark}}>\frac{81}{115}>\frac15.}
\tag{1.5}
$$
R22 的全局非刚体无穷小场在 $H$ 上恒零。
这些常数没有继承 R14 的 $\mu=\sqrt2$ 主干；
只有其已经证明的通用 connector 控制账和真实尾 profile 估计被复用。

## 2. 远帽真实输入：物理 $x$ 与 $u$ 的界

R21 已给整个未改闭主干的
$$
|X|<23/20,\quad K<4,\quad X\cdot n>4/5,\quad G<4,
$$
以及在物理 $x\ge3/2$ 上
$$
h>26,\qquad h_x/h>24/5,\qquad z>81/100,\qquad z_\infty<5/6.
\tag{2.1}
$$
还需要 connector 的 $\omega>5/4$ 输入。
在物理 $x\ge2$，由 $\cosh2>11/3$、$32+\sqrt2<34$，
$$
Q_x:=h_{xx}/h
>32-34\frac9{121}>29.
$$
令 $w=h_x/h$。Riccati 比较给
$$
w(x)>\sqrt{29}\tanh(\sqrt{29}(x-2)).
$$
当 $x\ge3$，使用 $\sqrt{29}>16/3$ 和
$\tanh\sqrt{29}>\tanh3>15/16$，得到 $w>5$。
后一双曲函数界只需 $e^6>2^6>31$。
又 R21 的首次交叉论证给 $w<4\sqrt2$，故
$$
\boxed{\frac54<\omega<\sqrt2\qquad(u\ge12).}
\tag{2.2}
$$
特别，共同参数 (1.2) 及全部 bump 区都远在这个范围内。

在未改主干的 $u$ 坐标，
$$
P:=h_{uu}/h=
2-\left(2+\frac{\sqrt2}{16}\right)\operatorname{sech}^2(u/4)
<2.
$$
所以接线入口
$$q=P/\omega^2-1\in(-1,7/25).$$
真实第四模为 $y=\operatorname{sech}^{16\sqrt2}(u/4)$，
故其 R22 投影变量
$$
R=\frac{y_u}{16\omega y}
=-\frac{\sqrt2\tanh(u/4)}{4\omega}
$$
位于 $(-3/10,-1/5)$。这给实际准备段所需的正输入区间。
此外，入口半径 $a_0<1/26$，且 $z_0>81/100$。

## 3. 正确的物理曲率与支撑公式

从 (1.1) 得
$$a_u=-\omega a,\qquad z_a=-\frac{a}{4\omega}=-W.$$
因此物理旋转主曲率为
$$
\boxed{
\kappa_\theta=\frac1{\sqrt{a^2+16\omega^2}},\qquad
\kappa_s=\frac{16(1+q)\omega^2}
 {(a^2+16\omega^2)^{3/2}}.}
\tag{3.1}
$$
符号可随一致法向同时改变，以下绝对值界不受影响。特别，
$$
|\kappa_\theta|\le\frac1{4\omega},\qquad
|\kappa_s|\le\frac{|1+q|}{4\omega}.
\tag{3.2}
$$
Gauss 曲率及外法向支撑为
$$
G=\frac{16(1+q)\omega^2}{(a^2+16\omega^2)^2},
$$
$$
\boxed{X\cdot n=
\frac{a^2+4z\omega}{\sqrt{a^2+16\omega^2}}
\ge\frac{z}{\sqrt{1+(a/(4\omega))^2}}.}
\tag{3.3}
$$
若 $t=\log(h/h_0)$，准确高度微分则是
$$\boxed{z_t=\frac{a^2}{4\omega}.} \tag{3.4}$$
第 (3.1)—(3.4) 式是后续所有缩放预算的来源。

## 4. 双 bump 与有限 connector

### 4.1 双 bump

R7 的明确 quintic bump 及不交支持给
$$
|\zeta|\le2^{-17},\quad
|\zeta_u|<1/1000,\quad
|\zeta_{uu}|\le3/16.
$$
写 $\widehat h=h e^\zeta$，则
$$
\widehat\omega=\omega+\zeta_u>6/5,\qquad
\widehat P=P+\zeta_{uu}+2\omega\zeta_u+\zeta_u^2,
$$
$$|\widehat P-P|<1/5,\qquad |\widehat P|<11/5.$$
又 $\widehat a<e^{2^{-17}}/26<1/25$。
用 (3.1)，或等价地
$\kappa_s=16\widehat P/(\widehat a^2+16\widehat\omega^2)^{3/2}$，
得到
$$
|\kappa_\theta|<5/24,\qquad
|\kappa_s|<\frac{11/5}{4(6/5)^3}
=\frac{275}{864}<4,
$$
$$G<\frac{11/5}{16(6/5)^4}<4. \tag{4.1}$$
高度仍单调增加，故 $z>81/100$。
由 $a<1/25,\ \omega>6/5$，(3.3) 的分母小于 $101/100$，
所以支撑大于 $81/101>4/5$。

积分中的物理 $1/4$ 不能删去。两个支持总 $u$ 长度不超过 $1/8$，
且原 $h>26$，因此
$$
|\Delta z_{\rm bump}|
\le\frac14\int h^{-2}|e^{-2\zeta}-1|\,du
<\frac{3\gamma_0}{32\cdot26^2}<\frac1{10000}.
\tag{4.2}
$$
两端完整二阶 jet 保持，所以外端 $a_0,\omega_0,q_0$ 完全不变；
$z_0$ 仅有上述已经支付的高度平移。

### 4.2 准备、放大与末端过渡

R22 使用与 R11 相同的 $t=\log h$ 控制方程
$$
(\log\omega)_t=q,\qquad R_t=q(1-R)+1-16R^2.
$$
两次短过渡的长度 $\eta=2^{-24}$。
准备段 $q\in[-1,2]$，其中 $q=-1$ 主段长度小于
$\log(11/8)$。从 (2.2)，每个前缀均有
$$
\omega>\frac54e^{-\log(11/8)-2\eta}>\frac9{10}.
$$
放大段 $q=2$ 使 $\omega$ 增加。因此
$$
|\kappa_\theta|<5/18,\qquad
|\kappa_s|<5/6,\qquad G<25/108<4.
\tag{4.3}
$$
末端全部前缀由 R22 的停时账给
$\omega>(4/5)\Omega$、$q\in[-8,2]$，所以
$$
|\kappa_s|\le35/(16\Omega)<1/4,\qquad
|\kappa_\theta|\le5/(16\Omega)<1/4.
\tag{4.4}
$$
整个 connector 上仍有 $\omega>9/10$。
$a\le a_0<1/26$ 和 $z\ge z_0>81/100$ 代入 (3.3)，
给支撑 $>81/101>4/5$。
其高度费用独立于巨大的放大总长度：
$$
\boxed{
\Delta z_{\rm con}
<\frac{1}{4(9/10)}
 \int_0^\infty a_0^2e^{-2t}\,dt
=\frac5{36}a_0^2.}
\tag{4.5}
$$

## 5. 真 R72 全部无限层的物理缩放

仍使用 R72 的真实参考尾，记
$$
\delta_*=(2/25)2^{-128},\quad b\in(1,2),\quad
\bar W_b=\delta_*^6/b^7.
$$
[R14 §11](R14-mode-four-full-tail-geometric-bounds.md)
已经从每个实际 log-quintic 层直接证明
$$
M_{\rm tail}:=
\sup\max\{\bar W/\bar r,|\bar W_{\bar r}|\}
\le2^{14}(1+|\log\delta_*|)\delta_*^{7/2}.
\tag{5.1}
$$
该证明只涉及参考 profile，故在这里可以使用；
并未继承 R14 的主干或物理缩放数值。

R22 的准确尺度是
$$
\rho=\frac1{H_eb},\qquad
\lambda=\frac1{4H_e^2b\omega_e\bar W_b},
\qquad
\boxed{\frac\lambda{\rho^2}=\frac b{4\omega_e\bar W_b}.}
\tag{5.2}
$$
物理 $W=(\lambda/\rho)\bar W(r/\rho)$，
$W_r=(\lambda/\rho^2)\bar W_{\bar r}(r/\rho)$。
由 $\omega_e>(4/5)\Omega$，以及 R14 §11 的整数包络
$$5\,2^{12}b^8(1+|\log\delta_*|)\delta_*^{-5/2}<2^{359},$$
得到
$$
\frac\lambda{\rho^2}M_{\rm tail}<\frac{2^{357}}{\Omega}
\le\frac18<\frac14.
\tag{5.3}
$$
所以**整个实际无限尾**都有 $W/r<1/4,\ |W_r|<1/4$。
其两个物理主曲率
$$\frac{W}{r\sqrt{1+W^2}},\qquad
\frac{W_r}{(1+W^2)^{3/2}}$$
的绝对值都小于 $1/4$。
这覆盖全部过渡，不把切口 $q=-8$ 误作全尾控制。

令物理平坦极限半径为 $r_{\rm flat}>0$、末端接缝半径为
$r_e=1/H_e\le a_0$。实际高度费用为
$$
\boxed{\Delta z_{\rm tail}
=\int_{r_{\rm flat}}^{r_e}W\,dr<\frac18a_0^2.}
\tag{5.4}
$$
再向盘心是固定平区，没有高度费用。
尾部支撑满足
$$
X\cdot n=\frac{z+rW}{\sqrt{1+W^2}}
>\frac{81/100}{\sqrt{1+(a_0/4)^2}}
>\frac{81}{101}>\frac45.
\tag{5.5}
$$
R72 的真实物理二阶平坦极限付清了闭盘的 $C^2$ 接合。

## 6. 完整闭背景的几何汇总

R22 给背景、第四模与尾部的实际二阶 jet 匹配；
双 bump 也保持端点二阶 jet。所有正端新部分半径递减、高度递增，
随后接平盘，负端镜像。因此完整面为闭 $C^2$ 嵌入。

每侧新部分的最高点由 (4.2)、(4.5)、(5.4) 控制：
$$
z_{\max}<
\frac56+\frac1{10000}
+\left(\frac5{36}+\frac18\right)\frac1{26^2}
=\frac56+\frac1{10000}+\frac{19}{48672}<\frac{17}{20}.
\tag{6.1}
$$
全部新部分的半径小于 $1/25$。
故其环境半径平方小于
$$
\frac1{625}+\frac{289}{400}<\frac{529}{400}.
$$
未改主干由 R21 已有相同目标界，所以
$D<23/10$。各段曲率、支撑和 Gauss 界联合给 (1.3)。

全局正支撑 offset 论证仍适用：每个足够近的法向偏移有正支撑，
其径向投影为球面的全局微分同胚，且不同偏移沿射线严格嵌套。
于是全局法向管单射，reach $>\min(4/5,1/4)=1/4$。
这里再次付清了全局双点控制。

## 7. 同一尺度上的低峰标记与握持集

令两真平盘物理半径为 $a_\pm>0$，并置
$$a_*=\min(a_+,a_-)<1/26,\quad R=a_*/8,\quad d=a_*/2.$$
完全按照 [R17](R17-fixed-four-curvature-markers.md) 的位置：
上帽中心 $(\pm d,0)$，下帽中心 $(0,\pm d)$；
使用
$$
u_{k,R}(r)=\frac{kR^2}{6}(1-r^2/R^2)_+^3,\qquad
k=2,\sqrt5,\sqrt6,\sqrt7.
$$
原主体全域 $G<4$，四个唯一正局部峰分别为 $4,5,6,7$；
R17 的曲率和非共面论证直接适用。
主曲率 $\le\sqrt7<4$，所以不会增加 (1.3) 的最大预算。

标记后支撑需要按本题较低的帽高度重新计算。
帽高度绝对值大于 $81/100$，而 $R<1/80$，故 R17 的直接公式给
$$
X^{\rm mark}\cdot n^{\rm mark}>
\frac{81/100-1/400}{401/400}
=\frac{323}{401}>\frac45.
\tag{7.1}
$$
最高新增高度小于 $1/9600$。
标记点半径小于 $1/26$、高度绝对值小于
$17/20+1/9600<9/10$，所以
$$
|X^{\rm mark}|^2<1/676+81/100<529/400.
$$
这给全部 (1.4)，没有把旧 $z_\pm\ge900/961$ 输入错误搬过来。

在两帽各取半径 $3a_*/4$ 的闭子盘，其并集为 $H$。
两轴心仍未被标记覆盖，其距离大于 $81/50$。于是
$$
\operatorname{diam}X^{\rm mark}(H)>\frac{81}{50},
\qquad
\frac{\operatorname{diam}X^{\rm mark}(H)}{D_{\rm mark}}
>\frac{81/50}{23/10}=\frac{81}{115}.
$$
四个曲率峰值点的非共面行列式也有本尺度下的直接界
$$
|\det(P_2-P_1,P_3-P_1,P_4-P_1)|>\frac{81}{50}a_*^2>0.
\tag{7.2}
$$
R22 的真实无穷小场在原平盘上为零，加入固定标记后继续为零；
其腰圈非刚体性不变。

## 8. 对后续有限幅对象的界限

本结果处理的是 R22 的同一个真实背景及全局无穷小场。
它解决了新 $\mu$、新物理尺度、真实无限尾和固定标记的联合几何问题，
没有借用旧主干的常数，也没有从数值候选外推。

未来实际非线性图应使用 R18 的点值/法向 witness 预算，
并对有限幅主体另付曲率、支撑、Gauss、精确等距及真实帽端匹配。
当这些误差转移已经支付时，四个固定标记可严格排除环境全等。
当前本文不声称这些有限幅条件已经成立。
