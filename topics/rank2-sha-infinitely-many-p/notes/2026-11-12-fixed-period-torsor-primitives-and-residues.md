# 固定周期 torsor 上的真实临界原函数与闭形式检验

日期：2026-11-12。状态：固定有理微分模型、两类准确 prime
coefficient 接口、周期域识别、闭一形式障碍及整条原函数的
非 D-finite 性均已证明。指定 prime diagonal 的无穷非零性仍未证明。

本篇使用 [R66](../results/R66-full-weight-one-and-fixed-division-unit-model.md)
的实际固定 $M_1$ 与全权一 Borel，而不把半权 theta 的普通平方
当成中央对角。它给出一个素数变化前固定的代数环境；
该环境含周期坐标，不能直接当成模参数基底上的有限秩线性系统。

## 1. 准确的固定原函数

沿用

$$
s=1-4t^2,\qquad
sY''-8tY'-Y=0,\qquad
K(0)=1,\ K'(0)=0,\ L(0)=0,\ L'(0)=1.
\tag{1}
$$

Wronskian 为 $KL'-LK'=1/s$。置

$$
u=L/K,\qquad \frac{du}{dt}=\frac1{sK^2},\qquad
\mathcal B_1(u)=K(t(u))M_1(t(u))=\sum_{n\ge4}C_nu^n.
\tag{2}
$$

这里 $M_1=t^4+(7/2)t^6+\cdots$ 是固定有理代数 germ，
$C_n=0$ 除非 $4\mid n$。以下所有积分在原点取零常数。

### 1.1 惰性除 $p$ 正好是一个固定原函数的系数

定义

$$
\mathcal H_i(u)=\int_0^u\frac{\mathcal B_1(v)}{v^2}\,dv
 =\sum_{n\ge4}\frac{C_n}{n-1}u^{n-1}.
\tag{3}
$$

代入 (2) 得到准确恒等式

$$
\boxed{\quad
\frac{d\mathcal H_i}{dt}
  =\frac{M_1K}{sL^2}=:\beta_i,\qquad
[u^p]\mathcal H_i=\frac{C_{p+1}}p .
\quad}
\tag{4}
$$

因此同一固定 $\mathcal H_i$ 的指定 prime coefficient 就是
惰性首层目标；没有先为每个 $p$ 另选一个 Sym$^p$ 多项式。
在 $t$ 坐标中，令

$$
J=L/t,\qquad W_i=\frac{M_1K}{sJ^2},\qquad
(t\partial_t-1)Z_i=W_i,\quad [t]Z_i=0 .
$$

则

$$
\mathcal H_i(t)=Z_i(t)/t.
\tag{5}
$$

这也准确连接 R66/R68 的 Euler 原函数。
在原点，$\beta_i=t^2+O(t^4)$、
$\mathcal H_i=t^3/3+O(t^5)$，所以 (4) 的 apparent pole
在那里被 $M_1$ 的四阶零点消去。

另一个较简单的固定 Euler 原函数是

$$
\mathcal H_e(u)=\int_0^u\frac{\mathcal B_1(v)}v\,dv,
\qquad
\boxed{\quad \frac{d\mathcal H_e}{dt}
=\frac{M_1}{sL}=:\beta_e .\quad}
\tag{6}
$$

它从 $t^4/4$ 开始。

### 1.2 普通的第二除 $p$ 也有固定的两步原函数

定义

$$
\mathcal E(u)=\int_0^u\mathcal B_1(v)\,dv,\qquad
\mathcal H_o(u)=\int_0^u\frac{\mathcal E(v)}v\,dv.
\tag{7}
$$

则完全准确有

$$
\mathcal E'=\frac{M_1}{sK},\qquad
\mathcal H_o'=\frac{\mathcal E}{sKL},\qquad
\mathcal H_o(u)=
 \sum_{n\ge4}\frac{C_n}{(n+1)^2}u^{n+1}.
\tag{8}
$$

特别

$$
\boxed{\quad [u^p]\mathcal H_o=\frac{C_{p-1}}{p^2}
       \qquad(p\equiv1\pmod4).\quad}
\tag{9}
$$

这些是同一固定有限维代数环境上的有理偏连接方程；
没有借 (7) 宣称已经得到一个基底上固定秩的 absolute flat
connection，或宣称 (9) 无穷次非零。

## 2. 实际周期域与固定代数 torsor

取一个固定复代数曲线覆盖，使 $M_1$ 单值，记其函数域为 $k$。
$k/\mathbb C(t)$ 有限。允许再扩大这个固定代数覆盖；
下述结论在每一个这样的覆盖上仍成立。

引入独立坐标 $K,L,Q,R$，并考虑

$$
X:\quad KR-LQ=1/s .
\tag{10}
$$

这是基底上一个行列式已固定的 $\operatorname{SL}_2$ torsor。
实际解对应 $Q=K'$、$R=L'$。其 GM 向量场是

$$
\begin{aligned}
\delta(t)&=1,& \delta(K)&=Q,&\delta(L)&=R,\\
\delta(Q)&=(K+8tQ)/s,&
\delta(R)&=(L+8tR)/s .
\end{aligned}
\tag{11}
$$

(11) 保持 (10)，因两边的导数都是 $8t/s^2$。
$\beta_i,\beta_e$ 由 (4)、(6) 现在成为 $k(X)$ 中的有理函数。
方程 $\delta\mathcal H_i=\beta_i$ 等正是沿这个固定向量场的
有理偏连接；$L\ne0$ 是其自然开集。

### 2.1 需要的 monodromy 可以直接核实

写 $\lambda=1/2+t$，(1) 等价于

$$
\lambda(1-\lambda)y''+(1-2\lambda)y'-\tfrac14y=0.
\tag{12}
$$

在 $\lambda=0$，唯一归一解析解为

$$
f_0(\lambda)=\sum_{n\ge0}
\frac{\binom{2n}{n}^2}{16^n}\lambda^n,\qquad f_0(0)=1 .
$$

reduction of order 给第二解

$$
f_0(\lambda)\int
\frac{d\lambda}{\lambda(1-\lambda)f_0(\lambda)^2}.
\tag{13}
$$

被积函数在 $0$ 的留数是 $1$，所以局部 monodromy 为非平凡
unipotent，固定线为 $\mathbb C f_0$。在 $\lambda=1$ 同理，
固定线为 $\mathbb C f_1$，其中 $f_1(\lambda)=f_0(1-\lambda)$。
两线不同：例如

$$
f_0(\lambda)=\frac2\pi
\int_0^{\pi/2}(1-\lambda\sin^2\theta)^{-1/2}\,d\theta
$$

在 $\lambda\to1^-$ 时有非零的对数发散，而 $f_1$ 在那里解析且
取值 $1$。该对数发散可在 $\theta=\pi/2$ 附近与
$((1-\lambda)+(\pi/2-\theta)^2)^{-1/2}$ 比较得到；
也可核对 NIST DLMF（2010–2026），
[19.12.1](https://dlmf.nist.gov/19.12.E1)。
(12) 与其局部指数亦见
[15.10.1](https://dlmf.nist.gov/15.10.E1)。

Wronskian 单值，故 monodromy 行列式为 $1$。
两个非平凡 unipotent 的固定线不同，其 Zariski 闭包为
$\operatorname{SL}_2$：一个 unipotent 的整数幂在其一参数根群中
Zariski 稠密；将两个 nilpotent 的固定线放到不同直线后，
其 Lie 代数及括号生成 $\mathfrak{sl}_2$。

通过一个固定有限代数覆盖只把 monodromy 换成有限指数子群。
每个上述 unipotent 的某个正整数幂仍属于该子群，其固定线不变；
所以 Zariski 闭包依然为 $\operatorname{SL}_2$。

### 2.2 没有额外的周期代数关系

实际代入给出的同态

$$
k[K,L,Q,R]/(KR-LQ-1/s)
\longrightarrow \{\text{实际周期的多值亚纯函数}\}
\tag{14}
$$

是单射。直接证明如下。若有一个额外的多项式关系，沿固定覆盖
上的闭路延拓会使同一个关系在 $Yg$ 上成立，其中

$$
Y=\begin{pmatrix}K&L\\Q&R\end{pmatrix}
$$

而 $g$ 遍历 Zariski 稠密的 monodromy 群。
在一般的基点，$Yg$ 因而遍历行列式为 $1/s$ 的矩阵的
Zariski 稠密集，关系只能属于行列式理想。
对一般基点逐点作此论证，系数函数也必须如此，得到 (14)。
因此实际周期域正是 (10) 的函数域，没有在余下论证中把
$K,Q$ 错当成独立而忽略一个实际关系。

## 3. 沿 $L=0$ 的准确留数

在 $X$ 的除子 $D:L=0$ 的一般点，(10) 给

$$
R=\frac1{sK}\ne0.
\tag{15}
$$

所以 $\delta$ 横截 $D$，$K,Q$ 在
$k(D)=k(K,Q)$ 中独立。这里的留数是以下意义：
若一个有理函数的主部为 $c\,\delta L/L$，它作为
沿 $\delta$ 的一形式的 residue 是 $c|_D$。

对简单极点函数 $\beta_e=M_1/(sL)$，准确有

$$
\boxed{\quad \operatorname{res}_D(\beta_e)=M_1K.\quad}
\tag{16}
$$

对 $\beta_i$，先作明确的 Hermite 约化

$$
q_0=-\frac{M_1K^2}{L},\qquad
\delta q_0=
\beta_i-\frac{M_1'K^2+M_1KQ}{L}.
\tag{17}
$$

所以去掉唯一可能的双极 exact 主部后，简单留数为

$$
\boxed{\quad
\operatorname{res}_D(\beta_i-\delta q_0)
 =sK^2(M_1'K+M_1Q).
\quad}
\tag{18}
$$

(16) 因 $K$ 变量而非恒定；(18) 中 $Q$ 的系数
$sM_1K^2$ 非零，所以也非恒定。$M_1$ 在特定 CM 基点有零，
并不使它在一般的 $D$ 上成为零。

普通第一原函数的 $\beta_+=M_1/(sK)$ 同样有准确检验：
沿 $D_+:K=0$，$\delta K=Q=-1/(sL)$，故
$\operatorname{res}_{D_+}(\beta_+)=-M_1L$，也非恒定。

## 4. 不能把这条偏连接直接改称普通闭 Kummer 形式

**命题。** 在 $X$ 上不存在闭的有理一形式 $\alpha$，满足
$\alpha(\delta)=\beta_e$、$\beta_i$ 或 $\beta_+$ 中的任何一个。

**证明。** 在 $D$ 一般点附近用 $L$ 作横向坐标，其他坐标可取
$t,K,Q$。一个闭有理一形式的 Laurent 极部总可写为

$$
dq+c\,\frac{dL}{L},\qquad c\in\mathbb C,
\tag{19}
$$

剩余部分沿 $D$ 正则。为完整核对 (19)，先将 $dL$ 分量中
$L^m$、$m\le-2$ 的系数逐项积分，减去相应的 $dq$。
剩下的 $dL/L$ 系数必须沿 $D$ 为常数：闭性要求其对
$t,K,Q$ 的各导数为零，而一个 Laurent 级数的 $L$ 导数没有
非零的 $L^{-1}$ 项。闭性同时迫使其余坐标分量不再有负次项。
于是得到 (19)。

因 $\delta L$ 在 $D$ 为单位，若 $q$ 有 $m$ 阶极点，
$\delta q$ 就有 $m+1$ 阶极点，首项不能消失。
对于 $\beta_e$ 的简单极点，$q$ 因而没有极部。
(19) 要求 residue 是常数 $c$，与 (16) 矛盾。

对于 $\beta_i$ 的双极点，$q$ 至多有简单极点，
匹配双极首项唯一强迫其极部为 (17) 的 $q_0$。
余下简单 residue 必须等于 (19) 的常数 $c$，
又与 (18) 矛盾。对于 $\beta_+$，沿 $K=0$ 的简单留数
$-M_1L$ 给出同样矛盾。$\square$

### 4.1 有限代数扩张中的 exact 加常系数对数也不能解决

设 $F=k(X)$、$F'/F$ 有限。假若在 $F'$ 中存在

$$
\beta=\delta g+\sum_j c_j\frac{\delta f_j}{f_j},
\qquad c_j\in\mathbb C,\quad f_j\ne0,
\tag{20}
$$

其中 $\beta$ 是上述任一个函数，取 trace 得

$$
[F':F]\beta
=\delta\operatorname{Tr}(g)
+ \sum_j c_j\,\frac{\delta\operatorname{Norm}(f_j)}
                         {\operatorname{Norm}(f_j)}.
\tag{21}
$$

特征零保证导数延拓唯一，并与 trace/norm 的相应恒等式相容。
右端来自 $F$ 上的闭有理一形式，违反上面的命题。
同理，任意有限代数扩张上的闭一形式都可用微分形式的 trace
降回，因而也不能给这样的 contraction。

该结论的范围是具体的 rank-two additive/Kummer 闭形式接口。
它不排除带非平凡 GM 系数的更高 extension，不排除继续使用
固定 torsor 上的有理偏连接，也不排除指定 prime coefficient
另有较小的几何实现。

## 5. 整条固定原函数仍不能下降为基底的有限秩线性系统

**命题。** $\beta_i,\beta_e,\beta_+,\mathcal H_i,\mathcal H_e,
\mathcal E,\mathcal H_o$ 都不满足任何固定有限代数扩张
$k/\mathbb C(t)$ 上的非零有限阶齐次线性微分方程。

**证明。** 在 §2 的有限指数 monodromy 群中，选一个不保持
$L$ 线的非平凡 unipotent $\gamma=I+N$。
它的整数幂作用后，第二个周期为

$$
L_n=(K\ \ L)\gamma^n e_2,\qquad
\gamma^n e_2=e_2+nNe_2.
$$

因为该 unipotent 不保持 $L$ 线，$e_2,Ne_2$ 独立。
故不同整数 $n$ 给出的 $L_n$ 两两不成比例。
对应的第一个周期记 $K_n$；$K_n,L_n$ 独立且行列式仍为 $1/s$。
固定覆盖使 $M_1$ 单值，所以延拓分支准确是

$$
\beta_{e,n}=\frac{M_1}{sL_n},\qquad
\beta_{i,n}=\frac{M_1K_n}{sL_n^2}.
\tag{22}
$$

在 torsor 上，(22) 分别沿不同的素除子 $D_n:L_n=0$ 有真实的
简单极点或双极点。分子在一般的 $D_n$ 不消失。
任意有限 $k$-线性关系中，取一个系数非零的 $n$，
沿仅属于该项的一般极点观察，即知该系数必须为零。
因此两族分支各自线性独立。

由 (14)，这些 torsor 函数的线性独立也是实际亚纯分支的
线性独立。若 $\beta_e$ 或 $\beta_i$ 满足 $k$ 上阶数 $d$ 的
线性方程，它们所有延拓分支在一个普通点处应位于至多 $d$ 维
的复解空间中，矛盾。
所用路径可以避开系数的有限奇点以及沿途的离散极点；
删去这些点不会去掉上述 cusp unipotent 的适当幂。

若 $\mathcal H_i$ 或 $\mathcal H_e$ 满足有限阶线性方程，
其导数也属于一个有限维微分模，于是 $\beta_i$ 或 $\beta_e$
也满足这样的方程，仍矛盾。积分延拓可能增加常数，不影响
这个导数论证。

对于 $\beta_+$，改选不保持 $K$ 线的 cusp unipotent，
由不同的 $K_n=0$ 极点得到同样的分支线性独立性。
所以 $\beta_+$ 和其原函数 $\mathcal E$ 也非 D-finite。
最后若 $\mathcal H_o$ 是 D-finite，则其导数是 D-finite；
$K,L$ 各自满足 (1)，而 D-finite 函数对有限乘积封闭，
故由 (8)
$\mathcal E=sKL\,\mathcal H_o'$ 也会是 D-finite，矛盾。
这个反推只使用已知 D-finite 的 $K,L$，没有使用
“非 D-finite 因子的乘积仍非 D-finite”这一错误推理。$\square$

这里的系数域是模参数的固定**代数**扩张 $k$。
在含周期的 $F$ 中，$\delta\mathcal H_i=\beta_i$ 本来就是一个
一阶非齐次偏连接，不能把两种系数域混在一起。

## 6. 对下一步实际研究保留的接口

(4)、(9) 把两类首层证书都放回了素数变化前固定的原函数，
其系数、参考周期和所有除 $p$ 因子完全准确。
这可以用来研究真实 arithmetic jets、沿 GM 的偏连接或
带非平凡系数的相对 Frobenius。

(16)–(21) 解释了为何一个普通闭有理一形式/固定单位对数
不能直接给出这些原函数；(22) 解释了为何整条序列不是基底上
固定有限秩线性方程的解。
这些范围结论不计算 (4)、(9) 指定系数的值。
当前仍须从实际 $M_1$、除法单位及完整 Frobenius/模数关系中，
得到对无穷多个素数足够的非零约束。
