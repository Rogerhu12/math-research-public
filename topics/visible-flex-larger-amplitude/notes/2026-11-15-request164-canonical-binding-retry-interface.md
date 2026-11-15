# Request164 r2：完整 Decimal/JSON 绑定序列化比较的最小工程修复

作者：OpenAI ChatGPT（amplitude 协作代理）。日期：2026-11-15。

## 实际动因与范围

[原 actual164 结论](../results/R364-actual164-literal-binding-type-failure-before-tracked-model-calls.md)记录了 run43741113847/source39e6ff8006f3c792a6672804e1fc1e3049767b86 的真实失败。setup、原699节点/112尾对象和输入表已构造；受跟踪 Decimal primal/forward/second 计数全0，伴随、六候选及二十真实 trial 尚未开始。

失败代码把 live binding 字典与 JSON recipe 字典直接比较。前者 cut_scale_exact_binary64_lift、height_sign_exact_binary64_lift 是 Decimal；后者是原 str 字面。现有冻结2422模型已经通过 clean 将有限 Decimal 无损转换为字符串，再由 encoded 作完整排序 JSON。二者的原规范化 binding 身份实际均为2984B/ad491da3f70900cabb0ba7beae87ef9fc63a4b2cd28bec8556ee49970ae8034b，canonical_binding_sha256 均为cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3。

本修订只解决这一类型边界。不更换父点、不改变有限模型，不从失败164提取新accepted状态；真正数值输入仍是原actual157九个Decimal50字符串。

## 唯一 producer 代码差异

~~~diff
-            if old_model.binding!=parameters_recipe['expected_original_literal_binding']:
+            if k.encoded(old_model.binding)!=k.encoded(parameters_recipe['expected_original_literal_binding']):
~~~

异常正文不变。这里比较的是两份完整序列化字节，不是单个摘要字段，也不做容差比较。现有 encoded/clean 实现、schema、arrays描述器、cut/height字面、祖先来源、完整原112固定Jacobian身份和所有其他元数据均参与比较。没有将Decimal折回binary64。

除这一行外，producer 的全部正文逐字不变。family09240b33、ten model8cb8352b、R351 adjoint12a95d40与原41个祖先源均保持。没有新增fixture、科学验收门或比较阈值。

## 必要的引用传播

reader 仅把 PRODUCER_SHA 换成新producer SHA；wrapper 仅把 SCIENCE_SHA、READER_SHA 换成相应新值。其完整读回、45源闭包、预算、同进程组、错误转发和清理流程均无其他代码改动。

request 保留原schema和request_number164，增加 engineering_revision=2、首跑实际tuple/摘要身份、修复说明，以及 failed_run_is_not_a_new_parent=true。原112 source pins仅更新producer/wrapper两项；原10 support pins仅更新当前reader一项；current_consumed45中producer pin同步。所有其他原request字段逐字JSON值保持，包括配方、原输入、数学策略、预算、运行时、README绑定和输出责任。

workflow 只更新这三个pin及可见名称中的r2说明。触发路径仍是原唯一 computations/public-adjoint-selected-ten-control-request.json 的push。没有预填未来run/source、科学结果或接受参数。更新此请求产生的运行是新的实际运行，必须单独按原日志核收。

原recipe完全不变：7483B / 76a93aa076d0a55781fdb3228a895b25583591b269fa5a866ea8068392946820。原科学合同也不变：6个显式宽形状、实际新10列forward重新定符号、新系数尺度0.01、原全三merit、准确提升的binary64 c_A、20真实回溯、初末120项FD、Arb160/depth14、原453圆及完整112末端责任。没有把它们预称已执行。

## 完整交付身份

除工作流外，路径相对topics/visible-flex-larger-amplitude。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| computations/geometry_20261115_adjoint_selected_ten_control_recipe.py | 35491 | 1998fa8062ca91d798fe13ef60e2dc4ee08e5709c871d88346e81692852cad2b | 0694e7928b944e083a34ebb3b91561eaf36b76ad |
| computations/root_20261115_adjoint_selected_ten_control_scalar_readout.py | 28130 | 54d38cc81927e0aae686613ab8384b1591402c71fd3488f4b66e4844e1f1562e | 056e6054e1f62316c63ee38b4b038766c27b1f90 |
| computations/geometry_20261115_adjoint_selected_ten_control_temporary.py | 19031 | d9b969a948e7afb661d4f1d9aa81371000692f234de5da7beef91670b4a8d289 | bbefc90cf0a9cd315c716827829f30042e5542af |
| computations/public-adjoint-selected-ten-control-request.json | 41858 | 089b73a13e86293b02410f06b9815bc283e842f2d794aeeda4ea7f033645920d | 9828f25d874295019297f95e80bb1b94945d8ad5 |
| .github/workflows/visible-larger-public-adjoint-selected-ten-control.yml | 20759 | cd4150ef19744324c08442fe5d5fbd619718207059b9dc0b394df245f9e4cfe1 | 6427365ca9d140e777be95ef641391ac1e88e68f |

完整五件差异为9273B / e522cdf1d05e9af2cb701a272648f30ebda552cd63197c4bdb8757797ec7639f，blob4295f5c6efe0270827bc31243ea25bafaea36509。差异基线为已发表首跑164八件，而非旧157原型。原request164接口保留为首跑历史说明，本页覆盖本次工程修订的身份与原因。

当前只做源文本替换、JSON字段核对、完整差异与SHA操作；未在本地导入或执行任何科学模块，也未声称本地AST运行。原workflow在Actions中的AST与源pin检查继续保留。所有新对象均为小源码/参数/接口文本，没有写ref、没有派发；所有raw仍只在实际Actions临时目录，先原摘要与完整错误后owned cleanup，不上传artifact/Release或原数据。

这不是已成功的科学重试。若后续出现新的工程异常、真实域拒绝、无负方向、全部回溯拒绝、预算partial或真实接受，应分别按新原件记录，不能用本修复说明替代实际结果。
