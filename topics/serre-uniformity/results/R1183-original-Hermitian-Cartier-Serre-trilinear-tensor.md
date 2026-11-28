# R1183 — 原 Hermitian Cartier–Serre 三张量及 Fermat 六次覆盖的准确限制

**状态：已证明。** 日期：2026-11-28。本文给出一个实际光滑曲线上的完整张量，不从有限酉群的等变性推断代数群等变性。它没有证明原 $e,K_4$ 不同时为零。

## 1. 原对象与完整正则基

令 $p\ge5$ 为奇素数，$K=\mathbf F_{p^2}$，并置
$$
\mathscr H:\quad X^{p+1}+Y^{p+1}=Z^{p+1},\qquad n=p-2.
\tag{1183.1}
$$
这是光滑射影 Hermitian 曲线，次数为 $p+1$、亏格为 $p(p-1)/2$。在 $Z=1$ 图中仍记坐标为 $X,Y$，并取
$$
\Omega=\frac{dX}{Y^p},\qquad
D=Y^p\partial_X-X^p\partial_Y.
\tag{1183.2}
$$
这里 $D$ 是函数域中满足 $df=(Df)\Omega$ 的实际导子；它不是在无约束二元多项式环之外另行假设的微分方程。曲线关系给 $DX=Y^p,DY=-X^p$，故在 $K(\mathscr H)^p$ 上它是常系数导子，且
$$
t=\frac{X}{Y^p},\qquad dt=\Omega,\qquad Dt=1,\qquad D^p=0.
\tag{1183.3}
$$
最后一式也可直接由 $D^pX=D^pY=0$ 得到。

对正整数 $a,b,c$，$a+b+c=p+1$，取
$$
\omega_{a,b}=X^{a-1}Y^{b-p-1}\,dX
=X^{a-1}Y^{b-1}\Omega.
\tag{1183.4}
$$
这些是完整正则基。等价地，令 $V_n=K[X,Y,Z]_n$，由
$$
f\longmapsto f(X,Y,1)\Omega
\tag{1183.5}
$$
把 $V_n$ 与 $H^0(\mathscr H,\Omega^1)$ 识别。为核实际极界，在 $Y=0$ 可改写 $\Omega=-dY/X^p$；在任一无穷点 $\Omega$ 的零阶为 $p-2$。因此总次数至多 $n$ 的所有仿射多项式都给正则微分，其维数也正是 $p(p-1)/2$。

## 2. 原有理 primitive、Cartier 零性与 Serre 对角

每条 (1183.4) 有完整有理 primitive
$$
P_{a,b}=Y^{-bp}
\sum_{j=0}^{b-1}
\frac{(-1)^j\binom{b-1}{j}}{a+j}
X^{a+(p+1)j},\qquad dP_{a,b}=\omega_{a,b}.
\tag{1183.6}
$$
确实，$Y^{b-p-1}=Y^{-bp}(1-X^{p+1})^{b-1}$，且整数指数的导数 $a+(p+1)j$ 在特征 $p$ 中正是 $a+j$。所有分母都在 $1,\ldots,p-1$ 中，因为 $a+j\le a+b-1\le p-1$。所以全部正则微分的 Cartier 都为零。

定义绝对 Cartier 配对
$$
\beta_{\mathscr H}(\alpha,\beta)=C_{\rm abs}(P_\alpha\beta).
\tag{1183.7}
$$
它与 primitive 的选择无关，输出正则，且在前两输入交替。这些性质直接来自局部正则 primitive：两个选择之差为 $p$ 次幂，而第二输入的 Cartier 为零。

沿 exact 序列 $0\to\mathcal O\xrightarrow{F}\mathcal O\xrightarrow d B^1\to0$，取连接
$$
\mathfrak k:H^0(\mathscr H,\Omega^1)\longrightarrow H^1(\mathscr H,\mathcal O).
$$
它在绝对写法中对标量取一次 $p$ 次根。采用原 Fermat 六次笔记 §11.1 的 Čech 约定：一个有理 primitive 的 $p$ 次根主部表示 $\mathfrak k$。相反的共同 Čech 约定只使本文的整个三张量共同变号。

置
$$
r_{a,b}=\sum_{j=0}^{b-1}\frac{(-1)^j\binom{b-1}{j}}{a+j}
=\frac{(a-1)!(b-1)!}{(a+b-1)!}\in\mathbf F_p^\times.
\tag{1183.8}
$$
中间有限和是 $\int_0^1 T^{a-1}(1-T)^{b-1}\,dT$ 的有理恒等式；其所有阶乘指标小于 $p$。

$P_{a,b}$ 只在 $Y=0$ 的 $p+1$ 个点有极。在无穷点，其最后一项的阶为 $p+1-a-b=c>0$，其余项更高。在 $(X,Y)=(\xi,0)$，$\xi^{p+1}=1$，所有 Laurent 指数属于 $-bp+(p+1)j$。由于 $dP_{a,b}$ 正则，负指数必须被 $p$ 整除；负部范围内 $0\le j<b<p$，故仅有 $j=0$。于是准确主部及其 $p$ 次根是
$$
(P_{a,b})_{\rm pp}=r_{a,b}\xi^aY^{-bp},\qquad
L_{a,b}=r_{a,b}\xi^{-a}Y^{-b}.
\tag{1183.9}
$$
这里使用了 $\xi^p=\xi^{-1}$，没有把绝对 Cartier 当作对 $K$ 线性。

再由 $\omega_{d,e}=-X^{d-p-1}Y^{e-1}\,dY$，逐点取留数并对全部 $p+1$ 个 $\xi$ 求和，得到
$$
\boxed{\quad
\langle\mathfrak k(\omega_{a,b}),\omega_{d,e}\rangle_{
\rm Serre}
=-r_{a,b}\,\mathbf1_{a=d,\ b=e}.
\quad}
\tag{1183.10}
$$
这也直接支付 $\mathfrak k$ 的非退化性。若 $i=a-1,j=b-1,l=c-1$，则 $i+j+l=n$，Wilson 给出另一个便于后面使用的准确写法：
$$
-r_{a,b}=(-1)^l i!j!l!.
\tag{1183.11}
$$

## 3. 不用表示论的完整 Cartier 微分公式

对任意函数 $h$，由 (1183.3) 的实际 $p$-基 $t$ 有
$$
C_{\rm abs}(h\Omega)=(-D^{p-1}h)^{1/p}\Omega.
\tag{1183.12}
$$
例如将 $h$ 唯一写成 $\sum_{j=0}^{p-1}h_j^p t^j$，两边都是 $h_{p-1}dt$。

令 $f,g\in V_n$，以下在 $Z=1$ 代入。由于 $D$ 的系数为 $p$ 次幂，完整展开中只对原多项式作普通偏导，各 $p$ 次幂系数的导数为零；原多项式次数至多 $p-2$，故 $D^{p-1}g=0$。对 $DP_f=f$ 使用完整 Leibniz 公式，得到
$$
\boxed{\quad
\left(\frac{\beta_{\mathscr H}(f\Omega,g\Omega)}{\Omega}\right)^p
=\sum_{j=0}^{n}(-1)^j D^jf\,D^{n-j}g.
\quad}
\tag{1183.13}
$$
首项 $P_fD^{p-1}g$ 确为零；其余系数只用了
$\binom{p-1}{j}=(-1)^j$。所以本式没有省掉一个尚未受控的 primitive 或主部。

取任意线性式 $\ell,m$ 的系数在 $K$ 中，并置
$f=\ell^n,g=m^n$。记 $c=\ell\times m$ 为两个系数行向量的叉积。
由于 $n!=(p-2)!=1$ 于 $K$，(1183.13) 的二项式求和准确为
$$
\sum_{j=0}^n(-1)^jD^j(\ell^n)D^{n-j}(m^n)
=(\ell\,Dm-m\,D\ell)^n
=(c_X X^p+c_Y Y^p-c_Z)^n.
\tag{1183.14}
$$
最后一步使用的是实际曲线关系 $XX^p+YY^p=1$。因此
$$
\boxed{\quad
\beta_{\mathscr H}(\ell^n\Omega,m^n\Omega)
=(c_X^{1/p}X+c_Y^{1/p}Y-c_Z^{1/p})^n\Omega.
\quad}
\tag{1183.15}
$$
第三坐标的负号来自 (1183.1) 的负 $Z^{p+1}$，不是可省的相位。

## 4. 完整 Cartier–Serre 三张量等于行列式微分

定义
$$
\mathscr T_{\mathscr H}(f,g,h)
=\langle\mathfrak k(\beta_{\mathscr H}(f\Omega,g\Omega)),
h\Omega\rangle_{\rm Serre}.
\tag{1183.16}
$$
绝对 Cartier 对前两槽各取一次 $p$ 次根，$\mathfrak k$ 再取一次。由于底域是 $\mathbf F_{p^2}$，这个复合在前两槽线性；第三槽本来线性。因此 (1183.16) 是本来就定义在 $V_n$ 上的 $K$-三线性张量。

把 (1183.15) 代入 (1183.10)–(1183.11)，第二次 $p$ 次根使 $c^{1/p^2}=c$，而 Serre 对角中的 $(-1)^l$ 与 (1183.15) 第三坐标的负号相消。对任意三个线性式得到
$$
\boxed{\qquad
\mathscr T_{\mathscr H}(\ell^n,m^n,h^n)
=\det(\ell,m,h)^n.
\qquad}
\tag{1183.17}
$$

为把这写成完整公式，给三份变量分别标号 $1,2,3$，置
$$
\mathscr D=
\det\begin{pmatrix}
\partial_{X_1}&\partial_{Y_1}&\partial_{Z_1}\\
\partial_{X_2}&\partial_{Y_2}&\partial_{Z_2}\\
\partial_{X_3}&\partial_{Y_3}&\partial_{Z_3}
\end{pmatrix}.
$$
则对所有 $f_1,f_2,f_3\in V_n$，
$$
\boxed{\quad
\mathscr T_{\mathscr H}(f_1,f_2,f_3)
=\mathscr D^{p-2}
\bigl(f_1(X_1,Y_1,Z_1)f_2(X_2,Y_2,Z_2)
f_3(X_3,Y_3,Z_3)\bigr).
\quad}
\tag{1183.18}
$$
右侧是常数。确实，纯 $n$ 次幂张成 $V_n$，因为 $n!$ 为单位；两侧在纯幂上分别是 (1183.17) 与 $(n!)^3\det(\ell,m,h)^n$，而 $(n!)^3=1$。

特别地，$n$ 为奇数，故该原三张量完全交替。它的全空间 radical 为零：对任意 $f\in V_n$，(1183.18) 给
$$
\mathscr T_{\mathscr H}(f,\ell^n,m^n)=f(\ell\times m).
\tag{1183.19}
$$
叉积取遍 $K^3$；若一个次数 $n<p^2$ 的多项式在 $K^3$ 全部为零，则它为零。也可扩到代数闭包后只作右侧多项式的代数论证。这里的 radical 结论只针对 Hermitian 曲线的**全部** $p(p-1)/2$ 维 Hodge 空间。

证明没有把有限 $\operatorname{SU}_3(\mathbf F_p)$ 的不变性提升成 $\operatorname{SL}_3$ 的不变性；完整行列式来自 (1183.6)、(1183.13) 和实际留数。

## 5. 回到原 Fermat 六次曲线：degree、trace 与原 e 槽

现限定 $p=6k-1\ge41$，取原实际曲线
$$
Z_6:\quad x^6+y^6=1,\qquad
\omega^{(6)}_{a,b}=x^{a-1}y^{b-6}\,dx.
$$
原覆盖是
$$
\pi:\mathscr H\longrightarrow Z_6,\qquad
(X:Y:Z)\longmapsto(X^k:Y^k:Z^k).
\tag{1183.20}
$$
它是可分 degree $k^2$ 的态射：在一般点有两个独立的 $k$ 次根选择，且 $p\nmid k$。不能把它误算为 degree $k$，也不能把三个 genus 4 子空间当作直和。

若 $a,b,c\ge1,a+b+c=6$，则完整原微分拉回为
$$
\boxed{\quad
\pi^*\omega^{(6)}_{a,b}
=kX^{ak-1}Y^{bk-1}Z^{ck-1}\Omega.
\quad}
\tag{1183.21}
$$
在 $Z=1$ 直接代入 $dx=kX^{k-1}dX$ 即得，$6k=p+1$ 保证两个 $Y$ 指数完全相同。

$\beta$ 与可分拉回相容，连接 $\mathfrak k$ 与拉回相容，Serre trace 复合为 degree $k^2$。因此对三个原微分有准确的、未经平均的关系
$$
\mathscr T_{\mathscr H}(\pi^*\alpha,\pi^*\beta,\pi^*\gamma)
=k^2\mathscr T_{Z_6}(\alpha,\beta,\gamma).
\tag{1183.22}
$$
置 $f_{abc}=X^{ak-1}Y^{bk-1}Z^{ck-1}$，由 $K$-三线性和 (1183.21) 得到
$$
\boxed{\quad
\mathscr T_{Z_6}(\omega^{(6)}_{a,b},\omega^{(6)}_{d,e},
\omega^{(6)}_{g,h})
=k\,\mathscr D^{p-2}(f_{abc}\,f_{def}\,f_{ghi}),
\quad}
\tag{1183.23}
$$
右侧三个因子各用自己的三份变量。这里剩余的因子是 $k^3/k^2=k$，不能省掉 trace 的 $k^2$。

与原 Fermat 六次笔记 §6、§11 的同一 $b_0,c,v,e,\delta$ 规范比较，
$$
\beta_{Z_6}(\omega^{(6)}_{2,2},\omega^{(6)}_{1,2})
=-c^{2k-1}\frac e\delta\,\omega^{(6)}_{3,2}.
$$
左侧及所用 Fermat 基都定义在 $\mathbf F_p$，故准确系数 $-c^{2k-1}e/\delta$ 本身在 $\mathbf F_p$；连接 $\mathfrak k$ 的另一次 $p$ 次根不会再改变它。若 $r^{(6)}_{3,2}$ 是该笔记 (G4.61) 的原单位，则 (G4.64) 与 (1183.23) 给
$$
\boxed{\quad
e=\frac{k\delta}{6r^{(6)}_{3,2}c^{2k-1}}
\,\mathscr D^{p-2}(f_{222}f_{123}f_{321}).
\quad}
\tag{1183.24}
$$
这确实是原 $e$，没有改成辅助 theta、不同 Picard 方向或未指定的 polarization。

## 6. 已付范围与后继缺口

(1183.18) 是原 Hermitian 曲线的全部 Cartier–Serre 张量；(1183.23) 是原 degree 六曲线的准确限制，含全部半线性、相位和 degree。其系数可逐项读取，不需要有限酉群表示论或另一个随机数值窗。

不过，(1183.19) 的全空间 radical 为零**不意味着**其在 (1183.21) 的十维子空间上限制后的 radical 为零。原 $e=0$ 恰使 $f_{222}$ 在这个指定十维限制中进入 radical，仍与 Hermitian 全空间的非退化性相容。本文既不宣布 (1183.24) 非零，也不把四次 primitive 插入 $K_4$ 当成该三张量的另一个独立坐标。

后继实际问题是把同一覆盖下的高 primitive 插入及原三分支交叉配对，与 (1183.18) 的具体系数比较；所有 $p$ 次幂补偿及 meromorphic pole divisor 仍须逐项保留。原 $e,K_4$ 共同非零目标仍 OPEN。

## 来源

- [原 genus 4 / Fermat 六次笔记](../notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md) §§6、11：原十维基、$P_{a,b}$、$e$ 槽、Serre Čech 约定及完整半线性。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md) §3 与 [R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md) §2.2：旧实际 Hermitian 切线来源，只消费同一曲线模型，不把其 Jacobian Frobenius 平方结论代作本文三张量。

o1_theta 逐式纸面证明；无数学程序执行、无有限素数扫描。
