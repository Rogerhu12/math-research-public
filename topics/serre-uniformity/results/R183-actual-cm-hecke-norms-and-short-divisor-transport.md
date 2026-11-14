# R183：实际 CM Hecke 范数及保留框架的短除子主函数

日期：2026-11-13。**状态：本文的两项主函数范数和两条短组合已证明并完成实际计算；完整全局高度仍未得。**

在 R179 的实际相离 Abel 图上，本文计算两个 CM 类的 $\rho_T$ 在第一形式除子上的准确范数，并构造 R178 所需的实际短组合函数 $F_\Sigma$。所有完整点理想、每步主截面及最后的理想同构均保存；没有用点的线性关系代替纤维上的函数。

## 1. 固定模型、真正的目标展开与范数

沿用 R102/R110 的 $X=X_{\rm ns}^+(41)$、$g=54$、$\deg\mathcal L=126$ 及原 $73,199,325$ 维截面基。计算环为
$$R_2=(\mathbf Z/47^4)[i]/(i^2+1),\qquad q=47^4=4879681.$$
记 $K_0=\operatorname{div}_{\mathcal L}(f_0)$，$m=\#J(\mathbf F_{47})$。对 $P=u=P_{-12}$ 或 $c=P_{-7}$，设 $C_P=P-b$、$Y=mC_P$。第一变量使用原 R141 的 family0：
$$A_0(Y)=\sum_{j=1}^{54}P_j(t_j)-\sum_{j=1}^{54}P_j(0),\quad t_j\in47R_2.$$

从 R170 已发布的三个完整真实二同源分支，按原项链排列准确截取这54个源点上全部162个目标点的三阶系数。每个分支逐个解码，保留全部四项系数、原完整目标 SHA、源展开 SHA 及原 Abel 基 SHA。该步骤只是限制已验证的实际展开，没有重新计算扭点或猜测对应分支。完整截取证书为 `p41_t2_first_family_cubic47_checkpoint.json.gz`，502528字节，SHA
`b8d7f38088e19f2e0a58f1a8f2907cdce6c8f8bddaf193137a378d2c8c1c5346`。

对在这些盘上为单位的实际函数 $f$，范数记为
$$N_P(f)=f[A_0(Y)]=\prod_{j=1}^{54}\frac{f(P_j(t_j))}{f(P_j(0))}.$$
由 Frobenius 下降，所得值在 $\mathbf Z/47^4$ 中；又因 $t_j\in47R_2$，它模47等于一。三阶展开已足够，因为全部更高项含 $t_j^4$。对同次数的截面比 $n/s$，直接取两个原始截面范数之比，次数框架自动相消。

实际函数值用原固定截面基求出；程序还核对源常数项与原模型相同、三次基常数项与原 $V_3$ 相同，以及每个截面满足原 $A_3$ 的 Frobenius 等式。全部162个 Hecke 目标的 $f_0$ 常数也都为单位，为后续整盘计算提供同一规范。

## 2. 两个实际 $\rho_T$ 的范数

R179 构造了实际函数
$$\operatorname{div}\rho_{T,P}=T_2A_S(Y)-A_S(T_2Y).$$
这里 $S$ 是 R179 的新54点图，满足 $S\cap S_0=T_2S\cap S_0=\varnothing$。将 R179 保存的325维分子、分母分别在第一族54个移动点及固定点取值。两类的每个分子和分母常数值都为单位，故本步无需任何非单位除法或局部消去。

| $P$ | $N_P(\rho_{T,P})\pmod q$ | $\log N_P(\rho_{T,P})\pmod q$ |
|---|---:|---:|
| $P_{-12}$ | 2361422 | 2361421 |
| $P_{-7}$ | 218692 | 218691 |

对数按 $\log(1+z)=z-z^2/2+z^3/3\pmod q$ 计算。证书保存全部54个固定和移动取值、两截面范数及最终比值，并核对对数的减法等式。输出 `p41_t2_transport_norms47_checkpoint.json.gz` 为5362字节，SHA
`719ff916ec8ed30940d8000e13b083ccba8b14a624ece741f34490a42f177205`。

## 3. 完整除子代表与短组合的精确框架因子

令 $h_S=v_S/f_0$；原 family1 的基截面类似给 $h_1=v_1/f_0$。完整 Makdisi 点的度零除子代表为
$$\widetilde A_S(Y)=A_S(Y)+\operatorname{div}h_S,$$
$$\widetilde A_1(Z)=A_1(Z)+\operatorname{div}h_1.$$
R179 已给出下列四个完整点理想及 Frobenius：
$$\widetilde A_S(T_2Y),\quad\widetilde A_S(Y),\quad
\widetilde A_1(3mD_b),\quad\widetilde A_1(3mD_P).$$
R178 的真实整数除子关系和 R179 的清挠检查给
$$81T_2Y+12Y+3mD_b=3mD_P.$$
程序还逐项核对这四个保存的实际形式对数满足同一等式；这里的点已由 R179 的完整指数构造确定，并非仅有抽象对数。

将 $S$ 与原 family1 的固定点从820点评价池删去。两集合交叠8点，恰剩720点；它们在 Frobenius 下稳定，且仍包含全部第一族54点。原基截面 $v_S,v_1$ 在各自54点以外的评价点上均为单位，这由实际值再次直接核对。因此所有输入的完整有效除子在剩余池上无零行。

限制后的 $V_2,V_3$ 分别以199阶和325阶单位子式重新归一，保存两个变基摘要并验证 Frobenius。720大于群运算所需的最大截面次数 $5\deg\mathcal L=630$；所以剩余点上的全部截面等式仍忠实。输出中的点及每个主截面都准确变回原 R102/R110 基。

以完整点 $\widetilde A_S(T_2Y)$ 为初始项，用整数向量递推得到 $(81,12,1)$。主计划含6次 double、5次 AddFlip 及1次末尾 flip；另先构造一次负 $T_2Y$，共13次真实点运算。每步保存实际二次或三次主截面。设 $A_R$ 为该步完整点的度零代表，函数递推为
$$F_R=(F_PF_Q\,s/f_0^3)^{-1},\qquad
F_{-P}=(F_P\,s/f_0^2)^{-1}.$$
因 $\operatorname{div}(s/f_0^3)=A_P+A_Q+A_R$，归纳得到末尾函数
$$\operatorname{div}F_{\rm build}=
81\widetilde A_S(T_2Y)+12\widetilde A_S(Y)
+\widetilde A_1(3mD_b)-A_{\rm final}.$$
完整整数向量在每步单独核对，所有截面的系数 SHA、Frobenius、点 SHA、随机状态及范数均写入检查点。

## 4. 末尾完整理想同构与准确 $F_\Sigma$

令 $E_{\rm final},E_Z$ 为末尾点及实际目标点的126次有效除子，$Z=3mD_P$。在720点上选 $s,g\in H^0(2\mathcal L-E_{\rm final})$，其中 $s$ 在这些点上为单位；解
$$\frac gs\,t\in H^0(2\mathcal L),\quad
t\in H^0(2\mathcal L-E_Z).$$
对应73列矩阵有72阶单位子式，核为秩一直和。先准确下降这个核，再取有理单位生成元。对所得 $t$，程序核验
$$\frac ts H^0(2\mathcal L-E_{\rm final})
=H^0(2\mathcal L-E_Z)$$
的完整73阶可逆变换矩阵；全部720个乘法式及矩阵逆均通过。这些乘法等式的次数至多 $4\deg\mathcal L=504<720$，所以是全曲线的真实等式。线丛的剩余次数126超过 $2g-1$，两空间完整生成相应理想；因而
$$g_{\rm full}=t/s,\qquad
\operatorname{div}g_{\rm full}=\widetilde A_1(Z)-A_{\rm final}.$$

由上一节逐项相减，两个 family1 的 $h_1$ 因子准确相消；而两个 $S$ 框架的系数和为 $81+12=93$。因此
$$\boxed{F_\Sigma=\frac{F_{\rm build}}{g_{\rm full}h_S^{93}},}\tag{183.1}$$
$$\boxed{\operatorname{div}F_\Sigma=
81A_S(T_2Y)+12A_S(Y)+A_1(3mD_b)-A_1(3mD_P).}\tag{183.2}$$
这个93次框架因子不可省略。此处 $g_{\rm full}$ 比较的是两个完整点；没有另行除 $h_1$，因为两个输入的该项已经在式中相消。

## 5. 两条短组合的全部范数

群运算选择的每个主截面都在720点上为单位，第一族又包含在这720点中。因此所有短链范数都直接用54点移动值除固定值计算。对次数 $d$ 的主截面，先准确除 $N_P(f_0)^d$；负基点函数按其保存二次截面的倒数计算。最后按式(183.1)合成。

| $P$ | $N_P(F_{\rm build})$ | $N_P(g_{\rm full})$ | $N_P(h_S)$ | $N_P(F_\Sigma)$ | $\log N_P(F_\Sigma)$ |
|---|---:|---:|---:|---:|---:|
| $P_{-12}$ | 4687969 | 2748279 | 2544581 | 3375353 | 3375352 |
| $P_{-7}$ | 4460536 | 3478142 | 2775116 | 1656751 | 1656750 |

全部数值模 $q=4879681$。每条短组合证书保存全部点、函数、整数向量、各步范数、最后理想同构和框架校正。完整输出为：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `p41_cm12_formal_combination47_checkpoint.json.gz` | 564531 | `a88af4cb86f28347d9243fc30775edf6e32edddb049a5a73b7c16b87db5708e2` |
| `p41_cm7_formal_combination47_checkpoint.json.gz` | 564912 | `ba60ed271ae5e1feaffec4e1ea58f604e8bb958c9315dbf4dc84ba545ffdd36c` |

同源驱动 `p41_formal_combination47.py` 为19422字节，SHA
`edb997ae4bf92caef21301f6c8af64a52d93eb7824bbf49f8fb49f92e2eb1e3a`。
两次完整运行分别约63秒，峰值107和112 MiB；这些资源数据只说明恢复成本，不参与数学结论。

## 6. 后续 Hecke 范数的整盘接口

以上已经完成 R178 的 $\rho_T$ 和 $F_\Sigma$ 两项。剩余长链要在 $T_2A_0(Y)$ 上计算 $f_{C,S}$，不能因最终支撑相离就把中间非单位截面直接取逆。

R159 的单位制备也可准确处理移动值。若实际整盘参数为 $z$，截面 $s(z)=W(z)U(z)$ 的剩余阶为 $e$，其中 $W$ 首一且除最高项外都被47整除，取 $a\in47R_2$。则 $W(z+a)$ 仍是同次数的首一特征多项式；所以对平移后的截面应用同一唯一单位制备，得到的单位常数恰为 $U(a)$。为模 $47^4$ 计算它，只须把原系数保留至 $4e+3$：平移后第 $j\le4e$ 项是
$$\sum_{k=j}^{j+3}\binom kj s_k a^{k-j}\pmod{47^4}.$$
更高项包含 $a^4$，因而消失。制备只对单位系数取逆；还可直接核验新首一因子等于原因子的准确平移。$e=0$ 时只需原来的三阶展开。

这给非单位盘的准确计算接口，不是说长链范数已经完成。后续还须以真实完整点理想核对初始、当前及末尾的首一因子，并把 $h=f_b/f_0$、$v_S/f_0$ 与末尾主函数一起消去。本文两个范数表及式(183.1)都不单独构成全局高度；54个高度差及全部 QC 盘仍在进行。

## 7. CM12 完整 Hecke 范数：全部非单位整盘已消去

CM12 的304位454步完整链已取得；完整点 SHA 为
`6dd6e2ae8aefcff12979a1b6c78b2259d28c9c41bbc3f2790a6c5e8d9a7806bb`。
原基主截面及模47零类检查保存在 `p41_cm12_slp47_saved.json.gz`，SHA
`5e505ebeb3b12f2f443766177c335a9ffc91e23206d9074e7dbe27f67f45f9c2`。
其末尾到新 S 图的实际完整73维理想同构给
$$g_S=(n/s)/(v_S/f_0),\qquad f_{C,S}=F_{\rm chain}/(g_Sh^m),\quad h=f_b/f_0,$$
$$\operatorname{div}f_{C,S}=mC_u-A_S(mC_u).$$

把全部454个三次截面、负点二次截面、初始 h、末尾两个二次截面及 vS 都在162个目标常数处检查，恰有12个非单位盘，最高剩余交数2。三个支点 b、u、c 与162个目标支撑均不相交：这一点比较的是原模型中完整73维项目坐标，不能用 j 相等或不同单独代替。S 与目标支撑相离由 R179 保证。

每个实际非单位盘使用全局二次关系的71阶单位法向子式，再加入 f0 规范和一个真实参数，得到73阶单位 Jacobian。由隐函数递推构造所需7或11阶展开；全部2701个全局二次关系逐阶成立，且把参数写回原源点参数后三个独立 GP 系数逐项相同。旧已算的18盘证书包含这12盘，故完整链无需重跑任何盘。

在每个盘，以 W_init、W_neg、W_current、W_target 表示四个完整有效除子的首一因子。程序从其完整199乘73理想直接选择达到最小局部阶的生成元，并用 R159 制备；所得因子与函数链逐步核对。准确等式是
$$W_{\rm init}=W_h,\qquad W_{q_-}=W_{\rm init}W_{\rm neg},$$
$$W_{\rm section}=W_{\rm left}W_{\rm right}W_{\rm next},$$
$$W_nW_{\rm current}=W_sW_{\rm target},\qquad W_{\rm target}=W_{v_S}.$$
最后一个等式允许 vS 的72次剩余零除子落在 Hecke 目标盘上；没有把完整末尾理想假定为单位。上述等式使 f_C,S 的全部首一因子在整个盘上准确消去，而非仅在一个代入值上试除。

随后用第6节的平移制备分别求每个单位因子的 U(0) 与 U(a)。每次还核新首一多项式恰为 W(z+a)。各盘可有不同的整参数，故中间剥离单位的三分支乘积不必先落在有理系数子环；仅对完成真实函数的全部消去后要求 Frobenius 有理性。最终得到
$$\boxed{f_{C_u,S}[T_2A_0(mC_u)]=4551951\pmod{47^4},}$$
$$\boxed{\log f_{C_u,S}[T_2A_0(mC_u)]=1585263\pmod{47^4}.}$$
完整证书 `p41_cm12_t2_miller_norm47_complete.json.gz` 为52118字节，SHA
`1078c340162d23371a8b56bb87574090b1c85c14d76cb2e8b6c553f6f1fe5c02`。
它保存162个实际最终比值、三个分支范数、全部非单位步骤的首一因子和移动单位值、四个完整理想的局部见证及初末校正。所有计算只取单位逆，非单位除法次数为零。这一范数已完整；CM7 的同项见下一节，共同函数的末尾范数继续计算。

## 恢复与来源

完整路径、源码、字节数及摘要见 `notes/2026-11-13-r183-stable-files.json`。从课题目录依次运行：

```
python -B scripts/p41_t2_first_family47.py --script-dir scripts
python -B scripts/p41_t2_transport_norms47.py --script-dir scripts
python -B scripts/p41_formal_combination47.py --script-dir scripts --class-name x12 --checkpoint /tmp/p41_cm12_formal_combination47_checkpoint.json.gz
python -B scripts/p41_formal_combination47.py --script-dir scripts --class-name x7 --checkpoint /tmp/p41_cm7_formal_combination47_checkpoint.json.gz
```

`--jets` 可显式指定已保存的第一族截取数据；短组合检查点保留随机状态和全部已完步骤，可从任一完整写出边界恢复。

- [R159](R159-integral-weierstrass-cancellation-and-exact-jet-precision.md)：整盘制备的精度与仅单位除法。本文的平移接口直接从其已证明的界推出。
- [R178](R178-actual-common-translation-divisor-and-initial-transport.md)：真实共同 $3D_b$ 及完整双变量函数规范。
- [R179](R179-disjoint-cm-hecke-frames-and-common-formal-endpoints.md)：新 $S$ 图、两个 $\rho_T$、六个共同形式端点和全部输入来源。


## 8. CM7 同一完整 Hecke 范数及最终两类对照

CM7 的完整304位454步链保存在 `p41_cm7_slp47_saved.json.gz`，SHA
`e0c0f13d9b3170d3956e0c9725d34ee300ffb22ce9542b7118e6f86539a0f024`；真实新S端点换框 SHA 为
`fd5232deac4c69e227bf67e2c63dcbf83b9ee6c34ea0f0593425e3701403ec5e`。
同一原基的460个截面检查给14个非单位目标盘，最高剩余阶仍为2。
CM7工作图虽删除原评价池第254行，所有实际主截面和点已转回原始基，第一族及其Hecke目标的评价没有混用两套基。

为包含完整CM7链，新补6个实际目标盘：`T2_2_P6`、`T2_2_P15`、`T2_2_P31`、`T2_2_P244`、`T2_2_P34`、`T2_2_P332`，都展开到11阶。总24盘文件 `p41_t2_quadratic_discs47_24_fixed.json.gz` 为174807字节，SHA
`a9cd7bef7f11786ed171c2dc78daa2569eff3f719c9c821141ba90724da6f6a6`。
既有18盘固定文件仍保留原SHA，CM12最终范数继续绑定原输入。所有新盘同样核单位73维Jacobian、全部2701个真实二次关系及独立三阶锚点。

逐步应用第7节完全相同的完整理想因子递推，检查初始、负点、全部454步、实际终点和\(v_S/f_0\)的首一因子，得到

\[
\boxed{f_{C_7,S}[T_2A_0(mC_7)]=945641,
\qquad\log_{47}=2692959\pmod{47^4}.}
\]

证书 `p41_cm7_t2_miller_norm47_complete.json.gz` 为52243字节，SHA
`d7591667ea309c0904792b4f85c44222e7bd668fb24c38aabf86a6e8926605f1`。
它同样保存全部162个最终比值、分支范数和局部整盘消去见证，非单位除法次数为零。两类结果汇总如下：

| 类 | \(f_{C,S}[T_2A_0(mC)]\) | \(\log_{47}\) | 完整链 | 非单位盘 / 最高阶 |
|---|---:|---:|---:|---:|
| \(C_{12}\) | 4551951 | 1585263 | 304位454步 | 12 / 2 |
| \(C_7\) | 945641 | 2692959 | 304位454步 | 14 / 2 |

恢复时从仓库将对应固定盘文件复制到脚本的 `--discs` 参数即可；不要覆盖证书所绑定的18盘和24盘两份输入。R184保存两类完整链、两端点换框、全部碰撞范数及形式双扩张值。剩余共同\(f_D\)范数须实际完成后才组装两个\(F_2\)高度，且两个高度仍只占R144的54条校准行中的两条。
