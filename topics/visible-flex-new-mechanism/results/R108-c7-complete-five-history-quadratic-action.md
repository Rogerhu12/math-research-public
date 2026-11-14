# R108：D25 的 c⁷ 周期是完整真实五历史二次 action

日期：2026-11-14。**已证明，且新增原式身份已在公开 Actions 通过。** 本结果消费 run [43642966285](https://github.com/Rogerhu12/math-research-public/actions/runs/43642966285)、source `d891604e0324491e241e1cc0dcbd9cafe49b988b` 的 `pure_tail_c7_reduce` 输出，不重新编译 forcing，不重新运行 R100 的 34 条旧身份。

在 R100 的 m=8、D25、常 scalar 端芽及完整 M=0 范围内，c⁷ 周期准确等于下文五个真实零端历史的二次 action。完整余式有 96 项、14 个历史单项式组；常数和线性组全部保留。**尚无符号、非零真实周期或完整第四 range 结论。**

## 1. 准确完整身份

沿用 [R95](R95-compressed-D25-action-and-top-parameter-endpoint-potentials.md) 的压缩 action 𝒜 及归一化

$$\mathfrak m=\frac{307328}{15},\qquad p=B_4.$$

定义新的端势

$$\boxed{\Phi_7=\frac{64}{5}p^2B_1+8p^2J_0.}\tag{1}$$

公开 consumer 已完整验证

$$\boxed{[c^7]\mathcal A=\mathfrak m\{D_s\Phi_7+\mathcal R_7\}.}\tag{2}$$

因为完整 M=0 给 p(0)=p(L)=0，(1) 两端准确为零。因此

$$\boxed{[c^7]\int_0^L D25\,ds
=\mathfrak m\int_0^L\mathcal R_7\,ds.}\tag{3}$$

这一步不要求完整第三算子 T=0。式 (2) 保留由微分端势产生的全部局部项，没有把 B₁、J₀ 或其他历史在区间内部设零。

## 2. 五个真实坐标及其方程

令

$$\eta=\omega-k/h,\qquad
\rho=h_s/h,\qquad
X=h_{ss}/h-2\rho^2,\qquad G=k^2-1+X.$$

保持 R100 的

$$
p=B_4,\qquad
\ell=B_3-J_2/2-\eta p,\qquad
\zeta=B_3-4\eta p.
$$

再定义

$$
\mu=B_2-3\eta B_3+6\eta^2p-\eta_s/8,
$$

$$
\nu=B_2-3\eta B_3+3\eta^2p+\eta J_2-J_1/2.
\tag{4}
$$

其真实方程是

$$
\boxed{\begin{aligned}
p_s&=hk/8,\\
\ell_s&=-\eta_s p,\\
\zeta_s&=G/8-4\eta_s p,\\
\mu_s&=-3\eta_s\zeta,\\
\nu_s&=k/(8h)-\eta_s(\zeta+2\ell).
\end{aligned}}\tag{5}
$$

五者在真实首锚均为零；完整 M=0 与常 scalar 末芽又给全部末值为零。特别 μ 的端值还使用 ηₛ=0，不能只凭原 Bⱼ 的末值擅自忽略这项。

式 (5) 中 η 的导数继续来自唯一真实关系 ωₛ=kₛ/(2h)，不是一个独立控制。完整 R100 证书的 23 条实际 RHS 及初值全保留；本 consumer **新增独立 histories 为零**，仅改变其中五条系数历史的坐标。

坐标有准确逆式

$$\begin{aligned}
B_4&=p,\\
B_3&=\zeta+4\eta p,\\
J_2&=2\zeta-2\ell+6\eta p,\\
B_2&=\mu+\eta_s/8+3\eta\zeta+6\eta^2p,\\
J_1&=2\mu+\eta_s/4-2\nu+4\eta(\zeta-\ell)+6\eta^2p.
\end{aligned}\tag{6}$$

公开实际已从完整余式反代 (6)，准确回到原系数历史，所有差式为零。

## 3. 完整二次 action 的系数表

下表给 𝓡₇ 的全部 14 个非零历史组。表中的导数都是固定尾参数 c 的真实 s 导数；h、k、ω 是参考带的 scalar 数据，k 不是曲面主曲率。未列出的历史单项式系数为零。

表是公开[完整可读系数](../notes/actions-43642966285-1-pure_tail_c7_reduce/pure-tail-c7-action-expressions.json)的因式整理；该文件也逐项保留全部 96 个 Laurent monomial，hⱼ、kⱼ 分别表示相应 j 阶真实导数。

| 历史单项式 | 完整系数 |
|---|---|
| 1 | C₀，见 (7) |
| ℓ | −hkηₛ/2 |
| ζ | 81hkηₛ/80 |
| p | (41G/40+36hkη/5)ηₛ−3kρ/(20h) |
| ℓμ | −4hk |
| ζν | −4hk |
| ζμ | 36hk/5 |
| ℓζ | −7G/2−32hkη |
| pμ | 73G/10+252hkη/5 |
| pν | −7G/2−28hkη |
| ζ² | 73G/20+152hkη/5 |
| pℓ | −3ηₛₛ−28Gη−140hkη²+2k/h |
| pζ | 39ηₛₛ/5+306Gη/5+1372hkη²/5−23k/(5h) |
| p² | 136ηηₛₛ/5+686Gη²/5+2394hkη³/5−86kη/(5h)−9G/(10h²) |

其中完整局部常数组为

$$\boxed{\begin{aligned}
C_0={}&\frac{7+7k^4-X^2-6X+38k^2}{1280}
+\frac{(32X+25\rho^2)k^2}{2240}\\
&+\frac{179\rho k k_s-43k k_{ss}-50k_s^2}{8960}
-\frac{hk\omega(G+8)}{160}.
\end{aligned}}\tag{7}$$

例如 pμ 系数原有五项，使用 G=k²−1+hₛₛ/h−2ρ² 和 ω=η+k/h 合并为表中两项；p² 系数的二十个原 Laurent 项合并为表中五项。式 (7) 展开为准确十七项，并保留与 ω 相连的部分。

完整 action 的历史总次数是二。这里“二次”包含零次和一次项，不是仅剩一个齐次二次型。不能删除 C₀，也不能只保 μ、ν 的交叉项去讨论正负。特别，C₀ 中的正数 7/1280 不意味着整个 action 或整个周期为正；其余局部与历史项均可能影响真实积分。

## 4. 为何端势只移走两条低参数历史

R95 完整二次部分的三个最高参数系数是

$$
[c^2](C_{cc}-5D_c+17hK/20)=-56p_s/5,
$$

$$[c^3](C_c+2D)=8p_s,
\qquad[c^3](B_c+5J)=14p.$$

所以 c⁷ 层中 B₁、J₀ 的系数分别为 128ppₛ/5 和 16ppₛ。常数组 L₀ 没有 histories，线性项 b L̃_b 的局部参数次数至多四，因而不能为 c⁷ 添加 B₁ 或更低历史。微分 (1) 正好消掉这两个系数，仍保 p²C₁、p²D₀ 的实际贡献。

此后恰剩 B₄、B₃、B₂、J₂、J₁，按 (6) 换成五个真实坐标。新增 μ、ν 的 ODE 来自移动参数 v=c+η 下的

$$
\beta_2=B_2-3\eta B_3+6\eta^2p,
\qquad j_1=J_1-2\eta J_2+6\eta^2p,
$$

$$
(\beta_2)_s=\eta_{ss}/8-3\eta_s\zeta,
\qquad(j_1)_s=(\eta_{ss}-k/h)/4-4\eta_s(\zeta-\ell).
$$

取 μ=β₂−ηₛ/8、ν=β₂−j₁/2 即得 (5)，包括其零初值与末值的准确范围。

## 5. 与反射、仿射不变量及四块的关系

scalar 反射 σ 保持 h、ℓ、ζ，而使 k、ω、p、μ、ν 反号。公开 actual 还对新的完整余式核了这项反射偶性，准确差式为零。

因此不能使用 R100 的 c⁸ 反号来消去这里的 c⁷。对 R104/R106 的四块设计，(3) 的贡献恰为原 B 的四倍：

$$a_7(\mathcal C)=4\mathfrak m\int_B\mathcal R_7\,ds.$$

R107 又表明 a₈=0 后，这个 a₇ 不能仅靠整体 h 缩放或 ω 平移消除。下一真实问题是该积分在受 (5)、完整 M=0 和共同端口约束下的符号、可达值，或用其他真实第四方向支付它；不是任取五个形式函数来令一个二次式为零。

## 6. 公开实际证据

实际运行完成用时 **0.141771324 秒**，峰值 RSS **42.234375 MiB**。全部十条新增准确差式为零：两条最低历史系数、端势的 p=0 端值、μ/ν 的两条真实 ODE 和两条常芽 trace、五坐标逆变换、完整消费 c⁷ 身份及新的反射偶性。没有意外原 histories，全部 23 条旧 histories 保留。

| 实际文件 | bytes | SHA-256 |
|---|---:|---|
| [主报告](../notes/actions-43642966285-1-pure_tail_c7_reduce/pure-tail-c7-action.json) | 8935 | `10bee55ddda0e8be85d97725ac5cc12fd5a92f51652c21bf7db8b009b2e12f22` |
| [完整可读式](../notes/actions-43642966285-1-pure_tail_c7_reduce/pure-tail-c7-action-expressions.json) | 11811 | `c94dc2d08468f9b0422d48a1bd1c875c5fb5d61d7a1cd2c634c406956d872c04` |
| [完整证书](../notes/actions-43642966285-1-pure_tail_c7_reduce/pure-tail-c7-action-certificate.json.gz) | 81402 | `7f6388ba9a88a2bf1685007a4a9c9e909461049002c26ac6eae8cafcd6aaa97e` |

证书解压 723,127 bytes，SHA-256 `661ecc435ec80e23f75c1e566d00d0d1e025e21feaf3d57083f6d18a2d8110f7`。原完整参数族 3154 项原样保留；源码 [literature_pure_tail_c7_reduce.py](../scripts/literature_pure_tail_c7_reduce.py) 为 21,545 bytes，SHA-256 `86cd885a8a1f224389f1cd9f4139ba17a8d9bb9bd20a7432572f6e866fb91d17`。

仍未授予：action 的统一符号、某一真实路径非零周期、非平凡零第四成本环、完整 period/ruling、高阶收敛或有限等距族。完整有限闭面、嵌入、reach 和宏观幅度也尚未支付。
