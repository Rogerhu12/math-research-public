# 实际 theta 平面的惰性首进位与共同次数谱行

日期：2026-11-12。**状态：本文首进位、首次指数分母、同一全列模 $p$
关系及有限饱和格证书均已证明。** 没有得到 R159 所需的严格惰性预算。
特别地，本文不把一条 Hurwitz 系数的模 $p$ 关系当作支付了最高阶乘的
全部分母，也不从首进位非对数型推断原中央目标不可能。

## 1. 固定的原源，不另选局部截面

采用 R117、R162 的同一平面
$$
(A_2(z),B(z))
 =\bigl(\vartheta(z)^{68}P(s),\vartheta(z)^{68}Q(s)\bigr),
\qquad s=u(z)^4,\quad u=x^{-1/2}.
\tag{1}
$$
$P,Q\in\mathbb Z[1/5][s]$ 是 R162 式 (1.3) 的固定多项式，均以 $s$
为首项。仍记 $V=Q/P-1=-22s+\cdots$。原源为
$$
\mathscr P_D=\bigoplus_{b+c\le D}\mathbb Z_p X^bY^c.
\tag{2}
$$
其整幺三角基也可写成 $A_2^jV^c$，$0\le c\le j\le D$。
参数 $s=z^4+O(z^8)$ 的首系数为一，所以在 $s$ 与 $w=z^4$ 中，
每一个准确前缀核相同，消失阶 $k$ 的首系数相同。这是严格的
饱和 jet 等距；不要求换元的其余系数整。

令
$$
W(s)=\log\vartheta(z(s))^{68}.
$$
R162 从整数流直接证明
$$
4s(1-s)W''+(3-5s)W'=17,\qquad
a_n=[s^n]W'=\frac{17}{3}\prod_{j=1}^n\frac{4j+1}{4j+3},
\qquad [s^m]W=\frac{a_{m-1}}m.
\tag{3}
$$
以下固定 $p=4r-1\ge7$。所有估值均为 $v_p(p)=1$；$17$ 在这些
惰性素数处自动为单位。

## 2. 实际首进位的完整范围

对 $0\le n<p^2$，定义
$$
\begin{aligned}
\epsilon_1(n)&=
 -\mathbf1_{\{\,r-1\le n\bmod p\le3r-2\,\}},\\
\epsilon_2(n)&=
 \mathbf1_{\{\,(p^2-1)/4\le n<(3p^2-3)/4\,\}}.
\end{aligned}
$$
则准确有
$$
\boxed{\quad v_p(a_n)=\epsilon_1(n)+\epsilon_2(n).\quad}
\tag{4}
$$
证明是逐个数 (3) 中 $4j+1$、$4j+3$ 的 $p$ 进因子。
每个完整的 $p$ 区间中两者各出现一次；分母第一次在 $j=r-1$，
分子第一次在 $j=3r-1$。对于 $p^2$，分子第一次在
$j=(p^2-1)/4$，分母第一次在 $j=(3p^2-3)/4$。
$n<p^2$ 时没有更高层因子，故得 (4)。

特别地，$pW'$ 到次数 $p^2-1$ 均整。置
$$
C_p=p a_{r-1}\pmod p\in\mathbb F_p^\times.
$$
首个完整 $p$ 区间有以下精确式：
$$
\boxed{\quad
pW'(s)\equiv C_p s^{r-1}(1-s)^{2r-1}
                 \pmod{p,s^p}.
\quad}
\tag{5}
$$
这里多项式次数为 $3r-2<p$。证明也可直接代入 (3)：
$pW'$ 的约化满足齐次方程
$4s(1-s)g'+(3-5s)g=0$，显示的多项式满足它。
在次数小于 $p$ 的范围，系数递推只有 $s^{r-1}$ 一个自由项；
由该项 $C_p$ 固定全部系数。**这不是对全级数或任意次数的
多项式解唯一性的断言**；高次可以出现 $s^p$ 的任意函数因子。

(4) 还给出
$$
v_p([s^m]W)\ge-1\quad(1\le m<p^2),\qquad
v_p([s^{p^2}]W)=-2.
\tag{6}
$$
若 $p\nmid m$，前一不等式直接来自 (4)。若 $m=tp<p^2$，则
$m-1\bmod p=p-1$，第一层因子数差为零，除去 $m$ 后最低为 $-1$。
$m=p^2$ 时两层因子数差都为零，故赋值恰为 $-2$。
所以不能把 $W'$ 和 $W$ 的首次下一层分母混为一谈。

## 3. 指数运算先产生的真实下一进位

即使 $pW$ 的有关系数整，指数的阶乘仍会产生更早的分母。
对真实截面因子
$$
U(s)=e^{W(s)}=\vartheta^{68}
$$
有
$$
\boxed{\quad
U(s)^p=e^{pW(s)}
\text{ 在 }s^m,\ m<pr\text{ 处整},\qquad
p[s^{pr}]U(s)^p\equiv-\frac{C_p}{r}\pmod p.
\quad}
\tag{7}
$$
因此 $[s^{pr}]U^p$ 的赋值准确为 $-1$。本式是实际固定
$\vartheta$ 的恒等式，不是任意指数模型的实例。

证明如下。记 $H=pW$。由 (6)，$H$ 到次数 $pr$ 均整；
次数小于 $r$ 的系数在 $p\mathbb Z_p$ 中，而
$[s^r]H\equiv C_p/r$ 是单位。
对 $m\le pr$，在 $H^h$ 的任一 $s^m$ 单项中，至多
$\lfloor m/r\rfloor$ 个因子可以取单位系数，所以
$$
v_p([s^m]H^h/h!)
 \ge \max(h-\lfloor m/r\rfloor,0)-v_p(h!).
\tag{8}
$$
因 $h\le m\le pr<p^2$，$v_p(h!)=\lfloor h/p\rfloor$。
若 $m<pr$，(8) 对所有 $h$ 非负；在 $m=pr$ 时，
唯一可能出现 $-1$ 的项是 $h=p$ 且每个因子都取 $s^r$ 的单位项。
其他项均整。因此
$$
p[s^{pr}]e^H\equiv
 \frac{(C_p/r)^p}{(p-1)!}\equiv-C_p/r,
$$
最后使用 Wilson 定理。本计算没有漏掉指数中次数大于 $p$ 的项。

式 (5) 的首多项式作为 $\mathbb A^1_{\mathbb F_p}$ 上的一形式
$C_ps^{r-1}(1-s)^{2r-1}ds$ 不是非零有理函数的 $d\log$：
它没有有限极点、在无穷处有阶数大于一的极点，而有理 $d\log$
只有简单极点。这个事实仅说明此首进位不能直接换成一个有理单位
的对数；它既不是中央斜率的非零证明，也不是任何通用预算的不可能性证明。

## 4. 原整数流给出的全部列共同谱

在整数环
$$
\mathcal R=\mathbb Z[1/5][z,u,v,L,\theta]/(v^2-1+u^4)
$$
上采用原导子
$$
\delta z=1,\quad \delta u=v,\quad \delta v=-2u^3,\quad
\delta L=u^2,\quad \delta\theta=L\theta.
\tag{9}
$$
初值为 $(z,u,v,L,\theta)=(0,0,1,0,1)$。
$E_\theta=\theta\partial_\theta$ 与 $\delta$ 交换。
原源列 $A_2^bB^c$ 是 $\mathcal R$ 中不含 $L$ 的实际多项式，
$E_\theta$ 的特征值为 $68(b+c)$。所有 Hurwitz 导数因此均 $p$ 整。

在特征 $p$ 下，曲线 $v^2=1-u^4$ 的 Hasse 系数为零：
$(1-u^4)^{(p-1)/2}$ 没有 $u^{p-1}$ 项，因为 $p-1\equiv2\bmod4$。
故其不变导子满足 $\delta^p u=\delta^p v=0$。
这是不变导子的 $p$ 次幂与 Hasse 系数的标准等式，亦是 R24/R38
使用的同一 Cartier 规范。

令
$$
\mathfrak c_p=\delta^{p-1}(u^2)\in\mathbb F_p,\qquad
\mathfrak b=L^p+\delta^{p-1}L.
$$
第一个式子确实是常数。由
$$
\delta^2u^n=n(n-1)u^{n-2}-n(n+1)u^{n+2}
$$
知 $\delta^{p-1}u^2$ 是次数至多 $p+1$ 的偶多项式；其导数为零，
因而是 $u^p$ 的多项式。次数及偶性只允许常数。
第一阶 Bell／Jacobson 公式给出
$$
\boxed{\quad
\delta^p=\mathfrak c_p\partial_L+\mathfrak b E_\theta,\qquad
\delta\mathfrak b=\mathfrak c_p,\qquad
\partial_L\mathfrak b=0,\qquad \mathfrak b(O)=0.
\quad}
\tag{10}
$$
$\mathfrak b(O)=0$ 也直接来自 $\delta^{p-1}L=\delta^{p-2}u^2$
是 $v$ 乘一个奇次 $u$ 多项式。

该常数与第2节的规范准确相接：
$$
\boxed{\quad \mathfrak c_p=-C_p/(68r)\ne0.\quad}
\tag{11}
$$
确实，$s=z^4+O(z^8)$ 的所需换元系数在自然次数 $p+1<p^2$
处整（R54 的高度二对数界）。低于 $s^r$ 的 $W$ 系数整，故
$p[z^{p+1}]\log\theta=C_p/(68r)$。
另一方面 $\mathfrak c_p=(\log\theta)^{(p+1)}(0)$，
且 $(p+1)!/p\equiv-1\bmod p$，给出 (11)。

对原 $P\in\mathscr P_D$，记
$$
h_n(P)=\delta^n P(A_2,B)(O).
$$
由 (10) 及不含 $L$，对于每个 $n,j\ge0$ 得到
$$
\boxed{\quad
h_{n+j(p+1)}(P)
 \equiv \mathfrak c_p^{\,j}(n+1)^{\overline j}
                    h_n(E_\theta^jP)\pmod p.
\quad}
\tag{12}
$$
其中 $(n+1)^{\overline j}=(n+1)\cdots(n+j)$。
证明先将 $\delta^pP=\mathfrak b E_\theta P$ 再微分 $n+1$ 次；
因为 $\delta^2\mathfrak b=0$，在原点只留下
$\mathfrak c_p(n+1)h_n(E_\theta P)$。迭代时 $p+1\equiv1\bmod p$，
得到准确的上升阶乘。

因此 (12) 对所有原列同时成立。它并不是逐列分别选择的关系。

## 5. 真正同一条前缀行与净成本

写
$$
\prod_{q=0}^D(T-68q)=\sum_{j=0}^{D+1}\gamma_jT^j.
$$
若 $(n+1)^{\overline{D+1}}$ 是 $p$ 单位，则 (12) 给原整个源的行：
$$
\boxed{\quad
\sum_{j=0}^{D+1}
 \frac{\gamma_j\mathfrak c_p^{-j}}{(n+1)^{\overline j}}\,
 h_{n+j(p+1)}\in p\,\mathscr P_D^\vee.
\quad}
\tag{13}
$$
这里给 $\mathfrak c_p$ 任取单位提升；所得模 $p$ 行与提升无关。
最高项系数为单位，全部源列使用完全相同的系数。

取 $4\mid n$，令 $N=n+(D+1)(p+1)=4k$。
在原准确饱和前缀核上，(13) 的低阶项为零，因此
$$
h_N(P)\in p\mathbb Z_p,\qquad
v_p([w^k]P(A_2,B))\ge1-v_p(N!).
\tag{14}
$$
**显示出的 $v_p(N!)$ 必须保留。**
本文没有从 (13) 推出 $p^{v_p(N!)}$ 整除，也没有把这单层关系
重复应用于一个未经证明仍在原源格中的除 $p$ 对象。

还有一个可用的完整边界校准。由 (10) 中两个导子交换，
$\partial_L^p=0$、$E_\theta^p=E_\theta$，可得
$$
\delta^{p^2}=\mathfrak b^pE_\theta.
$$
$\delta\mathfrak b^p=0$ 且 $\mathfrak b(O)=0$，故
$$
h_n(P)\equiv0\pmod p\qquad(n\ge p^2)
\tag{15}
$$
对全部原列成立。本式仍只是一层整除；
$\mathfrak b^p/p$ 可沿原流成为整 Hurwitz 级数，并不因此成为原整
多项式环中的元素。若作下一次除 $p$，必须重新支付该格的比较。

## 6. 已冻结的原饱和格有限证书

[可复跑脚本](../scripts/check-theta-plane-saturated-jets.py) 与
[完整逐行数据](../scripts/check-theta-plane-saturated-jets.json)
使用 $P(s)e^{W(s)}$、$V(s)$ 的精确有理系数，列顺序是
$(j,c)$，$0\le c\le j\le D$。
每一行在当前核坐标中选择最小 $v_p$ 的列；其余列减去
$r_l/r_{\rm pivot}$ 倍的枢轴列。这些比值都在 $\mathbb Z_p$，
所以操作是原源上的整可逆变换，剩余列就是准确饱和核。
没有逐行乘阶乘或另改成 Hurwitz 源格。

所有以下记录都在 $k=0,\ldots,\binom{D+2}{2}-1$ 逐行增加秩。
表中的 $v_k$ 是评价理想的赋值，故局部对数范数是 $-v_k\log p$。

| $D$ | $p$ | 行数 | $\sum_kv_k$ | 最后一行 $v_k$ |
|---:|---:|---:|---:|---:|
| 4 | 7 | 15 | $-21$ | $-3$ |
| 4 | 11 | 15 | $-1$ | $1$ |
| 4 | 19 | 15 | $-9$ | $-2$ |
| 8 | 7 | 45 | $-356$ | $-17$ |
| 8 | 19 | 45 | $-126$ | $-6$ |
| 8 | 23 | 45 | $-104$ | $-5$ |
| 8 | 31 | 45 | $-78$ | $-4$ |

例如 $D=4,p=7$ 的 $k=10,11$ 两行分别为 $-3,-2$；
局部范数不按一个固定的逐阶阶乘斜率单调变化。
$p=11$ 的 $V$ 首系数不是单位，但本计算始终用首项为一的 $s$，
未据此作不合法的 $V$ 参数整等距。该条也只用于有限诊断。

这些精确值没有施加未证明的中央共同消失，不能当作反设下的
统一上下界。R159 平面所需的全精度目标仍为
$a_I+2b_I<2$；(5)、(7)、(13)、(15) 只提供真实进位和共同源行，
尚未给出该严格不等式。后续须利用原两中央条件与实际 amplitude
之间的关系，而不是删除非中央列或将中央投影当作乘法同态。

## 依赖

- R24、R38、R54：同一不变导子／Cartier 规范及高度二换元整性。
- R57：原固定整数 Hurwitz 流，本文 (9) 为同一流。
- [R162 固定方程与原矩阵](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)：
  原 $P,Q,W$；本文第2–5节的计数和进位由显示公式直接证明。
- R151、R158、R159：原饱和旗标的定义、共同前缀行及准确严格预算目标。
