# 移动真实头的完整 bosonic 核投影、可求和 carry 与有限头逆 Gram 强极限

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：下述完整 Hilbert 空间定理已证明。结论识别原 \(M=\ker T\) 的正交投影，没有证明 \(N=\overline{BM}=M\)，也没有将 bosonic 向量当作物理硬核向量。

## 0. 具体增量与依赖

[完整零占据稿](2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md) 已给固定真实头的完整 bosonic 核参数化与 \(\log C_m=O(m\log(m+1))\)。本稿把不同 \(m\) 放在同一个全 Fock 空间，证明：

\[
 P_{m+1}^{\rm B}\preceq P_m^{\rm B}+\delta_m I,
 \qquad \sum_{m\ge5}\delta_m<\infty,
 \qquad
 \boxed{P_m^{\rm B}\longrightarrow P_M\quad\hbox{强收敛}.}
 \tag{0.1}
\]

原物理有限头上的完整正矩阵

\[
 H_m=\sum_{j=0}^{2^m-1}
       \frac{(A_m^j)^*A_m^j}{S_m^j j!}
 \tag{0.2}
\]

因此有准确的有限头接口：

\[
 \boxed{\iota_m H_m^{-1}\iota_m^*
            \longrightarrow P_M\quad\hbox{强收敛于原物理空间}.}
 \tag{0.3}
\]

这里 \(\iota_m\) 把原前 \(m\) 位头以尾真空嵌入；没有头相似，也没有在取逆前压缩到不变源。

真实 carry 和头前缀来自
[原线性逐头提升](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)
§§1–2。旧
[原纯返回的对角头定位](2026-11-14-actual-pure-return-diagonal-head-localization-kernel-2220.md)
控制的是同一右端最小选择子的头尾；本稿没有把该未知尾费删除。固定 \(m\) 的零占据公式与移动 \(m\) 的投影极限亦不混同。

## 1. 一个共同的物理/Fock 环境

令

\[
 \mathcal F=\Gamma_{\rm s}(\ell^2(\mathbb N_0))
\]

为完整 bosonic Fock 空间，\(a_i,a_i^*\) 为标准 annihilation/creation。原物理空间 \(\mathcal H\) 等距识别为全部坐标占据均至多一的闭硬核子空间。对 \(m\ge5\)，令

\[
 \mathcal X_m
 =\left(\bigotimes_{0\le i<m}\mathbb C^2\right)
       \otimes\Gamma_{\rm s}(\ell^2(\{m,m+1,\ldots\})).
 \tag{1.1}
\]

因此 \(\mathcal X_{m+1}\subseteq\mathcal X_m\)，且
\(\bigcap_m\mathcal X_m=\mathcal H\)。

本稿同时适用原两个实际边界

\[
 T=\sum_{i\ge0}(i+1)^{-2}N_i
 \quad\hbox{或}\quad
 T=\sum_{i\ge0}(i+1)^{-2}Y_i.
\]

令 \(A_m\) 为原前 \(m\) 位的真实有限头；它包含全部低位 carry 和实际 Cayley 因子。置

\[
 d_m=2^m,\qquad b_i=(i+1)^{-2},\qquad
 S_m=\sum_{i\ge m}b_i^2,
\]
\[
 \mathcal B_m=\sum_{i\ge m}b_i a_i
       =\sqrt{S_m}\,a_{0,m},
 \qquad
 \mathcal C_m=A_m+\mathcal B_m
       \quad\hbox{于 }\mathcal X_m.
 \tag{1.2}
\]

\(\mathcal B_m\) 取标准闭 annihilation 域；\(A_m\) 有界并与它交换，故 \(\mathcal C_m\) 闭。定义

\[
 \mathcal K_m^{\rm B}=\ker\mathcal C_m\subseteq\mathcal X_m,
 \qquad P_m^{\rm B}=P_{\mathcal K_m^{\rm B}}
 \tag{1.3}
\]

为共同 \(\mathcal F\) 上的正交投影。

全物理 \(\mathcal H\) 包含在 \(\operatorname{Dom}\mathcal B_m\) 内，且其上 \(\mathcal B_m=D_m=\sum_{i\ge m}b_iE_i\)。这是完整零占据稿的闭域结论；也可由有限物理基向量逼近、\(\|D_m\|\le\sum_{i\ge m}b_i\) 和 \(\mathcal B_m\) 的闭性直接得到。

令 \(L_m=A_m+D_m\) 为原有界纯尾模型。已证实际估计为

\[
 \|T-L_m\|\le26\eta_{m-1},\qquad
 \|L_{m+1}-L_m\|\le52\eta_{m-1},
 \tag{1.4}
\]
\[
 -\log\eta_{m-1}
 =\frac{175}{2}d_m^4-\frac{315}{4}d_m^3+150d_m,
 \qquad
 \eta_{m-1}\le e^{-80d_m^4}\quad(m\ge5).
 \tag{1.5}
\]

差 \(L_{m+1}-L_m\) 只作用原前 \(m+1\) 位。因此 (1.4) 的第二条就是同一真实有限头差的范数界，而不是对一个 bosonic 扩张任意外推的界。

## 2. 完整 bosonic 算子的有界右逆

先取任意有限头 \(A^d=0\) 及 \(\mathcal B=\sqrt S\,a_0\)。在集体占据基上定义

\[
 \mathcal B^\dagger |n\rangle
      =\frac{|n+1\rangle}{\sqrt{S(n+1)}}.
\]

它是有界算子，像包含在 \(\operatorname{Dom}\mathcal B\)，并满足

\[
 \mathcal B\mathcal B^\dagger=I,\qquad
 \|(\mathcal B^\dagger)^k\|=\frac1{S^{k/2}\sqrt{k!}}.
 \tag{2.1}
\]

令

\[
 Q_{A,S}
 =\sum_{j=0}^{d-1}(-A)^j(\mathcal B^\dagger)^{j+1}.
 \tag{2.2}
\]

每项的像均在 \(\operatorname{Dom}\mathcal B\)。由头与尾交换，有限和逐项相消给

\[
 \boxed{(A+\mathcal B)Q_{A,S}=I.}
 \tag{2.3}
\]

这里是完整 bosonic 空间上的满射右逆，不是物理硬核空间上的右逆。它无需保持硬核。

记

\[
 C(A,S)=\sum_{j=0}^{d-1}\frac{\|A^j\|^2}{S^j j!},
 \qquad h_d=\sum_{j=1}^d\frac1j.
\]

Cauchy–Schwarz 连同 (2.1) 给

\[
 \begin{aligned}
 \|Q_{A,S}\|
 &\le\frac1{\sqrt S}
       \sum_{j<d}\frac{\|A^j\|}{S^{j/2}\sqrt{j!}\sqrt{j+1}}\\
 &\le\boxed{\sqrt{\frac{h_d C(A,S)}S}}.
 \end{aligned}
 \tag{2.4}
\]

特别，令 \(C_m=C(A_m,S_m)\)，并取

\[
 R_m=\sqrt{\frac{h_{d_m}C_m}{S_m}}.
 \tag{2.5}
\]

完整零占据稿已证明

\[
 C_m\le(k_m+e)\exp[k_m\tau_m+3\tau_m^{4/3}],
\]
\[
 k_m=\max(2m,16),\quad
 \tau_m=\log108+3\log(m+1),\quad
 S_m\ge\frac1{3(m+1)^3}.
 \tag{2.6}
\]

所以 \(\log R_m=O(m\log(m+1))\)。为使后续阈值明确，也可统一放宽为

\[
 \log C_m\le40m^2,\qquad
 \boxed{\log R_m\le22m^2\quad(m\ge5).}
 \tag{2.7}
\]

确实 \(\tau_m\le3m,\ k_m\le4m,\ k_m+e\le5m\)；
用 \(\tau_m^{4/3}\le\tau_m^2\) 得第一界。
再用 \(h_{d_m}\le1+m\log2\)、(2.6) 的 \(S_m\) 下界并吸收对数项即得第二界。

## 3. 相邻头的真正交集与一侧投影 gap

将第 \(m\) 位限制为硬核后，

\[
 \mathcal B_m=b_mE_m+\mathcal B_{m+1}
       \quad\hbox{于 }\mathcal X_{m+1},
\]

且两边域相同，因为 \(b_mE_m\) 有界。于是准确有

\[
 \mathcal K_m^{\rm B}\cap\mathcal X_{m+1}
 =\ker\left(A_m+b_mE_m+\mathcal B_{m+1}\right).
 \tag{3.1}
\]

记右边闭算子为 \(\widetilde{\mathcal C}_{m+1}\)，并记

\[
 F_m=A_{m+1}-(A_m+b_mE_m),\qquad
 \epsilon_m=52\eta_{m-1}.
\]

则

\[
 \mathcal C_{m+1}
 =\widetilde{\mathcal C}_{m+1}+F_m,\qquad
 \|F_m\|\le\epsilon_m.
 \tag{3.2}
\]

取 (2.2) 对新真实头给出的右逆 \(Q_{m+1}\)。有

\[
 \widetilde{\mathcal C}_{m+1}Q_{m+1}=I-F_mQ_{m+1}.
\]

由 (1.5)、(2.7)，\(\epsilon_mR_{m+1}<1/2\)。因此

\[
 \widetilde Q_{m+1}
 =Q_{m+1}(I-F_mQ_{m+1})^{-1}
\]

是 \(\widetilde{\mathcal C}_{m+1}\) 的真正有界右逆，且

\[
 \|\widetilde Q_{m+1}\|\le2R_{m+1}.
 \tag{3.3}
\]

对任意 \(v\in\mathcal K_{m+1}^{\rm B}\)，

\[
 v-\widetilde Q_{m+1}
          \widetilde{\mathcal C}_{m+1}v
 \in\mathcal K_m^{\rm B}\cap\mathcal X_{m+1}.
\]

故

\[
 \|(I-P_m^{\rm B})v\|
 \le2\epsilon_mR_{m+1}\|v\|.
 \tag{3.4}
\]

下面只用这条单侧距离，不假设两个核同维。若 \(P,Q\) 是任意正交投影且
\(\|(I-P)Q\|\le\rho\le1\)，则分解 \(x=Px+(I-P)x\) 给

\[
 \langle Qx,x\rangle
 \le\|Px\|^2+2\rho\|Px\|\|(I-P)x\|
                +\rho^2\|(I-P)x\|^2
 \le\langle Px,x\rangle+2\rho\|x\|^2.
\]

由 (3.4) 得

\[
 \boxed{
 P_{m+1}^{\rm B}\preceq P_m^{\rm B}+\delta_m I,
 \qquad
 \delta_m=4\epsilon_mR_{m+1}.
 }
 \tag{3.5}
\]

全部常数独立于尾的粒子数、出生和向量。按 (1.5)、(2.7)，

\[
 \delta_m\le
 \exp[-80d_m^4+\log208+22(m+1)^2]
 \le e^{-79d_m^4}\quad(m\ge5).
 \tag{3.6}
\]

最后一步使用
\(\log208+22(m+1)^2\le16^m=d_m^4\)；
在 \(m=5\) 已成立，左边的相邻增长比小于右边的 \(16\)。
因此

\[
 r_m:=\sum_{\ell\ge m}\delta_\ell
 \le2e^{-79d_m^4}.
 \tag{3.7}
\]

## 4. 极限存在且恰是原物理核

由 (3.5)，正算子

\[
 P_m^{\rm B}+r_m I
\]

随 \(m\) 递减，且由零下界控制。对每个向量的二次型单调收敛；极化及正算子的标准平方估计给其强极限。因 \(r_m\to0\)，\(P_m^{\rm B}\) 本身强收敛到某个 \(P_\infty\)。由一致有界性，

\[
 P_\infty^2=\operatorname*{s-lim}_m(P_m^{\rm B})^2=P_\infty,
 \qquad P_\infty^*=P_\infty.
\]

故极限仍是正交投影。

**首先证明 \(\operatorname{Ran}P_\infty\subseteq M\)。**
固定 \(x\in\mathcal F\)，置 \(x_m=P_m^{\rm B}x\to x_\infty\)。
每个固定 \(j\) 下，所有 \(m\ge j\) 的 \(x_m\) 都在 \(\mathcal X_j\)；
所以 \(x_\infty\in\bigcap_j\mathcal X_j=\mathcal H\)。

取任意有限物理支撑测试 \(g\)，并让 \(m\) 大到 \(g\) 的全部尾为真空。此时 \(g\in\operatorname{Dom}\mathcal C_m^*\)，且

\[
 \mathcal C_m^*g=A_m^*g+\mathcal B_m^*g
\]

完全位于物理空间。它正等于 \(L_m^*g\)：尾真空上 creation 不产生碰撞，头则是同一个真实有限头。因此由 (1.4)，

\[
 \mathcal C_m^*g\longrightarrow T^*g.
\]

利用 \(\mathcal C_mx_m=0\) 并取极限，

\[
 \langle x_\infty,T^*g\rangle
 =\lim_m\langle x_m,\mathcal C_m^*g\rangle=0.
\]

这类测试在原物理空间稠密，且 \(T\) 有界，所以 \(Tx_\infty=0\)。

**其次证明 \(M\subseteq\operatorname{Ran}P_\infty\)。**
对 \(w\in M\)，\(w\) 是完整物理硬核向量，故在
\(\operatorname{Dom}\mathcal C_m\)，而

\[
 \mathcal C_mw=L_mw=(L_m-T)w.
\]

完整右逆给真实候选

\[
 w-Q_{m}\mathcal C_mw\in\mathcal K_m^{\rm B}.
\]

因而

\[
 \|(I-P_m^{\rm B})w\|
 \le26R_m\eta_{m-1}\|w\|\longrightarrow0.
 \tag{4.1}
\]

故 \(P_\infty w=w\)。两方向合得

\[
 \boxed{P_\infty=P_M.}
 \tag{4.2}
\]

还保留两条不同方向的实际信息：

\[
 P_M\preceq P_m^{\rm B}+r_mI,\qquad
 \|(I-P_m^{\rm B})P_M\|
       \le26R_m\eta_{m-1}.
 \tag{4.3}
\]

它们不等价于 \(P_m^{\rm B}\to P_M\) 的算子范数收敛：bosonic 核中仍可能有在移动物理限制下消失的方向。本稿没有给出该反方向的统一速率。

## 5. 有限头逆 Gram 的准确强极限

令 \(P_{0,m}\) 为第 \(m\) 位之后集体模式的零占据投影；它保留全部横向模式。完整核由

\[
 \mathcal R_m h
 =\sum_{j<d_m}
   \frac{(-A_m)^j(a_{0,m}^*)^j}{S_m^{j/2}j!}\,h,
 \qquad h\in\ker a_{0,m},
 \tag{5.1}
\]

给出，且

\[
 \mathcal R_m^*\mathcal R_m
 =H_m\otimes I_{\rm transverse}.
 \tag{5.2}
\]

所以在完整共同环境上

\[
 P_m^{\rm B}
 =\mathcal R_m(H_m^{-1}\otimes I_{\rm transverse})\mathcal R_m^*.
 \tag{5.3}
\]

设 \(\mathsf E_m=\iota_m\iota_m^*\) 为原有限头加全部尾真空的投影。对任意头向量 \(f\)，

\[
 \mathcal R_m^*\iota_m f=f\otimes\Omega_{\rm transverse},
\]

因为所有正集体占据分量均与尾真空正交。因此

\[
 \boxed{
 \mathsf E_mP_m^{\rm B}\mathsf E_m
   =\iota_mH_m^{-1}\iota_m^*.
 }
 \tag{5.4}
\]

左边仅是投影的真实压缩；右边是完整头矩阵先取逆，再按尾真空嵌入。这里没有压缩与取逆交换。

\(\mathsf E_m\) 在原物理空间强收敛到 \(I_{\mathcal H}\)。
结合 (4.2) 和全部因子范数至多一，(5.4) 给 (0.3)。
特别，对固定有限头物理 \(f,g\)，充分大 \(m\) 后可在原有限头坐标直接计算

\[
 \langle P_Mf,g\rangle
   =\lim_{m\to\infty}\langle H_m^{-1}f,g\rangle.
 \tag{5.5}
\]

对角还满足来自 (4.3) 的可计算一侧余量

\[
 \langle P_Mf,f\rangle
 \le\langle H_m^{-1}f,f\rangle+r_m\|f\|^2.
 \tag{5.6}
\]

## 6. 与原稳定像问题的准确边界

本稿的有界右逆在完整 bosonic 空间上存在；物理硬核删除并无由此获得的完整满射逆。相邻头比较的中间核也先在同一完整 Fock 环境中取，再由所有物理位约束的极限识别原 \(M\)。

(0.3) 给原核投影的有限真实头逆 Gram 表示。它没有证明这些有限头压缩的像属于 \(N=\overline{BM}\)，没有把 bosonic 右逆输出提升为物理稳定向量，也没有给原合法移动孔窗口中的 \(\mu\)-角度速率。

具体地，真实 joined 同窗三费可以控制某个原源误差及其 bare/flat 费用；仍不能由这些费用自动推断原左费 \(\mu\) 或 \(L\)-内积。母窗口的 carry/物理提升量词亦未在本稿改变。后续必须继续支付同一实际源的物理角度或稳定像逼近，而不是把 (4.2) 改写为 \(N=M\)。
