# 原 collocation 最大项的只读位置观察器

**分类：实现接口与源码事实；本文件不报告新的数值运行。**  
**作者：ChatGPT（amplitude）。**  
**日期：2026-11-14。**

## 1. 要补的具体记录

此前暖场报告保存了完整物理 collocation 最大绝对值，却没有保存其区间和分量。不能仅凭约 `.00711` 的数值猜测是末桥、高频、某个均值，或把所选域查询的位置当作这个最大值的位置。新的薄包装只记录原调用已经返回的数组。原十五查询、完整 R270、QP 预算、固定模型权重、全部真实试步、原域和 FD 判据均由原入口执行。

新源：

`computations/geometry_20261114_fifteen_query_collocation_observer_warm.py`

- 字节数：16716。
- SHA256：`3e9124137fa5ff8fb81bee17bfdce9dfffca6d2e61f90f223adf7e61f34b5d23`。
- 观察器 schema：`original-return-collocation-location-observer-v1`。
- 数学 producer schema 仍为 `exact-constraint-fifteen-query-condensed-complete-H-warm-v1`。

原十五入口、原 residual、原优化引擎文件分别保持：

| 原文件 | SHA256 |
|---|---|
| `geometry_20261114_fifteen_query_condensed_warm.py` | `f1310edc94fb3a9c9f95b5dad98e7073c1879997b9a9bdf06c5028e91f83351e` |
| `geometry_20261114_constrained_collocation.py` | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| `geometry_20261114_full_angle_projection_warm.py` | `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152` |

## 2. 原数组、行序和分量

原 `CompleteResidual.evaluate` 一次返回：

- `collocation`：所有区间 × 全部增广分量；当前尺寸为 $698\times453$。
- `vector`：先按区间优先、C-order 排列全部 $698\times338$ 物理 col，再接112个原右边界残差。
- 原 `y`、`f`、`middle`、`fm` 及原 `finite`、`report`。

物理残差是原函数已生成的数组

$$
C_{jk}=Y_{j+1,k}-Y_{j,k}
 -\frac{h_j}{6}(f_{j,k}+f_{j+1,k}+4f_{m,j,k}).
$$

观察器不重新计算这个表达式。它对返回的 `collocation[:, :flow.n]` 定位绝对值最大的元素，保存已有带符号值，以及原 `vector[j*n+k]` 的已有值。范围覆盖全部区间和全部物理分量，不限于十五个域查询、局部凝聚支持或最后几个节点。相同最大值采用原 C-order 中第一次出现的位置。

当 $M=112$、$n=338$ 时，原物理状态索引为：

| 索引 $k$ | 分量 | 基函数 / 角频率 |
|---|---|---|
| 0 | $r_0$ | 常数 |
| $1\ldots112$ | $r_k$ | $\cos(2k\phi)$ |
| $113\ldots224$ | $t_{k-112}$ | $\sin(2(k-112)\phi)$ |
| 225 | $z_0$ | 常数 |
| $226\ldots337$ | $z_{k-225}$ | $\cos(2(k-225)\phi)$ |

每个完整物理 argmax 保存 `interval`、两节点号、原 `x[j]` / `x[j+1]` / `h[j]` / `mid[j]`、分量族与模号、完整 residual 行号、原 signed/absolute value、以及原同分量 `yL/yR/fL/fR/fm/middle`。这些全是读取现成数组，不调用 scalar profile 或几何求值。

另保存整个原 `vector` 的最大项，并区分 `physical-collocation` 与 `original-right-boundary`。后者记录原右行序及原 separated boundary 行序，不能误标为某个物理区间。

## 3. 必须读取同一个模型的原权重

原引擎在基点 `evaluate` 之后只调用一次 `weights(state)`，得到

$$
(W_r)_{jk}=\frac{1}{h_j(1+|f^{\rm base}_{m,jk}|)},
\qquad (W_r)_{\rm right}=10^5.
$$

这一份 $W_r$ 在模型和每个实际试步中保持固定。新类的 `weights` 覆盖方法仍只调用一次 `super().weights(state)`，返回原来同一个对象；观察器仅保存其只读副本和字节身份、基点原 `fm` 的只读副本。绝不按试步的 `fm` 重算权重。

首次基点 `evaluate` 时原权重尚未生成，报告明确 `available=false`。原权重返回后，用同一份已返回基点 state 补齐报告并重写该 evaluate 的小报告，不再调用 `evaluate`。之后每个 trial 或原方向检查调用，直接从这份模型权重读取 `W[j*n+k]`，并记录权重调用编号、基点 evaluate 编号及原权重数组 SHA。这里只读取权重值，不增加加权 residual 或模型 action。

这区分了原未加权 col 最大值、原加权 merit 和正阻尼模型。观察器没有把任何一个最大值换成新的接受判据。

## 4. 接线与不干预范围

薄包装临时把 `entry.observed.OriginalCompleteResidual` 替换为只读子类；原十五入口内部的 `ObservedResidual` 正继承该对象。因此原中点观察器也仍执行。新类：

1. 每次原要求的 `evaluate`，先原样调用一次 `super().evaluate(...)`。
2. 在原返回之后读取数组并追加只读报告。
3. 每次原要求的 `weights`，先原样调用一次原方法，再保存观察副本，返回原 $W_r$ 对象。
4. `finally` 恢复临时替换的原运行时对象。

没有额外 RHS、Jacobian、profile、boundary、$A/A^T/B/B^T$、线性化或真实 trial 调用。没有改变坐标、系数、均值、$c/p$、query 集合、节点、模式、目标函数、容差、方向或接受结果。原函数自身的异常照常传播；仅观察和观察输出的异常记作 `observer_exception` / `collocation_weight_observer_error`，继续返回原 solver state 或原 weights。最终观察 summary 的写入错误也不能覆盖原入口的退出结果。

若任何物理 col 元素非有限，明确 `complete_physical_maximum_defined=false`，完整 argmax 为 null；不拿有限子集的最大值冒充完整最大值。完整 `vector` 也单独做同样区分。原 returned `finite` 及完整 col/vector 的字节身份在观察前后核对，核对结果仅诊断，不新增科学门。

## 5. 产物与来源身份

额外产物位于原 `--out` 下：

- `collocation-observer/evaluate-NNNN.json`：每次原 evaluate 的完整范围 argmax 和已有分量；基点同编号在原 weights 返回后补齐。
- `collocation-observer/run-summary.json`：原 evaluate/weights 调用次数、观察异常数、权重字节身份及恢复运行时对象说明。
- 原 `model-000.json` / `driver-status.json` 的 state reports 中也含 `read_only_collocation_location_observer`，便于把原 trial 与小报告对应。

原 mathematical `source_sha256` 字典和源名集合不变，以保持原十五 own-schema 父验证的确切规则。当前 intent/status identity/warm producer 均额外保存 `read_only_collocation_observer_entry` 与 `read_only_observer_source_sha256`，显式给出新包装文件和 SHA；顶层还区分 `execution_wrapper_source_sha256` 和 `mathematical_producer_source_sha256`。不把执行包装冒充原十五数值源，不递归改写 `resume_producer` 或以前的观察身份。

同十五 schema 的真实 warm/status pair 仍由原入口完整验证。原十五 response 入口能读取这个相同 schema，重做原完整 FD，并把实际新 warm 的完整 producer（包括观察元数据）保存到 response。其原数学 source 验证不增加或删除源名；观察器本身由后继 workflow 的 source pin 和这份独立 ledger 绑定，不能宣称旧 response 单独检查了一个未加入其数学 source 集合的观察器。

## 6. 最小 CLI 与当前验证范围

后继 Actions 只把原 warm 命令的程序名换为：

```text
python geometry_20261114_fifteen_query_collocation_observer_warm.py \
  <全部原 fifteen_query_condensed_warm 参数原样保留>
```

包含真实 `--resume` / `--expected-resume-sha`、解压恢复原 JSON 字节后的 `--parent-status` / `--expected-parent-status-sha`。原 `--condensed-max-working` 等优化参数由原入口解释，观察器不修改。FD 仍用冻结的 `geometry_20261114_fifteen_query_condensed_response.py` 对实际新 warm 做原检查。

本次仅完成 AST、三个冻结源 SHA、两覆盖方法各恰好一个原 super 调用及输出/父身份链的源码核对。没有本地导入科学模块、没有数值 fixture、没有新增科学计算或虚构 argmax。首次实际最大项位置仍须由公开仓库自己的 Actions 产物给出。
