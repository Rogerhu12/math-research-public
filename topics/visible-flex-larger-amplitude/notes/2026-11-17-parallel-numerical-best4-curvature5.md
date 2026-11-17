# best4 的 curvature-bound=5 新背景与实际有限 BVP

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条改变背景设计后重新求解；它不是原 g 的精化，也不把 producer 的参数值当成固定 Hermite g 或实际曲面的全域曲率界。

## 唯一设计改动及固定身份

从 [best4 确定配置生成段](2026-11-17-parallel-numerical-best4-tail-continuation.md) 生成 primitive-only 配置，其 SHA 为 `c776b7453496272129b29b52c07624e9f9c3b1af6417638123e2d03c3ef2365a`。真实 .992 cut、总宽 .6、bridge .01、prefixR8、pulseCaps 和全部160项 valleyControls 均不变。背景生成器 CLI 仅改 `--curvature-bound 5`。

新背景 `parallel-best4-k5-background.json` SHA256：

```text
ef37c9b93fda8fe7376db08846b133e9a872a2ed317987e2914363e319ca13d3
```

固定 Hermite 表仍为 depth4、每源段64点。实际 factory 的 alpha 为 `8.345568428532768`，minimumWarpWidth `.4157131221723859`，深端 `r=1.679270483693695`、`w=.0011985974673136036`。原 scalar source 的参考 heightSpan `.16604458093475957` 不是实际非轴几何的高度积分。

同源材料 m=2,4,...,16 的 far32→depth4 列全部重新传播，每源段512步；文件 `parallel-best4-k5-material-columns.json` SHA `ab3247c98e0e2bffcf540163e420e50572d9c85c5c078d7d50bea5528f2a1bfb`。没有把旧 curvature6 的深列移到这个新 g。

## 真实接受场

材料 M8/N256、tol1e-6，首先从未接受初猜解 lambda=1e-4，再用该新背景上的接受场暖起 lambda=.001。目标仍为原 material trace 的前8个 Dirichlet 系数，浅端 K 只读出，深端是上述有限线性 far 列。

| 量 | lambda=1e-4 | lambda=.001 |
|---|---:|---:|
| 节点 | 3776 | 4927 |
| 秒 | 45.92 | 42.38 |
| solver RMS | 9.98577e-7 | 9.99609e-7 |
| BC max | 2.16840e-19 | 1.69407e-21 |
| min D | .999762687 | .997747730 |
| min L | .924293868 | .212056393 |
| min y | .918553741 | .253117365 |
| max abs P | .010809775 | .093162306 |
| max abs K | .081446259 | .746882635 |
| 浅 K sampled mismatch | 1.45539e-5 | 1.43487e-4 |
| physical-r 完整 K 余项 max | .0251074 | 19.4281 |

所有诊断包括每接受 cell 的四分点实际插值导数。`--allow-height-turn` 保留，但两个接受场的 y 仍正。本次降低背景参数后，浅端 K mismatch 比旧 curvature6 同 lambda 小；同时内部 L 更低、K 更大。因此无法从 source 参数下降推断实际曲率下降。

lambda=.001 的 raw deep 非均值高度系数 l1 仍约 `9.65817e-5`，normal height derivative 的非均值系数 l1 约 `8.38472e-4`。小 w 与有限 far 行没有自动把实际高度退休成圆 cuff。实际 integral-K 高度、C²径向 Gram、曲率及冻结 Hermite 的内部峰另由几何读者核查；本条不宣称 reach 改善。

输出与 SHA256：

```text
parallel-best4-k5-material-scale1e4.json.gz
bd1e488f0eb76ecfc85359b8e794ccccd56b9ccd65f3b0bc173a09cf31cd2954
parallel-best4-k5-material-scale1e3.json.gz
015b2a25225b39cc0eacbb6560d54822ab758a601562d64c838784959beaa4f7
```

## 复现差异

按 best4 note 的同一 source recovery、配置生成及背景命令，仅将 `--curvature-bound 6` 改5并把背景输出路径改为 `parallel-best4-k5-background.json`。far 命令指向该新背景，输出改为 `parallel-best4-k5-material-columns.json`。两个 BVP 分别运行

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_tail_bvp.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-k5-background.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --deep-columns /workspace/scratch/16f63c8bce6b/parallel-best4-k5-material-columns.json \
  --modes 8 --angles 256 --scale 1e-4 --allow-height-turn --tol 1e-6 --max-nodes 12000 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-k5-material-scale1e4.json.gz
```

第二次增加 `--input` 指向这次新接受文件，scale改 `.001`，max-nodes改16000，输出为表中第二个文件。material trace SHA `c3a5c53fb090ca842c2aa00304e470da2f4151231b65bde98d21f0bbe9c17c6e`，material 高度 anchor `.9196724087226285`。

源没有修改：background generator `9abed37501b4a6ee55757082b1dd206626cf1ae5d25f9dee41aebf7baf15727d`；far propagation `9f2b98321e22ca71ab343de9f8aa01bee68beaee1d731705a156ed6664618f8f`；BVP runner `1a838ec97447664a2187fa0b942b1d668da36029403f570f270935b76203353a`；dynamic operator `e21034c9f1208506d16f1bed3cc46c470fdf15425c6466eb0f9623ad0fcfa8b5`；fresh-J helper `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`。raw 只在仓库外；全幅 prefix 接合、完整 cuff、闭面及全时刻目标仍未完成。
