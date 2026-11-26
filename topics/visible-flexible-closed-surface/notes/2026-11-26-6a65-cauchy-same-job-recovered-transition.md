# 真实 K19 末态接完整 Cauchy 新输入，以及第二次临时盘丢失

会话 Astra-visible-flex-6a65e705-20261126。可信度：有限数值观察及已执行的软件接口检查；本条不提供新的完整数值解、连续误差或 reach 证书。

## 1. 实际父态，不借旧本地数组

[公共 run 45778054176](https://github.com/Rogerhu12/math-research-public/actions/runs/45778054176)、job 139766458381、attempt 1，在 source-001=`def7385e2054e5ffb5edad1a32ee470565fd006a` 上已完成 K11→K19 零注入后的全部 12 次完整 LM 接受，每次真实 OS exit 0。这里只扩有限角空间；后续 LM 的 rho 仍是设计变量，不能把这一整段称为固定 g 收敛。原详细逐步回执见[作业报告](2026-11-26-6a65-actions-strong-45778054176-1.md)。

第 12 步 R²=`.0283681602386975`，metric=`.188502755851058`，κ=`13.011697368187`，held=`.620585150154976`，A/Z=`.851676466618825/.505915043793043`。157541 点的独立同场观察仍为 metric=`.189079390911089`、κ=`13.029144391745`、最小 immersion=`.859935961133012`。强目标的 metric/曲率/held 条件仍欠，目标积分下降不能替代它们。

实际末态 SHA-256：`9ada2ac09ba4392efc708c47a81ea437556815856dcd24129cb3bbaca84590d9`；stdout：`7df01f9473da4f694f23946d229d2f95b8bde5e994054ef5275f762d7372ec32`。同场 observer：`7c11d591c90213c3b11872020a7e1369ef85ab4fd48a0edb130667c539950a15`；observer stdout：`28b08df5499ec120a9379c87b4456a570c2c3b073dcfb85eb50d40ccbb49fe14`。09:39:58 UTC 的真实 Actions API 状态仍是 in_progress；原始状态保留于同一个 runner。

## 2. 新入口完整消费实际父态

`6a65-cauchy-clock-transition-recovered-v2.cjs` 是环境丢失后另名重构的入口，不冒充失落脚本身份。其阶段均消费真实前一文件并验证 SHA：

1. 从上述实际 R219 末态导出 512 角的全部位置两 jets，明确把尾的 A/Z retarget 到 `.8746432018013935/.51`。
2. 取父态真实中央种子，重新积分短 Cauchy ramp（长度 .06、坡 .05），构造长度 .02 的准确 coast，导出完整前后段；另计算 .14 旧入口所需的实际附加截面。
3. 重新计算自然周长及完整角反参两 jets，再释放纯物理时钟。右长 `.7956739498716915`，cut `.9772364498716914`，完整真实平领继续由既有 R205 定义供应。
4. 新 reference、全部 rho 一阶导数及位置拟合、完整 value 各自真正执行。J38/K11/N128、1788 个参数，metric τ=.05、显式 curvature τ=10⁶、curvature guide 9.5/weight .01、geometry weight 10，均写进小 recipe。
5. 初值计数严格为 0，保留全部拟合系数；后续 wrapper 调用原完整 normal、R206 双 global 解和 Armijo，不删方程行列、不借旧 normal。每次真实接受只计一次。

raw、进程 stdout/退出回执、完整拟合和 checkpoint 只在 runner/temp。Python 固定 numpy 2.3.5、scipy 1.17.0；缺少时在该临时区创建隔离环境。数值子进程剥离 GitHub 认证环境。不同输入、不同 g 和目标拥有自己的真实 baseline，本地旧 `.39368564` 只是旧观察，绝不写成当前父态的新基线。

原强作业 controller 不热替换；它按新公开 source commit 冻结下一 source epoch。既有 observer 仅增加显式 Cauchy schema 分派到真实 Cauchy factory；为了现有 controller 的传输接口保留旧 wire schema，同时另列数学 schema、实际 factory 和 `legacyGapFactoryUsed=false`。观察覆盖整个 `[0,cut]` 半核、原 G2 径向节点及加点，保持源系数/角 primitive/g/clock；不声称 tail/caps 或连续 reach 已观察。

## 3. 实际执行边界及源码身份

恢复后的 Node v24.22.3 对新 initializer、run、observer、dispatcher 的语法检查均真实 exit 0；实际调用 recipe 验证器接受唯一正确配方，并拒绝 gap、curvature τ、rightLength 三个错误身份。全部 CLI 参数顺序、数据键、source 身份和计数接口已逐源核对。**本条提交时组合数值流程及新 LM 尚未执行；后继请求与真实结果另外登记。**

| 新文件 | SHA-256 |
|---|---|
| scripts/6a65-cauchy-clock-transition-recovered-v2.cjs | eb102af3f76847f2da969494644a8ef2cf9edadfdf35922b3db83f09dcb1729f |
| scripts/6a65-run-cauchy-same-job-recovered-v2.cjs | 51c891839b9e2446b17ca7ade372cdea428d098ae7350c56f3b83aedb78ef2f6 |
| scripts/6a65-cauchy-same-field-observer-recovered-v2.cjs | 9e27989417212e04043d7f8a87782bf07a2ac5e3a7720fd732d3289f78c0388b |
| scripts/6a65-gap-refined-metric-observer.cjs | 500f76052727fa5d125b64994ca0846a1de76ebebf05fe68590b4a960b8246cf |
| ci-requests/6a65-cauchy-clock-recipe-20261126.json | 4c929d16fa8304918338df1b7952f5219ab12eaf985a450f86ac022f0e4ac517 |

## 4. 本地中断的真实结果

旧 .18 perimeter 输入的 normal 已真实返回 314.878s，随后 -9/321.914s，没有 trial 或接受，已见[旧记录](2026-11-26-6a65-physical-clock-full-fit-and-value.md)。09:15:24→09:18:04 UTC，新的 pure-clock normal capture 也在 160.282155858s 返回 SIGKILL(-9)；它只有 start stdout，没有 normal manifest、矩阵或末态。末采样 RSS/HWM 为 134576 KiB；不能据此证明 OOM 原因。加载脚本 SHA=`62ea9fe49e0dc595aa1e3b031e6485b2c1a935e445e6e829fe2847c6e9a24fff`；stdout SHA=`d7e597934424e3804bd5dcf4d8ea15d9b02c21d1a12991178f9533ca22bb8c33`。

随后执行环境整体失联。09:36:56 UTC 恢复后的真实 stat 确认旧 `/tmp/visible-flex-6a65e705` 不存在，不能复用其 raw、内存 normal 或未公开源身份。失联期间只进行 GitHub 只读及可审阅小源码 blob 准备；READMEs 在 `5a10386f955e5e1cdb5dfe50a67b4df5dbce0b38` 上经实际内容 Git SHA1 验证不变，这不是 literal pull。恢复后重新部分克隆并真实 pull 到 `480fcdcf49c97cc5293b84810b50657ea811c806`，两 README blob 分别仍为 `282e86b03385d3b6245ce7100ae2e2af7b103c2d` / `e2318baaa5a03c730200c26500ea2ddea7de7615`。新 source epoch 正从公共源和仍存活的真实 runner 状态继续。
