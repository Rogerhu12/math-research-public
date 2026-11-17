# µ-free 混合方程的最小复现

会话：`true_a_analysis`。本目录是独立实验入口；原正 A 尾求解器没有改动。

`mu_free_mixed_equations.md` 给出完整变量变换、零模、非线性求积和混合边值方程。`mu_free_fields.py` 是原密度的完整 cos/sin 扩展及解析导数；`mixed_bvp.py` 保留每点 L 和代数行，只分解整个稀疏边值 Jacobian。它既不分解局部 G，也不先对 L 消元。

## 已完成验证

`mixed_completed_scalar.json` 保留全部 12 组原引擎对照、6 组局部锥回归、6 组解析导数方向差分及全局 Jacobian 条件数。数组仅在用户指定 scratch 再生。

原引擎对照使用不可变 `general_root_tail_momentum.mjs` 的原正 A 实现，包含 M4/M8、w=.00358/.08/.3、正负 r_x、非零 `(log w)_x`、两种 orientation 和 µ=.6/1e−17。变量变换后的 flow 最大逐项差为 3.33e−16，完整 G 最大逐项差为 3.33e−15。它没有依赖新 LU 实验模块。

锥回归从 R10 独立球面曲线构造在每一幅度单独初始化；幅度 .002/.0088，M8/M16/M32，全 cos/sin，材料相位 .17，r=.25→.27，4 个 Hermite–Simpson 区间，512 角求积。每次从确定的非零扰动出发，最终均满足原 8e−14 相对代数根门及 1e−11 微分/边界残差门。完整零模始终保留。材料相位旋转并未消除曲线本身的反射对称性，故不能把这个回归称为非反射新曲面。

高 M 原始全局 Jacobian 病态显著：未缩放欧氏范数下，a=.002 的 M8/M16/M32 条件数约为 4.9e7/3.1e10/1.5e14；a=.0088 约为 1.55e8/1.36e11/3.1e13。这些数依赖明确的变量和网格，不能解释成范数不变的阻碍；同样不能因有限 Newton 成功而宣称一致可逆。M32 的状态误差没有给出模式收敛结论。

## 源闭包与命令

manifest 的五个不可变外部依赖只有原引擎及其两个导入、R10 曲线生成器和 Fourier 输入生成器；恢复器逐个 `git show` 并核 SHA，不 checkout 其它课题，不恢复旧数组。

在仓库根目录，按实际发布路径设置 `TASK_MIXED`，并自行选择空的 `TASK_TMP`：

```bash
TASK_REPO=$PWD
TASK_MIXED=$TASK_REPO/topics/visible-flex-held-10pct/scripts/nonlinear_tail/mixed_dae
TASK_TMP=/absolute/path/to/mixed-check
python "$TASK_MIXED/recover_mixed_dependencies.py" --repo "$TASK_REPO" --scratch "$TASK_TMP"
python "$TASK_TMP/make_cone_inputs.py" --cone-source "$TASK_TMP/cone_plateau_model.py" --out "$TASK_TMP/cone_inputs.json"
OPENBLAS_NUM_THREADS=1 python "$TASK_MIXED/crosscheck_original_engine.py" --source-module "$TASK_TMP/original/general_root_tail_momentum.mjs" --out "$TASK_TMP/original-engine-crosscheck.json"
OPENBLAS_NUM_THREADS=1 python "$TASK_MIXED/probe_mixed_cone.py" --inputs "$TASK_TMP/cone_inputs.json" --out "$TASK_TMP/cone-mixed-full.json" --modes 8,16 --amplitudes .002,.0088 --intervals 4 --angular 512 --phase .17
OPENBLAS_NUM_THREADS=1 python "$TASK_MIXED/probe_mixed_cone.py" --inputs "$TASK_TMP/cone_inputs.json" --out "$TASK_TMP/cone-mixed-full-m32.json" --modes 32 --amplitudes .002,.0088 --intervals 4 --angular 512 --phase .17
OPENBLAS_NUM_THREADS=1 python "$TASK_MIXED/audit_global_conditioning.py" --reports "$TASK_TMP/cone-mixed-full.json" "$TASK_TMP/cone-mixed-full-m32.json" --out "$TASK_TMP/global-jacobian-conditioning.json"
```

依赖只有 Python、NumPy、SciPy、Node 和已有 Git 仓库。`probe_mixed_cone.py` 输出的 `.npz` 是可再生状态，不提交。相对/绝对路径和运行时间会影响报告 SHA；所有实际本次输出 SHA 已另列在紧凑记录中。

## 明确范围

这个包验证有限方程变换和混合残差实现。它没有证明任意边值可解，没有证明跨过某个有限 G 奇异值，没有证明原反射非平谷可穿 A=0，也没有支付完整闭尾、固定 g 的 C² 收敛、全局 reach 或 10% 握持目标。下一步是带真实两端数据的非恒定物理 cell，逐区间对照原 momentum 稳定段及全二 jet。
