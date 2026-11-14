# R25：同一 M12 闭族的更紧包围球与几何比例

2026-11-09，Astra-visible-flex-db6f0b0e；作者 `/root/coupled_prefix`。**已证明：以下结论针对 R21 已严格认证的有限闭图；两份全文独审、独立实际重放与独立有理重构均通过，root 全文复核通过。** 没有改变几何、目标 $g$ 或任何求解参数，也没有新增完成门。本文只收紧已审 R21 唯一指定图的直径上界；主 G5 研究继续。

## 1. 结论及旧 3.92 的来源

对象仍为 `2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json`，SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`，使用其第一档 critical 尾 `cc23977e…`。没有混入 uniform M12 或第二档尾的位置数据。

R17 与 R21 的 $D\le3.92$ 是选定公共球半径 $R=49/25$ 后验证得到的。尾部检验把全径向上界 $c+U$ 与全高度上界同时放进一个矩形，再验证其外接球；它没有使用半径与已累计高度之间的联系，也不是实际直径或最小包围球。

已有**同一图**的完整连续 prefix 证书给精确 binary 上端点
$$
R_P=\frac{2131902881202937}{1125899906842624}
\simeq1.8935101319809684.
$$
以下只复用九段已认证积分，证明其两尾、圆领和两帽均严格在这个球内。因此对所有相位都有
$$
\boxed{|F^{12}_t(p)|\le R_P},\qquad
\boxed{D_{12}\le 2R_P
=\frac{2131902881202937}{562949953421312}
\simeq3.787020263961937.}
$$
直径**上界**比原3.92减少约3.39234%。这不宣称实际直径变了，更不宣称此球最优。

保留 R21 原有的绝对 reach、位移与握持区下界，即得到
$$
\frac{\operatorname{reach}}{D_{12}}
\ge\frac{316912650057057350374175801344}
{10156379431358714998583735712015}
>0.03120330942723168,
$$
$$
\frac{\delta_{hold}}{D_{12}}
\ge\frac{1800459358092517}{34110446099246992}
>0.05278322519892998.
$$
两完整固定帽的直径与 $D_{12}$ 之比下界相应大于 .9354609822667627。没有重新计算曲率、metric 或非全等矩。

## 2. 已审输入与高度规范

使用已审 height 报告 `db6f-tail-background-height-rigorous.json` 的 cell0 九段 A/B/AH/BH 区间，以及 `db6f-tail-tight-alpha.json` 的真实归一化夹界
$$
0<\alpha_-\le\alpha\le\alpha_+,
\qquad \alpha\in[97.64534740775791,97.64534740780157].
$$
这里 $\alpha$ 是冻结背景真积分定义的全局径向乘子，不是浮点保存值。有限源校准表、checkpoint 和 bookkeeping 身份相同；紧 alpha 的完整独审是已有 R21 背景链的一部分。

同一 critical 图的完整 first-jet 证书已经覆盖有限尾及自身 R6 圆领，给
$$
|V_h|\le U,\qquad |V_z|\le V,
$$
其中 $U,V$ 使用该报告有限段/圆领最大值的精确 binary Fraction，不取采样估计。

上尾按已审 R17 定义为
$$
X(r,\theta)=\left(r e^{i\theta}+V_h(r,\theta),\ H_c+\int_r^c w(\rho)\,d\rho-V_z(r,\theta)\right).
$$
共同 cut 常数不是 moment 报告的整个角向 `complete_cut_height_interval`。原闭预算的已审代码精确使用
$$
z_+=H_{c,+}+B_{\rm old}+V,\qquad z_-=H_{c,-}-V.
$$
因此本账本从其保存的 `tail_height_upper.exact`、原 height 上界的精确 binary Fraction 和同一 $V$ **精确相减**恢复 $H_{c,+}$；下端同理恢复。没有用小数显示反推。所得 $H_{c,+}\simeq1.771304847994985$，且 $H_{c,-}-V>0$。这个区间正是原闭预算消费的 `shape.background_cut_height` 包围，与当前 common-cut gauge 相同。

## 3. 九段连续位置盒

背景 cell0 的九个源段按 $j=0,\ldots,8$ 从内到外排列，正径向速度为
$$
r_x=A(x)+\alpha B(x)>0.
$$
每段严格积分分别为
$$
A_j=\int A,\quad B_j=\int B,\quad
A_{H,j}=\int wA,\quad B_{H,j}=\int wB.
$$
实际径向长度及背景增高是
$$
L_j=A_j+\alpha B_j,\qquad
J_j=A_{H,j}+\alpha B_{H,j}.
$$
已审报告的端点给出安全界
$$
\ell_j=A_j^-+\alpha_-B_j^-\le L_j,
\qquad h_j=A_{H,j}^++\alpha_+B_{H,j}^+\ge J_j.
$$
这里所有 $B_j^-$ 非负。少数 $A_j^-$ 为约 $-4.05\times10^{-320}$ 的向外舍入下界；它们仍有效，账本原样保留，不假设这些下端点非负。各 $\ell_j$ 仍严格为正。

对真实第 $j$ 段内的任意点，从 cut 向内经过的完整外段是 $k>j$，因此
$$
r\le c-\sum_{k>j}L_k
\le c-\sum_{k>j}\ell_k=:\overline r_j,
$$
$$
\int_r^c w\,d\rho
\le\sum_{k\ge j}J_k
\le\sum_{k\ge j}h_k.
$$
第二式将当前段的全部高度计入，故覆盖它的每一个连续内点，不依赖节点、角向采样或数值 inverse。由于高度为正、扰动有全域上界，
$$
|X(r,\theta)|^2
\le(\overline r_j+U)^2+
\left(H_{c,+}+\sum_{k\ge j}h_k+V\right)^2
=:Q_j.
$$
账本按 $8\to0$ 的真实顺序逐段累加，比较全部九个精确有理 $Q_j$ 与 $R_P^2$。它们全部严格小于 $R_P^2$；最大在 $j=7$，
$$
\max_j Q_j<3.564799,
\qquad \sqrt{\max_j Q_j}\simeq1.888067344624084<R_P.
$$
平方根小数只作说明；正式比较直接在平方的 Fraction 上执行。

## 4. 全部内层、圆领与固定帽

令 $\ell_0^{tot}=\sum_{j=0}^8\ell_j$、$h_0^{tot}=\sum_{j=0}^8h_j$。实际 cell0 内边界半径满足
$$
r_1=c-\sum_jL_j\le c-\ell_0^{tot}=:\overline r_1.
$$
已审背景高度证明给其余全部 cells（包括无限深背景）$0\le w\le1/49$，R17/R21 的实际 cuff 满足
$$
7/50<a_c<3/20.
$$
所以 cell0 内侧的总背景高度不超过
$$
\frac{r_1-a_c}{49}
\le\frac{c-\ell_0^{tot}-7/50}{49}.
$$
本次故意采用安全有理 cuff 下界 $7/50$，不把派生 cuff 的浮点显示当作精确半径。故全尾背景增高有新界
$$
B_{new}:=h_0^{tot}+
\frac{c-\ell_0^{tot}-7/50}{49}
\le0.05193687255607195.
$$
对所有内层和圆领，
$$
|X|^2\le(\overline r_1+U)^2+(H_{c,+}+B_{new}+V)^2
<3.420004<R_P^2.
$$
圆领的扰动包含在同一个 $U,V$ 内；背景依旧是同一个 $w$，没有另加 taper 或改变表示。

上帽采用 R16 原三凸起，总高度介于0与 $h_0=1/2000$；下帽平坦。两帽的径向半径小于 $3/20$，所以统一有
$$
|X_{cap}|^2\le(3/20)^2+(H_{c,+}+B_{new}+1/2000)^2
<3.348534<R_P^2.
$$
真实帽位置来自相同 $H_c$ 与全背景增高，故这里没有将帽平移到另一个几何位置。

## 5. 完整性、全时性与比例

上前缀已由原完整连续证书给 $|X|\le R_P$。下前缀与下尾是 z=0 镜像，范数不变；两帽由上一节覆盖。故初始完整图在原点中心的 $R_P$ 球内。

所有相位的活动带像集只是绕原 z 轴旋转，材料角换元不改变像集；固定帽不动。原点球在该旋转及镜像下不变，所以同一个球界覆盖全部 $t\in[0,1]$，不需采样相位。任意同图两点以三角不等式给 $D\le2R_P$。

R21 的绝对 reach 下界、支撑、曲率、位移见证与固定帽直径下界均未变。把这些同图下界除以新的 $2R_P$ 即给 §1 比例。此推导没有更换 metric、调用新曲率界，或把全局盒界误当实际点对距离。

## 6. 可复现记录及未来候选的使用范围

脚本 `scripts/db6f-prefix-m12-segment-ball-budget.py` 只加载被冻结的真实元数据/证明哈希，以 Fraction 计算；没有导入 solver、几何读取器或区间后端。作者实际自然 exit0：

```bash
python scripts/db6f-prefix-m12-segment-ball-budget.py \
  --out notes/2026-11-09-db6f-prefix-m12-segment-ball-budget-NEW.json
```

原输出 `2026-11-09-db6f-prefix-m12-segment-ball-budget.json` 保存九段各自的径向/高度/平方范数上界、内层与帽界、严格余量、完整输入哈希和上述比例。输入里的大分母仅来自原向外舍入微小负下端点；所有比较为精确有理比较，不因此截断。

本脚本固定 R21 M12 的真实输入，以免把旧数字误用到未来候选。将来若使用同背景的最终图，可复用这些解析公式和背景积分/alpha，但必须重新绑定该图自己的完整 prefix norm、实际 tail/collar 扰动界、共同 cut 高度和绝对 reach/位移。若新图不满足 $Q_j<R_P^2$，可取所有分量最大值的新的有理球上界；不能保留本图数字。没有必要为此先跑全位置后端或点对距离搜索。

本文是已有连续证书的额外位置预算。它不支付原误差降到求解容差、无限尾存在、最终全流程复跑或 README 完成。

## 7. 独立审查与冻结身份

本定理的完整证明与原作者稿数学内容相同。以下文件保存源码审查、真实退出证据和独立重构；所有旧 R21 证书保持原字节。

| 证据 | SHA256 |
|---|---|
| [作者完整证明](../notes/2026-11-09-db6f-prefix-m12-segment-ball-proof.md) | `bad275038aa56b96209620cfe91a0154fbb2dad55697c58264ea80b6c3044935` |
| [有理计算脚本](../scripts/db6f-prefix-m12-segment-ball-budget.py) | `b209f8e1feadf1fb39c9ba4c8173d617728d88532ebe130e92b3914b12066a89` |
| [作者账本](../notes/2026-11-09-db6f-prefix-m12-segment-ball-budget.json) | `f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c` |
| [tail_theory 全文独审](../notes/2026-11-09-db6f-tail-review-m12-segment-ball.md) | `66f81cc89c824ef30a8d810bb4c46ed2ac8a4f4a2c6c937c8922905bf512a444` |
| [independent_geometry 全文独审](../notes/2026-11-09-db6f-audit-m12-segment-ball-review.md) | `f5d159299e8f74e3bf6840210a60f31d1c4bfd09553dfe09c1930f4c5a908eb6` |

两位审查者各自实际重放作者脚本并自然 exit 0，输出均与作者账本逐字节相同；另分别编写未导入作者计算器的 Fraction 程序重建位置界与比例。independent_geometry 的检查实际覆盖 24 项冻结绑定、95 个精确字段。原连续证书的解析有效性使用其已经完成的独审，本次没有重跑原积分或全几何后端。

[root 全文复核](../notes/2026-11-09-db6f-root-review-m12-segment-ball.md) 已核对三份关闭清单的全部 15 件文件。清单为 `prefix-m12-segment-ball-publication`、`tail-closed-publication-11` 和 `audit-m12-segment-ball-publication`，分别绑定作者、第一独审和第二独审产物。历史作者稿及账本的 pending-review 状态不被改写；本节记录其后已经完成的审查。
