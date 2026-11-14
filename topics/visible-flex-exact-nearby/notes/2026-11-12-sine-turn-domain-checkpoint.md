# δ5 正弦像与准确转向域检查点

状态：R65 的局部解析域定理及下列有限有向证书已完成；完整两腿覆盖仍在推进。
没有真实流／共轭残差、KAM 或闭曲面完成结论。

## 已完成输入

对象、紧根、参考时间及 R59 盒的 SHA 全写入每个报告。
准确对象为 δ5 = −7789843107295549/4611686018427387904，网格来自
`step4_shared1032_reference_{forward,backward}/manifest.json`；网格身份为 δ4，
实际场身份为 δ5，二者不混淆。无限 R33 原函数的时间系数、全部角 alias／尾、
全部时间尾、真根高阶消根尾均已付。使用物理 θ 带 1/64，外带 1/32，R3/S4。

两腿各 0、1、2、548、549 共十段的真转向域全部实际通过，包含四个准确
±π/2 端点。统一 |D|>0.37529、Re Q>6.62159、|dθ/dτ|<0.22454。
这些常数不外推到其余区间。forward 第 3 段的两个普通 common germs 也均通过。

## 失败保留及合理后续

最先请求 14 段的编排在 forward3 被严格拒绝，因为该完整实径向像越出唯一
root common span。该段后来用普通两-germ union 付清。forward547 预备改用
精确二分普通域，不将相邻 span 的 K 多项式冒作 K(t)=0。

N512/Q256、160 bits 的五个快探针都在 native root refinement 被拒绝，消息为
`native refinement escaped the original positive root certificate`。这是当前
Q256 无限 E 预算无法把根收进既有紧区间的检查失败，不是图或域不存在。
后续可先使用独立 Q512 真根包，再对同一真实对象选择较短的场表示；必须仍
支付该表示自身的无限尾。此批没有假报任何 Q256 域通过。

新全支入口将使用真实单调端点 t sin(τ左)、t sin(τ右) 的有向包络枚举 germs。
这可避免宽 Arb 时间球造成的假阳性短 span，只有实际端点分离成立时才减少列表。
新的大时间半径、全覆盖器与 live 报告不在本冻结清单。

## 精确重跑入口

在本课题目录运行，依赖 python-flint 0.9、NumPy。避免产生 __pycache__。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_full_angle_sine_domain.py \
  --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --segment 0 --mode turn \
  --curvature-radius 3/1250 --radial-degree 64 \
  --time-order 40 --angles 1024 --cutoff 255 --primitive-nodes 512 --bits 192 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_forward000_turn_domain.json
```

其余九段只替换 leg、segment 与相应输出文件，准确请求列表见
`type_fixed_step02_d5_exact_affine_step5_turn_domain_batch_complete.json`。
普通 forward3 改为 `--segment 3 --mode ordinary`，去掉两个 curvature 参数，
输出 `type_fixed_step02_d5_exact_affine_step5_forward003_ordinary_domain.json`。
每次真正重跑的 elapsed 字段会改变整文件 SHA；不得复制旧摘要重造报告。

五个失败快探针见 `...step5_ordinary_fast_domain_batch.json`，其
`requested_cases` 逐项给 leg、segment、准确 sub-left/sub-right；用同入口
`--mode ordinary --angles 512 --cutoff 255 --primitive-nodes 256 --bits 160`
重放。保留异常是其实际结果，不能把 `complete`（遍历请求结束）解释为已证明。

源码独审由 independent_audit 完成，见
`2026-11-12-sine-turn-domain-independent-audit.md`。数学正文 R65 明确了
principal asin 的物理支、负 r 的时间方向、真 Q 因式、germ 边界和域继承限制。

下一项持续工作：在同一准确对象上完成两腿的闭时间覆盖，继承域必须检查
准确复圆盘包含与同一真实 germ；随后接真实场系数及连续残差，不能在本检查点收尾。
