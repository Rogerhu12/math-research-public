# R755 — 全部原 cube 的 carry 筛及指定值类不变性

日期：2026-11-15。**状态：下述原有限矩阵结论已证明；指定全 forcing 的非零及主目标仍未完成。**

R750 的值留数不能被先前固定前缀中的常数 cube 改变。
本篇把这个范围扩到完整原 $\mathcal W_D$ 中的**所有**
$F^3$-整除来源：先完整读取它们的两条十三行，
再证明凡通过 primitive 相对首核门者，
其原首 Bockstein 的整个值投影为零。
这保原真实来源帽，不要求它们带同一个 $qt^r$。

在没有通过该门的方向中，可能的值改变量也被准确压到最后至多十三行。
若尝试用这些真实 cube 修复指定 $P_B$ 的 carry，
其可解条件是一个明确的、至多十三维的原来源评价；
修复后的值类与修复选择无关，并给出完整系数 $1/6$ 的修正式。
另一方面，另外两个块通常仍非零，包含实际 $\xi$ 和第四 normal 项。
本篇不把值投影不变当成整个余类不变。

## 1. 同一原窗口及整个 cube 来源

保 R750 的全部原数据、整数帽和同源整提升：
$$
p=6s-1>101,\quad f_D<p,\quad
1\le\ell\le r\le13<h,\quad
k=2h+r-s,\quad0\le k<\ell.
$$
置
$$
\boxed{
d_0=r-k=s-2h,\qquad1\le d_0\le13,\qquad
N_0=s-13=2h+d_0-13\le2h.
}
\tag{1}
$$
仍保强窗 $h>\kappa,\ T_M-h>\kappa$，
其中
$$
T_M=s-r-13,\qquad T_J=s-r.
$$
特别 $h>d_0$、$h>\ell$。
原目标和 common 单位为
$$
M=c_*U_0w^{13}J,\quad
\Gamma^+=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2).
\tag{2}
$$
只逆整个真实整单位 $c_*U_0$；保全部 $P_{134}$、
common charge、原 $t=t(w)$ 和两个十三行。
局部量准确为
$$
\eta=\eta_0+p\xi,\qquad
\eta_0=t^hu,\qquad
\zeta_{\rm phys}=\eta+a\epsilon,\qquad
t^s=p\epsilon b_s,\quad b_s=(t/w)^s.
\tag{3}
$$

在 R750 的十九角曲面上，
$$
\operatorname{div}(P^{\rm fact})=3C+E,\qquad
E\ge0,\quad E\sim\mathcal B_D-3C,\quad C\not\subset E.
$$
定义整个原约化 cube 空间
$$
\boxed{
\mathcal C_D
=\{P\in\overline{\mathcal W}_D:F^3\mid d^{C_D}P\}
=d^{-C_D}F^3 H^0(X,\mathcal O_X(E)).
}
\tag{4}
$$
右边使用同一原多项式平凡化。
它一般大于 $kP^{\rm fact}$，也不假设每个元素带 $t^r$。
每条只按原 canonical 自由格及已付整角提升读取；
不借 (4) 新增一个算术中央零。

将一个真实元素写成
$$
P_H=F^3\mathscr H,\qquad
\mathscr H=d^{-C_D}H,\quad
H\in H^0(X,\mathcal O_X(E)).
$$
记其同一曲线值和法向值
$$
H_0=\mathscr H|_C,\qquad H_1=(\mathcal E\mathscr H)|_C,\qquad
e=(\mathcal EF)|_C,\quad f_2=(\mathcal E^2F)|_C.
\tag{5}
$$
$d,e,u,b_s$ 在原点均为单位。
$H_1$ 不由 $H_0$ 的消失阶自动控制。

## 2. 真实 E 来源及其低前缀，不免费指定 H0

R750 的完整 $F$-整除基证明同样适用于 $F^3$。
这里只把所有角阈值中的 $v(F)$ 改成 $3v(F)$。
具体置
$$
\lambda_\alpha=-2-3v_\alpha(F)
\quad(\alpha=0,h_{7,1},h_{7,2}),\quad
\lambda_1=-1-3v_1(F),
$$
$$
\lambda_d=2C_D-3v_d(F),\qquad
\lambda_\infty=-2C_D-8-3v_\infty(F).
$$
对 $0\le i\le D-3b$，令
$$
m_{\alpha,i}=\max\left(0,\left\lceil\frac{i+\lambda_\alpha}{4}\right\rceil\right),
\quad
m_{1,i}=\max\left(0,\left\lceil\frac{i+\lambda_1}{3}\right\rceil\right),
$$
$$
m_{d,i}=\max\left(0,\left\lceil\frac{\lambda_d-i}{2}\right\rceil\right),
\quad
a_i=t^{m_{0,i}}\prod_{\alpha=h_{7,1},h_{7,2}}
(t-\alpha)^{m_{\alpha,i}}
(t-1)^{m_{1,i}}d^{m_{d,i}},
$$
$$
n_i=\left\lfloor\frac{9i-\lambda_\infty}{2}\right\rfloor-\deg a_i.
\tag{6}
$$
则 $H$ 的完整原基准确是
$$
\boxed{Y^i a_i(t)t^j,\qquad0\le j\le n_i.}
\tag{7}
$$
$n_i<0$ 时该组为空。由 Gauss 乘法和原双向角识别，
(7) 保所有真实来源帽及十九角；不只给充分子格。

特别令
$$
\boxed{
r_E=
\min_{\substack{0\le i\le D-3b\\n_i\ge0}}m_{0,i}.
}
\tag{8}
$$
原 $P^{\rm fact}$ 保集合非空。
每条 (7) 在 $P$ 的评价首项都是单位乘 $t^{m_{0,i}+j}$，
因此 $r_E$ 正是 $H_0$ 在这个整个真实空间中的最小可能阶，
并有 $r_E\le r$。

另有无须先计算其余角的界。令 $m=-v_0(F)$。
因 $F(0,Y)$ 非零且在 $Y=1$ 有根，
它必为非恒定多项式，故 $v_0(F)\le-1$。
由 (6) 得
$$
\boxed{
r_E\ge\left\lceil\frac{3m-2}{4}\right\rceil\ge1.
}
\tag{9}
$$
这是真正原零角的限制。
需要完整低评价时，使用 (7) 在同一 $\psi$ 上的值，
不能把 $H_0\bmod t^{d_0}$ 换成任意多项式。

## 3. 全部 cube 的原首核与完整 carry 门

**定理 1。** 在 (1) 的原范围内，准确有
$$
\boxed{\mathcal C_D\subset\ker\bar M.}
\tag{10}
$$
其相对首核部分恰为
$$
\boxed{
\mathcal C_D\cap\ker\bar J
=\{P_H\in\mathcal C_D:\ H_0\in t^{d_0}k[[t]]\}.
}
\tag{11}
$$

**证明。** 沿原支 $F=e\zeta+O(\zeta^2)$。
在 $\zeta=\eta_0+a\epsilon$ 下，
$F^3$ 的普通部分至少为 $t^{3h}$，
第一 Gaussian 部分至少为 $t^{2h}\epsilon$，
第二部分至少为 $t^h\epsilon^2$。
由 $3h,2h\ge N_0$、$h\ge\ell$，
乘完整 $w^{13}$ 后三者全在原约化目标中消失。
这对任意在 $P$ 正则的 $\mathscr H$ 成立，证明 (10)。

相对 $J$ 中，普通部分因 $3h>s=2h+d_0$ 仍消失；
第三部分因 $h>\ell$ 仍消失。
第一 Gaussian 块则准确为
$$
\boxed{
\bar J_1(P_H)=3a e^3t^{2h}u^2H_0
\pmod{t^s}.
}
\tag{12}
$$
其余项从 $3h>s$ 起。
$3,a,e,u$ 均为单位，故 (12) 为零当且仅当
$H_0\in t^{s-2h}=t^{d_0}$，即 (11)。证毕。

因 (12) 的最低位置是 $2h=s-d_0$，
这一相对非零只能处在**第二条十三行的最后 $d_0$ 个位置**。
第一条 carry 带为零。
由 R449，任何 $P_H+pR$ 的 primitive $p^2$ 提升都必须先通过 (11)；
没有某个来源修正可以跳过原外面的 $p$ 行缩放。

若 (8) 的 $r_E\ge d_0$，则整个 $\mathcal C_D$ 已在 $\ker\bar J$。
特别
$$
\boxed{r=1,\ k=0\quad\Longrightarrow\quad
\mathcal C_D\subset\ker\bar J}
\tag{13}
$$
因为此时 $d_0=1$，(9) 自动成立。
这里没有假设原 cube 在整个首核中具有最大前缀。

(10) 只是这个准确原 $M$ 的模 $p$ 结论。
raw $\bar\Gamma$ 中的 $\zeta^3$、相对 $J$ 的 (12)，
以及下一位全部不得由 (10) 删除。

## 4. 完整首 Bockstein 的两余块

对同一个整来源，在原支展开
$$
F^3\mathscr H=C_3\zeta^3+C_4\zeta^4+\cdots,
$$
$$
\boxed{
C_3=e^3H_0,\qquad
C_4=e^3H_1+\frac32e^2 f_2H_0.
}
\tag{14}
$$
以下模 $p$ 系数仍用相同符号；所有整展开只读原实际有限目标。

由 (10)，$M(P_H)/p$ 整。
逆整个 $c_*U_0$ 后，前两块都具有 $w^{13}$：
在它们各自的行 $13,\ldots,s-1$ 除显示的 $w^{13}$，
再换到原 $t$，记为 $\widehat\beta_0,\widehat\beta_1$，
长度均为 $N_0$。
第三块仍用原物理 $w$ 行，不逆 $m_{13}$。

**定理 2。**
$$
\boxed{\widehat\beta_0=0,}
\tag{15}
$$
$$
\boxed{
\widehat\beta_1=
6a C_3\eta_0\xi+
b_s\left(C_3t^{h-d_0}u^3+
C_4t^{2h-d_0}u^4\right)
\pmod{t^{N_0}}.
}
\tag{16}
$$
完整第三块为
$$
\boxed{
\begin{aligned}
\left[(c_*U_0)^{-1}M(P_H)/p\right]^{(2)}
=w^{13}\biggl\{
3a^2C_3\xi
+a b_s\bigl(
3C_3t^{-d_0}u^2+
4C_4t^{h-d_0}u^3
\bigr)
\biggr\}
\pmod{w^{\ell+13}} .
\end{aligned}}
\tag{17}
$$
(17) 中最低 Laurent 阶为 $-d_0\ge-13$，
乘实际 $w^{13}$ 后才是原整坐标。
不把 $w^{13}$ 替换成 $t^{13}$。

**证明。** 普通低块的 native $p\xi$ 项从 $t^{2h}$ 起，
所以 (1) 使它不能进入第一块，得 (15)。
第一 Gaussian 块的 native 部分来自
$a p\xi\,\partial_\zeta^2(F^3\mathscr H)(\eta_0)$；
除一次 $p$ 后，只有 $6aC_3\eta_0\xi$ 位于 $t^{<N_0}$。
其余从 $t^{2h}$ 起。

普通值的一次 carry 则将
$C_3\eta_0^3+C_4\eta_0^4+\cdots$
乘 $b_st^{-s}$，给 (16) 的后两项。
第五次项的阶至少是 $3h-d_0$，
而
$$
3h-d_0-N_0=h-2d_0+13>0,
$$
所以确实不可读。普通值在 carry 前从 $t^{3h}$ 起且 $3h>s$，
这也证明前两块没有被漏掉的最初十三行。

第三块的 native 项来自
$(a^2/2)p\xi\,\partial_\zeta^3(F^3\mathscr H)(\eta_0)$，
除 $p$ 后只有 $3a^2C_3\xi$ 留在长度 $\ell$ 内。
显式第一 Gaussian 的一次 carry 给
$a b_s(3C_3t^{-d_0}u^2+4C_4t^{h-d_0}u^3)$。
再高项从 $2h-d_0>\ell$ 起。
普通值进两次 carry 已带 $p^2$，除 $p$ 后仍为零。

原整数常数与单位的高位没有被另行规范：
$\xi_0$ 保留，$b_s$ 用全部实际所需系数。
以上都在乘原 $w^{13}$ 的同一目标中读取，给 (17)。证毕。

特别，$C_4$ 在 (16) 中可能从 $d_0\ge7$ 开始可见；
在 (17) 中，当 $h-d_0<\ell$ 时也可能可见。
即使 $H_0$ 很深，也不能推出 $H_1$ 同样深。
这些正是需要保留的真实高 normal 项。

若已经通过 (11)，则 (14) 中含 $f_2H_0$ 的部分在两个显示窗口中消失，
但 $e^3H_1$ 一般仍保留。
对原 $P^{\rm fact}$，
$H_0=qt^r|_C$、$H_1=(\mathcal Eq)|_Ct^r$；
(17) 精确还原 R547 的
$3a w^{13}b_s q_0e^3u^2t^k$，其它两个项才由该特定前缀截掉。

## 5. 全部 primitive cube 都不能改变指定值类

使用 R750 的同一原投影
$$
\mathscr V_\eta\beta
=\widehat\beta_0-\eta_0\widehat\beta_1/a
\pmod{t^{N_0}}.
$$
由 (15)、(16) 得准确式
$$
\boxed{
\mathscr V_\eta\beta_M(P_H)
=
-\frac{e^3b_s}{a}\,
t^{2h-d_0}u^4H_0
\pmod{t^{N_0}}.
}
\tag{18}
$$
native 项乘 $\eta_0$ 后从 $2h$ 起，
$C_4$ 项从 $3h-d_0>N_0$ 起，均不可读。

因此即使不加相对首核门，
(18) 也只可能占最后
$$
\boxed{(2d_0-13)_+\le13}
\tag{19}
$$
个值位置。
若 $d_0\le6$，它已恒零。
而通过 (11) 后，其首阶至少 $2h$，故有更强结论：

**定理 3。**
$$
\boxed{
\mathscr V_\eta\beta_M
\bigl(\mathcal C_D\cap\ker\bar J\bigr)=0.
}
\tag{20}
$$

这覆盖所有原 $F^3$-整除来源，不只覆盖 $kP^{\rm fact}$ 或
$q t^r\mathcal H_3$ 内的 cube。

假定原 $P_B$ 已通过 R750 的 primitive carry 门，
即 $P_B\in\ker\bar J$。
则任何仍留在 $\ker\bar J$ 的替换 $P_B\mapsto P_B+P_H$
必须有 $P_H\in\mathcal C_D\cap\ker\bar J$。
由 Bockstein 的线性及 (20)，
其 R750 的整个 $\Omega_B$ 完全不变。
不能用这些更大的合法 cube 自由度消去一个非零的实际值留数。

这不把未通过相对首核门的 cube 也免费商掉；
它们的准确影响是 (18)、(19)，下一节单独处理。

## 6. 全 cube 修复指定 carry 的完整有限条件

若原 $P_B$ 只在 $\ker\bar M$，
允许先选择一个**真实** $P_H\in\mathcal C_D$，
再测试 $P_B+P_H$ 能否进入 $\ker\bar J$。
这是更换初始首核候选，不是将原 $P_B$ 的同一个 $R$ 偷换掉。

仍记
$$
\mathscr B=B_0+2\eta_0B_1,\qquad
\operatorname{ord}\mathscr B\ge T_M.
$$
R750 增补和 (12) 给完整必要且充分的相对首核方程
$$
\boxed{
t^r q_0e\,\mathscr B+
3e^3t^{2h}u^2H_0=0\pmod{t^s}.
}
\tag{21}
$$
普通块和第三块本来都为零，原 $a$ 单位在此同除。

首先，cube 的 (12) 不可能作用于第二条十三行最早的 $13-d_0$ 行。
所以 (21) 必须先有
$$
\boxed{\operatorname{ord}\mathscr B\ge T_J-d_0=2h-r.}
\tag{22}
$$
在此之后，定义实际低目标
$$
\boxed{
v_{\rm repair}
=-\frac{q_0}{3e^2u^2}\,
t^{r-2h}\mathscr B
\pmod{t^{d_0}}.
}
\tag{23}
$$
该式此时才是整 Taylor jet。

**定理 4。** 存在上述真实 cube 修复，当且仅当 (22) 成立，且
$$
\boxed{
v_{\rm repair}\in
\operatorname{im}\left(
H^0(X,\mathcal O_X(E))
\xrightarrow{H\mapsto(d^{-C_D}H)|_\psi}
k[t]/t^{d_0}\right).
}
\tag{24}
$$
(24) 由 (6)、(7) 的全部原列生成，不是一个自由 $d_0$ 维空间。

任意两个修复的差都满足 (11)；
所以修复后的值 forcing 不依赖修复的选择。
更具体地，将 (23) 代入 (18)，精确得到
$$
\boxed{
\begin{aligned}
\mathscr V_\eta\beta_M(P_B+P_H)
=q_0e\left\{
t^r\xi B_0
-\frac{b_s}{2a}t^ku^2B_0
-\frac{b_s}{6a}t^ku^2\mathscr B
\right\}\pmod{t^{N_0}}.
\end{aligned}}
\tag{25}
$$

**证明。** (21) 和单位性给 (22)–(24)。
两个解的 $H_0$ 差为 $t^{d_0}$ 倍，
恰是 (11)，由 (20) 其值改变量为零。

(18) 只读 $H_0$ 到阶 $(2d_0-13)_+-1<d_0$，
所以 (23) 已给足其全部实际输入。
代入后，cube 的值增量为
$$
\frac{q_0e b_s}{3a}t^ku^2\mathscr B .
$$
将其与 R750(9) 的 $-\frac12\mathscr B$ 系数相加，
得到 $-\frac16\mathscr B$，即 (25)。证毕。

(25) 的修正也只在 (19) 的最后窗口。
若 (8) 的 $r_E\ge d_0$，(24) 的像为零，
所有修复必须已有 $\mathscr B\in t^{T_J}$，
也就是原指定 $P_B$ 本身已通过 carry。
特别 $r=1,k=0$ 时不存在利用别的原 cube
补掉这个指定 carry 或改变值留数的办法。

若 (7) 中某组满足 $m_{0,i}=r_E<d_0$ 且
$n_i\ge d_0-1-r_E$，
则该组乘 $t^j$ 的真实列已经给
$t^{r_E}k[t]/t^{d_0}$ 的整三角像。
此时 (24) 就准确等价于
$\operatorname{ord}v_{\rm repair}\ge r_E$。
没有这个明确原帽条件时，仍保完整 (24) 而不认满射。

## 7. 同 R 与下一精度不能被值不变性替代

(20) 是对整个原来源的值投影结论。
式 (16)、(17) 显示，同一方向仍可改变实际第二块、第三块，
其中 $H_1$、$\xi$、完整 $b_s$ 及两个十三行均保留。
因此不能删掉这些方向的全部首 Bockstein，
更不能从 (20) 推原 $d_2/G_2$ 不变。

若改变最初首核候选为 $P_B+P_H$，
须在这个新候选上求同一个完整修正：
前两块、第三块及所有 carry 仍共用一个 $R$。
若已经固定 $P_2=P_B+pR$，再把一个实际首核方向加到 $R$，
下一位的代表要同时增加其完整 (15)–(17)，
然后才按原 $C_2$ 的全首 Bockstein 像取商。
两种操作不可混同。

本篇完成了原完整 cube 自由度对指定值类的影响，
但没有证明 (25) 在 R750 的真正全来源留数行上非零。
通过 (21) 后，仍须用实际较小因子 $v_F$、
同一残余主部像及完整原余块判定。
原三条完整中央也没有自动传播到 (4) 的全部列。

依赖：
[R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)；
[R502](R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R547](R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R731](R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)；
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R750 全来源增补](../notes/2026-11-15-r750-whole-divisible-source-and-primitive-carry-filter.md)。
