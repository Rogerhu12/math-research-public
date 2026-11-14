# 下一 c⁷ 系数：真实五历史消费设计

日期：2026-11-14。R104/R106 已用有限真实四块将 D25 周期多项式的偶参数系数全部消去；可能留下的最高项是 c⁷。本稿指定一个小 consumer 来提取它的完整真实 action。**新的研究 consumer 尚未运行；下文完整余式的实际项数和证书不得预报为成功。**

## 1. 只消费已有完整参数族

输入为公开 run 43640085842、source `bccbbe27c8c105666b2d2438b9d1d48812e3ce55` 的 R100 结果：

- `notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action.json`；
- `notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action-certificate.json.gz`。

完整证书 gzip 78,737 bytes，SHA-256 `60761416a641f702d60d161fcad1f161c406d6e3969c76f25e090d256a89dab3`；解压 699,591 bytes，SHA-256 `4b2fdc4d5210094575a14316a63705bb392d322aba862731d33727e79928f2df`。

使用该文件已验证的 `parameter_action_polynomial` 和 23 条真实零初值历史。R100 已完整支付原参数族、原 DAG 和 34 条身份；新脚本不重新做那批研究运算，也不重新编译 forcing。输入 receipt、压缩及解压 bytes/SHA、原 source hashes、23 条初值和真实 RHS 仍准确绑定。

新脚本为 `scripts/literature_pure_tail_c7_reduce.py`。研究入口只允许本公开仓库自己的 GitHub Actions；人工开发分支不读取任何研究输入。

## 2. 一条新的零端势

沿用 R95 的归一化 ℳ=307328/15，令

$$
A_7=[c^7]\mathcal A/\mathfrak m,
\qquad p=B_4,
$$

其中 𝒜 是 R95 的完整压缩 action，Bⱼ、Jⱼ 仍由真实系数 ODE 唯一给出。需要消费的端势为

$$
\boxed{\Phi_7=\frac{64}{5}p^2B_1+8p^2J_0.}
\tag{1}
$$

其选择有直接代数依据。R95 二次部分为

$$
B^2\left(C_{cc}-5D_c+\frac{17}{20}hK\right)
+\frac25B(B_c+5J)(C_c+2D).
$$

已知 C₄=pₛ、D₃=2pₛ、J₃=2p。三个所需最高系数分别为

$$
[c^2]\left(C_{cc}-5D_c+\frac{17}{20}hK\right)
=-\frac{56}{5}p_s,
$$

$$[c^3](C_c+2D)=8p_s,\qquad [c^3](B_c+5J)=14p.$$

所以 A₇ 中 B₁ 的完整系数是

$$-\frac{112}{5}pp_s+\frac25(14+1)8pp_s
=\frac{128}{5}pp_s,$$

J₀ 的完整系数是

$$\frac25\cdot5\cdot8pp_s=16pp_s.$$

局部项 L₀ 没有这些历史；b L̃_b 的 L̃_b 参数次数至多四，故不能在 c⁷ 层引入 B₁。B₀ 以及更低的历史也不可能到达此次数。微分 (1) 因而准确支付所有 B₁、J₀ 项，同时保留新增的 p²C₁、p²D₀ 项。

定义完整余 action

$$R_7=A_7-D_s\Phi_7.\tag{2}$$

它只含原来的 B₄、B₃、B₂、J₂、J₁ 五条历史。只因端点 p=0，(1) 已经端值为零；不需要把 B₁ 或 J₀ 在区间内部置零，不要求第三算子 T=0。

## 3. 两个新的真实坐标及零端条件

令 η=ω−k/h，并保留 R100 的

$$
\zeta=B_3-4\eta p,\qquad
\ell=B_3-J_2/2-\eta p.
$$

在移动参数 v=c+η 下，B 的 v² 系数和 J 的 v¹ 系数是

$$
\beta_2=B_2-3\eta B_3+6\eta^2p,\qquad
j_1=J_1-2\eta J_2+6\eta^2p.
$$

定义

$$
\boxed{\mu=\beta_2-\frac18\eta_s,
\qquad \nu=\beta_2-\frac12j_1.}
\tag{3}
$$

R100 的完整局部 C₂、D₁ 公式给

$$
\beta_{2,s}=\frac18\eta_{ss}-3\eta_s\zeta,
\qquad
(j_1)_s=\frac14(\eta_{ss}-k/h)-4\eta_s(\zeta-\ell).
$$

故有两条真正 ODE：

$$
\boxed{\mu_s=-3\eta_s\zeta,
\qquad \nu_s=\frac{k}{8h}-\eta_s(\zeta+2\ell).}
\tag{4}
$$

所有系数 histories 的真实初值为零，常 scalar 端芽令 ηₛ=0，因此 μ、ν 的初值也为零。在末端，只有完整 M=0 才给所有 Bⱼ、Jⱼ 的末值零；再用常端芽，才得到 μ(L)=ν(L)=0。脚本分别报告这项端点范围，不将末值条件当作全区间恒等式。

换元有明确逆式：

$$
\begin{aligned}
B_4&=p,\\
B_3&=\zeta+4\eta p,\\
J_2&=2\zeta-2\ell+6\eta p,\\
B_2&=\mu+\eta_s/8+3\eta\zeta+6\eta^2p,\\
J_1&=2\mu+\eta_s/4-2\nu+4\eta(\zeta-\ell)+6\eta^2p.
\end{aligned}
\tag{5}
$$

因此把 (2) 写成 p、ℓ、ζ、μ、ν 的 action 不会产生五个独立自由控制。它们仍由同一 h、k、ω 和同一真实首锚驱动。

## 4. 新 consumer 的有限工作

唯一 actual 仅做以下新增计算：

1. 从已验证完整参数多项式选择 c⁷ 并按 ℳ 归一，保留整份原参数族。
2. 核 B₁/J₀ 的两条新最高系数、它们至多线性以及 (1) 端势支付后的准确剩余历史集合。
3. 核 (3)–(4) 两条真实导数和常端芽零历史 trace；保全部 23 条旧 RHS，不新增独立状态。
4. 用 (5) 写出完整余 action，反代回原历史，再核 c⁷=端势导数+完整余 action。
5. 仅对新的 c⁷ 余式核 R106 预报的 scalar 反射偶性：p、μ、ν、k 及其所有 jets、ω 反号，ℓ、ζ、h 及其 jets 不变。
6. 输出全证书、全部系数组和可读式。任何未消历史或非零差式均保留并使完成验证为 false；不得丢项后宣布通过。

使用预算：240 s、250,000 DAG nodes、120,000 terms、2,500,000 memoized terms、RSS 1,800 MiB。预算退出只报告资源边界，不授数学阴性。输出 raw 大于 1 MB 时按既有 publisher 压缩，单件保持小于 5 MB。

建议 lane 为 `pure_tail_c7_reduce`，同一个 job 中先人工新接口、再唯一实际：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_c7_reduce.py \
  --check-only --out "$VISIBLE_OUT/pure-tail-c7-development.json"
python topics/visible-flex-new-mechanism/scripts/literature_pure_tail_c7_reduce.py \
  --report topics/visible-flex-new-mechanism/notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action.json \
  --certificate topics/visible-flex-new-mechanism/notes/actions-43640085842-1-pure_tail_c8_reduce/pure-tail-c8-action-certificate.json.gz \
  --out "$VISIBLE_OUT/pure-tail-c7-action.json" --max-seconds 240
```

新的人工接口检查只使用自造的小多项式和自造 metadata：五坐标往返、c⁷ 选择不混入 c⁸、完整端势拆分、错误低历史项不被抹去、JSON 往返，以及输入字节绑定的正确接受/篡改拒绝。它不读取 R100 研究文件，不运行几何、forcing 或真实目标。

## 5. 可授结论的边界

实际成功后可授一个完整、同锚、真实五历史的 c⁷ action 身份。对 R104/R106 的四块设计，其 c⁷ 周期是原单块该积分的四倍。

非零余式不等于非零真实周期；全部 μ、ν、p、ℓ、ζ 的 ODE/端值和完整 M=0 必须共同保留。反射使 c⁷ 成偶性，不能用之前 c⁸ 的反号直接消去它。即使 c⁷ 最后支付，c⁵、c³、c、其他 Dⱼ、mixed 模式、逐 s ruling、有限等距族及主课题几何门仍未完成。
