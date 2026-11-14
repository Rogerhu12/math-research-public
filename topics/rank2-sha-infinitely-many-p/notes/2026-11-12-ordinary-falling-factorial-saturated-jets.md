# 实际 theta 混合列的普通饱和 jet 行与次数敏感预算

日期：2026-11-12。**状态：本文的全列共同前缀关系、普通局部范数界、
全普通位预算及统一 Mellin 行均已证明。** 惰性位尚未包含在预算中；
本文没有把选定 $D\asymp k^{1/r}$ 的表观系数直接称为
Herblot 的全 $(D,k)$ arithmeticity 常数，也没有证明原中央导数非零。

## 1. 原固定源格与普通整测度

使用 R117、R155 的同一真实对象

$$
w=z^4,\qquad A_2(z)=A(2z)/16,\qquad B(z)=R(x(z)^2)A_2(z).
\tag{1.1}
$$

$A_2$ 和 $B$ 都是首项 $z^4$ 的次数六十八 theta 截面，系数在
$\mathbb Q$。源格始终是原来的普通系数格

$$
\mathscr P_D=\bigoplus_{a+b+c\le D}\mathbb Z\,w^aX^bY^c,
\qquad
\operatorname{ev}(P)=P(w,A_2,B).
\tag{1.2}
$$

取只用 $w,A_2$ 或只用 $w,B$ 的子格时，下述结论原样成立。
没有用 Hurwitz 格替换 (1.2)。写

$$
r_j(P)=[w^j]\operatorname{ev}(P),\qquad
\mathscr K_{D,k,p}=\ker_{\mathbb Q_p}(r_0,\ldots,r_{k-1})
                  \cap\mathscr P_D\otimes\mathbb Z_p.
\tag{1.3}
$$

$\varphi_D^k$ 是 $r_k$ 在这个真正饱和核上的限制，源采用最大系数范数，
目标采用 $dw$ 的原单位平凡化。冗余前缀行照常允许；若此行不增加秩，
其评价为零，以下上界仍成立。

固定普通 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$。R155 给同一个
完备未分歧整系数环 $\mathcal O$ 与单位周期 $\Omega_p$，使

$$
\mathcal A_2(T)=A_2(\Omega_p\log(1+T)),\qquad
\mathcal B(T)=B(\Omega_p\log(1+T))\quad\text{均在 }\mathcal O[[T]].
\tag{1.4}
$$

其任意乘积 $\mathcal A_2^b\mathcal B^c$ 对应范数至多一的整测度
$\mu_{bc}$。定义分布导数的符号为

$$
(\partial^j\mu)(g)=\mu(g^{(j)}).
\tag{1.5}
$$

Amice 变换准确为 $\log(1+T)^j\mathcal A_\mu(T)$，没有负号。
所以每个源元素 $P=\sum c_{abc}w^aX^bY^c$ 对应实际分布

$$
\nu_P=\sum_{a+b+c\le D}c_{abc}\Omega_p^{4a}\partial^{4a}\mu_{bc}.
\tag{1.6}
$$

它一般不是有界测度，但对于多项式测试函数总有定义。其矩准确满足

$$
\nu_P(x^m)=\Omega_p^{m}\frac{d^m}{dz^m}
                       P(z^4,A_2(z),B(z))\bigg|_{z=0}.
\tag{1.7}
$$

因为原输出四重对称，非 $4$ 倍的矩为零；对 $m=4j$，右边是
$\Omega_p^{4j}(4j)!r_j(P)$。这是此处唯一使用的尺度换算；例如
$\mu_{10}(x^4)=24\Omega_p^4$，与 R155 的原曲线校准相同。

## 2. 一个整数多项式对全部列给出的同一前缀行

置

$$
\mathcal F_n(x)=\prod_{v=0}^{n-1}(x-v)
              =\sum_{m=0}^n s(n,m)x^m,
\tag{2.1}
$$

其中 $s(n,m)$ 是带符号 Stirling 整数，$s(n,n)=1$。对
$0\le j\le n$ 定义

$$
E_p(n,j)=v_p(j!)+\sum_{h\ge1}
                    \max\!\left(\left\lfloor\frac n{p^h}\right\rfloor-j,0\right).
\tag{2.2}
$$

**整数导数引理。** 对每个 $x\in\mathbb Z_p$，

$$
v_p(\mathcal F_n^{(j)}(x))\ge E_p(n,j).
\tag{2.3}
$$

**证明。** $\mathcal F_n^{(j)}$ 是 $j!$ 乘上所有删去 $j$ 个不同因子的
剩余乘积之和。在每个模 $p^h$ 剩余类中，连续整数 $0,\ldots,n-1$
至少出现 $\lfloor n/p^h\rfloor$ 次。因此对固定 $x$，任意删去 $j$
个因子的剩余乘积，其被 $p^h$ 整除的因子至少有
$\max(\lfloor n/p^h\rfloor-j,0)$ 个。对 $h$ 求和，再乘 $j!$，
得到 (2.3)。相加不会降低这个下界。此证明也处理非整数的
$x\in\mathbb Z_p$，不要求选一个与 $x$ 相等的因子。$j>n$ 时导数为零。

现在取 $n=4k$、$K=4\min(D,k)$，并置

$$
e_p(D,k)=\min_{\substack{0\le j\le K\\4\mid j}}E_p(4k,j).
\tag{2.4}
$$

由 (1.6)、(2.3) 及整测度的范数，**对 (1.2) 的每一列同时**有

$$
\boxed{\quad
\sum_{j=0}^k s(4k,4j)\Omega_p^{4j}(4j)!\,r_j
                 \ \in\ p^{e_p(D,k)}\mathcal O^{\dim\mathscr P_D}.
\quad}
\tag{2.5}
$$

这是同一组系数作用于所有 $w^aA_2^bB^c$，不是逐列另选的关系。
超过 $k$ 的自然参数幂在 (2.3) 中给零导数，故 (2.4) 可用显示出的 $K$。
式 (2.5) 对全部 $D,k$ 成立，不要求原中央导数消失。

## 3. 真正饱和核上的局部范数

在 (1.3) 的核上，(2.5) 的所有低阶项准确为零，首项系数是
$\Omega_p^{4k}(4k)!$。于是

$$
\boxed{\quad
\log\|\varphi_D^k\|_p\le \Gamma_p(D,k)\log p,
\quad}
\tag{3.1}
$$

$$
\begin{aligned}
\Gamma_p(D,k)
&=v_p((4k)!)-e_p(D,k)\\
&=\max_{\substack{0\le j\le K\\4\mid j}}
 \left\{\sum_{h\ge1}\min\!\left(\left\lfloor\frac{4k}{p^h}\right\rfloor,j\right)
                        -v_p(j!)\right\}.
\end{aligned}
\tag{3.2}
$$

特别是 $\Gamma_p\ge0$，因为 $j=0$ 给零。最高阶乘及其全部 $p$ 因子
都已在 (3.2) 中支付；没有只把 (2.5) 的整除次数当作净收益。

也可直接写为 R151 的真实对偶条件

$$
r_k\in\operatorname{row}_{\mathbb Q_p}(r_0,\ldots,r_{k-1})
                         +p^{-\Gamma_p(D,k)}\mathbb Z_p^{\dim\mathscr P_D}.
\tag{3.3}
$$

虽 (2.5) 先在 $\mathcal O$ 中给出，(3.1) 对原 $\mathbb Z_p$ 源系数
直接成立，其值本来在 $\mathbb Q_p$；再由 R151 的饱和核／对偶格等价
得到 (3.3)。因此不需要把周期 $\Omega_p$ 假称为 $\mathbb Q_p$ 中的数，
也不需要假设所有对偶系数在扩域后自动下降。

一个较短但稍弱的共同关系来自
$x^e(x^p-x)^s$，其中 $4k=sp+e$、$0\le e<p$。其至多 $K$ 阶导数
在全 $\mathbb Z_p$ 上都有至少 $s-K$ 层 $p$，得到

$$
\log\|\varphi_D^k\|_p
 \le\bigl(K+v_p(\lfloor4k/p\rfloor!)\bigr)\log p.
\tag{3.4}
$$

主结果采用更准确的 (3.2)。两式都来自原输出的同一个多项式矩，
并保留整个 $\mathbb Z_p$，没有单位支撑省略。

## 4. 全普通素数的统一次数敏感预算

固定坏集外，所有普通素数满足同一 (3.2)。对 $1\le D\le k$，
记 $n=4k,K=4D$。舍去 (3.2) 中非正的 $-v_p(j!)$，有

$$
\Gamma_p(D,k)\le
       \sum_{h\ge1}\min(\lfloor n/p^h\rfloor,K).
\tag{4.1}
$$

其中 $h\ge2$ 的全素数贡献为

$$
\sum_p\log p\sum_{h\ge2}\min(\lfloor n/p^h\rfloor,K)
\le n\sum_p\frac{\log p}{p(p-1)}=O(n).
\tag{4.2}
$$

对 $h=1$，在 $y=n/K\ge1$ 分开。小素数贡献满足
$K\vartheta_1(y)=O(Ky)=O(n)$，这里 $\vartheta_1$ 仅计
$p\equiv1\pmod4$。大素数用固定模四的 Mertens 公式得到

$$
\begin{aligned}
\sum_{p\equiv1(4)}\min(\lfloor n/p\rfloor,K)\log p
&\le K\vartheta_1(y)
       +n\sum_{y<p\le n\atop p\equiv1(4)}\frac{\log p}{p}\\
&\le \frac n2\log K+O(n).
\end{aligned}
\tag{4.3}
$$

区间是 $[n/K,n]$，其对数宽度为 $\log K$，不是 $\log(n/D)$。
常数与 $D,k$ 无关。故得到

$$
\boxed{\quad
\sum_{\substack{p\equiv1\ (4)\\p\notin S}}
                \log\|\varphi_D^k\|_p
       \le 2k\log(4D)+O(k),\qquad 1\le D\le k.
\quad}
\tag{4.4}
$$

局部项可能为负，(4.4) 没有把它们删去后再声称等号。
$p>4k$ 时 (3.2) 为零。对 $D>k$，可以用
$D\mapsto\min(D,k)$ 的同一证明给上界，但不因此改变源的维数。

本式是真实普通位混合列的**次数敏感界**，并非中央条件带来的额外项。
当另有理由只需 $D\asymp k^{1/r}$ 的范围时，其显示主系数为
$2/r$。例如 $r=2$ 给 $k\log k$，$r=3$ 给
$(2/3)k\log k$。尚不能直接据此宣布某个 $\alpha$-arithmetic：
定义要求的完整 $(D,k)$ 范围、slopes 累计、惰性位及固定坏位仍须逐项支付。

## 5. 两条实际中央行也有共同 Taylor 前缀表示

本节补齐 R155 的全精度矩阵与普通 Taylor 行之间的接口。
它没有增加已经知道会消失的中央行数。

令 $d=p-1$，$f_p$ 为 R155 的完整单位对数核。在单位处
$pf_p(x)=c_p\log(x^d)$，其中

$$
c_p=\frac{p}{d\log(1+p)}\in\mathcal O^\times;
$$

在非单位处为零。给定精度 $N\ge1$，置 $K=4D$，选择整数 $s\ge2$
满足

$$
s-\lfloor\log_p s\rfloor\ge N+K.
\tag{5.1}
$$

可显式取 $s=N+K+\lceil\log_p(2(N+K))\rceil$。
定义有理 Hermite 多项式

$$
Q_s(Y)=Y^s\left[(1+Z)^{-s}\log(1+Z)\right]_{\deg Z<s}\bigg|_{Z=Y-1},
\tag{5.2}
$$

以及 $q_{p,s}(x)=c_pQ_s(x^d)$。有 $\deg Q_s\le2s-1$，
$Q_s$ 被 $Y^s$ 整除，且在 $Y=1$ 与 $\log Y$ 的前 $s$ 个 jet 相同。
例如 $Q_2=Y^2(Y-1)$、
$Q_3=Y^3((Y-1)-\tfrac72(Y-1)^2)$。

对每个 $0\le j\le K$，在整个 $\mathbb Z_p$ 上准确有

$$
\boxed{\quad
q_{p,s}^{(j)}(x)-(pf_p)^{(j)}(x)\in p^N\mathcal O.
\quad}
\tag{5.3}
$$

这里导数在单位和非单位两个开闭部分分别取，非单位处右项恒为零。
为证明估值，写

$$
(1+Z)^{-s}\log(1+Z)=\sum_{h\ge1}c_{s,h}Z^h.
$$

二项式卷积直接给 $v_p(c_{s,h})\ge-\lfloor\log_p h\rfloor$。
在单位处 $x^d-1\in p\mathbb Z_p$；对余项 $h\ge s$ 作至多 $K$
次微分后，赋值至少为
$h-K-\lfloor\log_p h\rfloor$。函数
$h-\lfloor\log_p h\rfloor$ 不减，故 (5.1) 足够。
在非单位处，$q_{p,s}$ 被 $x^{ds}$ 整除，系数分母至多
$p^{\lfloor\log_p(s-1)\rfloor}$；同样微分后估值至少
$ds-K-\lfloor\log_p(s-1)\rfloor\ge N$。这也证明所有相关导数
整值及余项的逐次微分收敛，未在非单位处使用对数。

令 $q_{p,s}(x)=\sum_{h=s}^{2s-1}q_hx^{dh}$。将 (5.3) 积分于
(1.6)，得到对所有源列同时成立的单一行

$$
\boxed{\quad
p\Lambda_p\bigl(P(w,A_2,B)\bigr)
 \equiv\sum_{h=s}^{2s-1}q_h\Omega_p^{dh}(dh)!\,
                          r_{(d/4)h}(P)\pmod{p^N}.
\quad}
\tag{5.4}
$$

因此同一行只用到 $w$ 阶 $(d/4)(2s-1)$，并且自然参数微分成本
明确是 (5.1) 中的 $4D$。若源的接触阶超过此上限，则实际
$p\Lambda_p$ 在该饱和核上的范数至多 $p^{-N}$。

这比逐列分别截断明确：相同 $q_h$ 同时用于所有混合列。
但 (5.4) 的左边通常不为零。两条原目标的全失败只令
$\Lambda_p(A_2)=\Lambda_p(B)=0$，没有令全部
$\Lambda_p(w^aA_2^bB^c)$ 消失。尤其 R155 的实际单位校准仍在。
若要将该左边消去以改进 (4.4)，仍需实际固定 ODE 或其他全局关系。

## 6. 实际闭包、复增长和目前可用的维数范围

三元组 $(w,A_2,B)$ 的 Zariski 闭包确实为三维；不是为了调整阈值
而自由加入一个辅助变量。

先记 $V=B/A_2-1=R(x^2)-1$。它是非恒定椭圆函数，具有无穷多个
复极点，故不可能代数于 $\mathbb C(w)$，因此 $w,V$ 代数独立。
若 $A_2$ 代数于 $\mathbb C(w,V)$，清分母得到
$P(w,V,A_2)=0$。选 $z_0$ 避开 $V$ 的极点、$A_2$ 的零点，且使
最高 $A_2$ 次数的系数在 $V(z_0)$ 处不是零多项式。

取足够大的正实双周期 $L$，消去 theta 的有限符号。在平方格规范下，
次数六十八的真实截面满足

$$
A_2(z+nL)
 =\exp\bigl(68\eta(L)(nz+n^2L/2)\bigr)A_2(z),
\qquad \eta(L)L>0,
\tag{6.1}
$$

而 $V(z+nL)=V(z)$。在 $z_0+nL$ 上，多项式关系的系数只以 $n$
的多项式速度增长，其非零最高系数仅可能在有限多个 $n$ 上为零。
代数根界因此迫使 $A_2(z_0+nL)$ 至多多项式增长，与 (6.1) 的
$\exp(cn^2+O(n))$ 矛盾。故 $w,V,A_2$，也即 $w,A_2,B$ 代数独立。
这个论证也给两个平面子图像的维数为二。

全部函数四重不变且在 $z$ 上整、增长阶至多二，所以作为 $w=z^4$
的整函数，其阶至多 $1/2$。三维射影映射可取
$[1:w:A_2:B]$；所有 Taylor 系数有理，原点为 $\mathbb Q$ 点，
无需 R152 中额外的次数二闭点模型。

因此已核的 Herblot 几何阈值分别是平面模型 $\alpha<1$、三维模型
$\alpha<4/3$。不过 (4.4) 目前仅支付普通位、且保留 $\log D$。
它在 $D\asymp\sqrt k$ 或 $D\asymp k^{1/3}$ 的显示值，不能替代
完整 arithmeticity 定义中的所有次数和全部位。本文也没有借
三维模型的 $D^3$ 截面数沿用平面 $D^2$ 的 slopes 计算。

## 7. 只取两条实际 theta 坐标时，普通成本为零

另一个真正固定的源模型是

$$
\gamma_2(w)=(A_2(w),B(w))\in\mathbb A^2_{\mathbb Q},
\qquad
\mathscr P_D^{(2)}=\bigoplus_{b+c\le D}\mathbb Z X^bY^c.
\tag{7.1}
$$

这里没有自由的 $w$ 源列。两个坐标的代数独立性由§6立即得到；
它们在 $w$ 上整、有限型阶至多 $1/2$，基点为 $(0,0)$，且
$A_2'(0)=1$，故仍是一条平滑形式曲线，不是去掉参数后的常值图像。

现在 (1.6) 中只剩 $a=0$。因此 (2.5) 可以取
$e_p=v_p((4k)!)$，最高阶乘完全抵消，得到对所有 $D,k$ 的
**实际饱和 jet** 结论

$$
\boxed{\qquad
\|\varphi_{D,2}^k\|_p\le1
\quad\text{对全部上述普通 }p.
\qquad}
\tag{7.2}
$$

也可用实际 $V$ 参数直接核定：$V=-22w+\cdots$，而
$A_2=F(V),B=(1+V)F(V)$ 均在 $\mathcal O[[V]]$。
对同一个 $P$，在 $w$ 或 $V$ 中的全部前缀核相同；若低于 $k$ 的项
全为零，第 $k$ 系数只乘 $(-22)^{\pm k}$。这是单位，即使反向
$w(V)$ 的更高系数并不整也没有额外成本。整 $V$ 系数因此直接给 (7.2)。

这个换参数不把 $V$ 添加为自由的 ambient 坐标。准确的源基来自整线性
变换 $(X,Y)\mapsto(X,Y-X)$，在实际曲线上是

$$
X^{j-c}(Y-X)^c\longmapsto F(V)^jV^c,
\qquad 0\le c\le j\le D.
\tag{7.3}
$$

不能把右边扩大成任意 $V^aF^b$ 的另一个次数格。

所以这个真实平面的全普通预算为非正，固定坏位仍只有 $O(k+D)$。
R159 的直接 slopes 命题应用于它时，所需惰性严格门槛变为
$a_I+2b_I<2$。本文没有支付该惰性界，也没有把两条中央导数零性
用于 (7.2)；它仅避免为不需要的自然参数源列付普通微分成本。

## 来源与依赖

- [R155](../results/R155-two-theta-rows-common-amice-lattice.md)：真实普通
  整测度、完整单位核及分布微分规范；本篇 (1.4)–(1.7) 使用同一对象。
- [R117 的实际卷积证明](2026-11-12-two-rank-two-theta-linear-convolution.md)：
  $A_2,B,R$ 的固定恒等式与共同 theta 次数。
- [R151](../results/R151-joint-central-failure-and-saturated-jet-rows.md)：
  真正饱和前缀格及同一行的对偶判据；固定模四 Mertens 估计亦沿用该文。
- [R152](../results/R152-all-degree-euler-stokes-gauge-isometry.md)：
  平方格准周期、增长规范及 Herblot 闭点次数／维数的准确约定。
- (2.3)、(2.5)、(3.2)、(4.4)、(5.3) 与 (5.4) 均由本文所显示的
  整数多项式、实际分布和估值直接证明，不依赖原中央非零猜想。
