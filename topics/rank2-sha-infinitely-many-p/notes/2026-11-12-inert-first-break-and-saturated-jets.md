# 两类素数的首个分母与真实饱和 jet 的非抵消子式

日期：2026-11-12。**状态：本文的整性、根数及 Plücker 子式结论已证明；没有得到所需的最优 arithmeticity 上界。**

固定
\[
F(Z)=\mathscr D(Z)=\sum_{m\ge0}e_mZ^m\in\mathbb Q[[Z]],
\qquad e_0=0,\qquad e_1=\frac4{17^3}.
\]
这里始终使用原来的 \(E:y^2=x^3-17x\)、导子
\(f=34(1+i)\)、256点 Hecke 轨道及中央 theta 对角。
本文把 [首层平移](2026-11-12-central-diagonal-inert-shift.md)
和 [真实 jet/minors 公式](2026-11-12-central-vanishing-jets-and-minors.md)
连接起来。

新增结论如下。存在一个**固定有限集合** \(S\)，对每个
好素数 \(p\ge7,\ p\notin S\)，令
\[
k_0(p)=
\begin{cases}p,&p\equiv1\pmod4,\\p+2,&p\equiv3\pmod4.\end{cases}
\]
则有：

1. \(e_m\in\mathbb Z_p\) 对所有 \(m<k_0(p)\) 成立，且
   \(v_p(e_{k_0(p)})=-2\)。因此两类首坏指标分别准确为 \(p,p+2\)。
2. 令 \(k_0=k_0(p)\)。在 \(X=\mathbb P^2\)、标准整模型和
   \(\mathcal O(D)\) 的全部截面空间上，只要
   \[
   D\ge\max\left(4,\frac{k_0+7}{4}\right),
   \]
   则真正饱和 vanishing 格上的评价映射满足
   \[
   \boxed{\ \|\varphi_D^{k_0}\|_p=p^2.\ }
   \]
   下文给出一个前缀为单位、增广后赋值准确为 \(-2\) 的具体子式。
3. 更一般地，对任意 \(\epsilon>0\)，存在固定常数
   \(C_\epsilon\) 及固定有限集合 \(S_\epsilon\)，使得
   \[
   D\ge\epsilon k+C_\epsilon,\qquad
   p\notin S_\epsilon,\quad k_0(p)\le k
   \]
   蕴含 \(\|\varphi_D^k\|_p\ge p^2\)。

第3项合并两类素数后仍只给选定有限位的**线性**总预算；它不构成正的
\(k\log k\) 下界，也没有处理关键的 \(D\asymp\sqrt k\) 区间。
固定有限集合来自同一个代数 sigma 截面及固定非零系数，
不是随 \(p\) 改变的排除条件。

## 1. 全权根数与两个恒零同余类

令
\[
\chi_0=\psi N^{-1/2},\qquad
\chi_m=\chi_0^{\,2m+1},\qquad \nu=\chi_0^4.
\]
\(\nu\) 在所有有限单位群上平凡，故是处处有限未分歧的特征。
\(E\) 的根数为 \(+1\)，已经在
[局部输入](2026-11-12-cm-local-inputs.md) 中直接核过。

下面完整计算 \(w(\chi_m)\)，不根据有限精度零或 \(e_1\ne0\)
倒推函数方程符号。采用由 \(\mathbb Q\) 的标准加法特征经迹诱导
的局部加法特征。Tate 的未分歧扭转式为
\[
\epsilon(\xi\eta,\psi_v)
=\epsilon(\xi,\psi_v)\,
 \eta(\varpi_v)^{a(\xi)+n(\psi_v)}
\tag{1.1}
\]
（\(\eta\) 未分歧）。其一维公式直接见
Tate, *Number theoretic background*, (3.2.6.3)；
也可从 (3.2.6.2) 的 Gauss 和读出：扭转不改变单位上的求和，
只把外面的统一化元值乘上所示幂。
这里 \(n(\psi_v)\) 约定为 \(\psi_v\) 平凡于
\(\varpi_v^{-n}\mathcal O_v\) 的最大整数。

在 \(\lambda=1+i\) 处，
\[
a(\chi_0)=a(\chi_0^{-1})=3,\qquad n(\psi_\lambda)=2.
\]
全局主 idèle 关系给 \(\nu(\lambda)=-1\)：在其他有限处，
\(\lambda\) 是单位，而 \(\nu\) 在单位上平凡；在无穷处，
\((\lambda/|\lambda|)^{-4}=-1\)。
所以用 \(\nu^r\) 扭转使此处 epsilon 因子乘
\((-1)^{5r}=(-1)^r\)。

在 \(17\) 的两个分裂素位，导子指数均为一，加法特征导子为零。
\(\nu\) 在两统一化元上的值互逆：它在有理 idèle 上平凡。
因此这两个未分歧扭转因子相消。其他有限处的导子指数和
加法特征导子均为零，不产生变化。

在复处，角权为 \(a\) 的 epsilon 因子为 \(i^{|a|}\)；
若同时使用相反的 Fourier 规范，则取其倒数，下面所用的
两个比值仍分别为 \(1,-1\)。
由
\[
\chi_{2r}=\chi_0\nu^r,\qquad
\chi_{2r+1}=\chi_0^{-1}\nu^{r+1},
\]
复处相对于角权 \(1\) 或 \(-1\) 的比值分别为
\[
i^{4r}=1,\qquad i^{4r+2}=-1.
\]
\(\chi_0^{-1}\) 与 \(\chi_0\) 的全局根数均为 \(+1\)。
于是
\[
\boxed{\quad w(\chi_m)=(-1)^{\lfloor m/2\rfloor}.\quad}
\tag{1.2}
\]

对偶 \(L\) 函数通过理想复共轭与原 \(L\) 函数相同；
完成因子的中心也相同。因此负号情形的中心值严格为零。
准确 theta 插值式的其他因子均非零，故
\[
\boxed{\quad e_m=d_m=0\qquad(m\equiv2,3\pmod4).\quad}
\tag{1.3}
\]
特别地 \(e_2=e_3=0\)，并且每个惰性 \(p\) 都满足 \(e_p=0\)。

本节的局部符号推导由 CM 研究线首先给出，本篇逐处核对并展开
了未分歧扭转指数。它只用标准局部 epsilon 公式和本曲线已证导子。

## 2. 固定 sigma 截面补上 \(e_{p+1}\) 的整性

使用已经构造的
[固定 sigma 平方范数](2026-11-12-fixed-sigma-theta-square-factorization.md)：
存在固定整数 \(d=L^2\)、固定数域 \(M\)、固定多项式
\(P\in M[X]\) 及固定非零代数数 \(c\)，使
\[
S(z)=P(x(z)^2)\sigma_E(z)^d=\sum_{m\ge0}s_mz^m,
\qquad \deg P\le d/4-1,
\tag{2.1}
\]
且对 \(4\mid m\)，
\[
e_m=c(Nf\,d)^{-m}s_m\overline{s_m}.
\tag{2.2}
\]
\(d\) 的素因子只在 \(2,17\)。这里的复共轭只作用于固定代数
系数；不把它当作同一个 \(p\) 位上的连续自同构。

取包含下列有理素数的固定有限集合 \(S_0\)：\(2,3,17\)，
\(P,\overline P,c\) 的系数分母，以及以后需要排除的固定非零系数
的分子。讨论 \(p\notin S_0\) 时，(2.1) 的两个共轭截面在
\(M\) 的每个 \(p\) 素位都可同时使用整系数。

令 \(t=-x/y\)、\(z=\log_E(t)\)，并置
\[
\Sigma(t)=\sigma_E(\log_Et),\qquad
A(t)=t^dP(x(t)^2).
\]
由于 \(x(t)\in t^{-2}\mathbb Z_p[[t]]\)，(2.1) 的次数限制给
\[
A(t)\in t^4\mathcal O_{M,v}[[t]],
\qquad
S(\log_Et)=A(t)\left(\frac{\Sigma(t)}t\right)^d.
\tag{2.3}
\]

在惰性 \(p\ge7\) 处，R38 的首坏项证明给出
\[
[t^j]\frac{\Sigma(t)}t\in\mathbb Z_p
\quad(0\le j<p+1).
\tag{2.4}
\]
特别地，(2.3) 中 \(A(t)\) 的四阶零点说明：
计算次数至 \(p+1\) 时，第二因子只需使用次数至 \(p-3\) 的整系数。
因此
\[
[t^j]S(\log_Et)\in\mathcal O_{M,v}
\quad(0\le j\le p+1).
\tag{2.5}
\]

还必须检查从 \(t\) 到 \(z\) 不产生新分母。
不变导子 \(\delta\) 保持 \(\mathbb Z_p[[t]]\)，且 supersingular
关系 \(\delta^p=0\bmod p\) 说明 \(\delta^p/p\) 仍保持该整环。
若 \(n=ap+r<p^2\)、\(0\le r<p\)，则
\[
(\delta^nt)(O)\in p^a\mathbb Z_p,\qquad v_p(n!)=a.
\]
所以形式流
\[
t(z)=\sum_{n\ge1}\frac{(\delta^nt)(O)}{n!}z^n
\]
在次数 \(<p^2\) 全部整，特别涵盖 \(p+1\)。
将它代入 (2.5)，得到 \(s_{p+1}\) 在每个 \(p\) 素位整。
对共轭截面作同一论证，得到 \(\overline{s_{p+1}}\) 也整。

因 \(p\equiv3\pmod4\)，\(p+1\) 正是 (2.2) 允许的权。
又 \(c\) 整、\(Nf\,d\) 为单位，故
\[
\boxed{\quad e_{p+1}\in\mathbb Z_p\qquad(p\notin S_0,\ p\equiv3\pmod4).\quad}
\tag{2.6}
\]

惰性平移笔记已经证明 \(e_m\) 在 \(m\le p-1\) 时整；
(1.3) 处理 \(m=p\)，(2.6) 处理 \(m=p+1\)。
而 R45 给出无未知有限例外的
\[
p^2e_{p+2}\equiv
\frac{\kappa_p^2}{(Nf)^2}\frac4{17^3}\not\equiv0\pmod p.
\tag{2.7}
\]
因而对本文的固定有限集合之外，\(p+2\) 确是首个非整指标。

**范围。** (2.6) 使用一个固定代数截面的整模型，故目前只断言
固定有限集合外的整性；没有把其系数分母凭空说成只含 \(2,17\)。
R45 的 (2.7) 本身仍对全部惰性 \(p\ge7\) 成立。

## 3. 饱和评价映射的规范

令
\[
V_{D,k}=\left\{Q\in\mathbb Q[Z,Y]_{\le D}:
                    \operatorname{ord}_Z Q(Z,F(Z))\ge k\right\},
\]
\[
L_{D,k,p}=(V_{D,k}\otimes\mathbb Q_p)
                    \cap\mathbb Z_p[Z,Y]_{\le D},
\qquad
\varphi_D^k(Q)=[Z^k]Q(Z,F(Z)).
\tag{3.1}
\]
范数是标准单项式系数的 sup 范数。
(3.1) 是完整截面空间的饱和单位球，不是预先选定一个
消去多项式后的非饱和格。

对 \(r_j=([Z^j]Z^aF^b)_{a+b\le D}\)，设 \(B\) 是前缀独立行组成
的矩阵，\(\delta_p\) 表示 maximal minors 的最小赋值。
前文已证明
\[
\log\|\varphi_D^k\|_p=
\{\delta_p(B)-\delta_p([B;r_k])\}\log p.
\tag{3.2}
\]
下面实际给出两边的子式，不只给出某个 entry 的赋值。

## 4. 一个次数约为 \(p/4\) 的明确单位前缀

由 (1.3) 及 R45，写
\[
W=Y-e_1Z,\qquad W(Z,F(Z))=aZ^4+O(Z^5),
\qquad a=e_4\ne0.
\tag{4.1}
\]
\(a\ne0\) 不需要新的浮点计算：
已冻结的惰性有限环证书在 \(q=7,m=4\) 给出
\(d_4^{\rm raw}\equiv2+2i\pmod7\)。
四个轨道只差 CM 单位，且 \(f\) 是 \(7\) 单位，所以固定
\(e_4\) 非零。这里只用这条已精确认证的非零结论。
把 \(a\) 的分子、分母加入 \(S_0\)，得到固定有限集合 \(S\)。

固定 \(p\notin S,\ p=4r-1\)，置 \(k_0=p+2=4r+1\)。
在变量 \((Z,W)\) 中定义 \(k_0\) 个不同的单项式
\[
B_j=
\begin{cases}
Z^j,&0\le j\le4,\\
Z^\alpha W^\beta,&5\le j\le4r,\quad
 j=4\beta+\alpha,\quad0\le\alpha<4.
\end{cases}
\tag{4.2}
\]
它们都没有单项式 \(W\)。
最大总次数不超过
\[
D_0=\max(4,r+2)=\max\left(4,\frac{p+9}{4}\right).
\tag{4.3}
\]
并且
\[
B_j(Z,F-e_1Z)=c_jZ^j+O(Z^{j+1}),\qquad
c_j=
\begin{cases}1,&j\le4,\\a^{\lfloor j/4\rfloor},&j\ge5.\end{cases}
\tag{4.4}
\]
所有 \(c_j\) 都是 \(p\) 单位。

取行 \(0,\ldots,k_0-1\)、列 \(B_0,\ldots,B_{k_0-1}\)。
由第2节，这个前缀矩阵全部整；由 (4.4)，它是三角矩阵，行列式为
\[
\Delta=\prod_{j=0}^{k_0-1}c_j\in\mathbb Z_p^\times.
\tag{4.5}
\]
因此完整前缀的秩为 \(k_0\)，且
\[
\delta_p(B_{<k_0})=0.
\tag{4.6}
\]

现在加入第 \(k_0\) 行及额外列 \(W\)。在这一行中，\(W\) 的系数
就是 \(e_{k_0}\)，赋值为 \(-2\)。
其余选定列的同阶系数都整。确实，在
\(Z^\alpha W^\beta\) 中使用一次 \(W\) 的首坏项时，最低次数为
\[
k_0+\alpha+4(\beta-1).
\tag{4.7}
\]
(4.2) 没有 \((\alpha,\beta)=(0,1)\)，故 (4.7) 严格大于 \(k_0\)。
纯 \(Z\) 列显然也整。

对前缀进行整消去，增广行列式因而为
\[
\det B^+=\Delta\{e_{k_0}-u\},\qquad u\in\mathbb Z_p.
\]
更准确地，
\[
\boxed{\quad
p^2\det B^+\equiv
\Delta\,\frac{\kappa_p^2}{(Nf)^2}e_1
\not\equiv0\pmod p.\quad}
\tag{4.8}
\]
这就是所要求的真实 Plücker 非抵消式。

对完整 \(\mathcal O(D)\) 空间，前缀所有 entries 都整，而新增行
所有 entries 的赋值至少 \(-2\)：在次数 \(k_0\) 的乘积中至多使用
一个首坏系数。故其全部增广 minors 的赋值至少 \(-2\)；
(4.8) 达到此值。于是
\[
\delta_p(B^+)=-2,\qquad
\boxed{\|\varphi_D^{k_0}\|_p=p^2\quad(D\ge D_0).}
\tag{4.9}
\]

最后，\((Z,Y)\mapsto(Z,W)\) 及其逆都是整线性变换，
因为 \(e_1\in\mathbb Z_p\)。
它们在次数 \(\le D\) 的截面格上给互逆的整矩阵，
故没有更改 sup 范数或饱和格。以上确是原标准整模型的结论。

等价的实际截面是
\[
Q_p=W-\sum_{j<k_0}b_jB_j,\qquad b_j\in\mathbb Z_p,
\tag{4.10}
\]
其中 \(b_j\) 由单位三角前缀唯一确定。
它消失到 \(k_0-1\) 阶，系数范数为一，而第 \(k_0\) 阶值的
赋值准确为 \(-2\)。它的系数允许依赖 \(p\)，这正是局部饱和格
允许的操作，并没有把它误说成一个固定全局消去多项式。

### 4.1 普通素数与中心额外四阶零

对好普通 \(p\ge7\)，完整 theta 矩的整性立即给
\[
e_m\in\mathbb Z_p\quad(0\le m<p),
\]
因为这些权的 \(m!\)、固定导子及普通周期都是单位。
R45 又给 \(v_p(e_p)=-2\)。更准确地，普通首层式为
\[
p^2e_p\equiv A_p^2e_1\not\equiv0\pmod p,
\tag{4.11}
\]
其中 \(A_p\in\mathbb F_p^\times\) 是 Hasse 不变量。
见 vanishing-jets/minors 笔记 (4.3) 的 \(s=1\) 情形。
因此普通首坏指标是 \(k_0=p\equiv1\pmod4\)。

第4节的三角构造只使用以下三个事实：
\(W=aZ^4+\cdots\) 且 \(a\) 为单位；
全部前缀 \(m<k_0\) 整；
第 \(k_0\) 项准确有两个 \(p\) 分母。
把 \(p+2\) 改为 \(p\)，同一构造给
\[
\boxed{\quad
\|\varphi_D^p\|_p=p^2
\qquad
\left(D\ge\max\left(4,\frac{p+7}{4}\right)\right).
\quad}
\tag{4.12}
\]
其明确增广子式满足 \(p^2\det B^+\equiv\Delta A_p^2e_1\pmod p\)。

这个前缀确实包含目标中心项 \(e_{p-1}\)。
但三角对角只用 \(1,e_4,e_4^2,\ldots\)，所以把已知的
\(e_{p-1}\in p^2\mathbb Z_p\) 加强成
\(e_{p-1}\in p^4\mathbb Z_p\)，不会改变本子式的单位前缀或 (4.12)。
这是针对实际原始格的明确不变性，不是以任意测度替换原 theta。
它也没有声称其他子式或更深层评价对这个加强不敏感。

## 5. 任意小的固定 \(D/k\) 比例仍有真实坏方向

还可把 (4.3) 的固定比例进一步减小，但必须清楚说明量词。

取整数 \(E\ge2\)，考虑固定的有理多项式空间
\[
\mathcal A_E=
\operatorname{span}_{\mathbb Q}
 \{Z^\alpha W^\beta:\alpha+\beta\le E,\ \beta\ge2\}.
\]
其维数是 \(n_E=E(E-1)/2\)。每个元素在图像上至少八阶消失。
令次数 \(8,\ldots,n_E+6\) 的 \(n_E-1\) 个系数为零，得到非零
\(Q\in\mathcal A_E\)。由于 \(F\) 已证超越于 \(\mathbb Q(Z)\)，
它不能在非零多项式 \(Q\) 上恒零。所以存在有限的准确消失阶 \(h\)，
\[
Q(Z,F-e_1Z)=bZ^h+O(Z^{h+1}),\qquad
h\ge n_E+7,\quad b\in\mathbb Q^\times.
\tag{5.1}
\]
\(Q\) 是固定有理多项式；除去其系数分母及 \(b\) 的分子、分母后，
在所有剩余 \(p\) 处都可用作整、首项为单位的输入。
并且 \(Q\in(W^2)\)，所以它没有线性 \(W\) 项。

把第4节的前缀列改为
\[
B_j=Z^\alpha Q^\beta,\qquad j=h\beta+\alpha,\quad0\le\alpha<h.
\tag{5.2}
\]
它们在图像上的准确阶为 \(j\)，首项 \(b^\beta\) 是单位。
这些多项式线性独立：若有线性关系，取最小消失阶的一项便矛盾。
其系数全部整，且都没有线性 \(W\) 项。

在任一类素数的第 \(k_0=k_0(p)\) 行，(5.2) 依然整：
任何出现一次首坏 \(W\) 系数的项还至少含另一个 \(W\)，
或含正次 \(Z\)，所以次数严格超过 \(k_0\)。
于是同样的单位前缀及增广论证给
\[
\|\varphi_D^{k_0}\|_p=p^2
\quad\text{只要}\quad
D\ge h-1+E\left\lfloor\frac{k_0-1}{h}\right\rfloor.
\tag{5.3}
\]
对 (5.2) 不要求它们本身是标准单项式：
三角单位前缀给出整消去截面作为下界，
完整新增行的赋值至少 \(-2\) 给出相反方向的上界。
因此 (5.3) 同样是原格的准确范数。

若 \(k\ge k_0\)，将相应 (4.10) 乘以
\(B_{k-k_0}\)。所得多项式系数仍整，准确消失阶为 \(k\)，
第 \(k\) 阶值为原坏值乘一个单位。其次数至多
\[
2(h-1)+E\left\lfloor\frac{k-1}{h}\right\rfloor.
\tag{5.4}
\]
这证明在该次数范围有 \(\|\varphi_D^k\|_p\ge p^2\)。

由 (5.1)，\(E/h\le E/(E(E-1)/2+7)\to0\)。
所以先固定 \(\epsilon>0\)，再固定充分大的 \(E\) 及其 \(Q,h\)，
便得到导言第3项。所有额外排除仍是这一个固定 \(Q,b\)
带来的有限集合。

## 6. 这对全局 jet 预算确实说明了什么

固定 \(\epsilon>0\)，取 \(D\ge\epsilon k+C_\epsilon\)。
对上述固定有限集合外的全部好素数 \(p\le k-2\)，
两类都满足 \(k_0(p)\le k\)，第5节给
\[
\log\|\varphi_D^k\|_p\ge2\log p.
\]
所以这部分有限位的和至少为
\[
2\sum_{\substack{p\le k-2\\p\notin S_\epsilon}}
 \log p
=2k+o(k).
\tag{6.1}
\]
这是完整饱和截面的真实坏方向，不能用“所有首坏 entries 会被前缀
吸收”来抹掉。由第4.1节，即使加强目标普通素数的中心零阶，
这两类明确子式仍保持。

(6.1) 只对显示出来的这一组有限位求和。其他素数处的评价范数
可能小于一，因而其对数可能为负；本式没有把那些项丢弃之后
冒称是全部有限位总高度的下界。

但 (6.1) 完全可以被 Herblot 算术界中的 \(C(k+D)\) 吸收；
它**不**迫使最优 \(\alpha>0\)。
而 (5.1) 中的 \(E,Q\) 是先固定再让 \(p,k\) 变化。
若让 \(E\) 随 \(p\) 增长，以希望达到 \(D\asymp\sqrt p\)，
就必须统一控制这些消去多项式的整系数格及首项 \(b\) 在当前
\(p\) 处是否为单位。本文没有这种控制。

因此接下来真正的新问题可精确表述为：

> 对这条固定中央图像，是否存在次数随 \(p\) 增长的高接触多项式，
> 其单位首项与整系数格可以在当前素数 \(p\) 处统一认证；
> 或相反，目标中心额外四阶零是否会迫使相关饱和 Plücker 差
> 获得一个能累积成 \(k\log k\) 的改善？

本文的首坏整性和明确非抵消式解决了前缀最初的一处真实比较，
没有以系数预算取代上述尚未解决的问题。

### 使用的输入

- Tate, *Number theoretic background*, Proc. Sympos. Pure Math. **33**, Part 2
  (1979), 3–26，§3.2，特别 (3.2.6.3)：
  <https://ncatlab.org/nlab/files/TateNumberTheory.pdf>。
- 固定曲线的导子与根数：本课题的 CM 局部输入及 R4/R5。
- 同一固定 sigma 的首个惰性分母与形式流整性：R38、
  惰性中央平移笔记。
- 同一个代数 sigma 截面及 (2.2)：
  固定 sigma theta 平方范数笔记，使用 Yang (1997) 已发表公式。
- \(e_1=4/17^3\) 与所有惰性 \(p\ge7\) 的 (2.7)：R45。
- \(e_4\ne0\)：已冻结的
  [惰性精确有限环证书](2026-11-12-central-theta-inert-samples.md)
  中 \(q=7,m=4\) 的单位输出。
- 饱和格及相邻 minors 的准确范数式：
  [vanishing jets/minors 笔记](2026-11-12-central-vanishing-jets-and-minors.md)。
