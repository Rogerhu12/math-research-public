# W 的两个原值四次进入三生成元模型：新固定 cofactor 与首一 λ 降次输入

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

本页固定新的原值输入。它增加原 $E_2,E_3,E_\Delta$ 的信息，不是重排已冻结的十八行泛型模块，也不重跑旧十二阶结果式。首次执行前不声明下述固定 cofactor 或余式非零。

## 1. 同一原值的两条四次关系

沿用[两个原值四次的完整原组合](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)及[全图首一 T 四次](../results/R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)。记

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
c=3-2\lambda,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+Jd\ell^2,
$$

$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
+2MuQc\ell T+C_*D,
$$

$$
b_\Delta=2Mm(A_*T+uQc\ell).
$$

同一个原值中心 $s$ 上已有

$$
q=Ms^2-D=\ell E_2,
$$

$$
H=K-2mDs=\ell(2ms+3\ell+3T)E_2-\ell^2E_3,
$$

$$
M\ell^2E_\Delta/\Phi-C_*q=a_\Delta+b_\Delta s.
$$

这里 $\Phi$ 是当前 W 原图中已付的权单位。于是

$$
R_4=Ma_\Delta^2-Db_\Delta^2,\qquad
C_4=2mDa_\Delta+Kb_\Delta
\tag{1}
$$

都在原 $E_2,E_3,E_\Delta$ 理想中。准确的交叉乘法来源为

$$
\Phi R_4=M^2\ell^2(a_\Delta-b_\Delta s)E_\Delta
+\Phi\{b_\Delta^2-MC_*(a_\Delta-b_\Delta s)\}q,
$$

$$
\Phi C_4=2mDM\ell^2E_\Delta-2mDC_*\Phi q+b_\Delta\Phi H.
\tag{2}
$$

既有原相容条件、个别 N/P 和完整 $N(V)$ 不由 (1) 自动成立；本次只增加确有 (2) 来源的必要关系。

## 2. 仅权单位的可逆换行

已成完整系数身份给

$$
[T^4]C_4=h_T=8muQ\ell^2d\in A_W^\times,\qquad [T^3]C_4=0.
$$

定义

$$
q_4=C_4/h_T,\qquad
r_3=R_4-[T^4]R_4\,q_4.
\tag{3}
$$

则

$$
\deg_Tq_4=4,\quad q_4\text{ 首一},\qquad \deg_Tr_3\le3,
$$

且

$$
[T^3]r_3=8M^2uQ\ell^3d(3-2\lambda)(2uQ-J).
\tag{4}
$$

本输入不倒置 (4)，即使 $\lambda=3/2$ 已由其它原定理闭合，这里也保留它的整多项式零支。$D,a_\Delta,b_\Delta,K$ 同样没有被倒置。

式 (3) 的换行矩阵在已付权环中可逆，所以

$$
(I_6,q_4,r_3)=(I_6,R_4,C_4),
\qquad I_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{5}
$$

这一步不会带入新的值范数逆或未付内容除法。

## 3. 原物理 λ 坐标下的三列

由全域已付 K7 的三均值规则，同一物理 $t$ 在 $x,y,\lambda$ 中仿射恢复，$T$ 也为同一点的仿射式。源先实际核其双侧坐标恢复。

因此 (3) 在 $x,y,\lambda$ 中总次数均不超过 4。将它们按已刊三条原规则约化到 $(1,x,y)$，得到三行

$$
r_N,\quad r_q,\quad r_r\in A_W[\lambda]^3
$$

以及完整八项原迹

$$
r_iv=\tau_i F_8,\quad v=(1,x,y)^T,\quad
F_8=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S,q_4,r_3)^T.
\tag{6}
$$

$N_1$ 仍为原双点的一阶极化 germ；没有把第二 Gram 行当成另一个简单点。

对值行，重写函数给的是

$$
\operatorname{rem}(P)-P=\sum_{j=0}^5 t_jF_j.
$$

故 (6) 在对应值位置保留 $+P$ 的完整系数。这一符号和全部八项多项式组合都在新源实际乘回。每行的分母清除及共同因子剥除仅用已付权量，所有未付内容保留。

原三规则的加权次数保证：$r_N$ 的常数列对 $\lambda$ 至多 2 次、两线性列至多 1 次；$r_q,r_r$ 的常数列至多 4 次、两线性列至多 3 次。后续固定 cofactor 因而不会超过 $\lambda$ 八次。

## 4. 固定三阶 cofactor 及无新逆降到五次

设 $\widehat r_N,\widehat r_q,\widehat r_r$ 为上述只按已付权单位多项式化后的三行，构成固定 $3\times3$ 矩阵 $\mathcal M$。取其第 0 列的完整 cofactor 向量 $\omega$，定义

$$
C_8(\lambda)=\det\mathcal M,\qquad
\omega^T\mathcal M=(C_8,0,0).
\tag{7}
$$

三列身份全部实际乘回。结合 (6) 和 $v_0=1$，得

$$
C_8=\sum_{i=0}^2\omega_i\,\widehat\tau_iF_8
\in(I_6,R_4,C_4).
\tag{8}
$$

最后的八项巨大展开无需另外保存；(6)、(7) 已给完整且可再生的原组合。

若 $C_8$ 非零，则 $\deg_\lambda C_8\le8$。使用已经实际构成的首一

$$
\chi_\lambda(\lambda)\in I_4\subset I_6,\qquad\deg_\lambda\chi_\lambda=6,
$$

作仅首一除法

$$
C_8=Q_2\chi_\lambda+R_5,\qquad
\deg_\lambda Q_2\le2,\quad\deg_\lambda R_5\le5.
\tag{9}
$$

所有除法只用最高系数 1；商与余式的权分母均仍已付。式 (9) 的完整系数乘积必须实际返回。因此

$$
R_5\in(I_6,R_4,C_4).
\tag{10}
$$

这里的归属在仅权局部化的多项式原理想中，不需要先饱和 $\lambda$、$3-2\lambda$ 或 $D$。$C_8$ 或 $R_5$ 的任何新头和内容都不能任意剥掉。

若固定 (7) 恒为零，源准确报告没有得到这条标量条件；若 (9) 余式为零，也不能记成新的五次约束。首派前本稿不预先排除这些情况。

## 5. 冻结源与边界

新源：

notes/2026-11-28-unit211-W-original-value-quartics-three-columns-lambda-five-8542.py

Git blob：dc173050e023489ba7502f1b9c640be4d2dcfca4。

SHA256：87a890d6bf90e3f50e63eac989680bd78973e63299b60557f90d1fcb29d4e2ad。

字节数：9867。固定首次预算：180 秒、4 GiB。冻结时尚未执行。

仅为新值输入构造两个必要前缀：

- 三均值规则与六乘法前缀：5833 字节，SHA256 8ea50cb422b81b5976bbb132e01809135ebbaedc06d545bcdb0c741fec4e3ff4；
- 首一 $\lambda$ 六次系数前缀：8601 字节，SHA256 ce868f00596f420d1a46a1503e2432be7bd13f0001e8ebc3e0cd68a53092fc7a。

第二个前缀只在新 (7) 非零后执行，为 (9) 再生必要系数；旧谱因子测试不执行。旧十八行泛型模块、十二阶 Sylvester 和六阶权行列式都不执行。

只保源、原定义、真实 run、SHA 与小回执；不传送或保存可重算系数、矩阵、迹或编码分片。整个 W 的其它原值条件继续保留。
