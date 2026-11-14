# R424 — 原二挠和的精确 Bezout 核与完整中央分离

日期：2026-11-14。**状态：已证明。** R423 的同一个原来源
$H=-\frac12\sum_{E[2]}S_t\otimes L_t$ 有一个完整的低 degree 因式：
$$
H(y,v)=G_{16}(y)J_{12}(v)\Theta(2v)
       \sigma(y-v)\sigma(y+v)\,\mathcal R(y,v),
\qquad\mathcal R\in\mathcal S_{16}\boxtimes\mathcal S_{16}.
$$
实际对称核 $\mathcal R$ 是两条明确 degree18 来源的 Bezout 商，
其九维偶 theta 系数矩阵在所有当前素数整且非退化。
乘回对角因子后，$H$ 更准确成为两条张量之差，其中一条第一轴正是
原 $S$，另一条被 principal 测试的真实 $\mu_6$ 对称性消去。
因此原中央零合法传播到 $H$ 上**任意完整第二输出测试**。
这不对任意原 sigma 隐藏输入域免费赋零；主目标仍未完成。

## 1. 固定原来源及最小的实际因子

保持 R398、R416、R423 的同一 $E_b:y^2=x^3+b$、$b=17$、原微分、
sigma、普通周期和 ray。写 $X=x^3$，
$$
P_2(X)=X^2-4bX/7+16b^2/7,\qquad R_2(X)=X^2+20bX-8b^2,
$$
$$
Q_4(X)=(X+4b)(X^3-96bX^2+48b^2X+64b^3).
$$
实际来源为
$$
S=\sigma^{34}x^2(X+b)(X-8b)P_2(X),\qquad
L=\sigma^{38}xR_2(X)Q_4(X),\qquad T=SL.
\tag{1}
$$
原 $H$ 是 untwisted degree $34\boxtimes38$ 的整来源，分别偶，并有
$$
H(y,0)=-2S(y)/3,\quad H(0,v)=H(z,z)=H(z,-z)=0.
\tag{2}
$$
这些全来源身份及完整 core 已由 R423 支付。

定义真正原因子
$$
\boxed{G_{16}(y)=\frac{\sigma(2y)\sigma(2\delta y)}{4\delta}
=\sigma(y)^{16}x(y)(x(y)^3+b)(x(y)^3-8b),}
\tag{3}
$$
$$
\boxed{J_{12}(v)=\frac{\sigma(4v)}{2\sigma(2v)}
=\sigma(v)^{12}R_2(x(v)^3),\qquad \Theta=x\sigma^2.}
\tag{4}
$$
$G_{16}=y^2+O(y^8)$；$J_{12}(0)=\Theta(0)=1$。
这些式子由原倍点式和 $\sigma(\delta y)=\delta\sigma(y)\Theta(y)$
得到，所有常数都已固定。

第一轴所有二挠项都含 $G_{16}$：它是
$\sigma(z)\sigma(\delta z)/(4\delta)$ 的 $[2]$ 拉回，底源两个
半特征因 $\delta\equiv1\pmod2$ 相消，故
$T_t^{(16)}G_{16}=G_{16}$ 对全部 $t\in E[2]$。
第二轴 $J_{12}$ 的零除子恰为 $E[4]\setminus E[2]$，在二挠平移下
保持。准确相位是
$$
T_t^{(12)}J_{12}=\epsilon_tJ_{12},\qquad
\epsilon_0=1,\quad\epsilon_t=-1\ (t\ne0).
\tag{5}
$$
直接将 $t=\ell/2$ 代入 (4)，分子的 $2\ell$ 半特征为一，分母
的 $\ell$ 半特征为 $-1$；其余指数与原 lift 相消，证明 (5)。
不能将这个 projective 二挠符号删掉。

因此 $H/(G_{16}(y)J_{12}(v))$ 是完整全纯来源，degree 为
$18\boxtimes26$。由 (2) 在两条对角的非空开集上消失，再延拓到
全对角，可整除真正的 $\sigma(y-v)\sigma(y+v)$，先得到
degree $16\boxtimes24$ 的商。下文完整多项式恒等式进一步给
$\Theta(2v)$ 因子，最终下降到 $16\boxtimes16$。
这些全在原输出上完成，不用双覆盖，也不丢四挠平坦 twist。

## 2. 完整对称核的明确系数

写
$$
v_0(x)=(1,x^3,x^6)^{\mathsf t},\quad
v_1(x)=(x,x^4,x^7)^{\mathsf t},\quad
v_2(x)=(x^2,x^5,x^8)^{\mathsf t}.
$$
定义两个实际矩阵
$$
M_0(b)=\begin{pmatrix}
512b^5&-128b^4&224b^3\\
-128b^4&-832b^3&1024b^2\\
224b^3&1024b^2&206b
\end{pmatrix},
$$
$$
M_{12}(b)=\begin{pmatrix}
-2432b^4&-256b^3&16b^2\\
-256b^3&1144b^2&-4b\\
16b^2&-4b&7
\end{pmatrix},
$$
$$
\mathcal B_b(x,z)=v_0(x)^{\mathsf t}M_0(b)v_0(z)
 +v_1(x)^{\mathsf t}M_{12}(b)v_2(z)
 +v_2(x)^{\mathsf t}M_{12}(b)^{\mathsf t}v_1(z).
\tag{6}
$$
这准确给出全部系数；它对称，两个次数都不超过八。
置
$$
\boxed{\mathcal R(y,v)=-\frac2{21}\sigma(y)^{16}\sigma(v)^{16}
          \mathcal B_b(x(y),x(v)).}
\tag{7}
$$
它是全纯、分别偶且对称的实际 $\mathcal S_{16}\boxtimes\mathcal S_{16}$
来源。完整因式为
$$
\boxed{H=G_{16}(y)J_{12}(v)\Theta(2v)
              \sigma(y-v)\sigma(y+v)\mathcal R(y,v).}
\tag{8}
$$

### 2.1 从全部原半周期项证明 (8)

在 $b=1$ 上，令 $s(x),l(z)$ 为 (1) 去掉 sigma 的多项式。
对 $e=x(t)=-1$ 的二挠点，完整常数
$c_t^{72}=(3e^2)^{-18}=3^{-18}$ 给出原项
$$
3^{-18}\sigma(y)^{34}\sigma(v)^{38}
   s_h(x)l_h(z),
$$
$$
s_h(x)=(x+1)^{17}s((2-x)/(x+1)),\quad
l_h(z)=(z+1)^{19}l((2-z)/(z+1)).
\tag{9}
$$
两者是完整多项式。其余两条非零半周期是共同 CM 旋转；总 degree72
没有额外相位。因此三根和准确把 $s_h(x)l_h(z)$ 中 $x^iz^j$ 的
$i+j\not\equiv0\pmod3$ 项杀掉，将其余项乘三。
记这个不乘三的投影为 $\Pi_3$，则 (8) 等价于明确有限多项式身份
$$
\boxed{
-\frac12\left[s(x)l(z)+3^{-17}\Pi_3(s_h(x)l_h(z))\right]
=-\frac2{21}\,x(x^3+1)(x^3-8)
 R_2(z^3)(z-x)z(z^3-8)\mathcal B_1(x,z).}
\tag{10}
$$
左边是包括原点在内的四个原 half-period 项，右边是显示的全部因子。
按 (9) 作有限二项展开直接得到 (6)、(10)；附带脚本逐系数验证整条
双变量身份，不使用插值、截断或采样。
最后使用已付
$$
\sigma(y-v)\sigma(y+v)
=\sigma(y)^2\sigma(v)^2(x(v)-x(y)),\qquad
\Theta(2v)=\sigma(v)^8x(v)(x(v)^3-8b)
$$
即还原 (8) 的所有 theta frame 与整体常数。

返回任意 $b\ne0$ 时，实际同源缩放使一个 $x^iz^j$ 项的系数乘
$b^{5-(i+j)/3}$。所有出现的 $i+j$ 都被三整除，所得恰为 (6)；
这证明原 $b=17$ 的全函数身份，不引入一个未定六次根常数。

## 3. 这是具体的两来源 Bezout 商

定义
$$
f_b(x)=xP_2(x^3),\qquad
g_b(x)=x^9-30bx^6-144b^2x^3-32b^3,
$$
$$
F_{18}(z)=\sigma(z)^{18}f_b(x(z)),\qquad
G_{18}(z)=\sigma(z)^{18}g_b(x(z)).
\tag{11}
$$
$F_{18}=z^4+O(z^{10})$、$G_{18}(0)=1$。
全部矩阵系数进一步给出准确的 Bezout 恒等式
$$
\boxed{\mathcal B_b(x,z)
=7\frac{f_b(x)g_b(z)-g_b(x)f_b(z)}{z-x}.}
\tag{12}
$$
分子沿 $z=x$ 为零，(12) 是多项式，不需要选择分支。
逐项比较 (6) 即核定全式；证书也验证这个完整有理恒等式。
所以
$$
\boxed{\sigma(y-v)\sigma(y+v)\mathcal R(y,v)
=-\frac23\{F_{18}(y)G_{18}(v)-G_{18}(y)F_{18}(v)\}.}
\tag{13}
$$
原 $S$ 的一个准确因式是 $G_{16}F_{18}=S$。
再置
$$
C_{34}=G_{16}G_{18},\qquad
B_{38}=J_{12}\Theta(2\cdot)G_{18},\qquad
D_{38}=J_{12}\Theta(2\cdot)F_{18}.
\tag{14}
$$
于是同一原 $H$ 的整个两输出来源恰为
$$
\boxed{H=-\frac23\{S\otimes B_{38}-C_{34}\otimes D_{38}\}.}
\tag{15}
$$
$B_{38}(0)=1$，$C_{34}$ 从 $z^2$ 起，$D_{38}$ 从 $z^4$ 起。
它们并未被称为新的 rank-two 曲线；定义 (11)、(14) 给了全部实际来源。

## 4. 整性、实际完美核及首边界

(7) 本身已证明整性：原 theta 基整，矩阵系数只除 $21$，
当前 $p>19$ 且 $b=17$ 为单位。
也可从因子直接读：$G_{16}$ 的 Amice 变换为正式群第一坐标的平方
乘整单位，$J_{12}$ 和 $\Theta(2\cdot)$ 的 Amice 常数均为一。
对两个对角因子使用 R422 的正式群差／和整除，保持整有界性。
这没有除 log 级数中的阶乘，也没有只得到小圆盘解析商。

在九维偶基 $\sigma^{16}x^i$、$0\le i\le8$ 中，(6) 的矩阵按
余数 $0,1,2\pmod3$ 分成 $M_0$ 与两份配对 $M_{12}$。
直接行列式计算给
$$
\det M_0=-2^{15}3^9b^9,\qquad
\det M_{12}=-2^{10}3^9b^6,
$$
$$
\boxed{\det\mathcal B_b=2^{35}3^{27}b^{21}.}
\tag{16}
$$
整体 $-2/21$ 也为单位。因此 (7) 在这个真实九维整格上给对称
完美配对。这里是原来源的完整矩阵，不是另配一个非退化环境。
该有限非退化不单独赋值给任何中央泛函。

最高 $z^8$ 系数给实际两个边界
$$
\boxed{\mathcal R(y,0)=\mathcal R(0,y)
=-\frac2{21}\Theta(y)\sigma(\gamma_7y)\sigma(\bar\gamma_7y).}
\tag{17}
$$
它们从 $-2y^2/3$ 起，所以原 Amice 的 $[U^2V^0]$ 为
$-2\Omega_p^2/3$，是单位。商仍 primitive，且边界是具体原来源。
例如
$$
\boxed{[y^2]H(y,v)=\frac23\sigma(v)^{38}x(v)^2
 (x(v)^3-8b)R_2(x(v)^3)P_2(x(v)^3).}
\tag{18}
$$
这也由 (8)、(17) 直接得到，是实际第一个偶混合矩列，不是其
inverse-square 单位矩已经非零的断言。

## 5. 完整 principal 中央确实对任意第二输出测试分离

原 CM 单位的绝对 sigma 式给 (15) 的四条来源的权：
$$
\begin{array}{c|cccc}
\text{来源}&S&B_{38}&C_{34}&D_{38}\\ \hline
\mu_6\text{ 权}&0&0&2&4.
\end{array}
$$
所以原 principal 测试沿第一输出准确杀掉 $C_{34}$，不影响任意
第二输出的连续测试 $\varphi$。完整测度式是
$$
\boxed{\int K_{0,u}(Y)\varphi(X)\,d\nu_H
=-\frac23J_S(u)\int\varphi\,d\nu_{B_{38}},}
\tag{19}
$$
其中 $K_{0,u}$ 包括原 $Y$ 单位指示函数。
在主中央求导，准确得到
$$
\boxed{\int\mathbf1_{Y\in\mathbf Z_p^\times}
 (p-1)\log_p\langle Y\rangle\,\varphi(X)\,d\nu_H
=-\frac23J'_S(0)\int\varphi\,d\nu_{B_{38}}.}
\tag{20}
$$
这是整个第二输出测度的返回，含任意开闭输出域；没有将 (19)
擅自扩大到依赖隐藏输入或同时依赖 $Y$ 的新域。

R423 已付 $K_YH=H$、$K_XH=-H$，统一外部 core 系数为
$\lambda=-\bar\pi_0^{-1}$。在 (15) 比较两个不同 CM 权的非零张量，
再用 $K_{34}S=S$，得到
$$
\boxed{K_{34}C_{34}=C_{34},\qquad
K_{38}B_{38}=-B_{38},\quad K_{38}D_{38}=-D_{38}.}
\tag{21}
$$
所以它们的全测度 core 分别为 $\lambda,-\lambda,-\lambda$，
原共同尺度仍是 $\kappa=p/\bar\pi_0^2$。
尤其
$$
\nu_{B_{38}}(p^n\mathbf Z_p)=(-\lambda)^n,\qquad
\nu_{B_{38}}(p^n\mathbf Z_p^\times)=(-\lambda)^n(1+\lambda).
\tag{22}
$$
$1+\lambda$ 是原 ray 上已付单位。于是双方输出为单位的整条
principal 函数为 $-2J_S(u)J_{B_{38}}(v)/3$，其第一中央行在 $v=0$
与原 $J'_S$ 相差准确单位 $-2(1+\lambda)/3$。
式 (20) 比仅对这些深度域的传播更强；所有尺度和质量均已保留。

## 6. 同一原 sigma／norm-three 输入的完整接口

(8) 也给直接的原测度卷积。令 $\nu_{\mathcal R}$ 的输出为 $(r,s)$，
令 $j$ 取 $\nu_{J_{12}}$、$t$ 取原 $\nu_\Theta$，再取四个独立原
sigma 输入 $a,b,c,d$。则准确有
$$
\boxed{\nu_H=\frac1{4\delta}(Y,X)_*
(\nu_{\mathcal R}\otimes\nu_{J_{12}}\otimes\nu_\Theta
                         \otimes\nu_\sigma^{\otimes4}),}
$$
$$
\boxed{Y=r+2a+2\delta b+c+d,\qquad
X=s+j+2t-c+d.}
\tag{23}
$$
这里是原输出，没有双 $[2]$ 或未写明的 $1/2$。
完整 $X$ 与 $a,b$ 无关，$W=Y+X$ 与 $c$ 无关，$V=X-Y$ 与 $d$
无关，所以三个零边际分别由对应 sigma 的零质量严格解释。
这些消去不能直接用于把额外混合条件后的积分设零。

在第一完整边际上使用 (17)，(23) 准确成为把原
$\sigma(\delta y)$ 以
$\sigma(\delta y)=\delta\sigma(y)\Theta(y)$ 展开的原 $S$，整体
标量为 $-2/3$。没有换掉 R339 的原目标。
另一方面，原第二源还有实际 norm-three 因式
$$
\boxed{\frac L{J_{12}}=
\frac{\sigma(3\delta v)}{3\delta\sigma(v)}
=\Theta(v)\Theta(\delta v)\Theta(3v).}
\tag{24}
$$
这是三次迭代同一个原 sigma 恒等式，因 $\delta^3=-3\delta$、
$\Theta$ 偶，所有相位相消。

(17) 只确定 $\nu_{\mathcal R}$ 的边际；不能把其整个联合免费替成
这个边际的独立 sigma／Theta 输入。要将 (20) 用到 R339 指定的
独立深度域，仍须运输那组实际隐藏条件到 (23) 或 (15)，包括各个
二次权、全部单位相消与完整补域。本篇未预支这一剩余步骤。

## 7. 证书与依赖

`scripts/check-original-half-period-small-symmetric-kernel.py` 用精确
有理多项式直接验证整个 (10)、(12)、对称性、三个行列式、(17)、
(18)。同名 JSON 给出全矩阵与全部一般 $b$ 系数。
它没有采样点、浮点近似或目标素数扫描。

- [R398：原多项式来源及物理规范](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。
- [R416：完整二挠归一与实际来源和](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R423：原 H、完整四态与四条真实 core](R423-original-four-state-signed-group-and-untwisted-half-period-source.md)。
- [R422：正式群差／和的整除](R422-original-two-diagonal-factor-integral-quotient-and-four-input-return.md)。
- [R339：原 norm-three 独立深度域](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
