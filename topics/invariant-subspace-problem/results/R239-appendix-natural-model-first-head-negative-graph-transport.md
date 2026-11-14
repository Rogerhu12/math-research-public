# R239 附录：同一原负源的天然模型首头负图运输

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文把同一个原真正负图源送到天然四块模型的首头负图，支付首头裸向量的实际差、原负号与模型平坦投影的相消，以及随后完整正 resolvent 的左费/两费用。模型头退化，另有核向量；本文不把其单首头负图冒作整个模型源流像。所需模型余比较仍为 OPEN，普通 ISP 与 $N=M$ 未解决。

依赖：[四块天然旗与裸链运输](R239-appendix-natural-four-block-free-flag-and-bare-chain-transport.md)、[完整平坦对偶运输](R239-appendix-natural-four-block-flat-dual-transport-with-one-head-condition.md)、[模型首源旗无角度支付](R239-appendix-natural-model-first-source-flag-without-angle-loss.md)，以及[完整正 resolvent 校正](R239-appendix-positive-resolvent-negative-source-defect-correction.md)。

## 1. 同一个原负图来源和同一个天然模型源

固定原参数
$$
m\ge8,\quad d=2^m,\quad h=d/4,\quad n=m-2,
\quad 4d\le q\le e^{d^3/4}.
$$
仍使用原尾 $D=D_m$ 和旧孔层 $q$。原头为 $A=A_m$，四块头为 $A_\square$。

令原源 $r$ 属于真正的负源图
$$
\mathscr N_A=\ker[P_A(L_A+B_A)],
\qquad L_A=J_{{\rm left},A}^{-1},\quad
B_A=J_{{\rm bare},A}^{-1}.
\tag{1.1}
$$
这里 $P_A$ 是原物理首源头投影。记
$$
v=E_{A,q}^{\dagger}r,\quad c^\flat=c_A^\flat(r),
\quad\mu=\|v\|,\quad\lambda=\|c^\flat\|,
\quad\chi=\sqrt{\alpha_A(r)^2+\lambda^2},
\quad a=\Gamma r.
$$

沿天然模型零源旗作原左 Schur 后，前稿得到模型天然源 $g$。它有不依赖所选自由补全的准确身份
$$
\boxed{g=\mathcal B_\square a.}
\tag{1.2}
$$
原因是 Schur 只改动天然模型零源旗 $\mathscr Y$，而 $\mathcal B_\square\mathscr Y=0$。因此本稿的 $g$ 与之前三种费用运输中的 $g$ 完全相同。

使用已付常数
$$
\rho=216\eta_{m-3}(2048q^2)^3dh(h+1)^2e^{11d^4/40}
\le e^{-d^4/20},\qquad
\sigma=e^{-d^4/600},\qquad\rho\le\sigma.
\tag{1.3}
$$
记 $\mathscr U_\square$ 为天然模型完整右最小者空间。之前完整测试/Riesz 运输已经给
$$
\boxed{
\|c_\square^\flat(g)-P_{\mathscr U_\square}c^\flat\|
\le\sigma(\mu+\lambda).
}
\tag{1.4}
$$
原左向量与模型真正左最小者还满足
$$
\|v-E_{\square,q}^{\dagger}g\|
\le\tau:=\rho\lambda+3\rho(1+\rho)\mu.
\tag{1.5}
$$

## 2. 模型天然首源空间和共同物理右空间

模型天然源的 Taylor 表示为
$$
\mathscr R_\square
=\left\{\sum_{t=0}^{h}Q_tu_t:
u_t\in\operatorname{Ran}A_\square^{t+1}\otimes K_{q-t}\right\}.
\tag{2.1}
$$
这是有限个有界 Taylor 坐标的闭直和表示；不声明不同 $Q_t$ 的像正交。

无角度旗稿已逐项证明 $e_0\in\operatorname{Ran}A_\square^{t+1}$ 对 $0\le t\le h$ 成立：$t\le h-2$ 使用第一低块头 $e_{t+1}$，最后两层分别使用 $e_{2h-1}$、$e_{d-1}$。所以普通物理首头投影保持 (2.1)。它在天然源空间的限制 $P_\square$ 因而为正交投影，且
$$
\boxed{P_\square\mathscr R_\square=e_0E_{h+1,q},
\qquad E_{h+1,q}=\ker D^{h+1}\cap\mathcal H_q.}
\tag{2.2}
$$
这是原首源旗 $e_0E_{d-1,q}$ 的子空间。

令 $R=D^\dagger:\mathcal H_q\to\mathcal H_{q+1}$ 为同一个原完整层 MP 逆。模型首头完整和裸最小链都准确为
$$
R_{0,\square}f=e_0Rf
\quad\text{置于右首段，其他右段为零},
\qquad f\in E_{h+1,q}.
\tag{2.3}
$$
它合法，因为 $A_\square e_0=0$，且 $Rf\in E_{h+2,q+1}\subseteq E_{d,q+1}$。任何同源完整或裸链与 (2.3) 的差，其首段首头被 $D$ 杀掉，故与 $Rf\perp\ker D$ 正交。这既证明最小性，也证明首头与其余源的两个右度量交叉为零。

因此模型首头共同度量为
$$
K_\square=R_{0,\square}^*R_{0,\square},\qquad
(B_\square)_{P}=K_\square,\qquad
(G_\square)_{P}=K_\square^{-1}.
\tag{2.4}
$$
注意 $K_\square$ 是原完整 MP 逆在较短源旗上的真实限制所给的 Gram；不假定原 $K_A$ 自动约化这个短核旗。

相应同一物理首段最小右空间为
$$
\boxed{
\mathscr V_{0,\square}=e_0R E_{h+1,q}
\subseteq e_0R E_{d-1,q}=\mathscr V_{0,A}.
}
\tag{2.5}
$$
它同时包含在 $\mathscr U_\square$ 中。记其物理正交投影为 $\Pi_{0,\square}$。

## 3. 首头裸链的向量差由同一个延拓误差支付

令 $C_A=P_{>q}\mathcal E_A^{\rm full}$，$C_\square$ 同理。两个完整延拓本身是真核，所以其首输出满足
$$
DC_Aa|_1=-r,\qquad DC_\square a|_1=-g.
$$
因此有准确向量身份
$$
\boxed{g-r=D(C_A-C_\square)a|_1.}
\tag{3.1}
$$
原首头裸链和模型首头裸链均用同一个 $R=D^\dagger$：
$$
a_{0,A}(r)=e_0R(P_Ar)_0,
\qquad a_{0,\square}(g)=e_0R(P_\square g)_0.
$$
由 (3.1)，差为将 $(C_A-C_\square)a$ 的首段首头施加正交投影 $D^\dagger D$。故
$$
\boxed{
\|a_{0,\square}(g)-a_{0,A}(r)\|
\le\|(C_A-C_\square)a\|
\le\rho\|\Gamma r\|\le\rho\mu.
}
\tag{3.2}
$$
这是同一物理右链空间中的向量差。单独的 $\alpha_\square(g)$ 范数上界不能替代它。

## 4. 原负号与模型平坦投影的精确相消

原 $r\in\mathscr N_A$ 给 $P_AL_Ar=-K_A(P_Ar)_0$。在实际首头右空间中，这等价于
$$
\boxed{\Pi_{0,A}c^\flat=-a_{0,A}(r).}
\tag{4.1}
$$
因为 (2.5) 是真实物理子空间包含关系，(4.1) 投影后仍是
$$
\Pi_{0,\square}c^\flat
=-\Pi_{0,\square}a_{0,A}(r).
\tag{4.2}
$$
又 $\Pi_{0,\square}P_{\mathscr U_\square}=\Pi_{0,\square}$，且
$a_{0,\square}(g)\in\mathscr V_{0,\square}$。模型首头缺陷向量
$$
d_\square^{\rm phys}
=a_{0,\square}(g)+\Pi_{0,\square}c_\square^\flat(g)
$$
于是有准确分解
$$
\begin{aligned}
d_\square^{\rm phys}
=\Pi_{0,\square}\bigl[
&c_\square^\flat(g)-P_{\mathscr U_\square}c^\flat\\
&+a_{0,\square}(g)-a_{0,A}(r)\bigr].
\end{aligned}
\tag{4.3}
$$
使用 (1.4)、(3.2)，得到
$$
\boxed{
\|d_\square^{\rm phys}\|
\le e:=(\sigma+\rho)\mu+\sigma\lambda.
}
\tag{4.4}
$$
这里原裸向量、原平坦向量和原 $v$ 全都来自同一个 $r$。没有从范数比较推断向量相消，也没有把短核 Gram 的压缩逆当成环境逆。

若原源并非精确负图，(4.4) 右侧只需再加原物理缺陷
$\|a_{0,A}(r)+\Pi_{0,A}c_A^\flat(r)\|$；本稿后续保留精确负图假设。

## 5. 用完整正 resolvent 进入模型首头负图

在天然模型源空间上记
$$
L_\square=J_{{\rm left},\square}^{-1},\quad
B_\square=J_{{\rm bare},\square}^{-1},\quad
G_\square=J_{{\rm right},\square},\quad
S_\square=L_\square+B_\square.
$$
完整右链的低出生投影是模型同源裸可行链，故
$B_\square\preceq G_\square^{-1}$。结合 (2.4)，正 resolvent 引理的全部假设成立。

定义
$$
t_\square=S_\square^{-1}P_\square S_\square g,
\qquad g_-=g-t_\square.
\tag{5.1}
$$
这是天然闭源空间内部的有界运算。共同单位坐标下的负图缺陷与 (4.3) 等距，所以该引理给
$$
\boxed{
g_-\in\mathscr N_{\square,0}
:=\ker[P_\square(L_\square+B_\square)],
}
\tag{5.2}
$$
$$
\boxed{
\chi_\square(t_\square)^2+2\mu_\square(t_\square)^2
\le e^2,\qquad
\mu_\square(t_\square)\le e/2.
}
\tag{5.3}
$$
于是
$$
\boxed{
\chi_\square(g_-)\le\chi_\square(g)+e,\qquad
|\mu_\square(g_-)-\mu_\square(g)|\le e/2.
}
\tag{5.4}
$$
整个校正未引入额外有限头条件数。它也未支付普通右费
$\lambda_\square(t_\square)$。

特别，真正左向量仍保留同一个原来源：
$$
\boxed{
\|v-E_{\square,q}^{\dagger}g_-\|
\le\rho\lambda+3\rho(1+\rho)\mu+e/2.
}
\tag{5.5}
$$

## 6. 原比较只需在这些模型首头负图来源上继续支付

前稿的同源三费用合计为
$$
\chi_\square(g)\le(1+2\sigma)\chi+\sqrt2\sigma\mu,
\qquad
\mu\le(1+\rho)\mu_\square(g)+\rho\lambda.
\tag{6.1}
$$
由 $\lambda\le\chi$ 和 (4.4)、(5.4)，得到
$$
\boxed{
\chi_\square(g_-)
\le(1+3\sigma)\chi+
\bigl((1+\sqrt2)\sigma+\rho\bigr)\mu.
}
\tag{6.2}
$$
另令
$$
a_*=1-\frac{(1+\rho)(\sigma+\rho)}2,\quad
b_*=(1+\sqrt2)\sigma+\rho,\quad
c_*=\rho+\frac{(1+\rho)\sigma}{2}.
$$
则
$$
\boxed{a_*\mu\le(1+\rho)\mu_\square(g_-)+c_*\chi.}
\tag{6.3}
$$
这些常数都显式，且 $a_*>0$。

若后续只在本稿同一来源产生的 $g_-$ 上证明
$$
\mu_\square(g_-)\le\sqrt{C_m}\,\chi_\square(g_-),
$$
并且
$a_*-(1+\rho)\sqrt{C_m}\,b_*>0$，便有
$$
\boxed{
\mu_A(r)\le
\frac{(1+\rho)(1+3\sigma)\sqrt{C_m}+c_*}
{a_*-(1+\rho)\sqrt{C_m}\,b_*}
\chi_A(r).
}
\tag{6.4}
$$
目标级别 $C_m=O(e^{d^3/4}/d)$ 足以让这个四次指数误差被吸收。但本文仍未证明这样的 $C_m$。

## 7. 首头负图、退化模型的完整源流和真实较小头的区别

$A_\square$ 有多个独立核头方向；原 $A_m$ 的第一条上对角非零，而模型没有该性质。因此 (5.2) 只称为“模型首头负图”，不将它等同于模型完整向下源流的像。其余模型核方向及相应源交叉条件仍须保留。

另一方面，尾重排稿的真实恒等式
$A_\square+D_m=A_{m-2}+D_{m-2}$ 使用物理层重排，将旧单层源变成新三层源。较小真实头 $A_{m-2}$ 仍是 regular 原头；该稿每个较低新切口的真正最小性，允许在相邻切口合法时进入较小头的完整原负图。不能用本稿旧分层中的单首头条件替代那个真实新分层结论；其最低头与窗口条件仍按所调用原引理分别核对。

若原 $r$ 还来自先前的真正 $\mathfrak M$ 余图，本稿只显式运输了其负图条件和三种费用。校正 (5.1) 没有自动运输原余图的 $\mathfrak M$ 正交条件，也不推出模型 primitive 支撑消失。后续对余图或更大模型核方向的处理须保持这些边界。

