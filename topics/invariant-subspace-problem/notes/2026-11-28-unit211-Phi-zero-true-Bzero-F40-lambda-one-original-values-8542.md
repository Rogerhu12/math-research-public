# 正确 B 的 F40：已成 lambda 一次式后的完整原值新输入

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

这是**尚未执行的唯一首次新输入**。源
`2026-11-28-unit211-Phi-zero-true-Bzero-F40-lambda-one-original-values-8542.py`
为 9615 字节，SHA256

`18d564ff3b28972d7476cbdc367d50ea1e624ffafccd9c8ea0d9edfb56c1191c`。

120 秒、1 GiB，外驱动 135 秒；所有嵌套 alarm 钳制在同一最初截止时刻，包含非正 alarm 请求。只输出小型返回摘要和哈希，不保存可重算参数载荷。

## 1. 与冻结旧门的差别

旧 d825 两个独立首次在整个首一 $\lambda^6,\omega^2$ 环境构造 QQ 理想矩阵时触及 1 GiB。F40 的 480 维矩阵、旧六对 Bézout及旧正目标全部冻结，不再执行。

之后唯一 f7 首次已给整个

$$
K_{40}=\mathbb Q[x]/(F_{40})
$$

上的真正原关系 $h_1=\lambda-\lambda_*(x)\in I_4$。其实际 run 46125572734 / job 140919309079，最终参数 SHA256 为

`da857429ce495f99a8122be93572a2ea843d686399306736f686cc563b0851ee`。

本次新目标是**先特化这个已成原关系**，再回原六式；未取其它原关系前，必要环境只有

$$
K_{40}[\omega]/q_\omega(\lambda_*,\omega)
$$

的 80 个 QQ 基元素。算法仅处理整个 $K_{40}[\omega]$ 的次数至多 3 多项式，不构造旧 QQ 大矩阵。

规范来源为：

- [正确整 B 原十二行](../results/R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)；
- [C76 一次原覆盖](../results/R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)；
- [F40 真原首一 lambda 一次式](../results/R150-appendix-unit211-Phi-zero-true-Bzero-F40-original-monic-lambda-one.md)。

## 2. 既有参数的最小定义再生

旧 d825 只读取到唯一标记
`for i,value in enumerate(env['original']):`
之前，准确前缀 SHA256 为

`a922242b457a02320499c8157642aa920ac930001bace88d4ce59b1ed5f90201`。

它仅提供当前不可变 $F_{40}$、全 K 算术、首一 $q_\omega$、原四行及原 N/P 的必要定义。旧四行验证、六对 gcd、原六列矩阵与正目标不进入。

原 $g_6$ 由既定第 (0,3) 原行对首一化再生，核 SHA：

`9a94efc0ec88870b215b47b5175bbc4832b9c3f75c66d14e16d59ab845198cfe`。

已成定理的首步和最终首一 gcd 同为一次，故

$$
h_1=\operatorname{monic\,gcd}(g_6,n_0),\qquad
n_0=a_0^2-q_1a_0b_0+q_0b_0^2
$$

就是已定参数的准确函数定义。新源只作普通 Euclid 再生这个参数并核已成末 SHA；不计算其它三个 norm、四 norm 的原三坐标证明、完整旧 Bézout 或其终端来源。该再生不作为旧结果的新审计门。

## 3. 真正新的完整原值专门化

在完整 K 内设置 $\lambda=\lambda_*$，保首一

$$
q(\omega)=\omega^2+q_1(\lambda_*)\omega+q_0(\lambda_*).
$$

全 K 不选某个复嵌入；任何系数倒数必须以全 K 扩展 Euclid 返回真逆。$q$ 的全部重根保持。没有按某个模素数判断 K 的某一支，也没有假设某条 $b_i$ 非零。

$f,t$ 沿既有真实仿射恢复成为 K 上的 $\omega$ 一次式。新源将四个完整原式 $(E_1,E_{Be},E_{Bo},N_1)$ **先作为完整 $\omega$ 多项式**代入，再用首一 q 作短除，返回余式与已定四行在 $\lambda_*$ 的特化相同；所有原坐标全乘回。

同时将旧实际 q 的原四式组合在这个新的 $\lambda_*$ 上直接返回：

$$
q=\sum_{i=0}^3\tau_i F_i.
\tag{1}
$$

随后首次在 $\lambda_*$ 上代入完整原加权 $N_S,P_S$，得到另外两个次数至多 3 的 $\omega$ 多项式。每条与首一 q 的短除均完整乘回。本次没有直接取旧 480 环境里的矩阵列当新原来源。

## 4. 新的单变量原理想与完整提升

对同一 K 上的新原多项式，实际计算

$$
g=\operatorname{monic\,gcd}(q,F_0,F_1,F_2,F_3,N_S,P_S).
$$

每次 Euclid 保完整多项式组合

$$
g=\beta_q q+\sum_{i=0}^5\beta_iF_i
$$

并乘回所有 $\omega$ 系数。再用 (1) 直接消去 q，返回

$$
g=\sum_{i=0}^5\widetilde\beta_iF_i.
\tag{2}
$$

若 $g=1$，(2) 排整个 F40 原纤维；若非恒定，只登记真正所得次数和余商维数，不凭泛域 gcd 标志宣称排空。每个在 $\lambda_*$ 上的身份可沿已成 $h_1\in I_4$ 提升，故没有用抽象新值点替换原 lambda。

## 5. 仅在新余商内的正 D 目标

如果 (2) 未返回 1，下一目标严格只在这个新 $\lambda^1$ 环境中进行。完整原恢复给

$$
D_{\rm val}=\ell(2\lambda_*^2-2\lambda_*+1)-T(\omega)^2
=bc(h_U-k_U)^2.
$$

其物理单位仅沿用当前两个不同 singleton 值的 $D_{\rm val}\ne0$ 范围。源不求 $D_{\rm val}^{-1}$、不求其范数逆，也不删可能 $D_{\rm val}=0$ 的代数分量。

因为 g 次数至多 2，只测试两个明确新目标 $D_{\rm val}$、$D_{\rm val}^2$。只有实际短除余数为零，并将相应倍数乘入 (2)、**返回全部原多项式坐标**，才由原物理非零排此整纤维。若两个目标都不返回，保持整余商及完整 K 嵌入，不抬时限、不重启冻结旧矩阵。

## 6. 精确文件依赖

工作流只需同目录复制四个已刊小源，均核全文 SHA：

1. `2026-11-28-unit211-Phi-zero-true-Bzero-large-constant-original-fiber-8542.py`，blob d8259998597c4779610c182854305d4e4e0af2f4，SHA a44a8fc4ca4842d97c4d94215250e8399f5988407c3971bdc68ffe96b3b77a48；
2. `2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py`，blob 6cde5a82e5a3ab499d3a26be19d27428b7a38ed6，SHA b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56；
3. `2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.py`，blob 4fb7fa723660043b5179c0f1302494064c1955f2，SHA 73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35；
4. `2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py`，blob f62e66a27d5c999a54d03631ab8d3b31297e7aa2，SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

没有历史 JSON、系数分片或 f7 执行依赖。环境若未设置，则固定使用 `ISP_B_FACTOR_DEGREE=40`；其它值直接拒绝。最终日志准确区分原理想 1、正 D 幂、残余次数和失败边界，未执行前不宣任何新排除。
