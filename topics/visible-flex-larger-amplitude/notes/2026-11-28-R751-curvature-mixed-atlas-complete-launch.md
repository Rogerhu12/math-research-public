# R751：完整曲率混合闭面与真帽材料费用 — 原任务登记

会话 Astra-larger-e4e2a2bf-20261126。数学结论与当前任务均未代替课题完成。五件完整正文已由根读取；下面测量按原输入、全部阶段执行，实际返回此刻尚未知。

## 已证明的精确范围

[R751完整证明](../results/R751-moving-curvature-mixed-section-and-exact-roll-into-both-physical-caps.md)构造真闭周期单位速曲率混合截面，保留固定圆握持和整柱同g。真实最后 .00015 材料转弧在 θ≥1 的曲率比 C=1.00001，使两侧全部实际圆端及两真帽 .0001 内领对同初g三行准确；整个剩下圆周仍须支付完整度量。闭曲线由两真实直段上的角度变量求闭合，非只形式jet。全闭支撑/曲率、直径、固定握持和未对齐held及不全等体积论证均见原稿，数值近似场须用实际误差检查，不自动承继精确方程。

同稿给出全局必要障碍：旧初g两中央标签的内在端部捷径 <.801，而规定终态中央弦长 >1.17。全锁旧中央时，任何端帽补齐都不可能严格同g；至少一个指定中央位置须移动 >.184。此限制没有否定中央可动的40号，也没有否定采用新固定初g的后续分支。

## 不删减的实际任务

原 3 层 (48,12,16)、(96,24,24)、(192,48,32)，分别为空间周向数、横向数与积分阶数；全部七相位 0,.4,.8,.9,1,1.2,π/2。每层、每相位完整计算 cylinder、end±、cap±、cap-normal±、cap-cartesian± 共九张材料图，附真实分片端点与弯曲boost窄带采样。两侧真实最后 .00015 材料子弧各17点，纵向遍历整圆端至真实帽及 .0001 内领；不以一条边或外推代替。

每张图独立比较同一初相位完整三行Gram的相对算子特征值，并由全部六jet计算主曲率，保留无效点计数。逐相位报告实际闭合角度变量与两指定中央标签的弦长和初内在距离上界。原始完整六jet二进制只在公开runner，报告保原始字节数与SHA256；不上传raw。有限采样仅为工作值，不是连续域证明。

完整命令：

```sh
python -u topics/visible-flex-larger-amplitude/scripts/resume_20261126/measure_r751_closed_mixed_atlas.py --raw "$RUNNER_TEMP/r751-actual-six-jets.raw" --report "$RUNNER_TEMP/r751-actual-report.json"
```

公开workflow整项60分钟，numpy2.2.6，BLAS/OMP单线程，无科学子任务另设缩短超时。启动前真实部分克隆、pull --rebase main、比较双README；自然完成后原完整小报告与真pull提交记入HANDOFF。NFF立即pull/rebase循环，不force。没有以检查阶段代替实际完整计算。实际run/job/结果尚待原任务返回，不能预填成功。

## 原文件完整身份

|路径|完整字节|SHA256|Git blob|
|---|---:|---|---|
|topics/visible-flex-larger-amplitude/results/R751-moving-curvature-mixed-section-and-exact-roll-into-both-physical-caps.md|17143|04e1643c2de80ac6265b2ad3f71d4967747f79441cfe0e1572683f1c6249d175|cb3984c0965c5c684843a2cc783933b8ab96fbd1|
|topics/visible-flex-larger-amplitude/scripts/resume_20261126/r751_curvature_mixed_closed_two_jets.py|13877|08416719155ce0d4a689410cf7ac5e9995f606358c5730298cb723d4eeb53e07|53f39fc18e4595102a7277a3008c2ad07325da88|
|topics/visible-flex-larger-amplitude/scripts/resume_20261126/measure_r751_closed_mixed_atlas.py|6096|846f9f94ca2f7480331eb59b482457ee7ecfd37ba24f58a01af8be0516f9f46e|642aafe09274a350bb080cbacf36ca2e83b8f8a9|
|topics/visible-flex-larger-amplitude/scripts/resume_20261126/publish_r751_mixed_atlas.py|5983|1da329125a780f78e3acab2c3669bf3364295412679930eb2995069bb1d124a0|27c3b87dc7edc328809d4a9eb0c2ffb5fe38b56a|
|.github/workflows/visible-larger-r751-curvature-mixed-atlas.yml|3388|0c803a5982cbdc0ce1aa8a600a5da1866f6be2b7580041341de8a00e066750a6|b5756a37c0113ebeb7354da2c3e0dcc3fcfbf2d0|

五个完整文件与本登记同一次普通提交入main；workflow只由原测量源/本workflow变化触发。原依赖 R740/R742/R744/R746/R747 与 publish_r734_exact_conclusion 保持main完整原文件；不借旧不同输入数值。课题未完成，后续继续真实全闭同g构造和全相位细化。
