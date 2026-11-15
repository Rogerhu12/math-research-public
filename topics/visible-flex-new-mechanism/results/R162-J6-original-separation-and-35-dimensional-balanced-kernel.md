# R162：J6 的完整原式分离与三十五维 pure-zero balanced 像

日期：2026-11-15。**已证明。** 唯一新增研究目标在公开 Actions [43663137188](https://github.com/Rogerhu12/math-research-public/actions/runs/43663137188) 完成；来源 commit 为 `0700d815a013cfdf375490016a8eb919904f30a9`。

主结论是

$$
\boxed{J_6\notin R_{-2}+\operatorname{span}_{\mathbb R}\{N^3G,J,D_0\}.}
\tag{1}
$$

证明来自同一固定实 profile 对、同一右锚下的真实原式有理评价和非零 44 阶子式，不依赖不完备 normal form 的余项。结合 R160 的一般 pure 身份，新增方向可取为真正 pure-zero 的 $H_6=J_6-K_6$。相应完整 44 维空间的 pure 核及其 faithful balanced 像恰为 35 维。

完整真实空间的已证下界因此升为

$$
\boxed{\dim U\ge240.}
\tag{2}
$$

这增加的是 span 下界；已付 lineality 和真实共同查询下界仍至少 237，没有由本次分离取得 $J_6$ 的有符号成本或完整 period/ruling 支付。

## 1. 原目标和已经完成的比较空间

记 $U=\mathcal U_4$、$R=\mathcal R_8$，下标 $-2$ 表示 profile 仿射真权。相位模式另记为 $V_{-4},V_{-2}$，不与该真权混同。

本次原目标仍是 [R160](R160-general-pure-J6-identity-and-balanced-mixed-entry.md) 的同一个完整两模式系数

$$
J_6=[h^{-2}k^0\omega^0(\log h)^0]\bar A_{kk}.
\tag{3}
$$

它来自 R136 已发布五族原式的 `family=A_kk`、`state_key=[-2,0,0,0]`，仅含真权 $-2$。两个原根 SHA256 为：

| 相位模式 | 完整原根 SHA256 |
|---|---|
| $-4$ | `9f28420162242f5899bcbf4bb2398b793935ebad021b8f57bbd1fe129f4a0ab1` |
| $-2$ | `19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f` |

[R131](R131-third-G-translation-separation-and-111-query-control.md) 已证明 $\dim R_{-2}=40$；[R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 和 [R153](R153-D0-original-separation-beyond-response-G-and-J.md) 已证明

$$
S=R_{-2}+\mathbb RN^3G+\mathbb RJ,\qquad \dim S=42,
$$

$$
E_D=S+\mathbb RD_0,\qquad \dim E_D=43.
\tag{4}
$$

这些是真实完整函数空间的已证维数，不是代表秩。本次按原固定顺序消费 $S$ 的 42 列 $U_1,\ldots,U_{42}$，末尾再接 $D_0$，不重算 40 个旧响应或任何旧上界关系。

## 2. 旧 42 枢轴与已存第 43 步

R136 已保存同一固定 profile 对上的 42 阶有理评价矩阵 $A$。其列为 $U_1,\ldots,U_{42}$，其行是已发表的 42 个相位/实虚部/位置查询。模素数

$$p=2147483647$$

有

$$\det\bar A=602105349\ne0.$$

R153 随后保存了 $D_0$ 的 42 个新原值、模坐标 $\bar c_D$ 及两个**完整模残差多项式**

$$
\bar R_D
=\overline{D_0-\sum_{j=1}^{42}\widetilde c_{D,j}U_j}.
\tag{5}
$$

这里 $\widetilde c_{D,j}\in\{0,\ldots,p-1\}$ 是模坐标的整数代表，不是宣称的有理成员坐标。旧额外查询是

$$
e=(\text{相位 }-2,\ \operatorname{Re},\ t=1/70,\ \xi=141/70),
$$

且已有准确非零证据

$$
\bar R_D(e)=379682857,\qquad
\det\bar A_{43}=267072587.
\tag{6}
$$

旧报告没有保存第 43 行的 42 个旧列单独值。本次没有补评这些值；式 (5) 的两个已存多项式已经支付下一步所需的全部旧残差查询。

## 3. 隐式 43 枢轴对应的真实有理泛函

令 $e_{42}(X)$ 是旧 42 个查询对任意目标 X 的值列，$r_z(U)$ 是查询 z 对旧 42 列的行。定义

$$
L_z(X)=e_z(X)-r_z(U)A^{-1}e_{42}(X).
\tag{7}
$$

由 (6)，真实有理数 $L_e(D_0)$ 非零。于是

$$
\boxed{
\Lambda_z(X)=L_z(X)-\frac{L_z(D_0)}{L_e(D_0)}L_e(X)
}
\tag{8}
$$

在 $\mathbb Q$ 上湮灭全部 43 个比较列。式 (8) 是真实泛函定义，不能把下节模数的整数 lifts 当作它的有理系数。

本次新原评价只包含：

1. $X=J_6$ 的两个完整模式；
2. 解 $\bar A\bar c_X=\bar e_{42}(X)$ 后，先把旧 42 原根按整数代表合并，再评价这个**单一整体和**的两个模式。

记新第一残差为

$$
\bar R_X=\overline{X-\sum_j\widetilde c_{X,j}U_j}.
$$

实际检查其旧 42 个枢轴值全部为零。然后直接使用已存的 $\bar R_D$，取

$$
\bar a=\frac{\bar R_X(e)}{\bar R_D(e)},\qquad
\bar E=\bar R_X-\bar a\bar R_D.
\tag{9}
$$

式 (9) 在旧 43 个枢轴全零，并且对每个新查询 z，$\bar E(z)$ 恰为式 (8) 的模 $p$ 约化。理由是全部新旧原式分母在 $p$ 处可逆，$\det A$ 与 $L_e(D_0)$ 的约化也都非零；所以有理坐标和分式可在局部环 $\mathbb Z_{(p)}$ 中运算后约化。

若把原 43 枢轴矩阵记为 $A_{43}$，再依次添加 X 列和 z 行，则标准 Schur 恒等式给

$$
\det\bar A_{44}=\det\bar A_{43}\,\bar E(z).
\tag{10}
$$

这没有要求在本次显式恢复缺失的旧额外行。

## 4. 本次非零原式见证

实际沿用 R136/R153 的同一固定实 profile 对。令 $t=\xi-2$，在 $[0,1]$ 上取

$$
f=[t(1-t)]^8,\qquad g=f(1+2t+3t^2+5t^3),
\tag{11}
$$

区间外零延拓。共同 signed 右原函数为 $I(F)(\xi)=\int_3^\xi F$。此对为 $C^7$；本次所有输入原根的最大 jet 阶数实际为 4。计算使用同一对 $q=f+ig,\bar q=f-ig$、同一右锚及同一原 DAG，没有逐列改 profile。

新目标与整体旧和的原多项式次数最多为 74。第一和第二残差的 pure 模多项式均为零，mixed 模均为 68 次；pure 的模零本身没有被当成普适 pure 身份。

实际标量为

$$
\bar R_X(e)=487272480,\qquad
\bar a=1219312013.
$$

在同一对 profile 的新查询

$$
\boxed{z=(\text{相位 }-2,\ \operatorname{Re},\ t=1/35,\ \xi=71/35)}
\tag{12}
$$

处，读取到

$$
\bar R_X(z)=1121319960,\qquad
\bar R_D(z)=1786090316,
$$

以及严格非零

$$
\boxed{\bar E(z)=1266268570\ne0.}
\tag{13}
$$

故

$$
\boxed{\det\bar A_{44}=1176345646\ne0.}
\tag{14}
$$

该 z 是最多 69 个不同有理点的确定有限网格中的第二个点。原第一个点正是 e，已由 (9) 消去。只增加查询位置，没有引入第二对 profile；也没有重新评价旧 42 单列。

新的两个最终模多项式完整系数对象 SHA256 为

~~~text
4b6d73d04c75f803183b30dda9ae7d8b0d62f273d77b1c65407f39350f498d81
~~~

其中 mixed 68 次多项式 SHA256 为

~~~text
e6413ad06d385895f506231eb1ca826b28f1e74e3abfcacb82cd2e4869dbffcd
~~~

全部新遇到的 83 种有理分母都通过模可逆检查；旧分母证书随原 R153 回执消费。模运算是准确运算，不是浮点近零判断。

### 4.1 也排除真实实系数成员

若假设 $J_6\in E_D$ 仅给实系数，旧 43 个查询的有理可逆矩阵已经迫使该坐标等于其唯一的有理解。因此其约化必须是本次求得的模坐标，而新第 44 行与 (13) 矛盾。故 (1) 同时排除 $\mathbb Q$ 和 $\mathbb R$ 的成员关系。

原式由有限次乘法、至四阶 jet、同右锚积分组成，在共同紧区间的 $C^4$ 拓扑连续。式 (11) 的端点消失阶为八，先在端点作平滑截断、再平滑化，可在右锚 3 固定不动的情况下，取得支撑严格位于 $(2,3)$ 的光滑 $C^4$ 近似。充分接近时同一真实 44 子式仍非零；选定这一对近似后，两 profiles 在 3 附近有共同的零 collar。因此这也排除了全部光滑 profiles 上的普适原式身份，不是只在某个低正则测试输入上的形式失败。

本次原对没有预先配平三矩；不能把它直接称为合法三矩圆，更不能据此排除所有圆、一般有限等距族或主课题的曲面。另作三矩补全须准确保留 R86 的共同区间与左 reserve 假设。

## 5. 完整纯零核及 faithful balanced 像

R160 已在原 $\mathbb Q$ 代数上证明

$$
(J_6)_{-4}=(K_6)_{-4},
$$

$$
K_6=-\frac{C_0}{64}-\frac{C_{88}}{64}-\frac{C_{41}}{128}
-\frac{C_{73}}{32}-\frac{5C_{81}}{128}+\frac{C_{193}}{256}\in R_{-2}.
\tag{15}
$$

此处是真正的普适 pure 原式身份，不依赖本次 pure 模多项式为零。

令

$$
H_6=J_6-K_6,\qquad E_6=E_D+\mathbb RJ_6.
$$

由 (1)、(15)，$H_6$ 是不属于 $E_D$ 的纯零向量，且

$$\dim E_6=44.$$

[R157](R157-general-pure-D0-identity-and-34-dimensional-zero-pure-kernel.md) 已证明 $\dim\pi(E_D)=9$；新增 J6 的 pure 像已在同一响应像中。因此

$$
\boxed{
\dim E_6=44,\qquad \dim\pi(E_6)=9,\qquad
\dim(E_6\cap\ker\pi)=35.
}
\tag{16}
$$

[R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 的 $\Xi$ 对 universal pure-zero canonical 函数单射，遂有

$$
\boxed{\dim\Xi(E_6\cap\ker\pi)=35.}
\tag{17}
$$

旧响应纯核及其 balanced 像仍恰 31 维。$N^3G,J,D_0,J_6$ 在完整权 $-2$ 商中给四个独立的新方向；用各自已付 pure 响应校正后，它们给 (17) 中超出响应纯核的四个独立类。本次没有重算旧 31 条关系或物化新的 35 列 balanced 基。

## 6. 全空间维数与正性边界

[R149](R149-ninth-G-membership-and-exact-nine-dimensional-orbit-quotient.md) 已证明 $A_G/R$ 恰九维、各权为 $1,0,\ldots,-7$，并有 $\dim R\ge228$。它在权 $-2$ 上只有 $[N^3G]$ 一个新类。因为 J、D0、J6 都是真权 $-2$，(1) 和已有分离证明

$$
\dim(U/A_G)\ge3,
$$

从而

$$
\boxed{\dim U\ge228+9+3=240.}
\tag{18}
$$

J6 的非成员不产生有符号实现；已付 lineality / 真实共同查询仍至少 237，不能由 (18) 改成 240。

对 R141 的权 $\sigma=-2$ 正字符，$c_0=\lambda J_6$ 仍是未支付的正性变量，PSD 门仍须保留。不能把 (1) 的模数读成 $c_0$ 的实数符号，也不能推 $c_0=0$ 或 $b_1=0$。

另一方面，(1) 只排除了已明列的比较空间。它没有排除 $J_6\in R_{-2}+NU_{-1}$；该成员门才直接关系到所有平移不变、权 $-2$ 字符是否必须杀掉 J6。因此后继完整字符头部仍须保留正确的低阶八矩修正，不能把本次完整 R8 非成员误当字符头部已非零。

## 7. 实际执行、保留原式与来源

公开 lane：`J6_implicit43_original_separation`。研究源

~~~text
literature_J6_implicit43_original_separation.py
49848 B
ae375c1aadf18538638c77e5224c3b0aec5e16e63daf0cd44d366bda22ae9bc8
~~~

先行 13 项人工检查全部通过；实际运行完成时间 3.984280618 秒，峰值 RSS 100.52734375 MiB。新评价仅 J6 和一条旧 42 根整体和；没有旧单列/缺失额外行补评，没有旧 D0 残差原式重评，没有旧 forcing/响应编译，也没有重复 R161 NF。

由于 (13) 已非零，本次没有触发模全零后的有界有理重构分支；没有求得或宣称任何有理成员系数。

公开目录为

~~~text
notes/actions-43663137188-1-J6_implicit43_original_separation/
~~~

| 文件 | 保存字节数 | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43663137188-1-J6_implicit43_original_separation/J6-implicit43-original-separation.json) | 57174 | `f152cfdf92bdfa1b2573cd7a65d4db2aaa563c126ecd8f396f6620126fad8028` |
| [receipt](../notes/actions-43663137188-1-J6_implicit43_original_separation/receipt.json) | 38495 | `5621a14b8caca6a8a621595073a4d0b81c82076841ff2c973116e08f048af747` |
| [人工报告](../notes/actions-43663137188-1-J6_implicit43_original_separation/J6-implicit43-development.json) | 34727 | `34864767349c3d9374623da3e746bf4cdbe04b35eb0f02b9288173808f674e8f` |
| [完整报告 gzip](../notes/actions-43663137188-1-J6_implicit43_original_separation/J6-implicit43-original-separation-complete-report.json.gz) | 39600 | `3c20b09aa65aab3dd4d047d19621fb65c711e22b4d8e7bb52a679259fdc25975` |
| [十个原根 gzip](../notes/actions-43663137188-1-J6_implicit43_original_separation/J6-implicit43-original-separation-original-residual.json.gz) | 135334 | `5563bacb42191c2506932c2282614944c3b13bc7b6907cf1fa7c7bd4f3866a2d` |

完整报告解压为 125219 B，SHA256 为
`a34adbd9a37cc51301ebc481afef7fe7f1506edc8140b38127f98957e68c2b18`。
十原根导出解压为 540738 B，SHA256 为
`9f6edbcfbc1976e78accdae4703a8927125652fb07e315e94208e2a828f29053`。

该导出保留 J6、旧 42 整体和、第一残差、旧 D0 残差以及最终整数-lift 残差的两个模式。最后一类的整数参数仅用于模约化；导出明确不把它们标成真实有理成员坐标。完整报告保留全部新 42 个值、模坐标、同一 profile 定义、原矩阵、全部新模多项式和有理泛函定义，足以按原算法复现证书。

receipt 列出 182 个来源文件，并记录发布前真实 pull 从研究源到 `8114c2cb3be9ad3097a0cba827e9581218a37e5a`，双 README 未变。研究源身份仍是本稿开头的 `0700d815…`，不把发布时更新后的 HEAD 当作研究输入源。
