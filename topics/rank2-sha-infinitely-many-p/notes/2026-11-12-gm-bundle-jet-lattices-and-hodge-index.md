# 实际 GM 束的向量 jet 格、Hodge 指数与首坏项

日期：2026-11-12。状态：下列整格、有限前缀、拉回阶数及实际周期
首坏项的比较均已证明。它们没有把所选标量代表的分母推迟直接转成
固定全局 vanishing-jet 的净预算改善。

本文只使用
[真实整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
已经构造的同一个 Legendre 秩二束，不另外引入任意微分模型。
这里 $t=\lambda_{\rm Leg}-1/2$ 是模参数。
以下取目标范围中的 $p\ge7$、$p\ne17$；普通方向因此为 $p\ge13$。
这保证真实 $M_1/t^4$ 在所用整模型中为单位，没有额外未计算的坏位。

## 1. 实际束与被修改的源格

令 $R=\mathbb Z_p[[t]]$，$H=H^1_{\rm dR}(\mathcal E/R)$，其中
$\mathcal E:y^2=x(x-1)(x-1/2-t)$。采用已经证明为整基的

$$
e=\binom{\omega}{\eta},\qquad
\eta=\nabla_{\partial_t}\omega,
\qquad\phi(t)=t^p.
$$

真实 Frobenius 的行约定为

$$
\Phi(e^\phi)=F_p(t)e,\qquad
F_p\in M_2(R),\qquad F_{p,1j}\in pR.
$$

令

$$
D=\operatorname{diag}(p^{-1},1),\qquad N_p=DF_p.
\tag{1.1}
$$

由实际周期矩阵公式，准确有

$$
\det F_p=p\frac{1-4t^2}{1-4t^{2p}},\qquad
\det N_p=\frac{1-4t^2}{1-4t^{2p}}\in R^\times.
$$

所以 $N_p\in\operatorname{GL}_2(R)$。它描述的整同构却是

$$
\widetilde H^\phi
 :=R\,(p^{-1}\omega^\phi)\oplus R\,\eta^\phi
 \xrightarrow{\ \Phi\ }H,
\tag{1.2}
$$

而原来固定的源格是 $H^\phi=R\omega^\phi\oplus R\eta^\phi$。
两者的商准确为 $(R/pR)\,p^{-1}\omega^\phi$。
在 $k$ 阶完整系数 jet（次数 $0,\ldots,k$）上，

$$
\operatorname{length}_{\mathbb Z_p}
 \bigl(J_k\widetilde H^\phi/J_k H^\phi\bigr)=k+1.
\tag{1.3}
$$

因此源格的修改不能因矩阵 $N_p$ 本身整可逆而删除。
此外 $\eta^\phi$ 是所选基向量的拉回；它不是
$\nabla_{\partial_t}\omega^\phi$。后者多出 $pt^{p-1}$，这个因子
同样不能在 jet 计算中省略。

## 2. 整矩阵真正保持的是完整向量前缀

对 $N(t)=\sum_{j\ge0}N_jt^j\in\operatorname{GL}_2(R)$，
普通系数的有限矩阵为

$$
T_k(N)=
\begin{pmatrix}
N_0&0&\cdots&0\\
N_1&N_0&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
N_k&N_{k-1}&\cdots&N_0
\end{pmatrix}
\in\operatorname{GL}_{2(k+1)}(\mathbb Z_p).
\tag{2.1}
$$

其逆为 $T_k(N^{-1})$，行列式为 $\det(N_0)^{k+1}$，是单位。
所以若两个**同一源格上的完整向量**评价矩阵准确相差
$B'_k=T_k(N)B_k$，那么：

- 每个前缀的整行格与全部阶数的 minors 理想相同；
- 前缀的真实饱和核相同，并与约化保持同样的关系；
- 在前一前缀的核上，第 $k$ 阶向量 jet 只乘 $N_0$，其最大范数不变。

证明是 (2.1) 的双向整行变换；最后一点因所有低阶项在前缀核上
消失而直接成立。

这个结论不对任意单分量自动成立。若只保留一个坐标，$N_0$ 会把
两个方向混合，所选坐标可能出现额外消失。也不能把一个原先指定的
多项式 section space 自动认作其经 $N(t)$ 变换后的同一个整空间；
只有真实的同源格评价矩阵比较已建立时，才能应用上述结论。

## 3. Frobenius 拉回的阶数及真正稀疏源的指数

完整 $R$ 模的 $\phi^*H$ 允许任意 $R$ 系数；一个固定 section 的
实际拉回则有 $f(t^p)$ 系数。两种空间的有限 jet 计数不同。

令 $q=\lfloor k/p\rfloor$。把实际多项式 section
$t^j\omega,t^j\eta$（$0\le j\le q$）拉回后，其系数只落在次数
$0,p,\ldots,pq$。对应稀疏插入矩阵

$$
E_{p,k}:\mathbb Z_p^{2(q+1)}
 \hookrightarrow\mathbb Z_p^{2(k+1)}
\tag{3.1}
$$

是原始直和嵌入。用列系数写 $\Phi$ 时矩阵为 $F_p^t=N_p^tD^{-1}$，
所以这一具体源的 jet 矩阵准确为

$$
T_k(N_p^t)E_{p,k}
 \operatorname{diag}(p,1,p,1,\ldots,p,1).
\tag{3.2}
$$

由于前两个因子给原始嵌入，(3.2) 的非零 Smith 指数准确是
$q+1$ 个 $1$ 与 $q+1$ 个 $0$。其像的饱和化就是把最后的对角矩阵
去掉；真实指数为

$$
\boxed{\quad q+1=\lfloor k/p\rfloor+1.\quad}
\tag{3.3}
$$

这比完整 $R$-jet 的 (1.3) 小，却仍然是实际被付出的格指数。
这里的源是明确列出的实际 GM section，不是用稀疏计数代替任意
section space 的饱和计算。

拉回还将非零向量 germ 的消失阶 $m$ 变为 $pm$；随后乘整可逆
$N_p(t)$ 不改变这个向量消失阶。因此目标前缀 $k$ 只看见源前缀
$\lfloor k/p\rfloor$，不能把拉回后的 $p$ 倍阶数同时当作源端
同样多的独立条件。

实际固定 $M_1=t^4v(t)$，$v\in R^\times$。若是在输出端乘
$M_1(t)$，上述稀疏次数改为 $4+pj$，指数成为

$$
\max\left(0,\left\lfloor\frac{k-4}{p}\right\rfloor+1\right).
\tag{3.4}
$$

若拉回的是 $M_1$ 本身，则其零点阶变为 $4p$，这是另一映射；
实际临界公式中的固定 $M_1(t)$ 不能未经证明替换成 $M_1(t^p)$。

## 4. 固定周期向量的首坏项没有推迟

令实际周期基本矩阵为

$$
Y(t)=\begin{pmatrix}K(t)&L(t)\\K'(t)&L'(t)\end{pmatrix},
\qquad Y(0)=I,
$$

其中 $K=1+t^2/2+\cdots$、$L=t+3t^3/2+\cdots$。
前文已经证明的水平式为

$$
F_pY=Y(t^p)F_p(0).
$$

置 $N_0=DF_p(0)\in\operatorname{GL}_2(\mathbb Z_p)$。准确重排后得到

$$
\boxed{\quad
Y(t)=N_p(t)^{-1}
 \underbrace{\begin{pmatrix}
 K(t^p)&p^{-1}L(t^p)\\pK'(t^p)&L'(t^p)
 \end{pmatrix}}_{\displaystyle D Y(t^p)D^{-1}}
 N_0.
\quad}
\tag{4.1}
$$

这在普通、惰性两型都成立。$K'(t^p),L'(t^p)$ 是先求导再代入，
不是对 $t$ 求复合导数。

中间矩阵在次数 $<p$ 为 $I$，而在次数 $p$ 有
$p^{-1}E_{12}+pE_{21}$。左右两个矩阵整可逆，所以

$$
[t^n]Y\in M_2(\mathbb Z_p)\ (n<p),\qquad
p[t^p]Y\equiv N_0^{-1}E_{12}N_0\ne0\pmod p.
\tag{4.2}
$$

这是一个非零秩一矩阵。它给固定秩二周期向量的首个分母准确在
$t^p$；不是只由某个上界推测存在分母。
再乘真实 $M_1=t^4v(t)$，得到

$$
p[t^{p+4}](M_1Y)\equiv N_0^{-1}E_{12}N_0\ne0,
\qquad[t^n](M_1Y)\text{ 整 }(n<p+4).
\tag{4.3}
$$

惰性时 $N_0$ 为反对角单位矩阵，故 (4.2) 的首坏方向位于
$K'$ 分量；单个标量 $M_1K$ 的首坏项在 $p+5$。
普通时首坏方向位于 $L$ 分量。完整向量与单个所选分量的首次分母
本来就不同，不能用单分量的推迟代替 (4.3)。

## 5. 右端初值的 $p$ 因子与源格指数不能混算

在惰性处
$F_p(0)=\left(\begin{smallmatrix}0&pa_p\\b_p&0\end{smallmatrix}\right)$，
在普通处它为 $\operatorname{diag}(pa_p,b_p)$；两者行列式都是 $p$。
因此在原式 $D Y(t^p)F_p(0)$ 中，$D$ 的行列式 $p^{-1}$ 确实被
$F_p(0)$ 的行列式 $p$ 补偿。但这只说明行列式线为单位，不能消去
矩阵条目的负赋值。式 (4.1) 把这件事准确写成了共轭 $DY^\phi D^{-1}$。

在实际 $\operatorname{End}(H)$ 的四个基方向上，该共轭的权为

$$
E_{11}:0,\quad E_{12}:-1,\quad E_{21}:+1,\quad E_{22}:0.
\tag{5.1}
$$

对次数为 $0,p,\ldots,pq$ 的完整稀疏系数格，它的 Smith 指数为
$q+1$ 个 $-1$、$2(q+1)$ 个 $0$、$q+1$ 个 $+1$。
总和为零，负方向却仍真实存在；(4.2) 正在该负方向取得非零首项。
所以不能把 (3.3) 的源 Hodge 指数与右端初值的 $p$ 简单相减，
继而声称所有前缀 minors 都没有代价。

若某个实际评价空间只取这些方向中的一部分，子式的权取决于被选
列。一般公式是对每个子式分别加上所选 Hodge 权之和，再取最小值；
不同子式可能成为最小者。完整格的指数只给环境中的准确计数，
不能代替该具体子空间的饱和计算。

## 6. 对 $p\to2p$ 改善的准确判断

整 Frobenius 笔记已经无损证明：所选临界标量行可以用
$U_p,V_p$ 的整代表重写，其首坏项由 $p+O(1)$ 推迟至 $2p+4$。
这是实际系数上的正面改进，本文没有否定该恒等式。

但这不能直接记为固定 GM 束的 vanishing-jet 预算改善，理由现在
可以逐项定位：

1. 在完整向量层，$N_p$ 的前缀矩阵整可逆，真实饱和 minors 和
   向量 jet 范数保持不变，且 (4.3) 的固定首坏项仍在 $p+4$。
2. 若转到原始 Frobenius 源格，必须保留 (1.3) 或实际稀疏源的
   (3.3)–(3.4)；同时计入 $t\mapsto t^p$ 的阶数变化。
3. 临界标量包含 $U_p/(V_p/t)$、$p$ 次幂差及 Euler 逆；它不是已经
   证明与上述完整向量评价矩阵只差整可逆行变换的线性 jet。

因此当前已证的是一个依赖 $p$ 的临界标量代表改善，不是免费的
固定向量格净收益。要得到真正收益，下一步须把该标量行作为这个
固定束的明确张量、商或带滤过评价，并计算**该指定空间**在 Hodge
修改下的真实饱和指数。仅比较两个首坏次数，或只比较整行列式，
都不足以完成这项判断。
