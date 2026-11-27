# R150：Q=1−u 边界的整条 H=(2u−1)ell+u=0 权线排除

**状态：已证明。** 在原 unit 2+1+1 非零孤立均值图、共同规范 p+q=2 中，
$$
Q=1-u,\qquad (2u-1)\ell+u=0
$$
不可能成立。本稿保原全部 mean/N/P 必要式的同一 Gram 来源，不要求原两线行列式 Delta 非零，也不假设 W=0。一般 Q=1−u 的 H 非零余支仍开放；普通 Hilbert ISP 未完成。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。日期：2026-11-27（台北）。

## 1. 已付边界、原单位与同一 Gram

原 Frobenius 代数、正确双点乘法及同点原 Gram 的定义沿用
[原y=1边界证明](R150-appendix-unit211-Q1minusU-singleton-mean-y1-exclusion.md)。
特别
$$
r^2=u,\quad p=1+r,\quad q=1-r,\qquad
b=\ell/2+(u-\ell)r/(2u),\quad c=\bar b,
$$
$$
X=x+yr,\quad Y=x-yr,\quad
M=\ell(2u-\ell Q)-u^2=4bcu.
$$
这里 y 是 singleton 均值的奇部系数。此前整个 Q=1−u、y=1 支已经排除，故本稿可用 y−1 非零。

令 d=2u−1、k=4u−1。H=0 和 u≠0 首先给 d≠0，并且
$$
\ell=-u/d,\quad
M=-u^3k/d^2,\quad
bc=-u^2k/(4d^2),\quad
P_{02}=uk(u-1)^2/d. \tag{1}
$$
所以原已付条件给
$$
u(u-1)dk\ne0. \tag{2}
$$
没有在 (1) 中另丢一个权重或 P0 零纤维。

仍用原
$$
R_t=\frac{u}{2bc}\left(EBo+\frac{u-\ell Q}{u^2}EBe\right),
\qquad R_y=-EBe+\ell R_t/2.
$$
它们与原两条 singleton 均值等价。在一般 Q=1−u 图上，[t]Ry=u(y−1)；在 H=0 上完整原式进一步为
$$
R_y=(y-1)\{u(t+2y)-2x+1-u\}. \tag{3}
$$
(3) 可直接由同一原 Gram 展开；它不是最高齐次项的近似。由已付 y−1 与 u，整个余支准确恢复
$$
t=\frac{2x+u-1}{u}-2y. \tag{4}
$$
此处只逆原 u，未逆 x 的任何新首项。

自含源以 (1)、(4) 重建原 f、lambda、T、K；保整个 r²=u 的二次代数。它逐项核验原 E0、N0、P1、f=tau(D_K1)/2 及 P02。所有后续分母逐项检查只含 (2) 中单位。

## 2. 原均值与 N1 的两个小二次式

定义
$$
F=x^2-(u+1)x+\frac{u+1}{4}
  +u(2u+1)y-2uxy,
$$
$$
G=x^2-\frac x2-4uxy+uy^2
  +\frac{u(4u+1)}2y-\frac{u(2u-1)}2.
$$
从同一个完整 Gram 准确得到
$$
E_1=\frac{2k(u-1)}{d^2}F,\qquad
R_t=-\frac{4(u-1)}{u^2}F,\qquad
N_H=\frac{4u(u-1)^2k}{d^3}G. \tag{5}
$$
各前因子由 (2) 非零。因而本图的全部三条剩余均值和原 N1 条件恰由 F=G=0 表达。式 (5) 已在实际自含源中逐项乘回；它没有把原 U 矩或剩余 N/P 宣称为这些两式的后果。

作准确原组合
$$
L=4(G-F)=a(y)x+b(y),
$$
$$
a(y)=4u+2-8uy,\qquad
b(y)=4uy^2-2uy-4u^2+u-1. \tag{6}
$$
这里不除 a(y)，尤其 a=b=0 的纤维始终保留。

## 3. 原加权 N/P 与不除首项的 x 消去

令原最高、第二梯度的加权行 NS、PS 如前一稿第 2 节：
$$
N_S=bN_4(k_B)+cN_4(k_C)-2\lambda P_{02}(\ell+2T+A),
$$
$$
P_S=bP_2(k_B)+cP_2(k_C)-P_{02}(\ell+3T+3A+B),
$$
A=2lambda²−2lambda+1，B=4lambda³−6lambda²+3lambda−1。

它们来自原三矩及全部 singleton N/P 的准确线性组合，所以任何原点都满足 NS=PS=0。源按正确双点乘法直接构造这些原式；同一个 r、f、lambda、T、t 在全部行中保持不变。

对任意
$$
J(x,y)=\sum_{i=0}^nJ_i(y)x^i
$$
定义完整齐次返回
$$
\mathcal L(J)=\sum_{i=0}^n J_i(y)(-b(y))^i a(y)^{n-i}. \tag{7}
$$
若 J=0 且 ax+b=0，则 (7) 为零，包括 a=0 的情形。源对 F 用完整 x 次数 2，对 NS、PS 用完整 x 次数 3；未除 a，也未丢任何 x 首项零纤维。

把各返回的有理 u 分母清除后，只剥已付 u、u−1、d、k 的共同因子，所得三个 y 多项式记为 Fhat、Nhat、Phat。精确范围为：

| 返回 | y 次数 | u 次数 | 清除分母 | 移除内容 |
|---|---:|---:|---|---|
| Fhat | 4 | 3 | 无 | u |
| Nhat | 6 | 9 | d⁴ | u |
| Phat | 6 | 9 | d⁴ | u |

Fhat 可取
$$
\begin{aligned}
\widehat F={}&-1+11u-24u^2\\
&+(-20u+56u^2+32u^3)y\\
&+(44u-144u^2-64u^3)y^2\\
&+(-32u+96u^2+128u^3)y^3\\
&+(16u-64u^2)y^4.
\end{aligned}
$$
其 y 首项 16u(1−4u) 由 (2) 非零。其余两式由 (7) 和原 Gram 唯一确定，源直接重建，不依赖任何外部 JSON。

## 4. 两个真正 QQ 结果式的严格整数重建

将 Fhat、Nhat、Phat 的有理内容分别乘常数 1、4、8 变为整数多项式。构造完整 y 次数 4、6 的两个原 10×10 Sylvester 矩阵：
$$
R_N(u)=\operatorname{Res}_y(\widehat F,4\widehat N),\qquad
R_P(u)=\operatorname{Res}_y(\widehat F,8\widehat P).
$$
常数内容不改变零点。两者的先验 u 次数上界都是
$$
6\cdot3+4\cdot9=54.
$$

本次没有从模多变量单位判 QQ 空集，也没有猜测有理重建。源先给整个整数 determinant 的严格系数界。若 L_F、L_J 是两个整数输入的全部系数绝对值之和，则由 determinant 的置换展开
$$
|\operatorname{coeff}_{u^j}R_J|
\le L_F^6L_J^4=:B_J. \tag{8}
$$
这是所有行系数范数乘积的直接上界；不依赖一般位置或数值估计。

对每个素数 p>54，在 u=0,...,54 上计算完整固定次数 Sylvester determinant，逐点高斯消元的每次非零常数逆均乘回。用完整 55 点 Newton 插值恢复模 p 的多项式，逐点再次代回。最后以 CRT 合并，模数积严格超过 2B_J 后才取唯一的有界整数系数。故所得是原整数 determinant 本身，而非候选投影。全部点的 y 首项退化都仍由固定 10×10 矩阵处理。

| 原结果式 | 严格系数界 B | CRT 模数积 | 实际次数 |
|---|---|---|---:|
| RN | 122305947211024212459180083072463220506624 | 17000404569331243624069340506514978245081217 | 53 |
| RP | 84266836609803328162381070076329177612550144 | 3383080509296917481189798760796480670771162183 | 53 |

RN 使用从 101 到 197 的连续 20 个素数；RP 增加 199，共 21 个。模积分别为 144、152 bit，系数界分别为 137、146 bit。所有插值、CRT 约化和最终系数界逐项检查。

完整整数系数数组的 SHA256 分别为：

- RN：dbb8d30ea4c685c0e1eac5d2112d552ea38861d82fbfd648499f5df54598bb7f。
- RP：011687f70673d5f10baf15e9b7c933b12ceed5349500342be1175e4ec9091daf。

## 5. 完整 QQ gcd 只余三次参数域

在上述两个**完整整数多项式**上作整数 primitive PRS。每个伪余步是
$$
R_{\rm new}=\operatorname{lc}(B)R-\operatorname{lc}(R)u^jB;
$$
随后只除非零整数内容，并逐系数乘回。因这些步骤均在 QQ[u] 保持 gcd，末非零 primitive 项准确给 QQ gcd。实际次数轨迹由 53、53 逐次降至 27、26，下一余项为零。

最终准确因式为
$$
\gcd_{\mathbb Q[u]}(R_N,R_P)
\doteq u^4(4u-1)^4D(u)^6,\qquad
D(u)=16u^3-4u^2+2u-1. \tag{9}
$$
源把 (9) 的全部因子乘回，并将完整 RN、RP 各自除以右侧后再次整项乘回。u 与 4u−1 已由 (2) 支付，任何原点只可能满足 D(u)=0。

注意：此时不能直接断言 a=b=0。下节实际返回所有 y 根，再返回原 x 条件。

## 6. 整个三次代数中的同根两层返回

进入完整
$$
\mathcal K=\mathbb Q[u]/(D).
$$
不选择复嵌入。u、u−1、2u−1、4u−1 在该代数中均为单位；可由 D 在 0、1、1/2、1/4 的值 −1、13、1、−1/2 直接看出。计算中每个被逆元素仍用 QQ 扩展 Euclid 构造实际逆并乘回 1。

先在 K[y] 对 Fhat、Nhat、Phat 作完整原返回。两次扩展组合准确给
$$
\gcd_{\mathcal K[y]}(\widehat F,\widehat N,\widehat P)
=\{y-(4u^2-u+1)\}^2. \tag{10}
$$
这不仅保留三次 D 的全部根，也保留共同 y 的全重数。由 D=0，
$$
4u^2-u+1=\frac{2u+1}{4u}.
$$
因此每个原点必须取同一
$$
y_0=(2u+1)/(4u).
$$
这时 (6) 确实有 a=b=0；是 (10) 证明其为唯一原候选 y，而不是事先删去其它 y。

将这个 y0 返回**原 F、原 NS、原 PS**。其中原 F 的准确二次式为
$$
4F=4x^2-2(4u+3)x+4u^2+5u+2. \tag{11}
$$
在完整 K[x] 中再作两次扩展组合，准确得到
$$
\gcd_{\mathcal K[x]}(F(x,y_0),N_S(x,y_0),P_S(x,y_0))=1. \tag{12}
$$
(12) 返回的是原同点式；没有仅在各自范数或不同嵌入上验证。全部两层返回共检查 55 个系数逆、12 条多项式除法、4 条完整 Bezout 组合，均实际乘回。任何复根 u of D 对这些恒等式求值，都得到原 x 不可能存在。

故 y≠1 支排空；合并先前已证整个 Q=1−u、y=1 排除，H=0 整权线全部排除。

## 7. 自含源、实际执行和未完成探针

源：[2026-11-27-unit211-Q1minusU-Hzero-original-CRT-return-8542.js](../notes/2026-11-27-unit211-Q1minusU-Hzero-original-CRT-return-8542.js)；[小执行回执](../notes/2026-11-27-unit211-Q1minusU-Hzero-original-CRT-execution-8542.json)。

- 自含源 21780 字节，SHA256 50a9b96bc3437aeaf9b768dfabcaee0098bfc539e009cd70b3b32df00fdef8a4。
- 已在纯 V8 中完整实际执行，源内 1430 ms；无第三方库、无本地文件或 scratch JSON 依赖。也可直接用 Node 执行。
- 从原 Gram、全部低次身份、严格整数 CRT 到两层 K 返回均在同一完整执行中通过。
- stdout 为 1812 字节；SHA256 f3a6eec3da47df9547ecea738fb609fa597860c7a63ffc8a4d8cfed8c5e99797。
- 小回执记录实际纯 V8 环境；没有伪装成本地终端或 GitHub Actions run。

在它之前，纯 V8 的直接 Q(u) 欧氏结式探针因分式系数增长被主动终止，未得到完整结式；随后完整 CRT 已返回但朴素 QQ 系数 gcd 未完的单元亦被主动终止。两者均未被当作成功，也未给不存在的源文件/SHA。最终采用上面的有严格界整数 CRT 与 primitive 整数 PRS，原输入和全部固定次数不变；当前完整源是独立完成的实际证明。

本结论只支付 Q=1−u 上的 H；一般 H≠0、y≠1 仍须回全部原条件，不由本稿推断空。
