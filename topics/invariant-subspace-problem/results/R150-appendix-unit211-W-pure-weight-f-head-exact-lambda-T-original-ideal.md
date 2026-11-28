# R150：W 纯权 f 一次头上的完整 lambda,T 原理想及纯 N5 替换

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 范围与新增结论

沿
[全图首一 f 二次与精确 I4／I6](R150-appendix-unit211-W-lambda-T-f-global-monic-f-two-and-exact-I4-I6.md)，
当前 W 的四原均值／极化理想有完整表示
$$
I_4=(q_f,r_1,r_2,r_3),\qquad
q_f=f^2+q_1f+q_0,\qquad r_i=A_i+B_if.
\tag{1}
$$
这里 $A_i,B_i,q_j$ 都属于已付纯权环再添自由 $\lambda,T$，
并且
$$
\deg A_i\le2,\quad\deg B_i\le1,\quad
\deg q_1\le1,\quad\deg q_0\le2.
\tag{2}
$$
本篇证明两项完整接口：

1. 任一具有纯权非零头的原关系 $hf+a(\lambda,T)\in I_4$，
   在且仅在其已明确保留的 $h\ne0$ 图上，
   把完整原 I6 化为同点纯 $(\lambda,T)$ 的三／四次条件；
   没有给各条原式独立选择不同 f。
2. 已刊完整十一行辅助原理想中的 $V_{\rm low}$，
   可在纯权环上用 **f 独立的 $\mathcal N_5$** 精确替换：
   $2m\ell^2V_{\rm low}=\mathcal N_5+2f\mathcal C_4/(MQ)$。
   这项理想等式没有 D 逆。

第 2–6 节先对任一具有原来源的纯权头给出完整开图引理，未知头的整个零面始终保留。
第 7 节随后使用独立已刊的完整权头识别，把本次具体头的这些等式推广到整个当前 W 图，
并收紧此前 b0 原支的不同规范点数界。
不重复计算该权头，也没有据此宣布完整 W 排空。

## 2. 一个实际非零的纯权 f 头来源

因 $B_i$ 对 $\lambda,T$ 仿射，令
$$
\mathcal B_i=([1]B_i,[\lambda]B_i,[T]B_i),\qquad
\mu_i=\text{后两列的第 i 个带符号余子式}.
$$
固定三阶恒等式给
$$
\sum_i\mu_iB_i=\det\mathcal B,\qquad
\sum_i\mu_i r_i=(\det\mathcal B)f+\sum_i\mu_iA_i.
\tag{3}
$$
所有 $\mu_i,\det\mathcal B$ 都是纯权函数；
(3) 是真正原 I4 组合，不依赖 f 或几何首项的逆。

新小精确定义计算在 $e=1,k=3$ 给
$$
\det\mathcal B=\frac{879351616}{1012683}\ne0 .
\tag{4}
$$
该计算使用完整正确 dual Gram、真有理二次扩张和 (2) 的次数界：
以 $f=-1,0,1$ 提取二次与一次系数，
以 $(\lambda,T)=(0,0),(1,0),(0,1)$ 提取已知仿射系数。
还在 $(2,3)$ 返回同一仿射式。
因此 (4) 只证明头是非零有理函数，不是物理解取样或纤维排空。

准确 source blob d95dbf5c3be0b538d61e16b42301141c8a3ef108，
SHA256 ebe11ef8d8cee3f17064faf3bd40c5efe55d70f2af10158109b3e0ad8af12f7e；
receipt 5952b68095676015666b2171ba6c88ee5872782a。
首次真实 V8 时间65 ms，46550次有理加乘；
无独立进程退出码或 RSS，不猜测。
无需再运行该小计算作为本篇纸证的门。

若后续实际源清四个原乘子的纯权分母并取消其共同多项式，
随后完整返回新的 $hf+a$，也可采用这个加强后的 h。
它的原来源必须是约后的实际乘子，不能只将 (3) 的等式两边
除以未付因子再宣称整个零面也覆盖。

## 3. 同一个 f 的精确消元

记 $\mathcal A$ 为当前已付纯权环添 $\lambda,T$，
在明确的 $\mathcal A[h^{-1}]$ 上令
$$
g=a/h,\qquad R=f+g.
$$
h 是纯权，所以 $\deg_{\lambda,T}g\le2$。
R 仍有原 I4 来源。
逐项相乘：
$$
q_f=(f+q_1-g)R+P_0,\qquad
P_0=g^2-q_1g+q_0,
\tag{5}
$$
$$
r_i=B_iR+P_i,\qquad P_i=A_i-B_i g.
\tag{6}
$$
R 原本就在 I4，(5)、(6) 两向给出
$$
\boxed{I_4=(R,P_0,P_1,P_2,P_3)}\quad
\text{于 }\mathcal A[h^{-1}][f].
\tag{7}
$$
$P_0$ 至多四次，$P_i$ 至多三次。
若某一系数恰为零，等式仍成立；不再加任一个 $B_i$ 的逆。

## 4. 完整加权 N/P 先首一短除，再同 f 恢复

原 $N_S,P_S$ 在自由 $(\lambda,T,f)$ 图总次数至多3。
对真正首一 $q_f$ 作唯一短除，写
$$
N_S=Q_Nq_f+A_N+B_Nf,\qquad
P_S=Q_Pq_f+A_P+B_Pf,
\tag{8}
$$
$$
\deg A_N,\deg A_P\le3,\qquad
\deg B_N,\deg B_P\le2.
$$
定义
$$
P_N=A_N-B_Ng,\qquad P_P=A_P-B_Pg.
\tag{9}
$$
两者总次数至多4。
例如
$$
N_S=\{Q_N(f+q_1-g)+B_N\}R+Q_NP_0+P_N ,
\tag{10}
$$
P 行完全同样。反向由 (8) 直接给 (9) 的原组合。
故在这个头图上
$$
\boxed{
I_6=(R,P_0,P_1,P_2,P_3,P_N,P_P).
}
\tag{11}
$$
这给准确的环同构
$$
\mathcal A[h^{-1}][f]/I_6
\cong
\mathcal A[h^{-1}]/(P_0,P_1,P_2,P_3,P_N,P_P).
\tag{12}
$$
没有假设原商自由，也不是仅同解集或参数配对的近似。
先按 qf 降次再代 f 的顺序，保证纯 N/P 仍至多四次；
直接把二次 g 代入原三次公式所得的表面六次不必先展开。

## 5. 整个 Vlow 的准确 f 独立替换

沿
[低 D 次完整原理想压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，
写同一原向量为 $V_{\rm val}=V_0+sV_1$，并取真正完整系数
$$
N_4(V_0+sV_1)
=Z_0^{\rm raw}+Z_1^{\rm raw}s+Z_2^{\rm raw}s^2.
$$
旧完整低次式是
$$
V_{\rm low}
=DZ_0^{\rm raw}+\frac K{2m}Z_1^{\rm raw}
+\frac{D^2}{M}Z_2^{\rm raw}.
\tag{13}
$$
当前纯 N5 的缩放系数采用
$$
\ell^2Z_0^{\rm raw}=Z_0,\quad
\ell^2Z_1^{\rm raw}=Mz_1,\quad
\ell^2Z_2^{\rm raw}=Mz_2.
\tag{14}
$$
(14) 只是同一个完整 N4 二次的逐系数等式，不选某个分量。
直接乘 (13) 得
$$
2m\ell^2V_{\rm low}=2mD(Z_0+Dz_2)+MKz_1.
\tag{15}
$$
[纯六／四／五次全原值表示](R150-appendix-unit211-W-pure-lambda-T-six-four-five-entire-value-equivalence.md)
的自由 f 系数身份又给
$$
2mD(Z_0+Dz_2)+MKz_1
=\mathcal N_5+\frac{2f}{MQ}\mathcal C_4.
$$
所以完整地得到
$$
\boxed{
2m\ell^2V_{\rm low}
=\mathcal N_5+\frac{2f}{MQ}\mathcal C_4 .
}
\tag{16}
$$
$\ell,m,M,Q$ 都为当前纯权单位，式中没有 D 逆，
没有新几何头，也没有 b0 或范数的逆。

旧 $q_{T4}$ 与 $\mathcal C_4$ 只差已付尺度
$8muQ\ell^2\delta$。因此，若 I11 表示已刊十一行辅助多项式理想，
则在当前纯权环上已有
$$
\boxed{
I_{11}
=I_6+(\mathcal C_4,\mathcal R_6,
       N_{\rm low},P_{\rm low},\mathcal N_5).
}
\tag{17}
$$
这是整组生成理想的双向等式，保整个原 $V_{\rm low}$；
不需要重新展开被冻结的完整 V 动作。

I11 与原个别值系统的等价仍采用已刊的物理 $D\ne0$ 范围。
(16)、(17) 的多项式身份本身不倒 D，
不据此把整个物理排除范围外推给 $D=0$ 碰撞图。

## 6. 个别两谱的条件继续保留

令
$$
N_4(\mathrm{row}_B)=n_a+\rho n_b,\qquad
P_2(\mathrm{row}_B)=p_a+\rho p_b,\qquad \rho^2=\delta.
$$
对 qf 唯一短除
$$
n_b=Q_bq_f+A_b+B_bf,\qquad
p_b=Q_cq_f+A_c+B_cf.
\tag{18}
$$
这些原三次的余系数满足 $\deg A\le3,\deg B\le2$。
令 $A_0=1+T/\ell$。在同一 f 头图上，完整低次个别条件变为
$$
\begin{aligned}
\widehat N_{\rm low}
={}&D(A_b-B_bg)
 +2\lambda P_{02}
 \left(\frac{KA_0}{m}+\frac{2mD^2}{\ell M}\right),\\
\widehat P_{\rm low}
={}&D(A_c-B_cg)
 +P_{02}\left[
 \frac K{2m}\left(3A_0^2+\frac{(3m^2/\ell^2+\delta)D}{M}\right)
 +\frac{6A_0mD^2}{\ell M}\right].
\end{aligned}
\tag{19}
$$
两式次数至多6。
由 (5)、(18) 逐项相减，原式与 (19) 的差都在 $(R,P_0)$ 中，
所以 (17) 的完整性没有损失。
加权 NS/PS 始终保留，配 (19)、R6 可恢复两个个别谱的偶奇行；
本篇没有用加权和代替个别 N/P。

于是整个当前 I11 在该纯权头图上的同点模型可完全写在
$(\lambda,T)$ 中，保：
$P_0,P_1,P_2,P_3,P_N,P_P$，
三个纯值式 $\mathcal C_4,\mathcal R_6,\mathcal N_5$，
以及 (19) 两式。
$h=0$ 的整个图继续使用原完整表示，不从本篇消元中删除。

以上给出原身份、度界和双向恢复。实际纯 N/P 系数、后继结式和最终排空仍须依各自真实新回执，
没有预先计入。下面只应用已经独立发表的权头结果，不增加执行门。


## 7. 已刊整头支付与 b0 规范不同点界 23088

[原 I4 六行、整个 f 头支付与唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)
已经以唯一真实运行的完整四源身份返回
$$
h f+a(\lambda,T)\in I_4.
$$
其完整 QQ 因子与既刊固定定义的精确匹配给
$$
h=c\,e^2ku(2e+1)G_{36},\qquad c\in\mathbb Q^\times .
\tag{20}
$$
这里 $(2e+1)$ 由 $(J-Q)\overline V=-2e^2k(2e+1)$ 支付，
$G_{36}$ 由其整个原权曲线排除支付。没有按同次数猜测因子，也不把泛型返回当整曲线排空。

因此针对 (20) 这个**已返回的具体原关系**，第 3–6 节的全部 $h\ne0$ 条件
在当前整个 W 原图都已经满足。
(7)、(11)、(12)、(17)、(19) 于是给整个当前 W 的精确同点纯 $(\lambda,T)$ 接口。
原均值里的 $f=-g(\lambda,T)$ 处处唯一。此处仍不把这些条件外推到其它 LS 图或 D=0 碰撞图。

这也直接改进
[整个 b0 原支的两条权曲线及原纤维界](R150-appendix-unit211-W-entire-b0-two-original-curves-5772-weights-46176-normalized-points.md)
中的不同规范点数界。该已成定理有：

- 原权曲线 $\mathcal C_{74},\mathcal D_{78}$ 完整 QQ 互素，所以其共同权点不超过 $74\cdot78=5772$，并已给相应权 scheme 长度界。
- 在整个 $b_0=0$ 原支，$A_* \ne0$，故
  $T=-\kappa(3-2\lambda)$，其中 $\kappa=uQ\ell/A_*$ 是原单位。
- 已返回二次 $q_2(\lambda)=a_2\lambda^2+a_1\lambda+a_0$ 的三系数满足
  $a_2+3a_1+4a_0=-32L$，$L=uQ\delta\ell\kappa^2$ 是原单位。

因此每一个允许权点处，$q_2$ 都不是零多项式，对 $\lambda$ 最多有两个不同根。
此论证包括 $\lambda^2$ 头或一次头消失的整个纤维，不倒任一新几何头。
每个 $\lambda$ 唯一决定 $T$，再由 (20) 唯一决定同一个 $f$。
不再需要使用首一 $q_f$ 的“至多两个 f”上界。

$\rho^2=\delta$ 最多给两个有序谱选择。
所有 Gram 坐标由原已付线性式唯一恢复。
完整两个值矩在物理 $D\ne0$ 图给
$$
s_{\rm val}=\frac{K}{2mD},\qquad
\zeta=\frac{T+u s_{\rm val}}{\ell},
$$
所以 $\zeta$ 和剩余原值也唯一；这里没有另外增加二次选择。
所有原个别 N/P 和完整 N4(V) 条件只能进一步减少点。

故整个当前 $b_0=0$ 原支的完整有序规范**不同点**满足
$$
\boxed{\#\{\text{完整有序规范原点}\}\le5772\cdot2\cdot2=23088.}
\tag{21}
$$
规范坐标可以取 $(e,k,\rho,\lambda,T,f,\zeta)$，
也可以用原可逆恢复取 $(e,k,\rho,x,y,t,\zeta)$。
这不是未归一原矩阵的自由轨道点数，也不是完整几何商的 scheme 长度或自由秩声明。
5772 的权长度界没有因此被冒充为后续含几何局部化商的自由模界。

此前 46176 界及其实际回执保留为历史记录。
(21) 只重用已刊两曲线／非零二次／完整恢复，加上新已刊全图 f 唯一性；
没有重算原结果式、gcd、二次系数组合、Gram 或任何有限纤维。
整个 b0 原支与整个 W 均未由有限性宣称排空。
