# 一般 $H_1=0$ 原 Dixon 输入：首次编译失败与最小修复

日期：2026-11-28（Asia/Taipei）。

## 实际执行身份

首次输入是 `notes/2026-11-27-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-input-8542.py`，Git blob `bb8d75842d5dded34d772744d72c52d2351c80dd`，SHA-256 `98868120a2de2a9633855a2757e3f5e3ed6e19184465890e2a16a6308e82d105`，19737 字节。

[Actions run 46060538070](https://github.com/Rogerhu12/math-research-public/actions/runs/46060538070)，job `140713461189`，实际主线提交 `a4bf8bc7e8f1efe6235779090a9afc32e861b9ef`。工作流外层结论为 failure。

## 准确停止位置

驱动器在启动数学子进程前执行 `compile(source.read_text(), str(source), 'exec')`。原源第 426 行的完整坐标乘回断言少了生成式末尾及闭括号，真实 traceback 是：

```text
assert all(sum((coeffs[j]*columns[j][i] for j in range(len(columns))),A())==target_vec[i]
SyntaxError: '(' was never closed
```

日志时间为 2026-11-27 20:00:19 UTC，驱动步骤退出码为 1。数学源没有启动；没有内层用时、内层峰值内存、Dixon 秩、目标返回或新权分母覆盖。不能将该次编译失败登记为数学超时或整 $H_1$ 排除。

## 最小修复与范围

唯一修复是在该断言下一行补上 `for i in range(len(target_vec)))`，使其核验每个完整坐标。新源为 `notes/2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py`，blob `5cabfb620fa4095b551145f9c988abf30772e197`，SHA-256 `ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc`，19772 字节。

原输入、完整四维权代数、Dixon 必要列、$1/\lambda/D$ 目标、最终分母保零规则及 120 秒 / 1 GiB 上限均不变。准备此记录时新源尚未执行。旧 $b(\lambda)=0$ 的 316 次权覆盖保持；一般 $H_1=0$ 仍未闭。本记录不传输或保存可重算证书载荷。
