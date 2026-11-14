# 同一固定测试的端点截断与真实小两费源

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。AI-assisted，GPT-6 Astra Pro。

状态：**技术结论已证明。** 由原固定测试的真正端点最小者向下截断，
可得到同一固定测试的真实源。其原裸／平坦两费和，以及它到原
Riesz 测试源的左费用距离，由同一个窗口的正投影耗散共同支付。
这不是端点消失，也没有支付普通完整右费。

依赖：[真实伴随测试流](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md) §§1、4、8、
[真正左最小者的截断源流](../results/R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、
[同未来带的两费投影](../results/R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md)。

## 1. 真正端点，不用 q_p 代替左最小者

固定同一个原 $m,d,A,D$ 和同一个
$f\in\mathcal H_{\le s}^{(m)}$。沿原测试流记
$$
q_p=P_{V_p}f,\qquad k_p=P_{\mathcal K_p}f,\qquad
t_p=E_pP_{V_p}f,\qquad U_p=E_p^\dagger.
$$
已证
$$
w_p^f:=U_pt_p=q_p-k_p=P_{\mathcal W_p}f,
\qquad \mathcal W_{p+1}\subseteq\mathcal W_p.
\tag{1.1}
$$
$\mathcal W_p$ 是增广左可行空间扣除原零源核后的真正嵌套物理余空间。
所有孔层始终使用这个原 $m$。

固定 $b>s$、$p=b+d\le Q$。
令 $T_{b\leftarrow p}$ 是原真正左最小者的向下源流，定义
$$
\boxed{s_b^f=T_{b\leftarrow b+d}\,t_{b+d}.}
\tag{1.2}
$$
因此
$$
\boxed{
U_bs_b^f=P_{\le b}w_{b+d}^f.
}
\tag{1.3}
$$
这是同一实际端点 $U_{b+d}t_{b+d}$ 的真正物理截断；
源 $s_b^f$ 对 $f$ 线性，没有在 $b$ 处重新挑一个较便宜的测试。

必须使用 $q_{b+d}-k_{b+d}$，不能改成
$q_{b+d}-k_b$。后者一般不正交于整个 $\mathcal K_{b+d}$，
因而不足以应用原完整平坦链的未来投影身份。

## 2. 左距离与真实未来带的准确 Pythagoras

定义同一窗口的耗散
$$
\Delta_b(f)
=\|w_b^f-w_{b+d}^f\|^2
=\sum_{\ell=b+1}^{b+d}
\left[
\|v_\ell(f)\|^2+\mu_{\ell-1}(e_\ell(f))^2
+\|\text{原归一首头创新}_\ell(f)\|^2
\right].
\tag{2.1}
$$
第一等号来自 (1.1) 的嵌套正交投影，第二等号是原伴随流的
准确正能量身份；没有对非正交误差单独求和。

令端点的真实未来带为
$$
y_b^f=P_{[b+1,b+d]}w_{b+d}^f.
\tag{2.2}
$$
$w_b^f$ 支持在 $\le b$，所以 (1.3) 直接给
$$
w_b^f-w_{b+d}^f
=U_b(t_b-s_b^f)-y_b^f.
$$
左右两项支持在互异孔层，因而
$$
\boxed{
\mu_b(t_b-s_b^f)^2+\|y_b^f\|^2=\Delta_b(f).
}
\tag{2.3}
$$
这比仅分别估计两项更准确。

## 3. 同一个端点给原裸和平坦两费

$w_{b+d}^f$ 是真正左最小者，其 $b$ 截断也是真正左最小者。
原同未来带身份因此适用于 (1.2) 的源及 (2.2) 的同一带：
$$
\mathcal A_b s_b^f=-P_{\rm bare}y_b^f,\qquad
F_b^*L_bs_b^f=P_{\rm full}y_b^f.
\tag{3.1}
$$
这里两个 $P$ 是原合法裸核、完整右核的正交投影；
完整平坦链仍是同一源的 $F_b^*L_bs_b^f$。
特别
$$
\boxed{
\Xi_b(s_b^f)^2
=\alpha_b(s_b^f)^2+\lambda_{{\rm flat},b}(s_b^f)^2
\le2\|y_b^f\|^2.
}
\tag{3.2}
$$
与 (2.3) 合并得到
$$
\boxed{
\mu_b(t_b-s_b^f)^2+\frac12\Xi_b(s_b^f)^2
\le\Delta_b(f).
}
\tag{3.3}
$$
原零源和完整共同费用方向给出的普遍负图条件也按 (3.1) 保持。
本文不把 $s_b^f$ 放进尚未在该端点实际施加的增长头旗余商。

## 4. 固定有限测试空间和同一个 good top

对 $\mathscr T_n=\operatorname{span}(e_0,\ldots,e_{n-1})$，
定义真正的正矩阵
$$
\boldsymbol\Delta_b
=P_{\mathscr T_n}(P_{\mathcal W_b}-P_{\mathcal W_{b+d}})
|_{\mathscr T_n}.
\tag{4.1}
$$
于是 $\Delta_b(f)=\langle\boldsymbol\Delta_bf,f\rangle$。
它不大于原共同 good-top 选择使用的
$D_b^{(n)}=\sum_{\ell=b}^{b+d}\Psi_\ell$，所以在同一个已选切口，
$$
\boldsymbol\Delta_b\preceq\frac{4n}{K_{\rm win}}I.
\tag{4.2}
$$
(3.3) 给该同切口、同固定测试映射的界
$$
\boxed{
\mu_b(t_b-s_b^f)^2+\frac12\Xi_b(s_b^f)^2
\le\frac{4n}{K_{\rm win}}\|f\|^2.
}
\tag{4.3}
$$
特别 $\mu_b(t_b-s_b^f)\le2\sqrt{n/K_{\rm win}}\|f\|$，
$\Xi_b(s_b^f)^2\le8n\|f\|^2/K_{\rm win}$。

此外，若 $b$ 沿步长 $d$ 的不交窗口网格取值，
$(b,b+d]$ 上的耗散项互不重复。因此准确有
$$
\boxed{\sum_b\boldsymbol\Delta_b\preceq I_{\mathscr T_n}.}
\tag{4.4}
$$
此式使用半开孔窗，不把两端都计入。
(4.2) 仍沿已选共同切口使用原常数，没有悄悄另选一个切口。

## 5. 等价的混合正 Gram 上界

本节只把 (3.3) 写成有限参数下的准确最小二次型，
不把它提升为所缺的纯两费固定测试 Gram。

在原源空间上记
$$
L=L_b,\qquad M_2=B_b+L_bG_bL_b,\qquad J=L^{-1}.
$$
固定参数下这些算子严格正、有界可逆。
对任意测试源 $t$，
$$
\inf_z\left[
\langle L(t-z),t-z\rangle+\frac12\langle M_2z,z\rangle
\right]
=
\left\langle (J+2M_2^{-1})^{-1}t,t\right\rangle.
\tag{5.1}
$$
这是两个正二次型的平行和。可由正规方程
$(L+M_2/2)z=Lt$ 直接核得；
各算子乘法次序不作交换。

令 $\mathcal T_bf=t_b(f)$ 为真正 Riesz 测试源映射。
在 (5.1) 中代入由 (1.2) 实际构造的 $z=s_b^f$，得到
$$
\boxed{
\mathcal T_b^*(J_b+2M_{2,b}^{-1})^{-1}\mathcal T_b
\preceq\boldsymbol\Delta_b.
}
\tag{5.2}
$$
因此该混合 Gram 的整条不交网格和不超过单位。
它允许一个左费用误差，所以不能替代只允许裸／平坦双链的
固定测试局部 Gram；这一区别在 (5.1) 中明确保留。

## 6. 实际原源配对的剩余项

若 $r_b$ 是同切口的任意原源，真正固定测试泛函为
$$
\langle U_br_b,f\rangle=\langle L_br_b,t_b(f)\rangle.
$$
(2.3) 给
$$
\boxed{
\langle U_br_b,f\rangle
=\langle L_br_b,s_b^f\rangle+\mathcal E_b(r_b,f),
\quad
|\mathcal E_b(r_b,f)|
\le\mu_b(r_b)\sqrt{\Delta_b(f)}.
}
\tag{6.1}
$$
当原 $\mu_b(r_b)$ 有界且使用共同 good top 时，显示的误差趋零。
但主项 $\langle L_br_b,s_b^f\rangle$ 没有消失：
两边的 $\Xi$ 都小，不自动控制它们的左费用交叉配对。

特别 (3.2) 没有提供 $\lambda_b(s_b^f)$，
不能将它代入需要普通完整右费的
$|\langle Lr,s\rangle|\le\lambda_{\rm flat}(r)\lambda(s)$。
原端点守恒、完整误差 $e_p$、跨头与真正纯高返回仍保留。
