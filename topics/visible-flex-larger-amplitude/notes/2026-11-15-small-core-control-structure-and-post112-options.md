# 原三参数共振结构与112实际结果之后的可执行选择

作者：ChatGPT `/root/exact_refinement`，`/root`按实际112选择的114接口更新；日期：2026-11-15。类型：冻结源码的结构分析和条件接续接口。本文不执行新数值计算；不宣称当前点是局部极小、无根或普遍浮点下界。

## 1. 三个参数到底改变什么

已重新全文读取 [原小核源](../computations/geometry_20261114_small_core_resonance.py)（SHA-256 `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`）、[原prefix controls](../computations/geometry_20261114_prefix_controls_profile.py)、[lifted modes](../computations/geometry_20261114_lifted_modes_profile.py)、[full scalar profile](../computations/geometry_20261114_full_scalar_profile.py)，以及 [R244](../results/R244-circular-support-scalar-control-null-direction.md)、[R255](../results/R255-circle-reference-linear-isometry-and-coast-shear.md)、[R259](../results/R259-small-core-homotopy-and-resonance-conditions.md)、[R278](../results/R278-finite-resonance-projective-normalization-and-local-elimination.md)。实际输入与消费源固定链见[112接口](2026-11-15-actual108-to-rejection-radius-retry112-interface.md)。

当前三个 p 不是三个独立模态的幅度。它们乘三个互不相交、位于原prefix内部的固定支撑 bump：

$$a(s;p)=a_0(s)+\sum_{i=1}^3p_i b_i(s),\qquad
\nu(s;p)=\nu_0(s)+\sum_{i=1}^3p_i b'_i(s).$$

在各自固定支撑内，`b_i=w_i²*64*x³*(1-x)³`，其中 `x=(s-left_i)/w_i`，支撑外为零。b、b′、b″在两端均为零。源的默认支持是prefix长度的 `.05–.30`、`.35–.60`、`.65–.90` 三段，但实际模型使用原prepared中明确序列化的 `control_supports_binary64`，不能以默认数替代实际输入。

因此三个参数都保入口与cut的scalar 0/1/2 jet及原tail参数，却通过整个传播链同时影响三个共振；不存在“p1只控制模1”的源级解耦。M112并未产生额外标量参数，LiftedModesPrefixProfile显式保持原三参数。

R244的圆形设计核是“同步改变scalar和圆形场、保原非均值边界”的完整设计残差核。它不是证明这三个首阶共振函数对p恒定，也不能代替当前3×3 Jacobian的秩分析。R259在圆支上进一步取core一阶传输，正是通过其p依赖产生共振条件。

## 2. 完整有限链与全部参数导数

原CircleReference每次从同一699mesh的节点和中点实际计算 `a,nu`，令q=nu/a；随后由原圆collocation半径标量递推确定R，而不是用a冒R。其后为V=qR、W=sqrt(1−V²)，并针对k=2、4、6形成

$$B_k=\begin{pmatrix}
q(1-k^2)&-Wk^2/R\\
Vq(k^2-1)/W&qk^2
\end{pmatrix}.$$

所有非零分母、正平方根及原节点/中点域均须保持。源没有使用app来求B。原完整112×112零尾J被实际读取并核为对角后，三条unit条件才是

$$d_j(p)=\ell_j(p)x_{j,N}(p),\qquad
\ell_j=(B_j(S)_{21},B_j(S)_{22}-\tau_j),\quad
\tau_j=\gamma\epsilon_h(J_0)_{jj},$$

其中x=(U,H)，入口为(1,0)，每步保持原L、R块与 `R_i x_{i+1}=-L_i x_i`。完整112右行仍由原程序另外形成，不能从另算的A_jd_j冒它的保存字节。

针对任意现有或新增的固定支撑方向b，有限模型的完整参数微分从

$$\delta q=(a\,\delta\nu-\nu\,\delta a)/a^2$$

开始。若圆半径递推为 `R_{i+1}=−l_i R_i/r_i`，其微分为

$$\delta R_{i+1}=-\frac{l_i}{r_i}\delta R_i
+R_i\left(-\frac{\delta l_i}{r_i}+\frac{l_i\delta r_i}{r_i^2}\right).$$

中点半径的原Hermite公式也必须微分，再使用 `δV=Rδq+qδR`、`δW=−VδV/W`。完整块的导数包括非交换乘积中的两项：

$$\delta L=-\frac h6(\delta B_L+2\delta B_m)
-\frac{h^2}{12}(\delta B_m B_L+B_m\delta B_L),$$
$$\delta R=-\frac h6(\delta B_R+2\delta B_m)
+\frac{h^2}{12}(\delta B_m B_R+B_m\delta B_R).$$

因此

$$R_i\delta x_{i+1}=-L_i\delta x_i-\delta L_i x_i-\delta R_i x_{i+1},\qquad
\delta d_j=(\delta\ell_j)x_{j,N}+\ell_j\delta x_{j,N}.$$

原complex-step `jacobian`实际是对完整evaluate调用，已经包括这些参数依赖。只微分局部bump、末端pair或边界中的某一个部分是不完整的新J。

虽然控制支撑互不相交，有限圆半径R会把上游p变化传到后面。不能无条件把整条有限传输写成三个只依赖各自p_i的独立2×2乘积。只有另证相应分段变量依赖后才可那样缩减。连续ν=a′时圆参考的R=a身份亦不能自动搬给当前有限collocation R。

## 3. 近零方向不提供哪些结论

R255已解释圆线性化的秩一瞬时结构、大频率剪切与曲率耦合；瞬时大k²项不自动意味着指数放大。R278已证明项目化可以保零集，且在共同零点时只给Jacobian行尺度。把当前同一3×3 Newton系统左乘可逆对角尺度，不会改变它的精确方向。

Actual108的SVD及原逐坐标real-FD读数是有限数值报告。原real-FD误差采用每列最大分量归一化，不能据此给近零线性组合提供相同相对精度界；普通float stationarity也不是严格导数包络。112因此需要保每次实际d、Jd、gdot、μ、半径及真实W，而不能仅凭条件数判无根或强制某一种失败原因。

## 4. 实际112之后选定的不同非线性路径

[实际112](2026-11-15-actual112-tiny-acceptances-and-final-twenty-trial-rejection.md)显示六个极小接受、末方向二十档拒绝，全步第三式相对线性预测有巨大偏离。114因此保同一三参数家族和原完整三列正阻尼方向v，改变回溯路径；不是已得到的根，也没有把近停滞归因为已证明的单一原因。

令当前两个较敏感的原条件为 $c=(d_2,d_3)$，$C=D_pc$，$S$为原相对参数尺度。若 $CS$ 有行秩2，对 $(CS)^T$ 作完整QR得到正交二维法向基N和一维单位切向t。三个参数列全保留，不凭单个J33选全局图，不截去弱列。原full3方向v和原真实斜率 $d^TJv$ 仍直接使用并完整记录。

对于每个原α，令 $\xi=t^TS^{-1}v$，在

$$q_\alpha=p+S(\alpha\xi t+Nw_\alpha)$$

中校正两个实际条件到目标

$$c(q_\alpha)=c(p)+\alpha Cv.$$

这使α=0的原点 $q_0=p,w_0=0$ 明确成立。这里未强制后两式为零，也未假设正阻尼v满足 $Cv=-c$。若另选这样的v，右侧才特化为 $(1-\alpha)c(p)$；114使用一般目标。

在对应原实表达式可微且 $CS$ 满行秩的局部，$CSN$可逆，R278的局部消元原理给精确校正曲线。它的初速度是v：对目标求导并利用 $CSt=0$ 得 $w'_0=N^TS^{-1}v$，而 $NN^T+tt^T=I$。故原full3斜率仍是这条理想曲线在α=0的导数。此为既有局部消元在具体算法坐标中的应用，不把数值QR非零或有限校正当严格横截性证明。

实际每档以内层初猜 $w=\alpha N^TS^{-1}v$ 开始，使用原完整evaluate/J校正，保存全部真实参数、两式目标、校正剩余误差和域失败。有限预算不保证内层达标；未达标的实际候选仍只由真实full3 W、原 `.2 Armijo`、全部原域及最终unit/full112门裁定。不能把真实非零d2/d3覆盖为零，也不能以内层失败宣称原方程无根。

这一路径同时处理两个敏感残差的曲率，区别于此前92/93/106固定p3图上的单式恢复。它仍可能遇到行秩变化、原合法域边界、有限精度或沿切向不能充分下降，当前不预言成功。实际114输出将决定继续当前家族还是扩充设计控制。

## 5. 若三参数家族持续失效：一个最小的诚实设计扩充

一个具体新增方向可放在现有一个prefix支撑内，避免移动支撑导致新的分支坐标问题。令

$$c_4(s)=b_i(s)(2x_i-1),$$

支撑外仍为零。其一、二阶导数是

$$c_4'=b_i'(2x_i-1)+2b_i/w_i,\qquad
c_4''=b_i''(2x_i-1)+4b_i'/w_i.$$

因此它的0/1/2 jets在两端全零，与原b_i作为函数线性独立；对其他两个不交支撑亦无混淆。新族为 `a_new=a_old+theta*c4`、`nu_new=nu_old+theta*c4'`。**函数线性独立不保证新增共振响应列补足秩**，必须在Actions通过上述完整圆/模态链得到真实3×4 J及真实试探。

这一方向的优势是明确可实现、保固定支撑和core/cut jets、原699mesh可继续评价全部公式；初始theta=0具有原数学profile。不能预称其binary64实现所有数组逐字相同，尤其不能把4列einsum的重新求和冒原3列有限次序。

扩充需要独立profile/source/schema及完整control polynomial声明。现有LiftedModesPrefixProfile和scalar_spec都硬锁3参数，不能仅将第四数塞入旧schema。原ScalarExpression/区间returned_ap也需完整覆盖新七次多项式及导数，原node/mid/RMS、全部112尾和最终域责任不变。

若以4参数在3方程中求候选，完整正阻尼3×4子问题可给唯一算法方向，但并不把新增参数算作原BVP已经约束。后续完整DN可将找到的theta冻结为新base标量的一部分，保原三剩余设计变量，或另明确一个设计规范来闭合维数；不能把4自由变量的欠定问题伪装成原三变量方阵。最终只在同一冻结全scalar上谈同g弯曲。

## 6. 与整体目标的连接仍不能跳过

即使后来低三原unit及完整112候选门通过，也须在该真实p重新处理高109完整两端块、区间/导数范围，并从全112首阶信息构造明确未接受的小非零λ场，调用真实非零H的native及原最终J/audit；旧78高109结果不能跨p继承。R259的加权λ同伦可以减少某个一阶低目标，但更高阶强迫及真正尾导数尚未支付，因此本稿不把它当已有可派发的替代入口。

实际112已经完整读回，114正在实现上述后两式弯曲试探；其结果未到，不将这份接口当接受点。如果仍不能有效推进，再按真实残差和域证据选择第五节的独立控制，不盲目增加相同外层预算。任何一条都不能把“缺原门”改成新的成功定义。

本文件只给可落地的数学与接口范围；没有本地求范数、SVD、矩阵或残差，没有伪造112或114的结果；代码与实际执行另循公开Actions入口。
