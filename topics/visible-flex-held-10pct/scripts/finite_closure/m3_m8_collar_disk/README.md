# m3 fixed-M8 有限 C² 尾闭合小包

本包对应 `m3_smallcut_fast45_q02_fixed_m8_breaks` 的实际成功 pair，实际 q=.020001225073149356。范围是有限 C² 尾、同一背景的圆领和平盘；尚未完成 prefix 的 literal 全 Cartesian 接缝，也不把 finite far Robin 输入当无限非线性解。

主要结果与证明见 `M3-finite-C2-collar-and-disk.md`。旧 R114 的可复用引理与不能继承的范围见 `R114-closure-scope.md`；出处逐文件 hash 见 `source_ledger.json`。

## 连续界与数值诊断

- 固定旋转背景：完整增高在 [.017226894332849643,.028865103743246846]，两主曲率绝对值不超过8；背景 deep 根范围引用明确列出的旧已审结果。
- 圆领与盘：(X\cdot n>.8)、(|X|<.817)、水平半径<.050563。圆领相对 metric<1.36e-29、曲率<8.002；平盘 metric和曲率均为0。
- 外有限尾：精确定义为 shared-2jet integrated-Fr C² map；目前只有采样 metric3.59745e-8、K8.04068，不是连续全尾证书。

## 复现源闭包

原70源之外增加4个精确C²/collar脚本，均来自本公开仓库固定提交。新空目录恢复已实际执行，74文件逐一SHA通过；fresh恢复的checker重算已有collar packet得到同一精确标量。没有重跑BVP。

```bash
python recover_prefix.py \
  --repo /path/to/math-research-public \
  --dest /path/to/scratch/closure-source \
  --manifest m3_closure_source_recovery_manifest.json \
  --endpoints
```

`--endpoints` 后不附名字，使通用恢复器只恢复源；不要使用其m2默认endpoint名字。

## 从重新生成的成功 pair 再生闭合

真实BVP的checkpoint由先前m3联合计算包再生，当前closure包不在Git存储这些可重算数组。以该pair以及对应规范port为输入：

```bash
python reproduce_closure.py \
  --source-topic /path/to/scratch/closure-source/bundle/topics/visible-flexible-closed-surface \
  --short-bridge /path/to/scratch/closure-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py \
  --prefix-checkpoint /path/to/regenerated/fixed_m8/seed.json.gz \
  --tail-checkpoint /path/to/regenerated/fixed_m8/seed_tail_0004.json.gz \
  --port /path/to/regenerated/fast45/port.json \
  --outdir /path/to/scratch/new-closure
```

此命令按依赖顺序运行：同点prefix mean及完整两jet恢复、finite C² exporter、exact collar checker、物理背景常数再生、完整区间积分、analytic gates、collar/disk Fraction预算。`reproduce_closure.py` 是据已执行单步命令整理的 replay 入口；整条包装命令本次未额外重复执行，避免重做约几分钟的finite流导出。已执行 exporter 的精确 argv、原源/变换源hash与成功状态在 `finite_tail_execution_record.json`。其他源均以内容hash冻结。

原exporter只改一个metadata字面值B6.001→8.001，其数学前提由新证明支付。原代码m3角模选择仍保留；该入口不能把spacing换4就冒充n4闭合器。

## 已执行单步命令的精确设置

```text
prefix endpoint: angular=512
finite export: depth=8, steps=32, angular-nodes=256, degree=96,
  difference-step=.00005, audit-angular-nodes=128,
  audit-fractions=.25,.5,.75, background-curvature=8.001
background interval: cells=16, panels-per-piece=64, mpmath.iv dps=60
collar/disk: Fraction arithmetic on exact finite binary coefficients
```

`finite_tail_scalar_record.json` 保存实际采样量与接口误差口径；`background_interval_result.json`、`background_analytic_gates.json`、`collar_disk_scalar_result.json` 只含标量预算。`failed_interval_method.json` 保留过宽的第一版Horner区间失败，避免把它写成几何障碍。`source_and_api_verification.json` 保存fresh74源及查询/精确端点恒等式核验。

## 查询这个 capped tail

```python
from finite_closed_tail import FiniteClosedTail
tail = FiniteClosedTail(
    "new-closure/finite/tail-manifest.json",
    "closure-source/bundle/topics/visible-flexible-closed-surface/scripts/db6f_tail_integrated.py",
)
# 六项依次为 X,Xr,Xtheta,Xrr,Xrtheta,Xthetatheta：
jets = tail.upper_jets(r, theta, h_of_r, w_of_r, wr_of_r, Zcap)
# 极点及整个内盘采用普通Cartesian图：
X, derivative, hessian = tail.upper_disk_xy(x, y, Zcap)
```

h,w,wr必须取同一固定旋转背景的真实函数；`Zcap=zcut+meanVcut+h(c)`。保存的height samples不是背景的定义。生成函数在浮点里近似求值，但其数学定义是有限binary系数的精确实运算以及本稿固定背景的真实积分。

本包只含源、物理参数、命令、hash和必要标量结果。没有checkpoint、DN、H、角数组、网格或渲染图。
