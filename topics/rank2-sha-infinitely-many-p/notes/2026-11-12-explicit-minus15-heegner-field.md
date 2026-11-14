# 显式辅助域 Q(√−15) 与严格中央导数证书

日期：2026-11-12。状态：本篇完整证明 R100 可以固定
$F=\mathbb Q(\sqrt{-15})$，无需再选择未指定的 BFH 判别式。
这是辅助秩一扭曲的证书，原 E17 的无穷 $p$ 目标仍未完成。

## 1. 明确的曲线、导子和符号

令
\[
E:y^2=x^3-17x,\qquad
E^{(-15)}:y^2=x^3-3825x,
\quad3825=17\cdot3^2\cdot5^2.
\tag{1}
\]
$-15$ 是基本判别式，且与 $N_E=9248=2^5\cdot17^2$ 互素。
扭曲曲线的导子为
\[
N=2^5\cdot3^2\cdot5^2\cdot17^2=2080800.
\tag{2}
\]
可以逐位直接核查，无需把数据库标签当作证明：

| 位 | $v_\ell(\Delta_{\min})$ | Kodaira 型 | 几何组件数 | 导子指数 |
|---:|---:|---|---:|---:|
| 2 | 6 | III | 2 | 5 |
| 3 | 6 | $I_0^*$ | 5 | 2 |
| 5 | 6 | $I_0^*$ | 5 | 2 |
| 17 | 3 | III | 2 | 2 |

这里 $\Delta=64\cdot3825^3$，各位的赋值均小于 $12$，模型已最小。
在 $2$ 处，$3825\equiv1\pmod {16}$，是 $\mathbb Q_2$ 中四次方，
故局部同构到 $y^2=x^3-x$。对后者作 $x\mapsto x+1$，
得到 $y^2=x^3+3x^2+2x$、$b_8=-4$，Tate 算法停在 III。
在 $3,5$ 处为好约化曲线的驯二次扭曲，$I_0^*$ 的剩余三次式分别为
$T^3+T$ 与 $T^3-3T$，均可分；$17$ 处 $v_{17}(a_4)=1$ 给 III。
导子指数由 $f_\ell=v_\ell(\Delta_{\min})+1-m_\ell$ 得到。

已证 $w(E)=+1$。互素二次扭曲的符号式给
\[
w(E^{(-15)})=w(E)\chi_{-15}(-9248)=-1,
\tag{3}
\]
因为 $\chi_{-15}(-1)=-1$、$\chi_{-15}(2)=+1$，而 $17$ 的指数为偶数。
因此 $L(E^{(-15)},1)=0$。

## 2. 没有截断假设的导数公式

写 $L(s)=\sum a_n n^{-s}$，并置
\[
A=\frac{\sqrt N}{2\pi},\qquad
E_1(x)=\int_x^\infty\frac{e^{-t}}t\,dt=-\operatorname{Ei}(-x)
\quad(x>0).
\]
对相关模形式 $f$，Mellin 变换和符号 $-1$ 给
\[
\Lambda(s)=A^s\Gamma(s)L(s)
=\int_1^\infty f(it/\sqrt N)
       (t^{s-1}-t^{1-s})\,dt.
\]
在 $s=1$ 求导。分部积分给
$\int_1^\infty e^{-bt}\log t\,dt=E_1(b)/b$，而 $L(1)=0$，所以
\[
\boxed{\quad L'(1)=2\sum_{n=1}^\infty\frac{a_n}{n}E_1(n/A).\quad}
\tag{4}
\]
这是收敛恒等式，未用“足够小的值视作零”的数值约定。

Hasse 界与好位 Euler 因子递推给
$|a_n|\le d(n)\sqrt n\le2n$；坏位均为 additive，$a_\ell=0$。
因为 $0<E_1(x)\le e^{-x}/x$，对于任意整数 $B\ge1$，尾项准确满足
\[
\left|L'(1)-2\sum_{n=1}^B\frac{a_n}{n}E_1(n/A)\right|
\le \frac{4A}{B+1}\,
 \frac{e^{-(B+1)/A}}{1-e^{-1/A}}.
\tag{5}
\]
这里所有 $n>B$ 的项都已包括；没有把有限列表当成整个导数。

## 3. 两套整数系数与球算术证书

[完整脚本](../scripts/check-minus15-heegner-field.py) 对 $B=10000$
使用两种不同方法生成全部 $a_n$，逐个核对相等。

第一种直接在有限域上数点，计算
\[
a_\ell=-\sum_{x\in\mathbb F_\ell}
              \left(\frac{x^3-3825x}{\ell}\right)
\]
并作 Euler 递推。对 $\ell\equiv3\pmod4$，配对 $x,-x$ 给零；
在 $2,3,5,17$ 处用已核 additive 因子。

第二种使用独立的 Gaussian CM 计算：取
$\pi=a+bi$，$a$ 奇、$b$ 偶、$a+b\equiv1\pmod4$，$a^2+b^2=\ell$。
在 $\mathbb Z[i]/(\pi)$ 中 $i=-a/b$。令
$r=17^{(\ell-1)/4}$，则 E17 的 trace 在
$r=1,-1,i,-i$ 时分别为 $2a,-2a,2b,-2b$，再乘
$\chi_{-15}(\ell)$ 得 (1) 的 trace。
第一种计数法已经独立确定系数，第二种用作独立算法的交叉核查。

脚本用 160-bit Arb 球算术计算 (4) 的有限和及 (5)。结果为
\[
\begin{split}
S_{10000}&=12.3988793252073086255620869035328264414814913
             \quad\text{误差}<4.0\cdot10^{-44},\\
T_{10000}&<2.548\cdot10^{-18},\\
L'(1)&\in 12.39887932520730863\ \pm\ 6.99\cdot10^{-18}.
\end{split}
\tag{6}
\]
最简严格结论是
\[
\boxed{12<L'(E^{(-15)},1)<13.}
\tag{7}
\]
系数 $a_1,\ldots,a_{10000}$ 逗号连接 ASCII 的 SHA256 为
`90e3384900c4c11cc88ca71625d24332df0de5886a5ec2012f28edd4d4f85fc3`。
另一位研究者独立用 CM 方法、192-bit Arb 和 $B=12000$，得到
同一严格区间及 $3.496\cdot10^{-22}$ 以下的尾界；前一万系数散列相同。

## 4. R100 的全部输入可以显式固定

(3)、(7) 给 $E^{(-15)}$ 解析秩恰一。
Gross–Zagier–Kolyvagin 遂给它代数秩一、整个 Sha 有限。
因此现在可以在 R100–R102 永久取
\[
F=\mathbb Q(\sqrt{-15}).
\]
$-15\equiv1\pmod8$ 给 $2$ 分裂；$-15\equiv2\pmod {17}$
且 $2$ 为模 $17$ 平方，给 $17$ 分裂。
约化正定二元二次型只有 $(1,1,4),(2,1,2)$，故 $h_F=2$。

输入素数可以明确写为
\[
\mathcal P_F=
\{p\ne17:\ p\text{为素数},\ p\equiv1,17,49,53\pmod {60}\}.
\tag{8}
\]
这四个互素剩余类准确等价于 $p$ 在 $\mathbb Q(i)$ 和 $F$ 都分裂，
并自动排除 $2,3,5$；它们各由 Dirichlet 定理给无穷多个素数。
类数例外 $p\mid h_F$ 对这些 $p$ 不出现。
本篇没有把 (8) 的输入素数全部认作原 E17 的有限 Sha 输出素数；
仍须证明实际导出点 $Y_\ell$ 不可整除。

## 来源与核查位置

- J. Cremona，*Algorithms for Modular Elliptic Curves*，
  [作者全文目录](https://johncremona.github.io/book/fulltext/index.html)，
  Chapter 3 的 Tate 算法及导子；Mellin 恒等式在本文直接推导。
- Arb/FLINT 的[球算术保证](https://flintlib.org/doc/algorithms/special-functions/overview.html)
  与[指数积分函数](https://arblib.org/arb_hypgeom.html)：
  使用返回包含精确值的区间及显式尾界，不使用普通浮点零阈值。
- 原 E17 秩、导子、根数见 R4 及已核局部输入；
  解析秩一的 Gross–Zagier–Kolyvagin 输入同 R100。
  [BCGS 作者终稿](https://web.math.ucsb.edu/~castella/Kolyvagin.pdf)
  引言列明这一标准定理及原论文，Heegner 系统的详细引用见 R100。
