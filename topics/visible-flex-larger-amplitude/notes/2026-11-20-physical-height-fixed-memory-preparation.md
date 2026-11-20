# 完整物理高度方向：永久曲率/半径位置记忆

状态：这次新实现的必要半径导数检查及初读已经实际通过，完整 256 次方向正在运行。未将启动当作求解成功。本条接 [物理高度首方向](2026-11-20-physical-height-first-result.md) 的具体遗漏峰证据；不再重复其单 witness 预算。

本条保留启动时的预算与必要检查；完整真实接受终态现见[13ce结果](2026-11-20-physical-height-fixed-memory-first-result.md)。下列执行源位置已换为字节相同的公共仓库路径。

## 1. 实际父与数值余量

父为 geometry v4b 已落盘第一个接受点 `work/geometry_path/curvature-qp-protected-992-twelve-step.accepted-1.npz`，SHA256 `24de4d7ea9d94c66f1daa948c96b1a396369e450ea34688d72016f14be4dda5a`。不是以当前正在变化的 progress 文件冒充父数组。

完整初读：weighted SSE=.35376249806745763，weighted mean=7.28442643711244e−5，all raw=698.728195663276，legacy raw=174.87636332193435，最大点 Gram=.045854577237769645，min determinant=.9689867440221298，H=1.9082325420224515。

本次数值 screen=.992，要求仍是原来的 reach≥.03 D，不改变 README 完成标准或真实必要阈值 1。它接根对危险胞的连续曲率界后选定的算法余量；仍只是求解时必要点筛选，不是 reach 证书。

源传来的静态小清单 `work/geometry_path/curvature-qp-protected-992-step1-witnesses.json` SHA256 `6bf691336d0d6893f7dfba7f27512fb9b07c18614ac5d5ce42ef8585a85ed58f`，含 20 个任意曲率位置、3 个任意半径位置及其历史 grid 拒绝峰记忆。合并本支已经付出的双 basin、prefix 拒绝峰及局部半径点、去除重复后，形成 57 个 κ 位置与 13 个半径位置。全部仅传位置，新场的值、符号、分支及梯度重算。

该父在这些全部位置上的真实初读：K=8.064315474195155、D_lb=4.091316631409991、.03 D_lb K=.9898100406153475<.992，与实际 v4b 接受态一致。这个一致性是新位置并集上的实际读取，不是沿用旧 κ 数值。

## 2. 约束与记忆规则

旧完整物理高度 map、全部 A/E/D 与原端口、1280 粗列及新正范数白化不变。新增的是任意半径位置的完整 cotangent。若 R(x)=2|F(x)|，则其六 jet cotangent 只有

$$
\frac{\partial R}{\partial F}=2F/|F|
$$

非零，其余 Fs、Fφ、Fss、Fsφ、Fφφ 分量为零。直接复用完整任意点 transpose，把原 Hermite、core→ρ/θ→lift 及 H 链保留。

对每个已知曲率位置 j，选当前真实直径伙伴中最大的 D_j，并强制保留

$$
\nabla(.03D_j|\kappa_j|)
=.03\left(D_j\operatorname{sgn}(\kappa_j)\nabla\kappa_j
+|\kappa_j|\nabla D_j\right)
$$

的当前步切向行。完整的非线性未知量及每条 Gram 方程都未冻结；投影只限制这一方向。57 个强制位置超过原默认 32 行，本次显式用 `--active-max-rows 64`，余位按当前近活动程度补充。实际 64 行经相对 1e−10 数值秩截断保留 49，QR 正交误差 1.1324274851176597e−14。

全部已知 κ 与 radius 位置在整条 line search 中永久保留，不作 LRU 淘汰。每个已经支付真实几何读取的试步，其新最坏 Gauss/任意 κ 位置及最远位置再追加到永久记忆。后续 trial 继续读它们；下一个方向也把它们加入活动行。强制行数不足会明确报错，不悄悄丢掉已知位置。这个规则没有使有限点覆盖变成连续证书。

## 3. 唯一新增导数检查

没有重做已经通过的高度 map、旧 Gram 或旧 κ transpose 检查。只核新增任意半径行经过完整 T 的方向导数：seed=2026112004，ε=1e−30，点 cell881、u=.315924656154、φ=.474459952722。

预测导数 .00126061199120247；复步读 `2 sqrt(F_complexᵀ F_complex)` 的导数 .0012606119912024639，相对差 4.816336992104386e−15。双线性复步平方根在实半径为正的当前场上取同一解析分支，不使用复向量的带共轭 norm。

## 4. 完整小源、位置清单及字面命令

- `fullclosed_gauss_physical_height_memory_lm.py`，34,495 bytes，SHA256 `ae596f07e8808737e26f95ec67d79d81bf696af264b11fc791165abf05a8697b`。
- `fullclosed_point_cotangent_memory.py`，15,829 bytes，SHA256 `029f581c74082e36fd37663192a0bb42a20ef595c324c1d4e1e8f85e1657c26e`。
- 沿用 `physical_height_coordinates.py`，SHA256 `f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e`。
- 完整小位置输入 `protected-step1-curvature-manifest.json`（57 点），SHA256 `34f0e2c3e795241599e33aad5908c2156a0c4455dc66f3316cd3cd846079d30f`。
- 完整小位置输入 `protected-step1-radius-manifest.json`（13 点），SHA256 `ddc74f4765fe4556c6af63b017fad2f4f55e60c5707ae625e6d8e8a650270db9`。

cwd=`/workspace/scratch/24b2ab87057a`。本次真正执行 session=67573，日志 `work/fullclosed_solver/logs/gauss-physical-height-memory-first.log`；以下把全部相关默认值展开，输出目录必须不存在。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_memory_lm.py \
  --repo math-research-public \
  --bundle work/geometry_path/curvature-qp-protected-992-twelve-step.accepted-1.npz \
  --outdir work/fullclosed_solver/gauss-physical-height-memory-first \
  --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
  --implementation math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
  --base-batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
  --observations work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --basis-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
  --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
  --helpers math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_lm.py \
  --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
  --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
  --geometry-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
  --geometry-observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
  --point-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_cotangent_memory.py \
  --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
  --witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-step1-curvature-locations.json \
  --radius-witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-step1-radius-locations.json \
  --angles 2048 --stage-block 64 --legacy-fraction .5 --low-modes 12 \
  --coarse-centers 0.3,0.6,0.8300000000000001,1.0570671854957785,1.1975374839662283,1.3580749679324564,1.5587468228902417,1.759418677848027,1.9400233473100337,2.140695202267819,2.26109831524249 \
  --reach-ratio .03 --reach-safety-factor .992 \
  --active-band .025 --active-max-rows 64 --active-rank-tolerance 1e-10 \
  --active-top-curvature 16 --active-top-radius 2 \
  --max-directions 1 --maxiter 256 --damping .0025 \
  --lsmr-atol 1e-6 --lsmr-btol 1e-6 --line-trials 15 --target 5e-7
```

本条不预报该方向是否接受。实际 trial、局部峰后验读、终态数组 SHA 与是否达到有限点目标另按真实完成结果登记。

父24de可由[v4b十二步完整命令](2026-11-20-curvature-qp-protected-992-twelve-step-result.md)在第一个接受步重建；默认保存该独立checkpoint。原warm/同标量carrier继续按该记录所链接的完整输入链取得。小位置JSON是完整算法输入参数，非逐场raw报告。
