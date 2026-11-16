# 原 Cat 秩三固定均值：含常数的完整 Macaulay 入口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

本入口延续原十七变量 Schur 模型，选真正 Cat 秩三均值

$$
y^\dagger=e_0+v(1)+e_5=(2,1,1,1,1,2),\qquad H=M.
$$

原 $4\times3$ catalecticant 由精确有理代码实际核秩三。所有偏导先在原六均值、十一 Hankel 变量上求完再限制；原六方向求导时零平移 $H_0$ 保持固定。没有沿三原子参数替代原梯度，也没有预设某个 $H$ 是临界点。

## 1. 新小模型与常数完整性

同 literal $K$、原 $J_3$ 及其双边逆重新生成 $R_3$。逐全部 $17\times78=1326$ 个常数、一、二次坐标，核自动六方向精确导数与独立原 $N,\Gamma$ 公式相等。再逐全部 1326 坐标核 primitive 整数行与原梯度的常数比例。

**这里十七条原式的常数项均实际非零。** 它们全部保留，绝不套用先前两原子点的零常数门。

新 exact 小模型已本地实际完成，其完整逻辑数据为 159454 B，SHA256：

~~~text
c05317c3fe6ac9342260fe08615d80ff8e21637f03969b80584282bf4848f48d
~~~

语义 binding：

~~~text
99455cc5512e802d02a50ca74a82b709003d2e5cb448f909469bf41b2463b63d
~~~

本入口重新运行同 producer 并核全部逻辑字节；同 out 续接可复用同完整 SHA。gzip 头不作为数学身份。原常数比例在 127 处须全部为单位，完整原系数也须 127 整；任一门失败只报告输入/单位失败，不擅换素数。

## 2. 全来源和含常数目标

固定原十七式 $\widetilde F_i$，来源保

$$
m^\alpha\widetilde F_i,\quad|\alpha|\le3,\quad i=0,\ldots,16,
$$

共 $17\cdot364=6188$ 条。目标保全部次数零至五普通单项式：

$$
1+11+66+286+1001+3003=4368.
$$

输入保存十七式的全部 78 个系数位置。native 自己生成源、目标字典；每个来源的全部项必须落在目标表内。所有原式次数至多二，所以此最高次数五是完整乘积范围，没有截断任何项。

native 输入魔数 R15N3M01/version1；checkpoint 为 R15N3C01/version1，完整核为 R15N3K01/version1。与旧 4367 目标的文件不可互读。线性部分的模 127 秩被记录，不作为预设十一的数学门。

## 3. 结果分支

若实际完整模 127 秩达到 4368，则存在同原整数来源的非零方块，故在 $\mathbb Q[M]$ 中原十七梯度理想包含 1。由伴随公式，1 的原乘子次数至多三；固定该均值的整个临界纤维为空。

同选行还可在六个原 $y_i$ 不被特化时形成一个只依赖 $y$ 的非零多项式 minor。此时所有目标含常数，原伴随公式给一个真实均值消去多项式及其原来源。没有除去参数函数或假定原梯度常数零。

若实际秩小于 4368，只记录特征零秩下界；native 必须反代完整 free-I 右核并逐全部 $6188(4368-r)$ 原坐标核乘回。这个余空间仅属于当前有限 Macaulay 矩阵。它不证明特征零有临界点，也不代表多项式全余模或更高乘法闭包。

即便有限域中的常数目标另有某个行表示，未有合法有理提升时也不能直接称 1 属于原有理理想。本入口只有真实满目标秩触发上述特征零单位理想结论。

## 4. 算术与续接

七位面 header 保原固定素数 127。全部独立标量加乘验证先运行。每条原行从十七式重建，规范主元并保全尾部；每次消去后首位置严格后移。

两槽状态只在完整原行、完整反代行、完整乘回行的安全边界提交，含规范基、原 source 标签、原主元值、阶段与 cursor。源 SHA、精确模型、native 输入、全部字典、协议都进入 binding。预算不是数学 binding 的一部分。

exit 75 只表真前缀。续接应依赖已完成输入而不以 exit 75 为成功祖先；同 source/out/binding 恢复，不重新消已付原行。全矩阵未完时不报完整秩。

## 5. 冻结源与 CLI

四源及精确 SHA 全在 [本 Cat 秩三独立 inputs 文件](2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-inputs-789f.json)：Git blob 9a97719f3204eb1d39ef69c4d12957259df637ec，2959 B，SHA256 7ce595b61fa1118b51b6c871d6e0f6fe30028e5f967f810c7a81ceb9bbb12e1e。完整目标数为 4368，含常数。

~~~text
python3 {scripts}/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-rank-789f.py
  --producer {scripts}/2026-11-16-r150-original-nonrankone-cat-rank-three-gradient-789f.py
  --native-source {scripts}/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-native-789f.cpp
  --header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp
  --out {work}/original-nonrankone-cat-rank-three-macaulay
  --seconds 180 --memory-mib 2048 --compile-seconds 30
~~~

外墙建议 240 秒。native 已在本地 g++ 14.2.0 实际编译；两 Python 源已真实 AST 通过。数学完成结果与小模型执行身份分开，只有实际完成后才填写正式定理。

wrapper 在参数内保存错误类型及文本，另保最后完整 checkpoint；不会把超时、编译失败或输入不合误报为数学负结论。仓库仅保存源码、参数、执行身份、输出 SHA 和证明，临时矩阵、profile、核、状态不新存入仓库。
