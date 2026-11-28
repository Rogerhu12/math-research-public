# 新输入：完整 Vlow 的第二纯权支持及两个固定坐标方向

日期：2026-11-28（UTC）。首次执行前输入，无新实际回执。

唯一源码：2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py
blob：079cc6744ab5ac9d95cc9ea649d94e7a34af9f3c  
SHA256：060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7；19677 字节。
预算：120 秒、1 GiB；建议外层 135 秒。绝对截止钳制所有嵌套 alarm 和 setitimer；只输出次数、SHA 和小回执，不保存系数载荷。

## 1. 真正新目标与完整原来源

当前正确 Phi、distinct singleton、物理 D 非零图中，已刊原身份给：

- 全图六原式的 $t$ 六次 $C_6$，包含原 N1 斜率两条整零曲线；
- 加入完整原孤立值式 $V_{\rm low}$ 后的 $t$ 八次 $C_{8,N}$；
- 旧正确原十五列模型给两个 $\lambda$ 六次，它们的固定 12 阶 Sylvester 行列式 $F$ 是非零必要纯权支持。

规范出处：

[全图 t 六次六原乘子](../results/R150-appendix-unit211-Phi-zero-corrected-whole-t-sextic-six-original-multipliers-and-H28.md)；
[完整 Vlow 与两个原八次](../results/R150-appendix-unit211-Phi-zero-corrected-t-complete-Vlow-original-mean-trace-and-two-octics.md)；
[既有固定 12 阶支持与维数](../results/R150-appendix-unit211-Phi-zero-corrected-nonzero-weight-support-and-whole-dimension-one.md)。

本次第一次定义并研究
$$
G(u,Q)=\det\operatorname{Sylv}_t(\widetilde C_6,\widetilde C_{8,N}),
\tag{1}
$$
容量固定为 $(6,8)$；波浪号仅是把系数变为 primitive 整数所需的非零有理常数倍。此前没有执行这个 14 阶投影或它与 $F$ 的整个单变量切片比较。

$V_{\rm low}$ 是
$$
D\ell^2N_4(V_{\rm phys})+\frac{Z_1H}{2m}-\frac{DZ_2q}{M};
$$
它来自完整三个 $Z_i$ 和原矩关系，不是单个分量或 Phi 倍数。只用既有 $m,M$ 权单位；$D$ 只正乘。

这里原 $I_6$ 表示六原式 $(\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS)$。$G$ 是 $I_6+(V_{\rm low})$ 的全权必要支持，尚未预报其非零、与 $F$ 互素或原图排空。

## 2. 四个准确源码依赖与执行边界

四份源码必须先全部核完整 SHA，才执行任何定义前缀。都位于 topic 的 notes 目录：

1. 2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py  
   blob dec77452e4631b4370e72d1b9491da01e35547b3；完整 SHA 0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335。
2. 2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py  
   blob ed0fc44e741f2482f4593b31ab22fa4f773cc241；完整 SHA 39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b。
3. 2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py  
   blob f73a06b941fe6c990c5d22ebf1778f05e7c76c74；完整 SHA 84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0。
4. 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py  
   blob f62e66a27d5c999a54d03631ab8d3b31297e7aa2；完整 SHA 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

t 参数入口仅取第一份在标记
“# Necessary deterministic coefficient/trace definitions only.”
之前的 8247 字节，SHA
84424bf3fe62591fc4f9316b5809d6240cca96fd01cd196f411157c085ef2e1f。
AST 去掉顶层旧断言、审核循环、打印、计时器及时间赋值；原类与系数定义保留。只再生真三均值、其规则、N1 和两条原三次。

此后仅按已定规则的系数递推取得 NS/PS/Vlow 三坐标，不重建旧完整乘子迹或重新核它们的普通原式证明。C6 的两个已定乘子以及第三 N1 系数只为唯一标量定义再生；不重跑六原乘子/分母门。C8 的既成三乘子共同内容为常数 1，直接使用该已成定义，不重做共同 gcd、两坐标返回或两 octic gate。

旧 $F$ 参数入口只取第二份在
“def evaluate_weight(poly,u0,q0):”
之前的 6371 字节，SHA
4e49026df6f798e62370af93c1ff821b698b82011ed797a72137bab24a358b16。
其中已审的两层定义 loader 会读取第 3、4 个依赖，但不进入旧点表选择、旧 fixed12 度证书、单点 gcd 或 144 坐标门。本次不读取历史系数 JSON 或旧日志载荷。

每次嵌套计时器设置都被最初绝对截止钳住，包括 alarm(0)；源码正常结束才恢复真正的 timer 关闭。

## 3. 已定参数身份与常数整化

t 两式的唯一规范 SHA 为
$$
C_6:\quad
5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1,
$$
$$
C_{8,N}:\quad
7be3f86635bb87c309fc15c6b386303624c0ca951e8578dce37d490fc925d3ea .
$$
两式的 $(u,Q,t)$ 次数分别是 $(36,23,6)$ 与 $(60,36,8)$，总次数 44、71。完整 Vlow 三余式的既定三个 SHA 也核回；没有用不同表示偷换输入。

旧 $\lambda$ 两式的规范 SHA 为
$$
fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5,
$$
$$
2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014 .
$$
它们是旧 $F$ 定义的同一对式子。

每式只乘一个非零有理常数变为 primitive 整数多项式。源码完整核 integer·content = original·denominator。这不是倒物理首项或在零面上约原方程；整数化后任意固定素数下的多项式矩阵都有明确原整数来源。

t 参数的必要定义可能暂在函数域写原斜率分母；本次不以该临时分母局部化物理图。已刊全六原式恒等式与精确最终 C6 SHA 已经付清其整零面延拓。

## 4. 固定矩阵与全原 adjugate 身份

14 行依次为
$$
C_6,tC_6,\ldots,t^7C_6,\qquad
C_{8,N},tC_{8,N},\ldots,t^5C_{8,N},
$$
列是 $1,t,\ldots,t^{13}$。记矩阵为 $S_{14}$。普遍恒等
$$
e_0^t\operatorname{adj}(S_{14})S_{14}
=\det(S_{14})e_0^t
\tag{2}
$$
给 (1) 的完整原理想来源，无需实际展开巨大二元 QQ 行列式或 adjugate。两个 t 头的全部零面和次数下降纤维包含在 (2) 中。

行权为前八行 $44+r$、后六行 $71+r$，列权为 $-j$。每个非零原条目都实际核其权总次数上界，故
$$
\deg_{u,Q}G\le 8\cdot44+6\cdot71-48=730.
\tag{3}
$$
旧 $F$ 的同一固定 12 阶定义继续保留总次数上界 444；本次不重复它的非零证明。

## 5. 事前固定两个切片；不删除任何模因子

唯一素数 $p=1009$。事前固定且无后选：

- $Q=2$，保留整个 $u$ 多项式；
- $u=2$，保留整个 $Q$ 多项式。

不根据 gcd、目标、秩或非零性换点、换素数、添加切片。每个方向都计算 $S_{12}$ 与 $S_{14}$ 的完整 $\mathbb F_{1009}[x]$ 行列式。

这些切片用于原整数纯权多项式的系数证据，不是抽取一个物理解。不需要把切片上某个原权单位的每个模零点宣告为空。

尤其：**不剥任何模 paid 因子。** 即使模 gcd 的因子看起来只位于原单位零面，也保留其全部因子与重数；没有 QQ 来源时不能把它们当作已付特征零分支删除。

固定矩阵的 Bareiss 消去每次完整核
$$
\text{new entry}\cdot\text{previous pivot}
=\text{pivot product difference}.
$$
行交换保符号。临时多项式主元只供精确除法，不成为原物理单位。若某列完全为零，则该固定行列式确为零；不改输入继续寻找成功点。

每个方向随后对两个完整单变量行列式作 xgcd，最终两个多项式乘子完整返回真实 gcd。输出仅给 profile/SHA，不输出其系数载荷。

## 6. QQ 次数上界与最高矩阵见证

每个方向先取原二维整数条目在该坐标的真实次数 $d_{ij}$。完整整数 Hungarian 计算给对偶 $a_i,b_j$，逐条核
$$
d_{ij}\le a_i+b_j,\qquad
B=\sum_i a_i+\sum_jb_j.
$$
另用所选完美匹配核同一 $B$，所以它是原行列式的严格 QQ 次数上界。零条目是禁用边，不误作零次非零条目。

若 $x$ 为当前方向，令
$$
H_{ij}(y)=[x^{a_i+b_j}]S_{ij}(x,y).
$$
则 $u^{-a_i}$ 一类 Laurent 行列尺度只用于估值证明，
$$
[x^B]\det S=\det H(y).
\tag{4}
$$
在事前固定的另一坐标值 2 和素数 1009 上，源码对 $H$ 作完整有行变换返回的数值消去。只有 $\det H(2)\ne0$ 才付：

1. 原 QQ 行列式对 x 的全局次数恰 $B$；
2. 该固定有理切片保 x 次数；
3. 再模 1009 同样保度且首项为单位。

同时把完整模单变量行列式的最高系数与该见证核对。若最高矩阵奇异，只记保守上界和实际模次数，不由后者反推 QQ 真次数，也不提高精度重启这个门。

## 7. 两个方向为何都需要

若 $Q=2$ 方向的模共同 gcd 为 1，而且至少一个支持的全局 u 度/切片/模度经 §6 保留，则不存在正 u 次数的 QQ 公共因子。

证明：任意这样的公共因子在 $Q=2$ 必保正 u 度，否则与被见证多项式的首项不消失矛盾。其在 QQ[u] 中的首一公共因子，因为整输入中有一个 p 单位首项，由 p-Gauss 整性可在 $\mathbb Z_{(1009)}[u]$ 中取首一，模后仍保正次数并整除两个模输入，矛盾。

但是这个方向不能排仅依赖 Q 的公共因子。故另用 $u=2$ 的完整 Q 方向，以同样的保度和 gcd1 论证支付它。源码只有两方向的严格条件都实际成立时才写 QQNoCommonCurveProved=true。

若任一方向头取消、共同 gcd 非常数或固定行列式为零，所有相应未付公共曲线/内容都保留。不能以只一条切片、generic gcd 或模 paid 饱和来给全局结论。

如果两方向确实都付清，特征零忠实平坦保证两支持在复数上无共同曲线，才可据 (3) 和旧 444 界给不同权点数至多 $444\cdot730=324120$。这仍不是排空；完整规范坐标与尺度的计数不属于本次输入。

## 8. 确切新旧边界

新数学是：完整原 Vlow 第一次固定 14 阶纯权支持；这条支持与既有固定 12 阶支持的两个完整单变量切片；两个全局坐标次数的真实对偶/最高矩阵；条件严格的 QQ 共同曲线排除。

本次不重跑旧 corrected f62、f73、t 六行/十行、整 ellhalf、全六原乘子、Vlow 原迹/两 octic 证明、旧 fixed12 单点门或任何冻结失败。已证的全权 22 生成只作为后续有限模型背景，没有伪称已取得完整的全权乘法表。

所有实际返回以唯一首次的内层结果为准。资源触界后只保最后完整 checkpoint，不能扩大预算、换切片、调整顺序或重跑同一目标。
