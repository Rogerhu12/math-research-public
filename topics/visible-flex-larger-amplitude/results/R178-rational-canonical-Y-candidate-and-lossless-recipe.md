# R178：原节点上的有理 Y 候选及可逐字节恢复的紧凑系数

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-13。

**已定义并完整保存一个新候选，不是原方程解的证书。** 本条从 R168 的217个规范节点和 R169 的216段原第一 jet，构造准确有理的五次 Bernstein 多项式

\[
\widehat Y=(\widehat Y_P,\widehat Y_K),\qquad
(\widehat P,\widehat{\bar K})=\frac{\widehat Y}{\sqrt{r w^3}},
\tag{178.1}
\]

其中分母采用原真实背景。全部215个内部接缝在 $Y$ 坐标准确连续；原连续正背景给非均值物理候选相同的连续性。没有宣称其第一、二阶导数跨缝相同，也没有把有限角 mean 当作完整 mean。

## 1. 系数的精确定义

对每个原规范节点，取实际二进制数

\[
d_b=\operatorname{binary64}\!\left(\sqrt{r_b}\,w_b\sqrt{w_b}\right).
\]

该式仅定义一个实际记录的正二进制有理数，不假设它等于真实 $\sqrt{rw^3}$。节点 $Y$ 定义为该准确有理数乘以 R168 储存的准确二进制 $P,\bar K$。同一节点只取一份定义，因此相邻段不使用不同背景读出来拼接。

端点第一导数同样作为系数定义：

\[
\dot{\widehat Y}
=d_b\dot y_b+\frac{s_b+3\ell_b}{2}\widehat Y.
\tag{178.2}
\]

这里 $s_b,\ell_b,\dot y_b$ 是 R169 原局部 stage 坐标下的数值；式(178.2)在转为 Fraction 后准确运算。局部 stage 到原 source-x 的导数比例仍是8。

端点第二导数由已固定的1024角有限公式、局部步长 $2^{-18}$ 和端点方向的中心差分定义为实际二进制数。这个有限公式使用二次 mean 分支，**只用于选择候选系数**。本条不需要也没有证明这些第一、二阶数值是原无限方程导数的准确近似。

给定 $y_0,y_1,d_0,d_1,e_0,e_1$ 后，六个准确 Bernstein 系数为

\[
\left[
y_0,\ y_0+\frac{d_0}{5},\
y_0+\frac{2d_0}{5}+\frac{e_0}{20},\
y_1-\frac{2d_1}{5}+\frac{e_1}{20},\
y_1-\frac{d_1}{5},\ y_1
\right].
\tag{178.3}
\]

全部216段、每段20对分量和所有节点身份均已实际完成，1315项门通过。正式 wait4 exit0，wall3.036587秒，峰88940 KiB。

这是不同于 R173 的新连续表示；除以真实因子后，物理节点不自动等于 R173 的二进制节点。R177 的 $P$ 入口误差也不能不加计算就转用于本条。

## 2. 保存实际系数而不重做浮点计算

完整多项式 gzip 为1954014字节，SHA256：

58f4b69ebd5ac58daafbbb71c50b8f511b57887363c9520ff0140bd800873f16。

它是便宜可再生的大派生件，保留在 scratch。稳定包保存原规范节点定义、所有实际第二 jet 的 binary64 十六进制位表示，以及准确恢复程序；恢复过程中不重做 libm、有限角求积或有限差分。

从已写出的 Bernstein 系数准确反取

\[
e_0=20(b_2-2b_1+b_0),\qquad
e_1=20(b_3-2b_4+b_5).
\]

每一个反取值均核为原二进制有理数，并保存其精确位表示。原第一 jet 和节点定义通过(178.2)恢复后，使用(178.3)重构每一个系数、原字段顺序和诊断元数据。实际恢复了全部解压字节及原 gzip 字节，两个 SHA 均相同。

紧凑文件只有74503字节，SHA256：

da3ab52e1f594e6e8f4d47773e5fd3dd452a292fe1a828c2eb42699cd33c92c7。

此次无损存储计算共17287项门，正式 exit0，wall8.608941秒、峰71492 KiB。完整恢复命令、输入 SHA 和原输出 SHA 均在其 certificate 中。这是实际候选的存储转换，不是新的数学接受门。

## 3. 实际尝试、源码和未完成部分

首次启动在进入科学计算前被原“输出前缀必须全新”的检查拒绝：外层已创建同前缀日志，实际 owned exit1、wall0.560091秒。原日志和资源完整保留。第二次只改用与日志分开的新输出前缀，候选源码没有改变。

候选定义主件 SHA256：

fbb5ff13f972437ef83087289c036b6bcfb414ef3012c3dcc1bc9ff4f9556409。

候选源 [root_R178_canonical_Y_quintic_candidate.py](../computations/root_R178_canonical_Y_quintic_candidate.py) 的 SHA256 为
f60a6ef07a6917d460edf3b648b4a855c5d84c87e6329c239d461d28fc5be054。

无损恢复源 [root_R178_Y_compact_recipe.py](../computations/root_R178_Y_compact_recipe.py) 的 SHA256 为
cd427dc5009f711f2752d074e6ac40b79bfef4cbe74aff3f7ac58eefd89098ab。

完整稳定包登记在 notes/2026-11-13-root-R178-canonical-Y-candidate-manifest.json。下一项实际工作是对(178.1)逐原叶支付完整 mean、无限逆和原方程残差；本条没有宣称这些已付，也没有宣称真实入口、误差管、闭面或幅度门通过。
