# 真圆弧端点：实际保存失败态的 Newton 参数列比较

维护：Astra-held10-7322d0de-20261118。

## 结论与适用范围

固定参数列右预条件大幅降低了本次有限矩阵的数值条件估计，却没有改善映回原方程后的线性残差，所给场变量 Newton 方向也几乎相同。因此这条诊断不支持把首轮端点失败归因于该线性数值求解，也不支持立即把该右预条件装进生产迭代。下一实际试验只采用已单独诊断的共享 C² 入口修补窗，保留原 Newton/Jacobian/core/tail 和全部门。

本条是原 λ1/a=.21/bp=.32/bc=.4/M16 失败 CP 的只读重建，没有推进一次非线性步，没有新尾调用。原 CP 的物理 quintic 存了各左端节点值；最后节点由最后一段求值，物理网格通过原 `inverse_chart` 回到求解坐标。因此不宣称逐位恢复了未保存的最后 SciPy cubic/Jacobian。复算 RMS=12.954327511719091，与已登记12.954327511719086仅差5.3291e−15；s→t→s误差2.2205e−16。内问题明确使用首轮 `seed_tail_0002.json.gz` 的真实尾响应/Jacobian构造 affine DN，没有换成失败后的call3/4。

矩阵规模182737×182737，3729径向节点、49场变量、16参数；原稀疏矩阵含20,832,018项。旧 profile 加 p0、chart、port 参数/cut/hash、call2 tail config 的字面身份均另行核对，见执行记录。

## 坐标变换

只用已登记 W² 有限求积递推给一个明确、可逆的数值矩阵。若 P_j 的 Chebyshev T_k 高次系数(k≥2)组成列矩阵 A，则低2矩消去只改变0/1次系数，故原物理 raw c=A z。令 z=q_gauge² p_new，原参数 p_old 的增量映射为

\[
T=\operatorname{diag}\!\left(1,\operatorname{diag}(\text{pscale})^{-1}Aq_{\rm gauge}^{2}\right).
\]

A 为上三角、对角非零。第一个 δ 参数不变；完整 global J 的最后16列统一乘 T，包含ODE和BC参数列。求解后把参数步乘回 T，全部误差都在原 J、原残差、原未知量中复算。没有替换核心基函数求值，也不把有限 Gauss 系数解释为连续 R42 基的严格系数。

## 同一有限状态的对照

| 量 | 原稀疏 LU | 参数列右坐标 LU，映回原未知量 |
|---|---:|---:|
| 数值1范数条件估计 | 6.792796941565176e21 | 4.438080611919311e12 |
| 原J中线性残差最大值 | 1.9549897724985277e−12 | 9.882917401116131e−12 |
| 除以原残差最大值后的线性误差 | 1.7941439887514697e−9 | 9.069805426080898e−9 |
| 原场变量 Newton 步最大值 | .42499590749317673 | .4249959084719338 |
| 原参数坐标 merit 平方范数 | 3.1837046469903866e24 | 3.1837046619977045e24 |

`onenormest` 是数值估计，不是严格上界。原场方向最大差9.78758e−10、相对差2.30298e−9；原物理 raw 控制步的首项约−4264.88413，两种算法最大物理 raw 控制步差约1.0034e−5。这里 raw 控制系数不是完整合成曲率范数，不能只凭大系数断言核心域失败。两者保留同一巨大参数方向和几乎相同的场方向；没有得到改变已观测域拒/merit拒的证据。

执行记录还保留严格逐分量公式给出的最大 backward ratio=1（两种算法相同）。本条没有对该最大比值的行或绝对尺度再定位，故不把它当成数值稳定性证明。决定只依据同时列出的原方程绝对/整体相对线性残差与方向差，不作线性误差已严格控制的推广。

## 复现与来源

```sh
python topics/visible-flex-held-10pct/scripts/resume_m3/compare_endpoint_newton_coordinates.py --run /workspace/scratch/7322d0dee069/m3_work/beta4625-q039912-raw-lam1-b032-w040-m16 --coordinate-probe /workspace/scratch/7322d0dee069/m3_work/m16-supported-orthogonal-coordinate-probe.json --out /workspace/scratch/7322d0dee069/m3_work/m3-circle-endpoint-newton-coordinate-comparison.json
```

进程41009正常exit0，约76.15秒。来源：`compare_endpoint_newton_coordinates.py`、已登记 `m3_raw_diagnostic_model.py`、`circle_endpoint_newton_coordinate_comparison_record.json`；后者保留实际失败CP/系数块/affine尾/坐标probe/源文件SHA、物理全参数、T的构造参数/标量与输入身份检查。可再生的完整A/S矩阵只留在已给SHA的scratch输出；大矩阵、checkpoint和曲线数组不入仓库。
