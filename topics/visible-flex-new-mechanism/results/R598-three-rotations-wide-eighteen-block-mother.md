# R598：同点 first 槽的三旋转平均与宽十八完整块母

日期：2026-11-26。**完整原式纸证；没有执行新求根、求积、符号或 ODE。**
本文从起点另选固定 profile。它把 R578 的 36 个完整块改为18个，
保全部低阶矩与完整 history，把微半宽从 $1/500000$ 改为
$1/12000$。不是在旧母上移动节点，也不继承旧 run 的状态或 $\chi$ 数值。

新库仍只提供 R521/R530/R584/R590 的实际完整方程输入；不授八矩根、
pose、pointwise fourth period、有限精确等距族或 README 几何比例。
第6节给出新输入的真实尺度与原几何坐标预算，明确何处只是尺度改善。

## 1. 为什么当前特殊母只需三旋转

沿用 R578 的32个真实不交微包。在每一点，
未旋转完整块满足
$$
F=\alpha u,\qquad G=\beta u,\qquad\alpha\beta=0.
\tag{1}
$$
所有阶混合导数乘积同样为零。固定
$$
\varphi\in\{0,2\pi/3,4\pi/3\},\qquad
f_\varphi=\cos\varphi F-\sin\varphi G,\quad
g_\varphi=\sin\varphi F+\cos\varphi G,
$$
$$
\phi_{\varphi,\theta}
=f_\varphi\cos\theta+g_\varphi\sin\theta
=\cos(\varphi-\theta)F-\sin(\varphi-\theta)G.
\tag{2}
$$
写
$$
q_{\varphi,\theta}
=\cos^2\varphi-\cos^2(\varphi-\theta),\qquad
\Delta_0=F\odot F-G\odot G.
$$
由(1)，实际所有二次密度及真二尾准确有
$$
D_{\varphi,\theta}=q_{\varphi,\theta}\Delta_0,\qquad
J_j^{\varphi,\theta}=q_{\varphi,\theta}J_j^0,\quad j=0,1,2.
\tag{3}
$$
这里 $J_2$ 仍含原 $2(F')^2-2(G')^2$；微包间不重置尾。

R586 的转置式证明，完整 fourth 与全部中心化第三更新只含两类角结构：

- QQ：两个 $\Delta_0$ 的线性输出；
- LLQ：**同一材料点**的两个 first jets，乘一个 $\Delta_0$ 的线性输出。

同点性质不能只靠次数计数猜测，逐原式说明如下。
R586(20) 的 $\mathfrak P_j[\phi](y)$ 乘 $C_{\rm loc},T,W$
或 chain，其余 first 槽也在该 $y$；$J$ 已转置，未留下另一 first
位置。R586(22) 的 $\mathfrak P_j[\phi](y)$ 分别乘同一 $y$
处的 $\phi,\phi',\phi''$ 和 $q_A$；$q_A$ 可保真二尾，但尾只含
$\Delta$，不是第二个非局部 first 槽。R586(26) 的两个 first jets
显然同点；(23)(25) 只有 QQ。实际时间导数和对已有实际路径的时间
积分不改变这个空间位置结构。因此这一判断包括有序 $B[M,A]$、
完整 $c$、$G$、$\mathscr L$、原 third chain 和真实历史；没有只看
$A=0$ 的局部 probe。

对三个角平均，频率 $0,\pm2,\pm4$ 被准确积分。直接三角恒等式给
$$
\operatorname{Av}_\varphi q_{\varphi,\theta}^2
=\frac{\sin^2\theta}{2},
\tag{4}
$$
$$
\operatorname{Av}_\varphi
\cos^2(\varphi-\theta)q_{\varphi,\theta}
=-\frac{\sin^2\theta}{4},\qquad
\operatorname{Av}_\varphi
\sin^2(\varphi-\theta)q_{\varphi,\theta}
=\frac{\sin^2\theta}{4}.
\tag{5}
$$
令当前微包的 $D_0=\alpha^2-\beta^2$。
由(1)(5)，同点 first 系数 $C_{\varphi,\theta}$ 满足
$$
\operatorname{Av}_\varphi C_{\varphi,\theta}^2q_{\varphi,\theta}
=-\frac{D_0}{4}\sin^2\theta.
\tag{6}
$$
因此 R586 的全部形式投影在三旋转下仍准确成立，
并统一乘 $\sin^2\theta$：
$$
D^aJ^{\mathbf b}P\longmapsto
\frac{\sin^2\theta}{2}D_0^a(J^0)^{\mathbf b}P
\quad(a+|\mathbf b|=2),
$$
$$
C^2D^aJ^{\mathbf b}P\longmapsto
-\frac{\sin^2\theta}{4}D_0^{a+1}(J^0)^{\mathbf b}P
\quad(a+|\mathbf b|=1).
\tag{7}
$$

这没有否定 R521 §5 对一般母的反射要求。一般非局部或重叠 first
槽可保一个反对称 $SO(2)$ 型；本稿以(1)和原式转置支付其在当前
特殊输入中的消失。不能把“三旋转足够”推广到任意 profile 圆。

## 2. 三组六正节点，包括两端 Radau 规则

仍取 R578 的明确多项式
$$
P_5(x)=\frac{63x^5-70x^3+15x}{8},\quad
P_6(x)=\frac{231x^6-315x^4+105x^2-5}{16},
$$
但三组参数改为
$$
\tau\in\{-1,0,1\},\qquad q_\tau=P_6+\tau P_5.
\tag{8}
$$
其六根记为 $x_{\tau,1}<\cdots<x_{\tau,6}$。
$q_{-1}$ 的最大根为 $1$；$q_1$ 的最小根为 $-1$，
端点导数分别为 $6,-6$，均简单。其余根按 $P_5$ 五根交错，
在相应开子区间中各一根；因此18根全简单。
不同 $\tau$ 无共同根，否则 $P_5=P_6=0$，三项递推降至 $P_0=1$
矛盾。R578 的 $|\tau|<1$ 根支延拓到这两个简单端点。

令 $L_{\tau,i}$ 为相应五次 Lagrange 基，取
$$
w_{\tau,i}=\frac12\int_{-1}^1L_{\tau,i}(x)\,dx.
\tag{9}
$$
对 $\deg p\le10$，除法 $p=q_\tau r+t$ 给
$\deg r\le4,\deg t\le5$。$P_5,P_6$ 对全部四次以下多项式正交，
所以仍有
$$
\sum_iw_{\tau,i}p(x_{\tau,i})
=\frac12\int_{-1}^1p(x)\,dx,\qquad
w_{\tau,i}=\frac12\int_{-1}^1L_{\tau,i}^2>0.
\tag{10}
$$
端点没有改变此证明。特别每组权和为1。

实际位置固定为
$$
c_{\tau,i}=5+\frac{99}{100}x_{\tau,i}.
\tag{11}
$$
三组实际0…10次位置矩完全相同，目标是
$\frac12\int_{-1}^1p(5+99x/100)\,dx$；
不能把它当作旧 R578 的另一个未经说明的相同位置图。

## 3. 十八节点的严格间距，不用未运行的浮点表

设 $\zeta_1<\cdots<\zeta_5$ 为 $P_5$ 的根。
R578 已给其非零根平方
$(35\pm2\sqrt{70})/63$，于是
$$
|\zeta_i|<\frac{91}{100}.
\tag{12}
$$
例如 $\sqrt{70}<17/2$ 给最大平方 $<52/63<(91/100)^2$。
又直接代入上述明确六次式，
$$
P_6(14/15)=\frac{1498191}{182250000}>0.
\tag{13}
$$
因 $14/15>\zeta_5$，$P_6$ 最大根 $x_{0,6}$ 满足
$x_{0,6}<14/15$。

在每个非端根支，R578(11) 给准确公式
$$
-\frac{dx_{\tau,i}}{d\tau}
=\frac{1-x_{\tau,i}^2}
 {6(1+2\tau x_{\tau,i}+\tau^2)}.
\tag{14}
$$
它在所需内部区间严格正。

对最右支的 $0\le\tau\le1$，
$0<x_{\tau,6}\le x_{0,6}<14/15$。用
$1+2\tau x+\tau^2\le(1+\tau)^2$ 积分，得到
$$
x_{0,6}-x_{1,6}>
\frac{1-(14/15)^2}{6}\int_0^1\frac{d\tau}{(1+\tau)^2}
=\frac{29}{2700}.
\tag{15}
$$
其另一相邻差 $x_{-1,6}-x_{0,6}=1-x_{0,6}>1/15$。
最左支由 $x_{-\tau,7-i}=-x_{\tau,i}$ 对称。
中间四个根支全在 $(-91/100,91/100)$，两半区用
$(1+|\tau|)^2$ 上界同理得到相邻差
$$
>\frac{1-(91/100)^2}{12}
=\frac{1719}{120000}>\frac{29}{2700}.
\tag{16}
$$

还须比较不同根支。R578 §3.3 已证明
$|P_6(\zeta_i)|>1/5$。对 $|x|\le1$，有
$|P_6'|\le21$、$|P_5'|\le15$，所以
$$
|q_\tau'(x)|\le36,\qquad|\tau|\le1.
\tag{17}
$$
为使这里的较强导数界明确：由三项递推求导可得
$P_n'=\sum_{j=n-1,n-3,\ldots}(2j+1)P_j$，
而 $|P_j|\le1$。后一界可由有限次数的 Laplace 表达
$$
P_j(x)=\frac1\pi\int_0^\pi
\bigl(x+i\sqrt{1-x^2}\cos t\bigr)^j\,dt
$$
直接得到；对 $j\le5$ 展开并积分即核该等式，
被积因子的模不超过1。故(17)不借用浮点极值。

均值定理给每个根到将其与邻支隔开的 $\zeta_i$ 距离
$>1/180$。邻支两根分居 $\zeta_i$ 两侧，**合计**
距离 $>1/90>29/2700$。更远根支更大。因此
$$
\min_{(\tau,i)\ne(\tau',i')}
|x_{\tau,i}-x_{\tau',i'}|>\frac{29}{2700},
$$
$$
\boxed{\min|c_{\tau,i}-c_{\tau',i'}|>
\frac{99}{100}\frac{29}{2700}=\frac{319}{30000}.}
\tag{18}
$$

## 4. 固定更宽微包、真实 collar 和幅

取同一个明确平坦 bump
$$
b(t)=
\begin{cases}\exp[-1/(1-t^2)],&|t|<1,\\0,&|t|\ge1,\end{cases}
$$
并固定
$$
\varepsilon=\frac1{12000},\qquad
u_{jm}(y)=
\frac{\varepsilon^{7/4}}{256}
b\!\left(\frac{y-(15j+3m-57)\varepsilon}{\varepsilon}\right),
$$
$$
a_j=(-1)^j\binom7j^{1/3},\qquad
F=\sum_{j=0}^7a_j(u_{j0}+\sqrt3u_{j2}),\quad
G=\sum_{j=0}^7a_j(\sqrt3u_{j1}+u_{j3}).
\tag{19}
$$
微包间真实间隙至少 $\varepsilon$。
整个块支撑半径为 $58\varepsilon=29/6000$。
选择块包络半径
$$
b_{\rm env}=\frac{31}{6000}.
\tag{20}
$$
每侧开放零 collar 宽为 $1/3000$。由(18)
$$
2b_{\rm env}=\frac{310}{30000}
<\frac{319}{30000};
\tag{21}
$$
任意两个包络间还有严格超过 $3/10000$ 的空隙。
又所有中心在 $[4.01,5.99]$，而 $b_{\rm env}<.01$，
所以全部块包络严格位于共同物理窗口 $[4,6]$。

将三个角依次与 $\tau=-1,0,1$ 配对；
在(11)位置放(19)的对应旋转，并乘真实共同幅
$$
\lambda_{\tau,i}=(2w_{\tau,i})^{1/4}>0.
\tag{22}
$$
额外 $2^{1/4}$ 明确补偿六旋转减为三旋转的总四次质量；
它不是把三组一般积分权任意乘二。最后如需第一三矩圆的共同幅
归一，可再一次共同正幅归一，不沿实际路径改变。

R521 已支付(19)中四微包的三矩圆以及八完整副本的全部第三四通道。
同一正交换基和共同实幅保这些条件。
故本稿每个完整块自己的 second/third 真场仍在双 collar 为零，
全部 block 可按原右锚准确相加。内部32微包、gap和二、三累计
仍是真实整个块，不按微包另设锚。
最后18块共有576微包；这只是明确库的规模，不是可控维数或最小性断言。

## 5. 完整方程与合法共同盒

设 $P$ 是 R586 的任意完整读出，先按实际位置十次矩(10)相等，
再按(7)作三角平均。若取任一六节点规则为参考，则
$$
\boxed{
\sum_{\tau,i}2w_{\tau,i}\int_{{\rm block}(c_{\tau,i})}P_{\varphi(\tau),\theta}
=6\sin^2\theta
 \sum_{i=1}^6\widehat w_i
 \int_{{\rm block}(\widehat c_i)}\mathcal A P.}
\tag{23}
$$
$\mathcal A$ 就是 R586 的 $\theta=\pi/2$ 形式投影。
右侧为同一新实际库的准确评价，不是六个重叠物理副本。
可选 $\tau=0$ 的参考规则；共同位置仍须按(11)缩放。

因此整个 fourth、真实 $A_s=M$、有序 third、
R584 中心平移以及 R590 正平方和 C² 更新均保留。
在任一实际原历史上，(23)与时间积分可交换；第三入值只准来自
同一恢复的已付历史，不能任意给18块各自的入常数。
选非零规范时，仍使用 R521 §8 的一次固定右逆，
令 $\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu$。
一个 $\nu$、一个 $\chi$ 同时用于整词和双侧。

R521 完整加速度 IBP 因(23)继续准确成立，
并可保原参考表达的总因子6。取 R530 共同盒
$$
4/5\le h\le3,\quad |k|\le2,\quad|\eta|\le1,\quad 4\le y\le6,
$$
则
$$
z=y+\eta\ge3,\qquad e=hz-k\ge2/5,
$$
$$
h^2z^2-(1+k^2)\ge\frac{144}{25}-5=\frac{19}{25}>0.
\tag{24}
$$
故两侧均有严格 $C_h<0,C_k>0$；固定完整母与紧盒后非零下界由
原正积分和连续性给出。R528 的另一个 $1-ke\ne0$ 条件未被假设，
也未从(24)偷推出。

这建立的是新母上的同形十九态方程。
原 R578 的浮点表、$\rho,E_c,\bar\nu,\chi$、端点或轨道
不能凭总四次质量相等移来；本稿的实际完整块宽度和位置矩目标都已改变，
必须重新求所有系数与真端点。

## 6. 真实高导与几何预算的边界

### 6.1 微宽代价并未消失

令单微包的 $u=\varepsilon^{7/4}b(t)/256$。
R590 正平方的最高 $r=u''$ 部分乘 $T^2=(u''')^2$ 后，积分尺度是
$$
u^4\varepsilon^{-9}
=\frac{\varepsilon^{-2}}{256^4}.
\tag{25}
$$
这里 $u^4$ 的意思是共同幅的四次幂；真实被积函数保所有 bump
jets 和几何/历史系数，不把它们用这个尺度替代。
更明确地，写
$$
H_A+2F_0=V_0(y)u+V_1(y)u'+V_2(y)u'',
$$
则最高项为
$$
\frac{\varepsilon^{-2}}{256^4}
\int \frac{D_0^2Q(y)}{64h}
 V_2(y)^2\,b''(t)^2b'''(t)^2\,dt
\tag{26}
$$
再按真实位置/幅相加；其中
$y=c+(15j+3m-57)\varepsilon+\varepsilon t$，
并非固定成 $c$。
它是正平方中 $V_2^2$ 的那一项，不将其与交叉项分开删改。

相比旧半宽，$\varepsilon_{\rm new}/\varepsilon_{\rm old}=125/3$，
所以**仅这个首微宽因子**改善 $(125/3)^2=15625/9$；
整值还有真实历史、位置和其它阶项，不能把旧 run 的 $10^{17}$
直接除以该数当作新结果。特别真八矩若重新造成大的 $p_2,r_0,s_1$，
平方仍可很大。新输入没有将其系数设为0。

### 6.2 材料宽度与原空间宽度

使用 R573 的原几何
$$
X(s,u)=\alpha(s)+uN(s),\qquad u=h/(y+\eta).
$$
在(24)盒中
$$
\left|\frac{\partial u}{\partial y}\right|
=\frac h{z^2}\le\frac13.
$$
故每个完整包络在同一 ruling 上的**原空间长度**至多
$$
\frac{2b_{\rm env}}3=\frac{31}{9000},
$$
每个最细微包至多
$$
\frac{2\varepsilon}3=\frac1{18000}.
\tag{27}
$$
整个原窗口同一 ruling 的长度则为
$$
\frac{2h}{(4+\eta)(6+\eta)}\ge\frac8{175}.
\tag{28}
$$
这些是原 $X$ 的准确几何范围；不将材料半宽称为实体管厚，
也不把(27)误当有限变形的直径或 reach 下界。

更直接地，原第一场在 $(T,N,B)$ frame 中为
$$
Y_f=\left(-\frac{f'}{2z},\ 0,\
\frac{hf}{z}-\frac{e f'}{2z}\right).
$$
固定 $s$，使用 $\partial_u=-(z^2/h)\partial_y$，
逐项两次求导（全部 $f,f',f''$ 低项准确相消）给
$$
\boxed{(Y_f)_{uu}
=-\frac{z^3}{2h^2}f'''(T+eB).}
\tag{29}
$$
原单位法向 $n=(T+eB)/\sqrt Q$，所以
$$
n\cdot(Y_f)_{uu}
=-\frac{z^3\sqrt Q}{2h^2}f'''.
\tag{30}
$$
这是原 ruling 法曲率的准确一阶变分系数。
由(24)，系数介于 $3/2$ 和 $343\sqrt{530}/(32/25)$ 之间。
因此 profile 的三导成本仍直接进入真实二 jet，不能用宽度变大或
有限方程闭合代替 reach 检查。

例如令 $C_j=\max|b^{(j)}|$。对实际任一第一 profile，
不交性、$w_i\le1$ 与 $\max\binom7j=35$ 给
$$
\|f^{(j)}\|_\infty,\ \|g^{(j)}\|_\infty
\le\frac{2^{1/4}\sqrt3\,35^{1/3}}{256}
 \varepsilon^{7/4-j}C_j.
\tag{31}
$$
(29)对应 $\varepsilon^{-5/4}$ 的真实二 jet 尺度；
第一场位移的主微宽尺度为 $\varepsilon^{3/4}$，
两者的比仍有 $\varepsilon^{-2}$ 代价。
这些界只明确新输入必须支付的预算，未排除某个有限参数，
也不作有限非线性族的曲率/位移结论。

## 7. 后续实际解算的使用方式

本稿的严格新增内容是一个完整可直接生成的更宽18块库、
全相位形式投影、实际正权/锚及合法盒。
公开新 source 可以沿 R586/R590 重建六参考块的固定积分，
但必须绑定(8)–(22)的新母身份，完整保 $\widehat\nu,\bar\nu,\nu$、
中心势、双侧符号及原29条边界。

真 guide 要共同处理八矩与 prepared 中心，而非只拟合四个 even
再让 odd 以巨大能量回付。对实际原方程可将两加速度保为代数阶段变量，
使原两条 ruling 与十九条微分方程一起求解；这只是待实现的等价质量形式，
本稿不以它的未知数计数授根或满秩。

本稿没有为旧表重跑门槛，亦未新跑科学。新的系数、guide、加速度、
整段空间范围与最后主几何门将在新公开运行中继续支付。

