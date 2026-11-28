# R724 — 两段中央区间配对半波：同均值闭合、斜率减半及完整位置与角 jet 账

2026-11-28。**已证明的对象是新的准确参考 seed，不是已返回的优化场或连续证书。** 在两个等长中央区间上，分别使用原 R711 profile 的正半波和负半波。两段合起来保留原完整三分量均值、同一个幅度根及其两角导数；每段的最大径向转角斜率严格等于原每段完整波的一半。第一段的横向均值不再为零，位移直到第二段末尾才抵消。本文给出这一中间位移、其两角导数及一个完整一致上界，并说明所有原端口、对称与物理相位的准确适用范围。

首个独立执行参数沿用 run19 的完整配置：相对端层总长 $b/S=1/2$、$\delta=1/32$、$M=160,J=923,N=2048$、全部32个 normal 阶段及全部原求解、方向、回溯、角、径向与时间预算，metric/restoration 的 $\mu$ 均为 $.01$。这是一个输入选择；没有从这些参数推出实际 $D,K,\sigma$、Gram、reach 或握持比例。没有将旧场、工作根、缓存、参考缺陷或已接受点迁作新场。早期源码准备表曾拟沿用 run21 的 $b/S=5/8$；其后 run21 的真实有限几何返回不支持该宽度更优，故最终单候选改回完整 run19 的 $b/S=1/2$ 并只换半波机制。早期准备表原字保为历史，十三个通用运行源码不含 $5/8$ 硬钉，全部从真实参数读取。本次没有把有限screen比较称为连续证明。

## 1. 已登记结论和本次真正改变的对象

使用已登记的：

- [R708：支撑内单位 meridian seed](R708-supported-unit-meridian-seed-contraction.md)；
- [R709：全局凸均值闭合](R709-global-convex-mean-closure-without-contraction.md)及 [R722：后验凸均值存在性](R722-posterior-convex-mean-root-existence.md)；
- [R710：完整两角 jet 费用链](R710-supported-unit-seed-complete-angular-jet-error-bounds.md)；
- [R711：十二片平滑三角 profile](R711-smooth-triangle-central-profile-and-geometric-comparison.md)；
- [R715：参考中心化及完整工作 lift](R715-reference-centred-normal-sixjets-and-error-ledger.md)；
- [R721：宽度与 profile 敏感性](R721-supported-seed-width-and-profile-sensitivity.md)。

R711 的原方案在每一个中央区间内走完整的正、负波，因而每段各自的正弦均值为零。本方案把这个抵消移到两个完整中央区间之间。原定理中的“每段总积分不变，所以全部中央区间之外逐点不变”不能直接套用；本方案在两段之间一般有非零位移。R711 原近最优斜率结论的相位类含每段内部中点为零的约束，本方案不属于那个类，故斜率减半不与该结论冲突。

准确固定标量函数 $a(s)$、材料图 $\Theta_0$、固定度量
$$
g=ds^2+a(s)^2\,d\Theta_0(\phi)^2
$$
及参考 $\Gamma_0,H_0,R,S$ 全不变。当前全部自由 core 系数、三个完整 omega 通道、当前自由 $H$、原控制 supports 和 normal 方程也不减少。变化是固定参考切向量 $T_{\rm ref}$ 的中央径向形状；它会改变完整物理场、参考数值缺陷和实际优化初值的统计。

## 2. 全部准确假设

固定 $S>0$、两个不相交的内部支撑和原四个端层。两个中央区间为
$$
I_1=[a_1,b_1],\qquad I_2=[a_2,b_2],\qquad
b_1<a_2,\qquad b_i-a_i=\ell>0.
$$
记 $L_c=2\ell$。等长是本机制的明确条件，不能仅以总长相等替代。

对每个材料角，假定原准确三均值方程
$$
L_c v+B(Nv)=K,\qquad N(v)=v/|v|
\tag{1}
$$
已有所声明的同一准确根，且
$$
0<r=|v|<1,\qquad d=v/r,\qquad
w=\frac{e_r(\Theta_0)-(e_r(\Theta_0)\cdot d)d}
 {|e_r(\Theta_0)-(e_r(\Theta_0)\cdot d)d|}
\tag{2}
$$
有定义。故 $|d|=|w|=1$、$d\cdot w=0$。需要全角二 jet 时，要求这条根、投影架和相应数据在全角上有共同的 $C^2$ 分支；需要全角可消费证据时，仍须原 R709 或独立 R722 的完整存在、唯一性、根关联及正则条件。工作保存的近单位向量不能直接替代(2)。

$K$ 包含原 $\Gamma_0,H_0$、完整补集积分；$B$ 包含原所有边界归一化积分。两者均不使用中央相位的细部形状。本方案不改变补集、端层、$\chi$ 或 $L_c$，所以(1)及其完整一二角导数逐项不变。这是准确方程的同一性，不是浮点工作字的自动同一性。

取固定 $0<\delta<1/8$。令 $h=h_\delta$ 为 R711 的完整十二片 $C^3$ profile，满足
$$
h(t+1/2)=-h(t),\quad h(1-t)=-h(t),\quad
h(0)=h(1/2)=h(1)=0,
$$
并且在这三个点一、二、三阶导数均为零。在 $[0,1/2]$ 内 $h\ge0$、内点严格正，$h(1/4)=1$。设
$$
A_\delta(\lambda)=\int_0^1\cos(\lambda h(t))\,dt.
$$
R711 已证明 $A_\delta$ 在 $(0,\pi)$ 严格下降，由1到0，因此准确幅度
$$
A_\delta(\lambda)=r,\qquad 0<\lambda<\pi
\tag{3}
$$
唯一。这里保留该完整原函数，不另定义或拟合一个新幅度方程。

## 3. 新的完整六片半波和全部准确切点

定义
$$
f_\delta(t)=h_\delta(t/2),\qquad 0\le t\le1.
\tag{4}
$$
它从0上升至1再下降至0，$f_\delta(1-t)=f_\delta(t)$。完整六片切点是
$$
0,\quad 2\delta,\quad \frac12-2\delta,\quad \frac12,\quad
\frac12+2\delta,\quad 1-2\delta,\quad1.
\tag{5}
$$
因为 $0<\delta<1/8$，相邻切点严格有序；没有零长片或被略去的 ramp。每个物理区间 $[a_i,b_i]$ 的切点都是
$$
a_i+\ell t_j,
\tag{6}
$$
并以完整准确 affine 表达式并入原径向节点、support 与端层边界的并集。局部坐标必须据自己的完整区间计算，不把近似旧胞坐标冒准确切点。

新切向量在两段中央分别为
$$
T_+(t,\phi)=\cos(\lambda f_\delta(t))d+
            \sin(\lambda f_\delta(t))w,
$$
$$
T_-(t,\phi)=\cos(\lambda f_\delta(t))d-
            \sin(\lambda f_\delta(t))w.
\tag{7}
$$
第一段取正号、第二段取负号，符号只取决于固定的径向发现次序。补集和四个端层的 $T$ 完全保留原公式。由正交架，(7)均严格单位。

设相对端层总长为 $q=b/S$，原 support 为
$$
[1/32,15/32]S,\qquad[17/32,31/32]S.
$$
四端层各长 $b/4$，所以
$$
\ell=\left(\frac7{16}-\frac q2\right)S,\qquad
L_c=\left(\frac78-q\right)S,\qquad0<q<7/8.
\tag{8}
$$
首候选 $q=1/2$ 给
$
I_1=[5S/32,11S/32],\qquad I_2=[21S/32,27S/32],\qquad\ell=3S/16.
$
$\delta=1/32$ 时(5)为
$$
0,\ 1/16,\ 7/16,\ 1/2,\ 9/16,\ 15/16,\ 1.
$$
这些是预先声明的短公式，不是从旧数值输出取出的节点或系数。

## 4. 精确的跨段均值抵消

记
$$
J_\delta(\lambda)=2\int_0^{1/2}\sin(\lambda h(u))\,du.
\tag{9}
$$
由 $0<\lambda<\pi$ 及正半波的正测度性，$J_\delta(\lambda)>0$。利用 $h(u+1/2)=-h(u)$ 和换元 $u=t/2$，
$$
\int_0^1\cos(\lambda f_\delta(t))\,dt=A_\delta(\lambda)=r,
$$
$$
\int_0^1\sin(\lambda f_\delta(t))\,dt=J_\delta(\lambda).
\tag{10}
$$
于是
$$
\int_{I_1}T_+\,ds=\ell(rd+J_\delta w),\qquad
\int_{I_2}T_-\,ds=\ell(rd-J_\delta w),
$$
$$
\boxed{\ \int_{I_1\cup I_2}T_{\rm new}\,ds=L_cv.\ }
\tag{11}
$$

每一段的正弦均值都非零；只有两个完整等长中央区间合起来为零。因而(1)确实仍是整个新 seed 的三分量闭合方程。若长度不等，剩余正弦项为 $(\ell_1-\ell_2)J_\delta w$，本结论不能使用。新实现以准确有理定义保留等长条件。

所有 $K,B,L_c,v,r,d,w$ 与(3)的准确对象和角方程不变。特别
$$
\lambda_\phi=\frac{r_\phi}{A_\delta'(\lambda)},\qquad
\lambda_{\phi\phi}=
\frac{r_{\phi\phi}-A_\delta''(\lambda)\lambda_\phi^2}{A_\delta'(\lambda)}
\tag{12}
$$
仍是原完整公式。各中央积分本身的两角 jet 改变，但两个完整区间的总积分及两角 jet仍分别为 $L_cv,L_cv_\phi,L_cv_{\phi\phi}$。这是对(11)求导的结论；积分交换须用第2节的共同正则分支，不能只靠有限角残差。

## 5. 严格的径向斜率收益和其范围

原每段完整波的相位为 $\alpha_{\rm old}(t,\phi)=\lambda h_\delta(t)$。新相位为 $\pm\lambda h_\delta(t/2)$，故
$$
\max|\partial_t\alpha_{\rm new}|
=\frac{\lambda}{2(1/4-\delta)},\qquad
\max|\partial_t\alpha_{\rm old}|
=\frac{\lambda}{1/4-\delta}.
$$
相同物理长度 $\ell$ 下，
$$
\boxed{\quad
\sup_{I_1\cup I_2}|(T_{\rm new})_s|
=\frac{\lambda}{2\ell(1/4-\delta)}
=\frac12\sup_{I_1\cup I_2}|(T_{\rm old})_s|.
\quad}
\tag{13}
$$
这里对每个固定 $\phi$ 成立。准确零外旋转、准确均值闭合的初始 seed 有 $F_s=T$，所以(13)也给中央 $|F_{ss}|$ 的比较。它不适用于未经误差付款的工作 lift，也不把后来非零旋转与 normal 控制的完整场自动排序。

更强的逐点对应是
$$
T_+(t,\phi)=T_{\rm old}(t/2,\phi),\qquad
T_-(t,\phi)=T_{\rm old}(1/2+t/2,\phi).
\tag{14}
$$
因此新两段合起来覆盖原完整波的所有参数值。对于 $j=0,1,2$，中央的 $\partial_\phi^jT$ 值域完全是原值域；对于已有的径向导数，
$$
\partial_s^k\partial_\phi^jT_{\rm new}
=2^{-k}\partial_s^k\partial_\phi^jT_{\rm old}
\tag{15}
$$
在相应点成立。右侧的物理导数仍按同一个旧长度 $\ell$ 理解。特别 $T_{s\phi}$ 的上确界也减半；$T_\phi,T_{\phi\phi}$ 的上确界不因这一重参数化增加。

(15)是切向量的局部规律。位置 $F_\phi,F_{\phi\phi}$ 包含累积积分，不能据此说其值域或 Gram 不变。真实主曲率还含法向投影、混合项、角二阶项及第一基本形式逆；reach还含完整全局注入条件。所以本结果没有 $K_{\rm new}=K_{\rm old}/2$ 或 reach 翻倍的结论。

### 5.1 新相位类中的最小斜率尺度

只为说明机制差异，令一个 Lipschitz 相位 $\alpha:[0,1]\to\mathbb R$ 满足两端为零，且 $\int_0^1\cos\alpha=r\in(0,1)$；不再要求内部中点为零。记 $M=\|\alpha'\|_\infty$。若 $M<2\pi$，则
$$
|\alpha(t)|\le M\min(t,1-t)<\pi
$$
给
$$
r\ge2\int_0^{1/2}\cos(Mt)\,dt=\operatorname{sinc}(M/2).
$$
若 $\lambda_\triangle(r)\in(0,\pi)$ 是唯一 sinc 根，便有 $M\ge2\lambda_\triangle(r)$；当 $M\ge2\pi$ 时同一结论自动成立。原 R711 已给 $\lambda_\delta(r)\le\lambda_\triangle(r)$，故本半波
$$
\|\alpha'_{\rm new}\|_\infty
=\frac{2\lambda_\delta}{1-4\delta}
\le\frac{2\lambda_\triangle}{1-4\delta}.
\tag{16}
$$
这是新类的 scalar 近最优斜率尺度；与原含中点零约束的 $4\lambda_\triangle$ 下界并不矛盾。它仍不是曲面几何最优结论。

## 6. 不可忽略的中间位移：完整准确公式

在准确旧、新初始 seed 中，core与cap端点相同，且总积分相同。因而可用同一 core锚定式
$$
F(s,\phi)=\Gamma_0(\phi)+\int_0^sT(u,\phi)\,du.
$$
令
$$
C(t,\lambda)=\int_0^t\cos(\lambda h(u))\,du,\qquad
S(t,\lambda)=\int_0^t\sin(\lambda h(u))\,du,
$$
$$
a(t,\lambda)=2C(t/2,\lambda)-C(t,\lambda),
$$
$$
b_+(t,\lambda)=2S(t/2,\lambda)-S(t,\lambda),
$$
$$
b_-(t,\lambda)=J_\delta(\lambda)-2S(t/2,\lambda)-S(t,\lambda).
\tag{17}
$$
则完整位置差 $\Delta F=F_{\rm new}-F_{\rm old}$ 是：

| 准确径向区域 | $\Delta F$ |
|---|---|
| 第一中央段之前 | $0$ |
| 第一中央段，$t=(s-a_1)/\ell$ | $\ell(a\,d+b_+\,w)$ |
| 第一中央段之后、第二中央段之前 | $\ell J_\delta w$ |
| 第二中央段，$t=(s-a_2)/\ell$ | $\ell(a\,d+b_-\,w)$ |
| 第二中央段之后 | $0$ |

例如在第一段末端，$C(1)=2C(1/2)=r$、$S(1)=0$，确有 $\Delta F=\ell J_\delta w$；在第二段末端才回到0。中间区域包括原未改变切向量的补集和部分端层。切向量不变不等于位置不变。

每一个区域的完整一二角 jet 可直接从(17)求得。若记所用的两个系数为 $a(\lambda),b(\lambda)$，则
$$
\Delta F_\phi=\ell\{a d_\phi+a_\lambda\lambda_\phi d
+b w_\phi+b_\lambda\lambda_\phi w\},
$$
$$
\begin{aligned}
\Delta F_{\phi\phi}=\ell\{&
a d_{\phi\phi}+2a_\lambda\lambda_\phi d_\phi
+(a_{\lambda\lambda}\lambda_\phi^2+a_\lambda\lambda_{\phi\phi})d\\
&+b w_{\phi\phi}+2b_\lambda\lambda_\phi w_\phi
+(b_{\lambda\lambda}\lambda_\phi^2+b_\lambda\lambda_{\phi\phi})w\}.
\end{aligned}
\tag{18}
$$
中间区域取 $a=0,b=J_\delta$。全部系数导数的真实积分为
$$
C_\lambda=-\int_0^t h\sin(\lambda h),\quad
C_{\lambda\lambda}=-\int_0^t h^2\cos(\lambda h),
$$
$$
S_\lambda=\int_0^t h\cos(\lambda h),\quad
S_{\lambda\lambda}=-\int_0^t h^2\sin(\lambda h).
\tag{19}
$$
没有删掉 $\lambda_\phi,\lambda_{\phi\phi}$ 或架导数项。对几何比较需要的 $e_1,e_2$ 应由(18)及真实全角输入向外支付，不能从一个零阶位置界直接推出。

## 7. 不依赖未返回数值的完整位置上界

以下界仅需第2节的准确单位与根条件。令
$$
R_r=\sqrt{1-r^2},\qquad J=J_\delta(\lambda).
$$
由正半波单位切向量的平均为 $rd+Jw$，
$$
r^2+J^2\le1,\qquad0<J\le R_r.
\tag{20}
$$

先给一个简单完整积分事实。若 $U:[0,1]\to\mathbb R^3$、$|U|=1$，均值为 $m$，则
$$
\left|\int_0^t(U-m)\,du\right|
\le\sqrt{t(1-t)(1-|m|^2)}.
\tag{21}
$$
证明：写成 $\int_0^1(\mathbf1_{[0,t]}-t)(U-m)$，Cauchy–Schwarz 与
$\int|U-m|^2=1-|m|^2$ 给出(21)。没有随机性、离散权或凸嵌入假设。

在第一中央区间，将旧切向量按均值 $rd$ 居中，新切向量按均值 $rd+Jw$ 居中。由(21)，
$$
\frac{|\Delta F|}{\ell}
\le tJ+\sqrt{t(1-t)}
 \left(R_r+\sqrt{R_r^2-J^2}\right).
\tag{22}
$$
第二中央区间同样得到右侧的 $tJ$ 换成 $(1-t)J$。中间区域为 $J$。对 $t\in[0,1]$ 最大化(22)右侧，得到
$$
\frac12\left[J+\sqrt{2R_r^2+2R_r\sqrt{R_r^2-J^2}}\right].
$$
令 $J=R_r\sin\theta$，$0\le\theta\le\pi/2$，上式为
$R_r(\frac12\sin\theta+\cos(\theta/2))$。
其导数为 $(\cos\theta-\sin(\theta/2))/2$，在 $\theta=\pi/3$ 换号，故最大值为 $3\sqrt3R_r/4$。因此
$$
\boxed{\quad
\sup_{0\le s\le S}|\Delta F(s,\phi)|
\le\frac{3\sqrt3}{4}\,\ell\sqrt{1-r(\phi)^2}.
\quad}
\tag{23}
$$
若只有完整准确 $r\ge r_->0$，可将右侧换成
$e_0=(3\sqrt3/4)\ell\sqrt{1-r_-^2}$；若尚没有可用的正下界但准确根条件已成立，则可用较粗的 $(3\sqrt3/4)\ell$。本文未填任何实际 $r_-$。

核心、帽及其标记保持相同；下片是同一正交反射，故(23)同样控制整张对应闭参数面的点差。物理相位只作正交旋转和同一准确材料重参数化，因此同一 $e_0$ 也对所有 $t\in[0,1]$ 的对应活动点成立。于是条件比较
$$
D_{\rm new}\le D_{\rm old}+2e_0
\tag{24}
$$
合法，整像距离、固定见证或非局部点对的比较仍须完整集合上的相应误差账。不能将(23)当成新直径已小、支撑已付或握持比例已成功。

## 8. 完整端口与闭曲面参数化

在每个新中央区间两端，$f=f'=f''=0$，故
$$
T=d,\quad T_s=0,\quad T_{ss}=0,\quad
T_\phi=d_\phi,\quad T_{\phi\phi}=d_{\phi\phi},\quad T_{s\phi}=0.
\tag{25}
$$
原端层在 $\chi=1$ 端有 $1-\chi=\chi'=\chi''=0$，所以全部相应端口一致。新中央峰值处 $f'=f''=0$，六个多项式片之间也具有原 $C^3$ 接合。原四个端层与补集没有改变。

两个中央段的总差及两角导数为零，因此第一段以前与第二段以后的位置及两角导数也完全相同。新 seed 在 core和cap附近与原准确 seed具有全部需要的六 jet端口。原 $\omega$ 端点 mask、控制 supports、closure lift、两片 core反射、两个平帽及固定 p4帽的公式照原保留。

这保证的是在原准确根和非退化条件下的完整 $C^2$ 参数化接合和同一闭参数域。它不证明新场已浸入、嵌入、外向、达到目标 reach 或满足全部 phase混合点对条件。完整新 Gram/法向、R650或R723输入仍必须实际支付。

## 9. 半转、平面反射与物理全相位

设正交变换 $O$ 同时作用于原 $K,T_0,e_r,\Gamma,P$ 数据。归一化、欧氏内积、完整边界积分和(1)均协变；在已付唯一根分支下，
$$
v\mapsto Ov,\quad d\mapsto Od,\quad w\mapsto Ow,\quad
r,\lambda\text{ 不变}.
$$
新符号只依固定径向区间次序，故(7)逐点变为 $OT_\pm$。原 $\phi\mapsto\phi+\pi$ 的水平半转与 $\phi\mapsto-\phi$ 的平面反射若满足原数据条件，均保留。反射的角一 jet另带参数反向符号，角二 jet不带该符号。新 seed没有使用叉积来定义 $w$，不额外引入轴向向量的错误变换律。

当前完整 normal校正仍须按原32阶段方程与全角根盒支付其所选分支的协变。上述准确 seed结论不把有限独立求根的近对称升级为准确 normal分支同一性。

原物理相位取 $\alpha=\pi t/2$，以及
$$
\zeta(t,\phi)=\Theta_0^{-1}(\Theta_0(\phi)-\alpha),\qquad
U_t(s,\phi)=R_\alpha U(s,\zeta(t,\phi)).
\tag{26}
$$
固定 $\Theta_0$、全部 $\zeta_\phi,\zeta_{\phi\phi}$ 链、下片反射、固定帽与 $t\in[0,1]$ 全域不变。新 seed只改变被代入的 $U$，不把 flex时间当中央profile坐标。只要新的完整 $U$ 与原端口条件成立，(26)保持原强 $C^2$ 连续参数性；不在此声称额外的 Banach $C^2$ 时间可微性。

活动上片的同相位旋转保持其主曲率和相对 Gram谱，但 marked wholeimage、与固定帽的 mixed pair、共同 support、D及 reach需要新场的完整证据。原 R718 必须使用同一新闭面的真实 $\sigma$；原 R723 的全闭法管条件也不能由(13)替代。

## 10. 完整可执行 seed 的最小确定变换

原完整 provider 是：

- fixed_fejer_supported_meridian_reference.py，39,771 B；
- SHA256 ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a。

新完整 provider 是：

- [fixed_fejer_paired_halfwave_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py)，43,697 B；
- SHA256 cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0。

完整变化是：

1. 新 source/schema和明确的配对物理 profile定义；准确等长中央条件由有理数定义检查。
2. 中央求值在同一完整 R711 evaluator上取 $t/2$，第一段符号为正、第二段为负，径向链乘相应 $\pm1/2$。
3. 将(5)(6)的所有真实半波切点加入 seed自己的完整 exact-affine计划。
4. 元数据明确区分每个物理中央的六片、两个物理中央共十二片、辅助 $A_\delta$ 规则原十二片，以及仅跨两段的正弦抵消。

原 _means 全函数、evaluate 及其完整角/radial公式、原 _radial 查询、原 scalar/图求值与全部失败逻辑均逐字保留。没有删掉任何真实角、端层、补集、尾部、控制或参数。

新 seed radial_plan.schema 是 complete-paired-halfwave-seed-radial-plan-v1；
working_definition.schema 是 paired-halfwave-reference-working-definition-v1。
model.mathematical_profile_piece_count=6 的明确 scope 是一个物理中央区间。完整 paired_halfwave_definition 同时记录所有准确切点、两区间、符号、辅助规则及链因子，不能用一个无范围的 piece计数混同两类规则。

## 11. f848 可完整共享的准确含义

原 supported_smooth_triangle_seed_mean_jets.py 全体34,725 B、SHA256
f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917
保持原字。

它接受完整 $K_0,K_1,K_2$、完整边界三 jet/权/$\chi$、$L_c$ 和投影架，真实求解(1)，再用原十二片正权规则计算 $A_\delta,A_\delta',A_\delta''$ 与幅度及两角 jet。由(11)，这一整套数学仍正是新配对 seed需要的完整方程；不需要把求积减为半段、改其节点顺序、强置一个浮点正弦和为零或改变原组合残差容差。

该 kernel元数据中的十二片和 odd profile描述的是其原辅助完整 $A_\delta$ 规则。新 seed明确记录辅助规则与物理每段半波的区别。它没有声称每个物理半波的横向均值为零，也没有声称全场 Gauss积分逐字等于辅助均值积分。

共享源码和准确方程不自动证明两次执行的均值、节点、closure或缓存字相同。新计划记录、模型身份、物理profile求值、调用时序与全场数据均独立保存。只有真实返回的完整记录才能报告实际工作量和字节。

## 12. 新切点与外层原工作积分的真实边界

seed的 _prepare_plan 在原准确 affine节点、support/端层边缘之外增加所有物理半波切点。每个新增中央 piece仍记录 node_count=0，因为 seed均值的中央部分单独通过(11)和原辅助十二片 $A_\delta$ 规则计算。补集与端层仍用全部原正权Gauss。

**这不意味着外层 working积分已经按这些切点重新分片。** 新 base的 integration_query、每个原胞的原8点Gauss、全部 cumsum、部分 Lagrange原函数和求和顺序均保留完整原正文。外层仍在原 $J-1$ 胞上计算完整物理新profile。原积分阶、角块、观察行和预算全保。

所以“seed准确计划含新六片切点”与“所有外层Gauss已按半波切点分片”是不同命题；后者本次不声称。原工作积分误差、scalar载体、三角函数、真实均值根、normal根及其混合 jet费用仍未自动支付。

未来同场准确径向费用必须把(5)(6)加入自己的完整准确叶划分，并在每叶使用带符号的半波及链因子；旧每中央完整 odd profile的物理包围函数不能仅改source标签继续使用。辅助 R710/R711/R722均值与两角根费用可以复用原数学，但物理叶、径向profile与源身份须明确新分支。

## 13. base、固定Q与参考校准的完整来源

新 base fixed_fejer_paired_halfwave_meridian_operator.py：

- 40,803 B；
- SHA256 b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6。

其 initial 及其后全部原方法正文原字；构造器只绑定真实新 seed/schema并记录新物理定义。固定材料图、完整原自由布局、Exp、全积分和物理 lift不改。

新 Q binder fixed_fejer_paired_halfwave_literal_zero_moment_input.py：

- 34,886 B；
- SHA256 53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333。

全部十八个旧已公开 Q常数保留其真实参数来源。它们不成为新场的已证矩逆。新 binder严格重核完整新 seed/base/参考/目标，并明确核每段6片、辅助12片、全对12片、全部准确区间/切点及反号，不放宽原完整对象等号。

新 calibration fixed_fejer_paired_halfwave_reference_calibration.py：

- 11,872 B；
- SHA256 c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106。

完整 FrozenReferenceCalibration class原字，只重钉新 seed/base/endpoint来源。它通过实际新 base._parent_tensor 取得同一积分查询下的新物理参考三 jet，并真实保存新的 reference defect。旧参考NPZ、角批、缺陷值或初场读数不继承。原 R715当前raw closure lift及其全部导数仍保留。

## 14. 下层、上层及实际新场的责任

解析局部J3、解析六控制frame、C1复用、stage/adjacent矩阵、immutable closure值与detached meridian值的数学正文不变；它们必须完整绑定新的 base和normal schema及递归实际 source。两次已经修复的真实 callable解包与 _meridian_data完整method guard保留。不能用旧 sourcehash冒新物理provider。

新的 endpoint仍包含全部32阶段、全部六控制、原全域/回溯/最终重读/上游J链与物理六 jet。packet记录新的实际 source/model/point/全部缓存角与实际stage，不能将旧packet冒新场。纯读者保每个原snapshot自己的点；模型、参考校准、seed/working定义和全部完整源各自重读。

旧完整科学与纯读者、所有失败/终态/未知typed与永久历史均保留。run22是从预先声明参考独立开始的新seed机制，不把旧 accepted/fullfinal偷偷改称同一物理场。原严格父全对象比较不能为此剥掉完整seed/base。后续若另需合法迁移，须另给明确完整输入合同；本结果不声明现已完成这种迁移。

物理相位、normal、Gram、D、曲率、握持、全帽/mixed支持、全reach、闭面外向与 E(3)商证据均须消费新实际同点完整报告/packet。准备好的输入、可变进度和旧模型的成功值都不满足这些前提。

## 15. 完整复现和当前事实范围

首四完整源码由
[reproduce_fixed_fejer_paired_halfwave_seed_sources.py](../scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_seed_sources.py)
从四份完整固定父按明确逐字替换再生；它保存全部父和输出SHA/字节及反向恢复。它只操作源码文本，不导入、编译或执行科学源码，不作为额外数值准入步骤。

完整原始来源为 ad52 seed、552f base、ca4 Q、aa40 calibration，以及共享 f848均值核与 e717固定参考输入。每个新运行体均有自己的完整源字节与身份，未以一个patch替代实际运行源码。所有科学执行只在公开 Actions。本文写作及源码构造没有本地科学、AST/compile或fixture。

本结果实际完成的是：一种不同于继续压缩中央长度的完整 seed机制；准确总均值和两角闭合的保持；中央径向斜率减半；完整中间位移与其导数账；原端口与协变的明确前提；以及新工作来源与切点的可执行定义。真实新场的直径、Gram、principal curvature、reach、握持和最终目标仍等待同源完整计算与连续费用，未填未来身份或成功数值。
