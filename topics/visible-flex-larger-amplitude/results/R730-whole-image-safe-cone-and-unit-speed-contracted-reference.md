# R730 — 全闭参考像的双见证安全锥与同弧长内缩种子

**已证明：下述完整假设下的全闭参考像距离、有限控制点构造、唯一弧长根、全角导数与端口接合。当前实际31的这些条件、角向度量、三百分比 reach 及 normal32 费用均未因此支付。**

2026-11-28。本文给出一个能从位置构造本身保住两 held 见证的新参考种子方向。它保留固定核心、帽半径、帽高、径向长度和既定目标度量的定义；它改变参考切向场，因而不继承 R728 的 working mean、Q、calibration、normal 根、Gram 或曲率。

本文不重新登记 R717 的全像抛物屏障，也不重证 R728 的 $F^\pm={\cal C}\pm{\cal A}w$ 恒等式。新增内容是：把整像避球要求变成**有限 Bernstein 控制点所在的凸锥**，在该锥及原直径球内构造全角参考片，再通过不离开这些集合的水平内缩和一个严格唯一的标量根支付原径向弧长。它给出真实可实施的替代机制，而非从一个角或一个热点推断完整场。

## 1. 准确对象、域和仍然独立的任务

令 $s\in[0,S]$、$\varphi\in\mathbb R/(2\pi\mathbb Z)$。沿用 R717 的准确 dyadic 固定图
$$
 \Gamma=p\,n+p'\,t,\qquad
 \Gamma_\varphi=\rho\,t,\qquad
 \Theta'=\rho>0,\qquad e=(\cos\Theta,\sin\Theta,0),
 \tag{1}
$$
其中 $n=(\cos\varphi,\sin\varphi,0)$、$t=(-\sin\varphi,\cos\varphi,0)$。令
$$
 X=p(0)>0,\quad Y=p(\pi/2)>0,\qquad
 P(\varphi)=R e(\varphi)+H e_z,\quad R>0,\ H>0.
 \tag{2}
$$
这里 $R,S$ 是完整声明的固定 scalar/reference 参数，$H$ 是新种子的声明高度。若使用当前原参考高度规则，须用该规则真实产生的完整字作为声明输入；本文不把它称为准确 scalar 高度积分。当前外层自由高度改变之后，也不自动沿用这个参考高度。

目标仍是
$$
 g=ds^2+a_{\rm deep}(s)^2\,d\Theta^2.
 \tag{3}
$$
本文只从构造证明参考片的 $|F_s|=1$。这不等于证明 $F_s\cdot F_\varphi=0$ 或 $|F_\varphi|=a_{\rm deep}\rho$。两项都必须按实际新场完整支付。

两比较相位的真实核心见证为
$$
 q_\pm=(0,\pm X,0).
 \tag{4}
$$
距离的目标集合是同一基准闭参考像 $S_0$：所有上片、所有下反射片、两完整帽及固定 p4 标记。不是固定 $q$ 到所有相位曲面的距离；在 $q$ 自己所属的相位，它本来就在曲面上。

以下先构造准确参考片，再说明与外层当前核心、自由高度、原始闭合 lift 和32阶段 normal 场之间的误差接口。没有把 working unit-vector 记录、近似根或有限screen改称连续证书。

## 2. 一个能容纳真实帽端口的凸安全锥

给定 $Y_c\ge0$、$m\ge0$，定义
$$
 {\cal K}_{Y_c,m}=\{(x,y,z):z\ge0,\quad |y|\le Y_c+mz\}.
 \tag{5}
$$
它是三个闭半空间的交，因而是凸集。设 $X>Y_c$，记
$$
 \Delta_c=X-Y_c,\qquad d_c=\frac{\Delta_c}{\sqrt{1+m^2}}.
 \tag{6}
$$

**引理1（完整双见证距离）。**
对每个 $p\in{\cal K}_{Y_c,m}$ 以及它的 $z$ 反射，均有
$$
 |p-q_+|\ge d_c,\qquad |p-q_-|\ge d_c.
 \tag{7}
$$

**证明。**
写 $z_*=|z|\ge0$。对任一符号，
$$
 |p-q_\pm|^2
 \ge z_*^2+\bigl[\max(\Delta_c-mz_*,0)\bigr]^2.
$$
若 $m=0$，下界不小于 $\Delta_c^2$。若 $m>0$，在
$0\le z_*\le\Delta_c/m$ 上配方得到最小值
$\Delta_c^2/(1+m^2)$，在其余范围竖直项已不小于
$\Delta_c^2/m^2\ge\Delta_c^2/(1+m^2)$。这证明(7)，并未假定最近点在核心、某条母线或某个角上。∎

这条锥约束是**位置条件**。它不要求在 cap 端口有
$|T_y|\le m T_z$。实际 cap 端口 $T=-e$、$T_z=0$ 一般不满足后一个切向条件；不能把前段的上升锥直接延伸到整个径向域。

若完整上片在(5)中、下片为其反射，且
$$
 R\le Y_c+mH,
 \tag{8}
$$
则两帽也在相应的上/下锥内。原 p4 标记不改变帽面水平坐标，并向外增加 $|z|$，故也保留(5)的反射版本。于是(7)覆盖基准闭像的**全部组成部分**，包括未活动的帽和标记。任何未覆盖的片都不能从这个最小值中删除。

## 3. 当前固定 Fejér 核心允许的明确余量

R717 已证明全核心 $|\Gamma_y|\le Y$，且其准确 dyadic 轴差满足
$$
 X-Y>\frac{939}{1000}.
 \tag{9}
$$
这里使用原理想差 $4714/5005>47/50$ 及已支付的有限 dyadic 比较；没有把理想系数当当前物理字。

一个具体的设计选择是
$$
 Y_c=Y+\frac1{200},\qquad m=\frac15 .
 \tag{10}
$$
于是
$$
 \Delta_c>\frac{467}{500},\qquad
 d_c>\frac{91}{100}.
 \tag{11}
$$
最后一步只用严格有理比较：
$$
 \frac{(467/500)^2}{1+1/25}-\left(\frac{91}{100}\right)^2
 =\frac{2783}{260000}>0.
$$
这不是实际 whole-field 数值。它说：**若按下面构造把整个参考闭像放入该锥，两见证同时有严格超过 $0.91$ 的距离。**

当前完整科学参数中的 witness budget 是 binary64 的 $0.9$，不是1。该字小于 $901/1000$，故(11)留下大于 $9/1000$ 的严格绝对余量。若同时有完整全相位 $D\le21/5$，则
$$
 \frac{d_c}{D}>\frac{91}{420}>\frac15.
 \tag{12}
$$
这是原强 held 目标的正确方向。不能把核心差(9)单独代入(12)：还必须保留整像锥及直径条件。

帽条件现在是
$$
 R\le Y+\frac1{200}+\frac H5 ,
 \tag{13}
$$
而不是不合实际的 $R\le Y$。原固定 grip 需要 $R>9/20$；R717 的短半轴 $Y$ 本来小于 $9/20$。忽略帽高度而要求所有帽都在 $|y|\le Y$ 内，会误排除实际端口。式(13)准确保留了这个区别。

## 4. 用六个完整控制点实现原 core/cap 六 jet

取一个与角无关的物理长度 $\eta>0$，以及一个准确声明的有限标量 $\kappa_0$。若要保留原参考核心二阶径向 jet，取
$\kappa_0=(T_0)_s(0)\cdot e$ 的原准确 scalar 定义；不能用某次工作数组代替。设
$$
 a_0=\frac54|\kappa_0|.
$$
定义六个三维控制点
$$
 \begin{aligned}
 P_0&=\Gamma,&
 P_1&=\Gamma+\eta e_z,\\
 P_2&=\Gamma+2\eta e_z+\frac54\kappa_0\eta^2e,&
 P_3&=P+2\eta e,\\
 P_4&=P+\eta e,&
 P_5&=P.
 \end{aligned}
 \tag{14}
$$
以完整五次 Bernstein 基底
$$
 b_j^5(t)=\binom5j t^j(1-t)^{5-j},\quad0\le t\le1,
$$
定义基线
$$
 B(t,\varphi)=\sum_{j=0}^5b_j^5(t)P_j(\varphi)
             =(b(t,\varphi),z(t)).
 \tag{15}
$$
这里 $b\in\mathbb R^2$ 是水平向量。**高度 $z(t)$ 与角无关。** 此前提在全像嵌入证明中不可省略。

设 $0<2\eta<H$。高度控制值为
$0,\eta,2\eta,H,H,H$，所以
$$
 z_t=5\{\eta b_0^4+\eta b_1^4+(H-2\eta)b_2^4\}>0
 \quad(0\le t<1),\quad z(0)=0,\ z(1)=H.
 \tag{16}
$$
在 cap 处 $z_t(1)=0$，但完整 $B_t(1)=-5\eta e\ne0$。

直接计算端点：
$$
 \begin{array}{c|cc}
 &t=0&t=1\\ \hline
 B&\Gamma&P\\
 B_t&5\eta e_z&-5\eta e\\
 B_{tt}&25\kappa_0\eta^2e&0.
 \end{array}
 \tag{17}
$$
经任意准确弧长重参数化，这给
$$
 \begin{array}{c|cc}
 &s=0&s=S\\ \hline
 F&\Gamma&Re+He_z\\
 F_s&e_z&-e\\
 F_{ss}&\kappa_0e&0\\
 F_\varphi&\Gamma_\varphi&R\rho e_\theta(\Theta)\\
 F_{s\varphi}&0&-\rho e_\theta(\Theta)\\
 F_{\varphi\varphi}&\Gamma_{\varphi\varphi}&
 R\{\rho' e_\theta(\Theta)-\rho^2e\}.
 \end{array}
 \tag{18}
$$
在(18)中 $F_{ss}$ 的计算使用
$(I-TT^{\mathsf T})B_{tt}/|B_t|^2$，不是把 $t$ 当作弧长。核心第二导数是水平向量，故下反射的 $C^2$ 接合成立；cap 第二径向导数为零，与原完整平盘接合。

下面的内缩函数在两端有足够高阶的零，故(17)–(18)原样保留。

## 5. 可逐项支付的控制点锥、球和长度条件

设 $C_\Gamma$ 是完整上界 $\sup_\varphi|\Gamma|\le C_\Gamma$，
$p_{\min}>0$ 是完整下界 $p\ge p_{\min}$。R717 已提供这样的准确全角界。

以下是一个明示的充分条件列表：
$$
 \begin{gathered}
 0<2\eta<H,\qquad
 a_0\eta^2\le Y_c-Y+2m\eta,\qquad
 R+2\eta\le Y_c+mH, \tag{19}\\
 C_\Gamma^2+\eta^2\le R_B^2,\qquad
 (C_\Gamma+a_0\eta^2)^2+4\eta^2\le R_B^2,\qquad
 (R+2\eta)^2+H^2\le R_B^2. \tag{20}
 \end{gathered}
$$
再有 $|\Gamma|\le R_B$。则每个(14)中的控制点都在
${\cal K}_{Y_c,m}\cap\overline B(0,R_B)$ 内。因此由 Bernstein 系数非负且和为1，
$$
 B(t,\varphi)\in{\cal K}_{Y_c,m},\qquad |B(t,\varphi)|\le R_B
 \quad\text{对所有 }t,\varphi .
 \tag{21}
$$
没有采样角，也没有用 control polygon 代替曲线的实际长度。

令
$$
 d_{\rm end}(\varphi)=|P(\varphi)-\Gamma(\varphi)|,\qquad
 d_{\rm end}\le d_+<S.
 \tag{22}
$$
Bernstein 曲线长度不超过其完整控制多边形长度：由
$B_t=5\sum_{j=0}^4 b_j^4(P_{j+1}-P_j)$ 积分即可证明。
对(14)使用 $2\sqrt2<3$，得到
$$
 {\cal L}(0,\varphi):=\int_0^1|B_t|\,dt
 \le d_++7\eta+2a_0\eta^2=:L_+.
 \tag{23}
$$
因此
$$
 d_++7\eta+2a_0\eta^2<S
 \tag{24}
$$
保证所有角都有严格弧长余量。

这些不是一组被宣称已通过的实际数值。它们也是**可满足**的：若
$$
 C_\Gamma<R_B,\quad \sqrt{R^2+H^2}<R_B,\quad
 R<Y_c+mH,\quad Y<Y_c,\quad d_+<S,
 \tag{25}
$$
则对于任何有限 $\kappa_0$，充分小的正 $\eta$ 同时满足(19)–(24)。每项在 $\eta=0$ 有明确严格余量，左端连续；可以用它们的完整有理/向外区间式选定一个明确 dyadic 长度。没有通过修改 $S,R,H,\Gamma$ 来制造余量。

式(22)是任何同端点单位速率母线都必须面对的几何长度条件。这里保留完整
$P-\Gamma=Re(\Theta)-\Gamma+He_z$；不能把 $\Gamma$ 错换成 $p e(\Theta)$，也不能把 $d_+$ 从一个角外推为全角。

### 5.1 当前完整端口的显式六控制点余量

先把控制点本身的可行性与弧长根分开。完整 R690 标量报告给出的准确 $R$ 盒是
$$
 \frac{564734175383798202556909871405419982993527884399889816081393673589866581}{10^{72}}
 \le R\le
 \frac{564734175384276192026033775321496111699110362164506431614854811271693793}{10^{72}} .
 \tag{25a}
$$
所以 $9/16<R<57/100$。当前参考声明高度的实际 binary64 字报告为
$1.947054437068418$，严格位于 $(19/10,39/20)$；这一字是原完整八点 Gauss
高度规则产生的种子参数，不是准确 scalar 高度积分。以下只用该明确开区间，
对其内任一声明 $H$ 都成立。新种子若另改 $H$，须重新支付相同条件。

令 $\varepsilon=2^{-53}$。R717 的理想轴值为
$X_*=82967/60060,\ Y_*=26399/60060$；准确 dyadic 轴误差各不超过
$7\varepsilon$。因七个非零系数严格交替号，
$$
 p(\varphi)\ge1-\sum_{j=1}^7|\bar c_j|=p(\pi/2)=Y>
 \frac{439}{1000},\qquad
 X<\frac75,\qquad C_\Gamma<\frac{10}{7}+7\varepsilon<\frac{143}{100}.
 \tag{25b}
$$
取 $D_*=21/5,\ h_{\rm mark}=1/1000$，故 $R_B=2099/1000$。
给任意准确有限有理上界 $K_0\ge|\kappa_0|$，明确选择
$$
 0<\eta\le \frac1{100(1+K_0)} .
 \tag{25c}
$$
于是 $\eta\le1/100$，并由 $K_0/(1+K_0)^2\le1/4$ 得
$$
 a_0\eta^2\le\frac1{32000}.
 \tag{25d}
$$
现在逐项可见：
$$
 \begin{aligned}
 2\eta&\le1/50<19/10<H,\\
 a_0\eta^2&\le1/32000<1/200+2\eta/5,\\
 R+2\eta&<59/100<
 439/1000+1/200+(19/10)/5<Y_c+H/5,\\
 C_\Gamma^2+\eta^2&<(143/100)^2+(1/100)^2<R_B^2,\\
 (C_\Gamma+a_0\eta^2)^2+4\eta^2
 &<(1431/1000)^2+(1/50)^2<R_B^2,\\
 (R+2\eta)^2+H^2
 &<(59/100)^2+(39/20)^2
 =41506/10000<R_B^2 .
 \end{aligned}
 \tag{25e}
$$
星形条件(28)也同时满足，因为
$$
 a_0\eta^2(C_\Gamma+1)
 <\frac{243}{3200000}<\frac{439}{2000}<\frac{p_{\min}}2
 \quad\text{可取 }p_{\min}=Y .
 \tag{25f}
$$
因此六个控制点的全部锥、球和星形条件已有非空、明确的选择范围，不是把
“足够小”当作数值结论。特别是核心实际 $F_s=e_z$，$P_2$ 的水平偏移为
$O(\eta^2)$，(25d)确实由 $1/200$ padding 容纳；不存在将错误的水平核心
$F_s=e_r$ 放入本证明的步骤。帽端的 $R+2\eta$ 也已在(25e)单独支付。

(25c)只是一个方便的存在选择，不声称它给出良好的最大曲率。实际输入可以采用
任何满足完整条件的较大声明 $\eta$，但必须按原准确链重新支付长度和曲率。

### 5.2 当前七模图的全角最大弦长

不能用长轴单点替代(22)。以下给出使它真正成为全角最大值的证明。

在 $0<\varphi<\pi/2$，置 $x=\pi-2\varphi$，
$\delta=\Theta-\varphi$。写 $\bar c_j=(-1)^{j+1}a_j$，其中 $a_j>0$。
则
$$
 -p'=\sum_{j=1}^7 A_j\sin(jx),\qquad
 -\delta=\sum_{j=1}^7 D_j\sin(jx),\qquad
 A_j=2ja_j,\quad D_j=\frac{4j^2-1}{2j}a_j .
 \tag{25g}
$$
两列都令第8、第9项为零。理想有理值满足
$$
 A_j^*=-\frac3{32}+\frac{45}{64(2j-1)}
                    +\frac{51}{64(2j+1)},\qquad
 D_j^*=\frac{3}{4j}-\frac3{32}.
 \tag{25h}
$$
对 $1\le j\le6$，
$$
 \begin{aligned}
 A_j^*-2A_{j+1}^*+A_{j+2}^*&\ge\frac4{1105},\\
 D_j^*-2D_{j+1}^*+D_{j+2}^*&\ge\frac1{224}.
 \end{aligned}
$$
第一式来自两个 $1/(2j\pm1)$ 的二阶差
$8/[u(u+2)(u+4)]$；第二式是 $3/[2j(j+1)(j+2)]$。
第7项的二阶差分别为 $A_7^*=7/520$ 和 $D_7^*=3/224$。
每个实际系数的 dyadic 误差使前六个二阶差改变至多
$56\varepsilon$，末项改变至多 $14\varepsilon$，均小于上述严格余量。
所以两列的全部二阶差严格为正。

若 $w_8=w_9=0$，则
$w_j=\sum_{k=j}^7(k+1-j)(w_k-2w_{k+1}+w_{k+2})$。
并且对 $x\in(0,\pi)$，
$$
 \sum_{j=1}^k(k+1-j)\sin(jx)
 =\frac{(k+1)\sin x-\sin((k+1)x)}{2(1-\cos x)}>0 .
 \tag{25i}
$$
严格性可由 $|\sin(nx)|<n\sin x$（$n\ge2$）得到：对应复数等比和的
$n$ 个单位向量在该开区间不可能同向。把(25i)用于两列，得到
$p'<0$、$\delta<0$。

再令 $I(\varphi)=\int_0^\varphi(p(u)-1)\,du$。
它在两个端点为零，且 $I''=p'<0$，所以内部 $I>0$。
准确恒等式 $\delta=p'+I$ 因而给出
$$
 0<-\delta<-p',\qquad |\sin\delta|\le-\delta<-p'.
 \tag{25j}
$$
令 $D_h=\Gamma-Re(\Theta)$，直接求导：
$$
 \frac12\frac{d}{d\varphi}|D_h|^2
 =\rho\left\{p'(1-R\cos\delta)+R(p-1)\sin\delta\right\}.
 \tag{25k}
$$
若 $p\ge1$，括号严格负。若 $p\le1$，由(25j)得到其上界
$$
 p'\{1-R\cos\delta-R(1-p)\}
 \le p'\{1-R(2-Y)\}<0 ,
$$
其中
$R(2-Y)<(57/100)(1561/1000)=88977/100000<1$。
所以 $|D_h|$ 在第一象限严格下降。原两反射与半转把结论传到整个角圆，
从而
$$
 \max_\varphi |P(\varphi)-\Gamma(\varphi)|
 =\sqrt{(X-R)^2+H^2}<\frac{17}{8}.
 \tag{25l}
$$
最后一个严格有理比较使用 $X<7/5$、$R>9/16$、$H<39/20$：
$$
 (X-R)^2+H^2
 <(67/80)^2+(39/20)^2
 =28825/6400<28900/6400=(17/8)^2 .
$$
这里没有改变 $\Gamma$、$\Theta$ 或 $g$，也没有把一个样本的弦长当作全域界。

若原完整 $S$ 的向外包围进一步给出准确有理
$0<\Delta_S\le S-17/8$，则在(25c)之外取
$$
 0<\eta\le \Delta_S/16 .
 \tag{25m}
$$
由于 $K_0\eta\le1/100$，
$7\eta+2a_0\eta^2\le281\eta/40<8\eta\le\Delta_S/2$。
于是(24)严格成立。这给全部六控制点和左端弧长条件的明确共同选择，
但没有把尚未读取的实际 $S$ 记录填成一个数字。
$S$ 必须是完整 FullHold 的物理长度包围，不能拿 integer oracle 的
精度缩放常量 $h.S$、工作 mesh[-1] 或一个局部参考段长度代替。

### 5.3 原完整 $S$ 与明确较宽 handle

既存准确元数据的完整只读返回给出
$$
 \frac{296412483966226858607817}{125000000000000000000000}
 \le S\le
 \frac{2371299871729836522645511}{1000000000000000000000000},
 \qquad \frac{237}{100}<S<\frac{119}{50}.
 \tag{25n}
$$
完整原 initial-law 的实际 $k_0$ 为
$$
 \kappa_0=k_0=\frac{3602879701896397}{18014398509481984}<\frac14 .
 \tag{25o}
$$
第一等号直接来自原完整源的 $a(0)=1,a_s(0)=0,a_{ss}(0)=k_0$ 与
$T_0=a_s e+\sqrt{1-a_s^2}e_z$。它不是 FullHold 的另一个曲率常量 $K$，
也不是某个 working hotspot。初始律 length、velocity 的准确 binary 字分别为
$8106479329266893/9007199254740992$ 和
$5404319552844595/18014398509481984$；全部416个原 scalar knot 未改。

可因此选用较宽的明确参数
$$
 \eta=1/32,\qquad K_0=1/4,\qquad a_0\eta^2<5/16384 .
 \tag{25p}
$$
它不借方便但较小的(25c)，而是直接支付原(19)–(20)、(28)：
$$
 \begin{gathered}
 2\eta=1/16<H,\qquad a_0\eta^2<5/16384<1/200+1/80,\\
 R+2\eta<253/400<Y_c+H/5,\\
 (C_\Gamma+a_0\eta^2)^2+4\eta^2
 <(1431/1000)^2+(1/16)^2<R_B^2,\\
 (R+2\eta)^2+H^2<672409/160000<R_B^2,\\
 a_0\eta^2(C_\Gamma+1)<1215/1638400<439/2000<p_{\min}/2 .
 \end{gathered}
 \tag{25q}
$$
$P_1$ 的球条件更弱，也已支付。完整左端长度进一步满足
$$
 {\cal L}(0,\varphi)\le L_+
 <17/8+7/32+5/8192=19205/8192<237/100<S
 \quad\text{对所有 }\varphi .
 \tag{25r}
$$
这里的物理 $S$ 是原 FullHold 完整域，R690 修改保持该域。
本节从未用 FullHold 的旧 $R$ 代替(25a)的 R690 半径。
第9.1节将用这同一份输入，给出完整右端长度的明确单宽脉冲支付。

## 6. 全角星形截面的直接证明

需要说明(15)中的每个水平截面单绕且不碰原点，而不只证明每条母线正规。

记
$$
 C(t)=b_0^5+b_1^5+b_2^5,\qquad
 E(t)=\frac54\kappa_0\eta^2 b_2^5+
       (R+2\eta)b_3^5+(R+\eta)b_4^5+R b_5^5 .
$$
则
$$
 b=C\Gamma+Ee,\qquad
 \det(b,b_\varphi)
 =\rho\{C^2p+CE[\Gamma\cdot e+\cos(\Theta-\varphi)]+E^2\}.
 \tag{26}
$$
R717 的准确对称性和严格单调性表明，在每个开放象限内，
$\Gamma$、$e(\Theta)$、$n(\varphi)$ 都在同一象限。在坐标轴处按连续值读取。
所以
$$
 \Gamma\cdot e+\cos(\Theta-\varphi)>0,\qquad
 \Gamma\cdot e+\cos(\Theta-\varphi)\le C_\Gamma+1.
 \tag{27}
$$
这使用真实非圆 $\Gamma$ 与真实 $\Theta$，没有假定连续 $O(2)$ 协变。

如果 $E\ge0$，(26)严格为正。若 $E<0$，则 $C>0$ 且
$$
 |E|/C\le a_0\eta^2.
$$
故额外的明确条件
$$
 a_0\eta^2(C_\Gamma+1)<p_{\min}/2
 \tag{28}
$$
给
$\det(b,b_\varphi)>\rho C^2p_{\min}/2>0$。
在 $t=1$ 直接有 $\det(b,b_\varphi)=R^2\rho>0$。
所以整个紧域内 $b\ne0$、$\det(b,b_\varphi)>0$。

绕数是1：随 $t$ 的连续无零水平曲线从原单绕 $\Gamma$ 变到圆，绕数不变；其辐角导数又处处为正。每个截面因而是一条严格星形的嵌入闭曲线。这里“严格星形”不等于凸，不继承凸面刚性或正高斯曲率。

条件(28)同样可随(25)选取足够小的 $\eta$。它没有消耗新的自由物理系数。

## 7. 保住锥和球的完整多项式内缩

对任一正整数 $N$，令 $x=2t-1$，以完整 Chebyshev 多项式
$T_0(x)=1,T_1(x)=x,T_{j+1}=2xT_j-T_{j-1}$ 定义
$$
 \psi_N(t)=(1-x^4)^6\,\frac{1-T_{2N}(x)}2.
 \tag{29}
$$
在 $[-1,1]$ 上 $T_j(\cos u)=\cos(ju)$，因此
$$
 0\le\psi_N\le1,\qquad
 \psi_N^{(j)}(0)=\psi_N^{(j)}(1)=0\quad(0\le j\le6).
 \tag{30}
$$
端点的第七阶零来自 $1-x^4$ 的六阶因子和
$1-T_{2N}(x)$ 在两个端点的额外一阶零。它是一个完整全局多项式，没有隐藏的内部物理切点或角依赖 piece 选择。

单脉冲 $N=1$ 有特别简单的全式
$$
 \psi_1(t)=(1-x^4)^6(1-x^2).
 \tag{31}
$$
它在 $[0,1/2]$ 严格上升，在 $[1/2,1]$ 严格下降，峰值为1。它保留为结构公式的一个例子；实际单一新输入采用第9.1节已支付完整长度区间的单宽脉冲，不并行扫描一组波数。

取固定 $0<\xi_{\max}<1$。对 $0\le\xi\le\xi_{\max}$，定义
$$
 G_\xi(t,\varphi)=
 \bigl((1-\xi\psi_N(t))b(t,\varphi),\ z(t)\bigr).
 \tag{32}
$$
因为收缩系数严格为正且不大于1，
$$
 |(G_\xi)_y|\le |B_y|,\qquad |G_\xi|\le|B|,\qquad
 G_\xi\in{\cal K}_{Y_c,m}.
 \tag{33}
$$
故内缩不会消耗已得的双见证锥距离或原完整球半径上界。
这与任意添加横向 wiggle 不同：后者会改变球半径和另一符号的距离。

在开区间 $z_t>0$；端点由(17)及(30)有
$(G_\xi)_t=5\eta e_z$ 或 $-5\eta e$。所以全域速度从不为零。
所有(18)中的物理端口 jets 保留。

## 8. 唯一正弧长根，不冒用旧三维均值

定义
$$
 {\cal L}(\xi,\varphi)=\int_0^1 |(G_\xi)_t|\,dt.
 \tag{34}
$$
它的 integrand 是 $\xi$ 的仿射向量的范数，所以
${\cal L}(\cdot,\varphi)$ 凸。完整速度非零给全部所需的光滑性。
令 $V=(G_\xi)_t$、$v=|V|$、$T=V/v$，则
$$
 \begin{aligned}
 {\cal L}_\xi&=\int_0^1 T\cdot V_\xi\,dt,\\
 {\cal L}_{\xi\xi}
 &=\int_0^1\frac{|V_\xi|^2-(T\cdot V_\xi)^2}{v}\,dt\ge0 .
 \end{aligned}
 \tag{35}
$$

**定理2（全角弧长根）。**
若对所有 $\varphi$
$$
 {\cal L}(0,\varphi)<S<{\cal L}(\xi_{\max},\varphi),
 \tag{36}
$$
则存在唯一
$$
 0<\xi(\varphi)<\xi_{\max},\qquad
 {\cal L}(\xi(\varphi),\varphi)=S.
 \tag{37}
$$
它在整个角圆上是 $C^2$ 的；对于这里的解析数据实际上光滑。它周期，且保原核心的两反射及半转对称性。

**证明。**
连续性与(36)给存在。设正根为 $\xi_*$。凸函数的切线支撑不等式给
$$
 {\cal L}_\xi(\xi_*,\varphi)
 \ge\frac{S-{\cal L}(0,\varphi)}{\xi_*}
 \ge\frac{S-L_+}{\xi_{\max}}>0.
 \tag{38}
$$
在正根之后导数不能下降，故不可能还有第二根；同理第一个正交叉已经唯一。
式(38)只声称在所证根处有这个下界，没有给整个候选区间随意套用同一个逆界。

隐函数定理和紧角域给完整周期 $C^2$ 根；两个角胞得到的根因同一正交叉唯一性一致，不需要把两条不同的近似根凭标签拼接。对任何原精确反射或半转，(14)、(29)、(32)使长度方程完整相同，因此唯一性直接给对应的 $\xi$ 相同。∎

两个角导数为
$$
 \xi_\varphi=-\frac{{\cal L}_\varphi}{{\cal L}_\xi},\qquad
 \xi_{\varphi\varphi}
 =-\frac{{\cal L}_{\varphi\varphi}
  +2{\cal L}_{\xi\varphi}\xi_\varphi
  +{\cal L}_{\xi\xi}\xi_\varphi^2}{{\cal L}_\xi}.
 \tag{39}
$$
这里的偏导均来自同一个完整(34)，包括其全部参数依赖。没有旧
$v,d,\lambda,B(d)$ 三维 mean 方程，也不能把旧 R726/R727 字段改写为 true 来表达(37)。

## 9. 弧长区间并非空条件：一般有限保证与明确单宽脉冲

定理2只使用脉冲非负、不超过1以及端口的高阶零。第9.1节给出当前准确输入上可直接支付右端长度的一个单宽脉冲；以下先保留一般有限非空论证，不把它作为实际高波数输入。

以下证明在(25)、(28)下总有一个有限多项式可以满足右端长度条件，明确区分**构造非空**与**实际 reach 选择**。

在 $I=[1/4,3/4]$ 上令
$$
 \mu=\inf_{I\times S^1}|b(t,\varphi)|>0,\qquad
 w_0=(15/16)^6>0 .
 \tag{40}
$$
$\mu>0$ 已由第6节和紧性证明，不能用一个 sampled minimum 代替。
完整(26)或全角有理区间可给其可消费下界。

取 $N=3n$，$n$ 为正整数。以 $x=\cos\theta$ 写(29)，在
$\theta\in[\pi/3,2\pi/3]$ 中有恰好 $n$ 个完整脉冲区间：
区间端点的 $\psi_N=0$，中间点的
$\psi_N=(1-x^4)^6\ge w_0$。它们按 $t$ 的实际次序完整覆盖对应的 $I$，未删中间区间。

令 $r(t)=|b(t,\varphi)|$。内缩水平半径为
$(1-\xi\psi_N)r$。在一个上述脉冲区间 $[a,b]$ 及上述中间点 $c$，其总变差至少
$$
 2\xi\psi_N(c)r(c)
 -|r(a)-r(c)|-|r(b)-r(c)|.
$$
求和，再用 $\int_I|r_t|\le{\cal L}(0,\varphi)\le L_+$，得到
$$
 {\cal L}(\xi_{\max},\varphi)
 \ge 2n\,\xi_{\max}w_0\mu-L_+ .
 \tag{41}
$$
因此任何满足
$$
 2n\,\xi_{\max}w_0\mu>S+L_+
 \tag{42}
$$
的有限整数都保证(36)的右端。若只持有有理
$S^+\ge S$、$L^+\ge L_+$、$0<\mu^-\le\mu$，则可准确取
$$
 n=1+\left\lfloor
       \frac{S^++L^+}{2\xi_{\max}w_0\mu^-}
      \right\rfloor,\qquad N=3n .
 \tag{43}
$$
这是一个有限、完全声明的构造公式，不是以无穷波数冒存在。
更好的完整长度下界当然可给更小的 $N$。

**重要范围。** (41)–(43)仅消除了“也许弧长根条件永远不可满足”的逻辑缺口。
它们没有证明高波数满足 $0.03D$ reach。实际采用第9.1节的单个宽脉冲；不能为了让长度条件通过便把大量脉冲当作曲率改善。波数、$\xi_{\max}$、$\eta$ 和全部多项式必须进入新完整 model；若不同输入选择不同 $N$，它们是不同声明的构造，而非被隐藏的执行策略。

### 9.1 单宽脉冲的完整有理非空证明

定义另一族单个全局多项式
$$
 \widehat\psi_k(t)=[1-(2t-1)^{2k}]^7,\qquad k\in\mathbb N_{>0}.
 \tag{43a}
$$
它在两端恰有第七阶零，值及前六阶导数为零；在两个开半区严格上升/下降，
只有中间一个峰且峰值1。因此(30)、(32)–(39)、(44)–(55)的全部论证可逐式使用，
只把 $\psi_N$ 换成 $\widehat\psi_k$。没有内部 cut 或逐角参数选择。

本次唯一声明的实际构造取
$$
 \eta=1/32,\qquad \xi_{\max}=3/4,\qquad k=6 .
 \tag{43b}
$$
这是第84次完整多项式 $(1-x^{12})^7$，不是84个脉冲。
令 $d=1/8$，以 $0,d,1-d,1$ 的三条完整弦长作为曲线长度下界。
写 $g(t)=b(t,\varphi)$、$\psi=\widehat\psi_6(d)=\widehat\psi_6(1-d)$。
核心和帽端的水平三角不等式，以及中间弦的竖直差，给出
$$
 {\cal L}(\xi_{\max},\varphi)
 \ge H+\xi_{\max}\psi(|\Gamma|+R)-E_d ,
 \tag{43c}
$$
其中
$$
 E_d=|g(d)-\Gamma|+|g(1-d)-Re|+z(d)+H-z(1-d).
 \tag{43d}
$$
例如第一条弦长至少是
$\xi_{\max}\psi|\Gamma|-|g(d)-\Gamma|$。
没有把真实积分切向量换成 working unit vector，也没有忽略端层。

在 $d=1/8$，六个完整 Bernstein 权以32768为共同分母，分子依次是
$$
 16807,\ 12005,\ 3430,\ 490,\ 35,\ 1 .
$$
记 $\gamma=(5/4)\kappa_0\eta^2$。由(14)逐项相加得到
$$
 E_d\le\frac{1052(H+\sup_\varphi|\Gamma-Re|)
                 +37730\eta+3920|\gamma|}{32768}.
 \tag{43e}
$$
这个式子包括两端全部水平偏移和竖直亏损，不能只计其中一端。
使用 $H<39/20$、$\sup|\Gamma-Re|=X-R<67/80$、
$\eta=1/32$、$|\gamma|<5/16384$，分子严格小于
$2933+1180+2=4115$，所以
$$
 E_d<4115/32768<63/500.
 \tag{43f}
$$
准确整数比较 $531441\cdot125<4\cdot16777216$ 给
$(3/4)^{12}<4/125$。Bernoulli 不等式因此给
$$
 \psi=[1-(3/4)^{12}]^7>1-28/125=97/125 .
 \tag{43g}
$$
实际声明的高度字还满足 $H>97/50$，这仍只是声明高度而不是准确 scalar 积分。
又有 $|\Gamma|\ge p\ge Y>439/1000$ 和 $R>9/16$。代入(43c)得到
$$
 {\cal L}(\xi_{\max},\varphi)>
 \frac{97}{50}+\frac34\frac{97}{125}
       \left(\frac{439}{1000}+\frac9{16}\right)-\frac{63}{500}
 =\frac{2396873}{1000000}>\frac{119}{50}>S .
 \tag{43h}
$$
结合(25r)，当前固定输入上的完整角圆都满足(36)且有严格余量。
因此这个明确单宽脉冲具有唯一正弧长根和完整两角正则性。
这个非空结论使用真实旧定义的完整 $S$、明确有理参数和全角解析界；
未求数值根，未从有限角的工作 bracket 推断全域。

它仍不支付 principal curvature、Gram 或原 $0.03D$ reach。
单宽脉冲消除了为增加长度而加入多次振荡的必要性，但其所有导数仍须完整进入新六 jet。
当前31、原Slerp种子的 normal、calibration、积分误差或曲率盒不能因此转移。

## 10. 准确弧长重参数化及全部六 jet

将(37)代回(32)，从此 $G(t,\varphi)=G_{\xi(\varphi)}(t,\varphi)$。
定义
$$
 \ell(t,\varphi)=\int_0^t|G_t(u,\varphi)|\,du,\qquad
 s=\ell(t,\varphi).
 \tag{44}
$$
速度严格正，故对每个 $(s,\varphi)\in[0,S]\times S^1$ 有唯一
$t=t(s,\varphi)$。置
$$
 F(s,\varphi)=G(t(s,\varphi),\varphi).
 \tag{45}
$$
于是 $|F_s|=1$，且所有角都使用同一个完整 $s$ 域。
(45)没有把一个角的 arclength table 复用于其它角。

为明确实际六 jet 接口，以下 $G_\varphi,v_\varphi,\ell_\varphi$ 都已包括
$\xi(\varphi)$ 的真实导数，但求偏导时固定 $t$：
$$
 \begin{aligned}
 t_s&=1/v,&
 t_\varphi&=-\ell_\varphi/v,\\
 t_{ss}&=-v_t/v^3,&
 t_{s\varphi}&=-(v_\varphi+v_t t_\varphi)/v^2,\\
 t_{\varphi\varphi}
 &=-\{\ell_{\varphi\varphi}
       +2v_\varphi t_\varphi+v_t t_\varphi^2\}/v .
 \end{aligned}
 \tag{46}
$$
因此
$$
 \begin{aligned}
 F_s&=G_t/v,\\
 F_{ss}&=G_{tt}/v^2-G_t v_t/v^3
       =(I-TT^{\mathsf T})G_{tt}/v^2,\\
 F_\varphi&=G_\varphi+G_t t_\varphi,\\
 F_{s\varphi}
 &=\frac{G_{t\varphi}+G_{tt}t_\varphi}{v}
   -\frac{G_t(v_\varphi+v_t t_\varphi)}{v^2},\\
 F_{\varphi\varphi}
 &=G_{\varphi\varphi}+2G_{t\varphi}t_\varphi
   +G_{tt}t_\varphi^2+G_t t_{\varphi\varphi}.
 \end{aligned}
 \tag{47}
$$
$F$ 本身由(45)给出。这些式子保留长度根、逆弧长及全部两角链导数。
新 provider 的 $T_0,T_{0s},T_{0\varphi},T_{0\varphi\varphi}$ 必须由同一个准确函数计算，不能只给位置后把旧 seed 的角数组接上。

原径向网格仍可表示 $s$ 的准确 affine 点，原外层全胞 Gauss 也可作为工作规则保留；但它们对新(45)的误差必须重新支付。
式(29)是全局多项式，所以没有被省略的内部 cutoff 分支；逆弧长本身仍是新的完整积分/根责任。本文不把 polynomial in $t$ 错称为 polynomial in $s$。

## 11. 完整闭面、全相位、双 held 和直径

现在证明的是参考像本身，不调用 R650 已通过作为前提。

对每个 $t$，由第6节
$\det(b,b_\varphi)>0$。记 $k=1-\xi(\varphi)\psi_N(t)>0$，则
$$
 \det(kb,(kb)_\varphi)=k^2\det(b,b_\varphi)>0.
 \tag{48}
$$
由 $z=z(t)$ 严格单调，同高度只能对应同一个 $t$；每个水平截面又单绕星形，
所以整个上片是嵌入环面片。在内部 $z_t>0$、水平 $G_\varphi\ne0$，故浸入；
在两端由(18)直接正规。弧长重参数化是一个保持边界的微分同胚，不改变像或嵌入性。

把下片定义为 $J_zF(-s,\varphi)$、$s\le0$，$J_z=\operatorname{diag}(1,1,-1)$。
由(18)，核心处完整 $C^2$ 接合。两端各接半径 $R$ 的平盘，cap 外侧加入原固定 p4。
上活动片在 $0<z<H$，只在 cap rim 达到 $z=H$；固定 p4 位于帽内且朝 $z\ge H$ 外侧。
下片同理。因此全部帽、活动、上下反射和标记均没有被省略，也不会靠同高度重叠隐藏自交。
原 $R>9/20$ 及 p4 支持严格在帽内的条件必须保留。

原全相位像为旋转活动片加固定帽：
$$
 S_t=R_{\pi t/2}(\text{upper}\cup\text{lower})\ \cup\ \text{fixed marked caps}.
 \tag{49}
$$
使用原 $\zeta=\Theta^{-1}(\Theta(\varphi)-\pi t/2)$ 材料公式。
旋转保持高度、截面单绕和帽 rim，故上述全闭嵌入及 $C^2$ 接合对全部 $t\in[0,1]$ 成立。
这仍不证明(3)是其每相位诱导度量；该等距条件不可省去。

由于(33)，整个基准上片在安全锥内，下片在反射锥内，两帽及标记由(8)覆盖。
引理1因此给两 held 见证对完整 $S_0$ 的距离均不小于 $d_c$。
两见证确属相位1的核心，故这是 image-Hausdorff 的有效下界，不是同材料位移。

若所有未标记控制点满足(20)并取
$$
 R_B=D_*/2-h_{\rm mark},\qquad h_{\rm mark}=1/1000,
 \tag{50}
$$
则未标记活动与帽都在半径 $R_B$ 的球内；原 p4 在竖直方向增加至多 $h_{\rm mark}$，
故整个 marked 全相位族都在半径 $D_*/2$ 的球内。
任意同片或 mixed pair 的距离均不大于 $D_*$。没有把上下或帽的极值当作可以省略的组成部分。

以 $D_*=21/5$、(10)为例，完整(11)–(12)支付参考族的强 held 比例；
原固定半径 $9/20$ grip 的直径 $9/10>D_*/5$ 也保留。
所有这类结论依赖本节完整参考构造的条件；不是当前31的数值证书。

## 12. 曲率、角向 metric 和 normal 不随这些界自动下降

新的中央物理关系不是 R728 的固定 $d,w,\lambda$ 半波。
式(47)给出了真实材料二阶导数，但 principal curvature 仍须由全部六 jet、
真正第一基本形式和第二基本形式求出。

尤其
$$
 G_{tt,xy}
 =(1-\xi\psi_N)b_{tt}
   -2\xi\psi_N' b_t-\xi\psi_N'' b .
 \tag{51}
$$
提高 $N$ 会提高多项式导数；在脉冲转向处 $\psi_N'=0$ 并不会消去
$\psi_N''b$。故有限长度存在性不提供与 $N$ 无关的曲率上界。
不能把收缩 $|F|$ 的单调性冒充 $|K|$ 或 reach 的单调性。

同样，
$$
 F_s\cdot F_\varphi
 =T\cdot G_\varphi-\ell_\varphi
 \tag{52}
$$
一般不为零。准确单位径向速度只支付 $g_{ss}=1$；
$g_{s\varphi}$ 和 $|F_\varphi|^2-a_{\rm deep}^2\rho^2$ 仍是真正待解量。
本文不提出用重命名角坐标把它们隐藏起来。

对当前完整科学程序而言，新 primitive 在准确定义下满足
$$
 \int_0^S F_s\,ds=P-\Gamma ,
 \tag{53}
$$
但这不等于 working integration、Q、reference calibration 或32阶段闭合链已经计算。
全部原 free core、三 SO3 通道、每个径向自由槽、自由 H、控制范围、
原32阶段、全角/full-radial域与预算必须保留。原 source/point/model/packet/branch 守卫仍然需要新的完整来源分支。

R723 的全闭法管、原 $0.03D$ reach、完整强 $C^2$ 参数性及 R716 的非零中心矩责任也仍独立。
本节不把参考像嵌入替代实际 current field 的 outward/tube 证据，更不从已标记像反推未标记外管。

## 13. 对已存在 R728 分支的完整使用接口

R730 也给当前 R728 一个直接的全域判据，而不用另造 seed 才能使用。
在其真实
$$
 F^-={\cal C}-{\cal A}w
$$
上，逐完整角胞/径向片支付
$$
 F^-_z\ge0,\qquad
 \pm F^-_y-mF^-_z\le Y_c
 \tag{54}
$$
即可调用第2节。线性式必须带入完整 $w=e_r$ 的正交投影、全部 ${\cal A}$ 前缀、
中间间隙及所有端层；不能沿用只对一个中央段成立的符号条件。

这里 ${\cal C}$ 包含全部 scalar 补集、Slerp 端层和完整尾；
所用 mean 必须来自全角准确 R726/R727 根及真实分支接合。
保存的近似 $d$ 非单位、working $\lambda$ 或 positive screen 都不能替代它们。
第2节把实际全叶界换成距离证书，但没有把这些所需全叶界写成已付。

若(54)不成立，并不证明当前曲面离见证球不够远：安全锥只是充分集合。
原完整三维盒距离和 R718/R723 的其它正确界仍可保留取强。
不会因为新锥未通过而删除一片、缩小角域或改变原阈值。

## 14. 从新参考像到实际 outer 场的严格余量账

设本定理参考闭像为 $S_{\rm ref}$，真实完整当前闭像为 $S_{\rm cur}$。
若以同一材料域完整证明
$$
 \sup |F_{\rm cur}-F_{\rm ref}|\le e_{\rm act},
$$
并分别覆盖两帽与标记的真实高度差，则得到全像
$d_H(S_{\rm cur},S_{\rm ref})\le e_T$；不得只使用上片误差。
若当前核心两相位见证 $q_{\pm,\rm cur}$ 相对参考见证满足
$$
 |q_{\pm,\rm cur}-q_\pm|\le e_q,
$$
则
$$
 \operatorname{dist}(q_{\pm,\rm cur},S_{\rm cur})
 \ge d_c-e_T-e_q .
 \tag{55}
$$
证明是对完整目标点取下确界的三角不等式。当前 $X$ 必须读取所有实际核心系数，
不能只因前三固定就把 $e_q$ 置零。帽的 H 改动也必须进入 $e_T$。

若实际完整 $D_{\rm cur}\le D_+$，则
$d_c-e_T-e_q\ge D_+/5$ 才支付对应实际强 held 条件。
参考证书并没有免除 whole-normal 分支、完整六 jet 或这些同场误差。
原 source-bound R723/R716 接口不能只收到本证明的路径就改为 true。

## 15. 可实施的最小新种子接口

本文授权的是一种明确构造，不是一组新优化试验。最小独立科学实现需要：

1. 用真实 fixed scalar/reference 读取 $S,R,\kappa_0$、声明的 $H$，以及全160个固定初始核心字；
   保原准确 $\Gamma,\Theta,\rho$ 及完整 target。
2. 将声明 $\eta=1/32$、$\xi_{\max}=3/4$、单宽脉冲 $k=6$、完整(14)及(43a)写入新 physical model。
   准确长度根的全角存在由(25r)、(43h)给出；实际 working 根、积分误差和后续 normal 仍须完整重算。
3. 在每个请求角解同一个完整标量(37)，保存完整长度残差、根区间/工作值及(39)的两角量；
   再以(44)的同一真实函数反解每个准确材料查询，给完整(47)。
   原三维球面 mean 的12个数组不能作为这条新定义的伪装返回值。
4. 新全局多项式没有内部 cutoff 拼接点；原 scalar/reference 的全部外部数据和原径向域仍完整保存。
   任何积分表、反解表和工作缓存必须绑定角、完整输入、该新 model 和 source。
5. base、Q、reference calibration、normal helper、packet、pure validator 需要明确的新来源/定义分支。
   能原字共享的通用数学可以共享；真正读取旧 mean/profile 字段的分支必须实际适配。
   不可只换 hash，或把旧 R727/R728 attribution 改为 true。
6. 科学仍只在公开 Actions 内执行；原变量、完整观察、32阶段、误差预算和正式/实时读数不因新种子缩减。
   准确后继必须支付长度根、逆弧长、所有两角导数及新工作积分误差，不能套旧 chord/Slerp 径向公式。

(19)–(24)、(28)、(36)是本构造自身的数学域和真实根条件，不是另加一个外部测试或审核 gate。
未满足时应有明确、完整的未付/失败报告；不能借另一个角的根、旧 working field 或缺失片来填补。

## 16. 完整来源与本次未做的计算

本证明直接核对以下完整来源。所有身份指完整文件，不是截取片段或同名旧版本。

| 来源 | 完整路径（题目录内） | 字节 | SHA-256 |
|---|---|---:|---|
| R717 | results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md | 24028 | 9727ed8b7e48d9aa4a343c1d3dcd666a9fbc0d74f876df1ee80494df7b337378 |
| R728 | results/R728-reversed-paired-halfwave-prefix-and-held-witness-distance.md | 23587 | 3a26814cfcf960be2a7c78ed92a00cf24f10c683f01a36daf85cea7e2b82f36e |
| 当前反号 seed | scripts/resume_20261126/fixed_fejer_R728_reversed_spherical_halfwave_meridian_reference.py | 53384 | c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86 |
| 当前 base | scripts/resume_20261126/fixed_fejer_r728_meridian_operator.py | 40877 | 427227b006741b809fc728d4c4d23fe7fa59f2ccbf5e020e15fc8ed0b730168c |
| 当前 geometry | scripts/resume_20261126/so3_fixed_fejer_r728_demanded_geometry.py | 88452 | bd176ef337575a88f1666479f27d94d503d7d776771ec3e444705e0aea0528ee |
| 固定 reference | scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py | 60335 | e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb |
| 固定 input maker | scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py | 39375 | 89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60 |

R728最末目标域澄清使用已发表 edef57558f257fda998b876ac6c819cb1b2b6539 的全文；
Git blob c70f38f8e0cc7c1e21aa245861db73cf673411ac。
当前31完整运行表是
computations/fixed-fejer-r728-demanded-current-runtime-binding.json，
74756字节，SHA-256
4af8d6d8ca43a8bc62005e091e0b3baddb6e0e382f0ba6c6ac62247678f3c4ea，
Git blob d79fd8c5e889f826585cd4ddaf64aeadbc0ef369。

原完整 R690 半径小记录为 Git blob de466e6b062e907841addc20455f43f99485dabe，
3345字节，SHA-256 51e486744a71195bdd19b0540d3299b8a839e4dcf7c21ebcac655e6659302d36；
它明确保留未达请求积分精度、全部无限尾仍覆盖的状态。完整 FullHold 源为
notes/2026-11-17-parallel-model-full-hold-oracle.py，11694字节，SHA-256
 a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670，
Git blob c52508fb931e8381a0f53cdd9991ef65427cedd7。实际 H 的范围只按原参考声明字解释，
本证明没有把它提高为准确 scalar 积分。

原 $S$/initial-law 完整只读来源为
notes/2026-11-28-public-actions-46108296054-1-part-002.md 第6阶段，
固定提交106767818ea8aed67cf6f74880abd9cee73d3dd2，
52652字节，SHA-256 47cf7953ed91408f689a58e70fc290fa931a46a652b418a16c5a86fb52300b6a，
Git blob9d4f30eae551516c9ee5357d3ec46f19606eb548。
完整元数据输出22366字节，SHA-256
038b92a34f6a33a40efeac7da4bff53e710ce22a999fe02c70f7b23ae26a9151；
原完整preparation为65325字节/c04003dc4e5e0eb6024df422507e6d5df4ecd3a0ceaa27d1280783363d277945，
原完整scalar输入40488字节/2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189。
该第6阶段的90个标量投影均有值，无summary错误；它只读取既存全源元数据，
$F/J/\mathrm{normal\ roots}/\mathrm{new\ integrations}$ 均为0。
第5阶段原13个非标量summary错误仍保留；没有冒称最初没有错误。
完整原定义来源 e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa
与(25a)的 R690 半径来源分开保留，不把原 FullHold 半径改名。

本文没有运行科学代码、AST、fixture、数值积分、均值根、normal根或网格。
没有填入任何未来源、model、point、报告或证书身份。
证明的新增结论是上述完整参考构造及其可消费条件；当前实际场的角向 metric、
$0.03D$ reach、强 $C^2$ 相位要求和 Euclidean 非全等仍保持原任务标准。
