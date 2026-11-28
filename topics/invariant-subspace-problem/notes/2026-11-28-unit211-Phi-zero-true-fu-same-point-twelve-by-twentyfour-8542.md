# 新输入：正确 Phi 的 f=u 支，同一点十二坐标原行容器

日期：2026-11-28（Asia/Taipei）。源尚未执行；SHA256 e35e019e9ee84448b8e4e5afc31c81f449b8b515598329e2fb8c2e38d4870aa6。120 秒、1 GiB，全部必要前缀共享最初的绝对截止。

## 1. 原范围和既有三次曲线

沿用[正确整 t=0 排除](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)、[f=u 整 u=3/2 排除](../results/R150-appendix-unit211-Phi-zero-fu-entire-u-three-half-original-exclusion.md)及[刚完成的原单 y 权曲线](../results/R150-appendix-unit211-Phi-zero-true-fu-single-y-common-weight-curve.md)。这是当前 $D_{\mathrm{val}}\ne0$、非零孤立均值的真实 Phi 图，不借旧错误 Rbar 的头或单位。

记 $s=u-1,\ \delta=1-Q,\ L=Q-2s(u-2),\ K=Q+4s$，
$$
M_n=2uL-L^2-u^2Q,\qquad
y=4s^2-Q+2L\lambda .
$$
只使用原权单位
$$
Q\delta sKLM_n(2u-3).
$$
先前原 cofactor 已经实际给出
$$
\begin{aligned}
\Psi={}&Q^3+(-10u^2+24u-15)Q^2\\
&+(32u^4-152u^3+276u^2-228u+72)Q\\
&-32u^6+224u^5-672u^4+1104u^3-1040u^2+528u-112
\end{aligned}
$$
属于同一点原五值理想。其对 $Q$ 首一三次。这里按已刊小式读取它，并校对 $\Psi/4$ 的已存 SHA；不会执行旧三个 cofactor 或旧 GB。

## 2. 固定十二坐标只作原多项式容器

从原单 y 源的 det 定义前取必要原 Gram 定义，得到
$$
E=E_{\mathrm{Be}},\quad O=E_{\mathrm{Bo}},\quad
N=N_1,\quad S=N_S,\quad P=P_S,
$$
前三条对 y 至多二次，后两条至多三次。仅清已付分母和已付行内容，原尺度逐项乘回。

令 $\widetilde E,\ldots,\widetilde P$ 为所得五条多项式。新输入为
$$
Q^i\{\widetilde E,y\widetilde E,\widetilde O,
 y\widetilde O,\widetilde N,y\widetilde N,
 \widetilde S,\widetilde P\},\qquad i=0,1,2.
\tag{1}
$$
对每一项按首一 $\Psi$ 作真正单变量 Q 短除，完整返回原多项式等于商乘 $\Psi$ 加余式。再在
$$
\mathcal V=\bigoplus_{\substack{0\le i<3\\0\le j<4}}
 \mathbb Q[u]\,Q^iy^j
\tag{2}
$$
的十二坐标中记录其余式，形成十二行、二十四列的原来源矩阵。

$\mathcal V$ 仅是固定次数原多项式的自由容器。没有把它当作完整 y 商代数；没有支付 $y^4$ 的约化，也没有假定任何未知 y 首项非零。所有 $\Psi$ 复嵌入及非约化纤维由首一多项式整商完整保留。

## 3. 新原目标与全部 pure-u 极点

在 $\mathbb Q(u)$ 中进行原列消去，仅为选择和构造组合。源码每一边都先在 $\mathbb Q[u]^{12}$ 返回
$$
g\,v_{\mathrm{new}}=b\,v_{\mathrm{old}}-a\,v_{\mathrm{pivot}},
\tag{3}
$$
并记录有理乘子 $b/g,-a/g$ 和原来源 DAG；不把任何临时 $u$ 主元当物理单位。

按顺序测试两个真正新目标：

1. 常数向量 $1$；
2. 原 $D_{\mathrm{val}}=\ell(2\lambda^2-2\lambda+1)-T^2$ 的实际分子，先完整模 $\Psi$ 短除。

在原值点
$$
D_{\mathrm{val}}=\ell A_2-T^2=bc(h-k)^2.
\tag{4}
$$
第二项只作正目标，不倒置它或其范数。其权分母均来自既有单位。

每个目标都完整返回十二坐标等式。若目标余式不为零，不宣称单位或排空。若目标为零，则只汇集实际可达 DAG 边、原种子尺度及终端组合的 pure-u 分母。令其 LCM 为 $\delta_u$，实际最大 DAG 深度加一为 $n$；由 (3) 沿深度归纳得到
$$
\delta_u^n\,\mathrm{target}
 \in(\widetilde E,\widetilde O,\widetilde N,
     \widetilde S,\widetilde P,\Psi).
\tag{5}
$$
五行尺度只用原已付权；$\Psi$ 已有完整同源原理想身份，故 (5) 是原五值理想中的真实身份。

剥 $\delta_u$ 中已有的原权单位支持后记余项 $C(u)$，仍有
$$
C(u)^n\,\mathrm{target}\in I_{\mathrm{original}}.
\tag{6}
$$
当前原点上 target 为 1，或为原非零 $D_{\mathrm{val}}$ 乘已付分母，所以必有 $C(u)=0$。整个未付纯 u 零集保留。只有实际 $C$ 为非零常数才能关闭当前整个 f=u 支；泛型 rank 或 $\mathbb Q(u)$ 中的单位本身不作全支排空。

若 $\deg C=d>0$，只给不同 u 值至多 d、不同 $(u,Q)$ 权对至多 $3d$，因为 $\Psi$ 对 Q 首一三次。没有据此宣称固定权处的全部 y 纤维有限。

## 4. 资源和依赖

先输出已经返回的原目标与覆盖，再可选精确分解新 $C$；因式乘回和平方自由幂整除均实际核对。未得目标、触边界或后续因式未返回时，逐项保准确状态，不重启旧计算。

仅两个规范源依赖：

- 2026-11-28-unit211-Phi-zero-true-fu-single-y-original-scalar-cofactors-8542.py，SHA 9d591ab41ed41cc7dbee8ac3e9ce326ef68348455751ae9ad1cea954a7d463cb；
- 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

前一份只截取 det 定义前的必要原五值；后一份只提供原算术。无 JSON 参数载荷，无原投影或旧清 LCM 重播。
