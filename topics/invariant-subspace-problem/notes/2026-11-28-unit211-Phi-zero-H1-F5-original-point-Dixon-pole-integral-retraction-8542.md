# Phi=0、H1 最后五次完成块：新的原有理点、Dixon 极点与整回缩输入

日期：2026-11-28（Asia/Taipei）。本文件是首次执行的数学输入与判据，**不是已运行成功的结论**。仅续原 $\Phi=0$、$D\ne0$、完整 $H_1=0$ 权图。前四个实际完成块已由整 $F_9$ 原头返回排除；当前至多五个权对、五个 $(u,Q,\lambda,T,v)$ 点及十个完整规范原点。上一次完整 Gram20 的十二原生成元全为零、$D$ 模 $1009$ 为零，不能据此在特征零排空。

## 1. 直接取新的原特征零输入

在完整首一四次 $g(u,Q)$ 中令

$$
q_*(u)=4(u-1)(u-2),\qquad
F_5^{\rm int}(u)=14u^5-90u^4+213u^3-234u^2+127u-28,
\qquad F_5=F_5^{\rm int}/14.
$$

实际构造要求逐项返回

$$
g(u,q_*(u))=16(u-1)^3F_5^{\rm int}(u).
$$

因此这是由原 $\ell=1/2$ 权条件导出的 QQ 输入，不是把一个有限域因子猜成 QQ 因子。程序保整个 $K=\mathbb Q[u]/(F_5)$，重新检查其模 $p=1009$ 的完整分解与乘回。该明确首一多项式的约化为

$$
\overline{F_5}=u^5+426u^4+808u^3+704u^2+946u+1007.
$$

若此完整五次在模 $p$ 不可约，Gauss 引理给 $F_5$ 在 QQ 不可约；其完整约化 SHA 必须与已经登记的最后一个真实 $P_{201}$ 完成块一致。单靠这项一致仍不说明 $F_5\mid P_{201}$，后面另付原极点证明。

在 $K$ 中设

$$
Q=q_*,\qquad \lambda=\ell=\frac12,\qquad T=-\frac12.
$$

程序从已刊四个原二次式 $R,W,O,N_1$ 的必要构造前缀，得到同一 $v$ 的四个次数至多二次的多项式。在整个 $K[v]$ 做完整短除及 Bézout 乘回，只有确实得到首一次共同因子 $v-v_*$ 才继续。然后逐式返回四原二次式及同一完整 $F_6,N_V$。这里不运行旧范数、五块秩或 Gram20 门。

所有原权及几何量保持原定义：

$$
\ell=1-\frac{2(u-1)(u-2)}Q,\quad
J=2u(1-u)+\ell Q,\quad
T_0=2u-\ell Q-2u^2,\quad
P_f=T_0(J-Q),
$$

$$
G=\lambda P_{02}+(u-1)T_0,\quad
f=\frac{GT_0-QP_{02}(\ell+T)}{P_f},\quad
z=\frac{v-Jf+G}{bc}.
$$

这里旧原 $z=Qt$，不与新 $v$ 混用。直接代入要返回

$$
D=\ell(2\lambda^2-2\lambda+1)-T^2=0.
$$

程序不会倒置 $D$。

## 2. 同一个点必须满足整个已有必要代数

把四原式在该点取值后，重新作其三行二次头的 adjugate 恒等式。其真实头 $h$、六个缩放乘法列 $M_T,M_v$ 要返回

$$
(1,T,v)M_T=hT(1,T,v),\qquad
(1,T,v)M_v=hv(1,T,v).
$$

原第四余行、完整交换子及完整 $F_6,N_V$ 的缩放列均须被该同一行消去；四个真实固定三列行列式均须逐项为零。此处只在该明确 QQ 点计算小列，不重造旧全参数范数。各列与原多项式之间只曾移去已经逐项乘回的原权单位。因此，只要程序返回这些原权在该点非零，四个已刊原 $\lambda$ 多项式在同一 $\lambda=1/2$ 全零，三个同 $Q$ 固定 Sylvester 结果式也全零，包含它们所有最高次退化的情况。

为使后面的提升合法，程序检查 $q_*,\lambda,T,v_*,z,h$ 在基 $1,u,\ldots,u^4$ 中的全部系数都为 $p$ 整；每个原已付权与实际 $h$ 的模值必须在整个五次剩余域中有真实 Bézout 逆，并逐个乘回。这一步不由“物理上非零”代替模单位，不换素数。

## 3. 新原单项式左核支付 $F_5\mid P_{201}$

只读取 ef9 原 Dixon 源直到旧 Gaussian 前，得到原八阶 $D_8$、旧多项式换元与确切原来源分母 $S_{418}$。先返回

$$
\gcd(F_5,S_{418})=1.
$$

它保证全部原输入、$b_1,A_0$ 与换元系数在 $F_5$ 正则。旧原恒等式为

$$
L=a(\lambda)T+b(\lambda)z+c(\lambda)
 =A_0T+C_0+\mu x,\qquad \mu=\lambda-\lambda_0,
$$

$$
x=a_1T+b_1z+c_1+2c_2\lambda_0+c_2\mu.
$$

程序在刚才那个 QQ 原点返回 $L=0$、两个方向的换元与原三多项式 $R,W,N_1$，再取原八个单项式行 $w(x,\mu)$，实际返回

$$
wD_8=0,\qquad w_0=1.
$$

这不做新的 Gaussian。已刊唯一向量 $D_8^{-1}e_0$ 若全部 QQ$(u)$ 四坐标在 $F_5$ 正则，便可在该原点取值，与上式给出的 $0=1$ 矛盾。因此其某一标量坐标必在 $F_5$ 有极点。已刊全部精确极点支持为旧来源支持 $C_{55}$ 与 $P_{201}$；$C_{55}$ 的支持包含于 $S_{418}$，故新真实 QQ 不可约 $F_5$ 必整除 $P_{201}$。

这项原极点证明与模约化不可约性合在一起，才识别出最后真实完成块：

$$
\mathcal O_\phi\simeq\mathbb Z_{1009}[u]/(F_5),
$$

其中 $\mathbb Z_{1009}$ 表示 $1009$ 进完备整数环。不能把一般模因子直接称为 QQ 因子。

## 4. 整回缩迫使最后原必要代数确实为碰撞点

设 $\mathcal C_\phi$ 是此前完成的同 $Q$、同 $\lambda$、同 $T,v$ 必要代数，**没有倒置 $D$**。已刊真实单位子式与 Nakayama 已证明它有限于 $\mathcal O_\phi$，模极大理想由 $1$ 生成，故结构映射为满射

$$
\pi:\mathcal O_\phi\twoheadrightarrow\mathcal C_\phi.
$$

这一步不要求先知道其核是否为零。

若本次所有实际返回成立，明确的 $p$ 整 QQ 点满足三个同 $Q$ 结果式、四个原 $\lambda$ 多项式、全部原二次式、交换子与完整 $F_6,N_V$。各原头和既有归一单位也保持单位。因此评价给出真实 $\mathcal O_\phi$ 代数映射

$$
\varepsilon:\mathcal C_\phi\longrightarrow\mathcal O_\phi.
$$

它保持基元素 $u$，所以 $\varepsilon\pi=\mathrm{id}$。满射 $\pi$ 因而亦单射，$\mathcal C_\phi\simeq\mathcal O_\phi$，其全部坐标等于本次精确点。特别是 **$D$ 在整个原必要代数中确实等于零**，不是仅模 $1009$ 为零。这才排掉最后原 $D\ne0$ 完成块。合已付 $F_9$ 四块和其余八个原单位块，才可宣布当前整个原 H1 图排空；不排除一般原 $D=0$ 碰撞图，也不解决 ordinary ISP。

若任何原点、旧 $L$、来源正则性或整单位判据未返回，程序保留准确的未决状态；不会由部分结果宣整图排空。

## 5. 唯一源、依赖与资源

新源建议：

`notes/2026-11-28-unit211-Phi-zero-H1-F5-original-point-Dixon-pole-integral-retraction-8542.py`

- blob：`a26a3130e5e9d1fd0a2203bd67a6cc644ec0313c`。
- SHA256：`bcd0f992fff149a388f378be1f435a809143cae8c82938eb97e61947be107ae6`。
- 16352 字节，120 秒 / 1 GiB；只输出小日志、定义、SHA 和乘回布尔结果。
- 本文生成时尚未执行。

只有四个直接依赖；两个历史 JSON 仅由 runner 的 provenance loader 临时读取，不再经工具搬运或入库：

1. `2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py`，SHA `5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef`。环境别名 `ISP_H1_POLYNOMIAL_V_SOURCE`；仅执行至 `def polynomial_norm` 前的必要定义并调用原四式构造。
2. `2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py`，SHA `ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc`。环境别名 `ISP_H1_ORIGINAL_DIXON_SOURCE`；仅执行至旧 Gaussian 注释之前。
3. `2026-11-27-unit211-Phi-zero-whole-first-head-original-linear-relation-exact-input-8542.json`，SHA `c6c0b8973ea18a3fd320921238a7e331e460ca26ed1d96ec5f4e6276fd45ff44`。
4. `2026-11-27-unit211-Phi-zero-H1-b-zero-lambda-linear-exact-part-01-8542.json`，SHA `1bc01ff121193bf3e50edd7545e0d95ef5a6f6ed1ded3e2b5973d4e6d4276393`。

ef9 在其自身文件同目录读取两个历史 JSON，runner 必须保同 basename。两个必要源码前缀均只设相同 1 GiB 上限；统一 execute_prefix 在整个前缀执行期间把其 signal.alarm 请求钳制到本源最初绝对 DEADLINE，退出后亦恢复真实剩余时间，不会因前缀重设闹钟而延长总 120 秒；不会尝试提高硬资源界。旧未执行 cbe2795 草稿仅有此计时包装差异，数学输入不变，不记录为实际失败。
