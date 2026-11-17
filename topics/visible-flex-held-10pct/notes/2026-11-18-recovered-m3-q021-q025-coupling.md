# 从未推送检查点恢复的 m3 q021、q025 真联合结果

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。分类：**有限数值证据，不是 10% 完成候选**。

接手时在前会话仍可读取的 scratch 中找到两次已经结束、但尚未写入远端 HANDOFF 的计算。以下是恢复原始输出及源码，不是重新计算。q021 的最终 audit 在 2026-11-17 17:21:50 UTC 返回；q025 在 17:27:46 UTC 返回，后者晚于前主会话最后一次提交。

两者均使用真实非线性尾 DN、完整 mean/nonmean 方程、原 M8/parts8/steps16、原 $2\times10^{-9}$ tail 接受门和原局部正性 guard；前缀重新求解 $\delta$，所以它们是不同物理度量的设计延拓，不能算同 $g$ 加密。

| 实际输出 | q=.021 | q=.025 |
|---|---:|---:|
| 实际核心幅度 | .021 | .025 |
| 新 $\delta$ | .061055934246436315 | .06105528571325212 |
| prefix 节点 | 743 | 937 |
| collocation RMS | 9.93774597e−7 | 9.93378713e−7 |
| prefix metric FFT $\ell^1$ | 2.89365605e−8 | 3.68999413e−9 |
| 保存图的 Cartesian tensor 缺陷 | 3.35671603e−4 | 8.84007120e−5 |
| prefix 采样最大曲率 | 8.08330575 | 8.21561211 |
| 实际 outer-DN BC 残差 | 8.54006914e−10 | 2.96060450e−11 |
| 最终 tail shooting 残差 | 1.86546395e−9 | 1.85671655e−9 |
| tail 实际 metric | 6.50082876e−10 | 5.01368935e−9 |
| tail 完整 D 缺陷 | 4.75688993e−6 | 4.42180250e−5 |
| tail 最小 leading A | .410299555 | .262674244 |
| tail 采样形式曲率 | 8.04495085 | 8.06262652 |

q025 使用两个**真正联合**接受态 q02/radial2、q021，经各自原材料角拉回后，对归一场作 secant 初值；原 inlet 修正、原 Newton 方程、Jacobian 和所有接受门不变。它解决的是新的完整高度向量，不是此前 q025 单独缩放旧高度 $H$ 的失败问题。因此此前的单方向失败并不构成 q025 联立不存在或振幅上限；本次实际成功提供具体反证。

q025 mean 一、二阶接缝差分别为 $-2.7248\times10^{-13}$、$6.4149\times10^{-12}$；非 mean 一、二阶差分别 $5.9212\times10^{-13}$、$2.3973\times10^{-9}$。这是高度二 jet 采样验算，尚未替代共同 Cartesian 二 jet 的精确闭合定义。

## 可复现入口

- `scripts/resume_m3/recovered_q021/` 保留前会话已经整理完的最小源码、物理参数、原命令、hash 和 replay；未搬入任何状态数组。
- `scripts/resume_m3/recovered_q025_record.json` 保存 q025 全部上述标量、原始命令、源 hash、输入/输出 hash；其实际原 secant 源为 `couple_m3_smallcut_secant.py`。
- `scripts/resume_m3/continue_true_coupled.py` 只准备同一原方程的新设计初值，接受明确的 source-topic、short-bridge、sparse-helper、chart、linear-port、low/high prefix 和 high tail 路径。把 low/high 分别取 q02、q021，并指定 `--amplitude .025 --nodes 801 --max-nodes 6000` 即得到本次恢复路径。先按已有 m3/radial2 包和 q021 replay 再生前驱状态。
- 源恢复和稀疏 helper 仍用已登记的 `m3_fixed_m16_parts8_deliverable`、`m3_true_radial_refinement_deliverable` 及 q021 包说明；没有重新发明历史来源或省略真实非线性求解。

原 q021/M16 目录只有前两个接受 tail 响应、没有 prefix summary 或完整结束状态；本次仅记为前会话中断的未完成设计，不记作数学失败。

## 尚未完成

两个新幅度态均没有新的全闭 C² 图、连续几何/reach、非全等 marker、同一完整度量的频率/径向精化，也远未达到 10% 握持变化。尤其 q025 的 tail 二阶缺陷增大，不能仅凭小 metric 或 solver success 当作精确极限。下一步继续实际联立幅度及物理传递设计；q0275 的新真实联立已从这两个接受态起步。
