# R150：一般等权六生成元的原乘法、余三次、NS/PS 与不同值返回

日期：2026-11-27（Asia/Taipei）；Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明输入。** 在[全域原六生成元](R150-appendix-unit211-equal-weights-global-original-six-generator-module.md)的同一已付参数环中，本页完成18条原乘法身份、其余两个三次组合的完整六列关系、原加权 $N_S/P_S$ 的同点返回，以及原不同值分子的六列返回。没有断言六生成元自由，也没有由这些必要矩阵声称整个参数图排空。

## 1. 原输入及六条规则

原六式依次记为
$$
\mathbf F=(F_0,F_1,F_2,F_3,\widehat N_S,\widehat P_S)^{\mathsf T},
$$
其中四二次原式及规范化与前页完全相同。后二式为独立 affine Gram 源的
$$
\widehat N_S=16F_S/m^3,\qquad
\widehat P_S=16F_P/m^3.
$$
所有原 weighted N/P 身份及 $N_0/P_1$ 的同一个值均保留，未另取根。

以
$$
\mathbf b=(1,x,y,t,y^2,yt)^{\mathsf T}
$$
为六项生成列。前页六条首一规则只逆 $m,m-1,Q,Q-1,J$，$J=2m+Q-2$ 已由整个 $T_0=0$ 支排除支付。六规则各自是四个原二次式的显式组合。

## 2. 18条真实原乘法

对每个 $a\in\{x,y,t\}$ 与 $b_i$，按前页总次数及 $x>t>y$ 的次序作首项下降，并同步累计六原式组合，得到
$$
a\,\mathbf b=M_a\mathbf b+E_a\mathbf F.
\tag{1}
$$
$M_a$ 是六阶参数有理矩阵，$E_a$ 是六阶原变量多项式矩阵，其参数分母只含已付单位。源对全部18个身份直接做完整原多项式乘回，确认为 (1)，不是仅核某种数值矩阵乘法。实际完成用时6.782秒。

这里 $M_a$ 只是选择确定返回次序所得的表示；(1) 不主张这些矩阵在自由六维空间上必须相互交换。若后续使用交换子，必须保持
$$
(M_aM_b-M_bM_a)\mathbf b
=\{aE_b-bE_a+M_bE_a-M_aE_b\}\mathbf F
\tag{2}
$$
的真实原组合，而不能删去右侧或预设六项独立。

## 3. 其余两条三次组合

前页由四二次得到四个 $\sigma_i$，只用 $\sigma_0,\sigma_2$ 的两列单位头构造两条首一三次规则。现在将 $\sigma_1,\sigma_3$ 分别用六规则完整返回：
$$
\sigma_i=q_i^{\rm rem}\mathbf b+\text{原六式组合},
\qquad
q_i^{\rm rem}\mathbf b=C_i\mathbf F,\quad i=1,3.
\tag{3}
$$
两条最终六列行都确实非零。各清已付分母、只剥已付整行因子后，参数双次数 $(m,Q)$ 均为 $(10,10)$。每条完整原组合已经乘回，合计13.941秒；整行清分母身份另0.222秒。

因此六条首一规则虽给有限生成，仍存在必须保留的参数六列关系。不能把任意规则返回称为独立自由基坐标。

## 4. 同一点的原 N/P 返回

把独立 affine Gram 源中的两条完整原三次式分别返回，得到
$$
\widehat N_S=n\mathbf b+\text{四原二次式组合},
\qquad
\widehat P_S=p\mathbf b+\text{四原二次式组合}.
$$
同步保留各原三次式本身，准确形成
$$
n\mathbf b=C_N\mathbf F,\qquad
p\mathbf b=C_P\mathbf F.
\tag{4}
$$
两条式子使用相同的 $m,Q,x,y,t$ 与相同六规则。各进行20个首项处理，全部原多项式乘回成功，实际合计49.212秒。

整行清已付分母后，六列参数多项式的双次数分别为
$$
(15,13),\qquad(14,13).
$$
六列项数分别为
$$
(151,132,138,122,136,122),\qquad
(148,128,135,119,132,119).
$$
清分母及逐列整乘积返回另用0.691秒。本页没有对某个未付参数因子求逆。

## 5. 原不同值条件的完整保留

令原 $P=P_{02}$、$L=P\lambda$、$J_{\rm germ}=P(\lambda-1-T)$。原不同值分子为
$$
D_{\rm num}=m(2L^2-2LP+P^2)-(L-P-J_{\rm germ})^2
=P^2\{m(2\lambda^2-2\lambda+1)-T^2\}.
$$
输入源规范化为
$$
\widehat D=16D_{\rm num}/m^2.
$$
本页将它作为原二次式完整返回：
$$
\widehat D-d_{\rm row}\mathbf b=C_D\mathbf F.
\tag{5}
$$
实际10步完成，0.859秒；各参数分母只需 $J^2$。由于原 $m,P$ 均非零，真实物理不同值条件仍为 $\widehat D\ne0$，必须在任何候选参数纤维中返回，不能把必要六列解直接当作原点。

## 6. 后续精确接口与再生

由 (3)–(4)，同一点的真实 $\mathbf b$ 满足四条参数六列关系，且首坐标为1。再用 (1) 作原同点乘法可以增加必要行，所有原系数和分母都能追踪到同一输入；取常数列 cofactor 时要保留完整列身份和全部未付参数零面。

本页本身没有计算完整参数 cofactor，也没有给这些关系的全域单位组合。另页已经完整排除[整个半权 $m=1/2$](R150-appendix-unit211-equal-weights-half-weight-complete-exclusion.md)，但本页的原身份不依赖该额外单位。

源均为 JavaScript Function body：

- [原18乘法与原NS/PS返回](../notes/2026-11-27-unit211-equal-weight-six-multiplication-return-8542.js)：参数分别为 (affine,"multiplication",six) 与 (affine,"NP",six)。
- [其余两原三次行](../notes/2026-11-27-unit211-equal-weight-six-remaining-cubic-rows-8542.js)：参数 (affine,"remaining",six,cubic)。
- [原不同值返回](../notes/2026-11-27-unit211-equal-weight-six-Dval-return-8542.js)：参数 (affine,"Dval",six)。
- [参数六列原整行清分母](../notes/2026-11-27-unit211-equal-weight-six-primitive-rows-8542.js)：输入上段各 rows。
- [源哈希及实际回执](../notes/2026-11-27-unit211-equal-weight-six-original-matrix-execution-8542.json)。

affine、six、cubic 的准确来源与再生次序见前页全域六生成元结果。上述数学阶段全已真实完成于 V8 有理 BigInt；没有 OS 子进程，RSS 未暴露。不保存可重算大矩阵输出。
