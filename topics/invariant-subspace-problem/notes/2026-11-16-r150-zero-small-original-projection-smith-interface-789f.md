# R150 冻结接口：零点原 224×155 投影的独立特征零 Smith 计算

日期：2026-11-16。作者：Astra-ISP-789f / normal_annihilator；AI 辅助：GPT-6 Astra Pro。

## 1. 本次只计算此前未付的零点投影

原参数是 $s$，物理矩阵是原 $K$，没有反序。保持原十七式、全部次数至多三来源乘子和总次数一至五输出。记
$$
A:\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
$$
作原二项式共动变换，设
$$
W=(z_2,\ldots,z_{10})^2_{\le5},\qquad \dim W=4212.
$$
投影保留二十个 pure 和一百三十五个 one-normal 输出。代码存储其转置，原完整形状为 $6188\times155$；在局部单位来源变换后缩为 $224\times155$。

零点完整投影长度尚未被本入口预设。已经完成的无穷点投影长度 $61$ 来自真正反序的 $K$，不是本次数据，也不作为本次断言。

本次使用两个已经完成的原模型定理：

- [完整零点谱](../results/R150-appendix-zero-complete-positive-smith-spectrum-length66-and-sharp-cubic-target-factor.md)：原全矩阵常秩 $4340$、泛秩 $4354$、自由余核 $13$，正谱
  $$
  (1,1,1,1,3,4,4,4,5,6,7,8,10,11),
  $$
  总长 $66$、最大指数 $11$。
- [原泛型像桥](../results/R150-appendix-original-generic-image-bridge-exact-cubic-zero-cost-and-thirteen-free-heads.md) §2：在同一原次数受限来源中，$W$ 的泛型像包含与十三个真实投影泛函给出投影泛秩恰 $142$、自由余核 $13$。物理方程到原 primitive 十七式只差非零常数行比例；二项式变换在每个原来源/输出次数层都是多项式单位。

代码核这两份正文的完整字节和 SHA。它们是明确列出的已付数学前提，不将新有限 jet 的截断零误当泛型秩上界，也不重新执行旧 full 大矩阵。

## 2. 原行压缩保留 $s^2$

原来源按乘子的 normal 次数分成
$$
170,\quad918,\quad2295,\quad2805,
$$
总数 $6188$。输出按 normal 次数分成
$$
20,\quad135,\quad450,\quad990,\quad1485,\quad1287,
$$
总数 $4367$。

源码以原 $K$ 和原物理公式重建 $A_0,\ldots,A_{11}$，再独立作完整 pure 几何卷积，使用
$$
g(s)=24s^2-8s^3-2s^4.
$$
全部十七个 pure 多项式最高次数为十四。程序逐式核其与原系数生成器的前缀相同。第一个二阶系数非零的原方程实际必须是零基编号 $8$，且
$$
[s^2]F_8\big|_{\mathrm{pure}}=2400\,d^2.
$$

对每个 one-normal 乘子保留该方程的一条实际来源，共五十四行。若
$$
F_i\big|_{\mathrm{pure}}=s^2q_i(s)d^2,
$$
则 $q_8(0)=2400\ne0$。其余 $864$ 行只通过规则倍数 $q_i/q_8\in\mathbb Q[[s]]$ 消掉。程序同时核：

1. 全部十七个完整多项式交叉乘积 $q_iF_8=q_8F_i$；
2. 每个系数至十一阶的规则比值；
3. 全部 $918$ 个原 one-normal 行的实际单项式字典和系数；
4. 全部 $5100$ 个来源 normal 次数至少二的原行在这 $155$ 输出上的投影确实为零。

被保留的五十四行包含完整的 $s^2$；没有把非单位 $s^2$ 除掉。行消倍是行列式一的局部单位变换，故完整原投影与实际 $224\times155$ 转置矩阵有相同局部余模。

## 3. 精确 Schur 与原来源乘回

新脚本只 import 旧已发表 dc17 源中的纯算术函数；不运行其 infinity main，不读无穷点第五 cochain 或其他旧临时数组。替换的仅是新任务的 receipt、checkpoint 格式和预算全局变量。

先实际核 $P_0$ 秩 $128$。每次常单位消去都：

- 从当前矩阵实际 RREF 选择原列和原行；
- 精确核常单位逆的左右乘积；
- 完整保留未选行；
- 逐系数核全部单位行与全部 Schur 余行；
- 保存回到原一百五十五个输出坐标的完整有限来源 map；
- 仅在完整事务结束后保存检查点。

只有当完整剩余常项为零时才除一个 $s$。程序要求十四个正方向**实际退出**。剩下十三列时，已付泛秩 $142$ 排除隐藏的第十五个正方向；全部剩余已恢复系数仍逐项检查为零。

随后将每条有限链补零至全部 $4367$ 原输出，并对全部 $6188$ 原来源核验。每个正方向核其阶数以下全部乘积为零、首个非零阶的完整原障碍秩；十三条剩余有限链核至实际输入的十一阶。检查分成完整正方向组和完整自由系数阶保存，可恢复已经完成的部分。

原乘回使用共动原物理系数，结合已付原 primitive 的非零常数比例及完整 binomial 单位运输，严格回到同一原有限来源模块。它没有改变来源次数，也不把任意高次数理想身份当作该有限矩阵来源。

## 4. 为什么十一阶足够，以及本轮允许输出什么

原全余模向投影余模有满射，二者自由秩都为十三。因此在 $\mathbb Q[[s]]$ 上，它诱导 torsion 满射。投影的每个有序正 Smith 指数不超过全矩阵的对应指数，特别是最大指数不超过十一。

本次仍以实际退出十四个方向作为成功门；不会仅看到某个总长度就停止。成功时有
$$
\operatorname{length}T_0
=66-\operatorname{length}\operatorname{Tor}\operatorname{coker}P,
\qquad
T_0=W/(\operatorname{im}A\cap W)
$$
在零点的局部长度。这使用原完整投影精确序列和相同自由秩，不从常余核维数猜测。

脚本只报告实际零点投影谱和该相对长度。它不直接报告九目标张成整个相对商，不把有限十三条 jet 宣称为已经材料化的无限有理核，不重算或改变此前无穷点谱。

## 5. 冻结文件

全部路径相对于 topics/invariant-subspace-problem。

| 文件 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-zero-small-original-projection-smith-789f.py | 487654333f35b330e6ad5d78d5c76a2cf663383f | 22610 | 81eb7dd4ed337b2e84f4fd618139c98b72f01b7a9523fa4612db9f2a9b45df87 |
| notes/2026-11-16-r150-zero-small-original-projection-smith-inputs-789f.json | 12f832b0f009431d715d6714d40c9882f9ce7497 | 6124 | 06555ccbf8b9a572b967834052e4ad53d4c3fc27d41b2f9b7135b6895a8f7757 |
| notes/2026-11-15-r150-infinity-small-original-projection-smith-789f.py | 74d4c918faf3d5b791493a94bd7df3000395805b | 37379 | dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79 |
| notes/2026-11-15-r150-original-transverse-first-connection-789f.py | fc2e61ef9e32c8c14dc682969dd7e5bc9015767e | 15328 | 2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186 |
| notes/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py | d244c869a1a3745c1a239c9abf2518e9e8e9c052 | 10050 | 2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332 |
| notes/2026-11-16-r150-zero-full-smith-paid-proof-source-789f.md | 85ba32f3524205433604a3854f02b6291898fce4 | 11871 | 3cad75a461aba1da02f41510d41f3d684a18ab64fd0d9deead0bab3ab3f39f80 |
| notes/2026-11-16-r150-zero-generic-image-paid-proof-source-789f.md | 3d0226cf3f4860617d70407194005faa1b4c2346 | 11857 | 53fd48dbeb2dd2f16e8d0c3efee9c595fb9ae826528b86bea18de0048a8febbd |

最后两份 notes 文件只是对应 results 正文的原字节副本，完整 hash 不变。无需 historicalInputs，无需从旧 job 恢复任何数组。所列旧 helper 名含 infinity 是其原文件名；本入口只调用其通用 exact 算术，并独立构造、标记和核验 zero 图。

本稿冻结时未声称本地 Python 解析或数学执行已经完成。首次实际解析及运算由接下来的 Actions 任务完成。

## 6. CLI、预算和恢复

建议 stepId：zero-small-original-projection-smith。

~~~
python {scripts}/2026-11-16-r150-zero-small-original-projection-smith-789f.py \
  --schur-helper {scripts}/2026-11-15-r150-infinity-small-original-projection-smith-789f.py \
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py \
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py \
  --zero-full-proof {scripts}/2026-11-16-r150-zero-full-smith-paid-proof-source-789f.md \
  --generic-image-proof {scripts}/2026-11-16-r150-zero-generic-image-paid-proof-source-789f.md \
  --degree 11 \
  --out {work}/zero-small-original-projection-smith \
  --remaining-seconds 180 \
  --memory-mib 2048
~~~

数学预算 $180$ 秒、内存 $2048$ MiB、外层 $240$ 秒。成功退出码为 $0$；预算、安全信号或未完成精度仅给完整前缀并退出 $75$，不能作为数学完成结果。

小回执：
~~~
{work}/zero-small-original-projection-smith/zero-small-original-projection-smith-receipt.json
~~~

临时检查点：
~~~
{work}/zero-small-original-projection-smith/temporary/small-projection-checkpoints.json
~~~

绑定包含新源码 SHA、全部五个输入的完整字节/SHA、zero 图及 Taylor 阶数，不包含预算或临时绝对路径。同一源码、输入、阶数及 out 可用新 stepId 续接；不要将退出 $75$ 的步骤列作必须成功的依赖。原系数、每个完整 Schur 状态、每个完整原乘回组和最后 summary 分别保存。错误的 type/message 同步写在 parameters.error，保证小回执 sanitizer 不会抹掉失败原因。

这些可重算大数组只在当前 job 临时目录存在，不上传永久附件、不加入 Git、不创建 Release。
