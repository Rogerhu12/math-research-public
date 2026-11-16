# 原 E 低交换子二十来源的最小常数消费者 v2

本页是执行前冻结接口；实际终止与已完成的三个逆以[第二次执行记录](2026-11-16-r150-original-exact-low20-second-termination-and-three-inverse-prefix-789f.md)为准，未完成constants不改记成功。

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。日期：2026-11-16。

## 1. 原对象与本次实际门

原数域保持为
$$E=\mathbf Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336).$$
十二参数 $y,w$ 不取值。原五十条低交换子为 $(N_iN_j-N_jN_i)e_{u_k}$，按 $i<j$ 后 $k=0,\ldots,4$ 的顺序；所选二十列仍是 $i=0$ 的那些原列。它们在原一百交换子字典中的索引为
~~~text
1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35.
~~~

本入口物化原数域的精确 $20\times50$ 系数，不把模 $127$ 的系数提升为 $E$ 系数。它不展开新的十二参数多项式、不重新求十六条巨大三次边界、不支付高交换子删除，也不搜索单位理想。

## 2. 已付来源为什么允许只核投影

引用[原 E 二十低交换子来源因子化](../results/R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md)。保留原 $35\times55$ 三次来源矩阵 $C$、原单位列 $0,\ldots,34$，令 $R$ 提取补坐标 $35,\ldots,54$。原十六条三次边界来源 $X_{i,v}$ 全部只在原单位列上，因而
$$RX_{i,v}=0.$$
全部低交换子的最高来源是
$$z_{ij,k}=u_j\alpha_{ik}-u_i\alpha_{jk}+\sum_v\rho_{ik,v}X_{j,v}-\sum_v\rho_{jk,v}X_{i,v}.$$
故无需重建 $X$ 数值即可准确计算
$$Rz_{ij,k}=R(u_j\alpha_{ik}-u_i\alpha_{jk}).$$

程序重建全部原 $C$ 系数并核同合法 place 下原单位、逆和字典；以已付的 $CX_{i,v}=u_i\mathfrak m_v$ 代入，逐五十个低来源的三十五项核 $Cz=0$。这是保原边界身份的符号替换门，**不是新算十六个 $X$ 数组的乘回**。

记 $Z$ 为全部五十列、$Z_{\mathcal I}$ 为所选二十列。求解
$$A\Lambda=B_0,\qquad A=RZ_{\mathcal I},\quad B_0=RZ$$
并核全部 $20\times50$ 个精确 $E$ 产品。两边同属 $\ker C$，而 $R|_{\ker C}$ 是同构，因此严格推出完整 $55$ 坐标等式 $Z=Z_{\mathcal I}\Lambda$。再用已付唯一性公式
$$a(z)=-U^{-1}\operatorname{elim}\Bigl(\sum_gz_g\ell_g\Bigr),\qquad \sigma_G(z)=z+a(z)$$
得到五十条完整参数向量及全部原来源的同一个常数矩阵表达。完整 $55\times50$ 展开乘回及十二参数乘回均不是本次新实际计数。

## 3. 完整原模型及数域算术

两份已锁原小源重新构造全部十七梯度、原 J3 逆和 Bell；保留原 $N/\Gamma$ 恒等式与加权 Euler 门。只提取 Bell 对 $H$ 的线性系数和原梯度的纯二次最高部分。原六个 Bell 主列固定为 $[2,1,0,3,4,5]$，其余五列为 $[6,7,8,9,10]$。

程序核两向共 $242$ 个完整 $11$ 维线性坐标逆产品、原五平方与十一二次单位的全部两向乘回、全部 $225$ 二次正规来源系数。原 $35\times55$ 来源、全部普通单项式及所选原列完整保留，与已付模型逐字段核对。

每个固定数域数保留精确三项有理表示和合法 place 的并行运算值。输入有理数先核分母为 $127$ 单位；六、五、十一维数域逆分别使用忠实的 18、15、33 维有理系统；原整矩阵在同 place 的行列式非零，候选分别保存后逐两向精确乘回。不能对运算后任意标准三分量的分母作未经证明的逐项约化。大系统的模像由**同一原矩阵单位**唯一决定，而精确解另作完整乘回。

将 $E$ 按 $1,d,d^2$ 的正规表示送到有理矩阵，得到 $60\times60$ 方阵和五十个 RHS。`fmpq_mat.solve(..., algorithm="dixon")` 返回候选后先完整封存；随后核全部 $3000$ 有理坐标，等价于原 $1000$ 个 $E$ 产品，及所选二十列的全部 $400$ 个单位坐标。模块没有从有限域表达式补有理数。

官方 API：[python-flint 0.9.0 的 fmpq_mat.solve](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html#flint.fmpq_mat.solve)。实际绑定 Python 3.12.14 / python-flint 0.9.0，防止既已定位的 gzip OS 字节差。

## 4. 冻结入口和预算

主源 `2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py`：

- blob `541c14b36925e3cc94018edd8a17a6a765041f5d`；
- 33539 bytes，SHA256 `d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da`。

完整 helper、已付原模型及 phase 的 bytes/SHA/binding 都在同名 inputs 文件中；不假定别的 job 临时文件仍然存在。

~~~bash
python 2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py \
  --model-source 2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper 2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --paid-model-source 2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --paid-model-out original-ten-parameter-module127-v2 \
  --out original-low-commutator-twenty-exact-constants-v2 \
  --through constants --seconds 180 --memory-mib 1024
~~~

常数完整后使用同源、同参数、同输出目录，改 `--through final --seconds 300 --memory-mib 2048`；外层分别为 240、360 秒。

只有来源已冻结及必要源码审读完成后才实际运行。当前 AST 已实际通过；尚无新数学结果或实际单位子式数值。

## 5. 事务与诚实失败范围

三个数域逆各自先登记 `original-inverse-*-candidate`，只有完整两向原 E 产品过门后才登记对应已验证逆。实际进度与最后完整 phase 分开记录，开始求逆事件不冒作完成。随后主阶段顺序为：

1. `original-exact-constants`：完整原常数、五十投影来源及同原 place 单位；
2. `candidate-exact-low20-coordinates`：完整候选，明确 `exactProductsVerified=false`；
3. `complete-exact-low20-coordinates`：只有全部精确产品和所选单位列门通过后登记。

每个阶段先写完整 gzip，再原子登记 manifest。恢复须核同源 binding、整个物理 SHA 和解压逻辑 SHA。候选阶段可以用于继续验证，但不能称作已成系数证书。C 调用若超出预算却没有返回任何完整候选，不宣称有可续候选。

退出 `0` 只表示所请求阶段完整，常数阶段仍是 `completed-prefix`。`75` 为实际预算检查点；只有新增完整阶段才有非空恢复进展。内存或数学核验失败为 `1`，`parameters.error` 保类型和原信息。失败目录和原回执不改写为成功身份。

数学数组、完整 raw、候选和 native 数据均留临时目录。仓库仅存来源、参数、证明及实际执行身份/SHA。

## 6. 若成功所得范围

本入口完成会给准确 $\Lambda\in E^{20\times50}$ 及其全部原来源解释。它把原低交换子的普通 $B$ 子模缩成同二十原列；加六均值、四十高交换子和十 Bell 轴，原 $116$ 种子由同模的 $76$ 列代替。已付两轮定理再给原 $E$ 的至多 $66\cdot10+10=670$ 列完整呈示。

这不使用有限域十四高列换源，不支付 $E$ 上的 $200/210$ 列，也不提前认定四次来源核的秩 $95$。后者是另一条尚待真实原常数门的任务。


## 7. 首次137与独立外层观测

v1 constants 实际 exit137，没有 Python 最终 raw 或已登记 phase；只有原物理模型 1.113559349 秒/RSS75140 KiB 的事件。原99字节stdout SHA `bc403e71d38c5cdea94b9dcc9999db6bec9d5cc44c4f7ea06ba3655dc5f4185d` 保留。没有足够证据把终止归于某一个数域逆或 OOM。v2 不跨 binding 复用 v1，只改三个逆的求解实现、逐逆检查点与进度，原 q/C/RZ 数学式及全部乘回门不变。

实际运行使用独立 `2026-11-16-r150-exact-low20-observed-execution-789f.py`，固定每10秒写 UTC、存活状态、VmRSS/VmSize、MemAvailable 和原stdout字节数；每条心跳落盘。结束另记真实返回码、结束 UTC、墙时、采样峰与父等待得到的子进程 ru_maxrss、原stdout全SHA。采样峰不是进程真实峰；系统未给原因时不猜原因。

只在显式外层 240/360 秒到达时，observer 才记录并向自己的子进程组发 TERM，3秒后仍存活才发 KILL。原stdout不加前缀、不改内容；observer身份与心跳独立文件保存。已存在的观测文件不覆盖。新算术须与其它重内存载入错峰；此项是资源排程，不是新的用户批准门。

~~~bash
python 2026-11-16-r150-exact-low20-observed-execution-789f.py \
  --outer-seconds 240 --heartbeat-seconds 10 \
  --stdout original-low20-v2-constants180.log \
  --heartbeats original-low20-v2-constants180-heartbeats.jsonl \
  --identity original-low20-v2-constants180-observed.json \
  -- python 2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py \
  --model-source 2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper 2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --paid-model-source 2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --paid-model-out original-ten-parameter-module127-v2 \
  --out original-low-commutator-twenty-exact-constants-v2 \
  --through constants --seconds 180 --memory-mib 1024
~~~
