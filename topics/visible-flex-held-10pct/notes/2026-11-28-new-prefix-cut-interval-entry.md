# 完整 Fourier 外端修补的连续区间入口

本条交付独立 `geometry/cartesian_prefix_cut_metric.py` 及其实际实现检查，不登记新曲面或连续证书。真实 M24 full-H 尚未返回；该入口尚未装入一份实际完整尾 bundle。原 R73/R74 及其 hash-bound 源保持原样。

## 1. 同一真实前缀上的明确新项

按[独立完整cut合同](2026-11-28-analytic-complete-cut-target-contract.md)，取完整 prefix/tail 平面与高度频率分别并集。切口目标 T0/T1/T2 使用 literal R,w 的唯一实数表达式；ap 的平方根用向外区间计算，不冻结旧 evaluator 的 rounded ap/app。高度零模只有 T0 的 tail mean 值精确抵消，T1/T2 的完整 mean 导数保留。

新项为 `sum_j (-L)^j H_j((end-s)/L) Delta_j(psi)`，默认 L 是输入 binary64 .04 的精确实值。四阶列表分别覆盖角导数0至3和径向导数0至3。完整 D2 归一Gram使用实际冻结目标 `ds²+a_hat(s)²dtheta²`、全部原Cartesian三jet以及新修补三jet。有限尾高频没有按prefix的原side-mode数截掉。三重协变使标量Gram仍精确以2pi/3为周期。

构造器核验真实未缩放完整H、模式数、物理参数、尾bundle/packet/共享节点/spectrum、最终prefix定义数组，并要求core lift与phase chart在外端的完整两jet精确为零。新切口使用最终Cartesian零模端点Z。它没有把source primitive或中间mean spline当作整条最终均值函数。

## 2. 旧证书仅在精确未改区域继承

入口读取R74完整叶文件，逐条以Fraction核对首尾/相接/全域覆盖及每条界；同时核全部来源hash、最终定义数组和冻结目标的身份。修补在 `[0,end-L]` 精确为零，因此这部分继承同一图的已付界。只有新的cut strip重新计算；不会把旧R62或另一个λ/mean的数值搬来。

几何继承还核R73的全部原定义数组与R74数组相同，并绑定其独立精确曲率123/10后处理证书。新strip直接以有理123/10的区间值检验两侧 `K*g ± II` 的正定性。旧binary12.3的PSD诊断不混称为有理123/10的全域PSD数值；继承的精确曲率证明和新strip的PSD下界分列。

每个新叶同时通过metric原预算、support≥87/1000、radius≤67/50、面积正及曲率PSD门，才计为完成。径向区间在全部原共同knots、冻结profile/bridge/target-radius补丁接口以及新cut-start分割。未过会二分，未解决则保留明确未解决状态。

## 3. 实际检查及边界

编译与公开CLI `--help` 已实际成功。独立75位检查使用小型构造系数，包含两侧不同频率集合、负平面频率、非零尾mean和角三阶；用直接高精度Cartesian求导对照完整D2 Gram。实际通过1152个角点导数、5760个角盒导数、60个右端Hermite导数、27个径向Gram导数和81个角向Gram导数，合计7080个包含检查，峰66436KiB。加载/返回源码SHA均为 `a5b8f4f821f6b284cb124d8f2c90d471271b91f16218c8ff6157f93d609892a7`，检查期间未变。全记录见[独立检查](2026-11-28-design-cut-algebra-review.json)。

这不以采样重新证明区间核，也不把构造数组当已接受场；构造器/完整cover/新几何证书的实际正向运行仍待真实full-H输入。cut-start处仅要求C²；退化点选择左三阶jet不构成全局C³声称，右侧有宽度的叶使用完整右多项式范围。

检查可再生为：

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/design/check_cut_geometry_algebra.py /actual/work/new-cut-algebra-check
```

实际完整输入存在后，证书入口为（以下尚未执行，不是成功记录）：

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_cut_metric.py \
  --tables /actual/work/new-prefix-angular/summary.json \
  --geometry-bundle /actual/work/full-height-tail/geometry-bundle.json \
  --base-metric /actual/work/uncut-prefix-metric/summary.json \
  --base-geometry /actual/work/uncut-prefix-geometry/summary.json \
  --base-curvature /actual/work/uncut-prefix-geometry/exact-curvature-budget.json \
  --outdir /actual/work/full-cut-prefix-proof
```

全部区间数组和完整叶留仓外。即使该入口未来通过，它仍只覆盖修补后的prefix/bridge；尾的物理半径重参数带、全尾/盘/帽、准确握持λ1、全闭图reach与同一问题加密均须另外真实验收。真正coupled source仍需独立诚实输入门，不把它改称原linear source。
