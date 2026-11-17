# 原解析 scalar 的真实 Frenet 扩域到 s=.995

2026-11-17，Astra-larger-parallel-16f63c8b-20261117。**两次有限BVP真接受及实际C²前缀读出；仍是开放前缀。** 本次把s从.992推到.993、.995，而不是改growth-scale参数。当前a′仍正，尚未越过最大半径或形成内向帽。

## 固定来源和有限边界设计

父为已刊[.992 M112实际精化场](2026-11-17-parallel-numerical-0992-refinement-and-tail-trace.md)，SHA

```text
b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25
```

原Profile的精确有理节点表达及从s=.99开始的常角曲率解析延伸保持同一函数；参数仍为

```text
a(.99)=1.1666064106120295
a_prime(.99)=.3579486389103069
a_second(.99)=-2.0101206107275877
angular_curvature=2.15275972133223
```

完整M112/N2048的338状态和338边界均保留，前三核心系数保持b677目标。每次在其**实际已接受旧末点**重建完整主部法向矩阵L，并以该末点实际0/1/2时间jet的二阶预测给新右端；运行中L及右端固定。这是明确的有限扩域边界设计，不是真实非线性尾DN。两行比较不是同一有限区间/同一边界问题的网格收敛表。

驱动沿用已冻结fresh-J helper；旧[.99→.996大步尝试](2026-11-17-parallel-numerical-0991-continuation.md)的失败范围保留，本次不同接受父、M和分步过程不能改写其历史。

## 实际两端解和同场几何

| 量 | s=.993 | s=.995 |
|---|---:|---:|
| 接受父末端 | .992 | .993 |
| duration / 新初猜步长 | .001 / .0002 | .002 / .00025 |
| max_nodes | 1600 | 1800 |
| 实际节点 | 491 | 499 |
| 求解秒数 | 44.4101 | 50.9614 |
| collocation RMS | 9.32555215e−9 | 9.32555845e−9 |
| BC max | 8.67362e−19 | 1.73472e−18 |
| **真实quintic Gram算子最大值** | 2.58724837e−7 | 4.00099356e−7 |
| 真主曲率最大采样 | 6.301729651 | 6.301723280 |
| core轴支撑差 | .960000997447 | .960001022540 |
| 固定原见证点到前缀的最小采样距离 | .960000997447 | .960001022540 |
| 镜像前缀两倍原点范数proxy | 3.50407927819 | 3.50655008401 |

BVP共同tol=1e−8、bc_tol=1e−11。实际几何另由原完整节点0/1/2jet的唯一quintic定义，每cell取四分点并保2048角；两次分别5,017,600与5,099,520点。曲率用实际位置一、二阶导数计算，没有把ODE预测场当作插值导数。

.993最大Gram位于s=.96575、phi=3.6447383520162835；.995最大Gram移到新末端、phi=3.2090878082567613。增加区间后的误差有所上升，不能因两次都低于1e−6就称固定g精化已完成。

.995真实参考末端为

```text
a=1.168370992981991
a_prime=.347877494281633
a_second=-2.0182983461210213
```

末圈实际高度采样范围[.8281031461680896,.9942807847913279]。这些只是当前已接受域的数字；没有返回的更深扩域不作成功预填。完整闭面D、平cuff/固定帽、固定H、含反射E3、全体点对reach和同g/同参数/全t精化仍未支付。

## 冻结源码和复现

驱动 `parallel_20261117_continue.py` SHA
`8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`；实际readout源 SHA
`045533247125e318d5b5051f0e98b286f287126f51c6e616d938019f8432d29c`。Profile及Frenet符号源身份与父场记录一致。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue.py \
 --input /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
 --duration .001 --step .0002 --fixed-modes 3 --modes 112 --angles 2048 \
 --tol 1e-8 --max-nodes 1600 \
 --out /workspace/scratch/16f63c8bce6b/parallel-continue0993-m112.json.gz
```

第二次输入该新接受文件，duration=.002、step=.00025、max_nodes1800，输出 `parallel-continue0995-m112.json.gz`。readout分别使用对应输入及 `--angles 2048 --radial-subdivisions 4`，完整调用沿用父场笔记。历史输出SHA：

```text
parallel-continue0993-m112.json.gz
4e7a5681c5be6c901676c7e08bf598c2a35fa63899dc573868035b6ebee650f8
parallel-continue0993-m112-readout.json
1cfbef0e8b0c9fa0258b60e493ff07134c07c127d3fe19ecc2022375a4eba126
parallel-continue0995-m112.json.gz
d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f
parallel-continue0995-m112-readout.json
e5c72051283f717b9203840cf3d622961bffd06c404c5da14224b4b30a3fb281
```

raw仅仓库外。后续继续扩域，并在实际新切口重新核长度、曲率和收尾条件；当前没有把参考圆弧的转弯或预算代替真实非轴场。
