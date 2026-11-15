# 第114轮：完整三列预测方向与二维法向弯曲试探

作者：ChatGPT，GPT-6 Astra Pro（AI-assisted）  
日期：2026-11-15  
分类：**算法设计与条件解析说明；尚未执行的新数值试验。** 下述实际112数值仅引用其公开 Actions 原读出。没有本地科学运算，没有新验收门，没有宣布低三根、非零核、原 native 或完整曲面问题完成。

## 1. 已有事实与本轮选择

实际112：run `43685696741`，source `a7ea42924dbdaf8dab9377ace446690e0ce922c5`，compute job `132725609910`、report job `132725862494`。原标量摘要为 80,385 B，SHA-256 `09f1525dcb21d3968f78ed8fe8c4b1c46a91fa55fadff972025cedc22fd439b2`；摘要哈希不含日志分隔 LF。临时原 status 为 1,030,933 B，SHA-256 `02d85cf1f46cc1d108bbe7743e671c2c68a932dbc41ec76bddd232c3a7c6053f`。按根规则15，原 status 不留存 Git、Release 或新 artifact。

112的八个完整方向中，第0、7方向各二十档全拒，第1至6方向接受的 $\alpha$ 依次为 $2^{-17},2^{-16},2^{-15},2^{-14},2^{-13},2^{-14}$。原未加权目标从 `6958.2257628163525` 到 `6958.225762769887`；最终：

```json
{
  "parameters": [0.46303183673359155, -0.19282285315249734, 0.631643600595406],
  "unit_equations": [-117.96801026240819, 0.008956935105133464, -0.00020358048375542664],
  "numerical_parameter_condition": 2278293017617.1587,
  "original_unit_stopping_tolerance_met": false,
  "low_mode_candidate_has_small_full_recorded_right_residual": false,
  "native_nonlinear_solver_called": false
}
```

第7方向原 `J*v` 的第三分量是 `-0.00014494222130892194`，而直线 $\alpha=1$ 的真实第三式为 `-168.6711199103772`。最终原实差分检查在步长 $5\cdot10^{-6}$ 的最大相对误差为 `4.2493825301133406e-10`；这是原检查口径，不能据此给近零切向导数同样的相对精度保证。六个已接受点附近反复换向、最后一方向全拒及极小目标降幅，均不构成驻点、无根或普遍浮点底线证明。

本轮仍使用原三形状、原三方程，保持112的完整三列正阻尼预测方向，改变**非线性试探路径**。用第二、第三式的完整二维法向校正控制直线的大量高阶偏离。是否仍沿约束曲线近驻点，由真实114输出决定；不提前增加第四形状。解析控制结构另见 [原三控制与后112选项](2026-11-15-small-core-control-structure-and-post112-options.md)。

112在同一 literal 参数重评的初始第二、第三式与108末位略有差别。本轮仍将所有参数重新交原模型评价，不把旧 residual、J、W 或 FD 改标签为当前值。

## 2. 五个运行文件与来源闭包

| 文件 | B | SHA-256 |
|---|---:|---|
| `geometry_20261115_small_core_full3_curved_normal_recipe.py` | 47,791 | `be37ce213ddfd87972b5edc241a0b220fe0f424c553f5836b5df337ff1dd980e` |
| `root_20261115_small_core_curved_normal_scalar_readout.py` | 16,310 | `5316d62bf777426484fd8f1f4efef2e1203e939b5e7ac2d7d177fee72c6800ee` |
| `actual112-explicit-parameter-recipe.json` | 1,253 | `80b8b209819a548a263b2fca1769c27f2d4e195b160a9064c1872e2c3778f1e1` |
| `public-small-core-full3-curved-normal-request.json` | 23,996 | `7107c02ca2e5f43146c0799683607159fa7492ba289951d9c698f541a458506a` |
| `visible-larger-public-small-core-full3-curved-normal.yml` | 14,751 | `550cd3b2ddb3b9b029f3ed8fcb0adb709b5a52248e04cfcb6355623f652b7cf3` |

科学新 schema：`R259-original-full-three-two-normal-curved-trust-recipe-v1`。临时目录 `small-core-full3-curved-normal`，原 status 名 `full3-curved-normal-status.json`。

主来源共77件：112的76个 SHA 全部原样保留，只加当前科学入口。另两件元数据支撑为当前小读者和原规则监控器。112 producer闭包为17件，当前为18件；不把旧17件冒作当前完整闭包。旧108 `5d354015…`、112 `b9fff58b…`只核来源，不执行它们的 `main`。原3169 helper及其15件闭包保持，原 `CircleReference` 为 `3b9c45ab…`，调用其原 evaluate、完整参数 Jacobian、description及终检。

短 recipe只含实际112末参数、原 run/source、producer身份、原 status/summary的 bytes/SHA和四原数学输入身份。它**不是原 parent-status**，也不声称重新读取已删除的原 payload。当前入口接受这次真实112 producer或未来本入口自己真实 producer的短 recipe；后者仍须自身完整18来源，不伪造上轮评价。

四原输入保持：accepted `b4d2b98a…`、prepared `0f94dd88…`、真实112维零高尾 anchor `e788a28d…`、tail config `01930f3b…`。完整路径、bytes与SHA均在请求 JSON，缺失时从历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 按完整原件恢复，不重造数据。新科学仍 M112/T112、699节点和原真完整112×112零尾 J；不能用旧 profile slope 或对角猜值替代。

## 3. 完整预测方向保持112

记原三方程 $r=F(p)$，原完整三列 Jacobian 为 $J$。保持

$$
S=\operatorname{diag}(\max(1,|p_j|)),\qquad v=Sz,
$$

并在当前固定线性模型中用正阻尼增广最小二乘形成 $z$：

$$
\min_z\|JSz+r\|_2^2+\mu^2\|z\|_2^2,
\qquad \|z\|_2\le\Delta.
$$

源码 `full3_trust_direction`、`norm`、`next_radius` 与112 AST完全相同。仍是完整6×3带列主元 Householder QR、完整3×3三角回代；没有法方程、`lstsq/rcond`或奇异值截断。正阻尼下界和至多64次上界寻址、64次几何二分均原样。初始相对半径0.1，最大1。

实际 $Jv$、$r^TJv$、正阻尼 $\mu$、完整参数方向、增广形成模型的 stationarity 均原样保存。只有有限严格负原斜率进入原回溯。先保存已求出的方向报告，再尝试生成法向框架，框架失败也不会丢失已经实际形成的方向。

## 4. 弯曲路径及原点导数的条件论证

令 $c=(F_2,F_3)$，$C=J_{\{2,3\},:}$，$A=CS$。为形成框架，按两条完整行的正范数作数值行平衡，再对转置作完整3×2 QR。$N\in\mathbb R^{3\times2}$ 为两个法向列，$t\in\mathbb R^3$ 为剩余切向列。两条方程和三个参数列均保留，不选单独 $J_{33}$ 图，也不截断小奇异值。

每个回溯量 $\alpha$ 定义预测点及待校正点：

$$
p_\alpha=p+\alpha v,\qquad
q(\alpha,w)=p_\alpha+SNw,
\qquad w_{\rm initial}=0.
$$

校正目标为

$$
c(q)=c(p)+\alpha Cv.
$$

它不是把当前 $c$ 覆盖为零，也不是无条件采用特例 $(1-\alpha)c(p)$。实现直接使用原方向报告实际保存的 $(Jv)_{2,3}$ 形成目标。所有实际候选的原三式均由原模型重新返回。

在原光滑有限模型的一个合法邻域中，若 $C$ 真为 $Dc(p)$ 且其秩为2，则 $CSN$ 可逆：$N$张成 $\operatorname{range}((CS)^T)$，而该空间与 $\ker(CS)$ 只有零交。对

$$
G(\alpha,w)=c(p+\alpha v+SNw)-c(p)-\alpha Cv
$$

有 $G(0,0)=0$、$G_w(0,0)=CSN$、$G_\alpha(0,0)=Cv-Cv=0$。隐函数定理给出局部 $w(0)=0$、$w'(0)=0$，因此

$$
q(0)=p,\qquad q'(0)=v,\qquad
\left.\frac{d}{d\alpha}\frac12\|F(q(\alpha))\|_2^2\right|_{0}=r^TJv.
$$

这是**条件局部论证**，不是本次浮点评价、复步长 Jacobian、原连续ODE或全局曲线分支的区间证书。源码对 `alpha == 0` 显式直接返回原 state，不先投影，不调用新 evaluate。对实际形成的框架，还保存完整原点导数读回、与 $v$ 的差、对应原 $J$ 作用和 full3 斜率；它们是诚实的有限精度诊断，不设额外门。

条件性的负导数只说明精确局部曲线上充分小的步长满足原 Armijo；它不保证有限二十档中一定有一档，不保证内层收敛或有限字长能分辨下降。此次也不证明旧残差近驻点或无根。

## 5. 有界二维校正：完整新 J，实际余量不清零

每个外层 $\alpha=2^{-j}$，$j=0,\ldots,19$：

1. 先按原 binary64形成直接 seed $p+\alpha v$，调用一次原 evaluate。如果该 seed 已失原域或原评价异常，这个 $\alpha$ 失败。本轮**不做沿曲线细分绕过非法 seed**；此算法范围不构成不存在合法弯曲路径的结论。
2. 保持当前外点的 $S,N$ 和两条正行尺度 $D$。对实际误差 $e=c(q)-[c(p)+\alpha Cv]$，内层目标仅为 $\Phi=\frac12\|D^{-1}e\|_2^2$。
3. 每次校正重新调用原完整3×3参数 Jacobian，形成完整 $M=Dc(q)SN$，用完整带主元2×2 QR解 $M\,\delta w=-e$。求解的行平衡只影响线性计算，不改变外层原三式权重。没有 $J_{33}$ 除法、法方程或秩截断。
4. 对法向坐标更新作至多二十档 $2^{-k}$ 原评价，按 $\Phi$ 的实际斜率和系数0.2回溯。每个内层实际点、原三式、真实 full3目标、两式余量、原域错误及完整新 J进入临时原 status/原评价事件账。
5. 至多十二个内层 Newton迭代。`normal_target_tolerance=1e-8` 是**内层计算停止目标**：只检查两条实际原单位式的目标误差。未达到它、二十内层回溯全拒、正常有限模型求解失败或参数词不再改变，均保留最后实际有限点供外层试验。它们不会单独禁止原 full3 Armijo，也不将实际第三式重置为0。

内层目标与外层原 $W$ 不同。内层的某次“accepted”只表示法向目标改善，不算原参数点接受。只有下一节的真实外层判断才更新主状态。

本轮相对信赖半径限制的是**预测方向** $S^{-1}v$。校正后实际位移和切向泄漏另存；不声称校正点自动仍在该球内，也不增加一个新的几何接受条件。原完整域与 full3目标负责裁决该真实点。

## 6. 外层门和全部原终检

校正后的真实三式 $F(q)$进入完全原样的未加权目标：

$$
W(q)=\tfrac12\|F(q)\|_2^2,
\qquad
W(q)\le W(p)+0.2\alpha\,r^TJv.
$$

原有限域检查、有限严格负预测斜率和原 full3充分下降均保留。目标右端使用原起点和原完整方向斜率；不能把校正点当新的 $\alpha=0$ 起点，不能改为只看 $F_1$ 或内层 $\Phi$，不能把目标 $c(p)+\alpha Cv$ 当成实际 $c(q)$。

每个外 trial 的主摘要表保留实际三个参数、三个原方程、$W$、原 Armijo界、两条目标、两条实际校正剩余误差、内层停止原因、评价/J次数、原域失败数和异常。每个方向保存完整原 $J$、原斜率和形成路径的起点导数读回。

仍最多八个**完整方向尝试**，包括全部回溯被拒的方向。一个方向二十外 trial全拒，只把半径除4，原接受参数/state/J不动；下一次重新形成完整预测方向与法向框架。已接受点按112原规则调整半径，下一外步鲜算完整 J。半径变化不计作接受。

最终 `description`（完整新 J、数值奇异值、原实差分）、原 scalar-domain160位/深度14、原完整圆参考与FFT切向检查的源码整段与112相同。原单位方程迭代停止阈值仍 $10^{-8}$，完整112行候选标志仍按自己的原真实 residual检查；两者不混用。高109可逆、非零幅度分支、当前非零 H 的原 native/finalJ/audit、全BVP以及本课题全部闭面完成门都没有由低三试验自动付清。

## 7. 预算、错误保全与小报告

本轮外预算是8方向×20档。每档校正预算是12次×20档，另有一次直接 seed。因此只计 seed与法向回溯评价的显式上界为

$$
8\cdot20\cdot(1+12\cdot20)=38560.
$$

另至多 $8\cdot20\cdot12=1920$ 次内层完整原参数 J调用；这些调用内部的原复步长评价、外层 freshJ、初末 description/FD、圆参考及原终检不包含在前一计数中。原事件账给实际尝试/返回次数，不用预算上界冒已执行数。

workflow科学 step75分钟、compute job90分钟，单任务不超过公开Actions限制。超时或规则变化是资源/指令中断，保原 partial状态和实际 step outcome；不能写成原二十档全部拒绝、无根或科学正常完成。源码最终异常保 traceback，已形成方向不会因后续框架失败被抹去。

只读 scalar reader不计算范数、差分、矩阵动作或新残差。通过 `GITHUB_OUTPUT`把至多90,000字节JSON交给独立 report job，标记为 `BEGIN_VISIBLE114_SCALAR_SUMMARY` / `END_VISIBLE114_SCALAR_SUMMARY`，另印完整 bytes/SHA。先保所有原外 trial核心表、初末原检查和真实flags。空间不足时仅省略重复因子/seed附表/源闭包副本/可选清单，记录被省字段的原序列化 bytes/SHA。若仍超限，明确输出元数据超限及原 status身份，不冒科学完成；每个外 trial另已在 compute stdout逐行打印真实值。

原 status、事件账、圆参考和区间结果均只存临时目录，完成小读出后清理。无 `upload-artifact`、无 Release、无 raw入库。root只保存源码、参数、真实run/输出SHA和紧凑结论。

## 8. 唯一运行接口及规矩同步

新workflow：`.github/workflows/visible-larger-public-small-core-full3-curved-normal.yml`。仅push `topics/visible-flex-larger-amplitude/computations/public-small-core-full3-curved-normal-request.json`触发；独立 concurrency，不取消旧运行。完整命令由请求字段组装：

```text
python geometry_20261115_small_core_full3_curved_normal_recipe.py
  --accepted ORIGINAL_ACCEPTED --prepared ORIGINAL_PREPARED
  --tail-anchor ORIGINAL_TRUE112_ZERO_ANCHOR --tail-config ORIGINAL_CONFIG
  --parameter-recipe actual112-explicit-parameter-recipe.json
  --parameter-recipe-sha256 80b8b209819a548a263b2fca1769c27f2d4e195b160a9064c1872e2c3778f1e1
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20
  --normal-iterations 12 --normal-backtracks 20 --normal-target-tolerance 1e-8
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14
  --out NEW_TEMPORARY_OUTPUT
```

运行环境保持 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、BLAS单线程，原78个公开数值来源恢复函数不变。固定science checkout不被规则镜像修改。

原规则监控器 `3b8b6dd5…`在单独镜像先真实pull/rebase，并每2700秒再次同步；当前已读根README `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`、题README `bff8aea253a9e6a7a4fac28d810ac454c5499fec`显式回填其 `BASELINES`，监控算法不变。规则真变化须打印diff并停止子进程；普通网络错误如实保留同步失败。H必须已有唯一规则行且不超过10KB，不能绕过原检查。Git `merge.stat=false`，关闭gc/maintenance，令牌只在process环境/CLI，未写文件。

## 9. 已完成静态工作及尚未声称之事

两新Python仅AST/compile；8段bash经`bash -n`，5个inline Python经AST/compile；77+2来源与17→18闭包、实际112 recipe原字节来源、独立路径和原四输入绑定已静态核对。完整方向/半径函数AST及原初始setup/全部最终诊断正文保留。

为解决具体90KB运输风险，使用**已存112的JSON字面量**仅做了可丢弃的160行序列化尺寸样例；没有数值模块导入或科学函数执行，不能冒114科学结果。该样例及其原科学字面值未留作新数据；运行期真实大小仍由读者诚实报告。

源码/reader/workflow/request相对112的差异可从已提交源直接重得；静态回执仅在临时目录，不按新数据提交Git或Release。静态检查不是派发或数学接受的新门。本文件没有未来run编号，没有预填新结果，也没有改变已发布112或其他冻结源。
