# R613后继完整奇频的内存组织（尚无新科学范围）

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。此处只核输入/输出维数、源码和线性代数恒等。没有执行Jac、QR、SVD、求解或旧门。compact1130q的原run45882634760仍按原2…88目标自然运行；它的真实末态才决定后继输入。

## 1. 保留N256的全部可分辨奇频

[R613](../results/R613-actual-position-defect-jacobian-and-complete-objective.md)给实际位置两个分量的完整导数。其已发纯算子接口取奇频1…63，是有限投影。后继若实际消费，应在新driver显式取N256全部非Nyquist奇频1、3、…、127，两个分量共128输出/r；保持同一角网、全径向点、同一高度1130q、所有core链和规范。fine512及[R615](../results/R615-position-fourier-majorants-and-discrete-primitive-error.md)读出仍另付；完整离散奇频不等于连续无穷角尾已清零。

旧真实work为726r，fine为1281r。新增三片compact节点分别有13、9、21个跨度。每跨度work分6段、fine分12段；单片共享端点，因此新点分别不超过

\[
6(13+9+21)+3=261,\qquad12(13+9+21)+3=519.
\]

原点与片间重合只会减少并集，故真实work≤987r、fine≤1800r。这里没有本地重新构造科学网或求值，只有原已付点数及静态源码跨度的上界计数。原run终态会给准确并集点数。

于是完整新目标的Jac不超过126336×1130，共142759680个float64，单份1142077440 B，即1.06364 GiB。原直接实现同时保J、列归一Js、完整薄U已经约3.19 GiB；LAPACK副本/内部U、Jac中间张量和模型缓存再加其上，不能把三份矩阵之和冒充进程峰值。

## 2. 每一原行都进入增广QR

为避免大型左奇异向量，新增纯helper
[r613_complete_row_qr_svd_20261127.py](../scripts/r613_complete_row_qr_svd_20261127.py)。调用者只传已必须构造的完整J、当前完整残差b及deadline检查；helper不求新的Jac、height、geometry或ODE。

先在4096行的小块中累计每列2范数，仍用原scale

\[
d_j=\max(\|J_{:j}\|_2,10^{-12}),\qquad A=J\operatorname{diag}(d)^{-1}.
\]

J本身不改。第二趟按原顺序把**每一行**的增广块[A,b]送入QR，后续把前一上三角因子叠在下一块上继续QR。最终有准确算术身份

\[
[A,b]=Q\begin{pmatrix}R&c\\0&\gamma\\0&0\end{pmatrix},
\qquad Q^TQ=I.
\]

Q无需显式形成或保留。每次把一个块左乘正交变换、仅去掉其准确零行，再叠上下一个块；归纳即给此身份，没有删原非零行或对原行作筛选。目标是全原行。

因此对任意缩放变量y，

\[
\|Ay+b\|_2^2=\|Ry+c\|_2^2+\gamma^2,
\qquad A^TA=R^TR,\quad A^Tb=R^Tc.
\]

这里只用后两式说明等价，**不实际形成法方程**。仅对1130×1130的R作SVD：R=UΣV^T。对所有奇异方向，原正阻尼λ的同一步是

\[
\delta q=-\operatorname{diag}(d)^{-1}
 V\operatorname{diag}\left(\frac{\sigma_j}{\sigma_j^2+\lambda}\right)U^Tc.
\]

没有截去任何小奇异值。诊断rank沿用原完整m×n的max(m,n)εσmax阈值，而不是改用小R的尺寸；该rank仍只是浮点观察。

同一函数空间限制和步分数α作用后，令y=αdiag(d)δq，完整原模型的预测下降直接写为

\[
-c^TRy-\tfrac12\|Ry\|_2^2.
\]

这消掉正交残差γ的相同常数，也避免两个大平方范数相减。candidate接受仍必须重新计算实际完整位置残差；QR身份不代替实际/预测下降检查、正域或其他原门。

## 3. 存储、费用与数值范围

此组织仍只构造一次完整J，然后以小块读取两趟；不会因先取列范数再QR重算任何方向或geometry。形成factor后调用者可删除J，只保R/U/V及c、d、σ。旧完整状态和必要模型缓存的费用仍在。

在上述保守点数下，增广QR最大输入块为(4096+1131)×1131，只占47293896 B。1130平方矩阵单份10215200 B。大矩阵J仍约1.064 GiB，但不再形成完整Js或完整薄U。Jac每个16方向的单个987×256×16张量占32342016 B；原解析链的多个张量和缓存仍须计入实际进程，不能把这个单张量当总内存。按源码同时存活量估计可将主要求解阶段留在约数GiB级；这不是已测峰值或内存认证，真实runner读数须以后原scope自然记录。

helper记录完整J因子化次数、列范数读取原行数、增广QR块数、真实新原行数、带旧R的处理行数和小SVD次数。并输出原残差范数、约化残差范数和正交残差，供同场追账。它们是这次真实算法固有读数，不另做旧核探针。浮点QR/SVD的后验误差仍未被区间认证，准确算术身份也不是连续逆估计。

本文件与helper只作本地文本/AST/hash核对；无新request、workflow、科学run或新的有限根结论。后继源须绑定真实compact末态，并把完整奇频和此存储组织写入实际接受/末读出scope，再发布执行。

## 4. 末读出只作一次同场系数遍历

纯接口 [r615_shared_coefficient_position_observation_20261127.py](../scripts/r615_shared_coefficient_position_observation_20261127.py) 把原 R606 系数、rho、turning 根、G 与 G_e 的整段代数原样保留，并在其唯一一次遍历中将已有数组传给 R615。root 已对原 `observe` 与新函数作逐行差分，差异仅为原模块/源绑定、同场 PositionMajorant 创建、一次消费及双结果打包；原代数和计数没有第二份执行。R615 用原真正合法域，在旧 R606 较松 metric 乘子溢出之前消费，不能由后者失败反推新实际 S 界无定义。

fine N512 使用全部非 Nyquist 奇频 1…255，首个未读奇频257的连续尾仍由 R615 公式支付；work N256 的目标仍是 1…127。新 helper 不调用旧 `observe`，不额外生成 geometry、种子或 ODE，仍明确径向系数/ODE/舍入只作条件浮点观察。它尚无独立 driver/request/run，必须由原 compact 自然终态绑定的后继真正消费。
