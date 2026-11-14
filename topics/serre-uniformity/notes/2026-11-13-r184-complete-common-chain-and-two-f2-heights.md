# R184 增补：完整共同平移链与两个真实 F2 高度差

日期：2026-11-13；qc_global。
**状态：已证明。完成范围为同一实际模型、同一 Hecke 相容对数、模 $47^4$ 的完整共同主函数及两个指定 $F_2$ 高度差。**
这完成 R184 原文与 CM7 增补中尚缺的共同 $f_D$ 项，不声称其余52条校准行或全部 QC 共同根已经完成。

## 1. 固定对象及完整369节点

记 $q=47^4=4879681$、$b=P_{-3}$、$u=P_{-12}$、$c=P_{-7}$，
$$F_2=27T_2+4,\quad C_P=P-b,$$
$$D_b=162u+8b-27Q_2+4K_{g_1},\qquad D_P=F_2C_P+D_b.$$
这些是 R148/R178 的实际整数除子，不只是在 $J\otimes\mathbb Q$ 中的等式。
所有函数和范数仍使用原 R102/R110/R112 模型、R141 双 Abel 族、R141 的 Hecke 修正及 R178 的 $g_1$ 典范规范。

R178 的24步短组合已给实际初始代表 $A_{\rm init}$ 及函数
$$\operatorname{div}h_D=A_{\rm init}-3D_b,$$
$$h_D=R_{g_1}^{,2}(f_b/f_0)^{324}/F_{\rm build}
=R_{f_0}^{,2}(g_1/f_0)^{-12}(f_b/f_0)^{324}/F_{\rm build}.$$
这里 $(g_1/f_0)^{-12}$ 没有删除。

固定 R121 的304位整数
$$m=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072.$$
有 $m\equiv9\pmod{47}$、$m\equiv459340\pmod q$。
宽5有符号窗口计划共369节点，精确计数为303次double、57次AddFlip、9次flip。
独立整数递推验证最终系数恰为 $m$，包括全部负号、预计算节点和缓存引用。

对每个节点保存实际主截面与
$$\operatorname{div}F_v=e_vA_{\rm init}-A_v.$$
AddFlip 的实际 $s\in H^0(3L)$ 满足
$$\operatorname{div}(s/f_0^3)=A_v+A_w+A_{-(v+w)},$$
故函数递推为
$$F_{-(v+w)}=(F_vF_ws/f_0^3)^{-1}.$$
flip 使用同一式的二次版本 $(F_vs/f_0^2)^{-1}$。
每个节点都保留原 R102/R110 基中的完整系数、Frobenius、真实点哈希及 RNG；没有把点类等式当成主函数。

17节点缓存及所有旧节点保持原字节。
第282节点后的两次进程退出只确认到 exit137，原因不作额外推测。
随后低驻留 finisher 先释放 JSON、只加载余程实际使用的8个缓存点，再构造同一模型；它不改变 DAG、RNG、任何数学运算或既有主函数。
源文件及精确起始282检查点作为 continuation 元数据保留，后续节点也记录该源 SHA。
完整369节点的特殊纤维零类检验核维数为1。

最终完整文件为 `scripts/data/p41_translation_window47_saved.json.gz`，1117830字节，SHA256
~~~
d8c81ce88340383955eb48965ef51b218fca39f65e39d663de4767b27e8fbdbf
~~~
其最终点哈希为
~~~
8add393932e8a0cbda933fa8824b57a0eecc94a8dc15ce64e06a999e1ac3c555
~~~
余程峰值RSS记录为117.71 MiB；原驱动与新 finisher 的来源均未混淆。

## 2. 真正的共同终点函数

R179 已独立给出第二 Abel 族的 $A_1(3mD_b)$，其点哈希为
~~~
4e625d66b78c5c547cfe0800924abc9ec47902c3b83e81007006bd9f58715ff9
~~~
现已用完整73维理想构造并核验单位同构；一维运输核的秩为72，完整同构矩阵的行列式为47进单位。
实际得到
$$g_D=\frac{s_{\rm new}/f_0^2}{s_{\rm old}/f_0^2}\frac{f_0}{v_1},\qquad
\operatorname{div}g_D=A_1(3mD_b)-A_{\rm old}.$$
所以
$$\boxed{f_D=F_{369}/(g_Dh_D^m),\qquad
\operatorname{div}f_D=3mD_b-A_1(3mD_b).}$$
这保留了真实 $v_1/f_0$ 和初始 $h_D$，并非只验证最终对数相同。

在两个第一 Abel 族 $A_0(mC_u)$、$A_0(mC_c)$ 上，369个主截面、初始短链、负点和终点函数的全部评价均为单位。
逐项采用实际移动54点除以其固定54点；固定的其余72点准确相消。
完整54方向三阶对数系数与直接点值乘积逐项吻合，最终 Frobenius 下降为 $\mathbb Q_{47}$。
得到

| 第一变量点 | $f_D(A_0(mC_P))$ | $\log_{47}f_D(A_0(mC_P))$ |
|---|---:|---:|
| $P=u$ | 2806230 | 773949 |
| $P=c$ | 2764729 | 4087919 |

两个初始 $h_D$ 范数仍分别是229643和1358348，与 R178 完全一致。
这里所有逆均为单位逆，没有除47造成的精度损失。

共同端点证书5639字节，SHA256 `a4cca8d8964f4667d24f5abce5c03d34f19515127a3cd8e13ef3483ca20c7b77`。
完整范数与54方向系数证书51199字节，SHA256 `2e08ea16403d3554a2562256d9bacf5b3e7fe36518fa70cec3a95643e02268ff`。

## 3. 完整第二变量运输

R184 两个 CM 主函数 $f_{C0}$、$f_{CS}$，以及 R179/R183 的真实 $\rho_T$、短组合 $F_\Sigma$，给
$$g_P=(\operatorname{Norm}_{T_2}f_{CS}\,\rho_T)^{81}\,f_{CS}^{12}\,f_D\,F_\Sigma,$$
$$\boxed{\operatorname{div}g_P=3mD_P-A_1(3mD_P).}$$
式中81、12分别是 $3\cdot27$ 和 $3\cdot4$；共同 $D_b$ 的三倍已包含在 $f_D$ 中。
新 $S$ 框架的全部 $v_S/f_0$，以及 $D_b$ 与最终第二族的相同基截面，都按 R183 的真实函数式相消，未假定某个 Norm 线丛平凡。

以下列出全部**对数**输入，均模 $q$：

| 项 | $P=u$ | $P=c$ |
|---|---:|---:|
| $\log f_{C0}[D_P]_j$ | 3497834 | 793971 |
| $\log\operatorname{Norm}_{T_2}f_{CS}(A_0)$ | 1585263 | 2692959 |
| $\log\rho_T(A_0)$ | 2361421 | 218691 |
| $\log f_{CS}(A_0)$ | 4870563 | 4360942 |
| $\log f_D(A_0)$ | 773949 | 4087919 |
| $\log F_\Sigma(A_0)$ | 3375352 | 1656750 |

因此直接乘积与独立对数求和同时给
$$g_u(A_0(mC_u))=2716037,\quad \log g_u=1662343,$$
$$g_c(A_0(mC_c))=1774956,\quad \log g_c=1138763.$$
R183 的 $T_2$ 范数使用18盘及24盘的各自固定证书；非单位中间因子已在整盘中准确消去，未把三阶值直接除47。
R184 的第一项按同一真实 $j$ 参数包含全部 tame 首项，故碰撞处没有漏掉单位或交换符号。

## 4. 两个完整高度差

R184 同一形式框架中的值为
$$\Lambda(A_0(mC_u),A_1(3mD_u))=4082232,$$
$$\Lambda(A_0(mC_c),A_1(3mD_c))=207646.$$
按 R175/R178 的双变量主函数运输，
$$3m^2\lambda(e_N(P))=
\Lambda(A_0(mC_P),A_1(3mD_P))
+3m\log f_{C0}[D_P]_j+\log g_P(A_0(mC_P)).$$
其中 $3m^2\equiv2126523\pmod q$ 是单位，所以这一步保留全部四位精度。
实际解得
$$\boxed{\lambda(e_N(u))=4388343,\qquad\lambda(e_N(c))=4641109.}$$

必须使用 R151 已确认的 $K_{g_1}$ 规范截面坐标
$$s_u=698837,\quad\log s_u=152280,\qquad
s_c=3999200,\quad\log s_c=170469.$$
未使用旧 $K_f$ 坐标。
故 R148 的刚性化 $L_b$ 截面给
$$\boxed{\lambda(\sigma_{L_b}(u))=4540623,\qquad
\lambda(\sigma_{L_b}(c))=4811578.}$$

最后，R144/R148 的原规范 QC 线丛是 $L_b^{\otimes800}$，其中 $800=2\cdot20^2$。
得到两个实际从 $b$ 起的高度差
$$\boxed{\lambda_{F_2}(u)-\lambda_{F_2}(b)=2015736\pmod{47^4},}$$
$$\boxed{\lambda_{F_2}(c)-\lambda_{F_2}(b)=4073772\pmod{47^4}.}$$
R134 已证明该 $F_2$ 的四个实际坏靶全为零，因此这两条 R144 校准右端不再需要减去未算的41处坏项。
本文仍只完成全54行校准中的两行；没有据此解出全部全局系数，更未排除全部 QC 圆盘。

## 5. 数据、绑定与恢复

两个最终小证书分别为1573和1568字节，SHA256：
~~~
u: a590b0c7ea0d1aa6cfcee0510573686b704c1e0b68ea8b10b28926852183aa65
c: cc893e1afe639d54751807915e0f104b891713ed1691c6e15added1baf30000d
~~~
汇总器 `p41_cm_f2_complete_height47.py` 不重新执行任何长链；它核对所有输入 SHA、共同的实际 Abel 点、完整 CM 主函数、新 $S$ 终点、第二变量形式点、$g_1$ 截面及六个范数的对数，再做上述单位整数运算。
初次汇总时发现两个旧模块分别用 `cm12/cm7` 和 `x12/x7` 作标签；已按它们各自实际字段逐项匹配，未改变任何算术证书。

恢复时先用固定参数和已发布输入，命令如下（路径按仓库实际位置设置）：

```bash
python scripts/p41_translation_window_finish47.py --script-dir scripts --original-driver scripts/p41_translation_window_slp47.py --initial scripts/data/p41_translation_build47_complete.json.gz --precomputation scripts/data/p41_translation_window47_precomputation.json.gz --checkpoint /tmp/p41_translation_window47_rolling.json.gz
python scripts/p41_miller_actual_endpoint47.py --script-dir scripts --class-name common --miller scripts/data/p41_translation_window47_saved.json.gz
python scripts/p41_translation_window_norms47.py --script-dir scripts --build scripts/data/p41_translation_build47_complete.json.gz --miller scripts/data/p41_translation_window47_saved.json.gz --endpoint /tmp/p41_common_original_endpoint47_certificate.json.gz --output /tmp/p41_translation_window_norms47_complete.json.gz
python scripts/p41_cm_f2_complete_height47.py --script-dir scripts --discriminant 12
python scripts/p41_cm_f2_complete_height47.py --script-dir scripts --discriminant 7
```

只有需要重建共同后缀时才用第一行；先把固定282输入复制成临时 rolling，并保留全部已发布17缓存。完整链已保存时不应重跑。
最后两行默认从 `/tmp` 读取已发布前置文件的同名恢复副本；完整清单同时给出所需目标文件。

后续 $B$–Hecke 高度统一用 $Z_{-4}$ 上的 $j-1728$ 与尖点的 $q_{41}$ 作切向首项规范。
R112 的 $t=B^2$ 满足 $t=-(j-1728)/11664+O((j-1728)^2)$；因此阶 $r$ 的首项换成 $j-1728$ 时必须乘 $(-1/11664)^r$。
这项新全局约定不改变上面两个已按各自 $j$ 参数完成的 $F_2$ 值，也不改变 R151 的54个实际 Abel 联络值。
