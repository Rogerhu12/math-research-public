# fixed-M8 全闭 C² 图及连续几何复现包

本包接续已经公开的 R21 finite tail/collar/disk 包。完整证明在 `R23-shared-jets-closed-c2-geometry.md`。

已证明的本层范围：由实际 fixed-M8 pair 生成整个显式闭 $C^2$ 曲面，统一 Cartesian 中心/外 cut 二阶数据及一个全局 mean gauge，给出全域支持量、实际曲率、嵌入和 reach 界；全相位查询使用同样严格 $C^2$ 的材料角图。安全界是 support>.7、K≤10、D<2.30242、reach≥.1、reach/D>.0434。

默认帽标记强度为0，所以相位像互为刚体旋转、delta_E=0。本包没有声称完成10%题，没有整域等距证书，也没有把有限tail截断当成无限非线性解。M8的prefix/tail采样metric都低于4e-8，但新材料角表示仍需纳入后续整域metric审计。

## 依赖及源恢复

公共仓库根为 REPO；课题目录为 `REPO/topics/visible-flex-held-10pct`。

1. `scripts/nonlinear_tail/m3_coupled_seed_deliverable/replay.py` 再生原q02联合设计态及其同g fixed-M8比较态。
2. `scripts/finite_closure/m3_m8_collar_disk/` 是已经公开的R21包（发布提交 `ef386aeff17`）。其 `m3_closure_source_recovery_manifest.json` 恢复74个精确来源文件，补足原70源里没有的 integrated-Fr exporter/reader 与 exact collar checker。
3. 本包只新增全闭表示、证明、区间核及phase查询；不复制旧求解器或保存生成数组。

先按R21 README恢复74源，SOURCE指向恢复后的 `bundle/topics/visible-flexible-closed-surface`。SHORT_BRIDGE指向同bundle里的 `topics/visible-flex-larger-amplitude/computations/root_short_bridge.py`。PREFIX、TAIL、PORT均来自重新生成的同一物理g成功pair；不能替换成旧design-M8或其它tail。

## 可执行再生链

先执行R21的有限闭尾再生：

```bash
python R21_PACKAGE/reproduce_closure.py \
  --source-topic SOURCE --short-bridge SHORT_BRIDGE \
  --prefix-checkpoint PREFIX --tail-checkpoint TAIL --port PORT \
  --outdir NEW_CLOSURE_OUTPUT
```

再执行本包：

```bash
python reproduce_closed_map.py \
  --source-topic SOURCE --short-bridge SHORT_BRIDGE \
  --prefix-checkpoint PREFIX --tail-checkpoint TAIL --port PORT \
  --closure-package R21_PACKAGE --closure-output NEW_CLOSURE_OUTPUT \
  --outdir NEW_CLOSED_MAP_OUTPUT
```

`reproduce_closed_map.py` 是据已经执行成功的单步整理的包装入口；没有额外重复跑整条链。每个单步来源、真实输出hash、已知的原argv、根据固定参数整理的replay argv均在 `execution_record.json` 区分。它不求解BVP。

运行会在scratch再生有限表示数组、区间结果及若干查询点；这些输出不提交到仓库。Git包只有源、来源参数、必要紧凑标量与hash。

## 查询API

```python
from closed_m3_map import ClosedM3Map
m = ClosedM3Map(SOURCE, SHORT_BRIDGE, PREFIX, TAIL, PORT,
    NEW_CLOSURE_OUTPUT + '/finite/tail-manifest.json',
    SOURCE + '/scripts/db6f_tail_integrated.py',
    R21_PACKAGE + '/finite_closed_tail.py')
try:
    # signed s跨过中心，依次是X,Xs,Xss,Xtheta,Xthetatheta,Xstheta。
    jets = m.prefix_jets(s, theta, phase=.17)
    # side=1/-1分别是上/下片；同样给出完整二阶数据。
    jets = m.tail_jets(radius, theta, side=1, phase=.17)
    # 极点使用普通Cartesian图，不依赖极坐标雅可比。
    X, DX, D2X = m.disk_jets(x, y, side=1)
finally:
    m.close()
```

数学对象由有限二进制常数、共享Hermite公式及固定背景真实积分定义。查询器是这些定义的近似求值器；不是把浮点函数的微小接缝误差解释为实际裂缝。背景查询的极深半径若超出binary64解析能力会明确报错，盘与有限circle collar按精确定义处理。

## 已执行结果与限制

- 全prefix：985径向区间 × 512完整角盒=504320盒，零失败；中心有1536个严格符号逆函数括区。
- 全finite tail：4637段、73系数的Bernstein与Fourier范数界；实际曲率≤9.281428927，support≥.7179126192。
- complete cut lift：全角一、二阶代价已计入prefix；两侧使用同一完整Cartesian函数。
- R21均值→新shared均值只作一次全局平移：−703/2^50，其支持量和半径代价已支付。
- phase材料角：共享二jet quintic，Fraction Bernstein证 |e|≤.16000000000000003，角导数>.8399；整个族C²连续。
- 上下三相位实际查询：24次prefix点、42次tail/collar/disk点；六种cut jet最大数值核对误差4.64e−16。
- 查询器实现曾在计算前有一处Python语法错误，在cut通用span求值中有一次端点roundoff拒绝，在保存标量时有一次longdouble JSON错误，均已修复；`query_implementation_failures.json`记录原hash与具体原因。它们不是数学或BVP失败。

本包的可选非零marker API未用于当前几何证书；不据此声称严格非全等。实际更精M16径向层将以同构造另行加密比较，不能自动继承本层具体数字。
