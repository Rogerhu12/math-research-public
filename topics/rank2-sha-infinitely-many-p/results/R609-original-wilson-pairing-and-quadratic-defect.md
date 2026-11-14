# R609 — 原二次共振行的 Wilson 配对与固定非齐次关系

日期：2026-11-14。**状态：已证明。**

本篇在 R607 的同一实际整目标内，把三条原二次 Euler 来源行接回固定的 degree $12$ 全函数恒等式。一个不能删除的 Gaussian 端点给出明确的单位右端；全部参考来源可以在同一个恒等式中消去。

结论是原全有限评价矩阵的非齐次约束。它在 R607 的整 Schur 分块后仍保持，但不是任意一个真饱和层的单位结论，也没有由原两中央同时零给这些二次行赋零。

## 1. 原来源、三个实际二次行

保持 R586、R607 的规范：
$$
p=6s-1>71,\qquad N=s-1,\qquad b=17,\qquad w=z^6,
$$
$$
D=\frac{d}{dz},\qquad Dx=2y,\qquad Dy=3x^2,\qquad y^2=x^3+b,
$$
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,\qquad
A_4=z^2f_4,\quad A_1=z^5f_1.
\tag{1}
$$
令
$$
a=6p[z^{p+1}]\log(\sigma/z)\in\mathcal O^\times,
\qquad
A_\ell=w\exp\!\left(\frac a p w^s\right)G_\ell(w),
\quad G_\ell=\sum_{r\ge0}g_{\ell,r}w^r.
\tag{2}
$$
以下有限域公式中 $a$ 表示其约化。所有 $r<s$ 的 $g_{\ell,r}$ 是原有理级数的整系数，$g_{\ell,0}=1$，并记
$$
c_{4,p}=\bar g_{4,N},\qquad c_{1,p}=\bar g_{1,N}.
\tag{3}
$$
这些是未除去 $b^N$ 的两个指定 forcing。

七个原 Euler 来源满足
$$
(6w\partial_w-h)W_{\ell,h}=A_\ell,
\qquad
h=0,1\quad(\ell=4),\qquad
h=0,\ldots,4\quad(\ell=1).
\tag{4}
$$
原有限目标采用 R607 的真实元素
$$
\epsilon=\frac{w^s}{p},\qquad
\upsilon=\frac{w^p}{p^6},\qquad
e_n=p^{-\lfloor6n/p\rfloor}w^n,\quad0\le n<ps.
\tag{5}
$$
其整格 $\mathcal C_p$ 及模 $p$ 环为
$$
\overline{\mathcal C}_p=
k[w,\epsilon,\upsilon]/
(w^s,\ \epsilon^6-w\upsilon,\
 w^{s-1}\epsilon^5,\ \upsilon^s).
\tag{6}
$$

保持 R607 的完整共振多项式
$$
\Gamma_{\ell,h}(\upsilon)=
\sum_{j=j_0}^{N}
 \frac{a^{6j+h-1}\bar g_{\ell,N-j}}
 {(6j+h)!}\upsilon^j,\qquad
j_0=\begin{cases}1,&h=0,\\0,&h>0.\end{cases}
\tag{7}
$$
定义三个具体数：
$$
Q_{44}=[\upsilon^N]\Gamma_{4,0}^2,\qquad
Q_{41}=[\upsilon^N]\Gamma_{4,0}\Gamma_{1,3},\qquad
Q_{11}=[\upsilon^{N-1}]\Gamma_{1,3}^2.
\tag{8}
$$

它们都是原二次来源的真实物理行：
$$
\boxed{
\begin{aligned}
Q_{44}
 &=\overline{p^{p-5}[w^{Np}]\,W_{4,0}^2},\\
Q_{41}
 &=\overline{p^{p-2}[w^{Np+3s}]\,W_{4,0}W_{1,3}},\\
Q_{11}
 &=\overline{p^{p-5}[w^{Np+1}]\,W_{1,3}^2}.
\end{aligned}}
\tag{9}
$$
特别，第三条不是误放在低权商中的 $\epsilon^6$：
$$
\epsilon^6\upsilon^{N-1}=w\upsilon^N
$$
在 (6) 中是保留的真实非零基位置。

为核 (9)，原 $W_{\ell,h}$ 的非共振部分权都至少为六，共振部分的权恰为 $h$。在指定总权 $0,3,6$ 上，只有对应的两个共振部分相乘能够贡献。更大的权若绕过 $p$，原乘法额外带一个 $p$，约化后为零。这个论证使用 R607 的实际整数进位，而非把旧 $J_p^2=0$ 当作原二次来源为零。

## 2. 三条固定 degree 12 全函数恒等式

对一个完整函数定义
$$
\mathcal H_4(f)=fD^4f-4(Df)(D^3f)+3(D^2f)^2,
$$
$$
\mathcal W(f_4,f_1)=f_4Df_1-(Df_4)f_1.
\tag{10}
$$

**引理 1。** 在特征零的原 sigma 规范中，有完整恒等式
$$
\boxed{
\begin{aligned}
\mathcal H_4(f_4)&=72x(x^3+2b)\sigma^{12},\\
\mathcal H_4(f_1)&=-432b^2x\sigma^{12},\\
\mathcal W(f_4,f_1)&=-3x^4\sigma^{12}.
\end{aligned}}
\tag{11}
$$
因此
$$
\boxed{
3b\,\mathcal H_4(f_4)
+72b\,\mathcal W(f_4,f_1)
+\mathcal H_4(f_1)=0.
}
\tag{12}
$$

这是全函数身份，证明如下。若一个 degree $6$ theta 来源在周期平移时乘上
$\exp(6\eta(z+\omega/2))$，则其导数在平移下由 $D$ 换成 $D+6\eta$。二变量差算子 $D_1-D_2$ 消去这个共同常数，所以 (10) 的两个表达式都是完整的 degree $12$ theta 截面。它们的 $\mu_6$ 型均为四；该型空间准确由
$$
x^4\sigma^{12},\qquad x\sigma^{12}
\tag{13}
$$
张成。没有删掉平坦角色或改变线丛。

原系数为
$$
f_4=z^4\left(1-\frac{4b}{35}z^6+O(z^{12})\right),
$$
$$
f_1=z\left(1+\frac{6b}{35}z^6
-\frac{1068b^2}{25025}z^{12}+O(z^{18})\right),
$$
$$
x^4\sigma^{12}
=z^4\left(1-\frac{18b}{35}z^6+O(z^{12})\right),
\qquad x\sigma^{12}=z^{10}+O(z^{16}).
\tag{14}
$$
$\mathcal H_4(f_4)$ 的前两系数为 $72$ 和 $3744b/35$，给第一式。
对 $f_1=z+Az^7+Bz^{13}+\cdots$，其 $z^4$ 系数为零，$z^{10}$ 系数为
$$
252A^2+10296B=-432b^2.
$$
这给第二式。由于 (13) 是完整二维空间，这两次求系数已定全函数，而非有限截断外推。

第三式可以直接在原函数域计算：
$$
xD(-xy)-(Dx)(-xy)
=x(-5x^3-2b)+2xy^2=-3x^4;
$$
共同的 $6D\log\sigma$ 项恰好相消。式 (12) 随即由 (11) 的两个固定基逐项消去得到。

## 3. Wilson 配对与不能删除的端点

对 $0\le m\le p-r$，Wilson 公式给
$$
\boxed{
\frac1{m!(p-r-m)!}
=(-1)^{m+r}\prod_{\nu=1}^{r-1}(m+\nu)
\quad\text{于 }k.
}
\tag{15}
$$
这里只用 $r=5$ 和 $r=2$；所有阶乘都小于 $p$。

定义原物理系数
$$
H_{44}=\overline{[z^{p-1}]\mathcal H_4(f_4)},\qquad
H_{41}=\overline{[z^{p-1}]\mathcal W(f_4,f_1)},\qquad
H_{11}=\overline{[z^{p-1}]\mathcal H_4(f_1)}.
\tag{16}
$$
这些系数均整。前两者只读取原 $r\le N$ 的整窗口。第三者的单个端点可能有一个 $p$ 分母，但其实际导数因子含 $p$；下文完整保这个端点。

### 3.1 第一平方行

对两个幂 $z^u,z^v$，当 $u+v=p+3$ 时，
$\mathcal H_4$ 的对称系数模 $p$ 为
$$
8\,u(u-1)(u-2)(u-3).
\tag{17}
$$
这是 $\frac12(D_1-D_2)^4$ 的五项展开：用 $v=3-u$ 后，每项都有同一个四次下降积，五个二项式系数之和为 $16$。

在 $f_4$ 上，$u=6i+4$，$i+j=N$。将 (15) 的 $r=5$ 代入 (7)，保 $\Gamma_{4,0}$ 的 $j=0$ 缺失项，得到
$$
\boxed{
H_{44}=-8a^6Q_{44}+384c_{4,p}.
}
\tag{18}
$$
这里两个缺失端点各贡献 $24c_{4,p}$，再乘 (17) 的 $8$；不能把它们并入 $Q_{44}$。

### 3.2 混合行

在混合 Wronskian 的同一个系数上，两个幂次之和是 $p$，故模 $p$ 的导数权为 $-2(6i+4)$。式 (15) 的 $r=2$ 给
$$
\boxed{
H_{41}=2a^3Q_{41}+2c_{4,p}.
}
\tag{19}
$$
只有 $\Gamma_{4,0}$ 对应的一个端点缺失；$\Gamma_{1,3}(0)$ 所含的 $c_{1,p}$ 已完整留在 $Q_{41}$ 中。

### 3.3 第二平方行的 Gaussian 端点

在 $f_1$ 上，该系数要求 $i+j=s=N+1$，而 $\Gamma_{1,3}^2$ 只含
$0\le i,j\le N$ 的内部项。由 R602 的原 Gaussian 后 Hurwitz 整性，$G_{1,s}$ 整。因此原 $f_1/z$ 的第 $s$ 个系数准确为
$$
[w^s](f_1/z)=\frac a p+g_{1,s}.
\tag{20}
$$
它与原线性首项 $z$ 配对时，(10) 的实际系数是
$$
(p+2)(p+1)p(p-5).
\tag{21}
$$
整的 $g_{1,s}$ 部分因此约化为零；$\frac a p$ 部分却给
$$
a(p+2)(p+1)(p-5)\equiv-10a.
\tag{22}
$$
这就是本篇的非齐次项。它不允许在先约化级数时删除。

内部项由 (15) 的 $r=5$ 和 (17) 得到，完整结论是
$$
\boxed{
H_{11}=8a^6Q_{11}-10a.
}
\tag{23}
$$
式 (20) 没有把原 sigma 全函数约化为有理函数，也没有调用一个未经支付的 Cartier 零命题。

## 4. 纯原来源的非齐次二次约束

将 (18)、(19)、(23) 代回特征零全函数恒等式 (12)，所有固定 degree $12$ 参考项都已实际消去。

**定理 2。** 对同一个原有限目标和两个指定 forcing，
$$
\boxed{
a^6(Q_{11}-3bQ_{44})
+18b\,a^3Q_{41}
+162b\,c_{4,p}
=\frac54a.
}
\tag{24}
$$

右端是单位，因为 $p>71$ 且 $a$ 是原 supersingular Gaussian 单位。因此这四个真实行不能全为零。特别，若额外满足指定 $c_{4,p}=0$，则
$$
\boxed{
a^6(Q_{11}-3bQ_{44})
+18b\,a^3Q_{41}=\frac54a\in k^\times.
}
\tag{25}
$$
于是三个原二次来源的实际首极部行中至少一条非零。式 (24) 不断言两个指定线性 forcing 不会同时零；即使两者同时为零，内部二次卷积仍完整保留在 (25) 中。

## 5. 同一整 Schur 分块和真实前缀

三个二次行都落在 R589 的原首极部位置，而不是对旧首极部取平方。准确地，
$$
\begin{array}{c|c|c}
\text{原列}&n=Qs+r&(Q,r)\\ \hline
W_{4,0}^2&Np&(p-6,1)\\
W_{4,0}W_{1,3}&Np+3s&(p-3,1)\\
W_{1,3}^2&Np+1&(p-6,2)
\end{array}
\tag{26}
$$
各行均有 $Q+6r\ge p$，且 (9) 的缩放恰为 $p^{Q+1}$。这正是
$\overline{pF}$ 在 $\overline{\mathcal A}_p$ 的实际读数。

取任意 $D\ge2$、$p>7D$，使用 R607 的同一个精确整回缩
$\mathcal P_{p,D}$。将 (26) 的每条原列 $B$ 换成
$$
\widetilde B=B-\mathcal P_{p,D}B
$$
后，三个 $Q$ 原样保持，因为纯 $S/T$ 多项式属于 $\mathcal A_p$，其
$\overline{pF}$ 为零。将线性原列 $W_{4,1}$ 同样换成其真实 Schur 列后，
$$
c_{4,p}=\overline{p[w^s]W_{4,1}}
$$
也保持，因为纯 $S/T$ 的这个低权像为零。

故 (24) 是**真实混合 Schur 部分**上的同一非齐次约束；它不依赖于另加自由目标列或假定约化核可提升。

但四个观察位于不同物理行，并作用在不同原列上。本篇没有把它们合并成一个 $\phi_D^k$，也没有证明任一高行处的原真前缀非空。特别，不能把这四条被选行的单位组合当作 R581 所需的非空真饱和层收益。所有更早物理行仍须在同一个实际矩阵中精确消去。

## 6. 与原 S/T 中央失败的准确接口

R595 采用除去 $b^N$ 的两个 forcing：
$$
\widetilde{\boldsymbol c}
=b^{-N}(c_{4,p},c_{1,p})^t.
$$
其完整首层比较是
$$
\binom{\widetilde a_{34}}{\widetilde a_{72}}
=M\widetilde{\boldsymbol c}+\boldsymbol R,
$$
$$
M=
\begin{pmatrix}
\frac{17}{45}503&-\frac{17}{45}488\\
\frac{12}{5}1472&-\frac{12}{5}1467
\end{pmatrix},
\qquad
\det M=-\frac{266084}{15}.
\tag{27}
$$
$\boldsymbol R$ 是 R595 明列的原低截断整卷积，不能删除。现有好惰性范围中 $M$ 可逆。

若原两条完整中央导数同时零，则其必要首层条件给
$$
\widetilde{\boldsymbol c}=-M^{-1}\boldsymbol R.
$$
将这个**实际**条件代入 (24)，得到
$$
\boxed{
a^6(Q_{11}-3bQ_{44})+18b\,a^3Q_{41}
=\frac54a+162b^s\,e_1^tM^{-1}\boldsymbol R.
}
\tag{28}
$$
这保留了全部原低残差。右端不能只因第一项是单位就宣称单位；残差可以参与同模数的真实相消。完整中央的下一 Bockstein 也未在本篇被替换为二次 $Q$ 行为零。

因此，本篇新增的是固定 degree $12$ 全函数所给的纯原二次非齐次约束及其完整算术接入式 (28)。原两中央与非空真前缀之间的进一步关系仍需支付。

## 7. 精确证书

[check-r609-wilson-pairing-and-quadratic-defect.mjs](../scripts/check-r609-wilson-pairing-and-quadratic-defect.mjs) 从原有理 sigma 递推完成 738 项精确检查：

- 两条完整 $\mathcal H_4$ 身份的原二维 theta 系数和 Wronskian 恒等式；
- Wilson 阶乘配对以及原 Gaussian 端点的准确 $-10a$；
- 在既有 $p=17,23$、原 $b=1,17$ 合法纤维上，(9) 的全部真实物理系数与独立 $\Gamma$ 计算的一致性；
- (18)、(19)、(23)、(24) 及全部物理首极部位置。

这些有限纤维只复核规范与固定公式，不是新的素数非消失扫描。一般 $p$ 结论由正文的全函数、完整窗口与 Wilson 恒等式证明。原主目标没有由此宣告完成。
