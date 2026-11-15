# R815：首四对共同分母探针的实际停止与已知列续接

## 1. 已证明的有限计算结果

实际公开run [43751142120](https://github.com/Rogerhu12/math-research-public/actions/runs/43751142120)，
job132925208417，源5abcb9ccfba85d6a708b1df94e6383ff549f72a7，
于2026-11-15 19:16:15 UTC完成计算步骤，exit2、包装器error=null。
数学核心实际用时14.461159467000016秒；其余时间用于原源传输、载体和输出。
同次AST通过，完整状态上传后，verify因没有完整Mg/Γ证书而按设计失败。

[原共同分母契约](R815-original-projective-rational-multiplier-reconstruction-method.md)
的首请求实际执行4对probe、每对7种固定列权、每格3条完整LLL行：
28个格、84条行，均无零分母或非单位分母筛除。
84条行产生57个不同分母；加原已知首列分母的基准候选，共58个实际候选。
全部58个均被原完整七点恒等式中的准确条目拒绝，尚未生成候选矩阵块、
完整交换子点证书或Mg index，Γ未进入计算。

实际首列最小共同分母d_g有825个十进制数字、2738 bits。
所有28个格的第0行都给同一个6483-bit正分母D，其整数文本SHA-256为
06f7fee289e6c08e506da445f8bbf4f51d3f94741e087443c430e35084918f1c。
该同一性来自原保存整数文本的相同摘要，不是仅比较位数。

这个候选的实际ID为
R815-projective-g-candidate-c9dd339a886df7dcfd163f1fa43611f0。
它在z=0的交换子(0,0)条目为零，在z=1的同一条目首次非零。
其余57个候选均在第一个z=0、(0,0)条目已非零。
这些条目都属于原要求的完整准确恒等式，没有以随机模检验代替准确式。

**6483-bit D的重复出现及一个条目通过，不证明它是真实Mg的全局分母。**
每次拒绝只否定当次完整构造规则下的候选：
首列准确D v_g，其他列系数取center_M(D r)。
本次没有证明原425个素数精度不足，没有证明不存在准确Mg，也没有改变原源。

## 2. 实际probe与恢复位置

所有已选probe的输出行恰为0；选择由实际425模数上的新strict RR失败决定。
下表使用“输出行、输入列、z次数”，不是把残差坐标反认作输入。

| pair | 第一个probe | 第二个probe |
|---:|---|---|
| 0 | (0,1,3)，flatten索引7 | (0,2,1)，索引10 |
| 1 | (0,2,2)，索引11 | (0,2,3)，索引12 |
| 2 | (0,2,4)，索引13 | (0,3,1)，索引15 |
| 3 | (0,3,3)，索引17 | (0,4,1)，索引20 |

当前scan的completed_pair_count=4、next_coefficient_index=21、
scalar_RR_failure_count=8、unpaired_failure=null、scan_finished=false。
search_stop明确为probe_pair_limit_reached=true、candidate_search_exhausted=false；
不是整个295936坐标的有限策略已穷尽。

同一核心若扩大probe-pair上限，必须从本次完整scan、LLL和拒绝记录恢复，
跳过已经闭合的58个候选，不重新生成首四对。
若加入新的准确已知列或改变候选构造，则使用真实新核心与新tag，
不能把新的矩阵表示当作旧核心续算或复用不再相同的旧拒绝。

## 3. 下一信息来自准确第二列

原R806已经证明W e0=e1，原Mg定义满足Mg e0=v_g并与W交换。
因此

$$
M_g e_1=M_g W e_0=W M_g e_0=Wv_g.
$$

右端仅使用已成原W和原v_g，给第二列的准确多项式向量。
它的加权次数界为4−eps_output。
下一消费者可以一次计算这列及前两列的最小共同分母，
把两列都准确构造，其余未知列才取中心提升。

在这种新构造中，交换子的第0列会由上述恒等式强制为零。
所以它不再提供独立的早期拒绝；检查顺序可以先取其他列中
本来就属于原七点完整恒等式的条目。
最终的全部weighted支持、准确列、七点全部交换子以及原cyclic唯一性完全不减。

本节只说明已成源给出的准确约束，尚未提供第二列的新计算值或新分母。
该新数学必须在公开Actions运行，使用独立方法/核心/配置身份。
原80516ff9同核425-prime续算继续，不因本次有限搜索失败而中断。

## 4. 实际来源绑定

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 新core R815_projective_reconstruction.py | 75693 | 126469e2e7c8377c484a9e0844db463fe93e6c90b2971233a11de556a49d9ddb |
| 包装器R815_projective_public.py | 74410 | 3a0fa603b4b76a801a26b106a35eaa3e1ddc2a69a77b97078d08545e5bc27a57 |
| 方法 | 12400 | ba9ac593615a1321e95a1dfcccd63740845dfc8b43b1775b393930846e74d960 |
| 实际请求 | 11386 | 226af5852f761976df71c60bac4eaa5c42133aaf7343cf7f8053ff421d8a68c8 |
| 完整输出manifest，218项 | 61830 | 1d55aec55b5f166587411a8a6dd021cc0559389d42a5e093b6a5473333c3389e |
| 核心回执 | 996 | 3b0f011622bea885408613106bfc5181a5450cbad771cef65228faba7547f130 |
| false FINAL | 12673 | f162deacea4df447c6355769624b9843d22be66260f2b08100e7fe46ef9571c2 |
| 完整stage清单 | 14934 | d99a08e32e83af040cc2c040a2661c58a3aca5323738bec0a16967da5f427944 |
| 当前probe scan | 2613 | 87466ebcb9cf55b25dd886abcdd35b1004d501aa8fa369bfd9906ba6076595c4 |
| 3037个实际旧源成员的活跃carrier | 2715514274 | 4c9a6d1e3c2c462efecabeba826697efbbc04a3357db1a74d8bd06027804a1b5 |

一日artifact14176572237：
serre-global-R815-original-normal-derivation-operators-43751142120-1，
2719932638 bytes，平台ZIP SHA-256
7884ab57b90d109c595ca5bb6f9b3f8fdf67a73a2dd98c1ae8225512f38e0e5a，
到期2026-11-16 19:16:15 UTC。

原425 current仍是402379e2b5a0d4b225fda74d798bbb164d77ce7c3001eddca789d0fe602ef27c；
其原完整来源和53输入见[425断点记录](R815-425-prime-checkpoint-and-same-core-continuation.md)。
旧W/g/h/Krylov及425历史留原80516ff9配置，新消费者没有重标旧stage，
也没有重新执行425个原Mg模素数步骤。

## 5. 只读诊断的实际执行

纯IO [run43752277161](https://github.com/Rogerhu12/math-research-public/actions/runs/43752277161)，
job132928712542，源beeb21c66677a071ab52a348f6d5155cccc3d39c，已成功。
同次rules job132928641056于2026-11-15 19:25:00.518356 UTC实际pull到该源，
两README均无变化。

reader R815_projective_ended_small_IO.py：
24325 bytes、SHA-256
4a1336a71d76e4b5e11e9e8ab9b8681e0e51b299c03efa75e984ca0603f471e4。
实际请求SHA-256
f9e7b4abfc886ccdf68542f3540a96da34a9e89edc4128dda66abc5578ea912c，
workflow SHA-256
d133f17f47a0046d9165ec1f817998f77c030556a8b9a3f8adbcffbaa608a361。

11个Range请求实际传输4480619 bytes，只读小metadata及全部实际probe、
LLL、候选定义、早期残差、拒绝和scan。
它未下载2.715GB carrier、未读取562MB current，
也未重做LLL、RR、矩阵乘法或残差运算。
其完整机器summary为272390 bytes、SHA-256
4ff1331d649e51a08e11f74d2f57231a4cd999d5d10cce887eac3fdf7d3cbf67，
只在活跃artifact保存；日志输出的是不含大整数和大矩阵的元数据投影。
本记录依据这个实际投影，不冒称在本地重哈希了整个大ZIP。

小IO artifact14176887224：4733661 bytes，平台ZIP SHA-256
8049382f0d2e1a4381b54240c8f092889efc95a8409f8f9bd5dbe02f5b308a63，
到期2026-11-16 19:25:14 UTC。
机器输出不进Git/Release，仓库仅保源码、参数、真实run和摘要。

主目标、原准确Mg/Γ及实际高度仍开放；后续采用上述准确额外列继续。
