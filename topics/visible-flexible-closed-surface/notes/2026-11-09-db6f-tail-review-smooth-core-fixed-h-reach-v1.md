# 完整独审：光滑固定 H 圆柱核、先升后降的鞍领与边界 reach

独立审查人：tail_review_continued_2。2026-11-09。
本审查没有参与被审稿的平面核、两扇区约束、曲率剖面、几何界或非全等证明。
依 root 分工，只新建本题小文本，不改作者冻结正文、HANDOFF、LOG 或 results。
执行器失联期间按已授权的文本后备保存；本文没有终端、PDE、几何轨迹或网格执行。

**结论：接受被审稿的完整有边族存在性结论；没有发现需要作者勘误的数学阻断。**
它实际给同一固定材料环带上的联合光滑等距族、逐点固定且具有非空内部的 H、
全部时间的嵌入及 reach 下界，并排除每个非零参数像与初态的全 E(3) 全等。
完整初态直径满足 D<9/4，握持直径/D>2/3，全部时间 reach/D>1/18>3/100。
这些结论属于仍有两条边界的环带；有效的 0.05D 像幅度、指定接缝、闭曲面和最终整链运行均未支付。

## 1. 不可变来源与依赖身份

主稿：
- 路径：notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md。
- 固定提交：[be7b380055c1906a1abacfc5682da0e372ef8579](https://github.com/Rogerhu12/math-research/blob/be7b380055c1906a1abacfc5682da0e372ef8579/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1.md)。
- Git blob：543ec104f6038f84ea05ea8f11d05445b02d72d8。
- UTF-8：17,561 B。
- SHA-256：45d197cbc2b3f6c103ecd131b8bf3f49fb374fad5cc9a900a3d45dd29f5e2687。

作者有理门回执：
- 固定提交：[3df775c15ba3ed8da72b1f761a8a14350f6536df](https://github.com/Rogerhu12/math-research/blob/3df775c15ba3ed8da72b1f761a8a14350f6536df/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-smooth-core-fixed-h-reach-v1-receipt.md)。
- Git blob：65f23366981312078e1f8282ba6a91224886ab49；2,241 B。
- SHA-256：66aeb7dbab1afe9224223024fabca695d47be7eafe3ced3221d9166f4a2f3889。
- 作者在 23:43:40 UTC 的 10 PASS 是作者运行，不算本次独立运行。

两份存在定理均按其完整证明和准确假设使用：
- 非减 Q 原稿 a07c2b1357e8e0a11bc0a7d15d28b6a16352b51b，blob f992cc801bc78e58c3ac174a5f6daaf2d22eff34，SHA-256 8fb0a24d0eba4841e31520665cf793081fc38e9dba67190190cf7665307b30f0。
  本审查人已另行完成全文独审，报告固定在
  [0fbb537133c97af06cf55ca3939f002f5cfb17ad](https://github.com/Rogerhu12/math-research/blob/0fbb537133c97af06cf55ca3939f002f5cfb17ad/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-increasing-q-smooth-flat-entry-v1.md)，
  blob f65f80b4e840a43cdba50eedb241815f9b597778，18,289 B，
  SHA-256 ff451747fda004ba3f1926719ce4229f3063a7368d276aace0c08d0007e6dc33。
- 非增 Q 原稿 9daa8aba8a341855811d2f1c164bfb3ca7eab0bc；
  完整独审固定在
  [15b02049c367e344901fb13264a950f8ff5bf933](https://github.com/Rogerhu12/math-research/blob/15b02049c367e344901fb13264a950f8ff5bf933/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-monotone-flat-collar-smooth-data-v1.md)。

主稿冻结时把第一份定理列为待审，符合当时事实。
本报告按上述新独审核组合的全部假设，不改写冻结主稿的历史身份。
我已读取主稿全部 11 节、作者小回执及两份定理的对应准确陈述。
原稿正文与回执均重新计算 UTF-8 字节数和 SHA-256，全部符合上述绑定。

## 2. 两个真实位移约束给闭合、共同单位速率的平面核

记 omega=2pi/3。原 T_0、nu_0 是水平单位正交对，且 nu_0=e_z×T_0。
h 和两个控制函数在扇区边界邻域恒零，其标量 omega 周期延拓确实光滑。
因此 f_tau 的标量周期性给 T_tau(theta+omega)=R_z(omega)T_tau(theta)；
cos、sin 组合同时精确保留单位长度。

两个首扇区位移分量对 alpha 的导数为

\[
G=\int_0^\omega \chi\,\nu_0\nu_0^{\,T}\,d\theta .
\]

对非零水平向量 z，
z^T G z 是 chi 乘 (z·nu_0)^2 的积分。
chi 在开弧严格正，而非零正弦余弦组合不能在开弧恒零，所以 G 严格正定。
有限维光滑隐函数定理据此解的是完整非线性位移方程；
没有把一次变分为零当作真实闭合。

以固定 gamma_0(0) 积分后，首扇区末值正好 gamma_0(omega)。
角向导数的 C3 关系再给整个位置的 C3 关系：
gamma_tau(theta+omega) 与 R_z(omega)gamma_tau(theta)
导数相同，并在 theta=0 处同值。
迭代三次得到实际周期位置。这里没有未固定的积分平移量。

材料 theta 已是共同单位速率，周长恰为 2pi。
控制区和自由区不交，在自由区 f_tau=tau h；
只要 tau 非零，该角函数就不恒零，同时它在固定邻域恒零。
这也排除了仅有材料重参数的非平凡性。

缩小一个共同的 tau 邻域，使 |f|<=1/100、|f'|<=1/10 是合法的：
alpha(0)=0 且整个有限维族在所有光滑范数连续。
固定紧区间 tau∈[0,tau_1] 后，后续所有选择都针对这同一个族。

曲率为 1+f'，故在 [9/10,11/10]。
总转角仍为 2pi。原稿的切线支撑论证正确：
从任意起点看内法向投影，其导数在切向转角 0 到 pi 为正，
从 pi 到 2pi 为负；闭合使末投影返回零，中途严格为正。
这给严格凸性。独立的全局弦下界同时直接给单射。

对最短角差 d_theta<=pi，
沿该弧积分 |T_tau-T_0|<=|f_tau|<=1/100，得到

\[
|\gamma_\tau(\theta)-\gamma_\tau(\phi)|
 \ge 2\sin(d_\theta/2)-d_\theta/100
 \ge (2/\pi-1/100)d_\theta
 > (3/5)d_\theta .
\]

周期闭合保证跨越角坐标接缝也可这样积分。
pi<22/7 由稿中正积分恒等式推出，因此 2/pi>7/11；
689/1100>3/5 核对无误。

若某个非零 tau 的像是圆，正曲率、单位速率和周长 2pi 迫使曲率恒为1，
于是 f'_tau=0；固定开弧又迫使 f_tau=0，和自由区矛盾。
所以非圆性对每个充分小的非零 tau 成立，不只是一阶变分非零。

## 3. 固定开握持片及其材料身份

负 r 圆柱图 F=gamma_tau+r e_z 精确诱导 dr^2+dtheta^2。
取 e_1=e_z、e_2=T_tau、N=nu_tau 时，
L=M=0、C=kappa_tau，和稿中的角向框架方程逐项相符。

每个扇区边界附近切向量都等于 T_0。
完整首扇区位移约束给各扇区端点位置等于原端点；
从两端分别积分，得到边界两侧整个开邻域的 gamma_tau=gamma_0。
因此 H 的逐点固定来自实际位置恒等，不需要事后欧氏对齐。

H 的径向区间有正长度，三个角区间也有正长度，
所以作为材料二维集合有非空内部。
r=-h_0/2、theta=0 和 omega 的两点都属于 H，
其初态像距离为 sqrt(3)>3/2。
不存在把周长变化或材料滑动补偿成固定 H 的问题。

## 4. 共同曲率剖面和统一系数界

S 的分母处处正，在两端分别恒0、恒1；
中间一个指数项递增，另一个递减，故 S'≥0。
拼接后的 Q_delta 在 r=0、delta、2delta 附近均为常数，
所以全为 C-infinity；它先非减、后非增，
并在 [3delta/4,5delta/4] 恰为1。

标量方程 a''=Q/a 从 a(0)=1、a'(0)=0 出发。
在解存在且正的区间，Q≥0 先给 a≥1；
继而 a''<=1，积分得

\[
0\le a'\le r,\qquad 1\le a\le 1+r^2/2 .
\]

这些界同时阻止在固定小窗失去正性或发生有限值爆破，
故延拓到稿中固定窗合法。
mu=a'/a 和 beta=aa' 因而具有与 delta 无关的统一界。
这一选择的 a_delta、Q_delta 对被动参数 tau 完全固定。

上升段所用 Q_up 在完成上升后继续恒1，仍满足相同界。
下降段在 r=delta 后用平移后的径向变量；
可以预先限制候选 delta<=1/200，并取例如不超过 1/4 的固定下降窗，
使整个系数窗落在上述 0<=r<=1/2 的控制内。
这里只是在定理允许的固定小窗内使用同一界，没有使用 Q' 的大小。

## 5. 两段共同寿命、交接 H4 和最后一次选 delta

这是本应用的关键依赖，已单独核对。

上升初值 X_0=0、Y_0=1/kappa_tau，
满足正 Y_0 下界和统一 H5/H4 数据界。
因此非减 Q 定理给一个与 delta 无关的 T_up。
其混合能量在 Q=1 处控制 X、Y 的实际 H4 范数；
一般公式 X=P+QZ 中本应用的 P 甚至恒为0。
Y 的正下界也统一保留。

正式的选择顺序可写成：
先得到 T_up，再只考察
0<delta<min(1/200,T_up/2) 的交接数据。
这些数据在同一 H4 有界集内，具有同一个正 Y 下界。
非增 Q 定理准确要求的正是 X_0、Y_0 的 H4 和正下界，
故对全部这些交接数据给同一个 T_down>0。
这一点不要求交接的全部径向导数对 delta 一致有界。

两段在 Q=1 的开领使用同一 a 和相同交接初值。
在交接右侧的非空重叠内，唯一性使两实际 PDE 解完全相同；
上升解又已定义到交接左侧，因此拼接后联合光滑。
对应 a 的一致性来自标量 ODE 相同初值与同一 Q=1 系数。
这里不是只匹配有限个径向 jet。

下降能量即使在 Q=0 处仍控制 X 的 H4 和 Y 的 H3；
结合 Y 正下界，足以控制 M=X/Y、C=1/Y 的 C1 角范数。
上升段的界更强。于是原物理方程给统一的

\[
|M_r|+|C_r|\le K_*,
\]

因为右端只含 M、C、一次角导数和 Q、mu、beta，
没有 Q'。K_* 对上述全部候选 delta 统一。

现在取同一个正 delta，同时小于
1/200、T_up/2、T_down/2，并满足 2delta K_*<1/10。
这仍有正选择空间，且不会反过来改变已经统一的寿命常数。
从 M(0)=0、C(0)∈[9/10,11/10] 径向积分，得到

\[
|M|\le1/10,\qquad 4/5\le C\le6/5
\]

贯穿整个两段和全部 tau。
固定这一 delta 后，材料域、度量、曲率剖面及参数区间全部固定。
没有循环地先以某个 delta 的寿命选择自己，也没有逐时间改变材料几何。

两个定理的参数结论都适用：
每次使用时 a、Q 对 tau 固定，而初值光滑依赖 tau。
上升给光滑交接初值，下降再给光滑族；
不需要对作为剖面尺度的 delta 宣称统一高阶参数界。

## 6. Gauss–Codazzi 实现为实际位置与全 jet 接合

给定主稿的 L,M,C，LC-M^2=-Q=-aa''。
径向正交框架 ODE 具有反对称系数，故正交性保持。
初值角向关系在原圆柱上逐项成立：
e_1,theta=0，e_2,theta=kappa N，N_theta=-kappa e_2。

Gauss–Codazzi 正好保证角向误差的径向方程齐次；
初始误差为零，所以 F_theta=ae_2 和其余角向框架关系在整个带上成立。
实际度量因此等于共同 g_delta。
实际周期初值和周期系数通过 ODE 唯一性给周期位置；
C3 同理保持。没有遗留的平移 monodromy 或可另选的出口高度。

在 r<=delta/4，Q=0、a=1，
M=0、C=kappa_tau 是物理系统的实际平稳解。
唯一性给它等于所构造的解，继而径向框架恒定，
F=gamma_tau+r e_z。
所以与负 r 原柱面在开领上相同，全部 Cartesian jet 相合。
H 在原柱面内部，始终逐点固定。

末段 r>=7delta/4 具有 Q=0、a 仿射。
中间 Q 严格正，故 a'(2delta)>0、a(2delta)>1。
此时 C>=4/5 且 LC-M^2=0，第二形式确为非零秩一。
a'(2delta)<=2delta<1/100，所述小锥角界也正确。
该终端没有被误称为平面端或已匹配的封帽。

## 7. 实际 Cartesian Hessian 的谱范数估计

由 0<=Q<=1、M^2<=1/100、C>=4/5，
有 |M^2-Q|<=1，故 |L|<=5/4。
实际 Cartesian 二阶导数为

\[
F_{rr}=LN,\qquad
F_{r\theta}=a'e_2+MN,\qquad
F_{\theta\theta}=-aa'e_1+CN.
\]

对任意平直参数方向 h=(h_r,h_theta)，法向系数是
h^T S_coord h，其中

\[
S_{\rm coord}=
\begin{pmatrix}L&M\\M&C\end{pmatrix}.
\]

把它拆成对角矩阵和非对角矩阵，算子范数至多
max(|L|,|C|)+|M|<=5/4+1/10=27/20。
这是合法的谱范数界；没有把三个绝对值无区别相加。
若改写为正交切标架中的形算子，因 a>=1，其对应上界也不会更大；
本次 Taylor 估计实际需要的是上述坐标二次型。

法向之外仍有切向项
2a'h_r h_theta e_2-aa'h_theta^2 e_1。
三角不等式和 2|h_rh_theta|<=h_r^2+h_theta^2 给

\[
|\text{切向项}|
 \le |a'|\{h_r^2+(a+1)h_\theta^2\}
 <(3/100)|h|^2.
\]

所以 |D^2F[h,h]|<=69|h|^2/50<2|h|^2。
这里仅用 a<2、a'<1/100；没有遗漏 Christoffel 切向部分。
负 r 圆柱的方向二阶导数界为11/10，
故整个固定材料域可统一使用 Taylor 常数 H_*=2。
即使 Q' 随 delta 变大，这个二阶位置界仍保持不变。

## 8. 全局弦下界确实支付嵌入

共同参考图 B_tau=gamma_tau+r e_z 在整个材料域定义。
其竖直和水平弦正交，中心曲线弦界给

\[
|B_\tau(p)-B_\tau(q)|
 \ge (3/5)\sqrt{(\Delta r)^2+d_\theta^2}.
\]

对正 r，直接积分实际二阶导数：

\[
|F_r-e_z|\le(5/4)r\le(5/2)\delta,
\]
\[
|F_\theta-\gamma'_\tau|
 \le r(1/100+1/10)\le(11/50)\delta .
\]

负 r 上差为零。因而 D(F-B) 的算子范数至多
(68/25)delta<17/1250<1/10。
这里使用两列范数之和作为算子范数上界是保守且有效的。

给定两个材料点，取最短角 lift，在闭径向区间与该角 lift 中连直线段。
这个段始终可行；跨周期接缝也无碍，因为 F、B 具有真实周期性。
沿段积分 D(F-B)，得到

\[
|F_\tau(p)-F_\tau(q)|\ge
(1/2)\sqrt{(\Delta r)^2+d_\theta^2}.
\]

所以全域单射。共同正度量保证浸入，
紧材料域上的单射浸入是所需的真正嵌入。
没有用局部浸入、采样网格或仅中心曲线嵌入代替整张带的嵌入。

## 9. 带边界最近点论证与 reach>=1/8

对任意空间点 z，紧像确保最近点 F(p) 存在。
取任意其他材料点 q，并沿上一节的可行最短角 lift 直线段前进。
无论 p 是否位于径向边界，距离平方在起点的一侧最小性都给

\[
(z-F(p))\cdot DF(p)(q-p)\le0.
\]

边界处只需要这个可行方向条件，
无需、也不能强加 z-F(p) 垂直整个切平面。

记 d=|z-F(p)|、h=q-p 为上述 lift 差。
H_*=2 的方向二阶界给 Taylor 余项至多 |h|^2，
全局弦下界又给 |h|^2<=4|F(q)-F(p)|^2。
因此

\[
(z-F(p))\cdot(F(q)-F(p))
 \le 4d\,|F(q)-F(p)|^2,
\]

从而

\[
|z-F(q)|^2-|z-F(p)|^2
 \ge(1-8d)|F(q)-F(p)|^2.
\]

若 d<1/8，任何不同像点都严格更远，最近点唯一。
这正好证明整个有边紧像的 reach>=1/8，且常数对全部时间共同。
co-Lipschitz 常数在换算时已经平方；没有漏掉因子2，
也没有借用无边闭曲面的 reach 公式。
参数圆周只要求选一个最短 lift，并不妨碍这条全局证明。

## 10. 全图初态直径、握持比例与全部欧氏群

初态中心曲线是单位圆。径向速度恒为1，
所以任一点到对应 gamma_0(theta) 的距离至多 h_0+2delta。
这虽比 max(h_0,2delta) 保守，却足以给整张新图

\[
D\le2(1+h_0+2\delta)<111/50<9/4.
\]

D 包含负 r 柱面和整个新领，没有以中心曲线直径或领宽替代。
结合握持的 sqrt(3)>3/2 和 reach>=1/8，严格得到

\[
\operatorname{diam}F_0(H)/D>2/3,\qquad
\operatorname{reach}F_\tau(M_\delta)/D>1/18>3/100.
\]

整体空间缩放 b 后两个长度界同时乘 b，比例保持。

底边长度2pi，顶边长度2pi a(2delta)>2pi。
任何使两完整像全等的欧氏等距都限制为有边嵌入曲面的内在等距；
它把边界分量映到边界分量并保持长度，因此不能交换上下两边。
底边必映到底边。

初态底边是单位圆。非零 tau 的底边 gamma_tau-h_0 e_z 非圆，
所以不存在这样的全等。
该论证没有使用欧氏等距的定向，包含反射和所有可能的平移旋转。
不需要假定对方刚体保留材料标号、C3 轴或预先指定的 H。

进一步，若固定两个紧像的 E(3) 商 Hausdorff 下确界为0，
取逼近刚体列。一个固定像点的有界距离迫使平移部分有界，
正交部分属于紧群 O(3)；子列极限给真实全等，矛盾。
故每个非零参数的商像距离严格正，
普通像 Hausdorff 变化及固定握持允许下的像变化亦严格正。

这只排除每个非零参数与初态全等；
没有冒称任意两个非零参数之间均已区分，
也没有得到可用的位移幅度数值下界。

## 11. 实际独立有理重放：10 PASS

独立运行身份：
tail-review-smooth-core-fixed-h-reach-rationals-01。

从主稿固定提交提取其唯一 JavaScript 围栏，
仅去除围栏前的末端换行，得到与作者记录逐字相同的 1,529 ASCII B 源：
SHA-256 c9d69ab537bf2319cd93aa85ef9a871e6ebbaac1abdd7970df6c87586a9f0bb8。
围栏若计入终端换行为1,530 B，其 SHA 是
d1ac96aaf5c51094b3764d7a01da3e79f272026f993295311a7cb148ed09862f；
两种计数的差仅此一个换行。

完整读过源后，直接在 functions.exec 的 JavaScript/V8 隔离运行时执行该原始表达式。
clock 工具开始和结束都实际返回 2026-11-09 23:52:18 UTC。
函数实际正常返回，functions.exec 实际显示 Script completed，10 项全部 PASS。
没有终端 shell，因此不宣称 shell exit0。

| 冻结门名 | 左端 | 右端 | 实际结果 |
|---|---:|---:|---|
| core chord | 3/5 | 689/1100 | PASS |
| a upper | 20001/20000 | 2 | PASS |
| diagonal maximum | 6/5 | 5/4 | PASS |
| normal plus tangent Hessian | 69/50 | 2 | PASS |
| full derivative error | 17/1250 | 1/10 | PASS |
| remaining global chord | 1/2 | 733/1250 | PASS |
| whole initial diameter | 111/50 | 9/4 | PASS |
| grip chord squared | 9/4 | 3 | PASS |
| grip diameter ratio | 1/5 | 2/3 | PASS |
| reach ratio | 3/100 | 1/18 | PASS |

这个实际重放只核原源列出的10项精确有理比较。
例如 H/D>2/3 的严格来源仍是第10节的几何和直径推导，
而不是把代码里名为 grip diameter ratio 的较弱比较改写成另一个已执行门。
隐函数定理、两个 PDE 定理、位置兼容、E(3) 和 reach 的论证由全文数学审查支付。

## 12. 准确接受范围与仍未支付的目标

本次接受完整固定 g 的实际 C-infinity 有边族：
真实周期和材料 C3、同一材料 H 的逐点固定、
H 的非空内部及尺寸、全部时间的嵌入和归一 reach，
每个非零参数相对初态的全 E(3) 非全等，
以及有限径向位置的非零秩一平坦终端。
非解析局部 bump 使用已经完整独审的两份光滑数据定理，
没有借用不适用的角解析 CK。

仍未给有效 tau_1 或 delta 数值，也未给0.05D像位移下界。
两个材料边界仍存在；平坦端不是零 II 平面端，且锥角仍小。
没有指定 R43 接口、封帽、闭曲面、几何网格、PDE 数值解、
主 flat17 的 G5 或最终从种子独立复算的全链。
所以这份接受不等于题目 README 的完成。

本次新数学程序仅第11节的独立 BigInt 有理门。
没有执行任何隐函数求根、PDE/BVP、DN、tail、RK、连续后台、
主优化数组读取、几何导出或矩阵测试。
