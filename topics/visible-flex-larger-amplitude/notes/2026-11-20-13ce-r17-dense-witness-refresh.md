# 13ce 对 r17 密角新峰的实际补读

输入真实场 SHA256 `13ce4975470b0aca3717ce20402616688857f5fd3b844f83d1a4f338af418614`。这条只复核新发现的位置，不重复原 Gauss 扫描或原几个已登记 basin 的优化。

原 r17 N8192 诊断小清单 `work/geometry_path/curvature-qp-r17-angular8192-witnesses.json` 的 SHA256 是 `52723ab1e61df0bb52c23f32d5c9396e54d7ef3e1869f05bc285a45910845f60`；它在另一个真实场上发现 cell227、u0、φ=.667566753913 的较高峰。读取时只取45个任意κ和7个任意radius坐标，旧场 κ/D 数字没有作为新场参数。

## 实际结果

52个新位置全部在13ce重新评价。新点集的最大κ为8.06167505037325。cell227原种子在13ce的K=7.645661093562703；一次局部细化至u=2.2014390310687305e−14、φ=.6660930980353788，K=7.652870813810301。半径新种子细化至cell881、u=.13902684021846082、φ=.49182652804702437，D点下界4.091847949611797。两次Nelder–Mead均success=true，迭代/调用数分别48/105与59/135，x/f tol=2e−10、maxiter300。

这没有替代同一13ce已经实际找到的更高低φ峰8.063363121077368。与那条同数组SHA的先前点证据合并，最大已知κ仍为8.063363121077368，D点下界仍4.091847949611797，必要点乘积仍 .9898216756186741<.992。本次新点集单独的 .9896144557591907 不能误写为更紧的整体最大值。

因此本次扩大已知位置集合没有触发13ce的数值恢复分支；从此父继续完整方向是依据实际复读，不是沿用旧的qualified标签。所有数值仍仅点下界及局部搜索见证，未证明连续最大值或reach。

## 完整来源和字面命令

reader_v2源码 SHA256 `03edefb832daefd5500099e33d30e0eb279ea2e6d22770b393200aa0eaaa5556`。实际报告在 `work/fullclosed_solver/gauss-height-memory-r17-new-points.json`，报告SHA256 `3f6445ea4d0dcae1ac8cd0224772c170cd465f6292698f417d7c9f1ec4ec367b`；其输入/source SHA、52点读数及两次完整优化状态保留于scratch，不把整段诊断写进Git。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/read_known_geometric_basins_v2.py \
  --repo math-research-public \
  --bundle work/fullclosed_solver/gauss-physical-height-memory-first/final.npz \
  --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --local-reader math-research-public/topics/visible-flex-larger-amplitude/scripts/read_closed_local_extremum_20261120.py \
  --fixed-manifest work/geometry_path/curvature-qp-r17-angular8192-witnesses.json \
  --curvature-point 227,0,.667566753913 \
  --radius-point 881,.2334093306,.4827103841 \
  --grid-curvature 8.0170467877243 --grid-diameter 4.091846962221483 \
  --reach-ratio .03 --safety .992 \
  --out work/fullclosed_solver/gauss-height-memory-r17-new-points.json
```

为公开复现，另有纯位置参数文件 `math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-r17-angular8192-locations-only.json`，3,718 bytes、SHA256 `4b53ab5c93701611ef52d7cfb57b26a650a888a0324c2edd17535f25220666a0`，完整保留本次reader实际消费的45+7坐标、carrier SHA及原清单SHA，没有旧几何诊断。上条CLI可将fixed-manifest换成该纯参数文件重现同一计算语义；它不声称与原诊断清单文件SHA相同。原top-level grid坐标本来就属于已付全Gauss扫描，本reader没有假装额外重扫它们。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
