# 二次一模式的真实消元：去掉重复根例外并证明全部平方向量循环

日期：2026-11-12。作者：l2_moments，独占稿。
状态：完整证明待父代理交叉核验。这里使用三阶共同正则化及有界消元式，不假定二阶闭乘子本身具有 gauge 同定义域，也不假定一般第一阶限制像稠密。

## 1. 主结论

设
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2,\quad a\ne0.
$$
令
$$
j_0=\min\{j:a_j\ne0\},\qquad
h=2^{j_0},\qquad a=a_{j_0}\ne0,\qquad d=d_{j_0}.
$$
单个 $a$ 仅表示首个非零系数。则
$$
\boxed{\lambda\ne a^2
\quad\Longrightarrow\quad
u^2-\lambda\text{ 对实际 }A\text{ 循环}.}
\tag{1.1}
$$
特别地，
$$
\boxed{u^2\text{ 对 }A\text{ 循环}}
\tag{1.2}
$$
对每个非常数复 $\ell^2$ 第一 chaos 向量都成立。

这是 R142 的二次结论的严格加强：其两个候选值 $0,a^2$ 中，重复根所产生的 $0$ 已经完全排除；本稿仍不自动处理唯一剩余候选 $a^2$。非零常数 $u$ 的平方当然循环，零常数除外。

## 2. 二阶闭乘子与自然一阶平方的准确关系

记 $X=X_u$ 为 R125 的第一阶闭乘子，$S=X_{u^2}$ 为 R131 的二阶闭乘子。复 Rademacher 有限矩估计给 $u^2\in H_{\le2}$，所以 $S$ 已真实构造，满足
$$
S^*=CSC,
$$
有限柱为图核心，全部有界交换子保持其域并与其域交换。此外
$$
S1=u^2,\qquad
\overline{\operatorname{Ran}(S-\lambda I)}
=\operatorname{cyc}_A(u^2-\lambda).
\tag{2.1}
$$

R134 的二阶 Bell 修正是
$$
B_2=\sum_j a_j^2(I-V_j^2)\in\mathcal A.
\tag{2.2}
$$
该级数按算子范数绝对收敛，$\chi(B_2)=0$，且 $B_2\in\mathcal A_h$。

在有限柱 $z$ 上，有真实等式
$$
Sz=X^2z+B_2z.
\tag{2.3}
$$
说明如下。R134 已证明 $1\in\operatorname{Dom}X^2$ 及
$X_N^21\to X^21$。写 $z=X_z1$，其中有限柱乘子 $X_z\in\mathcal A$，
由域交换得 $z\in\operatorname{Dom}X^2$，且
$X_N^2z=X_zX_N^21\to X^2z$。有限系数二阶恒等式
$X_{u_N^2}=X_N^2+B_{2,N}$ 与 R131 的固定次数收敛给 (2.3)。

进一步，对任意 $x\in\operatorname{Dom}X^2$ 和有限柱 $z$，
$$
B(x,Sz)=B(x,X^2z+B_2z)=B(X^2x+B_2x,z).
$$
因为有限柱是 $S$ 的图核心，且 $S$ 对双线性型 $B$ 自伴，通常伴随的定义域判据给
$$
x\in\operatorname{Dom}S,\qquad
Sx=X^2x+B_2x.
\tag{2.4}
$$
所以自然算子 $X^2+B_2$ 包含在 $S$ 中；反过来它包含有限柱图核心，由此
$$
\boxed{S=\overline{\,X^2+B_2\,}}
\tag{2.5}
$$
（自然定义域为 $\operatorname{Dom}X^2$）。

(2.5) 没有断言自然 $X^2$ 自己已经闭，也没有断言
$\operatorname{Dom}S=\operatorname{Dom}X^2$。后面的正则化专门处理这个区别。

## 3. 核内存在稠密的三阶共同定义域

固定 $\lambda\in\mathbb C$，令
$$
M=\ker(S-\lambda I).
$$
它闭且 $A$ 不变。R128 的四正分量共同正则化 $R(t)$ 满足
$$
\|R(t)\|\le1,\qquad R(t)\to I\text{ 强收敛},\qquad
R(t)H\subseteq\operatorname{Dom}X,\qquad XR(t)\in\mathcal B(H).
$$
它属于 $\{A\}'$，且与 $X$ 域交换。归纳可得
$$
R(t)^kH\subseteq\operatorname{Dom}X^k,\qquad
X^kR(t)^k=(XR(t))^k.
\tag{3.1}
$$
例如 $XR(t)^2=R(t)(XR(t))$ 的像再次落入
$\operatorname{Dom}X$；同一论证逐阶成立。

全部有界交换子保持 $M$，故 $R(t)^3M\subseteq M$。又
$R(t)^3\to I$ 强收敛，所以
$$
\boxed{M\cap\operatorname{Dom}X^3\text{ 在 }M\text{ 中稠密}.}
\tag{3.2}
$$
这里只需固定的三阶平滑；不需要一个同时处于所有幂域的稠密核。

对 dyadic $\zeta$，R125 给
$$
U_\zeta XU_\zeta^*=X+D_\zeta(A),
\tag{3.3}
$$
其中 $D_\zeta(A)$ 有界、与 $X$ 域交换。这不仅保证一阶同域，也归纳给
$$
U_\zeta\operatorname{Dom}X^k=\operatorname{Dom}X^k
\quad(k\ge1).
\tag{3.4}
$$
因为一个有界且保持 $\operatorname{Dom}X$ 的可交换扰动不改变自然平方的定义域；重复此判断得到所有固定幂。因此
$U_\zeta(M\cap\operatorname{Dom}X^3)$ 在 $U_\zeta M$ 中稠密，且仍处于三阶域。

## 4. 真正的两个解析差与一个有界消元式

固定 $\zeta$，简记
$$
D=\gamma_\zeta(X)-X,\qquad
E=\gamma_\zeta(B_2)-B_2.
$$
$D$ 是 R125 的有限真正解析和。由 (2.2)，高于 $\zeta$ 的阶所涉及位的 $V_j$ 均被固定，所以 $E$ 也是有限的真正解析和。

设 $\zeta^h\ne1$。两者的首阶系数为
$$
D=A^h d_\zeta(A),\qquad
d_\zeta(0)=-\frac{2a}{d}(\zeta^h-1)\ne0,
\tag{4.1}
$$
以及
$$
E=A^h e_\zeta(A),\qquad
e_\zeta(0)=\frac{4a^2}{d}(\zeta^h-1).
\tag{4.2}
$$
因此 $d_\zeta(A)$ 是解析单位，且真正的解析商
$$
G:=E/D:=e_\zeta(A)d_\zeta(A)^{-1}
$$
满足
$$
\chi(G)=-2a.
\tag{4.3}
$$
这里是两个明确真正解析芽同时提取 $A^h$ 后作商，不是一般
$\mathcal A$ 元素的非法有界除法。

在以 $w$ 为形式变量的交换有界系数环中，置
$$
C=B_2-\lambda I,\qquad
P(w)=w^2+C,
$$
$$
K=D^2+E,\qquad
Q(w)=P(w)+2Dw+K.
\tag{4.4}
$$
则有精确多项式恒等式
$$
\boxed{
R:=K^2+4D^2C
=(K-2Dw)\,Q(w)+(4D^2-K+2Dw)\,P(w).
}
\tag{4.5}
$$
两边展开即可核对；右侧的三次 $w$ 项相消，左侧为有界算子。

又由 $E=DG$，
$$
R=D^2\bigl[(D+G)^2+4B_2-4\lambda I\bigr].
\tag{4.6}
$$
方括号属于 $\mathcal A$，其常数特征为
$$
4a^2-4\lambda.
$$
所以只要 $\lambda\ne a^2$，它就是 $\mathcal A$ 单位；结合 (4.1)，有
$$
\boxed{R=A^{2h}W_\zeta,\qquad W_\zeta\in\mathcal A^\times.}
\tag{4.7}
$$
当 $\zeta^h=1$ 时无需构造这个商；这些 $\zeta$ 只构成有限群 $\mu_h$。

## 5. 在高阶共同域上消元，然后回到完整闭核

取
$$
x\in M\cap\operatorname{Dom}X^3,\qquad
y\in U_\zeta(M\cap\operatorname{Dom}X^3).
$$
由 (2.4)，$P(X)x=0$。写 $y=U_\zeta z$，$z\in M\cap\operatorname{Dom}X^3$。
自然幂域的 gauge 等式和 (3.3) 给
$$
Q(X)y
=\bigl((X+D)^2+B_2+E-\lambda I\bigr)y
=U_\zeta P(X)z=0.
\tag{5.1}
$$
这里没有要求 $U_\zeta$ 保持 $\operatorname{Dom}S$；只使用已证的自然一阶幂域 (3.4)。

(4.5) 在 $\operatorname{Dom}X^3$ 上合法。所有有界系数属于
$\mathcal A$，故与 $X$ 域交换，并且对 $B$ 对称。由于
$(K-2DX)x\in\operatorname{Dom}X^2$，双线性对称性及 (5.1) 给
$$
\begin{aligned}
B(Rx,y)
&=B\bigl(Q(X)(K-2DX)x,y\bigr)\\
&=B\bigl((K-2DX)x,Q(X)y\bigr)=0.
\end{aligned}
\tag{5.2}
$$
另一个项因 $P(X)x=0$ 消失。三阶域保证每一步乘积和配对都有定义；没有对全核向量直接应用未知的 $X$ 或 $X^2$。

$R$ 有界，(3.2) 及其酉像均稠密，故 (5.2) 延拓为
$$
B(RM,U_\zeta M)=0.
\tag{5.3}
$$
对 $\lambda\ne a^2$，(4.7) 中单位及其逆保持 $M$，R23 又给
$\overline{A^{2h}M}=M$，所以
$$
B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_h).
\tag{5.4}
$$

R122/R125 的有限 Fourier 支撑机制现在适用。任意 $v,w\in M$ 的反射乘积
$v(y)w(-1-y)$ 只有有限群 $\mu_h$ 的 Fourier 支撑；若 $M\ne0$，
其总本质支撑由 odometer 遍历性为全测。逐个低头柱选择非零乘积，
迫每柱上的限制至多一维，因此 $\dim M\le h$。这与 $A$ 单射拟幂零不允许非零有限维不变空间矛盾。故 $M=0$。

$S-\lambda I$ 的 $C$ 自伴性于是给稠密值域；最后由 (2.1)，
$u^2-\lambda$ 循环。定理完成。

## 6. 具体例子、补充子类与剩余边界

对
$$
u=\sum_{j\ge0}\frac{(-1)^j}{j+1}\chi_j
$$
有 $a=1$。因此本稿证明
$$
u^2-\lambda\text{ 循环}\quad(\lambda\ne1),
$$
特别证明了 R142 留下的 $u^2$。该第一阶闭乘子由 R138 具有全平面连续谱，
所以本证明不使用有界逆或空谱方法。

若原第一阶系数另属于 $\ell^1$，R133 也给一个覆盖剩余值的直接子类。
此时二阶 $u^2-\lambda$ 的首行和为
$$
\tau_{j_0}=2a\left(a_*+\sum_{j>j_0}a_j\right).
$$
若括号非零，R133 证明全部 $\lambda$ 的循环性，包含 $\lambda=a^2$。
该补充不适用于一般 $\ell^2\setminus\ell^1$ 输入。

本稿的消元单位在 $\lambda=a^2$ 时确实失去常数特征，因此没有把这一个候选值自动排除。仅有有限柱 $u=a\chi_{j_0}$ 时，
$u^2-a^2=0$，说明任何最终无例外版本都必须保留“输出非零”的条件。
对上述交替无限模式的非零 $u^2-1$，仍需继续研究。
