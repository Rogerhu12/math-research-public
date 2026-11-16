# R923 原两端目标正规函数：执行方法、精度和原来源合同

本文固定 R923 的一个公开 Actions 消费范围：在 R917 **已经实际认证**的两个原 rank-eight 正规 order 中，计算原目标函数 $V=q^*w$，继而计算全部 $272$ 个原目标正规函数。数学定义和整性证明使用 [R923 证明](../results/R923-original-target-normal-coordinates-in-certified-endpoint-orders.md)，固定 SHA-256 为：

~~~
d0c2ceada8d5d2888efe8258a390d4625ad4193958d840332f3830733ef9fc97
~~~

此处辅助特征始终为 $\ell=1000000753$，$\zeta=549966761$，$s=99932770$。下文的 $273,271,267$ 和输出精度均为原局部参数 $\rho_\epsilon$ 的系数精度，**不是** $41$-adic 球的精度。

## 1. 真实入口与本次出口

两个端点是原 $P_0,P_1$，参数分别为

$$
\rho_0=z-z_0,\qquad \rho_1=\iota^*\rho_0=z-2\beta_{72}-z_0.
$$

直接消费 R917 已成的共同清分母十七列、primitive order、primitive discriminant、一次 idealizer 后的完整正规 order、全长八特殊纤维和原标记帧。原始 $\widetilde P_8$ 是单位，实际 $h=0$；primitive 精度为 $273$、判别式阶为 $6$；正规 order 精度为 $271$、判别式阶为 $4$、指数长度为 $1$。这些是已有源的实际字段，程序逐项核对，不重新计算 idealizer、原 $273$ 个局部 jets 或原对应系数。

本次的成功出口是两端全部 $272$ 个正规函数的完整八坐标，加上原式逐坐标乘回证书。实际共同分母阶 $d_\epsilon$ 由本次运算读取，不能预填。请求只设最小输出精度 $1$；实际成功时保留全部 $267-d_\epsilon$ 项。

原 $P/K$ 仍由 R873 的准确 unit-solve DAG 定义。所有新数组均明确标为辅助特征下的局部值；不把这些数组称为特征零展开系数，也不把它们称为五个目标理想、$\operatorname{Nm}\Phi\det U$、参考帧数值或高度。未来 R903、R907 输入在首请求中均为 null。

## 2. 四组原数学来源、两个现行运输源

直接下载的两个已结束产物如下。下载使用已冻结 R824 标准库 Range helper；每个选入文件逐 bytes/SHA 核对，未整包下载时不宣称整 ZIP 已重新哈希。

| 运输源 | 真 run / source commit | artifact / ZIP bytes / SHA-256 |
|---|---|---|
| R917 | 43904492746 / 64228da6693769dcf70fb8bcaec4a72ad0faa445 | 14244312360 / 13739001 / 4ae6c58082f591a195978646039658a40c850df5c8c66803de234f29b7eb3056 |
| R885 polynomial producer（POLY） | 43842694142 / 0210f90f1ac7d2c89e948cae0cdc5f64f775dc07 | 14214590084 / 64381078 / 42bebd740b7bf4535ac7af50f072bcac8d1b7fc3a29796c43ad218c5c140021b |

R917 manifest 为 $32468$ bytes、$184$ 条，SHA 为 d8bac1cf2d29e385afd7222d87805506732e2dfecc440980b187e6112bb2af2b。其实际 FINAL 为 $13981$ bytes、cf539a58a7ab8212bb0e0d56c9621c2c6916ca25c2cbc3b50ce7be3890c15349。

POLY manifest 为 $77918$ bytes、$560$ 条，SHA 为 51dff64343665bf629603f42e43cc21ecc10aaf17912df5cc6f20bb7b8973154。其实际 FINAL 为 $7104$ bytes、fc323a7d1b74a03ff3c846c2dfa92e4cd7c5269b20b3eebd857439e727d73d30。

四组数学来源是：

1. **R917**：原 FINAL、source audit、stage manifest、两端九个指定阶段及原 metadata。阶段的 plain spec 从原 completed-endpoint certificate 和原 manifest 展开，禁止猜 bytes/SHA。
2. **POLY**：完整原 $272$ 个 polynomial-adjugate row levels、原 row index、全局 characteristic relation、原 FINAL 和 metadata。所有 row spec 由原 index 的 ordered entries 展开；逐项保 $b$-level 与 $T$-power。
3. **R827**：原四系数矩阵 $W(z)$、原 place audit 和原 metadata/manifest。仅从 POLY 已保留的 R885-retained-R827-inputs.tar.gz 中恢复原字节。原 R827 运行以 exit $124$ 结束、没有 FINAL；只消费其 complete=true 的旧 $W$/place 阶段，不要求不存在的整体成功证书。
4. **R873**：原准确对应 DAG、十七系数 unit-solve 表达式、原 FINAL 和 metadata/manifest。从 R917 的 R917-retained-original-inputs.tar.gz 恢复。

两个父 carrier 都按其原 inventory **逐成员哈希完整读取**：R917 的原 $40$ 件、POLY 的原 $15$ 件。随后仅保本消费者所需的原件，原 result、configuration、core/source SHA 均不改名。请求不再访问原 R873 或 R827 的旧平台产物，也不依赖代理本机缓存。

wrapper 在实际 prepare 后写四组 sources.files、selected_file_count 和 selected_files_sha256，并放入新展开配置。新载体为 R923-retained-original-inputs.tar.gz；manifest、inventory、receipt 和原数学 source identity 同时保留。运输路径不进入数学 tag，实际选件及其字节指纹进入 tag。

## 3. 原基方向与第一次商

原正规 order 的表约定为 table[left][right][output]。basis_in_primitive_Theta_powers 是列为新基坐标的矩阵 $B$；primitive_Theta_powers_in_basis 是按行存储的通常矩阵 $B^{-1}$。旧 helper 的 primitive_coordinate(j) 明确读取其第 $j$ 列。新消费者使用 $B^{-1}$ 左乘 primitive 坐标列，绝不转置，也不改旧 helper 全局常量。

记

$$
m=\widetilde P/\widetilde P_8,\qquad
b=\widetilde K/\widetilde P_8,\qquad M=M_{m'}.
$$

在旧 **primitive $273$ 精度**乘法表中构造 $M$ 的八阶 adjugate。算法用七次 Newton 矩阵递推，只逆常数 $1,\ldots,7$；完整核验左右两个 adjugate 乘积。其标量必须逐系数等于原 R917 已成 primitive discriminant；不重新计算旧 trace Gram 或旧判别式。

随后形成

$$
n=B^{-1}\operatorname{adj}(M)b.
$$

全部 $8\times6$ 个低阶系数必须准确为零。先除 $\rho^6$，再逆旧判别式的单位部分，从而保留 $267$ 项的 $V$。这里运输先于除法，因此不因正规表只有 $271$ 项而无谓少取两项。完整核验

$$
\partial_U\widetilde P(U)\,V=\widetilde K(U)
$$

在原八维 order 的所有坐标中成立。$V$ 的定义始终是 $\widetilde K/\partial_U\widetilde P$，不是 $\widetilde K$。

## 4. 直接消费完整全局 row，求全部正常函数

POLY 已保存

$$
(r_0,\ldots,r_{271})=e_0^{\mathsf T}\operatorname{adj}(T I-W(z)),
\qquad r_i=r_0\beta_i.
$$

消费者按原 $272$ 个 $T$-levels 做 Horner；各 level 的 $z$ 多项式从原 source 文件读取，以旧源绑定的真实 $U$ 求值。$U$ 的 $0,\ldots,273$ 次幂按 $32$ 个一块原子保存。正常列按 $16$ 个一组，Horner levels 亦按 $16$ 个一组保存。这样每个已完成块可原样续用。

全部运算在完整 rank-eight order 内进行，保留各因子、重数和幂零元。R885 的 $z=0$ 整 Artin 目标数组不属于本次端点数据，不能拿来替代。原 $W$、原 $\chi(z,T)$、原 $273$ 节点、原 polynomial adjugate 均不重算。

先完成第 $0,\ldots,15$ 列并形成 $M_{r_0}$。一次 adjugate 和一次单位逆服务全部 $272$ 个右端。设本次实际可见

$$
d_\epsilon=\operatorname{ord}_{\rho_\epsilon}\det M_{r_0}.
$$

对每个 $r_i$，完整验证 $\operatorname{adj}(M_{r_0})r_i$ 的所有低于 $d_\epsilon$ 的系数为零，再除 $\rho^{d_\epsilon}$ 并乘单位逆，得到精度

$$
T_\epsilon=267-d_\epsilon.
$$

这是已知商整性的精度，不采用双重损失 $267-2d_\epsilon$。每块完整验证 $r_0\gamma_i=r_i$；首块还核验 $\gamma_0=1$、$\gamma_1=V$。

最后消费原四个 $W$ 系数矩阵，完整核验

$$
\gamma W(U)=V\gamma
$$

的 $272\times8$ 个局部 series 坐标，并核验 $\chi(U,V)=0$。wrapper 只读这些实际旗标、形状、来源和 SHA，不再执行矩阵或多项式运算。

## 5. 精度不足、预算与原子恢复

若 $\det M_{r_0}$ 在现有 $267$ 项内全零，只记录其 valuation lower bound，不记录“函数为零”。该端点返回 NeedPrecision；程序继续另一个端点。已完成 adjugate、首 $16$ 列、全部源和 current 均保留。

若 $d_\epsilon$ 已见但 $267-d_\epsilon$ 小于请求值，则回执给出这个实际 $d_\epsilon$、当前输出界和所需原 jet 精度。最终 complete=true 仅在两端完整 $272$ 列都通过原式时成立。两端尚未完成的范围不会被其他已成端点替代。

所有数学阶段写入根目录 R923-target-*.json.gz，经 tmp 原子替换；每个 completed stage 含相同真实新 configuration。current 为 complete=false。stage manifest 只列实际 complete 阶段，不列自身或 current。

恢复只接受同 mathematical tag 的已完成/当前阶段、原四组载体和真实来源 receipt。预算可增加。旧 false FINAL 只作历史来源，不能用它的旧 current SHA 约束较晚 checkpoint；真正成功 FINAL 则核全部 live references 后复用。硬 timeout 没有 core receipt 时，如实保 run.complete=false、core_receipt_sha256=null，不造 receipt。

首 scope 不删除完整行、Horner 块或成功坐标。原子结果及必要原输入仅保一日 artifact，原始数学数据不写 Git。

## 6. CLI、配置和输出

数学 core：

~~~
python R923_original_two_endpoint_target_normal_coordinates.py \
  --config public-actions-expanded-job.json \
  --out OUTPUT \
  --budget-minutes 300
~~~

仅在 Rogerhu12/math-research-public 的 GITHUB_ACTIONS=true 环境允许新数学。入口关闭 Python 十进制字符串长度限制，使用 python-flint==0.9.0。唯一绑定数学 helper 为已成功 R917_endpoint_order_arithmetic.py，SHA：

~~~
c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d
~~~

标准库 wrapper 仅负责规则/源码 SHA、实际源解包、child core 调用、输出逐字节核验和一日载体。它不导入或调用数学 core/helper。真实 AST 与源码 SHA 检查位于本次 Actions 的初始步骤，不另设数学试算。

数学 RESULT 为 R923-original-two-endpoint-target-normal-coordinates，FINAL 为 p41-original-two-endpoint-target-normal-coordinates-certificate.json。每个真实完成端点列出 target_w、共同 adjugate/单位逆、$17$ 个完整 cofactor 块、$17$ 个完整正常坐标块、原 $\chi$ 与全部 $W$ 乘回、实际 $d_\epsilon,T_\epsilon$ 和未改变的原 R917 帧引用。

数学 tag 固定真实 core/helper/method/proof SHA、四组原身份/选件指纹、完整输入 spec、原 place、固定算法策略与请求的最小输出精度。机器目录和运行预算不进入 tag。结果继续明确：

- 全长八端点代数与 nilpotents 保留；
- 原 $\rho_1=\iota^*\rho_0$、原 $t$、原 $\nu=82\tau\,dq_Y/q_Y$、dual-seven 两个 determinant 因子保留；
- 没有计算五目标 endpoint ideal lattices；
- 没有完成 $\operatorname{Nm}\Phi\det U$、原参考帧或 Poincare/height 数值；
- 没有将辅助特征下的坐标误称为特征零展开。

本执行只补足 R923 证明中的实际小 rank-eight 函数求值叶，后继真实理想单位框架仍须消费自己的原函数、分母与精度。
