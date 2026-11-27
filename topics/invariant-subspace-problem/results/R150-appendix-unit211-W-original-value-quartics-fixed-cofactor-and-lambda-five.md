# R150：全 W 两个原值四次的固定八次 cofactor 与首一六次商中的五次必要式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 已完成结论

在当前一般 LS、$\Delta=0$、$W=0$ 的既有原物理余图，存在由固定原定义得到的非零

$$
R_5(\lambda)\in A_W[\lambda],\qquad \deg_\lambda R_5=5,
\tag{1}
$$

且

$$
R_5\in (I_6,R_4,C_4),\qquad
I_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{2}
$$

这里 $A_W$ 仅按已经独立支付的权因子局部化；(2) 不使用 $\lambda$、$3-2\lambda$、物理 $D$ 或新值系数的逆。$R_4,C_4$ 是同一个原值的两条四次式，具有完整原矩及 $E_\Delta$ 来源。

因此每个当前完整原点满足同一物理值上的

$$
\chi_\lambda(\lambda)=R_5(\lambda)=0,
\tag{3}
$$

其中 $\chi_\lambda$ 是已实际构成的首一六次式。$R_5$ 的真实五次系数及全部内容零支继续保留。本稿不宣称它首一、不可约或已穷尽全部个别原 N/P 条件，也不宣称整个 W 已空。

## 2. 原值四次及权单位换行

沿用[两个原值四次原组合](R150-appendix-unit211-W-original-two-quartic-necessary-values.md)，记

$$
m=u-\ell,\quad d=1-Q,\quad M=\ell^2d-m^2,
$$

$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell T A_\lambda+2T^3,
$$

$$
c=3-2\lambda,\quad A_*=4uQ-J,\quad C_*=A_*m^2+Jd\ell^2,
$$

$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
+2MuQc\ell T+C_*D,\qquad
b_\Delta=2Mm(A_*T+uQc\ell).
$$

同一个原值中心 $s$ 满足原理想身份

$$
q=Ms^2-D=\ell E_2,\qquad
H=K-2mDs=\ell(2ms+3\ell+3T)E_2-\ell^2E_3,
$$

$$
M\ell^2E_\Delta/\Phi-C_*q=a_\Delta+b_\Delta s.
$$

由此得到

$$
R_4=Ma_\Delta^2-Db_\Delta^2,\qquad
C_4=2mDa_\Delta+Kb_\Delta,
\tag{4}
$$

及完整原来源

$$
\Phi R_4=M^2\ell^2(a_\Delta-b_\Delta s)E_\Delta
+\Phi\{b_\Delta^2-MC_*(a_\Delta-b_\Delta s)\}q,
$$

$$
\Phi C_4=2mDM\ell^2E_\Delta-2mDC_*\Phi q+b_\Delta\Phi H.
\tag{5}
$$

当前 $\Phi$ 已付，故 (4) 均为原必要式，未倒置 $D$ 或 $b_\Delta$。

新源实际按[全域首一 T 四次定理](R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)构成

$$
h_T=8muQ\ell^2d\in A_W^\times,\qquad
q_4=C_4/h_T,\qquad
r_3=R_4-[T^4]R_4\,q_4.
\tag{6}
$$

完整乘积及全部 $T$ 次数均返回；$\deg_Tq_4=4$，$\deg_Tr_3\le3$，且

$$
[T^3]r_3=8M^2uQ\ell^3d(3-2\lambda)(2uQ-J).
\tag{7}
$$

式 (7) 没有被倒置。换行 (6) 只用权单位，故

$$
(I_6,q_4,r_3)=(I_6,R_4,C_4).
\tag{8}
$$

## 3. 全域三生成元上的三条实际原行

[整个 K7 排除](R150-appendix-unit211-W-entire-K7-complete-original-exclusion-and-global-three-generators.md)已支付固定三均值头。物理 $t$、$T$ 在 $(x,y,\lambda)$ 中均为原仿射式；新源实际核 $T$ 的正反恢复。

将 $N_1,q_4,r_3$ 按这三条原均值规则约化到 $v=(1,x,y)^T$。对每行只清已付权分母和共同已付因子，得到三个多项式行 $\widehat r_N,\widehat r_q,\widehat r_r$，以及完整八项原迹

$$
\widehat r_i v=\widehat\tau_i
(E_1,E_{Be},E_{Bo},N_1,N_S,P_S,q_4,r_3)^T.
\tag{9}
$$

全部三条 (9) 已实际乘回。其常数列、$x$ 列、$y$ 列的实际 $\lambda$ 次数依次为

$$
(2,1,1),\qquad(4,3,3),\qquad(4,3,3).
\tag{10}
$$

$N_1$ 始终是原双点的一阶极化 germ，没有增加错误的简单点值条件。

## 4. 固定 C8 及完整 cofactor 身份

按上述行序定义

$$
\mathcal M=
\begin{pmatrix}\widehat r_N\\\widehat r_q\\\widehat r_r\end{pmatrix},
\qquad C_8=\det\mathcal M.
\tag{11}
$$

令 $\omega_i=(-1)^i\det\mathcal M_{\widehat i,\{1,2\}}$。实际完整返回三列

$$
\sum_i\omega_i\widehat r_i=(C_8,0,0).
\tag{12}
$$

由 (9)、$v_0=1$ 直接得到

$$
C_8=\sum_i\omega_i\widehat\tau_iF_8
\in (I_6,q_4,r_3).
\tag{13}
$$

这是已返回原迹与已返回 cofactor 的精确组合；没有另行展开并保存巨大的最终八项迹。

实际 $C_8$ 非零，次数与规模为

$$
(\deg_e,\deg_k,\deg_\lambda)C_8=(71,103,8),\qquad
\deg_{\rm total}C_8=141.
$$

它有 42206 项，定义编码 2790962 字节，SHA256：

60bf40fc95238ced1ec780d93e43c45d3bca0777efd1202c0f3cfcc57ba70ef5。

所有清分母和组合都按多项式身份返回，未删掉任何瞬时主元零或新内容零支。

## 5. 首一除法实际得到非零 R5

[原首一物理 λ 六次定理](R150-appendix-unit211-W-global-original-physical-lambda-monic-six.md)及其首次实际系数回执已给

$$
\chi_\lambda\in A_W[\lambda],\quad
\deg_\lambda\chi_\lambda=6,\quad
\chi_\lambda(\lambda)\in I_4\subset I_6.
$$

本次对 (11) 作首一除法，实际得到

$$
C_8=Q_2\chi_\lambda+R_5,\qquad
\deg_\lambda Q_2=2,\quad\deg_\lambda R_5=5,
\tag{14}
$$

并核回完整系数乘积。因此由 (8)、(13)、(14) 得 (2)。没有倒置 $R_5$ 的五次头，也没有剥除它或 $C_8$ 的尚未支付的共同权内容。

对 $\lambda$ 的降次已经完成；当前权系数的规模如下。表中分子、分母均为实际约简后的权多项式：

| $\lambda$ 次数 | 分子双次数 | 分子项数 | 分母双次数 | 分母项数 |
|---|---|---|---|---|
| 0 | $(103,146)$ | 9797 | $(25,43)$ | 812 |
| 1 | $(102,146)$ | 9713 | $(25,43)$ | 812 |
| 2 | $(100,145)$ | 9461 | $(24,42)$ | 764 |
| 3 | $(100,145)$ | 9378 | $(24,42)$ | 764 |
| 4 | $(100,145)$ | 9294 | $(24,42)$ | 764 |
| 5 | $(99,145)$ | 9190 | $(24,42)$ | 764 |

所有这些分母已经逐一支付。后续可从固定 $C_8$ 的完整 $\lambda$ 内容作准确分层；任何未付内容因子都必须保留其整个零集，不能因“primitive part”这个名称而擅自除去。

## 6. 唯一实际执行与保存范围

源：

notes/2026-11-28-unit211-W-original-value-quartics-three-columns-lambda-five-8542.py

Git blob：dc173050e023489ba7502f1b9c640be4d2dcfca4。

SHA256：87a890d6bf90e3f50e63eac989680bd78973e63299b60557f90d1fcb29d4e2ad。

- run 46082636460；job 140784905290；
- 源提交 11f4acf4993e93c8060c14823b717a5298761d95；
- 源最终时间 39.281549478 秒；
- 驱动墙钟 39.385933311 秒，最大子进程 RSS 191120 KiB；
- 内层真实退出码 0；
- stdout 6962 字节，SHA256 61ea84e6f5c940b6248ec64292c9925955f773065c7b8385470dc798bac77bac；
- 2026-11-27 23:28:15.193246 UTC 实际 pull 前后同为上述提交，两 README 均未变。

旧十八行泛型模块与十二阶 Sylvester 均未执行。固定 $C_8$、$Q_2$、$R_5$ 及全部矩阵由源中原定义再生，仅记录 SHA 和规模，不保存可重算系数、矩阵、大迹或编码分片。整个 W 的完整同点原值返回继续。
