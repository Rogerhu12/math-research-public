# R66：全射线收缩的真实直纹环带族

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。
状态：**已证明；未参与者全文独审通过；不是闭曲面结果。**
正式整理：root；独审：independent_audit；2026-11-10。

本稿构造一个固定正宽、真实非线性、共同度量的 $C^\infty$ 嵌入环带族。
全部材料角变量精确闭合，存在逐点固定的开握持区，所有径向射线一开始
都向内收缩；全部非解析入口位于严格负曲率区。整环带同时有定量
reach 与握持直径门。两条径向边界尚未封住，也未给出 $0.05D$ 的有效幅度。

六秩初态由 root 提出并精确复算。本稿使用并完整说明其有限维输入；
root 的六秩贡献不算本稿的未参与者独审。配套文件是
[六秩完整原稿](../notes/2026-11-10-78718-root-ruled-port-rank.md)和
[冻结有理脚本](../scripts/78718-check-ruled-port-rank.py)。
本稿未运行 ODE、PDE、曲面优化或网格生成。

## 1. 精确命题与范围

固定 $h=1/100$。存在 $\tau_*>0$、一个固定解析度量 $g$ 以及实际映射

$$
F_\tau:[0,h]\times\mathbb R/(\ell\mathbb Z)\longrightarrow\mathbb R^3,
\qquad |\tau|\le\tau_* ,
$$

满足下列结论。

1. 每个 $F_\tau$ 是 $C^\infty$ 嵌入，且在全部阶数上光滑依赖 $\tau$；
   $F_\tau^*\langle\ ,\ \rangle=g$ 精确成立。
2. 有固定闭集 $H$，其内部非空，$F_\tau|_H=F_0|_H$；若
   $D=\operatorname{diam}F_0([0,h]\times S^1)$，则
   $D<203/100$、$\operatorname{diam}F_0(H)\ge2$。
3. 对全部 $\tau$，含两条边界的整个像满足
   $\operatorname{reach}(F_\tau)\ge1/8$，故
   $\operatorname{reach}/D>25/406>0.03$。
4. 写 $g=dr^2+a(r,u)^2du^2$，则全部射线上 $a_r<-99/200$。
   $K\le0$，全部非解析角点的一个固定开邻域中 $K<0$。
5. 每个非零 $\tau$ 的**整个像**均不与初态像在 $\mathrm E(3)$ 下全等；
   这包含反射和两条边界的交换。

这是一条实际环带族，不是有限阶形式解。第 5 点只给严格非平凡性，
不含有效的 Hausdorff 振幅下界。有限的 $\ell$-周期闭合不等于封住两条
$r$ 边界，因此它仍只支付本题的入口结构。

## 2. 解析闭曲线和倾斜标架

令 $v\in\mathbb R/(2\pi\mathbb Z)$，固定

$$
\epsilon=\frac1{10},\qquad
\gamma_0(v)=(\cos v,\sin v,\epsilon\cos2v),\qquad
s=|\gamma_{0,v}|.
\tag{1}
$$

水平投影是单位圆，所以 $\gamma_0$ 为解析闭嵌入。
令 $u(v)=\int_0^v s(w)\,dw$，$\ell=u(2\pi)$；它给一个固定的解析弧长
坐标。以下撇号表示 $u$ 导数。取

$$
\mathcal D=s^2\gamma_{0,vv}
 -(\gamma_{0,v}\cdot\gamma_{0,vv})\gamma_{0,v},\qquad
W=\mathcal D+\gamma_{0,v}\times\mathcal D,
\qquad d_0=\frac W{|W|}.
\tag{2}
$$

有 $\mathcal D\cdot\gamma_{0,v}=0$，且
$\mathcal D\cdot(\cos v,\sin v,0)=-s^2<0$，故归一化合法。
设 $(T_0,n_F,b_F)$ 为真实 Frenet 标架，$k_F>0$ 为曲率，
$\theta=\arctan s$。则

$$
d_0=\cos\theta\,n_F+\sin\theta\,b_F,
\qquad N_0=d_0\times T_0
 =\sin\theta\,n_F-\cos\theta\,b_F.
\tag{3}
$$

定义固定解析周期函数

$$
\alpha=d_0'\cdot T_0=-k_F\cos\theta,
\qquad
\beta=d_0'\cdot N_0=-(\theta'+\tau_F),
\qquad
\kappa_0=T_0'\cdot N_0=k_F\sin\theta.
\tag{4}
$$

因此 $\alpha<0$、$\kappa_0>0$。这里 $\tau_F$ 是曲线扭率，
与族参数 $\tau$ 不同。特别地，$\beta$ 的扭率项为负号。

## 3. 全圈低阶常数与严格负 K 控制区

写 $x=\sin2v$、$c=\cos2v$，并令
$p=|\gamma_{0,v}\times\gamma_{0,vv}|$。直接微分给

$$
s^2=1+\frac{x^2}{25},\qquad
p^2=\frac{29-3x^2}{25},\qquad
k_F=\frac p{s^3},\qquad
\tau_F=\frac{15x}{29-3x^2}.
\tag{5}
$$

于是

$$
1\le s<\frac{51}{50},\quad p<\frac{27}{25},\quad
\frac{25}{26}\le k_F<\frac{11}{10},\quad
\frac35< -\alpha<\frac45,\quad
\frac35<\kappa_0<\frac45.
\tag{6}
$$

例如 $k_F^2=(29-3x^2)/(25(1+x^2/25)^3)$ 随 $x^2$ 递减，
故其最小值为 $(25/26)^2$。上界 $|\alpha|,\kappa_0<4/5$
也可直接由 $p<27/25$、$s\ge1$、$\sqrt{1+s^2}>7/5$ 得到。
下界使用 $k_F\ge25/26$、$\cos\theta>2/3$、
$\sin\theta\ge1/\sqrt2>7/10$。

又有

$$
\theta'=\frac{(2/25)xc}{(1+x^2/25)(2+x^2/25)},
\quad
\beta=-x\left\{\frac{15}{29-3x^2}
 +\frac{(2/25)c}{(1+x^2/25)(2+x^2/25)}\right\}.
\tag{7}
$$

花括号大于或等于 $15/29-1/25=346/725>0$；在 $x=0,c=-1$ 取等号。因此 $\beta$ 的零点
恰为 $v\in(\pi/2)\mathbb Z$。选固定开弧

$$
J_v=(\pi/8,3\pi/8),\qquad J=u(J_v).
\tag{8}
$$

在其闭包上，$x\ge1/\sqrt2>7/10$，所以
$|\beta|>(7/10)(346/725)>1/3$。全圈则有

$$
|\beta|\le\frac{15}{26}+\frac1{25}<\frac58.
\tag{9}
$$

为后面的 reach 估计，记录三个导数界：

$$
|\alpha'|<\frac3{10},\qquad
|\kappa_0'|<\frac3{10},\qquad
|\beta'|<\frac85.
\tag{10}
$$

完整核法如下。$|s_v|\le1/25$、$|p_v|\le3/25$ 给
$|(k_F)_u|\le3/25+81/625=156/625<1/4$。
由 (7) 有 $|\theta'|\le1/25$，故前两项小于
$1/4+(4/5)(1/25)<3/10$。
此外
$|(\tau_F)_u|\le30\cdot32/26^2=240/169$。
置 $G=xc$、$B=(1+x^2/25)(2+x^2/25)$，则
$|G|\le1/2$、$|G_v|\le2$、$B\ge2$、
$|B_v|\le154/625$。因此

$$
|\theta''|\le\frac2{25}
 \left(1+\frac{77}{2500}\right)<\frac1{10},
$$

从而 $|\beta'|<240/169+1/10<8/5$。

## 4. 完整 SE(3) 端点映射确实有六秩

保持 (4) 的 $\alpha,\beta$ 固定，仅令 $\kappa(u)$ 可变，解

$$
\begin{aligned}
d'&=\alpha T+\beta N,&
T'&=-\alpha d+\kappa N,&
N'&=-\beta d-\kappa T,&
\gamma'&=T.
\end{aligned}
\tag{11}
$$

初值取 $u=0$ 的实际基线位置与标架。
矩阵右端反对称，所以全过程保持正定向正交标架。
记 $G=(R,\gamma)\in\mathrm{SE}(3)$，$R=(d,T,N)$。
对扰动 $\delta\kappa=f$，端点右平凡化变分为

$$
\delta G(\ell)G(\ell)^{-1}
 =\int_0^\ell f(u)
 \binom{d_0(u)}{\gamma_0(u)\times d_0(u)}\,du.
\tag{12}
$$

这由 $G'=G\xi$ 的常规 ODE 变分直接得到：控制项是体坐标
$(fe_1,0)$，而
$\operatorname{Ad}_{(R,\gamma)}(e_1,0)
=(d,\gamma\times d)$。更换端点的六维局部坐标只施加可逆线性变换。

为使六秩不是一般性假设，取以下六个真实圆周点：

$$
(\cos v,\sin v)=(1,0),(0,1),(-1,0),
(3/5,4/5),(5/13,12/13),(-3/5,4/5).
$$

将各点的 (12) 列乘以正数 $|W|$，即得有理列
$(W,\gamma_0\times W)^\mathsf T$。root 的冻结有理消元给

$$
\det[\mathcal P(v_1)\ \cdots\ \mathcal P(v_6)]
=\frac{15838112388562926448768487424}
 {9876209658570587635040283203125}>0.
\tag{13}
$$

完整列构造与无浮点消元源见本稿开头的配套文件；实际复算报告为
`../notes/2026-11-10-78718-root-ruled-port-rank-check.json`，而不是本稿新跑的计算。

令 $V(u)=(d_0,\gamma_0\times d_0)^\mathsf T$。它是解析周期向量函数。
若某个非空开弧内的 $V(u)$ 只张成真子空间，取消去该空间的非零线性
泛函，解析恒等定理使它在全圈消去 $V$，与 (13) 矛盾。
所以**任意**非空开弧中都能选出六个不同点，使六列独立。

## 5. 七个固定 bumps 和真实局部闭合族

先在 $J$ 内选两个闭包不相交的非空开区间 $I_f,I_c$。
在 $I_f=(a_f,b_f)$ 取固定非零自由 bump

$$
f(u)=\begin{cases}
\exp\{-1/((u-a_f)(b_f-u))\},&a_f<u<b_f,\\
0,&\text{其余点}.
\end{cases}
\tag{14}
$$

在 $I_c$ 中由第 4 节选六个独立点。分别取互不相交、足够窄的
开区间，并用同一平端公式取非负、单位积分控制 bumps $f_j$。
当支撑收缩到所选点时，$\int f_jV$ 趋于相应点值列；故可以一次性
固定正的六个宽度，使该真实积分矩阵可逆。此后不再随 $\tau$ 改变
支撑、宽度或共同度量。

设

$$
\kappa_{\tau,b}=\kappa_0+\tau f+\sum_{j=1}^6 b_jf_j.
\tag{15}
$$

在基线端点附近，以 $\log(G_{\tau,b}(\ell)G_0(\ell)^{-1})$
的六个李代数坐标定义闭合映射 $\mathcal E(\tau,b)$。
它由有限区间 ODE 对有限参数的光滑依赖而光滑；事实上系数对这些参数
解析，故它也解析。$\mathcal E(0,0)=0$，且 (12) 给
$D_b\mathcal E(0,0)$ 可逆。

有限维隐函数定理给 $b=b(\tau)$、$b(0)=0$，在一个固定正区间上
**精确**满足 $\mathcal E(\tau,b(\tau))=0$。记相应实际解为
$(\gamma_\tau,d_\tau,T_\tau,N_\tau)$，并缩短参数区间使
$\kappa_\tau>1/2$。

全部控制系数、整个标架和曲线在所有有限阶数上光滑依赖 $\tau$。
系数在 $u=0,\ell$ 的一个开邻域完全等于基线；端点位置和标架也完全
相同。因此 ODE 的唯一性把整套解延拓为 $\ell$ 周期的 $C^\infty$ 解，
并匹配全部角向 jets。这同时支付位置与旋转闭合。

从基点正向到 $J$ 前，解与基线相同。从 $u=\ell$ 反向到 $J$ 后，
由相同末值和相同系数再次相同。因此

$$
(\gamma_\tau,d_\tau,T_\tau,N_\tau)
=(\gamma_0,d_0,T_0,N_0)\quad\text{在 }S^1\setminus J.
\tag{16}
$$

所有非解析角点都在 (14) 和六个控制区间的端点，全部位于 $J$ 内。
这些实际指定函数在其余每一点局部解析。自由支撑与控制支撑分离，
所以每个非零 $\tau$ 都在 $a_f,b_f$ 处有不可消去的非解析平端。

## 6. 精确共同度量、第二形式与全射线收缩

定义实际映射

$$
F_\tau(r,u)=\gamma_\tau(u)+r d_\tau(u),\qquad0\le r\le h.
\tag{17}
$$

由 (11)，

$$
(F_\tau)_r=d_\tau,\qquad
(F_\tau)_u=(1+r\alpha)T_\tau+r\beta N_\tau.
$$

于是其精确第一形式为

$$
\boxed{g=dr^2+a^2du^2,\qquad
a^2=(1+r\alpha)^2+r^2\beta^2.}
\tag{18}
$$

它不含 $\tau$。单位法向是
$\mathcal N_\tau=((1+r\alpha)N_\tau-r\beta T_\tau)/a$。
直接再微分得实际第二形式

$$
L=0,\qquad M=\frac\beta a,\qquad
C=a\kappa_\tau+
\frac{r(1+r\alpha)\beta'-r^2\beta\alpha'}a.
\tag{19}
$$

故

$$
K=\frac{LC-M^2}{a^2}=-\frac{\beta^2}{a^4},\qquad
aa_{rr}=\frac{\beta^2}{a^2}.
\tag{20}
$$

所有非解析角点附近由 $|\beta|>1/3$ 给严格负 $K$。
这些射线的初始 $a_r=\alpha<0$，并非从圆柱的零斜率出发。
这是本构造避开 R64 固定正 $k$ 射线单调扩张前提的确切原因。

由 (6)、(9)，
$\alpha^2+\beta^2<21/20$。
在更大的 $0\le r\le1/10$ 窗口中，

$$
a_r=\frac{\alpha+r(\alpha^2+\beta^2)}a,\qquad
\alpha+r(\alpha^2+\beta^2)<-\frac35+\frac{21}{200}
=-\frac{99}{200}.
$$

故 $a$ 递减、$a\le1$，从而 $a_r<-99/200$。
实际固定宽度 $h=1/100$ 上另有
$a>1-(4/5)h=124/125$。
更精确地，$\kappa_0>35/52$。由 (19)，基线 $C$ 大于
$(124/125)(35/52)-\{(1/100)(8/5)+(1/10000)(5/8)(3/10)\}/(124/125)$，
该数大于 $13/20$。再使 $\|\kappa_\tau-\kappa_0\|_\infty<1/50$，
就有全族的 $C>3/5$。
这一点不被用于取代后续尚未构造的帽接口。

## 7. 基线全弦长与坐标 Hessian

下面给出可用于含边界 reach 的全局常数，而不只给局部曲率界。
本节先写 $F_0$。由 (10)、(11)，

$$
|d_0'|^2=\alpha^2+\beta^2<\frac{21}{20},
$$

$$
d_0''=-(\alpha^2+\beta^2)d_0
 +(\alpha'-\beta\kappa_0)T_0
 +(\alpha\kappa_0+\beta')N_0.
$$

三个系数的绝对值分别小于 $21/20,4/5,56/25$，其平方和小于 $9$，
故 $|d_0''|<3$。所以

$$
F_{0,rr}=0,\quad |F_{0,ru}|<21/20,\quad
|F_{0,uu}|\le k_F+h|d_0''|<23/20.
$$

矩阵 $\left[\begin{smallmatrix}0&21/20\\21/20&23/20\end{smallmatrix}\right]$
的最大特征值小于 $9/5$：$9/5$ 倍单位矩阵减去它的两个主子式
均为正。因此对任意参数向量 $w$，

$$
|D^2F_0[w,w]|<\frac95|w|^2.
\tag{21}
$$

给两点选 $|\Delta u|\le\ell/2$ 的 lift，令
$w=(\Delta r,\Delta u)$。参数直线完全留在带中。
若 $|w|\le1/2$，第一形式 (18) 与 Taylor 余项给

$$
|F_0(x+w)-F_0(x)|
\ge\left(\frac{124}{125}-\frac9{20}\right)|w|
=\frac{271}{500}|w|>\frac{27}{50}|w|.
\tag{22}
$$

若 $|w|>1/2$，则 $|\Delta u|>49/100$。
因为 $s(v)$ 有 $\pi$ 周期，所选 lift 对应 $|\Delta v|\le\pi$；
水平圆弦与 $s<51/50$ 给

$$
|\gamma_0(u)-\gamma_0(\tilde u)|
\ge\frac2\pi|\Delta v|
\ge\frac{100}{51\pi}|\Delta u|>\frac35|\Delta u|.
$$

减去最多 $2h=1/50$ 的两条直纹位移，再用
$|w|<(51/50)|\Delta u|$，得到

$$
|F_0(x+w)-F_0(x)|
>\left(\frac35-\frac2{49}\right)\frac{50}{51}|w|
=\frac{6850}{12495}|w|>\frac{27}{50}|w|.
\tag{23}
$$

因此基线本身已由全弦长界证明为嵌入，没有预先假定其直纹偏移不交。

## 8. 全参数嵌入与含边界 reach

由第 5 节的实际 $C^\infty$ 参数依赖，可以一次性缩短同一个正
$\tau_*$，使全族

$$
\|D(F_\tau-F_0)\|\le\frac1{50},\qquad
|D^2F_\tau[w,w]|\le2|w|^2.
\tag{24}
$$

沿上述参数直线积分第一项，结合 (22)–(23)，给

$$
|F_\tau(x+w)-F_\tau(x)|
\ge\frac12|w|.
\tag{25}
$$

这证明全部允许 $\tau$ 都为嵌入。
若空间点 $y$ 有两个不同最近点 $p=F_\tau(x)$、
$q=F_\tau(x+w)$，共同距离为 $d$，参数直线的单侧极小点条件给

$$
(y-p)\cdot DF_\tau(x)w\le0.
$$

该条件在两条边界同样成立。由 (24) 的 Taylor 余项，

$$
|q-p|^2=2(y-p)\cdot(q-p)\le2d|w|^2.
$$

而 (25) 的平方给 $|q-p|^2\ge|w|^2/4$，故 $d\ge1/8$。
紧像总有最近点，所以这正是

$$
\boxed{\operatorname{reach}(F_\tau([0,h]\times S^1))\ge1/8.}
\tag{26}
$$

它检验整个含边界像的最近点唯一性，包含内侧、外侧及边界法锥。

## 9. 固定 H、完整直径及像非全等

定义

$$
H=[0,h]\times(S^1\setminus J).
\tag{27}
$$

它为闭集且内部非空，由 (16) 被全族逐点固定。
在 $r=0$，$v=0,\pi$ 两点都属于 $H$，相距 $2$。
初始曲线的水平直径为 $2$、高度范围为 $1/5$；每条直纹长度至多 $h$。
故

$$
D\le\frac{\sqrt{101}}5+2h<\frac{203}{100},\qquad
\frac{\operatorname{diam}F_0(H)}D>\frac{200}{203},\qquad
\frac{\operatorname{reach}(F_\tau)}D>\frac{25}{406}.
\tag{28}
$$

最后证明**集合**非全等。初态的两条边界
$u\mapsto F_0(0,u)$ 与 $u\mapsto F_0(h,u)$ 都是解析正则嵌入曲线。
其局部弧长坐标是解析坐标：速度是严格正的解析函数，积分与逆映射
均解析。因此任何单位弧长参数化只可能差 $u\mapsto\pm u+c$，仍解析。

若某个非零 $\tau$ 的整个环带像与初态像由某个 $A\in\mathrm E(3)$
对应，作为嵌入流形的拓扑边界也必须对应。于是其 $r=0$ 边界
$\gamma_\tau(u)$，无论对应初态的哪一条边界，都是解析的单位弧长曲线。
由 (11)，它的普通空间曲率满足

$$
|\gamma_\tau''(u)|^2=\alpha(u)^2+\kappa_\tau(u)^2.
\tag{29}
$$

左边若解析，因 $\alpha$ 解析而 $\kappa_\tau>1/2$，正平方根反解
迫使 $\kappa_\tau$ 解析。
但在自由 bump 端点的一个邻域中，控制 bumps 恒为零，所以
$\kappa_\tau=\kappa_0+\tau f$；$f$ 一侧恒零、另一侧严格正且全部
端点导数为零。每个非零 $\tau$ 都使它非解析，矛盾。

这个论证并没有从“材料点固定”跳到“集合刚体变换固定该点”，也没有
假设刚体变换保留某条指定边界；反射与边界交换均已覆盖。

对每个这样的非零 $\tau$，两个紧像的刚体 Hausdorff 距离的最小值
严格为正：若下确界为零，近似最小序列的平移必有界，旋转与反射部分
位于紧群 $O(3)$；取子列得到一个实现零距离的刚体变换，违背刚才的
非全等性。因此本有边族也确实有 $\delta_{\rm E}>0$。

## 10. 这条入口结构支付了什么，仍缺什么

本稿给出固定 $h$、固定共同度量、固定支撑的真实非线性族，位置和标架
完整闭合、固定开 $H$、定量全时 reach 与严格像非全等均已证明。
特别是 $a_r<0$ 遍及整圈，而非解析端点落在 $C>0$ 的严格双曲区，
从入口就不具有 R64 的“固定坏射线由零斜率向外增长”障碍。

下一步必须从实际 $r=h$ 的整圈第二形式及位置/标架继续求解。
当前 $a$ 始终有正下界；(18) 的二次函数也不能原样一直缩到正则帽点。
需要新的混合曲率段、真正帽端匹配或另一种闭面拓扑拼装。
本稿没有这种帽，也不把局部 IFT 的未知小区间当作有效 $0.05D$ 幅度。

取 $F_t=F_{t\tau_*}$、$t\in[0,1]$，保持 $t=0$ 为上述直径估计的初态。
它仍是一族精确等距**有边环带**；本题完成标准的闭曲面与大幅度两项仍未支付。


## 11. 正式采纳、独立审查与真实执行身份

原作者完整稿为
[2026-11-10-78718-geometry-contracting-ruled-core-v1.md](../notes/2026-11-10-78718-geometry-contracting-ruled-core-v1.md)，
16091 B，SHA256 `cbdd1671eefd0e562df74ffe09a294f23af9f311b430b11f5909797943780819`。
root 已逐节全文读取并核对（实际工具 `cb3aa1`），没有把摘要代替全文。

未参与作者推导的 independent_audit 给出
[完整环带审稿](../notes/2026-11-10-78718-audit-contracting-ruled-core.md)，
21180 B，SHA256 `88c6ab5c52ad09eaf5adfb4130392f130b002bd73d9dc0eb6ada6470102d8a31`。
root 再次全文读取其全部十节（实际工具 `8f122d`），并在本正式稿落实三项订正：
全局花括号下界改为非严格号；两处漏写的公式间距修复；题设时间采用单侧子族，保留初态。
这些订正不改变原双侧局部族及其任何几何结论。原稿与审稿均保留冻结身份。

六秩输入另经
[完整独立六秩审稿](../notes/2026-11-10-78718-audit-ruled-port-rank.md)，
11482 B，SHA256 `3a7d6def8e7ec2959782078798469bc45e00367fbcfc3f9d7df32273489b477e`；
root 全文核对工具 `772866`。原脚本由 root 实跑 `3fb5bc`、独审者另跑 `130cd1`，
两次均正常 exit 0；确定性711 B报告SHA256
`cea200fb30287df84d815167d50739324ebb0fa8b9a7ac3a1045d488376ece4a`。
独审者另以三重积重新造列并作720项整数Leibniz求和，实际工具 `244f32`、exit 0；
919 B报告SHA256 `4d6c8ecaa8bde7d264834b77dda33943134dcebdf7835e998619d3b15af74b4a`。

全部几何常数另用39条纯有理余量检查，实际工具 `604846`、exit 0、39 PASS：
[独立程序](../notes/2026-11-10-78718-audit-contracting-ruled-constants.py)，
SHA256 `fae7af9e61dea590abe2a9d730ab764d06cb195dd9257d87140fe58103f42957`；
[标量回执](../notes/2026-11-10-78718-audit-contracting-ruled-constants.json)，
4260 B，SHA256 `84460be4c65c00c4e2a40ad74bb98c1c5ea7c32ac407e425e6821e039619a257`。
这些实际程序只核有限精确代数及常数，不冒充运行了非线性 ODE/PDE、曲面优化或网格。
真实族的存在由上文完整有限维隐函数定理、周期重构和几何证明支付。

本结果未使用、未修改、未认证本题运行中的 M14 数值候选，也没有满足 README 完成标准。
