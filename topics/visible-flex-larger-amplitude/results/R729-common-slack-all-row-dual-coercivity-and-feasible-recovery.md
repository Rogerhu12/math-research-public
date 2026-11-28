# R729. 完整 common-slack QP 的正象限强制有界、全行坐标收敛与可行恢复

日期：2026-11-28 UTC。会话：Astra-larger-e4e2a2bf-20261126 / root。

**状态：以下有限维准确算术命题已证明；新求解方法尚未科学执行。** 本条解决原恢复 QP 的一种实际停止机制。它不证明新的曲面、非线性可行性、准确 reach 或课题完成，也不改第31组已经锁定的运行体。

[R683](R683-all-old-row-constrained-second-order-correction.md) 已证明完整行半空间投影的对偶、KKT 与单坐标更新；这些结论直接沿用。本条新增的结构是：原恢复问题的每一行都含严格同号的公共 slack 列，因此奇异 Gram 在非负正象限上仍有二次强制有界性；由此可完整证明循环坐标法的极限最优性。另给任意物理步的逐全行可行 slack 恢复和原始上界、对偶下界，不删除近相关行。

## 1. 已返回事实和未返回事实

run46099929359/attempt1 的**原第一段** science 和 pure 均自然返回0。其 pure 的首个 restoration QP 投影为：

| 字段 | 原实际值 |
|---|---:|
| status | dependent_blocker_at_zero_step |
| advances | 2 |
| final_face_projected_gradient_norm | 0.529460169023458 |
| gradient_tolerance | 5.305849371949155e-7 |
| 原几何行 | 192 |
| amplitude 行 | 11 |
| permanent envelope 行 | 10 |
| 原全部行 | 213 |
| 加公共 slack 及非负 slack 行后 | 214 |
| 原行 cache 字节 | 2272062480 |
| 其中已知 prefix 字节 | 2165392880 |
| prefix_rewritten | false |

这是第一个方向的字段，不把其停止原因推广为全部4个方向。该次原 science 总共接受4个 restoration，最终 g=.5225620087197518、Gram=.40616533555531326，仍不可行。第25组当前同源 restart 是另一段原算法运行，不把本条算成它的运行结果。

原 QPv3 对 inactive 且 C_i d>0 的行取真实余量比；当最小阻挡步长不超过1e-15，调用 ActiveFace.add。该函数对完整行做两次正交化；若新正交分量不超过 rank_tolerance·max(1,原行范数)，返回未加入，随后原求解器报告上述 status 并停止。此处保留真实最后梯度，没有伪称 KKT。

实际小报告没有返回阻挡行号、它的正交分量或原 transition 全表。因此不能断言该行精确冗余、某个特定相消导致错误，或调小 rank_tolerance 就能修好。确认的是：这一个原有限恢复 QP 在2次 advance后停下，而报告的面投影梯度远未达到原容差。新方法针对无需行独立性的同一 QP，不借猜测的行号删约束。

## 2. 原问题的完整准确表达

设原物理步坐标 z∈R^n，原全部 m 个物理不等式为

\[
g_i+a_i^Tz\le \tau,\qquad i=1,\ldots,m,\qquad \tau\ge0.
\]

这里 a_i 包含原坐标映射、原归一化逆尺度以及实际选定的全部 typed 行。旧矩阵的归一化行和正尺度 s_i 满足 a_i^T=s_i C_i^{old}；原缓存的 bounds 与 −g_i/s_i 的关系仍须使用原完整接口。

源中的初始化为

\[
\tau_0=\max(0,\max_i g_i)+8\epsilon_{\rm mach}
  (1+\max_i|g_i|).
\]

记 d_i=\sqrt{\|a_i\|^2+1}>0。变量 x=(z,t)，t=δτ，\tau=\tau_0+t。完整增广行是

\[
\begin{aligned}
 C_i&=(a_i^T/d_i,-1/d_i),&
 b_i&=(\tau_0-g_i)/d_i &&(1\le i\le m),\\
 C_{m+1}&=(0,\ldots,0,-1),&
 b_{m+1}&=\tau_0.
\end{aligned} \tag{1}
\]

原源使用实际记录的 gradient_coordinate_norm 构造 d_i、使用实际 row_normalization_scale 乘回 a_i；本条不改变这些浮点输入的定义，也不以新公式重造另一个物理梯度。

原恢复目标完整保留为

\[
 f(x)=\frac12(\tau_0+t)^2+
       \frac{\mu^2}{2}(\|z\|^2+t^2)
     =\frac12x^THx+q^Tx+c,
\quad Cx\le b, \tag{2}
\]
\[
 H=\operatorname{diag}(\mu^2 I_n,1+\mu^2),\quad
 q=\tau_0 e,\quad c=\tfrac12\tau_0^2,\qquad \mu>0. \tag{3}
\]

e 是最后一个单位向量。原 Euclidean 增广步惩罚包含 t^2，不能删去该项，也不能把 (2) 换成纯最小 slack、SOC 最小范数或 metric QP。

令 M=m+1，写每个完整行

\[
 C_i=(u_i^T,-\beta_i),\qquad \beta_i>0. \tag{4}
\]

原 m 行的 β_i=1/d_i，最后一行为 β_M=1。允许任意物理零梯度、重复行和线性相关行；(4)始终保留所有这些行。正行缩放必须同时作用于 C_i、b_i，不能改可行集。

## 3. 原始最优解、对偶及所有行的 gap 恒等式

取 z=0，令 t 严格大于所有 −b_i/β_i，即得到 Cx<b。尤其可行集非空。H 正定，f 在全空间上强制有界，故 (2) 有唯一原始最优解 x_*。

对任意 λ∈R_+^M，

\[
 L(x,\lambda)=f(x)+\lambda^T(Cx-b).
\]

配方给

\[
 x_\lambda=-H^{-1}(q+C^T\lambda),\qquad
 D(\lambda)=c-\frac12(q+C^T\lambda)^TH^{-1}(q+C^T\lambda)-b^T\lambda.
 \tag{5}
\]

令

\[
 G=CH^{-1}C^T,\qquad r=b+CH^{-1}q.
\]

最大化 D 等价于

\[
 \min_{\lambda\ge0}\psi(\lambda)
       =\frac12\lambda^TG\lambda+r^T\lambda. \tag{6}
\]

这里 G 可能奇异，本条从不求 G^{-1}。

R683 的全行 KKT 证明直接应用于变量
y=H^{1/2}(x+H^{-1}q)：
目标仅差一个常数，约束成为 CH^{-1/2}y≤r。于是 (6) 存在最优乘子，最优对满足全部原行的可行性与互补性，且没有对偶间隙。这个引用沿用已刊完整有限生成锥证明，不新增独立性假设。

对任意原始可行 y 和任意 λ≥0，准确展开：

\[
 \boxed{\quad
 f(y)-D(\lambda)
   =\frac12(y-x_\lambda)^TH(y-x_\lambda)
       +\lambda^T(b-Cy)\ge0.
 \quad} \tag{7}
\]

每个约束都在最后一项中。它同时给出了可检查的驻点项、互补项与 gap，而不是以小矩阵的目标值代替原 C 的余量。

## 4. 公共 slack 列排除非负方向上的 Gram 退化

一般半正定 Gram 的 level set 可以无界；本题的同号最后一列给更强结论。对 λ≥0，

\[
 \lambda^TG\lambda
 =\frac{\|\sum_i\lambda_i u_i\|^2}{\mu^2}
       +\frac{(\sum_i\beta_i\lambda_i)^2}{1+\mu^2}
 \ge \frac{\beta_{\min}^2}{1+\mu^2}\|\lambda\|_1^2,
 \qquad \beta_{\min}=\min_i\beta_i>0. \tag{8}
\]

因而

\[
 \psi(\lambda)\ge
 \frac{\beta_{\min}^2}{2(1+\mu^2)}\|\lambda\|_1^2
       -\|r\|_\infty\|\lambda\|_1. \tag{9}
\]

所以 ψ 在非负正象限上的任意有限 level set 都紧，尽管 G 在整个 R^M 上未必正定。重复行导致的零空间方向必须含相反号；它们不会产生沿 λ≥0 无界逃逸的序列。

此外

\[
 G_{ii}=\|u_i\|^2/\mu^2+\beta_i^2/(1+\mu^2)>0
 \quad (1\le i\le M). \tag{10}
\]

(8)是本题特有的新增条件。它不是对所有不等式 QP、metric QP 或 R683 的任意 SOC 矩阵作一般强凸断言；也没有给整个 G 的正最小特征值。

## 5. 全循环坐标算法及准确收敛证明

从 λ^0=0 开始，固定每一轮顺序为1至M，且每一轮访问全部行。访问 i 时，以当前完整 λ 计算

\[
 h_i=(G\lambda+r)_i,\qquad
 \lambda_i^+=\max(0,\lambda_i-h_i/G_{ii}),
 \qquad \lambda_j^+=\lambda_j\ (j\ne i). \tag{11}
\]

这是准确的一维带非负约束极小值。实现可更新 h←h+G_{:i}(\lambda_i^+−\lambda_i)，而不是每坐标形成新大矩阵。所有 M 个坐标仍在每一轮中出现。

记 Δ=λ_i^+−λ_i。单坐标最优性给

\[
 h_i\Delta+G_{ii}\Delta^2\le0.
\]

因此

\[
 \psi(\lambda)-\psi(\lambda^+)
   =-h_i\Delta-\tfrac12G_{ii}\Delta^2
   \ge\tfrac12G_{ii}\Delta^2. \tag{12}
\]

所有迭代留在初始紧 level set。ψ 有下界，(12)逐项求和，结合有限个严格正 G_ii，得到每个单坐标更新 Δ→0。

现在在整轮起点取任意收敛子列 λ^{k_j}→\barλ。每轮只有固定有限 M 次更新，且每次更新趋零，所以该轮内各个中间迭代也趋于同一 \barλ。对第 i 个坐标的精确更新式取极限，连续性给

\[
 \bar\lambda_i=
 \max(0,\bar\lambda_i-(G\bar\lambda+r)_i/G_{ii}).
\]

即所有 i 同时满足

\[
 \bar\lambda_i\ge0,\quad
 (G\bar\lambda+r)_i\ge0,\quad
 \bar\lambda_i(G\bar\lambda+r)_i=0. \tag{13}
\]

这正是凸函数 ψ 在非负正象限上的全部一阶最优性条件。直接地，对于任意 ν≥0，
\(\nabla\psi(\bar\lambda)^T(\nu-\bar\lambda)\ge0\)，再用凸性可得 ψ(ν)≥ψ(\barλ)。故每个 cluster point 都是全对偶最优解。

由(5)，每个对偶最优解产生同一个唯一原始解 x_*。紧性及连续性说明整序列 x_{λ^k}→x_*，且 D(λ^k)→f(x_*)。乘子向量可能不唯一，本条不要求整个 λ 序列收敛到某个唯一乘子。整轮中间迭代同理。

这是一条无限准确迭代的收敛定理。它不保证64轮、某个墙钟预算或 binary64 实现达到指定容差，也不把有限 iteration_limit 当不可行性证明。

## 6. 任意物理步的全行可行恢复

x_λ 本身可以暂时不原始可行。无需投影到挑选的独立行，也无需抛弃它的全部物理步。对任意 z∈R^n，定义

\[
 L(z)=\max_{1\le i\le M}\frac{u_i^Tz-b_i}{\beta_i},
 \qquad
 t(z)=\max\left(-\frac{\tau_0}{1+\mu^2},L(z)\right),
 \qquad y(z)=(z,t(z)). \tag{14}
\]

所有行都有 β_i>0，所以 t≥L(z) 当且仅当全部 C_i y≤b_i。最后一个非负 slack 行包含在此 max 中，不能省掉。

固定 z 后，目标关于 t 的无约束极小值为 −τ0/(1+μ²)，且 t 部分严格凸。因此(14)不仅可行，而且是在固定完整 z 时的最优 slack。任何可行 (z,t_old) 均满足

\[
 f(y(z))\le f(z,t_{\rm old}). \tag{15}
\]

它并未使物理 g_i+a_i^Tz≤0；只是在原恢复问题中准确支付共同 slack。原非线性接受判据仍必须用候选场实际读取。

取 z 为 x_{λ^k} 的物理部分，记 y_k=y(z_k)。有限个仿射函数的 max 连续。最优点 x_* 的 slack 必已是固定 z_* 的最优 slack，否则可严格降 f。因此 y_k→x_*。

结合(7)，

\[
 U_k=f(y_k)\ge f(x_*)\ge D(\lambda^k)=L_k,\qquad
 U_k-L_k\longrightarrow0. \tag{16}
\]

可以保留迄今最小可行上界 U_best 与最大对偶下界 L_best。任何已经取得的准确可行旧 CG 点及零步都可加入上界候选；加入候选不会恶化 U_best。若旧点只是满足浮点容差，不能把它冒称准确原始上界，见第9节。

由原问题最优性、H 正定及(7)，

\[
 \|y_{\rm best}-x_*\|_H
       \le\sqrt{2(U_{\rm best}-L_{\rm best})}. \tag{17}
\]

证明：可行方向最优性使
\(\nabla f(x_*)^T(y_{\rm best}-x_*)\ge0\)；
二次函数准确展开给
\(f(y_{\rm best})-f(x_*)\ge\frac12\|y_{\rm best}-x_*\|_H^2\)，
再用 L_best≤f(x_*)。这不需要 G 的全空间正定。

## 7. 完整原坐标与逐块构造

原始步坐标一项不删。M×M 小矩阵由原完整 C 的**全部物理列**构造：

\[
 G=\frac1{\mu^2}\sum_B C_{:,B}C_{:,B}^T
       +\frac{cc^T}{1+\mu^2},\qquad
 c=C_{:,n+1}=-(\beta_1,\ldots,\beta_M)^T. \tag{18}
\]

B 遍历物理坐标的无遗漏连续列块；最后的 slack 列只计一次。原 StreamedRows 的32768列块与 CommonSlackRows 的虚拟整行切片可直接表达该式，不复制整个2.27GB行缓存。

由完整原矩阵重建

\[
 z_\lambda=-C_{\rm phys}^T\lambda/\mu^2,\qquad
 t_\lambda=(\beta^T\lambda-\tau_0)/(1+\mu^2). \tag{19}
\]

最终再由原完整 C 读取 Cx_λ、Cy、全部 slack 和原物理 g+Az。小 G 用来寻找乘子；不能以 Gλ+r 冒充实际原矩阵最终读取，也不能因两者不一致而删除有问题的行。

固定列块只限制暂存，不缩减自由变量、原行、物理类型、地址、normal chain、目标、预算域或非线性扫描。只需 O(M²+M·block_columns+n) 额外存储，不需原始全行的第二个长期副本。此处是算法存储量，不是已测内存峰值或加速结论。

## 8. 正行缩放的对应关系

设 S=diag(s_i)>0，同时把 C、b 换成 SC、Sb，令 \tildeλ=S^{-1}λ。则

\[
 \tilde G=SGS,\quad \tilde r=Sr,\quad
 (SC)^T\tildeλ=C^Tλ.
\]

同一顺序下，(11)的坐标更新满足 \tildeλ_i^+=λ_i^+/s_i，故物理 x_λ、原始目标、对偶目标和(14)完全相同。每个 β_i 同时乘 s_i，(14)的比值也相同。

这说明准确算法不靠某一归一化选择获利。binary64 的舍入序列未必逐字相同，本条不声称浮点缩放不变；已有原行缩放和 rank/feasibility 参数不会因此改动。

## 9. 有限浮点实现、触发和预算合同

本条给后续独立源家族的实现合同，不把源准备当作已运行：

1. 原 QPv3 先按原参数完整求解并保留整个 report、history、transitions、multipliers 和真实 residual replacement 记录。只对明确的 common-slack 恢复分支，且原状态为 dependent_blocker_at_zero_step 或 dependent_blocker_after_feasible_step，尝试本条全行方法。metric QP 和其他原状态继续原逻辑。
2. 新方法必须绑定原 μ、τ0、完整行及 bound。没有按 rank_tolerance 删行、正交截断、选 top rows、忽略 envelope 或缩小几何域。λ从合法非负点开始；原负乘子仍作为原报告保留，不冒成新合法乘子。
3. 一轮对偶法指完整访问 M 行。它不是原 CG advance。若使用原数值上限64，报告必须分别列原 advances、新完整 sweeps、实际坐标更新及总预算分配。可以只使用原64减已付 advance的剩余整数轮数，不能把214次坐标更新藏成一次原 CG advance，也不声称有限预算已收敛。
4. 每次实际候选的(14)以及最终诊断都直接读原完整 C。有限舍入造成的新不一致应明确报告，并保留原可交给外层的方向或零步；不能改变原非线性接受阈值以制造进展。
5. 由浮点数算出的 gap、stationarity、互补和余量只是数值诊断。若上界候选仅在原 feasibility_tolerance 内，则标为“按原有限容差可行”，不能套用准确(17)当严格证书。若要严格(7)/(17)证书，需要对全部表达式付有向舍入费用；这不是当前实际求解的新前门。
6. 外层仍做原方向本身的完整 Phi、全六族、所有旧新永久地址、原line_trials、原阻尼及真实接受。共同 slack下降、对偶改进、去掉一条算法阻挡，均不代替外层接受或课题完成。

没有公开新算法的实际回合、完整最终场或误差读数。本条也不把“准确算法无限收敛”转述为“该曲面构造必成功”。原内核的有限故障已明确，新的同问题方向必须继续在公开 Actions 真正执行并按返回推进。

## 10. 固定整文件来源与恢复

- [R683 完整旧证明](R683-all-old-row-constrained-second-order-correction.md)：8445B，Git blob 89b17224961882d38622a46350a1f1c10f6d5adf。本条沿用其完整半空间对偶和 KKT，新增同号公共列的紧 level set、全循环收敛及可行恢复。
- [原完整 QPv3](../scripts/resume_20261120/fullspace_feasible_active_cg_v3.py)：26947B，SHA-256 fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4，Git blob fabfcd7556a634d19e8dac788d5cb95d696b3d5d。
- [原完整第25组 driver](../scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_dk_cache_qp.py)：99410B，SHA-256 7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910，Git blob c0e24fb110b3f893bbd1fa1d52eb2457d78c6872。CommonSlackRows、原恢复目标和原 qp.solve/外层接受均来自这个完整源。
- [原 pure 完整分卷](https://github.com/Rogerhu12/math-research-public/blob/4969cfa0b12514b1466b4b916e5e877f26d95d48/topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46099929359-1-part-002.md)：33046B，SHA-256 b58b50d80400b671df9aa22b993e54ea9e7bed29b3d6052961ebe37dacbf3064，Git blob 9614c809d95c25d757c0406b9f168cb6094541f1。其单个完整JSON对象保423个实际formal值和22个原summary错误，本文不删除其余字段。
- 完整科学report只留runner：51804983B，SHA-256 c1be23826229f3df572ac3df64e25f2c4f65d0c5c8ec816436c9d3249fc221b4。未读大raw，未从未知transition捏造阻挡行。完整final bundle de44d265d795c4c4686dbc0fcf2273c06219644611b61c9fe2d7ab4b24bb7b1f 与typed13身份仍按原记录保留。

上述原 whole blob 或固定提交加完整路径可恢复全部源和原公开观察。新算法本身无需新的数值输入；它使用未来真实方向已经生成的同一完整 C、bound、μ及τ0。所有当前活跃运行和第31组完整原预算继续，新实现另列完整来源后执行。
