# R1004 — 原十三核的全部六阶 jet 与适配 Cartier 的固定非零残差

日期：2026-11-27 UTC。**已证明：在原 degree130 完整22维来源上，两条十三核的质量与六阶 Taylor 系数有一个准确、相位固定的四行映射。原四条来源 $\Phi_*,\Phi_{260},\mathcal X_{130},F_{10}$ 在每一条核上都给可逆的四阶矩阵；$K_{130},C_{130}$ 的两个完整六阶核值已经线性独立。** 下文给全部递推、实际小值、行列式、真正公开运行与固定坏素数范围。

这解决 R1005 后续适配 $Q_\pi$ 模型中尚未支付的十三核六阶输入。它不把核上的读数等同于整个中央导数：$E[2\pi]$ 的全部支撑、两个 exact 层、实际 Gaussian 比较与原全精度余式继续保留。

## 1. 同一原来源、微分与十三核 lift

沿 [R987](R987-original-thirteen-two-orbits-and-normalized-central-difference.md)、[R992](R992-original-common-old-zero-line-and-eleventh-central-source.md)、[R993](R993-original-thirteen-boundary-values-and-common-frame.md) 取

$$
E_1:y^2=x^3+1,\qquad dz=\frac{dx}{2y},\qquad X=x^3,
\qquad \delta^2=-3,
$$

$$
\omega=\frac{-1+\delta}{2},\qquad
\pi=\frac{7+\delta}{2},\qquad
\bar\pi=\frac{7-\delta}{2},\qquad N\pi=13.
\tag{1}
$$

原 principal 空间是

$$
V_{130}
 =\left\{\sigma^{130}R_F:
 R_F=x^2P_F(X),\quad \deg P_F\le21\right\},
\quad
e_i=\sigma^{130}x^2X^i\ (0\le i\le21).
\tag{2}
$$

它包括原非零质量列。若 $P_F=\sum u_iX^i$，则

$$
m_0(F)=u_{21},\qquad
c_6(F)=[z^6]F=u_{20}-\frac{26}{3}u_{21}.
\tag{3}
$$

这来自原 $\sigma/z=1+z^6/210+O(z^{12})$ 与
$x=z^{-2}(1-z^6/7+O(z^{12}))$，没有省掉 $u_{21}$ 对六阶的贡献。

原 norm13 除法身份是

$$
R_\pi(X)=X^2+(2+6\delta)X+\frac{40+24\delta}{13},
\qquad
\sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X(z)).
\tag{4}
$$

对 $T\in E[\pi]$，保持 R987 的准确 Mumford lift：

$$
\mathcal T_T^{(\pi)}F(z)
 =\sigma(\pi z)^{10}
   \frac{F(z+T)}{\sigma(\pi(z+T))^{10}}
 =\sigma(z)^{130}
   \left(\frac{R_\pi(X(z))}{R_\pi(X(z+T))}\right)^{10}
   R_F(z+T).
\tag{5}
$$

第二式也在 apparent 零点按完整截面延拓。由(4)，它还等于

$$
\mathcal T_T^{(\pi)}F(z)
 =\frac{\sigma(\pi z)^{10}}
        {\pi^{10}R_\pi(X(z+T))^{10}}R_F(z+T).
\tag{6}
$$

因此相位由原 sigma 与(4)唯一固定，没有再取一个可任选的十次根。
式(5)中的有理乘子直接望远镜相消，给
$\mathcal T_T\mathcal T_U=\mathcal T_{T+U}$；
下面的十三项和确是这一 lift 的完整核迹。

置 $D=d/dz=2y\,d/dx$。对非零 $T\in E[\pi]$ 定义

$$
d_T=DR_\pi(X)(T)=6x(T)^2y(T)R_\pi'(X(T)),
\qquad
A_T(z)=\frac{R_\pi(X(z+T))}{d_Tz}.
\tag{7}
$$

在特征零中 $d_T\ne0$；好约化时也如此。并且 $A_T(0)=1$。
定义实际质量和实际六阶核值
$m_T(F)=\mathcal T_TF(0)$、
$b_T(F)=[z^6]\mathcal T_TF$。
将(6)在原点展开，严格得到

$$
\boxed{m_T(F)=d_T^{-10}R_F(T),}
\tag{8}
$$

$$
\boxed{
b_T(F)=d_T^{-10}
 \left([z^6]\{A_T(z)^{-10}R_F(z+T)\}
             +\frac{\pi^6}{21}R_F(T)\right).}
\tag{9}
$$

这里 $\pi^6/21$ 来自
$\sigma(\pi z)^{10}/(\pi z)^{10}=1+\pi^6z^6/21+O(z^{12})$。
把它删掉会改变质量不为零的每一个核值。

两种函数 $T\mapsto m_T(F),b_T(F)$ 都在 $\mu_6$ 轨道上不变。
例如由(5)与原 $\mu_6$ 线性化，
$\mathcal T_{\zeta T}F(z)=\mathcal T_TF(\zeta^{-1}z)$；
取零阶和六阶即得不变性。因此它们属于完整二次代数

$$
A_\pi=K[X]/(R_\pi(X)),\qquad K=\mathbf Q(\delta),
\tag{10}
$$

其中一个 $X$ 根代表一个六点轨道。以下始终保留两根，不作单根选支。

## 2. 全部22列的有限代数计算及返回证明

实际计算先在完整十二点代数中进行：

$$
\mathcal A_\pi
 =K[X,x,y]/(R_\pi(X),x^3-X,y^2-X-1).
\tag{11}
$$

它对 $K$ 的维数为12。采用 $x^ay^b$，
$0\le a<3,\ 0\le b<2$ 为六个分量，每个分量保留 $1,X$ 两坐标。
这样原曲线上的十二点与其全部相位都在同一乘法代数中。

### 2.1 原曲线七阶 Taylor 与准确逆元

令 $x(T+z)=\sum x_nz^n$。原方程给
$x_0=x,\ x_1=2y,\ x''=6x^2$，故

$$
x_{n+2}
 =\frac{6}{(n+1)(n+2)}
       \sum_{i=0}^{n}x_i x_{n-i}
       \qquad(0\le n\le5).
\tag{12}
$$

这支付到七阶的全部系数。需要七阶而非六阶，是因为(7)先将
$R_\pi(X(T+z))$ 除以 $z$。消费者在整个(11)中另行返回
$(x'(T+z)/2)^2=x(T+z)^3+1$ 到六阶。

在(11)中，

$$
d_T^{-1}
 =\frac{xy}{6X(X+1)R_\pi'(X)}.
\tag{13}
$$

该等式由 $x^3=X,\ y^2=X+1$ 直接乘回。分母在 $A_\pi$ 中用二次范数求逆，再乘回确认为一。最后以

$$
A_T^{-10}
 =\sum_{j=0}^{6}(-1)^j\binom{9+j}{j}(A_T-1)^j
       \pmod {z^7}
\tag{14}
$$

求完整逆级数，并将它与 $A_T^{10}$ 乘回到六阶。

把 $R_F=x^2X^i$ 依次代入(8)–(9)，对所有 $0\le i\le21$ 计算。
每一列的非不变 $x^ay^b$ 分量都必须实际为零；不是只计算投影后选定的分量。

质量行还有一个与 Taylor 过程独立的返回式：

$$
\boxed{
m_T(e_i)=
 \frac{X^i}{6^{10}X^6(X+1)^5R_\pi'(X)^{10}}
                 \quad\text{于 }A_\pi.}
\tag{15}
$$

消费者将全部22列逐项与这一完整分母相乘，返回 $X^i\bmod R_\pi$。
然后对 $\bar\pi$ 核独立做同一过程；整个22列质量行和六阶行逐系数严格共轭。

以上是有限有理运算证明，不依赖任何选定素数的扫描。
所用分母来自固定来源、$R_\pi$、(12)的固定小阶数和(13)的二次范数；
它们给固定的有限坏素数集，不随 $p$ 增大。

### 2.2 原算术来源完整重建

消费者接受同一次原 direct22 上下文，即原48个完整 CM 纤维产生的
$N_7,N_{19}$。从两个完整算子构造原幂等元，分别提取：

$$
\Phi_*:\quad(\lambda_7,\lambda_{19})=(\omega,-1),
\qquad
\Phi_{260}:\quad(\lambda_7,\lambda_{19})=(\omega,-\omega^2).
\tag{16}
$$

对应指数分别为 $(4,3),(4,5)$，原 $\zeta_6=-\omega$。
每个共同像先实际检验秩一、质量零，再以 $c_6=1$ 归一，
并核对 R970/R973 的完整来源哈希。没有由两个好位特征任选一个替代来源。

其余两条来源亦完整重建。沿 R992 定义

$$
f_0=\sigma^{10}x^2,\qquad
\mathcal X_{130}
 =\frac{D_\pi f_0-D_{\bar\pi}f_0}{2520\delta},
\qquad D_\alpha f(z)=f(\alpha z).
\tag{17}
$$

以原完整 norm13 有理映射
$x(\pi z)=xA_\pi(X)/(\pi^2R_\pi(X)^2)$ 重生两个 raw pull。
原 $F_{10}$ 则由原六 sigma 的完整 $P_SJ_5$ 乘积重生。
消费者另行返回已有的 whole 身份

$$
F_{10}=-\frac{11}{2}\Phi_*+\frac{\delta}{10080}\Delta_{125},
\qquad
\Delta_{125}=D_\pi\Psi-D_{\bar\pi}\Psi,\quad
\Psi=\sigma^{10}x^2(X-8).
\tag{18}
$$

这里仅用该式核对完整多项式，没有用它拟合 $F_{10}$。

## 3. 真实返回的完整二次值与四阶行列式

以下令

$$
m_\pi(F)=a_F+b_FX,\qquad
b_\pi(F)=A_F+B_FX
                 \quad\text{于 }A_\pi.
\tag{19}
$$

注意 $b_\pi(F)$ 表示整个六阶核值，$b_F$ 仅是质量的 $X$ 坐标。
$\bar\pi$ 核的所有表项逐系数取复共轭。

### 3.1 四条原来源的质量行

| $F$ | $a_F$ | $b_F$ |
|---|---:|---:|
| $\Phi_*$ | $17/997920-\delta/199584$ | $-1/997920-\delta/498960$ |
| $\Phi_{260}$ | $-1/113400-\delta/302400$ | $-1/725760+\delta/1209600$ |
| $\mathcal X_{130}$ | $-1/816480+\delta/349920$ | $1/6531840-\delta/2799360$ |
| $F_{10}$ | $-13/90720+13\delta/90720$ | $1/181440+\delta/90720$ |

这四行与 R993/R992 的两根质量身份完全相同；新的计算对它们作了(15)的全22返回。

### 3.2 新的全部六阶核值

| $F$ | $A_F$ | $B_F$ |
|---|---:|---:|
| $\Phi_*$ | $212467/1496880+32773\delta/299376$ | $32357/748440-30277\delta/1496880$ |
| $\Phi_{260}$ | $-5617/34020-1391\delta/45360$ | $-1391/108864+1391\delta/181440$ |
| $\mathcal X_{130}$ | $604291/1224720-117037\delta/3674160$ | $-30269/4898880-21211\delta/2099520$ |
| $F_{10}$ | $413197/136080-98197\delta/136080$ | $-95899/272160+1619\delta/34020$ |
| $B_{130}$ | $-2643329/34020-13\delta/18$ | $-53843/54432+8263\delta/3780$ |
| $K_{130}$ | $-1852933/11340-85237\delta/68040$ | $-402721/181440+2517343\delta/544320$ |
| $C_{130}$ | $376249/11340-757409\delta/68040$ | $1164103/181440-1157269\delta/544320$ |

令 $M_\pi$ 按列取
$(\Phi_*,\Phi_{260},\mathcal X_{130},F_{10})$，
按行取 $(a_F,b_F,A_F,B_F)$。真实返回为

$$
\boxed{
\det M_\pi
 =\frac{16842811}{3754514173132800000}
   +\frac{58055281}{26281599211929600000}\delta
 \ne0.}
\tag{20}
$$

因此每条核上，完整映射

$$
V_{130}\longrightarrow A_\pi\oplus A_\pi,\qquad
F\longmapsto(m_\pi(F),b_\pi(F))
\tag{21}
$$

的秩准确为4，且这四条真实来源已给整个像。
对 $\bar\pi$ 也是同样结论，行列式为(20)的共轭。
这里只说一个核上的质量加六阶足以区分四条来源；没有把(21)换成中央泛函。

## 4. 原完整核迹的独立核对

在 $A_\pi$ 中记二根迹

$$
\operatorname{tr}_\pi(a+bX)=2a-(2+6\delta)b.
\tag{22}
$$

整个十三点核迹为
$\operatorname{Tr}_\pi F=\sum_{T\in E[\pi]}\mathcal T_TF$。
因此

$$
m_0(\operatorname{Tr}_\pi F)
 =m_0(F)+6\operatorname{tr}_\pi m_\pi(F),
$$

$$
c_6(\operatorname{Tr}_\pi F)
 =c_6(F)+6\operatorname{tr}_\pi b_\pi(F).
\tag{23}
$$

原两条 primitive 来源满足完整核迹为零，所以新表必须给

$$
\operatorname{tr}_\pi m_\pi(\Phi_*)
 =\operatorname{tr}_\pi m_\pi(\Phi_{260})=0,
\qquad
\operatorname{tr}_\pi b_\pi(\Phi_*)
 =\operatorname{tr}_\pi b_\pi(\Phi_{260})=-\frac16.
\tag{24}
$$

这两条六阶约束已在两核分别实返，不能误写为六阶迹零；
原点本身还有 $c_6=1$。

对 old 部分还有独立的 level10 检验。
在升序基 $(f_0,f_1)=(\sigma^{10}x^2,\sigma^{10}x^5)$ 上，原完整矩阵是

$$
N_\pi=
\begin{pmatrix}
 1/3-2\delta/9&20/3+20\delta/9\\
 1/12+\delta/36&1/6-5\delta/18
\end{pmatrix}.
\tag{25}
$$

这仍是 $N_\pi=\pi^{-1}\operatorname{Tr}_{[\pi]}D_{\bar\pi}$
的规范。若第一列记作 $(c_0,c_1)^t$，则
$m_0(N_\pi f_0)=c_1$、
$c_6(N_\pi f_0)=c_0-2c_1/3$。
R987 的完整迹给

$$
\operatorname{Tr}_\pi\mathcal X_{130}
 =\frac{D_\pi(13f_0-\pi N_\pi f_0)}{2520\delta}.
\tag{26}
$$

又 $N_\pi\Psi=\omega^2\Psi$，
$\Psi(0)=1,\ c_6(\Psi)=-26/3$。由(18)得

$$
\operatorname{Tr}_\pi F_{10}
 =\frac{\delta(13-\pi\omega^2)}{10080}D_\pi\Psi
 =\frac{\delta\pi}{2520}D_\pi\Psi.
\tag{27}
$$

代入 $\pi^6=253+1260\delta$，得到

$$
\begin{aligned}
m_0(\operatorname{Tr}_\pi\mathcal X_{130})
 &=-1/18144+\delta/30240,\\
c_6(\operatorname{Tr}_\pi\mathcal X_{130})
 &=\frac{401707-2625\delta}{68040},\\
m_0(\operatorname{Tr}_\pi F_{10})
 &=\frac{-3+7\delta}{5040},\\
c_6(\operatorname{Tr}_\pi F_{10})
 &=\frac{353847+26117\delta}{7560}.
\end{aligned}
\tag{28}
$$

这四个值由完整 level10 矩阵和 raw pull 得到；
消费者将其与(23)独立比较，四式及全部共轭式均返回相等。

## 5. 同双二挠 K/C 的准确非零边界

沿 [R999](R999-original-thirteen-residual-and-double-two-torsion-comparison.md)、
[R1005](R1005-original-single-p130-full22-and-thirteen-translate-correction.md) 定义

$$
B_{130}=120\Phi_{260}-11\Phi_*-108\mathcal X_{130}-F_{10},
$$

$$
K_{130}=254\Phi_{260}-11\Phi_*-243\mathcal X_{130},
$$

$$
C_{130}=90B_{130}-43K_{130}
 =-122\Phi_{260}-517\Phi_*+729\mathcal X_{130}-90F_{10}.
\tag{29}
$$

本次完整重建再次返回

$$
K_{130}=51840z^{12}+O(z^{18}),\qquad
C_{130}=-3151872z^{18}+O(z^{24}),
\tag{30}
$$

以及两条完整分子均在 $175^{-1}\mathbf Z[X]$ 内，且都被

$$
(X+1)^2Q_2(X),\qquad Q_2=7X^2-4X+16
\tag{31}
$$

整除。特别是 $m_0=c_6=0$，但这不使非零十三核上的(8)–(9)为零。

实际质量两列为

$$
\begin{aligned}
m_\pi(K_{130})
 &=\left(-\frac{23}{10800}-\frac{671\delta}{453600}\right)
   +\left(-\frac{13}{34560}
                    +\frac{1157\delta}{3628800}\right)X,\\
m_\pi(C_{130})
 &=\left(\frac{323}{75600}-\frac{3547\delta}{453600}\right)
   +\left(\frac{73}{241920}
                    -\frac{1151\delta}{3628800}\right)X.
\end{aligned}
\tag{32}
$$

按 $K,C$ 列序，两个二阶行列式是

$$
\boxed{
\det(m_\pi(K),m_\pi(C))
 =-\frac{23}{2903040}-\frac{23\delta}{5644800}\ne0,}
\tag{33}
$$

$$
\boxed{
\det(b_\pi(K),b_\pi(C))
 =-\frac{25996646899}{22861440}
          +\frac{14624773\delta}{90720}\ne0.}
\tag{34}
$$

所以单独质量与单独六阶各自已经在 $A_\pi$ 中满二维；
合并的四行两列矩阵秩2。共轭核也一样。
尤其，在保持(34)可逆的任何好约化处，没有非零的 $K,C$ 线性组合
能消掉该核的**两个完整六阶值**。这比只知道某个核迹非零更强。

为明确一个不依赖完整行列式的非零检测，(24)、(26)–(29)还给

$$
\boxed{
6\operatorname{tr}_\pi b_\pi(K_{130})
   =\frac{-401707+2625\delta}{280},\qquad
6\operatorname{tr}_\pi b_\pi(C_{130})
   =\frac{76893-284795\delta}{840}.}
\tag{35}
$$

因两来源的原点六阶均为零，右边也就是完整十三点迹的六阶系数。
二者在 $K$ 中都不为零。其非零性可由有理部分直接看出，
无需对大整数作数值近似。

### 5.1 准确的模 p 范围

所有以上恒等式在特征零中无条件成立。用于约化时，
先删去既有原来源的固定坏集，以及(4)、(12)–(15)、各表项的分母素数。
若要保(20)、(33)、(34)相应的满秩结论，还须删去
对应非零代数数范数的分子素数。

更精确地，对 $u\in K^\times$ 写 $N_{K/\mathbf Q}(u)$ 为既约非零有理数，
记 $\operatorname{Supp}(u)$ 为该范数的分子、分母素因子之并。
设 $D_4,D_m,D_6$ 分别为(20)、(33)、(34)的右边，则可以统一删去

$$
\mathcal S_{\mathrm{jet}}
 =\mathcal S_{\mathrm{original}}
 \cup\mathcal S_{\mathrm{den}}
 \cup\operatorname{Supp}(D_4D_mD_6).
\tag{36}
$$

这是由已显示的准确有理数指定的**固定有限集合**。
对 $p\notin\mathcal S_{\mathrm{jet}}$，两核的秩结论在相应剩余域中仍成立。

如果仅使用(35)分别检测 $K,C$ 的非零残差，
再排除以下两个明确正整数的素因子就足够：

$$
(401707^2+3\cdot2625^2)
(76893^2+3\cdot284795^2),
\tag{37}
$$

连同已述固定分母。这一范围不能不加说明地写成“所有 $p>211$”；
$211$ 只支付原整窗条件，不支付新固定行列式的分子。

## 6. 适配 Qπ 模型中真正得到的 Cartier 残差

本节只取局部上已经完全支付的部分，不预先处理其余全局支撑。
固定好惰性 $p>211$，并在需要非零结论时排除(36)或(37)明确指定的固定素数。
沿 R1005 的原 $P_{10},Z$ 定义

$$
Q_\pi(P)=
 \frac{P_{10}(\pi P)}
      {\pi^{10}R_\pi(X(P))^{10}},
\qquad
Z_\pi(P)=\frac{Z(\pi P)}{\pi},
$$

$$
\eta_\pi(F)
 =Z_\pi^{-7}Q_\pi R_F\,\frac{dx}{2y}.
\tag{38}
$$

在非零 $T\in E[\pi]$ 附近写 $P=T+z$。因为 $\pi T=O$，
分子 $P_{10}(\pi P)$ 与 $R_\pi(X(P))^{10}$ 的零阶准确抵消。
原第一个 Gaussian 修正从 $z^{p+1}$ 才开始；
原 $Z(\pi z)/\pi=z+O(z^{5p})$。
因此到六阶为止，$Q_\pi R_F$ 的完整局部展开与
$\mathcal T_T^{(\pi)}F$ 相同。由(8)–(9)得到

$$
\eta_\pi(F)
 =\left(m_T(F)z^{-7}+\cdots+b_T(F)z^{-1}+O(1)\right)dz,
\qquad T\ne O.
\tag{39}
$$

在 $O$ 同理，其留数为 $c_6(F)$。特别地，

$$
\boxed{
\operatorname{res}_T\eta_\pi(F)=b_T(F)\quad(T\ne O),
\qquad
\operatorname{res}_O\eta_\pi(F)=c_6(F).}
\tag{40}
$$

所有这些核点的极阶至多7。因 $p>7$，一次 Cartier 已杀掉该处除
$z^{-1}dz$ 之外的所有负次幂；三次 Cartier 的留数准确为

$$
\operatorname{res}_T C^3\eta_\pi(F)=b_T(F)^{1/p^3}.
\tag{41}
$$

在(37)及固定分母之外，(35)保证
$C^3\eta_\pi(K_{130})$ 与 $C^3\eta_\pi(C_{130})$ **各自都非零**：
若某一个在每个非零十三核点的留数都为零，(35)的和也将为零。
其它支撑点可以参与全局留数和，却不能取消一个不同核点上的局部主部。

这与 R1005 原单 $P_{130}$ 模型在 $c_6=0$ 时满足 $C^3=0$ 完全相容。
两个模型有不同的全局有理框架；其中央读者之间的准确 Gaussian 比较
不会把两条全局 Cartier 微分认成同一条。式(40)具体给出了其中一个
必须保留的边界差，不能再以 $K,C$ 在原点从高阶开始而略掉。

本节不把(41)解释成 $J'_F(0)\ne0$。例如在两条 canonical 坏条件下，
R1005 仍准确给 $J'_{K_{130}}(0)=0$，
而 $J'_{C_{130}}(0)=-\delta(p+1)\log_p(\pi/\bar\pi)/112\ne0$。
核留数的非零与整个中央是否为零是不同的读数。

## 7. 原位六阶读者仍保留的内容

从(21)、(34)、(40)现在可以直接消费两条核的完整零阶和六阶值，
不再引入未定的核高 jet。然而全局(38)还带有 $E[2\pi]$ 的真实支撑；
其每个分量及两个 exact 层必须同时返回到原第六读者。尤其：

- 原单 $P_{130}$ 与 $P_2^{65}$ 的比较仍用 R1005 的
  $A_pc_6(F)+B_pm_0(F)$，包括非零质量译像。
- 真正惰性 Tate 函数的适配 Gaussian 比较仍带
  $q_\pi=\pi^{p+1}/13$；对非零质量译像不能删去其对数修正。
- R989 六位 Schur 只允许把已付的真实最后一项放回同一完整系统；
  核值的秩4不增加物理窗，也不使两个 exact 层自动为零。
- 质量加六阶满秩不是 Hecke 或 torsion 平移保持中央零的断言。

这些保留项正是继续从真实 canonical 坏条件逼迫整个对照来源的内容，
不是(20)或(34)中的额外假设。

## 8. 真实公开运行及可重现入口

本篇有限代数身份由下列真实公开运行返回。没有本地运行数学任务，
没有提交生成矩阵或生成系数。

- 公开 run：[45916324833](https://github.com/Rogerhu12/math-research-public/actions/runs/45916324833)；
  job：140236318135；source：
  56f5c405d885932a9d8b213a5cdb431376fa2ea3。
- 2026-11-27 00:22:24–00:22:40 UTC；结论 success，
  原入口全部阶段及本消费者 PASS。
- request：2026-11-27-r1004-both-complete-kernel-sixth-jets；
  原入口 scripts/check-original-degree130-thirteen-torsion-entry.py --workers=4。
- 新消费者：scripts/check-original-thirteen-full-sixth-jet.py，
  18694 B，SHA-256：
  d33eb6db4b6251a2f893e5083e6b0d2d7f26a6e4e75cb6d0b9c6c625a93a727a。
  导出 check_original_thirteen_full_sixth_jet(degree130_context)。
- 原入口 SHA-256：
  63a157c8939327e23070bc51d1b64f7f89e4185298928ce968c0a25a7883512c；
  Python FLINT 0.9.0。全入口 11.565302307 秒，新有限代数消费者
  0.166022611 秒。
- 八来源 manifest：
  14f0b1ae3c90c48383eb477557d69d4267050f64ab952ac8e6f5641f5d3bf347；
  含 request/workflow manifest：
  dce1a3548ffc8a9f61030dc570572ab31ad7616c3ccd20ff09fb52b33f286779。
- 原 stdout 24433 B，SHA-256：
  7a2307e7df235267301f05e704884786f4a62a7a929078b6615e6a40d2180880；
  job 完整日志 66228 B，SHA-256：
  294480f4d70ae3cc778b2dba68e69e25221b48cb614ea4c05c585f0e57387b31。
  回执明确 outputs_persisted: false。

完整 direct22 矩阵哈希仍为

aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113。

本次新增的两核四行全22矩阵哈希为：

| 核 | 质量加六阶全22映射 SHA-256 |
|---|---|
| $\pi$ | 44a11f66c41b6c07bbd7cbb7e690af707c56d7d37eb2c65de9e6a8afed7705bc |
| $\bar\pi$ | 55b8b3cf2d2b51e26ebf80b572a6a62c3db609988499e564e0919b439dc2c01d |

完整十二点代数中、约化为不变分量之前的全部22列七项 Taylor 哈希：

| 核 | 全十二点 jet SHA-256 |
|---|---|
| $\pi$ | b8fd7d44d815a39ec128d70ac2b8fad621cdf1700691ac01834409743786b6f8 |
| $\bar\pi$ | b6983997c8ed274b6b9333db3ffb33b59bd433c794a242be1098033ad39b9e3d |

三个后继完整来源的哈希为：

| 来源 | 完整22列向量 SHA-256 |
|---|---|
| $B_{130}$ | ce676c4bb9243b89b1c32397f5ca7b1d7c1135575b82cebf0e935647d1ab251c |
| $K_{130}$ | 851b119ed2c4d1770c72010461724b9c6e45e71b4dfe8937ff33b9e0a120d588 |
| $C_{130}$ | 5d58896fc844512c27bed9cca3258665a3a9074b257a0723c77db850697a6a8f |

原48纤维、原22列、R987/R993/R992 的所有旧门在同次入口全部保留并通过。
本篇的新结论是(20)、(33)–(35)及(40)–(41)所支付的实际固定边界，
不将该中间结果登记为课题完成。

