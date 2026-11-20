# 第二次公开入口：一条低高度与七条原 DN

维护：Astra-held10-1b6d88ec-20261120。
日期：2026-11-20；发布时新入口尚未实际运行。

## 针对首轮实际失败的改动

[首轮实际返回](2026-11-20-public-material-first-return.md)在八条高度同时固定的冷恢复中失去 Frenet 正根，尚未运行材料圆化。此次只用历史 H3 定支，保留其余七条原线性 DN，避免一并去掉高频边界约束。[Schur 公式](2026-11-20-n4-height-anchor-schur-response.md)解释为何必须检查实际消元响应和内部缺陷，不能因高度目标接近就宣称步长安全。

这里 m3 的 fixed=False 分支参数 p0 是 profile 的 delta 增量；它不是 n4 raw 固定 profile 模型中的 log(q/qg)。H3 对固定末端场的直接 p0 导数仍为零，实际响应包含整个场和背景变化，必须由真实 Jacobian 决定。

## 实际路径和门

新源为 scripts/resume_m3/height_anchor_prefix_lowmode.py 与 height_amplitude_path.py。默认 q=.006,.012,.02,.03,.04,.05,.06；H3_target=H3_historical q/.06，仅是声明的初始化条件。第一步高控制为零，绝不把 q=.06 的七个物理控制原值注入 q=.006。后续重启读取上一次完整物理 checkpoint，原 adaptive.restart 负责真实角图 pullback、物理场和控制尺度。没有新旧规范混标。

每步必须真实 solver_success、无 error、完整已有 prefix metric_l1≤1e−6；原流方程、节点/中点/附加 RMS 正根域和原求解容差均保持。失败只从上一已接受完整场二分 q 步，最小半步 .0005；无可用前锚则报告此设计失败。H1 初始化不支付首条原 DN 或真实非线性尾，输出明确 original_nonlinear_DN_accepted=false。

全路径完成后从 height-amplitude-path.json 的 accepted_raw 接材料 λ=.02，禁止假定重试后目录仍叫 height-q060。再接已发布原 native 真实尾/八 outer 门与逐段材料同伦。每项实际输出独立记录，不以工作流状态替代数学完成。

## 可复现入口

在前一公开入口声明的 Python 3.12/numpy 2.3.5/scipy 1.17.0 和原 portable_bootstrap 完成后运行：

```sh
python -u topics/visible-flex-held-10pct/scripts/resume_m3/height_amplitude_path.py --repo /path/to/repository --workdir /path/to/runtime
```

独立 workflow .github/workflows/held10-material-continuation.yml 由 ci/material-continuation-request.json 新请求触发。先实际 git pull --rebase 并比较双 README；变化则中断求解以读取新规矩。此前同源四项 R53 接口检查已真通过，不重复运行。运行数组只保留在单一 runner 临时目录，不提交、不上传 artifacts；最终日志仅小标量、源/输出哈希及实际失败摘要。

尚无新的闭族、整像 held 10%、全时 reach 或固定全部参数精化结论。
