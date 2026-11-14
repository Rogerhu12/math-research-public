# R278 — 原强迫的完整中央投影、两条耦合 carry 与双极的实际去向

日期：2026-11-13。**状态：R273 强迫所生四个实际正中央来源的原 Gaussian 范数、R62 中央 Stokes 判据、R182 全深系数判据、两条 Frobenius carry、全变量 Mellin 转置及有理二阶强迫均已证明。原三曲线的中央零尚未传给这些新来源。**

主结论是：R273 的 $337/20$ 经真实导数与原 $1/10$ 几何 carry 接在同一条链上；它不是新增的独立非齐次方向。真正带 $q=4$ 单位双极的正中央来源，第一负层在完整二阶聚合后全部消失。以下给它们的准确中央函数，而不是仅比较裸连接或有限矩阵。

## 1. 固定原 frame 与四个实际来源

取惰性素数 $p=4r-1>67$，置
$$
d=p+1=4r,\quad w=z^4,\quad c=68c_0,\quad
v_p(c)=-1,\quad \alpha=pc\in\mathbb Z_p^\times,
$$
$$
\rho=p^{-1/(2p)},\quad R=\frac{p^2-1}{4}=r(p-1).
\tag{1}
$$
沿用 R272/R273 的实际 $q,U$，并区别
$$
F_{\rm rad}(q)=a_8(q)e^{Z(q)},\quad Z=\log\vartheta^{68},
\qquad \mathcal F=S_8^{17}=\vartheta^{68}t^{17},
$$
$$
s=q-q^2/4,\quad t=1-q/2,\quad
\nu=(1-q/4)^{1/4},\quad h=z/q^{1/4},\quad w=qh^4.
\tag{2}
$$
这里 $\nu,h$ 取原点常数为一的真实分支。准确有
$$
h+4qh'=\nu^{-3},\qquad h-\nu=q/10+O(q^2).
\tag{3}
$$
令
$$
T=\log F_{\rm rad}-L_0-a_0H/p,\quad
L_0=[\log F_{\rm rad}]_{<r},\quad H=q^rh_+,
$$
$$
Y=q^{1/4}U=q^{-p/4}T.
\tag{4}
$$
R273 的 $Y$ 为 $i$ 型，不能直接当作原正中央来源。最短的两个正型聚合是
$$
\boxed{\mathscr B_p=\mathcal Fz^3Y,\qquad
\mathscr C_p=\mathcal Fz^4Y'.}
\tag{5}
$$
再用 R273 的真正算子 $\mathcal A=f+g\partial_z$、$\mathcal K$，定义
$$
\boxed{\mathscr D_p=\mathcal Fz^3\mathcal AY,\qquad
\mathscr E_p=\mathcal Fz^5\mathcal K\mathcal AY.}
\tag{6}
$$
这四个符号不代表旧曲线 $E_{34}$ 的来源 $B$。它们都是现在完整指定的原 theta frame 上的实际函数；$Y$ 的四次覆盖、移动对数和所有 $p$ 修正均保留。

## 2. 全 Gauss 范数与原中央判据

**定理 1。** 四个 (5)--(6) 的来源都从 $z^4$ 或更高阶起，并满足
$$
\boxed{\|e^{-cz^d}\mathscr S_p\|_\rho\le\rho^4,
\qquad \mathscr S=\mathscr B,\mathscr C,\mathscr D,\mathscr E.}
\tag{7}
$$
特别，它们各自的完整中央函数
$$
J_{\mathscr S}(u)=\sum_{m\ge0}c^{-m}
[w^{rm}]\widehat{\mathscr S}_p\,(u)_{\underline m},\quad
\widehat{\mathscr S}_p=e^{-cw^r}\mathscr S_p
\tag{8}
$$
收敛，质量为零，并且
$$
J_{\mathscr S}(u)\in pu\mathbb Z_p+p^2u^2\mathbb Z_p\langle u\rangle.
\tag{9}
$$

**证明。** 先付完整 $U$，不只使用其低次整窗口。对
$$
z_n=[q^n]Z=\frac{34}{n4^n}\frac{(1/2)_n}{(3/4)_n},
$$
当 $n<(p^2+1)/4$ 时，两组 Pochhammer 仅含一次 $p$ 的计数，准确有
$$
v_p(z_n)=-v_p(n)
-\mathbf1_{\{r\le n\bmod p<2r\}}
\tag{10}
$$
（若固定分子再增加赋值，只会加强下界）。$n\bmod p=0$ 与显示坏区间不相交，所以这一范围的赋值至少 $-1$。原 $a_0H/p$ 已准确消去第一次 $r\le n<2r$ 的全部负层。固定 $\log a_8$ 的系数赋值至少 $-v_p(n)$。因而 $U$ 的第一次非整系数在 $q^{3r-1}$，之后到此范围末端的系数赋值都至少 $-1$。

对更大 $n$，令 $m=\lceil\log_p(4n)\rceil$。每一 $p^j$ 级的两个 Pochhammer 计数之差至少 $-1$，故
$v_p(z_n)\ge-2m$；固定角对数的界更强。若 $n\ge(p^2+1)/4$，则 $m\ge3$，并且
$$
\frac{2(n-r)}p>
\frac{p^{m-2}}2-\frac12-\frac1{2p}>2m.
$$
在 $q$ 半径 $\rho^4=p^{-2/p}$ 上，这些高项严格衰减。此前第一次坏项也满足
$-1+2(3r-1)/p>0$。因此
$$
\boxed{\|U\|_{\rho^4}\le1.}
\tag{11}
$$

R215 的真实几何给 $\|u\|_\rho=\rho$、$\|q\|_\rho=\rho^4$，以及 $\nu,h$ 和其逆的范数一。R245 给原 $\widehat{\mathcal F}$ 及其逆范数一。故 $\|Y\|_\rho\le\rho$。原有理系数满足
$\|f\|_\rho\le1$、$\|g\|_\rho\le\rho$；R273 的 $\mathcal B=b_0+g\partial_z$ 也有 $\|b_0\|_\rho\le1$。用真实恒等式 $\mathcal K\mathcal A=\mathcal B\partial_z^2$ 和闭盘微分界
$\|\partial_z^jV\|_\rho\le\rho^{-j}\|V\|_\rho$，即得四个 (7)。其中 $\mathcal AY$ 在原点从 $z^5$ 起，因为 $\mathcal Az$ 从 $z^{69}$ 起；故 (6) 也全纯且质量为零。

由 (7)，第 $m$ 个下降阶乘系数赋值至少
$$
m-\frac{dm-4}{2p}=\frac{m(p-1)}{2p}+\frac2p.
\tag{12}
$$
$m=1$ 时至少一；$m\ge2$ 时至少二，且随 $m$ 趋于无穷。下降阶乘的系数都是整数，证明 (8)--(9)。$\square$

现在可与 R62/R182 **逐个准确比较**。令
$$
\mathscr H_{\mathscr S}(z)=\int_0^z\mathscr S_p(\zeta)\frac{d\zeta}{\zeta},
\qquad K_{\mathscr S}=e^{-cz^d}\mathscr H_{\mathscr S},
$$
并令 $P_0$ 为原加法参数 $z$ 的次数模 $d$ 中央投影。R62 的完整逐余类递推只使用 (7)、质量零及 $v_p(c)=-1$，因此直接给
$$
\boxed{J_{\mathscr S}'(0)=0
\iff P_0K_{\mathscr S}\in\mathbb Q_p\langle z/\rho\rangle
\iff\|P_0K_{\mathscr S}\|_\rho\le\rho^{p+3}.}
\tag{13}
$$
没有将非中央块的消失性附加进去。

对所有 $n\ge0$，置
$$
N_n=rp^n,\quad e_n=\frac{p^{n+1}-1}{p-1},\quad
\epsilon_{p,n}=\frac{p^{e_n}c^{p^n}}{(p^n)!}\in\mathbb Z_p^\times.
$$
原 Gaussian 插值准确给
$$
p^{e_n}[w^{N_n}]\mathscr S_p
=\epsilon_{p,n}J_{\mathscr S}(p^n).
$$
由 (9)，
$$
\boxed{J_{\mathscr S}'(0)=0
\iff p^{e_n}[w^{N_n}]\mathscr S_p\in p^{2n+2}\mathbb Z_p
\quad\text{对全部 }n\ge0.}
\tag{14}
$$
所以这些新行确实进入与 R182 相同的完整深度判据，未以一个有限权代替中心。反向证明是除以 $p^n$ 后令 $n\to\infty$；正向则直接用 (9)。

## 3. 第一负层的两个真正 Frobenius 坐标

以下都在已经支付的第一带内约化；足够覆盖本篇用到的 $w$ 次数 $<7r-1$。R199/R215 给原 $\widehat{\mathcal F}$ 在 $w$ 次数 $\le R-1$ 的整性：也可将 R199 的原 $\widehat A=\widehat\vartheta^{68}P(s)$ 除以实际 $P(s)=w\cdot O[[w]]^\times$，再乘 $t^{17}$ 得到。所用两 Gaussian 的差整，不能删除原 $c$。

因此
$$
E_p(w)=e^{-cw^r}F_{\rm rad}(q(w))
\in1+w\mathbb Z_p[[w]]\pmod{w^R}.
$$
令
$$
\Lambda(w)=[\log F_{\rm rad}(q(w))]_{<r}.
$$
对任何整单位 $E$，当窗口小于 $p^2$ 时，展开 $p\log E$ 后只有对数展开次数为 $p$ 的倍数的项可留下。因此在当前第一带
$$
p\log E_p(w)\equiv\Lambda(w)^p\pmod p.
$$
这是同一原单位的对数 Frobenius 恒等式，不是将 Mellin 当作乘法。利用 $a_0\equiv\alpha\pmod p$、$L_0(q(w))$ 整，得到
$$
\boxed{pT\equiv\alpha(w^r-H(q))+\Lambda(w)^p\pmod p.}
\tag{15}
$$
乘回真实四次因子，准确为
$$
\boxed{pY\equiv
\alpha\{zh(q)^p-q^{1/4}h_+(q)\}
+\{q^{-1/4}\Lambda(w)\}^p\pmod p.}
\tag{16}
$$
最后一个大括号从 $z^3$ 起，没有原点极。这里的约化是在原形式分支的已付有限窗口中，未宣称全部无穷级数的 $pY$ 整。

由 R252 的 $h_++4qh_+'\equiv\nu^{4r-4}$ 和真实 $q'=4q^{3/4}\nu^3$，有
$$
\partial_z(q^{1/4}h_+)\equiv\nu^p.
$$
所以
$$
\boxed{\partial_z(pY)\equiv\alpha(h-\nu)^p,
\qquad \partial_z^2(pY)\equiv0\pmod p.}
\tag{17}
$$
这是原 $z$ 参数中的准确负层，而不是在 $q$ 中误用普通导数。

因为 $Y(iz)=iY(z)$，一个被 $\partial_z^2$ 消去的形式级数，其可能指数同时满足
$m\equiv0,1\pmod p$ 和 $m\equiv1\pmod4$。原低整窗口又排除了 $z$ 项。于是到次数 $7p$ 之前只可能剩 $z^{3p}$ 和 $z^{4p+1}$。
R273 给第一个系数，而 (3)、(17) 给第二个：
$$
\boxed{pY\equiv
Kz^{3p}+\frac\alpha{10}z^{4p+1}\pmod{p,z^{7p}},
\qquad K=337/20.}
\tag{18}
$$

两个常数的来源也能精确核齐。令
$\kappa=\binom{2r-2}{r-1}/4^{r-1}$，则 $\alpha\equiv68\kappa$。
原正规解 (4) 的第 $3r-1$ 项满足
$$
[q^{3r-1}]h\equiv\frac1{6\kappa}\pmod p.
\tag{19}
$$
证明：该 Pochhammer 分子唯一坏项是 $p/4$，分母 $4(3r-1)+1=3p$；去掉后用 Wilson 配对
$(r-1)!(3r-1)!\equiv(-1)^r$、$((2r-1)!)^2\equiv1$，得到
$\kappa[q^{3r-1}]h\equiv-1/(12(2r-1))=1/6$。
又 $[w]\Lambda=331/60$，所以
$$
\boxed{K=\frac{34}3+\frac{331}{60}=\frac{337}{20}.}
\tag{20}
$$
第一项来自旧 theta 首 carry 与原几何尾，第二项来自原径向初值。$\alpha/10$ 则正是同一 $h-\nu$ 的首项。这里没有增加一份独立的未知对数或常数。

## 4. 四个原 Gaussian 行的准确负层

记 $b=g/z$，并令所有带帽来源保留同一个 $e^{-cw^r}$。由 (5)、(6)、(18)，在 $w$ 次数 $<7r-1$ 内，
$$
\boxed{\begin{aligned}
p\widehat{\mathscr B}_p
&\equiv\widehat{\mathcal F}
 (K w^{3r}+\alpha w^{4r}/10),\\
p\widehat{\mathscr C}_p
&\equiv\widehat{\mathcal F}\,\alpha w^{4r}/10,\\
p\widehat{\mathscr D}_p
&\equiv\widehat{\mathcal F}
 \{Kf w^{3r}+\alpha(f+b)w^{4r}/10\},\\
p\widehat{\mathscr E}_p&\equiv0
\qquad\pmod p.
\end{aligned}}
\tag{21}
$$
特别第四行是整个实际负层消失，不是挑掉一个主系数。它由
$\mathcal K\mathcal A=\mathcal B\partial_z^2$ 和 (17) 得到。
固定有理算子在此原点窗口整，乘回 $\widehat{\mathcal F}$ 不改变结论。

第二个水平方向还保留 R273 的真实高阶接触：
$$
\boxed{f+b=\frac{w^{17}}{69a_*h_0}+O(w^{18}).}
\tag{22}
$$
所以 (21) 第三行里的第二个 Frobenius 方向从 $w^{4r+17}$ 才出现，不能按表面的一阶算子漏计这十七阶。

式 (21) 并不表示 $\widehat{\mathscr E}_p=0\pmod p$。其系数只是整；将 $pY$ 的导数除回 $p$ 会留下真实整 carry。例如在原点主部近似中
$$
\mathcal K\mathcal A(z^m)
=h_0(1-m)m(m-69)z^{m-2}+O(z^{m+2}).
$$
$m=3p$、$4p+1$ 两个原负项分别留下 $-207h_0K$、
$272h_0\alpha/10$ 的整贡献，还须加全部低系数和 theta 卷积。它们不是第四行的两个独立中央值。

### 4.1 完整 Stokes 的前两次非齐次聚合

写
$$
b_j=[w^{jr}]\widehat{\mathscr B}_p,\quad
c_j=[w^{jr}]\widehat{\mathscr C}_p,\quad
e_j=[w^{jr}]\widehat{\mathscr E}_p.
$$
由 (21)，$b_1,b_2\in O$、$pb_3\equiv K$；
$c_1,c_2,c_3\in O$、$pc_4\equiv\alpha/10$；所有当前 $e_j$ 都整。
结合 (12) 的完整尾界及
$\partial_u(u)_{\underline m}|_0=(-1)^{m-1}(m-1)!$，得
$$
\boxed{J_{\mathscr B}'(0)\equiv
\frac p\alpha b_1-\frac{p^2}{\alpha^2}b_2
+\frac{2p^2}{\alpha^3}K\pmod{p^3},}
\tag{23}
$$
$$
\boxed{J_{\mathscr C}'(0)\equiv
\frac p\alpha c_1-\frac{p^2}{\alpha^2}c_2
+\frac{2p^3}{\alpha^3}c_3
-\frac{3p^3}{5\alpha^3}\pmod{p^4},}
\tag{24}
$$
$$
\boxed{J_{\mathscr E}'(0)\equiv
\frac p\alpha e_1-\frac{p^2}{\alpha^2}e_2
+\frac{2p^3}{\alpha^3}e_3\pmod{p^4}.}
\tag{25}
$$
这里 (24) 的 $1/10$ 仍是原第四权几何项，已通过整个 Gaussian 聚合回来。对尾的说明是：$m=5,6$ 时 (21) 给至多一层分母，归一后至少 $p^4$；$m\ge7$ 时 (12) 本身已至少四。对 (23) 相同论证只需模 $p^3$。

因此若 **这条新行** $J_{\mathscr B}'(0)$ 为零，就须先有 $b_1\in pO$，再有
$$
\boxed{\alpha^2(b_1/p)-\alpha b_2+337/10=0\pmod p.}
\tag{26}
$$
不能把它直接加入原三零的条件：那还需要实际来源关系。式 (25) 则明确显示，单位双极本身没有在真实正中央聚合中留下一个可单独读取的强迫单位。

## 5. 不漏质量和负移权的全 Mellin 关系

令
$$
\mathcal E=z\partial_z,\quad
W_0=z\mathcal F'/\mathcal F-dcz^d,\quad t_M=du,
$$
$$
a_K=\frac{68xy}{U-1},\quad b_K=\frac{1088x}{U-1},\quad
a_z=za_K,\quad b_z=z^2b_K.
$$
由定义，实际函数准确满足
$$
\mathscr C=(\mathcal E-z\mathcal F'/\mathcal F-3)\mathscr B,
\quad \mathscr D=f\mathscr B+b\mathscr C,
$$
$$
\mathscr E=
\{(\mathcal E-z\mathcal F'/\mathcal F-4)
  (\mathcal E-z\mathcal F'/\mathcal F-3)
 +a_z(\mathcal E-z\mathcal F'/\mathcal F-3)+b_z\}\mathscr D.
\tag{27}
$$
所以完整全 $u$ 关系为
$$
\boxed{J_{\mathscr C}(u)=(du-3)J_{\mathscr B}(u)
-J_{W_0\mathscr B}(u)-duJ_{\mathscr B}(u-1),}
\tag{28}
$$
$$
\boxed{\begin{aligned}
J_{\mathscr D}(u)
={}&J_{(f-3b-\mathcal Eb-bW_0)\mathscr B}(u)\\
&+du\{J_{b\mathscr B}(u)-J_{b\mathscr B}(u-1)\}.
\end{aligned}}
\tag{29}
$$
这些是乘回原 theta 权后的公式，没有把 $J$ 当成乘法。

为写第三个全式，置
$$
f_0=J_{\mathscr D},\quad f_1=J_{W_0\mathscr D},\quad
f_2=J_{(W_0^2+\mathcal EW_0)\mathscr D},
$$
$$
g_0=J_{a_z\mathscr D},\quad
g_1=J_{(\mathcal Ea_z+a_zW_0)\mathscr D},\quad
k_0=J_{b_z\mathscr D}.
$$
全部函数保留原变量，则
$$
\boxed{\begin{aligned}
J_{\mathscr E}(u)={}&(t_M-4)(t_M-3)f_0(u)
 -(2t_M-7)f_1(u)+f_2(u)\\
&+(t_M-3)g_0(u)-g_1(u)+k_0(u)\\
&+du\{(d-2t_M+7)f_0(u-1)+2f_1(u-1)-g_0(u-1)\}\\
&+d^2u(u-1)f_0(u-2).
\end{aligned}}
\tag{30}
$$
这从 R273 的完整有乘子二阶式取除阶 $j=-3$ 得到；也可直接将 (27) 正规排序。若将 (29) 代入，必须同时保留最远 $u-3$ 的项，正是 R269 三阶结构。

本篇这些来源及乘子行的质量确实为零，不是预设原点值为零的抽象泛函。例如 (28) 的中央导数准确是
$$
J_{\mathscr C}'(0)=-3J_{\mathscr B}'(0)
-J_{W_0\mathscr B}'(0)-dJ_{\mathscr B}(-1).
\tag{31}
$$
(30) 的导数还保留
$$
d\{(d+7)f_0(-1)+2f_1(-1)-g_0(-1)\}-d^2f_0(-2)
$$
以及 $12f_0'(0)+7f_1'(0)+f_2'(0)-3g_0'(0)-g_1'(0)+k_0'(0)$。
所以既不能由 $J_{\mathscr C}'=0$ 删除 $J_{\mathscr B}(-1)$，也不能从 $\mathcal K\mathcal A$ 的齐次互逆删掉这些伴随行。

## 6. 全体原中央系数与真正有理二阶强迫

本节把 (14) 的每个 $n$ 都写成真实系数，不只给一个有限窗口。
由 $w=qh^4$ 和 (3)，对任意原 $q$ 函数 $G$，
$$
[w^N]G(q(w))=[q^N]G(q)h^{-4N-1}\nu^{-3}.
\tag{32}
$$
这是形式留数换元，全部 Lagrange 分母已含在真实 $h$ 中。
于是对所有 $N\ge1$，
$$
\boxed{[w^N]\mathscr B_p
=[q^{N-1}]e^Zt^{17}U h^{2-4N}\nu^{-3},}
\tag{33}
$$
$$
\boxed{[w^N]\mathscr C_p
=[q^{N-1}]e^Zt^{17}(U+4qU')h^{3-4N}.}
\tag{34}
$$
这两式的原点阶、theta 次数和完整 $U$ 都没有改变。

令 $\widetilde P(s)=s^8P_8(1/s)$、$\widetilde A(s)=s^8A_8(1/s)$，
$a_*$ 仍为 R264/R273 的固定周期系数，并定义
$$
\mathcal V_p=t\widetilde P\,U
-\frac{1-q/4}{a_*}\widetilde A\,(U+4qU').
\tag{35}
$$
则
$$
\boxed{[w^N]\mathscr D_p
=[q^{N-1}]e^Z\mathcal V_p h^{2-4N}\nu^{-3}.}
\tag{36}
$$
最后置 $V=\mathscr LU$，并令 $\partial_s\widetilde A$ 在下式按 $s=q-q^2/4$ 代入：
$$
\begin{aligned}
\mathcal W_p={}&\{t(a_*\widetilde P+66\widetilde A
-8s\partial_s\widetilde A)+(5q/4-3)\widetilde A\}\,V\\
&-q(4-q)\widetilde A\,V'.
\end{aligned}
\tag{37}
$$
直接使用 $Y''=4q^{3/4}\nu^2V$ 和 R273 的 $\mathcal B$，得
$$
\boxed{[w^N]\mathscr E_p
=\frac4{a_*}[q^{N-2}]e^Z\mathcal W_p h^{4-4N}\nu^{-1}.}
\tag{38}
$$
在 (33)--(38) 取 $N=rp^n$，就是 (14) 的全部原系数；没有将未来中央行免费移回低前缀。

这里 $V$ 必须使用 R272 (14) 的全强迫和特征零 $p$ 修正。
一个更直接的未共轭检查是
$$
\boxed{Z_{zz}=68/x,\qquad
(\log F_{\rm rad})_{zz}=68/x+(\log a_8)_{zz}.}
\tag{39}
$$
前者由 $Z$ 的原方程和 $q'=4u^3$ 逐项得到。因此令 $\ell=\log q$，
$$
T''=\frac{68}x+(\log a_8)''-L_0''-\frac{a_0}pH'',
$$
$$
\boxed{Y''=q^{-p/4}
\{T''-\tfrac p2\ell'T'
 +(\tfrac{p^2}{16}(\ell')^2-\tfrac p4\ell'')T\}.}
\tag{40}
$$
第一行完全有理于原固定覆盖及明确的 $p$ 依赖多项式。第二行的 $pT,pT'$ 在新负层并不消失，正是 (17)--(24) 支付的项；不能仅凭它们前面有 $p$ 就在约化时丢掉。

在 $q=4$，$\mathcal K\mathcal AY$ 仍有 R273 的单位双极。这与 (21) 最后一行相容：一个在另一分支的真极，既不等于原形式盘上的第一负层，也不等于 (13) 的中央 Euler 原函数 Stokes 常数。式 (38)、(40) 给出了实际比较所需的同一来源。

## 7. 原三曲线尚未支付的准确一步

原三零控制的是 R182/R247/R269 中 $S_A,S_B,S_H$ 的完整中央行；(13)--(14) 证明本篇四行属于同一类可检验中央对象，却没有证明它们是那三行的常数线性组合。

当前差异已经具体化：必须把 (33)--(40) 中的完整 $U,U'$、真实 $h$ 权、固定 $a_8$ 零点处极补偿及 (28)--(30) 的负移权，沿实际 theta/Hecke 图送回原三来源。单用有理 $T''$ 的固定极或有限块可逆性不会完成这一步。若某条实际图关系确实给 $J_{\mathscr B}'=0$，则 (26) 的非齐次下一位立即可用；若给 $J_{\mathscr E}'=0$，它须遵守 (25) 的完整整聚合，不能另加一个由双极想象出的单位。

因此本篇已经支付了单位双极与原 $P_0$、全 $n$ 深度判据之间的真实接口，也明确支付了 $337/20$ 回到原 $1/10$ 的全部 Gaussian/导数成本。下一步沿实际普通 $T_p$ 的全变量转置比较这些具体行，不能只使用轨道维数。

## 精确证书与依赖

[脚本](../scripts/check-actual-forcing-central-projection-and-carries.py) 与
[输出](../scripts/check-actual-forcing-central-projection-and-carries.json) 给出实际反序多项式、四个原来源、全中央系数式、符号共轭、Mellin 正规排序和两 carry 的准确系数。所有计算都是固定有理恒等式或符号参数恒等式，没有目标素数扫描。

依赖 R62 的全 Stokes 递推、R182 的原插值、R199/R215 的同一第一带整性和全深参数、R245 的真实 $S_8$ frame 范数、R247 的完整尾与几何 carry、R264/R268 的原连接，以及 R272/R273 的实际强迫和四个算子。
