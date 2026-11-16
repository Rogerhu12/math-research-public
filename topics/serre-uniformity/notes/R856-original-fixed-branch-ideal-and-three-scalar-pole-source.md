# R856：原固定 21 点的完整两图理想基与三标量极除子入口

日期：2026-11-16。状态：**来源上的纸面构造已完成；本篇首次消费者只计算固定 21 点的两个完整理想基，不预称新矩阵已执行。**

本文接 [原有限 RR 矩阵及来源叶子](2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md)（FM，SHA256 `a5d65aa4a841c77eb7d29ccf98e96b01e60691ffdf1d763115487889a1695fbe`），保留原 $Y$、原 $P_0=\phi(c_0)$、原正规基、原 $f_4$ 及所有尺度。第一部分给一个可直接执行、无需任何新函数域乘法矩阵的完整 FM 输入块；第二部分利用 [R838](../results/R838-certified-original-second-derivative-ideal-and-minimal-order3.md) 的实际完整像，减少后续原极理想所需的准确标量源。

## 1. 已成来源与本次范围

在原 $K=\mathbf Q(\zeta)$ 上，令 $\zeta^2+\zeta+1=0$，并沿 [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) 记

$$
z=\sigma/\tau,\quad v=1/z,\quad
\tau=e_0,\quad \sigma=e_1+e_{73},
$$
$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,
\qquad R_\sigma=\bigoplus_{i=0}^{271}K[v]\gamma_i,
\qquad \gamma_i=v^{\epsilon_i}\beta_i,
\qquad \epsilon=(0,1^{144},2^{127}).
\tag{FB.1}
$$

两个环均为原曲线仿射开集的完整正规环。本文没有把原扭曲截面任意宣称为 $\mathbf Q$ 定义；[R820](../results/R820-certified-original-cusp-finite-algebra-and-ideals.md) 已成的有理坐标 cusp 理想沿其已证忠实扩张取到原 $K$。其两个完整多项式基记为 $C_\tau,C_\sigma$，所定义的层是

$$
\mathscr C=\mathcal O_Y(-\mathcal C_0),\qquad \deg\mathcal C_0=20.
\tag{FB.2}
$$

原 [R837](../results/R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md) 已准确给出原全部 146 个 V1 截面与 418 个 V2 截面在 $P_0$ 的值。实际原值中 $\tau(P_0)=67419/4\ne0$；$\sigma(P_0)$ 的 $\zeta$ 分量为 $-45018\ne0$。故 $P_0$ 同时属于两张图。这里只引用已成原值，并未重做反射或 CM 算术。

本次目标为

$$
\mathscr B=\mathcal O_Y(-\mathcal C_0-P_0)
=\mathscr C\,\mathfrak m_{P_0}.
\tag{FB.3}
$$

同时输出两图的完整点理想 $\mathfrak m_{P_0}$，供 FM 的点幂和截面除子输入使用。原 $P_0$ 与 cusp 支撑不交；下面还用实际非零评价直接验证这一接缝。本次无需原 $W$ 的 34 组系数、一般 $\Gamma$、R842 的准确核展开、原 $B$ 的全部准确坐标或任何 $272^3$ 乘法表。

## 2. 用原尺度取得 272 个正规基值

令 $t_0=\tau(P_0)$、$s_0=\sigma(P_0)$，令 $d_0,\ldots,d_{126}$ 为原 R805 `degree2_original_indices` 的实际有序列表。用 R837 原值定义

$$
b_0=1,\qquad b_i=\frac{e_{i+1}(P_0)}{t_0}\quad(1\le i\le144),
$$
$$
b_{145+j}=\frac{V_{2,d_j}(P_0)}{t_0^2}\quad(0\le j<127),
\qquad z_0=s_0/t_0,\qquad v_0=t_0/s_0,
$$
$$
c_i=v_0^{\epsilon_i}b_i.
\tag{FB.4}
$$

于是 $b_i=\beta_i(P_0)$、$c_i=\gamma_i(P_0)$。原 V1 的 $82^2$ 和 V2 的 $82^4$ 已在 R837 值内；(FB.4) 只是同一截面框架中的比值，不另插入 $82$、content、共轭或 $s=\sqrt{-3}$。消费者逐项保存原值来源、实际 $d_j$、除数和乘回。$z_0v_0=1$ 及两个正规基值的过渡也准确乘回。

这给真正的环评价

$$
\mathrm{ev}_\tau\Bigl(\sum p_i(z)\beta_i\Bigr)=\sum p_i(z_0)b_i,
\qquad
\mathrm{ev}_\sigma\Bigl(\sum q_i(v)\gamma_i\Bigr)=\sum q_i(v_0)c_i.
\tag{FB.5}
$$

它们是原 $P_0$ 的同一评价，来源于真实截面值而非任意线性泛函。

## 3. 单个准确行核给完整基

以下命题对一张图成立。写 $x=z$ 或 $v$，$x_0=z_0$ 或 $v_0$，$e_i$ 表示原正规坐标列，$b_i$ 暂表示该图基值。

首先，$\mathrm{ev}(1)=1$ 给点理想的完整 $K[x]$ 基

$$
P_0(x)=(x-x_0)e_0,\qquad
P_j(x)=e_j-b_je_0\quad(1\le j\le271).
\tag{FB.6}
$$

证明不是仅比较支撑：对任意 $u=\sum p_i(x)e_i$，先减去 $\sum_{j\ge1}p_jP_j$，余下 $e_0$ 的系数为 $p_0+\sum_{j\ge1}b_jp_j$；它在 $x_0$ 为零，当且仅当可被 $x-x_0$ 整除。因此 (FB.6) 恰生成评价的全部核。其 determinant 是 $x-x_0$，保原列序，不引入符号。

再取原 R820 的完整 cusp 基 $C=(C_0,\ldots,C_{271})$，并准确计算

$$
r_j=\mathrm{ev}(C_j)\in K.
\tag{FB.7}
$$

因 $P_0\notin\mathcal C_0$，至少一个 $r_j\ne0$。程序必须从实际值选最小这样的 $k$，并验证其逆；不预填 pivot 或只以理论断言替代算术。定义

$$
H_k=(x-x_0)C_k,\qquad
H_j=C_j-\frac{r_j}{r_k}C_k\quad(j\ne k).
\tag{FB.8}
$$

**完整基命题。** (FB.8) 是 $\mathscr C(U)\cap\mathfrak m_{P_0}(U)$ 的完整 $K[x]$ 基，并且

$$
\mathscr C(U)\cap\mathfrak m_{P_0}(U)
=\mathscr C(U)\mathfrak m_{P_0}(U)
=\mathscr B(U).
\tag{FB.9}
$$

事实上，原 $C$ 给 $K[x]^{272}\simeq\mathscr C(U)$。在这些坐标中，评价行就是 $r$。对 $u=(u_j)$，减去全部 $j\ne k$ 的 (FB.8) 后，仅第 $k$ 坐标剩下

$$
u_k+\sum_{j\ne k}(r_j/r_k)u_j.
\tag{FB.10}
$$

原评价为零，当且仅当 (FB.10) 被 $x-x_0$ 整除。这证明完整性和线性独立。又 $r_k\ne0$ 给 $\mathscr C(U)+\mathfrak m_{P_0}(U)=R$，故交等于积，得到 (FB.9)。此证明不使用原环的平面呈示，也不需要分解任何闭点。

R820 的实际稀疏形为

$$
C_j=e_j-q_j(x)e_{271}\quad(j<271),\qquad
C_{271}=P_{20}(x)e_{271},\quad\deg q_j<20,
\tag{FB.11}
$$

其中 $P_{20}$ 首一。程序读取原准确系数；不重新求 cusp 有限代数或其20阶秩。由 (FB.8) 的显式坐标变换矩阵，

$$
\det H=(x-x_0)\det C=(x-x_0)P_{20}(x),
\qquad \dim_K(R/\mathscr B(U))=21.
\tag{FB.12}
$$

这里不用另求一个 $272$ 阶 determinant：原完整 $C$ 和实际 (FB.8) 的变换矩阵已经给准确行列式恒等式。消费者保存完整新列、显式两项变换、原列乘回、所有 $P_0$ 评价为零以及 (FB.12) 的多项式。不会只输出一个非零 minor 冒称完整理想。

## 4. 两图粘合及 FM 消费

两张图分别执行上述完整核构造。原 $C_\tau,C_\sigma$ 已认证为同一个全局 cusp 理想；(FB.4)–(FB.5) 又是同一个 $P_0$ 评价。因此两张图得到同一层 $\mathscr B$ 的限制。过渡始终是 (FB.1) 中的原正规基过渡，不把新两基矩阵错误宣称为逐列相等。

这立即给 FM 所需的两组完整点理想和固定支撑理想生成矩阵。它们是当前第一个可单独完成的实际块。它们不等于五个 $\eta_j$ 的完整理想，也不等于原 RR 函数 $a_j$；后者继续消费原函数和 Norm/理想运算。

## 5. 已成原二阶像的三个真实标量生成元

下面是可减少后继准确输入的纸面推论，不属于首次 R856 算术范围。

从本节起，将第1–4节的两图正规环、cusp 理想及点理想沿原 $K\hookrightarrow L=\mathbf Q(b,\zeta)$ 忠实标量扩张；后文 $R_c$ 均指 $R_c\otimes_KL$。原 $B,D,E_y$ 保留其原 $L$ 定义域，不将固定支撑块在 $K$ 上的构造误说成这些对象已降到 $K$。

令 $B$ 为 R838 明确认证的 **同一个原 canonical free1186 特征零截面**。其来源是原 R787 单位选行系统及完整核维数，已在 [R849](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md) 保持为准确 `exact_unit_solve_expression`；不是任意模向量提升。令

$$
f_\tau=B/\tau^5,\qquad f_\sigma=B/\sigma^5,
\qquad \delta_\tau=\tau^{-1}D_0,\quad
\delta_\sigma=v\delta_\tau.
\tag{FB.13}
$$

原 R814 证明两个导子在各自仿射正规环上正则。因此对一张图的 $R$、导子 $\delta$ 和任意 $f\in R$，完整原正规基 $\{\beta_i\}$ 满足

$$
\sum_{r=0}^2\sum_{i=0}^{271}K[x]\,\delta^r(f\beta_i)
=(f,\delta f,\delta^2f)_R.
\tag{FB.14}
$$

证明。Leibniz 公式给左边包含于右边。反向先有 $fR$；再由
$\beta_i\delta f=\delta(f\beta_i)-f\delta\beta_i$
取得 $(\delta f)R$；最后由
$\beta_i\delta^2f=\delta^2(f\beta_i)-2\delta f\,\delta\beta_i-f\delta^2\beta_i$
取得 $(\delta^2f)R$。每次剩余项均在已经取得的子模中，因为 $\delta R\subset R$。这也证明左边确为 $R$ 理想，而非先假定其稳定性。

必须同时检查另一图的齐次全局源。对权 $w$ 的原截面 $s$，写 $F=s/\tau^w$、$g=\delta_\tau z$。其另一图第0、1、2层齐次源在 $\tau$ 框架下依次为

$$
F,\qquad z\delta_\tau F-wgF,
$$
$$
z^2\delta_\tau^2F-(2w+1)zg\delta_\tau F
\; +\;\bigl(w(w+2)g^2-wz\delta_\tau g\bigr)F.
\tag{FB.15}
$$

这是将 $\sigma^{w+2r}\delta_\sigma^r(s/\sigma^w)$ 除以 $\tau^{w+2r}$ 逐步计算；第1层的算子为 $z\delta_\tau-wg$，第2层再用 $z\delta_\tau-(w+2)g$。全部系数在 $R_\tau$ 中正则。反向在 $\sigma$ 图同样成立，使用 $v,\delta_\sigma v$。对原 $s=Bd_i$，$w=5+\epsilon_i$，(FB.14)–(FB.15) 表明 R838 的完整两图全局像 $\mathcal J_2$ 在每张图恰为三标量理想。

实际 R838 已证 $\mathcal J_2=I_2=\mathscr C I_D$，因而

$$
\boxed{\quad I_D|_{U_c}
=\mathscr C_c^{-1}
\bigl(f_c,\delta_cf_c,\delta_c^2f_c\bigr)_{R_c},
\qquad c\in\{\tau,\sigma\}.\quad}
\tag{FB.16}
$$

这不需要先展开 R842 的 $395\times395$ 单位核块或全部295个 $D$-截面。它不撤销 R842/R845 的已成结果，只为新的准确生成矩阵提供一个更少标量的入口。

## 6. 原极除子与后继最小准确右端

原 R805/R838 已给

$$
E_y=(y_f)_\infty=\mathcal C_0+P_0+3D,
\qquad P_0\notin D,
\tag{FB.17}
$$

且 $D$ 约化。设 $J=(f,\delta f,\delta^2f)$。在原一维正规环的每个 DVR，理想重数是三个生成元重数的最小值，故

$$
J^3=(f^3,(\delta f)^3,(\delta^2f)^3)_R.
\tag{FB.18}
$$

这是一维可逆分式理想的等式，不是一般多元环中理想三次幂的生成恒等式。结合 (FB.16) 得原极理想

$$
\boxed{\quad I_{E_y}
=\mathfrak m_{P_0}\,\mathscr C^{-2}
\bigl(f^3,(\delta f)^3,(\delta^2f)^3\bigr).\quad}
\tag{FB.19}
$$

三者均为原 $f_4$ 的真正函数和框架；没有把 $D$ 换成任意有效除子，也没有删除原单位解或主标量。

后继因此只需取得同一个原 $f=B/\tau^5$ 的准确 normal 向量或原 $K(z,w)$ 表达，再以 FM 的链式导数求两阶导数。原 R813 的准确 $g=\delta z,h=\delta w$ 与实际 R806 的 $W$ 已足够定义这些步骤；不要求一般 $\Gamma$。对任一原有理表达 $F(z,w)$，

$$
\delta F=gF_z+hF_w,
\quad
\delta^2F=g^2F_{zz}+2ghF_{zw}+h^2F_{ww}
+(g g_z+h g_w)F_z+(g h_z+h h_w)F_w.
\tag{FB.20}
$$

原函数域关系的导数由同一真实 $g,h$ 保持，故表达式与代表选择无关。原 $W$ 的34组准确叶直接复用；每个实际需要的标量乘法矩阵只按 FM.3 的相应右端求解并乘回。这里没有要求完整 Krylov 逆或全乘法表。

本篇不宣称 $f,\delta f,\delta^2f$ 的准确 normal 坐标已经展开。原 U.1 的真实单位解及原 S5 来源仍是其数据叶；旧有限域 $816$ 列不能更名成特征零矩阵。首次实际 R856 只完成第2–4节的固定支撑块；其真实输出再接 FM 的完整生成矩阵运算，最终五个 $\eta$、$a_j$、连接和原指定高度均另有实际消费者。

## 7. 来源边界与冻结规则

最小三组旧来源是：R820 的两个完整理想 index、544条原准确列、有限代数接口及 metadata；R805 的原 free-basis、pencil 及 metadata；R837 的原 P0/V2 值及 metadata。R805 的小原件从 R820 原输入载体逐成员 SHA 核后取得，保其原 producer 身份；不将 R820 冒称 R805 的数学 producer。

所有新有理域评价、比值、多项式列及乘回只在公开 Actions 中执行。原已成阶段按完整来源和 tag 恢复；不同目录、运行预算或载体封装不改变数学身份。输出保存全列与源引用，不只保存结论。Git 仅保证明、源码、参数和简明实际回执；坐标、矩阵和输入载体只保一日活跃 artifact。
