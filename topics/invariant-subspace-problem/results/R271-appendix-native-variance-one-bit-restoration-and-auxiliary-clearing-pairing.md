# R271 附录：原方差一位 Schur 的完整恢复与辅助 mode 清零配对

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿直接在原连续尾方差 $S$ 下重算一位完整 Schur，不把大辅助方差的严格行收缩迁移到原模型。原投影源度量与每个删位 Gram 的比较仍有绝对常数，因而两种恢复反馈及指定的原权加权投影返回仍可付。另在共同 Fock 空间中给出辅助 mode 清零的准确投影损失，并将它送入保同一个原来源的整个一位投影交换配对。

这里的“无辅助 mode”不等于“所有远位已经硬核”：除指定的新增位外，完整 Schur 仍先在 bosonic 空间求解，再作同一个物理压缩。全部硬化、完整 MP 返回及 $N=M$ 仍未由本稿完成。

依据：[一位完整 Schur](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)、[正 commutator 因子](R271-appendix-one-bit-positive-commutator-and-complete-moving-source-occupation-row.md)、[原 coherent 同源列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)、[并行共同头恢复](R271-appendix-parallel-one-bit-schur-common-head-restoration-and-compressed-creation-row.md)、[真实创建合成](R271-appendix-adjoint-creation-synthesis-and-common-source-adjacent-flag-return.md)、[双恢复反馈](R271-appendix-one-bit-restored-adjoint-feedback-and-weighted-projection-return.md)。

## 1. 原方差、完整源和实际投影

保原 N/Y 模型共同的记号
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0,
$$
$$
b_i=(i+1)^{-2},\quad z_i=b_i^2,\quad
D=\sum_{i\ge x}b_iE_i,\quad S=\sum_{i\ge x}z_i.
$$
假设
$$
x\ge64,\qquad h\le2x,\qquad Q\ge R+h+1.
\tag{1.1}
$$
所有 $V_Q,K_Q,U_Q$、它们的正交投影及原强头真空嵌入 $i_0$ 都不换。记
$$
Z_E=P_Ei_0,\quad G_E=Z_E^*Z_E,\qquad E=V_Q,K_Q,U_Q.
$$

**本稿没有额外方差：** 旧方差就是 $S$，第 $i$ 位并头后的剩余方差为
$$
s_i=S-z_i>0,\quad p_i=z_i/S,\quad u_i=z_i/(S-z_i),
$$
$$
H=H_C(S),\quad H_i=H_C(s_i),\qquad
H_C(s)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{s^j j!}.
\tag{1.2}
$$
固定任意完整头 forcing $g$，令
$$
a=H^{-1}g,\quad q=\langle g,H^{-1}g\rangle,\quad
E_j=\frac{\|C^ja\|^2}{S^j j!},
$$
$$
\varepsilon=\sum_{j\ge1}E_j=q-\|a\|^2,\qquad
\mathfrak F_1=\sum_{j\ge1}jE_j.
\tag{1.3}
$$
各和实际止于 $h-1$，并有
$$
\mathfrak F_1\le(h-1)\varepsilon\le2x\varepsilon.
\tag{1.4}
$$

原物理 coherent 列 $\mathcal R_C(S)a$ 满足
$P_E\mathcal R_C(S)a=Z_EHa$、$\|\mathcal R_C(S)a\|^2\le\langle Ha,a\rangle$。因此
$$
G_E\preceq H^{-1}.
\tag{1.5}
$$
特别，其 $U_Q$ 投影是同一个 $u_{g,Q}=P_Ui_0g$，所以
$$
q\ge\|u_{g,Q}\|^2,\qquad
\boxed{\varepsilon\le\|g\|^2-q\le\Delta_{g,Q}^2},
\quad
\Delta_{g,Q}=\|i_0g-u_{g,Q}\|.
\tag{1.6}
$$
第一个不等式也直接来自 $0<H^{-1}\le I$。这里不要求 $g$ 只落在某个固定低头子空间。

## 2. 删除一位后的真实源度量比较

原尾积分比较给
$$
\frac1{3(x+1)^3}\le S\le\frac1{3x^3},
\qquad
p_{\max}=\frac{z_x}{S}\le\frac3{x+1},
\qquad
\sum_i p_i=1.
$$
在 (1.1) 下
$$
\frac{h p_{\max}}{1-p_{\max}}
\le\frac{6x}{x-2}<8.
\tag{2.1}
$$
设 $K_0=e^8$。逐项仅比较完整正幂 Gram 的标量系数，得到
$$
\boxed{
H\preceq H_i\preceq K_0H,\qquad
G_E\preceq H^{-1}\preceq K_0H_i^{-1}.
}
\tag{2.2}
$$
最后一个不等式是本稿与大辅助方差版本的关键区别。此处 $s_i<S$，不能沿用 $G_E\preceq H_i^{-1}$；(2.2) 是实际保留下来的恢复代价。

在共同全尾 Fock 中，旧闭核为 $C+a(b)$ 的核，其中 $a(b)=\sum_{i\ge x}b_i a_i$。第 $i$ 个新闭核再限制 $N_i\le1$。以 $q_{{\rm new},i}$ 记新投影平方，并置
$$
\ell_i=q-q_{{\rm new},i},\qquad
\gamma_i=q_{{\rm new},i}-\langle g,H_i^{-1}g\rangle .
$$
完整一位 Schur 给 $\ell_i,\gamma_i\ge0$。同一个非交换 inverse 差满足
$$
H^{-1}-H_i^{-1}
\preceq H^{-1}(H_i-H)H^{-1}.
$$
于是
$$
\ell_i+\gamma_i
\le\sum_{j=1}^{h-1}[(1-p_i)^{-j}-1]E_j.
$$
对 $j+1\le h$，
$$
(1-p_i)^{-j}-1
\le j p_i(1-p_i)^{-(j+1)}
\le K_0j p_i.
$$
对无限行使用非负有限部分和及 Tonelli，得
$$
\boxed{
\sum_{i\ge x}(\ell_i+\gamma_i)
\le K_0\mathfrak F_1
\le2K_0x\varepsilon.
}
\tag{2.3}
$$
没有重新选择参数，也没有把每个新源当成某个候选源。

## 3. 两种完整恢复反馈与首源方程

新头为 $C_i=C+b_iE_i$，其完整最小源记为
$(a_{0,i},a_{1,i})$。完整 Gram 仍准确为
$$
H_{C_i}(s_i)=
\begin{pmatrix}
H_i&(b_i/s_i)C^*H_i\\
(b_i/s_i)H_iC&
(1+u_i)H_i+(b_i^2/s_i^2)C^*H_iC
\end{pmatrix}.
\tag{3.1}
$$
令
$$
T_i=H_i^{1/2}CH_i^{-1/2}/\sqrt{s_i},
\qquad x_i=H_i^{1/2}a_{1,i}.
$$
正 commutator Schur 给
$$
\|x_i\|^2\le\gamma_i,\qquad \|T_i\|^2\le h-1.
\tag{3.2}
$$
后一个界来自原单 mode 等距核列的最高粒子数 $h-1$，不是环境 $\|C\|/\sqrt{s_i}$ 的粗界。

保两个不同次序的恢复源
$$
\sigma_i=\frac{b_i}{s_i}H_iCa_{1,i},\qquad
\alpha_i=\frac{b_i}{s_i}C^*H_i a_{1,i},
\qquad r_i=H_i a_{1,i}.
\tag{3.3}
$$
同一白化给
$$
H_i^{-1/2}\sigma_i=\sqrt{u_i}\,T_ix_i,\qquad
H_i^{-1/2}\alpha_i=\sqrt{u_i}\,T_i^*x_i.
$$
而 $u_i(h-1)\le8$。由 (2.2)--(2.3) 得对三个原投影同时成立的完整行预算
$$
\boxed{
\sum_i\|Z_E\sigma_i\|^2\le8K_0^2\mathfrak F_1,\qquad
\sum_i\|Z_E\alpha_i\|^2\le8K_0^2\mathfrak F_1,
}
\tag{3.4}
$$
$$
\boxed{\sum_i\|Z_Er_i\|^2\le K_0^2\mathfrak F_1.}
\tag{3.5}
$$
原首源方程仍为
$$
H_i a_{0,i}+\alpha_i=g,
$$
所以 (3.4) 也支付整个 $Z_E(H_i a_{0,i}-g)$ 行。没有交换 $C,H_i$ 或删去其中任何一种反馈。

## 4. 无辅助 mode 的指定实际投影返回

令 $F_i$ 为只硬化第 $i$ 位后的完整 Fock 投影的原物理压缩。它的 bit-$1$ 行由 $a_{1,i}$ 产生，因此
$$
\sum_i\|E_iF_i\|^2\le\sum_i\|x_i\|^2
\le K_0\mathfrak F_1.
\tag{4.1}
$$
原低 forcing 恒等式给
$$
\boxed{
P_EE_iF_i=Z_Er_i+P_EE_i^*i_0\sigma_i.
}
\tag{4.2}
$$
这里 $s_i<S$ 不妨碍代数身份。它只影响范数比较，已由 (2.2) 支付。

具体地，对 $j\le h$ 使用
$$
(D_{\widehat i}^*)^j-(-C_i^*)^j
=L_m^*\sum_{k=0}^{j-1}
(D_{\widehat i}^*)^{j-1-k}(-C_i^*)^k.
$$
中间来源的原总尾孔至多 $R+j\le Q-1$，故被原
$P_{V_Q}L_m^*$、$P_{K_Q}L_m^*$ 杀掉。再将完整新 Gram 作用于 $(a_{1,i},0)$，便是 (4.2)。没有使用 $V_Q$ 对单个 $E_i$ 或 $C_i$ 的未证不变性。

由 (3.5)、(4.1) 和 $\ell^2$ 行上的 Minkowski，
$$
\left(\sum_i\|P_EE_i^*i_0\sigma_i\|^2\right)^{1/2}
\le(\sqrt{K_0}+K_0)\sqrt{\mathfrak F_1}
\le2K_0\sqrt{\mathfrak F_1}.
\tag{4.3}
$$

对本稿指定来源定义
$$
\mathcal R_{E,i}
=P_EE_i^*i_0\sigma_i-E_i^*Z_E\sigma_i.
$$
旧真实创建合成对 $Z_V,Z_K$ 各有常数
$c_x=4/3+1/(x+1)\le5/3$，并且
$$
\sup_{i\ge x}b_i^2(i+1)=(x+1)^{-3}\le3S.
$$
因此对任意有限相位族 $|c_i|\le1$，
$$
\left\|\sum_i b_ic_iP_EE_i^*i_0\sigma_i\right\|
\le2K_0\sqrt{S\mathfrak F_1}.
$$
对另一项，$E=U_Q$ 时保 $Z_U=Z_V-Z_K$ 的两个来源，得
$$
\left\|\sum_i b_ic_i E_i^*Z_U\sigma_i\right\|
\le2\sqrt{24c_x}\,K_0\sqrt{S\mathfrak F_1}.
$$
$V_Q,K_Q$ 各自的界更小。于是
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_{i\ge x}b_ic_i\mathcal R_{E,i}\right\|
\le16e^8\sqrt{S\mathfrak F_1}
\le24e^8\sqrt{xS\varepsilon}
\le\frac{24e^8}{x}\Delta_{g,Q}.
}
\tag{4.4}
$$
这在原尾方差下保完整 Schur 和原物理投影，未从大辅助行收缩作任何外推。

第一个级数由 Cauchy 在绝对范数下收敛；第二个由创建合成的平方可和来源域收敛。有限部分和的尾界均趋零，所以 (4.4) 对无限尾、有界相位族及其绝对标量配对都合法。特别输出在 $Q+1$ 孔的部分没有被悄悄截掉。

## 5. 辅助 mode 清零的准确共同投影身份

本节允许任意 $t\ge0$，但不更换物理算子或原 forcing。对于 $t>0$，在同一个“原全尾 Fock 加一辅助 mode”的空间上令
$$
\mathscr M_t=\ker(C+a(b)+\sqrt t\,a_{\rm aux}),\qquad
\mathscr N=\mathscr M_t\cap\{N_{\rm aux}=0\}.
$$
两者都是闭子空间。$\mathscr N$ 正是无辅助 mode 的
$\ker(C+a(b))$ 张量辅助真空；它作为子空间不依赖 $t$。
对 $f=i_0g$ 以辅助真空嵌入，记
$v_t=P_{\mathscr M_t}f$、$v_0=P_{\mathscr N}f$。嵌套正交投影准确给
$$
\boxed{
\|v_t-v_0\|^2
=q_C(S+t)-q_C(S)
\le\Delta_{g,Q}^2.
}
\tag{5.1}
$$
最后一步使用 $q_C(S+t)\le\|g\|^2$ 和原
$q_C(S)\ge\|u_{g,Q}\|^2$。这不是在固定源 $a_t$ 上乘上 $(1+t/S)^j$ 来强行补偿方差；$v_0$ 包含原完整重新最小化。

只硬化第 $i$ 位时同样令
$$
\mathscr M_{i,t}=\mathscr M_t\cap\{N_i\le1\},\qquad
\mathscr N_i=\mathscr M_{i,t}\cap\{N_{\rm aux}=0\}.
$$
$\mathscr N_i$ 是无辅助 mode 的真实一位新核。以 $F_i(t),F_i(0)$ 记两个投影经同一“所有原位硬核、辅助真空”物理压缩所得的向量，则
$$
\boxed{
\|F_i(t)-F_i(0)\|^2
\le q_{{\rm new},i}(t)-q_{{\rm new},i}(0)
\le\Delta_{g,Q}^2.
}
\tag{5.2}
$$
平方等式只在两个完整 Fock 投影之间成立；物理压缩后仅保上界。
$q_{{\rm new},i}(0)\ge\|u_{g,Q}\|^2$ 来自同一个原低 forcing 身份，不能省略。

所有 annihilator 都用其闭自然域；$C$ 是有界扰动。对真空 forcing，collective/transverse 分解把未硬化核的非零 transverse 源正交消去；一位新核则先保完整两头源，再用剩余 collective mode。参与 (5.1)--(5.2) 的投影列因此均为有限次数多项式，严格属于上述自然域。该证明无需将非交换核投影互换，也没有把物理硬核投影视为核保持算子。

## 6. 保完整一位源包的加权清零

对每个 $t\ge0$，原低 forcing 门保持
$$
P_EF_i(t)=P_EF_i(0)=Z_Eg.
$$
定义完整的一位投影交换包
$$
\mathcal A_{E,i}(t)=P_EE_iF_i(t)-E_iZ_Eg.
\tag{6.1}
$$
这是完整 $[P_E,E_i]F_i(t)$；若展开它，必须一起保首恢复源和 creation 返回，不能只清零其中一个 Schur 块。其精确差为
$$
\mathcal A_{E,i}(t)-\mathcal A_{E,i}(0)
=P_EE_i[F_i(t)-F_i(0)].
$$
因为 $P_E,E_i$ 都为收缩、$\sum_{i\ge x}b_i\le1/x$，(5.2) 直接给
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_{i\ge x}b_ic_i
  [\mathcal A_{E,i}(t)-\mathcal A_{E,i}(0)]\right\|
\le\frac{\Delta_{g,Q}}x .
}
\tag{6.2}
$$
该和绝对范数收敛，对 $t=xS$ 亦成立，不乘未知来源条件数。

若需相邻原旗，可取 $Q\ge R+h+2$ 并定义
$$
\mathcal A^{\rm adj}_i(t)
=P_{U_{Q-1}}E_iF_i(t)-E_i u_{g,Q}.
$$
同一个差仍为
$P_{U_{Q-1}}E_i[F_i(t)-F_i(0)]$，故 (6.2) 的右端不变。这没有重新选择实际 $u_{g,Q}$，也没有假设 $P_{U_{Q-1}}$ 与 $E_i$ 对易。

## 7. 整个指定并行返回包的原权预算

对 $E=U_Q$，不仅 (4.4) 中的指定 $\sigma_i$ 部分，整个 (6.1) 都可估计。先由 (4.1) 和 Cauchy 得
$$
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_iP_UE_iF_i(0)\right\|
\le e^4\sqrt{S\mathfrak F_1}.
\tag{7.1}
$$
原固定 forcing 的删除弱行是
$$
\left(\sum_i
 \frac{|\langle E_i u_{g,Q},z\rangle|^2}{i+1}
\right)^{1/2}
\le\sqrt{\frac83}\,\Delta_{g,Q}\|z\|.
$$
将它与准确系数 $b_i\sqrt{i+1}\,c_i$ 配对，并使用
$$
\sum_{i\ge x}b_i^2(i+1)
=\sum_{i\ge x}(i+1)^{-3}
\le\frac1{2x^2},
$$
得到对整个实际来源的向量界
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_iE_i u_{g,Q}\right\|
\le\frac2{\sqrt3\,x}\Delta_{g,Q}.
}
\tag{7.2}
$$
这里没有把弱行升级为未付的 $\sum_i\|E_i u\|^2$ 范数行；仅以平方可和的明确系数作真实合成。

因此完整的一位包满足
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_i[P_U,E_i]F_i(0)\right\|
\le e^4\sqrt{S\mathfrak F_1}
+\frac2{\sqrt3\,x}\Delta_{g,Q}
\le\frac{e^4+2}{x}\Delta_{g,Q}.
}
\tag{7.3}
$$
最后一步保留 $\mathfrak F_1\le2x\varepsilon$、
$\varepsilon\le\Delta_{g,Q}^2$ 和 $S\le1/(3x^3)$。这是整个
$P_UE_iF_i(0)-E_i u_{g,Q}$，并非只估其中一个恢复源。

对 (6.2) 后的相邻包 $\mathcal A_i^{\rm adj}(0)$，第一半只把收缩 $P_U$ 换成 $P_{U_{Q-1}}$，第二半仍是同一个实际
$E_i u_{g,Q}$。因此在 $Q\ge R+h+2$ 时，(7.3) 原样成立。全部原 $K$ 反馈仍在这个向量中；没有靠相邻配对把它单独删去。

以上级数按先有限和、再对应的 Cauchy 或弱行合成自然域取极限；界对全部有限相位族一致且其尾界趋零。因此它也是实际无限尾的向量范数及绝对标量配对预算。

## 8. 已付范围与尚未清除的辅助量

(4.4) 支付了无辅助 mode 的指定恢复来源；(5.1)--(6.2) 支付了完整一位投影交换包从辅助模型到无辅助模型的实际配对代价；(7.3) 又直接支付整个 native 并行返回包的原权向量范数。三者都保同一个原 $V_Q/K_Q/u_{g,Q}$。

原方差下的两反馈行不再具有大辅助方差模型的 $36/x$ 收缩：本稿只给 (3.4) 的真实 $\mathfrak F_1$ 预算。不能据此拼成全部顺次返回词。即使清零辅助 mode，尚未硬化的远位仍有 bosonic 自由度；将所有这些约束加入后，完整源会再次最小化。所有硬核约束与核条件的正交投影也不能免费互换。特别，(7.3) 是原物理范数中的加权界；它的输入还没有被证明落在原完整返回的最小残量逆上具有相同费用。原 Moore--Penrose／帽返回度量中的运输、所有部分旗的共同控制及 $N=M$ 仍须另证。
