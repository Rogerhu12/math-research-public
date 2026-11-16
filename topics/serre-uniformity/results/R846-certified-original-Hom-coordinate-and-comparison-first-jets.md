# R846：原五个比较函数及六个 Hom 点的一阶表达式已实际完成

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：原 $p=41$、同一 $c_1$、同一粗参数 $z=a-1$ 下，原 $f=f_4$ 和五个 $g_j=(1+T^j)f$ 的坐标一阶项，以及原五个 $\mathcal R_j$ 的一阶导数与对数导数，均已在公开 Actions 生成来源完整的准确 DAG。** 本次没有证明这些对数导数非零，也没有生成 $c_0$ 刚性化、$\eta_h$ 或高度。

实际运行 [43783814426](https://github.com/Rogerhu12/math-research-public/actions/runs/43783814426)，计算 job 133026881969，source `94e4d5ece6cdb0b0d10bad40a2df625ef086a5fe`，在 2026-11-16T01:02:05.426514+00:00 完整结束。核心数学阶段计时 **0.03756468899999277 秒**；核心总 receipt 为 0.04599666099997535 秒，退出码0、error=null，两个完成阶段。原 529 个节点按内容哈希原样保留，新程序共 **733 个节点**；新点加法次数为0。

## 1. 直接消费的原对象

原点来自 [R844](R844-certified-original-five-Hom-word-points-and-comparison-values.md) 的五加法程序，而非 R794 的另一组五点。原参数、十二个 Hom 基和其切向来自 [R791](R791-certified-original-Hom-descent-and-eta-inputs.md)。全部非零原 Hom 在同一个点的非挠性来自 [R843](R843-certified-original-CM-point-nontorsion-and-Hom-value-separation.md)。

新方法为 [原比较函数一阶接口](../notes/R792-original-Hom-comparison-log-jets-from-certified-point-DAG.md)，SHA-256 `2d613dc15ac9a0fb93a22415633c58704c914affd987960d74b93637e9e9d555`。程序使用 R841 的原 DAG 节点定义和来源读写；没有重新执行旧 CM 响应、Dixon、Hom、非挠性计算或 R844 点加法。

| 本次保留的来源组 | 文件数 | 用途 |
|---|---:|---|
| CM | 165 | 原准确四响应与单位解表达式叶 |
| R791 | 9 | 原十二切向、Hom 字、Galois 运输 |
| DAG | 11 | 原 R841 点和下降节点 |
| NONTORSION | 66 | 原 R843 同点非挠和分母依据 |
| POINTS | 10 | 原 R844 的529节点、五个比较值及归一化 |
| 合计 | 261 | 全部按原 manifest 和父子身份绑定 |

这261件通过 R844 已完成载体续接；原父载体1816125字节、SHA-256 `479f587a0b67611f41f07cb616725620ee430df9d7e7f0305bf49ab40fa66bcb`。新载体还保留 R844 十件必要来源，便于后继继续，无须重新计算旧结果。

## 2. 准确一阶公式和所有逆元的来源

令 $u=\sum_{i=0}^{11}u_i f_i$ 为实际原 Hom 字，原切向为
$$
h_u=\sum_{i=0}^{11}u_i h_i,\qquad
u^*\frac{dx}{2y}=h_u(z)\,dz.
$$
本次六个字依次是 $f,g_1,\ldots,g_5$。它们的 $u_i$ 逐字来自 R844 原点记录；没有用任意 $L$ 线性微分替换实际整数 Hom 字。

在同一原目标 $C:y^2=x^3+b$ 上，
$$
x_u'=2y_u h_u,\qquad
y_u'=3x_u^2h_u,\qquad
\frac{(y_u^2-b)'}{y_u^2-b}=\frac{6y_u h_u}{x_u}.
\tag{846.1}
$$
因 $x_u=0$ 的点属于 $1-\zeta$ 的有限核，R843 的同点非挠性给这六个原 $x_u(c_1)$ 均非零。每个新增逆节点都绑定原 Hom 字、原点 ID、R844 程序和 R843 同点证书。这里的逆不是依靠模值候选、浮点零判或未接受的短 CM 候选。

程序将原十二个 $h_i$ 作为已认证 $L$ 元素读取。原 $h_0=h_{f_4}$ 的节点与 R844 内原节点完全一致；没有第二次 $c_1$ slash、额外 $\zeta^2$、$\lambda$、$246$ 或 $82^{10}$ 因子。系数6只来自 (846.1)，没有在迹外重复插入。

## 3. 原比较函数的五个一阶项

保持 R791 原 $r_j=a_j/b_j$ 的既约分数和正分母：
$$
r_j=\frac{31}{67},\ -\frac{41}{67},\ -\frac{34}{67},\
\frac{34}{67},\ \frac{103}{134}.
$$
记 $\operatorname{Tr}$ 为原七个 $\sigma_\gamma$ 共轭之和。由于 $z=a-1$ 是原 $\mathbf Q$ 参数，$\sigma$ 固定 $z$；因此每个共轭都作用于完整的准确叶、常数和原单位解图，不能只替换某个模嵌入的坐标。

本次准确生成
$$
D_j=\frac{\mathcal R_j'}{\mathcal R_j}(c_1)
=b_j\operatorname{Tr}\!\left(\frac{6y_{g_j}h_{g_j}}{x_{g_j}}\right)(c_1)
-(2b_j+a_j)\operatorname{Tr}\!\left(\frac{6y_fh_f}{x_f}\right)(c_1),
\tag{846.2}
$$
以及
$$
\mathcal R_j'(c_1)=\mathcal R_j(c_1)D_j,\qquad j=1,\ldots,5.
\tag{846.3}
$$
其中 $\mathcal R_j(c_1)$ 仍是 R844 的原节点，故原七因子范数及全部 $b^7/N(b)$ 比较常数均保留。虽然常数在对数导数中消失，它仍出现在 (846.3) 的原值中；程序没有重新归一化 $\mathcal R_j$。

本次没有选择解析对数分支。(846.2) 是在非零原函数值上的代数对数导数；它不是原 Poincaré 纤维的刚性化或局部高度值。

## 4. 实际完整产物和不可变来源

数学身份 configuration 的 SHA-256 为 `0b9025c1cb3816fd62b8a0de7a62118dcceef2343f9712b5cff6d9edfc1324cb`。预算30分钟不进入数学身份；所有已成阶段按同一身份保留，输入没有待补项。

入口为 [原公开 request](../notes/R792-Hom-comparison-log-jets-public-request.json)，[核心](../scripts/R792_original_Hom_comparison_log_jets.py)和[标准库 IO 包装器](../scripts/R792_public_original_Hom_comparison_log_jets.py)。工作流是 .github/workflows/serre-R792-Hom-comparison-log-jets.yml，只在本公开仓库运行。

| 项目 | 字节数 | SHA-256 |
|---|---:|---|
| 新核心 | 17269 | 417f2df7365fcb3ea2e9ce5403404b9c0d0859fc43359b52bb775468452328c2 |
| 公开IO包装器 | 25528 | f79f4aa340a7e8050d19c746c4a02bb495081710f54566454bc8332ad2a3778b |
| request | 5695 | fe21a7745d32f874e0b887334e0ac329f477bbad44d6d1337967fe46fa367c6e |
| workflow | 7424 | 4623fa0dce138058484be975be51a4c8e93622dab53f41811476e1df25914882 |
| p41-original-Hom-comparison-log-jets-certificate.json | 7716 | b35690551630afced22b426b92f58e5e5747c9d7667c66fb02413d750609054c |
| R792-Hom-log-jets-original-comparison-first-jet-program.json.gz | 93533 | 555e3c6c877ef2b3fb64f0dfe17f463f49fd6ca83bb1a1faedc2db562724547b |
| R792-Hom-log-jets-source-audit.json.gz | 3352 | 5522ff7ea58a2e5d55191fcff9cd73b21650bedd5047870bc5ea5559afed7868 |
| R792-Hom-log-jets-stage-manifest-66681dbe2e9e6c8b621c4c36.json.gz | 3267 | 880699c5275d0e270527a0438e515bfa04a2de2d5c89c9bdc99082d083a9bfe2 |
| R792-Hom-log-jets-retained-inputs.tar.gz | 1935655 | 2d36482535bc2ac2b0b31b688ffac81c96a828ba8610d63de9a51085a5c08448 |
| retained-inputs-receipt.json | 59178 | 2b57fd9bc0a9cae8c7f1c7c3e975b8f1cea479ebe41ab7645cfeb42a0634a5c4 |
| public-actions-input.json | 62430 | b251839e2d212af31d0ce80bee738423d200cae614df16fce4e35c9b609f45d4 |
| core-receipt.json | 366 | bfec39c9b9f5606b3273bc6b1defd3899ea1620a4f9fca9429719facc8c41b2e |
| run-receipt.json | 405 | 06b154df0d9af223031c8568bee3905f510d9dfd82ff73a3317d9445bed848f9 |
| 全输出manifest | 1520 | 07f58e44141e614c69142b1645a54550dfef38b63e4fc8c69c429d3eaa79fbdc |
| manifest reference | 189 | 2b30790632a23bec3157352bfc0ea1b5e6337e289678ec4b8e86c9d45aeac40c |

实际 artifact 是 `serre-global-R792-Hom-comparison-log-jets-43783814426-1`，ID 14189930390，ZIP 2170291字节，SHA-256 `16d214a10e91297df9874bbd892862990fe570f809dff6312c9a4cb9866663ce`，到期 2026-11-17T01:02:05Z。

根会话在真实结束后纯 IO 读取并重哈希完整 ZIP、全部12个成员，逐项核 manifest、最终证书、两阶段、原261件输入和完整父子来源。这个动作没有在本地执行节点算术。可重算表、证书、DAG机器输出和载体没有提交 Git、Release 或悬挂 blob；正式仓库只保存脚本、参数、方法和此简短结果索引。

## 5. 已成范围与后继准确边界

已成的是六个原 Hom 点的一阶坐标表达式、五个原比较函数的一阶表达式、真七共轭迹及全部分母证明。旧529节点未变，新增204节点只承担本次一阶任务。直接复用这些结果，不再运行旧点加法或切向生成。

以下仍未完成：展开原大有理坐标、原短 CM 候选的 A.1、任何 $D_j\ne0$ 的准确零判、原实下降点的一阶项、$c_0$ 处原刚性化、五个全局加法极理想的实际源图、$\eta_h$ 的标准 Jacobian 代表和真实高度。原全局三子式方法另行消费全局 $W/C/F$；本次 CM 点值或一阶项不能替代这些全局来源。

原主题的全 $p$ 完成标准仍 OPEN，继续其余原输入与真实高度/同标签单位缺口。
