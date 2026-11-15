# R679 补充 — 同一十二步过滤后的原负一深差

日期：2026-11-15。**状态：已证明。**

固定 R679 的同一个 $q_N^\sharp$，$N\in4\mathbf Z_{>0}$；
其实际系数不依观察深度 n。本文只对 R679(34)–(36) 的完整
L 深差使用该篇同一个 $\mathcal P_{12}$，不换成八角域的另一个测试。

令
$$
\mathcal P_{12}(\mathsf T)=
\prod_{a=1}^{12}(\mathsf T-\lambda^2\kappa^a),\quad
\beta=-\lambda,\quad h=b_L/b_Y,\quad I=I_{\Sigma_5,-1}\ne0.
$$
原 R679 实际系数满足
$$
J_2=\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N},
\qquad v_p(J_8)\ge-8N.
$$
全部其余负矩和两个原 moving unit cut 仍保持原规范。

## 1. 首模态的完整单位乘数

原首模态为 $\beta^n\kappa^{3n}$。直接计算
$$
\mathcal P_{12}(\beta\kappa^3)=\kappa^{33}U_{3,p},
$$
$$
U_{3,p}=(\beta\kappa^2-\lambda^2)
(\beta\kappa-\lambda^2)(\beta-\lambda^2)
\prod_{a=4}^{12}(\beta-\lambda^2\kappa^{a-3}).
\tag{1}
$$
原固定 ray 上 $1+\lambda$ 是单位，所以
$$
\boxed{U_{3,p}\equiv\lambda^{14}(1+\lambda)\pmod p,\qquad
       U_{3,p}\in\mathcal O^\times.}
\tag{2}
$$
此处没有丢掉 $a=3$ 的因子
$\beta-\lambda^2=-\lambda(1+\lambda)$。

新增 $J_8$ 的首模态为 $\beta\kappa^9$，其乘数准确具有值层
$$
v_p\bigl(\mathcal P_{12}(\beta\kappa^9)\bigr)
=\sum_{a=1}^{12}\min(a,9)=72.
\tag{3}
$$
相同的等深因子仍由 $1+\lambda$ 付为单位。

## 2. 两个完整尾项

若
$\mathcal P_{12}(\mathsf T)=\sum_{j=0}^{12}c_j\mathsf T^j$，
其实际整系数满足
$$
v_p(c_j)\ge\frac{(12-j)(13-j)}2.
$$
R679 的两个尾项分别属于 $J_2p^{5n}\mathcal O$、
$J_8p^{11n}\mathcal O$。因此
$$
\min_{0\le j\le12}
\left(5j+\frac{(12-j)(13-j)}2\right)=50,
$$
$$
\min_{0\le j\le12}
\left(11j+\frac{(12-j)(13-j)}2\right)=77.
\tag{4}
$$
这些界已保原 log 展开的所有 $1/k$ 分母，因为 R679(35)
对每个真实移位 $n+j$ 给同一个统一界。没有把形式级数先认成整系数。

由 R679(36)，完整得到
$$
\begin{aligned}
\mathcal P_{12}\Delta^\sharp_{N,n}
={}&72b\Omega^3h\,J_2\beta^n\kappa^{3n+33}U_{3,p}I\\
&-518400b^2\Omega^9h\,J_8\beta^n\kappa^{9n}
       \mathcal P_{12}(\beta\kappa^9)I\\
&+J_2p^{5n+50}\mathcal O+J_8p^{11n+77}\mathcal O.
\end{aligned}
\tag{5}
$$
特别第二行不是零；它是同一来源中已经支付的八阶条件项。

若 $n>N$，第二行相对首行多至少
$6(n-N)+39$ 层。再若 $2n>v_p(I)$，两个尾项也都严格更深。
所以
$$
\boxed{
v_p\bigl(\mathcal P_{12}\Delta^\sharp_{N,n}\bigr)
=3n-2N+33+v_p(I_{\Sigma_5,-1}).
}
\tag{6}
$$
实际首项也可写为
$$
36\ell_0^2\Omega h\,\lambda^N\beta^n
 \kappa^{3n-2N+33}U_{3,p}I_{\Sigma_5,-1}.
$$

## 3. 与原完整 S/T 行的同时范围

R679(29) 已付同一 $\mathcal P_{12}$ 下的两份完整 S 外部回原 $J_S$。
另一方面若原 $J'_T(0)=0$，该篇(38) 准确给
$$
\mathcal P_{12}
(\mathcal E_+^\sharp-\mathcal E_-^\sharp+\mathcal R^\sharp_{N,n})
=-\mathcal P_{12}\Delta^\sharp_{N,n}\ne0.
\tag{7}
$$
原 T 外部在 n 中不变，其实际乘数是
$\mathcal P_{12}(1)=\prod_{a=1}^{12}(1-\lambda^2\kappa^a)$，不能删去。
(7) 的全部 L 浅域、两个 moving W cut 及 log 质量继续保留。

(6) 没有把 (7) 左边认成 R679 的纯 S 外部；
若要推出两个原中央不能同时为零，仍须支付这两个完整观察之间
真实的来源/域关系。本文只给同一个已构造测试、同一个过滤器、
同一个原负一行的精确非消失。

依赖：[R679](../results/R679-neutral-degree-twelve-three-s-and-exterior-return.md)。
