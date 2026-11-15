# Request91：实际83四行完整列贡献与相邻词诊断接口

类型：实现接口与已保存来源事实；新算术结果尚未产生。  
作者：ChatGPT，`exact_refinement`。  
日期：2026-11-15 UTC。

## 1. 这次具体回答什么

Actual83 已逐行分开理想仿射残差 $m$、实际状态差 $h$ 所对应的仿射残差 $a$、原 noJ 实际残差 $t$。控制最大范数的 stage10/Pi76 上，状态形成项几乎抵消了理想下降；但另一行 stage10/Pi73 仍有较大的剩余流／切向模型项。原报告见 [actual83 完整精确结论](2026-11-15-actual83-exact-realized-step-component-decomposition.md)。

本入口只对原四个观察行给出**完整逐列账**，并区分三种相邻 binary64 间距：状态坐标、实际 flow 输出、已经除过原 $\sigma$ 的 native norm 标量。原 $\alpha=1/512$、原 $\delta$、原 $\eta$、原矩阵、原 $2\times10^{-9}$ 容差和原接受结果全部不改。

| 原 global row | stage $n$ | 局部行 $i$ | 物理分量 | 作用入节点 | 直接负项出节点 |
|---:|---:|---:|---|---:|---:|
| 2539 | 10 | 187 | Pi76；实际范数控制行 | 11 | 10 |
| 2536 | 10 | 184 | Pi73；剩余模型项最大行 | 11 | 10 |
| 2762 | 11 | 186 | Pi75；earlier61/69观察行 | 12 | 11 |
| 2128 | 9 | 0 | Q1；原方向 endpoint 最大行 | 10 | 9 |

**方向不能反转：** stage $n$ 的原方程使用 $J_n$ 作用于 node $n+1$，并减 node $n$。本次所有224个入列和出端一个负项均导出；没有只保 top 列。

本地只做 source／AST／真实原 metadata 结构检查，不 import 新科学模块，不运行 Fraction、矩阵、norm、相邻词或数值测试。所有新算术只由公开 Actions 执行。本次仍不是 native 或其他科学接受门。

## 2. 冻结源与最小依赖

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `exact_20261115_actual83_four_row_state_formation.py` | 41270 | `17659d25b5f24d21843c188f845247ce3a132a7462e28d7b4fbcdf59db17bc8c` |
| `exact_20261115_fetch_actual83_four_row_inputs.py` | 10726 | `e3dae97ae649dadd46cf77508e84b8573daaff30a77c14cc6f7c0a77a3bc6c92` |
| 原运输内核 `exact_20261114_fetch_pinned_public_artifact.py` | 28006 | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` |

只需 Python 标准库。没有 numpy、scipy、原78文件恢复、native worker、RHS/J 源导入或科学进程。新科学源不执行任何已冻结原模块。原 source 身份仍通过固定的 actual83 result、input-binding、probe/result 和已导出的完整原 source 字段保留。

`nearest_even_integer` 与 `rational_to_binary64_word` 两函数的 AST 与已付 actual50 源 `exact_20261114_saved_stage_full_rational_reference.py` 完全相同；来源 SHA 为 `119864f3dffd764500e3f15b9bfe8c7e27367384486eaaa11a5db885422b8f12`。本次直接保留两函数完整文本，不 import 该旧模块，因此没有引入旧四A数学或额外运行依赖。

静态回执为 `2026-11-15-request91-static-source-check.json`，2391 B，SHA`6feb9fc6bf87ffd2c28fde47785da3a572ae18d95dc48ca4a315f233288bda2e`。它记录实际83的字段／三完整块／四节点 metadata 检查、舍入函数 AST 恒同和运输安全提取代码前缀恒同；不是科学数值验证。

## 3. 确需两个真实 artifact，不能只靠83总响应恢复J

83完整小包没有保存任何 J 系数 payload：其 input-binding 只有原144个 J chunk 的 descriptor，原行账只保 stage SHA 与作用总和。不能从 $Ah$、$A\delta$ 的两个总和唯一恢复224个系数或逐列贡献。

因此最小新增原件是原73末 snapshot 的 **一个原 chunk**，含 stage8–11。新运输入口真实核验完整原73 ZIP 后只提该一件；不伪称只下载了1.6MB，也不声称其他成员单独做过解压／CRC。

| 输入种类 | 真实固定值 |
|---|---|
| 完整 actual83 | run`43668743706`；source`8d199eda5c1f1df162ded244e8dfd012e0c8d127` |
| actual83 artifact | `14143009723`；`visible-mainline-modelresponse-43668743706-1` |
| actual83 ZIP | 48375172 B；`9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c` |
| 原73单chunk来源 | run`43657001633`；source`9515d5aaf7c68f8efd366438d6bd81ce73c3486f` |
| 原73 artifact | `14141540502`；`visible-mainline-nojprimalnative-43657001633-1` |
| 原73完整 ZIP | 1752742419 B；`3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9` |
| 选中原文件 | `native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le` |
| 原文件大小／shape | 1605632 B；`[4,224,224]`，`<f8`／C，原 stage8–11 |
| 原 chunk SHA | `fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677` |

该原 chunk descriptor 同时与 actual83 的原 input-binding 逐项核：`chunk_index=2,row_start=8,row_stop=12`、原 file、bytes、SHA/rawSHA 都必须相同。完整原 J 的身份仍为 `1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4`；本次不重载全部231211008 B的未缩放J数组，只读取选中四行共896个系数做科学算术。

两个取件都沿冻结512247运输内核：精确公开 repository、Actions 环境、API run/id/name/size/digest/expired 与 source commit，完整 ZIP 流式大小／SHA，HTTPS，跨 origin 移除 Authorization，所有 ZIP 路径／重复／特殊文件／符号链接检查，独立新目录和完成 receipt。原73定制提取器的路径检查与单成员流式 CRC/SHA/size 实现前缀，与已运行83的 `51f86528...` 源逐字相同；只有选件范围和 provenance 独立改变。

凭据只由冻结内核从环境取得；新 helper 不读取或打印它们，不输出签名 URL。科学 step 不应配置 token。新 helper 将完整固定 tuple 转成原内核所需五个 CLI flags，调用方不再手写不完整的参数集。

## 4. 准确 CLI

三条命令分别独立运行，输出目录均须不存在；取件目录在 `RUNNER_TEMP` 下：

```bash
python computations/exact_20261115_fetch_actual83_four_row_inputs.py \
  --input actual83 \
  --out "$RUNNER_TEMP/request91-actual83"

python computations/exact_20261115_fetch_actual83_four_row_inputs.py \
  --input original73-j-chunk \
  --out "$RUNNER_TEMP/request91-original73-Jchunk"

python computations/exact_20261115_actual83_four_row_state_formation.py \
  --actual83-directory "$RUNNER_TEMP/request91-actual83" \
  --original73-chunk-directory "$RUNNER_TEMP/request91-original73-Jchunk" \
  --out "$VISIBLE_OUT/actual83-four-row-attribution"
```

这里的 `computations/` 相对课题根；workflow 可改用相同文件的绝对路径。无需新的 `--eta`、步长、容差、模式数或 future result SHA。

科学入口读取两个完成 `_pinned_public_artifact_receipt.json`，核全部固定 tuple、完整 ZIP actual_size/SHA、原 head SHA、新运输 helper 真 SHA 与冻结内核 SHA。只凭本地目录或 `.download-complete` 不足以越过该来源绑定。原83 exact result 固定为26350 B／`60feb7732547dcd04ef2469c5a1adf7cef5fd93f714107ac41cdb8f71282ff61`，实际 probe result 固定为2679 B／`7be2d7f0a98445e5efcd0ba146b7f8257483fa7593a54a6b389e8279f7fcf6ea`。

## 5. 算术合同：全224入列和出端负项

沿 actual83 原记号：

$$
h=x_{\mathrm{trial}}-x,\qquad
w=\alpha\delta,\qquad q=h-w.
$$

$h$ 是两原 binary64 词代表的精确实数差；没有先做 binary64 减法。本次只在四个相关完整节点9、10、11、12核 $h,w,q$ 与原83已保存 dyadic 编码的逐项相等，并保存全部896坐标。实际原词和 node SHA 均保留。

四个 stage 行逐一计算

$$
c_j=(J_n)_{ij}q_{n+1,j}\quad(0\le j<224),
\qquad c_{\mathrm{out}}=-q_{n,i}.
$$

要求并记录

$$
\sum_{j=0}^{223}c_j+c_{\mathrm{out}}=s_i^{(83)}.
$$

这只是在新诊断中核同一原件与编码，不是允许／拒绝原 native 的门。每列完整保存原 J 词、base/trial 词、$h,w,q$、未归一和原 $\sigma_n$ 归一贡献；出端直接负项单列。三类输入列明确划为：$h=0,w\ne0$、$h\ne0$、$h=w=0$。每类保完整列、带符号和与绝对贡献和，最大列仅是附加摘要，不替代全列输出。

同时用同四行核

$$
r_i+\sum_j(J_n)_{ij}h_{n+1,j}-h_{n,i}=a_i^{(83)},
$$

$$
r_i+\sum_j(J_n)_{ij}w_{n+1,j}-w_{n,i}=m_i^{(83)}.
$$

原 $t_i-a_i=f_i$ 和 $s_i+f_i=d_i$ 也与原83完整行账核同。没有再做完整129248行矩阵作用；完整行账只作为已经核验的原参考读取。未查看的其他 J 行、cut/far 或其他节点不被冒称新科学复算。

## 6. 相邻词与原 $\sigma$／容差的关系

### 6.1 状态坐标

对 node9–12每个原 base-state 词，分别给出相邻有限下词／上词及两个精确间距。幂二边界的上下间距可能不同，不强行合成一个“ULP”。同时保留真实 trial 词，邻词只是诊断对象，不写入 trial，不新增试探。

节点级显示使用原 `sigma[node]`。每个观察行的列贡献另报告

$$
\frac{|(J_n)_{ij}|\,\Delta_{j,\pm}}{\sigma_n}
$$

及其与原 binary64 `solveTolerance` 的比值。这是保存线性行对一个相邻输入间距的响应尺度，不是实际非线性效果或严格误差上界。

本次不把乘法舍入和加法舍入拆成独立因果。$q$ 仍代表原完整状态形成表达式的总效应。

### 6.2 实际 flow 输出与目标

对每行分别保存 actual83 `trial-stage-out[n,i]` 与 `trial-states[n,i]` 的原词、相邻词与间距。这里的归一尺度为原 equation `sigma[n]`。另给精确的 flow-out 减目标，与原保存 trial residual 的差；整数最近偶数舍入所给的词也单列，不能把“精确数学零固定舍为+0”冒为原任意 signed-zero 减法规则。

83没有导出原基态的完整 flow-out payload；本次不从 `saved r + base` 倒推原 flow-out 位模式，不声称提供该未付的旧／新 flow-out 逐位比较。

局部格点间距大于某个阈值，不意味着存在正的普遍残差下界：输出仍可能与目标完全相同。没有从这次关系直接推出任何容差修改。

### 6.3 Native norm 标量

这是一项已经除过各行原 $\sigma$ 的无量纲量，**不再除以一个状态 $\sigma$**。原83完整 $r,m,a,t$ 全局精确最大值的分子／分母直接复用，不重新扫描矩阵或优化。

本次用已冻结整数舍入函数新算它们的正确 binary64 最近偶数词，分别与原 native norm 词比较；原 norm 的上下相邻间距和与原容差的比值也单列。因此可以据实际输出回答：精确 $\|a/\sigma\|_\infty$ 的微小下降，在它自身正确舍入后是否仍与原 native base 同位。这个结论在 actual83 尚未给出，本接口不预写答案。

所有 exact ratio 的十进制显示不是区间包络。实际比较、求和、范数参考相等与最近偶数舍入均用整数／有理数，不依赖显示值。

## 7. 输出与原始文件继续保全

新主 schema：`actual83-four-original-rows-exact-state-formation-and-word-spacing-v1`。

- `summary.json`：小显示读数、原双 artifact 身份、四行索引／贡献摘要／输出与目标间距、norm 独立读出、完成与错误。summary 的 exact ratio 只给原新算十进制显示；完整分子／分母均在主 result 和逐行文件，明确标记没有区间保证。
- `large-arrays/result.json.gz`：完整主结果、来源、所有原件保存收据、四行完整结果描述符、norm 完整精确读出。
- `large-arrays/input-binding.json.gz`：双运输完成回执、原83全矩阵来源、原完整J descriptor、选中chunk及十五数组、原容差／步长、四行实际坐标。
- `large-arrays/row-2539-complete-attribution.json.gz` 等四件：每件全部224个入列、直接出端、全部原八向量该行编码、exact sums 与间距，列不截断。
- `large-arrays/original-J-row-2539.f64le` 等四件：各原224个系数的1792 B字节切片。
- `large-arrays/four-complete-node-word-spacing-and-exact-increments.json.gz`：node9–12完整896坐标，不只保选择的目标坐标。
- `large-arrays/selected-original-node-increments.jsonl.gz`：从原83 ledger 提取的四条完整原 JSONL 行，另存原整文件 SHA／解压 SHA／记录位置。
- `large-arrays/selected-original-row-blocks.jsonl.gz`：原 stage9、10、11的三条完整原 JSONL 块；提取有新文件身份，不冒完整578块原文件。
- `large-arrays/original-inputs/`：原1605632 B完整J chunk、actual83十五份完整原 raw、原压缩 result/binding、manifest/probe summary，以及两个取件 receipt。这样后继可以直接从91实际 artifact 取得这次真正缺失的原 J，不必为同一四行重复取1.75GB。
- `progress.json`、必要时 `diagnostic-error.log`：已经完成的原件及逐行结果全部保留，不删科学数据。

原 J chunk 和全部原数组均在 `large-arrays` 路径下，只进 artifact。现有 publisher 对路径任一 `large-arrays` 分量的规则可直接使用；不需要扩展新的共享发布例外。入口不改工作流或 Git。

## 8. 资源、失败和不声称的结果

运输原73仍需下载并核完整1752742419 B ZIP；只在验证后提一个1605632 B成员，临时 ZIP 沿冻结内核删除。actual83完整提取约49MB；科学输出保十五 raw 和少量提取／新逐行记录。建议本独立 Actions 预留至少4GiB空闲，以覆盖两原包、独立临时文件及输出；这不是完整多轮 native 的资源上界，也不降低任何科学预算。

科学任务规模固定为四行各224个原系数、四完整节点共896坐标及少量原全局 exact ratio；没有新全系统分解、RHS、J、QR、solve 或 trial。耗时／RSS 由本次实际 result 给出，不预造性能值。

任何输入身份或原行核对失败都保原件／已完成行／实际异常，并返回非零；它只说明这个独立诊断是否完成，不改变原83或原73科学 outcome。预算／执行状态与物理接受分开。未对未来完整状态、其他步长或其他参数声明保证。

**本接口不选择新权重、列尺度、$\eta$、补偿方向或步长，不放宽原容差，不新增接受门。** 如果以后提出新的可实现方向，它仍须支付完整原非线性求解与原十档试探证据。
