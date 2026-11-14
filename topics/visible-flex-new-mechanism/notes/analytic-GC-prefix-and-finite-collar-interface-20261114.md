# 准确解析 GC 前缀与有限外带的接口

日期：2026-11-14。作者：`/root/mechanism`。

**状态：已证明的局部存在及接口结论；数值长度、误差界和完整连接仍未支付。** 本稿应用 [R2](../results/R2-mixed-modes-local-eccentric-drift.md) 已证明的一阶解析 Gauss–Codazzi 正常形，说明一个真正等距入口怎样接入现有逐圈 $\Pi$ 表示。没有运行新几何、没有改当前固定度量或正在审计的参数，也没有启动新的求解。

这里的作用不同于只补 $u_4,v_7,b_6$：前缀若能得到经过控制的评价，它满足完整局部等距方程。其外仍是尚待求解的连接，不能把局部存在延伸成闭面存在。

## 1. 固定输入与一侧 Cauchy 兼容

取已冻结的完整度量

$$
g=ds^2+a(s)^2d\theta^2,\qquad \theta\in\mathbb R/(2\pi\mathbb Z).
\tag{1}
$$

令 $s_c$ 是准确柱段结束处，$x=s-s_c$。这里只使用 $x\ge0$ 的第一个解析径向片。规定 $a$ 在该片有一个实解析延拓，且

$$
a(0)=a_0>0,\qquad a'(0)=a''(0)=0.
\tag{2}
$$

当前旧固定 $g$ 的首段是 S5 原函数乘已冻结的 `exp(log-radius)`；其 body log 扰动从 $x^5$ 开始。局部新核心的半径差还乘 S11 cutoff。它们在各自第一个断点之前都有明确的一侧解析定义。此处必须读取完整已冻结表达式，不能把含 body 的 $a$ 换成未设计 seed。

设 $\Gamma(\theta)$ 是准确材料弧长参数下的解析严格凸平面闭曲线，

$$
\Gamma_\theta=a_0T_0,\quad |T_0|=1,\quad
(T_0)_\theta=k(\theta)\nu_0,
\quad \nu_0=e_z\times T_0,\quad k>0.
\tag{3}
$$

$k$ 是材料角转速；平面曲率是 $k/a_0$。指定侧别 $\sigma\in\{1,-1\}$ 和唯一空间位置，初值为

$$
X(0,\theta)=\Gamma(\theta)+z_*e_z,
\qquad X_s(0,\theta)=\sigma e_z.
\tag{4}
$$

这已支付初圈的 $E=1,F=0,G=a_0^2$。对角向长度求 $s$ 导数还迫 $a'(0)=0$，与 (2) 一致。若左侧是准确直柱，则完整位置二jet要求 $X_{ss}(0)=0$，这正需 (2) 中的 $a''(0)=0$；仅给 $a'(0)=0$ 的一般 R2 局部解不自动能以 $C^2$ 接到直柱。

以下法向固定为 $n=e_1\times e_2$，其中 $e_1=X_s,e_2=X_\theta/a$。初始 $n_0=\sigma\nu_0$。写第二基本形式为

$$
\mathrm{II}=L\,ds^2+2M\,ds\,d\theta+N\,d\theta^2.
$$

真实初值因此是

$$
M(0,\theta)=0,\quad N(0,\theta)=\sigma a_0k(\theta),
\quad L(0,\theta)=0.
\tag{5}
$$

特别地 $|N(0,\theta)|\ge a_0\min k>0$。不可任意另外选择 $N$、重置截面中心，或在固定 $g$ 下把这些边界量当作独立设计参数。

## 2. 真正的一阶解析系统与局部结论

在 $N\ne0$ 处令

$$
L=\frac{M^2-aa''}{N},\qquad
M_s=L_\theta-\frac{a'}aM,\qquad
N_s=M_\theta+\frac{a'}aN+aa'L.
\tag{6}
$$

展开第一式的角导后，右边只依赖 $s,\theta,M,N,M_\theta,N_\theta$，没有二阶角导。于是 (5) 与 R2 的一阶 CK 定理给出某个统一 $\epsilon_*>0$ 上的唯一解析解。缩小区间可同时保证

$$
a>0,\qquad |N|\ge\tfrac12a_0\min k,
\qquad |(e_2)_z|<\tfrac12.
\tag{7}
$$

最后一项保证后面使用的切向标量图没有极点。R2 的紧初圈管域论证还给更小区间上的真实嵌入；没有给本题所需的定量宽度或全闭面 reach。

这个局部存在不要求 $K=-a''/a$ 为负。初段若 $a'=-Cx^3+O(x^4)$、$C>0$，则 $K>0$ 紧邻右侧仍可用解析 CK。但该径向 Cauchy 演化不是通常的稳定双曲初值问题：其主矩阵特征值为

$$
\frac{M\pm\sqrt{aa''}}{N}.
\tag{8}
$$

在 $a''<0$ 区间它们非实。不能据“径向一阶”就承诺增加 Fourier 频率后普通 ODE 积分稳定，也不能把小实网格残差单独当作严格 Cauchy 误差界。

对当前首项，(6) 给

$$
L=\frac{3\sigma C}{k}x^2+O(x^3),\qquad
M=-\frac{\sigma Ck_\theta}{k^2}x^3+O(x^4).
\tag{9}
$$

它们属于同一真实局部解，重新产生 [R64](../results/R64-convex-core-entry-seventh-tangent-and-sixth-center-jets.md) 的必要 leading 系数；不是彼此独立调配的切向和高度多项式。

## 3. 周期、标架和位置闭合不另欠 monodromy 条件

系数及初值均 $2\pi$ 周期。CK 局部唯一性把平移 $\theta\mapsto\theta+2\pi$ 后的解与原解识别，因此 $M,N,L$ 周期。令 $E=(e_1,e_2,n)$，采用 R2 的矩阵

$$
U=\begin{pmatrix}0&0&-L\\0&0&-M/a\\L&M/a&0\end{pmatrix},
\qquad
V=\begin{pmatrix}0&-a'&-M\\a'&0&-N/a\\M&N/a&0\end{pmatrix}.
\tag{10}
$$

GC 正好给 $V_s-U_\theta+[U,V]=0$。先逐角解

$$
E_s=EU,\qquad E(0,\theta)=(\sigma e_z,T_0,\sigma\nu_0).
$$

斜对称性保持正交正定向，周期系数与周期初值保持 $E$ 周期。误差 $D=E_\theta-EV$ 满足 $D_s=DU,D(0)=0$，故 $D=0$。接着按唯一初始位置定义

$$
X(s,\theta)=\Gamma(\theta)+z_*e_z+\int_0^s e_1(r,\theta)\,dr.
\tag{11}
$$

它周期，且 $X_\theta-ae_2$ 的径向导数为零、初值为零。因此 $X_\theta=ae_2$，完整三项度量准确成立。环带的角向位置和标架闭合在这里已经逐式保留，没有调用仅适用于单连通局部片的结论来跳过 monodromy。

数值截断仍须报告其实际角闭合、正交、积分性误差；上述证明不允许数值后处理逐圈改中心或任意配平端点，除非把它们明确列为另一种近似评价。

## 4. 椭圆对称使逐圈 $\Pi$ 表示完整

一般 R2 初圈会产生横向中心漂移，故不能普遍写成只有竖直中心的表示。当前椭圆有

$$
\Gamma(\theta+\pi)=P\Gamma(\theta),\quad
P=\operatorname{diag}(-1,-1,1),
$$

以及 $\Gamma(-\theta)=S\Gamma(\theta)$、$S=\operatorname{diag}(1,-1,1)$。同一解析初值问题的唯一性给

$$
X(s,\theta+\pi)=PX(s,\theta),\qquad
X(s,-\theta)=SX(s,\theta).
\tag{12}
$$

初始位置中的竖直常量不破坏这两式。于是 $\langle X_x\rangle=\langle X_y\rangle=0$，水平切向分量在 $\theta+\pi$ 下变号，而 $T_z$ 在 $\theta\mapsto-\theta$ 下为奇函数。**并非整个 $T$ 都是 $\pi$ 反周期。**

取唯一零均值周期原函数 $\Pi$。因为 $T=e_2=X_\theta/a$，准确有

$$
X=a\Pi T+z_c e_z,\quad z_c=\langle X_z\rangle,
\quad b=z_c'=\langle(e_1)_z\rangle.
\tag{13}
$$

这没有丢掉当前对称类的横向中心，也没有给每个截面加入任意平移。固定 $z_c(0)=z_*$ 后，整段只有同一个共同原函数。

在 (7) 的切向图中写

$$
T=\frac{(-\sin(\theta+u),\ \cos(\theta+u),\ v)}{\sqrt{1+v^2}}.
\tag{14}
$$

$v=T_z/|T_{xy}|$；$u$ 由初始分支连续提升。初始水平切向绕数为一，缩短区间后不穿极点，所以 $u$ 是周期实函数；不存在逐点 `mod` 或重新 unwrap 的额外物理选择。它们继承既有二重／反射闭合对称。

## 5. 切口完整二jet及可计算递推

在某个已经选定并验证的 $0<\epsilon<\epsilon_*$，GC／GW 直接给出

$$
\begin{aligned}
X_s&=e_1,&X_\theta&=ae_2,&X_{ss}&=Ln,\\
X_{s\theta}&=a'e_2+Mn,&
X_{\theta\theta}&=-aa'e_1+Nn.
\end{aligned}
\tag{15}
$$

对逐圈表示，所需切向径向两阶为

$$
T_s=\frac Ma n,
\qquad
T_{ss}=-\frac{ML}{a}e_1-\frac{M^2}{a^2}e_2
 +\left(\frac{M_s}{a}-\frac{Ma'}{a^2}\right)n.
\tag{16}
$$

高度数据由同一解得

$$
b=\langle(e_1)_z\rangle,\quad
b'=\langle L n_z\rangle,\quad
b''=\left\langle L_s n_z-L^2(e_1)_z-\frac{LM}{a}(e_2)_z\right\rangle.
\tag{17}
$$

位置 $C^2$ 接合需要 $u,v$ 的 $0,1,2$ 阶径向函数、$b,b'$ 和唯一 $z_c(\epsilon)$。角向及混合导数由这些完整角函数的真实导数得到；若延用当前更强端口 API，解析性还提供 $ss\theta$ 等所需量。不能只让有限角采样上的几个值相等就称完整二jet已匹配。

一种直接递推是写 $M=\sum M_jx^j,N=\sum N_jx^j$，按幂级数除法形成 $L=(M^2-aa'')/N$，逐阶用

$$
\begin{aligned}
(j+1)M_{j+1}&=\partial_\theta L_j-[(a'/a)M]_j,\\
(j+1)N_{j+1}&=\partial_\theta M_j+[(a'/a)N+aa'L]_j.
\end{aligned}
\tag{18}
$$

GW 同样给标架及位置系数。每一步是明确的有限运算，但完整角函数不得在物理定义中被任意截断。

对椭圆，可在偏心角 $\varphi$ 上工作，避免把材料反解误差混入每次角导。令

$$
q(\varphi)=\sqrt{A^2\sin^2\varphi+B^2\cos^2\varphi},\quad
\partial_\theta=\frac{a_0}{q}\partial_\varphi,
\quad k=\frac{a_0AB}{q^3},
\quad d\theta=\frac q{a_0}d\varphi.
\tag{19}
$$

若 $A>B>0$，可先选复角带 $|\operatorname{Im}\varphi|<\rho<\operatorname{arctanh}(B/A)$；这是 $q^2$ 的最近复零点之前的明确范围。正实支解析延拓，$q$ 及初始 $N$ 不为零。圆情形单独用常值 $q$，不除 $A-B$。

## 6. 何谓“固定前缀长度已支付”

CK 给存在某个正长度，不给 $.081$ 或任何当前误差峰位置的覆盖保证。实际前缀必须同时满足：

1. $\epsilon$ 不越过尚未处理的首个完整 $a$ 解析断点；body knot、seed 段界和新核心 cutoff 都计入。
2. 所选复域上 $a$ 和 $N$ 保持可用的逆界；实域上标架和切向图保持正则。
3. 给出截断／积分误差控制，或至少先做同一完整 $a$、同一 $\epsilon$ 的可复现精化；改变 $\epsilon$、$a$ 或入口不是同场精化。

严格数值版本可从 (18) 和复带输入建立 CK majorant、明确其径向收敛半径及解界。若已证明某个 $|x|<r$ 上解的解析范数上界为 $C$，那么截断阶数 $p$ 的 $j$ 阶径向尾可按

$$
\frac C{r^j}\sum_{n>p}\frac{n!}{(n-j)!}
\left(\frac\epsilon r\right)^{n-j}
\tag{20}
$$

控制；角导再使用保留复带宽的 Cauchy 界。这只是可计算误差机制，当前没有实际建立所需 $C,r,\rho$，更不能从有限实网格反推它们已存在到目标长度。

若跨已知径向分段边界继续，可以把左侧完整解析角 trace 当右侧新 Cauchy 数据；须再次保 $N\ne0$，且 $a,a',a''$ 接合一致。这样 (15) 保位置 $C^2$。此步没有新增任选端口自由度，也没有保证能一直走到帽。

## 7. 有限外带如何准确支付整个二jet

切口上的数据是整圈函数，一般不属于现有有限 Fourier／椭圆角列。有限几个常数不能匹配任意这样的函数。但可以把它们作为固定基场的一部分，有限未知只负责外部余项。这与当前“准确核心固定、有限内部系数可变”的接口原则相同。

例如在连接过渡 $s\in[s_c+\epsilon,s_c+\epsilon+\ell]$，令 $t=(s-s_c-\epsilon)/\ell$。取三组左 Hermite 多项式

$$
\begin{aligned}
H_0(t)&=1-10t^3+15t^4-6t^5,\\
H_1(t)&=t-6t^3+8t^4-3t^5,\\
H_2(t)&=\tfrac12t^2-\tfrac32t^3+\tfrac32t^4-\tfrac12t^5.
\end{aligned}
$$

它们在左端满足 $H_j^{(i)}(0)=\delta_{ij}$，右端 $0,1,2$ 阶全零。对任一标量 $f=u,v$，使用完整切口函数 $f_j^-(\theta)$ 及给定外场函数 $f_j^+(\theta)$，

$$
f_{\rm base}(s,\theta)
=\sum_{j=0}^2\ell^j\left[
H_j(t)f_j^-(\theta)+(-1)^jH_j(1-t)f_j^+(\theta)\right].
\tag{21}
$$

再加两端灭径向二jet的有限基。于是所有系数都准确保整个切口二jet，而不是靠最小二乘罚项近似匹配。公式 (14) 自动保单位切向；上述角对称保闭合。**这个 lift 只支付接合，不支付中间的 $E=1,F=0$。** 历次大跨度高阶 lift 的数值失败还说明不能仅凭 (21) 就选很长支持并预告好初态。

高度可用相应 Hermite 基匹配 $b,b',b''$。若希望在过渡右端还恢复指定的旧共同中心，只需一个归一化径向 bubble

$$
\beta_\ell(s)=\frac{140}{\ell}t^3(1-t)^3,
\qquad\int\beta_\ell\,ds=1.
\tag{22}
$$

它及前二导在两端为零。把 $b_{\rm base}$ 加上

$$
\left[z_{\rm target}-z_c(\epsilon)
      -\int b_{\rm base}\,ds\right]\beta_\ell
\tag{23}
$$

便一次性支付唯一中心积分条件。不是逐截面独立平移，也不保证 $|b|\le1$、中间高度、曲率或外带等距。

## 8. 若要求所有参数下都恢复旧外域

仅让基场恢复旧外域不足以保全部可变状态。可以对旧有限切向列乘一个固定 $W(s)$：前缀上为零，过渡右端以完整二jet回到一；在首端至少三阶开启。这样切向自由度不污染准确前缀，而过渡外保原列。

高度列还需其**积分**恢复。设旧列为 $C_j(s)$，取 (22) 支撑在同一过渡内，令

$$
\widetilde C_j(s)=W(s)C_j(s)+d_j\beta_\ell(s),\qquad
d_j=\int_0^{s_c+\epsilon+\ell}(1-W)C_j\,ds.
\tag{24}
$$

这里 $W=0$ 覆盖整个新固定前缀，$W=1$ 覆盖右外域。则前缀高度自由列为零，右外域 $\widetilde C_j=C_j$，而其从共同原点的积分也与旧列相同。配合 (23) 的固定中心恢复，(13) 的逐圈 $\Pi$ 规范给出：**过渡外对应任意参数的全部位置二jet准确恢复旧场。** 横向部分没有额外的径向积分平移。

这是有限未知的可实施接口，并不要求增加每个角点的自由位置。完整切口函数、过渡长度、$W$、bubble、每个 $d_j$ 和新高度基都必须进入新的物理／空间身份。即使外域保持原场，也不能将新前缀称为旧物理态或只改评价规则。

## 9. 仍未解决的事项与下一执行边界

固定 $g$、初圈和 $X_s$ 后，解析 Cauchy germ 是唯一的。它没有可随意调节的有限端口旋钮；在 $N\ne0$ 的解析延拓范围内，准确外解也必须与这个 germ 的后续延拓一致。因此“固定完整二jet + 有限外部基”不保证任一固定有限空间含准确零，更不证明能接到六帽。它允许的是一个清楚的同度量近似序列，误差是否下降仍须真正求解和检验。

当前实测入口峰离 $s_c$ 有有限距离。极短的准确前缀可能只修掉更小区域，旧峰仍留在过渡里。若不能得到覆盖有用长度的解析误差控制，就不能把这个方案当作已经解决入口。

本稿只确定以下可执行顺序：保持选定完整 $g$ 和核心；从 (6) 产生并验证一个明确短前缀及其完整 trace；把 trace 作为固定函数按 (21)—(24)接入；只在明确的新物理身份下评价初态和外域，再决定外部优化。当前已部署的 `5d383918…` 单态审计及现有硬约束保持原样。没有新增实际求解或本地候选计算。
