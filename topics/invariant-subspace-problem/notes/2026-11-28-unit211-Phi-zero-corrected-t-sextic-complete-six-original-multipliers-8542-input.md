# 新输入：正确 Phi 六次 t 式的完整六原乘子、全斜率零延拓与真实首项支持

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：未执行。** 本次不重算已成两列结果作为证明目标。新的唯一主目标是补回真实第三 $N_1$ 乘子、合成完整六原来源，并仅据最终实际分母判断原 $C_6$ 是否覆盖整个 $\Delta=0$。若此目标完成，再首次精确因式其真实 $t^6$ 头。没有预报分母可消、整个首项单位或原图排空。

源：[2026-11-28-unit211-Phi-zero-corrected-t-sextic-complete-six-original-multipliers-8542.py](2026-11-28-unit211-Phi-zero-corrected-t-sextic-complete-six-original-multipliers-8542.py)。
Git blob fb4163bda5bb1d9d7d6c0ac778ccc899469d2c8f，16367 字节，SHA256
00f6e0b8b22b67031c37e5f983bdef4aa08b639cfb0b8d6ef3fca1bafbae4cf3。

自含、零依赖；最初绝对 120 秒 / 1 GiB，外层 135 秒。无旧日志或系数载荷输入；源末只读取自身 SHA，不写参数或矩阵缓存。

## 1. 新目标与明确不重放的边界

[中心 t 完整 NS/PS](../results/R150-appendix-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-and-sextic.md)的唯一首次 run 46149159181 已在 $\Delta\ne0$ 上支付首一二次、十行二列和非零
$$
C_6(u,Q,t),\qquad (\deg_u,\deg_Q,\deg_t)=(36,23,6),\quad \deg C_6=44.
$$
其规范 SHA 为
5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1。
这仍只是斜率补图结论。标量本身的分母小，不能代替完整原六式乘子的正则性。

新源只再生这些必要参数：

- 同一自由原 Gram、三个正确均值的系数和已付头逆；
- $r_N,r_{NS},r_{PS}$ 三个余式及它们的普通原三均值乘子定义；
- 已成两列的两个终端乘子，按实际两个分子 SHA 钉死。

三个余式的已成分子 profile 全部逐一匹配。普通原降次仍用于定义必要系数与迹，但源明确省去之前两个独立 raw NS/PS 返回检查及其阶段，不将它们再次登记。未执行旧 CH、斜率因式、$q_\omega$、两条 $\omega$ 倍、未中心六行、中心十行或旧二列 cofactor 证明段。

新的实际返回是第三 $N_1$ 乘子的全部三坐标、完整六原式合成身份，以及六个最终乘子全部实际分母的旧权分类。

## 2. 原系数环与斜率只作计算分母

系数环 $\mathcal A$ 仍为当前正确 Phi、distinct singleton、物理 $D\ne0$ 范围中的旧已付权环，使用
$$
u,\ Q,\ \delta=1-Q,\ s=u-1,\ K_w=Q+4s,\ L=Q-2s(u-2),\
M_n=2uL-L^2-u^2Q,\ 2\ell-1,\quad \ell=L/Q.
\tag{1}
$$
整 ell-half 终证已支付 $2\ell-1$。本次不使用旧错误 compact 的任何来源。

$\Delta$ 非零是既成有理函数事实，所以允许在 QQ 权函数域里形成下面的新乘子。但它的两个未付零曲线不因此被删除。只有最终分母确实只含 (1) 时，才返回 $\mathcal A$；若仍有未付分母则准确保留全 $\Delta=0$，不宣称全图结论。

## 3. 原三行与真正的新第三乘子

记 $F=(\mathcal R,E_{Be},E_{Bo})$、$e=(1,f,V)^t$。必要定义是
$$
n=r_Ne=N_1-\eta F,\quad
n=n_0+n_ff+n_VV,\quad
n_f=a_ft+b_f,\ n_V=a_Vt+b_V,
$$
$$
r_{NS}e=NS-\tau_{NS}F,\qquad
r_{PS}e=PS-\tau_{PS}F,\qquad
\Delta=a_fb_V-b_fa_V.
\tag{2}
$$
三行的 $t$ 次数分别为 $(2,1,1),(3,2,2),(3,2,2)$，所有原系数只含旧权分母。

在旧中心坐标 $\omega=a_ff+a_VV+At+B$ 中，NS、PS 的 $\omega$ 一次系数与中心平移无关，准确为
$$
b_{NS}=\frac{n_Vr_{NS,f}-n_fr_{NS,V}}{\Delta},\qquad
b_{PS}=\frac{n_Vr_{PS,f}-n_fr_{PS,V}}{\Delta}.
\tag{3}
$$
令 $\mu_{NS},\mu_{PS}$ 为已成两个多项式终端乘子。它们由 $(b_{PS},-b_{NS})$ 的实际纯权分母 LCM 定义；前次完整返回已证共同内容为常数 1，本次不重做这项 gcd。两个分子规范 SHA 固定为
17143d55d1cf0a3fe3680fb6965cda1f1eaa64087dbb40137ddf28a43dd8cedd
和
729506952659f75ea64caeabe64eed3db7f4438ef4d66109991db9669b05bd4e。

原 $(1,f,V)$ 到 $(1,\omega,n)$ 的仿射变换行列式是 $\Delta$。由其逆，原 NS、PS 对 $n$ 的两个系数为
$$
c_{NS}=\frac{-a_Vr_{NS,f}+a_fr_{NS,V}}{\Delta},\qquad
c_{PS}=\frac{-a_Vr_{PS,f}+a_fr_{PS,V}}{\Delta}.
$$
本次首次定义
$$
\kappa=\mu_{NS}c_{NS}+\mu_{PS}c_{PS}
\tag{4}
$$
并完整返回三个原坐标
$$
-\kappa r_N+\mu_{NS}r_{NS}+\mu_{PS}r_{PS}
=(C_{\rm raw},0,0).
\tag{5}
$$
这里的 $-\kappa$ 是需要真正支付的新第三乘子；不从已成两行消元猜测它的分母。

(5) 的标量分子、分母按既成实际 SHA
40588df48a5227d32d88a916170e9e0853acbefec5320b6f155299de1113b0b5、
e6ad630c7a116018ce1b4dcdd95145dc3b38ba861670c4774063194900672c59
核对定义身份。实际新证明来自完整三坐标及下一节的全原合成。

## 4. 完整六原来源与最终正则性

按原六式顺序
$$
F_0,F_1,F_2,N_1,NS,PS
$$
定义六个新终端乘子
$$
\Omega_{\rm mean}=\kappa\eta-\mu_{NS}\tau_{NS}-\mu_{PS}\tau_{PS},
\qquad
(\Omega_N,\Omega_{NS},\Omega_{PS})
=(-\kappa,\mu_{NS},\mu_{PS}).
\tag{6}
$$
源实际展开并返回
$$
\sum_{i=0}^5\Omega_i\,{\rm Original}_i=C_{\rm raw}
\tag{7}
$$
作为普通 $(t,f,V)$ 多项式恒等式。原 $N_4$、中心 $P_2$ 和真 dual 乘法全部保留。没有把某个非自由三列模当结合代数，也没有只检查数值点或一个函数域余式。

然后逐个取 **(6) 最终约分后** 的实际分母。每个分母必须是纯权多项式；只按旧支持 (1) 做精确剥除，保留因子乘回。如果任何剩余分母非恒定，就只记录 (7) 的有理身份和未付分母，完整保留斜率零曲线，不作全图或首项有限性结论。

若七个分母（六乘子及标量）全为旧单位，则 (7) 已在 $\mathcal A[t,f,V]$ 中成立。只清 $C_{\rm raw}$ 的实际旧分母、剥其旧付分子支持，并将同一因子运输到全部六乘子；再次完整返回
$$
\sum_{i=0}^5\widetilde\Omega_i\,{\rm Original}_i=C_6,
\qquad\widetilde\Omega_i\in\mathcal A[t,f,V].
\tag{8}
$$
(8) 的全部六分母再按 (1) 核回。如此才支付整个 $H_6=0$ 和 $H_8=0$，包括两者交点。证明是普通局部化多项式环内的身份，不从补图集合的稠密性单独推理想包含。

## 5. 条件完成后的真正新首项目标

只有 (8) 真返回后，才首次因式原 $t^6$ 头。旧实际头总次数 38，次数 $(36,19)$，434 项，SHA
89cadc1ec0de4d55df49a64ded467843259e929b15dd7dc88f973ccb80e6dd4b；
此前只保存 profile，未作此项 QQ 因式目标。

新源只剥头的旧已付支持 (1)，然后完整 QQ 因式和乘回。全部剩余因子零面保留；不把 QQ 不可约性称作单位性或绝对不可约性。

若该真实头的剩余支持记为 $H_t$，则在 $H_t\ne0$ 上 (8) 给首一 $t$ 六次，而已刊真三均值商在 $\mathcal A[t]$ 上由 $1,f,V$ 生成。因此未反演几何 $D$ 的必要 $I_6$ 商可由
$$
t^j(1,f,V),\qquad 0\le j\le5
$$
共十八个元素生成，不要求自由。这一推论只在本次全原延拓实际完成后使用。旧 $\Delta\ne0$ 补图仍可使用更小的十二生成；两者范围不混淆。

物理 $D$ 局部化不能自动保留基环有限模性质；独立 $U_0$ 尺度也未计入。没有任何全 Phi 排空或纯权有限点断言。若超时、资源错误或目标未返回，照实际最后阶段保留，不增加预算或重启旧目标。
