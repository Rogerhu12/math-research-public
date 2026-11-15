# Request75：原R259小核心备用诊断的首次执行草稿

分类：既有冻结科学源码的独立公开Actions接线及静态检查。  
作者：ChatGPT（amplitude，AI辅助；geometry补核原Arb运行时与scalar依赖）。  
日期：2026-11-15 UTC。

## 1. 执行对象与结论范围

本请求只执行已存在的
[R259条件推导](../results/R259-small-core-homotopy-and-resonance-conditions.md)
及其[原诊断接口](2026-11-14-small-core-resonance-diagnostic-interface.md)
对应的冻结入口`geometry_20261114_small_core_resonance.py`，25799B，SHA
`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。
没有修改该科学源码，也没有复制另一个同伦求解器。它与正在执行的
74前缀和73原生尾任务相互独立，不使用这两轮尚未完成的输出。

第一次采用原默认控制`p=(0,0,0)`及零次Newton候选搜索。
诊断用原699网格构造圆子空间的collocation参考，再求低三单位模式的
原二维传输链，读取真正完成的全部112×112零高度尾slope Jacobian。
它记录原有限方程/FFT的回读、三参数响应、实际全scalar区间边界；
不求非零振幅BVP，不生成已接受的小幅parent，也不完成本题大幅目标。

已全文静态阅读R259、科学入口和原接口，未发现需要修改科学源码才能
执行该默认诊断的具体阻断。数值可逆性、域、区间细分和实际耗时仍由
首次Actions给出；不存在从静态阅读推断成功的结论。

## 2. 完整尾耦合没有被删去

R259令原返回的独立径向速度为$\nu$、$q=\nu/a$，实际源圆满足
$R'=qR$，$Z'=\sqrt{1-(qR)^2}$。只有另证$\nu=a'$且初值相同时才可
把$R$等同于$a$。本入口遵循原circle collocation递推，不把有限Gauss
半径的独立`ap/app`字段冒成其真导数，也不使用`app`代替该证明。

完整尾首阶矩阵的条件仍是

$$
L(p)=\operatorname{diag}(H'_j(S;p))
 -\gamma J_0\operatorname{diag}(\epsilon_h H_j(S;p)),\qquad
L(p_0)\binom{A}{d}=0.
$$

若$J_0$有非对角项，完整高自由core消元应当涉及
$L_{LL}-L_{LH}L_{HH}^{-1}L_{HL}$。冻结入口只传输低三模式，真实
完整112行右残差均输出，同时明确
`high_free_core_Schur_elimination_computed=False`及高模非共振未证明。
不能把它的低三方程零、一个较小高行泄漏或一次数值SVD当作完成了
完整Schur条件。既不阈值清除非对角项，也不用`ready.linearD`替换真J。

原可选Newton搜索仅在所读完整J严格对角且三个低目标均非零时允许运行；
本请求`newton_steps=0`，不依赖预先假定对角性，也不偷偷启动搜索。
即使实际所读J逐项对角，高模式非共振和区间transversality仍未支付。
直线缩幅的三重首阶条件不被解释成所有非直线路径的强制条件。

原完整scalar的Arb检查针对同一声明实表达式中的$a>0$、$|\nu|<1$。
它不包办普通binary64求值误差、$\nu=a'$、分片C²接缝或实际$R$的
全区间Frenet条件。原circle还另经全部节点/中点/RMS和九个完整FFT
方向检查读回；这些实际结果仍需保存和解释。

## 3. 四个固定实际输入

全部路径均在本公开仓库，SHA与原trust入口`EXPECTED`逐项相同：

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| accepted96 | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| 原699-node prepared112 | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 真T112零高度完整响应/J | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原T112配置 | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

它们分别位于：

- `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz`；
- `notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz`；
- `notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`；
- `notes/public-actions-43588155190-1-prepare112/T112-config.json`。

路径均以`topics/visible-flex-larger-amplitude/`为前缀。请求保存完整
路径、size及SHA；实际Actions在执行前亲读全部字节核验。这里的size
取自已有Git对象元数据，SHA取自冻结入口，静态接线不冒称再次数值验收。
原prepared仅是数学定义和网格来源，仍不被标记为已接受的完整BVP。

## 4. 依赖与原预算

沿用Python3.12.14、NumPy2.3.5、SciPy1.17.0；Arb依赖采用原
operatorcheck lane已经明确使用的`python-flint==0.9.0`。没有Node安装
或新native进程。`geometry_20261114_direct_operator_cell.py`由原
`scalar_domain`延迟加载，`ScalarExpression`另用原`flint.arb_series`。

`prepare_public_source`仍从本仓当前HEAD恢复原manifest绑定的78件
公开数值源并逐件核SHA。另一个不同的来源集合是`computations/HERE`
中的完整scalar十源：r225 fixed profile、full scalar、prefix controls、
lifted modes、same metric、strong connector、三个alternative neck源
及strong_angle_boost。它们由`checked_original_sources`核原SHA；不能
以恢复public78替代这十个HERE文件。工作流保留完整computations窄检出，
这两组依赖都具备。

请求钉住68个文件：保守静态import及字面源码依赖闭包、scalar依赖、
原source-dependencies manifest和publisher。其中有默认诊断不执行的
辅助文件；这是源码身份范围，不声称68份均被运行。完整pin及大小见
`request75-static-check.json`。

本次原参数为：

```text
parameters = (0,0,0)
newton_steps = 0
backtracks = 12
candidate_resonance_tolerance = 1e-8
interval_bits = 160
interval_depth = 14
M = T = 112, physical FFT N = 2048
material/boundary angles = 4096, original RHS workers = 1
```

候选阈值只是原诊断读数，不是新BVP接受门。工程上job限60分钟、科学
step限45分钟，给原件上传与发布留时间；这些是首次执行的资源上限，
不是已测耗时，也不放宽任何数学条件。若超时，记录超时和既有部分
输出，不能称诊断已经完成。

## 5. 唯一工作流、请求与命令

草稿仅位于`/tmp/visible-larger-request75/`，未修改仓库文件或分支。

| 草稿 | 字节数 | SHA256 |
|---|---:|---|
| `visible-larger-public-small-core-resonance.yml` | 10771 | `891e79c2f917e5679d07d5bbb7b39ee909e1b240c1a7dffb31e60ea61c5b8822` |
| `public-small-core-resonance-request.json` | 11542 | `5359a2d34f17a6c828ffaed020734757bd35e49ca7bd87364fed0519edc15522` |
| `root_20261114_publish_actions.py` | 14455 | `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` |
| `root_20261114_publish_actions.py.diff` | 2685 | `d0e8563765dc90a8f7d98b91ee8be7f2b1fbf669572d1ba07abe30e6e31678c1` |
| `request75-static-check.json` | 14145 | `7be67c0bb0836af883ffbc709ba9f4c31d5b62b4bcbfb9eca51d6db828c1c903` |

工作流目标为`.github/workflows/visible-larger-public-small-core-resonance.yml`。
唯一push trigger指向
`topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json`。
请求文件必须落在这个computations路径。没有额外workflow_dispatch或
第二次触发路径；科学入口只调用一次。

publisher草稿仅在原5a0216d0版允许的lane元组中增加
`smallcoreresonance`；其余AST一致。普通pull/rebase、双README核验、
失败保全、Git文件限制和HANDOFF规则行处理均保留。root负责合入及
实际推送；该非科学路由变化不改冻结R259源码。

工作流从明确request构造参数列表，等价CLI为：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_small_core_resonance.py" \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --parameters 0 0 0 --newton-steps 0 --backtracks 12 \
  --candidate-resonance-tolerance 1e-8 \
  --interval-bits 160 --interval-depth 14 \
  --out "$VISIBLE_OUT/resonance"
```

在调用前保存实际source commit、原requestSHA、完整输入和源身份，
以及确切argv。输出目录只预建父目录，不预填科学入口要求为空的
`resonance/`。原入口报错、不可逆、失域和未解析区间均按其原行为记录。

## 6. 输出与首次读回责任

原输出仍是`resonance-status.json`、`complete-scalar-domain.json.gz`
及在原完整域有效时生成的`circle-reference.json.gz`，另有可能的
`circle-original-domain.json`。最后一份circle参考保留完整均值和
699×453场/RHS，但目标明确为零、`success=False`，不冒非零parent。

工作流的always只读step复制已存status字段为小摘要；不重算任何
残差、范数、FD或区间。如果完整摘要达到90000字节，则完整派生文本
留在artifact，公开摘要保phase/完成标记/错误/原status身份并给引用。
原科学进程若未产status，也明确报告其缺失，保留原日志。上传使用
`visible-mainline-smallcoreresonance-<run>-<attempt>`，包括全部成功
和失败输出；发布结果在同lane目录，普通文件限额由原publisher处理。

静态回执核过68个pin、7段bash语法、4段内联Python AST和唯一trigger；
这些不是科学运行。首次真实回执要分别读取完整J的对角/非对角事实、
全部112行右残差、高块未付范围、低三响应、scalar区间、完整circle
域/残差及其状态。无论哪项较小，都不能替代原全field、真非零尾、
FD、RMS、BC和最终fresh audit，更不能停在小幅作为本题最终解。
