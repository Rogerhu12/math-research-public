# R64. 实际临界对角的 Gauss–Manin 与 Legendre 提升

日期：2026-11-12。**状态：准确对角公式及模平方提升已证明；无穷次非零尚未证明。**

使用 $E_0:y^2=x^3-x$ 上实际次数十七截面
$A_1(z)=\sum\beta_mz^m=z^4+(97/60)z^8+\cdots$。
原曲线 $E_{17}$ 的第 $4r$ 系数为 $17^{r-1}\beta_{4r}$，
故所有目标惰性素数的非零判据保持不变。

## 1. 固定代数模函数和两条准确周期解

R53 的实际半权热族为
$$
F(\tau)=\sum_{17\nmid n}\lambda(n)\zeta_{289}^{19n^2}
                   e^{\pi i\tau n^2/289},\qquad \lambda(3)=-i.
$$
令 $t=\lambda_{\rm Leg}-1/2$，其中 $\lambda_{\rm Leg}=\vartheta_2^4/\vartheta_3^4$。
这里的 $t$ 是模参数。将 $F/\vartheta_3$ 在 $\tau=i$ 附近的 germ
除以其非零二阶系数，得到固定偶函数
$$
M(t)=t^2+O(t^4),\qquad M\in\mathbb Q(i)[[t^2]],
$$
且 $M$ 代数于 $\mathbb Q(i)(t^2)$。有限 theta 变换矩阵给模函数的
代数性；定义域由下述无周期尺度及实际 $\beta_m\in\mathbb Q$ 得到。

令 $K,L$ 为同一个 Picard–Fuchs 方程
$$
\mathscr D y=(1-4t^2)y''-8ty'-y=0
$$
的解，初值分别为 $(1,0)$、$(0,1)$。准确有
$$
K={}_2F_1(1/4,1/4;1/2;4t^2),\quad
L=t\,{}_2F_1(3/4,3/4;3/2;4t^2),\quad
u=L/K,
$$
$$
u'=\frac1{(1-4t^2)K^2}.
$$
定义 $\mathcal B(u)=K(t(u))^{1/2}M(t(u))=\sum C_Nu^N$。
Cayley 坐标、热算子及准确实周期比较给
$$
\boxed{\beta_{2N}=12\bigl(2(4+i)^2\bigr)^{N-2}
                    \frac{N!}{(2N)!}C_N.}
\tag{1}
$$
参考平方根取常数项一；没有将其视为一个固定有限秩线性模块的分量。
根端复跑[独立 Arb 脚本](../scripts/check-gm-halfweight-calibration.py)：
从原 Gaussian 热族与独立 theta jets 反解模参数，给
$(4+i)^4C_4/35=97/60$，严格误差小于 $10^{-250}$。
这检查非首项尺度；(1) 的证明本身来自准确恒等式。

## 2. 必须保留除 p 的实际行

置 $J=L/t$、$W=M/((1-4t^2)J^{3/2})$。
对于 $p\equiv3\pmod4$、$N=(p+1)/2$，留数换元给特征零恒等式
$$
\boxed{C_N=[t^N]W(K/J)^{p/2}.}
\tag{2}
$$
去掉固定代数 germ $M$ 的有限坏素数集合后，所需截断全部 $p$ 整，
且每个对数或指数分母都小于 $p$，所以
$$
C_N\equiv[t^N]W+\frac p2[t^N]W\log(K/J)\pmod{p^2}.
\tag{3}
$$
由实际 $\beta_{p+1}$ 整及 (1)，$p\mid C_N$，也有 $p\mid[t^N]W$。
准确首层判据为
$$
\boxed{\beta_{p+1}\equiv
-12\bigl(2(4+i)^2\bigr)^{N-2}N!
\left(\frac{[t^N]W}{p}+\frac12[t^N]W\log(K/J)\right)\pmod p.}
\tag{4}
$$
前因子为单位。仅有 (3) 的模 $p$ 零式不够；$(p+1)!$ 中的唯一一个 $p$
必须保留到模平方计算后再除。

还可定义固定级数
$$
(2t\partial_t-1)Z=W,\qquad
\mathcal G=Z+\tfrac12W\log(K/J),
$$
使 (4) 的括号准确为 $[t^N]\mathcal G$。
这是固定代数覆盖、固定秩二周期数据及明确原函数的接口；
不由此断言整条 $\mathcal G$ 为 D-finite。

## 3. 所需模平方参考有显式 Legendre 表达式

令 $n=(p-1)/2$，为奇数，并取
$$
\widetilde L_p(t)=\frac{P_n(2t)}{2P_n'(0)}.
$$
分母是 $p$ 进单位，且准确有
$$
\mathscr D\widetilde L_p=-p^2\widetilde L_p.
\tag{5}
$$
其模 $p$ 是以 CM 根导数正规化的 Hasse 多项式。
另一条解取
$$
\widetilde K_p(t)=Q_n^{\rm Leg}(2t)/Q_n^{\rm Leg}(0),
$$
其中
$$
Q_n^{\rm Leg}(x)=\tfrac12P_n(x)\log\frac{1+x}{1-x}
 -\sum_{k=1}^n\frac1kP_{k-1}(x)P_{n-k}(x).
$$
它同样满足 (5)，且初值为 $(1,0)$。
因为所需系数递推的分母均为 $p$ 进单位，
$$
\widetilde L_p/t\equiv J\pmod{p^2,t^{N+1}},\qquad
\widetilde K_p\equiv K\pmod{p^2,t^{N+1}}.
\tag{6}
$$
所以 (3)–(4) 的全部参考可用显式 Legendre 多项式与唯一的
$\log((1+2t)/(1-2t))$ 计算，仍保留除 $p$ 后的准确值。
次数 $n$ 随 $p$ 增长，(5) 的水平提升也没有自动等同于 crystalline Frobenius。

证明全文、Hasse 的准确次数范围、坏素数范围和全部尺度见
[临界 Gauss–Manin 与 Legendre 提升](../notes/2026-11-12-critical-gauss-manin-legendre-lift.md)。
下一缺口是将 (4) 识别为固定覆盖上的实际相对 Frobenius/Bockstein 评价，
并证明指定向量的值对无穷多个 $p$ 非零。


## 4. 两条周期的全系数分母与真正目标级数

对 $J$ 的超几何系数逐 $p^a$ 计数，可以严格证明其首个非整项在
$t^{p^2+p}$，赋值 $-1$；第一 Newton 斜率为 $1/(p^2+p)$。
其最近的 $p^2+p$ 个零点均单，半径恰 $p^{-1/(p^2+p)}$。
所以在前述有限坏位之外，固定 $W$ 的首坏项是 $t^{p^2+p+2}$，
且其收敛半径恰为这个更大的半径。

但实际需要的是 $\mathcal G=Z+\tfrac12W\log(K/J)$。
$K$ 的首坏项为 $t^{p+1}$，而临界 $W_{(p+1)/2}\in p\mathcal O_p$
只消去 $Z$ 在该处的一次分母。完整比较得
$$
[t^n]\mathcal G\text{ 整 }(n<p+3),\qquad
p[t^{p+3}]\mathcal G\equiv\tfrac12p[t^{p+1}]K\ne0\pmod p.
$$
因此周期部分的 $p^2$ 级整性收益已真实获得，但不能将其直接移给
目标全部对数组合。指定更低对角 $[t^{(p+1)/2}]\mathcal G$ 的非零性仍未证明。
逐项计数、零点与首坏项的完整证明见
[GM 周期的准确分母](../notes/2026-11-12-gauss-manin-period-denominators.md)。
