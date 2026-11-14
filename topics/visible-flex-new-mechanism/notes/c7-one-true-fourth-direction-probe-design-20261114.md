# c⁷ 是否看见一个真实第四方向：最小原式探针

日期：2026-11-14。本稿指定一个新的公开 Actions 小探针。它承接 R107 的仿射不变量，但**尚未得到 actual 值，不预设其非零或为零**。它不重算 R99 的旧查询、不重做 R100 的 c⁸ 消项，也不扩展已经排除的正 P1 路线。

## 1. 唯一目标

取 R99 已确定可由真实有限路径实现的方向

$$
P=\Phi_{t_1},\qquad Q=\Phi_{p_1},\qquad
\tau(a;b,c)=Q(a,P(b,c))-P(a,Q(b,c)).
$$

完整 R83 第四响应为

$$
\mathcal B_P(\tau)(F,\phi)
=2\tau(PD;D)-4\tau(\phi;\phi,PD)
+4P(\phi,\tau(\phi;D)),\qquad D=F-\phi^2.
\tag{1}
$$

本次只计算它的 unit pure 幂尾 q=(c−ξ)⁸ 中 c⁷(c−ξ)²⁵ 的准确有理系数。这个方向已在 R99 的另一查询泛函下非零；那不说明当前尾系数也非零，故需要这一项真正新探针。

## 2. 复用完整二阶原式

源码为 `scripts/literature_c7_transverse_tail_probe.py`。它直接调用旧的

`literature_pure_bulk_exact_membership.matrix_operator`

而不重新实现或截断二阶算子。对相应八坐标，旧函数准确给

$$
P(f,g)=\xi^2f'g'+\xi J_2^*(f,g),
$$

$$
Q(f,g)=-\frac12fg+\frac\xi2(fg'+f'g)
-\frac{\xi^2}{2}f'g'-\frac{\xi^2}{4}J_1(f,g),
$$

其中

$$J_1=\int_\xi^c\eta f''g''\,d\eta,
\qquad J_2^*=\int_\xi^c(\eta^2f''g''+2f'g')\,d\eta.$$

因此原公式中的局部项、右尾项及各自符号全部保留。底层只增加一个准确双变量多项式适配器，不调用旧的完整 fourth target 编译。

## 3. 新适配器的坐标与锚

令 r=c−ξ，准确有

$$\xi=c-r,\qquad D_\xi=-D_r,$$

$$\int_\xi^c f(c-\eta)\,d\eta=\int_0^r f(t)\,dt.$$

对 monomial cᵃrᵇ，导数和右原函数分别为

$$D_\xi(c^ar^b)=-b c^ar^{b-1},\qquad
J(c^ar^b)=\frac{c^ar^{b+1}}{b+1}.$$

所有系数使用 `Fraction`，没有数值求积、模素数或有限节点拟合。实际只评价两个已给出的算子和一个第三交换子，保留完整输出多项式；零系数由准确有理运算决定。

## 4. 完整 phase 与纯模式的归一

将 (1) 专门取 F=0、φ=q、D=−q²，得到完整 q⁴ 表达式

$$
K_{\rm pure}
=2\tau(P(q,q);q,q)+4\tau(q;q,P(q,q))
-4P(q,\tau(q;q,q)).
\tag{2}
$$

这一步保留三个外槽来源，尤其最后一项不能省略。

若 q=f+ig、φθ=(e⁻ⁱθq+eⁱθq̄)/2，那么 e⁻⁴ⁱθ 模式取 (2) 的 1/16。因此与 R100 的 pure −4 尾约定比较时，探针返回

$$\boxed{\kappa_7=[c^7r^{25}]K_{\rm pure}/16.}\tag{3}$$

输出同时保留未除 16 的完整 q⁴ 值和除后的纯模式值，避免归一混淆。

P、Q 及 τ、ℬ 的总算子权为零，所以输出在 c、r 中应齐次总次数 32。脚本检查这一点并记录 c⁸r²⁵ 的准确零值；它不把其他总次数的遗漏系数自动置零。该权检查不预设 c⁷r²⁵ 的值。

## 5. actual 及人工分支

建议 lane：`c7_transverse_tail_probe`。同一 job 先新接口人工检查、再唯一实际：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_c7_transverse_tail_probe.py \
  --check-only --out "$VISIBLE_OUT/c7-tail-probe-development.json"
python topics/visible-flex-new-mechanism/scripts/literature_c7_transverse_tail_probe.py \
  --out "$VISIBLE_OUT/c7-transverse-tail-probe.json" --max-seconds 60
```

actual 仅允许 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。没有输入 artifact，因此也不需要复制或重新拉取旧 profile 查询表。

预算为 60 秒、5,000 terms、最高总次数 80、有理数 8,192 bits；完整输出须小于 5 MB。超过预算即保留错误/预算状态，不给未知系数授零值。

小人工检查使用自造低次多项式：ξ 的导数、正右原函数的负导数、真实右端零值、故意错误积分常数的检测、两个旧算子在小输入上的对称性、自交换子零和准确 JSON 往返。它不评价 m=8 的研究目标。当前该人工分支已本地通过；公开 job 仍以自己的新接口回执记录实际执行。

## 6. 若非零，可以支付什么

如果 actual 给 κ₇≠0，可将 R101 的真实复制公式应用于“取该 pure 尾系数”的线性泛函。真实 M=T=0 词 Z(t,n) 的成本满足

$$a_7(V_Z)=e_7(t)+n\{2v_7+t\kappa_7\}.$$

这里 e₇ 和 v₇ 是实际未知基准，不能删除。先固定小 A(s)、第三环及共同 scalar 包络，再用 A(t/m)ᵐ 实现任意指定的有限 ±T；最后选有限 n 支配实际基准。两端异号和介值能匹配任意一个 a₇ 目标。

为得到 R104 的 I→D 块，可在 Z 后接一条固定的同 scalar 端芽、M=0、I→D 连接 C。零矩块的第四成本准确相加，故 a₇(B)=a₇(Z)+a₇(C)，连接成本必须计入目标。选择 a₇(Z)=−a₇(C) 后，再作 R104 的四块，便同时有 a₈=0 和 a₇=0；结合 R106 奇偶律，仅 D25 的 c⁵、c³、c 可以留下。

这段是**以 κ₇≠0 为前提的后续论证**。它仍不支付其他尾系数、完整 period、ruling、有限等距族、嵌入或厚度，也不需要把某个尾查询冒成全局合法 profile 圆。

## 7. 若为零

如果 κ₇=0，只能说明 a₇ 不看见这一条明确的真实方向。不能据此称 a₇ 湮灭全部 ℬE₈(W)，不能升级成正性或不可达障碍。

下一候选应继续由权零与原式结构决定，例如另一个外方向 Φp₁ 作用于同一个 τp₁,t₁，或 R99 的真实 h-shape(k) 第三方向。要先根据本次完整多项式说明新的测试理由，再开新的小目标；本次脚本没有自动扩展这些列，也没有无目标重复旧查询。
