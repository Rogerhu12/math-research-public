# R1060：实际 X0(108) 非 CM Cartier、Legendre 值与九挠点普通性

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：R1059 的同一个实际模型上，全部非 CM Cartier 块由一个明确值 $B_n$ 控制，而且 $B_n=P_n(3)=-a_p(E_{54})$。** 显式九阶有理挠点与三次同源进一步证明：在原 $p\equiv2,5\bmod9$ 范围，$B_n$ 必为单位。本篇尚未证明 R1059 的不同读数 $S_n$ 非零，不把非 CM 普通性自动作用于指定 Raynaud 配对。

## 1. 原模型、完整基及非 CM 子格

对 $p=6N+5\ge5$，置 $n=(p-2)/3=2N+1$。保持 R1059 已固定的实际模型
$$
z^3=1-\kappa x^3,\quad w^3=1+\kappa x^3,\quad
\kappa=3s,\quad s^2=-3,\quad s=\zeta-\zeta^2,
\qquad \Omega=\frac{dx}{z^2w^2}.
\tag{1060.1}
$$
同构、原 $q$ 参数及全部微分标量已经由 R1059 付清；本文没有另选模型。

它是平滑 $(3,3)$ 完全交，adjunction 给 $K_X=\mathcal O_X(2)$，其 ideal 没有二次项。因此十个次数至多二的单项式乘 $\Omega$ 正好是 $H^0(K_X)$ 的完整基。六条实际 CM 微分为
$$
\Omega,\ x\Omega,\ x^2\Omega,\ z^2\Omega,\ zw\Omega,\ w^2\Omega.
\tag{1060.2}
$$
它们分别来自 R1059 的 $g,c,d,a-\zeta b,h,a-\zeta^2b$。

另外四条
$$
v_1=z\Omega,\quad v_2=w\Omega,\quad
v_3=xz\Omega,\quad v_4=xw\Omega
\tag{1060.3}
$$
确为原非 CM 部分，不是任意补空间。具体地，Harrison 的
$\tau_3=S_3w_{27}S_3w_{27}$ 在 $g,c,d$ 上特征为 $\zeta$，
在 $a,b,h$ 上特征为 $\zeta^2$。代入 R1059 的实际函数，准确给
$$
\tau_3(x,z,w)=(x,\zeta^2z,\zeta^2w).
$$
故 (1060.3) 全部特征为一，六条 (1060.2) 的特征均非一。Harrison §4 的同一个非 CM 空间正是 $\tau_3$-固定空间。因此这些是实际非 CM 四基。$\tau_3$ 阶为三，$p>3$ 时其投影分母为单位；完整平滑模型的 canonical 基也为整基，没有一个未支付的格指数。

## 2. 四条准确 Cartier 公式

定义
$$
B_n=[T^n](1-T)^{2n+1}(1+T)^n.
\tag{1060.4}
$$
这个多项式次数为 $3n+1=p-1$，其反转等于自身的负号。因此
$$
[T^{2n+1}](1-T)^{2n+1}(1+T)^n=-B_n.
\tag{1060.5}
$$

例如
$$
v_1=\frac{dx}{zw^2}
=(z^{-2}w^{-1})^p
 (1-\kappa x^3)^{2n+1}(1+\kappa x^3)^n dx.
$$
后一个多项式次数为 $3p-3$，只含三的倍数次幂。
Cartier 的可能读数 $jp-1$ 中只有 $j=2$ 的指数符合。
乘上 $x$ 的 $v_3$ 则只有 $j=1$ 符合。交换 $z,w$ 等价于
$\kappa\mapsto-\kappa$。于是完整四式为
$$
\begin{aligned}
\mathscr C(v_1)&=(-\kappa^{2n+1}B_n)^{1/p}v_4,\\
\mathscr C(v_2)&=( \kappa^{2n+1}B_n)^{1/p}v_3,\\
\mathscr C(v_3)&=( \kappa^nB_n)^{1/p}v_2,\\
\mathscr C(v_4)&=(-\kappa^nB_n)^{1/p}v_1.
\end{aligned}
\tag{1060.6}
$$
由于 $s^p=-s$、$\kappa^p=-\kappa$ 且 $n$ 奇，这等价于
$$
\boxed{\begin{aligned}
\mathscr C(v_1)&=\kappa^{2n+1}B_n v_4,&
\mathscr C(v_2)&=-\kappa^{2n+1}B_n v_3,\\
\mathscr C(v_3)&=-\kappa^nB_n v_2,&
\mathscr C(v_4)&=\kappa^nB_n v_1.
\end{aligned}}
\tag{1060.7}
$$
所以此实际块可逆当且仅当 $B_n\ne0$。所有式子保持原 Cartier 半线性。

另一方面，$2n+1=p-n-1$，故在 $j\le n<p$ 时
$$
(-1)^j\binom{2n+1}{j}=\binom{n+j}{j}\quad\bmod p.
$$
由 Legendre 多项式的有限展开，准确得到
$$
\boxed{\quad
B_n=\sum_{j=0}^n\binom nj\binom{n+j}{j}=P_n(3)\quad\bmod p.
\quad}
\tag{1060.8}
$$

## 3. 原归一化新形式给准确 Frobenius 迹

令 $f=f_{54}^{(2)}$ 为 Harrison 第9页对应于
$$
E_{54}:\quad y^2+xy+y=x^3-x^2+x-1
\tag{1060.9}
$$
的原归一化新形式。其开头为 $q+q^2+q^4-3q^5+\cdots$，位于上述实际非 CM 四维空间。

R1059 的实际首项给
$$
x=q+O(q^7),\quad z=1-sq^3+O(q^6),\quad
w=1+sq^3+O(q^6),\quad g=q+O(q^7).
$$
$q,q^2,q^4,q^5$ 在 (1060.3) 上的四读数矩阵可逆，行列式只含二、三的单位。因此准确的微分身份是
$$
f\,dq/q=
\frac{1-1/s}{2}v_1+\frac{1+1/s}{2}v_2
+\frac{1-s}{2}v_3+\frac{1+s}{2}v_4.
\tag{1060.10}
$$
这是同一四维空间中的完整身份，由四个独立坐标确定，不是任意截断后猜测函数相等。

$p\nmid54$ 时 Hecke 关系模 $p$ 给
$\mathscr C(f\,dq/q)=a_p(E_{54})\,f\,dq/q$。
在 (1060.10) 中使用 (1060.7) 和系数的 $p$ 次根，再取首个 $q$ 系数，
$$
a_p(E_{54})=-s\kappa^nB_n.
$$
现在
$$
s\kappa^n=(-1)^{N+1}3^{3N+2}
=(-1)^{N+1}3^{(p-1)/2}=1.
$$
最后一步是 Euler 准则及 $(3/p)=(-1)^{N+1}$，对
$p=6N+5$ 的两个模十二分支分别成立。于是
$$
\boxed{\qquad B_n=-a_p(E_{54})\pmod p.\qquad}
\tag{1060.11}
$$
这保留了确切原形式及符号，不只是“某个同源 CM/非 CM 因子的单位倍”。

同一个 Euler 化简也使 R1059 的准确常数成为
$$
A_p=-S_n/3.
\tag{1060.12}
$$
它未将 $S_n$ 与 $B_n$ 等同。

## 4. 九阶有理挠点与到原因子的显式三次同源

考虑
$$
E_9:\quad y^2+xy+y=x^3-x^2-14x+29,\qquad P=(9,19).
\tag{1060.13}
$$
它由 Dwarshuis–Roelfszema–Top 的明确例子引入；这里只用实际方程，并直接核阶数：
$$
2P=(3,1),\qquad 3P=(1,3),\qquad
2(3P)=(1,-5)=-(3P).
$$
这些点均非无穷点，所以 $P$ 的阶准确为九。

还需把它接到 (1060.9)，不能只认同一个数据库标签。令
$Q=3P=(1,3)$。以 $\{O,Q,-Q\}$ 作核的三次商为
$$
E':\quad Y^2+XY+Y=X^3-X^2+106X-323.
\tag{1060.14}
$$
其准确坐标可以直接给出：
$$
X=x-\frac{24}{x-1}+\frac{64}{(x-1)^2},\qquad
Y=\frac{(2y+x+1)X'(x)-X-1}{2}.
\tag{1060.15}
$$
代入源方程后即满足 (1060.14)；这也来自把 $P+Q,P-Q$ 的加法横坐标完整相加。$X$ 的极点恰在 $O,Q,-Q$，各二阶，故这个固定原点的 morphism 为三次同源，核如上。等价的 Vélu 数据为
$g_Q^x=-16,g_Q^y=-8,v=-24,u=64,w=u+x_Qv=40$，
给目标 $a_4=-14-5v=106$、$a_6=29-(-3)v-7w=-323$。

在 (1060.14) 作准确变换
$$
X=9x_0-2,\qquad Y=27y_0+9x_0+14
$$
后，得到
$$
y_0^2+x_0y_0+y_0=x_0^3-x_0^2+x_0-1,
$$
正是原 (1060.9)。比如变换后原左边减右边准确为 $729$ 倍的这个新方程；没有遗失一个二次 twist。所有必要分母仅为二、三，在 $p>3$ 都是单位。

## 5. 原素数范围中的无条件单位输入

原 (1060.9) 判别式为 $-216$，$E_9$ 的判别式为 $-2^9 3^5$；两者在 $p>3$ 均良好。prime-to-$p$ 挠点的好约化保持九阶，故
$$
9\mid\#E_9(\mathbf F_p),\qquad
a_p(E_{54})=a_p(E_9)\equiv p+1\pmod9.
$$
若 $p\equiv2$ 或 $5\bmod9$，右侧分别为三或六，故这个整数迹非零。
Hasse 界 $|a_p|\le2\sqrt p<p$ 给
$$
\boxed{\quad
p=6N+5,\quad p\equiv2,5\bmod9
\quad\Longrightarrow\quad
B_n=P_n(3)=-a_p(E_{54})\ne0\quad\text{于 }\mathbf F_p.
\quad}
\tag{1060.16}
$$
由 (1060.7)，原非 CM 四维 Cartier 块可逆。原六 CM 方向来自
$j=0$ 椭圆曲线，在这些惰性素数 Cartier 为零。因此此范围中原
$X_0(108)$ 的 Cartier 核准确为上述六 CM 方向。

## 6. 不能省去的下一条关系

R1059 的实际 Raynaud 配对读数是 $S_n$，本篇的非 CM Cartier 读数是 $B_n$。本篇**没有**证明 $S_n=0$ 会迫 $B_n=0$，也没有证明二者的单位比例。Aut 作用保持 CM/非 CM，两类配对通道也不能自动混为一类。

新的、已支付的输入是完整实际矩阵、准确迹与在原模九范围内的普通性。下一步须在原双三次模型或明确有限和中证明足以连接指定 $S_n$ 的关系，或换另一实际输入；不以此结果关闭原端点/同标签筛选、bare 或 $DQ(1-Q)\lambda$ 最低值。O0 仍另行开放。

## 来源及核对

- [R1059](R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：同一个 actual 模型、CM 六方向、原 $q$ 与微分尺度。
- Michael Harrison, *A new automorphism of X0(108)*，[作者 PDF](https://arxiv.org/pdf/1108.5595)，第9页实际 $E_{54}$ 与新形式，Definition 4.2、Lemma 4.3 及 $\tau_3$-固定非 CM 空间。
- A. Dwarshuis, M. Roelfszema, J. Top, *Mazur's rational torsion result for pointless genus one curves: examples*, Research in Number Theory 7, 7 (2021)，[原文](https://link.springer.com/article/10.1007/s40993-020-00231-z)，九挠点例子（式 (1060.13)）；本篇另给阶数及原三次同源的逐项核准。

o1_theta 推导实际四基、完整 Cartier 及准确迹；root 给显式九点加法和三次商，双方独立核坐标变换。root 实读两份 primary 原文，核全次数、Frobenius 半线性、四个独立 q 读数及 Euler 符号。全文纸面推导，无数学程序执行，无新数值窗口；只登记已证明的单位输入。
