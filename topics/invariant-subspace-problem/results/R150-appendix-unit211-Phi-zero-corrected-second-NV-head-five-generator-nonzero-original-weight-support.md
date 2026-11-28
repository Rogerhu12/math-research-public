# R150：正确 Phi 第二 NV 头的五条原交换差列与非零纯权支持

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**结论。** 在当前正确 Phi、物理 $D\ne0$ 的整个第二 NV 头图上，存在由五个实际原列唯一规定的整数多项式
$$
F_{\rm wt}(u,Q)=\det\mathsf B(u,Q)\ne0
$$
作为必要条件，并有
$$
\boxed{\deg_uF_{\rm wt}\le142,\qquad
       \deg_QF_{\rm wt}\le72,\qquad
       \deg F_{\rm wt}\le142.}
\tag{1}
$$
这里 $\mathsf B$ 是本稿第4节精确定义的 $5\times5$ 原矩阵。首次实际执行在事前固定的 $p=1009,(u,Q)=(2,2)$ 返回
$$
\det\mathsf B(2,2)=382\pmod {1009}.
\tag{2}
$$
没有展开整个 QQ 行列式，也没有对其因式、内容、实际次数或零集非空性作新判断。完整 $F_{\rm wt}=0$ 权纤维全部保留；本结论不是整个第二头或整个 Phi 的排除。

本稿使用[第二头五生成原代数](R150-appendix-unit211-Phi-zero-corrected-second-NV-head-global-four-head-unit-and-five-generator-algebra.md)的显示结构，以及已经独立完成的[第二头与 ell=3/2 完整交集排除](R150-appendix-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-complete-original-exclusion.md)。后者只在当前第二头支付 $3-2\ell$，没有被外推到其他图。

## 1. 原系数环和三个完整原式

记
$$
s=u-1,\quad\delta=1-Q,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
K_w=Q+4s,\quad T_0=-K_w,\quad
J=Q-4s^2,\quad P_{02}=2sL,\quad
M_n=2uL-L^2-u^2Q .
$$
本次系数环为
$$
A=\mathbb Q[u,Q,\mathcal U^{-1}],\qquad
\mathcal U=Q(Q-1)sK_wLM_n(uQ-L)(3Q-2L).
\tag{3}
$$
所有因子都有当前正确物理图的原单位来源。特别 $m$ 来自已核的完整等权原排除，而 $3-2\ell$ 来自前述新交集排除；本源没有倒置 $D,t,\lambda,\sigma$ 或 $f-u$。

第二头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0
$$
给
$$
a=\lambda-\frac32,\quad
j=\ell\left(\lambda-\frac12\right)-m\sigma,\quad
T=j-\ell,\quad w=\lambda-1-T,
$$
$$
E=\frac{P_{02}j}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
\theta=u-\ell Q.
$$
完整两个矩为
$$
E_2=\ell a^2-2ma\sigma+\ell\delta\sigma^2-A_\lambda,
$$
$$
E_3=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2
                         -m\delta\sigma^3-B_\lambda,
\tag{4}
$$
其中 $A_\lambda=2\lambda^2-2\lambda+1$、
$B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1$。

真 dual-germ 极化给完整
$$
N^\sharp=2\left[
-\left(\lambda^2+\lambda-\frac34-\delta\sigma^2\right)f
+(a^2-\delta\sigma^2)E-w(ua+\theta\sigma)\right],
$$
$$
NV=N^\sharp-2fE_2 .
\tag{5}
$$
源码另对已经成立的幂等元紧凑定义逐普通系数核回 (5)。这里用的是完整 $NV$；没有把只在 $E_2=0$ 后相等的 $N^\sharp$ 偷换成完整原式。

以下令
$$
\mathbf F=(E_2,E_3,NV)^t,\qquad
I=(E_2,E_3,NV)\subset A[\lambda,\sigma].
$$

## 2. 原五生成动作与五个真实交换差

按三次基
$$
(\lambda^3,\lambda^2\sigma,\lambda\sigma^2,\sigma^3)
$$
取四原式 $\lambda E_2,\sigma E_2,E_3,NV$ 的头矩阵 $H$。本次实际构造并核回
$$
\det H=2P_{02}m\delta(3-2\ell).
\tag{6}
$$
它是 (3) 的单位。固定三阶 cofactors 给 $H^{-1}$，两向共32坐标全部实际返回。四个三次单项式因而各有完整普通原表示，其余式总次数至多二。再以 $E_2/(\ell\delta)$ 消 $\sigma^2$，得到真实生成集
$$
\mathcal B=(1,\lambda,\sigma,\lambda^2,\lambda\sigma).
\tag{7}
$$
它不被假定为自由基。

固定先降总次数至少三、后消 $\sigma^2$ 的次序。对 (7) 的每项分别乘 $\lambda$ 和 $\sigma$，实际得到两矩阵 $M_\lambda,M_\sigma$ 及十组普通原标签：
$$
\lambda\mathcal B_j
=\mathcal B M_\lambda e_j+\tau^\lambda_j\mathbf F,
\qquad
\sigma\mathcal B_j
=\mathcal B M_\sigma e_j+\tau^\sigma_j\mathbf F .
\tag{8}
$$
十个普通多项式身份全部回乘；所有约消后分母只含 (3)。

固定五列
$$
c_j=(M_\lambda M_\sigma-M_\sigma M_\lambda)e_j
\qquad(0\le j\le4).
$$
每列有显示原来源
$$
\mathcal Bc_j=
\left[
-\lambda\tau^\sigma_j
-\sum_i(M_\sigma)_{ij}\tau^\lambda_i
+\sigma\tau^\lambda_j
+\sum_i(M_\lambda)_{ij}\tau^\sigma_i
\right]\mathbf F .
\tag{9}
$$
五个 (9) 全部实际返回，非零种子恰为 $c_3,c_4$。这不是把两个裸矩阵视作交换乘法：交换差本身就是有原理想来源的列。

若 $\mathcal Bv=\Omega\mathbf F$ 已成立，实际子列 $M_\lambda v$ 使用
$$
\mathcal B M_\lambda v
=\left[\lambda\Omega-\sum_i v_i\tau^\lambda_i\right]\mathbf F,
\tag{10}
$$
$\sigma$ 同理。每个被生成的子列均逐普通系数返回 (10)。

## 3. 唯一固定点实际选出的原 DAG

在任何秩选择之前，唯一预定点
$$
p=1009,\qquad (u,Q)=(2,2)
\tag{11}
$$
的原单位乘积实际为625；全部动作与种子的实际分母也逐项合格。这里没有指定原几何 $\lambda,\sigma$ 值。

固定队列处理11个候选后，选出的五个对象依次为
$$
v_1=c_3,\quad v_2=c_4,\quad
v_3=M_\lambda c_3,\quad
v_4=M_\sigma c_3,\quad
v_5=M_\sigma M_\lambda c_3.
\tag{12}
$$
最后一项保持显示的动作次序；未假定 $M_\lambda M_\sigma=M_\sigma M_\lambda$。
其 DAG 深度为 $0,0,1,1,2$，模主元依次为 $0,1,2,3,4$，真实模秩五。

Gaussian 余向量只用于决定独立性。保留并参与后续 QQ 身份的始终是 (12) 中未经 Gaussian 改写的原列与其原标签。本次共返回8条新 DAG 子列；不存在把有限域逆或 Gaussian 余向量混进原 QQ 来源的步骤。

## 4. 精确定义整数矩阵和纯权多项式

对 (12) 的第 $j$ 列：

1. 取五个实际约消后系数分母的首一 LCM $d_j\in\mathbb Q[u,Q]$；
2. 将 $d_jv_j$ 的有理系数分母用正整数 $k_j$ 清掉；
3. 除其全部整数系数的正公因子 $c_j^{\rm int}$。

定义
$$
\gamma_j=\frac{k_jd_j}{c_j^{\rm int}},\qquad
\mathsf B_j=\gamma_jv_j\in\mathbb Z[u,Q]^5,\qquad
\mathsf B=(\mathsf B_1,\ldots,\mathsf B_5).
\tag{13}
$$
这些步骤和首一规范均由冻结源码唯一规定。只除非零有理常数内容，未除任何未付权多项式。每个 $\gamma_j$ 都是 (3) 的权单位乘非零有理常数。

本次五列各五坐标的整化等式全部返回，且同一 $\gamma_j$ 同时乘到全部三个原标签：
$$
\mathcal B\mathsf B_j
=\Omega_{1j}E_2+\Omega_{2j}E_3+\Omega_{3j}NV .
\tag{14}
$$
全部15个最终标签都保留普通原来源，实际分母逐项只含 (3)。

整数矩阵的25个条目全非零，总计6527项。其全部条目 profiles 的 SHA256 为
$$
\texttt{a0991ac91cf3fd9a839e5853c6f88861c3d9c17ac57c7b456076bd344a70bda4}.
$$
这里只给定义与小 profiles；没有保存或编码系数载荷。

定义 $F_{\rm wt}=\det\mathsf B$。普遍 adjugate 恒等式给
$$
\mathsf B\operatorname{adj}(\mathsf B)e_0=F_{\rm wt}e_0.
$$
结合 (14) 与 $\mathcal Be_0=1$，直接得到完整原身份
$$
\boxed{
F_{\rm wt}
=\sum_{r=1}^{3}
\left(\sum_{j=1}^{5}
\operatorname{adj}(\mathsf B)_{j0}\Omega_{rj}\right)\mathbf F_r
\in I.}
\tag{15}
$$
(15) 成立于原已付系数环的普通多项式理想。它不要求五生成商自由，不要求 $\mathsf B$ 在某个整个开图可逆，也不丢临时模主元零面。普遍 adjugate 已提供完整精确来源，所以不必展开巨大 QQ 行列式或它的全部三原乘子。

## 5. 非零性、次数和保留范围

在同一固定点 (11)，源码对整数列尺度逐项核非零，再返回真实 $\mathsf B(2,2)$ 的完整双向逆，合计50坐标。其行列式为 (2)，所以所定义的 QQ 多项式 $F_{\rm wt}$ 确实非零。

对实际非零整数条目，分别按 $u$ 次数、$Q$ 次数、总次数枚举五阶120个匹配。最大权和依次为142、72、142，得到 (1)。这只是严格上界；没有断言最高项不相消，也没有从模点非零常数推出保度。

由 (15)，整个当前第二头的原物理点都投到 $F_{\rm wt}=0$。因此本次支付的是一个定义明确的非零纯权必要支持。它没有给出：

- $F_{\rm wt}$ 的实际次数、因式分解或原始内容；
- 其与先前其他支持的 QQ gcd；
- 权零集上的原完整纤维排除；
- 原物理点总数、整第二头空性或整 Phi 空性。

前篇的五生成及加入首一 $t^2$ 后十生成结论继续成立于未作几何 $D$ 局部化的必要代数；随后取原单位开集不会增加维数。这里不把该事实改写为自由模，也不把有限纤维与非零支持曲线等同于零维或空集。

## 6. 唯一实际执行与可核来源

冻结源：

[2026-11-28-unit211-Phi-zero-corrected-second-NV-head-five-generator-original-commutator-weight-support-8542.py](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-five-generator-original-commutator-weight-support-8542.py)

源 Git blob **d2de722a2e2dc270979676f3456876f9055b1b4e**，16501字节，SHA256：

**8b6155be7e54a2e84866869e9427a486731522583364f39aa2ccb7d8749dcb54**。

[派发前 input](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-five-generator-original-commutator-weight-support-8542-input.md) 的最终 blob 为 **3a4bd3476eb3d4672a17d439d3baf9c24b5ba491**。本源零依赖，内层120秒/1 GiB，外层135秒；没有重放旧 scalar/gcd 或资源冻结门。

唯一 [Actions run 46182910418](https://github.com/Rogerhu12/math-research-public/actions/runs/46182910418)，job **141096296646**，attempt 1。内层真实 exit 0，driver **1.4510202269999866秒**、峰值 **46140 KiB**；最后数学记录 **1.3834710950000044秒**。

source commit **3a2ebf63bb0f459717d5e95af596599a6bad0367**。运行前真实 pull 到 **2931f7834c7708757ecfde8874dd8b2430a0f4e3**，时间 **2026-11-28T19:46:41.406741Z**，两个 README blobs 均未变化。

本人亲读全部四条数学记录并重新拼回 stdout，字节 **6315**、SHA256：

**89039058145ab52b864603321a83fb5eaeb0c36570e6bfa45a9cb875f6b4e167**。

最终统计：原 NV 全式返回1次；头双逆32坐标；十条普通动作全部返回；交换差5列；新 DAG 原返回8次；整原列5列；模双逆50坐标；完整精除乘回8615次；44项实际分母审核。所有数学结论来自真实记录与显示身份，不从 workflow 颜色推断。

[小执行回执](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-five-generator-original-commutator-weight-support-8542-execution.json) 保存实际元数据和 profiles，不含可重算的大系数。
