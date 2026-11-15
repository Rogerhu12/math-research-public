# 原自然无穷远的特征零十三核、指定自由归一与删十三输出投影

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。

## 1. 当前状态与完成对象

本文件锁定一个新的可执行入口；此时只已完成源码静态推导与冻结，尚未执行 Python AST、FLINT 或本题的特征零计算。首次真实解析、时间和结果由根代理安排的 Actions 回执记录。

入口使用同一原矩阵 $A^\infty(u)$，保留其全部 $4367$ 个输出、$6188$ 个来源、自然参数 $u=1/s$。它从原十七式重建三个泛型核泛函，连同十个纯切向泛函组成十三列，再在已经实际使用的十三个**原输出坐标**上归一化。只有全部坐标在 $u=0$ 无极点，且完整来源乘回为零，才证明这十三列是 $\mathbb Q[[u]]$ 上完整的原始形式左核基，随后计算同一 $I^c$ 的投影阶。

代码：

- 路径：topics/invariant-subspace-problem/notes/2026-11-15-r150-original-characteristic-zero-free13-projection-789f.py
- Git blob：5fd988245dfa29bf9c5acc3c40f62f5af92864ce
- 字节：30044
- SHA256：d9bf01ed8f621345104fb63805f298ecf72348a07c83c93c0bc6a1b6f16f1f6b

只新增至多 $17\times9$、$9\times9$ 和 $13\times13$ 的精确多项式/有理函数操作，不重做任何 $4318$ 或 $4340$ 阶消元。源码使用 python-flint 0.9.0 的公开接口；参考 [fmpq_poly 官方接口](https://python-flint.readthedocs.io/en/latest/fmpq_poly.html) 与 [fmpq_mat 官方接口](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html)。

## 2. 精确输入

所有输入先逐字节检查，路径不进入数学绑定。原历史二进制只临时恢复，不重新发布。

| CLI 输入 | 字节 | SHA256 |
|---|---:|---|
| primitive-equations | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| physical-generator | 15328 | 2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186 |
| paid-full-summary | 35730 | 2782f380fe5731fd4766fb05fa94a6fa38c36d2d5e491bd63dd1149adc3a9388 |
| paid-projection-summary | 20819 | 28b2605d03746fb5d1a4398c36d22650239d7989f5b68463ed9d6c9f99c5f830 |
| generic-rank-proof | 9957 | b803d92f159bf26bc9b4a80bbaf5a150ff8f17e81e201b0a99e845b7777038e4 |

原 primitive 历史定位为提交
$8c6304e273e64b0544d3dd58bc0e48a672a87c36$，仓库路径：

`topics/invariant-subspace-problem/notes/r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz`

解压后 SHA256 还须等于
`fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3`。

其余四件是既成小文本：

- 物理生成器：`notes/2026-11-15-r150-original-transverse-first-connection-789f.py`，blob `fc2e61ef9e32c8c14dc682969dd7e5bc9015767e`。
- full 小摘要：`notes/r150-full-infinity-dual27-session-789f/43731615668-full-infinity-original-dual27-v2-through21.json`，blob `920b3d22182f9a766983aab8db04db58fd44e5ef`。
- 投影小摘要：同目录 `43731615668-full-kernel-deleted-original-output-projection.json`，blob `5617487c9fbd2e79b8fb7b2fcce8d83cdc14e509`。
- 泛秩证明的同字节副本：`notes/2026-11-15-r150-full-infinity-generic-rank-proof-source-789f.md`，blob `3b7a938b65f2864e8d0ac315acfee8e5a11fef5b`。原正式结果为 `results/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md`。

所有 notes/results 路径均相对课题根目录。

## 3. 同一个自然参数、原行与完整多项式运输

自然矩阵的定义是

$$
N^\infty(u,m)=Q(m)+u^{10}L(1/u)m,\qquad
\Gamma^\infty(u,m)=u^5\Gamma(1/u,m).
$$

这些 $u$ 权是原齐次图的定义；本入口没有把从裸 $A(1/u)$ 到自然图的过程称作单位缩放。

**在已经定义的自然图内**，取
$K_\infty=R_6KR_6$，反转十一项矩序列，并分别反转十一条 $N$、六条 $\Gamma$。随后采用

$$
m_i^{\rm old}
=\sum_{j=0}^{10-i}\binom{10-i}{j}u^{10-i-j}z_j,
\qquad c=z_0,\quad d=z_1.
$$

反转是常数置换，二项式平移的行列式为 $1$。它们在全部次数至多三的来源乘子与次数一至五的输出空间上诱导多项式单位变换。没有删去任何原来源。

程序由反转后的原 $K,J_2,J_3$ 重建 $y(u)=(1,u,\ldots,u^5)$ 的完整六个系数映射，逐一生成原物理 $N,\Gamma$ 的全部自然参数系数。利用十一基向量的正负代入与五十五个交叉代入，恢复全部 $17\times77$ 个线性/二次矩变量系数多项式。

对 primitive 原式，直接做自然参数倒序与相同的变量、方程反转；每条方程求唯一**非零常数**比例，再核它的全部系数。共 $4433$ 个既有原参数坐标全部保留，原整模型的固定分母与行比例还须是 $31$ 的单位。比例不是从旧命名或点值猜测得到。

完整二项式平移之后，各式的纯切向项必须只可能含 $d^2$，而六条 $\Gamma$ 的全部纯项为零。代码逐多项式检查这一点。

## 4. 原九维线性块与十三个泛型核

把 co-moving 原式记成 $F_e$，令

$$
H_{ej}=[z_j]F_e,\quad
C_{ej}=[cz_j]F_e,\quad
D_{ej}=[dz_j]F_e,\quad
q_e=[d^2]F_e,\qquad 2\le j\le10.
$$

程序直接在原 $17\times9$ 多项式矩阵 $H$ 上作分数无关选行，得到一个真实非零的九阶多项式子式。它没有用模素数 profile 代替有理可逆性，也没有在参数点抽样。

同一九阶块经 Bareiss–Montante 求逆；每次多项式除法必须整除，最终全部 $81$ 个原块乘回坐标必须为单位阵。然后构造

$$
Hr=-q,\qquad Hr_c=-Cr,\qquad Hr_d=-Dr.
$$

每个等式都再核**全部十七行**，而不只核选中的九行。

十个纯泛函取出 $c,c^2,\ldots,c^5$ 以及 $d,cd,\ldots,c^4d$。其余三个的非零支撑为

$$
\begin{aligned}
&\varphi_2(d^2)=1,\quad \varphi_2(z_j)=r_j,\\
&\varphi_c(cd^2)=1,\quad
  \varphi_c(cz_j)=r_j,\quad\varphi_c(z_j)=(r_c)_j,\\
&\varphi_d(d^3)=1,\quad
  \varphi_d(dz_j)=r_j,\quad\varphi_d(z_j)=(r_d)_j .
\end{aligned}
$$

这些公式的来源是已推泛参数原十三核定理。本次还会执行完整 $6188\times13$ 精确乘回；不以引用替代本次身份核验。

## 5. 固定原自由坐标与原始性

同已完成 full/G 回执一致，零基原输出索引为

$$
F=(3001,3002,4002,4003,4288,4289,4353,4354,4355,4363,4364,4365,4366),
$$

$$
I^c=(3001,3002,4002,4003,4288,4289,4354,4355,4362,4363,4364,4365,4366).
$$

程序从两份实际小回执读取并核对这些索引，还核全部十三个被删输出的原单项式 key。二者只相差：$F$ 中的 $m_9^2$ 换成 $I^c$ 中的 $m_6$。

先将十三个泛型核在 $F$ 上评价，求其真实有理函数逆矩阵；随后整体乘此逆矩阵。全部 $13^2=169$ 个原自由块坐标必须恰为单位阵。

归一化可能引入极点，所以**完整 $155\times13$ 支撑的每一条有理函数**均约成互素分子、分母后，检查分母在 $u=0$ 非零。其余 co-moving 输出坐标严格为零，原 $4367$ 坐标再经上述多项式单位运输，故这一检查确覆盖原核全向量。

若该检查成功，令归一化矩阵为 $K$。由完整乘回与原泛秩 $4354$，它在 $\mathbb Q((u))$ 上是全部十三维核的基。任意形式核 $v$ 可唯一写为 $K a$。因为 $K_F=I_{13}$，有 $a=v_F\in\mathbb Q[[u]]^{13}$；因此

$$
\ker_{\mathbb Q[[u]]} A^\infty(u)^T
=K\,\mathbb Q[[u]]^{13}.
$$

这同时证明完整性与原始性，不从泛型维数或模 $31$ 结果免费推出。

若出现极点，入口保存实际极点位置与已完成阶段，返回
`fixed-original-free-chart-not-regular`；不会登记 primitive13 或特征零投影阶。此时需真正的列饱和或另一合法局部基，不能丢掉极点。

## 6. 完整乘回与投影阶

每个归一化核列统一清一个在 $u=0$ 非零的多项式分母。程序对原十七式乘**全部 $364$ 个**次数至多三的 co-moving 乘子，执行

$$
6188\times13=80444
$$

个精确多项式产品检查。co-moving 来源基是完整原来源基的多项式单位变换，因此这确实验证原矩阵核。回执准确记录：
`directUntransformed6188PolynomialMultiplicationPerformed=false`；
没有把经过已核单位运输的乘回冒称在未变换矩阵上再次直接相乘。

随后保存全部 $4367\times13$ 原输出坐标，逐项核原自由块。令

$$
G=K[I^c,:].
$$

十二个共有原输出仍给十二个单位行。程序依实际排序计算 cofactor 符号，再把 $\det G$ 化为余下一个有理函数条目，完整保留精确分子、分母与 $u$ 阶。若阶为 $\lambda>0$，$G$ 的十二个因子为单位、唯一正指数为 $\lambda$。

本次可用的特征零交叉上界是原 $A_I$ 的联合子式界：

$$
\delta(A_{I,\mathbb Q})\le68,\qquad
\delta(A_{\mathbb Q})\ge43
\quad\Longrightarrow\quad
\lambda_{I,\mathbb Q}\le25.
$$

这不同于把有限域 $\lambda_{I,31}=2$ 直接提升。

此外，只有全部归一化核条目都实际拥有“分母常项为 $31$ 单位、全部系数 $31$ 整”的表示，程序才将其投影行列式模 $31$ 的前十一项同原实际回执

$$
(0,0,13,10,0,11,28,29,13,17,8)
$$

比较。仅行列式自身可约模 $31$ 不足以执行这个比较。该额外检查不替代特征零正则性与原始性证明。

## 7. CLI、预算与恢复

建议在新临时 session 用以下参数：

```text
--primitive-equations {work}/inputs/repo/original-primitive-integer-equations.json.gz
--physical-generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
--paid-full-summary {scripts}/43731615668-full-infinity-original-dual27-v2-through21.json
--paid-projection-summary {scripts}/43731615668-full-kernel-deleted-original-output-projection.json
--generic-rank-proof {scripts}/2026-11-15-r150-full-infinity-generic-rank-proof-source-789f.md
--out {work}/original-characteristic-zero-free13-projection
--seconds 180
--memory-mib 1024
```


不编译 native，不安装新包。数学时钟从读入、散列与构造阶段开始；建议 outer timeout 为 $210$ 秒。SIGTERM/SIGINT 请求安全边界停，只有已完整写入并核 SHA 的阶段可复用。不是每个底层 FLINT 调用均可中断，超时时按实际回执与保存阶段报告。

四个完整阶段分别保存原多项式、原九块与泛型核、原自由归一、最终完整核/投影。数学绑定包含源码 SHA、所有输入 SHA、两个实际坐标集合与自然参数规范；绝对路径和预算不进入绑定。跨目录续接使用相同源码与输入字节，逐阶段核 SHA 后只重做未完成部分。

临时压缩矩阵、核、cache 不进入 Git 或 Release；仅小源、参数、运行号与 SHA 摘要长期登记。主回执为：

`original-characteristic-zero-free13-projection-receipt.json`

成功要求 `status=completed`、`outcome=complete-characteristic-zero-original-output-projection`，并且以下身份全真：

- `all4433OriginalParameterCoefficientsVerified`；
- `all17WholeNaturalPhysicalPolynomialsMatched`；
- `sameOriginalNaturalUAndReversedPhysicalKernelVerified`；
- `actualOriginalNineByNineRationalProductsVerified`；
- `samePaidOriginalFree13IdentityVerified`；
- `all155NormalizedCoefficientsRegular`；
- `all80444CoMovingOriginalSourceProductsZero`；
- `all4367OriginalOutputCoordinatesTransported`；
- `primitiveFormalKernelProved`；
- `completeCharacteristicZeroOutputProjectionComputed`。

完成值在 `characteristicZeroOutputProjectionLength`；精确投影分子、分母、符号及可执行的模 $31$ 对照均在 parameters。

超时返回 $75$ 并保实际完整阶段；坏输入或身份失败返回 $1$。固定自由图不正则也返回 $75$，但其 outcome 与预算耗尽明确区分。

即使全部完成，本入口仍保持
`characteristicZeroFullSmithComputed=false`、
`selectedLeadingCoefficientUnitProved=false`。
它只计算原始十三核的指定输出投影，不宣称原大方阵首项为 $31$ 单位，不宣称已经求出完整特征零 Smith 谱。
