# R592 — 原整 $\epsilon$ 五阶同态、两指定 forcing 与第六阶乘法修正

日期：2026-11-14。**状态：已证明。**

R589 的完整首极部秩七不读取两个最早 forcing。本篇在同一实际有限目标中取出此前保留的整项，证明一个从原九来源代数到 $k[\epsilon]/(\epsilon^6)$ 的真实代数同态。它把所有次数的原多项式同时送到由 $c_{4,p},c_{1,p}$ 决定的显示五阶曲线。第六阶不再直接套用这个同态：本篇保留来自首极部与原一次系数的完整乘法修正，并准确限制到原饱和前缀。

本篇不证明两个 forcing 至少一个非零，也不把它们的同时消失认作原算术中央失败的已知后果。

## 1. 同一原代数与指定整系数

取 $p=6s-1>71$、$b=17$，系数整数环为 $\mathcal O$，剩余域为 $k$。保持 R589 的
$$
\mathcal A_p=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^p),
\qquad
\mathcal B_p=\mathcal O[\boldsymbol F]\subset\mathcal A_p[1/p],
\tag{1}
$$
其中九个真实坐标按以下次序排列：
$$
\boldsymbol F=(S,T,W_{4,0},W_{4,1},
 W_{1,0},W_{1,1},W_{1,2},W_{1,3},W_{1,4}).
\tag{2}
$$
原 Euler 来源为
$$
W_{4,h}=z^h\int_0^z t^{1-h}f_4(t)\,dt\quad(h=0,1),
$$
$$
W_{1,h}=z^h\int_0^z t^{4-h}f_1(t)\,dt\quad(0\le h\le4),
\qquad f_4=x\sigma^6,\quad f_1=-xy\sigma^6,\quad w=z^6.
\tag{3}
$$
这些仍是 R575 的七个固定原函数经 R583 的固定整可逆基变换所得，并未新添全局坐标 $w$ 或 $\epsilon$。

R586 的真实 Gaussian forcing 记为
$$
z^{R_\ell}f_\ell
=w\exp((a/p)w^s)G_\ell(w),\qquad
G_\ell=\sum_{j\ge0}g_{\ell,j}w^j,
\tag{4}
$$
其中 $R_4=2,R_1=5$，$a\in\mathcal O^\times$。以下简写
$$
c_4=\overline{g_{4,s-1}}
=\overline{[z^{p-1}]f_4},\qquad
c_1=\overline{g_{1,s-1}}
=\overline{[z^{p-4}]f_1},\qquad
a_0=\bar a.
\tag{5}
$$
这里只约化已付整性的指定系数；没有约化整个未正则化 sigma 连接。

若
$$
F=\sum_{0\le Q<p,\ 0\le r<s}F_{r,Q}w^r\epsilon^Q\in\mathcal B_p,
$$
则
$$
F_{r,Q}=p^Q[w^{Qs+r}]F.
\tag{6}
$$
R589 的全来源估计准确是
$$
v_p(F_{r,Q})\ge-\mathbf1_{Q+6r\ge p}.
\tag{7}
$$
特别，**所有 $r=0$ 的系数都整**。因此可直接对实际 $F$ 定义
$$
\Psi_m(F)=\sum_{q=0}^{m}
 \overline{p^q[w^{qs}]F}\,\epsilon^q
 \in k[\epsilon]/(\epsilon^{m+1}),
\qquad 0\le m<p.
\tag{8}
$$
这是同一实际评价的行提取，不是给每列另选一个极部提升。

## 2. 前五阶是原代数上的同态

**定理 1。**
$$
\boxed{\Psi_5:\mathcal B_p\longrightarrow k[\epsilon]/(\epsilon^6)
\text{ 是一个 }\mathcal O\text{-代数同态。}}
\tag{9}
$$

证明保留 (1) 的真实进位。两个标准基单项式相乘，要对 $r=0$ 行有贡献，只可能：

1. 两个原 $w$ 指数均为零，此时得到 (8) 两个多项式的通常乘积；
2. 两个原 $w$ 指数 $r,t>0$ 且 $r+t=s$，用一次 $w^s=p\epsilon$，贡献
   $pF_{r,Q}G_{t,L}$ 到 $\epsilon^{Q+L+1}$。

第二种情形若两个系数均整，贡献模 $p$ 为零。若其中一个可能有一次 $p$ 分母，按 (7) 必须有
$$
Q+6r\ge p,\qquad Q\ge p-6(s-1)=5.
$$
因而它只能影响 $\epsilon^{Q+L+1}$ 的至少第六阶。若两者都可能有一次分母，则
$$
(Q+L+1)=
(Q+6r)+(L+6t)-p\ge p,
$$
已经被 $\epsilon^p$ 杀掉。故第五阶以内没有遗漏的进位贡献。这证明乘法性；加法、常数与 $\mathcal O\to k$ 显然相容。证毕。

这一步使用的是整个 $\mathcal B_p$ 的 (7)，所以同时覆盖所有 $D$、所有重复因子和混合单项式，并不只证明九个生成元之间的有限样本。

### 2.1 九个真实坐标的完整像

所有坐标在 $w=0$ 的常数为零。取 $k=qs$，$1\le q\le6$。在 R586 的系数公式中
$$
k-1=(q-1)s+(s-1).
$$
若 $q\ne h$，则 $6qs-h=qp+q-h$ 是 $p$ 单位，因此
$$
p^q[w^{qs}]W_{\ell,h}\equiv0\pmod p.
\tag{10}
$$
若 $q=h\in\{1,2,3,4\}$，原分母恰为 $qp$，所以
$$
\boxed{
p^h[w^{hs}]W_{\ell,h}
\equiv\frac{a_0^{h-1}}{h!}c_\ell\pmod p.}
\tag{11}
$$
R589 对原 $S,T$ 的成本是 $q-1$，故它们的相同六个整项均模 $p$ 为零。

因此 $\Psi_5$ 的生成元像准确为
$$
\begin{array}{c|c}
\text{原坐标}&\Psi_5\text{ 的像}\\ \hline
S,\ T,\ W_{4,0},\ W_{1,0}&0\\
W_{4,1}&c_4\epsilon\\
W_{1,1}&c_1\epsilon\\
W_{1,2}&a_0c_1\epsilon^2/2\\
W_{1,3}&a_0^2c_1\epsilon^3/6\\
W_{1,4}&a_0^3c_1\epsilon^4/24 .
\end{array}
\tag{12}
$$
把右列记作 $\boldsymbol v(\epsilon)$。对每一个原整系数多项式 $P$，得到显示的全次数公式
$$
\boxed{\Psi_5(P(\boldsymbol F))=\bar P(\boldsymbol v(\epsilon))
\bmod\epsilon^6.}
\tag{13}
$$

特别，第一条整行是原 augmentation 导数
$$
\boxed{
\overline{p[w^s]P(\boldsymbol F)}
=c_4\,\partial_{W_{4,1}}\bar P(0)
+c_1\,\partial_{W_{1,1}}\bar P(0).}
\tag{14}
$$
所有次数至少二的原单项式在这条指定行均为零。这不是先把七个首极部列换成两个自由 forcing 列。

### 2.2 同一实际像的准确秩

记 $\bar E_D$ 为次数至多 $D$ 的原多项式格模 $p$。由 (12)–(13)：

- 若 $c_1\ne0$，则 $D=1$ 时像准确为
  $\langle1,\epsilon,\epsilon^2,\epsilon^3,\epsilon^4\rangle$，维数五；
  $D\ge2$ 时，$W_{1,1}W_{1,4}$ 再给单位倍 $\epsilon^5$，像维数六。
- 若 $c_1=0,c_4\ne0$，则像维数准确为 $\min(D+1,6)$。
- 若 $c_1=c_4=0$，则像只有常数，维数一。

因此
$$
\boxed{(c_4,c_1)\ne(0,0)
\iff\Psi_5\text{ 不是 augmentation}
\iff\Psi_5(\mathcal B_p)=k[\epsilon]/(\epsilon^6).}
\tag{15}
$$
这是两条指定 forcing 在原完整代数中的准确判据；没有用首极部秩七来证明 (15) 左边成立。

## 3. 第六阶的全部乘法修正

定义两个实际线性行
$$
t(F)=\overline{[w]F},\qquad
\rho(F)=\overline{p^6[w^p]F}.
\tag{16}
$$
两者均有意义：前者由 (7) 整；后者就是
$\overline{pF}$ 在 $w^{s-1}\epsilon^5$ 的坐标，因为 $p=6s-1$。

它们都是相对于 augmentation $e(F)=\bar F(0)$ 的导子：
$$
t(FG)=e(F)t(G)+e(G)t(F),
$$
$$
\rho(FG)=e(F)\rho(G)+e(G)\rho(F).
\tag{17}
$$
第一式读原一次系数。对第二式，在目标 $w^{s-1}\epsilon^5$ 中不可能发生 $w$ 进位，因为两个标准 $w$ 指数和至多 $2s-2<2s-1$。一次极部若有贡献，按 (7) 只能是
$(r,Q)=(s-1,5)$，另一因子只能是常数。其余项乘外面的 $p$ 后均为零。故 (17) 成立。

**定理 2。** 对整个原代数中的任意 $F,G$，
$$
\boxed{
\Psi_6(FG)
=\Psi_6(F)\Psi_6(G)
+\epsilon^6\{\rho(F)t(G)+t(F)\rho(G)\}
\bmod\epsilon^7.}
\tag{18}
$$
证明继续定理 1 的进位分类。在第六阶，唯一可能未被 $p$ 杀掉的新项是
$$
(r,Q)=(s-1,5),\qquad(t,L)=(1,0),
$$
或者交换两因子。标准乘法给出一次 $p$，恰消一次分母，留下 (18) 的两个真实系数。没有其它第六阶项。

在原九坐标上，
$$
(t_i)_{i=1}^9=
\left(1,1,\frac16,\frac15,\frac16,\frac15,
 \frac14,\frac13,\frac12\right),
\tag{19}
$$
其中 $S,T$ 的首 $w$ 系数由 R418 的原径向式为一。由 R589 的完整极部公式，
$$
\rho(W_{\ell,0})=\frac{a_0^5}{720}\,\bar g_{\ell,s-2},
\qquad
\rho(S)=\rho(T)=\rho(W_{\ell,h})=0\quad(h>0).
\tag{20}
$$
这里的 $g_{\ell,s-2}$ 是相邻行，不能改标成 $c_\ell$。

由于 (10)–(12) 对 $q=6$ 仍给零线性像，(18) 与 (17) 给每个原多项式的完整第六阶式
$$
\boxed{
\Psi_6(P(\boldsymbol F))
=\bar P(\boldsymbol v(\epsilon))
+\epsilon^6
 \sum_{i,j=1}^9\rho_i t_j\,\partial_i\partial_j\bar P(0)
\bmod\epsilon^7.}
\tag{21}
$$
二阶导数在此有其通常的整数系数；例如 $P=X_i^2$ 的修正是 $2\rho_i t_i$。只有原二次部分能产生这个新项，高次项的对应二阶导数在原点为零。

因此，不能因为 (9) 成立，就把所有 $\epsilon$ 系数都按 (12) 作形式代入。准确的第一个可能修正已经是 (20) 的原首极部，而非一个可删除的误差。

## 4. 保持真正饱和前缀的运输

仍取 R589 的原整源格
$$
E_{D,9}=\bigoplus_{|\alpha|\le D}\mathcal O\,\boldsymbol X^\alpha,
\qquad
r_n(P)=[w^n]P(\boldsymbol F),
$$
以及真实的饱和前缀
$$
K_{D,k}=E_{D,9}\cap\ker(r_0,\ldots,r_{k-1})
$$
（先在分式域取精确零关系，再与同一整源格相交）。

对 $1\le q\le5$、$P\in K_{D,qs}$，原全部较早行已经为零，故 (13) 给
$$
\Psi_5(P(\boldsymbol F))\in\epsilon^q k[\epsilon]/(\epsilon^6)
$$
以及真实最后一行
$$
\boxed{
\overline{p^q\varphi_{D,9}^{qs}(P)}
=[\epsilon^q]\bar P(\boldsymbol v(\epsilon)).}
\tag{22}
$$
这不是仅在模 $p$ 矩阵中自由选一个核向量。右边只准在真正的 $K_{D,qs}$ 上使用。

若两个指定 forcing 同时为零，则 (13) 只剩常数。因此对全部 $D$、全部原 $P$，有五条真实条件改善
$$
\boxed{
v_p([w^{qs}]P(\boldsymbol F))\ge1-q,
\qquad1\le q\le5.}
\tag{23}
$$
在真实饱和前缀上也同样成立。第六阶则必须保留 (21)，不能从同一假设直接延长 (23)。

反过来，(15) 的像维数不保证 $K_{D,qs}$ 中存在非零最后一行。固定 $D$ 的真正前缀可以早已满秩；R589 对此保留的区别在本篇完全不变。

五条有限行的改善也不等于全 $k,D$ 的 cutoff。更不能把原 $S/T$ 或第三曲线中央失败，未经证明便替换成 $c_4=c_1=0$。本篇支付的是实际整项、完整乘法和原前缀之间的关系，算术输入仍需在同一个来源上另行连接。

## 5. 精确证书

[check-r592-integral-epsilon-jets.mjs](../scripts/check-r592-integral-epsilon-jets.mjs)
沿 R589 已用的共同解析纤维 $b=1,p=17$，直接由原有理 sigma 级数重建九个坐标到 $w^{6s}$：

- 核对全部九列的 (12)、(19)、(20)；
- 对次数至三的全部 219 个实际混合单项式核对完整 (21)，另外核对六次单项式；
- 在同一实际系数中显示第五阶同态及第六阶修正，而不把系数当作自由符号；
- 核对单位尺度 $b=2$；原 $b=17$ 的一般良位结论由 R586 的实际齐次运输保留；
- 核对若干参数范围内的全部可能进位位置。

这不是在坏位 $p=17$ 上约化 $b=17$ 曲线，也不是新的素数非消失扫描。证明对本篇全部 $p>71$ 已由 §§1–4 完成。

