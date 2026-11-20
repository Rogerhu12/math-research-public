# 扩大永久点集合的分块完整投影

状态：本条保留从13ce启动时的完整准备说明；该方向现已自然完成，[实际小步结果与归因](2026-11-20-physical-height-streamed-first-result-and-attribution.md)另列。分块活动因子已经实际构造完成并通过自身正交检查；下面不预告非线性接受结果。此前r17密角新位置在13ce上的实际补读见 [密角新位置复读](2026-11-20-13ce-r17-dense-witness-refresh.md)，没有以别的场的κ数字代入此父。

## 1. 当前完整输入与初读

父数组SHA256 `13ce4975470b0aca3717ce20402616688857f5fd3b844f83d1a4f338af418614`。合并本支所有旧永久位置、原每次已付trial的新增峰、2b末态位置、r17 N8192新峰，以及已经实际细化的位置，得到137个κ位置与29个半径位置。全部是算法输入位置，每一值、分支及梯度重新计算。

137+29位置与全7377×2048角轨道在初态上的实际复读一致：weighted SSE=.29494283376899294，all raw=677.0803361711287，legacy raw=169.38430743157983，最大点Gram=.03981717683962849，K=8.063363121077366、D点下界4.091847949611797，乘积 .9898216756186738<.992。故本次不需要先作数值恢复；不是跳过新增点筛选。

原1,332,245自由变量、同一标量g、原quintic与lift、全部A/E/D及964端口、物理高度正范数与1280粗列保持。metric目标仍是相同的混合径向加权Frobenius目标，没有在这一轮中途改成p8或其他目标。

## 2. 与原投影相同的有限维代数

令C为归一活动行矩阵，每行是该κ位置与当前最强实际直径伙伴的乘积梯度，拉回全部增广坐标。137个已知κ行均强制保留，其余按近活动大小补到本次显式上限192。非线性场没有冻结；这里只约束当前更新切向。

把坐标列分块，逐块形成

$$
G=CC^T=\sum_j C_jC_j^T.
$$

采用与旧版本相同的相对特征值截断1e−10，若保留特征对为V、Λ，则

$$
Q_0=\Lambda^{-1/2}V^TC.
$$

C的192行逐行写入scratch的float64映射文件，不同时保存其RAM副本。每块生成Q0的相应列后即释放该块。Q0的行已经近似正交，接着两次形成小行Gram H_i=Q_i Q_iᵀ，取Cholesky H_i=L_i L_iᵀ并令 Q_{i+1}=L_i⁻¹Q_i。每次变换可逆，保留行空间不变；正交投影仍为P=I−QᵀQ。相比旧Householder QR，这改变有限精度的求和/重正交顺序，不声称逐位等同旧实现的方向。

这些块处理不改任何几何导数或Gram算子。已核的完整κ/半径cotangent和物理高度map直接复用，不再跑旧证书。实际构造时检查最终Q行Gram，若误差超过2e−11立即报错；没有把存储重构当作无需验证。

## 3. 本次实际因子与内存

- 实际192行，保留秩114；增广坐标1,334,489。
- 初次特征行Q0的行Gram误差9.372537136560986e−8；第一重正交后1.3322676295501878e−15；第二次后6.661338147750939e−16。
- 每块32768列，最大输入块50,331,648 bytes（48MiB）。
- C的scratch映射文件2,049,775,104 bytes；RAM保留Q为1,217,053,968 bytes。C文件是可重算中间数组，不进入Git。
- 此因子完成时实际Linux `ru_maxrss` 为2,167,184KiB，约2.07GiB。源继续在报告中记录求解后的实际峰值，未把这个中途读数冒充最终进程峰值。

这允许保留较大已知位置集合，避免因RAM限制造成任意点记忆淘汰。非线性line search仍真读全部Gauss、全部历史任意点及新trial追加点，余量.992仍仅数值筛选，不是reach证书。

## 4. 完整小源码与纯位置输入

- `fullclosed_gauss_physical_height_streamed_lm.py`，35,579 bytes，SHA256 `7b21e8ce397d98d387d47577a0e9fc3bb81005006359bba88e348f3a72954c3b`。
- `fullclosed_point_cotangent_streamed.py`，19,478 bytes，SHA256 `5fe5fe6aba95a4cae1eec4c1e878b150f39ea6d988eba507e7df750a47693c43`。
- 沿用高度源 `physical_height_coordinates.py`，SHA256 `f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e`。
- `protected-13ce-all-curvature-manifest.json`：137个纯位置，12,886 bytes，SHA256 `ecba40af327335fa3839531ae540cbfc9b7b1c8a08c6ebddcd06f229f2cf7955`。
- `protected-13ce-all-radius-manifest.json`：29个纯位置，3,768 bytes，SHA256 `4548cbb0f43eade55568c52abf592cb58de12d13f9028d5a432efcebb07b79bf`。

## 5. 本次实际完整CLI

cwd=`/workspace/scratch/24b2ab87057a`，session=9720；标准输出实际重定向到 `work/fullclosed_solver/logs/gauss-physical-height-streamed-13ce.log`。以下展开全部相关默认参数。输出目录必须不存在，不能覆盖已登记预算。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_streamed_lm.py \
  --repo math-research-public \
  --bundle work/fullclosed_solver/gauss-physical-height-memory-first/final.npz \
  --outdir work/fullclosed_solver/gauss-physical-height-streamed-13ce \
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
  --point-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_cotangent_streamed.py \
  --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
  --witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-13ce-all-curvature-manifest.json \
  --radius-witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-13ce-all-radius-manifest.json \
  --angles 2048 --stage-block 64 --legacy-fraction .5 --low-modes 12 \
  --coarse-centers 0.3,0.6,0.8300000000000001,1.0570671854957785,1.1975374839662283,1.3580749679324564,1.5587468228902417,1.759418677848027,1.9400233473100337,2.140695202267819,2.26109831524249 \
  --reach-ratio .03 --reach-safety-factor .992 \
  --active-band .025 --active-max-rows 192 --active-rank-tolerance 1e-10 \
  --active-top-curvature 16 --active-top-radius 2 --active-block-columns 32768 \
  --max-directions 1 --maxiter 256 --damping .0025 \
  --lsmr-atol 1e-6 --lsmr-btol 1e-6 --line-trials 15 --target 5e-7
```

实际trial及最终候选身份已在上述终态记录中登记；不能把本条因子正交性或峰值内存读数当作等距/几何完成。

公开源码路径均对应实际执行的同SHA字节；临时数组沿原输入链再生。纯位置输入若替代原诊断清单，计算语义保持，文件路径与输入清单SHA不冒称原raw报告逐字相同。
