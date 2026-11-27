# 原 full47 的五级 Riemann–Roch 乘法来源

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明的有限认证方法；实际乘法空间尚待公开回执。**

本请求只新读取原曲线 $X=X_{\rm ns}^+(47)$ 的
$\mathcal L^2,\ldots,\mathcal L^5$ 产品基。原
$\mathcal L=\Omega^1_X(C_\infty)$、$g=73$、
$\deg C_\infty=23$、$\deg\mathcal L=167$
及95元整来源均消费 R1090，不重搜旧候选、旧 Hodge 秩，
不重算 CM 首对数、高度或辅助点筛选。

## 1. 同一原尖点上的完整可证坐标

R1090 固定 $\zeta_{47}=2\in\mathbf F_{4513}$ 和真实 Tate 参数
$t=q_{\rm Tate}^{1/47}$。其95个原 weight-two Reynolds sections
在标准尖点的局部表示是
$$
s_i=F_i(t)\,(47\,dt/t).
$$
$47\,dt/t$ 是 $\mathcal L$ 的整单位局部标架。
因此乘积的原局部表示准确是 $F_iF_j$ 等，
没有额外的 $47$、Cartier或CM period因子。

对 $1\le n\le5$，若 $s\in H^0(X,\mathcal L^n)$
在此标架下的836项全部为零，其零除子在该原点的次数至少836。
但非零截面的零除子次数恰为 $167n\le835$，矛盾。故
$$
H^0(X,\mathcal L^n)
 \longrightarrow \mathbf F_{4513}[[t]]/(t^{836})
\quad\text{单射。}
\tag{RR.1}
$$
只用一个真实原尖点；乘法后统一模 $t^{836}$ 是同一标架中的实际乘法。
不把稀疏Tate指数当成粗参数。

因 $167n>2g-2=144$，Serre 对偶及 Riemann–Roch 给
$$
\dim H^0(\mathcal L^n)=167n+1-73.
$$
五个准确目标维数依次为
$$
95,\quad262,\quad429,\quad596,\quad763.
\tag{RR.2}
$$
只在新实际产品达到对应维数后才登记完整空间。
不以“正常生成应成立”代替实际有限秩。

## 2. 保原95来源的有限产品算法

按已认证95个 descriptor 和其哈希重建原168 jets、
23个留数及73维Hodge核。然后只延长同一来源到836项，
核前168列与旧来源逐项相等；不重开旧候选搜索。

令 $B_1=(F_1,\ldots,F_{95})$。
对 $n=2,\ldots,5$，按固定顺序遍历
$$
fF_j,\qquad j=0,\ldots,94,\quad f\in B_{n-1}.
\tag{RR.3}
$$
$n=2$ 时省去对称重复对。
以95项为一个批次，将旧独立行与新实际产品一起取 transpose-pivots。
旧独立前缀必须全部保留；rank若超过 (RR.2) 则失败，达到目标即停。

每一保留行仍是实际产品，未被行消元的线性组合替换。
runner内保留它在 $B_{n-1}\times B_1$ 中的两索引。
所以以后在任一点或局部jet评价 $B_n$，
只须从同一95个原section的值按产品索引递推。
未借另一曲线的embedding或modular-symbols坐标。

若有限候选或预算内没有达到目标，只报告完成的级数。
成功时 (RR.1)、(RR.2) 及原section来源证明：
这些产品构成真正 $H^0(X_{\mathbf F_q},\mathcal L^n)$ 的基。
它们由原整section相乘而有整lift；
相同大小的模$q$单位minor与 $H^1(\mathcal L^n)=0$ 的base change
再经Nakayama给 $\mathbf Z_q$ 上整基，未任取不合法的lift。

## 3. 全部23个cusps与实际微分空间

原95个section在第$b$个尖点的值是
R1090留数矩阵第$b$行除以47。
沿 (RR.3) 递推全部产品值，得到每一级的真实
$23\times(167n-72)$ 评价矩阵 $E_n$。

对 $n\ge2$，
$$
\mathcal L^n(-C_\infty)
 =\Omega_X^1\otimes\mathcal L^{n-1},\qquad
\deg\mathcal L^n(-C_\infty)=167n-23>144.
$$
故完整23项评价全满秩，准确核维是
$$
239,\quad406,\quad573,\quad740
\qquad(n=2,3,4,5).
\tag{RR.4}
$$
消费者实际求该核并核 $E_nK_n^{\mathsf T}=0$。
不能只去掉标准尖点常数或用总留数零代替全部23条件；
总留数关系仅适用于 $n=1$ 的真微分，不自动适用于高次section。

特别得到
$$
U=H^0(\Omega_X^1\mathcal L^2)
 =H^0(\mathcal L^3(-C_\infty)),\quad \dim U=406,
$$
以及
$$
W=H^0(\Omega_X^1\mathcal L^4)
 =H^0(\mathcal L^5(-C_\infty)),\quad \dim W=740.
$$
这是后继真第三类微分的有限来源，不是已经求出的微分。

## 4. 后继colon运算与准确限制

设 $S$ 是 Galois 稳定的约化有效除子，$\deg S\le159$，
并已由真实粗参数支付全部支撑。此时
$\deg\mathcal L^2(-S)\ge175>2g$，所以该线丛全局生成。
取 $h,w\in H^0(\mathcal L^2(-S))$。
若它们作为 $\mathcal L^2$ 截面的公共零除子恰为 $S$，则
$$
\{F\in U:Fw\in hU\}
 =h\,H^0(\Omega_X^1(S)).
\tag{RR.5}
$$
在 $S$ 外，$h,w$ 无公共零，$Fw/h$ 正则迫 $F/h$ 无极；
在 $S$ 上公共零最小阶恰一，同一条件迫 $F/h$ 极阶至多一。
反向若 $\eta\in H^0(\Omega^1(S))$，
则 $h\eta,w\eta\in U$，给所述等式。
全部乘法只进入 $W\subset H^0(\mathcal L^5)$，由836项原jet认证。

若额外公共零除子为 $D$，基点消去后的两section exact sequence给
$$
\dim(hH^0(\mathcal L^3)+wH^0(\mathcal L^3))
=763-\deg S-\deg D.
\tag{RR.6}
$$
其kernel是 $\mathcal L(S+D)$，次数大于144，故 $H^1=0$；
codomain为 $\mathcal L^5(-S-D)$，次数仍至少501，
其 $H^1$ 亦零。因此达到 $763-\deg S$ 即证明无额外公共零。

(RR.5) 的实际留数条件、Cartier固定修正、
八个点的曲线评价、Miller函数及最终QC行秩
均非本请求执行内容；这里只认证其原乘法来源。

## 5. 公开执行、复用与保存

固定官方SageMath10.6 image digest；仅本公开仓库Actions执行。
预算900秒、预留30秒，到预算保实际完成级数。
检查实际HEAD、两README、来源/方法/请求SHA、
原Hodge证书及固定参数。

输出每级维数、考察项数、最后source索引、
产品索引/原836矩阵/全cusp评价和核的SHA-256。
原矩阵、级数、产品索引只留runner内，不提交或上传artifact/Release。
后继可调用确定性 build_graded_source 作为输入重建并核完整certificate，
不宣称重新认证旧结论；新的RR操作另给范围和回执。

来源：R1090的原整 $\Omega(C_\infty)$ 及95元Reynolds来源，
R1078的原genus73与23个cusps。
本文的degree单射、RR维数、整lift、完整cusp核与colon身份均已直接证明。
