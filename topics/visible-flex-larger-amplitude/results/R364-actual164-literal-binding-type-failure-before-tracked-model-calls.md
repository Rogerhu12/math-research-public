# R364：actual164 在绑定比较阶段因 Decimal/JSON 类型误拒而退出

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 1. 本次实际结论

[request164 的公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43741113847) 已结束：compute job 为 failure，report job 为 success。实际异常不是六个新形状都没有下降，也不是二十档原 Armijo 全拒，而是 producer 在受跟踪 Decimal primal/forward/second 调用之前，直接比较一个含 Decimal 对象的实时绑定字典和一个从 JSON 读取、用字符串保存相同 Decimal 字面的绑定字典，产生了错误的“不相同”判断。

原错误为：

    ValueError: The actual reconstructed original literal coefficient identity differs

失败位置是本次 producer 的第 197–198 行。实际原九坐标模型的 primal、forward 和 second-forward attempt 计数全部为 0；伴随构造、六候选响应、新十坐标模型求值、二十档真实试探、全部初末 FD、Arb 域消费者和原 453 维圆场终检查均未到达。本次没有接受点、没有新形状选择、没有可续接的新场。

最小修复是让两边使用已经冻结的原 encoded/clean 序列化约定比较完整绑定。它保留所有字段与全部数组身份，不把校验降为单个哈希，也不删除原绑定字段，更不改变任何科学接受门。修复后的实际运行尚未发生，本报告不能作为其结果。

## 2. 真实运行、来源和读回范围

| 项目 | 实际值 |
|---|---|
| run | 43741113847 |
| 触发 source commit | 39e6ff8006f3c792a6672804e1fc1e3049767b86 |
| 创建时间 | 2026-11-15T17:26:27Z |
| compute job | 132894269288，failure |
| report job | 132894506668，success |
| compute 原日志 | 80158 B；SHA256 75be8c8780de1fec921df385eae7f0fef62a8e2dc0feb5a06da60fe8c7ce0f3a |
| report 原日志 | 30174 B；SHA256 fe85ca3caac83cad3fc0fcdba0d4b1e240144c0a419ce3c9590b1ad0c05f1e80 |
| 唯一紧凑科学/失败摘要 | 12736 B；SHA256 eed3e357555f320bcf273fccc8fe90ea15d3cfdb3769d7eb839a51884f61756b |
| 原 status | 67661 B；SHA256 cebba1c3f2e65b4b7e5d6322c300e5f21f7581decaf34d967cd236393e882e61 |
| producer 完整 stderr | 664 B；SHA256 1625b16b12e5fc6f26211312570e5e32f5a59af4be8b8f59cf62d08dd3a4668a |
| producer 完整 stdout | 397 B；SHA256 ca1c019c924b3203762527e2f8a252c1c752a1995692d048db073ef844f115b2 |

两个 job 的 BEGIN_VISIBLE164_COMPACT_SUMMARY 块已按原 JSON 文字提取，移除的只是 Actions 行首时间戳。compute 与 report 的 12736 字节正文逐字相同，均不含日志分隔 LF，均与原打印的 SHA256 相同。原 stderr/stdout 的单块工程错误传输也已无损还原，字节数与 SHA256 均相符。reader stderr 为 0 字节。

本报告只读取已产生的日志、JSON 字段、源文本和字节身份，没有重新构造数值模型，没有求范数、响应、伴随或 FD。原 status 作为临时文件已按工作流清理，本次未重新取得其完整文件；本报告核对的是日志保留的 status 身份和紧凑字段。十个数组的身份是原 Actions 对实际输入字节计算并保存的身份，不冒充本地再次取得数组后独立审核。完整规范化绑定的哈希比较则只涉及短 JSON 元数据。

## 3. 已完成和未到达的步骤

前七个 compute 步骤全部 success，包含 Python/runtime、112 个 source pin 与 10 个 workflow support pin、参数文件及四个原输入身份、原 78 源的临时恢复。实际来源闭包仍为旧 41 个 consumed source，加新 family、model、adjoint、producer，共 45 个。科学步骤 8 failure；步骤 9 原始读回、步骤 10 完整 child 错误回传、步骤 11 自有临时目录清理均 success。

原 producer 已完成旧九坐标 setup、原 699 节点和 112 模尾 Jacobian 的构造器绑定，以及原数组身份记录。随后在进入 fresh-original-nine-at-actual157-parameter-words 的 evaluate/response 上下文之前抛出异常。这一区别很重要：本次已经有实际的输入表及对象构造，却没有本次点的 Decimal 全三残差或响应结果。

| 原记录 | 实际值 |
|---|---|
| phase | exception |
| diagnostic_completed | false |
| accepted_point_count | 0 |
| selected_catalogue_index | null |
| 六候选表 | 空 |
| catalogue_unvisited_indices | 0、1、2、3、4、5 |
| 真实 trial 表 | 空 |
| 未访问的真实 trial indices | 0 至 19，全部未访 |
| initial / final | 均 present=false |
| 初末 binary64 projection | 均 present=false |
| 原九 adjoint comparison | present=false |
| primal_attempts / primal_returns | 0 / 0 |
| forward_attempts / forward_returns / forward_columns | 0 / 0 / 0 |
| second_forward_attempts / axes / returns / symmetric_pairs | 全部 0 |
| 科学事件 ledger | 0 B、0 个事件、空文件 SHA256 |
| 原 FD level / column check | 0 / 0 |
| native_nonlinear_solver_called | false |
| nonzero_field_completed / success | false / false |

空 ledger 的 SHA256 是 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855。

摘要保留了二十行计划表，每一行 visited=false、actual_trial=null、unvisited_reason=exception。这些是明确的未访范围，不是二十次数学拒绝。读回字段 required_available_recorded_fields_complete=true 只表示本次已存在记录所要求的字段完整，不表示任何未到达的科学步骤已完成。

## 4. 类型误拒的源码证据

失败源是 [geometry_20261115_adjoint_selected_ten_control_recipe.py](../computations/geometry_20261115_adjoint_selected_ten_control_recipe.py) 的本次已绑定版本，SHA256 为 9da7ebacbf40ff65733d518169c028a82f9060770c62ab89562b29f87793a782。其逻辑顺序为：

    old_model = old_model_module.LiteralCircleModel(original_model, event_sink)
    status['original_nine_literal_binding'] = old_model.binding
    if old_model.binding != parameters_recipe['expected_original_literal_binding']:
        raise ValueError('The actual reconstructed original literal coefficient identity differs')

原 [2422 Decimal 模型](../computations/geometry_20261115_nine_control_decimal_literal_model.py) 的构造器将 self.gamma、self.eh 作为 Decimal 保存在：

- cut_scale_exact_binary64_lift；
- height_sign_exact_binary64_lift。

原 [ad568 二阶模块](../computations/geometry_20261115_nine_control_decimal_second_variation.py) 继承此构造器，再加入 second_variation 与来源说明，重新计算 canonical_binding_sha256。它并不把这两个运行时 Decimal 改成字符串。本次导入的 ad568 源全文已按公开版本读取，其 11219 字节、SHA256 ad568abc8bf35003375d80e303c44df6dcb2f1c75fd41163cf5c0f423ba321a1 与固定 pin 相符。

另一方面，参数 recipe 是 JSON，保存的值为：

    "cut_scale_exact_binary64_lift":
      "0.99681527853612494904922414207248948514461517333984375"
    "height_sign_exact_binary64_lift": "-1"

原 clean 函数的明确责任是把有限 Decimal 转为其原 str 字面；encoded 对 clean 后的完整对象作 sort_keys=True、ensure_ascii=True、紧凑 JSON 编码。原 digest 同样调用 encoded。因此，运行时 Decimal 与 JSON 字符串应在这一既有序列化边界比较，而不能直接做 Python 字典类型比较。

本次原 binding 的 canonical_binding_sha256 仍是：

    cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3

更强的短元数据证据是：读回为完整原 binding 报告的规范化 JSON 身份为 2984 B、SHA256 ad491da3f70900cabb0ba7beae87ef9fc63a4b2cd28bec8556ee49970ae8034b。对当前固定 recipe 中 expected_original_literal_binding 仅做同样的字段排序及 JSON 文字编码，得到完全相同的 2984 B 与 SHA256。这不需要任何科学算术。紧凑摘要省略的 14 个说明字段不能被误称为实际 binding 缺字段；它们只是 reader 白名单未展开，完整对象身份已经另外保留。

## 5. 实际输入表与父身份

原 Actions 保存的十个数组描述器均与固定父 recipe 的对应描述器逐字段相同，包括 shape、dtype、exact_Decimal_from_float_lift 和 raw_C_order_sha256。没有证据表明本轮重新形成了不同的原九有限表。

| 数组 | shape | 原实际 raw SHA256 |
|---|---|---|
| mesh | 699 | 3b837d4580a1dff2575208ef6fc76bc19021e744eb6b37277040a2fbc9eb350e |
| h | 698 | ee6981d6d293a1d067fd7fb53e4ea4ea93b1a4e7406364a3dc503c83162266e7 |
| mid | 698 | f06f265bd25b0d1d499f94b984caca930f00e357348a8d58372f2875430d263f |
| base | 699×2 | 5a26da19688c7d77b9c20bc3d90f39b4b84038788ed4bc696b724c512ccd96dd |
| base_mid | 698×2 | 0c375941ce46d907c4b8b4532a97a8721f88e582473dce891f41922191173703 |
| controls | 699×2×9 | 6523f85bd59aeb25c1e9f3d791d9ac79ef1408b007731a3c91d060466c265f2a |
| controls_mid | 698×2×9 | 532a6ddb558dab6dce208ebc8e2f79aa52a2ac6c3739a5c7aa727818ba7cc8e6 |
| native_slope_J | 112×112 | 44039f96cb20b0edca76a843a44f40235fbfbf72c19093a12a212c1cf6eb655d |
| target | 3 | 8ca034c42495150b10a778e9cad2a338837e06c275b36490301f0b656c181585 |
| frequency | 3 | 51c16f13beb17c892ed884b329f39d62a6d4318ec7f3d0004f24dcb18872c76f |

这些数组均是原 binary64 字面表再准确提升到 Decimal；它们不是重新高精度生成的连续几何数据，也不是新的非线性 native Jacobian。

本次初始数值来源仍是 actual157：

| 父记录 | 身份 |
|---|---|
| run/source | 43729310294 / c71cbeac7fd13c65cf50c7eb39842e9949737b25 |
| 原 status | 51842612 B / 931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0 |
| 原紧凑 summary | 89063 B / 7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2 |
| 原 chain | 29684 B / 9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd |
| 本次参数 recipe | 7483 B / 76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820 |

本次没有继承父 J、父残差、父 FD 或父状态缓存。父九个 Decimal 字符串仅用作独立重构点的数值输入；父半径 0.0000390625 仅作来源说明。计划的新形状系数初值为 0，新的明确尺度为 0.01，但均尚未产生实际方向或试探。

四个原数学输入仍为：

- accepted：b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff；
- prepared：0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714；
- tail_anchor：e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51；
- tail_config：01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5。

## 6. 退出、预算、规则同步和清理

producer 原 elapsed_wall_seconds 是字符串 0.559115709。wrapper 原 wall_seconds 是 2.021806650000002；child_exit_code=1，reader_exit_code=0。wrapper partial=true 表示计划的实验没有完成，而 producer resource_partial=false、explicit_wall_termination=false、received_signal=null，说明没有到达独立 2400 秒预算，也没有信号或规则变化导致的资源退出。wrapper_exception 和 post_step_reader_exception 均为 null。

本次保留原规则 runner 的 2700 秒真实同步机制。原日志 actual_rules_sync_completed 明确记录 round=0，于 2026-11-15 17:27:12 UTC 读取 origin main 39e6ff8006f3c792a6672804e1fc1e3049767b86，并发布规则记录 commit 2f057b3c1ce9e3264ccf485db145119a9d532e6a。科学源仍绑定触发 checkout 的 39e6ff...，不把该元数据发布当成模型源替换。

实际审核的根 README blob 为 21bd547f56590b7f2dd279d0297efb289a9b2783，题 README blob 为 bff8aea253a9e6a7a4fac28d810ac454c5499fec。没有 RulesChanged 退出。

完整失败正文和紧凑结果先输出，随后原 owned cleanup 删除三处自有临时目录：

- visible-adjoint-selected-ten-control/adjoint-selected-ten-control-temporary；
- visible-adjoint-selected-ten-control/original-inputs；
- adjoint-selected-ten-control-original-source。

原日志明确 raw_artifact_or_Release_upload=false。清理成功不能反过来证明读回或科学成功，本报告按各自原记录分别陈述。

## 7. 保持全部原科学门的最小修复

应只把实时绑定比较改为：

    if k.encoded(old_model.binding) != k.encoded(
            parameters_recipe['expected_original_literal_binding']):
        raise ValueError('The actual reconstructed original literal coefficient identity differs')

这个改动使用已冻结、已经用于模型身份与所有原 status 输出的精确字面序列化，不重新舍入 Decimal，不转换为 binary64，不删除比较字段，不替换为容差比较。recipe 及数学输入保持原字节。应随后只更新实际 producer SHA、严格 reader/wrapper 中相应 pin、request/workflow 的真实引用与明确的工程重试元数据。

六个宽形状的公式和支撑、真正十坐标有限族、实际新十列 forward 定符号、完整三残差及原二十档 Armijo、Decimal50、初末全部 FD、Arb160/depth14、完整 112 末端和 453 圆场责任均不改变。系数仍是实际157的数值输入；不能把本次空结果当作新父。

任何重新派发均是新的实际运行，须由新日志证明其到了哪些步骤。本次错误既不支持“六形状无法下降”，也不证明新的局部站形状一定有效；[R363](R363-local-C2-shapes-and-complete-finite-sample-response-rank.md)、[R366](R366-coincident-inputs-complete-value-and-slope-shape-response.md) 的条件响应结论与后续173/174设计仍须独立保持准确有限表达、实际形成权、真实原门和连续模型的边界。
