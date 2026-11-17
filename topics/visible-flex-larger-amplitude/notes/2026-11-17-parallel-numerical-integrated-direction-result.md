# R647 补充：保全 Pr 行的积分坐标单方向实测

## 结论与范围

从原 `1662ee34…` 的 602 节点暖场出发，执行已冻结的唯一积分坐标方向，进程正常退出。全部 580328 个原 Pr/边界残差、M160/N2048、同一 Hold 标量背景和 325+157 边界均保留。一次 damp=1、最多 128 次 LSMR 后，真实满步 raw SSE 从 `1.5321026127227238e-4` 降至 `3.481273683531508e-6`；8192 角全部原节点及实际 cubic 中点的正分支门通过。

LSMR 返回 `istop=7`，达到 128 次预算，并未线性收敛。真实 cubic 相对 Gram 最大 `7.50579740879674e-4`，高于课题 `1e-6` 门。这是完整行、固定预算的一个可行试点诊断，不是新的解父；未启动后继非线性迭代，未读旧失败场作初值。

## 同方程、不同步范数

沿用已登记的可逆坐标 `C=Y_0`、全部 U、全部
`D_i=(Y_{i+1}-Y_i)/h_i-(U_i+U_{i+1})/2`，没有把 D 置零或删去 compatibility 自由度。复用 `ef81…` 的 T/Tᵀ、`7aff…` 的完整列平方和尺度 S 及同一 BTS 边界投影 Π。d0 支付原有微小 BC 右端，方向为

\[
\delta x=d_0+TS\Pi z,\qquad
\min_z\|r+Jd_0+JTS\Pi z\|_2^2+\|z\|_2^2.
\]

本次普通 damp=1 施于新 z，确实改变步范数；不声称只是数值等价地重解旧正则化目标。raw residual 权重未变。LSMR 的 atol/btol=`1e-8`、conlim=`1e6`、maxiter=128；仅实算 alpha=1。R647 ray hook 另列原 17 个 dyadic 点的四次式预测，未额外评价候选或求解。

## 数值结果

|量|本次 T 方向|
|---|---:|
|LSMR 返回/迭代数|7 / 128|
|线性模型 SSE|3.4812035135010523e-6|
|真实 alpha=1 SSE|3.481273683531508e-6|
|实际/预测下降率|0.999999531353289|
|正则项 \(\|z\|^2\)|9.613035963816497e-6|
|显式坐标 normal 残差 L2|6.706689429747385e-5|
|相对初始坐标梯度|0.0010337694100163487|
|真实 node / midpoint 最大残差|2.4983824314262794e-4 / 4.067948626675685e-4|
|真实 BC 最大残差|1.249000902703301e-16|
|线性剩余 BC|5.930537640771422e-23|
|最大 dY / dU|4.146433381170096e-7 / 1.4413432051025e-5|

同一原始 (Y,U) 系数下，`||Jᵀr||₂=2224.068299842505`；本次 `||Jᵀ(r+Jδ)||₂=156.63393845757238`，相对为 `.07042676633117079`。只读旧 S-only 缓存方向 `5629…`、在当前同一 J 上重乘得到旧线性 SSE `5.45386957703086e-5` 和梯度范数 `543.6016986469244`（相对 `.24441771805542978`）。没有重跑旧 LSMR/旧试点。原坐标这些梯度含约束法向分量，不能单独当等式约束下的驻点证书；两套正则项也不能互相替代。

ray 的全部向量核对给 `||q||₂²=2.292391461840748e-13`，complex-step 方向核相对 L2 `3.2034439255788317e-15`。完整实际残差与 `r+j+q` 的最大差，node 为 `5.352531425015564e-16`、中点为 `1.2445800835915845e-11`、BC 为 `1.2490007296749288e-16`。后者包含极短 h 下实际更新/差分舍入，不强称逐位相等。模型 SSE 与实际值相差约 `7.02e-11`；这条方向没有重现先前 Newton 的巨大二次余项。

## 真实满步的原分支与 metric 审计

原 P.physical_samples 在 602 个节点、601 个实际 cubic 中点，各取 8192 角：rho 最小 `.16601817776336159`，Q 最小 `.027562035347866685`（node0/s0/phi0），W/H/正法速度最小依次为 `.00021937453762779338`、`.00021262912917352337`、`.014581768767236113`。后三者同在 node569，s=`1.0233471879626843`，phi=`.01687378866674205`。

相对 Gram 最坏点为 midpoint600，s=`1.029958740822432`、phi=`1.4289031039154747`，值 `7.50579740879674e-4`。未保留二次模式 j161..320 的 r0/r1/r2 系数最大值为 `[2.157294471023731e-6,1.4266261551499013e-5,1.49157054333567e-6]`，均完整报告。raw 点残差最大值为 `[.001331248733022261,.001389007399807518,.0006209267596597456]`。这仍是原有限 cubic 的样本审计，未支付全角/全径向证明或共同 C² 二jet；分支合法与小 raw SSE 不能替代 metric 门。

## 身份与复现

冻结算法 `parallel-implicit-integrated-direction.py` SHA256：
`2754dbcb63a21fc58789b27d756ec9433e748ef12a14a25bc4000d2c54c1b7cc`。
原暖场 SHA `1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`。
T prepared SHA `7affbce1eac7e61b94a03ca8b463c35ea1c4e28dfc3f02e74f1847670923965e`。
其余完整依赖与实际 scipy lsmr 源 SHA 在报告 identities 中，原边界字节 SHA 为 `8c32e71e1fe5428ccb28a39f2314ab78dd4ff223309e1553f8d52e7675490910`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-implicit-integrated-direction.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --prepared parallel-root-integrated-coordinate-preparation.prepared.npz \
 --preparation-report parallel-root-integrated-coordinate-preparation.json \
 --ray-source parallel-implicit-quadratic-ray.py \
 --baseline-direction parallel-implicit-lm-direction-once.direction.npz \
 --out parallel-implicit-integrated-direction-once.json --execute-direction
```

所有原始输出仅存 scratch：

|文件|SHA256|
|---|---|
|parallel-implicit-integrated-direction-once.json|de935a244029c3e183f5663225db555168764bb7d5c894b197df914d4b69b3df|
|parallel-implicit-integrated-direction-once.preparation.json|0d50a85ebd158d928093b92d5fb7de0963f7ba37da31fb04bf3ccdef189531c5|
|parallel-implicit-integrated-direction-once.direction.npz|eb3e5ea4393111a20b9d5582594e05f3dc13a16a7c00d6d0df74e244cb6db340|
|parallel-implicit-integrated-direction-once.ray.json|eca3589c64d46bc39ec85fc3af962d76bba4960699c1f9c227ace229b4959e66|
|parallel-implicit-integrated-direction-once.log|228bd5e31b69d1338cd73a1a0141ed4812d15ef0a6837bd19fdd99ddd2df0fd7|

方向 NPZ 保存原 Y/U、真实 dY/dU 与 z；候选 Y/U 二进制 SHA 为 `15ae6199a873b00a29dd22356db11cb5c5dd1296d660f34254079878f8056f4d`。单次 LSMR 用时 73.156s，整次含既定核对 87.802s，最大 RSS 381244 KiB；复用了列尺度，未重算 moments。普通浮点证据不冒作区间证书。
