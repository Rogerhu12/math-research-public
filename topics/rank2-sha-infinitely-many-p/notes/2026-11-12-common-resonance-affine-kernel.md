# 一个真正取共同共振的固定仿射核

日期：2026-11-12。**状态：固定曲线、精确局部深度、非代数性及实际 jet 上界均已证明；所得常数尚未改进原来的总预算。**

本篇构造新的固定 $\mathbb Q$-germ。它在惰性素数处把两个分母条件取交集，
同时保留全平面亚纯一致化。没有把逐素数选取的 Bézout 系数拼成一个“固定函数”。

## 1. 固定数据与形式解

仍取
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad b=2+i,\quad u=\frac b{\bar b}=\frac{3+4i}{5}.
$$
于是 $N(u)=1$、$|u|_{\mathbb C}=1$，且 $u$ 不是根单位。
令 $\ell_0=(\ell+\ell\circ[i])/2$，其中 $\ell=\delta\log\Phi$。
此前已经证明 $\ell_0$ 非零、在原点至少四阶消失，且所有极点均简单，
属于本原 $f$-division 点。后一条来自 R19 的零极点描述；
取 $[i]$-平均只会消去某些极点，不会引入非本原点。

记
$$
h(z)=\ell_0(\operatorname{Exp}_Ez)
=\sum_{\substack{k\ge4\\4\mid k}}h_kz^k,\qquad
\sigma_aF(z)=F(az).
$$
定义固定算子
$$
\mathcal D=\sigma_2-\frac{\sigma_u+1}{2},
\qquad
q_k=2^k-\frac{u^k+1}{2}.
\tag{1.1}
$$
由于 $|u|=1$，
$$
|q_k|\ge2^k-1>0\qquad(k\ge1).
$$
因此对任意固定 $m\ge1$，存在唯一常数项为零的正则形式解
$$
\mathcal D^mG_m=h,\qquad
G_m(z)=\sum_{\substack{k\ge4\\4\mid k}}\frac{h_k}{q_k^m}z^k.
\tag{1.2}
$$
换回 $t$ 坐标后 $G_m\in K[[t]]$。其常数项和一次项均为零。

## 2. 严格收缩展开与二阶复增长

由几何级数的高阶版本，令 $C_n=\binom{m+n-1}{n}$，有精确恒等式
$$
\boxed{\quad
G_m(z)=\sum_{n\ge0}C_n2^{-n}
\sum_{j=0}^n\binom nj
h\!\left(\frac{u^jz}{2^{m+n}}\right).
\quad}
\tag{2.1}
$$
逐系数核对即为
$$
\frac1{q_k^m}
=\sum_{n\ge0}C_n\,2^{-(m+n)k}
\left(\frac{1+u^k}{2}\right)^n.
$$
同一层的系数绝对值之和为 $C_n$；
全部实际参数的模都为 $2^{-(m+n)}$，没有未缩小的无限旋转逆。

在任意固定紧集上，当 $n$ 足够大时，
$$
\left|h\!\left(\frac{u^jz}{2^{m+n}}\right)\right|
\le C|z|^4\,2^{-4(m+n)}
$$
对 $0\le j\le n$ 一致成立。因此尾和正常收敛。
任意紧集上只有有限层可能出现极点，而每层只有有限项，
所以 $G_m$ 为全平面亚纯函数。

它的 Nevanlinna 特征满足
$$
T(R,G_m)=O(R^2).
\tag{2.2}
$$
确实，固定椭圆函数 $h$ 满足 $T(R,h)=O(1+R^2)$。
取 $N=O(\log R)$，把 $n>N$ 放入上述一致收敛尾项。
前面的各个函数项之特征和由
$$
R^2\sum_{n\ge0}(n+1)4^{-(m+n)}=O(R^2)
$$
控制；有限项常数和系数的贡献只有
$O((\log R)^2\log\log(R+3))$。
尾项在圆盘内全纯，其上确界至多为 $\log R$ 的固定次幂，
所以特征贡献为 $O(\log\log(R+3))$。

对稍后使用的图像映射，所需增长概念是 Herblot Definition 5.1。
不能仅凭“全平面亚纯”替代它。为避免对整数阶的有限型分解作额外断言，
这里对每个 $\varepsilon>0$ 构造阶数至多 $2+\varepsilon$ 的整函数
齐次表示 $(D,N)$。本例的极点计数直接给出：
第 $n$ 层至多 $(n+1)$ 个缩放格，其极点密度为
$O((n+1)4^{-n})$，故总零计数为 $O(R^2)$。
相应的 genus-two canonical product 消去极点，并满足
$\log M(R,D)=O_\varepsilon(R^{2+\varepsilon})$。
令 $N=DG_m$，它是整函数；由
$T(R,N)\le T(R,D)+T(R,G_m)+O(1)$ 及整函数的 Poisson 估计，
同样有 $\log M(R,N)=O_\varepsilon(R^{2+\varepsilon})$。
这给所需齐次截面，已足以把 Herblot 的最终阈值取到 $\rho=2$ 的极限。
本篇下面的预算比较只使用这个任意 $\rho>2$ 的版本。

## 3. 共轭迹仍非代数

定义
$$
\mathcal H_m(t)=G_m(t)+\overline{G_m}(t)\in\mathbb Q[[t]].
\tag{3.1}
$$
共轭项对应 $u\mapsto u^{-1}$ 和 $\ell_0\mapsto\bar\ell_0$。
两项均有 (2.2) 的增长界。

取 $\ell_0$ 的一个极点 $s$，其非零留数为
$r_s=\operatorname{Res}_s\ell_0\omega_E$。
写 $\Lambda=\Omega\mathbb Z[i]$。
选择 $s$ 的复对数
$$
z_s=\Omega\eta/f,
$$
其中 $\eta$ 是模 $f$ 的单位，并用 CRT 使 $(\eta,5)=1$。
令
$$
z_n=2^{m+n}u^{-1}z_s,\qquad n\ge1.
$$
在 (2.1) 中，只有指标恰为 $(n,j=1)$ 的项在 $z_n$ 有极点：

- 若 $j\ne1$，参数中残留非零次 $u^{j-1}$，其 $b$ 或 $\bar b$ 分母
  不能被 $\eta$、$f$、$2$ 消去，故不是 $f$-division 点；
- 若 $j=1$ 而层数小于 $n$，相应点是 $[2]^a s$，$a>0$，
  已失去本原 $f$-division 的二初级部分，不是 $\ell_0$ 的极点；
- 若层数大于 $n$，会出现不能消去的额外二初级分母。

于是留数准确为
$$
\boxed{\quad
\operatorname{Res}_{z_n}G_m(z)\,dz
=2^m u^{-1}\,n C_n r_s.
\quad}
\tag{3.2}
$$
其模按 $n^m$ 增长。
共轭项的每一层都含 $u^{-j-1}$，$j\ge0$，由同一个五初级分母论证，
它在 $z_n$ 正则。因此迹的留数仍为 (3.2)。

这些 $z_n$ 在 $E$ 上的像属于一个固定有限扭点集合，例如 $E[5f]$。
乘以足够多次 $2$ 后，二初级部分消失，剩余部分上的 $[2]$ 为置换。
故可取一个无限子序列，使它们投影到同一个代数点。
若 $\mathcal H_m$ 代数于 $\overline{\mathbb Q}(E)$，
该固定点处只能有有限多个代数 Laurent 分支，也只能有有限多个留数。
这与 (3.2) 矛盾。因此
$$
\boxed{\mathcal H_m\text{ 不代数于 }\overline{\mathbb Q}(E).}
\tag{3.3}
$$
其图像仍在 $\mathbb Q$-曲面 $E\times\mathbb P^1$ 中稠密。

## 4. 惰性处恰为两个深度的最小值

设 $p\equiv3\pmod4$、$p\nmid10$。
在 $K_p/\mathbb Q_p$ 中，$u$ 为范数一的单位。
对任意 $k\ge1$ 置
$$
x=2^k,\quad y=u^k,\quad t=x-1,\quad
q=q_k=t-\frac{y-1}{2}.
$$
这里 $x\in\mathbb Z_p^\times$、$y\bar y=1$。
将 $y=1+2(t-q)$ 代入范数一等式，得到
$$
t(t+1)
=-q\bar q+\left(t+\frac12\right)(q+\bar q).
\tag{4.1}
$$
若 $s=v_p(q)$，右边的赋值至少为 $s$。
因为 $t+1=x$ 是单位，故 $v_p(t)\ge s$，
再由 $y-1=2(t-q)$ 得 $v_p(y-1)\ge s$。
反向不等式由 $q=t-(y-1)/2$ 直接给出。
所以
$$
\boxed{\quad
v_p(q_k)=\min\{v_p(2^k-1),v_p(u^k-1)\}.
\quad}
\tag{4.2}
$$
这是完整深度等式，不只是模 $p$ 的共同零点比较。
特别地，其分母支撑确实取两个共振集合的交集。

这也解释了为什么一个纯几何的“极点不可能只落在余维二交集”论证
不能排除本核：沿惰性剩余域中的实际点，额外有
$x\in\mathbb F_p^\times$、$y^{p+1}=1$。
仿射直线 $x-1-(y-1)/2=0$ 与这个范数条件只给 $x=1,y=1$，
另一个交点是 $x=0,y=-1$，而 $x=2^k$ 从不取零。
这不是把算术点的整性误作有理函数的几何局部整性。

## 5. 阶数、提升深度与实际图像大小

记
$$
a_p=\operatorname{ord}_{\mathbb F_p^\times}(2),\qquad
r_p=\operatorname{ord}_{\mathbb F_{p^2}^\times}(u),\qquad
d_p=\operatorname{lcm}(a_p,r_p),\qquad
D_p=\operatorname{lcm}(d_p,4).
$$
有 $a_p\mid p-1$、$r_p\mid p+1$、$p\nmid D_p$。
置
$$
c_p=\min\{v_p(2^{a_p}-1),v_p(u^{r_p}-1)\}\ge1.
$$
式 (4.2) 与提升指数公式给出
$$
v_p(q_k)=
\begin{cases}
0,&d_p\nmid k,\\
c_p+v_p(k/d_p),&d_p\mid k.
\end{cases}
\tag{5.1}
$$
在本篇只有 $4\mid k$ 的权，因此首个共振权为 $D_p$。

高度二形式群的对数与指数估计、整 tame 分解及图像直化，
与此前的加法 CM 笔记相同。这里 $\sigma_2,\sigma_u$ 都是整 CM 形式自同态，
因为只排除了固定素数 $2,5$。
非共振块上的 $\mathcal D$ 在 $(p,t)$ 完备拓扑中有整逆，
其剩余标量由 (4.2) 为单位。
共振块则由 (5.1) 得到
$$
S_p(\widehat{\operatorname{graph}}G_m)
\ge p^{-s_p},\qquad
s_p=\frac1{p^2-1}+\frac{m c_p}{D_p-1}.
\tag{5.2}
$$
具体地，在 $z$ 坐标中的系数满足
$$
v_p(h_k)\ge-\frac{k-4}{p^2-1},\qquad
c_p+v_p(n)\le c_p n\le\frac{c_p(D_pn-1)}{D_p-1}.
$$
再用整缩放后的 $\log_E$ 复合，即得
$v_p([t^k]G_m)\ge-s_p(k-1)$，
从而 $(t,y)\mapsto(t,y-G_m(t))$ 真正直化相应圆盘中的图像。

对共轭迹，惰性处的 $a_p,r_p,c_p,D_p$ 不变。
同一截断预算适用于 $\mathcal H_m$；
当 $D_p>k$ 时，前 $k$ 阶仍整。

## 6. 完整惰性求和常数

定义
$$
M(k)=\sum_{D_p\le k}c_p\log p,\qquad
W(k)=\sum_{D_p\le k}\frac{c_p\log p}{D_p-1}.
$$
Primitive 因子给
$$
\sum_{a_p=a}c_p\log p\le\log|\Phi_a(2)|,
\qquad
\sum_{r_p=r}c_p\log p
\le\log|\Phi_r(b,\bar b)|\quad(r>1).
\tag{6.1}
$$
$r=1$ 只有固定有限例外。
一边用 $\log|\Phi_a(2)|=\varphi(a)\log2+O(1)$，
另一边用已经独立核过的 Stewart Lemma 4.1：
$$
\log|\Phi_r(b,\bar b)|
=\frac{\varphi(r)}2\log5
+O(2^{\omega(r)}\log(r+1)).
\tag{6.2}
$$
相应累计误差为 $O(x\log^2x)$。

还可使用 $(2/p)$ 的准确奇偶限制：
$$
\begin{array}{c|c|c}
p\bmod8&a_p&r_p\text{ 的二进阶}\\ \hline
3&v_2(a_p)=1&v_2(r_p)\le2\\
7&a_p\text{ 奇}&\text{无额外限制}.
\end{array}
$$
由 $\gcd(a_p,r_p)\mid2$，准确的首权表为
$$
\begin{array}{c|c|c}
&r_p\text{ 条件}&D_p\\ \hline
a_p\text{ 奇}&r_p\text{ 奇}&4a_pr_p\\
a_p\text{ 奇}&v_2(r_p)=1&2a_pr_p\\
a_p\text{ 奇}&v_2(r_p)\ge2&a_pr_p\\
v_2(a_p)=1&r_p\text{ 奇}&2a_pr_p\\
v_2(a_p)=1&v_2(r_p)=1&a_pr_p\\
v_2(a_p)=1&v_2(r_p)=2&a_pr_p/2.
\end{array}
\tag{6.3}
$$

对 $a_p$ 奇数部分按 $a_p\le x$ 和 $a_p>x$ 划分，
并分别控制三种 $r_p$。
使用
$\sum_{n\le x,n\text{ 奇}}\varphi(n)\sim2x^2/\pi^2$、
$\sum_{n\le x,v_2(n)=j}\varphi(n)\sim x^2/(2^j\pi^2)$，
得到二次主项
$$
\frac1{\pi^2}
\left(2\log2\,x^2+\frac{3\log5}{8}\frac{k^2}{x^2}\right).
$$
优化后常数为 $\sqrt{3\log2\log5}/\pi^2$。

对 $a_p$ 偶数部分，$r_p$ 只需列出二进阶 $0,1,2$，
对应主项为
$$
\frac1{\pi^2}
\left(\frac{\log2}{2}x^2+\log5\,\frac{k^2}{x^2}\right).
$$
优化后常数为 $\sqrt{2\log2\log5}/\pi^2$。
两边的最优 $x$ 都是 $\sqrt k$ 的固定倍数，因此
$$
\boxed{\quad
M(k)\le C_{\rm aff}k+O(\sqrt k\log^2k),\qquad
W(k)\le C_{\rm aff}\log k+O(1),
\quad}
\tag{6.4}
$$
其中
$$
C_{\rm aff}=
\frac{\sqrt3+\sqrt2}{\pi^2}\sqrt{\log2\,\log5}
=0.3367017014\ldots.
\tag{6.5}
$$
第二式由此前已写出的分部求和公式直接得到。
因此 $m=3$ 的惰性 jet 预算系数为
$3C_{\rm aff}=1.0101051043\ldots$。
它尚大于原单乘子 $\mu_4$ 方案的 $0.9450820411\ldots$；
本构造证明共同共振与全平面一致化可以兼容，并未虚称常数已改善。

## 7. 普通目标角色中的确切中心比较

现在设 $p$ 为本题的良好分裂素数，另排除 $p=5$。
$2,u\in\mathbb Z_p^\times$，$\sigma_2,\sigma_u$ 是除法塔中相应的 Galois 元。
在单位模上使用算子
$$
\mathcal B=\frac12\sigma_2-\frac1{2u}\sigma_u-\frac12.
\tag{7.1}
$$
链式法则准确给
$$
\delta\log(\mathcal B v)=\mathcal D(\delta\log v).
\tag{7.2}
$$
这里单位模按加法记号书写，所有系数都是 $\mathbb Z_p$ 中的整元。

在 $\chi$ 块上，令
$r_a=\log\langle a\rangle/\log(1+p)$。
其 Iwasawa 符号是
$$
\mathcal B(T)=
\left(\frac{1+T}{1+p}\right)^{r_2}
-\frac12\left(\frac{1+T}{1+p}\right)^{r_u}
-\frac12.
\tag{7.3}
$$
所以 $\mathcal B(p)=0$，而除以 $T-p$ 的商为单位，当且仅当
$$
v_p\!\left(\log 2-\frac12\log u\right)=1.
\tag{7.4}
$$
等价地，固定数
$$
v=\frac4u
$$
在该分裂处满足 $v_p(v^{p-1}-1)=1$。
这只是固定代数数的一个非 Wieferich 条件；本篇未证明其对无穷多个 $p$ 成立。
$\log v\ne0$ 因 $v$ 是局部单位且不是根单位，
但逐点非零不给 (7.4) 的统一深度一。

若本题的中心整除假设给 $(T-p)^m\mid H_p(T)$，
并且 (7.4) 成立，则可在整单位模中解
$\mathcal B^m v=e_\chi\Phi$。
由 (7.2)，$\delta\log v$ 是 $e_0\ell_0$ 的整 $\mathcal D^m$ 逆像。
它与本篇 $e_0G_m$ 仅差一个整常数，减掉该常数后得到
$$
e_0G_m\in\mathbb Z_p[[t]].
\tag{7.5}
$$
这保留了所需 ordinary 目标块接口。
其余 tame 块及 (7.4) 失败时的额外小除数尚未得到统一控制。

## 8. 后续真正需要的改进

本篇已经给出固定 $\mathbb Q$-germ、非代数性、实际复一致化，
以及没有随 $p$ 变化的共同分母核。
待改进的是这个实际对象的算术预算，而不是重新证明上述形式存在性。
可继续研究多个独立 norm/angle 约束能否放入一个同样具有严格收缩展开的核，
或改进 (6.4) 的实际共同素因子质量。
单对 $S$-unit gcd 的小量界还不能无损求和到整个双指标区域。

## 来源与依赖

- R19：$\Phi$ 的本原 $f$-division 零极点及准确对数矩。
- 本课题的加法 CM 逆像、惰性加权和、Herblot jet 接口三篇笔记。
- C. L. Stewart，*On divisors of Lucas and Lehmer numbers*，
  Acta Math. 211 (2013)，Lemma 4.1；
  [出版原文](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s11511-013-0105-y.pdf)。
- M. Herblot，*Algebraic points on meromorphic curves*，
  [作者原文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)，
  Definition 5.1、Theorem 6.1。
- 新核、深度等式、收缩展开、单边极点证明及上述常数均在本文直接证明。
