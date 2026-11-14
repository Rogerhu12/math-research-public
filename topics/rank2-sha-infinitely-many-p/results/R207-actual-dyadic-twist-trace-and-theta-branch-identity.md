# R207. 原 B 行的逆 Frobenius 权、固定极点与准确全纤维迹

日期：2026-11-12。**状态：下述恒等式及单位范围已证明；没有据此证明原两条中央行非零。**

本结果一直使用 [R197](R197-actual-two-weight-determinant-and-common-theta-gauge.md)
的原 $A=A_2,B$、共同 $E_0$ 尺度及微分，不更换实际有限角色。
全部迹都是未除以 $p$ 的函数域迹。

## 1. 原 P/Q 的准确二挠奇偶

在
$$
E_0:y^2=x^3-x,\qquad \omega_0=\frac{dx}{2y},\qquad
s=x^{-2}=u^4,\qquad \vartheta(z)=\frac{\sigma(z)}{u(z)}
$$
上，原截面为
$$
A=\vartheta^{68}P(s),\qquad B=\vartheta^{68}Q(s).
$$
沿用 R197 的原多项式，记
$$
\begin{aligned}
J(s)&=\frac{s(1-2s+5s^2)(5-2s+s^2)}5,\\
H_1(s)&=1+4s+70s^2+4s^3+s^4,\\
H_2(s)&=1+20s-26s^2+20s^3+s^4,\\
Q_8(s)&=1+364s^2-1088s^3+1190s^4-1088s^5+364s^6+s^8.
\end{aligned}
$$
则
$$
P=J(1-s)^2(1+s)H_1H_2,\qquad
Q=J(1-s)(1+s)^2Q_8.                                      \tag{1}
$$
准确倍乘式 $\vartheta(2z)=\vartheta(z)^4(1+s(z))$ 给共同参考
$$
\Theta(z)=\vartheta(2z)^{17},\qquad
A=\Theta\,a,\quad B=\Theta\,b,\qquad
a=\frac{P(s)}{(1+s)^{17}},\quad b=\frac{Q(s)}{(1+s)^{17}}.
\tag{2}
$$
这里 $\Theta$ 是原正次数 theta 截面，不是有理函数。

令 $T_0=(0,0)\in E_0[2]$。平移公式为
$$
(x,y)\longmapsto(-1/x,y/x^2),\qquad s\longmapsto1/s.
$$
由 (1) 逐项得到
$$
s^{17}P(1/s)=P(s),\qquad s^{17}Q(1/s)=-Q(s).
\tag{3}
$$
所以 $a$ 对 $T_0$ 不变，$b$ 变号。特别地，对任何下降到
$E_0/\langle T_0\rangle$ 的有理参考，未加权的 $b$ 完整迹恒为零；
这会同时消去原 $O$ 分支及其 $T_0$ 伙伴，不能当成中央非零结论。

## 2. 固定商与两个实际低次数多项式

取 R202 已付的严格二同源
$$
E_+:\ Y^2=X^3+4X,\qquad
X=x-1/x,\quad Y=y(1+1/x^2),\qquad
\omega_+=\frac{dX}{2Y},\quad \phi^*\omega_+=\omega_0.
\tag{4}
$$
为避免与素数混用，记
$$
q_0=\frac1{X^2+4}=\frac{s}{(1+s)^2},\qquad
\rho=\frac{1-s}{1+s},\qquad
\rho^2=1-4q_0.
\tag{5}
$$
$\rho$ 是原 $E_0$ 上对 $T_0$ 变号的有理函数。
将 (1) 除以相应的 $(1+s)$ 幂，准确得到
$$
\begin{aligned}
a={}&q_0\left(1-\frac{32}5q_0+\frac{64}5q_0^2\right)
 (1-4q_0)(1+64q_0^2)(1+16q_0-64q_0^2),\\
b={}&\rho\,b_0(q_0),\\
b_0(q)={}&q\left(1-\frac{32}5q+\frac{64}5q^2\right)
 (1-8q+384q^2-2560q^3+4096q^4).
\end{aligned}                                                   \tag{6}
$$
展开第二个多项式：
$$
b_0(q)=q-\frac{72}5q^2+448q^3-5120q^4
       +\frac{126976}5q^5-\frac{294912}5q^6+\frac{262144}5q^7.
\tag{7}
$$
因此这些始终是原两行的实际因子；没有用任意同次数有理函数替代。

## 3. 保原两权 jet 的逆 Frobenius 权

以下令 $p=4r-1\ge19$ 为素数，$d=(p-1)/2=2r-1$，
全部有理函数在完美特征 $p$ 常数域上取约化。定义
$$
\widetilde b_p=b\,\rho^{-p}
 =b_0(q_0)(1-4q_0)^{-d}
 =X^{1-p}(X^2+4)^d b_0\!\left(\frac1{X^2+4}\right).
\tag{8}
$$
两个变号因子相乘，所以它准确下降到 $E_+$。

在原 $O$ 的严格参数中，$s=z^4+O(z^8)$、
$\rho=1+O(z^4)$、$b=O(z^4)$。特征 $p$ 中
$$
\rho^{-p}=1+O(z^{4p}),\qquad
\widetilde b_p-b=O(z^{4p+4}).
\tag{9}
$$
因此加上任何在 $O$ 正则的同一参考后，$p+1$、$2p+2$ 两个
原 jet 完全保留。这里 (9) 只给有限 jet 比较，不把 $\rho^{-p}$
当成保原全部 Mellin 变换的操作。

令
$$
T'=(0,0)\in E_+,\qquad P_\pm=(\pm2i,0).
$$
$q_0$ 在 $P_\pm$ 各有二阶极点；因 $\deg b_0=7$，
(8) 在两点的阶至少为 $p-15>0$。
在 $T'$，$X$ 的阶为二，$1-4q_0$ 的阶为四，而
$$
b_0(1/4)=-1/20.
$$
所以 $\widetilde b_p$ 只在 $T'$ 有极点，极阶准确为 $2p-2$。
它在 $O$ 从四阶起。这个构造将固定参考零点处的极点消掉，
代价为一个明确的 $O(p)$ 极点，未使用逐个移动分支的插值投影。

## 4. 原 degree-p 参数的显式多项式

使用 [R202](R202-rational-elliptic-parameter-and-unit-cartier-obstruction.md)
的原下降参数 $Z=\overline Z_p$，而不是其 $2p$ 次修复 $Z_p^\dagger$。
它满足
$$
dZ=\omega_+,\qquad Z=z+O(z^{3p})\ \text{于 }O,
\qquad (Z)_\infty=pT'.
\tag{10}
$$
记
$$
\kappa_p=\frac{\binom{2r-2}{r-1}}{4^{r-1}},\qquad
\mathfrak h_p=h_p(1),\qquad \mathfrak h_p\kappa_p=-1
\quad\text{于 }\mathbf F_p.
$$
存在唯一次数 $r-1$ 的多项式 $F_p(T)$，使
$$
\boxed{\quad
Z=Y X^{-2r}F_p(X^2),\qquad
F_p(T)+2(T+4)F_p'(T)=\frac12T^{r-1}.
\quad}                                                        \tag{11}
$$
其首项系数为 $-1$，并且
$$
F_p(0)=-\mathfrak h_p/2\ne0,\qquad
F_p(T)\equiv F_p(0)(1+T/4)^{-1/2}\pmod{T^r}.
\tag{12}
$$

证明如下。对 (11) 的右边沿 $\omega_+$ 微分，利用
$D X=2Y$、$D Y=3X^2+4$ 及 $4r=p+1$，得到
$$
D\{Y X^{-2r}F_p(X^2)\}
 =2X^{2-2r}\{F_p+2(T+4)F_p'\}=1.
$$
方程的各系数递推中，$2j+1$ 及 $8(j+1)$ 在所用范围均为单位；
最高项为 $F_{p,r-1}=1/(4r-2)=-1$。
所得函数在 $O$ 从 $z$ 起，仅在 $T'$ 有至多 $p$ 阶极点。
它与 R202 的 $Z$ 之差微分为零，故是一个 $p$ 次幂；
其 $p$ 次根只能在 $T'$ 有至多一阶极点，在椭圆曲线上必为常数。
两者在 $O$ 都为零，因而相等。
在 $T'$ 用 $Y$ 比较极部 $-2\mathfrak h_pY^{-p}$
与 $4F_p(0)Y^{-p}$，得到 (12) 的常数。
低次递推
$$
(2j+1)F_{p,j}+8(j+1)F_{p,j+1}=0\qquad(0\le j<r-1)
$$
即给 (12) 的截断二项式。

作为原函数域次数的直接核对，
$$
Z^2X^p=(X^2+4)F_p(X^2)^2,\qquad
Y=\frac{ZX^{2r}}{F_p(X^2)}.                                  \tag{13}
$$
因此 $X$ 生成 $k(E_+)/k(Z)$，而这个可分扩张的次数正是 $p$。

## 5. 实际迹的准确计算

先给一个在同一原覆盖上的有限公式。
对任意 $B_0(q)\in k[q]$，$\deg B_0\le d$，置
$$
f_{B_0}=B_0(q_0)(1-4q_0)^{-d}.
$$
它只可能在 $T'$ 有极点，阶至多 $2p-2$。
因 $Z$ 在此全分歧、阶为 $p$，其函数域迹在 $Z=\infty$
至多有一阶极点，故为次数至多一的多项式。
自同构
$$
(X,Y)\longmapsto(-X,iY)
$$
保持 $f_{B_0}$，将 $Z$ 送到 $iZ$；所以该多项式必为常数。

迹与留数的相容性给
$$
\begin{aligned}
\operatorname{Tr}(f_{B_0})
 &=-\operatorname{Res}_{T'} f_{B_0}\frac{dZ}{Z}\\
 &=-[T^{r-1}]
 \frac{(T+4)^{2r-2}}{F_p(T)}
 B_0\!\left(\frac1{T+4}\right).
\end{aligned}                                                   \tag{14}
$$
第二步中的因子没有省略：
$$
f_{B_0}\frac{dZ}{Z}
 =\frac12X^{1-2r}
  \frac{(T+4)^{2r-2}}{F_p(T)}
 B_0\!\left(\frac1{T+4}\right)dX,
$$
而 $X$ 在 $T'$ 的分歧指数是二，恰消掉前面的 $1/2$。
式 (14) 的第一步也可从各局部嵌入求和直接读出；没有除以
扩张次数 $p$。

写 $B_0(q)=\sum b_kq^k$。用 (12)，其第 $k$ 项在 (14) 的贡献为
$$
-F_p(0)^{-1}4^{r-1-k}
 \binom{2r-\frac32-k}{r-1}\,b_k.
$$
由于 $r\equiv1/4\pmod p$，
$$
\binom{2r-\frac32-k}{r-1}
 =(-1)^{r-1}\binom{r+k-1}{k}\quad\text{于 }k.
$$
此外
$$
(-4)^r=2,\qquad
-F_p(0)^{-1}(-4)^{r-1}
 =-\mathfrak h_p^{-1}=\kappa_p.
$$
于是得到完整的原覆盖迹公式
$$
\boxed{\quad
\operatorname{Tr}_{k(E_+)/k(Z)}
 \bigl(B_0(q_0)(1-4q_0)^{-d}\bigr)
 =\kappa_p\sum_k b_k\,\frac{(1/4)_k}{4^k k!}.
\quad}                                                        \tag{15}
$$
这里只用 $k\le d<p$；所有分母均为单位。

对原多项式 (7)，有限和准确为
$$
\begin{aligned}
\sum_{k=1}^7 b_k\frac{(1/4)_k}{4^k k!}
 &=
 \frac1{16}-\frac9{64}+\frac{105}{128}-\frac{975}{512}
 +\frac{20553}{10240}-\frac{41769}{40960}+\frac{3315}{16384}\\
 &=\frac{2261}{81920}
 =\frac{7\cdot17\cdot19}{5\cdot2^{14}}.
\end{aligned}                                                   \tag{16}
$$
所以
$$
\boxed{\quad
\operatorname{Tr}_{k(E_+)/k(Z)}(\widetilde b_p)
 =\kappa_p\,\frac{2261}{81920}.
\quad}                                                        \tag{17}
$$
特别地，对所有 $p>19$ 的目标惰性素数，这个准确全纤维迹是单位。
$p=19$ 时右边为零；不能用此前个别小素数的退化推断一般行列式恒等式。

## 6. 同一常数的固定有理微分解释

这不是另换一个参考得到的数。
在原 $E_0$ 上置 $v=-y/x$，则
$$
v^2=X,\qquad q_0=\frac1{v^4+4},\qquad
b\,\omega_0
 =-\frac{v^2}{v^4+4}\,
     b_0\!\left(\frac1{v^4+4}\right)dv.
\tag{18}
$$
利用恒等式
$$
d\left(\frac{v^3}{(v^4+4)^k}\right)
 =v^2\left\{\frac{3-4k}{(v^4+4)^k}
            +\frac{16k}{(v^4+4)^{k+1}}\right\}dv
$$
逐项作有理积分约化，得到
$$
b\,\omega_0\equiv
 -\frac{2261}{81920}\frac{v^2\,dv}{v^4+4}
 \pmod{d\,\mathbf Q(v)}.
\tag{19}
$$
因为 $\rho\,\omega_0=-v^2\,dv/(v^4+4)$，这也可写成
$b\,\omega_0\equiv(2261/81920)\rho\,\omega_0$。
每个 $a^4=-4$ 处的留数为 $-2261/(327680a)$。
因此 (16) 是原有理微分的准确固定留数常数，
不是由数值样本拟合出的比例。

(19) 并不允许在 $B=\Theta b$ 中丢掉 $\Theta$：
对有理原函数 $g$，
$\Theta\,dg=d(\Theta g)-g\,d\Theta$，实际连接项仍须保留。

## 7. 保留有限 theta jet 后的准确分支公式

令 $w=z^4$，沿用 R197 的 $\widehat K$ 和唯一坏系数 $k_r$。
共同整参考的局部形式是
$$
\widehat\Theta_p(z)
 =e^{-68k_rz^{p+1}}\Theta(z)
 =e^{68\widehat K(w)}(1+s(w))^{17}
 \pmod{w^{2r}},
\tag{20}
$$
所需系数在 $\mathbf Z_p$ 中。
取 $U_p(Z)\in\mathbf F_p[Z^4]$ 为 (20) 到次数 $2p-2$
的 Taylor 截断。R202 的 $Z=z+O(z^{3p})$ 与 (9) 给
$$
\overline{\widehat B_{jr}}
 =\operatorname{Res}_{O}
   \frac{U_p(Z)\,\widetilde b_p\,\omega_+}{Z^{j(p+1)+1}},
 \qquad j=1,2.
\tag{21}
$$
这恰是 R197 原 $B$ 行的两个系数，仍保原共同指数规范。

将 (17) 乘以 $U_p(Z)$，真正得到的是
$$
\sum_{Q:\,Z(Q)=0}
 \operatorname{Res}_{Q}
 \frac{U_p(Z)\widetilde b_p\,\omega_+}{Z^{j(p+1)+1}}
 =
 \kappa_p\frac{2261}{81920}\,[Z^{j(p+1)}]U_p(Z).
\tag{22}
$$
零纤维有 $p$ 个简单点，包括 $O,P_+,P_-$。
其余 $p-3$ 个点在 $\mu_4$ 下组成 $(p-3)/4$ 个四元轨道。
在两个中央权上，上述微分在 $\mu_4$ 下不变，因此同轨道的
留数相等，而不是相反；$P_+,P_-$ 两个留数也相等。
若 $\mathcal R$ 是其余四元轨道的代表集，准确地
$$
\overline{\widehat B_{jr}}
 =
 \kappa_p\frac{2261}{81920}[Z^{j(p+1)}]U_p
 -2\,\operatorname{Res}_{P_+}(\cdots)
 -4\sum_{Q\in\mathcal R}\operatorname{Res}_{Q}(\cdots).
\tag{23}
$$
特别地，真实 $\mu_4$ 对称本身并不消掉移动分支。

式 (20) 只指定原点有限 jet。$U_p(Z)$ 在 $P_\pm$ 的值为一，
而原 $\Theta$ 在那里有零点；它不是该 theta 线丛的全局平凡化。
(22) 因而不能把完整迹单位变成 (21) 的单分支单位。
选择更高次的 $U_p$ 可以改变 (22) 的右边，同时相应改变其余
分支项，原点所需系数仍不变。

## 8. 已付内容与剩余比较

已付的是原 $b$ 的低次数表达、保两权 jet 的逆 Frobenius 权、
一个固定点的准确 $2p-2$ 极点、无归一化除 $p$ 的实际覆盖迹，
以及保原有限 theta jet 的完整分支等式。

剩余的原目标是：
在共同 theta 参考及原 $A/B$ 两行上，控制 (23) 的其余分支，
或与只在固定点有极点的原 theta–Faber 留数作真正比较。
(17) 的单位不等于 R197 的双行行列式单位；
第一行已被 $p$ 整除时，仍必须支付先除第一行再读下一位的实际精度。
本文没有证明无穷多个素数的 Tate–Shafarevich 群有限。

依赖：原 $P,Q$ 及共同规范见 R197；
原 $Z$、严格二同源、$\mathfrak h_p\kappa_p=-1$ 和零纤维性质见 R202。
本结果的多项式 (6)–(7)、方程 (11)、迹 (14)–(17) 与分支式
(21)–(23) 均在这些原对象上逐式计算，不调用额外的跨素数非消失定理。

