# 首次新输入：整 b0 的原 C2、完整 Loww 与同 lambda 七源投影

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 状态：未执行，不预记 C2、纯 Loww、结式、权核、原单位或排空成功。
- 源：2026-11-28-unit211-W-b0-cross-C2-complete-Loww-same-lambda-seven-source-projections-8542.py。
- Git blob：43638940b02eb65da644a1b2eef4f68c078c4aec。
- SHA256：7a732655b5bf64144f91d6992910ceb67563e4125a12246c12dbb83e1f4f1831。
- 22818 字节；自含零依赖；唯一首次 180 秒、4 GiB，外层可用 195 秒。

## 1. 当前原图和真正新增来源

沿[整 b0 五原二次](../results/R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)的当前 W、distinct-singleton、$D\ne0$ 原范围。所有物理原单位与规范固定；本输入保完整 $I_{11}$。

既有五源是

$$
(E_1,E_{B,e},E_{B,o},N_1,q_2),
\qquad q_2=2a_d/\ell,\qquad C_4=mD\ell q_2.
$$

新的完整输入加入同一个原 Gram 的 NS、PS，固定七源顺序为

$$
\mathcal F=(E_1,E_{B,e},E_{B,o},N_1,q_2,NS,PS).
\tag{1}
$$

新增目标首先是三个原 f 一次余式的叉积二次 C2，以及完整 Loww 的同 f 纯 lambda 条件；随后只做这条新 Loww 参与的两个固定投影。没有重算 1898 的四乘五伴随/h/K，没有重放旧六个 pair/norm 投影、primitive PRS、全十一式或全图六 NS/PS cofactor 门。

原 $q_f,r_i$、真 Gram 和全域 $f+g$ 只按必要定义重建，以提供新目标的原系数和来源。未调用旧 head 因式或旧证明尾段。

## 2. 同一个全支权坐标与 b0 恢复

取

$$
\nu=\frac{(2u-1)(k+2)}{uk+2},\quad
d=u\nu-(2u-1),\quad r=2u-1-\nu,
$$

$$
k=\frac{2r}{d},\quad Q=\frac{2(u-1)r}{d},\quad
\ell=\frac{u(\nu^2-(u+1)\nu+2u-1)}r.
\tag{2}
$$

源码保全部正反权身份及旧已付分母。只在本 b0 整支，既有原值论证支付

$$
A_*=uQ(\nu+2),\qquad
\kappa=\frac{\ell}{\nu+2},\qquad
T=-\kappa(3-2\lambda).
\tag{3}
$$

$\nu+2$ 不用于前面的整个 W 定义，也不外推到全 W。

程序先从自由 T 的完整真 Gram 构造必要四均值、NS、PS 及 qf/ri 系数，再对所有原式、原乘子和同点几何进行同一个 (3) 的多项式代入。代入只使用纯权已付分母；没有专门化尚未支付的参数逆。

## 3. 已刊纯权 f 恢复在此图保持全域

旧首一式和三个余式为

$$
q_f=f^2+q_1(\lambda,T)f+q_0(\lambda,T),\qquad
r_i=A_i(\lambda,T)+B_i(\lambda,T)f.
\tag{4}
$$

由[全域 f 唯一恢复](../results/R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)及[六核完整呈示](../results/R150-appendix-unit211-W-three-pairs-three-same-f-norms-complete-original-I4-presentation.md)，存在纯权 $v_i$ 满足

$$
\sum_i v_iB_i=1,\qquad
f+g=\sum_i v_i r_i,\qquad g=\sum_i v_iA_i.
\tag{5}
$$

新源只按旧必要系数定义得到这些 $v_i$，对每个实际比值先完整约消，核最终分母全是既有原单位，然后返回 (5) 的完整四原源。原 raw 三阶头可能有已取消的公共因子，程序没有把 raw 头当物理单位。

将 (3) 代入后，仍记 $r_i=A_i(\lambda)+B_i(\lambda)f$，且

$$
B_i(\lambda)=B_{i0}+\lambda B_{i1}.
$$

因为旧 v 只依赖权，完整系数比较给出

$$
v\cdot B_0=1,\qquad v\cdot B_1=0.
\tag{6}
$$

因此这个分支上的 f 恢复不依赖新叉积或新 h 非零。源码对 (6) 与同 f 的四原源逐项核回。

## 4. 新 C2 的完整原来源，叉积零面保留

取纯权三向量

$$
\mu=B_0\times B_1.
$$

由叉积的两条恒等式，

$$
\mu\cdot B_0=\mu\cdot B_1=0.
$$

因此新的原条件是

$$
C_{\rm raw}(\lambda)=\mu\cdot A(\lambda)
=\sum_i\mu_i r_i(\lambda,f).
\tag{7}
$$

它对 lambda 次数至多二，完整来自四原均值，而不需反演 $\mu$ 的任何分量或新的首项。

对 (7) 的七源乘子，只清实际已付分母并共同精除全部七个分子，再把新组合完整乘回 (1)；最后只剥旧已付权支持，得到记为 C2 的条件。若原叉积整体为零或新核为零，准确记零并保所有原条件；不从叉积零面推出解不存在。

即使共同精除因子含有几何变量，新核仍必须有完整七源多项式返回、最终纯权已付分母、f 次数零、lambda 次数不超过二；任何一条失败都不能作为数学排空。

## 5. 完整 Loww 与同 f 纯 lambda 条件

自由 T、自由 f 的完整 Gram 给出

$$
E_{W2}=b(2p-u-X)E_B+c(2q-u-Y)E_C
      =c_eE_{B,e}+c_oE_{B,o},
$$

$$
c_e=2u-u\ell-V,\qquad
c_o=2\theta-um-mx-\ell\delta y,\qquad \theta=u-\ell Q.
\tag{8}
$$

源码先在自由 T 图核 (8)，再作同一个 (3) 代入。使用准确的全自由 f 修正：

$$
\begin{aligned}
K_w=2[&t^2+(5u-4x-2)t+2(x^2-\delta y^2)\\
 &+4x+4\delta y-4ux+2u^2-6u+Q],\\
L_w={}&2P_{02}(2\lambda-1)w
       -bc\,t\{K_w+4(f-u)(t-2)\},\\
w={}&\lambda-1-T.
\end{aligned}
\tag{9}
$$

其同一点完整原身份为

$$
L_w=NS-PS+E_{W2}.
\tag{10}
$$

没有将 Loww 称为二次。它对全部几何变量总次数至多三。原七源乘子明确为

$$
(0,c_e,c_o,0,0,1,-1).
$$

对同一个首一 $q_f$ 作短除，

$$
L_w=Q_Lq_f+A_L+B_Lf,
\qquad \deg A_L\le3,\quad \deg B_L\le2.
$$

再用已刊全域同 f 身份，得到真正新的纯条件

$$
P_L=A_L-B_Lg
=L_w-Q_Lq_f-B_L(f+g).
\tag{11}
$$

在 (3) 后它的 lambda 次数至多四。程序完整返回七个原源及全部 f 系数，只约全部七个真实乘子的公共因子，最后只剥旧单位；所有新首项、未知公共因子零面保留。若短除后的实际次数更低，如实输出，不假定四次头非零。

## 6. 两个新固定六阶原投影

只有在 C2、纯 Loww 定义和原来源完整返回之后，才按预定顺序处理

$$
(q_2,P_L),\qquad(C_2,P_L).
\tag{12}
$$

不再计算旧 $q_2/C_2$ 的同 h 兼容关系。每对都固定左容量二、右容量四，使用行

$$
L,\lambda L,\lambda^2L,\lambda^3L,\quad
P_L,\lambda P_L
$$

对 $1,\lambda,\ldots,\lambda^5$ 的六阶系数矩阵。所有实际头零与降次均保留在这个固定矩阵里。

带完整右单位矩阵的 fraction-free 消元，每一步只作精确多项式整除并核乘回。结束时逐 36 坐标核

$$
TM=RI.
$$

于是第一行直接给

$$
R=U(\lambda)L+V(\lambda)P_L,
\qquad \deg U\le3,\quad \deg V\le1.
\tag{13}
$$

把 (13) 复合到 (1) 的七源乘子，仍只共同精除所有实际乘子并完整返原；没有把瞬时主元、左或右的首项、C2 的叉积或 unknown content 付成单位。固定矩阵若奇异，只准确输出这个必要标量为零，保整原支。

若 C2 或 $P_L$ 已是非零纯权式，保其原权条件，不人为升次数计算无用投影。若任何新标量在完整原返回后为非零有理常数，则才报告当前物理整 b0 被排除并结束剩余目标。任何其它情况不宣称排空。

本次没有新的 QQ 多变量 gcd、因式分解、纯 u PRS 或有限纤维门。最多两个新投影都含完整 Loww；未含 Loww 的旧门不重放。

## 7. 原范围、输出与停止边界

全程固定 180 秒、4 GiB、自含、单个 real-time alarm；没有嵌套旧脚本或隐藏较低硬限。前缀只提供新输入必要定义，不运行全图旧 NS/PS 六 cofactor、全十一式、1898 伴随或 10ab 六投影/PRS。

只输出定义、参数次数/字节/SHA、原返回计数与小回执；不输出或保存可重算大系数。任意资源或实现边界按实际最后 checkpoint 冻结，未返的新结式或原单位不补称成功，不增加预算、换序或重派同目标。

这些七源仍只是原完整系统的必要输入。所有 q2/C2/Loww 头零、叉积零和未付权因子整纤维都保持原条件；没有把有限必要参数覆盖当作完整原解或普通不变子空间问题的结论。
