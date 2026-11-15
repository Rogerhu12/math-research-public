# R709 — 原平面目标素数的连续单位前缀与全部精确饱和层整性

日期：2026-11-15。**状态：下述原平面来源的两个无例外整性结论已证明；旧短矩阵中指定同一修正的第二余类及主课题仍开放。**

本文保持原 $G_0\mathcal W_D$、其 canonical 系数格及全部十九角。得到两个不同结论。

第一，对实际目标惰性素数 $p$，一个显示的连续普通 Taylor 前缀在
$$
p>\frac{141}{2}D^2+O(D)
$$
时有列满秩的整单位子式。证明使用原截断 ODE 在每个实际因子上的接触能量及整个来源除子类的 nef 性，不经过一个辅助有理行列式的坏素数集。

第二，使用 R657 已付的特征零接触界，对同一来源的**全部精确饱和核旗标**，在
$$
p>\left(\frac{297}{20}+o(1)\right)D^2
$$
时每层算子范数均至多一。这个较小门只需低行整性及特征零旗标终止，**不**断言每个短前缀的像饱和。两个门均给出准确有限参数公式。

R644/R658 的五个正规 $z$ 来源属于另一空间；本文不删除它们边界定理中的 $v_p(\Delta_D)=0$，不并入七个 primitive 塔，也不新增完整中央零。

## 1. 同一来源、同一物理函数及两个整数界

取
$$
D\ge3,\qquad p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p.
\tag{1}
$$
保留
$$
d=1+8t,\qquad h_7=7+4t+16t^2,
$$
$$
\mathcal W_D=
\bigoplus_{n=0}^{D}Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
\tag{2}
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4,\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{3}
$$
标准列准确为 $C_{n,j}=Y^nq_n(t)t^j$，
$0\le j\le e_{n+1}$。本篇的来源格 $E_D$ 就是这些列的整数系数直和；
固定坏素数以外可局部化，范数始终是这些原系数的最大范数。

原固定特征零函数空间及评价为
$$
\mathfrak F_D=G_0\mathcal W_D,\qquad
\Phi(P)=G_0(w)P(t(w),\mathscr R(w)).
\tag{4}
$$
在当前 $p$ 的准确 Gaussian 分解中，
$$
\boxed{
\Phi(P)=c_*w^{13}U_0(w)
 e^{40a w^s/p}
 P\!\left(t(w),g(w)e^{a w^s/p}\right).
}
\tag{5}
$$
$a,c_*,U_0(0),t'(0)$ 是原单位。$G_0,\mathscr R$ 是固定的原来源，
不是随 $p$ 自由选择的替代函数；$P_{134}/U_0$、共同 charge 四十及 $w^{13}$ 全保留。

记 R680 的真实十九角除子为 $\mathcal B_D$，置
$$
c_D=C_D,\qquad u_D=2c_D+4,\qquad
M_D=f_D+C_D=5D+4-(D\bmod2).
\tag{6}
$$
其自交的准确整数为
$$
\boxed{\mathcal B_D^2
=4D^2+2Du_D-3\Sigma_4(D)-\Sigma_3(D)-4c_D^2.}
\tag{7}
$$
若 $D=4a+r$，$\Sigma_4(D)$ 是以下四元组的平方和：
$$
\begin{array}{c|c}
r&\text{四步链重数}\\ \hline
0&(a,a,a-1,a-1)\\
1&(a,a,a,a-1)\\
2&(a,a,a,a)\\
3&(a+1,a,a,a).
\end{array}
$$
若 $D=3a+r$，$\Sigma_3(D)$ 是
$(a,a,a-1)$、$(a,a,a)$、$(a+1,a,a)$ 中相应一组的平方和。
其余两条两步链的重数各为 $(c_D,c_D)$。所以 (7) 保持全部十九个实际中心，
而非以一个自由矩形替代原角帽。

定义
$$
\boxed{
Q_D=M_D+3\mathcal B_D^2+8D,\qquad L_D=13+Q_D.
}
\tag{8}
$$
由原取整式，
$$
\mathcal B_D^2=\frac{47}{12}D^2+\frac{35}{3}D+O(1),
\qquad
Q_D=\frac{47}{4}D^2+48D+O(1).
\tag{9}
$$
所有有限参数结论使用 (7)–(8)，不以 $O(1)$ 判断端点。

## 2. 任意一个实际值接触的目标 p 上界

本节不假设 $\mathcal EP$ 也有长零，不假设 $P$ 在原第一、第二或第三核中。

**引理 1。** 对任意非零 $\bar P\in\mathcal W_D\otimes k$，其中 $k$ 为当前剩余域，有
$$
\boxed{
\min\{\operatorname{ord}_t\bar P(t,g(t)),s\}\le Q_D.
}
\tag{10}
$$
若评价恒为零，左侧按 $s$ 计。$g$ 是 (5) 的同一原 regular 部，
仅使用 $g\equiv(1+8t)\Theta^{17}\pmod{t^s}$。
本节所有截断阶只读这个实际 $k[t]/(t^s)$ 元素；若写成完整 $k[[t]]$ 的阶，
任选其形式延拓后取与 $s$ 的最小值，结果与延拓无关。未假定原 regular 全尾模 $p$ 都已整。

**证明。** 将剩余域扩到代数闭包不改变非零或秩。
清除原分母，令
$$
\widehat P=d^{C_D}\bar P,\qquad r=\operatorname{ord}_t\widehat P.
$$
由全部原帽，
$$
0\le r\le\deg_t\widehat P\le M_D,\qquad
\deg_Y\widehat P\le D<p.
\tag{11}
$$
这里允许 $r=0$；R680 对两 jet 核证明的 $r\ge1$ 不在本引理中使用。

若 $r\ge s$，则左侧至多 $s\le M_D$，结论成立。
以下保 $r<s$。在 $\widehat P/t^r$ 的实际几何因子中，只取经过
$(0,1)$ 的非垂直因子，记为 $F_i^{m_i}$，
$b_i=\deg_YF_i\ge1$，其在原曲面上的严格变换为 $C_i$。
其他因子在该点是单位；$Y=0$ 也不经过该点。
垂直因子在该点的总贡献已经准确包含于 $t^r$。
因此
$$
\sum_i m_i b_i\le D,\qquad 1\le m_i<p.
\tag{12}
$$

在 $(0,1)$ 的完整局部 Hensel 因子中取全部根 $\psi_{i,j}$。
因 $b_i<p$，每个不可约因子关于 $Y$ 可分，其分裂域的 Galois 群阶整除
$b_i!$，所以分支扩张 tame。允许奇异点和分数 Puiseux 阶。
置
$$
h_{i,j}=\operatorname{ord}_t(\psi_{i,j}-g),\qquad
\bar h_{i,j}=\min(h_{i,j},s).
$$
局部 Hensel 分解的单位不改变接触阶，故
$$
\min\{\operatorname{ord}_t\bar P(t,g),s\}
\le r+\sum_i m_i\sum_j\bar h_{i,j}.
\tag{13}
$$
(13) 对一个根接触超过 $s$ 或评价恒零的情形仍成立：
截断总和不会大于把各非负项分别截断后再相加。
它没有把原低轴 ODE 延长过共振。

R680 §§3–4 在单个 $C_i$ 上已经支付下述三个事实：
$$
K_{F_i}^{E}\in H^0(X,\mathcal O_X(3C_i+L)),\qquad
K_{F_i}^{E}|_{C_i}\ne0,\qquad L C_i\le8b_i,
\tag{14}
$$
以及该完整 Hensel 因子的局部交数估计
$$
\sum_j\bar h_{i,j}+3\Delta_i
\le I_{(0,1)}(C_i,K_{F_i}^{E})
\le3C_i^2+LC_i.
\tag{15}
$$
$\Delta_i\ge0$ 是完整判别式阶。
这里的非零性来自原整数幂 ODE 共振：
在 $n=s-1$ 处 $6n+5=p$ 而前一项非零，故没有这样的 tame 代数解。
(15) 中 Euler forcing 的额外一份 $t$ 正好补回二阶方程可能损失的一阶。
这些证明对单个值接触就成立；R680 后来使用的第二 jet 和根对能量
不是 (14)–(15) 的前提。
因此
$$
\sum_j\bar h_{i,j}\le3C_i^2+8b_i.
\tag{16}
$$

各 $C_i$ 均由 R680 引理2为 nef，特别 $C_i^2\ge0$。
令
$$
\mathscr C=\sum_i m_i C_i.
$$
它是同一个实际截面的部分除子，所以
$\mathcal B_D-\mathscr C$ 有效。$\mathcal B_D$ 与 $\mathscr C$ 都 nef，故
$$
\mathscr C^2\le\mathcal B_D^2.
\tag{17}
$$
同时不同不可约曲线的交数非负，因而
$$
\sum_i m_i C_i^2
\le\sum_i m_i^2C_i^2
\le\mathscr C^2.
\tag{18}
$$
重复因子没有被当成不同根；它们的真实 $m_i$ 保留在 (12)、(13)、(18) 中。

将 (11)–(18) 合并，得到
$$
\min\{\operatorname{ord}_t\bar P(t,g),s\}
\le r+3\mathscr C^2+8\sum_i m_i b_i
\le M_D+3\mathcal B_D^2+8D=Q_D.
$$
这证明 (10)。整个论证使用原实际因子、同一个十九角线性系和至多 $s$ 的接触；
没有免费增加来源列。证毕。

## 3. 原普通低行的准确整性范围

**引理 2。** 在 (1) 下，(5) 的所有原标准列在普通 $w$ 行
$$
0\le k<13+s
\tag{19}
$$
上系数均整。对任意 $H<s$，其行 $0,\ldots,13+H$ 的模 $p$ 评价，
除共同零行和原单位三角变换外，准确为
$$
P\longmapsto P(t,g(t))\pmod{t^{H+1}}.
\tag{20}
$$

**证明。** R618/R657 保持原 $g,t/w,U_0$ 的完整 regular 高尾；
它们的相关单位系列满足
$$
v_p(c_n)\ge-\lfloor6n\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}.
$$
当 $0\le n<s$ 时 $6n\tau_2<1$，故这些低系数整。
原 $q_n(t)t^j$ 只有 $d$ 的负幂，而 $d(0)=1$；全部其余角因子有整系数。
因此同一来源的 regular 评价到次数 $<s$ 整。

(5) 中每个第一 Gaussian 都从 $w^s$ 起。
共同 $w^{13}$ 说明这些项在绝对普通行 $13+s$ 之前完全没有贡献，
不是将高 Gaussian 免费删除。$U_0$ 是低窗整单位，
$t(w)=t'(0)w+\cdots$ 的首系数为单位；其复合逆的低系数也整，
可按首项逐次解而不除以次数。
所以对 $H<s$，乘 $c_*U_0$ 及换参 $w\leftrightarrow t$
给该低窗的整可逆三角变换，证明 (19)–(20)。证毕。

这里保留了真正的共同 $w^{13}$。因此最后可读的低整行是
$s+12$，而非提前截成 $s-1$；第 $s+13$ 行开始必须恢复原 Gaussian 分母。

## 4. 目标素数处的连续单位前缀

**定理 3。** 若 (1) 成立且
$$
\boxed{Q_D<s,\quad\text{等价于}\quad p>6Q_D-1,}
\tag{21}
$$
则原普通系数矩阵
$$
\boxed{
\mathsf T_{D,p}
=\bigl([w^k]\Phi(C_{n,j})\bigr)_{
0\le k\le L_D,\ (n,j)}
}
\tag{22}
$$
是整矩阵，模 $p$ 全列秩。它有一个原系数的列满秩单位子式及整左逆；
其像在 $\mathcal O^{L_D+1}$ 中为直和因子，全部非零 Smith 因子都是单位。

**证明。** 整性由引理2和 $L_D=13+Q_D<13+s$。
若一个原单位系数向量在 (22) 的约化核内，则其非零约化
$\bar P\in\overline{\mathcal W}_D$ 满足
$$
\operatorname{ord}_t\bar P(t,g)\ge Q_D+1.
$$
由于整数 $s\ge Q_D+1$，
$\min(\operatorname{ord}_t\bar P(t,g),s)>Q_D$，
违反引理1。因此约化矩阵满列秩。
选其中一个非零列满秩子式即可得到原整单位子式；其单位逆给整左逆。
DVR 上这等价于显示的分裂单射和单位 Smith 因子。证毕。

由 (9)，本定理的明确目标素数门为
$$
p>\max\{101,f_D,6Q_D-1\}
=\frac{141}{2}D^2+O(D).
\tag{23}
$$
“无例外”指每个满足该门的好惰性目标 $p$，没有额外的
$p\nmid\Delta_D$ 条件。证明没有选辅助素数。

(22) 是完整连续普通前缀，包括原十三个零行；没有抽出非连续观测来替代前缀。
本定理只保证这个长度及更长的**仍整**矩阵含有该单位子式，
不推断更短前缀的像也饱和。它也不是旧三块矩阵 $M$ 的满射定理。

## 5. 精确饱和旗标的更小无例外门

对同一固定特征零评价 (4)，记
$$
r_k(P)=[w^k]\Phi(P),\qquad
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D.
\tag{24}
$$
令 $\varphi_D^k=r_k|_{K_{D,k}}$，范数从原标准列的最大系数范数继承。
这与 R579 式(2) 的饱和前缀定义相同，但来源只取 (2)，不是九坐标格。

使用 R657 的明确有理终止界。令 $q_D$ 为满足
$$
q_D\equiv5\pmod6,\qquad q_D>\max(101,f_D)
$$
的最小素数，$s_D=(q_D+1)/6$。本节只有这个 $q_D$ 是辅助素数。
置
$$
b_n=A_n+e_{n+1},
$$
$$
C_u=\sum_{n=0}^{D}
\left(\left\lfloor\frac{b_n+13-u}{s_D}\right\rfloor+1\right)_+,
\quad 0\le u<s_D,
$$
$$
\boxed{
J_D^{\rm aux}
=\max_{\substack{0\le u<s_D\\C_u>0}}
\{u+s_D(C_u-1)\}.
}
\tag{25}
$$
这里 $b_n$ 不加一，$J_D^{\rm aux}$ 是最大行号，连续长度是
$J_D^{\rm aux}+1$。R657 的原完整高尾与合流证明准确给
$$
K_{D,k}=0\quad(k>J_D^{\rm aux}),\qquad
J_D^{\rm aux}=\left(\frac{99}{40}+o(1)\right)D^2.
\tag{26}
$$

**定理 4。** 对每个实际目标惰性素数 $p=6s-1$，若
$$
\boxed{
p>101,\quad f_D<p,\quad
J_D^{\rm aux}<13+s,
}
\tag{27}
$$
则在同一个原系数范数下，对所有 $k\ge0$，
$$
\boxed{\|\varphi_D^k\|_p\le1.}
\tag{28}
$$
一个完全明确的充分门是
$$
\boxed{
p>\max\{101,f_D,6(J_D^{\rm aux}-13)-1\}.
}
\tag{29}
$$
它的主常数为
$$
\frac{297}{20}D^2+o(D^2).
\tag{30}
$$

**证明。** 先说明没有在“饱和”二字中漏掉来源分母。
对有限前缀的有理系数方程统一清分母，得到一个整数矩阵。
其整数核正是 (24)，并为饱和子模。
$\mathbf Z_p$ 平坦，且清分母后的目标无挠，故
$$
K_{D,k}\otimes\mathbf Z_p
=
\ker_{\mathbf Q_p}(r_0,\ldots,r_{k-1})
\cap(E_D\otimes\mathbf Z_p).
\tag{31}
$$
因此 (28) 的单位球是原系数整、前缀**准确为零**的实际来源，
不是一个模 $p$ 核，也不是对评价像另作不明代价的除 $p$ 操作。

若 $k\le J_D^{\rm aux}$，由 (27) 和引理2，
$r_k$ 的每个原列系数都整。所以 $r_k$ 在整个 $E_D\otimes\mathbf Z_p$
上的范数就至多一，限制到 (31) 后仍如此。
若 $k>J_D^{\rm aux}$，(26) 给该来源核为零，算子为零。
这覆盖全部 $k$，并给 (28)。

(30) 由 (26) 直接乘六，固定的十三行不改变二次主项。
固定模数六的素数定理及其在 (25) 中的全部取整计算已经在 R657 §5 支付；
本篇不增加增长模数或短区间假设。证毕。

此证明只用辅助 $q_D$ 证明特征零有限矩阵满列秩，
没有要求同一有理子式在目标 $p$ 处为单位。
因此不能将 (28) 反读为“(25) 的前缀在每个目标 $p$ 处有单位子式”。
后一个更强断言由定理3在其较大显示前缀和较大门中独立支付。

## 6. 与既有证书、原成本及同一个 R 的边界

两种“饱和”须区分：

| 对象 | 本篇准确结论 |
|---|---|
| 长度 $L_D+1$ 的目标 $p$ 原普通前缀像 | 在 (21) 下分裂、全列单位 Smith |
| 任意长度的特征零精确核旗标 (24) | 在较小的 (27) 下每层范数至多一 |
| 任意更短前缀的整评价像 | 未由定理4认作饱和 |
| R644/R658 的五来源辅助边界空间 | 不属于本篇的免费扩大范围 |

R657 §6 原来提醒“辅助素数的有理子式非零不控制其他素数分子”，
这一提醒完全保留。若只据那个子式去断言目标 $p$ 单位，确实不成立。
本篇增加的是两项独立输入：定理3的原目标 $p$ 接触论证，以及
定理4对**精确来源核旗标**使用的低行整性和终止。
所以 R657 当时尚未给出的全部饱和层整性，现在在 (27) 的明确范围内得到补充；
没有删除 R644 边界证明真正需要的 $v_p(\Delta_D)=0$。

两个门只对同一个 canonical 平面格 $G_0\mathcal W_D$ 成立。
从别的单项式格、三来源归一化格或九坐标格返回本格时，
真实 conductor、预算变化和系数范数须各自保留。
尤其不把 R644 的额外 $z/H$ 方向、七塔或五来源并入 (2)。

本篇也没有给任何新列完整中央零。
即使将二次 cutoff 配回原平面的 Gaussian 正包络，
它本身仍不足支付 R418 的严格斜率门；不能以“全部大 $p$ 低层整”
代替整个不同来源格所需的全次数成本。

最后，旧目标 $M$ 的原两长块、一短块、两组十三行及同一
$P_2=P_{\rm fact}+pR$ 均不变。
本文的长普通前缀与 (24) 的精确核不能替代原
$K_1(M)$、$K_2(M)$、$d_2$ 或 $C_R$ 的真实像。
R697/R701 的两个 normal 补项、非单位乘子及下一位 carry 继续保留。
临界 $p/D^2\to47/8$ 并不满足本文这两个较大的统一门；
指定 forcing 的非零仍须在原短窗口内证明。

## 依赖

- [R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)：
  全十九角来源类、nef、原 Euler 三次 forcing 的极帽及单点截断接触。
- [R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)：
  原连续长前缀、完整高尾、明确 $J_D^{\rm aux}$ 及其 $99/40$ 主常数。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  同一原 regular 高尾的全系数估值。
- [R579](R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md)：
  精确饱和来源旗标及系数范数的定义；本篇不使用其九坐标范围扩张。
- [R644](R644-bounded-degree-original-polynomials-and-full-boundary-obstruction.md)、
  [R658](R658-original-auxiliary-gaussian-minor-and-quadratic-jet-bound.md)：
  五来源辅助空间、目标素数单位子式条件与本篇范围的区别。

本篇为全参数证明，不新增目标素数扫描或可重算数据文件。
