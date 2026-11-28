# R150：全 W 原 D 双列精确取消、e93 曲线与非零纯 k 覆盖

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 范围与完整结论

本文始终在已刊当前 W 原权图及物理 $D\ne0$ 图中工作。保留整个 $L_{1/2}=0$、H198=0、所有未付的多项式首项零纤维；没有将这些因子加入单位表，也没有向一般 $D=0$ 碰撞图外推。

固定
$$
u=e+1,\quad Q=ek,\quad V=(e+1)k+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV},
$$
$$
L=4ke^2-(k^2+4k+8)e-(k^2+6k+8).
\tag{1}
$$
有 $2\ell-1=-L/(kV)$。$L$ 的 $e,k$ 双次数为 $(2,2)$，总次数为 3。

本次完整原式返回给出两个具有固定原定义的权多项式
$$
P'=\frac{P_{164}}{L^2}\in\mathbb Q[e,k],
\qquad Q_*=\det N_* \in\mathbb Q[e,k],
\tag{2}
$$
满足
$$
\deg_{e,k}P'=(93,119),\quad\deg_{\rm total}P'=158,
\qquad\deg_eQ_*\le210,\quad\deg_kQ_*\le284.
\tag{3}
$$
在整个当前 W 的原物理商中，$P'=Q_*=0$。这是原理想的结论，覆盖 $L=0$，并非把旧必要方程任意除以 $L^2$。

固定形式次数为 $93,210$ 的 Sylvester 行列式定义
$$
\boxed{\mathcal K(k)=\det\operatorname{Sylv}_{e;(93,210)}(P',Q_*)\in\mathbb Q[k].}
\tag{4}
$$
本次证据严格证明
$$
\mathcal K\ne0,\qquad \deg_k\mathcal K\le51402,
\qquad \mathcal K(k)=0
\tag{5}
$$
对所有当前原物理点成立，包括两多项式的首项降次处。式 (4) 是完整固定定义；其 QQ 系数尚未展开或因式分解。

更直接地，两条原曲线没有未付共同分量，双次数 Bézout 给出整个当前 W 的权商长度至多 $51402$，继而
$$
\boxed{\dim_{\mathbb Q}\mathcal A_{\rm mean}\le308412,\qquad
\dim_{\mathbb Q}\mathcal A_{\rm normalized}\le616824.}
\tag{6}
$$
最后一个商采用固定七坐标 $(e,k,\rho,x,y,t,\zeta)$，包含完整原条件和所有非约化重数。这不是整个 W 排空，也不是未经规范化的矩阵轨道数。所有有限候选仍须同点返回。

## 2. 原六行与同一个 D 目标

令
$$
v=(1,x,y,t,y^2,yt)^T,\qquad F_6=(E_1,E_{B,e},E_{B,o},N_1,N_S,P_S)^T,
$$
并以 $F_4$ 表示前四式。沿用[全域 native 原六行定理](R150-appendix-unit211-W-entire-original-native-NSPS-necessary-weight-curve.md)的固定次序
$$
N_S,\ P_S,\ yN_S,\ tN_S,\ yP_S,\ tP_S.
$$
清除的分母和行内容全部为该定理已付的 native 权单位。所得多项式矩阵 $M$ 满足完整原身份
$$
Mv=\Theta F_6,\qquad
\det M=c\,U\,P_{164},\quad c\in\mathbb Q^\times,
\tag{7}
$$
其中 $U$ 为同一权单位积。$P_{164}$ 双次数 $(97,123)$、总次数 164。

本次只重建 $M$ 的必要定义，不重跑旧 QQ 行列式。六行定义串 1,728,830 字节的 SHA-256 为
e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf。

对同一个原量
$$
D=\ell A_2-T^2,\qquad A_2=2\lambda^2-2\lambda+1
$$
应用既有六规则并完整保留原乘子，只清已付分母 $b_D$，实际返回
$$
d\,v=b_DD+\tau F_4.
\tag{8}
$$
$b_D$ 是权单位。本次并未倒置几何 $D$ 来生成这条身份。实际 $d$ 的分母定义双次数 $(11,15)$、总次数 22、109 项，SHA-256
0b63aa2e51ac3f71129c4cfaec89f7eebeab5e970b596ded1705cb80d2a8ff6c。

## 3. 矩阵和目标的同时精确取消

令 $C$ 为单位矩阵仅将第零列改为
$$
c_0=(1,\tfrac12,\tfrac12,0,\tfrac14,0)^T.
$$
因此 $\det C=1$，第一列仍为 $c_x=(0,1,0,0,0,0)^T$。对任意行 $r$，
$$
rC=(r_0+\tfrac12r_1+\tfrac12r_2+\tfrac14r_4,\ r_1,r_2,r_3,r_4,r_5).
$$
QQ 双数族说明选择这两列的原几何来源；本次仍对实际 QQ 多项式逐项精确整除并乘回，建立
$$
MC=N\Lambda,\qquad dC=d'\Lambda,\qquad
\Lambda=\operatorname{diag}(L,L,1,1,1,1).
\tag{9}
$$
所有六个坐标的正向和反向身份都实际返回。特别地，反向第零坐标是
$$
r_0=Lr'_0-\tfrac12Lr'_1-\tfrac12r'_2-\tfrac14r'_4.
$$
不存在 $L^{-1}$。

交换环上的伴随身份直接给
$$
\boxed{\det(N)d=d'\operatorname{adj}(N)M.}
\tag{10}
$$
证明是将两边右乘 $C$，利用 (9) 和 $\operatorname{adj}(N)N=\det(N)I$，最后仅用常数矩阵 $C$ 可逆。

合并 (7)、(8)，得到完整原理想身份
$$
\det(N)b_DD
=d'\operatorname{adj}(N)\Theta F_6-\det(N)\tau F_4.
\tag{11}
$$
它在整个 $L=0$ 仍成立。本次不必展开伴随的巨型系数；(7)–(10) 的全部实际原矩阵身份和普遍伴随公式已经给出完整原组合定义。

同时 $\det M=L^2\det N$。此前[完整 QQ 双数族](R150-appendix-unit211-W-generic-original-dual-family-D-return-and-finite-physical-support.md)在整个
$\mathbb Q(k)[e]/(L)$ 上实际支付 $U$ 的全部 native 因子，故 $L$ 与 $U$ 在该一元环中互素。$L$ 关于 $e$ 在 $\mathbb Q[k]$ 上本原，因为 $4k$ 与 $k^2+4k+8$ 互素。因此在 UFD $\mathbb Q[e,k]$ 中，
$$
L^2\mid P_{164},\qquad \det N=cUP'.
\tag{12}
$$
(3) 的 $P'$ 三个确切次数由乘积次数相加得到，不是模次数猜测。由 (11)，只在最后使用本图原 $D,b_D,U$ 单位，得到整个物理原商中的 $P'=0$。

## 4. 一条真正新原交换子行

原三轴乘法行满足
$$
a\,v=M_av+E_aF_4,\qquad a=x,y,t.
$$
因此在真实值列上，
$$
(M_aM_b-M_bM_a)v
=(aE_b-bE_a+M_bE_a-M_aE_b)F_4.
\tag{13}
$$
不要求六个生成元自由，也没有将两个裸矩阵直接宣布为交换。

本次唯一实际有用的新行是
$$
r_*=(M_xM_y-M_yM_x)_{4,*},
\tag{14}
$$
即对应基元 $y^2$ 的行。源码完整返回 (13)，按原 native 单位清分母和内容，并对这一实际多项式行同样建立 (9) 的两列精确整除。其被取消后的行双次数上界为 $(30,41)$、4775 项，SHA-256
3c51635281b8312c2c352bdc4463fd4dd9f6de09d0a603bd12898a4985493f17。

将 $M$ 第零行替换为该原行，得到 $M_*$，相应被取消矩阵为 $N_*$。式 (10) 对同一个原 $d$ 仍成立，所以
$$
Q_*b_DD\in I_6,\qquad Q_*=\det N_*.
\tag{15}
$$
同样整个 $L=0$ 保留。实际六行的双次数上界依次为
$$
(30,41),(28,37),(36,49),(40,54),(36,49),(40,54).
$$
行列式每项每行取一项，故得到 (3) 的 $(210,284)$ 上界。没有宣称这两个上界就是实际次数；$Q_*$ 的 QQ 行列式没有被展开。

## 5. 完整特化与 Gauss：只有无共同曲线结论

固定 $p=1009,k=3$ 在任何新行选择前已经给出。由[P164 整模型及无竖直分量定理](R150-appendix-unit211-W-native-P164-integral-specialization-no-vertical-component-and-local-weight-model.md)，在
$$
A=\mathbb Z_{(1009)}[k]_{(1009,k-3)}
$$
中可将 $P_{164}$ 对 $e$ 首一化。$L$ 的 $e$ 首项 $4k$ 在 $A$ 为单位；对首一 $L^2$ 的精确除法因此也给出 $P'$ 的同一局部首一模型。其约化的 $e$ 次数保持为 93。

从新 $N$ 计算的固定一元行列式实际为 $e191$。55 个 Bareiss 商积完整返回；只剥原 native 单位支持的总次数 98，得到首一
$$
\overline P'(e)\in\mathbb F_{1009}[e],\qquad\deg\overline P'=93.
$$
完整乘积、平方自由及与 $\overline L$ 互素都已返回。$\overline P'$ 定义串 364 字节，SHA-256
a4299c51c7278f5b39c5e46f6a0a768378ac0a333a63162ffab772097dc3caab。

新原交换子行的每个 QQ 系数均实际作 $p$ 整性检查，并在完整 $\overline P'$ 代数里核对原 paid 行尺度。由行列式的多线性，算出的余式正是同一个 $Q_*$ 的约化对 $\overline P'$ 的余式，次数 92，SHA-256
ce1a4e7fcc8549b792bac0abe0a84b594fd3a90e266378f90a5ad26fb68d0cf2。

唯一一个替换行列式已经给出
$$
s(e)\overline P'(e)+t(e)\overline Q_*(e)=1.
\tag{16}
$$
全部乘积实际加回 1，Bézout 定义串 734 字节，SHA-256
23b1a8c1a0c8ce6eae4768ac05a56bdf4ad1c9eaaab5c3d084efbbdcb5bbed63。
这里 $\overline Q_*$ 可用其完整余式书写，差别只是改变 $s$。

假若 $P',Q_*$ 在 $\mathbb Q(k)[e]$ 中有共同正次因子，将其首一化。因 $P'$ 在整闭环 $A$ 上首一，Gauss 引理给这个首一因子和相应商均在 $A[e]$；它整除 $Q_*$ 的商也因首一除法而在 $A[e]$。约化后该因子仍首一正次，与 (16) 矛盾。因此
$$
\gcd_{\mathbb Q(k)[e]}(P',Q_*)=1.
\tag{17}
$$
这不是从多变量模理想为空推出 QQ 理想为空；(17) 只排除共同的非竖直曲线分量，所有有限交点保留。

源码还实际验证 $\overline Q_*e^j$、$0\le j<93$ 的 93 个系数列满秩，8649 个逆坐标乘积全返。全部列正是同一 $Q_*$ 的连续幂倍数。它给出的 93 阶伪余式覆盖次数上界为 1,841,400；下面直接利用同一已成原式得到更小且更明确的 (4)，不再运行一个新门。

## 6. 固定 Sylvester 覆盖与全部首项零

以确切 $e$ 次数 93 的 $P'$ 和形式 $e$ 次数上界 210 的 $Q_*$ 定义 (4)。这是固定 303 阶矩阵：210 行为 $P'$ 的适当单项式倍数，93 行为 $Q_*$ 的适当倍数。

设 $a(k)=\operatorname{lc}_eP'$，实际 $m=\deg_eQ_*\le210$。在 $\mathbb Q(k)$ 上，
$$
\mathcal K(k)=\pm a(k)^{210-m}\operatorname{Res}_e(P',Q_*).
\tag{18}
$$
由 (17)，右端非零。也可直接在本次固定整特化核非零：$\overline P'$ 保持 93 次，$a(3)$ 是单位，(16) 使真实特化结式非零；即使 $\overline Q_*$ 降次，形式次数只额外乘 $a(3)$ 的幂。因而无需将 $Q_*$ 的任何首项支付成单位。

每个行列式单项式包含 210 个来自 $P'$ 的系数和 93 个来自 $Q_*$ 的系数，故
$$
\deg_k\mathcal K\le210\cdot119+93\cdot284=51402.
\tag{19}
$$
这个固定 Sylvester 行列式在任一共同有限根 $(e,k)$ 上都有非零 Vandermonde 核列。因此 $P'=Q_*=0$ 必迫 $\mathcal K(k)=0$，包括 $a(k)=0$ 和 $Q_*$ 首项为零处。没有在这些纤维上使用 (18) 除法；适用它们的是原固定多项式矩阵身份。

QQ 系数未展开、未作分解、未给出所有根表。已成结论是有非零、次数有界、源定义固定的纯 $k$ 覆盖。

## 7. 双次数交长和完整规范界

已付无竖直分量定理说明 $P_{164}$ 的 $\mathbb Q[k]$ 内容只含原已付纯 $k$ 因子。除去 $L^2$ 不会引入新的竖直内容，所以 $P'$ 同样没有未付的竖直分量。

将 $P'$ 的纯 $k$ 内容剥去，只是在已有权单位环中换一个同理想生成元；所得多项式记 $P_0$。由 (17)，$P_0,Q_*$ 在 $\mathbb Q[e,k]$ 中没有共同不可约因子。特别地，未将两变量 gcd1 误认为单位理想：它们仍可有有限交点。

这两条仿射曲线的闭包在 $\mathbb P^1_e\times\mathbb P^1_k$ 上没有共同分量。采用各自实际双次数齐次化，不额外填入无穷远边界分量；其次数分别不超过 $(93,119)$ 和 $(210,284)$。双次数 Bézout 的交数为两个交叉乘积之和，所以包括全部非约化结构的仿射交长至多
$$
93\cdot284+119\cdot210=51402.
\tag{20}
$$
其余纯权单位局部化只删除有限 Artin 分量，不增加长度。这给当前全 W 的原权商上界，而非仅 $H198\ne0$ 或 $L\ne0$ 的开图界。

原 native 六生成元在整个当前权图上成立；在 (20) 的有限权环上基变换并加入其余原方程，均值商长度至多 $6\cdot51402=308412$。这里不要求六个生成元自由。

$\rho^2=1-Q$ 是首一二次，最多再乘二。完整 HA/HB 在本图原单位 $\ell,m=u-\ell,D$ 上唯一恢复
$$
\zeta=\frac{T+uK_{\rm moment}/(2mD)}{\ell},
\qquad K_{\rm moment}=\ell^2B_3-3\ell TA_2+2T^3.
\tag{21}
$$
其余规范权、Gram 和值坐标由同一原图恢复。此时几何 $D$ 局部化发生在已有限的 Artin 环中，只删除分量；完整个别 N/P 再取商也不能增加长度。故 (6) 的 $616824$ 界保留所有非约化重数和所有允许的有限纤维。

## 8. 唯一实际执行和保存边界

源：
[2026-11-28-unit211-W-entire-D-two-column-cancellation-first-finite-k-cover-8542.py](../notes/2026-11-28-unit211-W-entire-D-two-column-cancellation-first-finite-k-cover-8542.py)。

源 blob a29b26b6f5bee924ea7f4ee8e35f76d60ae08fd3，19002 字节，SHA-256
d325a48ae84c1142eed3a1d087670d2e2a139425c4e5d74bd97b8e36a40470c8。
唯一首次 run46099681457 / job140839055797，source commit
0a352d576d8b8df88813e67ac27bd2c862b00e18。

原 D 双列完整身份在 11.410195648 秒返回，新 e93 模型在 11.693638429 秒返回，唯一新 QQ 交换子行在 12.868018290 秒返回，完整 Bézout 在 12.869330813 秒返回，93 列及全部结束标记在 13.086716220 秒返回。驱动 13.166233637 秒，峰值 RSS 94152 KiB，真实内层退出码 0。

计数为 28 个 QQ 精确列除法乘积、110 个新模多项式 Bareiss 商积、109454 次实际整系数检查、31 个完整残余代数真逆及 8649 个选中系数矩阵逆坐标乘积。第一原候选已经给完整 gcd1，无需后续候选或参数/素数重试。

2026-11-28 02:46:31.873873 UTC 真实 pull 从 source commit 到
7e527749e2bac983d21846051d560f7c36c694de。
两 README blob 仍为
282e86b03385d3b6245ce7100ae2e2af7b103c2d、
5fbd905291dd044c88d35bd9c07ac0e586ff795a，均无变化。

stdout 7593 字节，SHA-256
ce1c3755cd0d8934c0787383011d56e61bbdf60d673724fc720751bcc40f076b。
[实际小回执](../notes/2026-11-28-unit211-W-entire-D-column-finite-weight-cover-actual-receipt-8542.json)保留完整阶段、计数和定义 SHA。

总限 180 秒 / 4 GiB。仅执行旧 native 源 8074 字节必要原行前缀及原 C9 定义，未重跑旧 95 秒 QQ determinant、旧六范数、特征多项式或 primary 门。新固定 303 阶 QQ 覆盖由第 6 节普遍代数身份定义，不冒充已展开计算。

只保存源、参数定义、SHA 和小回执，没有可重算系数缓存、编码或分片。全 W 的有限候选、其完整原值返回以及普通无限维 ISP 均继续开放。
