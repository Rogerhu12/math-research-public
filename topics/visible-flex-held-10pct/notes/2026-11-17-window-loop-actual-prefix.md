# 消耗圆弧特征窗口后的 loop：实际有限前缀计算

会话：`true_a_analysis`；2026-11-17。

本记录区分三个对象：固定的旋转度量、实际求解的有限 Fourier 前缀、精确圆弧核心。**目前只有第一个和部分有限前缀得到计算支持，没有得到圆弧核心的合格前缀，更没有闭合曲面。**

## 1. 新度量及线性筛选

`consumed_window_loop.py` 保留已发表 v38 设计的头两段：原 H 带和新增负 K ramp 完全不变。其后依次使用正 K 回转、负斜率 coast、负 K 回升、终端 quintic 速度桥。所有段的 a、a′、a″、a‴在内接点相容。cut 仍为 r=.6、w=.5、w_r=−7w/r。

`window-loop-short-parameters.json` 定义一次明确的线性设计参数。主要数值为 extra_speed=.38、extra_acceleration=1、return_speed=.8、turn_acceleration=4.799999999999999、stop_speed=−.2、final_length=.36、stop_acceleration=2.895293801030502。此处后续回升段并没有把速度提高至零。

在真实旧三重 DN 下，m=3 归一化入口残差约 −4.9e−11；背景半高约1.389858、半径约1.126636、采样曲率约7.515、末桥最小1−a′²约.0648。m=6 入口残差约.978，故这不是多模线性共振设计。头两段不变，因此 v38 的 R=2、法向宽.9 特征窗口预算保持；这并不证明实际非线性解圆整或存在。

筛选入口为 `window_loop_short_scan.py`。它只记录线性端口根及背景采样，不将不同参数的候选当作同 g 精化。

## 2. 真正完成的非线性计算

全部使用实际 Cartesian Frenet 速度、完整物理 metric/Darboux 审计及同一 r=.6 有限线性 DN。`window_prefix.py` 没有将有限 Fourier 核心投影称为精确圆弧；参考 lift 保留完整定义的核心，再求有限表示的修正。

| 计算 | 明确终态 | 完整几何残差与范围 |
|---|---|---|
| compact 控制，q=.002、M3、lambda=0 | 344节点收敛 | metric约2.027e−6；这是未平顶基线 |
| 同一支线 lambda=.03/.1/.3 | 均收敛 | metric约5.23e−5、1.72e−4、5.34e−4；每步修改了g |
| 同一支线 lambda=.6 | profile控制出搜索域 | 没有成功解，不是不存在证明 |
| compact M3 lambda=.3 warm → M4 design | 1181节点后超 cap1800 | stop_acc接近20、残差8.88；不是固定g精化 |
| 相同低阶矩的控制同伦，q=.002、M4、lambda=0 | 371节点收敛 | metric1.7760673e−9，Darboux9.13194e−8 |
| 此同伦 lambda=.03/.1/.3 | 均收敛 | metric4.64e−6、4.31e−5、3.92851e−4；每步修改了g |
| 此同伦 lambda=.5 | 1243节点后超 cap1800 | stop_acc接近20、残差15.8、背景曲率约32；不可用候选 |

另一次较长 loop、q=.01/M4 的 lambda=0 启动也超节点上限：最大残差.00432，BC约5.26e−6。最初程序把负 coast 域错误抛成 ValueError，后改成 FloatingPointError 以接入原有 Newton 回溯；记录中的第二轮是这一修复后的真实终态，没有放松正长度条件。

## 3. 唯一已完成的冻结同 g 对照

冻结文件为 `window-loop-frozen-lam0-m4.json`，其 stop_acceleration **固定为2.895180987993422**。所有其他参数也冻结。此时 lambda=0，核心仍为光滑、非圆弧的三重曲线。

| 项 | M4设计点 | M6冻结g精化 |
|---|---:|---:|
| 实际主幅值 q | .002 | .002003776170939374 |
| metric_l1 | 1.7760672540903817e−9 | 6.392854606952645e−10 |
| Darboux_l1 | 9.131941631702114e−8 | 2.651074144090568e−8 |
| 采样最大曲率 | 7.54046 | 7.5421364 |
| 半高 | 约1.38993 | 1.3899285577 |
| M6节点数 | — | 734 |

这仅证明该新 metric 的有限数值基线可以精化一次。它不包含精确圆弧、H固定、尾闭合或无限精化结论。

## 4. 两个数值接口改进

`exact_lift_parameter_jac.py` 使用固定材料角的解析核心两jet参数导数。若 U=δu(φ)、δφ=−U/ρ，则

\[
\delta\Gamma_u=-\delta\phi\,n,\qquad
\delta\Gamma_{uu}=-\frac{\delta\phi}{\rho}t+
\frac{\delta\rho|_\phi+\rho_\phi\delta\phi}{\rho^2}n.
\]

这些导数经完整参考 lift 和 Frenet JVP 传递；仅后H的度量控制仍用中心差分。独立中心差分检查的绝对误差在约1e−9到1.3e−7之间，属于浮点诊断，不是区间导数证书。固定g M6检查中导数信号仅约2e−6，故1.6e−8绝对差表现为约.8%相对差；不能把它说成高精度小奇异值证书。

`homotopy_plateau_core.py` 在 lambda=0 用每个紧支撑 f_j 的前M个正弦 Fourier 模，lambda=1 恢复原紧支撑 f_j。这样保留表示的低阶矩，避免人为的低阶控制矩阵换向；终点精确圆弧约束没有改变。此改进没有消除上表中的几何残差增长和边界控制饱和。

## 5. 最小复现

先按已发表 `plateau_recovery_manifest.json` 和 `recover_prefix.py` 恢复历史 source 与 flat17-port96 到仓库外。以下 SRC 指恢复的 visible-flexible-closed-surface，PORT 指恢复的 flat17-port96。所有输出放在 OUT 下。

```bash
python window_prefix.py --source-topic SRC --port-file PORT --profile window-loop-short-parameters.json --out OUT/m4 --q .002 --modes 4 --halfwidth .2 --transition .1 --lambdas 0 .03 .1 .3 .5 --nodes 151 --max-nodes 1800 --tol 2e-6 --angular 160 --analytic-parameters --check-parameters --core-basis moment-homotopy
python window_prefix.py --source-topic SRC --port-file PORT --profile window-loop-frozen-lam0-m4.json --out OUT/fixed-m6 --q .002 --modes 6 --halfwidth .2 --transition .1 --lambdas 0 --max-nodes 2000 --tol 2e-7 --angular 224 --restart OUT/m4-lam0.json.gz --analytic-parameters --check-parameters --core-basis moment-homotopy --fixed
```

`window_loop_source_manifest.json` 给出本轮最小源码与参数的 SHA-256。运行产生的 checkpoint、数组、扫描表和日志全部可再生，不提交。后续工作已转向真正的前缀/非线性尾联立，不继续在 stop_acc 上界附近追加模数。
