# R150：正确 Phi 中心 t 模型的完整 NS/PS、精确十行二列与非零六次必要式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整证明，唯一首次实际成功。** 在正确原 $t$ 参数 $N_1$ 的斜率补图上，完整原 NS、PS 已分别返回普通三均值组合，随后只作一次中心化仿射替换。得到首一 $\omega^2$、系数 $t$ 次数均为三的两个原线性行、它们的两个 $\omega$ 倍，以及完整 $I_6$ 的精确十行二列呈示。两个真实乘子的共同内容为常数；其原组合给非零必要式
$$
C_6(u,Q,t)=0,\qquad
(\deg_u,\deg_Q,\deg_t)C_6=(36,23,6),\quad
\deg C_6=44.
\tag{1}
$$
**本结论仍限斜率补图。两条 $H_6,H_8$ 整零曲线及 $C_6$ 的全部首项零纤维保留。原标量分母较小，不足以自行证明全图提升。**

## 1. 已付原范围和同点斜率

沿[原 t 参数 N1 与六行二列模型](R150-appendix-unit211-Phi-zero-corrected-t-parameter-N1-two-slope-curves-and-six-by-two-model.md)，$\mathcal A$ 为正确 Phi、distinct singleton、物理 $D\ne0$ 图中已经支付的权环，本次使用的支持是
$$
u,\ Q,\ 1-Q,\ u-1,\ Q+4(u-1),\ L,\ M_n,\ 2\ell-1,
$$
$$
L=Q-2(u-1)(u-2),\qquad \ell=L/Q,\qquad
M_n=2uL-L^2-u^2Q,\qquad M=M_n/Q.
$$
其中 $2\ell-1$ 由[整个正确 ell-half 排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)支付，不恢复错误 compact 均值链。

设 $F=(F_0,F_1,F_2)=(\mathcal R,E_{Be},E_{Bo})$ 为同一个完整原三均值。已成 $N_1$ 余式为
$$
n=N_1-\eta\cdot F
=n_0(t)+(a_ft+b_f)f+(a_Vt+b_V)V,\qquad
n_0=At^2+Bt+C,
$$
$$
\Delta=a_fb_V-b_fa_V.
\tag{2}
$$
只在 $\mathcal A'=\mathcal A[\Delta^{-1}]$ 中工作；$\Delta$ 的未付支持是 QQ 不可约的 $H_6H_8$。定义
$$
\omega=a_ff+a_VV+At+B,
$$
$$
\widehat f=\frac{(a_Vt+b_V)\omega-Ab_Vt-Bb_V+a_VC}{\Delta},\qquad
\widehat V=\frac{-(a_ft+b_f)\omega+Ab_ft+Bb_f-a_fC}{\Delta}.
\tag{3}
$$
本次两个完整逆身份均返回。$A,B,C$ 是 $n_0$ 的系数，与旧权头的同名字母无关。

[中心化纸面推论](R150-appendix-unit211-Phi-zero-corrected-t-slope-centering-and-original-NSPS-cubic-pairs.md)已证明 (3) 固定 $\omega$ 后对 $t$ 一次；没有新增 $t,D,\lambda$ 或个别几何头的逆。

## 2. 完整原 NS/PS 的普通三均值来源

令 $v_B,v_C$ 是同一原 Gram 的两个 singleton 行，
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
本次完整原输入为
$$
NS=bN_4(v_B)+cN_4(v_C)
-2\lambda P_{02}(\ell+2T+A_2),
$$
$$
PS=bP_2(v_B)+cP_2(v_C)
-P_{02}(\ell+3T+3A_2+B_3).
\tag{4}
$$
$N_4$ 保留全部原五项，$P_2$ 使用完整中心三次；没有省略 $(1+\xi)^2,(1+\xi)^3$ 的低项。真 dual 乘法的一阶坐标仍为 $v_0w_1+v_1w_0$。C 行由完整原共轭返回；这与 trace、DK 和中心化交换，不选择某个 $\rho$ 根。

三条真均值规则为
$$
(f^2,fV,V^2)^t-\mathbf r(1,f,V)^t=H^{-1}F^t,\qquad
\det H=32uQ(2\ell-1)/M^2.
\tag{5}
$$
程序对 (4) 固定选择最高 $(f,V)$ 单项式，用 (5) 替换并累计同三个原均值的普通多项式乘子。十四次降次步骤后，完整返回
$$
NS-r_{NS}(1,f,V)^t=\tau_{NS}\cdot F,\qquad
PS-r_{PS}(1,f,V)^t=\tau_{PS}\cdot F.
\tag{6}
$$
两行 $r_{NS},r_{PS}$ 的真实 $t$ 次数均为 $(3,2,2)$，各三个 $\tau$ 的 $(f,V)$ 次数均为一。两个差式在原多项式环中全式返回；没有把一个未经证明的三维模型当自由结合代数。

必要的 $N_1$ 和 $\Delta$ 系数只按既成 profile SHA 再生。本次未重跑旧 CH、斜率因式、未中心化六行门或旧 $\lambda$ 六次 cofactor。

## 3. 中心首一二次及四条新行

令
$$
\gamma=(a_f^2,2a_fa_V,a_V^2)H^{-1}.
$$
本次返回完整原三来源
$$
q_\omega=\gamma\cdot F(\widehat f,\widehat V)
=\omega^2+q_1(t)\omega+q_0(t),
\qquad \deg_t(q_0,q_1,1)=(2,2,0).
\tag{7}
$$
首一性不使用任何单个均值的 $\omega^2$ 头逆。

将 (3) 一次代入 (6) 的三个余式坐标，得到
$$
\ell_N=N_0(t)+N_1(t)\omega,\qquad
\ell_P=P_0(t)+P_1(t)\omega,
\tag{8}
$$
其中四个系数的实际 $t$ 次数都是三。这里的 $N_1(t)$ 只是 $\ell_N$ 的一次系数，不是原极化式 $N_1$。

两个新的 $\omega$ 倍完整返回为
$$
\omega(a+b\omega)
-\{-q_0b+(a-q_1b)\omega\}=bq_\omega.
\tag{9}
$$
两行 (8) 的次数均为 $(3,3)$，两个倍数行次数均为 $(5,5)$。它们通过 (6) 的完整原来源与 (3) 的可逆原 $N_1$ 消元相接。

在首一二次环境
$$
S=\mathcal A'[t,\omega]/(q_\omega)
$$
中，原四式由已刊六行的可逆平移像精确呈示；加上 (8)–(9) 四行，恰给整个 $I_6$ 的十行二列呈示。自由性只用于所定义的首一环境 $S$，不用于原方程商。六条旧行没有作为本次目标重新运行。

## 4. 两个实际原乘子的共同内容与非零 C6

取两个实际乘子
$$
\mu=(P_1,-N_1).
$$
将它们的纯权分母取最小公倍数清除；两个所得多项式乘子的共同内容实际为常数。用这两个新的多项式乘子重新返回完整两坐标：
$$
\widetilde\mu_N(N_0,N_1)+
\widetilde\mu_P(P_0,P_1)=(C_{\rm raw},0).
\tag{10}
$$
式 (10) 是新原行组合，不是将一个旧标量方程除以未付因子。

原 $C_{\rm raw}$ 的约分分子总次数 45，次数 $(u,Q,t)=(37,23,6)$，3554 项；分母总次数 6，次数 $(u,Q)=(2,5)$，13 项，profile SHA256
e6ad630c7a116018ce1b4dcdd95145dc3b38ba861670c4774063194900672c59。
按本次补图已明确允许的权支持剥除后，得到 (1) 的非零 $C_6$：

| 参数 | 实际返回 |
| --- | --- |
| $(u,Q,t)$ 次数 | $(36,23,6)$ |
| 总次数 | $44$ |
| 项数 | $3402$ |
| 规范 SHA256 | 5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1 |

其真实 $t^6$ 系数 $h_t(u,Q)$ 为总次数 38、双次数 $(36,19)$、434 项，SHA256
89cadc1ec0de4d55df49a64ded467843259e929b15dd7dc88f973ccb80e6dd4b。
没有因式分解或单位性结论；整个 $h_t=0$ 保留。

因此在当前斜率补图上，$C_6$ 是原 $I_6$ 的必要式。在进一步 $h_t\ne0$ 的权开图，$C_6/h_t$ 为首一 $t$ 六次式，与首一 $q_\omega$ 共同说明：未反演几何 $D,t$ 的必要商可由
$$
t^j,\quad t^j\omega,\qquad 0\le j\le5
\tag{11}
$$
这十二个元素生成。不要求它们线性独立。这个推论只针对明确的必要坐标代数；随后几何局部化只可直接继承固定权纤维的有限性，不能无证声称仍为原基环的有限模，也没有加入独立 $U_0$ 三次尺度的计数。

本次没有构造原六式上的最后六个展开乘子，也没有检验补回的第三 $N_1$ 乘子是否在整个旧权环内。因此，即使 (10) 的标量分母较小，仍不得将 (1) 外推至 $\Delta=0$。全图提升是另一个真实原来源目标。

## 5. 唯一实际身份与范围

[源码](../notes/2026-11-28-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-8542.py)；
[输入](../notes/2026-11-28-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-8542-input.md)；
[小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-8542-execution.json)。

源 blob 5ebffd4768a82d2244deda197ec501d5b67ea5ca，15867 字节，SHA256
dc945d90b88ff9388b561daf411304787a92cbc5c542fe32950e0e5739bc1a26。
自含、零依赖，最初绝对 120 秒 / 1 GiB，外层 135 秒。

唯一 run 46149159181 / job 140991685588。源提交
0b65eec6c741db5c03f663ff2c4856258307f3dd；真实 pull 到
da5f2a79af66fc6702df9c7e2b64ba1e123eb35a，2026-11-28T13:21:06.209356+00:00，两规则未变。
数学 2.698057075 秒；driver 2.776731405 秒；峰值 92920 KiB；exit 0。
stdout 9754 字节，SHA256
a4eb3fe409d3d242ac6ae06faa39049f4a8eef879630ffa9ccbc438190542888。

实际共 165 次精除回乘、14 次三次原降次、2 条普通 NSPS 来源、2 条中心逆、1 条首一原组合、4 个新线性坐标、2 个新倍数身份及2个新 cofactor 坐标返回。全部九条数学阶段记录已读取；没有仅据工作流绿色判断成功。

$H_6=0,H_8=0,h_t=0$ 的全部原纤维仍在当前未付范围。这里不声明补图或整个 Phi 为空，不将 $\deg_t C_6=6$ 当纯权有限点结论，也没有恢复任何撤回的错误紧凑均值后继。
