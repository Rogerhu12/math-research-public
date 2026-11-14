# R187 有限分支的 dense normal LM / 真实值 Armijo 入口

本组为 R187 新实际参数化提供独立数值工具。它不使用或改变 36 的字段、normal、方向或接受态。源码已经在 functions.exec 的 V8 中编译并执行，六个小算例均完成；没有创建 OS 进程，不记虚构的 session 或 exit 0。本组没有运行完整 R187 provider；其真实 181 维求解由主线直接消费此入口。

## 文件与接口

- `scripts/fd2d_dense_normal_lm.cjs`：20,013 B，SHA256 `1e74ee24bd59b3f7a0b41fedf17e338f7ea42f113de72986396fde484de38ea4`。
- `scripts/fd2d_dense_normal_lm_check.cjs`：可重复的有限算例。
- `notes/2026-11-12-fd2d-dense-normal-lm-v8-check-01.json`：实际 V8 输出与来源。

模块导出：

```javascript
const {
  prepareNormal, solveDampedNormal, lmStep, runLM
} = require("./fd2d_dense_normal_lm.cjs");
```

输入 normal 的约定是同一个实际参数向量处的
$$
H=J^T J,\qquad g=J^T r,\qquad R^2=\|r\|_2^2.
$$
`H` 可为 row-major 的 `Float64Array(n*n)`，也可为二维 rows；`g` 是长度 n 的数组。`diagonal` 可选：若给出，会报告它与实际 `H[j,j]` 的差异；尺度仍由实际 H 对角计算。`normal.z` 若提供，必须逐数等于传入的 z。所有这些数组在求解前复制，后续 value 回调复用 provider 缓冲区不会覆盖当前模型。

`value(z)` 可同步或异步返回平方残差数值，或 `{squaredNorm,...diagnostics}`。接受后的 `evaluation` 完整保留该回调对象，因此真实 `maxRelativeMetric`、`minImmersion` 等观察不会丢失。`valid:false`、非有限/负平方残差、回调异常、或回调修改输入向量均明确拒绝；不会把预估值替代真实值。

首个 normal 已有时直接消费：

```javascript
const step = await lmStep({
  z,
  normal: storedNormal,
  value: v => provider.value(v),
  lambda: 1e-3,
  maxDampingAttempts: 8,
  alphas: [1, 0.5, 0.25],
  onTrial: record => saveTrialObservation(record)
});
if (step.accepted) {
  z = step.z;
  lambda = step.nextLambda;
  // 此处保存 step.evaluation、实际 z 与来源；不能只保存预测方向。
}
```

连续有限迭代入口：

```javascript
const answer = await runLM({
  z,
  normal: v => provider.normal(v),
  value: v => provider.value(v),
  lambda: 1e-3,
  maxIterations: 40,
  squaredNormTolerance: 1e-18,
  onAccept: ({iteration,z,step}) => saveActualAccepted(iteration,z,step),
  onIteration: record => saveIteration(record)
});
```

`squaredNormTolerance` 是调用者明确选择的有限目标，不是连续几何证书或 README 最终条件。`maxIterations` 只是本次调用的保存边界。`lmStep` 不需要重算已保存的首个 normal；`runLM` 每次接受后在下一迭代生成匹配新 z 的 normal。回调可以异步闭存实际接受态。

## 列尺度、阻尼与实际线性残差

对正对角，严格使用
$$
S_{jj}=H_{jj}^{-1/2}.
$$
准确零对角取尺度 1，并列出对应列；对真正的 Gram 矩阵，这列完全不可观察。负对角不是合法的 `J^TJ` 输入，会明确报错。

工作矩阵先采用
$$
H_s=\tfrac12(H+H^T),\qquad
A=S H_s S+\lambda I,\qquad \lambda>0.
$$
两个尺度乘法造成的最后舍入不对称也只作明确记录的对称平均。报告同时给出对原始非平均 scaled H 的真实方程残差；不会以工作矩阵残差冒原矩阵残差。

Cholesky 求解
$$
Aq=-Sg,\qquad d=S q.
$$
若 `H_s` 半正定，正阻尼使 A 正定；非零梯度下
$$
g^T d=-(Sg)^T A^{-1}(Sg)<0.
$$
实际浮点因子发现非正/非有限 pivot、非有限解或非下降方向时，显式增加 lambda 再求。没有隐藏 pivot floor、额外 diagonal shift、伪逆或把近零列偷偷删除。默认 lambda 区间为 `[1e-16,1e16]`，增加因子 10；调用者可显式选择别的正范围。单独的 `solveDampedNormal` 仅求一次指定阻尼，自动增加逻辑位于 `lmStep`。

点积和三角求解使用补偿累加。报告包括原矩阵残差、工作矩阵残差、pivot 范围及所有对称化改变量。模型预测来自当前有限线性化，不称为该空间或原问题的最小残差下界。

## 全、半、四分真实值才接受

费用为
$$
\Phi(z)=\tfrac12 R^2(z).
$$
默认依次实际评估 $\alpha=1,\tfrac12,\tfrac14$，仅当
$$
\Phi(z+\alpha d)
<
\Phi(z)+c_1\alpha g^Td,\qquad c_1=10^{-4},
$$
才保存接受态。三个实际候选全部失败后才提高明确阻尼。每次候选的真实值、Armijo 右端、错误（若有）、预测降低和实际降低均留在 trace。

预测降低为
$$
-\alpha g^Td-\tfrac12\alpha^2 d^T H_s d.
$$
实际与预测的比值仅用于下一次阻尼选择：全步且比值大于 .75 时除以 3；比值小于 .25 时乘增加因子。其他情况保当前阻尼。没有通过预测降低直接接受。所有默认接受点都是真实全/半/四分之一候选。

## 实际 V8 检查范围与结果

这次执行全部维数至多 2，实际 wall-clock 记录为 2 ms；它核数值与回调机制，不是大模型性能测试。

| 算例 | 实际结果 |
|---|---|
| 三残差、二维满秩线性 LS | 与独立 2×2 逆矩阵方向误差 $2.22\times10^{-16}$；原 scaled 方程残差 $4.44\times10^{-16}$；一次真实全步接受 |
| Rosenbrock 两残差 | 19 次接受、31 次实际 value 调用、12 次真实拒绝；包含全/半/四分步；平方残差 $24.2\to8.184433124263162\times10^{-24}$ |
| 准确零列 | 未观察坐标 7 逐数不变，实际平方残差降至约 $9.98\times10^{-7}$ |
| 准确 rank-one normal | lambda $10^{-6}$ 时实际平方残差 $4\to9.99999\times10^{-13}$ |
| 故意加入舍入量级不定扰动 | 这不是准确 Gram 的声明；三个非正 pivot 被明确拒绝，lambda 从 $10^{-18}$ 显式增至 $10^{-15}$ 后真实步接受，隐藏 shift 为 0 |
| 返回 valid:false | 全/半/四分三次都实际调用，全部拒绝 |

Rosenbrock 的每个接受点均单独核了严格 Armijo 和真实平方残差单调下降。所有原输入数组保持不变。检查完整 JSON 保留实际向量、逐次接受平方残差、回调次数和所有近奇异诊断。

## 复现与范围

在 Node 可用时，可执行：

```text
node scripts/fd2d_dense_normal_lm_check.cjs
```

当前已完成的运行在 V8 isolate 中用同一 CJS 源编译，并调用同一导出检查函数；没有把未来 Node 命令记成已运行。完整 R187 真实 provider 的参数身份、采样定义、实际接受态及几何残差应由其独立报告绑定。此工具只执行所传有限目标，不能把其中 norm 收敛替代连续度量、嵌入或 reach 的支付。
