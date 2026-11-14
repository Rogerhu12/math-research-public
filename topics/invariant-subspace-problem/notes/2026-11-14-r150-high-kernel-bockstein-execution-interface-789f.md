# R150：一次全200高核 Bockstein 的300秒执行接口（已编译，尚未运行）

本条只登记可执行接口与准确输入，不是新的 Bockstein 计算结果。
三个新 C++ 已分别在30秒/512MiB限制下实际编译成功；两个新 Python 已通过语法解析。
实际准备记录见 `2026-11-14-r150-high-kernel-bockstein-source-preparation-789f.json`。

## 1. 唯一统一入口

```text
python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-high-kernel-bockstein-runner-789f.py \
  --recovery-root RECOVERY_DIR \
  --out OUTPUT_DIR \
  --seconds 300 --memory-mib 512 --compile-seconds 30
```

输入从既有 run `43597823809`、artifact `14114364261` 解压恢复。
程序只查找并验证该目录里的原文件，不重建旧正常形或旧完整图。
Python 阶段使用既有 `python-flint` 接口；当前开发环境版本0.9.0 / FLINT3.6.0。

编译先于数学时钟，三个编译进程分别有30秒、512MiB address-space界。
输入验证及编译完成后启动唯一300秒 deadline；三个 native 阶段及最终 Python 必要判据共享它。
每个子进程的 `timeout` 等于当时剩余时长，TERM后保留10秒强制结束余量；每个进程均限512MiB。
数学阶段之间的输出校验也计入 deadline。末尾恢复文件清单与 artifact 保存另记，不追加数学计算。

`--prepare-only` 仅验证输入和编译，输出明确 `prepared-no-mathematics-executed`。
正式任务不使用此选项。

## 2. 六个固定 artifact 输入

| 名称 | SHA256 |
|---|---|
| `reweighted-basis.bin` | `bb2b36e3b083bf3b66e692f3fdef603941ef3c9c0a1b8fa7a74fad6722fb56ce` |
| `normal-form-input.txt` | `291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6` |
| `nf-normal-forms.bin` | `eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840` |
| `nf-reduction.bin` | `e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b` |
| `nf-forward.bin` | `66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e` |
| `nf-backward.bin` | `cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f` |

通常分别位于 `isp-r150-reweighted-graph-work/t96/` 与 `isp-r150-native-nf/`。
程序接受模型在 CI 中的另一文件名 `native-normal-form-input.txt`，但 SHA 必须完全相同。

原 integer mod961 模型、完整315维torsion状态、真实首轮余从已经落库的 notes 读取，
同样按未压缩 SHA 验证。原模型的17条方程、primitive行尺度及所有原行编号不变。

## 3. 四个实际阶段的数学范围

### 阶段一：原6188行的完整核与整除身份

从完整 T96 图读取且只读取成本80、81、85的200个实际核行，数量为160、38、2。
每列记录原 graph row、来源主分量、成本、原2195 source index与原6188行号。
全部200列打包在7个32位 word内，同一次重放原 H、backward、forward 记录，恢复

\[
\widehat\kappa_j=(\text{原常预基补偿},K_j)
\]

的完整原 primitive 来源。所有系数取规范 mod31 数字。
然后只用原整数方程 mod961 做全输出卷积，检查每个原系数都被31整除，并计算

\[
b_j=\frac{A\widehat\kappa_j}{31}\pmod{31}.
\]

注意此处符号为正，后续需要解 \(\beta(k)=[r_1]\)。
同时逐列核所有原来源和输出的成本不超过该列实际80/81/85标签。
不是只检查正常形投影后为零。

### 阶段二：同一原常预基正常形

对200个完整原 \(b_j\) 作原3333常预基正常形。
新 forward/backward 二进制必须与旧哈希逐字节相同。
完整正常形和原来源 trace 都保存，列标签使用真实 kernel 主分量（大于1034），
不会伪装成原九目标2至10。

### 阶段三：完整 image 商证书

使用同一个实际1021行 image GB，逐列保存 G 商和不可约余，并从保存的商重新累加核验

\[
GQ_j+\rho_j=b_j
\]

在全部1034分量、全部200列、参数次数至85的身份。
这一阶段只计算无限 polynomial 商。

### 阶段四：全315维必要判据

与已保存的完整状态核对全部标准坐标字典，再对200个余核505条观测全部为零，
并以 K 重构全部820个正常形坐标。
对每个高核列保留所有成本不超过85的 s 移位，恰得1152列。
在完整315维torsion内检验这1152列是否同时包含原九个首轮余。

保存完整315×1152矩阵、九个真实右端、每一移位的原源标签、系数RREF及一个实际解（若兼容）。
不兼容时给出对全部1152列都为零、对一个真实右端为1的显式对偶证书。

**无论必要判据通过与否，均写 `finite_budget_verified=false`。**
通过不意味着有限1658维 cokernel 通过：还须支付正常形来源的 cost>85 系数。
本任务也不把 mod961 可解与特征零原理想包含混同。

## 4. 输出与恢复

可以回存仓库的小结果集中在 `OUTPUT_DIR/results/`：

- `bockstein-pipeline-receipt.json`：实际总状态、各阶段退出码/marker、全部来源与输入SHA、时限、必要判据及 `finite_budget_verified=false`。
- `original-bockstein-metadata.json`：全原核/31整除身份与200列原标签。
- `image-bockstein-metadata.json`：全部 image 商/余身份。
- `high-kernel-infinite-quotient-result.json`：完整315维必要判据与可能的显式dual。
- `complete-infinite-quotient-system.bin.gz`、`all200-torsion-columns.bin.gz`：完整小矩阵。
- 每阶段实际日志、编译日志及 `recovery-manifest.json`。

完整原核、原整除右端、正常形与全部原来源trace、完整G商/余集中在
`OUTPUT_DIR/recovery/`。这些大文件应与小结果一起在单次 Actions recovery artifact 中保全；
它们不直接作为超大仓库文件提交。清单给出准确大小和SHA，超时也保存已存在的真实部分，
并标明 `completeMathematicalRun=false`，不能把部分文件误作完整证书。

两个新原式二进制格式：

- `R150KK31`：prime31、原行6188、列200、预算85；200列标签；逐原行保原方程号、m乘子、成本及200个升幂系数。
- `R150BK31`：prime31、预算85、列200、原分量4367、加权输出219032；同一200列标签；逐原m分量保其完整参数系数。

正常形与 image 余沿用 `R150NF31`，ns=0、nt=200，target字段明确是真实 kernel head label。
`R150IQ31` 保存同一实际G首一化的完整200列商。
所有范数/位平面只是精确域算术的实现；数学判断最终依赖原式全系数身份与真实来源字典。

## 5. 新源码

- `2026-11-14-r150-high-kernel-bockstein-original-789f.cpp`
- `2026-11-14-r150-high-kernel-bockstein-normal-form-789f.cpp`
- `2026-11-14-r150-high-kernel-bockstein-image-789f.cpp`
- `2026-11-14-r150-high-kernel-bockstein-torsion-789f.py`
- `2026-11-14-r150-high-kernel-bockstein-runner-789f.py`

复用已冻结 `2026-11-14-r150-f31-bitplane-789f.hpp` 与
`2026-11-14-r150-torsion-characteristic-789f.py` 的原状态 reader。
上述三 native 已编译、两 Python 已作语法解析；尚未启动新数学运行。
