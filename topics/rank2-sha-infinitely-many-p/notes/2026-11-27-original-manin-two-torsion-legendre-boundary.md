# 原 Manin 特殊值的 Legendre 返回与完整 Rodrigues 边界

状态：下列恒等式全部针对 R1043 的同一个多项式和规范截面，均有完整证明。它们把原规范纤维读数返回一个有限整数卷积；尚未证明该卷积对无穷多个所需素数非零，因而不将原特殊值非零门标为完成。

依赖：[R1043 §§19–22](../results/R1043-original-two-isogeny-level-transport-and-weighted-orbit-reduction.md)，尤其其 (111)、(112)、(119)、(131)、(132)。不新增数学运行，不重算已完成的 $q=11$ 截面或 Manin 回执。

## 1. 同一参数、同一实际二挠点

设 $q>5$ 为素数，
$$
 q=6n+5=6r-1,\qquad r=n+1,\qquad M=2n+1=(q-2)/3.
 \tag{1}
$$
本篇的 $q$ 是几何辅助特征。原通常全 $\Sha$ 的检测素数仍另记 $p$，不把两者混同。

R1043 的原基曲线及坐标是
$$
 B:\quad X^3=Y(Y+1),\qquad
 V=2Y+1,\qquad V^2=1+4X^3,\qquad
 t=(1-V)/54.
 \tag{2}
$$
因此 $X^3=-1/4$ 准确等价于 $V=0$、$Y=-1/2$。在原 $B$ 上，负元为 $(X,V)\mapsto(X,-V)$；这三个点恰是三个非零二挠点。这里没有把它们替换成另一个同 $j$ 的模型，也没有先指定新的 CM 周期。

沿用原归一
$$
 H_q(U)=\sum_{j=0}^{n}h_{q,j}U^j,\qquad
 h_{q,j}=(-4)^j\frac{(5/6)_j(2/3)_j}{j!^2},
$$
$$
 P_q(U)=\sum_{j=0}^{n}\frac{h_{q,j}}{3j+1}U^j,\qquad
 A_q(t)=V H_q(X^3).
 \tag{3}
$$
所有分母都是 $q$ 单位，$P_q(0)=1$。这里 $(a)_j$ 为上升阶乘。

当原最短截面存在并满足 R1043 的好约化前提时，仍用其已付规范
$$
 \mu(Q_{\min})=c_Q X P_q(X^3),\qquad c_Q\in\delta\mathbf F_q^\times.
 \tag{4}
$$
纯多项式恒等式 (3) 及下述证明对每个 (1) 的素数成立；涉及实际截面和三权下降的结论，则保留 R1014/R1043 原来的充分大 $q$ 及有限坏集前提。

## 2. 原 Hasse 多项式正是指定的 Legendre 多项式

令 $\mathcal L_M(Z)$ 是由
$$
 \mathcal L_M(1-2z)
   =\sum_{j=0}^{M}\frac{(-M)_j(M+1)_j}{j!^2}z^j
 \tag{5}
$$
定义的 Legendre 多项式，归一为 $\mathcal L_M(1)=1$。

由 $q=3M+2$，
$$
 -M\equiv2/3,\qquad M+1\equiv1/3\pmod q.
$$
而原 $27t=(1-V)/2$，故逐个系数给
$$
 \boxed{A_q(t)=\mathcal L_M(V)\quad\text{于 }\mathbf F_q[V].}
 \tag{6}
$$
更明确地，
$$
 \frac{(1/3)_j(2/3)_j}{j!^2}(27t)^j
   =\frac{(3j)!}{j!^3}t^j;
$$
原 Hasse 多项式截于 $j=M$，与 (5) 的终止位置相同。所有所用阶乘的指标均小于 $q$，故此比较没有先除一个 $q$ 因子。

因 $M$ 为奇数，$\mathcal L_M$ 为奇多项式，(6) 也直接核回 (3) 中的 $V H_q$ 分解。它不是另选的 Legendre 近似。

## 3. 原积分常数由两个端点和次数上界完全固定

在 $\mathbf F_q[V]$ 中置
$$
 \mathcal F_q(V)
 =\frac32(V^2-1)^{M+1}
       P_q\bigl((V^2-1)/4\bigr).
 \tag{7}
$$
其次数不超过
$$
 2(M+1)+2n=3M+1=q-1.
$$
由 (3) 有 $P_q(U)+3U P_q'(U)=H_q(U)$。又
$3(M+1)=q+1=1$ 于 $\mathbf F_q$，故直接求导得
$$
 \mathcal F_q'(V)
 =(V^2-1)^M V
 \left(P_q\bigl((V^2-1)/4\bigr)
       +3\frac{V^2-1}{4}P_q'\bigl((V^2-1)/4\bigr)\right)
 =(V^2-1)^M\mathcal L_M(V).
 \tag{8}
$$
并且 $\mathcal F_q(1)=0$。次数小于 $q$ 的多项式中，导数及这个端点值唯一确定原函数；因此没有一个未付的 $q$ 次幂或水平常数。

定义有理数
$$
 I_M=\int_0^1(1-v^2)^M\mathcal L_M(v)\,dv.
 \tag{9}
$$
这里只是有限多项式逐项积分的有理数，不是一个尚未归一的 $q$-adic 积分。被积多项式次数为 $3M=q-2$，故积分所除的整数都在 $1,\ldots,q-1$；$\mathcal L_M$ 本身仅有 $2$ 的分母。因此 $I_M$ 在 $\mathbf Z_{(q)}$ 中，可以准确约化。

由于 $M$ 奇、$M+1$ 偶，(7)–(9) 给
$$
 \mathcal F_q(0)=\frac32P_q(-1/4)
 =I_M\pmod q.
$$
即
$$
 \boxed{P_q(-1/4)=\frac23I_M\pmod q.}
 \tag{10}
$$
式 (10) 是模 $q$ 恒等式，不声称两边在有理数域逐项相等。

## 4. 完整 Rodrigues 边界式

令 $f(v)=(v^2-1)^M$。由 (5) 的二项式展开可逐系数验证 Rodrigues 式
$$
 \mathcal L_M(v)=\frac{f^{(M)}(v)}{2^M M!}.
 \tag{11}
$$
定义有限双线性表达
$$
 \mathcal B(v)=
 \sum_{j=0}^{M-1}(-1)^j
 f^{(j)}(v)f^{(M-1-j)}(v).
$$
求导后相邻项严格抵消；因 $M-1$ 偶，剩下
$$
 \mathcal B'(v)=2f(v)f^{(M)}(v).
 \tag{12}
$$
对 $0\le j<M$，$f^{(j)}(1)=0$，所以 $\mathcal B(1)=0$。在 $v=0$，只有 $j=2k$ 项留下，而
$$
 f^{(2k)}(0)=
 (2k)!(-1)^{M-k}\binom Mk.
$$
于是
$$
 \mathcal B(0)=(-1)^n C_n,
$$
$$
 C_n=
 \sum_{k=0}^{n}
 (2k)!(2n-2k)!
 \binom{2n+1}{k}\binom{2n+1}{n-k}.
 \tag{13}
$$
结合 (9)、(11)、(12)，得到有理数域中的精确恒等式
$$
 \boxed{
 I_{2n+1}=
 \frac{(-1)^n C_n}
 {2^{2n+2}(2n+1)!}.
 }
 \tag{14}
$$
因此原特殊值准确为
$$
 \boxed{
 P_q(-1/4)=
 \frac{(-1)^n C_n}
 {3\cdot2^{2n+1}(2n+1)!}\pmod q.
 }
 \tag{15}
$$
这里 $C_n$ 是显式正整数；但正整数本身仍可能被 $q$ 整除，故 (13) 的实正性不支付 (15) 的非零。

原 R1043 (132) 的规范纤维读数是
$-3c_Q2^{2r-1}P_q(-1/4)$。因为 $2r-1=2n+1$，所有这几个固定幂严格相消，得到同一实际三权下降截面的完整式
$$
 \boxed{
 \mu_{\min}(P_Q)(O)
  =\frac{(-1)^{n+1}c_Q}{(2n+1)!}\,C_n.
 }
 \tag{16}
$$
此式没有改 $P_Q$、源二商、原 $\omega$ 权或微分规范，也没有把 $\mu_{\min}$ 改称抽象纤维点值。

## 5. 同一值的终止超几何形式与尚未付的整数条件

从 (3) 还可完全有限地写成
$$
 P_q(-1/4)=
 \sum_{j=0}^{n}
 \frac{(5/6)_j(2/3)_j(1/3)_j}
 {(1)_j(4/3)_j\,j!}\pmod q.
$$
用
$$
 (5/6,2/3,1/3,4/3)
 \equiv(-n,-2n-1,2n+2,2n+3)\pmod q
$$
逐系数返回有理终止和
$$
 S_n={}_3F_2
 \left(\begin{matrix}-n,-2n-1,2n+2\\1,2n+3\end{matrix};1\right)
 =\sum_{j=0}^{n}
 \binom nj\binom{2n+1}{j}
 \frac{2n+2}{2n+2+j},
 \tag{17}
$$
$$
 P_q(-1/4)\equiv S_n\pmod q.
 \tag{18}
$$
(17) 的分母均小于 $q$，且也等于
$$
 (2n+2)\int_0^1x^{2n+1}
 {}_2F_1(-n,-2n-1;1;x)\,dx.
$$
这与 (10) 是同一模 $q$ 值的两个不同有理提升，不将它们在特征零直接相认。

由 (15)–(16)，在原几何好范围中，准确剩余问题是
$$
 C_n\not\equiv0\pmod{6n+5}
 \quad\text{对无穷多个素数 }6n+5.
 \tag{19}
$$
本篇没有证明 (19)，也没有把分子实数非零、有限个已付实例，或上下超几何参数相差整数后的半单角色取消，替代 (19)。即使 (19) 后续付清，原 degree17 标记、全部 $\eta$ 权及全 corestriction 的非零消费仍须沿 R1043 的既定图逐项返回。



## 6. Wilson 返回的准确中央二项式段

本节只给 (19) 的一个完整有限重写，不把它作为已付非零。
仍令 $M=2n+1$，并置
$$
 N=3n+2=(q-1)/2,\qquad L=4n+3.
$$
则
$$
 \boxed{
 C_n\equiv
 -\frac{M!^2}{4^{2n+2}L!^2}
 \sum_{a=n+1}^{2n+1}
       \binom La\binom L{N-a}\pmod q.
 }
 \tag{20}
$$
显示的阶乘和 $4$ 的幂全是 $q$ 单位。

为逐项证明，先把 (13) 的第 $k$ 项写为
$$
 T_k=\frac{M!^2(2k)!(2n-2k)!}
 {k!(n-k)!(M-k)!(n+1+k)!}.
$$
Wilson 恒等式 $(q-1)!=-1$ 给
$$
 (2n-2k)!\equiv-\frac1{(4n+4+2k)!}.
$$
使用
$$
 (2j)!=4^j j!(1/2)_j,\qquad
 (1/2)_j\equiv(-1)^j\frac{N!}{(N-j)!}
 \quad(0\le j\le N),
$$
其中 $j=k$ 或 $j=2n+2+k\le N$，完整相消得
$$
 T_k\equiv-\frac{M!^2}{4^{2n+2}}\,
 \frac1{(N-k)!(M-k)!(n+1+k)!(2n+2+k)!}.
 \tag{21}
$$
没有把 $(2k)!\binom Mk$ 错写成另含 $1/k!$ 的指数级数。
在 (21) 置 $a=n+1+k$，则
$$
 L-a=N-k,\qquad N-a=M-k,\qquad
 L-(N-a)=2n+2+k,
$$
于是 (20) 逐项成立。

这个中央段不能替换成完整 Vandermonde 和。完整和准确为
$$
 \sum_{a=0}^{N}\binom La\binom L{N-a}
 =\binom{2L}{N}\equiv0\pmod q.
 \tag{22}
$$
最后的零也不需任何未知同余定理：
$2L=q+M$，而在 $\mathbf F_q[Z]$ 中
$(1+Z)^{q+M}=(1+Z^q)(1+Z)^M$；
因 $M<N<q$，其 $Z^N$ 系数为零。
对称性 $a\leftrightarrow N-a$ 进一步给
$$
 \sum_{a=n+1}^{2n+1}\binom La\binom L{N-a}
 \equiv-2\sum_{a=0}^{n}\binom La\binom L{N-a}\pmod q.
 \tag{23}
$$
因此所需的是 (20) 的中央段或 (23) 的准确短尾非零；
完整和为零既不证明，也不否定这个问题。

最后标明此读者的几何范围。对任意与 $q$ 互素的整数 $b$，
原 Manin 同态及 (111) 给
$$
 \mu([b]Q)=b\,\mu(Q),\qquad
 c_{[b]Q}=b\,c_Q,\qquad
 \frac{\mu([b]Q)}{c_{[b]Q}}
   =\frac{\mu(Q)}{c_Q}=X P_q(X^3).
 \tag{24}
$$
所以规范多项式本身不记录某个目标 $p\ne q$ 的饱和指数。
原最短截面的高度和本原性仍全部保留；(24) 不声称 $[b]Q$
也是最短截面。它只是说明：要将 (16) 的特征 $q$ 非零消费为
R1043 (77)–(78) 的 degree17 实际点群模 $p$ 非零，仍必须
支付同一个有权评价映射及其饱和性，不能仅靠 (20) 的非零。
