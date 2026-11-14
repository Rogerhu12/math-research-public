# P1 word 实际结果：真实响应关系、有限余式与新增局部方向

日期：2026-11-14。状态：公开 Actions 的准确代数计算及已存表达式分析；没有本地重编研究目标、取值研究 profile 或运行几何。主课题未完成。

## 1. 真正取得的结论

公开 run `43630157008`、源码 `f3381b7556368457aaa5d855c141eeef48fa04e4` 的 `p1_word_exact` 完整成功，用时 $2.33566728$ 秒，峰值 RSS $40.8320$ MiB。全深度 word/shuffle 没有给出旧 $28$ 个 R71 响应对 pure target 的匹配关系；它从原始括号重新验证了 $10$ 条准确列依赖，故这些普适响应函数的张成空间维数**不超过 $18$**。尚未证明其维数恰为 $18$，也没有证明目标不在真实函数空间内。

更有用的新判断是：实际余式已经只含 $q,q',q''$ 和至多二重右原函数。新层的实际额外操作只有 $10$ 次 shuffle，没有触发新的唯一最高 jet IBP、纯 $x$ 前 letter IBP 或 cycle fallback。因此本例的旧失败不是更深嵌套积分尚未展开造成的；不应继续无目标地增加正规化规则。

同一 run 的 `local_third_exact` 还取得了新的**形式普适函数阳性**：加入真实变化几何局部密度的 $26$ 个 profile 代表后，$54$ 个响应中存在准确目标关系，从未改写原式重验的余项为零。这把下一任务转为真实路径与端口对这些局部系数的可实现性，而不是继续加密失败 profile。

## 2. 可追溯输出

word 目录：`notes/actions-43630157008-1-p1_word_exact/`。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `p1-bulk-word-normal-form.json` | 27311 | `1aac09b4caf9fdc8a565ca1a0e032db513071e1f31654a7718cb0a245b0285f2` |
| `p1-bulk-word-normal-form-expressions.json` | 25974 | `2f16d7fb23f478b67cb8c6a276d983a8b0e1f48a033abafdf54082fd65d451bb` |
| `receipt.json` | 22533 | `e316a48cc1b86ea9b96839a67f6e4f58580357294a5b8f3ede999c1b1b6d35fe` |

可读式文件的 `all_expression_rows_included=true`，没有截掉余项。回执的最后一次真实 pull/rebase 记录双 README 无差，`readmes_read_commit=0abf1faff0ecb4e3fe413b2701417c9a62837f27`。来源使用既有完整绑定，不重复机械枚举。

主脚本 SHA 为 `d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65`。原始 target 仍为 $473$ 项，SHA

`a4d4c092f3ff4582b9bfe386a9f176eb36c47f8a25dd03abace8c19fb1b35685`，

与旧 run `43628716304` 完全相同。目标没换；改变的是准确表达和消元方式。旧层的 $59$ 项变成 $65$ 个 word 项，余项从旧的 $76$ 项变为新表示的 $95$ 项。这不是误差或目标值增长：项数会随原语乘积展开和完整 pivot 消元而改变。

local 阳性来自 `notes/actions-43630157008-1-local_third_exact/local-third-decomposition.json`，14209 字节，SHA `8e167f08a081a038f8803975cc69936191fcc0dcf6699e583a9fde5f6e714b0e`，用时 $2.899914617$ 秒。

## 3. 列关系支付了什么

记

$$\tau_{ij}=\Phi_i(q,\Phi_j(q,q))-\Phi_j(q,\Phi_i(q,q)),\qquad
\mathcal H_{ij}=\frac{D\tau_{ij}(q)[A(q,q)]-2A(q,\tau_{ij}(q))}{8}.$$

此次 $10$ 条依赖均从原始未正规化 $\tau_{ij}$ 重新形成响应，再核余式为零。例如

$$\mathcal H_{r_0,s_0}=3\mathcal H_{r_0,r_1},\qquad
\mathcal H_{p_2,t_1}=\frac43\mathcal H_{p_1,p_2},$$

以及

$$2\mathcal H_{p_0,s_1}+2\mathcal H_{p_1,s_0}+\mathcal H_{p_2,r_0}=0.$$

这些是**第四响应**的关系，不能不经证明就改成原始三阶 holonomy 的关系。完整有理系数见主 JSON 的 `column_dependency_certificates`。它们逐条提供了真实维数上界的正证据，而不是把显示代表当作独立函数。

## 4. $95$ 项余式的具体结构

固定

$$I(f)(x)=\int_r^x f(t)\,dt,\quad Q=1+x^2,\quad
B=I\{2(q')^2+Q(q'')^2\}.$$

这里 $I=-J$，所有乘法普通复双线性，右 collar 唯一，左尾不清零。可读表中的 $W_8,W_{12},W_{31}$ 分别是 $I((q')^2),I((q'')^2),I(x^2(q'')^2)$，因此 $B=2W_8+W_{12}+W_{31}$。

余式有 $7$ 个无原语项、$76$ 个一重项、$12$ 个二重项，总 profile weight 全为 $4$。所有二重项准确合成

$$\begin{aligned}
N_4={}&\frac{x}{256}I\{x(q'')^2B\}\\
&+\frac{x^2}{512}I\{[10(q')^2+(3+5x^2)(q'')^2]B\}\\
={}&\frac{5x^2B^2}{1024}-\frac{x}{256}I\!\left(I\{(q'')^2B\}\right).
\end{aligned}\tag{1}$$

第二个等式只用 $B'=2(q')^2+Q(q'')^2$、$I(B'B)=B^2/2$ 和同一右锚的多项式 IBP；不是额外拟合。

另有 $27$ 项准确合成

$$[Qq'-2xq]I(C_3),\tag{2}$$

其中

$$\begin{aligned}
C_3={}&-\frac{q(q')^2}{16}-\frac{(1+2x^2)q(q'')^2}{64}
 +\frac{x(q')^3}{48}\\
&+\frac{x(3+4x^2)q'(q'')^2}{128}
 +\frac{Q(1-4x^2)(q'')^3}{768}.
\end{aligned}\tag{3}$$

$15$ 项是某个明确局部二次多项式乘 $B$；剩下 $34$ 个一重项分别是 $xI(A_4)$ 和 $x^2I(D_4)$，$A_4,D_4$ 都是只含 $q,q',q''$ 的局部四次多项式。全部系数及 $7$ 个无原语项已完整保存在可读文件，不在这里重复抄表。

这给出可继续纸推的有限对象；没有隐藏的高阶 jet、无限深度或未知左尾。按形式次数 $\deg x=1,\deg q_j=-j,\deg I=1$，目标与余式都只出现 $0,-2,-4,-6$ 四种偶次数。它是当前多项式代表的准确分块，不另声称实际函数独立性。

## 5. 新局部阳性如何解释旧余式

local producer 准确分解同一真实密度

$$\mathcal C_s=\partial_s P+
\mathrm{Area}(k_s h_{ss}-h_s k_{ss})+\mathrm{Cubic}+k_sR(h,k,\omega;q).$$

选定的 $h$ 原函数满足 $P_h(1,k,\omega)=0$，常 germ 的加速度势为零。新增 formal 列是上述余项中各几何 monomial 的 profile 系数，尚不能任意指定其实际路径积分。

实际准确关系用了以下 $5$ 个局部列和 $5$ 个已有 R71 响应：

| 局部列的几何 monomial | 关系系数 |
|---|---:|
| $h^{-5}h_s^2k_s$ | $-16/3$ |
| $h^{-4}k h_s^3$ | $8/3$ |
| $h^{-1}k_s$ | $-4$ |
| $k_s$ | $-2$ |
| $h k_s$ | $-4$ |

R71 列及系数依次为 $(p_0,s_0):1/12$、$(r_0,r_1):-1/32$、$(r_0,t_1):-1/96$、$(r_1,s_1):1/24$、$(s_0,s_1):3/16$。加入这些响应后，真实 pure target 的原式余项恰为零；没有取值 profile 后的数值投影。

这是具体的正向输入：原 $28$ 响应以外的真实局部三次密度提供了足够的形式补偿。下一步必须保完整密度和真实路径相容性。例如 $\int k_s\,ds=k_{\rm end}-k_{\rm start}$，闭 scalar loop 不能把这一列单独指定为 $-2$；从 $+1$ 到 $-1$ 的内部桥则准确给出 $-2$。其余 $h^{\pm1}dk$、速度三次项、加速度面积及端点势同样不能作为互相独立的按钮。

因此接下来的分工是完整 $C_1$ 一形式的准确 quotient 与端口兼容，以及 $C_3$ 路径 signature 的真实可实现性。二者若满足，还须支付基准桥、其余相位模式、$P_0$、完整第四 ruling 和有限族；本次仍没有闭嵌入或主课题比例证书。
