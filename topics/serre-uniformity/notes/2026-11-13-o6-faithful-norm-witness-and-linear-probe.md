# O6：Norm 原像必须生成全域，以及一个实际线性试解的排除

**状态：§1–3 为已证明的全局约束；§4–5 为已执行的有限试解及严格局部排除。实际 $X$ 与 $\mathcal L$ 仍未知。**

沿用 R191、R207、R210、R219 的同一个域与标号：
$$
 K=\mathbb Q(i),\quad F/K\text{ 循环 }44\text{ 次},\quad
 L=FL_q,\quad [L_q:K]=43,
$$
$$
 \Delta=\operatorname{Gal}(F/K),\qquad
 \Gamma=\operatorname{Gal}(L/F),\qquad
 \chi(\sigma)=\omega=8+25i\in\mathbb F_{43^2}.
$$
$\chi$ 忠实，$\omega$ 的阶为 $44$。
R219 已实际写出的普通实单位是
$$
 U=\prod_{j=0}^{43}(\sigma^jz)^{a_j},\qquad
 a_j\equiv15\operatorname{Re}(\omega^j)\pmod{43},
$$
其中 $a_j$ 取中心整数代表。
它有普通实单位 Norm 原像，但原像尚未求出。

## 1. 目标保留了忠实角色

在 $(F^\times/F^{\times43})\otimes_{\mathbb F_{43}}\mathbb F_{43^2}$ 中，
$$
 e_\chi[U]
 =\left(\sum_{j=0}^{43}a_j\omega^j\right)e_\chi[z]
 =\frac{15\cdot44}{2}e_\chi[z]
 =29e_\chi[z]\ne0.                                      \tag{1}
$$
最后的不消失来自 R210/R219 的精确单位关系
$e_\chi[u_0]=-15i\,e_\chi[z]$ 与 $u_0$ 的原始性。
普通单位到 $F^\times/F^{\times43}$ 的映射是单射：若一个单位是
$y^{43}$，则 $43v_\mathfrak p(y)=0$ 对所有有限素点成立，故 $y$ 也为单位。

因 $\chi$ 忠实，若 $U$ 落在 $F/K$ 的某个真子域，则相应非平凡
子群固定 $U$，其 $e_\chi$ 投影必须为零，与 (1) 矛盾。因此
$$
 K(U)=F.
$$
又 $\tau U=U$，所以 $\mathbb Q(U)=F^{\langle\tau\rangle}=H$。
这也确认 R219 的实际 $44$ 系数目标自身生成整个底实域，而非其
$11$ 次子域中的一个元素。

## 2. 所有真 $K$ 子域的元素乘积都不足以给出原像

由于 $44$ 与 $43$ 互素，$L/K$ 为循环 $1892$ 次扩张。
设
$$
 D=\left\langle M^\times:\ K\subseteq M\subsetneq L\right\rangle
 \subseteq L^\times.
$$

### 定理

若 $N_{L/F}X=U$，则
$$
 X\notin D\,L^{\times43}.                               \tag{2}
$$

**证明。** 循环扩张的子域由次数唯一确定。对任意真子域 $M$，
分两种情形。

若 $43\nmid[M:K]$，则 $M\subseteq F$，故对 $x\in M^\times$，
$N_{L/F}x=x^{43}$，其模 $43$ Kummer 类为零。

若 $43\mid[M:K]$，写 $[M:K]=43d$，其中 $d\mid44$、$d<44$。
令 $F_d$ 为 $F/K$ 的唯一 $d$ 次子域。则 $M=F_dL_q$，且
$$
 N_{L/F}x=N_{M/F_d}x\in F_d^\times\qquad(x\in M^\times).
$$
$\Delta$ 的非平凡子群 $\operatorname{Gal}(F/F_d)$ 固定右侧。
忠实 $\chi$ 在该子群上非平凡，因而右侧的 $e_\chi$ Kummer 投影为零。

这证明 $N(D)$ 的所有 $e_\chi$ 模 $43$ 投影均为零。
而 $N(Y^{43})=N(Y)^{43}$ 同样给零。若 (2) 不成立，则
$e_\chi[U]=0$，与 (1) 矛盾。证毕。

该证明允许任意非单位元素；不是只对普通单位的子群作限制。
因此不能靠在这些真子域内引入分母来绕过 (2)。

## 3. 每个原像的必要生成次数

若 $K(X)$ 是 $L/K$ 的真子域，则 $X\in D$，与 (2) 矛盾。所以
$$
 \boxed{N_{L/F}X=U\quad\Longrightarrow\quad K(X)=L.}       \tag{3}
$$
特别地，若采用 R219 保证存在的实单位原像 $\tau X=X$，则
$\mathbb Q(X)\subseteq L^+=L^{\langle\tau\rangle}$。
实嵌入使 $\mathbb Q(X)\cap K=\mathbb Q$，因此
$$
 [\mathbb Q(X):\mathbb Q]
 =[K(X):K]=1892=[L^+:\mathbb Q],
$$
从而
$$
 \boxed{\mathbb Q(X)=L^+.}                                \tag{4}
$$

R219 的 $11\times4$ 表示仍可降低底域运算的常数，但不能将实际
Norm 原像放进 $K(s)L_q$ 的 $473$ 次子域，亦不能从所有真子域
元素的乘积拼出它。这是一个必要次数约束，并不声称相应 Norm 方程无解。

## 4. 实际混合线性试解：$z-2\theta$ 不能经底域修正变成所需原像

令 $\theta$ 为 R207 的同一个 Gaussian trace 生成元，首一多项式为
$P_\theta(T)$，次数 $43$。混合线性候选
$$
 X_{a,b}=z-b-a\theta
$$
满足精确公式
$$
 N_{L/F}X_{a,b}=a^{43}P_\theta((z-b)/a).                   \tag{5}
$$

本次实际筛查 $a\in\{-3,-2,-1,1,2,3\}$、$b=0$，采用
$433<\ell<30000$、$\ell\equiv3\pmod4$ 的 $1591$ 个素数。
检测到 $a=2$ 的下述严格失败证书：
$$
 \ell=6343,\qquad r=5847,\qquad R=27648641\pmod{\ell^2}.
$$
程序直接核验
$$
 f_z(r)=0\pmod\ell,\quad f_z'(r)\ne0\pmod\ell,
 \quad R\equiv r\pmod\ell,\quad f_z(R)=0\pmod{\ell^2},
$$
以及
$$
 2^{43}P_\theta(R/2)
 \equiv30446400=6343\cdot4800\not\equiv0\pmod{\ell^2}.    \tag{6}
$$
这里 $\ell^2=40233649$。由 Hensel 引理，$r$ 决定 $H$ 的一个
完成为 $\mathbb Q_\ell$ 的素点；再添 $i$ 是未分歧二次扩张，
故在相应的 $F$ 素点 $\lambda$ 上，(6) 给
$$
 v_\lambda(N_{L/F}(z-2\theta))=1.
$$
若任取 $y\in F^\times$，则
$$
 v_\lambda(N_{L/F}(y(z-2\theta)))=43v_\lambda(y)+1\ne0.
$$
右侧不能等于普通单位 $U$ 的赋值零。因此
$$
 \boxed{N_{L/F}(y(z-2\theta))\ne U\quad\text{对每个 }y\in F^\times.}
                                                               \tag{7}
$$
其余五个候选在这次赋值筛查中没有取得失败证书。下面的另一个
固定素点给出全部六个候选的统一排除，因此不继续扩大这个小候选枚举。

## 5. 一个固定素点排除全部六个底域修正线性试解

取 $\ell=859$，在 $\mathbb F_{859^2}=\mathbb F_{859}[i]$ 中取
$$
 \overline z=802+606i.
$$
直接核验 $f_z(\overline z)=0$、$f_z'(\overline z)\ne0$。
因此它决定一个未分歧的 $F$ 局部嵌入，剩余域恰为
$\mathbb F_{859^2}$。利用 R219 已实际算出的完整 $U$ 幂基系数，得到
$$
 \overline U=49+45i.
$$
令 $n_a=\overline{N(z-a\theta)}$；所有六个 $n_a$ 都非零。
本次精确运算得到下表，其中最后一栏是
$(\overline U/n_a)^{17160}$，且
$17160=(859^2-1)/43$。

| $a$ | $n_a$ | $(\overline U/n_a)^{17160}$ |
|---:|---:|---:|
| $-3$ | $199+481i$ | $97+30i$ |
| $-2$ | $779+227i$ | $103+56i$ |
| $-1$ | $582+797i$ | $492+786i$ |
| $1$ | $489+452i$ | $504+235i$ |
| $2$ | $343+259i$ | $601+369i$ |
| $3$ | $835+411i$ | $236+517i$ |

最后一栏的值均为非平凡 $43$ 次单位根。这里不需要离散对数或
选取新的 Weil 根：为排除底域 $43$ 次幂，只需证明该栏不等于 $1$。

若某个 $y\in F^\times$ 满足 $N(y(z-a\theta))=U$，则
$$
 y^{43}=U/N(z-a\theta).
$$
右侧在所取素点为单位，故 $y$ 也为局部单位；约化后是剩余域的
$43$ 次幂，其 $17160$ 次幂必为 $1$，与表中结果矛盾。
因此得到完整的有限候选排除
$$
 \boxed{N(y(z-a\theta))\ne U
 \quad\text{对全部 }a\in\{-3,-2,-1,1,2,3\},\ y\in F^\times.} \tag{8}
$$
本结论只排除这六个混合线性元及其任意底域乘法修正，不把它们
扩张为一般混合元素或一般 Norm 原像的不可能性。

精确失败数据在 `notes/linear_norm_witness_probe.json`；§4 的赋值
以及本节全部六个幂剩余结论可用
`scripts/verify_o6_linear_norm_failure.py` 快速重验，不需要重跑
R207 的 CRT 或完整素数筛：

~~~sh
python scripts/verify_o6_linear_norm_failure.py \
  notes/small_robert_norm_target_certificate.json \
  notes/r207_gaussian_trace_degree43_certificate.json \
  notes/o6_single_real_norm_target_certificate.json \
  notes/linear_norm_witness_probe.json
~~~

本次该直接验证已经实际运行，结果 `PASS`。
这些排除与必要次数均未计算 $\mathcal L$；R202 继续只留给真实求值。
