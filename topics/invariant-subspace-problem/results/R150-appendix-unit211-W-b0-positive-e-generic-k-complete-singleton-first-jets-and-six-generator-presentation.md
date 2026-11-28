# R150 补充：正 e 一般 k 图的完整 singleton 首阶原式、九次必要式及六元同点环境

日期：2026-11-29（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127。

## 1. 本次完成的原范围

沿[物理 f 整性稿](R150-appendix-unit211-W-b0-positive-e-generic-unit-k-physical-f-integrality-and-singleton-model.md)，取当前 W/b0 的
$$
v(e)>0,\quad v(k)=0,\quad\bar k\notin\{-2,-4,4\}.
$$
准确权坐标为 $L=(k+2)/k$，$\mu=2\lambda-3$。已证明 lambda 单位、mu 和 f 整、sigma 及全部原 Gram 坐标整，并且
$$
U=L(L-1)(2L-1)(2L-3)
$$
的剩余非零。

唯一新实际输入从真实原 Gram 的一阶系数返回四个同点必要式。只有前两个非零；它们的固定六阶来源结式给一个
$$
\deg_L C=33,\qquad \deg_\mu C=9,\qquad \deg C=42
$$
的必要多项式，仍未返回单位。本稿还给这些原式与 q2、R6、完整 N5 联合的六元自由环境；其原值商不被称为自由，后继十八列尚不冒称实际生成。

## 2. 四个完整原首阶式

全部参数仍按原恢复，不作物理 f=0 或 t=0：
$$
u=1+e,\quad Q=ek,\quad \delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad
T=\frac{u\ell\mu}{4u+2u/k-\ell}.
$$
提取准确原 e 幂后，
$$
T_0=e t_0,\quad \Phi=e^2\phi_2,\quad
P_{02}=e^2p_2,\quad G=e^2g_2,\quad P_c=e^3p_c,
$$
所有显示系数及原仿射恢复在当前图整。完整定义见
[首次输入](../notes/2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542-input.md)；
其代数是普通系数环模 $e^2$，原 Gram 第一块的乘法另外始终为
$(vw)_1=v_0w_1+v_1w_0$。

对同一完整 singleton 行 B、C，记原值 $N_B,N_C,P_B,P_C$。完整原零阶身份为
$$
[N_B]_0=[P_B]_0,\qquad [P_C]_0=[N_C]_0=0.
$$
于是定义正则的四个新式
$$
F_0=[P_B]_0,\quad F_1=[(N_B-P_B)/e]_0,\quad
F_2=[P_C/e]_0,\quad F_3=[N_C/e]_0.
\tag{1}
$$
原物理右侧 $2\lambda P_{02}h^2,P_{02}h^3$ 和 C 的对应值都有至少 $2v(e)$ 的阶；因为全部物理值已整，它们不影响 (1)。所以每个原解必须在同一 $(\bar L,\bar\mu,\bar f)$ 上满足四式。此处取正幂商的正则性由整个零阶多项式身份保证，允许 L、mu、f 随实际赋值参数变化。

本次唯一实际返回准确为
$$
F_2=F_3=0
\tag{2}
$$
的有理多项式身份，另外两个为非零三次式。其清纯权分母后的 profile 是：

| 式 | L 次数 | mu 次数 | f 次数 | 总次 | 项数 |
|---|---:|---:|---:|---:|---:|
| $F_0$ 分子 | 9 | 3 | 3 | 12 | 97 |
| $F_1$ 分子 | 11 | 3 | 3 | 14 | 117 |

对应分母只依赖 L，次数为8和10，且全部支持均在 U 中；其有理系数为1009整。两式关于(mu,f)的总次数均至多三。

$F_0$ 的完整 f 三次头再次准确返回
$$
c_f=\frac{16(2L-2)(2L-3)}{(2L-1)^2},
\tag{3}
$$
为已付单位。没有把新的 mu 头或一般权多项式当单位。

## 3. 固定六阶原来源及实际九次必要式

三个事先固定的组为 $(F_0,F_j)$，$j=1,2,3$；每组均使用固定 f 容量(3,3)。写 $F_i=n_i/d_i$，所有 $d_i$ 已付。

第一个六阶 Sylvester 完整返回全部六个伴随坐标和
$$
A n_0+B n_1=C_{\rm raw}(L,\mu).
\tag{4}
$$
随后仅从右侧剥除 U 支持，将相同尺度一起运输回原式，返回
$$
\Omega_0F_0+\Omega_1F_1+\Omega_2F_2+\Omega_3F_3
=C(L,\mu).
\tag{5}
$$
本次后两乘子为零，前两实际最终分母均为1。它们的 profile 均为
$(\deg_L,\deg_\mu,\deg_f)=(32,6,2)$、总次38，项数分别577和559。原式 (5) 是普通完整身份，未倒 Sylvester 的主元或任一新头；所有固定次数下降面保留。

实际右侧：

- $C_{\rm raw}$：L58、mu9、总67、587项，规范 SHA-256
  7337f04b6e42aa8df9fd1e459e6d6d3a8b0195688a5a102e95f4e9de41b816a3；
- 剥除的旧权因子：L25，26项，SHA-256
  7adbe4696d2ed5681c1cda38b58a144bae36f7edc0df4a7bb9108490d331c812；
- $C$：L33、mu9、总42、337项，SHA-256
  b2cd28dcd017f6802730eb09c5c536c08963d4ac8ac8d0040bd103d92834b734。

由于 (2)，另两个固定矩阵在步骤3精确奇异，按原计划记录为零；没有更换组或追加目标。非零 C 仍可能在原点为零，本次没有从次数或 profile 推出排空。

## 4. 与完整原 q2 联合的真六元环境

这一节是新完整纸面呈示，不声称下面的十八条坐标已经运行。

取
$$
\mathcal A=\mathbb Z_{(1009)}[L,U^{-1}],\qquad h=3-2L.
$$
[准确 q2 剩余式](R150-appendix-unit211-W-b0-positive-e-unit-k-exact-residual-quadratic-and-k-plus-minus-four-exclusion.md)
已经给同一点原必要式
$$
q_{\rm raw}=\frac{h^3}{9}\mu^2-4h(L-1)\mu+2h^2-3.
$$
其最高系数 $c_\mu=h^3/9$ 为已付单位，故
$$
q_\mu=q_{\rm raw}/c_\mu
$$
是真首一二次。将 $F_0/c_f$ 对 q_mu 作普通首一 mu 除法，定义
$$
F_0/c_f=\widetilde F_0+Wq_\mu,\qquad
\deg_\mu\widetilde F_0<2.
$$
因为 (3) 与 mu 无关，$\widetilde F_0$ 对 f 仍首一三次。因此
$$
\mathcal B=\mathcal A[\mu,f]/(q_\mu,\widetilde F_0)
$$
在 A 上真正自由六元，基为
$$
1,\ \mu,\ f,\ \mu f,\ f^2,\ \mu f^2.
\tag{6}
$$
证明是先取首一 mu 二次商，再在这个自由二元系数环上取首一 f 三次商；全部重根与幂零结构保留。

设 R、N 为同一个正 e 剩余点上完整 R6、N5 的正则剩余，定义
$$
\mathcal J=(q_{\rm raw},F_0,F_1,R,N).
$$
R、N 使用完整原定义，不来自旧结果式的一个必要根集合。任意 G 先对 $\widetilde F_0$ 除 f，再对 q_mu 除 mu：
$$
G=r+Q_f\widetilde F_0+Q_\mu q_\mu
=r+\frac{Q_f}{c_f}F_0
  +\frac{Q_\mu-Q_fW}{c_\mu}q_{\rm raw}.
\tag{7}
$$
(7) 是普通原多项式身份。由 (6)，在 B 中的理想 $(F_1,R,N)$ 由三个种子各自六个基倍完整生成。因此
$$
\mathcal A[\mu,f]/\mathcal J
\simeq\operatorname{coker}(\mathcal A^{18}\longrightarrow\mathcal A^6).
\tag{8}
$$
原值商不被假设为自由，也不把五个原条件称作原物理解的充分条件。式 (8) 提供下一不同原输入的准确呈示：它加入已付首一 q2 和两条完整值方程，不重跑 (4) 的已完成 f 结式。

## 5. 唯一实际执行

[新完整 singleton 首阶源](../notes/2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542.py)
blob **2f951f2fb6a9733e4de9a9aa3a403f8e5d61087e**，
SHA-256 **958f1bbbf613211a047bb2adf91d340c8fd3ed23b5794470dee3f4d0ba9cfc5a**。

唯一 [run 46174516962](https://github.com/Rogerhu12/math-research-public/actions/runs/46174516962)，job **141070093707**：

- 预算120秒、1GiB，外135秒；实际 **0.3235243199999971秒 / 40120KiB / exit0**；
- 五条数学记录完整读取，最后阶段0.25074698199999546秒；
- 六条完整原jet身份、六个新Sylvester坐标、两次原来源回乘、3515次精确乘积返回；
- stdout **4943B**，SHA-256 **99ad0a454abd0d186cf4197588b57a9b95946c00025271ce0c1970efb0ff35a5**；
- source及实际pull提交均为 **92f3e866acacff93d72950b35d5b366fbf52d214**；
- 实际pull时间 **2026-11-28 18:12:02.508537 UTC**，两份README未变。

[小回执](../notes/2026-11-29-unit211-W-positive-e-generic-k-complete-singleton-NP-first-jets-8542-execution.json)
保存完整阶段、源指纹和内层退出状态。没有大系数缓存，没有重跑旧 q2/R6/N5 投影或83e初始理想。一般 k、内部权图和DVR边界继续，普通ISP尚未完成。
