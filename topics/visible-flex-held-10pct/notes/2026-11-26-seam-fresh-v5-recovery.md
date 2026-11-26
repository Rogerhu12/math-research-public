# 新 runner 原 q 链恢复后直接进入 v5 的薄入口

维护：Astra-held10-06bbeb39-20261126。范围：启动入口与实做的源码检查；本记录没有新增求解结果、接受场或几何证书。

## 为何需要此入口

当前 probe 的 v4 三次尝试仍在自然运行。独立新 runner 可以重生其自己的原始 $q=.006\to.06$、$\lambda=0$、$\lambda=.002$ 的 M8/M16/M24 链，然后直接调用已冻结的 v5 设计控制器；不必先运行 v2/v3 重表达、单 Newton 方向诊断或 v4 尝试。新场只按当次返回及原门接受，不声称与任何已经丢失的旧场逐字相同。

入口是 `scripts/resume_20261126/seam_recover_v5_material_design.py`。它由 `lowq_prefix_recovery_design.py`（SHA256 `a69f5c6ca118221700b16f01645b87be94afba349ca576825c47993891c22223`）作薄改：原恢复块逐字保留 6801 bytes，块 SHA256 为 `c6eb048d90ffa2863234455b68c324a43869ff7a5a10b88a6d2c7141dcc4dd9a`。原 `solve` 函数的完整 AST 相等；数值 chart 的当次 setup 绑定、冻结及原入口域检查逐字相等。

M8/M16 的 $\lambda=.002$ 场仍只在原 BVP 成功、完整物理文件和 SHA 通过后用于原完整场升阶；最终 M24 必须通过原全部有限前缀门。只有该真实 `lambda002_m24/run.json` 能进入 v5。原恢复阶段仍只接受子进程返回码 0。

## 唯一新分支

原入口末端的 `material_design_continue.py` 调用被替换为：

```text
warm_delta_phase_continue_v5.py
  --repo @REPO@ --work @WORK@
  --source-run @WORK@/fresh-v5/lambda002_m24/run.json
  --outdir @WORK@/fresh-v5/v5-material-design
  --max-attempts 3
```

v5 继续使用自己的真实零控制重表达和原求解/保存/接受门。这里不重新解释其参数、均值规则或原始元数据，不标记任何未求解重表达为新求解。v5 的正常三次预算返回码可能是 2；父入口完整保留实际返回码 2 与小 summary，不把它转换成成功。所有恢复阶段的返回码门不变。v5 三源在启动前核对固定 SHA，并记录其实现依赖与恢复输入的实际 SHA；v5 自身继续核对完整 provider 绑定。

## 调用与小投影

复用现有 lowq workflow 的真实 bootstrap 后，命令为：

```text
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261126/seam_recover_v5_material_design.py
  --repo @REPO@ --work @WORK@ --outdir @WORK@/fresh-v5
```

`@REPO@`、`@WORK@` 由现有 worker 替换。父入口只调用恢复链和 v5；不启动原 `.004` material design、尾求解或另一个诊断。数组、完整检查点和场仍只留 runner。父 `fresh-v5/summary.json` 只发布 `status/results/result/error/source_hashes`，子 `fresh-v5/v5-material-design/summary.json` 只发布 `status/stages/result/error`。不发布日志字符串或父 stages 中嵌套的子 progress；子控制器的 stage 是原 RMS、边界、metric、域统计、路径和 SHA 的小记录。

## 本次实际验证与限制

源文件 SHA256：`a8992f4de1b4ddc1a07c3a932f27254d98d6013ad022ffaa6113bcdcdbf4bd8f`。实际 `py_compile` 与 `--help` 均 exit 0；精确块/AST/源码 SHA 检查见 `2026-11-26-seam-fresh-v5-source-checks.json`。未启动 BVP，未生成新候选场，未执行原尾。这里仍是 $\delta$ 设计而非同一固定 $g$ 的精化；完成标准的真实全尾、共同 Cartesian 接缝、精化与几何证书均不由此入口自动支付。
