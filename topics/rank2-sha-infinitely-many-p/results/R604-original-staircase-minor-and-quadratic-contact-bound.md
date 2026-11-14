# R604 — 原两来源的整截面、单位阶梯子式与二次接触上界

日期：2026-11-14。**状态：已证明。**

本篇把 R600 的逐余类首层接到原 $S/T$ 全列格的一个显示方阵。按来源总次数排列，方阵的对角块是公差 $38pc$ 的 Vandermonde；高次数列在相应低余类严格为零。因此在 $D<s=(p+1)/6$ 的实际范围，原正规化方阵行列式为单位，并给出真正全前缀的空区间。

该论证比先把全部 theta 权分组更强：无需假设 $p>72D$，也不要求不同总次数间的权不碰撞。它还给原两个固定函数的 $O(D^2)$ 特征零接触上界。选定非连续行的行列式不被当成真正连续饱和旗标的成本；本篇明确展示两者的区别。

## 1. 固定原格和同权的真实整截面

保持 [R596](R596-original-pole-reconstruction-and-full-prefix-central-constraints.md) 与 [R600](R600-original-central-residue-blocks-and-true-prefix-vandermonde.md) 的原共同曲线 $E_b:y^2=x^3+b$，$b=17$，以及
$$
\Theta=x\sigma^2,\qquad \tau=-b/x^3,\qquad w=z^6.
$$
实际来源为
$$
S=b^{-1}\Theta^{17}f(\tau),\qquad
T=b^{-1}\Theta^{36}f(\tau)V(\tau),
\tag{1}
$$
$$
f(\tau)=\tau(\tau-1)(16\tau^2+4\tau+7)(1+8\tau)/7,
$$
$$
V(\tau)=(1-4\tau)(1-20\tau-8\tau^2)
       (1+96\tau+48\tau^2-64\tau^3).
\tag{2}
$$
二者都以 $w$ 为首项。只使用原格
$$
E_{D,2}
=\bigoplus_{\mu+\nu\le D}\mathcal O\,S^\mu T^\nu,
\qquad M_D=\binom{D+2}{2}.
\tag{3}
$$

记单项式的 theta degree 为
$$
m=34\mu+72\nu=2n,\qquad q=\mu+\nu.
$$
由 (1)，它是同一真实线丛 $\mathcal O(mO)$ 的截面
$$
S^\mu T^\nu
=\sigma^m\,
 b^{-q}x^n f(-b/x^3)^q V(-b/x^3)^\nu .
\tag{4}
$$
这里的有理因子实际上在 $E_b\setminus\{O\}$ 正则：$x^{17}f(-b/x^3)$ 的最低 $x$ 幂为二，$x^{36}f(-b/x^3)V(-b/x^3)$ 的最低 $x$ 幂为三。分母仅来自固定单位 $7,b$。所以 (4) 给原整截面，未删除 flat twist 或另选一个抽象同维空间。

对于固定整数 $m$，不同单项式的总次数 $q$ 不同。确实
$$
n=17q+19\nu
\tag{5}
$$
同时确定 $n,q$ 时便唯一确定 $\mu,\nu$。更具体，两组同权指数之差为 $(36j,-17j)$，总次数之差为 $19j$。

在代数截面 (4) 中，其有理因子在 $O$ 的首极部为
$$
x^{m/2-3q}+\text{较低极阶},
\tag{6}
$$
对应完整截面的首项为 $w^q$，系数为一。同一 $m$ 中这些首极阶互异。因此任何 primitive 的同权整组合在好约化后的截面格仍非零；其原点零阶为 $6q_{\min}$，其中 $q_{\min}$ 是约化后非零系数的最小总次数。尤其当 $D<s$ 时，$w^r$、$0\le r\le D$ 的真实整低 jet 已忠实读取每个同权组合。

这也支付了较保守的 $p>72D$ 情形：此时所有 $m\le72D<p$，可先按实际整数权分组，再用线丛度数或 (6) 证明低 jet 非零。不过下面的完整方阵不需要这个较强条件。

## 2. 原非中央行构成的显示方阵

现在取
$$
p=6s-1>71,\qquad 0\le D<s,\qquad
c=[z^{p+1}]\log(\sigma/z),\qquad
\zeta_p=pc\in\mathcal O^\times.
\tag{7}
$$
列按总次数 $\ell=0,\ldots,D$，同次数内按 $\nu=0,\ldots,\ell$ 排列：
$$
P_{\ell,\nu}=S^{\ell-\nu}T^\nu.
$$
行用原物理指标
$$
(q,h),\qquad 0\le q\le D,\quad0\le h\le q,\qquad
n(q,h)=hs+q.
\tag{8}
$$
因为 $D<s$，这些原行互不重复；除 $(0,0)$ 外全是非中央余类。全部位于首 $p^2$ 窗口内：
$$
n(q,h)\le D(s+1)<ps.
$$
定义真实正规化评价方阵
$$
\boxed{
\mathcal V_{p,D}((q,h),(\ell,\nu))
=p^h h!\,[w^{hs+q}]P_{\ell,\nu}.
}
\tag{9}
$$
$(q,h)=(0,0)$ 就是原常数行。每个矩阵元素整，未作依赖列的缩放。

由 R600 的全次数非中央式，$q\ge1$ 时准确有
$$
\overline{\mathcal V_{p,D}((q,h),(\ell,\nu))}
=
\overline{\zeta_p(34\ell+38\nu)}^{\,h}
\,\overline{[w^q]P_{\ell,\nu}}.
\tag{10}
$$
若 $\ell>q$，低系数严格为零。若 $\ell=q$，它准确为一。故按总次数排列后，(9) 模 $p$ 是块下三角，其第 $q$ 个对角块为
$$
\boxed{
\bigl((\bar\zeta_p(34q+38\nu))^h\bigr)_{0\le h,\nu\le q}.
}
\tag{11}
$$
即便某个节点为零，Vandermonde 仍保留该节点；同次数的任意两节点之差为
$38\bar\zeta_p(\nu'-\nu)$，在 $q<p$ 下非零。不同总次数间的权碰撞不会破坏块下三角论证。

## 3. 全原格的单位行列式和范数恒等式

置
$$
B_D=\binom{D+2}{3}.
$$
各对角块的行列式是
$$
(38\bar\zeta_p)^{q(q+1)/2}\prod_{j=1}^q j!.
$$
逐块相乘得到完整绝对公式
$$
\boxed{
\det\mathcal V_{p,D}\equiv
(38\bar\zeta_p)^{B_D}
\prod_{j=1}^D(j!)^{D-j+1}
\pmod p.
}
\tag{12}
$$
右边为单位。因此
$$
\boxed{\mathcal V_{p,D}\in\operatorname{GL}_{M_D}(\mathcal O).}
\tag{13}
$$
这里没有只取一个 rank 推断：所有行、原列、完整首系数和整体行列式均已给出。

若 $F=\sum c_{\ell,\nu}P_{\ell,\nu}$，则 (13) 还给完整原系数范数的准确读取
$$
\boxed{
\max_{\ell,\nu}|c_{\ell,\nu}|_p
=
\max_{\substack{0\le q\le D\\0\le h\le q}}
 |p^h h!\,[w^{hs+q}]F|_p .
}
\tag{14}
$$
正反两个方向来自 $\mathcal V$ 与 $\mathcal V^{-1}$ 均整。

未缩放的选定行矩阵
$$
\mathcal R_{p,D}=([w^{hs+q}]P_{\ell,\nu})
$$
的行列式赋值也准确为
$$
\boxed{v_p(\det\mathcal R_{p,D})=-B_D,}
\tag{15}
$$
因为全部 $h!$ 都是单位，而 $\sum_{q=0}^D\sum_{h=0}^q h=B_D$。

## 4. 同一个完整真前缀的空区间

仍用所有原物理行定义
$$
K_{D,k}=E_{D,2}\cap
 \ker([w^0],\ldots,[w^{k-1}]).
\tag{16}
$$
没有只取余类行定义一个替代前缀。

若 $k=D(s+1)+1$，则 (8) 的全部选定行都在 $k$ 之前。对 $F\in K_{D,k}$，(9) 的全部值恰为零；(13) 迫所有原系数为零。因此
$$
\boxed{K_{D,D(s+1)+1}=0\qquad(D<s).}
\tag{17}
$$
这不是模 $p$ 核能否提升的推测：矩阵在原整格上已经可逆。

更一般，任意一部分选定行都是独立的真实线性泛函，所以
$$
\boxed{
\operatorname{rank}_{\mathcal O}K_{D,k}
\le M_D-
 \#\{(q,h):0\le h\le q\le D,\ hs+q<k\}.
}
\tag{18}
$$
右边读取的是同一个全前缀，遗漏的原行只可能进一步降低其秩。

因此 R600 的统一全权 Vandermonde 后段不能在本格上被假定仍有真实非零层。这里甚至在 $D(s+1)$ 之后就完全没有前缀；比先用至多 $36D$ 个整数权得到的较大空区间更强。

## 5. 两个固定函数的特征零接触恰为二次数量级

定义
$$
\mathfrak m(D)
=\max_{0\ne P\in\mathbf C[X,Y],\ \deg P\le D}
 \operatorname{ord}_{w=0}P(S(w),T(w)).
\tag{19}
$$
对每个 $D$，取一个好惰性素数 $p_D>6D$，并另保 $p_D>71$。式 (12) 的矩阵元素来自原有理 Taylor 系数；它在 $\mathbf Q_{p_D}$ 非奇异，就在特征零非奇异，包括 $\mathbf C$。因此 (17) 给
$$
\boxed{\mathfrak m(D)\le \frac{D(p_D+7)}6.}
\tag{20}
$$
这同时保证 (19) 中没有非零多项式恒等于零。

固定模六的素数定理给：可选 $p_D\equiv5\pmod6$ 且
$p_D=(6+o(1))D$。这里只用固定模数、任意固定相对长度区间的素数存在，不用随 $D$ 增长的模数或条件性短区间定理。所用标准定理可见作者原文
[I. Soprounov, *A Short Proof of the Prime Number Theorem for Arithmetic Progressions*, Theorem 2.1](https://academic.csuohio.edu/soprunov-ivan/wp-content/uploads/sites/93/2023/02/primes.pdf)；
其结论应用于 $a=5,q=6$ 即可，去掉固定有限坏集不改变该选择。

故
$$
\boxed{\mathfrak m(D)\le(1+o(1))D^2.}
\tag{21}
$$
另一方面，$M_D$ 个原单项式上施加前 $M_D-1$ 个齐次 Taylor 条件，总有非零解；由已经支付的非奇异性，该解不是恒零函数。所以
$$
\boxed{
\binom{D+2}{2}-1
\le\mathfrak m(D)\le(1+o(1))D^2.
}
\tag{22}
$$
于是原纯 $S/T$ 格的最大真实接触是 $\Theta(D^2)$。这不是为整个九来源格声称相同接触次数：七个 Euler 坐标没有被加进本篇的方阵。

## 6. 非连续行列式不等于真实旗标成本

式 (15) 只能描述选定的非连续行，不能直接记成 (16) 连续饱和旗标的范数成本。这在 $D=1$ 已有完全具体的反例。

本篇选定的原行是 $0,1,s+1$；(15) 给其未缩放行列式赋值 $-1$。但原连续前三行 $0,1,2$ 的行列式是
$$
[w^2](T-S)=-1118b/15,
\tag{23}
$$
在本篇范围为单位。因此原真前缀在第三行已结束，全部非零真实层的成本并没有 (15) 的那一阶分母。后面的原行可以在早已读取的商空间上具有分母；这不创建一个新的非零饱和层。

本篇的 (17)–(22) 是严格的真前缀和接触结论，(14) 是另一种实际选定评价范数。二者均保留原列格，但不得互相冒认。因此没有由本篇推出 R581/R584 所需的九格 cutoff，亦没有将原两中央失败提升为新的全来源零。

## 7. 精确原来源证书

[check-r604-original-staircase-minor.mjs](../scripts/check-r604-original-staircase-minor.mjs) 使用此前已采用的同一个解析纤维 $p=23$，分别保 $b=1,17$，从原 Weierstrass/sigma 有理递推直接构造 $S,T$。它核对 $D=1,2,3<s$ 的：

- 全部实际正规化矩阵元素、块下三角零和对角 Vandermonde；
- 完整公式 (12)；
- 未缩放选定行列式的精确赋值；
- 同次数原连续前缀子式，用以区分 (15) 与真实旗标。

215 项精确检查全部通过。两个尺度下，$D=1,2,3$ 的选定行列式赋值依次为 $-1,-4,-10$，而连续前 $M_D$ 行的行列式赋值依次为 $0,-1,-5$；每个后者在特征零都非零。这里只作固定纤维的完整核对，不从这些有限数值外推一般连续旗标形状。一般全部 $D<s$ 的结论由 (10)–(13) 证明。

本篇把原全权 Vandermonde 的真实空区间支付到完整格上，并给两个固定函数的二次接触上界。原主目标仍须把原完整中央条件接到非空真层或实际来源的非齐次关系；这个空区间本身不代替该算术步骤。
