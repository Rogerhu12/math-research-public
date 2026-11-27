# v12 真终态与原完整返回函数的捕获绑定

日期：2026-11-27 UTC。会话：Astra-rank2-Sha-0b097461-20261127。主目标仍未完成。

## 1. 消费实际终态

唯一原完整 v12 的公开执行为 [run 46033409751](https://github.com/Rogerhu12/math-research-public/actions/runs/46033409751)，job 140622660136，source 048e20343a5f7ec65db9089d824d0635d6815b2b。源脚本仍为 produce-original-complete-quadratic-shadow.py，原参数、两个 char0 pins、全60来源、全部几何接受门均照[完整二次域返回](2026-11-27-complete-quadratic-polynomial-returns.md)。

本次先确认 job completed/failure，再直接读取 GitHub 返回的完整 job 日志。实际 UTF-8 内容 5694056B、12522行，SHA256：

80552d07f846435ca65e372cba161a4c0240e820abec053c3589d969239ce907

22:15:38.202 UTC 的 host 回执明确写 pipeline incomplete、没有数学 PASS；随后 InterruptedError 指向 signal 15，Actions 退出码124。执行开始16:25:38，所设21000秒门限实际终止了本次执行。这是时限终止，不是已执行的数学断言失败；未执行到的门也不能据此前缀命名为通过。

这份最终内容取代此前只返回到19:05的缓存前段作为本轮执行状态证据。完整日志不写入仓库，不再次运行只读 collector 重复取同一已取得内容。

## 2. 已返回与未返回的界限

完整两端地图身份已于17:48返回。最终日志有30个原 degree-bounded module start 和30个对应 native row result；每个实际采用了原完整 prime-subfield descent。因此不能把本轮瓶颈未经核查地归于一个尚未被采用的“真正二次域 HNF 算法”。

随后共有六条完整 cusps primary 回执，各自处理完整长度612的商；其全重数和不可约厚分量均由原完整程序返回。最后一条于22:10返回。这里只记录其完成边界和日志身份，不把这些可重算的矩阵或局部因子列表另存为结果文件。

下一原 cubic-branching positive base-prime 的306维完整块于22:11返回，306条 Frobenius 基行于22:13完成；22:15:28出现第一实际 maximal-ideal 的完整返回。最后进度是原 direct pair batches 的96批，随后被门限中止。

四交、Norm 和最终 $18\times9$ 的原接受门仍没有终回执。有限特征的这条原影子即使将来完整通过，也仍须接本课题真正的无穷不同 $p$ 条件，不能用它代替通常全 $\Sha$ 的主完成标准。

## 3. 静态定位的实际绑定遗漏

以下是源代码控制流的核查，不是一次新增数学运行：

1. original_native_pair_reset.prepare_backend 从原 reference 模块复制 globals，再对独立 namespace 执行生成函数源码；生成的 PREPARED 持有这个独立字典。
2. v12 先调用 entry.prepare_source_bindings，已经完成上述 native preparation。
3. 此后 original_complete_quadratic_returns.bind_original_returns 才修改已加载模块里的 _hermite_remainder_rows 属性。
4. 修改模块属性不修改此前复制的 PREPARED.__globals__。其中这个别名仍指旧的完整 Sage remainder，因而 native 规约末尾的全部原生成行回验没有采用本轮已核的完整 quadratic wrapper。

该遗漏不取消已经执行的完整回验，不把错误输出改成正确输出；它使预定的完整返回实现未进入被调用的生成函数。完整二次域 wrapper 的既有软件 PASS 并未独自验证这一次实际 prepare-then-bind 顺序，故必须增加针对这一顺序的检验。

## 4. 最小后继的接受条件

后继只允许在原准备和原 module binding 均完成后，对 PREPARED.__globals__ 的这一明确别名作受检绑定。必须断言：

- 原生成函数对象、code object 以及其余全部 globals 身份不变；
- 原全部行操作、degree 门、attached 变换和常数因子都保留；
- 原素子域返回及恢复到调用者完整二次域后的返回都仍实际执行；
- 不适用素子域下降时，原完整 reference fallback 保留；
- 所有源 pins、输入和最终数学接受条件仍照原协议。

独立软件检查应先准确重现旧顺序下的未绑定别名，再验证最小修正；对显式小例比较整份原操作流、每个输出及全部完整返回。它不运行原几何，也不声称原四交/Norm/$18\times9$ 通过。root 静态复核初稿时发现一处多余右括号，已退回修正；未把存在语法错误的稿触发为生产运行。

本条登记时，新检查尚未返回 PASS，生产后继尚未启动。是否足以使整条原计算落入时限仍需实际证据；不得把这一确定的软件遗漏直接等同于全部性能问题。


## 5. 已提交的独立软件核验范围

修正后的 helper 与 checker 已完成逐字静态复核。固定 request selector 在任何 Sage 数学 import 前先核对两个指定路径和 SHA256，并在公开作业里执行 AST 解析；只允许这个确定的检查，不接受任意脚本路径。旧 API 请求的原主体逐字保留，当前新请求只运行三个明确的小软件夹具。

checker 先重现 v12 的 prepare-then-bind 顺序和捕获别名遗漏，再验证一次绑定及幂等性；两个 prime-descent 夹具应实际观测完整返回的常数域次数依次为1、2，真正二次域左块则保持原完整 fallback。包括矩形全部生成行、零行、全部 attached 列和原常数恢复。与原 reference 的每一个回执字段比较时只排除 label 和 elapsed_seconds；此外以原 Sage remainder 对所有输入行独立回验。

修复范围也已明确：PREPARED 内只有两个该 remainder 调用。已见30个原 HNF 都下降到素子域，第一次完整返回仍走原 prime-field 路径，第二次恢复原二次域后的全行返回才切换到已核 quadratic wrapper。v12 的外部 primary/projector/direct-pair 模块别名本来已绑定，这次修改不会额外改变那些调用。

源码 SHA256：

- original_native_complete_return_binding.py：23f862035b668478bfafebdf95cf4d7f600d251243c3e47791fd4fec47c2c5bd。
- check-original-native-return-binding.py：e706e6ff3ee7033907c3f2a817592fc0ccbac35f3f8037b14a528890a0d5a146。
- 既有 API entry 加固定 selector：f93c54d4e7ebad92fb7465fbb435f56ed6b5eabb8b6492aad1f0f0c43272a438。
- 固定软件 request：05e6c1078577d50ee91be3be53833b1a832090c978caf809f189fa619fba736b。

本节提交触发原公开软件 workflow，尚待实际回执；原生产 request、producer、launcher 和几何输入未修改。没有据静态核查宣称软件 PASS 或性能达标。
