# R244 后续附录：最小有限秩的逐分母湮灭与正 Koszul 零商同构

日期：2026-11-13（UTC）。作者：normal_resume_1cf；Astra-ISP-1cf8c51d 已核查最小秩转换、删除/插入链、全部商投影、真实单射消因子及有界同构。

状态：已证明，完整有限秩推导。对秩最小的正慢理想见证及全部谱向量的广义预解数据，证明每个单独预解子在一个明确的循环 S 零商上都为零；因而此前只在秩二成立的有界等价正化扩展到任意有限秩。没有声称这些预解子在整个共同交域商都为零，没有声称共同最小图等于最大交域。

## 1. 最小秩的两种定义确实相同

固定本题实际慢算子 S，$\mathfrak C=A'$。所有有界交换子都由 R88 的有界强多项式网逼近，故本文可以等价地用 $S\mathcal A$ 或 $S\mathfrak C$ 的有限秩湮灭条件。

先完整重述 [R228A §1](R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md) 所用的秩等价。若有限秩泛函
$
 \psi(F)=\sum_{j=1}^k\langle Fv_j,w_j\rangle,\qquad
 \psi(S\mathfrak C)=0,\quad \psi(I)\ne0,
$
令 $v=(v_j)$、$w=(w_j)\in H^{(k)}$，并取
$
 M=\overline{\mathfrak C^{(k)}v},\qquad
 N=\overline{S^{(k)}M}.
$
这里 $\overline{\mathfrak C^{(k)}v}$ 指全部对角交换子轨道的闭线性空间。S 属于代数并与全部 F 交换，故 $N\subset M$；w 与 N 正交而 $\langle v,w\rangle\ne0$，所以 $Q=M\ominus N\ne0$。

任取 $0\ne q\in Q$，有
$
 \langle(SF)^{(k)}q,q\rangle=0\qquad(F\in\mathfrak C),
$
因为 $F^{(k)}q\in M$、$S^{(k)}M\subset N$。于是
$\sum_jq_j\otimes q_j$ 是秩至多 k 的非零正见证。反方向正见证本来就是一般有限秩泛函，因此
$
 \boxed{\min\operatorname{rank}(\hbox{一般分离泛函})
       =\min\operatorname{rank}(\hbox{正分离泛函}).} \tag{1.1}
$

以下选正见证
$
 \rho=\sum_{i=1}^r f_i\otimes f_i,\qquad
 \tau=\sum_i\|f_i\|^2>0,\qquad \phi(S\mathfrak C)=0,
 \quad \phi(F)=\sum_i\langle Ff_i,f_i\rangle,
$
使 r 达到 (1.1) 的最小值。真秩一见证的原乘子已有 R244 的空广义预解结论；本文讨论 $r\ge2$ 且每行都给定广义预解数据的情形。

最小性还给一个以后会用到的直接事实：在任何实际 $H^{(k)}$ 的闭旗子商中，若 $k<r$，每个闭的对角交换子不变子空间 Y 都满足
$
 \overline{S_Y Y}=Y. \tag{1.2}
$
否则非零 $q\in Y\ominus\overline{S_YY}$ 的原 k 个坐标就给正秩至多 k 的见证。这里对旗子商使用压缩的代数表示，乘法等式正确；与 q 配对的压缩等于原 $H^{(k)}$ 配对。没有把全 H 的 S 稠密像直接传给商。

## 2. 广义预解给共同交域的有界模型

令 $M_i=X_{Cf_i}$ 为原最小闭乘子，并取
$
 R_i=(M_iU_i+B_i)^{-1}\in\mathfrak C,\qquad
 U_i\in\mathfrak C^\times,\quad
 D_i=M_iR_i\in\mathfrak C.
$
这里 $B_i=F_i-\lambda_iI$，符号表示 $\lambda_i$ 确在相应广义算子的预解集。所有 R_i 单射，范围恰为 $\operatorname{Dom}M_i$，且
$
 U_iD_i+B_iR_i=I. \tag{2.1}
$
置
$
 R=\prod_iR_i,\quad P_i=\prod_{j\ne i}R_j,\quad
 x_i=Cf_i,\quad g_i=U_ix_i+B_i1.
$
真实域交换及逆等式给
$
 R_ix_i=D_i1,\qquad R_ig_i=1,\qquad D_ig_i=x_i. \tag{2.2}
$
定义
$
 d_Rh=(P_i h)_{i=1}^r,\qquad
 K_R=\{y\in H^{(r)}:R_iy_i=R_jy_j\ (i,j)\},
$
$
 N_R=\overline{\operatorname{Ran}d_R},\qquad
 Q_R=K_R\ominus N_R.
$
所有空间为实际闭不变旗，记其商表示为
$\pi_R(F)=P_{Q_R}F^{(r)}|_{Q_R}$。

K_R 是共同最大交域图的有界坐标实现：对 $y\in K_R$，令 $v=R_iy_i$，则 v 属于每个原 $\operatorname{Dom}M_i$，且 $M_iv=D_iy_i$；逆变换取 $y_i=(M_iU_i+B_i)v$。N_R 对应共同乘积 R 正则化的闭图。并未把 K_R 认成共同最小图。

真正态给
$
 h=\sum_iD_iP_i f_i=0. \tag{2.3}
$
为明确来源，$RH\subset\bigcap_i\operatorname{Dom}M_i$，所以 h 是 $\sum_iM_iRf_i$ 的实际 H 向量。对全部 F，
$
 B(FSh,1)=\sum_i\langle FSRf_i,f_i\rangle=\phi(SRF)=0.
$
原 1 循环及 S 单射遂给 (2.3)。

令 $g=(g_i)$、$z=(D_i^*Cf_i)$。由 (2.2)--(2.3)，
$
 g\in K_R,\quad z\perp N_R,\quad
 \langle g,z\rangle=\tau.
$
因此 $Q_R\ne0$，且对
$q=P_{Q_R}g$、$z_R=P_{Q_R}z$，
$
 \boxed{\phi(F)=\langle\pi_R(F)q,z_R\rangle,\qquad
        \langle q,z_R\rangle=\tau.} \tag{2.4}
$
这一步用 $\langle FCf_i,Cf_i\rangle=\langle Ff_i,f_i\rangle$，即 R228 已证 C 对称泛函恒等式。

先保留一个准确的全商结论：
$
 \pi_R(P_i)=0. \tag{2.5}
$
若 $y\in K_R$，令 $t=R_jy_j$，则逐坐标有
$P_i^{(r)}y=d_R y_i$。例如 j≠i 时
$P_i y_j=(\prod_{k\ne i,j}R_k)R_jy_j
       =(\prod_{k\ne i,j}R_k)R_iy_i=P_jy_i$。
r=2 时这杀掉每个单独 R_i；r>2 时 (2.5) 本身不允许这样改写。

## 3. 删除和插入精确因式分解每个 R_i

删去索引 i，按相同公式在 $H^{(r-1)}$ 定义
$K_{\widehat i},N_{\widehat i},Q_{\widehat i}$。
若只剩一个索引，则 K 是 H，空乘积为 I，N 是 H，Q 为零。

记 $E_i:K_R\to K_{\widehat i}$ 为删除第 i 坐标。
边界满足
$
 E_i d_Rh=d_{\widehat i}(R_i h),
$
故 $E_iN_R\subset N_{\widehat i}$。

反向定义有界插入 $T_i:K_{\widehat i}\to K_R$：对 y 的共同值
$t=R_jy_j\ (j\ne i)$，令
$
 (T_i y)_i=t,\qquad (T_i y)_j=R_i y_j\quad(j\ne i). \tag{3.1}
$
共同值可用任一固定 j 计算，故这个映射有界。
所有输出的 R-乘积均为 $R_it$，所以确在 K_R。
又
$
 T_i d_{\widehat i}h=d_Rh,\qquad
 T_iE_i=R_i^{(r)}|_{K_R},\qquad
 E_iT_i=R_i^{(r-1)}|_{K_{\widehat i}}. \tag{3.2}
$
于是两个映射诱导商映射
$
 \varepsilon_i=P_{Q_{\widehat i}}E_i|_{Q_R},\qquad
 \theta_i=P_{Q_R}T_i|_{Q_{\widehat i}},
$
并有
$
 \boxed{\theta_i\varepsilon_i=\pi_R(R_i).} \tag{3.3}
$
在复合中删掉的正交边界再次被送进边界，所以 (3.3) 不是取消未付出的投影。

结合 (2.4)，
$
 \phi(R_iF)
 =\langle\pi_{\widehat i}(F)\varepsilon_iq,\theta_i^*z_R\rangle. \tag{3.4}
$
右侧是实际 $H^{(r-1)}$ 上的双向量表示。
若它对某个 F 非零，则把该 F 合并进第一向量，便得到秩至多 r−1、仍湮灭 $S\mathfrak C$、在 I 不为零的一般分离泛函。
(1.1) 与最小性矛盾。因此
$
 \boxed{\phi(R_i\mathfrak C)=0\quad(1\le i\le r).} \tag{3.5}
$
这在最小秩条件下将先前的 r−1 因子理想湮灭加强为每个单独预解子理想湮灭。对任意非最小见证，(3.4) 只给“可以降秩，或该理想已经湮灭”的准确分支。

## 4. 更强的算子零结论只在循环 S 零商上

令
$
 M=\overline{\pi_R(\mathfrak C)q},\qquad
 N=\overline{\pi_R(S)M},\qquad Q_0=M\ominus N.
$
由 (2.4) 及真湮灭，$z_R\perp N$ 且 $\langle q,z_R\rangle=\tau>0$，所以 $Q_0\ne0$。
记其表示为 $\pi_0$，
$q_0=P_{Q_0}q$、$z_0=P_{Q_0}z_R$。
则
$
 \phi(F)=\langle\pi_0(F)q_0,z_0\rangle,\qquad
 \pi_0(S)=0. \tag{4.1}
$

对固定 i，置 $M_i^{\rm del}=\overline{\varepsilon_iM}\subset Q_{\widehat i}$。
它是实际 r−1 重放大旗子商中的闭不变空间，所以 (1.2) 给
$
 \overline{\pi_{\widehat i}(S)M_i^{\rm del}}=M_i^{\rm del}.
$
有界性及 (3.3) 给
$
 \theta_iM_i^{\rm del}\subset M,\qquad
 \theta_i\pi_{\widehat i}(S)M_i^{\rm del}\subset N.
$
第二式可先在 $\varepsilon_iM$ 上核为
$\pi_R(SR_i)M\subset N$，再取闭包。
稠密性因此迫
$
 \pi_R(R_i)M=\theta_i\varepsilon_iM\subset N.
$
所以得到算子等式
$
 \boxed{\pi_0(R_i)=0\quad\text{对每个 i}.} \tag{4.2}
$
它强于单一泛函的 (3.5)，但作用范围严格是 Q_0。

现在 (2.1) 给
$
 \pi_0(D_i)^{-1}=\pi_0(U_i),\qquad
 \pi_0(D_{\rm tot})^{-1}=\pi_0(U_{\rm tot}),
 \quad D_{\rm tot}=\prod_iD_i,\ U_{\rm tot}=\prod_iU_i. \tag{4.3}
$
这里绝不把 (4.3) 改成整个 Q_R 上的单位性。

## 5. 全有限秩的实际正 Koszul 向量

置
$
 b_i=D_iP_i=M_iR\in\mathfrak C.
$
考虑完全有界的一阶 Koszul 余链
$
 \delta_0h=(b_i h)_i,\qquad
 (\delta_1v)_{ij}=b_i v_j-b_jv_i\quad(i<j).
$
交换性给 $\delta_1\delta_0=0$。
记
$
 N_b=\overline{\operatorname{Ran}\delta_0},\qquad
 K_b=\ker\delta_1,\qquad Q_b=K_b\ominus N_b,
$
商表示记为 $\pi_b$。b_i 不要求单射。

真实正向量 $x=(Cf_i)_i$ 准确属于 Q_b。对 i≠j，令
$P_{ij}=\prod_{k\ne i,j}R_k$，(2.2) 给
$
 b_i x_j=D_iP_{ij}R_jx_j=D_iD_jP_{ij}1=b_jx_i.
$
因此 $x\in K_b$。另一方面 (2.3) 给
$
 \delta_0^*x=\sum_i b_i^*Cf_i
            =C\sum_i b_i f_i=0,
$
故 $x\perp N_b$。于是
$
 \boxed{\phi(F)=\langle\pi_b(F)x,x\rangle,\qquad
        \|x\|^2=\tau.} \tag{5.1}
$
这对非最小有限秩见证也成立；最小性尚未用于本节。
r=2 时 Q_b 正是[交叉分母附录](R244-appendix-cross-denominator-positive-quotient-and-equivalent-metric.md)的新商。

## 6. 两个全域有界链映射及不能省掉的消因子

令
$
 \Delta=\operatorname{diag}(D_i),\qquad
 \nabla=\operatorname{diag}\left(\prod_{k\ne i}D_k\right).
$
有 $\Delta K_R\subset K_b$、$\Delta N_R\subset N_b$，因为
$
 b_iD_jy_j-b_jD_iy_i
   =D_iD_jP_{ij}(R_jy_j-R_iy_i),\qquad
 \Delta d_R=\delta_0. \tag{6.1}
$

反向的 $\nabla K_b\subset K_R$ 需要真实单射性。
若 $v\in K_b$，
$
 0=b_iv_j-b_jv_i
   =P_{ij}(D_iR_jv_j-D_jR_iv_i).
$
每个 R_k 单射，故 P_{ij} 单射，可消得
$D_iR_jv_j=D_jR_iv_i$。
再乘 $\prod_{k\ne i,j}D_k$，恰给
$R_i(\nabla v)_i=R_j(\nabla v)_j$。
此外
$
 \nabla\delta_0=d_R D_{\rm tot}. \tag{6.2}
$
因此有有界商映射
$
 \mathcal L=P_{Q_b}\Delta|_{Q_R},\qquad
 \mathcal V=P_{Q_R}\nabla|_{Q_b},
$
满足
$
 \mathcal V\mathcal L=\pi_R(D_{\rm tot}),\qquad
 \mathcal L\mathcal V=\pi_b(D_{\rm tot}). \tag{6.3}
$
它们交织全部 F。令
$
 m=\max_i\|D_i\|,\qquad
 n=\max_i\left\|\prod_{k\ne i}D_k\right\|,
$
则 $\|\mathcal L\|\le m,\ \|\mathcal V\|\le n$。

由 $\Delta g=x$、g−q 属于 N_R、x 属于 Q_b，得到
$
 \mathcal Lq=x,\qquad \mathcal L^*x=z_R. \tag{6.4}
$
但在 r>2 的整个 Q_R 上，尚不能由 (6.3) 断言 $\mathcal L$ 有下界；此处 D_tot 未证单位。

## 7. 最小秩的两个循环零商有界同构，且正向量不损失范数

现在只取 §4 的 M、N、Q_0。令
$
 M'=\overline{\pi_b(\mathfrak C)x}
    =\overline{\mathcal LM},\qquad
 N'=\overline{\pi_b(S)M'},\qquad
 Q'_0=M'\ominus N'.
$
关键正交关系在投影以前就成立。由 (5.1)，对全部 F，
$
 \langle\pi_b(S)\pi_b(F)x,x\rangle=\phi(SF)=0.
$
因此
$
 \boxed{x\in Q'_0,\qquad \|x\|^2=\tau;} \tag{7.1}
$
不能用一个未经核验的投影 x 替代这一步。

$\mathcal L$ 把 M、N 分别送入 M'、N'。
由 (6.3)，$\mathcal V\overline{\mathcal LM}\subset M$；
再用 S 交换，$\mathcal VN'\subset N$。
故两者真正诱导
$
 \mathcal L_0=P_{Q'_0}\mathcal L|_{Q_0},\qquad
 \mathcal V_0=P_{Q_0}\mathcal V|_{Q'_0},
$
且
$
 \mathcal V_0\mathcal L_0=\pi_0(D_{\rm tot}).
$
用 (4.3) 得
$
 \pi_0(U_{\rm tot})\mathcal V_0\mathcal L_0=I_{Q_0}.
$
于是
$
 \boxed{\frac{\|y\|}{\|U_{\rm tot}\|n}
           \le\|\mathcal L_0y\|\le m\|y\|
         \qquad(y\in Q_0).} \tag{7.2}
$
非零 Q_0 使分母常数非零。

$\mathcal L_0$ 的像闭；M' 的定义又使其商像稠密于 Q'_0，所以它实际满射，是两个循环 S 零商的有界同构。特别
$
 \mathcal L_0q_0=x,\qquad
 \mathcal L_0^{-1}=\pi_0(U_{\rm tot})\mathcal V_0. \tag{7.3}
$
全部单独 R_i 也在 Q'_0 上作用为零，因为该同构交织相应表示。

置 $G_0=\mathcal L_0^*\mathcal L_0$。由 (6.4)、(7.1)--(7.3)，
$
 \boxed{(\|U_{\rm tot}\|n)^{-2}I_{Q_0}
              \le G_0\le m^2I_{Q_0},\qquad
        G_0q_0=z_0,} \tag{7.4}
$
且
$
 \boxed{\phi(F)=\langle\pi_0(F)q_0,G_0q_0\rangle
             =\langle\pi'_0(F)x,x\rangle.} \tag{7.5}
$
这给参数控制的等价 Hilbert 内积与实际正 Koszul 零商，而不是任意指定一对向量以后抽象挑一个正度量。

## 8. 准确增益与剩余共同域

本稿在真正的最小正秩条件下完成三件相连的事：逐个 R_i 理想湮灭；循环 S 零商上每个 R_i 的算子零作用；全有限秩交叉 Koszul 正向量与原循环零商之间的有界同构。

没有把 Q_0 的零作用或单位性传回整个 Q_R。Q'_0 仍是 H 的 r 重放大旗子商，正向量 x 的 Schmidt 秩仍可能为 r；本稿没有把它搬成原 H 上的秩一见证。链中的实际单射消因子也没有产生共同真空原像，或支付全部交叉 $Cf_i\in\operatorname{Dom}M_j$。普通 Hilbert ISP 的完成标准仍未达到。
