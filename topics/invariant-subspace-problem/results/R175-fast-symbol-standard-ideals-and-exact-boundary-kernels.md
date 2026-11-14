# R175：快坐标符号的标准闭主理想与精确边界核

日期：2026-11-12。作者：l2_moments。根代理预留 R175。
状态：完整证明。已重新逐项核对 R118 的归一化幂、首单位系数和重排三次型假设。
本稿把 R158/R159 的具体快符号类加强为范数闭主理想等式；不声称任意 $\mathcal G$ 元素都满足该等式。

## 1. 主定理

令 $f\in C(\mathbb Z_2)$ 非零，其坐标振幅
$$
d_j(f)=\tfrac12\sup_x|f(x)-f(x^{(j)})|
$$
具有有限非零支持，或者其非增重排满足
$$
\frac{-\log d_\ell^*(f)}{\ell^3}\longrightarrow+\infty.
\tag{1.1}
$$
取任意复第一阶指数
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
R159 已构造唯一的实际乘子
$$
P_{f,w}\in\mathcal A,\qquad P_{f,w}e^w=f e^w.
$$
非负整数在 $\mathbb Z_2$ 中稠密，故连续非零 $f$ 有有限的首个非零整数值。
记
$$
r(f)=\min\{n\in\mathbb N_0:f(n)\ne0\}.
\tag{1.2}
$$
并令 $I_r=\overline{A^r\mathcal A}^{\|\cdot\|}$，其中 $I_0=\mathcal A$。

**定理。**
$$
\boxed{
\overline{P_{f,w}\mathcal A}^{\|\cdot\|}
=I_{r(f)}.
}
\tag{1.3}
$$
所以闭主理想只由首个非零整数位置决定，不依赖指数权 $w$。

更具体地，若 $r(f)\ge1$，存在实际单位 $Z_\nu\in\mathcal A^\times$，使
$$
\boxed{P_{f,w}Z_\nu\longrightarrow A^{r(f)}
\quad\text{于算子范数}.}
\tag{1.4}
$$
这里不声称 $Z_\nu$ 一致有界，也不声称存在一个固定有界商使等式精确成立。

本定理覆盖 R154 的快模式多项式、R158 在实际紧值域邻域全纯的快模式符号，以及 R159 的任意 Hölder 快模式符号和非解析无限 Walsh 次数例子。

## 2. 所用 R118 接口和一般尾引理

R118 的定理准确如下。
设
$$
S=\sum_{n\ge1}c_n\frac{A^n}{W_n}V_n,\qquad
\|V_n\|\le1,
$$
令 $r=\min\{n:c_n\ne0\}$，且 $\chi(V_r)\ne0$。
如果有限支持，或者非零 $c_n$ 的模长重排满足
$$
\liminf_{\ell\to\infty}\frac{-\log c_\ell^*}{\ell^3}>400r^4,
$$
则 $\overline{S\mathcal A}=I_r$，并有单位右乘逼近 $SZ_\nu\to A^r$。
其证明是在实际交换 Banach 代数内作准备分解和范数估计；
因此 (1.3) 是范数闭理想结论，不只是某个 Hilbert 表示中的核结论。

下面是直接应用时需要的精确版本。

**引理2.1。**
设
$$
P=H(A)+\sum_{m\ge0}c_m\frac{A^{n_m}}{W_{n_m}}T_m,
\tag{2.1}
$$
其中 $H$ 是真正解析芽，$n_m$ 是互异正整数，
每个 $T_m\in\mathcal A$，$\sup_m\|T_m\|<\infty$，
$c_m$ 按模长重排超三次，级数范数收敛。
若 $P\ne0$ 的形式首阶为 $r\ge1$，
且可以把有限项吸收进解析头，使余下全部 $n_m>r$，
则
$$
\overline{P\mathcal A}=I_r.
\tag{2.2}
$$

**证明。**
吸收有限项后的头仍真解析，记为 $H_0(A)$。
因为每个剩余项的形式阶至少 $n_m>r$，
连续形式系数给头与 $P$ 的前 $r+1$ 个系数相同。
故
$$
H_0(z)=z^rU_0(z),\qquad U_0(0)\ne0.
$$
$U_0(A)\in\mathcal A$ 是单位。

取 $D_0=\|U_0(A)\|>0$，把解析头作为 R118 的单个首项
$$
H_0(A)
=(W_rD_0)\frac{A^r}{W_r}\,
\frac{U_0(A)}{D_0}.
\tag{2.3}
$$
首因子范数为1且字符非零。
取 $D=\max(1,\sup_m\|T_m\|)$，其余项改写为
$$
(Dc_m)\frac{A^{n_m}}{W_{n_m}}\frac{T_m}{D}.
\tag{2.4}
$$
未出现的整数指数系数置零。
指数互异且都大于 $r$，所以首非零系数恰在 $r$，没有指数合并问题。
有限添加首项、删除有限尾项和乘一个固定常数均不改变重排超三次性。
故新的非零系数满足 R118 的阈值，得到 (2.2) 及单位逼近。证毕。

引理要求吸收的每个有限项真解析。
它没有从“所有因子有界”推出解析性；
下面 R158/R159 的构造恰已分别验证每个 $T_m$ 真解析。

## 3. 指数倾斜的整数系数公式

记
$$
q_j=e^{-2b_j},\qquad
t_j(z)=z^{2^j}/d_j,\qquad d_j=W_{2^j},
$$
以及形式乘积
$$
\mathcal H_q(z)=\prod_{j\ge0}(1+q_jt_j(z)).
\tag{3.1}
$$
每个固定阶只涉及有限个位，所以 (3.1) 是定义良好的形式幂级数，常数为1。
这里不要求它有正收敛半径。

对整数 $n$ 的二进位集合 $\operatorname{bits}(n)$，令
$$
q(n)=\prod_{j\in\operatorname{bits}(n)}q_j.
$$
每个 $q(n)\ne0$，且 $W_n=\prod_{j\in\operatorname{bits}(n)}d_j$。

R159 使用实际局部乘子
$$
M_j=(I-q_jN_j)(I+q_jN_j)^{-1}.
$$
若 $g$ 是有限柱，定义
$$
\Psi_w(g)=\sum_J\widehat g(J)\prod_{j\in J}M_j.
$$
其形式符号满足
$$
\boxed{
\mathcal H_q(z)\,\iota(\Psi_w(g))
=\sum_{n\ge0}\frac{g(n)q(n)}{W_n}z^n.
}
\tag{3.2}
$$
证明只需把有限的 Walsh 展开乘上 (3.1)。
对位于 Walsh 单项式 $J$ 内的每个位，分子是 $1-q_jt_j$；
其他位的因子是 $1+q_jt_j$。
在 $z^n$ 项中，符号正好为
$(-1)^{|J\cap\operatorname{bits}(n)|}=\chi_J(n)$，
求和即得到 $g(n)$。二进位分解唯一，所以没有遗漏其他分拆。

R158/R159 的实际构造给有限柱 $f_m\to f$ 一致，
并且
$$
\Psi_w(f_m)\longrightarrow P_{f,w}
$$
按算子范数。
R32 的每个固定形式系数都是 $\mathcal A$ 上的连续线性泛函。
因此对 (3.2) 每次只比较有限个系数并取极限，得到
$$
\boxed{
\iota(P_{f,w})
=
\frac{\displaystyle\sum_{n\ge0}f(n)q(n)z^n/W_n}
{\mathcal H_q(z)}.
}
\tag{3.3}
$$
分母常数为1，故
$$
\boxed{
\operatorname{ord}P_{f,w}=r(f),\qquad
[z^{r(f)}]\iota(P_{f,w})
=\frac{q(r(f))f(r(f))}{W_{r(f)}}\ne0.
}
\tag{3.4}
$$
这是对连续符号的真实整数值公式。
没有为任意 $L^2$ 向量指定不存在的整数点值。

## 4. R159 的重排尾完全满足引理

令 $j_0,j_1,\ldots$ 按非零 $d_j(f)$ 递减排列。
R159 的有限锚定柱 $f_m$ 保留 $j_0,\ldots,j_{m-1}$，其余物理位设为0。
令
$$
C_w=\max(1,\sup_j\|M_j\|),\qquad K_w=1+C_w.
$$
大有限 $q_j$ 及其逆只影响这些固定常数；
由于 $b_j\to0$ 和 $N_j^2=\eta_jN_{j+1}$，
所有高位的实际逆均有统一界。

R159 的真实差分恰为
$$
\Psi_w(f_{m+1})-\Psi_w(f_m)
=c_mN_{j_m}T_m,
\qquad
c_m=K_w^m d_{j_m}(f),
\tag{4.1}
$$
其中每个 $T_m$ 真解析，且
$$
\sup_m\|T_m\|
\le
\sup_j2|q_j|\|(I+q_jN_j)^{-1}\|<\infty.
\tag{4.2}
$$
$K_w^m$ 已吸收有限柱求值范数随已选位数的增长；
并非把它隐藏在一个随 $m$ 变化的“统一常数”里。

对任意 $\Gamma>0$，充分大 $m$ 有 $c_m\le e^{-\Gamma m^3}$。
删除原枚举前 $\ell$ 项后，剩余上确界至多 $e^{-\Gamma\ell^3}$，
所以其非增重排也超三次。
固定常数的进一步正规化不改变这一性质。

若 $r=r(f)\ge1$，有限集合
$$
\{j:2^j\le r,\ d_j(f)>0\}
$$
会包含在某个枚举头 $J_{m_0}$ 内。
取这样的 $m_0$ 后，所有剩余指数 $2^{j_m}>r$。
前 $m_0$ 项组成真解析头 $\Psi_w(f_{m_0})$；
其形式首项与 $P_{f,w}$ 相同，理由有两种等价写法：

- 余尾每项的形式阶严格大于 $r$，固定系数连续；
- 对每个 $n\le r$，整数 $n$ 的所有非零物理位已被保留，零振幅位又不影响 $f$，故 $f_{m_0}(n)=f(n)$，再用 (3.2)。

因此该头恰为 $A^r$ 乘真解析单位。
引理2.1 适用，给 (1.3)—(1.4)。

若只有有限个正振幅，$f$ 是有限柱，$P_{f,w}$ 本身真解析；
(3.4) 直接给 $P_{f,w}=A^rU$，$U$ 是单位。
若 $r=0$，则 $\chi(P_{f,w})=f(0)\ne0$，它本来就是 $\mathcal A$ 单位，结论为 $I_0$。
全部分支均已覆盖。

## 5. 全纯快模式与 Hölder 快模式

R158 的另一直接表示是
$$
P_{F(U),w}
=P_{\rm head}+\sum_{j\ge m_0}s_jN_jT_j,
$$
其中联合幅度 $s_j$ 超三次重排、每个 $T_j$ 真解析且一致有界。
其小尾 Taylor 展开和有限头分支已在 R158 完整处理；
本稿不假定一个全局 Taylor 球覆盖非凸紧值域。
因此也可直接用引理2.1。

更统一地，R159 已证明：若联合快模式 $U$ 的幅度为 $s_j$，
且 $F$ 在其实际紧值域上为 $\alpha$-Hölder，则
$$
d_j(F(U))\le L\,2^{\alpha-1}s_j^\alpha,
$$
从而满足 (1.1)，主定理立即适用。

在紧值域邻域全纯的 $F$ 也在该紧集上 Lipschitz：
取一个闭的小管状邻域仍包含于全纯定义域；
近点用该管内有界的一阶导数，远点用紧集上的有界函数值。
所以 R158 全部非零符号、以及 R154 的所有快模式多项式均被覆盖。
这里的 $r$ 总是实际复合符号 $F(U(n))$ 的首个非零整数位置，
无需模式的代数独立性。

## 6. 任意连续表示的核和闭值域

令 $\pi:\mathcal A\to B(X)$ 为任意连续含幺 Banach 空间表示。
由 (1.3) 的两向范数逼近，
$$
\boxed{
\ker\pi(P_{f,w})=\ker\pi(A)^r,
}
\tag{6.1}
$$
$$
\boxed{
\overline{\operatorname{Ran}\pi(P_{f,w})}
=
\overline{\operatorname{Ran}\pi(A)^r}.
}
\tag{6.2}
$$

具体地，若 $\pi(P)x=0$，由 $PZ_\nu\to A^r$ 得 $\pi(A)^rx=0$。
反向用 $P\in I_r$，即 $A^rV_\nu\to P$，得到 $\pi(P)x=0$。
表示连续且全部像交换，所以这两步都是真正的范数极限。

同样，$\pi(A)^rx=\lim\pi(P)\pi(Z_\nu)x$ 给一个闭值域包含；
用 $A^rV_\nu\to P$ 给反向包含。
本节没有使用某个未知表示中的 $\mathcal G$ 强近似单位或未知不变限制上的稠密像。

对原模型任意闭不变限制，R23 的 $A^r$ 单射稠密给旧循环结论；
现在得到的 (6.1)—(6.2) 还适用于不满足原模型高位弱极限的其他表示。

## 7. 负整数边界的精确核

取 R174 的实际负整数表示 $\pi_-$，其中
$$
B=\pi_-(A),\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\quad Be_0=0.
$$
全部权非零，所以
$$
\boxed{
\ker\pi_-(P_{f,w})
=\operatorname{span}\{e_0,\ldots,e_{r-1}\},
\qquad \dim\ker\pi_-(P_{f,w})=r.
}
\tag{7.1}
$$
$r=0$ 时右侧按零空间理解。
$B^r$ 的值域稠密，故 $\pi_-(P_{f,w})$ 的值域也稠密。

若 $\mathcal N$ 是任意闭 $B$-不变子空间，诱导的连续表示给
$$
\ker(\pi_-(P_{f,w})|_{\mathcal N})
=\mathcal N\cap\operatorname{span}\{e_0,\ldots,e_{r-1}\},
$$
以及
$$
\overline{\pi_-(P_{f,w})\mathcal N}
=\overline{B^r\mathcal N}.
\tag{7.2}
$$
这并没有要求先分类 $\mathcal N$。
任意有限放大的全边界空间上，核维数相应为放大倍数乘 $r$。
一般子商只保留 (6.1)，不额外声称一个未证明的统一维数界。

例如 R159 的
$$
f(x)=\sqrt{\sum_{j\ge0}e^{-(j+1)^4}(1-\chi_j(x))}
$$
满足 $f(0)=0$、$f(1)=\sqrt{2/e}\ne0$，所以 $r=1$。
尽管它非解析、Walsh 次数无界，其全部指数倾斜乘子都生成 $I_1$，
在边界表示中的核恰为 $\mathbb Ce_0$。

## 8. 减标量与限制

对任意 $\lambda$，只要 $f-\lambda$ 非零，就仍满足相同振幅条件，
而
$$
P_{f-\lambda,w}=P_{f,w}-\lambda I.
$$
因此其标准闭主理想和边界核由
$$
r_\lambda=\min\{n\ge0:f(n)\ne\lambda\}
$$
精确给出。
如果 $\lambda\ne f(0)$，则 $r_\lambda=0$，实际乘子为单位；
若 $f$ 非常数且 $\lambda=f(0)$，则 $r_\lambda$ 有限且为正。

本稿没有证明任意 $\mathcal A$ 元素的闭主理想标准，
也没有从 $\mathcal G$ 的定义单独推出标准性。
它使用 R158/R159 已有的具体、互异整数阶、超三次系数和逐项解析的真实尾表示。

同一标准闭理想不等于存在一个固定有界商；
R167 的无界除法及零形式阶闭分式全谱实例仍然适用。
边界核的 (7.1) 也没有给原任意未知慢符号的核分类或有界传输。
一般边界 unicellularity、一般慢平方共振及完整 Hilbert 不变子空间问题仍未解决。
