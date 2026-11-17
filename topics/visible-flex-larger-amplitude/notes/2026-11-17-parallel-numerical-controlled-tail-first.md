# 浅端完整双迹与新标量背景：两次失败的有限 BVP

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。这里把浅端非均值 P、K 同时固定，释放 M 个背景函数参数，以直接支付 prefix 的非均值 DN 配平。本条两次实际运行均失败，没有新的接受父，也没有达到完整课题的结论。

## 完整问题与新 g 的身份

材料角状态仍是完整 `P_sin(M), K_cos_nonzero(M), c`。浅端固定真实 trace 的前 M 个 P 和 K 系数乘 lambda，并施加字面 mean=0；深端固定 M 个 P 系数为零。边界有 `3M+1` 行，未知为 `2M+1` 个状态及 M 个常数参数。没有删除状态方程、均值方程或深端行。浅端 P/K 及深端 P 行除以 lambda 只作数值尺度调整，不改变零集合。

新标量背景定义为原固定 Hermite logw 加上 M 个紧支撑多项式泡。每个泡在支撑两端有零0/1/2 jets，以标准化的 `64 u^3(1-u)^3 Legendre_d(2u-1)` 给出。背景改变仅在支撑内部，cut 和 deep 的原有 jets 保留。第一次把两个泡放在整个 cell0；第二次把同样的偶、奇两个泡仅放在 cell0 的 valley segment4，物理 r 区间约为 `[1.33580198,1.44202421]`。

完整参数 Jacobian 为 `F_ell B_x + F_z (2zB)`，状态 Jacobian 仍由完整有限方程计算。保持原 S,D,L,N 正性，并显式允许 y=1+K 的符号改变；两次终态 y 实际仍正。另施加 `abs(p_j)<=5` 以及当前求解评价点的参考曲率 `abs(w_r)/(1+w²)^(3/2)<=7`。后者是新设计中的采样可行域，**不是**连续曲率证书或实际非轴 reach 证书。

输出 metric 文件用 `parallel-frozen-logw-controls-v1` 明确保存原背景字节和 SHA、泡定义、参数；读取者必须用源码中的 `FrozenControlBackground`。其精确定义是原 Hermite 加 factored 多项式，展开 PPoly 只是求值缓存。失败输出不能作为已接受新 g 或新场。

## 实际结果

共同设置 M2/N128、lambda=1e-5、source-index、tol1e-6、max_nodes12000。初猜来自已接受 M8 的新有限 Dirichlet 场，显式截断为 M2；它不是已接受的 M2 双迹解。

| 支撑 | 最终参数 | 节点 | 秒 | solver RMS | scaled BC max | sampled max reference curvature | min L |
|---|---|---:|---:|---:|---:|---:|---:|
| cell0 全胞元 | `[-.8190235590,-.3823260241]` | 6522 | 24.96 | .17228393 | .12625892 | 6.99945367 | .98756379 |
| cell0 valley | `[2.8310638209,-.5214244636]` | 6245 | 45.55 | 2.41776223 | .08063953 | 6.99994232 | .34514282 |

两者都以所需加点超过上限结束。终态靠近参考曲率7的采样约束；第二次边界剩余较小，但完整方程剩余更大，不能算改善后的接受解。最大 mean 漂移分别为 `.0003873,.0093108`，完整 physical-r K 方程余项分别约 `16.04,2009.58`。这里记录失败控制路线的明确范围，不声称不存在可配平背景。

输出与 SHA256：

```text
parallel-controlled-m2-scale1e5.json.gz
daf98ce8a0ef25d17257a0ad8ddd74edb2eeced449adf161d39fea95e66bf15c
parallel-controlled-m2-scale1e5-background.json
81af84efd34a85d0d42c5b2bcdfa47430965745ca8a3565c455ba5b13bd0a0f1
parallel-controlled-valley-m2-scale1e5.json.gz
8280fb154d35a25f9c342603f9c44e0895d3668a0424cb5e377a46b24065cad2
parallel-controlled-valley-m2-scale1e5-background.json
48303be4c5e81fc0e396a8ec0f272fd843646ddce81bbc182829e846db105e73
```

## 源码版本与复现

第一次实际运行时通用文件名后来增加了 valley 选项；原运行字节已完整保存为 [controlled_tail_v1.py](../scripts/parallel_20261117_controlled_tail_v1.py)，SHA `066749f53e88ca259b110d7a00be5a0e6c8deac285888c3fb032c257700668ae`，与输出内 source SHA 一致。第二版 [controlled_tail.py](../scripts/parallel_20261117_controlled_tail.py) SHA `af1e7628859f8285379fa19e43e0e6edccc39d7d6594c82e303271515d76bfe9`。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_controlled_tail_v1.py \
 --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
 --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
 --input /workspace/scratch/16f63c8bce6b/parallel-best4-dirichlet-scale1e5.json.gz \
 --modes 2 --angles 128 --scale 1e-5 --tol 1e-6 --max-nodes 12000 \
 --allow-height-turn --parameter-bound 5 --reference-curvature-limit 7 \
 --out /workspace/scratch/16f63c8bce6b/parallel-controlled-m2-scale1e5.json.gz \
 --metric-out /workspace/scratch/16f63c8bce6b/parallel-controlled-m2-scale1e5-background.json
```

第二次用第二版文件，加 `--support-mode valley`，out 和 metric-out 改为上面对应的 valley 文件名。其余实参相同。

背景 SHA `487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`，trace SHA `c3a5c53fb090ca842c2aa00304e470da2f4151231b65bde98d21f0bbe9c17c6e`，接受初猜 SHA `654d5d47d004c10688de355c330b434db55bb89e4cc9a247084e284facce2695`。dynamic operator SHA `e21034c9f1208506d16f1bed3cc46c470fdf15425c6466eb0f9623ad0fcfa8b5`，fresh-J helper SHA `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`。

附带记录另一独立失败：固定 best4 g 的有限 deep-P=0 从已接受 lambda=5e-5 暖试1e-4，最终7668节点、RMS3.64703656、BC4.21e-10，未接受；输出 `parallel-best4-dirichlet-scale1e4-warm.json.gz` SHA `11e62a1192270e403dbf1f945be712419f7afb926b527d5ab6f7f8fece9eb4f7`。这不改变此前5e-5接受父。两条路线均继续保留真实几何、尾端0/1/2jet退休和 lambda=1接合的缺口。
