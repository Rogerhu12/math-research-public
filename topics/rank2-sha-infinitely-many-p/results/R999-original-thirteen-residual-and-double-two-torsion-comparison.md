# R999 — 原十三消核余式、准确二挠首 jet 与一个双零非零对照

日期：2026-11-26 UTC。**已证明：R992/R993 的两个完整十三消核余式可组合成一个固定有理来源，其中央导数在两条 canonical 失败时明确非零，而其三个二挠点上的来源零阶由二提高到至少四。** 这个来源是

$$
\boxed{\mathcal B_{130}=120\Phi_{260}-11\Phi_*-108\mathcal X_{130}-F_{10}.}
\tag{1}
$$

全部来源、绝对相位与共同 Gaussian 均沿用原 degree130。下面给出完整分子整格、首项、二挠 jet 的纸笔证明，以及同一个原 $Z^{-7}P_2^{65}$ 的全极帽。没有将来源乘积、固定核的零阶质量或消核后的高 jet 改写成新的算术零；本篇不声称已证明无穷素数非零。

## 1. 同一原模型及两份真实消核余式

仍在

$$
E_1:y^2=x^3+1,\quad dz=dx/(2y),\quad X=x^3,\quad
\delta^2=-3,\quad\omega=(-1+\delta)/2,\quad
\pi=(7+\delta)/2
\tag{2}
$$

中使用同一原 sigma。记

$$
\Phi_*=\sigma^{130}x^2P_*(X),\quad
\Phi_{260}=\sigma^{130}x^2P_{260}(X),\quad
\mathcal X=\sigma^{130}x^2P_{\mathcal X}(X),\quad
F_{10}=\sigma^{130}x^2P_F(X).
\tag{3}
$$

四条来源均首项 $z^6$；$\mathcal X$ 是 R992 的真实双中央零来源。定义

$$
G_{65}=\Phi_{260}-\Phi_*,\qquad
G_{\mathcal X}=\mathcal X-\Phi_*,\qquad
G_{\rm old}=\Delta_{125}+21840\delta\Phi_*
=3360\delta(\Phi_*-F_{10}).
\tag{4}
$$

本次原 direct22 完整消费者得到以下准确系数：

$$
c_\pi=\frac{403200(4+\delta)}{19},\qquad
d_\pi=-90720(1+\delta)=181440\omega^2,
\quad c_{\bar\pi}=-\bar c_\pi,
\quad d_{\bar\pi}=-\bar d_\pi.
\tag{5}
$$

于是两个**完整来源**

$$
\mathscr R_\pi=G_{\rm old}-c_\pi G_{65}-d_\pi G_{\mathcal X},\qquad
\mathscr R_{\bar\pi}=G_{\rm old}-c_{\bar\pi}G_{65}
                                      -d_{\bar\pi}G_{\mathcal X}
\tag{6}
$$

分别在完整二次核代数

$$
R_\pi(X)=X^2+(2+6\delta)X+(40+24\delta)/13,
\qquad R_{\bar\pi}=\overline{R_\pi}
\tag{7}
$$

中质量为零。准确地，若 $\mathscr R_\pi=\sigma^{130}x^2P_{\mathscr R_\pi}$，则 $R_\pi\mid P_{\mathscr R_\pi}$，可除重数恰为一；对核 $R_{\bar\pi}$ 上的完整余式非零。共轭支同理，并有

$$
\mathscr R_{\bar\pi}=-\overline{\mathscr R_\pi}.
\tag{8}
$$

这不是只从两根各取一个数：消费者重建原全部22维算子、两个完整 rank-one 来源及两 raw norm13 列，求两系数后回乘整个 degree19 多项式，并反复整除至第一次非零余式。两个原点阶均准确为12。

完整回执还给

$$
P_{\mathscr R_\pi}\in\mathbf Z[1/19,\delta][X],\quad
[X^{19}]P_{\mathscr R_\pi}
=\frac{-168799680+737190720\delta}{19}.
\tag{9}
$$

最高次系数及全部二十列均被返回；(9)没有由首项拟合来源。首次除商模 $R_\pi$ 的两个分母是 $19\cdot13^7$，对核余式分母是 $19\cdot13^9$。在约化后保留准确一次重数时，仍须删去首次余式范数的固定素支撑，不能只凭分母断言其分子全为 $p>211$ 单位。

## 2. 原二挠点上的完整一阶读取

以下撇号专指分子对 $X$ 求导。令 $C=3^{30}=27^{10}$。准确的四个导数是

$$
\boxed{
P_*'(-1)=\frac{3C}{385},\qquad
P_{260}'(-1)=0,\qquad
P_{\mathcal X}'(-1)=-\frac C{2835},\qquad
P_F'(-1)=-\frac C{21}.}
\tag{10}
$$

同时四个分子在 $X=-1$ 均为零。下面逐项证明这些值；$P_{260}'(-1)=0$ 使用 R982 同次完整来源返回的 $t=1$ 准确二阶，不需要重算其来源。

### 2.1 两条真实 norm13 raw pull

保持 R978 的原多项式 $R=R_\pi$、$A=A_\pi$：

$$
\sigma(\pi z)=\pi\sigma(z)^{13}R(X),\qquad
x(\pi z)=\frac{xA(X)}{\pi^2R(X)^2}.
\tag{11}
$$

其 level10 第一列及 $X$ 像分别为

$$
P_0=\pi^6A^2R^6,\qquad
U=\frac{XA^3}{\pi^6R^6}.
\tag{12}
$$

在非零二挠点，原相位给

$$
\pi R(-1)=-27\omega,\qquad
A(-1)=\omega(\pi R(-1))^2,
\qquad P_0(-1)=C,\quad U(-1)=-1.
\tag{13}
$$

若其 $x$ 坐标是 $e$，则在原局部参数 $u$ 中
$x(T+u)=e+3e^2u^2+O(u^4)$。因 $x(\pi T)=\omega e$，
同一个原微分给

$$
U'(-1)=\pi^2\omega=-11+4\delta.
\tag{14}
$$

这里没有重新规范 CM 微分。由 $R'(-1)=6\delta$ 以及(13)，

$$
\frac{R'}R(-1)=-\frac43+\frac{2\delta}{9},\qquad
\frac{A'}A(-1)=\frac{1-\pi^2\omega}{3}
                         +2\frac{R'}R(-1).
$$

对(12)求对数导数，得到

$$
\frac{P_0'}{P_0}(-1)
=\frac23(1-\pi^2\omega)+10\frac{R'}R(-1)
=-\frac{16}{3}-\frac{4\delta}{9}.
\tag{15}
$$

因此

$$
P_{\mathcal X}'(-1)
=\frac{P_0'(-1)-\bar P_0'(-1)}{2520\delta}
=-\frac C{2835}.
\tag{16}
$$

而 $D_\pi\Psi_{125}$ 的分子为 $P_0(U-8)$，故

$$
\begin{aligned}
P_{\Delta_{125}}'(-1)
&=-9(P_0'-\bar P_0')(-1)
   +C(\pi^2\omega-\bar\pi^2\omega^2)\\
&=16\delta C.
\end{aligned}
\tag{17}
$$

这两条式子同时保留了 raw pull 的全部相位和实际 $X$ 像。

### 2.2 原六 sigma 及 canonical 线

R971 的整个分子是

$$
P_F=P_S\mathcal J_5,\qquad
P_S=\frac{(X+1)(X-8)Q_2(X)}7,
\qquad Q_2=7X^2-4X+16.
\tag{18}
$$

原完整五倍点式在 $X=-1$ 只保其 $j=4$ 项，给
$\mathcal J_5(-1)=3^{24}$。又 $P_S'(-1)=-3^5/7$，所以

$$
P_F'(-1)=-3^{29}/7=-C/21.
\tag{19}
$$

由 R978 的完整身份

$$
F_{10}=-\frac{11}{2}\Phi_*+\frac{\delta}{10080}\Delta_{125},
\tag{20}
$$

将(17)、(19)代入便得 $P_*'(-1)=3C/385$。R982 的原全部角坐标已付 $P_{260}$ 在 $X=-1$ 恰二阶，故其一阶导数为零。至此(10)全部支付。

### 2.3 十三消核后没有消失的真实二挠首 jet

由(4)、(10)、(17)，

$$
P_{G_{65}}'(-1)=-\frac{3C}{385},\qquad
P_{G_{\mathcal X}}'(-1)=-\frac{254C}{81\cdot385},\qquad
P_{G_{\rm old}}'(-1)=\frac{2048\delta C}{11}.
\tag{21}
$$

再代(5)–(6)得到

$$
\boxed{P_{\mathscr R_\pi}'(-1)
=-\frac{64\cdot23\cdot3^{30}}{19}(1+5\delta).}
\tag{22}
$$

因为 $N(1+5\delta)=76=4\cdot19$，(22)在每个当前 $p>211$ 为单位。于是 $P_{\mathscr R_\pi}$ 在 $X=-1$ **准确只有一次因子**，共轭支也如此。它们在三个非零二挠点的来源零阶准确为二。这个结论保住了消十三核后真实剩余的二挠输入，没有用“质量零”把它删去。

## 3. 双二挠零的完整非零对照

以(5)、(8)直接展开，得到全函数身份

$$
\boxed{
\mathcal B_{130}
=\frac{(1-5\delta)\mathscr R_\pi
             +(1+5\delta)\mathscr R_{\bar\pi}}{6720\delta}
=120\Phi_{260}-11\Phi_*-108\mathcal X-F_{10}.}
\tag{23}
$$

例如两 $G_{65}$ 系数合计为 $-806400\delta$，两 $G_{\mathcal X}$ 系数合计为 $725760\delta$；再用(4)，即得右式。它不是只在十三核的商代数中相等。

式(22)与其负共轭在(23)准确相消，给

$$
P_{\mathcal B}(-1)=P_{\mathcal B}'(-1)=0.
\tag{24}
$$

也可直接将(10)代入(1)：
$-11(3C/385)-108(-C/2835)-(-C/21)=0$。
R982 已付两 canonical 的完整 $Q_2$ 因子，R992 已付 $P_{\mathcal X}$ 的 $Q_2$ 因子，(18)支付 $P_F$。因此

$$
\boxed{(X+1)^2Q_2(X)\mid P_{\mathcal B}(X).}
\tag{25}
$$

这是整个多项式整除，不仅是给两个点赋值。未断言 $(X+1)$ 的最高重数恰二，也未新增 $R_\pi R_{\bar\pi}$ 或 $X-8$ 因子。

同次完整回执给 $P_{\mathcal X}\in105^{-1}\mathbf Z[X]$，其中确出现分母21、15、35，所以105是最小清分母。原 $\Phi_*$、$\Phi_{260}$ 的最小分母分别为385、175。对 $F_{10}$ 使用(18)的准确分母：$P_S\in7^{-1}\mathbf Z[X]$，R971 原完整五倍除法式逐项给 $\mathcal J_5\in5^{-1}\mathbf Z[X]$，故 $P_F\in35^{-1}\mathbf Z[X]$。于是(1)逐项给

$$
\boxed{P_{\mathcal B}\in35^{-1}\mathbf Z[X].}
\tag{26}
$$

由(9)，(23)的 $X^{19}$ 系数准确为

$$
\frac{737190720+5\cdot168799680}{19\cdot3360}
=24768=2^6\cdot3^2\cdot43.
$$

所以没有发生额外原点取消：

$$
\boxed{\deg P_{\mathcal B}=19,\qquad
\mathcal B_{130}=24768z^{12}+O(z^{18}).}
\tag{27}
$$

这个首项在全部当前 $p>211$ 为单位。

若需把(25)作为 whole 除法消费，可以写

$$
P_{\mathcal B}=(X+1)^2Q_2Q_{15},\qquad\deg Q_{15}=15.
$$

原六 sigma 真实来源

$$
S_{30}=\frac{\sigma(2z)^4\sigma(\gamma_7z)
                         \sigma(\bar\gamma_7z)}{112}
=\frac17\sigma^{30}(X+1)^2Q_2
\tag{28}
$$

给完整乘积 $\mathcal B_{130}=S_{30}\,(7\sigma^{100}x^2Q_{15})$。
两个因子的首阶都是六。式(28)只支付完整来源除法；不把两个因子的中央导数赋零，也不把乘积的 Mellin 读数拆成两个中央值相乘。

## 4. 同一个真正中央非零值

固定当前好惰性 $p=6s-1>211$，$d=p+1$，并且只在本节明确使用两 canonical 失败假设

$$
J'_{\Phi_*,p}(0)=J'_{\Phi_{260},p}(0)=0.
\tag{29}
$$

R992 给 $J'_{\mathcal X,p}(0)=0$ 无条件；R978 给
$J'_{\Delta_{125},p}(0)=d\log_p(\pi/\bar\pi)$。从(20)、(1)准确得到

$$
\boxed{J'_{\mathcal B,p}(0)
=-\frac{\delta}{10080}(p+1)\log_p(\pi/\bar\pi)\ne0.}
\tag{30}
$$

这里的非零仍是完整局部对数非零：$\pi/\bar\pi$ 不是全局根单位，局部对数的单位核只有根单位，嵌入为单射。没有据(30)给它一个未证明的跨 $p$ 赋值上界。

在 R968 已固定的普通射线上，同样的 whole 线性身份给

$$
j^{\rm ord}_{\mathcal B,p}
=-\frac{\delta}{10080}(p-1)(1-\upsilon_p)
                         \log_p(\pi/\bar\pi)\ne0,
\tag{31}
$$

其中读者指数仍是 $\langle x\rangle^{(p-1)v}$，不能漏去 $p-1$ 或实际单位切的 $1-\upsilon_p$。回原共同 $b=17$ 首六阶规范，(30)–(31)另有统一 $17^{-1}$。本节没有推广到未支付 whole core scalar 的其它普通射线。

## 5. 未平移原全权的真实极集合与第六 Cartier 行

保持 R887 的原初始化

$$
DZ=1,\quad DG=-x+c_pZ^{p-1},\quad
P=P_2=-(D-2G)^{p-1}Z^{p+1},
\quad c_p=\binom{3s-1}{2s-1}.
\tag{32}
$$

令 $R_{\mathcal B}=x^2P_{\mathcal B}(X)$，考察真正的未平移第六输入

$$
\eta_{\mathcal B,6}=Z^{-7}P^{65}R_{\mathcal B}\,\omega_E.
\tag{33}
$$

原 $Z$、$P$ 没有重选。以下逐点给其完整极集合。

在 $O$，$P=z^2+\cdots$，而(27)给 $R_{\mathcal B}$ 的极阶118。因此(33)在 $O$ 的阶是五，特别正则。若 $Q\ne O$ 是任一个其它 $Z$ 零点，R853 原方程给 $\operatorname{ord}_QP\ge p$；$R_{\mathcal B}$ 在该点正则。所以

$$
\operatorname{ord}_Q\eta_{\mathcal B,6}\ge65p-7>0.
\tag{34}
$$

这逐点支付了**这个未平移完整输入**的所有移动 $Z$ 零点取消，不是先忽略它们。其它非二挠点也无极。

在任一非零二挠点，$X+1=y^2$，(25)给
$\operatorname{ord}R_{\mathcal B}\ge4$。原准确极阶为

$$
-\operatorname{ord}Z=p,\qquad
-\operatorname{ord}P=p^3-p^2+p+1.
$$

故(33)全部可能的极只在原三个非零二挠点，每处极阶至多

$$
\boxed{65p^3-65p^2+58p+61.}
\tag{35}
$$

相比(22)那两条实际消十三核来源，这里又准确降低二阶。式(35)是上界，不据未计算的二阶导数将它宣称为每处准确极阶；二挠主部全部仍在读者中。

记

$$
\mathcal B^\circ=e^{-130cz^{p+1}}\mathcal B,\quad
c=[z^{p+1}]\log(\sigma/z),\quad
g_{\mathcal B,6}=[z^{6(p+1)}]\mathcal B^\circ,\quad
a^+_{\mathcal B}=[z^{p+7}]\mathcal B^\circ.
$$

因为 $[z^6]\mathcal B=0$，R711 在同一原整窗准确给

$$
\boxed{
\left(\frac{D^5}{5!}
       \frac{\mathcal C\eta_{\mathcal B,6}}{\omega_E}(O)\right)^p
=\overline{g_{\mathcal B,6}}
 +7\kappa_5\overline{a^+_{\mathcal B}},\qquad
\kappa_5=(3/5)^p/c_p.}
\tag{36}
$$

原点无简单极，所以这里不减 $1/Z$；共同 $\eta_p$ 和第五行常数 carry 都因准确的首六阶零消失。**剩下的 $7\kappa_5a^+_{\mathcal B}$ 并未消失。** (36)是原全权的精确读取，并非给左侧或低卷积新增一个零。

对十三核平移 $T$，完整转置仍必须使用

$$
\begin{aligned}
&Z^{-7}\widehat{T_T\mathcal B}\,\omega_E
 -t_T^*(Z^{-7}\widehat{\mathcal B}\,\omega_E)\\
&=\left[Z^{-7}P^{65}a_T^{10}
 -(Z\circ t_T)^{-7}(P\circ t_T)^{65}\right]
       (R_{\mathcal B}\circ t_T)\,\omega_E,
\qquad a_T=\frac{R_\pi(X)}{R_\pi(X\circ t_T)}.
\end{aligned}
\tag{37}
$$

平移后的来源可有非零质量或非零六阶项；不能把未平移(27)、(34)当作它在 $O$ 的新零。原 $P(T)$ 权、$O,-T$ 的实际读取以及两个二挠集合的主部在(37)全部保留。

## 6. 同次完整回执及接续范围

本篇消费 public Actions 的 source
`5ce57788fdf943376c908f815e42756f859dc0c7`、run `45907263972`、job `140206875320`，执行时间2026-11-26 22:50:12–22:50:23 UTC。新消费者用时0.054701184秒；原 R987/R993 全部来源门、48条完整纤维、22列及质量列、两额外纤维、交换、共轭逆、十二次幂和原矩阵哈希全部保持。

新源 `check-original-thirteen-inert-zero-source.py` 为15567字节，SHA-256：
`220a18e1b483a7981da1621614ecddf902e3184f220053814a6c1e749f6d26ae`。

原 stdout 为16730字节，SHA-256
`91636d1016ee94422abb30bdced465501081d89819d923909607c4ab3dbda049`；同次 source manifest 为
`67fa1cef0890f8ae65636cd0df2a2ae80fe08ef57e1ced4d46e5af9064c9c121`。

关键完整来源哈希为：

| 来源 | SHA-256 |
| --- | --- |
| $\mathcal X_{130}$ | `4ae3a846a90365a6f1bb1baf0fe4e66f254311938d9f20ab994d3200386fbb32` |
| $G_{\mathcal X}$ | `60154677285e59ce1fa451ac78d8483984154eb311b20393f5c0e06c54abf7d8` |
| $\mathscr R_\pi$ | `b0d610c4713f4a0ae7b56061a1cd29b504defcaede3f0e3bffc5224b4aea9d49` |
| $\mathscr R_{\bar\pi}$ | `9b571fde92e85e340a66c9798c6daf72d9c179d22fc0c61f1c6107a03619b0d8` |

本篇没有运行数学或新增可重算系数文件；(10)–(28)、(34)–(37)均从原完整身份、已实际返回的坐标和显示的局部计算证明。新的可消费对象是(1)这个带明确非零中央的 whole 来源、(22)的原二挠单位首 jet，以及(25)、(35)的完整除子改善。主目标仍须在原完整中央条件中实际消费剩余二挠主部、全部低卷积及 mixed 读者，不能以(30)的另一个非零来源替代固定秩二曲线的中央非零。

## 依赖

- R971、R978：原 $F_{10}$、两 raw norm13 列、全部 old 系数及对数身份。
- R982：同次完整四新来源角式，特别 $P_{260}$ 的二挠恰二阶、两 canonical 的完整 $Q_2$ 因子和最小分母。
- R987、R992、R993：相同 canonical lift、全二次质量代数、实际 $\varrho$ 与三条真零方向。
- R711、R853、R887：原 $P_2$ 初始化、完整极阶、移动零点零阶及第六 Cartier 的两个真实误差。
