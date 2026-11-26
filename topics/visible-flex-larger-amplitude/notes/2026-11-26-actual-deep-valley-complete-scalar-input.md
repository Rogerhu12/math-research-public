# R690 新输入首个真实完整标量包围

run [45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394) 实际stage54，exit0；源码提交 `f73b158511cfc59f2724e4853c78785999b5e7c0`。完整命令和所有精确输出见 [第5卷](2026-11-26-public-actions-45762076394-1-part-005.md)，参数逐值保 [首请求](../computations/resume-20261126-deep-valley-input-first-step.json)。

## 实际身份

完整producer `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`；实际新模型 `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d`。实际旧scalar输入 `2ca2f11fdc2e1bad0c38fe35fc52e81ef7cd35644d53f7e7aefc64d820b6b691`；旧FullHold/integer/Hold完整源码分别为 `a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`、`babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0`、`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。

raw报告7856 B、SHA256 `d9c466301672e7e98858ffcf577035e9b11b6826134b34547c5e0a54676a5834`，只留runner。报告中的GITHUB_SHA是workflow初始提交；真正本步源码提交由控制器单独给出如上，二者不混用。

## 实际包围及其范围

新终端R完整有理盒为

```text
[564734175383798202556909871405419982993527884399889816081393673589866581,
 564734175384276192026033775321496111699110362164506431614854811271693793] / 10^72
```

新参考高度增量、与旧高度之差、0–4阶无限尾导数界和解析位移有理界全部已在第5卷逐字返回。参考修改段曲率上界仍为解析 `35211/65536`，完整Hold扩段参考界为 `5/2`；它们只属于旋转参考Hold，不包括更早scalar前缀，不包括待求非圆场的K或reach。

首积分保持准确tail-cutoff `1/8`、128panels、请求宽 `1/1000000000000000000`、admission300秒。真实留下1318个合法积分叶，评估2635叶；标量核自然返回300.1594400590002秒，完整阶段303.85885794599926秒。实际积分宽为

```text
117189455695462483460444874276720736574480900650425726242182059049815587382513
/ 900719925474099200000000000000000000000000000000000000000000000000000000000000000000000
```

`requested_integral_accuracy_reached=false`，但 `all_tail_domain_included=true`、`unresolved_oscillations_dropped=false`。每个尚未细分叶已经有合法全段盒，预算只影响宽度；未把有限分辨率当删无限振荡的定义，也未将未达请求精度写成模型无效或全域未覆盖。后续需要更窄费用时在同一明确模型上继续包围，而非移动公式。

## 继续完整非圆求解

R690只证明新输入避开准单调线性唯一性充分判据并有可执行全域包围。本次 `original_metric_unchanged=false`、`scalar_prefix_unchanged=true`、`old_certificates_inherited=false`、`nonlinear_surface_solved=false`、`new_nonradial_solution_exists=false`。新R/I和固定 `g_n=ds²+a_n(s)²dθ²` 必须真实进入完整原q/core/H变量及全部观察残差。不能在移动均值中将a分母约掉后冒称消费了这个新固定度量；新场自己的连续metric、D/L/K/reach、非平面及固定参数精化继续实际求解。

完整新factory/固定gn求解入口直接接下一科学步骤；本次标量返回不作为研究终点，也不新增必须先通过1e−18的门。
