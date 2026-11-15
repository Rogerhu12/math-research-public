# 同原选集的自然 u 来源与小 Schur 系列：执行接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

状态：以下是从已完成的原第一连接继续的可执行入口及来源证明。源码尚未在本次环境编译或执行；不得把请求的八阶或任何 Smith 长度预记成完成。本地执行环境不可用，实际编译与数学由同一已授权 Actions session 运行。这里只提交小文本源码与接口，所有可重建数组均留在 job 临时目录。

## 1. 已完成输入与本次新工作

已付的原第一连接实绩为 run43679903558 的
`selected-natural-first-connection-f31-stdlib`：
原自然参数一阶产品全部 $4367\times36$ 坐标已保留；同选 $36$ 维余空间连接及全输出 $49$ 维连接均秩三。完整三十三维常项核已经给出，但尚未恢复其真正的一阶原来源校正。

本次复用这一 $R_1$ 与同一个原常数图核 $K_0$，不重算原参数一阶产品。新的工作是：

1. 按原常数单位块，将自然 $u$ 来源递推到请求的有限阶；
2. 每阶完整乘回原 $4367$ 个输出，核同选 $4318$ 个单位输出为零；
3. 保同选的全部 $36$ 个补输出与额外 $13$ 个原输出；
4. 用已付 $33$ 维常项核实际形成第一校正并核其全部原输出为零；
5. 只在新的 $36\times36$ 有限系列上作单位 Schur 消元，报告已经付到的模 $31$ Smith 指数或准确未完成下界。

这里不新增 Dixon 位，不再消元原大矩阵，也不把有限域数据解释成特征零参数长度。

## 2. 固定单位行、单位列及真实来源

记同一原矩阵为

$$
A^h(u)=\sum_{i=0}^{10}A_i u^i,\qquad
B(u)=A^h(u)_{I,J}.
$$

原 $J$ 的 $4354$ 个来源分为 $4318$ 个单位来源与 $36$ 个固定自由来源。原 $I$ 同样分为 $4318$ 个单位输出与 $36$ 个补输出。全部编号由既有 $3333$ 预基和 $985$ 选列像的真实来源操作记录恢复。

令 $E$ 嵌入单位来源，$F$ 嵌入自由来源，$P$ 取单位输出。已付单位块为

$$
U_0=P A_0E,\qquad
W=EU_0^{-1}P.
$$

$W$ 是原来源的真实部分逆，不是新选的有限商代表。其实现只重放已经付清的：

- $782976$ 条 forward 操作；
- $1010703$ 条 backward 操作；
- $462972$ 条 $985$ 像来源操作。

它对一个新右端给出全部 $6188$ 个原来源系数，同时保原 $36$ 个自由坐标为零。操作记录及输入的实际 SHA256 均在入口锁定；不会将模 $31$ 系数解释成有理系数。

## 3. 唯一自由坐标归一的自然来源递推

取已付 $X_0=K_0$。逐阶定义

$$
R_k=\sum_{i=1}^{\min(k,10)}A_iX_{k-i},
\qquad
X_k=-W R_k\quad(k\ge1).
\tag{3.1}
$$

每个 $X_k$ 的原支撑都在 $J$，而 $36$ 个自由坐标在 $k\ge1$ 时严格全零。对每一完成阶，程序实际核验

$$
P(A_0X_k+R_k)=0,
\tag{3.2}
$$

并保存完整原残量

$$
E_k=A_0X_k+R_k\in\mathbb F_{31}^{4367\times36}.
\tag{3.3}
$$

未选的十三个原输出也保留在 (3.3)，不因同选余空间只有三十六维而删除。

来源递推有一个准确的形式解释：

$$
X(u)=F-E\,[P A^h(u)E]^{-1}P A^h(u)F.
\tag{3.4}
$$

因为 $P A_0E$ 是已付单位块，(3.4) 在
$\mathbb F_{31}[[u]]$ 中唯一存在，且自由来源坐标恒为 $I_{36}$。逐系数展开就是 (3.1)。因此从原 $I$ 的补输出取出的系列

$$
S(u)=Q_I A^h(u)X(u)
$$

是同一原方阵 $B(u)$ 的真实 Schur 余块。按固定行列重排，

$$
\det B(u)=\pm\det(P A^h(u)E)\det S(u),
$$

首因子在模 $31$ 下为 $u$ 单位。所以 $S$ 的完整 Smith 长度如果算出，就等于原同一子式的模 $31$ 无穷远阶。这一步没有更换原 $I,J$。

## 4. 与本次已经完成的第一连接完整接合

旧来源消元记录留下的三十六个补输出，未必就是前一小余空间计算的坐标基。入口由已付 $585\times29$ 左核及删行后的 $585\times26$ 左核，构造真实 $36\times36$ 基变换 $T$，实际要求

$$
\operatorname{rank}T=36,\qquad TS_1=\beta_I^{(31)}.
$$

全部 $1296$ 个坐标逐项核对。对完整原残量 $E_1$，再检查全 $49$ 维余空间的 $1764$ 个坐标恰等于前一实际连接，原额外输出未丢。

设前一已付完整常项核为 $H\in\mathbb F_{31}^{36\times33}$。入口实际保存

$$
X_1H\in\mathbb F_{31}^{6188\times33}
$$

并核

$$
E_1H=0_{4367\times33}.
$$

只有通过这个完整原乘回，才置
$all33CompleteOriginalFirstCorrectionsVerified=true$。这给出了之前只存在、尚未构造的三十三条原第一校正。

## 5. 有限系列的严格 Smith 信息

对已知 $S_0,\ldots,S_N$，只在大小至多三十六的矩阵中操作。

每层按常数矩阵的真实非零子式选单位行列，写成

$$
M(u)=
\begin{pmatrix}U(u)&V(u)\\W(u)&Z(u)\end{pmatrix}.
$$

程序递推 $U^{-1}$ 到当前全部可用精度，并逐系数检查
$U U^{-1}=I$。形成

$$
Z-WU^{-1}V,
$$

核其常数项准确为零后才除以 $u$。常数单位秩给出该层确定的 Smith 指数，剩余块继续同样步骤。

如果三十六个指数全确定，回执给出其和与
$completeSelectedInfinitySmithLengthComputed=true$。
若已知精度用完，则仅记录完整已确定指数及未定指数的严格下界；不会把某个截断后零块记为形式零块，也不会把本轮执行完成等同 Smith 长度完成。

无论哪一种分支，

- $characteristicZeroInfinityOrderComputed=false$；
- $leadingUnitProved=false$。

参数子式的首个非零系数是 $31$ 单位，仍需同一特征零长度与有限域长度的一致证据或等价原整系数证明。

## 6. 文件、CLI 与明确预算

本入口由同名前缀的 C++ 来源递推程序和 Python 执行程序组成。实际命令如下：

~~~
python -B {scripts}/2026-11-15-r150-selected-natural-u-schur-source-jets-runner-789f.py
  --native-model {native_model}
  --point-model {selected_model}
  --selected-model {work}/koszul-exact-sparse-preparation/exact-original-koszul-outside-model.json.gz
  --unit-profile {work}/seven-original-exact-rational/seven-original-unit-row-profile.json
  --kernel36 {bockstein_dir}/actual-original-kernel36.bin
  --source-dag {dixon_dir}/actual-selected-image-source-dag.bin.gz
  --repo-notes {repo_dir}
  --first-dir {work}/selected-natural-first-connection-f31
  --out {work}/selected-natural-u-schur
  --maximum-degree 8
  --seconds 60
  --memory-mib 512
  --compile-seconds 30
~~~

`--repo-notes` 参数指旧恢复输入的 notes 根目录；其中包含旧 forward/backward 两份压缩记录及需要时的 bitplane 头文件。它不是一次新的 Git 克隆。入口两个通用头文件优先从 `scripts` 取，再从此目录补入：

~~~
2026-11-15-r150-saturated-global-common-789f.hpp
2026-11-14-r150-f31-bitplane-789f.hpp
~~~

只需 $g++$、标准 C++17、Python 标准库与已经安装的 python-flint；不依赖 NumPy、GMP 或原生 FLINT 开发头。一次编译上限三十秒，实际数学共享六十秒，每进程 $512$ MiB。源码允许显式请求有限更高阶，但不得在未改变任务参数时自行无界延长。

编译时间单独记录；同一已编译二进制经 SHA 与源码绑定一致后恢复时直接复用。数学共享时钟包括输入核验、来源操作重放、新原乘回及小系列后处理。native 在完整阶边界保存，并在共享余时不足时正常退出 $75$；外层若需要发送终止信号，最多给五秒保存宽限并照实记录实际耗时。

## 7. 真实恢复与临时文件

语义绑定包含全部输入字节、执行源码及头文件 SHA、固定原字典与归一规则；不含恢复目录绝对路径、请求最高阶或时长。因此同一数学源可在原完成阶后增加精度或预算。

每个完整阶 $k$ 保存三份 canonical field 数组：

~~~
natural-source-k.bin       6188 × 36
natural-schur-k.bin          36 × 36
natural-residual-k.bin     4367 × 36
~~~

它们分别采用 `R150US31`、`R150UJ31`、`R150UR31` magic，带模数、阶数、形状及同一 $64$ 字符绑定。三份全数组写完后，才原子更新完整阶游标。Python 外层同时保存完整文件 SHA 清单；恢复逐一核实后跳过已完成来源阶，不能把一个日志中的来源行数当成检查点。

已付常数来源操作可以再次读取与重放以建立部分逆；此前已完成的自然来源系数与原乘回结果不会再求解。未完成阶不改变已提交游标。第一连接的旧产品只从真实缓存读取。

主回执为：

~~~
selected-natural-u-schur-pipeline-receipt.json
~~~

主要完成字段：

- `completedNaturalDegree`、`previouslyCompletedNaturalDegree`；
- `all4354SelectedJetIdentitiesVerified`；
- `all4367OriginalResidualCoordinatesRetained`；
- `all36FreeSourceCoordinatesVerified`；
- `all33CompleteOriginalFirstCorrectionsVerified`；
- `all4367FirstCorrectedProductsZero`；
- `completeSelectedInfinitySmithLengthComputed`；
- `selectedMinorInfinityOrderModulo31`，仅长度完整时有值；
- `selectedMinorInfinityOrderModulo31LowerBound`。

实际小 Smith 分层、单位行列、未定指数范围、基变换、源码与临时文件哈希均放进 `parameters`，保证现有 session 的小回执保存器保全这些数学数据。全部重建数组留在 session 临时目录，不经工具二进制传输，不进入 Git 或 Release。
