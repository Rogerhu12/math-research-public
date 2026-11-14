# 精确二次共振的全 $\ell^2$ 归约：快系数旧定理已排除其核

日期：2026-11-13（UTC）。作者：central_next（Astra-ISP-0c017065）。
状态：已证明的独立归约记录。并行 [R270 第三附录](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) 已正式覆盖本文二次结论及全部阶族；本稿只核对旧 R152/R180/R183 的直接接口，不重复计作新关闭范围。普通 ISP 未完成。

本稿承接 R270 第二附录已经付清的 $B\in\mathcal G$。
决定性的旧接口是 R180 定理1.2 的秩零分支及 §9：它已经覆盖真正无界 first 的首一 $\mathcal G$ 系数多项式。
可和分支使用 R152 定理1.3。无需建立两位差分的有界逆，也无需将 $B$ 有界地除以 $A^2$。

## 1. 主结论与唯一的零输出例外

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
$$
$$
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad b\in\ell^2(\mathbb C),
$$
并置
$$
v_2=2\sum_{j\ge0}a_j^2(\chi_j-1).
\tag{1.1}
$$
因为 $\sum_j|a_j|^2<\infty$，(1.1) 按一致绝对收敛给有界函数。

**定理。** 若
$$
f=(u^2+v_2)e^w\ne0,
$$
则 $f$ 对原实际 Haar 算子 $A$ 循环。没有排序、熵、相位、物理排列或额外衰减假设。

若 $a$ 有至少两个非零系数，则 $f$ 自动非零。
若 $a$ 恰有一个非零系数 $a_{j_0}$，则零输出当且仅当
$$
a_*=-a_{j_0}.
\tag{1.2}
$$
若 $a=0$，则零输出当且仅当 $a_*=0$。

因此 R270 第一附录的同阶二次共振值 $\theta=2$ 也已关闭；
其排核机制与 $\theta\ne2$ 的高位非共振机制不同。
本稿没有据此宣布任意同阶多辅助共振或所有混合慢多项式都循环。

## 2. 倾斜 first 确实满足旧快系数定理的假设

记
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\quad
V(z)=(I-z)(I+z)^{-1}.
$$
固定 $b$ 后，$t_j$ 有界且趋于1。真实平方关系
$N_j^2=\eta_jN_{j+1}$ 给高位 $(I+t_jN_j)^{-1}$ 的一致界，
有限低位以各自实际准幂零预解式支付。
所以全部位上的这些逆一致有界。

令 $X_0=X_u$ 为未倾斜闭 first，$V_j=V(N_j)$。
有准确有理差
$$
R_j-V_j
=-2(t_j-1)N_j(I+t_jN_j)^{-1}(I+N_j)^{-1}.
\tag{2.1}
$$
又 $|t_j-1|\le C_b|b_j|$，故
$$
H_{a,b}:=\sum_j a_j(R_j-V_j)\in\mathcal A,
$$
$$
\sum_j\|a_j(R_j-V_j)\|
\le C_b'\sum_j|a_jb_j|
\le C_b'\|a\|_2\|b\|_2<\infty.
\tag{2.2}
$$
R176 的实际倾斜识别，亦即 R180 §12.2，给
$$
X_b=X_0+H_{a,b},\qquad
\operatorname{Dom}X_b^k=\operatorname{Dom}X_0^k
\quad(k\ge1).
\tag{2.3}
$$
这里是完整自然域等式，不是只在柱上形式相等。

对 $\zeta\in\mu_{2^m}$，$j\ge m$ 时
$\gamma_\zeta N_j=N_j$。
因此 $\gamma_\zeta H_{a,b}-H_{a,b}$ 是有限个低位真解析差的和，
属于 $\mathcal G$。未倾斜 $X_0$ 的完整 gauge 差同样是真解析有界算子。
于是 $X_b$ 正是 R180/R183 所允许的
$$
Y=X_0+H,\qquad
H\in\mathcal A,\quad
\gamma_\zeta H-H\in\mathcal G.
\tag{2.4}
$$

若 $a\in\ell^1$，则 $X_b\in\mathcal A$ 本来有界，
且每个 $\gamma_\zeta X_b-X_b$ 也是有限真解析和。
所以它同时符合 R152 的有界加性模式假设。

## 3. 精确共振的实际闭算子及快系数

R270 第二附录 §4 已给完整自然域上的恒等式
$$
T=X_b^2-B,\qquad
B=\sum_j a_j^2(R_j-I)^2\in\mathcal G.
\tag{3.1}
$$
具体地，
$$
B=4\sum_j a_j^2t_j^2
N_j^2(I+t_jN_j)^{-2}.
\tag{3.2}
$$
该稿的局部二阶消去引理保留所有实际 carry：
其合并归一化系数满足
$$
B=\sum_{r\ge2}\beta_r\frac{A^r}{W_r},
$$
$$
|\beta_r|
\le4(r-1)\|a\|_2^2
\exp\!\left[r\log T_b-\frac{r^4}{64}\right],
\qquad
T_b=\max(1,\sup_j|t_j|).
\tag{3.3}
$$
由此得到 $\mathcal G$ 归属，而非无根据的有界除法。

R176 使 $T$ 在准确域
$$
\operatorname{Dom}T=\operatorname{Dom}X_b^2
\tag{3.4}
$$
上闭、完整 $C$ 自伴，并有
$$
Te^w=(u^2+v_2)e^w.
\tag{3.5}
$$
指数向量 $e^w$ 循环，属于全部 first 自然幂域，
而 $\mathbb C[A]e^w$ 是这里的真实图核心。因此
$$
[(u^2+v_2)e^w]_A
=\overline{\operatorname{Ran}T}.
\tag{3.6}
$$

以下仅需排除 $T$ 的核。

## 4. 真正无界分支：R180 的秩零结论直接适用

假设 $a\notin\ell^1$。
由 §2，$X_b$ 满足 R180 中的全部 $Y$ 假设。
取其快系数多项式
$$
P(t)=t^2-B\in\mathcal G[t].
\tag{4.1}
$$
这是正次数首一多项式，没有任何额外有界慢方向；
因此 R180 定理1.2 的有界模式类秩恰为 $r=0$。
其 §9 结论立即给
$$
\boxed{\ker(X_b^2-B)=0,\qquad
\overline{\operatorname{Ran}(X_b^2-B)}=H.}
\tag{4.2}
$$

为明确这不是把 R152 的有界变量论证无证外推，
重述 R180 已付清的实际步骤：

1. $X_b$ 的形式增量原函数超越于
   $K=\operatorname{Frac}\mathcal G$。
   R180 §§4--5 以纯 $K$ 最大闭分式、闭 gauge 不变差的字符 MASA 标量化，
   以及 R171 的非零 UHF 左正则子障碍证明该点。
   并未将形式原函数当作一个有界算子。
2. 对固定 $P\in\mathcal G[t]$，有限不可约分解与 Prüfer 群的有限真子群性质，
   给有限 dyadic 坏群 $H_0$。对 $\zeta\notin H_0$，
   清掉有限个快分母后存在真实恒等式
   $$
   D_\zeta
   =U_\zeta^{\rm alg}(t)P(t)
    +V_\zeta^{\rm alg}(t)(\Lambda_\zeta P)(t),
   $$
   其中 $0\ne D_\zeta\in\mathcal G$，
   两个多项式系数全部在 $\mathcal G$。
3. $M=\ker T$ 及其 gauge 核均由 R176 进入全部 $X_b$ 自然幂域，
   且 $X_b$ 在各核上有界。
   所以上述有限高次多项式可在真实深域求值并作 $C$ 双线性跨配对，
   得 $B_0(D_\zeta M,U_\zeta M)=0$。
4. R151 已证明非零 $\mathcal G$ 元素在每个闭不变限制上像稠密，
   因而 $B_0(M,U_\zeta M)=0$。
   有限 Fourier 支撑、总本质支撑全测及柱限制秩论证使 $M$ 有限维，
   与原 $A$ 单射拟幂零矛盾。

这正是 R180 §9 的原证明；不存在尚待补充的无界域迁移。

此外，R171 排除正次数首一多项式在全部有限柱上恒为零，
故此分支的 $T$ 非零。
若 (3.5) 的向量为零，图循环核心将迫使 $T$ 为全域零算子，
同样矛盾。因此这里非零输出是自动的。

## 5. 可和分支：R152 与准确的非零性检验

现在设 $a\in\ell^1$。有
$$
X_b\in\mathcal A,\qquad
s=\chi(X_b)=a_*+\sum_j a_j.
$$
令 $S=X_b-sI$。
其字符为零且全部 gauge 差属于 $\mathcal G$。
R152 定理1.3/§7 应用于
$$
P_s(t)=(t+s)^2-B\in\mathcal G[t].
\tag{5.1}
$$
因此只要实际 $T=P_s(S)\ne0$，
它就单射稠密。

这里把非零性完整检验如下。
若 $s\ne0$，则 $\chi(T)=s^2\ne0$，$T$ 已是 $\mathcal A$ 单位。
若 $s=0$，令
$$
Q_j=a_j(R_j-I).
$$
这些算子绝对按范数可和，全部交换，且
$$
X_b=\sum_jQ_j,\qquad B=\sum_jQ_j^2,
$$
故
$$
\boxed{T=2\sum_{i<j}Q_iQ_j.}
\tag{5.2}
$$
若至少有两个非零系数，记其最早物理位为 $j_0<j_1$。
$Q_j$ 的首阶及首系数准确是
$$
\operatorname{ord}Q_j=2^j,\qquad
\gamma_{2^j}(Q_j)=-2a_jt_j/d_j.
$$
因此 (5.2) 的最低阶只能来自 $(j_0,j_1)$，
$$
\boxed{
\operatorname{ord}T=2^{j_0}+2^{j_1},\qquad
\gamma_{2^{j_0}+2^{j_1}}(T)
=\frac{8a_{j_0}a_{j_1}t_{j_0}t_{j_1}}{d_{j_0}d_{j_1}}\ne0.
}
\tag{5.3}
$$
绝对范数收敛和连续形式系数保证这里的取系数合法。
故 $T\ne0$。

若只剩一个非零 $a_j$ 且 $s=0$，
(5.2) 是空和，$T=0$。
点态上同样有
$$
u=a_j(\chi_j-1),\qquad
u^2+2a_j^2(\chi_j-1)=0.
$$
若 $a=0$，则 $T=a_*^2I$。
这些正好给 §1 的全部零输出例外。

只要 $T\ne0$，$e^w$ 的循环性又保证 $Te^w\ne0$：
一个有界交换乘子若杀掉循环向量，必在全空间为零。
所以算子与点态的非零性条件完全一致。

## 6. 图循环结论与范围修正

§§4--5 对所有非零输出都给 $\ker T=0$。
完整 $C$ 自伴性给 $\ker T^*=C\ker T=0$，
所以 $T$ 像稠密。由 (3.6)，主定理成立。

这是 R270B 的具体新结构接上旧 R152/R180 的推论。
R183 的首一特例也可作为无界分支的替代引用，
其 §§3--6 还完整给出正则最大图与全部核内高幂测试；
这里自然首一图已经由 R176 闭合，故不需要另扩大定义域。

结论不依赖 $B=A^2C$ 之类未证有界商，
不把 $\mathcal G$ 视为整个 $\mathcal A$ 的理想，
不把简单的 $X_M^2=B_M$ 或 $X_M$ 单射稠密单独当成排核。

这个精确二次抵消例已由并行 R270C 从开放范围移除，本稿提供旧定理接口的独立验证。
一般同阶辅助共振、多独立慢模式、规则 $1<\alpha\le3$
混合重根的剩余范围、正常湮灭者、实际边界缺陷与普通 ISP 均不因此完成。

## 原文接口

- R152：定理1.3 与 §7，任意有界加性模式的实际非零 $\mathcal G$ 系数多项式。
- R176：完整首一自然域、$C$ 自伴与指数向量图循环核心。
- R180：§1 定理1.2(1)、§§7--9 的秩零排核，§12.2 的任意 first 指数倾斜。
- R183：§§1、3--6 的同一无界慢方向快系数闭多项式，作为替代核对。
- R270 第二附录：§§2、4 的真实二阶消去和 $B\in\mathcal G$。
