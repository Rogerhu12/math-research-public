# R271 附录：放大方差的完整逆 Gram 强极限、同实际来源的阻尼相干代表与远孔指数矩

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文保留原 N/Y 算子及全部物理源最小化。已付的原方差 $S_m$ 逆 Gram 强极限，可扩展到任意
$$
s_m\ge S_m,\qquad s_m\longrightarrow0.
$$
比例 $s_m/S_m$ 允许无界。新增强位数 $R_m$ 亦可任意变化；只要仍用 $s_m\ge S_m$，完整强头上的同一结论成立。进一步，完整 Gram 可以截到任意 $J_m\ge1$：这个逆仍强趋原 $P_M$，并不需要先支付全部头相似的环境条件数。

对应的物理阻尼代表精确保持原 $V_Q/K_Q$ 投影，在同一个 forcing 上有远孔指数矩、完整头幂预算和准确残量因式分解。它不是一般真核向量；小 $C f$ 或小残量尚未经过原受限右逆、帽返回和全局 carry 修复。本文不证明 $N=M$。

已付依据：

- [移动真实头 bosonic 投影及完整逆 Gram 强极限](../notes/2026-11-14-moving-true-head-bosonic-projections-and-inverse-gram-strong-limit-789f-next.md)，尤其 §§1、4、5；
- [同实际测试的相干代表及原 cut 身份](R271-appendix-same-actual-test-minimal-coherent-representative-and-exact-residual.md)，§§1--3；
- [精确相容 Bernoulli 塔及完整源最小化](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md)。

## 1. 原算子、完整 Gram 与共同空间

令 $T$ 为原 $T_N$ 或 $T_Y$，$M=\ker T$。原前 $m$ 位真实头记为 $A_m$，$d_m=2^m$。在原物理空间中
$$
L_m=A_m+D_{\ge m},\qquad
D_{\ge m}=\sum_{i\ge m}b_iE_i,\qquad b_i=(i+1)^{-2},
$$
$$
S_m=\sum_{i\ge m}b_i^2,\qquad
\|T-L_m\|\longrightarrow0.
\tag{1.1}
$$
这里 $A_m$ 包含全部原 carry 与 Y 型 Cayley 项。有限整数头是 $T$ 的不变子空间，$T$ 在其上的限制正是 $A_m$。

对 $s>0$ 定义真正的完整头矩阵
$$
H_m(s)=\sum_{j=0}^{d_m-1}\frac{(A_m^*)^jA_m^j}{s^j j!}\succeq I.
\tag{1.2}
$$
所有逆先在完整头上取，再嵌入物理空间。原已付定理是
$$
\iota_mH_m(S_m)^{-1}\iota_m^*\xrightarrow{\rm strong}P_M.
\tag{1.3}
$$

为保完整 Fock 域，令 $\mathcal F$ 为共同 bosonic Fock 空间，
$\mathcal X_m$ 为前 $m$ 位硬核、其后全 bosonic 的闭子空间。令
$$
a_{0,m}=S_m^{-1/2}\sum_{i\ge m}b_i a_i.
$$
在标准闭 annihilation 域上定义
$$
\mathcal C_{m,s}=A_m+\sqrt{s}\,a_{0,m}.
\tag{1.4}
$$
$A_m$ 有界且与尾作用对易，所以 (1.4) 闭。其完整核投影记作
$\mathcal P_{m,s}^{\rm B}$，作为共同 $\mathcal F$ 上的正交投影理解。

在集体模式与所有横向模式的分解中，准确参数化为
$$
\mathcal R_{m,s}h
=\sum_{j<d_m}\frac{(-A_m)^j(a_{0,m}^*)^j}{s^{j/2}j!}\,h,
\qquad h\in\ker a_{0,m}.
$$
按归一集体占据展开 $v=\sum_{j\ge0}v_j\otimes|j\rangle$，核方程逐项给
$$
v_{j+1}=-\frac{A_mv_j}{\sqrt{s(j+1)}}.
$$
因 $A_m^{d_m}=0$，所有核向量的正集体占据均截在 $j<d_m$。反之上述有限列全部在闭 annihilation 域内并满足核方程；横向分量可以任意，未删除任何零模。该有限列的完整 Gram 为 $H_m(s)\otimes I_{\rm transverse}$。因此对尾真空 forcing $\iota_mg$，
$$
\|\mathcal P_{m,s}^{\rm B}\iota_mg\|^2
=\langle H_m(s)^{-1}g,g\rangle.
\tag{1.5}
$$
这仍保留完整头 inverse；没有将它压到 $g$ 的原低头支持。

## 2. 可无界方差比例的强极限

### 定理 2.1

若 $s_m\ge S_m$ 且 $s_m\to0$，则
$$
\boxed{
\mathcal P_{m,s_m}^{\rm B}\xrightarrow{\rm strong}P_M
\quad\hbox{于共同 }\mathcal F,
}
\tag{2.1}
$$
$$
\boxed{
\iota_mH_m(s_m)^{-1}\iota_m^*
\xrightarrow{\rm strong}P_M
\quad\hbox{于原物理空间}.
}
\tag{2.2}
$$
$P_M$ 在 $\mathcal F$ 中按零延拓理解。没有要求 $s_m/S_m$ 有统一上界。

**证明。** 先固定有限物理支撑 forcing $f$。充分大 $m$ 后它是原头加尾真空。令
$v_m=\mathcal P_{m,s_m}^{\rm B}f$，$q_m=\|v_m\|^2=\langle f,v_m\rangle$。由 $s_m\ge S_m$，
$$
H_m(s_m)\preceq H_m(S_m),\qquad
q_m\ge\langle H_m(S_m)^{-1}f,f\rangle.
$$
所以 (1.3) 给
$$
\liminf_mq_m\ge\|P_Mf\|^2.
\tag{2.3}
$$

下面核对真正无界比例下的上界。每个弱收敛子列的极限都在
$\bigcap_\ell\mathcal X_\ell=\mathcal H$，因为 $m\ge\ell$ 时
$v_m\in\mathcal X_\ell$。取固定有限物理测试 $\xi$。充分大 $m$ 后它的尾为真空；因而
$\xi\in\operatorname{Dom}\mathcal C_{m,s_m}^*$，且尾 creation 仍是物理向量。准确有
$$
\|\mathcal C_{m,s_m}^*\xi-T^*\xi\|
\le
\|L_m^*\xi-T^*\xi\|
+|\sqrt{s_m}-\sqrt{S_m}|\,\|\xi\|
\longrightarrow0.
\tag{2.4}
$$
第二项使用归一尾模式在真空上的 creation 范数恰为 $1$，不把
$\sqrt{s_m/S_m}$ 单独当有界常数。由
$\langle v_m,\mathcal C_{m,s_m}^*\xi\rangle=0$，任意弱极限 $v$ 满足
$Tv=0$。

若沿子列 $q_m\to q$、$v_m\rightharpoonup v$，则
$$
q=\langle f,v\rangle=\langle P_Mf,v\rangle
\le\|P_Mf\|\|v\|
\le\|P_Mf\|\sqrt q.
$$
故 $q\le\|P_Mf\|^2$。结合 (2.3)，得到 $q=\|P_Mf\|^2$、
$v=P_Mf$，并由范数收敛得到强收敛。有限物理向量稠密且投影一致收缩，故该结论扩展到整个 $\mathcal H$。又
$\mathcal P_{m,s_m}^{\rm B}=\mathcal P_{m,s_m}^{\rm B}P_{\mathcal X_m}$，
而 $P_{\mathcal X_m}\to P_{\mathcal H}$ 强收敛，故扩展到整个共同 $\mathcal F$。

最后令 $\mathsf E_m=\iota_m\iota_m^*$ 为全部尾真空投影。准确压缩为
$$
\mathsf E_m\mathcal P_{m,s_m}^{\rm B}\mathsf E_m
=\iota_mH_m(s_m)^{-1}\iota_m^*.
$$
$\mathsf E_m\to I$ 在物理空间强收敛，遂得 (2.2)。证毕。

另有一个完全在原物理空间中的核对。对每个固定 $s>0$，
$$
\mathcal H_T(s)=\sum_{j=0}^{\infty}\frac{(T^*)^jT^j}{s^j j!}
$$
是有界正算子，且
$$
P_M\preceq\mathcal H_T(s)^{-1}
\preceq(I+T^*T/s)^{-1}\xrightarrow[s\downarrow0]{\rm strong}P_M.
$$
原头不变性给 $H_m(s)=\iota_m^*\mathcal H_T(s)\iota_m$，完整 inverse compression 因而给
$$
\iota_mH_m(s)^{-1}\iota_m^*
\preceq \mathsf E_m\mathcal H_T(s)^{-1}\mathsf E_m.
\tag{2.5}
$$
这独立确认了上界方向；(2.5) 不是压缩与取逆相等。

## 3. 任意强前缀，以及只到第一项的完整 inverse

令 $R_m\ge0$ 任意，置
$$
x_m=m+R_m,\quad
C_m=A_m+D_{[m,x_m)},\quad
h_m=d_m+R_m,\quad C_m^{h_m}=0.
$$
强头始终保留全部前 $x_m$ 位物理度量。仍假设
$$
s_m\ge S_m,\qquad s_m\to0.
\tag{3.1}
$$
对 $1\le J_m\le h_m-1$ 定义
$$
H_{C_m,J_m}(s_m)
=\sum_{j=0}^{J_m}\frac{(C_m^*)^jC_m^j}{s_m^j j!}.
\tag{3.2}
$$
固定有限物理 $f$ 视作前 $m$ 位 forcing、其后真空，记同一强头中的向量为 $g_m$。

则
$$
\boxed{
\iota_{x_m}H_{C_m,J_m}(s_m)^{-1}g_m
\longrightarrow P_M f
\quad\hbox{强收敛}.
}
\tag{3.3}
$$
特别 $J_m=1$ 合法。此处是整个 $2^{x_m}$ 维头的 inverse，没有删中间孔层或只保原 forcing 的坐标。

先证完整 $J=h_m-1$。在前 $x_m$ 位硬核、其后 bosonic 的共同环境上，考虑
$C_m+\sqrt{s_m}\,a_{0,x_m}$。其核包含
$$
\left\{
\sum_{j<d_m}
\frac{(-A_m)^ja\otimes\Omega_{[m,x_m)}
\otimes(a_{0,x_m}^*)^j\Omega}
{s_m^{j/2}j!}:a\in\mathcal H_{<m}
\right\}.
$$
因此它对 $f$ 的投影能量不小于
$\langle H_m(s_m)^{-1}f,f\rangle$，后者由定理 2.1 趋于 $\|P_Mf\|^2$。所有弱极限仍在物理空间；固定测试的伴随与 $T^*$ 之差不超过原
$\|L_m-T\|$ 项及 $|\sqrt{s_m}-\sqrt{S_{x_m}}|$ 项，均趋零。因此 §2 的弱极限与范数论证原样给完整强头核投影和 inverse 的强极限。

再令 $J_m\ge1$ 任意。完整 inverse 的次序给其 forcing 二次型下界。置
$$
a_m=H_{C_m,J_m}(s_m)^{-1}g_m,\qquad
q_m=\langle g_m,a_m\rangle.
$$
有 $\|a_m\|^2\le q_m\le\|f\|^2$ 及
$$
\|C_ma_m\|^2\le s_m q_m\longrightarrow0.
\tag{3.4}
$$
在原物理嵌入中，固定有限测试上 $C_m^*\to T^*$，因为
$C_m+D_{\ge x_m}=L_m$，而相应尾创建范数趋零。因此任意弱极限仍属 $M$。与 §2 同样的
$q\le\sqrt q\,\|P_Mf\|$ 上界和完整 inverse 的下界相合，得 (3.3)。

同时得到准确正能量
$$
\boxed{
\epsilon_m:=
q_m-\|a_m\|^2
=\sum_{j=1}^{J_m}\frac{\|C_m^ja_m\|^2}{s_m^j j!}
\longrightarrow0.
}
\tag{3.5}
$$
逐参数还有 $0\le\epsilon_m\le\|f\|^2/4$，因为对 $H\ge I$，
$H^{-1}-H^{-2}\preceq I/4$。强极限没有给 $\epsilon_m$ 的移动参数速率。

## 4. 同一实际来源的阻尼物理列

本节先固定任意真实强头 $C^h=0$、远尾起点 $x$，令
$$
D=D_x,\quad S=S_x,\quad
\omega_j=(D^*)^j\Omega,\quad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j(b^2).
$$
取 $s\ge S$、$1\le J<h$，置
$$
r=S/s\le1,\quad
H_J(s)=\sum_{j=0}^{J}\frac{(C^*)^jC^j}{s^j j!},\quad
a=H_J(s)^{-1}g,
$$
$$
\boxed{
f_{s,J}=\sum_{j=0}^{J}
\frac{(-C)^ja\otimes\omega_j}{s^j j!}.
}
\tag{4.1}
$$
这是物理有限远孔列；它通常不是交投影，也不是 $C+D$ 的真核向量。

设 $C=A_m+D_{[m,x)}$、$R=x-m$。对于原 $V_Q$，相同逐列低方程身份给
$$
P_{V_Q}(D^*)^ji_0=(-1)^j(P_{V_Q}i_0)(C^*)^j,
\qquad j\le Q-R.
$$
故若
$$
\boxed{Q\ge R+J,}
\tag{4.2}
$$
则
$$
\boxed{
P_{V_Q}f_{s,J}=P_{V_Q}i_0g,\qquad
P_{K_Q}f_{s,J}=P_{K_Q}i_0g.
}
\tag{4.3}
$$
其来源是
$P f_{s,J}=(Pi_0)H_J(s)a$，不是把新 $H_J$ 换成旧最小相干 Gram。
$f_{s,J}$ 支撑总尾孔 $\le R+J\le Q$。

于是原同一个
$$
u_g=(P_{V_Q}-P_{K_Q})i_0g
=(P_{V_Q}-P_{K_Q})f_{s,J}
\tag{4.4}
$$
完全保持；任何内部顶部和两端 partial 仍来自这个原 $u_g$。其他 joined/full 投影只要满足原逐列身份及其各自 cut 条件，同样保持，不能从 (4.2) 删除原内部窗口条件。

## 5. 全远孔指数矩与完整源缺陷

令
$$
E_j=\frac{\|C^ja\|^2}{s^j j!},\quad
q=\langle H_J(s)^{-1}g,g\rangle=\sum_{j=0}^J E_j,
$$
$$
\kappa_j=\frac{\sigma_j^2}{j!S^j}\le1.
$$
不同 $j$ 位于正交远孔层，并且准确有
$$
\boxed{\|(f_{s,J})_j\|^2=\kappa_j r^j E_j.}
\tag{5.1}
$$
所以当 $r>0$，
$$
\boxed{
\sum_{j=0}^J r^{-j}\|(f_{s,J})_j\|^2\le q\le\|g\|^2.
}
\tag{5.2}
$$
这是真实代表的向量范数指数矩，独立于 $h,J,m,R$；它不是将既有实际 $u_g$ 的标量行提升为范数行。进一步
$$
\|f_{s,J}-i_0a\|^2
\le r\epsilon,\qquad
\epsilon=q-\|a\|^2\le\|g\|^2/4,
\tag{5.3}
$$
$$
\|P_{\{N_>\ge k\}}f_{s,J}\|^2
\le r^k\epsilon\quad(k\ge1),
\qquad
\|f_{s,J}\|^2\le q.
\tag{5.4}
$$
例如在 (4.2) 下，
$$
\|f_{s,J}-u_g\|^2
=\|f_{s,J}\|^2-\|u_g\|^2
\le q-\|u_g\|^2.
\tag{5.5}
$$
这里的 $\epsilon$ 和全部 inverse 都由同一个 forcing $g$ 给出。

将 §3 的参数代入后，(3.3)、(3.5)、(5.3) 给
$$
\boxed{
f_{s_m,J_m}\longrightarrow P_Mf
\quad\hbox{于原物理 Hilbert 空间}.
}
\tag{5.6}
$$
事实上不必额外假设 $r_m\to0$。若 $r_m=S_{x_m}/s_m\to0$，则 (5.3) 还给独立于未知收敛速率的
$\|f_{s_m,J_m}-i_0a_m\|^2\le r_m\|f\|^2/4$。
未由 (5.6) 得到原 $K_Q$ 到全局 $N$ 的运输率。

## 6. 完整塔的头幂与准确正占据残量

本节先取完整 $J=h-1$，仍记 $f_s=f_{s,h-1}$。若 $r<1$，对每个整数 $k\ge1$，
$$
\begin{aligned}
\|C^kf_s\|^2
&\le s^k\sum_{j\ge0}r^j\frac{(j+k)!}{j!}E_{j+k}\\
&\le
\boxed{\frac{s^k k!}{(1-r)^{k+1}}\,\epsilon},
\end{aligned}
\tag{6.1}
$$
其中 $E_\ell=0$ 对 $\ell\ge h$，而
$\epsilon=\sum_{\ell\ge1}E_\ell$。最后使用
$\sum_{j\ge0}\binom{j+k}{k}r^j=(1-r)^{-k-1}$；这只是上确界的一个明确上界，没有独立拆开完整 inverse。

令真实远尾占据算子
$$
\mathcal W=\sum_{i\ge x}b_i^2n_i,\qquad 0\preceq\mathcal W\preceq S I.
$$
逐物理坐标有
$$
D\omega_j=j(S-\mathcal W)\omega_{j-1}.
$$
代入相同列并保 $C^h=0$，得到整列恒等式
$$
\boxed{
Df_s=-\frac{S-\mathcal W}{s}\,Cf_s,\qquad
(C+D)f_s=
\left[(1-r)I+\frac{\mathcal W}{s}\right]Cf_s.
}
\tag{6.2}
$$
系数 $(1-r)I+\mathcal W/s$ 是 $[0,1]$ 中的正收缩。因此
$$
\boxed{
\|Df_s\|\le r\|Cf_s\|,\qquad
\|(C+D)f_s\|^2
\le\|Cf_s\|^2
\le\frac{s}{(1-r)^2}\epsilon.
}
\tag{6.3}
$$
该残量没有被写成两个分别粗估的大项；它保留同一个 $Cf_s$ 和实际占据因子。

对于截断 $1\le J<h-1$，(6.2) 的 $D$ 身份只作用在远孔 $<J$ 的部分，最高层没有下一列。准确残量为
$$
(C+D)f_{s,J}
=\left[(1-r)I+\frac{\mathcal W}{s}\right]Cf_{s,J}
+\left[rI-\frac{\mathcal W}{s}\right]C(f_{s,J})_J.
\tag{6.4}
$$
两项在最高层合成 $C(f_{s,J})_J$，没有删 top。对 $r<1$，
$$
\boxed{
\|(C+D)f_{s,J}\|^2
\le\|Cf_{s,J}\|^2
\le
\left[\frac{s}{(1-r)^2}+\|C\|^2r^J\right]\epsilon.
}
\tag{6.5}
$$
第一项用 $E_{j+1}$，最后一层用
$\|C^{J+1}a\|\le\|C\|\|C^Ja\|$。这是实际截断 top 的单独费用，不是把完整塔预算移到截断列。

## 7. 尚未付清的原接口

本稿所用 $H_{C,J}(s)^{-1}$ 始终是全部强头的完整 inverse；因此强收敛与指数矩并未假设中间孔层 nuisance 消失。量词中的 $s_m\ge S_m$ 是保证下界的已付条件，不能改成任意 $s_m\ll S_m$ 后继续调用同一强极限。

新代表的远孔尾受 (5.2) 控制，但其强头零孔源 $a_m$ 可含全部 $R_m$ 个强位孔以及所有旧头反馈。它不具有未经证明的低物理孔支持，原 $P_{\widehat{\mathscr E}}$、普通右最小 lift 和 source-return 仍可能移动这些分量。

同样，(6.3)--(6.5) 的小残量不是到真核的距离。直接对 $Cf_s$ 乘 $D^\dagger$ 可能重新产生很大的 $s/S_x$ 成本，完整 $(C+D)$ 修复还需保持全部后继项。原 $V_Q/K_Q$ 的同源身份及原 $T$ 的 carry／同一 $w$ 导数条件都仍按各自实际窗口使用。本稿没有通过放大方差替换原算子或原真实源。
