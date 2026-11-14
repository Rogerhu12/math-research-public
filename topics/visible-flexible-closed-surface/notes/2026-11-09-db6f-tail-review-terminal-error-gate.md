# 最终误差后验门：全文独审与真实 M12 负例重放

审稿人：`/root/tail_theory`，2026-11-09。

**结论：在“输入是已经独立验证的完整连续证书”这一明定前提下，后验门的完整数学、来源连接和两个 CLI 分支的静态审查 PASS；真实已冻结 M12 负例的独立执行也 PASS。没有运行未来候选分支，没有产生新的曲面证书或完成声明。**

审查对象如下，均未修改。

| 对象 | SHA256 |
|---|---|
| `scripts/db6f-audit-terminal-error-gate.py` | `1be7add52ec2c06653a2a64baa8653e675559a55551cf22603d14a80f9cfb234` |
| `notes/2026-11-09-db6f-audit-terminal-error-gate-method.md` | `06dc6928cd0581ec7e0ccde947ab9de2dc9adff351d3598cd31703fad8b7fb5a` |
| 作者真实 M12 负例与本次独立重放输出 | `3f75f6668aaf0c90dbca169e353a6eb9d8df38de8e01b24acf0bafcd7daaa213` |

我未参与这个后验检查器的实现。对我曾参与的上游 tail supplier、transfer producer 等组件，本审只核来源和使用条件，不以本次审稿替代它们已有的独立审查；也不把本人作为最终候选的未参与优化者。

## 1. 精确阈值与实际改善命题

记旧 R21 指定 M12 图和新图的真实全域、全相位误差分别为 $E_{12}$、$E_{\rm new}$。前提是已经认证

$$
E_{12}\ge L,
\qquad 0\le E_{\rm new}\le U,
$$

其中被冻结的实际点证书给出

$$
L=\frac{370012576184137}{18889465931478580854784}.
$$

后验门直接固定

$$
B=\frac1{500000000},
\qquad F=\frac{195883}{20000}.
$$

我未调用作者的 `scalar_gate`，另用 `Fraction` 精确重算得到

$$
L-FB=
\frac{61863470598928509}
{23058430092136939520000000000000}>0.
$$

所以只要 $U\le B$，就有

$$
E_{12}\ge L>FB\ge FU\ge F E_{\rm new}.
$$

这给出严格的实际改善因子 $F=9.79415$，不是两个上界之比，也不是把某个采样值当作全域误差。论证没有除以 $E_{\rm new}$ 或 $U$，故 $E_{\rm new}=0$ 的情形也被包含。代码另保存并核 $L-FU>0$，与上述充分推论相容。

阈值是精确有理数 $B$，没有可放宽它的 CLI 选项。`binary` 拒绝布尔值，仅把原整数或 binary64 数按其真实数值转成 Fraction；已保存的 exact 字段另按 Fraction 读取。这里没有把打印的十进近似替代证书端点。

## 2. 旧 M12 见证的实际身份

`reference` 指定了旧 common-cut geometry、critical-r01 manifest、whole、exact bridge、target、point 方法及独审的哈希。点证书采用 `inputs.geometry/manifest/whole` 格式，代码按实际 M12 schema 连接，未套用旧 M8 的顶层格式。

逐项核查：

- point、geometry、whole 都对应指定的 M12 actual manifest；point packet 与 whole 所用的 separate metric packet 相同。
- point 的 six-background mapping 与 packet 相同，各定义文件按固定 SHA 重读；其不是一份可随候选改变的数值背景。
- point 所选 `relative_operator_lower` 的精确 binary Fraction、保存的 exact 字符串与上面的固定 $L$ 三者相同。
- 真实 manifest 的全部分片、字节数、共享行计数和 input checkpoint 被重新哈希；几何数据不经过对话内容。
- 点公式的源、方法及独审身份被绑定。本门没有重搜点，也不冒充重新认证该点不等式。

真实增量表示把每跨的未归一化径向增量保存在对应系数分片的最后一列；`radialGeometry` 的精确锚与缩放信息在 manifest 内。因而本例不存在一个未被 manifest/分片哈希覆盖的额外径向 sidecar。R6 collar 也按已审 reader 从实际首行定义，不另借一份不同系数的圆领。

## 3. 新图、固定目标与背景的连接

`candidate` 只接受已审的新 closed-budget-transfer-v3 和 whole-v2 实现。预算的七项输入集合必须完全等于 geometry、geometry certificate、metric certificate、moment certificate、tail-first、height、positive-alpha；未知集合不能悄悄改变依赖。

前缀固定定义的 `frozen_profile`、完整 chart、warp-reference、ell 及 profile loader/implementation 均与 M12 对照。新 common-cut 的 base、checkpoint、port、数据、镜像、共同 cut、tail reader 也按实际身份连接。前缀 geometry、metric、moment 的 geometry SHA 必须是最终 common-cut 图的 SHA，而不是未修正 base 或旧 M12 的 SHA。

精确桥绑定新 base/target，cut 半径和斜率从实际 manifest 中的 binary 参数转 Fraction，并核

$$
w_r=-\frac{7w}{r}.
$$

完整 exact bridge 的根盒、正导数、唯一性、pt/ps/L、重新参数化及相位字段与固定参照相同。若桥使用较早的数值支持 manifest，必须显式给其文件，按桥 SHA 读取真实支持 manifest 和 checkpoint，再核支持网格、实际网格、M12 三者的物理参数。这里使用较早网格只识别同一背景/cut，实际新图的 metric 和曲率仍由实际新 manifest 支付。

`parameters` 的键存在性与 canonical JSON 比较保留类型；未知新增 null、False 与 0、True 与 1 以及嵌套类型改变不会被 Python 的宽松相等掩盖。只有原数值白名单和明确的四个 I/O/分配键允许差异；四键自身有类型检查。

`transfer` 要求正式 `finite-background-grid-transfer`、`finished=True`、实际新 manifest 绑定，显式 pin v3 producer、旧 base 和 policy 的真正身份。参数预检不能作为正式转包。六项定义固定为 checkpoint/calibrations/alpha/cell-zero-A/inner-A/outer-B，并重新核 tight-alpha 的 A/B 依赖、height/positive-alpha 与共同 bookkeeping 的连接。固定帽的目标由同一 R16 定义与 cuff 支付，竖直平移不改变其诱导度量。

这些检查足以防止本门在汇总时有意许可更改目标 $g$。它们仍依赖上游已经证明的“这些源和参数确实定义所宣称的目标”这一数学事实，不是仅凭任意 JSON 自证来源正确。

## 4. 新图必须拥有自己的完整界

### 4.1 前缀转移只做一次

前缀 polynomial 或 angular 报告的兼容 `metric_operator_upper` 是相对 source target 的 $\epsilon$；精确桥给 $\eta$。代码从二者的实际 binary 数另算

$$
U_p=\epsilon(1+\eta)+\eta.
$$

它与 closed-budget、whole 的 exact 字段核同值。angular 报告已有的两个 exact-target 字段仅用于比对上式，未被再当作 source $\epsilon$，因此没有二次转移。angular 的 source float 与 source exact 也要相等。

原后端要求显式 target 路径；angular 按 `inputs.target` 读取。两条路径都核 target/base/bridge、固定 profile、bridge constants、extension guard、源、算术后端及目标 data SHA。angular 必须是全域运行：`requested_intervals=None`、finished、processed=target intervals、exact partition reread 及完整 baseline 等条件同时成立。局部 fixture 没有这些条件，不能用作完整上界。

### 4.2 实际尾、圆领与曲率

完整 tail certificate 和可选 metric-only certificate 都必须指向新实际 manifest，同一个 packet finite manifest、六背景定义和实际 data/rows。完整计数应覆盖 collar 索引 $-1$ 和全部有限跨 $[0,n)$，即 saved range 为 $[-1,n]$，末端是排他界。

full 报告的曲率必须全部 resolved，且使用的背景上界不得小于已证明的 $6$。允许的 streaming adapter 只改变读取方式，身份和原后端也被 pin。metric-only 明确不计算/认证曲率；它只提供同一实际图的另一个合法 metric 上界。

故可取

$$
U_t=\min(U_{t,\rm full},U_{t,\rm metric}),
\qquad U=\max(U_p,U_t,0),
$$

其中没有额外 metric-only 时忽略第二项。曲率则始终取这个新图自己的前缀和 full-tail 证书，与固定帽 $10/3$ 取 max。代码重新核该 max、support、diameter、R10 的 $\min(\sigma,1/K)$ 以及 reach/D 的精确有理组合，不将旧 M12 曲率接到新 exporter 网格。

### 4.3 检查范围的关键限制

本门重新哈希 row/packet/manifest 数据，并核完整声明、计数、范围和身份，**没有自己解码全部 NPZ 或逐行重新证明分区覆盖/全局最大值**。因此“输入已独立验证且完整”是实质证明前提。方法 §4.2、源码说明、正常输出 scope 及 `independent_complete_input_certificates_remain_proof_dependencies=True` 均明确保留它。

这与作者声称的能力一致，不是一个尚未披露的验证步骤。未来实际候选仍须运行自己的连续后端与最终独立完整流程；本门不把 source SHA、布尔声明或一个可编辑报告本身当作后台运行证明。

## 5. 实际执行与独立算术复核

本次独立执行过且观察到 exit 0 的唯一 gate 命令是：

```bash
python -B topics/visible-flexible-closed-surface/scripts/db6f-audit-terminal-error-gate.py \
  --check-m12-negative \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-terminal-error-m12-negative.json
```

输出与作者 18,371 字节报告逐字节相同，状态 `EXPECTED_REJECTION`，48 个真实文件。独立复核器 `scripts/db6f-tail-audit-terminal-error-check.py` 不导入 gate，而是另用固定有理常数重建全部 scalar 字段、源码 import AST、两输出字节相等和 48 个实际文件 SHA/大小；它也已实际 exit 0，输出在同日期 `tail-audit-terminal-error-check.json`。

旧 M12 完整上界为

$$
U_{12}=\frac{38493756262750339563330485335957988971213899}
{1496577676626844588240573268701473812127674924007424}>B.
$$

更强地，实际旧图满足 $E_{12}\ge L>B$。所以负例确实对应不可能达到新阈值的真实图，不是人为制造的无效输入。两数值门均应拒绝；测试退出 0 表示正确观察到这种预期拒绝，不表示图通过终门。

我没有运行 `candidate` 分支、创建正例、修改 active worker、重新执行 root/flow/DN/metric/曲率，也没有重新生成 packet 或 manifest。正常分支的代码审查不能冒充未来成功运行。`coupled_prefix` 的互补正常入口定向审稿已另外完成，含真实 M12 metadata 的十项 Fraction/schema 对照；本稿没有把那十项检查记作本人运行。

## 6. 放行范围

正常门在所有输入身份/证明前提和精确数值门均成立时，只可宣称

$$
E_{\rm new}\le2\times10^{-9},
\qquad E_{12}>9.79415E_{\rm new}.
$$

单个终值与一次实际下降不单独证明加密序列趋于求解容差，也不证明无限非线性图的严格存在。正常和负向输出均保留 G5、最终独立全流程、无限存在和 README 完成的 false 标记。这与当前研究尚未完成的状态一致。

**完整审查与真实负例：PASS；未来正常候选实跑：未执行；新几何证书：未产生。**
