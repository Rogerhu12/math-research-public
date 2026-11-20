# νc=24 正角二导尺度与当前几何工作集

状态：本条保留该方向的完整启动记录；[真实终态与归因](2026-11-20-angular-h2-first-result-and-attribution.md)已另付；本条登记其新范数、工作集规则、实际必要检查及可重建输入，不预告接受。依据是已登记的真实拒绝峰归因：cell171净δκ约79%来自m≥33，Y/φφ项主导；这不是先验假定高模有错。

## 1. 一个固定的新正范数

固定νc=24，ν=2m，定义

$$
\lambda_\nu=1+\nu^2,\qquad
\sigma_\nu=\sqrt{1+(\nu/24)^2}.
$$

在上一物理高度DI范数上，每个A/E/D及free core坐标的尺度都除以σν，H尺度与可逆物理高度三角map不变。于是

$$
s_A=\frac1{\sqrt w\sqrt{\lambda_\nu}\sigma_\nu},\quad
s_E=\frac1{\sqrt h\sqrt{\lambda_\nu}\sigma_\nu},\quad
s_D=\frac{\sqrt h}{\sqrt{\lambda_\nu}\sigma_\nu},\quad
s_c=\frac1{\lambda_\nu\sigma_\nu}.
$$

所有尺度严格正，全部原角模、A/E/D缺陷、core自由变量及原端口都保留。固定μ=.0025时，相对上一范数的每模正则平方成本乘以1+(ν/24)²；m≤12时至多2，M=160最高模时为178.7777777777778。它保留已经有效的低模方向，同时渐近加强A/E/D角尺度至ν⁻²、core至ν⁻³。未扫描多个转折参数。

core派生T必须计入：一个cν诱导(R,T)=(cν,−νcν)，所以其系数对平方范数为λν cν²。直接角H²系数成本为λν³cν²；此次core成本为λν²σν²cν²，并满足

$$
\frac1{576}\lambda_\nu^3 c_\nu^2
\le \lambda_\nu^2\sigma_\nu^2 c_\nu^2
\le \lambda_\nu^3 c_\nu^2.
$$

这也与完整lift里ρφ对core的三阶频率量级相容。它没有省略派生T或core→ρ/θ→lift链。上述是更新坐标范数及系数频率控制，不是精确物理弯曲能量，更不自动给连续κ上界。

粗列在**同一**新范数中白化：原分离径向Gram每个角通道的权由λν变为λνσν²。物理高度末列在A⁻¹下仍是e_H，最后对角元仍120/(7S³)，交叉项为零。没有用旧白化矩阵冒充新范数。原端口投影对每个模式各槽同乘正因子，原964条约束保留。

## 2. 全部永久点与有限线性工作集分开

0241纯位置清单含377κ/54radius，与此前完整方向保存的位置并集为417κ/67radius；7个明确protected位置保持。每次非线性trial真读全部484个位置及全部Gauss点，之后新峰继续加入，未做LRU删除。

线性working set最多192行：先保留7个protected位置与其当前最强实际D伙伴；其后在当前product≥.992−.025的候选中，优先各位置的最强D伙伴，按当前product取大者，再补其他直径伙伴。未选入当前工作行的历史位置仍在全部真实筛选中。这样不把数百个当前已非活动的过去点一概设为齐次等式。

前一版全强制等式可能让方向用未受约束的高角频率在旧点间插值；真实归因已证实那一方向的高模Y/φφ增长，但并未证明全强制等式是唯一原因。本轮同时明确更强角范数与当前工作集；与旧方向的差异不能全归到其中一个改动。

## 3. 真实父、基底与必要检查

输入 `work/geometry_path/curvature-qp-physical-h2-next-six.npz`，SHA256 `0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`。417κ/67radius全并集初读：weighted SSE=.13368399851982452，最大点Gram=.024013578471355768；K=8.07248383453773、D点下界4.095782603260304，乘积约.991894165638<.992。通过新并集后才进入LSMR。

沿用geometry实际17径向中心的1964粗列，另保完整1,333,209积分坐标。实际新检查：

- 新T/Tᵀ固定探针相对差5.549079354270155e−15，端口4.9873299934333204e−18，seed=2026112006。
- 新1964列分离范数与字面DI.inverse(A⁻¹B)/scale相对差3.661585780174103e−15；normalized coarse Gram条件数402289.4482012395。
- 端口小块最大normalized条件数13.960165322888452，最小正尺度7.303634558415858e−7。
- 192个工作行保留秩87；分块小Cholesky两次重正交误差6.661338147750939e−16。因子完成时实际RSS峰2,299,472KiB，约2.19GiB；最终峰值会随方向报告继续记录。

没有重跑旧Gram或curvature-cotangent证书。metric目标仍是同一混合径向加权Frobenius目标；p8在另一明确分支推进，没有在本轮中途切换。

## 4. 完整小源与纯输入参数

- `angular_h2_coordinates.py`，5,075 bytes，SHA256 `11fd0b8c3bc8139cbce19374cc81ba73b47bddecb007eed3cd296285951c298b`。
- `fullclosed_point_cotangent_working.py`，20,100 bytes，SHA256 `fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad`。
- `fullclosed_gauss_angular_h2_lm.py`，33,926 bytes，SHA256 `ce6ffd8f20394d7f419056bdc14225226891c4575666f10028e2f752e35f7cea`。
- `protected-0241-working-curvature-manifest.json`，417纯位置/7protected、46,306 bytes，SHA256 `850023bf18b07ae3f437aa8844d1bd3303c6741978397102141b86d72f6acc8b`。
- `protected-0241-working-radius-manifest.json`，67纯位置、6,623 bytes，SHA256 `485c0963cedabad0d1fdb901397fe394bb3bebedd69024e9071c2432707dab1b`。

## 5. 本次实际完整CLI

cwd=`/workspace/scratch/24b2ab87057a`，session=96304；日志 `work/fullclosed_solver/logs/gauss-angular-h2-0241-first.log`。以下展开全部相关默认值；输出目录须不存在。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_angular_h2_lm.py \
  --repo math-research-public \
  --bundle work/geometry_path/curvature-qp-physical-h2-next-six.npz \
  --outdir work/fullclosed_solver/gauss-angular-h2-0241-first \
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
  --point-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_cotangent_working.py \
  --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
  --angular-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/angular_h2_coordinates.py --angular-transition 24 \
  --witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-0241-working-curvature-manifest.json \
  --radius-witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-protected-0241-working-radius-manifest.json \
  --angles 2048 --stage-block 64 --legacy-fraction .5 --low-modes 12 \
  --coarse-centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
  --reach-ratio .03 --reach-safety-factor .992 \
  --active-band .025 --active-max-rows 192 --active-rank-tolerance 1e-10 \
  --active-top-curvature 16 --active-top-radius 2 --active-block-columns 32768 \
  --max-directions 1 --maxiter 256 --damping .0025 \
  --lsmr-atol 1e-6 --lsmr-btol 1e-6 --line-trials 15 --target 5e-7
```

实际接受、拒绝和小步终态已在上述结果记录登记。该准备过程本身不是README完成标准的证据。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
