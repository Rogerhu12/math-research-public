# 正确 Phi：完整六原乘子给全图 t 六次，真实 H28 首项补图十八生成

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

## 1. 已实际完成的结论与范围

在当前正确的 $\Phi=0$、两个 singleton 谱值不同、物理 $D\ne0$ 的原规范图中，存在非零多项式
$$
C_6(u,Q,t)\in I_6,\qquad
(\deg_u,\deg_Q,\deg_t)=(36,23,6),\qquad
\deg C_6=44.
\tag{1}
$$
这里的包含成立于只反演既有原权单位的普通多项式环中。它覆盖整个旧斜率 $\Delta=0$，包括 $H_6=0$、$H_8=0$ 及其交点；没有把这些曲线本身宣称为已排空。

(1) 是此前中心坐标所得的同一个规范 $C_6$，这次新支付的是完整第三 $N_1$ 乘子以及全部六个原始乘子的正则性。其 3402 项规范 profile SHA256 为
5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1。

原 $t^6$ 头总次数 38。只剥既有原权单位后，剩下总次数 28、双次数 $(26,15)$ 的 $H_{28}$；完整 QQ 因式只有一个不可约因子，重数为一。在 $H_{28}\ne0$ 上，未反演几何 $D$ 的必要 $I_6$ 商由
$$
t^j,\quad t^jf,\quad t^jV,\qquad 0\le j\le5
\tag{2}
$$
十八个元素生成。这里不要求商自由；整个 $H_{28}=0$ 曲线及其全部原值纤维仍保留。

本结论不宣全 Phi 排空、全权首项单位或有限权点。旧错误 compact 所污染的来源不因本文恢复。依据是唯一首次 run [46150593405](https://github.com/Rogerhu12/math-research-public/actions/runs/46150593405)，内层 exit 0；准确小回执见[执行记录](../notes/2026-11-28-unit211-Phi-zero-corrected-t-sextic-complete-six-original-multipliers-8542-execution.json)。

## 2. 原系数环及六个原式

沿用[全 t 参数真三均值](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)中的
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad
M_n=2uL-L^2-u^2Q .
$$
本次实际分母分类只使用
$$
u,\ Q,\ \delta,\ s,\ K_w,\ L,\ M_n,\ 2\ell-1
\tag{3}
$$
这些既有原权单位；最后一项由[整 ell-half 原排除](R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-original-exclusion.md)支付。令 $\mathcal A$ 为相应的 QQ 权局部化环。特别地，$\Delta$、$H_6$、$H_8$ 都不在 (3) 中。

记
$$
F=(\mathcal R,E_{B,e},E_{B,o}),\qquad e=(1,f,V)^t,
\qquad I_6=(\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{4}
$$
$\mathcal R$ 与真第一均值满足 $2\mathcal R+E_1-bE_B-cE_C=0$；所以 (4) 使用正确原均值，而非错误的 germ 分量平方。

$N_1$ 为原 N4 极化减去 $4\lambda wP_{02}$，而
$$
\begin{aligned}
NS&=bN_4(B)+cN_4(C)-2\lambda P_{02}(\ell+2T+A_2),\\
PS&=bP_2(B)+cP_2(C)-P_{02}(\ell+3T+3A_2+B_3),
\end{aligned}
$$
其中 $A_2=2\lambda^2-2\lambda+1$、$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。源中 N4、中心 P2 和双数乘法都取完整原定义。$\lambda,T$ 在 $(t,f,V)$ 中的恢复为
$$
\lambda=\frac{Jf-QV+bcQt-sT_0}{P_{02}},
\qquad
T=-\ell+\frac{T_0(f-V+bct)}{P_{02}}.
\tag{5}
$$
这些恢复只用原权单位。

真三均值的首一二次规则给
$$
\begin{aligned}
n=r_Ne&=N_1-\eta F,\\
r_{NS}e&=NS-\tau_{NS}F,\\
r_{PS}e&=PS-\tau_{PS}F .
\end{aligned}
\tag{6}
$$
$\eta,\tau_{NS},\tau_{PS}$ 都是普通原均值乘子。三个余式的 t 次数分别为 $(2,1,1)$、$(3,2,2)$、$(3,2,2)$。它们及之前两个终端乘子本次只作唯一参数定义再生，并按已成 SHA 钉死；未重放旧 $q_\omega$、$\omega$ 倍或两列 cofactor 证明门。

## 3. 真正新增的第三 N1 乘子

写
$$
n=n_0+n_ff+n_VV,\quad
n_f=a_ft+b_f,\quad n_V=a_Vt+b_V,\quad
\Delta=a_fb_V-b_fa_V.
$$
[中心 t 的原 NS/PS 结果](R150-appendix-unit211-Phi-zero-corrected-centered-t-original-NSPS-ten-by-two-and-sextic.md)给出的两个多项式乘子记为 $\mu_{NS},\mu_{PS}$。它们由
$$
b_{NS}=\frac{n_Vr_{NS,f}-n_fr_{NS,V}}{\Delta},\qquad
b_{PS}=\frac{n_Vr_{PS,f}-n_fr_{PS,V}}{\Delta}
$$
的 $(b_{PS},-b_{NS})$ 清实际纯权分母而定义。前次共同内容为常数一，本次不重算该 gcd。

定义
$$
c_{NS}=\frac{-a_Vr_{NS,f}+a_fr_{NS,V}}{\Delta},\qquad
c_{PS}=\frac{-a_Vr_{PS,f}+a_fr_{PS,V}}{\Delta},\qquad
\kappa=\mu_{NS}c_{NS}+\mu_{PS}c_{PS}.
\tag{7}
$$
这里 $\Delta^{-1}$ 暂时只在 QQ 权函数域中用于计算，不能据此丢掉其零面。新运行完整返回三个原坐标
$$
-\kappa r_N+\mu_{NS}r_{NS}+\mu_{PS}r_{PS}
=(C_{\rm raw},0,0).
\tag{8}
$$
第三乘子 $-\kappa$ 最终实际分母的双次数为 $(2,2)$、总次数 3、共 7 项，SHA256 为
bcda16ffc34a4e04988212d0963b447de4e7b026cc2bdc91388c638994b53ac9。
其分子 t 次数 4、总次数 36、1754 项。运行同时核对 (8) 的标量确是此前定义的同一 $C_{\rm raw}$；这只钉住对象，新证明来自全三坐标的实际乘回。

## 4. 完整六原乘子在旧权环中返回

按 (4) 的六式顺序，定义
$$
\Omega_{\rm mean}
=\kappa\eta-\mu_{NS}\tau_{NS}-\mu_{PS}\tau_{PS},
\qquad
(\Omega_N,\Omega_{NS},\Omega_{PS})
=(-\kappa,\mu_{NS},\mu_{PS}).
\tag{9}
$$
由 (6)、(8)，其应有身份是
$$
\sum_{i=0}^{5}\Omega_i\,{\rm Original}_i=C_{\rm raw}.
\tag{10}
$$
新运行将 (10) 展开为普通 $(t,f,V)$ 多项式完整乘回。它没有假定三生成元商自由、结合或具有独立坐标。

随后逐个分类 **最终约分后的实际分母**，包括六个 $\Omega_i$ 与 $C_{\rm raw}$。七个分母全部只含 (3) 的旧已付支持，未付剩余分母列表为空。前三均值乘子的实际分母总次数为 $3,4,4$；$N_1$ 的为 3；NS、PS 两乘子为多项式。$C_{\rm raw}$ 自身的分母总次数为 6。判定使用每个分母的精确剥除与因子乘回，不由标量分母小而推测其它乘子。

只清 $C_{\rm raw}$ 的实际旧分母、剥其分子中的旧已付因子，并把完全相同的乘因子运输到六个乘子，运行又完整返回
$$
C_6=\sum_{i=0}^{5}\widetilde\Omega_i\,{\rm Original}_i,
\qquad
\widetilde\Omega_i\in\mathcal A[t,f,V].
\tag{11}
$$
六个新最终分母再次通过旧权分类。(11) 是普通局部化多项式环中的原身份，故包含 $\Delta=0$ 的整个零纤维，不依赖补图点集稠密性。它也不反演物理 $D$、$t$、$\lambda$ 或任何斜率因子。

因此 (1) 现在是整个当前原 Phi 权图的必要关系。此前只在 $\Delta\ne0$ 的两列表示仍可使用，但它不是本次全图包含的依据。

## 5. 真实 H28 与十八生成的准确推论

令 $h_{38}=[t^6]C_6$。新运行首次对其作完整 QQ 因式，先剥 (3) 的旧单位，并全乘回，得到
$$
h_{38}=U\,H_{28},\qquad U\in\mathcal A^\times .
\tag{12}
$$
实际参数如下：

| 对象 | 双次数 $(u,Q)$ | 总次数 | 项数 | 规范 SHA256 |
|---|---:|---:|---:|---|
| 原 $h_{38}$ | $(36,19)$ | 38 | 434 | 89cadc1ec0de4d55df49a64ded467843259e929b15dd7dc88f973ccb80e6dd4b |
| 剩余 $H_{28}$ | $(26,15)$ | 28 | 250 | 49c4eef279d2593cbf0355dcac116dbfb6505fa5e785866f3cc02fb2a595de49 |

$H_{28}$ 的 FLINT QQ 因式常数为 $1/131072$，仅一个因子、重数一；该因子 profile SHA256 为
a9971537b149e10d05746789fd2dd959760ca47b65b9672af753412d865a0236。
完整因子乘回已返回。这说明 QQ 不可约，不宣称复数域绝对不可约，更不把它当权单位。

在 $\mathcal A[H_{28}^{-1}]$ 上，(11)、(12) 给首一 t 六次关系。原三均值商已在 $\mathcal A[t]$ 上由 $1,f,V$ 生成，所以其进一步商 $I_6$ 在 $\mathcal A[H_{28}^{-1}]$ 上由 (2) 生成。具体地，先用真二次规则把任意 $(f,V)$ 单项式降到三生成元，再用首一 t 六次将每个系数降到 t 次数至多五。无需选择模基或假定没有其它关系。

该有限生成断言针对 **未作几何 D 局部化的必要代数**。再取物理 $D\ne0$ 开集只保证纤维仍有限、维数不增，不能自动保留基环上的有限模性质。独立 $U_0$ 尺度没有计入十八生成；本文不给新增完整规范点数。$H_{28}=0$ 全部保留；它与此前 $C_{77}$ 是不同 QQ 因子这一事实本身也不支付全权单位理想。

## 6. 实际执行身份与不重放边界

新源：[完整六原乘子源码](../notes/2026-11-28-unit211-Phi-zero-corrected-t-sextic-complete-six-original-multipliers-8542.py)；[冻结输入说明](../notes/2026-11-28-unit211-Phi-zero-corrected-t-sextic-complete-six-original-multipliers-8542-input.md)。

- 源 Git blob：fb4163bda5bb1d9d7d6c0ac778ccc899469d2c8f；16367 字节。
- 源 SHA256：00f6e0b8b22b67031c37e5f983bdef4aa08b639cfb0b8d6ef3fca1bafbae4cf3。
- 唯一首次 run/job：46150593405 / 140996173610，attempt 1。
- source/pull commit：dfc2ab4ab7d8c8125d9ff9f94145b84285575497。
- 真 pull 时间：2026-11-28T13:38:23.564797+00:00；两 README 规则均未变。
- 内层 exit 0；driver 1.107809790 秒；数学阶段 1.031441200 秒；峰值 52184 KiB。
- stdout 4975 字节，SHA256 61ff3e0ed1e231379c0a867d142bcf598fc52427959cf69ec1203e0177d0c0c0。
- 新返回包括三原坐标、完整六原普通身份、七个最终分母分类、规范 $C_6$ 六原再次返回，以及首项完整因子乘回；43 次精确除法乘回。

本源自含、零依赖、总 120 秒 / 1 GiB；没有执行旧中心二次、六行/十行或两列 cofactor 证明门，也没有保存大系数载荷。必要原迹定义再生只用于新终端合成，不另登记旧结果。实际代码、输入和小回执足以唯一重建本文对象；不把工作流绿色代替上述内层返回。
