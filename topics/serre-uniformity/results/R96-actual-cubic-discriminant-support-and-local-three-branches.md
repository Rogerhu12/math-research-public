# R96：实际判别式的三次支撑与 $3$ 处的精确导子分支

日期：2026-11-12。状态：**已证明的必要条件与局部分类；主问题未完成。**

本文保留 **$j(E)\in\mathbb Z$** 前提，把 R66 的实际三次商导子接到实际 $E[3]$ 的 $S_3$ 商，并完整处理环类数三、底域类数一的七个 $(D,c)$。在 $K=\mathbb Q(\sqrt{-3})$ 的两项中，导子 $c=6$ **允许** $v_3(\Delta)\equiv2\pmod3$；其来源是局部整基指数 $3$，不能以多项式判别式代替三次域判别式。

本文件于执行环境重置后从已核证明恢复；标准库证书重新计算，SHA256 与重置前完全相同。

## 1. 设置与结论

设 $E/\mathbb Q$，$p>37$，实际模 $p$ 像为完整非分裂 Cartan 正规化子
$$
\rho_{E,p}(G_{\mathbb Q})=N,\qquad C\simeq\mathbb F_{p^2}^{\times}.
$$
商虚二次域记为 $K$，$D=|D_K|$，并假设
$$
\rho_{E,p}(I_p)=C^3,\qquad j(E)\in\mathbb Z.                 \tag{1.1}
$$
R66 给
$$
p\equiv2,5\pmod9,\qquad v_3(p^2-1)=1.                      \tag{1.2}
$$
取阶恰为三的 $\vartheta:C\to\mu_3$，写
$$
\lambda=\rho_{E,p}|_{G_K},\quad
\eta=\vartheta\lambda,\quad
r=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\eta,\quad
L=\overline{\mathbb Q}^{\ker r}.
$$
精确导子为
$$
\mathfrak f(\eta)=c\mathcal O_K,\qquad
c=3^aR,\quad M=Dc^2,\quad
R\text{ 平方自由},\quad(R,3Dp)=1.                         \tag{1.3}
$$
$\Delta$ 表示全局最小 Weierstrass 判别式；其三次类与模型、二次扭曲均无关。

**定理 96.1。** 对每个有理素数 $q\ne3,p$，包括 $q=2$，
$$
\boxed{q\mid R\quad\Longleftrightarrow\quad
3\nmid v_q(\Delta).}                                      \tag{1.4}
$$
又有
$$
v_p(\Delta)\not\equiv0\pmod3,\qquad
3\nmid c\Longrightarrow3\mid v_3(\Delta).                 \tag{1.5}
$$
实际模三表示经 $\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3$ 的商域为
$$
\boxed{\mathcal L_3(E)=\mathbb Q(\zeta_3,\sqrt[3]{\Delta}).} \tag{1.6}
$$
这里 $\Delta$ 非立方，所以其群确为 $S_3$。

**定理 96.2。** 若 $K=\mathbb Q(\sqrt{-3})$、$c=6$ 或 $9$，则
$$
\boxed{\mathbb Q_3(E[2])=L_w,\qquad
\Delta\in-3\mathbb Q_3^{\times2}.}                         \tag{1.7}
$$
$L$ 在 $3$ 只有一个素点 $w$，$L_w/\mathbb Q_3$ 为全分歧 $S_3$ 扩张。其任一三次子域 $F$ 满足
$$
v_3\operatorname{disc}(F)=
\begin{cases}3,&c=6,\\5,&c=9.\end{cases}                   \tag{1.8}
$$
原曲线的最小判别式还满足
$$
\begin{array}{c|c|c}
c&v_3(\Delta)\bmod6&v_3(\Delta)\bmod3\\ \hline
6&3\text{ 或 }5&0\text{ 或 }2\\
9&1\text{ 或 }5&1\text{ 或 }2.
\end{array}                                               \tag{1.9}
$$
第 5 节给出带局部整环指数及单位条件的完整必要分支表。

**推论 96.3。** R90 的七个底域类数一、原始环类数三的组合给以下三次类，等式均在 $\mathbb Q^\times/\mathbb Q^{\times3}$ 中解释。

| $(D,c)$ | $\Delta$ 的必要三次类 |
|---|---|
| $(11,2),(19,2),(43,2),(67,2),(163,2)$ | $2^u p^v$，$u,v\in\{1,2\}$ |
| $(3,6)$ | $2^u3^w p^v$，$u,v\in\{1,2\}$，$w\in\{0,2\}$ |
| $(3,9)$ | $3^w p^v$，$w,v\in\{1,2\}$ |

因此 (1.6) 的候选域可规范为：

- $c=2$：$\mathbb Q(\zeta_3,\sqrt[3]{2p})$ 或 $\mathbb Q(\zeta_3,\sqrt[3]{2p^2})$；
- $(D,c)=(3,6)$：$\mathbb Q(\zeta_3,\sqrt[3]{2\cdot3^w p^v})$，$w\in\{0,1,2\}$、$v\in\{1,2\}$，至多六个；
- $(D,c)=(3,9)$：$\mathbb Q(\zeta_3,\sqrt[3]{3p})$ 或 $\mathbb Q(\zeta_3,\sqrt[3]{3p^2})$。

第二行域的规范式允许 $w=1$，因为取整个三次类的逆不改变分裂域；原判别式的允许指数仍为 $\{0,2\}$。

本文只给实际曲线的必要条件，不证明候选域均由实际曲线实现，不给所有 $p$ 的排除。证明本身不使用无 CM 性；满足同样实际像与局部条件的 CM 点仍须保留。

## 2. 真实有限惯性与实际 $E[3]$ 商

### 2.1 忠实检测三次惯性，包括 $q=2$

取 $q\ne p$。整 $j$ 给潜在好约化，有限惯性商记为 $\Gamma_q$。它在任意素于 $q$ 的 Tate 模上忠实；模 $p$ 仍忠实，因为
$1+pM_2(\mathbb Z_p)$ 没有非平凡有限阶元素。

$\Gamma_q$ 的每个阶三元在 $N/C$ 中平凡。由 $v_3(|C|)=1$，$\vartheta$ 在 $C$ 的阶三子群上忠实，故
$$
\eta\text{ 在 }q\text{ 上方分歧}
\quad\Longleftrightarrow\quad3\mid|\Gamma_q|.               \tag{2.1}
$$
若 $q$ 在 $K$ 分裂，两处字符互逆，分歧与否一致。

再设 $q\ne3$。$T_3(E)\to E[3]$ 的核 $1+3M_2(\mathbb Z_3)$ 同样无扭，所以有限惯性在 $E[3]$ 上忠实。映射
$$
\operatorname{GL}_2(\mathbb F_3)\longrightarrow S_3
$$
的核 $Q_8$ 为二群，保留全部三次惯性。这个论证在 $q=2$ 原样成立，没有使用温和约化或二次好约化扭曲。

### 2.2 判别式的立方预解式

对有理短模型
$$
y^2=x^3+Ax+B,\qquad \Delta=-16(4A^3+27B^2),
$$
四个循环三子群的 $x$ 坐标为
$$
X^4+2AX^2+4BX-\frac{A^2}{3}
$$
的根。四个对象的三种两两分组给 $S_4\to S_3$；其三次预解式平移 $2A/3$ 后为
$$
T^3+\frac{\Delta}{27}.                                    \tag{2.2}
$$
$\operatorname{PGL}_2(\mathbb F_3)\simeq S_4$ 中此映射的核是 Klein 四元群，其在 $\operatorname{GL}_2(\mathbb F_3)$ 中的原像是 $Q_8$。所以 (2.2) 的分裂域就是 (1.6)。详尽的实际除法域解释也见 R93；不能由此把 $L$ 与 $\mathcal L_3(E)$ 认作同一全局域。

在 $q\ne3$，$\mathbb Q_q(\zeta_3)/\mathbb Q_q$ 不分歧。写 $\Delta=q^n u$，$u$ 为单位：

- $3\nmid n$ 时，立方根的赋值分母为三，分歧指数为三；
- $3\mid n$ 时先除去立方。剩余单位的立方根至多需要不分歧三次扩张，主单位的取三次幂映射由 Hensel 引理为同构。

故该商域的惯性含三次部分，恰当且仅当 $3\nmid v_q(\Delta)$。与 (2.1) 及 R66 的 $R$ 定义合起来即得 (1.4)。

### 2.3 $p$ 与未分歧的 $3$ 处

R66 给小惯性分支在 $p$ 的最小好约化惯性阶为 $e_p=3$ 或 $6$。由于 $p>3$，精确公式
$$
e_p=\frac{12}{\gcd(12,v_p\Delta)}
$$
给 $v_p\Delta\bmod12\in\{4,8,2,10\}$，所以非零模三。这也证明 $\Delta$ 非立方。

若 $3\nmid c$，(2.1) 给 $3\nmid|\Gamma_3|$。取得好约化后判别式变为单位，模型缩放给
$$
12\mid|\Gamma_3|\,v_3(\Delta),
$$
从而 $3\mid v_3(\Delta)$。这里只使用必要缩放关系，没有把它当成特征三的完整惯性分类。定理 96.1 得证。

## 3. $K=\mathbb Q(\sqrt{-3})$ 的真实局部商同域

本节设 $c=6$ 或 $9$；因此 $\eta$ 在三上方分歧，$K_3/\mathbb Q_3$ 也分歧。

### 3.1 有限惯性恰为 $C_3\rtimes C_4$

(2.1) 给 $\Gamma_3$ 含阶三元。商域在三分歧，惯性还含 $g\in N\setminus C$。其行列式为一，因为 $p$ 进圆分特征在三的惯性上平凡。写外侧作用为 $x\mapsto ax^p$，则
$$
g^2=N_{\mathbb F_{p^2}/\mathbb F_p}(a)I,\qquad
\det(g)=-N_{\mathbb F_{p^2}/\mathbb F_p}(a).
$$
所以 $g^2=-I$，$g$ 的阶为四。

$\Gamma_3$ 嵌入好约化特殊纤维的保原点自同构群。特征三中含阶三自同构的椭圆曲线有 $j=0$，在代数闭包上写为 $y^2=x^3-x$。其所有保原点自同构为
$$
(x,y)\longmapsto(u^2x+t,u^3y),\qquad
u^4=1,\quad t^3-t=0.
$$
直接代入及 Weierstrass 坐标变换给出全部十二个自同构，群为 $C_3\rtimes C_4$，四阶元反演三阶子群，中心为 $\{\pm1\}$。由于 $\Gamma_3$ 含三、四阶元，必等于此十二阶群：
$$
\Gamma_3=C_3\rtimes C_4,\qquad
\Gamma_3/\{\pm1\}\simeq S_3.                              \tag{3.1}
$$

### 3.2 惯性同构延拓到整个局部群

中心 $-1$ 在 $E[2]$ 上平凡；$T_2(E)\to E[2]$ 的核为 pro-$2$，不能杀掉阶三元。$\Gamma_3$ 的最大正规二子群恰为中心，所以 $E[2]$ 的惯性核正是 $\{\pm1\}$，像为全部 $S_3$。

对 $r$，$\vartheta$ 在三阶子群忠实，在 $\pm1$ 上平凡，外侧元变为换位，故惯性核也恰为中心。两种惯性 $S_3$ 表示相差一个内自同构；共轭后可令二者相同。

任意 $g\in G_{\mathbb Q_3}$ 的两种像在该全部惯性 $S_3$ 上实施相同共轭，所以两像之比中心化整个 $S_3$，只能是单位元。于是整个局部群上的核相同：
$$
\mathbb Q_3(E[2])=L_w.                                    \tag{3.2}
$$
惯性像已为全部 $S_3$，这个六次扩张全分歧，且 $L$ 在三只有一个素点。

$E[2]$ 的符号特征对应 $\mathbb Q_3(\sqrt\Delta)$，$r$ 的符号特征对应 $K_3$，所以
$$
\Delta\in-3\mathbb Q_3^{\times2}.                          \tag{3.3}
$$
尤其其赋值为奇数，除去全部 $3$ 幂因子后的单位满足
$$
3^{-v_3\Delta}\Delta\equiv-1\pmod3.                        \tag{3.4}
$$

这是局部同域。R66 证明 $L$ 在 $p$ 不分歧，而 $\mathbb Q(E[2])$ 在 $p$ 有三次惯性；二者不是同一全局域，不能将 (3.2) 扩大。

### 3.3 三次域判别式指数

$(3)=\mathfrak p^2$。精确导子 $c=6,9$ 分别给 $\eta$ 的局部导子 $\mathfrak p^2,\mathfrak p^4$；这两个偶数指数已在 R66 §3.4 由局部单位过滤证明。Artin 导子诱导公式给
$$
a_3(r)=v_3(D_K)+v_3N\mathfrak f(\eta)
=\begin{cases}3,&c=6,\\5,&c=9.\end{cases}                  \tag{3.5}
$$
任一三次子域 $F$ 的三维置换表示为 $1\oplus r$，导子—判别式公式给 (1.8)。也可直接比较：所有非平凡野惯性都是 $C_3$，两个二维表示在其上无不变量，温和项均为二。

## 4. 保持相关数据的局部归一化

在三处取最小整模型，完成平方后为
$$
y^2=x^3+a_2x^2+a_4x+a_6,\qquad a_i\in\mathbb Z_3.
$$
坏约化且 $j$ 整给 $v_3(c_4)>0$；由 $c_4\equiv a_2^2\bmod3$ 得 $3\mid a_2$，可作整平移消去二次项，得到最小短模型
$$
y^2=x^3+Ax+B,\qquad A,B\in\mathbb Z_3.
$$
坏约化迫 $3\mid A$。

若 $v_3(A)\ge2,v_3(B)\ge3$，作局部二次扭曲
$$
(A,B)\longmapsto(A/9,B/27),\qquad
\Delta\longmapsto\Delta/3^6.                               \tag{4.1}
$$
它保持 $j,E[2],\eta$ 及判别式的三次类、平方类；$\eta$ 不变因为二次扭曲仅乘被 $\vartheta$ 杀掉的标量 $\pm1$。反复进行可取
$$
a=v_3(A)\ge1,\quad b=v_3(B)\ge0,\qquad
a<2\ \text{或}\ b<3.                                      \tag{4.2}
$$
零系数赋值按 $+\infty$。过程不会产生 $a=0$：否则判别式为单位，与所保持的奇平方类 $-3$ 矛盾。

最终模型最小：$a=1$ 时 $v_3(c_4)=2<4$；$b<3$ 时 $v_3(c_6)=3+b<6$，均排除非单位缩放。因此最终指数 $n$ 与原最小指数相差六的倍数。它为奇数，整 $j$ 又给
$$
n\le3(a+1)                                               \tag{4.3}
$$
（$A=0$ 时右侧无限）。比较 $n=v_3(4A^3+27B^2)$，全部分支为：

- $a=1,b\ge1$：$n=3$；
- $a=1,b=0$：$3\le n\le6$，奇性只余 $3,5$；
- $a\ge2,b=0$：$n=3$；
- $a\ge2,b=1$：$n=5$；
- $a=2,b=2$：$n=6$，不允许；
- $a\ge3,b=2$：$n=7$。

还必须计算整基指数与单位条件，不能合并两个 $n=5$。

## 5. 整基指数与完整实际分支表

设 $f(X)=X^3+AX+B$。由 (3.2)，它不可约，根给全分歧三次域 $F$。其判别式 $\Delta/16$ 的三进指数为 $n$。

### 5.1 $n=3$

域判别式指数由 (1.8) 只能为三或五，且不大于 $n=3$，故此时为三、原根已经生成最大整环，对应 $c=6$。

$a=1,b=0,n=3$ 不能出现：写 $A=3a_0$，则 $a_0,B$ 为单位；无额外抵消迫 $a_0\equiv1\bmod3$，于是
$$
\Delta/27\equiv-(a_0+B^2)\equiv1\pmod3,
$$
违反 (3.4)。在 $a=1,b\ge1$ 时则须
$$
A/3\equiv1\pmod3,                                        \tag{5.1}
$$
而 $a\ge2,b=0$ 时单位条件自动成立。

### 5.2 特殊 $a=1,b=0,n=5$：局部整环指数三

写 $A=3a_0$，$a_0,B$ 为单位，且
$v_3(4a_0^3+B^2)=2$。取 $r_0\in\{\pm1\}$ 使 $f(r_0)\equiv0\bmod3$，写
$$
a_0=-r_0^2+3d,\qquad C_0=f(r_0).
$$
由 $B=C_0+2r_0^3-9dr_0$，直接展开得
$$
4a_0^3+B^2
=27d^2(4d-r_0^2)+C_0(4r_0^3-18dr_0+C_0).                 \tag{5.2}
$$
$C_0$ 被三整除，第二括号为单位，第一项被二十七整除，所以
$$
C_0=9c_0,\qquad c_0\in\mathbb Z_3^\times.                  \tag{5.3}
$$
平移 $X=Y+r_0$ 得
$$
Y^3+3r_0Y^2+9dY+9c_0=0.
$$
对根 $y$ 取 $\beta=y^2/3$，则
$$
\boxed{\beta^3+3(2d-r_0^2)\beta^2+
3(3d^2-2r_0c_0)\beta-3c_0^2=0.}                          \tag{5.4}
$$
这是三处 Eisenstein 多项式，所以 $\beta$ 为素元且
$\mathcal O_F=\mathbb Z_3[\beta]$。

精确的判别式核算如下。对 $g(Y)=Y^3+sY^2+tY+u$，
$\beta=y^2/3$ 的多项式为
$$
X^3+\frac{2t-s^2}{3}X^2+
\frac{t^2-2su}{9}X-\frac{u^2}{27}.
$$
两两根差相乘给
$$
\operatorname{disc}(\beta)=
\operatorname{disc}(g)\frac{(u-st)^2}{3^6}.                \tag{5.5}
$$
这里 $u-st=9(c_0-3r_0d)$ 的赋值为二，故域判别式指数为
$$
5+2\cdot2-6=3.                                           \tag{5.6}
$$
所以这个 $n=5$ 分支对应 **$c=6$**，原根的局部整环指数为三。单位条件进一步为
$$
\Delta/3^5\equiv-r_0c_0\pmod3,\qquad
r_0c_0\equiv1\pmod3.                                     \tag{5.7}
$$

精确局部例子为 $y^2=x^3-3x+11$。原三次式判别式
$-3159=-3^5\cdot13$；平移后为 $y^3+3y^2+9$，$\beta=y^2/3$ 的多项式是
$$
X^3-3X^2-6X-3,
$$
在三 Eisenstein，判别式 $-351=-3^3\cdot13$。此例在三的 $j$ 整，局部平方类为 $-3$。它只反驳“局部导子指数三迫 $3\mid v_3\Delta$”；不是本题一条全局整 $j$ 的异常曲线。

### 5.3 $a\ge2,b=1,n=5$：没有指数修正

写 $A=9a_0,B=3b_0$，$b_0$ 为单位。原多项式
$$
X^3+9a_0X+3b_0
$$
已经 Eisenstein，生成最大整环，且
$$
\operatorname{disc}(f)=-3^5(12a_0^3+b_0^2).               \tag{5.8}
$$
所以域判别式指数五，对应 $c=9$。单位为 $-1\bmod3$，自动满足 (3.4)。

### 5.4 $a\ge3,b=2,n=7$：另一个指数三

写 $A=27a_0,B=9b_0$，$b_0$ 为单位。$\beta=x^2/3$ 的多项式是
$$
X^3+18a_0X^2+81a_0^2X-3b_0^2,                            \tag{5.9}
$$
它为 Eisenstein，且
$$
\begin{aligned}
\operatorname{disc}(f)&=-3^7(36a_0^3+b_0^2),\\
\operatorname{disc}(\beta)&=-3^5b_0^2(36a_0^3+b_0^2).
\end{aligned}                                            \tag{5.10}
$$
域判别式指数五，原根指数三，对应 $c=9$；单位条件自动成立。

### 5.5 完整必要表

下表始终保留第 3 节的实际 $S_3$ 惯性前提。它不声称任意满足这些系数赋值的多项式均不可约或均来自异常曲线。$a,b,n$ 均为二次扭曲归一化后的赋值。

| $a=v_3(A)$ | $b=v_3(B)$ | $n=v_3\Delta$ | 三次域判别式指数 | 原根的局部整环指数 | $v_3(c)$ | 单位条件 |
|---|---:|---:|---:|---:|---:|---|
| $1$ | $\ge1$ | $3$ | $3$ | $1$ | $1$ | $A/3\equiv1\bmod3$ |
| $\ge2$ | $0$ | $3$ | $3$ | $1$ | $1$ | 自动 |
| $1$ | $0$ | $5$ | $3$ | $3$ | $1$ | $r_0c_0\equiv1\bmod3$ |
| $\ge2$ | $1$ | $5$ | $5$ | $1$ | $2$ | 自动 |
| $\ge3$ | $2$ | $7$ | $5$ | $3$ | $2$ | 自动 |

归一化只改变指数六的倍数，故表格证明 (1.9)，完成定理 96.2。

### 5.6 精确的 $j$ 赋值

若 $j\ne0$，二次扭曲不改变 $j$，可在表中代入
$v_3(j)=3(a+1)-n$，得到
$$
\boxed{
\begin{aligned}
c=6&:\quad v_3(j)\in\{1\}\cup3\mathbb Z_{>0},\\
c=9&:\quad v_3(j)\ge4,\qquad3\nmid v_3(j).
\end{aligned}}                                           \tag{5.11}
$$
前者还给
$$
v_3(j)=1\Longrightarrow j\equiv6\pmod9,\qquad
v_3(j)=3\Longrightarrow j/27\equiv1\pmod3.                 \tag{5.12}
$$
第一条用特殊分支中 $a_0\equiv-1\bmod3$、(5.7) 和 $c_4=-144a_0$；第二条用 (5.1) 与 $\Delta/27\equiv-1\bmod3$。其他分支的 $j$ 单位由 $A/3^a$ 决定，不固定为某一值。

因此，写 $j=dX^3$ 为逆三次支撑时，$c=6,v_3(d)=1$ 要求 $3\nmid X$；$c=9$ 的两种 $d$ 都要求 $3\mid X$。只用三次支撑的枚举仍是安全必要超集。

## 6. 全局支撑与真实 Frobenius 筛

R90 的七对为
$$
(11,2),(19,2),(3,6),(43,2),(3,9),(67,2),(163,2).
$$
代入定理 96.1、96.2，所有 $2,3,p$ 外的赋值被三整除，余下指数恰为推论 96.3。负号是有理立方，不增参数；取整体三次类的逆给所列 $2,6,2$ 种域。

这些是实际 $E[3]$ 商域。对 $q\ge5$、$q\ne p$、$q\equiv1\bmod3$，设 $q$ 不整除规范代表 $d$：

- $d$ 模 $q$ 为立方时，商的 Frobenius 为一；实际好约化模型的 $E[3]$ Frobenius 在 $Q_8$ 中，所以
  $$
  a_q\equiv0\pmod3\quad\text{或}\quad
  a_q\equiv\pm(q+1)\pmod9;
  $$
- $d$ 模 $q$ 非立方时，商的 Frobenius 为三循环，所以 $3\nmid a_q$。

模九条件来自 Frobenius 为 $\pm I$ 时，曲线或其二次扭曲的全部三挠点在剩余域有理。若原曲线尚未好约化、但 $q$ 在 $K$ 分裂，R63 给保留剩余域的全分歧好约化扩张；该商域在 $q$ 不分歧，其 Frobenius 类保持。只有在这种实际扩张后才能使用真正整数迹，不能给未好约化模型直接代入“$a_q$”。

有限层筛选不代替所有 $p$ 的排除，通过筛选的 CM 扭曲也不能删去。

## 7. 标准库精确证书

[verify_ring_class_three_discriminant_support.py](../scripts/verify_ring_class_three_discriminant_support.py) 只用标准库的整数、有理数及稀疏多项式，验证：

1. $\beta=y^2/3$ 的多项式在原三次关系下严格为零，以及 (5.5)；
2. 特殊分支平移、Eisenstein 性及判别式指数从五降到三；
3. 其余分支判别式恒等式、全部首项模三和 $j$ 单位条件；
4. $A=-3,B=11$ 的局部整数证书；
5. 候选商域规范式的 $2,6,2$ 项计数。

无限分类由 §§2–5 证明；模三有限检查只核对符号恒等式中已决定赋值的首项，不代替证明。

在本目录运行：

~~~sh
python -B scripts/verify_ring_class_three_discriminant_support.py
~~~

重建证书加 `--write`。正常执行重算全部恒等式并逐字比较
[ring_class_three_discriminant_support.json](../scripts/data/ring_class_three_discriminant_support.json)。

证书 SHA256：
~~~text
c44cac982d2d9ff3c8d4255ab44ff99503a6b9716ed8c9278cd0576f2f1e2b23
~~~

## 8. 输入、来源与边界

- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md) §§2–6：实际小惯性、精确三次导子及三处单位过滤。
- [R90](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)：七个原始 $(D,c)$。
- [R93](R93-class-three-exclusion-by-the-actual-three-division-field.md)：实际 $E[3]$ 的 $Q_8$ 商与整数迹检测。
- J.-P. Serre，*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*，Invent. Math. **15** (1972), 259–331，§5.6，尤其 pp. 311–312；[作者原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。所用输入为实际有限惯性、素于剩余特征且阶至少三的挠点上的忠实性、自同构实现及大于三特征的精确温和惯性阶。
- J.-P. Serre，*Local Fields*，GTM **67**，Springer (1979)，Chapter VI 的 Artin 导子诱导与导子—判别式公式；[出版社章节](https://link.springer.com/chapter/10.1007/978-1-4757-5673-9_7)。全部有歧义的局部整环指数已在本文直接计算。

整 $j$ 前提不能删除：在 Tate 位置，模 $p$ 单幂部分可能因参数为 $p$ 次幂而消失，而 $v_q\Delta\bmod3$ 不由 $\eta$ 不分歧决定。因此 (1.4) 与有限三次支撑不适用于任意非整 $j$ 曲线。
