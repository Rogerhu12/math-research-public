# 原85保存的3×3方向：奇异方向、残差投影和局部η滤波

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：独立Actions消费者源码与接口；尚未执行。** 本消费者只对实际85已保存的小矩阵作算术，不求新的场、RHS、参数Jacobian、尾、有限差分、候选试步或优化。不修改原85/87，不复写原接受标志，也不设置新的候选或BVP门。所有SVD、范数、矩阵乘法和滤波预测只在本公开仓库的Actions执行；本地完成的仅是源文本、AST、原JSON/SHA及整数形状核对。

## 1. 有限诊断所要分开的事实

[实际85原结论](2026-11-15-actual-request85-damped-resume-eight-full-steps-publication-limit.md) 的八次试步全部在α=1接受。已有原字段显示，末次方向的缩放矩阵第三行为 `[0.9999999587945169,0.9999877763891754,-0.9999999085937623]`，第二行为 `[-0.0002870641531240283,0.004944397337599663,-0.00042756316303207287]`，第一行约为百万分量级；原η为0.1。这提示列尺度受第三方程高参数敏感度影响，但不能仅据这些条目确定残差主要投在哪个弱奇异方向。

另一个原读数是末三mode轨迹最大值 `[10.9259498266004,3540.629483970082,15.145895646229546]`。第三方程Jacobian条目很大，并不直接等于第三mode的当前轨迹幅度很大。第三mode幅度、边界方向及其几何解释由独立saved-boundary消费者处理；本文件不做项目化、UH相位或Robin归一化。

本消费者支付缺少的局部线性分解：当前保存的未加权残差在原缩放Jacobian左奇异方向上的投影，以及原η对每一方向的保留比例。它也能区分“原方程的有限Jacobian条件差”与“增广矩阵因ηI而满列秩”。二者都不是严格参数横截性证明。

## 2. 唯一输入及来源范围

硬锁实际85完整原状态：

```text
run 43667636063
source c9daab1a9f7b1330c6099450bd018bfab9026b0d
job 132670464205
artifact 14143056682 / 268505 B
ZIP SHA 708ce51fb634552d376013d05b57e4f42cdc07d699e25753a2af0a2ea36e5775

small-core-damped-resume/damped-resume-status.json
54251 B
SHA256 72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a
```

消费原八份 `searches[i].direction_model`，逐项保留原 `r,J,D,A,z,d,Jd`、6×3增广矩阵和六项右端。还读取各原accepted trial以及下一原残差；最后一步的下一残差来自 `final.low_equations_used`。这八步均为原α=1，故保存的实际方程变化可以与同一步的线性预测直接分列，完全不需要重跑原模型。

完整状态SHA、schema、完成/未解身份、0.1/8/20、原0.2 Armijo系数、1e-8阈值、四原输入身份以及11个原消费源码的完整文件SHA均核对。原状态中的11源payload须与消费者同置于computations目录，但**不导入或执行它们**。四大数学输入仅核原状态内的既有绑定，不重新下载或读取accepted/prepared/anchor/config payload，不声称本消费者新审了真实112尾矩阵原字节。

本消费者的原始状态副本按原字节保存。85科学step成功但最终候选标志false、publisher另失败，这三个含义分别保留。

## 3. 所计算的固定小模型

每个保存迭代采用原记录的

$$A=JD^{-1},\qquad m_{\eta}(z)=\tfrac12\|Az+r\|_2^2+\tfrac12\eta^2\|z\|_2^2.$$

在普通浮点中，原保存的A、重新做 `J/D`、`Az` 与 `J(z/D)` 可能有不同运算顺序。因此消费者保留所有原数组，分别读回差异；不以它们逐位相同作为新科学门。

直接对原3×3 A作SVD：

$$A=U\Sigma V^T,\qquad \xi=U^Tr.$$

对显式正η，理想实数模型的解及残差滤波为

$$z_{\eta}=-V\operatorname{diag}\!\left(\frac{\sigma_i}{\sigma_i^2+\eta^2}\right)\xi,$$

$$\widehat r_{\eta,i}=\frac{\eta^2}{\sigma_i^2+\eta^2}\xi_i,\qquad
q_i=\frac{\sigma_i^2}{\sigma_i^2+\eta^2}.$$

保存每个原奇异方向的初始残差投影、半平方贡献、保留/移除滤波及新预测分量。**不从6×3增广奇异值平方减η²反推小奇异值**，以免相近量相减掩盖当前需要查看的弱方向。

同η=0.1的SVD方向只用于和原实际保存方向对照，不替换它。原方向仍通过原 `Jd`、真实斜率及原非线性试步解释。原增广返回秩3并不是原J的秩证明：ηI本来就使增广矩阵满列秩。

若CLI显式请求 `0.01`、`0.001`，仅在**同一保存的r/J/D/A**上形成两个局部线性模型预测，保：

- 三个参数方向、原J作用、原方程预测残差与各原方程的斜率/线性目标下降；
- 保存A的模型下降、阻尼罚项及相应正阻尼二次目标下降；
- 原A模型的stationarity读回，以及A动作和原J动作之间的运算差异。

原J动作下的未加权线性下降为

$$\Delta m_J=-r^T(Jd)-\tfrac12\|Jd\|_2^2.$$

正阻尼模型的下降则严格以保存A动作计算

$$\Delta m_{A,\eta}=-r^T(Az)-\tfrac12\|Az\|_2^2-\tfrac12\eta^2\|z\|_2^2.$$

二者在输出分列。没有把罚项加到原非线性residual或原试步merit。

## 4. 判读边界与可支持的后继

若原残差在 `sigma_i` 相对η较小的方向上有实质投影，而该投影被滤波大量保留，这提供当前**固定小模型**受阻尼限制的直接证据。它不保证改变η后新的参数仍在域内、原真实merit下降或原单位缺陷达到阈值。

原参数图是否具有严格非退化Jacobian仍未由普通浮点SVD证明。原final保存的三次坐标有限差分为“每列最大相对误差”摘要；它不能自动作为弱奇异组合方向的导数误差证书。本消费者明确保留这条边界，不为它重新支付FD或加入新门。

当前原轨迹和边界幅度的分析由独立消费者负责。此处只把原final轨迹max、原右块条件、原域最小值及参数FD摘要原样复制作上下文；不从高参数敏感度推断轨迹爆炸，也不据缩放后的弱奇异值宣称新的根或高109非共振。

第87轮继续原η=0.1，不依赖本消费者完成。下一次真实候选如改变η，应作为明确的新算法参数，仍保原域、真实斜率、原Armijo、原unit/full112阈值及最终FD/Arb/circle。这里的0.01/0.001预测从不冒实际试步接受。

## 5. CLI、依赖与产物

```text
python -u computations/geometry_20261115_saved85_direction_spectrum.py
  --status <上述85完整原状态文件>
  --comparison-damping 0.01 0.001
  --out <fresh-output>/saved85-direction-spectrum
```

`--comparison-damping`也可省略，此时只分析原η=0.1。不允许隐式网格扫描或其他未声明η。本入口只有公开repo Actions的环境门后才导入NumPy；依赖为stdlib和已有 `numpy==2.3.5`，不需要SciPy、Flint、native、原78恢复或网络请求。

与独立saved85几何诊断可共用原状态输入、同一job运行，两个输出目录独立。该source仅负责原方向小模型，不与几何消费者重复。

产物：

- `actual85-original-status.json`：原输入字节副本；
- `saved-direction-summary.json`：少量原标量、八组奇异值/残差投影/显式η预测与范围，供公开读回；
- `large-arrays/saved-direction-analysis.json`：完整原数组、U/σ/V、全部算术对照和来源，artifact保全；
- 若发生工程/算术异常，`saved-direction-error.txt`与上述JSON保留具体异常/traceback和已完成行，不删除原数据、不把原85状态改成失败。

数值对照仅报告，不依据小误差、秩或滤波比例决定科学接受。输入不匹配、缺字段或文件不是本消费者所声明的对象时才明确拒绝接线。

## 6. 冻结前静态范围

`source-only-static-check.json`记录：原85完整SHA/字段形状、八次原记录、11个数学源文件SHA、源码AST以及numpy只在Actions门之后导入。没有导入此消费者，没有构造数值fixture，没有执行SVD、norm、dot、滤波或任何科学函数。

源文件、接口及静态回执的最终字节数与SHA统一列在同目录 `frozen-files.json`。新消费者不是87的前置门，不占用现有原求解源码，也没有由本作者派发任何Actions。

## 主控发布接线

科学源码保持20fcaa26原字节。草稿中的`source-only-static-check.json`原件在此保存为[唯一源码静态回执](2026-11-15-saved85-spectrum-source-static-check.json)，原`frozen-files.json`保存为[原冻结目录清单](2026-11-15-saved85-spectrum-source-frozen-files.json)；其中接口SHA记录的是追加本节前的原草稿，不冒当前文档SHA。唯一实际请求与工作流见[88接线](2026-11-15-request88-saved85-spectrum-workflow-interface.md)。
