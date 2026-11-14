# R21 同一闭图分段球界的独立审查

2026-11-09，`/root/independent_geometry`。

**结论：PASS。** 已全文审查作者的完整证明与 Fraction 脚本，并完成一次独立命名的实际重放；另以不导入作者计算器的独立程序重建所有分段和最终标量。没有发现需要修改的数学或实现问题。

本次仅组合已审的原始连续证据，收紧原 R21 M12 图的球包络和直径上界。审查者未参与该图的数值优化。本次没有计算新积分、运行流或根求解、重新评价几何后端，也没有创建另一张图。

## 1. 冻结对象与输入身份

审查对象为：

- 脚本 `scripts/db6f-prefix-m12-segment-ball-budget.py`，SHA256 `b209f8e1feadf1fb39c9ba4c8173d617728d88532ebe130e92b3914b12066a89`；
- 证明 `notes/2026-11-09-db6f-prefix-m12-segment-ball-proof.md`，SHA256 `bad275038aa56b96209620cfe91a0154fbb2dad55697c58264ea80b6c3044935`；
- 作者账本 `notes/2026-11-09-db6f-prefix-m12-segment-ball-budget.json`，SHA256 `f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c`。

实际完整图仍为 `root-flat17-common-cut-m12-critical-r01.json`，SHA256 `253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2`；实际尾仍为第一档 critical manifest，SHA256 `cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。前缀连续位置界、该尾自身的完整 first-jet 界、共同 cut 几何、原闭预算及 R21 whole 报告的身份相互一致。没有引用 uniform 或第二档尾的位置值。

独立检查程序还实际重读该 manifest，确认其精确二进 `rCut` 等于前缀物理 profile 的 cut；实际 cuff 严格满足 $7/50<a_c<3/20$。高度报告和紧 alpha 的 checkpoint、bookkeeping 相同，cell 0 校准区间等于冻结表的同一常数；alpha 的六个输入文件均重新核 SHA。现有同背景 transfer 的实际文件也已核验。这些检查支付的是固定已审对象的身份；没有重新证明原始积分区间或逐行连续证书。

## 2. 真实段顺序与高度基准

已审 source 实现中，第 $j$ 段的旧源距离为
$$
d(x)=d_{\rm after}+d_{\rm offset,j}+x\,\lambda_j,
\qquad r_o(x)=a_c\exp(d(x)/\sqrt{12}),\quad \lambda_j>0.
$$
九段的 offset 按 $j=0,\ldots,8$ 递增。新径向速度是 $A+\alpha B>0$；保护端的定义也保持此方向。因此编号确为从内到外，最外 cut 位于第 8 段末端。从 cut 向内累计时必须采用 $8,7,\ldots,0$。作者实现的顺序正确。

原共同 cut 的精确定义是：反射整个尾高度及全部高度扰动，以 cut 的均值匹配精确前缀均值。于是上尾的位置为
$$
X(r,\theta)=\bigl(r e^{i\theta}+V_h(r,\theta),\,
H_c+\int_r^c w(\rho)\,d\rho-V_z(r,\theta)\bigr).
$$
其中 $H_c$ 不是 moment 报告的角向完整 cut 高度区间。`db6f-root-common-cut-v2.py` 中的 `background_cut_height` 给此常数的区间；已审闭预算精确保存
$$
z_+=H_{c,+}+B_{\rm old}+V,\qquad z_-=H_{c,-}-V.
$$
本次以这些保存的 **exact Fraction** 和原二进区间端点恢复 $H_{c,\pm}$，没有从 display 小数反推常数。恢复后的 $H_{c,-}-V>0$，故整个上尾的高度为正，后面的高度上界可安全平方为绝对高度界。

这里 $U,V$ 是同一 critical 尾有限部分与其自身 R6 圆领的全域扰动界之最大值。不能换成节点采样、不同尾端点或未反射的高度。作者及独立检查均使用了正确的两项全域上界。

## 3. 连续九段、内层与帽的组合

记九段的真实径向长度和高度增量为
$$
L_j=A_j+\alpha B_j,\qquad J_j=A_{H,j}+\alpha B_{H,j}.
$$
由于 $B_j^-$ 非负、$\alpha_->0$，已有区间给
$$
\ell_j=A_j^-+\alpha_-B_j^-\le L_j,
\qquad h_j=A_{H,j}^++\alpha_+B_{H,j}^+\ge J_j.
$$
少数 $A_j^-$ 是极小负数；非负真实积分允许有这种向外区间下端点。脚本原样保留这些数，未偷偷夹零。全部 $\ell_j$ 仍为正。严格比较使用任意精度 Fraction，未因分母很大而截断。

第 $j$ 段任一点满足
$$
r\le c-\sum_{k>j}\ell_k,
\qquad
\int_r^c w\le\sum_{k\ge j}h_k.
$$
径向界只减去完整外段的长度下界；高度界计入当前段的全部高度。因而
$$
|X|^2\le
\left(c-\sum_{k>j}\ell_k+U\right)^2+
\left(H_{c,+}+\sum_{k\ge j}h_k+V\right)^2.
$$
这是整段连续位置界，不要求 source 分段与有限扰动 $V$ 的五次多项式网格对齐。背景段覆盖每个实际半径，$U,V$ 对所有半径及角度都有效。对九段分别求和不会遗漏跨 source 端点的扰动区间。

在 cell 0 内侧，使用既有全背景结论 $0\le w\le1/49$，包括有限内层和受保护的无限深背景。令
$$
\overline r_1=c-\sum_j\ell_j,\qquad
B_{\rm new}=\sum_jh_j+\frac{\overline r_1-7/50}{49}.
$$
用 cuff **下界** $7/50$ 扩大剩余径向宽度，因此是合法高度上界；内尾的水平半径仍不超过 $\overline r_1+U$。R6 只改变已纳入 $U,V$ 的扰动，背景没有改变。

在两帽上，扰动的两 jet 已在 cuff 消失，帽高度来自同一 $H_c$ 和完整背景高度。上帽三个支撑互不相交的原固定凸起总高度至多 $1/2000$，下帽为平帽。用 cuff **上界** $3/20$ 得
$$
|X_{\rm cap}|^2\le(3/20)^2+
(H_{c,+}+B_{\rm new}+1/2000)^2.
$$
上下 cuff 的不同单侧界用在正确方向；没有把帽重新平移或更改凸起。

所有九段、内尾/圆领及两帽的平方界都严格小于原前缀的 $R_P^2$。最大外段为 $j=7$。作为独立的较松交叉检查，即使内尾和帽继续使用旧 $B_{\rm old}$，其球界也已严格小于 $R_P$；因此新球界不存在依赖一个未经支付的更紧内层积分的风险。

## 4. 同一完整族与精确比例

原完整连续前缀证书给
$$
R_P=\frac{2131902881202937}{1125899906842624}.
$$
下前缀和下尾是关于 $z=0$ 的完整镜像，欧氏范数不变；固定两帽已分别覆盖。全部活动相位的像集只是绕原 $z$ 轴旋转，材料角换元不改变像集，固定帽不动。因此原点球对整个相位族有效：
$$
|F_t^{12}(p)|\le R_P,
\qquad
D_{12}\le2R_P=\frac{2131902881202937}{562949953421312}.
$$
README 的 $D$ 是初始完整曲面的实际直径。上述全时结论比仅初始时刻所需更强，但并不宣称该上界等于实际直径或最小包围球。

原 R21 的绝对支撑、曲率、R10 reach、握持位移见证和固定帽直径下界均是同一图的既有证书。新组合只替换分母的合法上界。独立 Fraction 重构确认
$$
\frac{\operatorname{reach}}{D_{12}}
\ge\frac{316912650057057350374175801344}
{10156379431358714998583735712015}
>0.03120330942723168,
$$
$$
\frac{\delta_{\rm hold}}{D_{12}}
\ge\frac{1800459358092517}{34110446099246992}
>0.05278322519892998.
$$
作者稿的 $B_{\rm new}$、三个平方上界及固定帽比例的单侧十进陈述也已全部以精确分数逐项核验。说明性平方根和近似小数没有用于正式比较。

## 5. 实际重放与独立重构

作者脚本的独立输出为 `notes/2026-11-09-db6f-audit-m12-segment-ball-replay.json`。实际自然 exit 0，0.054 秒；输出与作者的 54,651 字节报告逐字节相同，SHA 同为 `f08875b2…483c`。完整命令、实际退出码、启动与结束源哈希及日志哈希保存在同 stem 的 `.execution.json` 和 `.log`。

另一个独立程序 `scripts/db6f-audit-m12-segment-ball-check.py` 不导入作者计算器。它用按索引的完整后缀求和重建每段，逐项比较九段及最终标量，并检查显示端点的包含性。实际运行 exit 0，结果为 `notes/2026-11-09-db6f-audit-m12-segment-ball-check.json`：24 项冻结文件绑定、95 项 exact record 比较全部通过。它还直接读取当前 manifest 的真实 cut/cuff、核验有限尾 span 数，并确认作者只导入标准库模块。

在本题目录下，可用新输出文件名重放：

```bash
python scripts/db6f-prefix-m12-segment-ball-budget.py \
  --out notes/2026-11-09-db6f-audit-m12-segment-ball-replay-NEW.json
python scripts/db6f-audit-m12-segment-ball-check.py \
  --out notes/2026-11-09-db6f-audit-m12-segment-ball-check-NEW.json
```

第二个检查器固定绑定本次已关闭的重放文件，新的 `--out` 仅改变检查报告的保存位置。

## 6. 审查范围

PASS 覆盖作者的新组合证明、同一图身份、完整高度规范、镜像及全时性、精确标量计算和实际轻量重放。原连续位置/扰动/积分/曲率证书的解析正确性取已完成独审为前提，本次没有再次跑其行级后端。

本结论没有改变目标 $g$、求解或表示网格、metric 上界、绝对曲率、绝对 reach、非全等矩及固定帽。没有支付 G5 的误差达到求解容差、无限非线性尾存在或最终未参与优化者的全流程重跑；README 仍未完成。未来 M15 若采用相同公式，必须使用它自身完整前缀、尾、圆领、cut 高度和绝对几何证书，不能搬用本次 M12 数值。
