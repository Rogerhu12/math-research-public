# 修复后低权对角类的全局高度与指定 AJ：引用范围

状态：**来源范围核查；未证明新全局非零。** 2026-11-15。
本注对应 [R830](../results/R830-distinct-degeneracy-test-vectors-and-fourth-slot.md) 的固定不同退化向量。
不增加数值计算，不把未核实稿件用作主目标证明输入。

## 1. 本课题已经支付的输入

[R826](../results/R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md) 的三组固定
$(f,g_j,h_j)$ 满足 $N_f=10404$、$N_g=N_h=2601$，对应表示在有限位恰于
$2,3,17$ 分歧。R818及R826的完整因子分解给三重积的中心解析秩1。
R830已把第三个old输入改为 $q_4^*h$，并证明全部有限位的指定三线性测试非零。

这三件事不因换 $q_4$ 而使局部表示未分歧：换的是同一表示中的向量。
R829原同 $q_0$ 的类已为零；以下只讨论R830新类。

## 2. 已亲读的 YZZ 版本保留分歧补项

X. Yuan、S.-W. Zhang、W. Zhang，*Triple product L-series and Gross–Kudla–Schoen cycles*，
作者所载 2023-11-14 版本：
[全文](https://web.math.princeton.edu/~shouwu/publications/triple2023.pdf)，
§1.3，Conjecture 1.3.1、Proposition 1.3.2、Theorem 1.3.3（正文第7–8页）。

该版本将高度写成 $\mathscr L(\pi)\alpha(v,\widetilde v)$；
Theorem 1.3.3 对分歧表示保留
$$
\mathscr L(\pi)=
 \frac{16\zeta_F(2)^2}{L(1,\pi_L,\mathrm{ad})}
 L'(1/2,\pi_L)+\sum_{\ell\in P}c_\ell\log\ell,
 \qquad c_\ell\in\overline{\mathbf Q}.
\tag{1}
$$
这里 $P$ 是位于表示分歧位下方的有理素数集。
本课题的 $P=\{2,3,17\}$，所以不能直接删去这三项。
该版本明确在未分歧情形得到无补项的猜想公式。

因此，仅将R830的非零局部测试和R818的复导数非零代入(1)，
还没有排除右端补项相消。
这不是断言原稿结论错误，也不是断言不存在更强的其他定理；
这里只记录所检定理未支付本题的这一接口。
按本课题README，尚未被公认的论证若要实际使用，仍需本仓库完整证明。

## 3. 另一个已发表惰性定理也保留指定非零输入

L. Marannino，*Diagonal cycles and anticyclotomic twists of modular forms at inert primes*，
Research in the Mathematical Sciences 13 (2026), article 70，2026-08-17发表，
[期刊全文](https://doi.org/10.1007/s40687-026-00651-w)，
§1、Assumption 1.1、Theorem 1.2。

该定理假设第一模形式非CM、大像、平方自由level，且其level与CM判别式互素；
结论由一个指定反圆分 $p$-adic $L$ 值非零推出Selmer维数1。
它没有给出该指定值非零。
当前 $f$ 是CM、level $10404$ 非平方自由，且与判别式3不互素，
故不能直接套用。改变ordinary素数集合也不改变这些固定障碍。

## 4. 继续所需的是哪条实际等式

R830已付的精确式仍是
$$
\operatorname{AJ}_p(\Delta_{04})(\omega_f\omega_{g,0}\omega_{h,4})
 =
 \frac{\left\langle\omega_f,
 [\,\{4G_g(Q)h(Q^4)-\bar\pi G_h(Q^4)g(Q^p)\}\,dQ/Q\,]\right\rangle}
 {1+\bar\pi/\pi^2}.
\tag{2}
$$
分母和所有有限局部因子非零，没有证明(2)的分子非零。
本课题还须证明新类的原 $\lambda_j$ 投影与
[R814](../results/R814-common-fixed-good-pair-and-three-original-aj-squares.md)
指定类的真实全局比较，或直接控制(2)在无穷多个目标 $p$ 的值。

即使另行证明某个复高度或Chow类非零，也仍须支付到这里这个指定
$p$-adic局部AJ泛函的桥；R817在7993的非零不自动传播到其他素数。
本注没有关闭原跨 $p$ 非零、三原值线性行或全Sha主目标。
