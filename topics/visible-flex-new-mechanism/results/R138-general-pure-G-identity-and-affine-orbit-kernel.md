# R138：G 的一般 pure 原算子恒等式及整个仿射轨道的纯模态消去

日期：2026-11-14。**已证明。** 本文把 R123 的一个 $m=8$ 阳性投影提升为任意同右 collar 复 profile 上的完整 pure 原算子恒等式。证明用公开 Actions 上的一条有限有理原式归约，不作任何新的 profile 评价、幂尾代入或 mixed 响应计算。

准确结论是

$$
\boxed{G_{-4}(q)=\frac1{128}\mathfrak B_{p_2}(W_1)_{-4}(q).}
\tag{1}
$$

因此整个真实仿射轨道 $\mathsf P_{H,d}G$ 的 pure 分量都在一般 pure 响应像中。它们在完整 $\mathcal U_4/\mathcal R_8$ 中仍可非零，并可选择 pure 恒零的完整代表。本文不证明整个 $\mathcal U_4$ 的一般 pure 像等于响应像，也不支付完整 mixed、ruling 或有限等距族。

## 1. 定义、槽位和同一个右锚

继续采用 [R117](R117-static-weight-one-reduction-and-reciprocal-costs.md) 和 [R118](R118-static-G-exact-separation-and-nonzero-fourth-cost-quotient.md) 的 G：它是已发完整静态局部密度中几何键

$$
(1,3,0,0,0,0,0,0)
$$

的系数，再投影到真 profile 仿射权 1。其完整两个模式原根均由原公开导出固定；本次只处理 $-4$ 分量。

令 $P=A_{p_0}$、$Q=A_{p_2}$ 为真实八矩二次算子。对共同右锚 r 置

$$
J_0(f,g)(\xi)=\int_\xi^r f''(\eta)g''(\eta)\,d\eta,
$$

$$
J_2(f,g)(\xi)=\int_\xi^r
\bigl(\eta^2f''(\eta)g''(\eta)+2f'(\eta)g'(\eta)\bigr)\,d\eta.
$$

由 R73 的原八矩公式准确得到

$$
\begin{aligned}
P(f,g)={}&\frac12(fg'+f'g)-\frac\xi2f'g'
-\frac{\xi^2}{4}J_0(f,g)+\frac14J_2(f,g),\\
Q(f,g)={}&-\xi fg+\frac{\xi^2}{2}(fg'+f'g)
-\frac{\xi^3}{2}f'g'-\frac{\xi^2}{4}J_2(f,g).
\end{aligned}
\tag{2}
$$

R116 的 retained 第三模板索引 1 是

$$
W_1(a;b,c)=P(a,Q(b,c))-Q(a,P(b,c)).
\tag{3}
$$

后两个槽对称，外槽不能与它们随意交换。二次算子 $p_2$ 是八矩索引 2，所以 (1) 使用的确为 R123 的原响应列

$$
8\cdot1+2=10.
$$

所有 q 都是普通复 $C^\infty$ profile，在共同右 collar 上为零。本文的原式积分约定是 signed

$$
I(F)(\xi)=\int_r^\xi F=-J(F).
$$

没有改变右锚，没有独立指定任何 primitive 的值，也没有把左端常数或 period 置零。原算子含全部相位系数；不是去掉 $1/16$ 的 forcing 片段。

## 2. 完整 pure 响应与一个简短显式表达式

令

$$
\tau(q)=W_1(q;q,q)=P(q,Q(q,q))-Q(q,P(q,q)).
$$

[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md) §3 的原相位公式给

$$
\mathfrak B_Q(W_1)_{-4}(q)
=\frac18\left(D\tau(q)[Q(q,q)]-2Q(q,\tau(q))\right).
\tag{4}
$$

这里 Fréchet 微分同时微分实际 jets 和同锚 Volterra 原函数。因内槽对称，(4) 也准确等于

$$
\frac18W_1(Q(q,q);q,q)
+\frac14W_1(q;q,Q(q,q))
-\frac14Q(q,W_1(q;q,q)).
\tag{5}
$$

式 (5) 与完整 R78/R89 的 $-4$ 响应一致。故 (1) 中不再附加 $1/16$。

若写 $a=P(q,q)$、$b=Q(q,q)$，则 (1)、(4) 给 G 的一般 pure 分量如下短原式：

$$
\boxed{
\begin{aligned}
G_{-4}(q)=\frac1{1024}\bigl\{
&P(b,b)+2P(q,Q(q,b))-Q(b,a)\\
&-4Q(q,P(q,b))+2Q(q,Q(q,a))
\bigr\}.
\end{aligned}}
\tag{6}
$$

(6) 的五项由 (3) 的真实链式微分直接展开，没有把外槽对称化。它与原 G 的 231 项展开是同一完整 pure 函数，下一节给出其可复现的有限原式证书。

## 3. 有限有理原式证明

公开运行：

- run **43654909901**；
- source **82a3dae98e471c80b1fa5f50ce752584626fb399**；
- lane `general_pure_G_identity`；
- 源码 [literature_general_pure_G_identity.py](../scripts/literature_general_pure_G_identity.py)，18430 bytes，SHA-256 `a6731a1c0b4940aadc689f97b9d516029518697619986aa7577b79a71ba5bcc7`。

消费器从 run 43645177423、source 2f1b809c0b0abb7a26303d36940edc203815f872 的原静态 DAG 恢复 G 和 W36。它复用冻结 G helper 的完整来源门：主报告、真实终端 publisher receipt、run/source、压缩与原文 SHA、430 个原 roots 的内容 hash、36 个 retained 原模板和原 v2 receipt 全部匹配。

旧主报告的 `output_limit` 原样保留。这一状态只对应当时主摘要超过限制；完整导出已成功并由实际发布 receipt 绑定。没有通过改写完成状态来消费原式。

本次固定比较的内容身份为：

| 对象 | 原 terms | SHA-256 |
|---|---:|---|
| 原 $W_1$ | 原模板保完整 | `74989d9bb1c98d42670b014315707d42bf4cd936c4b1f9251e67badda4462b13` |
| 对角 $\tau$ | 保完整 | `bf707582d52ef79edf067d143718317c0250be07660cd70f141fdbad2299c9ba` |
| 原 $G_{-4}$ | 231 | `4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a` |
| 新 $\mathfrak B_Q(W_1)_{-4}$ | 243 | `def0d761eeec6781e03f455e3e7b91b4fc91c243096bd501506dc17cf06176cd` |
| 整条原差 $G_{-4}-\mathfrak B_Q(W_1)_{-4}/128$ | 398 | `d78a3284957e93f6d2569597f0e8ce992b3fa97424c6edcefd28d57682db1b1f` |

所有系数运算在 $\mathbb Q$ 中进行。先对原 $W_1$ 同时代 $a,b,c\mapsto q$，再用冻结 `Ring.variation` 精确生成 (4)。G、响应及原差均保持 profile 次数 4、真仿射权 1；没有截断、profile 求值或幂尾替代。

对上述完整 398 项原差，冻结 `ProfileNormalizer` 依次作 sound 同右 collar IBP 与 word/shuffle，最终准确得到空表达式：

$$
\operatorname{NF}\left(G_{-4}-\frac1{128}\mathfrak B_Q(W_1)_{-4}\right)=0.
\tag{7}
$$

空表达式 hash 为 `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。

为何 (7) 是原函数证明：每个 right-IBP 重写只使用真实乘积求导与积分分部；需要边界消失时，所取原函数具有严格正 profile 次数，在共同右 collar 上为零。非空迭代 word 的右边界也为零。乘积使用同右锚的完整 shuffle 恒等式，未把这些 words 假设为线性独立。最终是从原差通过函数恒等式得到零，而不是从不完备正规形的非零结果推断函数非成员。

实际记录有 173 次 unique-high-jet IBP、14 次 first-level shuffle、6 次 all-depth shuffle、12 次 nonempty-word polynomial IBP；两层 cycle fallback 都是 0。该有限计算已终止，不需任何正规化完备性假设。由此 (7) 推出 (1)，再由链式法则得到 (6)。

本轮只新建 **1 个 pure 响应**；新 mixed 响应、profile 评价、幂尾代入、旧 W 或局部 density 编译次数全部为 **0**。实际耗时 **1.5530076009999974 秒**，峰值 RSS **123.9921875 MiB**。同 job 的六项新人工先运行且全部通过；它们只核相位、外槽/内槽、同锚、$1/128$、颜色和原 DAG 往返，不承担研究结论。

## 4. 完整证书和可复现入口

公开目录：

`notes/actions-43654909901-1-general_pure_G_identity`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [general-pure-G-identity.json](../notes/actions-43654909901-1-general_pure_G_identity/general-pure-G-identity.json) | 16657 | `c02d93afbe3eedd8586d000675194a8573813ff88b3cbbc6fe40437f0d3f6eae` |
| [general-pure-G-development.json](../notes/actions-43654909901-1-general_pure_G_identity/general-pure-G-development.json) | 5576 | `585476c0d7babdbe4d86adf6fcb7c51371bff9eb8546ac7b8e72ee65e9f93b4d` |
| [receipt.json](../notes/actions-43654909901-1-general_pure_G_identity/receipt.json) | 34808 | `385d82c3d2f71a4047f4685518108ce4e76569795899f63a66855709b126c30d` |
| [general-pure-G-identity-certificate.json.gz](../notes/actions-43654909901-1-general_pure_G_identity/general-pure-G-identity-certificate.json.gz) | 9533 | `412dbe8f76e69650818383a9531902a808256a5371cccd49b67bdf962c3a0de0` |
| 上项解压原文 | 38766 | `d0f7de98869865b0a871bbc3127907aab50d62013ad518d61d2272408a8f363a` |

完整证书保存五个原 roots：$W_1$、其对角、$G_{-4}$、新响应和完整原差；保完整可达 atom DAG、每根原 hash、全部来源、整条 NF 和实际重写统计。它不只有一句 `passed`，也不需要重编旧 forcing 或旧响应组。具体参数和来源路径在 [消费设计](../notes/general-pure-G-fixed-identity-design-20261114.md) §5；真正研究入口只允许运行于本公开仓库 Actions。

## 5. 整个仿射轨道的一般 pure 像已经支付

记 $\pi V=V_{-4}$ 为一般 profile pure 投影，$R=\mathcal R_8$、$U=\mathcal U_4$。它们与 R133 的幂尾代入不同。

[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 的真实变换 $\mathsf P_{H,d}$ 对所有输入、jets 和右锚同步作用，不改变相位角，所以

$$
\pi\mathsf P_{H,d}=\mathsf P_{H,d}\pi.
\tag{8}
$$

R89/R105 同时证明 $\mathsf P_{H,d}R=R$。令完整响应 $K=\mathfrak B_Q(W_1)\in R$，把已证 (1) 输运，得到

$$
\boxed{\pi(\mathsf P_{H,d}G)
=\frac1{128}\pi(\mathsf P_{H,d}K)\in\pi R.}
\tag{9}
$$

因此所有平移导数 $N^jG$ 的 pure 分量也属于 $\pi R$；这来自有限真实仿射表示的线性系数比较，不是再次作 profile 测试。

令 R122 的控制子空间为

$$
Z=R+\operatorname{span}\{\mathsf P_{H,d}G:H>0,d\in\mathbb R\}.
$$

准确结论为

$$
\boxed{\pi Z=\pi R.}\tag{10}
$$

[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 已证明 $U/Z\ne0$，故 (10) 不能扩大为整个 U。R122 的新增轨道控制仍对完整两模式有作用，但没有扩大一般 pure 响应像。

## 6. 非零完整商可用 pure 恒零代表

由 R117/R118 的真实成本论证及 R130，$G\in U$；由 R105，$K\in R\subset U$。定义

$$
H_0=G-\frac1{128}K.
$$

由 (1) 与 R118 的完整非成员结论，

$$
\boxed{\pi H_0=0,\qquad[H_0]=[G]\ne0\quad\text{于 }U/R.}\tag{11}
$$

故其完整 $-2$ 分量非零。不能进一步自动断言 $(H_0)_{-2}\notin\pi_{-2}R$：某个响应也许能匹配 mixed 分量，却会带来不需要的 pure 分量；完整商与单坐标投影商必须区分。

更一般地，(10) 使包含映射诱导准确同构

$$
\boxed{\frac{Z\cap\ker\pi}{R\cap\ker\pi}\ \simeq\ \frac ZR.}\tag{12}
$$

证明：任意 $z\in Z$ 都有 $r\in R$ 使 $\pi z=\pi r$，故 $z-r\in\ker\pi$ 且与 z 同商类，映射满射；其核恰为 $R\cap\ker\pi$。因此整个 G 轨道商都有 pure 恒零的代表，其维数恰为 R122 的 s；[R139](R139-fifth-G-translation-separation-and-188-query-control.md) 的 G 至 $N^5G$ 完整非成员现已给 $s\ge6$。

(11)–(12) 在真实线性 span 中成立，不是一个实际成本取负的构造。R122 的有限联合查询控制仍须保各 prototype、连接、共同 I 和全部基准；不能把线性组合 $H_0$ 自动称为某条实际路径的成本。

## 7. 后继准确问题

R130 给

$$
U=R+K_{\rm norm},
$$

其中 $K_{\rm norm}$ 是完整八矩归一化和真实水平 IBP 后 14 个状态函数族的值 span。因此一般 pure 完整支付仍恰需

$$
\pi K_{\rm norm}\subseteq\pi R.
\tag{13}
$$

本稿付清 G 轨道的 pure 部分，尤其包括 R117 的归一静态最高剩权 $h(k^3-k)G$。它没有支付 (13) 的其余静态低权、速度二次、加速度二次、面积型和速度四次族。下一原式门应消费已经导出的正规系数，复用 R133 的候选响应组合并回到原函数核实，不再检验已经成立的 (1)，也不重跑 m8。

R134 的三 $\overline A$ 与两 H 只由已发 $v_4$ 决定，可先复用并行消费导出的完整原根。一般 pure 的阳性和完整 mixed 的新商都必须分别保真；即使未来 (13) 成立，完整 mixed、第四 ruling、更高阶收敛、闭嵌入、全时 reach 和宏观幅度仍是未付终局。
