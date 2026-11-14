# R610 — 原整目标的第二 Euler 导子与两算术来源的真实除 p 行

日期：2026-11-14。**状态：已证明。**

本篇在 R607 已证明的同一个无扭有限目标内，先除以 $p$，再约化，构造原 Euler 算子的下一整商。约化后的下一位确实是整个实际目标环的导子；未经修正的 $(D^p-D)/p$ 则有完整的 Witt 乘法交叉项，不能直接当导子。

同一操作还给出七个原 Euler 来源的真实 forcing 行，以及原 $S/T$ 的六个低权整除商。后者不是新增来源，也不从中央失败获得整条零行：其常数项读原首中央系数，而高 $\upsilon$ 项始终含单位。全部原前缀和完整中央的边界保持。

## 1. 同一个目标、物理行和原 Euler 算子

保 R607 的原规范
\[
p=6s-1>71,\qquad w=z^6,\qquad
t_n=\left\lfloor\frac{6n}{p}\right\rfloor,\qquad
e_n=p^{-t_n}w^n,\quad 0\le n<ps,
\]
以及
\[
\mathcal C_p=\bigoplus_{n<ps}\mathcal Oe_n
=\mathcal O[w,\epsilon,\upsilon]/
(w^s-p\epsilon,\epsilon^6-w\upsilon,
 w^{s-1}\epsilon^5-p\upsilon,\upsilon^s).
\tag{1}
\]
这是同一原九来源评价的实际整数目标，不另换格。

令
\[
D=6w\partial_w=z\partial_z.
\tag{2}
\]
它在 (1) 上是整导子，$De_n=6ne_n$。
对每个实际基向量唯一写
\[
n=jp+ts+r,\quad 0\le j<s,\quad0\le t\le5,\quad0\le r<s,
\quad(t,r)\ne(5,s-1).
\]
则
\[
q_n=6r+t\in\{0,\ldots,p-1\},\qquad
6n=q_n+p(6j+t),\qquad t_n=6j+t.
\tag{3}
\]

以 $\Pi_q$ 表示对同一物理基中 $q_n=q$ 的整线性投影。
所有 $\Pi_q$ 都保真实物理前缀；它们只是目标行操作，
未被加入原固定来源多项式格。
定义实际整算子
\[
\boxed{
\Xi=\sum_{q=0}^{p-1}\frac{D-q}{p}\Pi_q,\qquad
\Xi e_n=t_ne_n.
}
\tag{4}
\]
每项的除法在原无扭 $\mathcal C_p$ 内准确成立。
若 $q=6r+t$，在整个权块上
\[
\Xi\bigl(w^r\epsilon^t f(\upsilon)\bigr)
=w^r\epsilon^t(6\upsilon\partial_\upsilon+t)f(\upsilon).
\tag{5}
\]
式 (5) 是同一实际整算子的公式，不是先在特征 $p$ 形式引入导数。

## 2. 下一位约化是整个目标环的导子

对 $n+m<ps$，保 R607 的真实乘法
\[
e_ne_m=p^{c(n,m)}e_{n+m},\qquad
c(n,m)=t_{n+m}-t_n-t_m\in\{0,1\}.
\]
由 (4)，准确有
\[
\boxed{
\Xi(e_ne_m)-(\Xi e_n)e_m-e_n(\Xi e_m)
=c(n,m)p^{c(n,m)}e_{n+m}.
}
\tag{6}
\]
若 $n+m\ge ps$，各项均为零。
(6) 的右端总在 $p\mathcal C_p$；
因此在原约化目标
\[
\overline{\mathcal C}_p
=k[w,\epsilon,\upsilon]/
(w^s,\epsilon^6-w\upsilon,w^{s-1}\epsilon^5,\upsilon^s)
\]
上，$\bar\Xi$ 是真正的导子。其准确值为
\[
\boxed{
\bar\Xi=\epsilon\partial_\epsilon+6\upsilon\partial_\upsilon,
\quad
\bar\Xi(w)=0,\quad\bar\Xi(\epsilon)=\epsilon,\quad
\bar\Xi(\upsilon)=6\upsilon.
}
\tag{7}
\]
特别，$\epsilon^6=w\upsilon$ 的两边导数同为六倍自身；
实际第六次乘法进位没有被遗漏。

原第一 Euler 约化则是
\[
\bar D=6w\partial_w+\epsilon\partial_\epsilon,\qquad
\bar D^p=\bar D .
\tag{8}
\]
两个导子由实际对角算子所得，彼此交换。
它们都保持 $(w)$ 和 $(\upsilon)$，所以在 R607 的真实低权环商
\[
\mathcal Q_p=\overline{\mathcal C}_p/(w)
=k[\epsilon,\upsilon]/(\epsilon^6,\upsilon^s)
\tag{9}
\]
中仍成立。这里不是任意扩充目标后获得的新方向。

## 3. 未修正的 Fermat 商及完整乘法缺陷

另一条无需权块表示的实际整算子是
\[
\mathscr B=\frac{D^p-D}{p}.
\tag{10}
\]
其在 $e_n$ 上的特征值为 $((6n)^p-6n)/p\in\mathbf Z$，
故 (10) 确实保 (1) 的原整格。

对整数 $0\le q<p$ 置
\[
\phi_p(q)=\frac{q^p-q}{p}\pmod p.
\]
由 $6n=q_n+pt_n$ 和
$(q+pt)^p\equiv q^p\pmod{p^2}$，
\[
\boxed{
\overline{\mathscr B}\,e_n
=(\phi_p(q_n)-t_n)e_n .
}
\tag{11}
\]
设 $\Phi_p(T)\in k[T]$ 为在 $q\in\mathbf F_p$ 取值
$\phi_p(q)$ 的次数至多 $p-1$ 的插值多项式，例如
\[
\Phi_p(T)=\sum_{q=0}^{p-1}
\phi_p(q)\bigl(1-(T-q)^{p-1}\bigr).
\]
则 (11) 也准确写为
\[
\boxed{\bar\Xi=\Phi_p(\bar D)-\overline{\mathscr B}.}
\tag{12}
\]
这里插值中的 $q$ 使用固定整数代表 $0,\ldots,p-1$；
不能在除 $p$ 前任意更换提升。

未经 (12) 的有限修正，$\overline{\mathscr B}$ 一般不是导子。
完整 Leibniz 展开给
\[
\boxed{
\overline{\mathscr B}(fg)
-\overline{\mathscr B}(f)g-f\overline{\mathscr B}(g)
=
\sum_{i=1}^{p-1}\frac{(-1)^{i-1}}{i}
(\bar D^if)(\bar D^{p-i}g).
}
\tag{13}
\]
证明是先在原整目标中展开 $D^p(fg)$，再用
$\binom pi/p\equiv(-1)^{i-1}/i\pmod p$。
全部分母 $i$ 都是单位；没有丢弃任一中间交叉项。

特别，对 (9) 中的低权 $h\in\{0,\ldots,5\}$，
\[
\boxed{
\overline{\mathscr B}(\epsilon^hf(\upsilon))
=\epsilon^h\{(\phi_p(h)-h)f-6\upsilon f'\}.
}
\tag{14}
\]
(7)、(12) 与 (13) 是同一个算子的三种实际表示，
而不是新增三个独立的来源约束。

## 4. 七个原 Euler 来源的真实 forcing 除商

保 R586/R607 的原恒等式
\[
(D-h)W_{\ell,h}=A_\ell,\qquad
(\ell,h)=(4,0),(4,1),(1,0),\ldots,(1,4),
\tag{15}
\]
其中
\[
A_\ell=w\exp\!\left(\frac a p w^s\right)G_\ell(w),
\quad a=6pc\in\mathcal O^\times,\quad
G_\ell(w)=\sum g_{\ell,r}w^r.
\]
原低权的完整共振多项式为
\[
\Gamma_{\ell,h}(\upsilon)=
\sum_{j=j_0}^{s-1}
\frac{\bar a^{\,6j+h-1}\bar g_{\ell,s-1-j}}{(6j+h)!}\upsilon^j,
\quad
j_0=\begin{cases}1&h=0,\\0&h>0.\end{cases}
\tag{16}
\]
R607 已证明 $\Pi_h\bar W_{\ell,h}
=\epsilon^h\Gamma_{\ell,h}$。
对 (15) 先取同一个整投影，再使用 (4)，得到整恒等式
\[
\Pi_hA_\ell=p\,\Xi\Pi_hW_{\ell,h}.
\]
所以这里的下一位除法不是选择一个模 $p$ 原像：
\[
\boxed{
\overline{\Pi_hA_\ell/p}
=\epsilon^h(6\upsilon\partial_\upsilon+h)
                 \Gamma_{\ell,h}(\upsilon).
}
\tag{17}
\]
它处在原 $\overline{\mathcal C}_p$ 的整个 $h$ 权块中，
不只是抽象商中的一个候选类。

记 $c_{\ell,p}=\bar g_{\ell,s-1}$。
对于原来源中实际存在的 $h\ge1$，(16) 给
\[
\boxed{
(6\upsilon\partial_\upsilon+h)\Gamma_{\ell,h}
=\bar a\Gamma_{\ell,h-1}
+\mathbf1_{h=1}c_{\ell,p}.
}
\tag{18}
\]
因而 R607 的有限多项式递推现已接回真实整算子 (17)。
$h=0$ 则只取 $6\upsilon\Gamma'_{\ell,0}$，
没有添加 $\Gamma_{\ell,-1}$ 或未付的来源。

## 5. 原 S/T 的六个实际低权除 p 行

令 $X$ 为原 $S$ 或 $T$，保持同一原物理缩放。
写
\[
X=w\exp\!\left(\frac{\gamma_X}{p}w^s\right)G_X(w),
\quad G_X=\sum_{r\ge0}g_{X,r}w^r,\quad g_{X,0}=1,
\tag{19}
\]
其中
\[
\gamma_S=34pc,\qquad\gamma_T=72pc.
\]
这些 $\gamma_X$ 在当前好惰性素数范围内都是单位。
R602 已对这些同一个实际余项证明
\[
r!g_{X,r}\in\mathcal O\quad(r\ge0),
\qquad g_{X,r}\in\mathcal O\quad(r<p).
\tag{20}
\]

**定理。** 对每个 $h=0,\ldots,5$，
\[
\Pi_hX\in p\mathcal C_p,
\]
且实际除商的完整约化为
\[
\boxed{
\overline{\Pi_hX/p}=\epsilon^h\Lambda_{X,h}(\upsilon),\qquad
\Lambda_{X,h}=
\sum_{j=j_0}^{s-1}
\frac{\bar\gamma_X^{\,6j+h-1}\bar g_{X,s-1-j}}
     {(6j+h-1)!}\upsilon^j .
}
\tag{21}
\]
$h=0$ 从 $j_0=1$ 开始，$h>0$ 从 $j_0=0$ 开始。
这里的 $\Lambda$ 是原 $S/T$ 评价的实际整行，
没有把其 Euler 原函数加进原九个全局坐标。

**证明。** 低权 $h$ 的所有真实物理指标恰是
$n=jp+hs$，$0\le j<s$，其归一化指数为 $t_n=6j+h$。
零指标的 $X$ 系数是零；对其余指标置
\[
L_0=6j+h-1,\qquad r_0=s-j-1 .
\]
有 $0\le L_0<p$、$0\le r_0<s$，
并且 $n-1=L_0s+r_0$。因此
\[
p^{t_n-1}[w^n]X
=\sum_{L=0}^{L_0}
p^{L_0-L}\frac{\gamma_X^L}{L!}g_{X,r_0+(L_0-L)s}.
\tag{22}
\]
$L=L_0$ 给 (21) 的显示项，且整。

若 $d=L_0-L\ge1$，令 $r=r_0+ds$。
由于 $r<n<ps<p^2$，(20) 给
\[
v_p(g_{X,r})\ge-\left\lfloor\frac r p\right\rfloor .
\]
又
\[
r\le(d+1)s-1<dp,
\]
故 $d-\lfloor r/p\rfloor\ge1$。
全部 $L!$ 为单位，所以 (22) 的每个其余项都在 $p\mathcal O$。
这同时证明真实整除和完整约化式；
并没有把高系数的可能分母当作零。证毕。

两个端点尤其明确。令
\[
C_X=[w^s]X=g_{X,s-1}\in\mathcal O.
\]
则
\[
\boxed{
\Lambda_{X,0}(0)=0,\qquad
\Lambda_{X,h}(0)
=\frac{\bar\gamma_X^{h-1}}{(h-1)!}\bar C_X
\quad(1\le h\le5).
}
\tag{23}
\]
另一方面，每个 $h=0,\ldots,5$ 的最高项为
\[
\boxed{
[\upsilon^{s-1}]\Lambda_{X,h}
=\frac{\bar\gamma_X^{p+h-6}}{(p+h-6)!}\in k^\times .
}
\tag{24}
\]
所以六个实际除商均非零，包括原首中央系数约化为零时。

## 6. 与原完整中央、真前缀和同预算来源的边界

R602 的完整 Newton 尾给同一原中央导数
\[
j_X/p\equiv C_X/\gamma_X\pmod p .
\tag{25}
\]
因此 $j_X=0$ 迫 $\bar C_X=0$；
(23) 的五个常数项只是这个同一条件的单位倍数。
由 (24)，中央失败不迫 (21) 整条实际除商为零。
R606 的第二完整中央类仍须保 $C_X/p$ 的真实两位除法、
规范余项以及 $H^{-p}$ 的 log 修正；它们没有从 (23) 自动消失。

同样，若两个 $c_{\ell,p}$ 都为零，
R607 的七个低权像都在 $(\upsilon)$ 中。
(7)、(8)、(12) 保持该理想，
故任意组合这些目标 Euler 行操作仍在 $(\upsilon)$ 中。
不能从它们的非零高项抽出一个未经证明的非零常数 forcing。

(4) 与 (10) 都是物理行上的整对角操作，
保持目标中任意原前缀消失。
但是要把操作后的评价重新表示成同一个
$E_{D,9}$ 中的原来源多项式，还需证明实际来源像的稳定性
及相应次数和整性；本篇不假定这个未付步骤。
特别，目标导子的存在不等于加入免费全局坐标，
也不把 $\ker\overline{\widehat M}_{p,D}$ 当作真前缀核。

本篇完成的是：原强化整目标中的下一 Euler 商、
其完整乘法缺陷修正、七来源实际 forcing 行，
以及两原算术来源的全部六条真实低权第一除商。
原完整中央与非空真层之间的算术传播仍保持为开放条件。

## 依赖与验证范围

- [R586](R586-original-euler-resonant-coefficients-and-first-square-window.md) 的原 Euler 恒等式和共振系数，使用时以 [R607](R607-original-integral-target-and-mixed-schur-decomposition.md) 第 3 节的同一规范为准。
- [R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md) 的原全 Hurwitz 余项及完整 Newton 尾。
- [R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md) 的完整第二中央类。
- [R607](R607-original-integral-target-and-mixed-schur-decomposition.md) 的无扭整目标、全部来源像及真前缀。

以上各式由原整基逐项证明，覆盖全部允许的 $p,n,h$，
无新增素数扫描或以有限检查代替一般证明。
主目标尚未完成。
