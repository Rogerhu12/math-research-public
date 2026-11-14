# 全部正长度 reciprocal 状态的 P1：权零准确分离与同圆推论

日期：2026-11-14。完整结果 R98，消费已完成的公开 GitHub Actions，不重跑研究目标。来源为 run **43638896281**、提交 **5ba4eceb196f6c899aae45921b3802014a0e09c6**、lane `total_P1_blocks`。

## 1. 结论及准确范围

沿用 [R90](R90-seven-state-complete-response-and-positive-baseline-system.md)、[R91](R91-affine-character-dichotomy-for-positive-universal-P1.md)、[R94](R94-scaling-blocks-for-total-P1-membership.md) 的标准完整基准 $b$ 和全部状态响应空间 $\mathcal R_*$。本次实际证书证明

$$\boxed{b\notin\mathcal R_*.}\tag{1}$$

更具体地，存在定义于真实有限函数空间

$$V=\mathcal R_*+\operatorname{span}\{b_{H,d}:H>0,d\in\mathbb R\}$$

上的准确实线性泛函 $\Lambda$，满足

$$\boxed{\Lambda(\mathcal R_*)=0,
\qquad \Lambda(b_{H,d})=1
\quad\text{对全部 }H>0,d\in\mathbb R.}\tag{2}$$

因此，当前模型内任意有限多个 reciprocal 状态、任意正 bulk 长度、任意允许的独立真实第三控制，都不能给出 universal 完整 P1 恒等式。这里包括全部正整数完整圈配置，不能靠继续增加同类状态或扩大同类第三控制列消去这个门。

结合 [R96](R96-single-profile-faithfulness-for-affine-Volterra-spaces.md)，存在合法非退化 $C^\infty$ 三矩 profile 圆，使同一个固定圆上的真实查询泛函已经具有 (2) 的全状态同号性质。按 R96 的无统一导数盒、可变左 collar 约定，这类 profile 圆相对开稠密。这仍不排除所有特殊 profile 圆，也不排除其他弯曲机制或固定有限 $N$ 的 $P_0+NP_1$ 相消。

本结果没有构造主课题要求的闭面，也没有证明一般闭曲面不可弯。P0、完整第四 ruling、所有更高阶、收敛、嵌入、reach 和宏观位移均未因此完成。

## 2. 公开实际文件与来源核对

本次索引与独立块位于

`notes/actions-43638896281-1-total_P1_blocks/`。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| [total-P1-blocks.json](../notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks.json) | 50926 | `e397c05396b679b5cd1c847828e0c4812f54f7e9bc95767d0fe5ee879b84674e` |
| [total-P1-blocks-weight-p2.json](../notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p2.json) | 6234 | `abb8fb020e1a07acd8b78dccbfd9f7ccfcbde83981e6dce1c2d7400c57bfaae2` |
| [total-P1-blocks-weight-p1.json](../notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p1.json) | 7052 | `61f51d588e6409e0dc9085e93b247e0718a8c5430b5138184fffc81c70160844` |
| [total-P1-blocks-weight-p0.json](../notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p0.json) | 56173 | `1146e6789d2f842ecc255930e2394bec5073029b13dcff4cc6f1aa445d07a78d` |

四文件的原始/存储长度及 SHA、索引中三块的长度/SHA、三块同一源码集合与问题身份均已逐字节核对。九个直接数学依赖的当前字节/SHA 与报告相同；publisher 的 receipt 另外列出该来源提交的 131 个源文件，但本段不把“列出”冒充对其每个文件的独立数学审查。

主源码 [literature_total_P1_scaling_blocks.py](../scripts/literature_total_P1_scaling_blocks.py) 为 37293 B，SHA256 `40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa`。实际问题身份为

`f41d89d4e49618c80a105b270c6dbcf94099b6ffa84d374ed523fe89349c9b8b`。

运行完成用时 37.240391258 秒，RSS 峰值 90.83203125 MiB。状态为 `complete`，三个实际块依次为 `member_identity_verified`、`target_zero_verified`、`nonmember_certified`。这不是资源退出，也不是由非零 word 余项单独作出的阴性判断。

## 3. 两个更高权已经准确支付

按 R94，将完整原式标准基准分解为有限权和

$$b=\sum_{n=-8}^{2}b_n.$$

实际原式清单没有高于 2 的权。记

$$\tau_{i,j}(f;g,h)
=\Phi_i(f,\Phi_j(g,h))-\Phi_j(f,\Phi_i(g,h)),$$

与已冻结 producer 的原始括号方向一致。权 2 的两个原列是

$$\mathcal B_{\Phi_{p_2}}(\tau_{p_1,p_2}),\qquad
\mathcal B_{\Phi_{p_2}}(\tau_{p_2,t_1}).$$

该块从原始常态目标、原始端点基准及原模板 fresh 复核了两个模式的准确恒等式

$$\boxed{b_2=-\frac14\mathcal B_{\Phi_{p_2}}(\tau_{p_1,p_2}).}\tag{3}$$

因此 $b_2\in(\mathcal R_*)_2$。这里没有另称两列已经数值证明独立；成员恒等式本身足够。

权 1 也从完整原式同时核对两模式，得到

$$\boxed{b_1=0.}\tag{4}$$

这些原式等式是后面得到**常数正字符**所需的更高权信息，不能省略成“只检测了权零”。

## 4. 权零的完整原列与真实 14 维上界

记

$$E_0=\Phi_{p_1}-\Phi_{t_1}/4.$$

令 $T^{\mathrm{area}}_{h^{-2}}$ 为 R77 的 area 系数原模板，$T^{\mathrm{shape}}_k$ 与 $T^{\mathrm{shape}}_{h^{-1}k^2}$ 为 R79 h-shape 原模板。它们分别对应 v2 原列 40、109、104；定义、方向、所有标量因子均以已绑定的原始模板为准，没有另行重新归一。

R94 的权分块给出恰好以下 16 个原生成列 $C_j$。所有列都是完整两个模式，而不是只取 $-4$ 模式。

| 本块列 $j$ | 二阶算子 | 第三算子 | v2 原第三列 |
|---:|---|---|---:|
| 0 | $\Phi_{p_0}$ | $\tau_{p_1,p_2}$ | 7 |
| 1 | $\Phi_{p_0}$ | $\tau_{p_2,t_1}$ | 17 |
| 2 | $\Phi_{s_1}$ | $\tau_{p_1,p_2}$ | 7 |
| 3 | $\Phi_{s_1}$ | $\tau_{p_2,t_1}$ | 17 |
| 4 | $E_0$ | $\tau_{p_0,p_2}$ | 1 |
| 5 | $E_0$ | $\tau_{p_1,t_1}$ | 12 |
| 6 | $E_0$ | $\tau_{p_2,s_1}$ | 16 |
| 7 | $E_0$ | $T^{\mathrm{shape}}_k$ | 109 |
| 8 | $\Phi_{p_2}$ | $\tau_{p_0,p_1}$ | 0 |
| 9 | $\Phi_{p_2}$ | $\tau_{p_0,t_1}$ | 6 |
| 10 | $\Phi_{p_2}$ | $\tau_{p_1,s_1}$ | 11 |
| 11 | $\Phi_{p_2}$ | $\tau_{p_2,r_1}$ | 14 |
| 12 | $\Phi_{p_2}$ | $\tau_{p_2,s_0}$ | 15 |
| 13 | $\Phi_{p_2}$ | $\tau_{s_1,t_1}$ | 27 |
| 14 | $\Phi_{p_2}$ | $T^{\mathrm{area}}_{h^{-2}}$ | 40 |
| 15 | $\Phi_{p_2}$ | $T^{\mathrm{shape}}_{h^{-1}k^2}$ | 104 |

本次从原式准确核对

$$\boxed{\begin{aligned}
C_9&=4C_0+C_1-4C_4+4C_8,\\
C_{13}&=4C_2+C_3+4C_6-4C_{10}.
\end{aligned}}\tag{5}$$

两个模式的原始差在这两条关系中已经直接相消为零。因此保留

$$\mathcal J=(0,1,2,3,4,5,6,7,8,10,11,12,14,15)\tag{6}$$

给出真实上界 $\dim(\mathcal R_*)_0\le14$。这一步依赖全部第三空间已由真实 36 基张成及 R94 的准确分权，不是从一个模秩不足推有理上界。

## 5. 同一有理 profile 的原式 15 阶分离子式

实际评价采用同一实 profile 对，支撑为 $[2,3]$，$t=\xi-2$：

$$f=[t(1-t)]^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad q=f+ig.$$

这是有限正则性的有理测试对，原测试本身没有被强设为三矩圆。所有 14 列、全部点与两个模式均使用它。查询点为 $t=j/49$，$j=1,\ldots,48$。每点的四行依次为

$$\operatorname{Re}(-4),\quad\operatorname{Im}(-4),\quad
\operatorname{Re}(-2),\quad\operatorname{Im}(-2).$$

因此全表有 192 个真实有理评价行。值由原始 profile jet、普通复乘法与准确右原函数递归求出；没有用 word 代表取值。

原报告核到常态原式最高输入 jet 为 3，原第三模板最高 jet 也为 3；与最多取两阶导的 $\Phi$ 组合后，响应及基准最多需要五阶输入 jet。固定较大区间上的这些有限原式关于 $C^6$ 输入连续。上述 polynomial 对零延拓为 $C^7$，可在 $C^6$ 中用紧支撑光滑对逼近。因此一个在全部光滑 profile 上成立的真实函数关系也必须在该测试对上成立；后面的非零有理子式合法证明光滑 universal 算子空间中的非成员与独立性。

取控制行编号

$$\mathcal I=(0,1,2,3,4,6,7,10,11,14,15,18,19,22)\tag{7}$$

与 (6) 的 14 列，形成真实有理矩阵 $A$。再添行 23，即 $t=6/49$、$\xi=104/49$ 处的 $\operatorname{Im}(-2)$。

在已检查的素数

$$p=2147483647$$

下，公开原式评价给出

$$\boxed{\det A\equiv1836229422\not\equiv0\pmod p,}$$

$$\boxed{\det[A\mid b_0]_{\mathcal I\cup\{23\}}
\equiv1852863582\not\equiv0\pmod p.}\tag{8}$$

其中第二个矩阵是 15 行 15 列的增广方阵，最后一列为同一原式目标 $b_0$。

实际遇到的 84 个分母均在模 $p$ 下可逆：它们为 $1,\ldots,76$ 及

$$96,128,192,256,512,1024,2048,4096.$$

该分母列表 SHA256 为 `5a66499b3f2ea909b10698e4b2c715e27fc9c540f61e645c159d21bedc61d913`。最高实际 polynomial 次数为 76。所有这些是回执中的已执行检查，不是从浮点残差推测。

第一式结合上界证明

$$\boxed{\dim(\mathcal R_*)_0=14,}\tag{9}$$

第二式证明 $b_0$ 不属于它。因此 (1) 已经成立，无须继续计算其他八个较低权块。

## 6. 真正的有理泛函，不把模整数当实符号

令 $e_{\mathcal I}$ 表示 (7) 的 14 个真实有理评价，$e_{23}$ 表示附加行，$a=e_{23}(C_{\mathcal J})$ 为一个真实有理行向量。定义

$$\lambda_0(F)=e_{23}(F)-aA^{-1}e_{\mathcal I}(F).\tag{10}$$

矩阵 $A$ 在有理数域可逆，由 (8) 已严格保证。于是 $\lambda_0(C_j)=0$ 对全部 16 个原生成列准确成立，且

$$\kappa=\lambda_0(b_0)\ne0.$$

其模约化为

$$\kappa\equiv2115674793\pmod p,$$

并在实际中核对了 $\det\mathrm{Aug}=\det A\cdot\kappa\pmod p$。报告中的 15 个模泛函系数只是 (10) 的约化，用来复核模证书；它们不是 (10) 在有理数域中的系数。

令 $\Pi_0$ 为 R91 的真实缩放权零投影，定义

$$\boxed{\Lambda(F)=\frac{\lambda_0(\Pi_0F)}{\kappa}.}\tag{11}$$

无须知道 $\kappa$ 的实符号；除以真实非零的 $\kappa$ 使 $\Lambda(b_0)=1$。所以后面的正性不是将模整数的大小或符号提升到实数域。

因为 $\Pi_0\mathcal R_*=(\mathcal R_*)_0$，(10)–(11) 湮灭整个 $\mathcal R_*$，包括所有其他缩放权。

## 7. 常数正字符：所有 $H,d$ 一次支付

R91 的真实组合律给

$$b_{H,d}=S_He^{dN}b,$$

其中 $N$ 降权 1，且保持 $\mathcal R_*$。由目标最高权为 2、(3) 和 (4)，得到

$$\Pi_0 e^{dN}b=b_0+\frac{d^2}{2}N^2b_2,$$

而 $N^2b_2\in(\mathcal R_*)_0$。$S_H$ 对权零是恒等，所以

$$\Lambda(b_{H,d})
=\frac{\lambda_0(b_0)+\tfrac12d^2\lambda_0(N^2b_2)}{\kappa}
=1.$$

这证明 (2)。每个候选状态的 $H,d$ 都可不同，且不必落在一个预先固定的有界盒；只要其共同物理区间使实际原式有定义，就受同一代数结论约束。

按 R89 的规范，完整多 pair P1 是

$$4\sum_{j=1}^m\ell_j
\{b_{H_j,d_j}+\mathcal B_{A_{H_j,d_j}}(T_j)\},
\qquad\ell_j>0.$$

施加 (11) 后准确为

$$\boxed{4\sum_{j=1}^m\ell_j>0.}\tag{12}$$

因此不是某个特定正权向量失败，而是当前 reciprocal-pair/真实第三控制模型的全部有限正权 universal 组合都失败。不能用负 bulk 权、零长度 helper 或遗漏新增状态基准成本来绕过 (12)。

## 8. 合法同 profile 圆上的严格推论

式 (11) 含一个算子权投影，因此第 5 节原测试对并不自动成为完整未投影 P1 的固定圆证书。这里必须使用 R96 的额外定理，不能仅把“同一有理测试对”重新命名为合法三矩圆。

空间 $V$ 是有限仿射不变的真实四次齐次右因果 Volterra 空间，且全部原函数节点有正 profile 次数。R96 因而给出一个光滑紧支撑、归一且满足三复总矩的 $q_*=f_*+ig_*$，以及同一 $q_*$ 上的有限查询映射 $E_*$，使 $E_*|_V$ 单射。

于是 $\Lambda$ 可准确写成同一 profile 上的查询行向量：$\Lambda=\lambda_*E_*$。由 (2)

$$\lambda_*E_*(\mathcal R_*)=0,
\qquad \lambda_*E_*(b_{H,d})=1.$$

式 (12) 因此对这个固定合法圆成立，即使每个实际桥的控制系数允许依赖该圆重新选择也一样。R96 的相对开稠密结论给出同样性质的开稠密圆类；没有施加统一振幅/导数盒或固定宽左 collar。

这是存在性及相对泛性推论。本次 Actions 未输出该 packet 构造的具体数值参数，也没有声称第 5 节的原 polynomial 测试对已被直接用作该见证。证明依赖 R96 的非零多项式、因果拼接和准确左矩补偿。

## 9. 本次明确结束的子问题与仍开放的工作

当前有限 reciprocal 状态的 universal P1 正组合机制已被 (12) 排除。无需为了这一子问题继续跑余下八个权块，也无需再给同一实际控制类增加状态或重复 72/252 混合列任务。

仍未被排除的方向包括：特殊的非泛 profile 圆、完整固定有限 $N$ 中 $P_0+NP_1$ 的真实相消、不同一阶目标/不同几何机制。R83/R84 的 P0 基线与半群约束必须保留，不能因本结果而把第四成本随意取负。整个闭面研究课题仍未达到完成标准。
