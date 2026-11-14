# R735：原 p41 正 CM 椭圆模型的精确七次系数证书

日期：2026-11-14。状态：**已在公开仓库 Actions 完成并由精确恒等式认证。**
本结果首次将 R725/R728 原目标模型的系数 $b$、其次数七数域和
Néron 逆不同落实为完整代数数据。原 $X_1\to C$ 的函数、
原 $\beta$ 坐标及高度仍未生成，不能从本结果外推这些对象已算出。

## 1. 原模型与实际公开来源

始终固定
$$
p=41,\qquad E_{27}:y^2=x^3+16,\qquad
t=-x/y,\qquad s=\sqrt{-3}.
$$
对原非零 $41$-挠点 $P$，用 R725 的同一函数
$$
w(P)=\prod_{a\in\mathbb F_{41}^{\times}}t([a]P),\qquad
r_0=\frac{w(P)-w([s]P)}2,\qquad b=r_0^6.
\tag{735.1}
$$
故实际正 $\kappa_4$ 分量仍是
$$
C:\ y^2=x^3+b,\qquad L^+=\mathbb Q(b),\quad L=K(b).
\tag{735.2}
$$
本次未选一个方便的六次扭曲来替代 (735.1)。

真实执行为公开仓库
[run 43608152850](https://github.com/Rogerhu12/math-research-public/actions/runs/43608152850)，
源提交
`ff405af51e13bb966fecd066a14513eee0947702`，
2026-11-14 15:08:07 UTC 完成，进程退出码零。
核心精确算术耗时约 $226$ 秒。所有新算术均在该次公开 Actions 内，
未重算任何旧 41 层点分类、旧 M2 或旧群链。

固定源程序
`R732_p41_original_CM_model.py` 的 SHA256 为
`4d6f860506347ab578f1a4f0e30eb0041f8a56b6e62b29762aa958c843f17ec5`。
完整小证书是
[p41-original-CM-model-certificate.json](../computations/R732-p41-original-CM-model/43608152850-1/p41-original-CM-model-certificate.json)，
19620 bytes，SHA256
`752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574`。
下文的系数、迹与逆不同均指该一份不可混淆的证书。

## 2. 完整除法商代数及原系数的准确表达式

设 $\psi_{41}$ 为 $E_{27}$ 的原除法多项式。程序从完整除法递推生成它，
其次数为 $840$。利用所有指数均为三的倍数，置
$$
U=\frac{64}{x(P)^3},\qquad
P_0(U)=\sum_{j=0}^{280}
 [x^{840-3j}]\psi_{41}(x)\left(\frac U{64}\right)^j.
\tag{735.3}
$$
将 $P_0$ 首一化得 $P(U)$。真实运行已完整核准
$\deg P=280$、可分及 $41$-Eisenstein；以下在同一
$\mathbb Q[U]/(P)$ 中作精确运算。

对 $1\le a\le20$，原倍点公式给
$$
x([a]P)=x(P)\frac{A_a(U)}{B_a(U)}.
$$
三次权重分拆和 $x^3=64/U$ 的代数替换给出的 $A_a,B_a$
无浮点或拟合。令
$$
W=\prod_{a=1}^{20}
 \frac{A_a^2B_a}{4A_a^3+UB_a^3},
\qquad
R=\prod_{a=1}^{20}
 \frac{A_a^3+UB_a^3}{A_a^3-2UB_a^3}.
\tag{735.4}
$$
$\pm a$ 配对后，$w(P)=x(P)U^7W/4$。
同一 $s$-三同源准确满足
$$
x([s]P)=-\frac{x(P)^3+64}{3x(P)^2},\qquad
\frac{t([s]P)}{t(P)}
=s\,\frac{x(P)^3+64}{x(P)^3-128}.
$$
因此 $w([s]P)/w(P)=3^{20}R^2$，完整原定义成为
$$
\boxed{
b=\frac{U^{40}}{64}\,
   \left[W(1-3^{20}R^2)\right]^6 .
}
\tag{735.5}
$$
这里 $1/64$ 来自 $x(P)^6=(64/U)^2$ 和 $(1/8)^6$，
不是可自由更换的尺度。全部除法使用扩展 Euclid，
并完整检查逆元乘积在原 $P$ 商代数中等于一。

程序已保存 (735.5) 的全部 $280$ 维有理坐标。
由于这是可重现的大中间数据，它只保留在本次完整 artifact；
仓内保留其准确 SHA，不将大坐标复制入结果文件。

## 3. 原七次多项式、真实重数与完整代入认证

$840$ 个 $x$-根按 $\mu_3$ 合为 $280$ 个 $U$-根。
R725 已证明 $b$ 的次数为七；在上述商代数中，
它的每个共轭准确重复 $280/7=40$ 次。
程序保留这个重数，没有把重复目标当作不同的七次共轭。

设 $a(U)$ 为原商代数中的任意元素。首一可分多项式的
Lagrange 插值给
$$
\operatorname{Tr}(a)
 =[U^{279}]\bigl(aP'(U)\bmod P(U)\bigr).
\tag{735.6}
$$
真实运行计算 $b^k$ 的完整迹，$1\le k\le7$，除以 $40$，
用 Newton 恒等式生成首一七次 $F_{41}(Z)$。

为了避免复制数千位系数造成第二份不一致数据，完整多项式以 §1
证书中的以下准确字段定义：
$$
D=\texttt{minimal\_polynomial.denominator},\qquad
A_i=\texttt{minimal\_polynomial.numerator}[i]\quad(0\le i\le7),
$$
$$
\boxed{\quad F_{41}(Z)=D^{-1}\sum_{i=0}^{7}A_i Z^i.\quad}
\tag{735.7}
$$
字段全为十进制整数，按升幂排列，$A_7=D$；证书亦给每个约分后的
有理系数及全部七个幂迹。特别地，
$$
A_0=-738590338888761344.
$$
这是一份完整精确多项式规格，不是数值近似或仅有特征根的描述。

关键的独立闭合是：程序把 (735.7) **重新代入 (735.5)**，
在原 $280$ 次商代数中完整验证
$$
\boxed{\ F_{41}(b)=0.\ }
\tag{735.8}
$$
又实际得到
$$
v_{41}([Z^i]F_{41})=1\quad(0\le i\le6),\qquad
[Z^7]F_{41}=1,
\tag{735.9}
$$
以及
$$
\boxed{\quad v_{41}(\operatorname{disc}F_{41})=6.\quad}
\tag{735.10}
$$
故 $F_{41}$ 是 $41$-Eisenstein，特别地不可约。
这些准确检查同时认证 (735.7) 是原 $b$ 的最小多项式，
不能只凭七个近似共轭或一次低精度余式取得这个结论。

原实标签同样已固定而不需要猜一个复根：R725 的
$L/K$ 为七次循环扩张，复共轭按反演作用，
故 $L/\mathbb Q$ 为二面体扩张，$L^+$ 的签名是 $(1,3)$。
由原实 $41$-挠点选出的 $r_0$ 为非零实数，$b=r_0^6>0$。
因此 (735.7) 的唯一实根就是原正 $b$；
它与 (735.1) 的标签一致。

## 4. 实际 p 进模型及 Néron 逆不同

令 $F=\mathbb Q_{41}(b)$。由 (735.9)，
$$
[F:\mathbb Q_{41}]=7,\qquad
\mathcal O_F=\mathbb Z_{41}[b],\qquad v_{41}(b)=1/7.
\tag{735.11}
$$
这是次数七的全分歧 tame 扩张。
模型 (735.2) 在归一为 $v_F(b)=1$ 的赋值下为类型 II 最小模型，
原 $\omega_C=dx/(2y)$ 是 Néron 微分。

程序另外在 $\mathbb Q[Z]/F_{41}$ 中精确计算
$$
J(Z)F_{41}'(Z)\equiv1\pmod{F_{41}(Z)}
\tag{735.12}
$$
并将 $J$ 的全部有理坐标保存在
`inverse_different_generator` 字段。
由 (735.9)，$F_{41}'(b)$ 的唯一最低项是 $7b^6$，故
$$
v_{41}(F_{41}'(b))=6/7.
$$
R728 的原 Weil restriction
$B=\operatorname{Res}_{L^+/\mathbb Q}C$
在 $41$ 处的真实余切格因而有完整可计算基
$$
\boxed{
\frac{b^j}{F_{41}'(b)}\,\omega_C,
\qquad 0\le j\le6.
}
\tag{735.13}
$$
原本原六维因子的格仍须按同一 $e_{42}^*$ 投影，
不能把七维 Weil restriction 整体当作原六维商。

(735.13) 固定的是目标模型的真实 Néron 规范。
它未计算原 $J_{X_1}\to A_{\theta,1}$ 到该模型的同源尺度，
因而不宣称原 KS/Manin 比较行列式为 $41$-单位。

## 5. 完整产物、保存与下一实际输入

以下均为本次实际返回的 SHA256：

| 产物 | SHA256 |
|---|---|
| 核心完成凭据 | `92a0771abbdb34c89b42bf053ae01a2f40c9cbc88daca10c57e5ca64549ba967` |
| 完整七次模型小证书 | `752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574` |
| 原 280 维坐标状态 | `9cd5f6731c7cfa76cd118b5f3a8ab1efb12d0d69ba95ab08817fcb80c2073427` |
| 原完整除法模数 | `7063eacd17ffec4c68dea5d8c3a2cab278286653fd12aae07f1c955bb1ad94fb` |

最后两项在
`serre-global-R732-p41-original-CM-model-43608152850-1`
完整 artifact 中。大状态 8386194 bytes 不入 Git；
[完整清单](../computations/R732-p41-original-CM-model/43608152850-1/full-outputs-manifest.json)
把它们与小凭据、规则/源 SHA 及同一 run 对齐。

后续直接使用本次原 $F_{41},b,J$，不重做已完成的除法和迹。
R732 的原曲线闭周期、CM Hodge translate 表、有限周期核、
有理函数与两个 CM places 求值继续推进。当前结果关闭的是
“原 $p=41$ 目标 CM 模型仅有抽象定义、尚无准确系数”这一输入缺口；
原高度外积、共同无根和 Serre 主目标没有因此完成。

依赖：[R725](R725-original-CM-elliptic-model-and-splitting-field.md)、
[R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)、
[R732](R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)，以及
[本次完整方法](../notes/R732-p41-original-CM-model-input-computation.md)。
