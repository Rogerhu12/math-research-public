# 实际固定测试流的低出生裸链与无 primitive 源

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。AI-assisted，GPT-6 Astra Pro。

状态：**以下技术身份已证明。** 这是原固定测试伴随流和原高出生共同商的直接接合，不另编号为主要结果。它解决实际测试未来向量的裸域缩头问题，并记录真正首段 MP 原像及全部未消除的误差。没有得到测试源的完整右费、纯高返回费或固定测试局部 Gram 上界。

依赖：[真实伴随测试流](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md) §§1–8、[首物理头共同商](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md) §§1–2、[原短核两带](../results/R271-appendix-fixed-original-heads-asymptotic-common-right-cost-and-minimal-chain-closeness.md) §2。

## 1. 保同一个固定测试与原受限伴随

固定原 $m,d=2^m,A=A_m,D=D_m$。对同一个
$f\in\mathcal H_{\le s}^{(m)}$，使用已证伴随流
$$
\mathscr X_p=\bigoplus_{i=0}^{d-1}e_iE_{d-i,p},\qquad
\mathscr R_p=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,p},
$$
$$
\mathcal D_p=D|_{\mathscr X_p},\quad
J_p=E_pE_p^*,\quad U_p=E_p^\dagger,\quad L_p=J_p^{-1}.
$$
置
$$
Z_p=J_{p-1}+\mathcal D_p\mathcal D_p^*,\quad
h_p=Z_p^{-1}t_{p-1},
$$
$$
v_p=\mathcal D_p^*h_p,\quad
e_p=J_{p-1}h_p,\qquad p>s.
\tag{1.1}
$$
为免与原完整右最小链混淆，本稿 $h_p$ 只表示这里的受限正逆输入。
原身份是
$$
t_{p-1}=Dv_p+e_p,\qquad
t_p=-Av_p,\qquad
Av_p+Dv_{p+1}=-e_{p+1}.
\tag{1.2}
$$

因为 $E_p$ 是 $A$ 的顶层行，$\|E_p\|\le\|A\|\le6$，所以
$0\prec J_p\preceq36I$。由 $e_p=J_{p-1}h_p$，
$$
\boxed{\|e_p\|^2\le36\,\mu_{p-1}(e_p)^2.}
\tag{1.3}
$$
这仅是物理源范数界，不是任何右逆费用界。

## 2. 实际 v 与 t 的 primitive 自由条件

$\mathcal D_p$ 的核为
$$
\ker\mathcal D_p
=\mathscr X_p\cap(\mathbb C^d\otimes E_{1,p})
=\mathbb C^d\otimes E_{1,p}.
$$
故 (1.1) 的真正受限伴随自动给
$$
\boxed{
v_p\perp\mathbb C^d\otimes E_{1,p}.
}
\tag{2.1}
$$
也可逐头核：第 $i$ 头的伴随是
$P_{E_{d-i,p}}D^*|_{E_{d-i-1,p-1}}$，
它与每个 $D$-primitive 向量正交。最高第 $d-1$ 头的源空间为零。

$A$ 只作用物理头，故保这个尾正交补。于是
$$
\boxed{
t_p\in\mathscr R_p\cap
(\mathbb C^d\otimes E_{1,p})^\perp
=\bigoplus_{i=0}^{d-3}e_i
(E_{d-i-1,p}\ominus E_{1,p}),\qquad p>s.
}
\tag{2.2}
$$
所以真正测试源没有零次 primitive jet：
$P_{E_{1,p}}t_p=0$。
这不等于 $t_p$ 位于一个固定小物理头前缀；
其允许的头数仍随整个 $d$ 增长。也不把此条件传给
$Z_{p+1}^{-1}t_p$ 或真正 $\mathcal G^\dagger\zeta(t_p)$。

## 3. 原低出生商自动给全部裸右旗

固定 $b>s$ 且 $b+d\le Q$。对 $1\le j\le d$ 定义
$$
\boxed{
a_j=P_{E_{j-1,b+j}^{\perp}}v_{b+j}.
}
\tag{3.1}
$$
原 $v_{b+j}$ 在第 $i$ 头的尾属于 $E_{d-i,b+j}$。
若 $i>d-j$，则 $d-i\le j-1$，该分量被 (3.1) 杀掉。
因此
$$
\boxed{
a_j\in
\bigoplus_{i=0}^{d-j}e_i
\bigl(E_{d-i,b+j}\cap E_{j-1,b+j}^{\perp}\bigr).
}
\tag{3.2}
$$
这恰是第 $j$ 段的原裸输入域，包括全部缩短头旗。
无需假定完整的 $v_{b+j}$ 本身缩头。

高出生空间在 $D$ 下不变：
$DE_{j,b+j+1}\subseteq E_{j-1,b+j}$，
且在 $A$ 下也不变。因此把 (1.2) 压到共同商，准确得到
$$
\boxed{
Da_1=t_b-e_{b+1},
}
\tag{3.3}
$$
$$
\boxed{
P_{E_{j-1,b+j}^{\perp}}
(Aa_j+Da_{j+1})
=-P_{E_{j-1,b+j}^{\perp}}e_{b+j+1},
\quad1\le j<d.
}
\tag{3.4}
$$
末段 $a_d$ 只含第零物理头，所以 $Aa_d=0$。
(3.4) 右端自动位于正确输出域
$$
\bigoplus_{i=0}^{d-j-1}e_i
(E_{d-i-1,b+j}\cap E_{j-1,b+j}^{\perp}).
$$
这是原裸近链，并非零内部输出的完整右链。

第 $j=1$ 段不作任何出生截断，$a_1=v_{b+1}$。
由 (2.1)，它正交于整个 $\ker D$，结合 (3.3) 得
$$
\boxed{
a_1=
(D:\mathcal H_{b+1}\to\mathcal H_b)^\dagger
(t_b-e_{b+1}).
}
\tag{3.5}
$$
每头分别理解这个真正 MP 逆。
它支付的是显示的同源组合，不能把 $e_{b+1}$ 删除后换成
$D^\dagger t_b$。

## 4. 全部真幂的带误差身份与同窗预算

反复用 (1.2)，且 $D^j$ 杀掉 (3.1) 扣除的高出生分量，得
$$
\boxed{
D^ja_j=(-A)^{j-1}t_b
-\sum_{\ell=1}^{j}(-A)^{j-\ell}D^{\ell-1}e_{b+\ell},
\quad1\le j\le d.
}
\tag{4.1}
$$
证明从 (3.3) 开始；乘下一次 $D$ 后用
$Dv_{b+j+1}=-Av_{b+j}-e_{b+j+1}$，
并利用 $A,D$ 交换，即得到下一阶。所有误差均来自同一个
$f$ 的真正流，乘法次序与孔层均保持。

记右端为 $z_j$。则有真正幂 MP 的投影身份
$$
\boxed{
(D^j)^\dagger z_j=P_{E_{j,b+j}^{\perp}}a_j,\qquad
\sum_{j=1}^{d}\|(D^j)^\dagger z_j\|^2
\le\sum_{j=1}^{d}\|v_{b+j}\|^2.
}
\tag{4.2}
$$
它没有将每个 $z_j$ 误称为同一个无误差源的 $A$ 次幂。

若 $b$ 是原共同 good top，对固定
$f\in\mathscr T_n=\operatorname{span}(e_0,\ldots,e_{n-1})$，
原全窗正预算给
$$
\sum_{p=b+1}^{b+d}
[\|v_p\|^2+\mu_{p-1}(e_p)^2]
\le\frac{4n}{K_{\rm win}}\|f\|^2.
\tag{4.3}
$$
于是本稿的实际裸输入和所有内部物理误差均有
$$
\boxed{
\sum_j\|a_j\|^2\le\frac{4n}{K_{\rm win}}\|f\|^2,
\qquad
\sum_{p=b+1}^{b+d}\|e_p\|^2
\le\frac{144n}{K_{\rm win}}\|f\|^2.
}
\tag{4.4}
$$
(3.4) 的低投影误差之和不更大。
这些仍是输入／输出的原范数；没有对内部约束的伪逆作免费估计。

还可记录首个误差的低高度部分。由 (2.2) 和 (1.2)，
$$
P_{E_{1,b}}e_{b+1}=-P_{E_{1,b}}Dv_{b+1}.
$$
原 $D^*E_1\subseteq E_3$、(2.1) 及短核界
$\|D|_{E_3}\|^2\le2S_m$ 给
$$
\boxed{
\|P_{E_{1,b}}e_{b+1}\|
\le\sqrt{2S_m}\,
\|P_{E_{3,b+1}\ominus E_{1,b+1}}v_{b+1}\|.
}
\tag{4.5}
$$
在每个 $p>s+1$ 有相同公式。不能仅由 (4.5) 的源范数小
推断这个单独 primitive 投影的裸或完整右费小。

## 5. 可用接口及未消除的误差

本稿付清了实际 $v$ 的裸商缩头、首段真正 MP 费用，
以及所有误差的同窗物理平方和。它保留真正固定测试、同一个
$b$ 与同一个原实际源族。

欲把 (3.1) 修成 $t_b$ 的真正裸或完整右链，仍须补
首误差 $e_{b+1}$ 和 (3.4) 的全部内部误差；(4.3) 支付的是
$\mu(e_p)$，(1.3) 仅降到物理范数。原与实际左流的弱配对可用
$$
\langle L_{p-1}r_{p-1},e_p\rangle
=-\langle u_p,v_p\rangle
$$
逐项或整段支付，但该身份保持真实端点配对守恒，
本身不产生右修复。任何后续双链表示或端点消元必须继续保留
这些准确误差，不能从 (2.2) 或 (4.4) 直接删除终端测试源。
