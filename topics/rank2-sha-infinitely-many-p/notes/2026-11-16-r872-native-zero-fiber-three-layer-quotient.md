# 原零纤维前三层的有限商与同一首核的实际二／三行

日期：2026-11-16。**状态：以下真实有限商、原低系数读取和其准确退化范围已证明；完整 $K_1$ 在这些行中的像、其它底纤维及原三尾 $\Pi$ 的联合像仍未判定。**

本注接[原有限纤维商](2026-11-16-r872-native-finite-fiber-quotient-and-cubic-ramification.md)。它只把物理 $t=0$ 纤维中的一个明确商写成实际低系数，**不把它认作整个 $\mathscr T_{D,0}$**，也不以低前缀的可赋值替代全 $K_1$。

## 1. 原零角及有限三次因子

沿用原 $r=3$、$\tau=3+2h-s\in\{1,2,3\}$、
$\tau<\ell\le h-1$、$T=s-13>3$、
$D\ge4b$ 和 $p>D+40$。
仍取同一个原不可约 $F$，满足
$$
\deg_YF(0,Y)=3,\qquad F(0,1)=0,\qquad F_Y(0,1)\ne0 .
$$
只在系数记录中用前注的本原多项式代表 $\widehat F$，并乘一个 $k^\times$ 常数使
$$
F_0(Y)=\widehat F(0,Y)
$$
monic。它不改变任何因子格或实际来源提升。

原 $t^3F^4q$ 来源且 $q(0,1)\ne0$ 给
$$
\boxed{v_0(\widehat F)=-3,\qquad
v_0=\min_n(4\operatorname{ord}_t f_n-n).}
\tag{1}
$$
证明是 $\deg F_0=3$ 给 $v_0(\widehat F)\le-3$；
$q(0,Y)\ne0$ 给 $v_0(q)\le0$；
同一原 Gauss 下界
$12+4v_0(\widehat F)+v_0(q)\ge-2$
迫 $v_0(\widehat F)\ge-3$。
固定清分母 $d^c$ 在此处的 Gauss 值为零。

在 $k[[t]]$ 的有限 $Y$ 图作 Weierstrass 分解，得到唯一 monic 度三因子
$$
F_{\rm fin}(t,Y)=F_0(Y)+tF_1^{\rm fin}(Y)+O(t^2),
\quad\deg_Y F_1^{\rm fin}\le2.
$$
其余因子在 $t=0$ 的有限图为单位。记
$$
\mathcal A=k[[t]][Y]/F_{\rm fin},\qquad
\mathcal A_0=k[Y]/F_0 .
\tag{2}
$$
这保了有限三次代数，包括另外两根可能重合或等于零的情形。这里只把原物理根 $1$ 用已付导数单位单独分出。

若
$\widehat F=F_0+t\widehat F_1+O(t^2)$，则准确有
$$
F_1^{\rm fin}=\operatorname{rem}_{F_0}\widehat F_1 .
\tag{3}
$$
因为 Weierstrass 单位在 $t=0$ 为一，其一次项只加一个 $F_0$ 倍数。

## 2. 两个真实 primitive 列与有限商

始终用原 $L=Y\partial_Y+40$。定义
$$
b_0=\left[L^{-1}(F_0^3)\right]\in\mathcal A_0,\qquad
b_1=\left[L^{-1}(YF_0^3)\right]\in\mathcal A_0,\qquad
V=\operatorname{span}_k\{b_0,b_1\}.
\tag{4}
$$
$L^{-1}$ 在此仅把次数 $n$ 的系数除以 $40+n$；
所用次数至多十，都是原单位。

由 (1)，前注的真正 residual 角格在 $j=3$ 时给
$$
[t^2]A_3\in k+kY,\qquad [t^0]A_3=[t^1]A_3=0 .
$$
因此在**底 DVR 的原系数束**上，
$$
\boxed{
\operatorname{im}\left(\mathbf J_{3,0}\longrightarrow
\mathcal A/t^3\mathcal A\right)=t^2V.
}
\tag{5}
$$
反向包含也确实成立于这个底 DVR 格：原 $n=0,1$ residual 系数都恰从 $t^2$ 开始，其它固定角在此为单位，所以这两列可分别取到。
全球 $H^0(\mathbf J_3)$ 的像只保证包含于 (5)；其余角帽和全球连接类没有删除。

另一个真来源事实是
$$
\mathcal W_D\longrightarrow\mathcal A/t^3\mathcal A
\quad\text{满射}.
\tag{6}
$$
这里是全部原 $\mathcal W_D$，不是 $K_1$。
只需使用原 $n=0,1,2$ 三列：它们在 $t=0$ 的角因子为单位，且原剩余多项式帽至少容纳三个 Taylor 系数；$1,Y,Y^2$ 是 (2) 的真基。
逐列用这些固定角单位的二阶逆截断选择真实多项式，给出 (6)。这个构造没有省去 $h_7,t-1,d$。

$F$ 因子列在 $\mathcal A$ 上为零，(5) 因而给前注实际有限层的一个明确满商
$$
\boxed{
\mathscr T_{D,0}\twoheadrightarrow
Q_0:=\frac{\mathcal A/t^3\mathcal A}{t^2V}.
}
\tag{7}
$$
由 (6)，原全来源到 $Q_0$ 也满射。
令 $v=\dim_kV$，则 $Q_0$ 的准确底 $t$ 指数为
$$
\boxed{
\underbrace{2,\ldots,2}_{v\text{ 个}},
\quad
\underbrace{3,\ldots,3}_{3-v\text{ 个}};
\qquad \dim_kQ_0=9-v .
}
\tag{8}
$$
这只分类 (7) 的商，不分类完整 $\mathscr T_{D,0}$。

若
$$
\boxed{\gcd(F_0,YF_0')=1,}
\tag{9}
$$
则 $v=2$，故 (8) 为 $(2,2,3)$。
完整证明只用真多项式，而不借数值行列式：考虑三列
$$
A\in k[Y]_{\le2}\longmapsto
L^{-1}(F_0^3A)\bmod F_0 .
$$
若其值为零，则 $W=L^{-1}(F_0^3A)$ 被 $F_0$ 整除。
由 (9)，逐次除法同前注迫 $F_0^4\mid W$。
但 $\deg W\le11<12$，所以 $W=A=0$。
三列矩阵可逆，前两列 (4) 必独立。
条件 (9) 不由原物理根 $1$ 简单自动推出；失败时始终保 (4)、(7)、(8) 的真实秩。

## 3. 分出同一个物理根，不能给其它两根赋条件

由 $F_Y(0,1)\ne0$，取原分支 $\psi(t)$ 并写
$$
F_{\rm fin}=(Y-\psi(t))G(t,Y),\qquad
G=G_0+tG_1+O(t^2),\quad\deg_YG=2 .
$$
准确有
$$
G_0=\frac{F_0}{Y-1},\qquad
\psi_1=-\frac{F_1^{\rm fin}(1)}{F_0'(1)},\qquad
G_1=\frac{F_1^{\rm fin}+\psi_1G_0}{Y-1}.
\tag{10}
$$
后一分子在 $Y=1$ 为零。$G_0(1)\ne0$，
所以原有限代数实际分裂为
$$
\mathcal A\simeq k[[t]]\oplus
\mathcal B,\qquad
\mathcal B=k[[t]][Y]/G(t,Y).
\tag{11}
$$
二次块可为域、分裂代数或含幂零元，均不删。

记
$$
u_i=b_i(1),\qquad c_i=\operatorname{rem}_{G_0}b_i,\qquad
V_-=\{a_0c_0+a_1c_1:\ a_0u_0+a_1u_1=0\}
\subset\mathcal B_0:=k[Y]/G_0 .
\tag{12}
$$
若 $\varepsilon=\operatorname{rank}(\operatorname{ev}_1|_V)\in\{0,1\}$，
则
$$
\dim V_-=v-\varepsilon .
\tag{13}
$$
这包括两列本身相关的退化情形。

对真正 $W\in K_1$，原三个长块的常数行给 $[t^0]W=0$；
原同分支 Taylor 还给
$\operatorname{ord}_tW(t,\psi(t))\ge T>3$。
所以其在 (11) 中模 $t^3$ 的值必为
$$
(0,\ t\beta_1+t^2\beta_2),\qquad
\beta_1,\beta_2\in\mathcal B_0 .
$$
与 $t^2V$ 的交恰为 $t^2V_-$，从而得到一个**真正来源读取**
$$
\boxed{
\mathcal B_{\rm low}:K_1\longrightarrow
\mathcal B_0\oplus(\mathcal B_0/V_-),\qquad
W\longmapsto(\beta_1,\ \beta_2\bmod V_-).
}
\tag{14}
$$
所选 $1,Y$ 基决定这个直和写法；内在对象是同一个 (7) 的过滤商，不能独立移动两个系数。

其目标维数准确是
$$
\boxed{4-v+\varepsilon.}
\tag{15}
$$
在 (9) 下，它是二或三维：若 $(u_0,u_1)=(0,0)$，只剩 $\beta_1$ 的两行；否则 $\dim V_-=1$，留下两条 $\beta_1$ 行和一条真实 $\beta_2$ 行。
没有证明 $K_1$ 到 (14) 满射。

## 4. 每行都用同一个原 $W$ 的完整低系数读取

写原多项式在 $t=0$ 的真展开
$$
W=t\,w_1(Y)+t^2w_2(Y)+O(t^3).
$$
原帽给 $\deg w_1\le6$、$\deg w_2\le10$；
这些是来源系数，不是记号 $W_i$ 所表示的 Euler 读取。

对同一个 $G_0,G_1$，准确有
$$
\boxed{
\begin{aligned}
\beta_1&=\operatorname{rem}_{G_0}w_1,\\
\beta_2&=\operatorname{rem}_{G_0}
\left(w_2-G_1\operatorname{quo}_{G_0}w_1\right).
\end{aligned}}
\tag{16}
$$
证明是
$w_1=G_0a+\beta_1=(G-tG_1)a+\beta_1+O(t^2)$，
代入同一个二次商后保留到 $t^2$。
因此第二行必须保 $G_1$，不能只对 $F_0$ 作静态值代入。

若 (9) 成立且 $(u_0,u_1)\ne(0,0)$，则
$$
z_{\rm crit}=u_1c_0-u_0c_1\ne0
$$
生成 (12) 的一维空间。写 $z_{\rm crit}=a+bY$，最后那一行可取
$$
\boxed{
a\,[Y]\beta_2-b\,[1]\beta_2 ,
}
\tag{17}
$$
连同 $\beta_1$ 的两个坐标。至少一个 $a,b$ 非零；这只是行规范的单位选择，不是该行对指定 $K_1$ 非零。

原首核的 $t^1$ 条件还保
$$
w_1=(Y-1)^4a_2(Y),\qquad\deg a_2\le2,
\tag{18}
$$
因为 $\ell>1$ 且四个原 Euler 读取在该层同时为零。
式 (16)–(18) 并不授权任选 $a_2,w_2$：余下所有长前缀及末块仍对同一 $W$ 施加条件。

## 5. 它是全来源余商的真实读者，但没有代替三尾

(14) 杀掉
$$
K_1\cap\mathscr J_3,\qquad K_1\cap\mathscr V_1 .
$$
前者由 (5)、原物理值零及 (12)；后者因其整个有限因子值为零。
故它准确下降到
$$
\boxed{
K_1\big/\big((K_1\cap\mathscr V_1)+(K_1\cap\mathscr J_3)\big).
}
\tag{19}
$$
这与前注保留的实际有限层／全球连接类相容。

但 (7) 只是整个有限层的一个商，(14) 的像仍须用原完整前缀求出。
没有证明这些二／三行等于 $\Pi$，没有证明其它底纤维或 $H^1$ 连接类消失，也没有把另外两个有限支认成算术测试。
对于 $R\mapsto R+W$ 或 $S\mapsto S+W$，只能按同一个 $W\in K_1$ 同时改变 (14)、原 $\Pi$、全部 normal 与三条十三行 carry。

本注仅使用原符号、实际有限帽与三次多项式商，无新增数学数值运行。
