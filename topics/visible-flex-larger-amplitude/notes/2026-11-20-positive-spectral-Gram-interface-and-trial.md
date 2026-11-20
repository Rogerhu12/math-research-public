# 正谱 L8 完整接口与一次同像机制试验

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**已完成：可被原全空间 LSMR 和粗 QP 消费的严格正 $3\times3$ 残差块权；一次22列径向同像方向实际试验。** 完整数学为 [R660](../results/R660-positive-spectral-Gram-blocks-and-maximum-control.md)。径向试验仅说明新目标会主动交换均方误差与峰值，不作为主线新父；geometry 已从其更新、更好的原空间父接同一块权接口。

## 1. 固定参数和目标

本次固定 p=8、$\epsilon=.001$、c=.05，基础权是原半 Simpson／半六 Gauss 径向权乘完整角 orbit 重数，再归一化为和1。全部7377径向观察、N2048全角的513个带重数表示和原三项都保留。目标为

$$
\Phi=\sum_i\nu_i\operatorname{tr}
\left({E_i^2+\epsilon^2I\over c^2}\right)^4.
$$

未缩放幂目标是 $\Psi=c^8\Phi$；报告的 phi_normalized 始终是上式的 $\Phi$。报告的 smoothed_spectral_lp 为 $c\Phi^{1/8}$。epsilon/p/c 在该方向全部回溯中固定，原 a 仍在原 s 取值。

最小归一化 orbit 权为 $2.756087833527076\times10^{-10}$。正块 W 的准确理论谱下界是 $(.001/.05)^6=6.4\times10^{-11}$；源码的实数权读取最小值为 $6.399999999999996\times10^{-11}$，没有将其删掉。普通浮点值不冒称向外端点。

## 2. 完整3×3接口，已交给主线求解线程

源码 [positive_spectral_gram_weights.py](../scripts/resume_20261120/positive_spectral_gram_weights.py)，11,186 B，SHA-256：

e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91。

冻结 $W=(E_0^2+\epsilon^2I)^3/c^6=\begin{pmatrix}u&v\\v&w\end{pmatrix}$ 后，原三项 $(e,f,g)$ 的权为

$$K=\begin{pmatrix}u&v&0\\v&u+w&v\\0&v&w\end{pmatrix}.$$

它已包含混合项 Frobenius 因子，不再另乘 $\sqrt2$。矩阵块正定，全部原行保留。接口同时提供：

- raw 或 native-orbit 三项的 K 应用，以及任意列 Jacobian 的 K 应用；
- 准确代数的流式 $J^\top KJ$、$J^\top Kr$ 收缩；
- Cholesky $L^\top$ 正向与 L 转置；
- NativeLinearization 包裹原完整 operator，直接给 LSMR operator、对应残差、梯度与真实 $\Phi$ 梯度比例；
- 真实 trial 的 $\Phi$、旧 $J_w$、直接 maxGram、epsilon/p/c、最小正权和公式边界。

NativeLinearization 行数为 $7377\times513\times3=11\,353\,203$；列仍为原完整自由变量。原 H² 坐标映射、粗列白化及几何约束都可原样包裹。

若采用已有“mean-data normal + $\mu^2I$”的物理 H² 约定，为保持真实 $\Phi$ 的单位，应将 raw $H_K,g_K$ 同乘 $k/c^2=1600$ 后再除原 $C_0$。不可只放大 gradient。等价保持 raw 二次量时，应取 $\mu_{\rm raw}=\mu_{\Phi}/40$。实际阻尼宜以当前真实 H² 白化后数据正规矩阵量级定义，而不将旧目标的绝对阻尼数值机械搬用。

geometry 已确认未有重复 IRLS 工作，其物理 H² 主方向自然完成后接本接口；随后主线继续获得了更新父0241，正从该父接完整1964列、相同几何约束的谱目标。full solver 保正在执行的方向字节不动，后继由 root 分工接 NativeLinearization。没有把工作停留在下述窄空间诊断。

## 3. 新块算术的一次小模型检查

这里只检查新引入的权重桥，没有重复旧 FFT、dense 或连续证书：

| 检查 | 实际相对差 |
|---|---:|
| 真实 trace 多项式的 complex-step 梯度与 $Kr$ 公式 | 0 |
| 正向／转置因子复合与 K 应用 | $8.727480409895017\times10^{-17}$ |
| 因子的双线性伴随 | $1.4013882354571499\times10^{-16}$ |
| 任意列 $J^\top KJ$ 组装与直接作用 | $2.710708300490573\times10^{-16}$ |

小正规矩阵最小特征值约 .04613125。样例为固定种子20261120的3×4观察块、7列、p8/.001/.05；梯度直接用 $2\times2$ 复矩阵的四次幂 trace 求 complex-step，没有通过同一特征值导数公式自我对照。

完成报告 positive-spectral-block-small-check.json 的 SHA-256：

5f41fb9a099d9770bdfa8166036a700c3eed715f8620c74925c95dd3b59e3ec4。

这些数值检查支撑新实现衔接，数学正性、梯度和转置由 R660 完整证明；不是新增必须重复的科学验收门。

## 4. 固定 r17 父的唯一径向谱方向

固定父 work/geometry_path/curvature-qp-protected-992-r17-six-step.npz，SHA-256：

1240c633c959a9f1df2c7a78bc25bcb6d2663f23ba8abc1a30e0b1e116a5e4d9。

这个父不是后来 geometry 的 e19 或0241；数值比较没有换父。沿 [前一个径向机制](2026-11-20-exact-radial-reparameterization-first-trial.md) 同22个 C² bump，使用真实复合 $F_{\rm parent}(\sigma(s),\phi)$，目标 a 不复合，不生成伪 quintic。

新的冻结谱块系统保留22/22列。实际 $\Phi$ 方向导数约 $-2.45088139688\times10^{-4}$；原块最小／最大谱权约 $6.4\times10^{-11}$、.13273121。方向的每个真实 trial 都先以准确 Fraction/Bernstein 证明 $\sigma'>0$，再读取全部原有限目标。

| 步长 | 真实归一化 $\Phi$ | 全行 maxGram | 原 $J_w$ | 实际处理 |
|---:|---:|---:|---:|---|
| 父 | 0.000060808548235794765 | 0.03569673566390885 | 0.28193249239672247 | 基准 |
| 1 | 0.0016357623086964376 | 0.04422591182819957 | 0.9633999649246405 | 真目标升，拒绝 |
| 1/2 | 0.00007293845674199428 | 0.03170491027693867 | 0.4558495321166538 | max虽降、真目标升，拒绝 |
| 1/4 | 0.00003677268425333897 | 0.03170491027693867 | 0.32718628478486456 | 真目标与max均降，记录诊断 |

这直接示范了冻结二次模型不是 $p>2$ 的 MM 上界；本次没有凭冻结模型预测接受全步。

四分之一步使 $\Phi$ 降39.5271%、有限 maxGram 降11.1826%，但旧 $J_w$ 升16.0513%。准确 $\sigma'$ 下界大于 .9853724；最大观测位移 .0006205764。新有限最坏点 s2.3206222983372733、$\phi=\pi/2$ 已落在 bump 支持外的 identity 邻域，因此该点根本未被本22列改变。没有继续扩该窄空间或重复同像优化。

r17 的原几何数值 screen 状态不因同像复合改变；这个试验不添加 reach／held 结论。后来主线原空间 e19 已有更小 maxGram .030589，0241继续更好，所以本诊断不作为新的主线父。

## 5. 范数界在本次确实较松

R660 的归一化公式正确应用 c=.05 后，四分之一步的普通数值代入为

$$0.0127556151\ \lesssim M\ \lesssim0.2185845664.$$

右端因 $\nu_{\min}$ 很小而远松于实际直接读出的 .03170491。这是数学关系正常的保守性，不以它伪造更好的最大误差证书。报告明确 formula_evaluation_outward=false；严格的关系是 R660 的数学公式，而本段数字不是向外连续证明。

同样，所有有限 maxGram 值都仍需连续范围支付。没有把新的 Lp 目标、平滑 epsilon 或某个相位读数替代 README 的同 g 闭族完成标准。

## 6. 源码和实际运行身份

谱径向驱动：

[spectral_radial_reparameterization_trial.py](../scripts/resume_20261120/spectral_radial_reparameterization_trial.py)，8,852 B，SHA-256：

86ee4d38fc3696102cb8c01ba0438c3ad147d171c984433491eacbbcc0a6ff00。

它消费前一个径向完整 evaluator SHA fec3425b9c10b44f1d9b5d210a9f4ca8f182ff21edf1dc5c9d51bb418d12530c 和上述 e837 正块源；原 dense/batch/Gauss 源不变。实际报告：

work/recover_evidence/spectral-radial-r17-p8-first.json

SHA-256：

14a0769609dd2846020d314e1cc21ad6190fd39c3124a0aa1b42e22b4954f65f。

session93796 自然退出0，总耗时4.39秒。一个正规方向、三次自然回溯；未扫描 p、epsilon 或候选表，没有额外全域几何／连续度量证书运行。可重生 raw 不入库。

实际 CLI：

```bash
python -u math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/spectral_radial_reparameterization_trial.py \
  --bundle work/geometry_path/curvature-qp-protected-992-r17-six-step.npz \
  --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --node-report work/fullclosed_solver/data/fullclosed-hold-warm.json \
  --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
  --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
  --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
  --radial-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_radial_reparameterization_trial.py \
  --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
  --p 8 --epsilon .001 --scale .05 \
  --out work/recover_evidence/spectral-radial-r17-p8-first.json
```

公开CLI将原scratch执行源位置换为本仓库内的同字节源。cwd为含math-research-public与work的共同目录，单BLAS环境沿前序；父2b143/1240、carrier和节点报告依前序实际公开命令重建。原字段数组及完整逐点输出仅scratch，不以唯一文件路径替代完整配方。
