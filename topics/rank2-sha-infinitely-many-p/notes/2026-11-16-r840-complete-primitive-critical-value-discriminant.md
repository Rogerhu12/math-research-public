# R840 补充 — 同一原 Euler 原函数族的判别式平方行列式

日期：2026-11-16。**状态：原函数的完整相对临界值映射、准确常数和判别式平方退化除子已证明；原三长前缀的受限像及指定 forcing 仍未判定。**

本注继续 [同格联合交](2026-11-16-r840-full-primitive-and-ramification-ideal-intersection.md)。它不重证“Euler 原函数只有一个可由零 charge 修复的方向”，而给该完整相对族在底参数 $t$ 上的准确行列式。下面的退化阶是 **$t$ 纤维的退化阶**，不是原物理矩阵的 $p$-Smith 指数。

## 1. 保原来源的相对多项式映射

先在原有限 $Y$ 坐标中工作。设 $A$ 是交换环，$1,\ldots,3b$ 可逆，$b\ge1$，且
$$
F(Y)=Y^b+f_{b-1}Y^{b-1}+\cdots+f_0\in A[Y]
\tag{1}
$$
首一。定义两个真正有限自由模
$$
Q_b=A[Y]_{\le b-2},\qquad
V_b=A[Y]/(F)\big/A ,
\tag{2}
$$
当 $b=1$ 时二者均为零模，空行列式取 $1$。$V_b$ 按 $Y,\ldots,Y^{b-1}$ 为基。

对 $Q\in Q_b$，取常数项为零的实际多项式原函数
$$
W_Q(Y)=\int_0^Y F(X)^2Q(X)\,dX .
\tag{3}
$$
这里只逐项除以 $1,\ldots,3b-1$；不引入解析积分、自由积分常数或新的曲线。置
$$
\Phi_F:Q_b\longrightarrow V_b,\qquad
Q\longmapsto W_Q\bmod(F,A).
\tag{4}
$$

**定理 1。** 在 (2) 的升幂基中，准确有
$$
\boxed{\det\Phi_F=\frac{2^b}{(3b-1)!}\operatorname{disc}(F)^2.}
\tag{5}
$$
这里 $\operatorname{disc}(F)=\prod_{i<j}(r_i-r_j)^2$ 为首一多项式的判别式；其平方不含根次序的号。特别在原 $p>3b$ 范围，(5) 的常数是整单位。

### 证明：五阶碰撞与完整常数

先在有理系数的通用分裂环中写
$$
F(Y)=\prod_{i=1}^b(Y-r_i),\qquad
\Delta(r)=\prod_{i<j}(r_j-r_i).
$$
考察 $(b-1)\times(b-1)$ 矩阵
$$
M_{ij}
=\int_{r_1}^{r_{i+1}}F(X)^2X^j\,dX,
\quad 1\le i\le b-1,\quad 0\le j\le b-2.
\tag{6}
$$
每个积分均指多项式原函数的两个值之差。

任意两根 $r_i,r_j$ 碰撞时，若需要先作一行相减，(6) 中便出现区间 $[r_i,r_j]$ 的一行。令
$X=r_i+(r_j-r_i)u$。$F(X)^2$ 的这两根因子给 $(r_j-r_i)^4$，$dX$ 再给一次。因此
$$
(r_i-r_j)^5\mid\det M .
$$
各根差为两两不伴随的素因子，而行列式总次数为
$$
\sum_{j=0}^{b-2}(2b+j+1)=\frac{5b(b-1)}2.
$$
故存在有理常数 $c_b$ 使
$$
\det M=c_b\Delta(r)^5.
\tag{7}
$$

为不借一个未核实的积分公式，下面直接求 $c_b$。置
$$
f(Y)=\prod_{i=1}^{b-1}(Y-r_i),\qquad r_b=R.
$$
将末列的 $Y^{b-2}$ 换为首一多项式
$f'(Y)/(b-1)$；该列变换行列式为 $1$。

前 $b-2$ 行、前 $b-2$ 列的最高 $R$ 次项是 $R^2$ 乘 $b-1$ 根的原矩阵。末列在这些行的 $R^2$ 项为
$$
\frac{R^2}{b-1}\int_{r_1}^{r_i}f(X)^2f'(X)\,dX=0,
$$
因为两端均为 $f$ 的根。故这些末列元素的 $R$ 次数至多为 $1$。

末行、末列的最高次项为
$$
R^{3b-1}\int_0^1u^{3b-4}(1-u)^2\,du
=
R^{3b-1}\frac{2}{(3b-3)(3b-2)(3b-1)}.
\tag{8}
$$
此处积分同样只是三项有理数之和。其它末行列的次数至多 $3b-2$；若行列式取到前面某行的末列，最高总次数至少少二。因此 (7) 的最高 $R^{5(b-1)}$ 系数给
$$
c_b=c_{b-1}\frac{2}{(3b-3)(3b-2)(3b-1)}.
$$
由 $c_1=1$，得到
$$
c_b=\frac{2^b}{(3b-1)!}.
\tag{9}
$$

最后，差值评价
$$
V_b\longrightarrow A^{b-1},\qquad
v\longmapsto(v(r_i)-v(r_1))_{i=2}^b
$$
在基 $Y,\ldots,Y^{b-1}$ 下的行列式为 $\Delta(r)$。所以
$M=(\text{差值评价})\Phi_F$，由 (7)–(9) 得
$$
\det\Phi_F=c_b\Delta(r)^4
=c_b\operatorname{disc}(F)^2.
$$
清去 $(3b-1)!$ 后这是通用多项式恒等式，故对 (1) 中的全部 $A$ 成立。证毕。

## 2. 全临界值核及退化纤维的准确长度

若 $A=k$ 为域，$\operatorname{disc}(F)\ne0$，则 (5) 说明 $\Phi_F$ 为同构。这里也有与原 Euler 核完全相容的直接证明。

若 $\Phi_F(Q)=0$，则 $F\mid W_Q-c$。在每个简单根处，
$$
W_Q'=F^2Q
$$
使 $W_Q-c$ 至少为三重零。因此 $F^3\mid W_Q-c$。但
$\deg W_Q\le3b-1$，故 $W_Q=c$，再由 (3) 得 $Q=0$。

若把来源扩到 $\deg Q\le b-1$，则同样的论证给
$$
\boxed{
\ker\left[Q\longmapsto W_Q\bmod(F,k)\right]=kF_Y.
}
\tag{10}
$$
准确原函数为
$$
W_{aF_Y}=\frac a3\bigl(F^3-F_0^3\bigr).
\tag{11}
$$
式 (11) 中的 $F_0^3$ 是真实零 charge 值，不能在实际前缀问题中删除。

现令 $A$ 为离散赋值环，均匀元为 $\tau$，仍假定 (1) 首一且常数 (9) 为单位，并且一般纤维可分。则 $\Phi_F$ 是两个秩 $b-1$ 的有限自由模之间的单射，余核为有限长度模，并且
$$
\boxed{
\operatorname{length}_A\operatorname{coker}\Phi_F
=2v_\tau(\operatorname{disc}(F)).
}
\tag{12}
$$
这是完整行列式给出的准确总长度。它没有给各个 Smith 指数，也没有把模 $\tau$ 的值映射认成满射。

例如对真实局部模型 $F=X^m-\tau$，
$$
\Phi_F(X^j)=
\frac{2m^2}{(j+1)(m+j+1)(2m+j+1)}
\,\tau^2X^{j+1}\bmod(F,A),
\quad 0\le j\le m-2.
\tag{13}
$$
因此该模型的全部 $m-1$ 个指数都恰为 $2$，总长度为 $2(m-1)$，与判别式的阶 $m-1$ 一致。式 (13) 只是该实际模型或其已经支付的整同构中的结论；不由此把一个任意奇异纤维或全局有帽来源换成任意局部多项式。

## 3. 非首一式及坐标变化的成本

对非首一 $F=f_bY^b+\cdots+f_0$，仅在 $f_b$ 可逆的开集上按同一基定义 (4)。写 $F=f_b\widehat F$。因原函数乘 $f_b^2$，得到
$$
\boxed{
\det\Phi_F
=\frac{2^b}{(3b-1)!}
\frac{\operatorname{disc}(F)^2}{f_b^{\,2b-2}}.
}
\tag{14}
$$
因此 $f_b$ 的零点不能被称作单位图；它们及原正水平的真实帽必须另保。

若在某个开集作
$$
Y=\alpha Z+\beta,\qquad
\widetilde F(Z)=uF(\alpha Z+\beta),
$$
其中 $\alpha,u$ 为单位，则来源基变换的行列式为
$\alpha^{(b-1)(b-2)/2}$，目标模常数基变换的行列式为
$\alpha^{b(b-1)/2}$，原函数还乘 $\alpha u^{-2}$。
逐项比较给
$$
\boxed{\det\Phi_{\widetilde F}=u^{2b-2}\det\Phi_F.}
\tag{15}
$$
这与 (14) 的判别式、首系数变换完全一致。若 $\alpha$ 或 $u$ 在边界非单位，(15) 只能作为分式域中的转框恒等式；实际格的该单项式成本不能删除。特别本注没有借有限 $Y$ 图抹掉 $Y=\infty$、固定角载体或非单项式的原水平正规化。

## 4. 回到同一原 $\mathcal J$，不增加自由系数

保 R833/R840 的
$$
\mathcal J=
\mathcal E_+^{-1}(F^2\mathcal H_1^{>0})\oplus\mathcal H_3^0,
\qquad \mathcal E=Y\partial_Y.
\tag{16}
$$
对同一个实际 $L\in\mathcal H_1^{>0}$，
$$
Q=\frac{L}{Y}
$$
在原有限 $Y$ 图是多项式，$\deg_YQ\le b-1$。在 $f_b$ 可逆的开集，可唯一写
$$
Q=Q_<+a(t)F_Y,\qquad \deg_YQ_<\le b-2.
\tag{17}
$$
于是同一个实际
$$
W=\mathcal E_+^{-1}(F^2L)+G_0
$$
准确满足
$$
\boxed{
W|_C\bmod k(t)
=\Phi_F(Q_<),\qquad
W=\int_0^YF^2Q_<\,dY+
\frac{a(t)}3(F^3-F_0^3)+G_0 .
}
\tag{18}
$$

因此 (5)、(12)、(14) 确实读取原 $\mathcal J$ 的全族，而不是一个新增自由来源。与此同时：

- $Q_<$ 与 $a(t)$ 由同一个原 $L$ 决定；不能把它们各自任意取值。
- 除以 $f_b$ 可能产生真实底边界极点。式 (17) 不证明 $Q_<$ 自己属于原 $\mathcal H_1$ 的某个放宽格。
- $G_0-a(t)F_0^3/3$ 是同一个原函数的零 charge；在原点前缀、负水平标签和同 $cF^3$ 尾中都须保留。
- (18) 的“模 $k(t)$”只用于比较相对临界值，不是物理矩阵允许商去任意底函数。

对目前的联合问题，仍须在同一个 $W$ 下求真正
$H_{\rm corr},K_{\rm corr}\in\mathcal H_2$，使
$$
eK_{\rm corr}|_C+W|_C\in H^0(C,N^3(-TP)),
$$
$$
eH_{\rm corr}|_C+f_2K_{\rm corr}|_C+
e(\mathcal EK_{\rm corr})|_C\in H^0(C,N^3(-TP)),
\quad T=s-r-13,
\tag{19}
$$
再读同一个第三 $3\eta$ 镜轴及第四短行。(12) 不证明 (19) 有解或无解，也不证明受限 $W_T$ 对分歧值商满射。完整原 $G_0/U_0$、十九角、所有低行右逆高尾及物理十三带保持。

本注给出的是原相对族中**判别式平方的精确退化成本**；不是由未加前缀的同构推断原受限像或指定 forcing 非零。

依赖：[R833](../results/R833-original-euler-image-and-negative-horizontal-cokernel.md)、[R834](../results/R834-original-three-long-euler-blocks-and-complete-ramification-ideal.md)、[R840](../results/R840-original-double-ramification-euler-image-and-unique-normal-tail.md)及上述同格联合交。无新数学程序运行。
