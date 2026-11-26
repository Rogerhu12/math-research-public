# 原 M12 固定 g 全前缀的恢复版公共执行入口

**可信度：完整数值方案与已执行的语法/接口核验；新求解结果尚未返回。** 该入口消耗原 M12 固定度量、准确中央曲线及准确积分尾端点，对共同切口之前的全部位置自由度联动。r=.6只是内部尾接口；[R223](../results/R223-m12-common-chart-through-flat-cuff.md)另已支付延伸到真正平领的共同图，完整尾的装入与求解仍继续。

恢复版保留全部158个实际单元（80个均匀分点与原接口合并）、J径向基和完整M32角基，总15386未知量；G6/N384训练、完整J/JT、带状H1右预条件和800次LSMR上限，不删物理行列。一次Newton之后另做G8/N768的同一位置场观察。中央和当前common-cut完整二jet固定，所有内部prefix接口自由。源码重构后拥有新身份，失联前exit137的尝试不算此版本成功。

已公开的24块尾端点读取器逐块核Git SHA1/SHA256、准确Fraction积分，原prefix由已知历史blob26ce0426c60ef868c53597a82252e0559c1cc21e恢复并核3,112,330字节/SHA256。raw仅在RUNNER_TEMP；只发布run编号、源/输出哈希和标量观察，无artifact或Release。workflow和topic内小request的窄push触发实际运行，55分钟上限；读取的触发source commit在计算中保持不变。每个literal pull核两README，具体SHA进自己唯一H marker；NFF立即pull --rebase再推，无强推。规则变化打印差异并标明待根会话读取。GitHub认证只经进程环境，不存凭据文件。

新数值任务尚未启动时不能把预计15386列、一次Newton或G8观察写成实际结果。当前已实际完成的核验为Python AST、YAML、各shell段bash -n、所有Python heredoc语法。此前流式算子的真实小方向/伴随对照证明它能复现完整J/JT；新全尺寸求解仍以实际OS返回为准。

源码和精确请求：

- `topics/visible-flexible-closed-surface/scripts/6a65-streaming-cartesian-full-gram.py`：SHA256 `0c1b791f7c8526b366759ac86e52dd9339f8817e081b86f992ade75b6d22323c`。
- `topics/visible-flexible-closed-surface/scripts/6a65-m12-global-common-cut-position-recovered.py`：SHA256 `ddca0e263e7ff8e28b959b18da2439de6245d05914b6612efe9840bd661c7edd`。
- `.github/workflows/6a65-m12-fixed-g-joint-prefix.yml`：SHA256 `2f1062607a84dc252ce6b129820f00a6bcdd607948664db354bd8758e26461f0`。
- `topics/visible-flexible-closed-surface/ci-requests/6a65-m12-fixed-g-joint-prefix.json`：SHA256 `622dc339980476c5ba0f9b83da2fbb72e9c535b804143c143931053920dd006b`。

运行后以独立的 `notes/2026-11-26-6a65-m12-global-prefix-ci-RUN-ATTEMPT.json` 核实际来源、退出前job状态、独立峰值及输出SHA；不能用workflow已触发替代数学成功。可复算的大系数文件不发布。

## 首次 GitHub 启动校验失败与改正

run [45796927002](https://github.com/Rogerhu12/math-research-public/actions/runs/45796927002) 对 source `4fdea93b441d027776fafb127fe1fbb5c3c09568` 立即返回 failure，实际 jobs 列表为空；没有BVP、端点恢复或数学结果。YAML/Python/bash语法通过不等于GitHub表达式上下文通过。该版本在job级env引用runner.temp；现改为首个shell step用实际RUNNER_TEMP/GITHUB_RUN_ID/GITHUB_RUN_ATTEMPT建立非秘密路径，并写GITHUB_ENV供后继步骤消费。数学脚本和参数未改，随后重新核实际作业是否启动。

改正后的workflow SHA256：`5fa310bb580ccc1c6f252ea8f7d37aa11090d72d21c533e4a0ca213ff514650b`。
