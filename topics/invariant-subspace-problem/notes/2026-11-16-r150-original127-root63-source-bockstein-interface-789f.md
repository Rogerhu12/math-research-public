# 原全参数来源的 127 第一系数连接：$s=63$ 的标量消费者

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本入口读取已经完成的原 F127 正常形、完整参数模基及 whole torsion，检验唯一 $s+64$ primary 的第一 **系数 127** Bockstein。这里的除法是除整数素数 $127$，不是沿参数 $s-63$ 取下一页。本文冻结算法与严格接受门，不预报实际连接是否非零。

## 1. 冻结来源与实际父数据

下列三个依赖文件均为小 UTF8 文本：

| 文件（相对本课题） | Git blob | 字节数 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-original127-root63-source-bockstein-native-789f.cpp | 2220492326f5bea20bc03706b9f22c4d6784b6bd | 24871 | 6a932e17fbeb7c81f335281c88bd1dfe0003a09371d454ea23f1861c86823bfc |
| notes/2026-11-16-r150-original127-root63-source-bockstein-789f.py | 935d6458b34bfc948821fb195ca94e7e13e0cf7c | 27228 | 3ee3b83dbac5fa3f96aea04cfc01a7c86cf2423fd027f050bc46f3a97406253f |
| notes/2026-11-16-r150-original127-root63-source-bockstein-inputs-789f.json | 2698e85b8a04d3317caf712776a3de35694a5971 | 5264 | 15bbab725722b16862612e4b9ed74106d74d343ae981282564284b68d3a7a120 |

完整输入 pins 见上表 JSON。父回执为：

- notes/r150-source-kernel-session-789f/43772109844-original127-original-model-all6188.json；
- notes/r150-source-kernel-session-789f/43772109844-original127-complete-normal-forms-all6188-180.json；
- notes/r150-source-kernel-session-789f/43772109844-original127-complete-graded-module-gb900.json；
- notes/r150-source-kernel-session-789f/43772109844-original127-complete-whole-torsion60.json。

这组父数据使用原全部 6188 列：3333 个预基来源与 2855 个完整补列。相对旧 2195 列名单恢复的 660 列全部重算，其中 658 个正常形为零，原 ID 6046、6063 的两个正常形非零，并已经进入完整 GB。新程序不使用“旧 660 全零”假设。

完整 GB 有 1021 个不同 leading-component 基向量、13 个自由方向，DAG 包含 69,407,428 次原来源 reduction 与 11,591 次 swap。whole 的有限窗口为 805，完整 torsion 维数为 299。原特征多项式在 $s=63$ 有简单根，故该 primary 的向量空间维数恰为 1。新程序从原 300 个特征系数再次检验函数值零、导数值非零。

当前本地执行环境未可用，未声明本地编译或数学运行；第一次 C++ 编译和 Python 执行发生于下列真实 Actions 任务。

## 2. 构造原左泛函，不把点核充作全参数来源

令 $p=127$、$\alpha=63$。程序把已付完整 GB 的所有 1021 个多项式行在 $\alpha$ 处求值，保留全部 1034 个坐标，得到 $G(\alpha)$。实际 RREF 必须给

$$
\operatorname{rank}G(\alpha)=1020,\qquad
\dim\ker G(\alpha)=14.
$$

保存完整的 $1034\times14$ 核并核全部 $1021\times14$ 乘积。这里的核仅用于产生原输出上的左泛函，不作为整数除源。

whole 临时状态中的窗口坐标为 $(c_i,d_i)$。对每个 $a\in\ker G(\alpha)$，令

$$
x_i=\alpha^{d_i}a_{c_i}.
$$

读取已付真核 $K\in\mathbb F_p^{805\times299}$ 与完整参数作用 $J\in\mathbb F_p^{299\times299}$，对所有 14 个 $a$ 同时计算 $q=xK$。必须核：

$$
\operatorname{rank}\bigl(q_1,\ldots,q_{14}\bigr)=1,\qquad
q_iJ=\alpha q_i\quad(1\le i\le14).
$$

选择首个非零 $q_i$，以其首个非零原 torsion 坐标归一。这样选的是完整原 torsion 在 $s+64$ 上的对偶，不以 13 个泛型自由泛函冒充额外方向。

随后按原 nf-prebasis.bin 作转置回填。1034 个原非主元输出坐标直接取 $a$，3333 个主元按矩次数递增恢复。各同次数主子块仍要实际核为单位矩阵；线性尾读已经恢复的低一次数坐标。完成后核所有 3333 个完整预基点积，并保存全部 4367 个原输出坐标 $\ell$。

最后使用原 primitive 整数 17 式，在 $\mathbb Z/p^2$ 上直接构造全部原 6188 列。新消费者逐项复核原 4433 个多项式系数与已付 F127 模型的一致性、原 6188 个 monomial-major 标签及原 18 个归一常数为 $p$ 单位；必须实际得到

$$
\ell\,\bar A(\alpha)=0
$$

的全部 6188 个坐标。仅有 GB 点矩阵的核而未通过此门，不产生连接结论。

## 3. 真正全参数零来源及标量递推

令原多项式矩阵为 $A(s)$。NF 的 forward、backward 文件保存原 3333 来源的常数行运算，包括每次规范化的非零标量；nf-reduction.bin 保存全部 2855 来源的参数移位消元配方。GB 的每个 R 事件是

$$
y_{\mathrm{new}}(s)=y_{\mathrm{old}}(s)-a s^k y_{\mathrm{pivot}}(s),
\qquad a\in\{1,\ldots,126\}.
$$

所有系数均按其实际标准整数代表解释。I、B、S、F 事件只改变输入、基位、交换及最终单位缩放的标签；完整新消费者核每个原节点的路由、顺序与边界。

每个 Z 事件来自已经真实归零的完整多项式行。因此相应整数 DAG 来源 $y(s)$ 满足

$$
A(s)y(s)\in p\,\mathbb Z[s]^{4367}.
$$

这一全参数身份来自原 NF 与 GB 的已付来源运算及实际 Z 端点，不由 $A(\alpha)y(\alpha)=0$ 推出。

预基完整补列的 GB 过程只有交换、加减参数单项式倍及非零域常数规范化。最后 1021 个不同 leading-component 行在 $\mathbb F_p[s]$ 上独立；因此 2855 个输入中的 1834 个 Z 端点，连同原预基运输，给完整全参数来源核的一组生成基。新扫描核所有 2855 个输入、1021 个最终基与 1834 个 Z 端点，不只尝试少数来源。

先由原整数矩阵计算

$$
c_j=\ell A(\alpha)e_j\bmod p^2,\qquad
\delta_j=c_j/p\bmod p.
$$

全部 6188 个 $c_j$ 必须在标准余数中被 $p$ 整除。此后每个来源节点的整数标量都属于 $p(\mathbb Z/p^2)$。其除后的递推严格为

$$
\delta_{\mathrm{new}}
=\delta_{\mathrm{old}}-\bar a\,\alpha^k\delta_{\mathrm{pivot}}
\pmod p.
$$

程序使用 uint8 存储每节点的 $\delta$，同时在每次 R 运算核对上述值乘 $p$ 后与真实模 $p^2$ 的整数运算相等。F/B/NF 来源运算也保相同规范与符号。输入原列、预基常数单位和参数移位均未替换成另一组图坐标。

69,407,428 个 scalar 节点约 70 MB。763 MB 原操作文件只顺序读取。进度停在完整事件边界；原子 checkpoint 记录全部已付 scalar、原路由与准确输入 offset，续接不重做既有 GB 高斯或多项式消元。

## 4. 任一非零值还须通过完整原乘回

若所有 1834 个值均零，入口只报告本 primary 第一系数 Bockstein 为零；不排更高 $p$ 阶扭、不改 Q 成员性结论。

若有非零值，选择第一个这样的实际 Z 端点。新反向消费者利用每 65536 个 reduction 的稀疏 offset 表，逆向重放同一个 GB DAG，随后逆向 NF、backward、forward 运算。全过程在 $\mathbb Z/p^2$ 上保真正整数 lift，恢复

$$
\widehat y(\alpha)\in(\mathbb Z/p^2)^{6188}.
$$

它不是由点核重新求得的另一来源。原全参数 $y(s)$ 仍由父 DAG 与选定 Z 节点精确可复现，未在永久数据中展开大多项式。

Python 外层用原 primitive 17 式重新乘出全部 4367 个坐标：

$$
v=A(\alpha)\widehat y(\alpha)\bmod p^2.
$$

必须逐坐标核 $p\mid v_i$，并核

$$
\ell(v/p)\bmod p=\delta_Z\ne0.
$$

原 6188 来源向量、原 4367 除后乘积、左泛函、对应节点及全部实际 SHA 均只存 job 临时证书。只有以上全门完成，才能标为真实正证书。中途停在 scalar 或反向恢复阶段，不提前计新系数扭。

## 5. 正证书的严格特征零推论

设 $D=\mathbb Z_{(127)}$，$L=\operatorname{im}A\subset D[s]^{4367}$，$N$ 为同原泛像在 $D[s]^{4367}$ 中的饱和交，$C=N/L$。原 global Z 来源给

$$
r(s)=A(s)y(s)/127\in N,\qquad 127[r]=0\text{ in }C.
$$

原泛函 $\ell$ 在 $s=63$ 处杀 $L$ 与 $127N$。故非零读数证明

$$
[r]\ne0\text{ in }C/127C.
$$

这里的有限 $D$ 模性质来自[原无穷远127完整同谱证明](../results/R150-appendix-complete-original-infinity-prime127-spectrum66-and-affine-gauss-bound299.md)：同Q的自然无穷远长度66给某原最大minor的 $u^{66}$ 首项为127单位，而Q上更低项为零；其原参数行列式遂有127单位首项并湮灭 $N/L$，故 $C$ 在 $D$ 上有限。没有挪用31的单位首项。

这付出至少一个指数恰为 1 的系数 127 扭方向，而不仅是在模 127 中出现一个参数根。有限 $D$ 模的 $127$-torsion 与其约化的映射，在指数大于 1 的循环块上为零；所以这种非零读数确实贡献第一系数页。

结合已付 whole affine 长度 299 与
results/R150-appendix-exact-external-reduction127-and-zero-quotient-defect.md
中的 $J_{127}=0$，有 $\dim_{\mathbb F_{127}}C/127C=299$。因此正结果给

$$
\deg\Delta_{\mathbb Q}=\operatorname{rank}_D C\le298.
$$

该推论仍不单独付 $\mu=1$、九个 $h^*t_j$ 的 Q 原来源、其余 primary 的系数 127 饱和性，或后继高阶 lifting。负结果也不证明 $\deg\Delta_{\mathbb Q}=299$。

## 6. 有界执行与恢复

同 run 43772109844 的实际目录；不需要新历史输入：

~~~text
python {scripts}/2026-11-16-r150-original127-root63-source-bockstein-789f.py
  --model-out {work}/original127-model-all6188
  --normal-forms-out {work}/original127-normal-forms-all6188
  --gb-out {work}/original127-complete-graded-module
  --whole-out {work}/original127-whole-torsion
  --primitive {work}/original127-inputs/original-primitive-integer-equations.json.gz
  --sources-root {scripts}
  --out {work}/original127-root63-source-bockstein
  --seconds 180 --memory-mib 1024 --compile-seconds 30
~~~

外层墙钟 240 秒。只依赖已成功的 model/NF/GB/whole 步骤。所有已完成阶段以本源码、真实输入字节、三项父 binding 及相同 $p,\alpha$ 绑定；预算和临时路径不改变数学 binding。phase gzip 与每个输出文件均完整核 SHA。scalar 中断点为完整原事件，反向来源阶段若超时则保 scalar 完成结果，后继只重做尚未完成的反向阶段。

原小回执名 original127-root63-source-bockstein-receipt.json。预算或异常的 type/message 同时写入 parameters.error，保留小回执 sanitization 后的真实诊断。完整数组只在临时目录；Git 只保存源、参数、接口及小执行回执。新段没有运行旧 NF、GB 或 whole torsion。
