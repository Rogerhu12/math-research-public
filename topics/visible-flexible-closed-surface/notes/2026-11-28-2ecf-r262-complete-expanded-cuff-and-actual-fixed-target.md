# 原真实闭图扩大平领后的完整位置、独立观察与首次固定新目标求解

[R280](../results/R280-complete-R262-ambient-cuff-enlargement-and-new-fixed-target.md) 证明的是同一个原 R262 完整空间图的全局变换。原始场 SHA 始终为 `5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8`，原十二阶实际前缀、全部有限尾、真 cuff、原 W、归一材料角均参与。只更换新源，不转移原误差/reach。

先直接在原缓存的真实径点上读取全部物理六 jets；圆周使用 384 个 native 角。对于原背景的非轴对称偏差，r≈.32 的位置及经向一阶范数约为 4.45546e−6、1.65828e−4；r≈.25 为 9.70843e−8、2.89422e−6；真 cuff 的全部两阶偏差为舍入量。这些是完整实际原场的有限观察，不据此把中间一圈认作平领。

新图用 R280 的同一保旋转全空间映射，真平领半径准确等于 8/25，参考平区从21/50向内延伸。新参考高度数值为 1.832054848 左右。实际整个有限非轴对称尾仍留在新场中，只有实际原 cuff 被严格映成新的平接圆。完整纯有理预算给 Jacobian>21/100，参考尾主曲率<6；这两个结论的对象分别是空间映射和旋转参考。

| 真实新场观察 | 全半核径点×角点 | 新固定g的相对Gram峰 | 实际曲率峰 | 最小向外支撑 |
|---|---:|---:|---:|---:|
| 初始普通组 | 73×96 | .158810080408 | 7.973295581 | .8178848940 |
| 初始径角移位组 | 75×113 | .066237673291 | 7.973295581 | .8178848942 |
| 位置求解后的第一完整独立组 | 315×192 | .158810080408 | 9.246230899 | .8178848941 |
| 位置求解后的第二完整独立组 | 292×233 | .158601977105 | 9.043601202 | .8178848940 |

两组较密的真实观察暴露原粗组的漏峰，未使用其间插值推全域界。首次位置求解在 q/T1=(S−.20)/T1 至真 cuff 的同一物理区间中设置24跨度五次样条，角频率含所有整数至13，共943个真实Cartesian系数；跨越原 cut，区间两边均零二阶端迹。保持新目标径向/角向系数及真中央不动，直接重算所有六jets和完整E/F/G。训练为241×160。实际四种阻尼3e−6、1e−4、.003、.05，每个试1、1/2、1/4、1/8、1/16；接受需训练全峰下降且曲率小于9.5。**没有接受步**，结束态准确就是初始新场。原小标记仍给δE≤1/2000。下一真实输入需保留无限振荡尾并改变幅度/外段，不把有限阶新平参考当成强解。

程序的 background.point 使用原各 profile 的真实单调逆和积分；不把空间半径的微小变动交给径向插值。数值 primitive 仍按原有限高精度积分求值，原受保护无限背景在数学定义里保留。旧报告中名为originalCuffExact/ originalCutExact 的两个元数据键原先把 long-double 展示值转成有理数；它们不是精确输入定义。已保留原版源与回执，另版只把这两个键改为原 binary64 的准确分数，并用相同输入重写新回执；两组几何/误差数据完全相同，不计为新的独立研究。R280与准确预算从始至终用原分数a、b。初版有理预算试用严格 (b−a)16/15<.48 时因真实dyadic端点超过该十进界而拒；正式证明改用充分的<1/2，未改几何输入。

## 可移植重生

S为公开课题scripts；M为R262数据目录；W为新输出目录。原数据的全部重生见[R262记录](2026-11-28-2ecf-complete-original-G12-base-numerical-composition.md)。运行 Bash：

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
G="$M/h2-c2-m48-g12-04"
a=(--scripts "$S" --data "$M/m12-prefix-data.npz.gz" --grid "$G/grid.json"
   --field "$M/h2-c2-m48-g12-04r1/result.json.field.npz"
   --query-report "$G/exact-tail-queries.json" --query-cache "$G/exact-tail-queries.json.npz")
python "$S/2ecf-r262-earlier-flat-cuff-numerical-probe.py" "${a[@]}" --output "$W/r262-enlarged-cuff-original-jets.json"
python "$S/2ecf-r262-expanded-cuff-ambient-position-v1.py" "${a[@]}" --output "$W/r262-expanded-cuff-032-direct.json"
python "$S/2ecf-r262-expanded-cuff-ambient-position.py" "${a[@]}" --output "$W/r262-expanded-cuff-032-direct-v2-metadata.json"
python "$S/2ecf-r262-expanded-cuff-fixed-target-solve.py" "${a[@]}" --ambient-source "$S/2ecf-r262-expanded-cuff-ambient-position-v1.py" --output "$W/r262-expanded-cuff-032-fixed-target-actual.json"
python "$S/2ecf-expanded-cuff-rational-geometry-bounds.py" --output "$W/r280-expanded-cuff-rational-bounds.json"
```

所有生成所列最终报告的实际进程均自然返回0。纯有理报告中32闭区间的全部最低Bernstein控制为严格正数。没有产生新STL或把局部旋转参考的曲率当作完整新场厚度。

## 文件身份

| 源或回执 | SHA-256 |
|---|---|
| 2ecf-r262-earlier-flat-cuff-numerical-probe.py | `0ccb584924c2b13d54cf7324e542eb4a8a24605877d6bfcaf11fff392ea19e55` |
| 2ecf-r262-expanded-cuff-ambient-position-v1.py | `e7c71f30be86bdb513d652b72d76e53616de2002b0318be1d048e00ab1aab8bb` |
| 2ecf-r262-expanded-cuff-ambient-position.py | `5b0b6af1e03300f77bb4ac54be329f429f0f36a30715380cca04dc6c620d4c3d` |
| 2ecf-r262-expanded-cuff-fixed-target-solve.py | `c4895526ea0012ca13f84932740cdcd08e8ce2ab88f1983061f7534ef1f5144a` |
| 2ecf-expanded-cuff-rational-geometry-bounds.py | `e47e9b5d3cf15de4db95b23ca32f7c4ed00d7b342ee26a779490d8d90650b63d` |
| r262-enlarged-cuff-original-jets.json | `9803786b5648ff44fa72c41a4fe9164d3ab6b9210d470ce92e2194de42ec462f` |
| r262-expanded-cuff-032-direct.json | `9a4d8423b29ea6d2e38afa9b522be42f62654e144eb7a01586351379034a9158` |
| r262-expanded-cuff-032-direct-v2-metadata.json | `c7f56829397e348626c0a8524a90b21ffbde960bdb74c95e02d9784116ed3852` |
| r262-expanded-cuff-032-fixed-target-actual.json | `aee8be22e18d845e5551f25f487fb52487afe264524f327f13e2d811db04c5ee` |
| r280-expanded-cuff-rational-bounds.json | `4141b2f065784387d81a4c6d5d782d17f7f91ad1051118e4ce50685e81bdfbfb` |
