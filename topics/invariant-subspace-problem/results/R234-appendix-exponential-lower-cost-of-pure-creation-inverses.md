# R234第五附录：纯创建最小增益的真实指数退化

日期：2026-11-13（UTC+8）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明。

本稿证明纯孔创建 $C=D^*=\sum_{j\ge0}(j+1)^{-2}E_j^*$ 在第 $q$ 层的最小增益至多
$$
\exp\!\left[-\frac{3+\log3}{2}\,q+O(\log q)\right].
$$
因此其逐层纯删除右逆的指数成本不是对角相似法凭空造成的。此结论严格属于纯删除/创建模型；没有据此断言带真实 carry 的 $T_N,T_Y$ 必须有同样下界。

## 1. 头部顶向量的一条精确逆链

固定 $q\ge1$，头位集合 $H=\{0,\ldots,q-1\}$，头创建
$$
C_H=\sum_{j<q}a_jE_j^*,\qquad a_j=(j+1)^{-2}.
$$
令 $e_F$ 表示恰在有限集合 $F$ 上有孔的基向量，头顶向量为 $\omega_H=e_H$。
对 $0\le r\le q$ 定义
$$
 v_r=\frac{(q-r)!}{q!}
 \sum_{\substack{J\subset H\\|J|=r}}
 \left(\prod_{j\in J}a_j^{-1}\right)e_{H\setminus J}.
\tag{1.1}
$$
它属于头中第 $q-r$ 孔层，$v_0=\omega_H$。

对任意缺失集合 $K$、$|K|=r-1$，在 $C_Hv_r$ 中产生 $e_{H\setminus K}$ 的输入恰为 $J=K\cup\{j\}$、$j\in H\setminus K$。共有 $q-r+1$ 个。每个贡献中的 $a_j$ 正好消去 $a_j^{-1}$。因此
$$
\boxed{C_Hv_r=v_{r-1}\ (1\le r\le q),\qquad C_Hv_0=0.}
\tag{1.2}
$$
末端为
$$
 v_q=\frac1{q!}\prod_{j<q}a_j^{-1}\,e_\varnothing
 =q!\,e_\varnothing.
\tag{1.3}
$$

## 2. 用纯尾幂作望远镜相消

令
$$
 C_{\mathrm{tail}}=\sum_{j\ge q}a_jE_j^*,\qquad
 \Omega_{\mathrm{tail}}=e_\varnothing,
$$
其中所有尾算子作用在第 $q$ 位及以后。定义整个无限位置第 $q$ 孔层中的向量
$$
 \xi_q=\sum_{r=0}^q(-1)^r
 v_r\otimes C_{\mathrm{tail}}^r\Omega_{\mathrm{tail}}.
\tag{2.1}
$$
每项的总次数是 $(q-r)+r=q$。各项的头次数不同，因而两两正交；第 $r=0$ 项的范数为 $1$，所以
$$
\|\xi_q\|\ge1.
\tag{2.2}
$$
尾创建有界，故所有这些向量确为 Hilbert 向量，而不是形式序列。

由 (1.2)，$C=C_H+C_{\mathrm{tail}}$ 作用于 (2.1) 后逐项消去，准确留下
$$
\boxed{C\xi_q=(-1)^q v_q\otimes
 C_{\mathrm{tail}}^{q+1}\Omega_{\mathrm{tail}}.}
\tag{2.3}
$$

## 3. 真空尾幂与指数上界

对任意整数 $r\ge0$，不同位的创建交换且每位平方为零。因此
$$
 C_{\mathrm{tail}}^r\Omega_{\mathrm{tail}}
 =r!\sum_{\substack{F\subset\{q,q+1,\ldots\}\\|F|=r}}
 \left(\prod_{j\in F}a_j\right)e_F.
$$
若 $g_q^2=\sum_{j\ge q}a_j^2$，则基本对称和满足
$$
 r!\sum_{|F|=r}\prod_{j\in F}a_j^2\le g_q^{2r}.
$$
所以
$$
\boxed{\|C_{\mathrm{tail}}^r\Omega_{\mathrm{tail}}\|
\le\sqrt{r!}\,g_q^r.}
\tag{3.1}
$$
此外，积分比较给
$$
 g_q^2=\sum_{n=q+1}^{\infty}n^{-4}
 \le\int_q^\infty t^{-4}\,dt=\frac1{3q^3}.
\tag{3.2}
$$
合并 (1.3)、(2.3)、(3.1)、(3.2)，
$$
\boxed{
 \|C\xi_q\|
 \le\varepsilon_q:=
 \frac{q!\sqrt{(q+1)!}}{(3q^3)^{(q+1)/2}}.
}
\tag{3.3}
$$

使用直接由对数积分上下界得到的
$\log n!=n\log n-n+O(\log(n+1))$，有
$$
\begin{aligned}
\log\varepsilon_q
&=\log q!+\tfrac12\log(q+1)!
 -\tfrac{q+1}{2}(\log3+3\log q)\\
&=-\beta_0q+O(\log q),\qquad
\boxed{\beta_0=\frac{3+\log3}{2}>2.049.}
\end{aligned}
\tag{3.4}
$$
这里 $q\log q$ 项完全消去，留下严格的负线性指数。

记
$$
\sigma_q=\inf\{\|Cu\|:u\in H_q,\ \|u\|=1\}.
$$
以 $\xi_q/\|\xi_q\|$ 为实际 Hilbert 测试，(2.2)、(3.3) 给
$$
\boxed{\sigma_q\le\varepsilon_q
=\exp[-\beta_0q+O(\log q)].}
\tag{3.5}
$$
这不是从有限位置数值矩阵外推的结论，而是完整无限尾上的显式上界。

## 4. 所有纯删除逐层右逆都必须付指数范数

若 $Q_q:H_q\to H_{q+1}$ 是任意有界右逆，满足
$$
D Q_q=I|_{H_q},
$$
取 Hilbert 伴随得到 $Q_q^*C|_{H_q}=I$。所以
$$
1\le\|\xi_q\|\le\|Q_q\|\,\|C\xi_q\|
\le\|Q_q\|\varepsilon_q.
$$
从而
$$
\boxed{\|Q_q\|\ge\varepsilon_q^{-1}
=\exp[\beta_0q-O(\log q)].}
\tag{4.1}
$$
特别，不能把纯删除右逆的普遍次数成本改进成 $\exp(o(q))$。创建最小增益也不可能有 $\exp[-o(q)]$ 的统一下界。

## 5. 尾起点随次数作对数级增长时，障碍仍保留

对尾起点 $m\ge0$，将头改为 $\{m,\ldots,m+q-1\}$。同一证明中
$$
\|v_q\|=\frac1{q!}
\left(\frac{(m+q)!}{m!}\right)^2,
\qquad
 g_{m+q}^2\le\frac1{3(m+q)^3}.
$$
因此在这个完整纯尾第 $q$ 层有单位测试使创建范数至多
$$
\boxed{
\varepsilon_{m,q}=
\frac{[(m+q)!/m!]^2\sqrt{(q+1)!}}
{q!\,[3(m+q)^3]^{(q+1)/2}}.
}
\tag{5.1}
$$
若 $m=O(\log(q+2))$，则
$$
\log\varepsilon_{m,q}
=-\beta_0q+O(\log^2(q+2)).
\tag{5.2}
$$
核对误差只需
$\log(m+q)!-\log q!=O(m\log(q+m))$、
$\log m!=O(m\log(m+1))$ 以及
$q\log(1+m/q)=O(m)$。
这覆盖[R234](R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md) 及 [共同尾相似附录](R234-appendix-single-tail-similarity-and-exponential-hole-right-inverse.md) 中的 $m(q)\asymp\log(q+1)$ 尺度。

## 6. 对真实慢边界研究的限制与用途

纯尾右逆的指数成本确有实际见证；不能仅凭其权单调下降，就主张最小奇异值有多项式或亚指数下界。本文也没有使用这种不成立的一般单调推理。

另一方面，真实 $T_N,T_Y$ 具有 carry，且此前已证明它们与纯 $D$ 的有界单因子比较在两方向均失败。因此 (4.1) 不自动传给真实 $T$ 的右逆，更不构造非零 $M\ominus\overline{BM}$。

实际缺陷的指数形式原像界之后，仍需一个真正的跨次数能量论证或别的闭合接口。本文只关掉“将原纯尾右逆直接改成亚指数预算”这一具体路线。
