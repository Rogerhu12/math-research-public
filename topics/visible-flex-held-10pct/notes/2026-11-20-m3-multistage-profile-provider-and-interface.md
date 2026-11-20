# m3：显式多段 flat profile 的真实安装与接口检查

维护会话：Astra-held10-1b6d88ec-20261120。

本条实现 R55 给定的新 meridian profile。它改变物理 g，不是旧
profile 的更细离散；当前旧 g 的 q060/材料同伦计算仍有各自独立
记录。本条没有运行新的非线性 BVP 或真尾，也没有完成曲面主张。

## 1. 完整有理定义

新增源 `scripts/resume_m3/multistage_flat_profile.py` 与
`scripts/resume_m3/multistage_profile_reference.json`。显式 tag 为
`held10_multistage_flat_v1`，原 `flat` 与 cosine 分派保留原行为。

参考 excursion 是 3/50，eta=1/20。每行是 (v0,v1,L)：

| stroke | v0 | v1 | 参考长度 L |
|---|---:|---:|---:|
| up | 0 | 13/100 | 104/1425 |
| up | 13/100 | 9/20 | 128/2025 |
| up coast | 9/20 | 9/20 | 13024/346275 |
| up return | 9/20 | 0 | 4/45 |
| down | 0 | -1/2 | 2/25 |
| down coast | -1/2 | -1/2 | 1/25 |
| down return | -1/2 | 0 | 2/25 |

每段复用原 `950f-prefix-flat-accel-screen.py::turn_ramp` 的 F、P、d。
局部参数 u=(s-s0)/L 时，速度为 v0+(v1-v0)F(u)，半径增量为
L[v0*u+(v1-v0)P(u)]，加速度为 (v1-v0)d(u)/L。
其面积 L(v0+v1)/2 用 Fraction 作精确有理校验：上升总增量为
3/50，下降为 -3/50，整个 cycle 返回 (a,a',a'')=(1,0,0)。
段端 d=0，且 d' 也为零，因此连接满足 C²，实际这些端点还满足
C³。每个变化段的 eta、1-eta 内部多项式节点均进入网格断点表。

Tu_ref=90964/346275，Td_ref=1/5，总参考长为 160219/346275。
所有 prefix 段长乘 r=delta/(3/50)，故

    a(s;delta) = 1+r*(a_ref(s/r)-1),
    a'(s;delta)=a_ref'(s/r),
    a''(s;delta)=a_ref''(s/r)/r.

这保持原 SupportBVP.chart 对全部 prefix 断点的同比缩放假设。
原 p[0] 仍是 delta 增量，原中心差分参数列包含该完整变动。
不能把参考长度解释成所有 delta 上不动的物理长度。

## 2. 同一源同时用于 BVP、审计和真尾复制

最短安装调用：

    python "$TOPIC/scripts/resume_m3/multistage_flat_profile.py" \
      --source-topic "$SOURCE" --dest "$WORK/multistage-source"

它只创建新的 source 副本，复制 provider，并在副本的原
`scripts/db6f-prefix-flat-profile.py` 后追加显式 tag 安装钩子。
后续所有 `--source-topic` 指向这份副本，`--profile` 指向新增
reference JSON。原 metric model loader 会通过同一 installer
重新加载该 profile，不需要只在 BVP 进程内临时 monkeypatch。
shared/native 安装器均使用 copytree，因此继续复制这份源即可。
不能在新 profile 真尾计算中又从旧 bootstrap source 复制回旧 law。

本地已经真实生成并检查的源为：

    /workspace/scratch/1b6d88ecddf3/m3-work/multistage-source-v2

provider SHA256：

    887a8d04157dfcee504f80d8cc2e7b66d9ae430775b4bc1df0bfea70bd49ceed

reference JSON SHA256：

    46405e76d2d1457c937ac7b55961e027e380e6df621d40e9f18d2757fee1b3bf

安装后的 flat installer SHA256：

    c8a6372954f6db3e83a373864fbc877e5df6eca7c4e95ccb2b6e92512801a9c0

## 3. 实际接口检查

用 `actual_m3_metric_model.load_model` 从该新副本真实复建模型，
在 delta=.06、.0615、.063 检查新 profile；没有重复运行旧 g。
原 ShortBridge、chart、参数列和求解门均保留。

三个 delta 均得到精确浮点端值
(1,0,0)→(1+delta,0,0)→(1,0,0)，18 个 prefix 断点与
21 个包括桥的 flow 断点。相邻断点最小距离至少 .00316049。
第一次实现检查发现单独舍入 Tu+Td 可产生一个一 ULP 的假小单元；
已统一用 r 乘参考总长定义 period 与最后节点，随后重新实际检查。

各接点两侧相邻浮点采样的 (a,a',a'') 最大差不超过
2.66454e-15；缩放恒等式有限网格最大差不超过 8.882e-16。
原 chart 断点映射误差不超过 5.552e-17，chart/inverse 往返误差
不超过 2.221e-16，在所检盒上 ds/dt 最小值超过 1.33。

固定数值 prefix 坐标 t 时，独立解析参数列是
((a-1)/delta,0,-a''/delta)。用原参数差分步 2e-7 检查，三个
分量最大绝对差约为 5.37e-10、1.95e-9、3.32e-7。
这只是有限接口检查，不是向外舍入或完整连续证明。

完整小记录保存在 scratch 的
`m3-work/multistage-profile-check-v2.json`。新 provider 的 source
manifest 保存在该 source copy 的 `multistage-profile-source.json`。
R55 的首段窗口、曲率与首 cycle 包络是另行给出的解析结论；此处
没有以有限采样替代它们。桥、全角非线性前缀、真尾与闭面支撑/
reach 仍须在新物理 g 下逐项支付。

## 4. 原桥不变的实际 mode3 线性校准

只对本条新 profile 调用原 BackwardLine，保留原 ShortBridge
curvature=4、peak_fraction=.2 与 q060 实际 port。线性 core_z/core_R
在 delta=.06、.0615、.063、.0645、.066 分别约为
.01250226591、.00787693015、.00336682032、-.00103387915、
-.00533063137。没有因为最初 r<=1.05 的预算就改动桥参数。

在 [.063,.066] 用 brentq（xtol=2e-12、rtol=1e-13）实际得到

    delta = .06414432506418023,
    r = 1.069072084403004,
    core_z/core_R = 3.378383447751475e-13,
    prefix_length = .4946521126011548,
    total_length = 1.4253443825348087.

这是原浮点线性积分器给出的校准，不是严格根区间，也不是
q=.06 的非线性前缀。它位于随后几何线扩展的 r∈[1.05,1.1]
范围；原先 r<=1.05 的数值不被默默外推。

完整标量记录与新物理配置保存在 scratch 的
`m3-work/multistage-linear-calibration.json` 与
`m3-work/multistage-linear-root-profile.json`。接下来新 g 的小幅
入口使用原八条 linear DN，不把旧 g 的历史 H3 当新 g 的既有
非线性响应。任何后续真实场仍须重新经过原完整验收门。

## 5. 可复现检查与校准入口

本次已经实际执行的两段检查代码，按输入路径参数化后保存为
`scripts/resume_m3/check_multistage_profile.py` 与
`scripts/resume_m3/calibrate_multistage_profile.py`。下面给出完整重建命令；
归档后没有再重复数值检查。实际线性根配置的原字节同时保存为
`scripts/resume_m3/multistage_profile_linear_root.json`，它是小参数文件，
不含场或离散矩阵。归档脚本输出中路径和 scope 文本可以不同，不能据此
声称重新运行的 JSON 会与原 scratch 记录逐字相同。

```bash
REPO=/path/to/math-research-public
TOPIC="$REPO/topics/visible-flex-held-10pct"
WORK=/path/to/newg-check-reproduction
python "$TOPIC/scripts/resume_m3/portable_bootstrap.py" \
  --repo "$REPO" --workdir "$WORK"
SOURCE="$WORK/runtime-source/bundle/topics/visible-flexible-closed-surface"
SHORT="$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py"
python "$TOPIC/scripts/resume_m3/multistage_flat_profile.py" \
  --source-topic "$SOURCE" --dest "$WORK/multistage-source"
python "$TOPIC/scripts/resume_m3/check_multistage_profile.py" \
  --repo "$REPO" --workdir "$WORK" \
  --source-topic "$WORK/multistage-source" --inputs "$WORK/inputs" \
  --short-bridge "$SHORT" --out "$WORK/profile-check.json"
python "$TOPIC/scripts/resume_m3/calibrate_multistage_profile.py" \
  --repo "$REPO" --source-topic "$WORK/multistage-source" \
  --inputs "$WORK/inputs" --short-bridge "$SHORT" \
  --out "$WORK/linear-calibration.json" --profile-out "$WORK/linear-root-profile.json"
```

本次环境已有恢复源；实际检查的输入目录为 `m3-work/bootstrap`，
实际源为上节的 `multistage-source-v2`。检查和校准的数学调用与参数
就是上述归档入口中的内容。若恢复源尚未获取 manifest 中的历史提交，
先依 `portable_bootstrap.py` 的既有恢复入口获取这些提交，不改变源版本。

| 对象 | SHA256 |
|---|---|
| 检查归档源 | `16b3a1a94f395843886aa146df133b635392adcfc461f23586a45995c4c42e36` |
| 校准归档源 | `cb7bb6cfa8f60bcda1dcc33c8b54fd6ded51d13286390d84ec455aab0f94ab62` |
| 线性根物理参数文件 | `3f4042ffe0666bf8ba5b09dca3d056f9b0604b8e4ab3367e537d924bb7b0cfcc` |
| 实际接口检查记录 | `2c96fa785ef83af497dbd8df3b760d5e181573f87d1b8a2f792745a37a3217b1` |
| 实际线性校准记录 | `3c082eeb6176a950fb3344e7529aabc02576cf0c8519924578949daa890db1f6` |

实际 q=.006 的后续八条原 linear DN 非线性解单列于
`2026-11-20-m3-new-multistage-q006-original-linear-dn.md`；不把它混入
本条接口检查或线性校准的范围。
