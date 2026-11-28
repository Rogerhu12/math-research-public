# R150 补篇：原 F9 极点及实际头整提升排除四个 H1 完成块，余图至多十个完整点

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 已完成结论及准确范围

本篇在 unit211、$\Phi=0$、物理 $D\ne0$ 的 H1 余图中，完整排除此前模次数为 $1,1,3,4$ 的四个实际 $P_{201}$ 完成块。不是把模 h 零直接提升为特征零 h 零；新的完整 QQ 原 Dixon 极点证书和实际原头的整 Bézout 身份付清了这个提升。

结合[第五块的真实原几何返回](R150-appendix-unit211-Phi-zero-H1-fifth-block-original-geometry-and-334-points.md)，现在只有次数为 $5$ 的最后完成块尚未排空，且

$$
\boxed{
\#(u,Q)\le5,\quad
\#(u,Q,\lambda)\le5,\quad
\#(u,Q,\lambda,T,v)\le5,\quad
\#(\text{完整固定规范原点})\le10.
}
\tag{1}
$$

式 (1) 是不同点的上界。最后块可能仍为空；本篇没有证明它存在，也没有排除它。原 $D=0$ 图、其它 $\Phi$ 分支、W 图和普通不变子空间问题不由本篇关闭。

## 2. 真正的原 QQ 极点证书

沿用[原三头零集完整排除](R150-appendix-unit211-Phi-zero-H1-new-three-head-zero-complete-original-exclusion.md)的原四次 $g_4(u,Q)$、实际原头

$$
h=\det(H_R,H_W,H_N)
=(u-1)^5Q^3T_0^2\ell_nh_*.
$$

$F_9$ 仍严格定义为 $\operatorname{Norm}_{g_4}(h_*)$ 的唯一首一 QQ 九次因子，不从模因子猜测。其规范系数字节数为 138，SHA256 为
30a60a6e2188e060f610ae64e0df7543dec5cce437c7c355d5987bf5a8fb7e39。

旧原 Dixon 计算已给整个首一 Q 四次代数上的唯一向量

$$
q=D_8^{-1}e_0
$$

和其全部最终坐标极点、原图极点的平方自由覆盖

$$
C_{256}=C_{55}P_{201},\qquad \deg P_{201}=201,
$$

其中去掉的 $u,u-1$ 已在原图支付。本次只构造这个原 $8\times8$ 矩阵和次数 418 的原分母覆盖 $S$，没有重跑旧 QQ(u) Gaussian。

在完整域 $K_9=\mathbb Q[u]/(F_9)$ 中，本次实际返回

$$
a(Q)g_4(Q)+b(Q)h(Q)=Q-q_h,\qquad
g_4(q_h)=h(q_h)=0.
\tag{2}
$$

新 (2) 用的是未剥任何因子的**实际原 h**。因子 $h_*$ 只用于固定 $F_9$ 的定义。

随后实际核

$$
\gcd(F_9,S)=1,
\qquad
\boxed{D_8\big|_{K_9,Q=q_h}=0_{8\times8}.}
\tag{3}
$$

全部 64 个原系数都在同一个九次域中返回零。这次的专门化秩为 0，根本没有进入非零 Gaussian 主元步骤。取 $w=e_0^{\mathsf t}$，全部八个乘积及常数目标配对实际返回为

$$
wD_8=0,\qquad we_0=1.
\tag{4}
$$

若旧唯一 $q$ 的全部八个分量的四坐标（共 32 个标量坐标）都在 $F_9$ 处正则，(3) 的源分母互素性允许把原 $D_8q=e_0$ 专门化到 $K_9,Q=q_h$，即得 $0=e_0$，矛盾。因此至少一个真正最终坐标分母含 $F_9$。又因为 $F_9$ 与原源覆盖及 $u(u-1)C_{55}$ 互素，旧完整覆盖立即给

$$
\boxed{F_9\mid P_{201}\quad\text{于 }\mathbb Q[u].}
\tag{5}
$$

这里的论证使用真实特征零零矩阵与常数目标不相容，不是从模秩下降猜测 QQ 秩下降。Dixon 列本来只是原点的必要列；本论证只使用其已付唯一向量和极点定义，不把它们另称为未经证明的原理想生成元。

## 3. 四个原 λ cofactor 在该同一个 Q 分量全零

还需把 (5) 接到当前保留的同 Q 原理想。以下是完整的原列恒等式，不重新执行旧范数门。

记三个原二次头构成 $H$，其原常数与线性尾为 $N$。缩放规则恰为

$$
\mathcal R=-\operatorname{adj}(H)N.
$$

在 $K_9(\lambda)$ 上，$h=0$ 给 $\operatorname{rank}\operatorname{adj}(H)\le1$，所以 $\mathcal R$ 的三行位于同一条线，包括全部为零的情形。转置后令共同列方向为 $c$；三个规则列为 $a_0c,a_1c,a_2c$。

原缩放乘法矩阵 $M_T$ 的第 0 列是 $(0,h,0)^{\mathsf t}$，此处为零；其余两列是 $a_0c,a_1c$。剩余原 O 列 $r$ 也在同一列方向上，所以

$$
r\in K_9(\lambda)c,\qquad M_Tr\in K_9(\lambda)c.
$$

当前四个固定原 $\lambda$ cofactor 都含前两列 $r,M_Tr$，第三列分别是 $M_vr$、真实交换子 T 列、完整 F6 列、完整 NV 列。因此四个 cofactor 在同一 $F_9,Q=q_h$ 上恒为零。

原 primitive 化只除当前原图已付权单位。旧实际九次头零模型已核这些单位在其整个真实 Q 分量非零；旧 $g_4,h_*$ 的一次根也满足原 h 零，由新 (2) 的唯一性必等于 $q_h$。故 primitive 四式 $F_0,F_c,F_m,F_n$ 仍全零。

于是三个固定原结果式

$$
r_i=\operatorname{Res}_\lambda(F_0,F_i),\quad i=c,m,n
$$

在同一个 $q_h$ 上为零。评价 $Q\mapsto q_h$ 是原四维 Q 代数的非零线性商，因此乘 $r_i$ 的完整正则矩阵奇异。其真正原范数满足

$$
F_9\mid N_c,\qquad F_9\mid N_m,\qquad F_9\mid N_n.
\tag{6}
$$

此处不倒置 h，不在头零处建立错误的自由三生成元模型，也不重放旧 QQ 范数计算。

## 4. 完整整身份和四个真实完成块

固定 $p=1009$。本次实际核首一 $F_9$、$q_h$ 及 (2) 中 $a,b$ 的全部系数均在

$$
\mathbb Z_{(1009)}[u]/(F_9)
$$

中。原 $q_h$ 的次数为 8，规范字节数 262，SHA256 为
3d1857776ac5d69e429833db333847359e2e98874553ac50a8e37a56135e3ff7。
完整 Bézout 系数身份的 SHA256 为
e28ee18505b3f90475accd65c3d5b0cd8026f6dddae9d5cb4effb3221fa0bcd3；
只保存定义与身份，未保存可重算系数载荷。

$\overline F_9$ 首一、次数保持 9、平方自由。其完整因式分解乘积实际返回，次数模式准确为

$$
1,1,3,4.
\tag{7}
$$

| 次数 | 模因子规范 SHA256 |
|---:|---|
| 1 | a103b9ea1ab500ebd624c6c616659f2d805a764d622ed83bedfdf7d5c7b266dd |
| 1 | b3bbce2093c7010b6fbeeb60bd1db1a04093f9bd1ff672121557bfe9521a0c38 |
| 3 | 9d01d315c97361825a1fc0e0ebd2f61e46b3179a09d306ac56d2cc8302487916 |
| 4 | e65a337d8d9d8132a57a3b16e26437e817a903234d9258ec8bf7d67fec2393cc |

[整 P201 的完整约化](R150-appendix-unit211-Phi-zero-H1-P201-integral-squarefree-complete-modular-reduction.md)已证明 $P_{201}$ 首一整、模约化平方自由。由 (5)，首一长除给 $P_{201}/F_9$ 也整；$\overline F_9$ 与补因子互素，因此它对应的真实 Hensel 因子确实落在 F9 上。

再由 (5)–(6) 及首一整长除，

$$
\overline F_9\mid
\gcd(\overline P_{201},\overline N_c,\overline N_m,\overline N_n)
=G_{14}.
$$

已付 $G_{14}$ 的完整模式为 $1,1,3,4,5$，所以 (7) 恰好选中前四个当前块。不能只凭总次数九作这一步；例如 $4+5$ 也为九。本次已经返回完整模式和乘积，而且因子身份逐项吻合。没有把一个模不可约因子直接认成 QQ 因子。

## 5. 在真实同 Q 商中提升为 h=0

令 $O_\phi$ 为任一上述实际 Hensel 因子给出的非分歧 $1009$ 进整数环，剩余域为 $K_\phi$。由已付原单位子式，实际同 Q 商

$$
R_\phi=O_\phi[Q]/(g_4,r_c,r_m,r_n)
$$

是 $O_\phi$ 的某个商，其模 Q 值为 $\bar q$。此前[原 Q/λ 返回](R150-appendix-unit211-Phi-zero-H1-original-Q-relations-same-lambda-and-354-points.md)已在这四块实际证明

$$
\overline g_4(\bar q)=\overline h(\bar q)=0,\qquad
\overline g_4'(\bar q)\ne0.
\tag{8}
$$

把真实整 Bézout (2) 模约化并代入 (8)，直接得

$$
\bar q=\overline q_h.
$$

因为该真实 $O_\phi$ 来自 F9，(2) 又在 $O_\phi$ 中给 $g_4(q_h)=h(q_h)=0$。在同一个 $R_\phi$ 中，

$$
g_4(Q)-g_4(q_h)=(Q-q_h)H(Q,q_h)=0.
$$

$H$ 的模像为 (8) 的 $g_4'(\bar q)$，是单位；$R_\phi$ 是有限局部整商，所以 $H$ 在 $R_\phi$ 中为真单位。因此

$$
\boxed{Q=q_h,\qquad h(Q)=0\quad\text{于实际 }R_\phi.}
\tag{9}
$$

不要求 $R_\phi$ 自由、平坦或无挠。若其通用纤维本已为零，该块本来为空；否则 (9) 对所有通用原点成立。

已刊原 h=0 定理排除本图的全部原解，故这四个实际特征零完成块均排空。这里才使用旧排除，不重跑其 54 维值门，也不以单独的模 h 零代替 (2)、(5)、(9)。

## 6. 剩余第五块和十点上界

前四块关闭后，只剩 [1be35 原几何定理](R150-appendix-unit211-Phi-zero-H1-fifth-block-original-geometry-and-334-points.md)中的第五完成块。其同 Q、同 λ、完整 T/v 必要几何商均为同一 $O_\phi$ 的商，通用维数至多 5；因此每层不同坐标点的总数至多 5。

原完整规范恢复只再加 $\rho^2=1-Q$ 的至多两个选择；其它 Gram 与值坐标由已付原恢复确定，故得到 (1)。这是同一个有理数域有限点问题的通用纤维计算；扩张到代数闭 p 进域不改变其几何不同点数。没有把模余维当作精确 QQ 长度，也没有重复乘 λ 或 T/v 的次数。

下一输入仍须在第五块加入完整原矩、Gram 的个别 N/P 及 N4(V) 条件。两次首一二次扩张可以保留模 D=0 的全部值根，不预先倒置物理 D。

## 7. 唯一执行、来源和回执

- [新原 QQ 源](../notes/2026-11-28-unit211-Phi-zero-H1-F9-original-Dixon-pole-and-integral-head-lift-8542.py)；
- [执行前完整原输入及条件桥](../notes/2026-11-28-unit211-Phi-zero-H1-F9-original-Dixon-pole-and-integral-head-lift-8542.md)；
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-H1-F9-original-Dixon-pole-and-integral-head-lift-execution-8542.json)。

源 blob 4e9f89b7c3bef195419fee0dc039907e464dc3be，SHA256
61ee08cca0d182948cf33c0a30593eb92f7dc510dcaddf9997f3b375f4580351。

实际 run 46082897887 / job 140785748521，源提交
a4a162683ca6a62321c3100f7d55dfea0ce6d240。
耗时 7.504925993 秒，驱动峰值 55720 KiB，内层退出码 0。
stdout 3862 字节，SHA256
69c4c7e08ad5e1941ade34941d7d98903f91b5d9930313bb539dfcb471a732d4。

2026-11-27 23:31:04.147969 UTC 真实 pull 保持同一提交，两份 README blob 无变。必要前缀仅为 e3cf 的 5447 字节原头定义、ef9 的 14724 字节原 D8 构造。旧全 QQ Gaussian、旧范数门、旧同 Q 秩驱动和旧 h0 原值门均未执行。

未执行草稿 7c57435 在首派前改成使用实际 h 的整 Bézout；实际只有当前 4e9f 版本执行一次。无可重算矩阵、左零向量系数、Bézout 系数或编码分片入库。
