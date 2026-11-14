# vu032 强前缀的连续水平半径包络

2026-11-12，root，GPT-6 Astra Pro，AI-assisted。

## 对象与结论

对已正式保存的 `2026-11-12-strong-angle-vu032-q085-m20.json.gz`，用全部实际五次系数和冻结的背景程序，对每一个径向区间及全部角度给出

\[
|F_{xy}(s,\eta)|\ge
69141903081734805054098178565\,2^{-98}
>0.2181733770150431.
\]

这里的对象是**明确固定的有限实表达式**：输入 binary64 系数、分段常数和64点求积节点/权重都作为精确二进制数，随后以实数运算解释公式。它不是源函数的精确径向积分，也没有把分段舍入数据自动认成全局 C² 曲线。因此，本结论支付的是这个有限水平表示的正半径；尚未支付 R9 的角向正性或投影 Jacobian、竖直高度、精确共同度量、嵌入、闭合、reach。

计算覆盖原保存网格的全部888个五次区间，按背景分段切成910个交叠片。最小下界位于第5段 loop outward turn，实际区间编号637。末端 brake 段的下界为0.2999989384029172。不能因此把整个前缀的半径下界写成0.29；R21 中此前0.29只是一个有条件的装配示例。

## 不采角度的估计

将水平平面写成复数。原材料角图的冻结参考部分与实际扰动为

\[
Z=a(s)\{(1-b)e^{i(\eta+bA(\eta))}+bC(\eta)\}
 +q\,(R(s,\eta)+iT(s,\eta))e^{i\eta},
\]

其中 \(b=1-x^3(10-15x+6x^2)\)、\(x=s/L\)，而参考支持函数 \(h\) 满足
\(\Re(Ce^{-i\eta})=h\)。所以

\[
|Z|\ge\Re(Ze^{-i\eta})
=a\{(1-b)\cos(bA)+bh\}+qR.
\]

由实际冻结参考 Fourier 系数 \(c_n\)，取

\[
A_* =\sum_n |1-n^2|\,|c_n|/n,
\qquad h_* =1-\sum_n|c_n|.
\]

在一个径向片上，程序以有向包络得到 \(0\le b\le B\le1\)、\(a\ge a_*>0\)，并验证 \(A_*<\pi/2\)。令 \(C_* =\cos(BA_*)\)，则参考径向分量的共同下界为

\[
G_* =\min\{C_*,(1-B)C_*+Bh_*\}>0.
\]

实际五次 Fourier 系数逐项用区间 Horner 法求值，得到

\[
R(s,\eta)\ge \underline{R_0}-\sum_{j=1}^{20}\overline{|R_j|}=:R_*.
\]

由于保存的 gauge \(q>0\)，最后使用 \(a_*G_*+qR_*\)。切向扰动 \(T\) 在这个投影恒等式中精确消失；未忽略它对其他几何量的影响。对全部角度的结论来自此恒等式和 Fourier 的绝对和界，不来自角采样。

## 背景有限程序与算术范围

`root_prefix_radius_enclosure.py` 首次从原 provider 的真实 profile/port 构造并冻结12个背景段，要求物理尾参数、cut、总弧长与成功包精确匹配；随后重跑使用同一个冻结程序。Hermite 和旧 cubic boost 使用其多项式公式；angle boost、turn、coast、brake 使用原64点求积和分段转角公式。转角在每个子段单调，用端点包络整个 sin 值域。

原 mesh 和各段界点按精确二进制有理数分割。每段边界外扩 \(10^{-12}\) 后与 mesh 相交，覆盖舍入导致的细小界点缝隙；相邻片重复覆盖不影响下界，程序逐个有理区间核对没有漏域。这是对有限程序的保守包络，**不是对接缝的修补**。真实积分误差以及积分半径与独立保存导数之间的一致性仍须另外认证。

本次使用 python-flint 0.9.0 的 Arb，midpoint precision 为96bit。每个 binary64 输入以其精确二进制值进入；最终下界由 `.lower().man_exp()` 保存为精确 dyadic，JSON 中的小数仅作显示。Arb 的球运算与输入语义见官方文档：

- <https://python-flint.readthedocs.io/en/stable/arb.html>
- <https://python-flint.readthedocs.io/en/latest/general.html>

## 分段结果

下表为包络下界的小数显示，正式有向值在 JSON 的 mantissa/exponent 中。

| 段 | 背景类型 | 水平半径下界 |
|---:|---|---:|
| 0 | Hermite | 0.9084860642 |
| 1 | angle boost | 1.0145730584 |
| 2 | first descending turn | 1.0513565313 |
| 3 | coast | 0.3526623595 |
| 4 | speed sync | 0.3391661691 |
| 5 | loop outward turn | 0.2181733770 |
| 6 | loop coast | 0.3481450804 |
| 7 | loop inward turn | 0.3832712554 |
| 8 | coast | 0.3499972285 |
| 9 | terminal turn | 0.3353957780 |
| 10 | terminal coast | 0.3086110240 |
| 11 | terminal brake | 0.2999989384 |

完整重跑在2.3–6.5秒内完成，峰RSS不超过44148KiB，exit0；不构造 BVP 或 Jacobian。补充输入守卫要求base mode为2且blend范围恰为整个径向区间，不改变当前包络。

## 复现与身份

从课题目录执行：

```bash
python computations/root_prefix_radius_enclosure.py \
  --input notes/2026-11-12-strong-angle-vu032-q085-m20.json.gz \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --snapshot notes/2026-11-12-root-vu032-radius-program.json \
  --out notes/2026-11-12-root-vu032-radius-enclosure.json.gz
```

- 成功输入 SHA256：`4562ab36dcfcdbef4456ed89429288caafb4c495cf248101c90240c23cad0441`。
- 冻结背景程序 SHA256：`0ae1ba8b879f3b368005b18897acb57e88ca598bebfb7789b08e1a90164fac06`。
- 本次包络脚本 SHA256：`3f0363237812895bb7289303e976c903a365b97732453989b7e3a8e3c793a68c`。
- 程序还逐块核对原五次系数 SHA256、布局和连续状态编号，报告保存每个片的全部下界分量。

该工具以后可复用于同一种实际表示，不能把当前数值移交给另一幅度或另一背景。接下来几何账本仍需要实际高度、角向/投影导数以及全部接缝和连续法向弦输入。

## 进一步支付有限表示的角向单调性

同一个对象上，`root_prefix_angular_enclosure.py` 又对全部910片证明

\[
\partial_\theta\beta
\ge 60065586970290931610293035489\,2^{-98}
>0.1895335732400604,
\]

其中 \(\beta=\arg Z\)，\(\theta=\eta+bA(\eta)\) 是真实材料角。全部角向 determinant 下界为正。因为前面的径向投影 \(U=\Re(Ze^{-i\eta})>0\)，可选连续 lift \(\beta=\eta+\arctan(V/U)\)，后项为周期函数，所以每个纬圈的绕数恰为1。

具体地，写 \(Z=e^{i\eta}(U+iV)\)、\(Z_\eta=e^{i\eta}(P+iW)\)，则

\[
\begin{aligned}
U&=a[(1-b)\cos(bA)+bh]+qR,\\
V&=a[(1-b)\sin(bA)+bh']+qT,\\
P&=-a(1-b)\sin(bA)(1+bA')+q(R_\eta-T),\\
W&=a[(1-b)\cos(bA)(1+bA')+b\rho]+q(R+T_\eta),
\end{aligned}
\]

这里 \(\rho=h+h''=1+A'\)。脚本用同一Arb径向包络和 Fourier 绝对和，分别取得 \(U\ge U_*>0\)、\(W\ge W_*>0\)、\(|V|\le V^*\)、\(|P|\le P^*\) 与半径平方上界 \(r^{2,*}\)，逐片验证

\[
UW-VP\ge U_*W_*-V^*P^*>0,
\qquad
\beta_\theta\ge
\frac{U_*W_*-V^*P^*}{r^{2,*}(1+B\sum_n|1-n^2||c_n|)}.
\]

其中参考支持函数及导数界直接由冻结的真实系数计算。实际R/T五次系数也逐块校验，导数采用精确 Fourier 因子2j；没有径向有限差分或角采样。5.80秒、峰RSS46772KiB、exit0。输出为 `notes/2026-11-12-root-vu032-angular-enclosure.json.gz`，其输入hash还绑定上面的完整半径报告和辅助脚本。

复现时先运行上一节半径命令，再执行：

```bash
python computations/root_prefix_angular_enclosure.py \
  --input notes/2026-11-12-strong-angle-vu032-q085-m20.json.gz \
  --snapshot notes/2026-11-12-root-vu032-radius-program.json \
  --radius-report notes/2026-11-12-root-vu032-radius-enclosure.json.gz \
  --out notes/2026-11-12-root-vu032-angular-enclosure.json.gz
```

这进一步支付R9所列条件中的角向单调性和绕数，但对象依旧是上述有限水平表达式。竖直/径向投影Jacobian仍未认证，不能从本节推得曲面嵌入或reach。
