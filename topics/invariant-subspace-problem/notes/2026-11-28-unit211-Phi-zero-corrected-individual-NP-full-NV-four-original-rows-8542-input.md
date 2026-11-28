# 首次新输入：正确 Phi 的个别 N/P、完整 N4 与四条原值行

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。
**状态：未执行，不预记新头、纯权支持、有限性或排空。**

本次在纠错后的全图三生成呈示中加入尚未使用的个别谱条件和完整孤立列 $N_4$。它与已完成的加权六式、两个 C6 和固定十二阶结果式是不同的原输入；既有六式和全部共同头零纤维继续保留。

## 1. 真实原范围及已付系数

沿[正确整个 I6 的十五列呈示](../results/R150-appendix-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-and-two-sextics.md)，当前图是正确 $\Phi=0$、物理 $D_{\rm phys}\ne0$ 的原单位支。使用
$$
\delta=1-Q,\quad s_u=u-1,\quad K_w=Q+4s_u,\quad
L=Q-2s_u(u-2),\quad \ell=L/Q,
$$
$$
m=u-\ell,\quad M=\ell^2\delta-m^2=4bc\delta=M_n/Q.
$$
程序的纯权分母表仅为已刊原
$$
Q\delta s_uK_wLM_nAB
$$
再乘已独立恢复的 $m$ 分子。$A,B$ 是正确两条完整头零支的已付因子。本次没有从被撤回的旧紧凑式恢复任何单位。

$m$ 的来源为[完整等权原排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md)；当前规范与其真实原图的对应和分母范围已在
[静态来源记录](2026-11-28-unit211-Phi-corrected-equal-weight-m-unit-static-provenance-8542.md)
列明。该记录是旧正确 vm 来源的读取，不是重跑。这里不借 W 的单位或 $\Phi^{-1}$。

令 $\mathcal A$ 为上述纯权环，已有
$$
\mathcal A[\lambda,T,z]/I_6
\simeq\mathcal A[\lambda]^3/
\langle G,M_TG,M_zG\rangle,\qquad |G|=5.
\tag{1}
$$
基是 $1,T,z$，不假设自由。新的任何乘法均用既有原二次规则的六系数差身份和真实乘法 DAG；不得在裸三向量上假设结合律。

## 2. 同一原值变量的两矩与三矩

记
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K_{\rm val}=\ell^2B_\lambda-3\ell A_\lambda T+2T^3.
\tag{2}
$$
原孤立列为 $V_{\rm val}=(1,w,h,k)$，$w=\lambda-1-T$。取同一个原值中心 $\sigma$，写
$$
v_0=1+\frac{T+m\sigma}{\ell},\qquad
h=v_0-\rho\sigma,\quad k=v_0+\rho\sigma,\quad \rho^2=\delta.
\tag{3}
$$
该表示只是解 $b(h-1)+c(k-1)=T$，保所有原根。

令两个原移位矩误差
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda,\qquad
E_3=b(h-1)^3+c(k-1)^3-B_\lambda.
$$
直接展开给
$$
q=M\sigma^2-D=\ell E_2,
$$
$$
H=K_{\rm val}-2mD\sigma=(3T+2m\sigma)q-\ell^2E_3.
\tag{4}
$$
因此原点有 $q=H=0$。从 (4) 得新的原必要行
$$
R_6=MK_{\rm val}^2-4m^2D^3
=MH(K_{\rm val}+2mD\sigma)+4m^2D^2q.
\tag{5}
$$
没有倒 $D$，也没有从某个模值判断 $D$ 非零。

## 3. 完整个别 N/P 的五次原条件

按原真 dual 乘法定义
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)
-4\tau(v)\tau(dv)+4f\tau(v)^2+\tau(vDKv),
$$
$$
P_2(v)=\tau((v-\tau(v)1)^3).
\tag{6}
$$
对真正原行 $g_B,g_C$，定义完整奇系数
$$
N_o=\frac{N_4(g_B)-N_4(g_C)}{2\rho},\qquad
P_o=\frac{P_2(g_B)-P_2(g_C)}{2\rho}.
$$
它们是二次扩张中的实际奇坐标，程序从 (6) 构造 $g_B$ 的完整偶、奇两列；共轭给同一个 $g_C$，并非从加权 NS/PS 反定义个别值。

原个别谱条件是
$$
N_4(g_B)=2\lambda P_{02}h^2,\quad
N_4(g_C)=2\lambda P_{02}k^2,\qquad
P_2(g_B)=P_{02}h^3,\quad
P_2(g_C)=P_{02}k^3.
$$
用 (3)，其奇误差为
$$
E_N=N_o+4\lambda P_{02}v_0\sigma,\qquad
E_P=P_o+P_{02}(3v_0^2\sigma+\delta\sigma^3).
\tag{7}
$$
记 $a_0=1+T/\ell$。只用 (4) 中的
$M\sigma^2\equiv D$ 和 $2mD\sigma\equiv K_{\rm val}$，得到
$$
\begin{aligned}
N_{\rm low}={}&DN_o+
2\lambda P_{02}\left(
 \frac{K_{\rm val}a_0}{m}
 +\frac{2mD^2}{\ell M}\right)
\equiv DE_N\pmod{(q,H)},\\
P_{\rm low}={}&DP_o+
P_{02}\left[
 \frac{K_{\rm val}}{2m}
 \left(3a_0^2+
  \left(\frac{3m^2}{\ell^2}+\delta\right)\frac D M\right)
 +\frac{6a_0mD^2}{\ell M}\right]
\equiv DE_P\pmod{(q,H)} .
\end{aligned}
\tag{8}
$$
这些同余只除原纯权单位 $m,M,\ell$；把 (7) 展开后，各替换均是相应 $q,H$ 的显式多项式倍数。尤其 $D$ 在 (8) 只作正乘子，所有 $h/k$ 原嵌入保留。

$N_o,P_o$ 的总几何次数至多三，故 (8) 至多五次。它们是真正个别 N/P 的新增必要条件，不能由只保加权 NS/PS 替代。

## 4. 完整 N4 的五次原条件

本节只使用[九自由变量的全一般 N4 三短式](../results/R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)，不使用 W 的纯 f 消失或 $\Phi^{-1}$ 恢复。

令当前原 Gram 的
$$
\mathcal V=bX+cY,\quad \mathcal W=bpX+cqY,\quad
c_\lambda=3-2\lambda.
$$
原 $\ell V_{\rm val}$ 可写为
$$
\widetilde V_0+\sigma\widetilde V_1,\qquad
\widetilde V_0=(\ell,\ell w,\ell+T,\ell+T),\quad
\widetilde V_1=(0,0,m-\ell\rho,m+\ell\rho).
$$
完整一般恒等式是
$$
\ell^2N_4(V_{\rm val})=Z_0+Z_1\sigma+Z_2\sigma^2,
\tag{9}
$$
其中
$$
\begin{aligned}
Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD
 +2\ell u w(\ell c_\lambda+T)\\
 &+2\mathcal V(\ell^2+\ell c_\lambda T+T^2)
 +2bc\,t(T^2-\ell^2),\\
Z_1={}&2(\ell c_\lambda+2T)(u\mathcal V-\ell\mathcal W)
 -2\ell Mw+4bc\,mTt,\\
Z_2={}&2\bigl((u^2-\ell^2Q)\mathcal V
 -2m\ell\mathcal W-\ell Mf-bcMt\bigr).
\end{aligned}
\tag{10}
$$
(9)–(10) 已从完整原二次型和其完整极化证明，不是单个分量或最高项条件。当前同点的 $f,t,\mathcal V,\mathcal W,A_1,w$ 都由正确原恢复给出，对 $\lambda,T,z$ 仿射。

定义本次新的
$$
V_{\rm low}=DZ_0+\frac{K_{\rm val}}{2m}Z_1+
\frac{D^2}{M}Z_2.
\tag{11}
$$
完整原理想身份为
$$
\boxed{\quad
V_{\rm low}=D\ell^2N_4(V_{\rm val})
+\frac{Z_1}{2m}H-\frac{DZ_2}{M}q .
\quad}
\tag{12}
$$
所以 (11) 在当前所有原点为零。其几何次数至多五，分母仅为已付纯权，未倒 $D$ 或 $D$ 范数。(12) 对当前图的解释保持原 $D_{\rm phys}\ne0$ 范围；不将原物理碰撞图擅自排除。

## 5. 新的十二原列与辅助 I10 完整呈示

定义本次必要辅助理想
$$
I_{10}=I_6+(R_6,N_{\rm low},P_{\rm low},V_{\rm low})
\subset\mathcal A[\lambda,T,z].
\tag{13}
$$
原完整物理系统满足 (13)，但本次不宣称这十式已充分代替整个物理系统。

程序将四条新行按真正三规则约化到 $1,T,z$，并逐二元乘法返回实际三个坐标和局部原规则差。预定次数上界为

| 新原行 | 总几何次数上界 | 三系数的 lambda 次数上界 |
|---|---:|---:|
| $R_6$ | $6$ | $(6,5,5)$ |
| $N_{\rm low}$ | $5$ | $(5,4,4)$ |
| $P_{\rm low}$ | $5$ | $(5,4,4)$ |
| $V_{\rm low}$ | $5$ | $(5,4,4)$ |

它们的实际次数只能依据首次输出登记。

每行再添 $T,z$ 的真实作用，并与同一个原变量乘法路径逐坐标比较，得到十二条新增原列。先行四个矩阵缺陷使旧十五列加这十二列已被两个动作保持：任何二次动作归为一次动作及旧 commutator 列。因此由同一个循环 $e_0$ 和原双向映射，(13) 的商有精确二十七列三坐标呈示。这里引用已成四缺陷定理，不执行旧三十六坐标门，也不假设裸三坐标自由或结合。

随后只取两组真正新三列：
$$
(N_1,N_{\rm low},V_{\rm low}),\qquad
(N_1,P_{\rm low},V_{\rm low}).
\tag{14}
$$
对每组按后两列 cofactor 构造三个实际乘子，清纯权分母，再只约除三个乘子分子的共同因子。新乘子须实际返回全部三个原坐标才给纯 $(u,Q,\lambda)$ 必要条件。最后只能剥运行表中的原权单位；所有新内容零和 lambda 首项零仍保留。若某 cofactor 为零，按零式记录，不更换组合或扩大本次目标。

## 6. 必要定义与唯一首次预算

新源：

    2026-11-28-unit211-Phi-zero-corrected-individual-NP-full-NV-four-original-rows-8542.py

Git blob：

    05c1ebdc879f2f19320e7e6b8c8882fb6cc4c21e

SHA256：

    359458b9b598460fcacaf3fbb6e8b1e270149a533ddc06ed543e5c573e592097

大小 $12091$ 字节；首次总限额 $120$ 秒、$1$ GiB，外层 $135$ 秒。两层必要前缀的 alarm 都由最初绝对截止钳制。

依赖只有两个已刊小源码：

    2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py
    2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py

完整 SHA256 分别为

    84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0
    5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7

两者均在 AST 外完整核 SHA。第一文件只取旧 NS 构造之前的 $11204$ 字节，SHA 为

    2693b11fb556d56d04b04750be5342f063bedb3d03cefb11faf2d49dee2106a6

AST 只保原四式系数的定义循环，省略旧动作、overlap、缺陷及其专用中间值、旧证明 assert 和输出。保留三规则、$N_1$、真 Gram 及原 $N_4/P_2$ 函数定义；旧 NS/PS、十五列、两个 C6 和十二阶结果式根本未进入该前缀。第二文件内部只取已知 $4007$ 字节的正确原式定义。

完整一般 (9)–(10) 是已成纸面来源，只在本次新正确三生成环境运输，不重跑其九变量整数证书。程序输出逐条真实新行、小型次数/项数/哈希回执和局部返回计数，不保存大系数、缓存或分片。没有新增旧源审核门，没有预记全 Phi 排空。
