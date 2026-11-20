# 2026-11-20：完整角 H² 过渡范数的真实首方向与不等式转向

## 1. 实际身份与状态

这是从同一原标量 g、相同 M=160、923 节点/922 胞、7377 个原/新增 Gauss stage、2048 完整角行（513 精确轨道代表）的真实完整变量方向。输入是 geometry 的物理 H² 六步父 `curvature-qp-physical-h2-next-six.npz`，SHA-256 `0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`。

保留原 1,332,245 个自由变量，DI 的全部 A/E/D 与精确端口投影；物理高度可逆三角变换不变。此次附加 m≤12/r17 的 1964 个粗列，在新范数中重新白化。目标仍为原混合径向 Frobenius Jw（.5 Simpson + .5 Gauss），没有采用另一路 p8 目标。

进程自然 exit 0；一方向 256 次内迭代，453.811060686 s；Linux 真实进程 peak RSS=2,299,472 KiB。最终数组 SHA-256 `5b1e426a3ab4b3c75a1531e3d7f390b6f5c16bf5b7a7fb91bd40550ca6b82057`，方向数组 SHA-256 `2ca3bec1b104550bfc6a578bc1a66a365b819d52c716a1172546d8b285223fce`。数组、完整 raw report 与缓存只在 scratch；均不提交 Git。

结果仅为数值候选，未到 1e-6、未付连续 metric/reach/全族证书，不能收尾。该方向成功接受 α=1/32，但下降很小，不再盲重复同类等式预算。

## 2. 新范数与工作集合

令 ν=2m、λ=1+ν²、σ=sqrt(1+(ν/24)²)。在已刊物理高度 DI 范数上，全部 A/E/D 和 core 坐标的正尺度再除以 σ；H 尺度仍为 sqrt(7 S³/120)。对应系数范数为

$$
\sum_k\lambda_k\sigma_k^2\left(\sum_jw_j A_{jk}^2+\sum_i h_i E_{ik}^2+\sum_i D_{ik}^2/h_i\right)
+\sum_{m>3}\lambda_m^2\sigma_m^2 c_m^2+H^2/s_H^2.
$$

m≤12 的尺度代价变化至多 sqrt(2)，高模 A/E/D 渐近 ν²、core 渐近 ν³。core 的派生 T=-νc 已在系数估计中说明；这不是完整几何 bending energy，不能把此范数称为旧 LM 等价。原方程和自由度未改。

合并的不可变位置清单含 417 个 κ 点（7 protected）和 67 个半径点。所有位置保留于每次真正非线性筛选，不再把所有 417 点强制为同次等式。当前线性工作集合按 protected、当前 near-active 产品和最强直径伙伴排序取 192 行，其秩 87。C 仍逐块存盘，Q 只保实际秩；2 次小 Cholesky 再正交后误差 6.66e-16。该轮新增拒绝位置继续永久保存，接受时共 490 个额外真实位置。

新映射必要核：full T/T* 双线性相对误差 5.54907935427e-15，端口 4.98732999343e-18；1964 粗列规范与 literal DI.inverse(A^-1 B)/scale 的相对差 3.66158578017e-15。未重跑旧 Gram 或旧 point-cotangent 证书。

本轮同时改变角权、工作集合且使用更好的 0241 父；不能从与旧方向的数值差异中作单一因素因果断言。

## 3. 真实线搜索

初态 Jw=0.13368399851982452，max Gram=0.024013578471355768，已知全点产品 0.991894165638。使用同一人为数值余量 .992；真正 reach 必要阈值仍为 1，完成标准未变。

| α | 原径向目标 Jw | max relative Gram | 实际 K 点下界 | .03 Dlb K | 接受 |
|---:|---:|---:|---:|---:|:---:|
| 1 | 0.113272102051391 | 0.0197540264190532 | 8.69754104882901 | 1.06860090700435 | 否 |
| 0.5 | 0.12017693380396 | 0.0217940596571873 | 8.36605847351807 | 1.02792014236112 | 否 |
| 0.25 | 0.126105492088445 | 0.0229031073103609 | 8.20198661533471 | 1.00778378449604 | 否 |
| 0.125 | 0.129688456899105 | 0.0234581649523951 | 8.12169572981519 | 0.997929680797428 | 否 |
| 0.0625 | 0.131634644808292 | 0.023735827227247 | 8.08752911545947 | 0.993737189442634 | 否 |
| 0.03125 | 0.132646424264461 | 0.0238746917281547 | 8.07250721320265 | 0.991894222394142 | 是 |

接受态 all raw SSE=604.1554108873338，legacy raw SSE=151.1546561347394，H=1.879789418449448。原 Jw 仅降 0.77614% 左右；最大 Gram 降约 0.578% 。满步的线性目标预测 2.332951777819429e-5 与真平均目标 2.332418781747507e-5 很接近，主要阻力是几何约束，而非该满步 metric 非线性失真。

LSMR stop=7（256 内迭代上限），normr=.004842225716979647、normar=7.328552306149347e-6、normA=32.53047716525141、condA=33.19951566112654、normx=.13719015473139726。预算终态不是研究完成标志。

## 4. 已付的新局部复读

只对该真实接受态作必要的新峰复核：cell188/φ≈.5553、cell182/φ≈.5614、旧188/φ≈.501、821 的两个已知 basin、879 新胞内峰，以及 cell880 半径。局部优化仅给真实点下界，不是全局最大证书。

最高 K 点变为 cell188,u=0,φ=.5009884545146875，K=8.072510598353887；D 点下界=4.09577097926383，组合 .03 Dlb K=.9918946391561263<.992。新邻角 basin 本身在接受态分别 K=8.06011046268742 和 8.070621232356899；821 低 φ basin K=8.069999528303958、另一 basin K=8.065759003007654。此读出没有升级连续或真实 reach 标签。

## 5. 实际方向归因改变了后继选择

在真实 0241 父与已算满方向上，cell188,u=0,φ=.5553010452146021 的 κ 从 8.013022084505874 到 8.697541048829008；一阶 δκ=.6840556016869745。按原完整变量与物理 six-jet 两种已验证转置链分解：

- Y 贡献 .6813577283472628；物理 Fphiphi 贡献 .6848235213671731。
- m1–12 贡献 .44948827122090845，约净一阶增量的 65.7%。
- m33–80 与 m81–160 合 .2382271454356604，约 34.8%。
- m13–32 为 -.017994235593228564；均值为 .014334420623634353。

在 cell182 新峰，m1–12 贡献 .4234116138731465，而总 δκ=.545588049680841。当前旧最高点 cell188/φ=.5009630056335 的 δκ仅 .0007448960091734567，由强烈的模态正负抵消形成。

这与上一弱角范数方向“新峰 79% 的净一阶增量来自 m≥33”不同。新的主要阻力包含低模，并有当前等式工作集合在一角限制增量、邻角继续增长的具体现象；不能再无依据地只加强高模权。后继转为带实际余量的完整线性不等式 QP，允许旧峰向内移动。全部永久点仍做真正非线性筛选；不会把不在线性 working set 的点删除。

## 6. 完整可复现参数

单命令和所有默认展开在同批 [完整准备](2026-11-20-angular-h2-working-preparation.md)。该命令读取原父和 carrier，输出 `gauss-angular-h2-0241-first`；M=160，N=2048，stage_block=64，legacy_fraction=.5，low_modes=12，角转折24，µ=.0025，maxiter=256，max_directions=1，active_max_rows=192，block_columns=32768，active_band=.025，rank_cutoff=1e-10，top_curvature=16，top_radius=2，LSMR atol=btol=1e-6，line_trials=15，reach_ratio=.03，safety=.992。r17 desired centers 是

```text
.30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826
```

两份纯位置参数清单可入 Git；完整输出 JSON 只保 scratch。

- `angular_h2_coordinates.py`：5075 B，SHA-256 `11fd0b8c3bc8139cbce19374cc81ba73b47bddecb007eed3cd296285951c298b`。
- `fullclosed_point_cotangent_working.py`：20100 B，SHA-256 `fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad`。
- `fullclosed_gauss_angular_h2_lm.py`：33926 B，SHA-256 `ce6ffd8f20394d7f419056bdc14225226891c4575666f10028e2f752e35f7cea`。
- `protected-0241-working-curvature-manifest.json`：46306 B，SHA-256 `850023bf18b07ae3f437aa8844d1bd3303c6741978397102141b86d72f6acc8b`。
- `protected-0241-working-radius-manifest.json`：6623 B，SHA-256 `485c0963cedabad0d1fdb901397fe394bb3bebedd69024e9071c2432707dab1b`。
- `read_full_step_curvature_channels.py`：5721 B，SHA-256 `34b3406c363fe44a037390f3b16cfee3d75eb6bb244f70ebe883126763c785b4`。
- `read_known_geometric_basins_v2.py`：6580 B，SHA-256 `03edefb832daefd5500099e33d30e0eb279ea2e6d22770b393200aa0eaaa5556`。
- `angular-h2-full-step-curvature-channels.json`：10687 B，SHA-256 `c282ca339512b987fdadb4a25c0e237aef27adc049e1d4681d48140cd99a2c3d`。
- `angular-h2-final-known-basins.json`：9067 B，SHA-256 `69b81224f7098f14b44667e7484bca742300f59df8416a6758771aaecda52b37`。

局部复读命令（同 cwd）为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/read_known_geometric_basins_v2.py --repo math-research-public --bundle work/fullclosed_solver/gauss-angular-h2-0241-first/final.npz --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz --local-reader math-research-public/topics/visible-flex-larger-amplitude/scripts/read_closed_local_extremum_20261120.py --curvature-point 188,0,.5553010452146021 --curvature-point 182,0,.5614369683661447 --curvature-point 188,0,.5009630056335 --curvature-point 821,.422249305974,.016682618788 --curvature-point 821,.106192866623,.637095276398 --curvature-point 879,.8306046932331322,.5123495831538042 --radius-point 880,.686841094411,.529274999458 --grid-curvature 8.072507213202652 --grid-diameter 4.095770975886694 --safety .992 --out work/fullclosed_solver/angular-h2-final-known-basins.json
```

实际方向归因命令为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/read_full_step_curvature_channels.py --repo math-research-public --bundle work/geometry_path/curvature-qp-physical-h2-next-six.npz --direction work/fullclosed_solver/gauss-angular-h2-0241-first/direction-000.npz --point-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_cotangent_working.py --geometry-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py --point 188,0,.5553010452146021 --point 182,0,.5614369683661447 --point 188,0,.5009630056335 --out work/fullclosed_solver/angular-h2-full-step-curvature-channels.json
```

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
