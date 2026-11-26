# R1063：原 Hecke 与 Hodge graph 的实际整 MW 消去族

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient，root 复核。

**已证明：原固定完整对数可与一族实际整交错型配对，所得每一行
都消去全部原 Mordell–Weil 对数及其饱和交。**
初始族由真实 split-Hecke 与原 Hodge graph 算子的偶次幂生成；
§9 再用本原负角色块的整因子分解和真实 Hecke 交换子解格扩族，
不反除未知的 bare 核范数。
其最低系数是否含单位，准确等价于一个明确的剩余域轨道正交条件。
因此可以继续整个合法族，而不必预设单个已命名的
$\mathcal C_{\rm actual}$ 为单位。

§7.1 进一步证明该轨道必各向同性，因而不可能满新部。
本篇不证明最低系数理想为单位理想，也不把
任意替换 $\lambda$ 当作有理点来源。原 bare 高系数与全部深盘排除仍开。
全部论证为纸面代数，无数学程序执行。

## 1. 原两行与完整对数

设 $p=6N+5\ge41$，保留课题原 $p\bmod9$ 条件。置
$$
\ell=2N+2=(p+1)/3,\qquad n_0=\ell-1=(p-2)/3,
$$
$$
m=(p-1)/2,\quad \pi_0^{m(p+1)}=p,
\quad\varepsilon=\pi_0^m.
\tag{1063.1}
$$
始终使用同一个原 $J_1$、$P=(p-1)D_0$、真实最低型 $e_1$，
以及 R1035/37、R1038/40 的实际整 Lie 格。
令 $R$ 为这些比较所在的原离散赋值整数环，剩余域为 $k$，
分式域为 $K_R$，并记
$$
\mathscr L_R=M_L\otimes R,\qquad
\mathscr L_R^{\rm new}
 =\ker(1+\delta+\delta^2:\mathscr L_R\to\mathscr L_R).
$$
$3$ 为单位，所以新部为整直和因子；其秩是 $n_0=2N+1$。
下面不需要额外声称每个新构造的系数都下降到一个更小的未分歧环。

在 $p\equiv11\bmod12$ 行，取 R1037 的完整
$v_{\rm full}=\varepsilon^{-1}e_1\log P$。
在 $p\equiv5\bmod12$ 行，按 R1038/40 先减去实际
prime-to-$p$ Teichmüller 挠点，只在 formal 群、Raynaud 好部分及
Lie 上施 $e_1$，取
$v_{\rm full}=\varepsilon^{-1}e_1\log_B(P_B)$。
另用原整新部投影定义
$$
v_{\rm full}\in\mathscr L_R,\qquad
e_{\rm new}=1-\frac{1+\delta+\delta^2}{3},\qquad
v_{\rm new}=e_{\rm new}v_{\rm full}\in\mathscr L_R^{\rm new}.
\tag{1063.2}
$$
以下未加下标的 $v$ 表示完整的 $v_{\rm full}$。
不从首层没有旧分量推断完整对数没有旧分量。
后文的交错型在旧部为零，所以第一槽用 $v_{\rm full}$ 或
$v_{\rm new}$ 给相同的泛函；有限轨道只在实际新部上取 $v_{\rm new}$。

原实际完美对称型与 Hodge graph 算子为
$$
B(x,y)=\langle\Pi x,y\rangle,\qquad
\Pi=F\alpha^{-1},\qquad
\mathcal Q=\varepsilon^{-2}\Phi\Pi.
\tag{1063.3}
$$
原两次 PD 比较已经证明 $\Phi(M_H)\subset\varepsilon^2M_L$，
所以 $\mathcal Q$ 确为整 Lie 算子。这是本篇唯一使用的
Hodge graph 除法；以后取其幂不再另除 $p$ 或 $\varepsilon$。
原外部线性算子
$$
D=\frac{\delta-\delta^{-1}}{\zeta-\zeta^2}
\tag{1063.4}
$$
在正、负新 deck 上分别为 $1,-1$，在旧 deck 上为零。
R1037 与 R1040 已逐行支付
$$
\mathcal Q^\dagger=\mathcal Q,\qquad D^\dagger=D,
\qquad \mathcal QD=-D\mathcal Q,
\tag{1063.5}
$$
其中 $\dagger$ 是相对于双线性型 $B$ 的伴随，不对外部系数作
复共轭或 Frobenius。
原 $\delta$ 亦对 $B$ 自伴，故 $e_{\rm new}$ 自伴。
旧部与新部对 $B$ 正交；整直和分解与 $B$ 的完美性遂给
$B$ 在实际新部上的限制也完美。
由 $\mathcal Q\delta=\delta^{-1}\mathcal Q$ 以及
$1+\delta^{-1}+\delta^{-2}=1+\delta+\delta^2$，
$e_{\rm new}$ 与 $\mathcal Q,D$ 及所有 split-Hecke 交换。
两行的全部 CM 新 Lie 只有正 deck，且 $\mathcal Q$ 在它上为零。
$p5$ 的额外 $\mathbf Q(\sqrt{-3p})$-CM 型已由 R1040 §6
在真实 $e_1$ 中排除；这里不重新假定整个 Jacobian 好约化。

## 2. 确切的整 Hecke 代数

令 $\mathbb T_{{\rm spl},R}$ 为以下真实算子生成的含幺 $R$-代数：
$$
\mathbb T_{{\rm spl},R}
=R[T_\lambda:\lambda\ {\rm prime},\
       \lambda\nmid6p,\ \lambda\equiv1\bmod3]
\subset\operatorname{End}_R(\mathscr L_R).
\tag{1063.6}
$$
这里 $T_\lambda$ 是 R1035/36/40 在原格中运输的实际对应，
不另换同谱矩阵。该代数的元素是这些生成元有限乘积的有限
$R$-线性组合。

各生成元彼此交换，保持原 $e_1$ 和新旧 deck 分解，与
$\mathcal Q,D$ 交换，且对 $B$ 自伴。
最后一点由实际 Rosati 自伴和与 $\Pi$ 的相容性取得。
由于生成元交换，其任意乘积仍自伴；$B$ 是双线性的，
故任意 $R$-线性组合亦自伴。因此对每个
$T\in\mathbb T_{{\rm spl},R}$ 都有
$$
T^\dagger=T,\qquad [T,\mathcal Q]=[T,D]=0.
\tag{1063.7}
$$

对确实来自整数 Hecke 多项式的 $T$，
$Tv=\varepsilon^{-1}e_1\log(TP)$，按两行同一个好部分约定理解。
若 $T$ 含一般 $R$ 系数，它仅是这些完整对数的整线性组合，
不声称仍是一点的对数。
更不会将 $\mathcal Q^{2j}Tv$ 称为某个有理点的对数。
后面的消去证明使用改变后的实际交错型，而不是这种未证身份。

R1036 §§5–6 和 R1040 §7 已证明：在任一个原 $D_0$ 投影非挠的
non-CM paired block 中，split-Hecke 生成真正中心 $F_0$，
该原块只出现一次 $C$，并且全部有理 MW 空间为 $F_0\beta$。
不同 paired blocks、以及它们与 CM 块，由同一 split-Hecke 分离。
这些是特征零的有理分解结论；本篇不把对应幂等元当作整幂等元。

## 3. 全部实际整交错型

对任意 $T\in\mathbb T_{{\rm spl},R}$、整数 $j\ge0$，定义
$$
\mathscr A_{T,j}(x,y)
   =B\bigl(x,T\mathcal Q^{2j+1}Dy\bigr).
\tag{1063.8}
$$
由 (1063.5)、(1063.7)，
$$
\begin{aligned}
(T\mathcal Q^{2j+1}D)^\dagger
 &=D\mathcal Q^{2j+1}T\\
 &=-T\mathcal Q^{2j+1}D.
\end{aligned}
$$
所以 (1063.8) 反对称；$2\in R^\times$，它是交错型。
所有因子均已在实际格中整，故该型亦整。

对任何原 split-Hecke $S$，
$$
\mathscr A_{T,j}(Sx,y)=\mathscr A_{T,j}(x,Sy).
\tag{1063.9}
$$
原因是 $S$ 自伴且与 $T,\mathcal Q,D$ 交换。
在上述相关 non-CM block 中，这准确延拓为
$F_0\otimes K_R$-平衡性。该延拓使用 R1036 的真正中心结论，
不是只对某个未证饱和的整 Hecke order 测试。

旧 deck 被 $D$ 杀；CM 新部被 $\mathcal Q^{2j+1}$ 杀。
不同 split-Hecke 块之间的交叉配对为零：若两块的某个
split-Hecke 本征值不同，将 (1063.9) 两边相减，并在特征零中
除该非零差即可。没有在整格中除这个差。

## 4. 对原完整 MW 的逐块消去

第一槽始终是 (1063.2) 的同一个完整 $v=v_{\rm full}$。定义实际整 Lie 泛函
$$
\boxed{\quad
\Lambda_{T,j}(w)
 =B\bigl(v,T\mathcal Q^{2j+1}D\,e_1w\bigr).
\quad}
\tag{1063.10}
$$
两行对 $e_1w$ 的 formal/good-BT 解释仍按 §1；
没有对一个尚未减去的 Teichmüller 点施 $e_1$。

按原有理 paired block 分解审查一个任意 MW 对数：

1. 若 $P$ 在该块的像为挠点，$v$ 的该块为零。
   本篇不对这类块的秩作任何要求。
2. 若该块 non-CM 且原点像非挠，原整个 MW 空间是
   $F_0\beta$，而 $v$ 是 $\beta$ 的同一非零归一对数。
   因而每个 MW 向量在该块为 $av$，$a\in F_0\otimes K_R$。
   交错性和平衡性给
   $$
   \mathscr A_{T,j}(v,av)
    =\mathscr A_{T,j}(av,v)
    =-\mathscr A_{T,j}(v,av)=0.
   $$
3. 原旧部和全部 CM 新部按 §3 被第二槽算子杀掉；
   不同块交叉项亦已消去。

所以
$$
\boxed{\quad
\Lambda_{T,j}(\log J_1(\mathbf Q))=0
\quad\text{对每个 }T,j.
\quad}
\tag{1063.11}
$$
线性给其分式域 span 上消失；整性给与原 Lie 格相交的饱和格上
亦消失。这是完整 MW 消去，不只是与单个 $v$ 正交。

消去证明本身不使用 $p>C_*$。该界仅在引用原负角色首 log 非零、
从而已有 $T=1,j=0$ 行本原时需要。即使某个高幂行是零或非本原，
(1063.11) 仍成立。

为把各行放进原消去格，置
$$
c_{T,j}=D T\mathcal Q^{2j+1}v_{\rm full}
       =D T\mathcal Q^{2j+1}v_{\rm new}
       \in\mathscr L_R^{\rm new}.
\tag{1063.12}
$$
自伴性给准确符号
$$
\Lambda_{T,j}(w)=B(c_{T,j},e_1w).
\tag{1063.13}
$$
特别地，不将 $D\mathcal Q$ 与 $\mathcal QD$ 无负号交换。
每个 $c_{T,j}$ 都属于原实际 MW 消去格在 $R$ 上的版本
$\Sigma_R$：对完整 MW span 在同一原整格中取正交。
本文不声称这些行生成整个 $\Sigma_R$。

## 5. 首层完整保持原 $\lambda$ 与系数固定的 Frobenius

以 $\overline{\mathcal Q}=Q$ 记原实际剩余域算子。
令 $r=1-b^3$、$A=A_p(b)$、$k_0=(2p-4)/3$；
$a\in k[b]/(A)$ 取唯一次数 $<\deg A$ 代表。两行均有
$$
Q(a)=\operatorname{quo}\bigl(r^{k_0}a(b^p),A^2\bigr)\pmod A,
\qquad \bar v_{\rm full}=\bar v_{\rm new}=(1-Q)\lambda,
\qquad\lambda=-6(b+1)/r\pmod A.
\tag{1063.14}
$$
以下 $\bar v$ 表示 (1063.14) 中相同的首层。
$a(b^p)$ 保持外部 $k$ 系数不变；不能任意改为 $a(b)^p$。
商必须由整个分子除 $A^2$ 后才取模 $A$。
因此 (1063.12) 的准确首层为
$$
\boxed{\quad
\bar c_{T,j}=D\bar T Q^{2j+1}(1-Q)\lambda.
\quad}
\tag{1063.15}
$$
它包含 $Q^{2j+1}\lambda-Q^{2j+2}\lambda$ 两项；
特别是 $j=0$ 保留原全部 $Q^2$ 返回。
第一槽的正规化一直是 $\varepsilon^{-1}\log P$，
没有给高幂行另选一个首层尺度。

形式上可以将右侧写成
$DQ(1-Q)\bar TQ^{2j}\lambda$，因为各相应算子交换；
这只是已证明的同一表达式。
除真实 Hecke 像及其线性组合外，不据此宣布
$\bar TQ^{2j}\lambda$ 有新的有理 divisor 主化来源。
实际授权来自 §§3–4 的完整交错型证明。

## 6. 同一完整 CM 轮廓与最低读数

保留原 $w=(a_{\rm src}-1)/p^3$ 和完整整 Lie-valued Abel log
$$
\mathcal H(w)=(p\varepsilon)^{-1}
              e_1\log[P(w)-c_1].
$$
由 R1033/39，$\mathcal H(0)=0$，全部 Tate 系数整，
约化次数至多 $n_0$。定义
$$
F_{T,j}(w)=\Lambda_{T,j}\bigl((p\varepsilon)^{-1}
                      \log[P(w)-c_1]\bigr)
            =B(c_{T,j},\mathcal H(w)).
\tag{1063.16}
$$
原盘内所有有理点都使整个族 (1063.16) 为零。

对任意 $c\in k[b]/(A)$，令
$$
T_c\equiv r^{k_0}c(b^p)/A'\pmod A,\qquad
\deg T_c<\deg A.
$$
记 R1052 的 period 函数为 $q_{\rm CM},j_{\rm CM}$，
与本篇整数幂指标 $j$ 区分；同一个实际参数和 principal part 为
$$
Z=-\frac r3(q_{\rm CM}/j_{\rm CM})^3,\qquad
b=B_{\rm CM}(Z),\qquad
L_{\rm CM}=\operatorname{PP}_{b=1}(Z_b'/Z^\ell).
$$
R1052 的完整 source/target、全部节点与积分尾比较对任意原行均成立，
故可直接用于每个 $\bar c_{T,j}$：
$$
\overline{F_{T,j}}(w)=
-\sum_{k=1}^{\ell-1}
\frac{\kappa_1^k(2\sqrt{A_{\rm tail}})^{3k-2}
      \lambda_0^{-(\ell-k)}}{2m(3k-1)}
[Z^k]\left(\frac{T_{\bar c_{T,j}}}{A}\right)
       (B_{\rm CM}(Z))\ w^{\ell-k}.
\tag{1063.17}
$$
没有抹掉 $p5$ 的两个无穷端；它们已在该原两行公式中支付。
所有 $\kappa_1,A_{\rm tail},\lambda_0$ 仍是原单位。

置
$$
\mathcal C(T_c)=[Z^{n_0}](T_c/A)(B_{\rm CM}(Z))
               =2\bar B(c,L_{\rm CM}).
$$
那么最低实际系数是
$$
[w]\overline{F_{T,j}}
 =u_{\min}\,\mathcal C(T_{\bar c_{T,j}}),\qquad
u_{\min}=-\frac{\kappa_1^{n_0}
(2\sqrt{A_{\rm tail}})^{3n_0-2}\lambda_0^{-1}}
{2m(3n_0-1)}\in k^\times.
\tag{1063.18}
$$
因 $3n_0-1=p-3$，显示分母确为单位。
自伴性和正确的 $DQ$ 顺序给
$$
\boxed{\quad
\mathcal C(T_{\bar c_{T,j}})
 =2\bar B\bigl(\bar TQ^{2j}\bar v,
                    QD L_{\rm CM}\bigr).
\quad}
\tag{1063.19}
$$
这保留同一实际最低列，不将其换成最高 $J_0$、参考核列、
原 bare 系数或另一个三挠点的 Petri 标量。

## 7. 精确轨道条件与真正的深盘后果

在实际新部 $k$-空间 $\bar{\mathscr L}^{\rm new}$ 定义
$$
\mathscr A_k=k[Q^2,\bar T_\lambda:
               \lambda\ {\rm prime},\
               \lambda\nmid6p,\ \lambda\equiv1\bmod3],
\qquad \mathscr U_k=\mathscr A_k\bar v.
\tag{1063.20}
$$
这是原实际算子的轨道，不是取一个抽象同维模块。
在 $R$ 上令
$\mathscr U_R=R[\mathcal Q^2,\mathbb T_{{\rm spl},R}]v_{\rm new}$；
(1063.20) 是它在
$\mathscr L_R/\pi_0\mathscr L_R$ 中的**像**。
不预设 $\mathscr U_R$ 饱和，或它自身的模 $\pi_0$ 商单射进该空间。

由 (1063.19)，有严格等价
$$
\boxed{\quad
\mathcal C(T_{\bar c_{T,j}})=0\ \text{对所有 }T,j
\quad\Longleftrightarrow\quad
QD L_{\rm CM}\in\mathscr U_k^{\perp_{\bar B}}.
\quad}
\tag{1063.21}
$$
因 $\bar B$ 完美，这只有在另已证明 $\mathscr U_k$ 满时
才允许进一步推 $QD L_{\rm CM}=0$；本篇没有该满轨道结论。
同样，不将整个 $\Sigma_R$ 的最低系数条件与本子族的条件混同。

全部输入可取有限个。事实上 $\mathcal Q^2$ 在秩 $n_0$ 的
实际新部上满足其首一特征多项式，故整数幂只需
$0\le j<n_0$；此处不作任何除法。
整 Hecke 代数的实际像是有限自由 End 格的子模，
$R$ 为 Noetherian，因此可取有限个真实 Hecke 乘积的线性张成。
这只给一个有限来源，不自动给实际矩阵的满秩。

若 (1063.21) 右侧不成立，则至少一行 (1063.16) 满足
$[w]F_{T,j}\in R^\times$。
由于整个 $F_{T,j}$ 整、常数项为零，
$$
F_{T,j}(w)=w\left(a_1+\sum_{n\ge2}a_nw^{n-1}\right),
\qquad a_1\in R^\times,\ a_n\in R.
$$
对 $v_p(w)>0$，括号的其余部分全在极大理想中，故括号为单位。
于是原深盘中的整个族只能在 $w=0$ 有共同零点。
特别地，原有理点在此盘只有中心 $c_1$。
这是一个使用真实全 MW、整尾和实际最低单位的条件后果；
不由一般 $M=1$ 或最高次数界代替其前提。

如果全部最低读数为零，仍不能据此断言有非中心根，
也不能停止：可继续使用同一个族的完整共同多项式关系，
或更大的实际饱和消去格。单行的失败不会令合法族消失。

### 7.1. 实际轨道必各向同性；正确目标在辛商中

在实际新部取
$$
A_Q(x,y)=\bar B(x,QDy).
\tag{1063.22}
$$
任意 $S,S'\in\mathscr A_k$ 都自伴、彼此交换并与 $Q,D$ 交换，故
$$
A_Q(S\bar v,S'\bar v)
 =\bar B(\bar v,SS'QD\bar v)=0,
\tag{1063.23}
$$
因为 $SS'QD$ 反自伴且 $p\ne2$。所以实际轨道 $\mathscr U_k$
对 $A_Q$ 全各向同性。

由 R1037/40，$\ker Q=kc_0$ 且 $Dc_0=c_0$。新部上的 $\bar B$
完美，$D$ 可逆，因而
$$
\operatorname{rad}A_Q=kc_0,\qquad
\bar{\mathscr L}^{\rm new}/kc_0
\text{ 是 }2N\text{ 维辛空间}.
\tag{1063.24}
$$
这里没有用 $\bar B(c_0,c_0)$ 为单位；原 bare 核范数可以尚未知。
于是
$$
\dim_k((\mathscr U_k+kc_0)/kc_0)\le N,\qquad
\dim_k\mathscr U_k\le N+1<2N+1.
\tag{1063.25}
$$
**该轨道不可能占满整个新部。** 因此 §7 的条件式不能被推进为
一个全新部循环性证明。

令 $L_{\rm new}=e_{\rm new}L_{\rm CM}$。
若另已证明 (1063.25) 左边等于 $N$，则 $\mathscr U_k$ 在辛商中的像
是 Lagrangian，故
$$
\mathscr U_k^{\perp_{A_Q}}=\mathscr U_k+kc_0.
\tag{1063.26}
$$
在这个尚待支付的最大商维数条件下，全部最低读数同时为零，
准确等价于
$$
L_{\rm new}\in\mathscr U_k+kc_0.
\tag{1063.27}
$$
最大商维数及排除 (1063.27) 都仍开放。即使达到 Lagrangian 维数，
也不能把落在该子空间误写成落在一维核。

## 8. 后续目标与来源

新的精确剩余问题是：证明原 $QD L_{\rm CM}$ 不在
真实 $k[Q^2,\bar T_\lambda]\bar v$ 的 $\bar B$-正交中，
或从整个实际多行共同关系直接排除正赋值非中心点。
原 $\bar v=(1-Q)\lambda$ 不能替换为任意输入；
原 $Q$ 的单核及 R955 奇链结构也不能冒充满轨道证明。

- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md) §§4–7：实际整 $B$、split-Hecke 自伴、真正 $F_0$、原重数一与完整 MW 的逐块证明。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：$p11$ 的实际 $\mathcal Q$、整性、反 deck、完整首 log 和 coefficient-fixed 矩阵。
- [R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：$p5$ 的真实 Raynaud 好部分、双端相位、CM 排除与相同整比较。
- [R1047](R1047-original-MW-saturated-profile-and-common-zero-bound.md)：实际全部 MW 消去格与共同整 Tate 函数；本篇不假定所构子族等于该格。
- [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md) §§7–8：任意原行的完整轮廓、实际最低 principal part、全部尺度与尾。

本篇未增加任何未经原比较支付的整 Hecke 幂等元，
未称 $\mathcal Q$ 为 BT 端同态，未借分式域的 $F_0$ 平衡推出
剩余域轨道饱和或满秩。原高单位、全共同深盘排除及 O0 仍开放。


## 9. 不反除核范数的整负角色因子分解与更大消去族

### 9.1 原本地 Hecke 与实际 Hodge graph 交换

R1035 §4 的两次 PD 态射自然性，对原本地 $T_5$ 给出同一晶体矩阵
$T_H,T_L$，保持实际 Fil graph，故
$$
T_L\Phi=\Phi T_H.
$$
R1036 §4 的真实 Frobenius 与算术下降相容性给
$T_H\Pi=\Pi T_L$。于是
$$
T_L\mathcal Q
 =\varepsilon^{-2}\Phi T_H\Pi
 =\mathcal Q T_L.
\tag{1063.28}
$$
$p5$ 行使用 R1040 §1 已运输的同一个实际 $T_5$ 和同一 PD 自然性；
不在整个坏约化 Jacobian 上假定好模型。

同一论证适用于原 canonical 全组件上、在素数
$\lambda\nmid6p$ 的真实 Hecke 对应，经
$X^{\rm can}_{\mathbf Q_p}\simeq X_{1,\mathbf Q_p}$ 运输后的 $T_\lambda$。
该同构使用 $p\equiv2\bmod3$ 时实际的
$\sqrt[3]4\in\mathbf Q_p$。对应在原好 BT 部分延拓且与 $p$-惯性相容，
所以 R1035 的态射论证逐个适用。
原全组件及 graph 返回按 R970 (970.18a–g) 保留；
这里是 weight-two Jacobian/Lie 作用，不添
(970.18h) 的高权 Igusa 因子。

这些实际算子彼此交换、Rosati 自伴，与 $F,\alpha$ 相容。
对 inert $\lambda\equiv2\bmod3$，完整返回给
$T_\lambda D=-DT_\lambda$；对 split 素数则与 $D$ 交换。
故所有这里使用的本地 $T_\lambda$ 都与 $\mathcal Q$ 交换。
不因此把 inert 算子称为 $X_1$ 上的 $\mathbf Q$ 对应。

### 9.2 本原负角色块与唯一整因子

置
$$
X=e_+\mathscr L_R,\qquad Y=e_-\mathscr L_R,\qquad
\operatorname{rk}X=N+1,\quad \operatorname{rk}Y=N,
$$
其中 $D$ 在两格上分别为 $+1,-1$。它自伴且 $2$ 为单位，
所以 $X,Y$ 对 $B$ 正交，限制 $B_X,B_Y$ 都完美。写
$$
\mathcal Q=
\begin{pmatrix}0&U\\ U^\dagger&0\end{pmatrix}.
\tag{1063.29}
$$
R1037/40 的负角色模 $\pi_0$ 单射给 $U:Y\to X$ 满列秩。
因此 $U$ 是本原整单射；对完美格取对偶，$U^\dagger:X\to Y$ 满射。
令
$$
K=\ker U^\dagger.
$$
则 $K$ 为本原秩一整格，且
$$
\operatorname{im}U=K^{\perp_{B_X}},\qquad
\ker\mathcal Q=K,\qquad
\operatorname{im}\mathcal Q=\operatorname{im}U\oplus Y
\text{ 为饱和子格}.
\tag{1063.30}
$$
(1063.29)–(1063.30) 的核与像均在实际新部 $X\oplus Y$ 中取。
这是满射的整对偶，不需要 $B_X$ 在 $K$ 上非退化。
尤其没有对 $B(c_0,c_0)$ 作除法。

对上述实际 inert $T_\lambda$，写
$$
T_\lambda=
\begin{pmatrix}0&V_\lambda\\ V_\lambda^\dagger&0\end{pmatrix}.
$$
它与 $\mathcal Q$ 交换又换正负角色，所以
$T_\lambda K\subset\ker\mathcal Q\cap Y=0$。
因此 $V_\lambda^\dagger K=0$，
$\operatorname{im}V_\lambda\subset K^\perp=\operatorname{im}U$。
存在唯一整算子
$$
S_\lambda:Y\longrightarrow Y,\qquad V_\lambda=US_\lambda.
\tag{1063.31}
$$
此处只在已证饱和的像中取唯一因子，不使用 $\mathcal Q^{-1}$。

交换式的 $X$ 块为
$$
US_\lambda^\dagger U^\dagger=US_\lambda U^\dagger.
$$
$U$ 单射、$U^\dagger$ 满射，故 $S_\lambda^\dagger=S_\lambda$。
令 $A_Y=U^\dagger U$；交换式的 $Y$ 块给
$[S_\lambda,A_Y]=0$。
split-Hecke 的相容性又给
$[S_\lambda,T_{{\rm spl},-}]=0$。
最后，原 $T_\lambda,T_\mu$ 交换的 $X$ 块给
$U[S_\lambda,S_\mu]U^\dagger=0$，故
$$
[S_\lambda,S_\mu]=0.
\tag{1063.32}
$$
从而实际代数
$$
\mathscr C_R=
R[A_Y,S_\lambda,T_{{\rm spl},-}]
       \subset\operatorname{End}_R(Y)
\tag{1063.33}
$$
交换且各元素对 $B_Y$ 自伴。所有生成元均由真实整格取得。

### 9.3 新整族及完整 MW 消去

对任意 $S\in\mathscr C_R$，在新部定义
$$
R_S=\begin{pmatrix}0&US\\ SU^\dagger&0\end{pmatrix},
\tag{1063.34}
$$
旧部上置零。它整、$B$ 自伴、反交换 $D$，并与全部 split-Hecke 交换。
原 CM 新 Lie 在 $K$ 中，故 $R_S$ 杀它。
因此
$$
\Lambda_S(w)=B(v_{\rm full},R_S D e_1w)
\tag{1063.35}
$$
是原完整 $v_{\rm full}$ 定义的真实整交错测试。
§4 的全部 paired block 论证逐项适用，给出
$$
\Lambda_S(\log J_1(\mathbf Q))=0
$$
以及原整 Lie 格中相应饱和交上的消失。

原 §3 的族是 $S=A_Y^jT_{{\rm spl},-}$；
原本地 $T_\lambda D$ 对应 $S=S_\lambda$。
例如 $S_\lambda^2$ 也给一个合法整行；
无需先把它写成一个除以未知 $\mathcal Q$ 或核范数的旧奇多项式。

### 9.4 同一最低列在显式整辛商中的读数

整满射
$$
\Psi:X\oplus Y\longrightarrow Y\oplus Y,\qquad
\Psi(x,y)=(U^\dagger x,y)
\tag{1063.36}
$$
的核是 $K$。原交错型满足
$$
B((x,y),\mathcal QD(x',y'))
 =B_Y(y,U^\dagger x')-B_Y(U^\dagger x,y').
\tag{1063.37}
$$
所以 (1063.36) 给原整辛商的显式标架，即使核的 $B$-范数
模 $\pi_0$ 为零也成立。

写
$$
\Psi(v_{\rm new})=(a,b),\qquad
\bar\Psi(L_{\rm new})=(\xi,\eta).
$$
第一对是原完整对数的整像，第二对是同一最低列的剩余域像。
取 $c_S=DR_Sv_{\rm full}=DR_Sv_{\rm new}$。
§6 的完整轮廓对这条实际行仍成立，最低读数准确为
$$
\boxed{\quad
\mathcal C_S
 =2\{\bar B_Y(\bar S\bar b,\xi)
          -\bar B_Y(\bar S\bar a,\eta)\}.
\quad}
\tag{1063.38}
$$
实际 $w$ 一次系数仍是同一个 $u_{\min}\mathcal C_S$。
$T_{\bar c_S}$ 的完整 Cartier/商定义仍保持外部系数不变；
$Q^2$ 返回已经在原 $\bar v=(1-Q)\lambda$ 中保留。

设 $\bar{\mathscr C}$ 是实际整代数 (1063.33) 的约化像。
则
$$
\mathscr W=\bar{\mathscr C}(\bar a,\bar b)\subset Y_k\oplus Y_k
$$
对 (1063.37) 全各向同性，故 $\dim_k\mathscr W\le N$。
若另证其维数为 $N$，则全部 (1063.38) 为零，
准确等价于 $(\xi,\eta)\in\mathscr W$。
最大维数及排除此包含仍未证明。

### 9.5 更一般的真实整交换子解格

还可令
$$
\mathscr E_R=
\operatorname{End}_{\mathbb T_{{\rm spl},R}|Y}(Y).
\tag{1063.39}
$$
它是与全部实际 split-Hecke 整矩阵交换的整解格。
这些是线性交换子方程；若 $\pi_0S$ 满足全部方程，则
$S$ 也满足，所以该解格在 $\operatorname{End}_R(Y)$ 中饱和。
不把它的约化像认作整个模 $\pi_0$ 的 centralizer。

任意 $S\in\mathscr E_R$ 不必先假定自伴。定义
$$
R_S=\begin{pmatrix}0&US\\ S^\dagger U^\dagger&0\end{pmatrix}.
\tag{1063.40}
$$
它仍整、自伴、反 $D$、对 split-Hecke 平衡，并杀旧部和原 CM。
因此 (1063.35) 的全部 MW 消去仍成立。
同一个最低读数变为
$$
\mathcal C_S=
2\{\bar B_Y(\bar S\bar b,\xi)
       -\bar B_Y(\bar a,\bar S\eta)\}.
\tag{1063.41}
$$
此一般族不附未经证明的交换轨道或 Lagrangian 断言。
它提供的是实际整解格中的更多合法行；非零读数及全深盘排除继续待证。


## 10. 原 $r=2$ bare 失败分支的实际 adjugate 读数

本节只在原 $p\equiv11\pmod{12}$、$p\ge41$ 行，
把 R1041/48 已付清的 bare 范数身份用于§9；
不把它扩充为 $p\equiv5\pmod{12}$ 行原 $r=8$ 的身份。
记原剩余域上的核生成元为 $c_0$，仍以
$T_{c_0}=T_0$、$\mathcal LT_0=A$、$\operatorname{lc}(T_0)=-1$ 定标，其中
$$
r=1-b^3,\quad A=bQ(b^3),\quad
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b.
$$
R1041 的原标量身份给
$$
\text{原 }r=2\text{ bare 标量}=0
\quad\Longleftrightarrow\quad
\bar B(c_0,c_0)=0.
\tag{1063.42}
$$
以下假定这两个等价条件成立；这不是宣称它们实际会发生。

§9的 $U$ 始终为本原单射，$U^\dagger$ 满射。
令 $A_Y=U^\dagger U$，并在此段以横线表示约化。
因为 $\ker\bar A_Y$ 经 $\bar U$ 单射进入
$\ker\bar U^\dagger=kc_0$，其维数至多一。
另一方面，$\bar B(c_0,c_0)=0$ 给
$c_0\in(kc_0)^\perp=\operatorname{im}\bar U$，故有唯一 $y_0\in Y_k$ 满足
$$
\bar U y_0=c_0,\qquad Qy_0=c_0,\qquad \bar A_Yy_0=0.
\tag{1063.43}
$$
所以 $\operatorname{rank}\bar A_Y=N-1$。
取整算子 $S_{\rm adj}=\operatorname{adj}(A_Y)$。
它是 $A_Y$ 的整多项式，属于实际代数 $\mathscr C_R$，
不除 $\det A_Y$。其约化非零、秩一；
由自伴性和 $B_Y$ 完美性，存在 $\kappa\in k^\times$ 使
$$
\operatorname{adj}(\bar A_Y)(z)
 =\kappa y_0\bar B_Y(y_0,z).
\tag{1063.44}
$$
这里 $\kappa$ 保留原 adjugate 和 $c_0$ 的实际定标，不置为一。
该证明不除 $\bar B_Y(y_0,y_0)$，此范数也可以为零。

$S_{\rm adj}$ 因而给§9.3真正的整 MW 消去行。
原最低 $w$ 系数仍须乘同一 $u_{\min}$；以下计算其完整剩余域标量。

### 10.1 唯一负角色前像的完整有限递推

记 $H=r^{\ell+1}(AT_0'-T_0A')$，$\ell=2N+2$。
R1048 的原规范恒等式给
$$
H'=r^\ell A^2,\qquad
c_0\equiv-H(b^p)/r\pmod A.
\tag{1063.45}
$$
令 $T_1=T_{y_0}$、$F_i=T_i/A$（$i=0,1$）。
$T_1$ 在 $2\bmod3$ 次数类，故唯一写成
$T_1=b^2V(b^3)$、$\deg V\le N-1$。
由原系数固定的 $Q$ 公式
$Qz\equiv\mathcal LT_z/(2rA')\pmod A$
及 $Qy_0=c_0$，得到完整多项式恒等式
$$
\mathcal LT_1=R_0,\qquad
R_0=\operatorname{rem}_A(-2A'H(b^p)).
\tag{1063.46}
$$
两边次数均至多 $3N$，且均在 $0\bmod3$ 类；
所以这里不只是再取模 $A$ 后相等。
右端保留规范 $H$ 的全部 $b^p$ 代入，
不以 $H(b)^p$ 代替一般外部系数固定的约定。

写 $R_0=\sum_{j=0}^Nr_j(b^3)^j$、
$V=\sum_{j=0}^{N-1}v_j(b^3)^j$。由
$$
\mathcal L(b^{3j+2})
 =(3j+2)(3j+1)b^{3j}
   -(3j+7/2)^2b^{3j+3}
$$
准确得到
$$
\begin{aligned}
2v_0&=r_0,\\
(3j+2)(3j+1)v_j-(3j+1/2)^2v_{j-1}
 &=r_j\quad(1\le j<N),\\
-4v_{N-1}&=r_N.
\end{aligned}
\tag{1063.47}
$$
显示递推中除数全是单位；最后一式来自
$3N+1/2\equiv-2\bmod p$，是实际前像存在条件，
不能在未假定 (1063.42) 时删掉或自动满足。
它在当前分支由 (1063.43) 保证。
于是 $T_1$ 及其端点、最低读数都由原规范输入唯一确定。

### 10.2 四个真实配对与两列最低值

令 $C_i=\mathcal C(T_i)$、$F_i(1)=T_i(1)/A(1)$。
R1045 的三个原 CM 点全留数对任意新部向量 $z$ 给
$\bar B(z,\lambda)=3(T_z/A)(1)$；
R1052 给 $\mathcal C(T_z)=2\bar B(z,L_{\rm CM})$。
这里确实保留三个留数 $4,-2,-2$：
新部的 $T_z/A$ 属于两个非平凡三次角色，
故其在另外两 CM 点的值之和为负的中心值。

由 $Q$ 自伴、$Qy_0=c_0$、$Qc_0=0$，
以及同一个 $\bar v=(1-Q)\lambda$，得到
$$
\begin{aligned}
\bar B_Y(y_0,\bar b)&=3\{F_1(1)-F_0(1)\},\\
\bar B_Y(y_0,\bar a)&=3F_0(1),\\
\bar B_Y(y_0,\xi)&=C_0/2,\\
\bar B_Y(y_0,\eta)&=C_1/2.
\end{aligned}
\tag{1063.48}
$$
其中 $(a,b)=\Psi(v_{\rm new})$、
$(\xi,\eta)=\bar\Psi(L_{\rm new})$ 正是§9.4的原两列；
例如 $\bar B_Y(y_0,\bar a)=\bar B(c_0,\bar v)
=\bar B(c_0,\lambda)$，没有另取前像或改变 $v$。

代入§9同一最低公式，实际标量为
$$
\begin{aligned}
\mathcal C_{\rm adj}
 &=3\kappa\bigl\{\{F_1(1)-F_0(1)\}C_0-F_0(1)C_1\bigr\}\\
 &=3\kappa\det
 \begin{pmatrix}F_1(1)-F_0(1)&F_0(1)\\ C_1&C_0\end{pmatrix}.
\end{aligned}
\tag{1063.49}
$$
实际最低 $w$ 系数是 $u_{\min}\mathcal C_{\rm adj}$。
等价的原行向量为
$$
\bar c_{\rm adj}
 =3\kappa\bigl\{\{F_1(1)-F_0(1)\}c_0-F_0(1)y_0\bigr\},
\qquad
Q\bar c_{\rm adj}=-3\kappa F_0(1)c_0.
\tag{1063.50}
$$
完整返回由 $\bar v=(1-Q)\lambda$ 和指定 $Q$ 前像保留；
本式没有删除原 $Q^2$ 项。
另由 R1043，$F_0(1)=-6f_N/A(1)$，
但端点非零不代 (1063.49) 的行列式非零，
也不把 $f_N$ 与 bare 核范数混同。

本节支付 bare 失败分支中 adjugate 行的原整来源、全部四个配对、
有限前像递推与准确最低尺度，尚未证明 (1063.49) 非零。
若该值非零，原整 Tate 论证即排除指定深盘内的非中心有理点；
若为零，仍须继续其余真实整族或完整共同零关系，
不据此宣称有非中心点。

本节由 o2_high_coefficient 推导，root 独核原 $Q$ 商与次数、
完整三 CM 留数、递推末边界、adjugate 定标和最低行列式符号。
无数学程序执行。


## 11. 固定 $X_0(108)$ 四维块与原零主分量的 Hecke 障碍

令 $k$ 为本篇实际剩余域，$W=\mathscr L_k^{\rm new}$，
$Q=\overline{\mathcal Q}$，并令 $W_0=\ker Q^h$，其中 $h$ 充分大；
这是原 $Q$ 的完整零主分量。这里的 $T_5$ 始终是§9.1
原 canonical 全组件上的标准 weight-two Hecke 对应，经同一
$\mathbf Q_p$ 同构和实际好 BT/PD 比较运输所得的作用。
不插入高权 Igusa 的度数或微分因子。

由 (1063.28)–(1063.31)，有
$$
[T_5,Q]=0,\qquad \ker Q=kc_0\subset X_k,\qquad T_5c_0=0.
\tag{1063.51}
$$
最后一个等式不依赖核范数：$T_5$ 换 $X_k,Y_k$，
故 $T_5\ker Q\subset\ker Q\cap Y_k=0$。
因此 $T_5$ 在 $W_0$ 上幂零。确实，可在 $\bar k$ 中作本征分解；
若 $T_5$ 的某个非零本征值的广义块 $Z\subset W_0$ 非零，
则 $Z$ 被 $Q$ 保持。$Q|Z$ 幂零，故 $\ker(Q|Z)\ne0$；
这给 $\ker Q$ 中一个 $T_5$ 可逆子空间，与 (1063.51) 矛盾。
所以
$$
(T_5|W_0)^{\dim W_0}=0.
\tag{1063.52}
$$
此结论也适用于 $W_0$ 的任意 $T_5$ 稳定子商。

另一方面，R1060 固定 $X_0(108)$ 上 $\tau_3=1$ 的四维 non-CM 格
记为 $V_{108}$。Harrison §4 的实际 oldform 基为
$$
f_{54}^{(1)},\quad f_{54}^{(1)}|\delta_2,\quad
f_{54}^{(2)},\quad f_{54}^{(2)}|\delta_2,
\qquad (f|\delta_2)(\tau)=2f(2\tau).
$$
两 primitive forms 的 $a_5$ 分别为 $+3,-3$。
因 $5\nmid108$，标准 $T_5$ 与 $\delta_2$ 交换，故
$$
T_5^2|V_{108}=9\,\mathrm{id}.
\tag{1063.53}
$$
这是 characteristic-zero Hecke 身份，并在 $\tau_3=1$
的整饱和格上成立；$3$ 为单位，$\tau_3$ 的整投影给同一个四维约化空间。
因此 $p\ge41$ 时，$T_5$ 在该空间及任何稳定子商上均可逆。
这一点无须先调用 R1060 的 Cartier ordinary 性结论。

若 $E_0$ 是 $W_0$ 的任一 $T_5$ 稳定子商，
$F_0$ 是 $V_{108,k}$ 的任一 $T_5$ 稳定子商，则
$$
\operatorname{Hom}_{k[T_5]}(E_0,F_0)
=\operatorname{Hom}_{k[T_5]}(F_0,E_0)=0.
\tag{1063.54}
$$
一侧 $T_5$ 幂零，另一侧由 (1063.53) 可逆，任一 intertwiner 必为零。

因此，固定四维 ordinary Cartier 块不能通过保持这些实际 $T_5$
作用的线性子商识别，控制原 $Q$ 的零主分量或其奇 Jordan 链厚度。
本节只排除上述 Hecke 相容线性桥，未排除尚未构造的非线性或改变
Hecke 作用的对应。R1059/R1061 已付的 Raynaud $\beta$ 是双线性原来源，
其输出 $zw\Omega$ 位于固定曲线的六维 CM Cartier 核；
不能把它改称上述已被排除的线性识别。

原始来源：[M. Harrison, *A new automorphism of $X_0(108)$*,
arXiv:1108.5595v3](https://arxiv.org/pdf/1108.5595)，§4，printed pp.8–11：
p.9 两个 $f_{54}$ 的 $q^5$ 系数，p.10 Definition 4.2 的
$e_1,\ldots,e_4$，以及 p.11 的 $\tau_3$ 作用。
o2_high_coefficient 推导，root 重读原 Hecke/PD 身份及上述 primary，
独核整个零主分量而非仅 $\ker Q$ 上的幂零证明；无数学程序执行。
