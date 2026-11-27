# Phi=0 整首个二次头零曲线：原线性关系已返，D 公共取消首次超时

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

**准确状态：本次返回完整原线性关系及三条多项式消元恒等式；后续 D 目标的第一个公共因子计算达到原定 120 秒限额。** 没有最终约消后的 D 必要多项式、没有有限权重覆盖、没有整个首项零曲线的排除。原源码与失败身份冻结，不抬限重跑。

## 1. 此次真正的新输入

此前首项非零图的长 $\lambda$ 行模块另有独立失败记录。本次处理其互补的整条首项零曲线，以
$$
g(u,Q)=-12H_{6,4}(u,Q)
=\sum_{j=0}^4g_j(u)Q^j,\qquad g_4=1
$$
为完整权代数
$$
A=\mathbb Q(u)[Q]/(g)
$$
的定义。其余系数是
$$
\begin{aligned}
g_0={}&64-272u+512u^2-544u^3+336u^4-112u^5+16u^6,\\
g_1={}&-112+348u-496u^2+440u^3-248u^4+80u^5-12u^6,\\
g_2={}&60-123u+104u^2-52u^3+13u^4,\\
g_3={}&-13+\frac{53}{4}u-3u^2.
\end{aligned}
$$
整个 $Q$ 四次代数均保留，不假定它是域或约化代数。权代数逆由完整四阶正规表示解出，并逐四分量乘回；原 $Q^4$ 首项恒为 1。其参数分母不自动成为实际原单位，零纤维仍须保留。

源码直接使用已刊紧凑原均值及 N1 恒等式，没有重放旧 cofactor 或此前失败的长模块。

## 2. 已完整返回的原关系

原前三均值在 $(T^2,Tz,z^2)$ 上的实际头矩阵于 $A$ 中行列式为零。源码取得其一条非零伴随行 $\alpha$，并完整核回
$$
\alpha H=0,\qquad
\alpha_1R+\alpha_2W+\alpha_3O=L,
$$
其中
$$
L=a(\lambda)T+b(\lambda)z+c(\lambda),
\qquad
(\deg_\lambda a,\deg_\lambda b,\deg_\lambda c)=(1,1,2).
$$
此阶段在 0.082881465 秒完成。全部精确系数保存于
[原线性参数](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-whole-first-head-original-linear-relation-exact-input-8542.json)，包括每个 $\lambda$ 系数的四个 $Q$ 分量及共同 $\mathbb Q[u]$ 分母。未把 $a,b,c$ 的任何 $\lambda$ 因子当作新单位；如需跨过其权参数分母零纤维，须先清回多项式身份。

对任一原二次式
$$
P=q_0+q_T\,T+q_z\,z+q_{TT}T^2+q_{Tz}Tz+q_{zz}z^2
$$
，定义
$$
\begin{aligned}
\widetilde P_0&=b^2q_0-bcq_z+c^2q_{zz},\\
\widetilde P_1&=b^2q_T-b(aq_z+cq_{Tz})+2acq_{zz},\\
\widetilde P_2&=b^2q_{TT}-abq_{Tz}+a^2q_{zz},\\
\widetilde P&=\widetilde P_0+\widetilde P_1T+\widetilde P_2T^2.
\end{aligned}
$$
完整多项式身份为
$$
b^2P-\widetilde P
=L\{b(q_{Tz}T+q_z+2q_{zz}z)-q_{zz}L\}.
$$
源码对同一原 $R,W,N1$ 三式分别完整乘回；最后一条在 0.741128849 秒完成。三个新二次式的 $\lambda$ 系数次数都是 $(4,3,2)$。全程没有除以 $b$，因此 $b=0$ 分支仍包含在这三个必要多项式中。

## 3. 后续未完成部分

随后以三个新二次式的 $(1,T,T^2)$ 系数组成实际矩阵，目标保持
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2.
$$
程序开始对原伴随行和原行列式作共同取消。第一个 $\lambda$ Euclid 链实际只完成如下三步：

| 时间（秒） | 除式次数 | 余式次数 | 最大 u 系数次数 |
|---|---:|---:|---:|
| 6.421604563 | 7 | 6 | 527 |
| 12.573403186 | 6 | 5 | 694 |
| 34.251608199 | 5 | 4 | 1247 |

每步都已核回完整四分量的商乘除式加余式身份。最后临时分母支持记录的次数为 1450，但它不是一个已完成排除论证的覆盖；不能由该数字声称只剩有限权点。

120 秒信号到达时没有下一步完整返回。特别地，最终 D 多项式、原 F6 或完整 NV 的新固定结果式、最后原公共根排除均未执行到完成。

## 4. 唯一实际身份

[冻结源码](2026-11-27-unit211-Phi-zero-whole-first-head-quartic-original-linear-D-input-8542.py)：

- blob：9f03cd560852b293a5486112b8df369abd5bb53e。
- SHA256：7dfa17a6a871f6a2c1be4773d58f096f3a3252bcffbc61c8f6f766302bc8ea2e。
- run/job：46049436790 / 140676791106。
- source commit：0526ab6b035556abf0c9051e1a69c11afb6f6566。
- 内层：120.074362658 秒 / 264344 KiB / exit −14（SIGALRM）。
- stdout：46925 字节；SHA256：3728422257594d47c2e373bee21d028a66308a5da17c738a9cda0d5bd1806de6。

2026-11-27 18:26:20 UTC 的实际 pull 前后提交相同，两份 README 的 blob 均无变化。资源预算始终为 120 秒/1 GiB。

[小回执](2026-11-27-unit211-Phi-zero-whole-first-head-linear-D-first-timeout-execution-8542.json)保存数学阶段及精确执行身份；约 60 KB 的原线性参数独立保存，避免把它重复塞入失败回执。该已返线性关系可以用于不同的新输入，但本次长公共取消门不继续抬限。整条首项零曲线仍开，普通 ISP 尚未完成。
