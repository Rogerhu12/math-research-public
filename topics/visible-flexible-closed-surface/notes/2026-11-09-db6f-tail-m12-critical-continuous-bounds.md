# critical 第一档 M12 的完整连续尾界

计算及核查：`/root/independent_geometry`，2026-11-09，未参与源数值优化。采用已由其他人员独审的有限图、区间公式与流式存储实现。

## 1. 完整运行已经结束

输入是 `2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`，SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。它有 18,552 个有限 span，加上 R6 collar。

原 M8 最终背景包通过已审同背景精确转移得到 `2026-11-09-db6f-audit-transfer-tight-m12-critical-r01.json`，SHA256 `c3dbdbe79e42528b58b033f48e3694e70776666b8b890fbcb0d5b378539d2108`；数据 SHA256 为 `47509eb91f8b714dc78bd02a17f5386737582a88fb50c72fcee604a8b9a6ff69`。

完整调用：

```bash
python scripts/db6f-audit-tail-stream.py \
  --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json \
  --packet notes/2026-11-09-db6f-audit-transfer-tight-m12-critical-r01.json \
  --out notes/2026-11-09-db6f-audit-tail-m12-critical-tight-full.json \
  --angular 128 --direct-threshold 8.5 --progress 1000
```

进程实际退出码为 0，共 29,023 个审计盒全部完成，覆盖整个有限尾与 collar；所有曲率盒均 resolved。耗时 2,288.48 秒，RSS 334,610,432 字节，直接形算子分支调用 57 次。

结果为

$$
\varepsilon_{\rm tail}\le9.93630067500459\cdot10^{-7},
\qquad
\max_i|\kappa_i|\le8.462559071292288.
$$

正式报告 SHA256 为 `9c6a7f1b5e9a440a0a51581d76f657cb4df0784b99a2284b167062dec2db8015`，逐盒 gzip 报告 SHA256 为 `cb88576c24f831803b5fc2cf99bbb3dfa9a5be57e6337821c5d3bf7dc43fbaab`。

## 2. 完成后的覆盖与汇总核查

`2026-11-09-db6f-audit-tail-m12-critical-full-check.json` 检查了实际 manifest、背景包及其数据、逐盒报告、全部后端与 adapter 的 hash。逐个核对 29,023 行的 `packet_row`、span 与输入分割顺序，所有曲率状态为真，重新取最大值与全局报告逐位相同。

这里的 adapter SHA256 为 `adfcfbfe03643cf8a4284c078edb13d5caa49ad5eb7f94ce822ba8c27354a456`，冻结数学后台为 `ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`。它们此前已有 root 的完整逐系数存储比较和 M8 全量数值回归，不将这次作者运行自称为新的实现独审。

## 3. 与同一 closed-map 对接

root 为该 manifest 自身重新构建公共接缝，并重算前缀几何、metric 和矩；对应轻账本已经独立重放及核验。见 `2026-11-09-db6f-audit-closed-budget-m12-critical-r01.md`。

已审 whole/reach 汇总脚本实际应用于这个账本与本尾证书，结果为 `2026-11-09-db6f-audit-whole-metric-reach-m12-critical-r01.json`。帽曲率上界为 $10/3$，前缀曲率小于尾界，故全曲面 $K$ 等于上面的尾界。完整正支撑下界仍大于 $0.7370435198982139$，$D\le98/25$。

R10 的完整法向管论证给出精确有理数下界

$$
\frac{\operatorname{reach}}{D}
\ge\frac{1407374883553280}{46687172903089131}
>0.0301447870162247>0.03.
$$

全相位传递仍由同一解析旋转及材料角作用支付；固定帽的目标 metric 精确不变。这个计算未改变任何物理参数、证明图或相位区间。

## 4. 更紧背景值包的局部实际结果

在同一 critical manifest 上，raw2/raw3 的新 $w$ 供应包转移后，用已经独立完整回归的 metric-only 后端检查新 span $[9230,13843)$，共 7,393 盒。报告为 `2026-11-09-db6f-audit-metric-r23-m12-critical.json`，进程实际退出码 0。

| 所属源单元 | 实际连续 metric 上界 |
| --- | ---: |
| raw2 | $1.754747468210149\cdot10^{-11}$ |
| raw3 | $3.805081221364939\cdot10^{-10}$ |
| 选择外包碰到的首个 raw4 span | $1.131198664964397\cdot10^{-9}$ |

最后一行是 span 9230，属于尚未收紧的 raw4；它不是 raw2/raw3 新包的失败。该运行没有曲率声明。图与目标 $g$ 均未变，已完成的完整曲率证书可以保留；后续较紧 $w$ 的 metric 证书必须分别绑定其包和实际覆盖。

本节体现的是背景表示精度提高，不单独算作 G5 的几何加密。固定 $g$ 的高模、径向及时间加密证据与最终网格仍在推进，README 完成位保持为假。
