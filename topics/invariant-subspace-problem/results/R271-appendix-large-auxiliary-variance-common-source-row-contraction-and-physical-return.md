# R271 附录：大辅助方差下共同完整源的反馈行收缩及物理返回

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 在原允许的方差自由度中确定取 $t=xS$，不按 forcing 或远位选参。所有并行一位反馈仍作用于同一个原强头。完整 $H_i$ 与共同 $H_0$ 的比较具有接近 $1$ 的常数，两种恢复反馈因此在同一个 $H_0^{-1}$ 度量中形成严格的无限行收缩。另保同一实际 source 的全部正高度能量，得到物理占据、完整恢复与指定投影返回的 $O(x^{-1})$ 平方预算。

最后的树界只适用于这些固定 $C,H_0$ 的真实头算子；本文没有把顺次硬化后的不同头、原全部 MP 返回或未证的源拼合算子等同于这棵树。

依赖：[一位完整 Schur](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)、[正 commutator 因子](R271-appendix-one-bit-positive-commutator-and-complete-moving-source-occupation-row.md)、[并行共同头恢复](R271-appendix-parallel-one-bit-schur-common-head-restoration-and-compressed-creation-row.md)、[双恢复反馈](R271-appendix-one-bit-restored-adjoint-feedback-and-weighted-projection-return.md)、[原 coherent 同源列](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)。

## 1. 确定参数与同一完整源度量

沿原记号取
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad
h=d+R,\quad C^h=0,
$$
$$
b_i=(i+1)^{-2},\quad z_i=b_i^2,\quad
D=\sum_{i\ge x}b_iE_i,\quad S=\sum_{i\ge x}z_i.
$$
要求
$$
x\ge64,\qquad h\le2x,\qquad Q\ge R+h+1 .
\tag{1.1}
$$
所有 $V_Q,K_Q,U_Q$ 及其投影仍为原模型的实际空间。$i_0$ 是原强头张量远尾真空的嵌入，$Z_E=P_Ei_0$、$G_E=Z_E^*Z_E$，$E=V_Q,K_Q,U_Q$。

确定地选择
$$
t=xS,\qquad s_0=S+t=(x+1)S,\qquad
s_i=s_0-z_i,
$$
$$
H_0=H_C(s_0),\quad H_i=H_C(s_i),\quad
G_0=H_0^{-1},\quad
p_i=z_i/s_0,\quad u_i=z_i/s_i .
\tag{1.2}
$$
$G_0$ 是本稿共同源度量，不是原 graph 中另有既定含义的 $G$。
此选择对所有 forcing、远位及后续 cut 都相同。

原尾和给
$$
\frac{z_x}{S}\le\frac3{x+1},\quad
p_{\max}\le\frac3{(x+1)^2},\quad
s_i\ge xS,\quad
\sum_i u_i^2\le\frac{z_x}{x^2S}
\le\frac3{x^2(x+1)} .
\tag{1.3}
$$
又
$$
\frac{h p_{\max}}{1-p_{\max}}\le\frac6x.
$$
由于 $H_C$ 是全部正幂 Gram 的和，逐项只比较标量系数可得
$$
\boxed{H_0\preceq H_i\preceq e^{6/x}H_0.}
\tag{1.4}
$$
这一步没有交换任何逆和压缩，也没有估 $H_0$ 的环境 condition number。

标准 $R=d,x=m+d$ 给 $h=2d\le2x$；$Q\ge4d$ 在原大 $m$ 范围内满足 (1.1)。并且 $s_0\le(x+1)/(3x^3)\to0$。所以这是原已允许的方差选择，未改变实际来源的 support 门或 carry 母窗。

## 2. 保同一实际源的增益与损失

固定任意完整头 forcing $g$，令
$$
a=H_0^{-1}g,\qquad
E_j=\frac{\|C^ja\|^2}{s_0^j j!},\qquad
q_0=\langle g,H_0^{-1}g\rangle,
$$
$$
\varepsilon_0=\sum_{j=1}^{h-1}E_j
=q_0-\|a\|^2.
\tag{2.1}
$$
由 $0<G_0\le I$，有
$$
\varepsilon_0\le\|g\|^2-q_0.
$$
完整 coherent 同源身份又给 $q_0\ge\|u_{g,Q}\|^2$，故
$$
\boxed{\varepsilon_0\le\Delta_{g,Q}^2.}
\tag{2.2}
$$
这不需要 forcing 固定在某个旧低维子空间。

在共同 Fock 中，记旧投影平方为 $q_0$，只将第 $i$ 位硬化的新投影平方为 $q_{{\rm new},i}$，并设
$$
q_i=\langle g,H_i^{-1}g\rangle,\quad
\ell_i=q_0-q_{{\rm new},i},\quad
\gamma_i=q_{{\rm new},i}-q_i .
$$
真实闭核包含给 $\ell_i,\gamma_i\ge0$，且
$\ell_i+\gamma_i=q_0-q_i$。

非交换 inverse 差保持准确方向：
$$
H_0^{-1}-H_i^{-1}
\preceq H_0^{-1}(H_i-H_0)H_0^{-1}.
\tag{2.3}
$$
例如将 $H_i-H_0$ 用 $H_0^{-1/2}$ 白化后，(2.3) 就是
$K(I+K)^{-1}\le K$。因此
$$
q_0-q_i
\le\sum_{j=1}^{h-1}[(1-p_i)^{-j}-1]E_j.
$$
而
$$
(1-p_i)^{-j}-1
\le j p_i(1-p_i)^{-(j+1)}
\le(h-1)p_i e^{6/x}.
$$
使用 $\sum_i p_i=1/(x+1)$、$h\le2x$ 和
$e^{6/x}\le4/3$，得到整个无限行
$$
\boxed{
\sum_i(\ell_i+\gamma_i)
\le\frac83\,\varepsilon_0
\le3\varepsilon_0.
}
\tag{2.4}
$$
这里不需要再作参数平均。

一位已付的完整候选投影损失还给
$$
\ell_i\le\sum_j j(j-1)p_i^2(1-p_i)^{-j}E_j.
$$
所以
$$
\boxed{
\sum_i\ell_i
\le e^{6/x}h(h-1)
       \left(\sum_i p_i^2\right)\varepsilon_0
\le\frac{16}{x}\,\varepsilon_0 ,
}
\tag{2.5}
$$
其中
$\sum_i p_i^2\le3/(x+1)^3$。所有无限和均由非负有限部分和及这些上界定义。

## 3. 两个完整恢复反馈算子

对每个远位，仍取新头 $C_i=C+b_iE_i$ 的完整源
$(a_{0,i}(g),a_{1,i}(g))$。记
$$
T_i=H_i^{1/2}CH_i^{-1/2}/\sqrt{s_i},\quad
\mathcal K_i=I+T_i^*T_i-T_iT_i^*\succeq0,
\quad \mathcal R_i=(I+u_i\mathcal K_i)^{-1}.
$$
完整正 Schur 给
$$
x_i:=H_i^{1/2}a_{1,i}
=-\sqrt{u_i}\,\mathcal R_iT_iH_i^{-1/2}g,
\qquad \|T_i\|^2\le h-1,\quad\|\mathcal R_i\|\le1.
\tag{3.1}
$$
$\|x_i\|^2\le\gamma_i$。

定义原共同头上的线性算子
$$
\mathsf A_i g=\alpha_i
=\frac{b_i}{s_i}C^*H_i a_{1,i}(g),
\qquad
\mathsf S_i g=\sigma_i
=\frac{b_i}{s_i}H_i C a_{1,i}(g).
\tag{3.2}
$$
完整第一行仍是 $H_i a_{0,i}=g-\alpha_i$。白化后，
$$
H_i^{-1/2}\alpha_i
=-u_iT_i^*\mathcal R_iT_iH_i^{-1/2}g,
$$
$$
H_i^{-1/2}\sigma_i
=-u_iT_i\mathcal R_iT_iH_i^{-1/2}g.
\tag{3.3}
$$
它们不是同一个算子；尤其后一项不是前一项的自伴替代。

由 (1.4)，输出源范数和输入源范数分别满足
$$
G_0\preceq e^{6/x}H_i^{-1},\qquad
H_i^{-1}\preceq G_0 .
$$
将 (3.3) 的完整次序保留，得到对每个 $g$
$$
\|\mathsf A_i g\|_{G_0}^2,\ 
\|\mathsf S_i g\|_{G_0}^2
\le e^{6/x}u_i^2(h-1)^2\|g\|_{G_0}^2 .
$$
据 (1.3) 求和，便有整个共同源算子不等式
$$
\boxed{
\sum_{i\ge x}
\left(\mathsf A_i^*G_0\mathsf A_i+
      \mathsf S_i^*G_0\mathsf S_i\right)
\preceq
\frac{24e^{6/x}}{x+1}G_0
\preceq\frac{36}{x}G_0.
}
\tag{3.4}
$$
$x\ge64$ 时最后的常数严格小于 $1$。没有改变 $H_0$ 的度量，也没有使用其可能很大的环境条件数。

另以 (2.4) 保原实际能量，而不是只用 $\|g\|_{G_0}$，可得
$$
\sum_i\|Z_E\alpha_i\|^2,\ 
\sum_i\|Z_E\sigma_i\|^2
\le\frac6x\sum_i\|x_i\|^2
\le\frac{16}{x}\varepsilon_0,
\qquad E=V_Q,K_Q,U_Q.
\tag{3.5}
$$
这使用 $G_E\preceq H_i^{-1}$，是完整物理恢复后的行。
$Z_E(H_i a_{0,i}-g)=-Z_E\alpha_i$ 也受同一预算。

## 4. 固定共同模型中的全部反馈词

取字母表
$$
\mathcal A=\{(i,A),(i,S):i\ge x\},
$$
分别对应 $\mathsf A_i,\mathsf S_i$。对长度 $k$ 的字 $w$，令
$\mathsf F_w$ 为相应有序乘积，且空字为恒等。
反复使用同一个 (3.4) 并对非负平方和作 Tonelli，得到
$$
\boxed{
\sum_{|w|=k}\|\mathsf F_w g\|_{G_0}^2
\le\left(\frac{36}{x}\right)^k\|g\|_{G_0}^2
\qquad(k\ge0).
}
\tag{4.1}
$$
故这个固定共同源上的整棵平方能量树可求和，常数
$(1-36/x)^{-1}$。

(4.1) 不把无权求和的全部向量词视为一个自动收敛的 Neumann 级数；若另有合并这些分支的算子，其准确范数仍须支付。尤其，逐位真正硬化会改变 $C_i$、nilpotency 和完整 Gram；那些变化后的反馈不是 (4.1) 中固定 $C,H_0$ 的词，除非另证真实运输。原 MP／返回递推也尚未被证明具有这套固定字表示。

## 5. 公共物理代表与首恢复源也获得 x^{-1} 预算

令 $F_0$ 为旧共同 Fock 投影的物理压缩，$F_i$ 为只硬化第 $i$ 位的新投影的相同物理压缩。完整共同核包含及物理收缩给
$$
\sum_i\|F_i-F_0\|^2\le\sum_i\ell_i
\le\frac{16}{x}\varepsilon_0.
\tag{5.1}
$$
$F_0$ 的第 $j$ 个远孔层满足
$$
\|(F_0)_j\|^2=\kappa_j(S/s_0)^jE_j,\qquad0<\kappa_j\le1.
$$
令 $r=S/s_0=1/(x+1)\le1/2$，则对所有 $j\ge1$，
$j r^j\le r$。所以
$$
\boxed{
\sum_i\|E_iF_0\|^2
=\sum_j j\|(F_0)_j\|^2
\le\frac{\varepsilon_0}{x+1}.
}
\tag{5.2}
$$
在整个 $\ell^2$ 行上使用 Minkowski，而非逐列后乘位置数，得到
$$
\boxed{
\sum_i\|E_iF_i\|^2\le\frac{25}{x}\varepsilon_0.
}
\tag{5.3}
$$

首恢复源记为 $r_i=H_i a_{1,i}$。为估其真正物理投影，使用全远尾 coherent 列，而不退回环境 $H_i$ 范数。令 $\mathcal R_{\widehat i,s_i}$ 是删去第 $i$ 位的 coherent 列。原二项式展开准确给
$$
\mathcal R_{s_i}a_{1,i}
=
E_iF_i-\frac{b_i}{s_i}E_i^*
 \mathcal R_{\widehat i,s_i}Ca_{1,i}.
\tag{5.4}
$$
右边两项分别在第 $i$ 位的 $0/1$ 扇区，物理正交。第二项的平方不超过
$$
\frac{b_i^2}{s_i^2}
\langle H_iCa_{1,i},Ca_{1,i}\rangle
=u_i\|T_ix_i\|^2 .
$$
用 (2.4) 求和，该项总量至多 $16\varepsilon_0/x$。由于
$P_E\mathcal R_{s_i}a_{1,i}=Z_Er_i$，(5.3)--(5.4) 给
$$
\boxed{
\sum_i\|Z_Er_i\|^2\le\frac{41}{x}\varepsilon_0,
\qquad E=V_Q,K_Q,U_Q.
}
\tag{5.5}
$$
这是首完整恢复源的新物理预算；并未声称
$\sum_i\|H_i^{1/2}a_{1,i}\|^2$ 本身具有相同的 $x^{-1}$ 因子。

## 6. 指定实际投影返回的加强

完整新头和原低 forcing 门保持精确式
$$
P_EE_iF_i=Z_Er_i+P_EE_i^*i_0\sigma_i.
$$
据 (5.3)、(5.5)，有
$$
\left(\sum_i\|P_EE_i^*i_0\sigma_i\|^2\right)^{1/2}
\le(5+\sqrt{41})\sqrt{\varepsilon_0/x}
<12\sqrt{\varepsilon_0/x}.
\tag{6.1}
$$
另由 (3.5)、真实创建合成及
$\sup_i b_i^2(i+1)\le3S$，$U_Q$ 版本满足
$$
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_i E_i^*Z_U\sigma_i\right\|^2
\le192c_x S\varepsilon_0/x
\le320 S\varepsilon_0/x,
$$
其中 $c_x=4/3+1/(x+1)\le5/3$。$V_Q,K_Q$ 各自的常数更小。
结合 (6.1) 的原权 Cauchy，便有
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_i
 \left[P_EE_i^*i_0\sigma_i-E_i^*Z_E\sigma_i\right]\right\|
\le30\sqrt{\frac{S\varepsilon_0}{x}},
\quad E=V_Q,K_Q,U_Q.
}
\tag{6.2}
$$
所有来源均为 (3.2) 指定的完整 Schur 源。第一项的级数按绝对范数收敛，第二项在已付创建源行的平方可和自然域中收敛，故无限尾及有界相位族都合法。

## 7. 与原来源及剩余闭合门的关系

本稿的 $t=xS$ 是确定的原允许方差，$C,H_0$ 及所有头算子不依赖 $g$ 或后续 cut。完整低 forcing 恒等式继续使全部物理 $F_i,F_0$ 投影为同一个原 $u_{g,Q}$。特别，(2.2) 将 (3.5)、(5.5)、(6.2) 的实际能量接到原缺陷，未添加未知恢复速率。

已经获得的是完整共同头的严格反馈行收缩，以及这些指定来源的实际物理返回预算。未完成的识别是：原全部顺次 MP 返回、相邻投影反馈或顺次硬化过程，是否真的能由 (4.1) 这套固定模型反馈词和一个已付的分支合并算子表示。不能因树的平方能量收缩，就删除不同头之间的 Schur、真实高旗或完整零源。普通 $N=M$ 仍未证明。

辅助方差 $t=xS$ 占总方差 $x/(x+1)$，始终不是原物理尾的一部分。本稿的行收缩只处理真实远位的一位反馈；若某个后继需要移除辅助 mode 或把其方差降到零，必须另证该步骤的实际来源、投影及完整返回费用，不能从 (4.1) 自动推出。
