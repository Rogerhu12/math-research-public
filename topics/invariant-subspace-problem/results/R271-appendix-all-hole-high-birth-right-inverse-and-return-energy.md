# R271 附录：全部孔数的高出生旗右逆及返回能量界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已证明，root 与 kernel 全文独立核查；保留原 Hilbert 范数及真实有限头。新增范围是高出生旗右逆对全部孔数有同一常数。本文不扩大已有有限核提升窗口，也不声明无权 $N=M$。

[真实返回源笔记](../notes/2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md) §1 已用固定孔层的 $D$ 右逆证明高链满射，未给孔数无关常数。本稿改用 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的真实有限头相似：从给定输出段向左求解，最左残量由该输出本身的删除核条件消失。旧合法窗口中的同时右逆通常有更好的常数；本文的新增结论不应被登记为该窗口内的数值改进。

## 1. 真实高出生旗与全部孔数

固定 $m\ge5,d=2^m$。$A=A_m$ 是 $T_N$ 或 $T_Y$ 的实际有限头，$D=D_m$ 是对应纯布尔尾删除，仍使用
$$
D:\mathcal H_p\longrightarrow\mathcal H_{p-1},\qquad
E_{h,p}=\ker(D^h|_{\mathcal H_p}),\qquad E_{0,p}=0.
$$
负孔层为零；若 $h>p$，则 $E_{h,p}=\mathcal H_p$。记
$$
W_j=\operatorname{span}\{e_0,\ldots,e_{j-1}\},\qquad
\nu_m=\|D_m\|\le\sum_{j\ge m}(j+1)^{-2}\le m^{-1}<1.
\tag{1.1}
$$

此节允许任意整数 $q\ge0$，没有提升窗口的上界。沿用联合旗
$$
\mathscr C_{q,t}=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t},\qquad
\mathscr Y_{q,t}=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t}.
$$
$\mathscr C_q$ 的段号为 $1\le t\le d$，$\mathscr Y_q$ 的段号为 $1\le t\le d-1$，并定义
$$
F_qc=Dc_1,\qquad
(S_qc)_t=Ac_t+Dc_{t+1}.
\tag{1.2}
$$
在 $U_{h,q+t}=E_{h,q+t}\ominus E_{h-1,q+t}$ 上，相对出生数是 $t-h+1$。相对出生数至少 $2$ 的输入、输出准确为
$$
\boxed{
\begin{aligned}
\mathscr X_{H,q,t}&=W_{d-t+1}\otimes E_{t-1,q+t}
&& (2\le t\le d),\\
\mathscr Y_{H,q,t}&=W_{d-t}\otimes E_{t-1,q+t}
&& (2\le t\le d-1).
\end{aligned}}
\tag{1.3}
$$
首段均为零。确实，输入每个允许头指标满足 $d-i\ge t$，输出满足 $d-i-1\ge t$，所以附加的 $h\le t-1$ 条件已经强于原逐头删除核条件。

由 $A(W_j\otimes E_{h,p})\subset W_{j-1}\otimes E_{h,p}$（只作用头）及 $DE_{t,p}\subset E_{t-1,p-1}$，$S_q$ 把 $\mathscr X_{H,q}$ 送入 $\mathscr Y_{H,q}$。写
$$
S_{H,q}=S_q|_{\mathscr X_{H,q}}.
$$

## 2. 向左的显式高旗右逆

把 R249 的头相似矩阵 $S_m$ 暂记为 $\Sigma_m$，以免与内部链 $S_q$ 混淆：
$$
A=\Sigma_m(\gamma_m J_d)\Sigma_m^{-1},\qquad
J_de_i=e_{i-1},\quad J_de_0=0,
$$
$$
\gamma_m=e^{20-L_m},\qquad
L_m=\frac{25d^4}{2(d-2)},\qquad
\kappa_m=\|\Sigma_m\|\,\|\Sigma_m^{-1}\|.
\tag{2.1}
$$
$\Sigma_m$ 与其逆都是上三角矩阵，故保每个 $W_j$。它们只作用有限头，因此也保 (1.3) 的全部删除核。

先取仅第 $t$ 段非零的 $f^{[t]}\in\mathscr Y_{H,q}$，$2\le t\le d-1$。令 $\widetilde f_t=\Sigma_m^{-1}f_t$，并定义
$$
\boxed{
c_{t-k}^{[t]}
=(-1)^k\gamma_m^{-k-1}\Sigma_m
(J_d^*)^{k+1}D^k\widetilde f_t,
\qquad 0\le k\le t-2,
}
\tag{2.2}
$$
其他输入段为零。

逐项检查实际空间。令 $u=t-k$。$\widetilde f_t$ 的最大头指标为 $d-t-1$，应用 $(J_d^*)^{k+1}$ 后最大头指标为 $d-u$，故所得头在 $W_{d-u+1}$ 内，且没有越过有限头顶端。另外
$$
D^kE_{t-1,q+t}\subset E_{t-1-k,q+t-k}
=E_{u-1,q+u}.
$$
所以 $c_u^{[t]}\in\mathscr X_{H,q,u}$，全部相似和位移均在真实旗内。

在输出第 $t$ 段，没有头溢出给
$$
Ac_t^{[t]}=\Sigma_mJ_dJ_d^*\widetilde f_t=f_t.
$$
对 $2\le u<t$，置 $k=t-u$，则
$$
Ac_u^{[t]}
=(-1)^k\gamma_m^{-k}\Sigma_m(J_d^*)^kD^k\widetilde f_t
=-Dc_{u+1}^{[t]}.
\tag{2.3}
$$
第 $1$ 个内部输出也为零，因为
$$
Dc_2^{[t]}
=(-1)^{t-2}\gamma_m^{-(t-1)}
\Sigma_m(J_d^*)^{t-1}D^{t-1}\widetilde f_t=0.
\tag{2.4}
$$
这里准确用了 $f_t\in E_{t-1,q+t}$，没有删去最左端方程。输入首段为零，故 $F_qc^{[t]}=0$。输入末段 $d$ 也为零。

对任意 $f\in\mathscr Y_{H,q}$ 求和
$$
\mathcal Q_{H,q}f=\sum_{t=2}^{d-1}c^{[t]}.
$$
于是得到
$$
\boxed{
S_{H,q}\mathcal Q_{H,q}=I_{\mathscr Y_{H,q}},
\qquad F_q\mathcal Q_{H,q}=0.
}
\tag{2.5}
$$
该构造没有使用任何 $D^k$ 的逆。

## 3. 孔数无关的实际范数

按 (2.2) 的同一 $k$ 分组，输出段 $t$ 被送到输入段 $t-k$；这个段号映射是单射，所以组内正交平方和保留。由三角不等式，
$$
\boxed{
\|\mathcal Q_{H,q}\|
\le\Gamma_m
:=\kappa_m\sum_{k=0}^{d-3}
\gamma_m^{-k-1}\nu_m^k
\le d\kappa_m\gamma_m^{-(d-2)}.
}
\tag{3.1}
$$
全部常数与 $q$ 无关。尤其 $\bigoplus_{q\ge0}\mathcal Q_{H,q}$ 在对应外直和链空间上是有界右逆；这不把全尾 $D$ 的 Moore–Penrose 逆说成有界。

为给可直接使用的数值界，R249 §4 给
$$
\log\kappa_m\le L_m(d-1)-\omega_{d-1}
+d\log12+2\log d,
$$
$$
\omega_{d-1}=\frac{20}{3}d^4-15d^3
+(150m-275)d+\frac{850}{3}.
$$
代入 (3.1)，准确得到上界
$$
\begin{aligned}
\log\Gamma_m
\le{}&
\left(\frac{55}{3}+\frac{25}{2(d-2)}\right)d^4+15d^3\\
&-(150m-255-\log12)d-\frac{730}{3}+3\log d
<20d^4.
\end{aligned}
\tag{3.2}
$$
最后一步用 $d\ge32$：
$55/3+25/60+15/32<20$，第二行严格为负。因此
$$
\boxed{\|\mathcal Q_{H,q}\|\le e^{20d^4}
\quad\text{对所有 }q\ge0.}
\tag{3.3}
$$

## 4. 真正高块及两个 Schur 度量

令
$$
A_{H,q}=S_{H,q}S_{H,q}^*.
$$
由 $\mathcal Q_{H,q}^*S_{H,q}^*=I$，有
$\|S_{H,q}^*z\|\ge\Gamma_m^{-1}\|z\|$，所以
$$
\boxed{
A_{H,q}\ge\Gamma_m^{-2}I\ge e^{-40d^4}I.
}
\tag{4.1}
$$
这里是原空间中的真实伴随、真实正交范数。

沿原返回源笔记，设 $\mathscr X_L=\mathscr X_H^\perp$，
$S_L=P_{\mathscr Y_H^\perp}S|_{\mathscr X_L}$，
$Z=\ker S_L$，以及
$$
B=P_{\mathscr Y_H}S|_Z.
$$
出生数分解 $S=S^{(0)}+S^{(1)}$ 中，只有 $S^{(1)}$ 能把低输入送进高输出，故
$$
\|B\|\le\|D^{(1)}\|\le\nu_m.
\tag{4.2}
$$
注意 (4.2) 保留实际输出投影，不假设低输入的各低输出分别为零。

令 $\mathsf F=F|_Z$、$\mathcal N=\ker\mathsf F$、$R=\mathcal N^\perp\cap Z$、$B_R=B|_R$。旧末块与[首段先消元稿](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)的新末块准确为
$$
\mathcal H_2=A_H+BB^*,\qquad
\mathcal H_2^\circ=A_H+BP_{\mathcal N}B^*.
$$
因而两者都至少为 $\Gamma_m^{-2}I$。特别，真实低链与裸源上的两个正算子满足
$$
K=B^*A_H^{-1}B,\qquad
K_{\rm eff}=B_R^*(\mathcal H_2^\circ)^{-1}B_R,
$$
$$
\boxed{
0\le K,\ K_{\rm eff}\le k_m I,\qquad
k_m:=\nu_m^2\Gamma_m^2\le m^{-2}e^{40d^4}.
}
\tag{4.3}
$$
这些结论可以在每个固定 $q$ 的已知满射框架使用；(2.5)–(4.3) 的常数对全部 $q$ 相同。

## 5. 返回费用的明确范围

以下等式均指同一个窗口，并取可行源 $r\in\operatorname{Ran}\mathsf F$。令
$$
a=\mathsf F^\dagger r\in R,\qquad
c_L=\arg\min_{\mathsf Fc_L=r}\langle(I+K)c_L,c_L\rangle,
$$
$\lambda(r)$ 为完整最小修复范数，$r_{\rm ret}=\mathsf F Kc_L$。
首段先消元稿给
$$
\lambda(r)^2=\|a\|^2+\langle K_{\rm eff}a,a\rangle,\qquad
\mathsf F^\dagger r_{\rm ret}=K_{\rm eff}a,
$$
$$
\mathcal E_2
=\lambda(r)^2-\|a\|^2+\|K_{\rm eff}a\|^2.
\tag{5.1}
$$
因此对全部上述孔数及可行源，
$$
\boxed{
\mathcal E_2\le k_m\lambda(r)^2,\qquad
\lambda(r_{\rm ret})\le k_m\lambda(r).
}
\tag{5.2}
$$
第一式也可直接由
$\mathcal E_2=\langle Kc_L,c_L\rangle+\|Kc_L\|^2$
和 $K\le k_mI$ 得到。第二式用真正的低链候选 $Kc_L$：
其完成范数是 $\|(I+K)^{1/2}Kc_L\|$，由于 $K$ 与 $I+K$ 交换，该范数至多 $k_m\lambda(r)$。这里没有把返回源的裸范数代替完整修复费。

对实际 $r=r_{m,q}(w)$，若仍在旧合法范围
$4d\le q\le e^{d^3/4}$，首段先消元稿 §4 的
$$
\|a\|\le\beta_q(w)+e^{-72d^4}\|w\|
$$
还给明确但较粗的
$$
\lambda(r_{\rm ret})
\le k_m\sqrt{1+k_m}
\left(\beta_q(w)+e^{-72d^4}\|w\|\right).
\tag{5.3}
$$
例如 $k_m\sqrt{1+k_m}\le2e^{60d^4}$，所以 carry 部分至多
$2e^{-12d^4}\|w\|$。未来带系数仍为 $2e^{60d^4}$，没有被宣布为可忽略。

## 6. 与已有窗口结论的区别

旧 $D$ 递推在每个固定 $m,q$ 已给高链闭像；原合法窗口的同时右逆还可给更好的 $e^{d^4}$ 级常数。本稿新增的是 (2.2) 的无需删除逆的高旗构造，以及 (3.3)、(4.3)、(5.2) 对所有孔数使用同一个依赖 $m$ 的常数。它们不是旧合法窗口内更强的数值估计。

[固定头 Chebyshev 稿](R271-appendix-fixed-head-condition-and-uniform-window-convergence.md) 比较给定源的有限链与无限链最小能量；本文证明另一件事，即高出生内部输出的有界右逆。两个结果都没有消除有限头的条件数成本。

对于原 $w\in M\ominus N$，低截断、有限核提升及 $e^{-75d^4}$ 的距离估计继续使用其原窗口。本文没有把 $q$ 的上述代数全范围用于扩大该窗口，也没有证明 $J_{\rm left}=J_{\rm bare}$、$r^\flat=r_{\rm ret}$ 或移段源 $\rho_k$ 的这些身份。普通 ISP 与无权 $N=M$ 仍未完成。
