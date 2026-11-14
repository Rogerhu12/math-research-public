# R79：同一精确桥的势结构与双屏障普通源反馈

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明（固定背景结构及条件接口）；全文独审通过。** 本文沿用 R21 第 2 节已经证明
并固定的唯一 exact bridge；不重新选择度量，不把旧图的 metric-transfer
证书移用到本轮候选。本轮新图仍须运行自己的 bridge/metric 证书。
这里仅证明同一背景函数的真实势结构与所需反馈门，没有新 PDE 或尾请求。

## 1. 已有精确桥与 raw Target 的区别

R21 已全文独审：旧 M8/M12 的目标 $g$ 共用同一精确桥根，两份桥证书
的 exact_pt、exact_ps、exact_L 包围、根区间及两端符号相同。源
scripts/db6f-root-exact-bridge.py 用有理 Taylor 积分异号与正导数下界
证明唯一根，并把 raw Target 误差转移到这个共同精确目标。

因此“精确匹配的背景桥存在”不是当前新缺口。前一实际端口报告讨论
raw Target 的冻结二进桥时保留的端点差，不能被读成忽略这一已审结果。
下面采用的正是 R21 的精确桥；若以后讨论本轮有限几何，仍需绑定它自己
的新转移证书，不能把背景定义相同当作新几何已经认证。

记同一精确 cut 半径为 $a_c$（原 binary .6），
$$
w=\frac12,\quad E=1+w^2=\frac54,\quad
w_r=-\frac{7w}{a_c},\quad
p=\frac\pi2-\arctan w,\quad
p_s=\frac{w_r}{E^{3/2}}<0.
\tag{1}
$$
这里 $\sigma=-1$。既有唯一桥长满足
$$
\frac35<L<\frac7{10},\qquad
L\int_0^1\sin\varphi(t)\,dt=1-a_c.
\tag{2}
$$
置 $d=-Lp_s>0$，则原 cubic turn 精确写为
$$
\varphi(t)=(3p+d)t^2-(2p+d)t^3,\qquad 0\le t\le1,
\tag{3}
$$
$$
a(s)=1-L\int_0^{s/L}\sin\varphi(t)\,dt,\qquad
c=a_s=-\sin\varphi,\qquad z_s=\cos\varphi.
\tag{4}
$$
本稿直接全文读过上述 exact-bridge 源，以及原
DirectionalBridge.turn/profile，并回读 R21 的同一目标 $g$ 证明。

## 2. 足够宽裕的严格参数和相位界

原 binary 半径满足 $599/1000<a_c<601/1000$。
由 $3<\pi<22/7$、$\arctan(1/2)<1/2$ 及其四项交错 Taylor 下界，
$$
1<p<\frac{111}{100}.
\tag{5}
$$
后一比较可完全写为
$$
\frac{11}{7}
-\left(\frac12-\frac{(1/2)^3}{3}
+\frac{(1/2)^5}{5}-\frac{(1/2)^7}{7}\right)
<\frac{111}{100}.
$$
又因为 $E^{3/2}=(5/4)\sqrt{5/4}>11/8$，
$$
0<-p_s<\frac{28000}{6589}<\frac{17}{4},
\qquad
0<d<\frac{19600}{6589}<3.
\tag{6}
$$

由 (3)，$\varphi(t)>0$ 对 $0<t\le1$ 成立。
其导数只有一个内零点
$$
t_*=\frac{2(3p+d)}{3(2p+d)}
=\frac{6p+2d}{6p+3d}\in(2/3,1).
\tag{7}
$$
$\varphi$ 先严格上升、后严格下降，最大值为
$$
\varphi(t_*)=\frac{4(3p+d)^3}{27(2p+d)^2}.
\tag{8}
$$
该表达式对正 $p,d$ 都严格递增，因为其对数导数分别为
$$
\frac9{3p+d}-\frac4{2p+d}>0,\qquad
\frac3{3p+d}-\frac2{2p+d}>0.
$$
所以用 (5)–(6) 的上端即可严格核得
$$
\varphi(t_*)<
\frac{4(633/100)^3}{27(261/50)^2}<\frac75.
\tag{9}
$$
$\cos(7/5)$ 的四项交错 Taylor 下界给
$$
\cos(7/5)>
1-\frac{(7/5)^2}{2}
+\frac{(7/5)^4}{24}
-\frac{(7/5)^6}{720}>\frac16.
\tag{10}
$$
因此整个桥确有 $z_s=\cos\varphi>1/6$，不是仅由采样检查声称其保持
正图。半径由 (2)、(4) 严格下降，故
$$
a_c\le a\le1,\qquad a>\frac{59}{100}.
\tag{11}
$$

## 3. 桥的真实 Sturm 势与两个屏障

沿用已独审的精确 Sturm 变量
$x=\beta/\alpha$、$y=\pi/\bar p^3$、
$dr/ds=1/(a^2\bar p)$。由 $\bar p=1/\cos\varphi$，势为
$$
V=\frac{a^3a_{ss}}{(1-c^2)^2}
=-\frac{a^3\varphi_s'}{\cos^3\varphi}.
\tag{12}
$$
(7)、(10) 因而给准确符号：
$$
V<0\quad(0<t<t_*),\qquad
V=0\quad(t=t_*),\qquad
V>0\quad(t_*<t\le1).
\tag{13}
$$
这条桥不满足“全段 $V\le0$”。它自己有一个非正势段和一个右侧非负
外区；将其与第一周期相接之后，第一周期的中央负势段与此桥的负势段
之间，存在第二平段和末个严格正势 ramp。

按方程 $y_{rr}+n^2Vy=0$ 的符号，这就是两个指数型区间之间有一个
振荡型区间的双屏障排列。此名称只陈述真实符号结构，不声称某个具体
整数频率已发生共振，也不宣称候选不存在。

实际桥起点也不是把第一周期的二次零点继续成同阶零点。以桥起点为
$s=0$，由 (3)、(4)：
$$
V(s)=-\frac{2(3p+d)}{L^2}s+O(s^2).
\tag{14}
$$
第一周期的左邻势则以二次方式趋零；桥内部 $t_*$ 是简单零点。
整个连接仍有 $a\in C^2$、$V$ 绝对连续，正是前述局部非线性及能量
证明允许的范围。不能未经证明把它替换成两侧光滑的简单根模型，也
不能因此给全题添加 $C^3$ 门。

## 4. 实际桥的有效有限区间输入

记桥的 Sturm 长度为 $R_b$，负势段长度为 $\ell_b$。由
$dr/ds=\cos\varphi/a^2$、(2)、(7)、(10)、(11)，
$$
R_b<
\frac{7/10}{(59/100)^2}<\frac{21}{10},\qquad
\ell_b>\frac16\frac35\frac23=\frac1{15}.
\tag{15}
$$
写 $A_1=6p+2d$、$B_1=6p+3d>A_1$，则
$\varphi_s'=t(A_1-B_1t)/L$。正最大值至多
$A_1^2/(4B_1L)<A_1/(4L)<53/10$，负最大绝对值在终点，
由 (6) 小于 $17/4$。故
$$
|\varphi_s'|<53/10,\qquad |V|<216(53/10)<1200.
\tag{16}
$$
这些都是完整区间的严格界，不来自有限采样。

在右侧正势外区 $[t_*,1]$，写
$$
V=\omega\,v_b,\qquad
\omega=\frac{a^3}{\cos^3\varphi},\qquad
v_b=-\varphi_s'>0.
\tag{17}
$$
$a$ 与 $\varphi$ 都递减，故 $\omega$ 递减；
$\varphi_{ss}''=(A_1-2B_1t)/L^2<0$，故 $v_b$ 递增。
并有
$$
\frac15<\omega<216,\qquad 0\le v_b<17/4,\qquad 0\le V<918.
\tag{18}
$$
$\omega>1/5$ 来自 $a_c^3>(59/100)^3>1/5$。

对第 $n$ 模取 $m=\langle n\rangle^{-1}$、
$q=\sqrt{V+m^2}$、$S=\operatorname{diag}(1,q)$。
与前一频率证明同样，正势区的能量增长只有
$|n|m/2$ 和 $(\log q)'_+$。
沿向前方向，$\omega$ 的正变差为零，$v_b$ 单调，故
$$
\exp\int(\log q)'_+\le\sqrt{1+918\langle n\rangle^2}
<31\langle n\rangle.
$$
沿反向方向，$v_b$ 的正变差为零，$\omega$ 的比值小于1080，故
$$
\exp\int(\log q)'_+<\sqrt{1080}<33.
$$
两方向都可用 $33\langle n\rangle$。
再用 $\|S\|<31$、$\|S^{-1}\|\le\langle n\rangle$、
$e^{R_b/2}<e^{21/20}<3$，得到真实双向外区传播
$$
\boxed{\quad
\|T^{Z,b}_n(r_2,r_1)\|
<3100\langle n\rangle^2
\quad(r_1,r_2\hbox{ 在桥的右正势外区}).\quad}
\tag{19}
$$
常数因子为 $31\cdot33\cdot3=3069<3100$。
普通源同样由实际变常数公式给
$$
|Z_n(r_2)|\le3100\langle n\rangle^2
\left(|Z_n(r_1)|+\int|g_n|\,dr\right).
\tag{20}
$$
左外区为空；(15)、(16)、(19) 是将单中央屏障的弱 Dirichlet/通量
证明用于桥自身的具体输入。这里没有用这些输入跳过桥内部源估计，也
没有把桥与周期的级联合并当作仍是一个屏障。

## 5. 两个实际模块的内部反馈

设第一周期和桥的精确 Hadamard 两端口散射矩阵分别为
$\mathcal S^c_n,\mathcal S^b_n$。它们均由实际有限维背景 ODE 定义，
满足逐模酉性，cross-channel 是相应传递块的非零倒数。
设它们的普通源输出为 $f^c_n,f^b_n$。在共享界面处 $a=1,c=0$，
Sturm 变量和通量基完全相同，故可以直接接线。

令 $I_L,I_R$ 为整个前缀的外端 incoming，
$u$ 为第一周期右 incoming（等于桥的左 outgoing），
$v$ 为桥的左 incoming（等于第一周期右 outgoing）。接口两式是
$$
\begin{aligned}
v&=(\mathcal S^c_n)_{21}I_L+
   (\mathcal S^c_n)_{22}u+f^c_{R,n},\\
u&=(\mathcal S^b_n)_{11}v+
   (\mathcal S^b_n)_{12}I_R+f^b_{L,n}.
\end{aligned}
\tag{21}
$$
所以真正内部反馈分母是
$$
\boxed{\quad
\Psi_n=1-(\mathcal S^b_n)_{11}(\mathcal S^c_n)_{22}.
\quad}
\tag{22}
$$
右边源项完整为
$$
(\mathcal S^b_n)_{11}(\mathcal S^c_n)_{21}I_L+
(\mathcal S^b_n)_{12}I_R+
(\mathcal S^b_n)_{11}f^c_{R,n}+f^b_{L,n}.
\tag{23}
$$
此式特别保留两个模块的普通源列，不能只接齐次解。

每个有限整数模都有 $\Psi_n\ne0$，因为两个 reflection 的模都严格
小于一；这只给逐模存在，未给一致的 tame 界。设
$r_c=(\mathcal S^c_n)_{22}$、$r_b=(\mathcal S^b_n)_{11}$，
$t_c,t_b$ 为各自 cross transmission，则
$$
|\Psi_n|\ge1-|r_br_c|
\ge\frac{|t_c|^2+|t_b|^2}{2}.
\tag{24}
$$
第二步由酉性和
$\sqrt{(1-A)(1-B)}\le1-(A+B)/2$ 得到。
右边没有现成的统一正下界；逐模非零不可当作全空间有界逆。

更准确地，若 $r_br_c=\rho_ne^{i\vartheta_n}$，则
$$
|\Psi_n|^2=(1-\rho_n)^2+
4\rho_n\sin^2(\vartheta_n/2).
\tag{25}
$$
明确取常数 $\gamma>0$、有限实数 $q\ge0$ 和整数 $N\ge1$。
一个足够且可逐项核验的高频门是：对所有 $|n|\ge N$ 且 $\rho_n\ge1/2$ 的模
$|\sin(\vartheta_n/2)|\ge\gamma\langle n\rangle^{-q}$；
而 $\rho_n<1/2$ 的模自动有 $|\Psi_n|\ge1/2$。
该门在已覆盖的高频范围给
$$
|\Psi_n|\ge
\min(1/2,\sqrt2\gamma)\langle n\rangle^{-q},\qquad |n|\ge N.
\tag{26}
$$
若要整个频率空间的有效界，还须并入有限头部：
$$
c_*=\min\left\{\frac12,\sqrt2\gamma,\min_{|n|<N}\langle n\rangle^q|\Psi_n|\right\}>0.
$$
有限头部的定性正性来自逐模非零；要有效常数必须给实际有限核查，不能以未测的数值代替。
只要高频条件和有限头部真正支付，接口普通源消元仅再损失有限 $q$ 次角导数；
(21)–(23) 可据此接入相应加权空间。

本文没有计算或证明当前所有高模的真实 $\vartheta_n$ 满足 (26)，
没有把另一简单根轮廓的相位展开移植过来，也没有以“可能产生势阱”
冒充已经发现具体失败模。这里将剩余门定位到同一固定背景的准确
反射乘积，而不是任意选取的 Hadamard 边界。

## 6. 仍需与实际闭合一起支付的部分

除了内部反馈 $\Psi_n$，原平面核心与真尾 Robin/非线性 DN 还给
实际端点反馈；其准确行见
notes/2026-11-10-78718-geometry-actual-port-transfer-v1.md。
两种反馈不要混成一个已可逆的算子。

以上是径向背景的完整符号/能量结构。当前非径向候选的真实线性化、
无限尾普通源、全低模/mean/标量行，以及最终闭图的几何和误差认证，
均不能由本稿代付。本稿未使用候选数据数组，未执行新 tail 或 PDE，
也不改变主数值问题的同一 $g$ 或原完成标准。

## 7. 冻结来源、完整独审与条件量词

[冻结原稿](../notes/2026-11-10-78718-geometry-bridge-two-barrier-feedback-v1.md)9860B，
SHA256 `9336712dd04a7fc8ecd29b72997a3284074a11b4f4b65bea2da8ef3de075fbaa`；
[全文未参与者独审](../notes/2026-11-10-78718-audit-bridge-two-barrier-feedback-v1.md)13074B，
SHA256 `b2ce9b33cbc3ba2d292de0b8a89a5cae5d17448a3833205fef01110f081c5f79`。
root689181全文回读。正式稿按审稿明确gamma、q和高频/有限头部量词，未把条件相位门认作已验证；
其余数学公式不变，冻结原稿不改。

[有限符号/有理检查](../scripts/78718-geometry-bridge-two-barrier-check.py)
SHA256 `86794b2b29ba3cbb307eb6c64488375b1d65e8aa9a791873ce7911ac93375ec6`。
未参与者真实4e7715自然exit0，8符号/16有理；
[独立报告](../notes/2026-11-10-78718-audit-bridge-two-barrier-check-01.json)2084B，
SHA256 `c24bde9204804cfc303a01b141afcd9e4e287d0e8c00bfdc0a8498721a3e6325`。
0root求解/PDE/tail/候选数组，未重算已审唯一桥根。
