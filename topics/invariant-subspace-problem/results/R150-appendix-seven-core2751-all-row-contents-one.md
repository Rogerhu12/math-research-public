# R150 附录：2751 原单位块列归一后的全部行内容为一

Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。2026-11-15。

## 同一个原七方向系统

承接[完整列内容及唯一结构块](R150-appendix-seven-core2751-column-contents-and-single-structural-block.md)，固定原系统 $UX=E$、2751个未知坐标、七个右端及1567步完整逆代图。列内容为 $h_j>0$，$U_c=U\operatorname{diag}(h_j^{-1})$。本次未作新主元或有理求解，也未改变前序状态。

对每个实际输出行，取**只涉及矩阵系数**的正内容
$$
g_i=\gcd_j |(U_c)_{ij}|.
$$
不是对增广矩阵取内容。因此若将矩阵除以 $g_i$，须同时保留右端 $E_{it}/g_i$，不能无说明地丢掉这些分母。一般第 $t$ 列的最小正公共分母为
$$
d_t=\operatorname{lcm}_i\frac{g_i}{\gcd(g_i,|E_{it}|)}.
$$
置 $R=\operatorname{diag}(g_i)$、$C=\operatorname{diag}(h_j)$，则准确等价为
$$
U_b=R^{-1}UC^{-1},\qquad
U_bW=R^{-1}E\operatorname{diag}(d_t),\qquad
X=C^{-1}W\operatorname{diag}(d_t^{-1}).
$$
还原 $X$ 后才接原1567步逆代。

## 全部原系数的实际结果

run43679903558 中 step seven-row-content-profile 读取同一个80674893B原状态和109635B已核列内容，核对两份文件的完整SHA256及binding，并逐项检查全部424921项的列除法、行除法。实际结果为
$$
\boxed{g_i=1\quad(1\le i\le2751),\qquad d_t=1\quad(1\le t\le7).}
$$
没有达到分母位数截断门槛；所有七个分母均为准确值。因此仅剩原已付列缩放，右端不再产生新分母，但矩阵高度也不再下降。最大系数3691bit、全部非零系数位数和465478525、右端最大3677bit。

这关闭本系统“继续按行整数内容降低高度”的具体分支。它不排一般有理换基、低填充消元或可恢复精确求解；没有证明七方向的有理存在性。

## 代码、实际回执和接续身份

源码[行内容与真实右端分母](../notes/2026-11-15-r150-seven-exact-row-content-profile-789f.py)，8712B，SHA256 a638f5fc7b19814b7cf1edc079c8ff644e668279726fc93837ab7e96e595fa7f。execution source 7b120d4d075540c059d9d8255efaa1728795f361，数学自选30秒/2048MiB，外部65秒；实际数学2.5603509129996382秒，原生环境只读检查1.009757919000549秒，总墙钟3.671990684000775秒，exit0。

[小回执](../notes/r150-infinity-remote-session-789f/43679903558-seven-row-content-profile.json)保全部参数、规则核对和身份。完整临时回执2771B，SHA256 07a7bf351d97d2131311081009e6c457d649df5dba63e78d3b812424d3ac8abe。缩放文件 seven-exact-row-column-scale-factors.json.gz 仅留 job 临时目录，118120B，SHA256 9ff2019837a8d86d8c1d912821802971150bb9c8fde844dae182624d43586ec4，binding 6bf64a842cf35cb7ee587a9e6c86c4f9fade57ae88c206caef62bf9f4c83f6c5。

实际 python-flint 0.9.0 使用 FLINT 3.6.0；该 job 未检出系统 FLINT pkg-config 条目及标准位置开发头，且没有 rg。后续原生代码须先查实际 wheel 库和编译器，再按真实开发环境编译，不把系统开发包或匹配头文件当作已经存在。此环境事实不影响上述全部整数身份。

当前真核仍29条，同选有理秩4318至4325；剩余七方向仍须求解并付完整原4367输出整数残差。

