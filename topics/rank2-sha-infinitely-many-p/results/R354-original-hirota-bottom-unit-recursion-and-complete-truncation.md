# R354 — 原 Hirota 的完整底部单位递推与 degree-s 截断条件

日期：2026-11-13。**状态：以下原实际核的底部递推、整个无共振范围、
degree-$s$ 截断的充分必要条件，以及原 Faber 三行的同一单参数表达
均已证明。没有从递推唯一性推出任何指定末行非零；主目标未完成。**

本篇接 [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)、
[R343](R343-original-three-torsion-phase-and-two-complete-faber-observers.md)、
[R349](R349-critical-faber-cubic-row-and-complete-norm-three-projections.md)。
它把 R349 的实际理想消元化成完全明确的一变量问题，保留所有
degree 截断及完整 norm-three 条件。

## 1. 原对象与变量

固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad p=6s+1>7,\quad
D=d/dz,\quad Dx=2y,\quad Dy=3x^2,
$$
$$
H=\binom{3s}{s}b^s,\qquad \epsilon_3=b^{3s}\in\{1,-1\}.
\tag{1}
$$
以下所有 polynomial identities 在原普通剩余域 $\mathbf F_p$ 中。
真实可分核为
$$
f_V=P(X),\qquad X=x^3,\quad
P(X)=\sum_{n=0}^sP_nX^n,\quad P_s=1,\quad P_0\ne0.
\tag{2}
$$
R336 已支付
$$
\frac{P_1}{P_0}=-\frac{H^3\epsilon_3}{24b}.
\tag{3}
$$
所有 $X$ 导数写作撇号，$D$ 始终是曲线上的原不变导子。

## 2. 原 Hirota 在 X 中的完整形式

真实核满足
$$
D^2\log P=-H^2x(V).
$$
使用 $D^2x(V)=6H^2x(V)^2$、$g_2=0$，得到
$$
P D^4P-4(DP)(D^3P)+3(D^2P)^2=0.
\tag{4}
$$
它是 R349 中的同一实际 Hirota 恒等式。

令
$$
S=(7X+4b)P'+6X(X+b)P'',\qquad A=S+3XS'.
\tag{5}
$$
四次导数逐项为
$$
DP=6x^2yP',\quad D^2P=6xS,\quad
D^3P=12yA,\quad
D^4P=36x^2\{A+2(X+b)A'\}.
\tag{6}
$$
因此在函数域中约去共同 $36x^2$ 后，(4) 等价于多项式恒等式
$$
\boxed{
P\{A+2(X+b)A'\}-8(X+b)P'A+3S^2=0.
}
\tag{7}
$$
约去的是非零函数，不是只在 $x\ne0$ 的数值点断言结论；故 (7)
也控制 $X=0$ 的全部系数。

写 $S=\sum S_nX^n$。准确的三角表达是
$$
\boxed{
S_n=n(6n+1)P_n+2b(n+1)(3n+2)P_{n+1}.
}
\tag{8}
$$
又 $A_n=(3n+1)S_n$，而 $A+2(X+b)A'$ 的第 $n$ 项为
$$
(2n+1)(3n+1)S_n+2b(n+1)(3n+4)S_{n+1}.
\tag{9}
$$

## 3. 每一步真正解出的系数与无共振范围

在 (7) 的 $X^n$ 项中，$P_{n+2}$ 只由第一乘积中
$P_0\cdot2b(n+1)(3n+4)S_{n+1}$ 贡献。其系数恰为
$$
\boxed{
4b^2P_0(n+1)(n+2)(3n+4)(3n+5).
}
\tag{10}
$$
其他各项只涉及 $P_0,\ldots,P_{n+1}$。因此只要 (10) 是单位，
该行唯一确定 $P_{n+2}$。

对全部
$$0\le n\le2s-2$$
四个整数因子都小于 $p$ 且非零；最大者 $3n+5$ 为 $p-2$。
$b,P_0$ 也是单位。因此 (10) 在这个整个范围内都是单位。
尤其实际需要的 $P_2,\ldots,P_s$ 完全由 $P_0,P_1$ 确定。

第一个可能的共振是
$$n=2s-1,\qquad 3n+4=p.$$
它在所需的 degree-$s$ 系数之外，不能被误写成底部递推中的
未知除法。另一方面，也不能因递推无共振就忽略高于 $s$ 的系数：
真实核要求它们全部截断，§5 给完整条件。

例如令 $q=P_1/P_0$，第零行给
$$
\boxed{\frac{P_2}{P_0}=-\frac{3q}{8b}-\frac{q^2}{10}.}
\tag{11}
$$
这里的非线性项是实际 Hirota 交叉项，不能省略。

## 4. 去掉 b 与整体尺度后的通用一参数递推

置
$$
U=X/b,\qquad R(U)=P(bU)/P_0,\qquad
t=bP_1/P_0.
\tag{12}
$$
实际参数由 (3) 精确给出
$$\boxed{t=-H^3\epsilon_3/24\ne0.}\tag{13}$$
设
$$
R(U)=\sum_{n\ge0}r_n(t)U^n,\qquad r_0=1,\quad r_1=t.
$$
(7) 在此规范中不再含 $b$：
$$
R\{\mathcal A+2(U+1)\mathcal A'\}
-8(U+1)R'\mathcal A+3\mathcal S^2=0,
$$
$$
\mathcal S=(7U+4)R'+6U(U+1)R'',\qquad
\mathcal A=\mathcal S+3U\mathcal S'.
\tag{14}
$$

以下系数规则完整定义 $r_2,\ldots,r_{2s}$，不是仅仅声称存在递推。
令
$$
e_n=n(6n+1)r_n+2(n+1)(3n+2)r_{n+1},\quad
a_n=(3n+1)e_n,
$$
$$
d_n=(2n+1)a_n+2(n+1)a_{n+1}.
\tag{15}
$$
负指标取零。(14) 的第 $n$ 个系数是
$$
\begin{aligned}
\mathcal H_n={}&\sum_{i+j=n}r_i d_j
-8\sum_{i+j=n}(i+1)r_{i+1}a_j\\
&-8\sum_{i+j=n-1}(i+1)r_{i+1}a_j
+3\sum_{i+j=n}e_i e_j.
\end{aligned}
\tag{16}
$$
先将 $r_{n+2}$ 置零，记所得多项式为 $\mathcal H_n^{(0)}$。
则准确递推为
$$
\boxed{
r_{n+2}=
-\frac{\mathcal H_n^{(0)}}
{4(n+1)(n+2)(3n+4)(3n+5)}
\qquad(0\le n\le2s-2).
}
\tag{17}
$$
各 $r_n$ 是 $\mathbf Z_{(p)}[t]$ 中的显式多项式，且 $\deg_t r_n\le n$。
整性由 §3，次数界由 (15)–(17) 归纳。初始三项是
$$
\boxed{
r_2=-\frac38t-\frac1{10}t^2,\qquad
r_3=\frac{93}{448}t+\frac3{40}t^2-\frac1{210}t^3.
}
\tag{18}
$$
(16) 的第零、一行直接核定这些常数；没有改变原不变导子。

## 5. 完整 degree-s 截断条件是充分必要的

对一个参数 $t$，令
$$R_s(U;t)=\sum_{n=0}^{s}r_n(t)U^n.$$
假定 $r_s(t)\ne0$，以保证准确次数为 $s$。则：

**截断定理。** $R_s$ 满足整个 (14)，当且仅当
$$
\boxed{r_{s+1}(t)=r_{s+2}(t)=\cdots=r_{2s}(t)=0.}
\tag{19}
$$

若 $R_s$ 满足 (14)，对 $n=0,\ldots,2s-2$ 按 (17) 的唯一性比较，
得到 (19)。反向则要核定高阶边界，不能只说初始递推已足够。

当 $R_s$ 的次数至多为 $s$，$\mathcal S$ 的最高候选项是
$s(6s+1)r_sU^s$，在当前特征中为零，所以
$\deg\mathcal S,\deg\mathcal A\le s-1$。
(14) 的残差次数至多 $2s-1$。由 (19)、(16)，次数
$0,\ldots,2s-2$ 的项全部为零。

最后令 $e=[U^{s-1}]\mathcal S$。残差的 $U^{2s-1}$ 系数准确为
$$
r_s(3s-2)e\{(2s-1)-8s\}
=-(6s+1)r_s(3s-2)e=0.
\tag{20}
$$
因此整个残差为零，证明充分性。也就是说，第一个共振行在这个
真正 degree-$s$ 截断里由 (20) 自动支付；没有删除一个未检验条件。

此定理并不宣称任意 $t\ne0$ 都满足 (19)。
真实参数 (13) 必须同时满足全部这些高次多项式条件。

## 6. 原完整 norm-three 在同一个单参数中

monicity 给出准确尺度
$$
P_0=\frac{b^s}{r_s(t)},\qquad
P(X)=\frac{b^s}{r_s(t)}R_s(X/b;t).
\tag{21}
$$
令
$$
\phi(U)=-\frac{(U+4)^3}{27U^2},
$$
$$
\mathcal T_R=
36U(U+1)(R'^2-RR'')-6(7U+4)RR'.
$$
把 (21) 代入 R336 的完整 norm-three 多项式恒等式，所有尺度准确相消，
得到
$$
\boxed{
r_s(t)^2 U^{2s}R_s(\phi(U);t)=R_s(U;t)\mathcal T_{R_s}(U;t).
}
\tag{22}
$$
$U^{2s}$ 清除左边的全部分母；(22) 是最高次数 $3s$ 的完整
多项式等式。后续理想消元必须保留它的全部系数，不能只保留
R349 的某一条 polar 投影。

尤其在 $U=0$，左边只保留 $R_s$ 的最高次项。由于
$(-27)^s=1$、$64^s=1$，给
$$
\boxed{r_s(t)^3=-24t.}
\tag{23}
$$
这里 $(-27)^s=1$ 来自原普通嵌入中的 $\delta^{p-1}=1$，
不是另选立方根的规范。(23) 也再次确认真实参数的 $r_s$ 是单位，
与 (21) 的合法性一致。它只是 (22) 的一个具体系数，不能替代
整条 norm-three。

## 7. 两旧行与新三次行的准确一变量表达

定义不再含 $b$ 的原 Faber 多项式
$$\mathfrak F_j(U)=b^{-j}F_j(bU).$$
由于同一曲线的权齐次性，这就是 $b=1$ 的相同原基。
写
$$
R_s(U;t)=\beta_0(t)+\sum_{j=1}^{s}\beta_j(t)\mathfrak F_j(U).
\tag{24}
$$
基变换是整的上三角变换，$\beta_s=r_s$；
由 (21) 得所有准确尺度
$$
\boxed{\alpha_j=\frac{b^{s-j}}{r_s(t)}\beta_j(t).}
\tag{25}
$$

设
$$
Q_\beta(t)=
\sum_{j+k=s+1}\{-18(j-k)^2-3(s+1)\}\beta_j(t)\beta_k(t),
$$
$$
K_\beta(t)=486\sum_{j+k+l=2s}jkl\,
\beta_j(t)\beta_k(t)\beta_l(t).
$$
则 R343、R349 的三个真实观察分别是
$$
\boxed{
\mathcal L=\frac{b^{s-1}}{r_s}\beta_1,\qquad
\mathcal Q=\frac{b^{s-1}}{r_s^2}Q_\beta,\qquad
\mathcal K=\frac{b^s}{r_s^3}K_\beta.
}
\tag{26}
$$
因此原两行同零恰对应 $\beta_1(t)=Q_\beta(t)=0$，但只在真实参数
满足 (13)、(19)、(22) 和 $r_s\ne0$ 的前提下。
新三次行仍具有 R349 的完整临界 carry：
$$
\frac{b^s}{r_s^3}K_\beta=-\eta-\frac92H.
\tag{27}
$$
这里没有重新忽略 $p t_0=-H$ 或 $y^p$ 的临界修正。

(17)、(19)、(22)、(24) 现在给出一个完全明确的一变量理想问题。
递推唯一性保证没有自由选择遗漏的核系数；它不保证一个特定
$\beta_1$ 或 $Q_\beta$ 在真实参数上非零。本篇尚未证明
$K_\beta$ 在完整条件商环中属于 $(\beta_1,Q_\beta)$，也没有将
(27) 的单位性当作这项归属的证明。

## 8. 同一个既有纤维核规范

仍只使用 R336 的 $p=13,b=17$。此时 $s=2$、$b\equiv4$、
$P=X^2+7X+7$，故 $t=bP_1/P_0=4$。准确有
$$r_2(4)=6,\qquad r_3(4)=0,$$
且由 (21)
$$P_0=b^2/r_2=7,\quad P_1=P_0b^{-1}r_1=7,\quad P_2=1.$$
(23) 也给 $r_2^3=8=-24t$。这些有限数只核原规范；所有次数与
无共振的论证在 §§2–7，对全部当前普通素数成立。

本篇通过 GitHub Contents API 提交小文本时执行环境不可用；
这不是一次本地 git pull，也不声称新运行了未执行的扫描或脚本。
