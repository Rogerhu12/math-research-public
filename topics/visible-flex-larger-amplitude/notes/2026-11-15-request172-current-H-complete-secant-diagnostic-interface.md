# Request 172：真实 current-H 原十试步的完整 R360 分解与公开执行接口

作者：AI。状态：独立源码与显式实验配方；本文件不登记未来运行、实际新状态、数值分解结果或成功证书。

## 1. 本次实验支付什么

本次从 Request 145 同一六参数配方、同一四数学输入和原冻结尾源重新形成当前完整物理问题及 $H_\star$，沿原完整高度路径请求同一 live native worker。对每个实际计算出完整 R273 方向并进入原试步循环的迭代，新增一次同状态 noJ 基点评价，保存原十档实际形成的完整状态和返回残差；原十档全部拒绝后，再显式尝试三个较小步长，作为诊断而不参与原接受。新的准确算术消费者逐行形成 [R360](../results/R360-current-H-full-residual-secant-and-formation-decomposition.md) 的分解。

其目的是区分保存 withJ 残差与另一次 noJ 基点的差、实际浮点状态形成差、以及剩余有限评价与保存线性模型之差。它不预判其中哪项主导，不将一次分解解释为全局误差下界，也不将诊断换成新的 Newton 接受门。

这些额外 noJ 调用是**新的科学调用**，准确整数分解也是新的科学计算。观察器虽不回写原状态和接受变量，但原内部缓存、统计和初猜路径对额外调用是否完全无影响没有在此证明；额外耗时更不为零。因此，本次不声称逐词复现 Request 145 的后续轨迹。R360 是任意实际向量的准确代数恒等式，仍可用于本次实际形成的向量。若进一步将余项解释为某个固定准确映射的 Taylor 余项，必须另外支付该映射、导数和状态条件，不能由本接口自动推出。

原 Request 145 实际失败及四次接受只作为重生本实验的动机，见 [R343 原结论](../results/R343-actual145-current-H-R273-and-positive-height-line-search-stop.md)。没有导入其失败状态、保存 J、方向、H 字词或 checkpoint。本次也不使用新声明 C、射影 Robin 或 168/169 的未来结果；对象仍是原 145 冻结数值尾及原六控制物理问题。

## 2. 冻结文件与完整来源

下表 SHA256 均针对真实完整 UTF‑8 文件字节，包括文件末 LF。九份新源码独立命名；原 145 的 115 个源 pin 逐项保留，总计 124，原数学源不覆写。

| 角色 | 文件 | 字节 | SHA256 |
|---|---|---:|---|
| system | [exact_20261115_current_H_secant576_system.py](../computations/exact_20261115_current_H_secant576_system.py) | 28933 | 9933e75ab4a07e920f8784e36eae93345c3735cf11b5a90f86d0eaef3073f25e |
| qr | [exact_20261115_current_H_secant576_chain_qr.py](../computations/exact_20261115_current_H_secant576_chain_qr.py) | 21973 | 0cc45afa1cec2f73d53e370cf8be7cd75a7ba9a1b6025da4724e2b2d0bde9036 |
| hook | [geometry_20261115_current_H_secant_tail_client_hook.mjs](../computations/geometry_20261115_current_H_secant_tail_client_hook.mjs) | 65124 | 3f9feb2b0897f2da555780c74f5ca46fc76eb59e2e904d958a7195eb18e618ac |
| client | [geometry_20261115_current_H_secant_tail_client.py](../computations/geometry_20261115_current_H_secant_tail_client.py) | 20766 | d76785f533de468b4b7eebbad160120fdc85be2138b4281388fc1f81269d2ad8 |
| consumer | [exact_20261115_current_H_secant_decomposition.py](../computations/exact_20261115_current_H_secant_decomposition.py) | 34129 | 0eef38715c408048021c5a2a3b9402ca6970ca3759ee9e1b9959c311e19c36a3 |
| height | [geometry_20261115_current_H_secant_height_path.py](../computations/geometry_20261115_current_H_secant_height_path.py) | 23764 | b1a202c543ae9d25288ce8f28e164d33517b586bd04332a2cd34fc3f5819753e |
| driver | [geometry_20261115_six_control_current_H_secant_full112.py](../computations/geometry_20261115_six_control_current_H_secant_full112.py) | 47148 | 7a6b9d0784e358b2f38bfbcdaddeabf32701f36b66b34769f7d51543bff0b5f1 |
| launch | [root_20261115_current_H_secant_run.py](../computations/root_20261115_current_H_secant_run.py) | 13807 | 442ab034d513285e054356fe5cc499aca544d303e51888aac0461f6c3bc02480 |
| reader | [root_20261115_current_H_secant_scalar_readout.py](../computations/root_20261115_current_H_secant_scalar_readout.py) | 37271 | 0cb0dea52ef00bb924afcd47145ab49c627efec36ee59c6c9e3d8710dfcbcc11 |

运行件：

| 角色 | 文件 | 字节 | SHA256 |
|---|---|---:|---|
| recipe | [actual119-batch3-current-H-secant172-lambda0p001-recipe.json](../computations/actual119-batch3-current-H-secant172-lambda0p001-recipe.json) | 8030 | 52841cec83b89d34e882e6db4731eec89e77bf6fcbf2e617856a77f6b4eb0e26 |
| request | [public-six-control-current-H-secant-request.json](../computations/public-six-control-current-H-secant-request.json) | 32271 | e6971124f64840a1806a15719c2c8e23a72eedec80b0b6408228e008d62e4f5e |
| workflow | [visible-larger-public-current-H-secant.yml](../../../.github/workflows/visible-larger-public-current-H-secant.yml) | 29786 | 568e076381718ca66d29b42caf34074c0c256efc2eb19ed31e4f52193aa4a5cf |

R360 原证明为 13761 字节，SHA256 f11d3084cc2d2d651d1c61dbe1ce9dd35a195e2cde4b4535e12f522d2d998ad7，原公开提交 4260114d9c1196881d11ad1433278fc0df3a1e54。工作流显式 sparse 取出该证明并核原字节，不能只凭请求里一句 proof 名称通过。

本次入口层次为 launcher → 新 full112 driver → 新 height path → 一个新 current-H client → 新 hook → 新 system/QR；诊断 consumer 由实际循环结束处同步调用。新 QR 仍调用冻结 factor engine exact_20261114_native_damped_chain_qr.py，SHA256 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33；旧 dyadic 位解码核为 exact_20261114_native_allrows_dyadic_residual.py，SHA256 0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f。该复用不允许把旧核的固定整数单位直接套到带额外 dyadic 步长的新状态差上，见第 6 节。

原 145 的完整 system/QR/hook/client/height/driver/launcher/reader 仍在来源闭包，只作冻结基线。原旧 publisher、旧 120/124/145 wrapper 和历史 accepted-state loader 不作为当前入口执行。当前分叉的 system/QR 保留实际调用、迭代、完整 H、当前原状态与矩阵身份，不能把 cached 旧问题改标签成当前问题。

本地仅做源码文本构造、差异与字节 SHA；未导入科学模块、未执行 AST/Node 检查、未运行数值或精确算术。实际 Actions 前置将逐 124 pin 核字节、解析/编译 Python AST、Node 检查 hook，并对当前工作流的 bash 块和 Python heredoc 做语法检查，不执行科学正文。完整差异是临时审读材料，不作为可重算数据再提交一份。

## 3. 精确六参数来源与旧输入的作用

参数顺序为 $(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3)$，本次字面值为

$$
(0.41654476801167684,\ 0.23884336093393582,\ 0.5270922473095916,\
-0.13437878055563054,\ -0.005765450212224129,\ 0.4141025261683763).
$$

仅前三项参与原物理 BVP 参数未知量，后三项冻结。显式新实验 $\lambda=0.001$，不是某个历史正参数场的成功记录。初猜种类仍为 fresh-circle-low-three-linear，保完整 112 模、2048 角求值及原 453 维物理系统。原 699 初始 mesh 重新形成，节点上限 1200 不变。

这些六参数来自 actual119 第 3 批末点，而不是第 8 批末点：run 43693462669、source 6fffce1f36e876f3b08a1c73198a7fde259d94d6；原 status 1568824 字节 / 10c31f1da398f537f1c9dfb19a162bb6aadb30e7e57fddafffebf7a9a60c08e4；原 compact summary 73546 字节 / 4ec08e23ea41bc3f443f04f613270163c9e8624d8b4172ab2a35f998b75acf5a。配方保完整首次来源声明、原六列与前三列 SVD 读数的历史作用，但不把它们当本次 fresh J、低三根证明或连续域证。

四数学输入从历史提交 8bd267107cc8710d371f3b62c02986655ac965b0 的真实 blob 恢复到本 job 独占临时目录，逐原字节核验：

| 原输入 | 字节 | SHA256 | 当前作用 |
|---|---:|---|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff | 原构造与来源输入 |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 | 原完整初猜构造输入 |
| tail_anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 | 仅原初猜资料，不是本次 H 响应/J |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 | 原 112 模、spacing 2、2048 角、32/10/2e−9 配置 |

另恢复原 ledger-ready 109004 字节 / 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6，以及 stored-ready 29774 字节 / c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d。请求保真实历史路径与 Git blob；两者经原环境变量交给真实旧冻结几何消费者，不自行重造。

配置明确无 initialCheckpoint。原 78 份公共尾源码只恢复一次。输入恢复只 fetch 所需历史对象，不 checkout 旧 main、不覆盖实际本次 source commit，也不将恢复 raw 上传或写回 Git。

## 4. 当前 H、原高度路径和最终 BVP 责任

完整当前 H 由本次新建物理问题、完整当前 scalar/profile 及原 true_height 路径计算。旧 compact H、历史零 J 或失败状态不填入当前响应。高度路径保原策略：

- 初次正高度比例 $s=1/64$；接受后增量乘 2，上限 $1/4$。
- 首个正高度请求遇原明确数学拒绝即停止该路径，不靠反复减半隐藏失败。
- 原 64 个 bootstrap 请求资源上限包含零请求与最终 endpoint-J 请求。
- 零请求和中间高度请求不要求 J；实际终点完整 $H_\star$ 请求要求原 J。
- bootstrap audit=false；这不免除原 fullDN 末独立 fresh audit。
- $s$ 是请求高度路径参数，既不是 core 的 $\lambda$，也不是曲面相位。

完整 H 到达后，仍须实际得到当前尾响应及全 338×112 响应导数，先做原 actual-H FD，再进入原完整 fullDN。原 453 维 RHS、原 341/112 边界、原 material/physical 4096 角测试、outer 8、inner 17、物理 RMS/BC 门、最后 fresh audit 均保留。诊断阶段不把某个较小 H 的成功改称 $H_\star$ 成功；末端未到时 fullDN/FD/最终审计继续明确未执行。

本次仅原非线性 correction 被同一完整 R273 $\eta=1$ 方向替换；最终 sensitivity 的原方程与实际源路径不被 $\eta=1$ 正则化代替。worker.last、原同 H 非 audit 缓存、原 predictor/fallback 由原 worker 管理，观察器不赋值它们。后续真实末 p 的连续 scalar/domain 等课题责任不会因本次有限 native 成功而自动支付。

## 5. 三个真实插槽和额外 noJ 调用

hook 对冻结原 core 的唯一 correction 句及原十试步的三个观察位置作可逆源变换。保存当前原源与变换源，逐个唯一锚核验；逆向移除观察插入并恢复 correction 后必须回到原 core 字节。evaluate、flow、root 的函数正文不改。没有用伪装的 toString 将新正文声称为旧正文。

每轮流程如下：

1. 原 fresh evaluate(withJ) 产生本轮完整状态、576 个 J、stage-out/r、cut/far、scales、H、target、mean 与 guard 字段；新 snapshot 绑定真实 call/iteration/sequence 和所有原 bytes。
2. 同步 Python QR 对该 snapshot 求原完整 $\eta=1$ 方向，恢复全部 577×224 原坐标 $\Delta$，核 checkpoint/负零和输出 identity。
3. 在回到原十试步之前，拷贝本轮 X 并额外调用一次原 evaluate(false)，形成 $r^0$。这次调用有独立 attempted/returned/guard/elapsed，不能伪称原 withJ 的另一标签。
4. 每个实际访问的原试步先保存原源码真正形成的 T，然后原 evaluate(false) 照常执行。观察返回原 test.norm、guard 与完整 r；接受判断仍是原严格 test.norm < ev.norm。
5. 原循环若接受，只处理已访问前缀；原循环若十档全拒，才额外尝试 $2^{-10},2^{-11},2^{-12}$。这些状态保存在独立目录，不回写原 states，没有第 11 个接受入口。
6. 原循环结果已确定后，同步准确消费者生成完整或部分 R360 结果。诊断错误只写本身失败范围，不能把原接受反转，也不能让原拒绝变成功。

同状态基点 noJ 的输入副本逐 word 保存；观察器核该调用没有回写原 states/target/scales。此局部数组核验不等价于证明 profile/root 中所有其他缓存完全无影响。第 1 节的额外调用声明始终适用。

## 6. 准确分解与全行索引

令 $X$ 为本轮原状态，$r^J$ 为本次 withJ 保存残差，$A$ 为其完整原矩阵，$\Delta$ 为已恢复原坐标方向；已付原 QR exact ledger 保存

$$
e=r^J+A\Delta.
$$

对本次实际访问的 dyadic 步长 $\alpha=2^{-k}$，$T$ 是原浮点表达式真正形成的 577×224 字词数组。把各字词准确嵌入实 dyadic 后定义

$$
q=T-X-\alpha\Delta,\qquad
\ell=r^J+\alpha(e-r^J),\qquad
b=r^0-r^J,
$$

$$
s=t-r^0-\alpha(e-r^J)-Aq,\qquad
d=t-\ell.
$$

这里 $t$ 是该次实际完整 noJ 返回残差。于是逐行准确核

$$
d=b+Aq+s.
$$

新消费者只对 $q$ 做完整一次矩阵作用；原 $e$ 账逐块原身份核后复用，不重复做 $J\Delta$。$q$ 包括整个实际状态形成表达式的舍入效应，不只最后一次加法。它先以整数提升各原 IEEE word，再作准确减法与 dyadic 乘法，绝不先以 binary64 算出一个 rounded q 再解码。

设本次所有已捕获原/额外 trial 中的最大步长指数为 $k_{\max}$（包括 guard 未返回完整残差的观察记录）。所有 finite binary64 字词可提升到 $2^{-1074}$ 单位；状态形成采用 $2^{-1074-k_{\max}}$，完整矩阵乘积与残差累加采用 $2^{-2148-k_{\max}}$。因此包含原 subnormal 与 $\alpha$ 增加的指数范围。实现对每次移位/二幂除法检查精确整除，旧 $2^{-2148}$ 固定单位没有被无条件外推。signed exact 结果压成 [带符号十六进制整数, 二进制指数]；零的数学值与原输入负零 provenance 分开。

全行顺序不抽样：

| 区块 | 行数 | global 行号与矩阵作用 |
|---|---:|---|
| cut | 112 | 0…111；$q_{0,Q}$ |
| stage n=0…575 | 每块 224 | $112+224n+j$；$-q_n+J_nq_{n+1}$ |
| far | 112 | $112+576\cdot224+j$；$q_{576,\Pi}-Gq_{576,Q}$ |

总计 129248。这里 G 是当前原冻结 far graph 字词，不换新 C 的 general-Robin 行。各区块使用原 sigma；最大值比较以准确整数/正 sigma 的有理商进行，不用浮点 decimal68 决定最大者。显示十进制仅供读数，准确分子、分母、符号、原行位置与见证同时保存。

全行临时 ledger 包含 withJ、same-state noJ、actual trial、ideal affine、b、Aq、s、d、realized affine 的原约定向量顺序。每个完整 trial 报告所有分量的全域与 cut/stage/far 最大值、原行见证、准确恒等式完成行数和原 norm 比较。原打印 binary64 norm、保存原 residual 的准确 sigma-max、理想模型最大值是三个不同对象；分解不回写原打印 norm或原接受。

若额外 baseline guard 失败，则没有完整 $r^0$，对应 b/s 不得填零或伪造；若某个原/额外 trial guard 失败，则没有完整 t，完整 s/d 不得填数。已形成 T 和实际错误、位置、调用次数仍保留。原末期失败时仅可读已闭合的完整行/区块，未开始后缀列入 unpaid。精确恒等式 verified=true 只表示实际已覆盖相应全部行的那个 trial，不推广给未返回向量。

## 7. 原件数组与目录合同

每个真实请求、迭代及观察对象有独立目录，不复用上轮文件名承载当前数组。核心小 schema 为：

| 对象 | schema |
|---|---|
| 当前诊断模型 | current-H-secanted-model-input-v1 |
| 实际状态输入 | current-H-actual-state-input-v1 |
| 实际 noJ 返回 | current-H-actual-noJ-observation-v1 |
| 原十档循环观察 | current-H-actual-ten-trial-loop-observation-v1 |
| 准确分解总结果 | current-H-complete-original576-secant-decomposition-v1 |
| 单个实际 trial 分解 | current-H-one-observed-trial-exact-decomposition-v1 |
| 最终小读回 | request172-current-H-necessary-secant-scalar-readback-v2 |

其中 secanted 是当前冻结字段字面，不是另一个未实现 schema。model 绑定实际 snapshot/result、当前 QR result、完整 current-state SHA、当前矩阵 SHA、H/target/sigma、来源和 R360 SHA。

每次 observation 输入保存 actual-states[577,224] 的原 Float64Array f64le bytes。正常返回保存 stage-residuals[576,224]、stage-out[576,224]、cut-residual[1,112]、end-residual[1,112]；cut 是对该实际 T 和当前 target 用同原表达式作的只读减法副本，stage/far 来自原返回数组。每阵保 dtype/order/shape、完整闭 chunk 行覆盖、raw SHA、bytes。负零依原二进制保存，不经 JSON 数值再恢复状态。

flow-scalars 保存每段原 meanHeight、实际 minA/minD 的 numberRecord；noJ 的无穷占位照实保分类和原 words，不加新的 finite guard。原完整 226 状态推进中的两个 mean 仍由原科学函数计算；本观察接口只导出其真实返回的 meanHeight 和，未虚构两个单独 mean 数组。原 guard 未返回完整 residual 时，不从 stage-out 或基态反推缺失原 residual。

原 QR 的 current576-all-exact-rows.jsonl.gz 每块 kind/node/global 起点、完整 signed e、原 J-stage SHA 与当前 identity 均须对应新 snapshot。这个旧 ledger 每行本身没有另一个 schema；其完整 report、manifest 与源身份一起校验，不能只按同名文件取数。

## 8. CLI 与执行资源

launcher：

```
python root_20261115_current_H_secant_run.py \
  --request COMPUTATIONS/public-six-control-current-H-secant-request.json \
  --recipe COMPUTATIONS/actual119-batch3-current-H-secant172-lambda0p001-recipe.json \
  --inputs-directory OWNED_INPUTS \
  --source-topic RESTORED_ORIGINAL_78_SOURCE \
  --out OWNED_BASE/execution
```

准确子程由真实 hook 构造 argv，shell=false：

```
python exact_20261115_current_H_secant_decomposition.py \
  --iteration-directory ACTUAL_ITERATION \
  --model-sha256 ACTUAL_DIAGNOSTIC_MODEL_SHA \
  --loop-sha256 ACTUAL_DIAGNOSTIC_LOOP_SHA \
  --budget-seconds ACTUAL_CLIPPED_REMAINDER \
  --workers 2 \
  --out ACTUAL_ITERATION/diagnostic-exact
```

model/loop SHA 在实际产生之后取原文件字节，不预填未来值。准确子程每轮显式预算 900 秒，再按全局剩余预算与 60 秒原传输余量裁剪。原 R273 eta1/exact-workers2/factor-bytes2147483648 保留。准确子程不调用 RHS/root/RK/QR/native，仅做新准确算术。

原科学 global deadline 18000 秒从 launcher 完成自身来源/argv准备、启动科学 child 之前的单调时钟起实际执行，包含本次新增 baseline、额外三档和分解耗时；它不把前面 checkout、恢复输入、规则 startup 和 launcher 自身此前的文件绑定伪计为已覆盖；不是增加原 native 32 轮或原十档的数量。science step 330 分钟，compute job 350 分钟；小读回 step 上限 30 分钟、独立 report 5 分钟。各限额并非可以相加后保证都完成，job 硬限可能先到；外部中断及未读后缀必须原样报告，不能承诺无条件留足最后读回时长。

原外层迭代 8、原 inner 17、native 32、每轮原试步 10、native tol2e−9、collocation1e−6、BC1e−11、FD5e−5、max-nodes1200、material/physical angles4096、Node heap6144 全不变。过小的资源剩余只可导致明确 partial，不构成根不存在、目标域失败或原数学拒绝。

原 64 bootstrap 上限保持原角色，含零与末 J；本次不再另加基于“估计总请求数”的科学 call 门。每个真实请求的身份和原路径照实记录，原 fullDN 后续调用仍受实际总资源约束。

## 9. 原数据退役与故障分责

必须区分三个时间点：

1. QR 子进程已退出、完整 delta/checkpoint 校验、correction 小记录已写后，只退役新分解不会读取的因子 raw。当前 J/r/sigma/Delta、原 e 账、状态与观察输入仍在。
2. 原实际试步循环已观察、准确子程已退出，并已得到完整或明确 partial result/receipt 后，才登记本 iteration 全 large-arrays 清单与原 SHA 并退役。预算不足在启动子程前也须先写明确整行未付。子程没有结果、I/O/JSON 异常或循环尚未收尾时保原 payload，不凭失败状态猜已读取。
3. job 最末只有完整必要小摘要读回成功、marker 匹配且 owned scientific group 与规则父进程均已止，才清整 namespace。这个最终清理条件不改变原科学接受，只决定是否允许主动删除尚可能被写入或尚未读回的数据。

因此，最终 reader 的 complete_scalar_readback 只指第 10 节明确选择的必要标量表完整输出且其原件在 Actions 内读取完成；全 dyadic 行见证、原巨大 stdout、完整数组与全行 ledger 不通过日志分段搬出，也没有在本机逐数审计。科学 consumer 自身完整产生/绑定/准确作用的范围与这个小摘要的选择范围分开。最终持久化仅脚本、参数、run 和必要结论/hash。

原 native guard/严格 norm 拒绝、QR 工程异常、准确分解部分完成、观察 I/O 失败、外部 SIGTERM/SIGINT、全局资源时钟、读回错误各有不同字段和退出范围。诊断异常被捕获记录，不成为第十档之外的新接受/拒绝公式。若外层资源限实际中断原 science，其 partial 仍是实际限制，不能通过“非 gate”标签抹去未完成范围。

## 10. 单份必要摘要、原件内部读取和条件清理

reader CLI：

```
python root_20261115_current_H_secant_scalar_readout.py \
  --directory OWNED_BASE/execution \
  --request COMPUTATIONS/public-six-control-current-H-secant-request.json \
  --recipe COMPUTATIONS/actual119-batch3-current-H-secant172-lambda0p001-recipe.json \
  --rules-directory OWNED_BASE/rule-sync \
  --compute-outcome ACTUAL_STEP_OUTCOME \
  --out OWNED_BASE/scalar-readout
```

这是标准库原件读取器，不调用科学模块。它在 Actions 内完整读取选择范围的 JSON、JSONL 和日志字节并核文件身份；不是把这些大对象编码成小 part 后交 connector 重建。普通 large-arrays 仅统计现存文件/字节，生产者原 descriptor 不改；完整数组和准确全行 ledger 不由这个 reader 重算。

正常只输出一份不超过 90000 字节的紧凑 ASCII JSON；trial 与 maxima 使用一个明确列定义的表，避免每行重复长字段名，保留全部必要标量值，schema 为 request172-current-H-necessary-secant-scalar-readback-v2。必要标量包括：

- 实际 process、height path、FD/fullDN 最终状态和真实错误/未执行范围；
- 各实际原 trial 与额外 trial 的原 alpha 指数、是否完整返回、原 norm/words、gate、guard/error、输入状态 SHA 和原 observation/report 文件身份；
- 各完整或部分 trial 的 129248 行完成范围、全行 identity 标志；
- 原准确消费者已经算出的全局 withJ、noJ base、trial、ideal、b、Aq、s、d、realized-affine 的 decimal68 sigma-max 及其原 global/node/coordinate 位置；
- 原打印 norm 与原准确 sigma-max 比较中的十进制读数、完整 comparison 对象身份；
- 此前 native trace/trial 中选定的原迭代 norm、步长、接受/错误等简明字段，以及实际 partial 后缀。

这里只复制原 decimal68 和位置，不重新做任何数学比较。完整有理分子/分母、全部 dyadic row witness、各 family 的完整大极值对象仍有原文件和 parsed-object 身份，但其值不全部输出。cut/stage/far 仍在科学 consumer 的全部 129248 行之内；小摘要没有凭未导出 witness 宣称独立逐数复核。

所有 JSONL 原行在 Actions 内按原 bytes 读取；小摘要只取明确字段。解析失败与未完末行记录原 offset、bytes/SHA、LF 状态和有限原文摘段，剩余内容明确未导出。日志整流只在 Actions 内 hash/读取；错误原文选择首部 traceback/实际错误行和末部错误行，记录原行号与 byte offset。文件过多时明确只选最前两与最后两份错误文件，其他选择表有身份；不是声称完整 stderr 已返回。巨大 stdout、完整源码树、重复 producer 树和多 MB witness 不分块/编码搬出。

正常摘要输出三个 GITHUB_OUTPUT 键：scalar_summary、scalar_summary_bytes、scalar_summary_sha256。SHA 针对单份紧凑 ASCII JSON，不含分隔 LF；临时文件另含末 LF，marker 按其真实文件字节和 SHA 核。没有 semantic-begin/part/end、没有 index-split 大对象重构协议。

如果必要原 trial 标量表本身仍超过 90000 字节，reader 不静默截成“完整”。它仅输出 schema request172-current-H-necessary-secant-readback-incomplete-v2 的小失败范围，保原科学末状态、计数与大摘要身份，明确必要表未全导出，返回 2；raw 保留至 runner 销毁，不写 complete marker。这是工程读回未完成，不是原 native/BVP 数学拒绝。解析/身份/活流错误同样不得出 complete 标志。没有把这样的不足改为第 11 个接受门或额外 epsilon 条件。

读前/读后按 launcher 的独占 child PGID、PID、start_ticks、session 身份检查 quiescence。父 Python 可能属于 runner 共享 PGID，工作流只核其 PID 与 start_ticks 已退出或已由不同实例复用，不要求共享组为空，也不 kill runner。launcher 使用 start_new_session=True，捕获 SIGTERM/SIGINT 后只停止自有子组，等待退出并保存现场；外部信号不冒数学失败。当前输出仍活时 reader 只能标明已观察前缀，不能授权清理。

只有完整必要摘要已经输出、内部所选原件读取完成且原科学组已止，reader 才返回 0 并写 request172-necessary-owned-scalar-readback-marker-v2。工作流另输出一份本身很小的规则父 owner 收据，不允许该 record 超限后分块。cleanup 再核 marker 的实际 run/source、request/recipe/reader SHA、执行目录和 scalar-summary 原 bytes/SHA，重新观察 owned group 与规则父 PID；只有 scalar step success 且证据齐全，才删除 RUNNER_TEMP/visible-current-H-secant172。否则不主动删尚活或尚未完成必要读回的数据。

规则 runner 的 mirror 在另一 sibling 临时目录，不在 rule-sync 子树；没有 clone/config/凭据递归回传。实际规则 metadata 与错误状态照原值选入小摘要，规则变化仍由原 runner 停止科学。没有 artifact/release/raw Git 上传。

## 11. 规则、公开运行与报告边界

工作流仅 main 上 computations/public-six-control-current-H-secant-request.json 的 push 触发，独立 concurrency，cancel-in-progress=false。root 唯一发布/调度，本文件没有预填未来 run/commit/job。

规则基线为 root README blob21bd547f56590b7f2dd279d0297efb289a9b2783 与题 README blobbff8aea253a9e6a7a4fac28d810ac454c5499fec；原 rules runner 原源 pin、2700 秒真实 pull/rebase 周期及规则改变停止语义保持。GH_TOKEN 只供原父规则 runner 使用，科学 child 沿原机制去除认证环境。源 checkout 的真实本次 commit 不被规则 mirror 的新 head 替换；日志分别记录两种身份。

report job 只核并重复这一单份必要摘要或明确 incomplete 的原 bytes/SHA，不存在待 connector 拼接的大对象。完整大 witness/日志不在报告中，只保其身份与未导出范围。报告不补读未产生数据、不把 workflow success 解释成 native/BVP/连续域成功。若主步骤无输出，给 unavailable 结构和实际 compute/readback 结果，不填 0 残差。

## 12. 实际后继读取应回答的问题

原包运行结束后，必须从实际 call/iteration 逐条说明：完整 H 路径走到何处，原哪一档接受/拒绝，哪个 baseline/trial 返回完整残差，R360 全129248行是否付完，b/Aq/s/d 的控制行和全局最大是否同一行，原 guard 与准确模型比较是否有可见差别，以及未访数据和资源范围。更小三档如有下降，仍只是本次诊断结果，不能追认第11档接受或更新 worker.last。

如果本次达到原 complete endpoint/J、FD/fullDN/fresh audit，仍只能按实际原结果给结论；若未达到，则保其未执行范围。准确恒等式、一次线性模型下降、较小残差或当前 finite native 接受都不自动支付连续 scalar 全域合法、同 g 精化、完整闭场 C²/reach/metric 等课题责任。下一算法决策应由这些实际读数决定，本源码不预选一个失败原因或更改原门。
