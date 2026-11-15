# R271 附录：同源位置加权交换、完整真旗与排斥 Hardy 界

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文在原连续尾上证明带位置平方权的实际交换行界。它保原同一个固定测试、同一个真正顶部和真实投影缺陷；其总费用为 $Q\|f-u_f\|^2$，常数与 $m,Q$ 无关。还证明在整个真实正交尾核旗之后，该位置加权界只增加一个绝对常数，不乘旗高度。另给原物理交换形式的全 Fock 排斥 Hardy 下界。

这些量与此前 $\sum_i\|P_i^-u_f\|^2=O(\zeta_f^2/x)$ 不同：本稿保每个位置的 $(i+1)(i+2)$ 权，没有把高位置的交换差并入一个无权总量。本文不从这两个已付界推断顺次 MP、Feshbach 逆或完整返回的相对不等式；那些联合步骤仍待证明。

依赖：[真实投影缺陷与全暗矩](R271-appendix-actual-projection-defect-two-sided-generator-and-all-dark-moments.md)、[全部真旗导数带宽](R271-appendix-all-orthogonal-jet-flags-dark-factorial-moments-and-derivative-bandwidth.md)、[原同一顶部强尾源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。

## 1. 原投影、局部缺陷和位置形式

固定原强联块
$$
C=A_m+D_<,\quad C^h=0,\quad h=2^m+R,\quad x=m+R\ge1,
\qquad D=\sum_{i\ge x}(i+1)^{-2}E_i .
$$
仍用原总尾窗口 $Q$、闭空间 $K=K_{m,Q}\subset V=V_{m,Q}$。令固定有限物理 $f$ 在第 $x$ 位及以后为真空，且用同一个
$$
v=P_Vf,\qquad k=P_Kf,\qquad u=v-k,\qquad e=f-v .
$$
这里 $e\perp k$，因而
$$
\Delta_f^2:=\|e\|^2+\|k\|^2=\|f-u\|^2 .
\tag{1.1}
$$
$f,e,k,u$ 的原总尾支撑均 $\le Q$，故其远孔数也 $\le Q$。令 $\mathcal N$ 是远孔数，并置
$$
\mathcal Q_f=\langle\mathcal Ne,e\rangle+\langle\mathcal Nk,k\rangle
\le Q\Delta_f^2 .
\tag{1.2}
$$
本稿先保 $\mathcal Q_f$，最后才可使用这个 $Q$ 上界。

对所有相邻对 $(i,i+1)$、$i\ge x$，不要求互不相交，令
$$
H_i=n_{i+1}-n_i,\qquad P_i^-=(I-U_i)/2,
$$
其中 $U_i$ 是物理交换酉反射。令 $A_i^-$ 是原一孔 primitive 行
$$
\frac{b_{i+1}e_i-b_ie_{i+1}}{\sqrt{b_i^2+b_{i+1}^2}},
\qquad b_i=(i+1)^{-2},
$$
的正交投影，在该对真空/双占据上为零。定义非负位置形式
$$
\mathfrak e_{\rm pos}(z)=
 \sum_{i\ge x}(i+1)(i+2)\|P_i^-z\|^2,
$$
$$
\mathfrak a_{\rm pos}(z)=
 \sum_{i\ge x}(i+1)(i+2)\|A_i^-z\|^2.
\tag{1.3}
$$
它们先读作有限部分和的单调极限；有限值给相应闭行算子的自然形式域。物理算子形式
$$
\mathcal G_{\rm pos}
=\sum_{i\ge x}(i+1)(i+2)(I-U_i)
$$
准确满足 $\langle\mathcal G_{\rm pos}z,z\rangle=2\mathfrak e_{\rm pos}(z)$。

## 2. 每个真实相邻对的相对缺陷积分

每次只变一个原对。写
$$
\theta_i=\log\frac{i+2}{i+1},\quad
b_i(t)=a_ie^t,\quad b_{i+1}(t)=a_ie^{-t},
\quad a_i=\sqrt{b_ib_{i+1}},\quad0\le t\le\theta_i .
$$
原其余权不变，端点 $t=\theta_i$ 是原模型。真实相似
$$
D(t)e^{tH_i}=e^{tH_i}D(0)
$$
保持全部原头旗和孔截断，给 $V(t)=e^{tH_i}V(0)$、
$K(t)=e^{tH_i}K(0)$。若 $P(t)$ 是任一个这样的物理正交投影，则
$$
P'=H_iP+PH_i-2PH_iP.
$$
由于 $H_if=0$，对 $z(t)=(I-P_{V(t)})f$ 和 $z(t)=P_{K(t)}f$ 分别有
$$
z'=(I-2P(t))H_iz.
\tag{2.1}
$$
反射的范数为 $1$。更重要的是，$H_i$ 不随 $t$ 变化，因此
$$
(H_iz)'=H_i(I-2P(t))H_iz .
$$
沿同一个实参数区间反向使用 Gronwall：
$$
\|H_iz(t)\|\le e^{\theta_i-t}\|H_iz(\theta_i)\|.
\tag{2.2}
$$
这是局部相对界，右边仍是原端点中同一个 $H_i$ 的真实向量；没有换成环境 $\|z\|$ 后再无限求和。

在 $t=0$，配平空间被 $U_i$ 约化，且 $f$ 对称，所以
$P_i^-z(0)=0$。由 (2.1)–(2.2)，
$$
\begin{aligned}
\|P_i^-z(\theta_i)\|
&\le\int_0^{\theta_i}\|H_iz(t)\|\,dt\\
&\le(e^{\theta_i}-1)\|H_iz(\theta_i)\|
=\frac{\|H_iz(\theta_i)\|}{i+1}.
\end{aligned}
\tag{2.3}
$$
最后的等号使用原连续权的准确相邻比。

对真正 primitive 暗投影 $A_i^-(t)$，直接的一孔计算给
$\|(A_i^-)'(t)\|=1/\cosh(2t)\le1$。它及其导数都只支撑该对的单占据扇区，而 $H_i^2$ 正是这个扇区投影。因此
$$
\|(A_i^-)'(t)z\|\le\|H_iz\|,
\qquad
\left\|\frac d{dt}\bigl(A_i^-(t)z(t)\bigr)\right\|
\le2\|H_iz(t)\|.
$$
平衡面上 $A_i^-(0)z(0)=0$，于是
$$
\|A_i^-z\|\le\frac{2}{i+1}\|H_iz\|.
\tag{2.4}
$$

现在回原同一个 $u=f-e-k$。两个暗投影都杀 $f$。令
$$
r_x=1+\frac1{x+1}.
$$
由 (2.3)–(2.4) 以及平方三角不等式，
$$
\begin{aligned}
\mathfrak e_{\rm pos}(u)
&\le2r_x\sum_{i\ge x}
  \bigl(\|H_ie\|^2+\|H_ik\|^2\bigr),\\
\mathfrak a_{\rm pos}(u)
&\le8r_x\sum_{i\ge x}
  \bigl(\|H_ie\|^2+\|H_ik\|^2\bigr).
\end{aligned}
$$
相邻对虽可重叠，但原逐位恒等式给
$$
\sum_{i\ge x}H_i^2
=\sum_{i\ge x}(n_i+n_{i+1}-2n_in_{i+1})
\preceq2\mathcal N .
\tag{2.5}
$$
因此
$$
\boxed{
\mathfrak e_{\rm pos}(u)\le4r_x\mathcal Q_f
\le4r_x Q\Delta_f^2,\qquad
\mathfrak a_{\rm pos}(u)\le16r_x\mathcal Q_f
\le16r_x Q\Delta_f^2.
}
\tag{2.6}
$$
也即
$$
\boxed{\langle\mathcal G_{\rm pos}u,u\rangle
\le8r_x Q\|f-u\|^2.}
\tag{2.7}
$$
每次变形都回到同一个原端点，所以这里相加的是同一个 $u$ 上全部原位置的能量。

## 3. 先取全部真正正交旗，仍无旗高度损失

在每个远孔层及独立头上，置
$$
\Pi_\ell(t)=P_{\ker D(t)^\ell},\qquad
F_\ell(t)=\Pi_\ell(t)-\Pi_{\ell-1}(t),\quad\Pi_0=0.
$$
每个 $\Pi_\ell,F_\ell$ 与远孔数 $\mathcal N$ 交换。$H_i$ 自伴且
$\operatorname{ad}_{D(t)}^2H_i=0$，所以它相对该真旗严格三带：
$$
F_aH_iF_b=0\qquad(|a-b|>1).
\tag{3.1}
$$

以下固定一个 $i$，暂省参数。由投影导数公式及 (3.1)，令
$T_\ell=F_{\ell+1}H_iF_\ell$，则准确有
$$
F_\ell'=T_\ell+T_\ell^*-T_{\ell-1}-T_{\ell-1}^* .
\tag{3.2}
$$
对任意 $z$，不同输出旗的正交性和中间两项的平方三角不等式给
$$
\sum_\ell\|F_\ell'z\|^2
\le3\sum_\ell
 \bigl(\|T_\ell z\|^2+\|T_\ell^*z\|^2\bigr)
\le3\sum_\ell\|H_iF_\ell z\|^2 .
\tag{3.3}
$$
同一三带结构还给
$$
\|H_iz\|^2\le3\sum_\ell\|H_iF_\ell z\|^2.
\tag{3.4}
$$
这些是完整正交分析列的估计；没有把每个 $\ell$ 的环境上界相加。

对 §2 的任意一个实际缺陷 $z(t)$，令
$$
\mathcal H_i(z,t)=(H_iF_\ell(t)z(t))_\ell,\qquad
c=2\sqrt3 .
$$
由 (2.1)、(3.3)–(3.4) 和
$\sum_\ell\|H_iF_\ell y\|^2\le\|y\|^2$，
$$
\|\mathcal H_i'(z,t)\|
\le2\sqrt3\,\|\mathcal H_i(z,t)\| .
$$
故
$$
\|\mathcal H_i(z,t)\|
\le e^{c(\theta_i-t)}\|\mathcal H_i(z,\theta_i)\|.
\tag{3.5}
$$
而整个旗分析列的导数满足
$$
\left\|\frac d{dt}(F_\ell(t)z(t))_\ell\right\|
\le c\,\|\mathcal H_i(z,t)\|.
$$
各 $F_\ell(0)$ 也被平衡交换约化，所以所有物理暗分量在 $t=0$ 消失。积分得
$$
\left(\sum_\ell\|P_i^-F_\ell z\|^2\right)^{1/2}
\le(e^{c\theta_i}-1)
  \left(\sum_\ell\|H_iF_\ell z\|^2\right)^{1/2}.
\tag{3.6}
$$
若换成 $A_i^-(t)$，其导数多给一次
$\|\mathcal H_i(z,t)\|$，故右边只多乘 $(c+1)/c$。

对 $t_0=i+1$，均值定理给
$$
t_0(t_0+1)(e^{c\theta_i}-1)^2
\le c^2\left(1+\frac1{t_0}\right)^{2c-1}
\le c^2 r_x^{2c-1}.
\tag{3.7}
$$
此外 (2.5) 与 $\mathcal NF_\ell=F_\ell\mathcal N$ 给
$$
\sum_{i,\ell}\|H_iF_\ell z\|^2
\le2\sum_\ell\langle\mathcal NF_\ell z,F_\ell z\rangle
=2\langle\mathcal Nz,z\rangle.
\tag{3.8}
$$

由于 $D(t)f=0$，始终有 $F_1(t)f=f$、$F_{\ell>1}(t)f=0$；这列的暗分量为零。分别对 $e,k$ 应用 (3.6)–(3.8) 后合并，得到
$$
\boxed{
\sum_\ell\mathfrak e_{\rm pos}(F_\ell u)
\le4c^2r_x^{2c-1}\mathcal Q_f
\le4c^2r_x^{2c-1}Q\Delta_f^2,
\qquad c=2\sqrt3 ,
}
\tag{3.9}
$$
以及
$$
\boxed{
\sum_\ell\mathfrak a_{\rm pos}(F_\ell u)
\le4(c+1)^2r_x^{2c-1}\mathcal Q_f
\le4(c+1)^2r_x^{2c-1}Q\Delta_f^2 .
}
\tag{3.10}
$$
这些常数与 $\ell,h,Q,m$ 无关。$F_\ell$ 始终是物理正交旗；本文没有以顺次 $Q_n\cdots Q_{n-j+1}D^j$ 替换它。

所有求和先在有限对族和有限孔直和中证明，再用非负极限。$u,e,k$ 原本支撑远孔数 $\le Q$，旗投影不改变该支持，故 (3.5) 的分析列和导数均属于同一有限孔自然域。

## 4. 全物理排斥 Hardy 下界

本节不要求向量来自某个实际投影。对原物理相邻交换形式，有
$$
\boxed{
\mathcal G_{\rm pos}\succeq\frac14\mathcal N,
\qquad
\mathfrak e_{\rm pos}(z)\ge\frac18\langle\mathcal Nz,z\rangle .
}
\tag{4.1}
$$
这是闭二次型不等式，允许任意独立头张量。

先在一个固定 $q$ 孔层的有限支撑向量上证明。其基标由
$I\subset\{x,x+1,\ldots\}$、$|I|=q$ 给出，令正函数
$$
\omega(I)=\prod_{j\in I}(j+1)^{-1/2}.
$$
不要求 $\omega$ 属于 Hilbert 空间。对相邻配置 $I,J$ 及边权 $a>0$，
$$
\begin{aligned}
a|z_I-z_J|^2
={}&a\,\omega(I)\omega(J)
 \left|\frac{z_I}{\omega(I)}-\frac{z_J}{\omega(J)}\right|^2\\
&+a\left(1-\frac{\omega(J)}{\omega(I)}\right)|z_I|^2
 +a\left(1-\frac{\omega(I)}{\omega(J)}\right)|z_J|^2 .
\end{aligned}
\tag{4.2}
$$

设 $t=i+1$、$a_i=t(t+1)$、$s_i=\sqrt{t/(t+1)}$。
对应势可准确写为
$$
V(I)=\sum_{j\in I}v_j
+\sum_{\substack{i\ge x\\i,i+1\in I}}
 a_i(s_i+s_i^{-1}-2).
\tag{4.3}
$$
第二项非负：把两个单粒方向在双占据时删去，只增加势。左端点满足
$$
v_x=(x+1)(x+2)
 \left(1-\sqrt{\frac{x+1}{x+2}}\right)
\ge\frac{x+1}{2}\ge\frac12 .
$$
内点 $j>x$、$t=j+1$ 给
$$
v_j=t^2\left[2-\sqrt{1+1/t}-\sqrt{1-1/t}\right]\ge\frac14 .
\tag{4.4}
$$
最后用
$\sqrt{1+s}+\sqrt{1-s}\le2-s^2/4$，$0\le s\le1$。
例如先平方得左边至多 $\sqrt{4-s^2}$，再用平方根的切线界。
所以 $V(I)\ge q/4$。对 (4.2) 的全部配置边求和，非负第一项给
$\langle\mathcal G_{\rm pos}z,z\rangle\ge(q/4)\|z\|^2$。

为保最大自然形式域，可按固定 $q$ 用对数位置截断：
取 $\chi_L(I)$ 为 $\log(2+\max I)/L$ 的一个 $1$-Lipschitz 紧支撑截断，等于 $1$ 的区域随 $L$ 扩大。相邻配置跨位 $i$ 时，
$|\chi_L(I)-\chi_L(J)|\le1/[L(i+1)]$。
每个配置至多有 $2q$ 条可动边，所以新增截断能量
$\le CqL^{-2}\|z\|^2$；其余能量差由原有限能量的支配收敛趋零。
故有限位置支撑向量在固定 $q$ 的自然形式域中稠密。
再按孔数截断并取非负极限，即得全 Fock 的 (4.1)。
这里没有把只在有限支撑成立的算子恒等免费延拓到某个未证实域。

(4.1) 只用于物理 $P_i^-$。不能把它替换成 $\mathfrak a_{\rm pos}$ 的相同下界：例如在一孔层，向量 $\sum_{i\ge x}b_i e_i$ 属于 Hilbert 空间并被全部 $A_i^-$ 杀死。真实 primitive 暗行的零模始终保留。

## 5. 原同源切口与缺陷量词

$\mathcal G_{\rm pos}$ 及两行形式均保持远孔数，因此 (2.6)、(3.9)–(3.10) 是对全部输出孔层同时支付。例如对任意层集合 $\mathcal J$，
$$
\sum_{n\in\mathcal J}\mathfrak e_{\rm pos}(u_n)
\le4r_x\mathcal Q_f
\le4r_x Q\Delta_f^2.
\tag{5.1}
$$
不能逐层再乘一个 $Q$。对固定宽度 $h$ 的未来窗口族，若一层至多被 $\nu$ 个窗口读取，则其总行费用至多在 (5.1) 上乘 $\nu\le h$；这是实际重叠数，间距 $h$ 的网格只乘 $1$。

在[真正最小投影窗口](R271-appendix-true-minimal-projection-weighted-window.md)的
$$
m\ge10,\qquad 4\cdot2^m\le Q\le
 \exp\!\left(\frac{1601}{64}8^m\right)
$$
中，同一 $w\in W$ 已付 $P_Uw\to w$，且该收敛对窗口内 $Q(m)$ 一致。
故对一次选定的固定有限 $f$，
$$
\Delta_f=\|(I-P_U)f\|
\le\|f-w\|+\|(I-P_U)w\|,
\qquad
\limsup\Delta_f\le\|f-w\|.
\tag{5.2}
$$
所以 (2.7) 的归一位置能量满足
$$
\limsup_{m\to\infty}Q^{-1}
 \langle\mathcal G_{\rm pos}u_f,u_f\rangle
\le8\|f-w\|^2
\tag{5.3}
$$
（$x\to\infty$，故 $r_x\to1$），完整真旗也有相同类型、明确绝对常数的结论。这是固定测试逼近程度所控制的真实 $Q$ 尺度，而非把一个无速率尾乘增长常数。

仍未证明的是把顺次投影的完整部分和或真正 Feshbach 逆相对支配于这些位置形式。尤其两端 partial sums、真正 MP 返回与所有同源交叉都不能只凭 (4.1) 删除。本文只提供它们可使用的新共同正预算，不把诸如
$-\operatorname{Re}N_{\rm seq}\preceq C(\mathcal N+\mathcal G_{\rm pos})$
或原 primitive 逆的相应联合式列为已得结论。普通 $N=M$ 仍未完成。
