# R459 — 真角含量与保留 t 次数的三次首提升判据

日期：2026-11-14。**状态：已证明。** 本篇保留实际 canonical 格强迫的 $t$ 因子，给出全部角层的真实 charge 集，并对 $\bar P=t^rF^3Q$ 的首次提升推导三个实际接触条件。无需预先保持因子，两条完整 carry 已强制首次修正在同一个 $F$ 正规分支上有一个单位 $5$ 的法向导数首项；当更低一条分支值仍在可读窗内时，它另有单位 $-2$ 的首项。这两个量中的未知 $\xi$ 严格消去。因此真实提升必须离开 $F^2$ 理想，在后一范围甚至必须离开 $F$ 理想。由同格修正空间或明确结式界，可以得到完整排除判据；没有将首次修正免费除以 $t^r$。

本篇单位 $5$、$-2$ 的必要条件均以第3节式 (11) 的相对 $J$ 层 $p^2$ 提升为前提；整个原 $M$ 的两条十三行 carry 余核仍按第7节保留，不能直接删掉。R475 进一步明确了这个适用范围。

本篇给的是同一实际格中的必要条件和可用的排除判据，尚未给出满足全部高接触及保因子条件的具体低预算原首核。矩形结式界不被预设为通常 Padé 或全部临界窗的性质。R456 的纯三次单位余因子范围为空，按其已发布更正保留；本篇不撤回该来源约束。

## 1. 原最低角层及所有角层的准确电荷

保持 R453/R456 的 $p=6s-1>83$、$L=2s+\ell$、
$1\le\ell<s-13$、$0\le J\le16$，以及
$$
\widetilde{\mathcal W}_{D,J}
=\bigoplus_{n=0}^D\bigoplus_{j=0}^J
\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}+6j}T_0^j.
\tag{1}
$$
仍有 $\mathscr R=\Theta^{17}d$、$T_0=\Theta^{36}f$，
$d=1+8t$、$f=d\,t(t-1)h_7/7$。每一 $(n,j)$ 分量在真实多项式环 $\mathcal O[t,\Theta]$ 中的最小 $t$ 阶是
$$
m_{n,j}=A_n+j,\qquad A_n=\lfloor(n+1)/4\rfloor,
$$
其相对 charge 和 $\Theta$ 指数分别为
$$
q_{n,j}=n+36j/17,\qquad 17n+36j.
$$
由于 $0\le j\le16$，这些 $\Theta$ 指数彼此不同；这个多项式独立性在模 $p$ 后也成立。

因此，在实际 $t$ 过滤
$(\widetilde{\mathcal W}_{D,J}\cap t^r\mathcal O[t,\Theta])$
的第 $r$ 层，出现的 charge **准确**为
$$
\boxed{\mathscr Q_r=\left\{n+\frac{36j}{17}:
0\le n\le D,\ 0\le j\le J,\quad
A_n+j\le r\le A_n+j+e_{n+1}+6j\right\}.}
\tag{2}
$$
原未扩充格的条件是删去右端的 $6j$。证明是在每个独立部分将其单位角因子消去，只问允许多项式是否被 $t^{r-A_n-j}$ 整除；这没有把形式单位的逆加入来源。

特别有 $j\le r$、$n\le4(r-j)+2$。在 $r=0$ 时仅有 $j=0,n=0,1,2$，所以
$$
P(0,\Theta)=c_0+c_1\Theta^{17}+c_2\Theta^{34},
\tag{3}
$$
不存在的 $n$ 项取系数零。三个真实径向常数行是这一个二次式在 $\Theta=1$ 的 $1,\mathcal E,\mathcal E^2$ 值，其中
$\mathcal E=(\Theta/17)\partial_\Theta$。其 $3\times3$ Vandermonde 为单位；原第三块因 $\ell\ge1$ 确实读到常数行。因此
$$
\boxed{\bar P\in\ker\bar J\quad\Longrightarrow\quad
t\mid\bar P\quad\text{于真实 }k[t,\Theta].}
\tag{4}
$$
这给 R456 更正的完整理由。若 $\bar P=F^3Q$，且 $F_\Theta(0,1)$、$Q(0,1)$ 都为单位，则 $F(0,\Theta)^3Q(0,\Theta)$ 非零，不能满足 (3) 的三重根条件；该范围确实为空。

在 $r=1$、$D\ge6,J\ge1$ 时，(2) 则有十条真实 charge：$j=0$ 的 $n=0,\ldots,6$ 与 $j=1$ 的 $n=0,1,2$。三重根不再被角层本身排除。例如
$$
t(t-1)h_7(\mathscr R-1)^3\in\mathcal W_{3,0}
\tag{5}
$$
是实际来源：四个径向系数分别除以 $q_0,q_1,q_2,q_3$ 后为允许多项式。式 (5) 仅说明带角含量的因子形状确实能出现在原格；它的接触阶不足以成为当前窗口首核，不能把它说成一个已找到的深类。

## 2. 保原 regularized 轴的三次接触

同 R456 置
$$
\vartheta=(g/d(t))^{1/17},\qquad
\Theta_{\rm phys}=\vartheta e_2(a\epsilon/17),\qquad
w^s=p\epsilon,\quad a=p\kappa\in\mathcal O^\times.
$$
对任意局部整来源 $P$ 写
$P_i(w)=(\mathcal E^iP)(t(w),\vartheta(w))$。完整实际评价仍为
$$
\boxed{J(P)=\left(
[P_0]_{<s},\quad
[aP_1+p\mathscr SP_0]_{<s},\quad
\left[\frac{a^2}{2}P_2+pa\mathscr SP_1+p^2\mathscr S^2P_0\right]_{<\ell}
\right),}
\tag{6}
$$
其中 $\mathscr S$ 是完整 $s$ 阶移位，而不是自由尾项。

现在取一个非零实际来源约化
$$
\boxed{\bar P=t^rF^3Q,\qquad r\ge1,\qquad
F\text{ 不可约},\quad F(0,1)=0,\quad
F_\Theta(0,1)Q(0,1)\ne0.}
\tag{7}
$$
设其真实接触
$$
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w)),\qquad1\le h<s.
$$
这里 $t$ 不被当作单位：$t(w)=-w+\cdots$。由于 $\mathcal EF$ 为单位，三个 regularized Euler 值的阶准确是 $r+3h,r+2h,r+h$。所以
$$
\boxed{\bar P\in\ker\bar J
\quad\Longleftrightarrow\quad r+2h\ge s,\qquad r+h\ge\ell.}
\tag{8}
$$
以下置
$$
k=2h+r-s\ge0.
\tag{9}
$$
定理的两条 carry 都真正可读的窗口是
$$
\boxed{k<\min(s-h,\ell,h).}
\tag{10}
$$
最后一个 $k<h$ 用来保留而排除更高的 $\mathcal EH$ 项；它不能悄悄省去。

## 3. 真首次修正必须满足三个接触条件

假设存在同一格中的提升 $P^{(2)}$，满足
$$
P^{(2)}\bmod p=t^rF^3Q,\qquad J(P^{(2)})\in p^2\Gamma_L.
$$
取保持双次数的系数提升 $\widetilde F,\widetilde Q$，准确写成
$$
\boxed{P^{(2)}=t^r\widetilde F^3\widetilde Q+pR.}
\tag{11}
$$
允许的 $\bar R$ 是 R456.13 的真实仿射修正空间；没有假定 $R$、$F$、$Q$ 分别在原格，更没有假定 $t^r\mid R$。

令
$$
q=\min(r,k).
$$
在 (10) 中 $q<\ell$、$h+q<s$、$q<h$。**真正必要条件**是
$$
\boxed{
\operatorname{ord}\bar R_0\ge s,\qquad
\operatorname{ord}\bar R_1\ge h+q,\qquad
\operatorname{ord}\bar R_2\ge q.}
\tag{12}
$$

**证明。** 写
$$
f=\widetilde F(t(w),\vartheta(w))=w^hu+p\xi,
\qquad e=(\mathcal E\widetilde F)(t(w),\vartheta(w)),
$$
其中 $\xi\in\mathcal O[w]_{<h}$、$u(0)e(0)$ 为单位。另写
$$
C(w)=\left(\frac{t(w)}w\right)^r
\widetilde Q(t(w),\vartheta(w))\in\mathcal O[[w]]^\times.
\tag{13}
$$
$C$ 只是实际整系数的记号；未倒置 $t^r$ 运输核。

第一块中
$w^r C f^3\equiv w^{r+3h}Cu^3+3pw^{r+2h}Cu^2\xi\pmod{p^2}$。
因 $r+2h\ge s$，整个低块已经被 $p^2$ 整除，所以 $\bar R_0$ 的阶至少为 $s$。

第二块首次商的 Gaussian 部分最低可能阶为 $r+h$，来自 $6a w^{r+h}Cu\xi e$；真正进位 $\mathscr S(t^r\bar F^3\bar Q)$ 的最低阶是 $3h+r-s=h+k$。含 $\mathcal EQ$ 的其余项从 $r+2h\ge s$ 起，不进入这个低块。于是两者总和至少有 $h+\min(r,k)=h+q$ 阶，得到 $\bar R_1$ 的界。

第三块首次商的最低 Gaussian 项是 $3a^2w^rC\xi e^2$；其余含 $f^2$ 的项至少从 $r+h\ge\ell$ 起。进位 $a\mathscr S\mathcal E(t^rF^3Q)$ 最低可能阶为 $k$；含 $\mathcal EQ$ 的额外项更高。故第三块的 forcing 至少有 $q$ 阶。$a^2/2$ 为单位，得到 $\bar R_2$ 的界。全部断言只读取 (10) 保证存在的实际行。$\square$

## 4. 不先保持因子的真实非零分支余项

记 $\psi(t)$ 为 $F(t,\psi)=0$、$\psi(0)=1$ 的唯一正规分支。以下 $R$ 指 (11) 首次修正的约化，$a,u,e,C,\xi$ 也取同一实际约化。所有分支式仍以原 $t(w)$ 参数化；其阶等于 $t$ 阶。

**定理 1。** 不假设 $F\mid R$ 或 $F^2\mid R$，每个真正的 (11) 都必须满足
$$
\boxed{
(\mathcal ER)(t(w),\psi(t(w)))
=\frac5a C(0)u(0)^3w^{h+k}+O(w^{h+k+1}).}
\tag{13a}
$$
如果再有 $2h+k<s$，准确等价于 $r>2k$，则还必须满足
$$
\boxed{
R(t(w),\psi(t(w)))
=-\frac{2C(0)u(0)^4}{a e(0)}w^{2h+k}
+O(w^{2h+k+1}).}
\tag{13b}
$$
两个显示首系数都是单位，且均不含自由的根修正 $\xi$。因此在 (10) 内，任何真实首次修正必不被 $F^2$ 整除；在 (13b) 的更窄可读范围中，连 $F$ 整除也不可能。

**证明。** 直接保留 (6) 中两条实际 carry，在所需的有限低轴上有
$$
\begin{aligned}
R_1&\equiv-6w^{h+r}Cu\xi e-a^{-1}w^{h+k}Cu^3
                                      &&\pmod{w^s},\\
R_2&\equiv-6w^rC\xi e^2-6a^{-1}w^kCu^2e
                                      &&\pmod{w^{k+1}}.
\end{aligned}
\tag{13c}
$$
第一个式子中含 $\mathcal EQ$ 的首次商从 $r+2h\ge s$ 起；第二个式子中它们的真正进位从 $h+k$ 起。这就是能够排除它们的准确原因。这里也保 $R_0=0\pmod{w^s}$。

令 $\delta=\bar\vartheta-\psi$。由 $F_\Theta$ 为单位，
$$
\delta=\frac{\bar\vartheta}{17e}w^hu+O(w^{2h}).
$$
将 $\mathcal ER$ 作为一个完整多项式函数展开到真分支，得到
$$
(\mathcal ER)(\psi)
\equiv R_1-\frac{w^hu}{e}R_2\pmod{w^{h+k+1}}.
$$
全部二次 Taylor 项至少有 $2h$ 阶，而 $k<h$；$\delta$ 的二次误差乘 $R_2$ 也至少有 $2h+q$ 阶。因此上述截断没有遗漏可读项。代入 (13c)，两个含 $\xi$ 的整段准确相消，留下
$5a^{-1}w^{h+k}Cu^3$，证明 (13a)。这里 $h+k<s$ 和 $k<\ell$ 是两条输入行真的存在的条件。

再设 $2h+k<s$。这要求 $r>2k$，特别 $r>k$。展开 $R$ 本身到二阶；使用
$$
\partial_\Theta^2R
=\frac{289\mathcal E^2R-17\mathcal ER}{\Theta^2},
$$
得到
$$
R(\psi)\equiv
-\frac{w^hu}{e}R_1+
\frac{w^{2h}u^2}{2e^2}R_2
\pmod{w^{2h+k+1}}.
$$
$R_0$ 的首个可能项在 $w^s$，严格高于所读行；包含 $R_1$ 的额外二次项至少有 $3h+q$ 阶，三次 Taylor 余项至少有 $3h$ 阶，均高于 $2h+k$。含 $\xi$ 的项从 $2h+r$ 起，因 $r>k$ 也不进入目标阶。两个剩余系数为 $1$ 和 $-3$，故首项为 (13b) 的 $-2$。

当 $2h+k=s$ 时 $R_0$ 的未知尾已经能到达该阶，不能继续使用 (13b)。定理特意保留这个边界。$\square$

这是实际首次修正的必要分支值，未把它叫作已经在整个原修正空间中非零的余核。是否存在同格 $R$ 实现这些非零值，仍须比较 (11) 的真实仿射空间。

它还有准确的提升选择不变性。改变 $\widetilde F$ 或 $\widetilde Q$ 的系数提升，使 $R$ 的约化分别改变一个 $3t^rF^2QB$ 或 $t^rF^3B$；二者均在 $F^2$ 理想中。因此 $R|_F$ 和 $(\mathcal ER)|_F$ 都不变。这不是挑选一个方便的 $\xi$ 所制造的非零值。

具体地，选任一实际 $P^{\rm base}$ 并令
$R^{\rm base}=(P^{\rm base}-t^r\widetilde F^3\widetilde Q)/p$。
真正同格提升必须使
$$
\boxed{
\left[(\mathcal E(R^{\rm base}+W))(t(w),\psi(t(w)))\right]_{\le h+k}
=\frac5a C(0)u(0)^3w^{h+k},\qquad
\bar W\in\overline{\widetilde{\mathcal W}_{D,J}}.}
\tag{13d}
$$
在 $r>2k$ 时，还须同时实现 (13b) 的整个低于等于 $2h+k$ 的分支值。这里的 $W$ 只能取原真实修正列；(13d) 是一个可直接在同一个有限格内计算的明确必要像条件，不能通过换成全部双次数多项式而宣称已解。它尚不是充分提升条件，(6) 的其余行仍保留。

## 5. 真分支的接触界、结式排除及 F 平方保持

对完整计算格可继续用 R456 的两个明确上界
$$
N=17D+36J,\qquad M=\lfloor11D/2\rfloor+4+11J.
$$
记
$$
a_F=\deg_tF,\qquad b_F=\deg_\Theta F,
\quad B_0=b_FM+a_FN,\quad B_1=B_0-2a_Fb_F.
\tag{14}
$$
**定理 2。** 若 (12) 成立，且
$$
\boxed{\min(s,2h+q)>B_0,\qquad h+q>B_1,}
\tag{15}
$$
则 $F^2\mid\bar R$。

**证明。** 令 $\psi(t)$ 为 $F(t,\psi)=0$、$\psi(0)=1$ 的唯一正规分支；$F_\Theta(0,1)$ 为单位给
$\operatorname{ord}(\bar\vartheta-\psi)=h$。式 (12) 和
$$
\partial_\Theta R=\frac{17}{\Theta}\mathcal ER,
\qquad
\partial_\Theta^2R
=\frac{289\mathcal E^2R-17\mathcal ER}{\Theta^2}
$$
给三项真实 Taylor 估计
$$
\boxed{\operatorname{ord}R(t,\psi)\ge\min(s,2h+q).}
\tag{16}
$$
三次和更高项至少有 $3h$ 阶，而 $q<h$，所以它们不降低显示界。对 $\mathcal ER$ 同样展开则得
$$
\boxed{\operatorname{ord}(\mathcal ER)(t,\psi)\ge h+q.}
\tag{17}
$$
这里一阶变化读到的是 $\mathcal E^2R$，它的 $q$ 阶不能省去。

如果 $F\nmid R$，非零结式 $\operatorname{Res}_\Theta(F,R)$ 的次数至多 $B_0$。无分母的 Sylvester Bézout 式代入 $\psi$，由 (16) 使它有严格大于 $B_0$ 的消失阶，矛盾。因此 $R=FR_1$。

在真分支上 $F=0$，所以
$$
(\mathcal ER)(t,\psi)
=(\mathcal EF)(t,\psi)R_1(t,\psi).
$$
第一因子为单位，(17) 使 $R_1(t,\psi)$ 至少有 $h+q$ 阶。$R_1$ 的双次数至多 $(M-a_F,N-b_F)$，故其与 $F$ 的结式次数至多 $B_1$；第二个不等式同样迫 $F\mid R_1$。$\square$

也可以不使用矩形过估 (15)，直接在 **(11) 的实际仿射修正空间** 验证：满足 (12) 的元素都被 $F^2$ 整除。以下定理只使用这个已核定的保因子结论。

### 单一 Kummer 部分中不收十七倍次数

若使用的是整个 $J=0$ 原格，且因子在 $k[t,\mathscr R]$ 中，则不必先把径向次数乘十七。对同一来源乘完整角单位 $d^{C_D}$，准确得到
$$
d^{C_D}\mathcal W_{D,0}\subset
\mathcal O[t,\mathscr R]_{\deg_{\mathscr R}\le D,\,
\deg_t\le M_R},\qquad
\boxed{M_R=f_D+C_D=5D+4-(D\bmod2).}
\tag{18}
$$
证明每一径向系数的次数为
$3A_n+B_n+C_D-C_n+e_{n+1}=f_n+C_D\le f_D+C_D$。
这个操作在物理目标中是乘同一个 $d(t(w))^{C_D}$ 整单位，故所有精度的真实核和 Bockstein 都保持。它不是来源中免费除去 $t$，也不改原公共 $U_0$。

在此完整单部分问题中可以直接用 $\mathcal E=\mathscr R\partial_{\mathscr R}$、实际 $\mathscr R_{\rm phys}=g e_2(a\epsilon)$，并将 (14) 中 $N,M$ 换成 $D,M_R$。定理 1、2 的 Taylor/结式证明不变；所有原 $\Theta$ 次数十七因子由真实坐标消去。混合 $j$ 问题仍须使用整个十七阶扩张，不能把这一单部分改善直接赋给全部修正列。

### 不需要先保持 F 平方的直接次数后果

在 (10) 中，$q=\min(r,k)$ 和 $k=2h+r-s$ 给
$\min(s,2h+q)=\min(s,2h+k)$。结合定理 1，有以下更直接的必要条件。

- 若 $r>2k$，则 $R(\psi)$ 的阶**准确**为 $2h+k$，所以必有 $2h+k\le B_0$；否则一个非零结式不能容纳这个实际分支值。这里不需要 $B_1$ 或预先保持 $F^2$。
- 若 $\min(s,2h+k)>B_0$，则 (16) 先迫 $F\mid R$。此时 $R=FR_1$，(13a) 使 $R_1(\psi)$ 的阶准确为 $h+k$。因此必须有 $h+k\le B_1$；若反向严格大于，已经排除首次提升。

第一条的证明同时使用定理 1 的非零首项：若结式非零，其次数至少为 $2h+k$；若 $F\mid R$，分支值却应为零，也与 (13b) 矛盾。第二条同理。它们是对同一个原 $R$ 的真限制，不把分支值自由补成一个任意多项式。

## 6. 不除 t 次数的两条 carry 单位障碍

**定理 3。** 假定 (7)–(10)，且真实首次修正空间满足上述 $F^2$ 保持条件，例如 (15) 成立。则 $t^rF^3Q$ 不属于 $K_2^{\rm red}(J)$；其相对首 Bockstein 类非零。

**证明。** 若有 (11)，可取整 $H$ 使
$$
P^{(2)}\equiv t^r\widetilde F^3\widetilde Q
+p\widetilde F^2H\pmod{p^2}.
\tag{19}
$$
本式中的 $H$ 完全可以不被 $t^r$ 整除。后面既不消去 $w^r$，也不把 (19) 改成一个未付的全局立方根。

沿 (13) 记 $H_0=H(t(w),\vartheta(w))$，并在剩余域定义
$$
\zeta=\bar H_0+3w^r\bar C\,\bar\xi.
\tag{20}
$$
仍使用同一个 $u,e,C$ 的约化。第二块的首次商，在 $w^{h+k}$ 及以前准确为
$$
\boxed{
\left[w^hu\{2ae\zeta+w^kCu^2\}\right]_{\le h+k}=0.}
\tag{21}
$$
确实，base 的两个贡献分别是
$6aw^{r+h}Cu\xi e$ 与 $w^{3h+r-s}Cu^3$。
修正 $F^2H$ 的 Euler 值是
$2F(\mathcal EF)H+F^2\mathcal EH$。
后一个真实项从 $w^{2h}$ 起；因为 $k<h$，它在 (21) 所读的最后一行之后，故此时才能排除。

第三块首次商，在 $w^k$ 及以前准确为
$$
\boxed{\left[ae\{ae\zeta+3w^kCu^2\}\right]_{\le k}=0.}
\tag{22}
$$
这里 base 的贡献为 $3a^2w^rC\xi e^2$ 和
$3aw^kCu^2e$；修正的贡献为 $a^2e^2H_0$。
$\mathcal E^2(F^2H)$ 中含 $F$ 的其余项均从 $w^h$ 起，高于第 $k$ 行。base 中含 $\mathcal EQ$ 的进位也从 $w^{h+k}$ 起。未省掉任何能够到达所读行的项。

由 (10)，(21) 的第 $h+k$ 行确实属于完整第二块，(22) 的第 $k$ 行确实属于完整第三块。整单位 $u,e,a$ 只在所示有限低轴内消去。两个条件变为
$$
2ae\zeta+w^kCu^2=0\pmod{w^{k+1}},
$$
$$
ae\zeta+3w^kCu^2=0\pmod{w^{k+1}}.
$$
第一式减去第二式的两倍，给
$$
-5w^kCu^2=0\pmod{w^{k+1}},
$$
其第 $k$ 系数是原单位 $-5C(0)u(0)^2$，矛盾。$\square$

系数五来自同一个立方的完整 Gaussian 与 carry 组合；它不要求两条中央零，也不要求 $a$ 是自由参数。式 (21)–(22) 从未除掉 $t^r$ 的两条跨界带。

### 精确贴边情形

若 $r+2h=s$，则 $k=0$。只要 $h<s$、$\ell\le r+h$，(10) 自动成立。第一块还要求
$\operatorname{ord}H_0\ge s-2h=r$；因此此时第二块的首 carry 已不能由 $F^2H$ 抵消。这也直接恢复同一个单位障碍，而不需要假设 $t^r\mid H$。

若 $h=\lceil(s-r)/2\rceil\ge2$ 是给定角含量下最小三次接触，且首核第三条件 $\ell\le r+h$ 成立，则
$k=0$ 或 $1$。在保因子条件已付时：

- $s-r$ 为偶数时，所有 $\ell\ge1$ 都在 (10) 的可读范围内。
- $s-r$ 为奇数时，$\ell\ge2$ 被排除；$\ell=1$ 的真实末块读不到第一个 $w$ 系数，本证明留下该边界。

上述还默认 $k<s-h$，在当前 $s>13$ 及 $r\ge1,h\ge2$ 的最小接触范围自动成立。一般情形继续使用 (10)，不将截断外的行算入。

## 7. 实际可用范围与原第二余核

与 R456 已纠正的空范围不同，(7) 的真实角含量被保留，(2)、(5) 明确说明这种因子形状能够出现于原格。但这不等于已经找到一个满足所有高接触、同格首核和保因子条件的具体候选。特别：

1. $h$ 必须由同一个实际 $g,t$ 读取，不能按需要选一个形式分支。
2. 若使用 (15)，必须代入真实 $N,M,a_F,b_F$。由于 $N\ge3b_F$、$M\ge r+3a_F$，有 $B_0\ge6a_Fb_F+rb_F$；它可能只涵盖异常高接触。
3. 若不用 (15)，应在 (11) 的原仿射空间中核 $F^2$ 保持；只在一个较小的试验修正空间中成立不够。

这正是下一次实际比较应支付的条件。当前没有把来源饱和 $f_D<p$、显示维数或通常 Padé 接触当成它们的替代物。

原矩阵仍为
$$
M^{\rm orig}=c_*U_0m_{13}J.
$$
本篇的非零 $\beta_J$ 排除的是相对第二核。由 R449，若该首提升落进两条十三行 carry 的真实像，原 $K_2^{\rm red}(M)$ 仍可能存在；其区别继续由 $\ker(\pi\beta_J)$ 和
$G_2=C_2(J)/\overline H$ 读取。全部 $P_{134}/U_0$、十三个初始自由行及两条完整 carry 没有改变。

两原中央条件也仍是同一个 $S,T=VT_0$ 的三个完整权及第三位。它们没有被赋给 $F,Q$、各角层、计算来源或其立方。本篇没有证明两中央失败会构造一个满足本判据的首核，更没有由此声称无穷多个好素数。

## 依赖与复算

R453 的实际计算格和一次整返回；R456 的饱和加强、已更正的角层边界和完整三块；R449 的相对/原 carry 精确序列。脚本 `scripts/check-r459-angular-cubic-carry.py` 直接在 $w^s=p\epsilon$ 中先作完整乘法再截断，保 $pF^2H$ 的全部 Euler 项，核 (21)–(22) 的单位五和最小接触边界；不扫描目标素数。
