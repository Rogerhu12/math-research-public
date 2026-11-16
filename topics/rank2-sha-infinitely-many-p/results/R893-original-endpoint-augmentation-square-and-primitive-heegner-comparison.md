# R893. 原端点的增广平方与固定 Heegner 类的本原比较

日期：2026-11-16。**状态：下述有条件定理已证明。** 固定原普通素数及一个原最高角色，若 R831/R885 的原端点底类非零，则其有界反循环提升与 R814 那个固定 good pair 的 Heegner 提升在增广完成环中相差一个单位。由此，原 canonical 局部函数恰为原端点局部函数的单位倍平方，canonical 全局类恰为该端点函数乘原端点类的单位倍。

这里的“单位”指增广完成环中的单位；不表示其常数是 p 整数单位、代数数或与 p 无关。定理保留可能出现的全部增广零，不由底类非零推出 ordinary 局部化非零，也不把固定 7993 的 canonical 检测换成原端点检测。

## 1. 同一原角色、三种实际来源

固定 $j\in\{4,10,16\}$，以及 R814 所用固定有限数据之外的原普通 $p>211$。沿
[R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、
[R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)，置
$$
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
\phi_j=\lambda_j\mathbf N^{-2}=\nu_j^{-1}.
\tag{1}
$$
原目标是 $V_j=E(1)\widehat\nu_j^{-1}$；与 Castella 的 $T_{\phi_j^\tau}$ 的对应，仍使用 R811 的几何互反与真实共轭。其原 ordinary 条件在 $\mathfrak p$ 为全、在 $\bar{\mathfrak p}$ 为零，等于该表示的 Bloch–Kato 条件。

以下三个来源始终区别：

- $c_1=z^{\rm end}_{j,p}$：原 q/q⁴ 端点的 étale AJ 类，保 R831 的 oldcopy、X₀/X₁、全部 finite Artin 与最高 CM 投影。
- $\mathbf D=\mathfrak D_{j,p}$：R885 的同端点有界反循环类；其增广值为
  $$
  \operatorname{sp}_0\mathbf D=\mathscr E_p c_1,\qquad
  \mathscr E_p=
  \frac{(1+\bar\pi^{-1})^3(1+\pi/\bar\pi^2)}
       {(1-\pi/\bar\pi)^3}\in\mathcal O_p^\times .
  \tag{2}
  $$
- $\mathbf c=\mathbf c_{{\rm can},j,p}$：R804/R811 指定的椭圆单位类，原模数 $34\delta$、30平滑及 $\sqrt{17}$ 的局部 Artin 基全部保留。其增广值记为 $z^{\rm can}_{j,p}$。

R814 在选择 p 以前固定了一条 weight4 形式 $g=\theta_\psi$ 和三个有限角色 $\chi_j$，使
$$
\psi\chi_j=\lambda_j,\qquad
L(\psi^\tau\chi_j,2)\ne0 .
\tag{3}
$$
本文使用的 Heegner 类就是该固定来源的类；没有随着 p 重选 good pair 或 cycle。

唯一非零前提是
$$
\boxed{c_1\ne0\quad\text{在 }H^1(K,V_j).}
\tag{4}
$$
R891 已针对原有限 tame 系统证明
$$
\operatorname{Sel}_{\rm bal}(K,V_j)=E c_1 .
\tag{5}
$$
这里不以另一个来源非零替代 (4)。

## 2. 实际增广环与有限生成模

使用 R811/R885 的同一个顺序：扩大固定系数以容纳 (3)，反演 p，局部化于增广素理想，最后完成，得到
$$
\mathscr R=\mathscr F[[T]],\qquad T=\gamma-1.
\tag{6}
$$
$\mathscr R$ 是 DVR，$\mathscr F$ 是该局部系数域；这些操作平坦。

原全局 Iwasawa 上同调及 compact Selmer 模是有限生成的 Iwasawa 模。这里可在包含 $p,2,3,17$ 和固定 good-pair 坏位的有限集合上取连续上同调：有限自由格和有限 p-上同调给有限生成的 Iwasawa 上同调，局部条件是有限个相应局部模之间的核。R811 使用的 Castella Proposition 4.3.4 的证明进一步给原 relaxed 模无扭、秩一。故其在 (6) 中的像
$$
\mathcal M=\check{\mathcal S}_{\rm rel}(V_j)\otimes\mathscr R
\tag{7}
$$
是有限生成、无扭、秩一的 $\mathscr R$-模，从而自由秩一。

R885 已把 $\mathbf D,\mathbf c$ 放入同一个 (7)。R811 的固定 Heegner 类经真实共轭输送后也在 (7) 中。非 p 位的原有理局部 $H^1$ 为零；加入 good pair 的固定辅助位不产生另一份 relaxed 条件。

R811 的 Coleman 映射来自**有限余核**的实际定理。其余核在反演 p 后为零，故在 (6) 中是同构
$$
\operatorname{Col}_{\mathfrak p}:\mathcal H_{\mathfrak p}
 \xrightarrow{\sim}\mathscr R .
\tag{8}
$$
不得把这一步弱化为伪同构后自行删除可能的 $\mathscr R/(T)$。

记
$$
D(T)=\operatorname{Col}_{\mathfrak p}
       (\operatorname{loc}_{\mathfrak p}\mathbf D),\qquad
C_{\rm can}(T)=\operatorname{Col}_{\mathfrak p}
       (\operatorname{loc}_{\mathfrak p}\mathbf c).
\tag{9}
$$
R885 的局部特殊化已经支付
$$
D(0)=\mathscr E_p\,\ell_{j,p}
       (\operatorname{loc}_{\mathfrak p}c_1),
\tag{10}
$$
其中 $\ell_{j,p}$ 是规定局部基的非零线性坐标。没有另藏一个 $T$ 因子。

## 3. 固定 good pair 的 Heegner 类确在增广处非零

这一节是不能仅由 (4) 和全局秩一省略的步骤。

### 3.1 所用条件与权4范围

R814 的 (3) 满足 Castella Definition 5.1.1 的 S1–S4：
cyclic conductor、精确有限 self-dual 条件、$\psi\chi_j=\lambda_j$、实际伴随中心值非零。Theorem 4.1.1 和 Corollary 4.6.1 的假设正是这些权4可用的条件，不包含仅在 $r=1$ 另外定义的 S5–S8。

原文 Theorem A.2.1 的结论以任一 good pair 定义其 Heegner 分量；其证明开头有 “strong good pair” 一语。本文不据该词为权4增添一个未经定义的条件，而直接使用其证明中实际的主猜想、CM 分解和控制步骤。以下逐项重做，所有输入均适用于 R814 的固定 S1–S4。

记 Castella 侧的 Heegner compact/discrete dual 模为
$$
\mathcal S_H=\check{\mathcal S}_{\rm BK}(g,\chi_j)\otimes\mathscr R,\qquad
\mathcal X_H=\mathcal X_{\rm BK}(g,\chi_j)\otimes\mathscr R .
$$
这两个模均有限生成，$\mathcal S_H$ 无扭；Corollary 4.6.1 给两者秩一，并给真正的特征理想等式
$$
\operatorname{char}_{\mathscr R}(\mathcal X_{H,\rm tors})
=
\operatorname{char}_{\mathscr R}
 \bigl(\mathcal S_H/\mathscr R\mathbf Z_H\bigr)^2 .
\tag{11}
$$
$\mathbf Z_H$ 是同一固定 Heegner 塔的类，不是另选的生成元。

### 3.2 伴随部分与控制余项

令
$$
A(T)=\mathscr L_v(\psi^\tau\chi_j\mathbf N^{-2}).
$$
R814 已由 (3)、经典插值及两个不同赋值的 ordinary 根证明
$$
A(0)\ne0.
\tag{12}
$$
Castella Theorem 4.3.5 的 companion 主猜想与其 A.2 证明中的 (A.7)–(A.8) 控制，因而给
$$
\operatorname{Sel}_v(K,V_{\psi^\tau\chi_j})=0.
\tag{13}
$$
这些控制映射的核、余核是有限的；反演 p 后都消失。此处不是从“伴随 Iwasawa 模 torsion”直接推出 (13)：需要 (12) 排除增广素因子。

同一 CM 分解及 Shapiro 给
$$
\operatorname{Sel}_{\rm BK}(K,V_{g,\chi_j})
\simeq
\operatorname{Sel}_{\rm BK}(\mathbf Q,V_{\lambda_j}(2))
 \oplus\operatorname{Sel}_v(K,V_{\psi^\tau\chi_j}).
\tag{14}
$$
原 $V_j$ 与第一项之间用 R811 的真实 $\tau$ 输送；这不改变维数。由 (5)、(13)，(14) 维数恰为一。

还需支付的是同一实际局部条件下的控制。Castella A.2 证明的 (A.6) 分解将 $\mathcal X_H$ 分成两个 rank-one CM 角色的 dual Selmer 模；对各因子应用那里引用的 Mazur 控制，得到
$$
\dim_{\mathscr F}\mathcal X_H/T\mathcal X_H=1.
\tag{15}
$$
其有理核、余核没有被默默忽略：p 处的两个 CM 角色的 Tate 指数为 $2,-1$，原 finite 角色在 p 处未分歧，p>211 时残余 tame 惯性均非平凡，因此不存在该处的异常不变直线。非 p 位保留原未分歧条件；纯权排除了 Frobenius 特征值1，原控制中的局部误差为有限模。原文 (A.7)、(A.8) 和随后对 (A.6) 两因子的控制正是在此范围内。我们只在反演 p 后使用它们，未断言原整数控制是无误差同构。

DVR 结构定理现在给出明确结论。若
$$
\mathcal X_H\simeq\mathscr R\oplus
 \bigoplus_{\alpha=1}^{b}\mathscr R/(T^{m_\alpha}),
\qquad m_\alpha\ge1,
$$
则其模 $T$ 维数为 $1+b$。(15) 迫 $b=0$。所以 (11) 的左边是单位理想，从而
$$
\mathcal S_H=\mathscr R\,\mathbf Z_H .
\tag{16}
$$

最后，原文 A.2 证明中 (A.8) 后的**compact** 特殊化复合
$$
\mathcal S_H/T\mathcal S_H
\longrightarrow \operatorname{Sel}_{\rm BK}(K,V_{g,\chi_j})
\longrightarrow \operatorname{Sel}_{\rm BK}(\mathbf Q,V_{\lambda_j}(2))
\tag{17}
$$
在反演 p 后是单射。其整数版本核有限；(13) 杀伴随部分，而非通过一个任意向量投影。由 (16)，$\mathbf Z_H$ 在左边非零；(17) 的像是 Theorem 3.2.2 所给的
$$
E^{\rm Iw}_{j,p}\,\mathcal Z^{\rm tar}_{j,p},\qquad
E^{\rm Iw}_{j,p}
=\left(1-\frac{\chi_j(v)p}{\alpha_p}\right)
 \left(1-\frac{\chi_j(\bar v)p}{\alpha_p}\right)\in1+p\mathcal O.
\tag{18}
$$
因此 R814 **那份固定 cycle** 的 target 全局 AJ 确非零：
$$
\boxed{\mathcal Z^{\rm tar}_{j,p}\ne0.}
\tag{19}
$$
(19) 仍是全局类非零，未称其局部 AJ 配对非零。

## 4. 两个实际提升都是同一 DVR 模的生成元

令 $\mathbf Z$ 表示 R811 中位于 $T_{\phi_j}$ 的 Heegner target 类，
并置
$$
\mathbf Z^\circ=\tau^{-1}\mathbf Z\in\mathcal M.
\tag{20}
$$
反循环变量随之完整反演
$$
\iota(T)=(1+T)^{-1}-1=-T/(1+T).
\tag{21}
$$
R811 §4–6 的 $\tau/\iota$ 约定在此保持；不是对 $\mathbf C_p$ 任意作 Galois 共轭。

由 (19)、(18)，$\operatorname{sp}_0\mathbf Z^\circ\ne0$。
由 (2)、(4)，$\operatorname{sp}_0\mathbf D\ne0$。
若它们任一在 $T\mathcal M$ 内，其全局特殊化必为零。因此二者都不在 $T\mathcal M$。
结合 (7) 的有限自由秩一性质，存在唯一
$$
\boxed{\mathbf D=U(T)\mathbf Z^\circ,\qquad U\in\mathscr R^\times .}
\tag{22}
$$

这一步用到了第3节证明的 (19)。仅有“$\mathcal M$ 秩一”和
“$\mathbf D$ 特殊化非零”只能说明 $\mathbf D$ 本原，不能自行说明
$\mathbf Z^\circ$ 本原。

由 R811 的原 Iwasawa 局部化单射，(22) 还说明 $D(T)$ 不是零函数。
它在 $T=0$ 仍可能为零。

## 5. 全部单位因子和精确平方

以下使用 R811/R814 的实际记号，不在可能为零的常数值上取比。
令
$$
C_K(T)=\mathscr L_v(\phi_j),\qquad
B(T)=\mathscr L_v(g,\chi_j),\qquad
B^2=u_{\rm fac}\,C_K A,\quad u_{\rm fac}\in\mathscr R^\times .
\tag{23}
$$
$C_K\ne0$ 是原 root−1 的非零 Iwasawa 函数。
记 $d(T)$ 为原 30 平滑比较因子，$r_{\rm Col}(T)$ 为同一局部模上 Heegner 与输送 EU Coleman 同构的比例。R811 已付
$$
d,\ r_{\rm Col}\in\mathscr R^\times,\qquad
C_{\rm can}=d\,C_K.
\tag{24}
$$
置
$$
e_\iota(T)=C_K^\iota/C_K.
\tag{25}
$$
若 $C_K=T^a c(T)$，$c(0)\ne0$，则
$$
e_\iota=
 \left(-\frac1{1+T}\right)^a
 \frac{c(\iota(T))}{c(T)}\in\mathscr R^\times.
$$
它在 $C_K(0)=0$ 时仍有定义；$e_\iota^\iota=e_\iota^{-1}$。

R811 的完整全局式为
$$
\mathbf c^\tau
=\mathfrak u(T)B(T)\mathbf Z,\qquad
\mathfrak u=
\frac{r_{\rm Col}d^\iota e_\iota}{u_{\rm fac}A}
\in\mathscr R^\times,
\tag{26}
$$
且
$$
\operatorname{Col}_{\mathfrak p}
 \bigl(\operatorname{loc}_{\mathfrak p}\mathbf Z^\circ\bigr)
=\frac{B^\iota}{r_{\rm Col}^\iota}.
\tag{27}
$$
因此由 (22)，
$$
D=U\,\frac{B^\iota}{r_{\rm Col}^\iota}.
\tag{28}
$$
对 (26) 作真正 $\tau^{-1}/\iota$ 输送，再用 (22)、(28)，得到
$$
\boxed{\quad
\mathbf c=H(T)\,D(T)\,\mathbf D,\qquad
C_{\rm can}(T)=H(T)\,D(T)^2,
\quad}
\tag{29}
$$
其中完整单位为
$$
\boxed{\quad
H(T)=\frac{\mathfrak u^\iota r_{\rm Col}^\iota}{U^2}
=\frac{d\,(r_{\rm Col}^\iota)^2}
       {u_{\rm fac}^\iota A^\iota e_\iota\,U^2}
\in\mathscr R^\times .
\quad}
\tag{30}
$$
第二个等式也可直接由同一个 (8) 施于第一个得到。
因而两式中的单位是**同一个** $H$，并非各选一个数值比例。

(30) 分母的每一因子都已付增广可逆：$A$ 由 (12)，
$u_{\rm fac}$、$r_{\rm Col}$、$d$ 来自原固定规范，
$e_\iota$ 由 (25)，$U$ 由第3–4节。
原 Artin/CM 周期、30平滑以及两个不同 ordinary Euler 分别仍在
(24)、(26) 和 (2)、(18) 中。未将它们约定为1。

## 6. 准确的消失阶与普通局部化

令
$$
s=\operatorname{ord}_T D(T)\ge0,\qquad D=T^s D_s,\quad D_s(0)\ne0.
\tag{31}
$$
由 (22)、(29)，在同一实际全局模中有
$$
\boxed{
\operatorname{ord}_{\mathcal M}(\mathbf c)=s,\qquad
\operatorname{ord}_T C_{\rm can}=2s,\qquad
\operatorname{ord}_T C_K=2s .
}
\tag{32}
$$
这比 R885 只给 $C_{\rm can}\mathbf D=D\mathbf c$ 更精确：
在前提 (4) 下，比例中剩余的所有增广因子恰为一个 $D$，
没有另一个未定的共同 $T$ 因子。

特殊化 (29) 给
$$
\boxed{
z^{\rm can}_{j,p}
=H(0)D(0)\mathscr E_p\,c_1 .
}
\tag{33}
$$
故在 (4) 下，下列条件等价：
$$
\begin{aligned}
&s=0;\\
&\operatorname{loc}_{\mathfrak p}c_1\ne0;\\
&z^{\rm can}_{j,p}\ne0;\\
&\operatorname{loc}_{\mathfrak p}:
 \operatorname{Sel}_{\rm bal}(K,V_j)
 \longrightarrow H^1(K_{\mathfrak p},V_j)
 \text{ 是单射}.
\end{aligned}
\tag{34}
$$
最后一步使用 (5) 的实际一维性。
R804/R811 还将第三项等价为同标签原负二值非零；这里不混三个不同角色的线性和。

若 $s>0$，则 (33) 中原 canonical 底类为零，
而 $c_1\ne0$ 且整个一维 Selmer 群处于 ordinary 严格核中。
本文未排除这一情形。
准确的首个 derived canonical 类仍可读取：
$$
\operatorname{sp}_0(T^{-s}\mathbf c)
 =H(0)D_s(0)\mathscr E_p\,c_1\ne0.
\tag{35}
$$
$T^{-s}\mathbf c$ 在 (7) 中真实存在，由 (29) 定义；
但它不是 R804 的未除 $T$ canonical 类。
特别是不能把 R811 仅针对原 $\mathbf c(0)$ 的严格核结论
再套到 (35) 上，借此删除 $s$。

## 7. 所得比较的范围

本篇将 R891 的原端点条件秩一定理与 R814 的固定 good pair 接合，
得到真实 Iwasawa 单位比例 (22) 和保留全部增广阶的平方 (29)。
这不是 Chow 循环成比例的证明；$U,H$ 也未声称属于
$\overline{\mathbf Q}[[T]]$。其定义对象在每个固定 p 相同，
但常数可随 p 改变。

若某个独立的**同一目标 p** 的 canonical 检测已付，
(33) 可在前提 (4) 下给 ordinary 注入；
反过来，别的系数素数上的 shadow 或固定 7993 的 canonical 检测
均不自动证明当前 p 的 (4) 或 $s=0$。
原三中央导数同时为零的排除、原端点在无穷 p 的非零，
以及 (31) 在无穷 p 上的零阶判定仍需实际输入。

## 8. 精确原文依据

- [R891](R891-original-ring-class-anti-kummer-and-one-prime-descent.md)：
  原四角、共轭双点选择及 (4) 推出 (5)；没有使用 restricted-set JNS 扩张。
- [R885](R885-original-endpoint-bounded-anticyclotomic-lift-and-unit-specialization.md)：
  同原端点有界提升、(2)、真实 ordinary 局部空间及 (10)。
- [R811](R811-canonical-soule-classes-and-global-heegner-comparison.md)、
  [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)：
  同模、固定 good pair、有限余核、完整 $\tau/\iota$、
  原 smoothing/period 和 (23)–(27)。
- F. Castella, *Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*，
  [固定 v3 HTML](https://arxiv.org/html/2407.11891v3)、
  [固定 v3 PDF](https://arxiv.org/pdf/2407.11891v3)：
  Proposition 3.5.1，Theorems 3.2.2、4.1.1、4.3.5，
  Corollary 4.6.1，Definition 5.1.1，
  以及 Appendix A.2 的 (A.5)–(A.8) 与后续 compact 控制。
  第3节已明确提取其实际输入，不凭 “strong” 一词为权4补设条件。

本篇没有数学程序、数值扫描、可重算数据输出或新的素数选择。
