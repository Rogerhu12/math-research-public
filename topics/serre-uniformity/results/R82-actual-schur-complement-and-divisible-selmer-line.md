# R82：实际同余曲线的二阶消去与可除 Selmer 直线

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的必要结构；没有构造实际非 CM 同余曲线。**
设 $E/\mathbb Q$ 实际满足
$$E[43]\simeq A[43],\qquad A:y^2=x^3-x,$$
并设 $r=859$、$q=49019$ 都是 $E$ 的新增**分裂乘法**素数。
R78 已计算的非退化二阶主块可以从 R50 的实际 Selmer 矩阵中
精确消去。若全部新增分裂乘法素数恰有三个，则
$$
\boxed{
\operatorname{Sel}_{43^n}(E/\mathbb Q)
\simeq\mathbb Z/43^n\mathbb Z
\quad\text{对每个 }n\ge1,
}
\tag{82.1}
$$
以及
$$
\boxed{
\operatorname{Sel}_{43^\infty}(E/\mathbb Q)
\simeq\mathbb Q_{43}/\mathbb Z_{43}.
}
\tag{82.2}
$$
任意多个新增非分裂乘法素数不影响此结论。

这仍保留两个算术分支：
$$
\begin{array}{c|c}
\operatorname{rank}E(\mathbb Q)&\Sha(E/\mathbb Q)[43^\infty]\\\hline
1&0\\
0&\mathbb Q_{43}/\mathbb Z_{43}.
\end{array}
\tag{82.3}
$$
第二行未被本篇排除。因此 (82.1)、(82.2) 不是无条件的
Mordell–Weil 秩一结论，也不产生 R51 要求的原始高指标整数点。

## 1. 实际矩阵中的固定二阶块

保留 R50 的记号
$$
S=\{\ell:v_\ell(j(E))<0,\quad
E/\mathbb Q_\ell\text{ 为分裂乘法约化}\}.
$$
设 $r,q\in S$，按顺序写
$$S=(r,q,t_1,\ldots,t_n),\qquad n=|S|-2.$$
其他 $t_i$ 可以在 $K=\mathbb Q(i)$ 中分裂或惰性。
R50 已经在必要时商掉两条 Kummer 条件的共同交，
所以每处仍只贡献一个二维双曲平面。

在 $r,q$ 取 R78 的规范双基，其余位置任取 R50 所要求的
$B(a_t,e_t)=1$ 双基。实际矩阵具有分块形式
$$
M_E=
\begin{pmatrix}
J&B\\
-B^{\mathsf T}&C
\end{pmatrix},
\qquad
J=
\begin{pmatrix}0&6\\-6&0\end{pmatrix},
\quad C^{\mathsf T}=-C.
\tag{82.4}
$$
所有系数均在 $\mathbb F_{43}$ 中，$-6=37$。

这里 $J$ 确实等于 R78 的普适块，而非重新假定它对实际 $E$
仍成立：R60 的单素数类 $c_r,c_q$ 在其余位置都满足
$A$ 的通常条件，因而属于 R50 的松弛群 $H^+$。
它们的奇异投影分别为标准向量。
由 R50 的全局唯一性，它们正是实际矩阵在 $r,q$ 的两列所用的类。
所以这些列在 $r,q$ 的主块不受其他新增素数及其局部模型影响。

若 $t_i$ 惰性，它对应的列也可用 R60 的普适 $c_{t_i}$。
若 $t_i$ 在 $K$ 分裂，则其共同交及剩余局部直线可能依赖实际 $E$；
下文使用 R50 已构造的实际列类 $h_{t_i}$，不把它冒称为一个
与 $E$ 无关的 R60 惰性素数类。

## 2. Schur 补及消去后的真实全局类

定义
$$
\boxed{M^{\rm red}=C+B^{\mathsf T}J^{-1}B.}
\tag{82.5}
$$
由于 $(J^{-1})^{\mathsf T}=-J^{-1}$，此矩阵仍交替。
直接作合同变换
$$
P=
\begin{pmatrix}
1_2&-J^{-1}B\\
0&1_n
\end{pmatrix}
$$
得到
$$
P^{\mathsf T}M_EP
=\begin{pmatrix}J&0\\0&M^{\rm red}\end{pmatrix}.
\tag{82.6}
$$
因而
$$
\boxed{
\operatorname{rank}M_E=2+\operatorname{rank}M^{\rm red},\qquad
\ker M_E=
\left\{\binom{-J^{-1}By}{y}:M^{\rm red}y=0\right\}.
}
\tag{82.7}
$$
结合 R50，这就是实际 $\operatorname{Sel}_{43}(E)$ 的精确识别。

若 $m_{uv}$ 表示原矩阵的行 $u$、列 $v$ 条目，则
$$
(M^{\rm red})_{uv}
=m_{uv}+
\frac{m_{q,u}m_{r,v}-m_{r,u}m_{q,v}}6,
\qquad u,v\in S\setminus\{r,q\}.
\tag{82.8}
$$
该式可直接用于算术计算，不仅是维数公式。

消去后的列也有实际全局代表。令 $h_t$ 为原矩阵在 $t$ 的列类，
定义
$$
\widetilde h_t
=h_t+\frac{m_{q,t}}6c_r-\frac{m_{r,t}}6c_q.
\tag{82.9}
$$
由交替性及 (82.4)，它在 $r,q$ 的不分歧分量恰为零；
在这些位置已经满足实际 $E$ 的 Kummer 条件。
它在其余位置的剩余不分歧系数就是 (82.8)。
于是 $\sum y_t\widetilde h_t$ 属于实际 Selmer 群，当且仅当
$M^{\rm red}y=0$。

这不是从曲线导子中删除 $r,q$，也不产生另一条曲线。
式 (82.9) 的类在 $r,q$ 仍可有非零奇异 Kummer 坐标；
消去的是矩阵中的两个自由变量。

## 3. 三个新增分裂乘法素数时的唯一方向

现在设 $S=\{r,q,t\}$。一个一阶交替矩阵只能为零，故
$M^{\rm red}=(0)$。令
$$x=m_{r,t},\qquad y=m_{q,t}.$$
则
$$
M_E=
\begin{pmatrix}
0&6&x\\
-6&0&y\\
-x&-y&0
\end{pmatrix},
\qquad
\ker M_E=\mathbb F_{43}(y,-x,6).
\tag{82.10}
$$
特别地
$$
\boxed{\dim_{\mathbb F_{43}}\operatorname{Sel}_{43}(E)=1.}
\tag{82.11}
$$
其非零方向可取
$$y c_r-x c_q+6h_t.$$
不需要预先算出 $x,y$ 才能证明 (82.11)；
若要写出该类的具体根式，则仍须计算这两个条目或相应全局类。

一般地，只要 $r,q\in S$，就有
$$
\dim\operatorname{Sel}_{43}(E)\le |S|-2,\qquad
\dim\operatorname{Sel}_{43}(E)\equiv |S|\pmod2.
\tag{82.12}
$$
若 $|S|=5,7,\ldots$，仅有已知二阶块不保证核只剩一维。
此时仍须计算 (82.5)，不能把三处结论推广到所有奇数个位置。

## 4. Cassels–Tate 的准确接口：从一维到可除直线

以下引理对任意奇素数 $p$ 适用。

**引理 82.1。** 若椭圆曲线 $E/\mathbb Q$ 满足
$$E(\mathbb Q)[p]=0,\qquad
\dim_{\mathbb F_p}\operatorname{Sel}_p(E)=1,$$
则
$$
\operatorname{Sel}_{p^\infty}(E)\simeq\mathbb Q_p/\mathbb Z_p,
\qquad
\operatorname{Sel}_{p^n}(E)\simeq\mathbb Z/p^n\mathbb Z
\quad(n\ge1),
\tag{82.13}
$$
且
$$
\Sha(E)[p^\infty]/\Sha(E)[p^\infty]_{\rm div}=0.
\tag{82.14}
$$
其 Mordell–Weil 秩与可除 $\Sha$ 的可能性恰为 (82.3) 的一般 $p$ 版本。

**证明。** 设
$$\mathcal S=\operatorname{Sel}_{p^\infty}(E),\qquad
\mathcal X=\Sha(E)[p^\infty].$$
通常 Kummer 正合列为
$$
0\longrightarrow E(\mathbb Q)\otimes\mathbb Q_p/\mathbb Z_p
\longrightarrow\mathcal S
\longrightarrow\mathcal X\longrightarrow0.
\tag{82.15}
$$
$E(\mathbb Q)[p]=0$ 也排除全部有理 $p$ 幂挠点。
有限层与无限层的 Kummer 正合列比较给
$$
\operatorname{Sel}_{p^n}(E)
\xrightarrow{\sim}\mathcal S[p^n].
\tag{82.16}
$$
一般情形该映射的核是
$E(\mathbb Q)[p^\infty]/p^nE(\mathbb Q)[p^\infty]$；
这里为零。局部 Kummer 条件相容保证其像恰为右侧，
不是仅在整个 $H^1$ 上作比较。

$\mathcal S$ 是余有限生成的 $\mathbb Z_p$ 模。
例如其 $p$ 挠有限，Pontryagin 对偶的紧 Nakayama 引理给出有限生成；
这也是有限 Selmer 群理论的通常结构结论。
因此 $\mathcal X$ 可写成
$$
\mathcal X\simeq(\mathbb Q_p/\mathbb Z_p)^\delta\oplus B
$$
其中 $B$ 有限。它恰代表可除子群的商。
经典 Cassels–Tate 配对在
$\Sha(E)/\Sha(E)_{\rm div}$ 上非退化；由椭圆曲线的主极化，
其奇数 $p$ 部分是交替配对。因此有限群 $B$ 有非退化交替配对，
并可按双曲对分解为
$$
B\simeq\bigoplus_{j=1}^t
\left(\mathbb Z/p^{a_j}\mathbb Z\right)^2,
\qquad a_j\ge1.
\tag{82.17}
$$
这里没有假设 $\mathcal X$ 本身有限。

为了看清 (82.17)，取 $B$ 中阶最大的元素；
非退化性给一个与其配对具有相同准确阶的元素，
二者生成一个非退化的等阶循环双对。
它与其正交补直和，有限归纳即得所述分解。

设 $r_E=\operatorname{rank}E(\mathbb Q)$。
(82.15) 的左项是可除群，因而是单射对象，正合列在群的范畴分裂。
故
$$
\mathcal S\simeq
(\mathbb Q_p/\mathbb Z_p)^{r_E+\delta}\oplus B.
$$
由 (82.16)，取 $p$ 挠的维数得到
$$
1=\dim\operatorname{Sel}_p(E)=r_E+\delta+2t.
\tag{82.18}
$$
因此 $t=0$、$r_E+\delta=1$。
这证明 (82.13)、(82.14)，并给出恰好两个可能：
$(r_E,\delta)=(1,0)$ 或 $(0,1)$。证毕。

该论证中从 $\operatorname{Sel}_p\simeq\mathbb F_p$ 到
$\operatorname{Sel}_{p^\infty}\simeq\mathbb Q_p/\mathbb Z_p$
的同一经典接口，也明确写在 Castella–Wan (2024)
期刊版 Corollary B 的证明中。
本引理只使用该段的 Kummer 与 Cassels–Tate 论证，
不使用他们后续需要半稳定假设的 $p$-converse 定理。

对当前实际同余，$E(\mathbb Q)[43]=A(\mathbb Q)[43]=0$，
由 (82.11) 应用引理，立即得到 (82.1)–(82.3)。
若另知 $\Sha(E)[43^\infty]$ 有限，则只剩秩一且该群为零的分支；
这种有限性不能从引理的结论反过来自动取得。

更一般地，(82.18) 的同一结构证明给
$$
\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E)
\equiv \dim_{\mathbb F_p}\operatorname{Sel}_p(E)\pmod2.
\tag{82.19}
$$
所以 R50 的矩阵奇偶性无条件传到 **Selmer 余秩**；
只有再排除可除 $\Sha$，才传到 Mordell–Weil 秩。

## 5. 已发表的 supersingular $p$-converse 不能直接补掉可除分支

这里 $E$ 在 $p=43$ 好超奇异：
R13 给好约化，残余局部表示与 $A[p]$ 同构，
其不可约的水平二惯性排除 ordinary 情形。
然而
$$
N_E=32\,\operatorname{rad}(Z)
\tag{82.20}
$$
在 $2$ 的导子指数是 $5$，故 $E$ 不是半稳定曲线。

Castella–Wan,
*Perrin-Riou's main conjecture for elliptic curves at supersingular primes*,
Mathematische Annalen **389** (2024), 2595–2636，
期刊版 Theorem A／Theorem 6.11 和 Corollary B
要求 $E/\mathbb Q$ **半稳定**。
其 Theorem C、Theorems 5.3、6.9、6.10 的相应主要输入明确要求
$N$ **平方自由**。因此不能把 (82.2) 直接代入这些定理，
然后宣称 (82.3) 的第二行已被排除。

还须准确区分残余分歧要求：

1. 在该文 Theorem C／5.3／6.9 中，
   $\Lambda_{\rm ac}[1/p]$ 上的主猜想等式或整除关系
   不要求在每个 $\ell\mid N^-$ 上残余分歧。
   因而不能把这个额外假设误写成 Theorem A 的明文前提。
2. 同一定理加强到整数 Iwasawa 代数
   $\Lambda_{\rm ac}$ 的版本，确实额外要求
   $E[p]$ 在每个 $\ell\mid N^-$ 上分歧。
   其证明指出该条件使有关 Jacquet–Langlands 周期比成为 $p$ 进单位。
3. 本题每个新乘法素数 $\ell\parallel N_E$ 都有
   $$v_\ell(\Delta_{\min}(E))=p\,v_\ell(Z),$$
   因而 $E[p]$ 在该处不分歧；也可直接由 $E[p]\simeq A[p]$
   及 $A$ 在所有奇素数好约化看出。
   所以这些素数全部不能满足上述整数版本所需的残余分歧。
4. 该文 Theorem 6.11 的证明利用半稳定性及降层选一个
   在残余表示中仍分歧的导子素数。这里所有新增奇乘法素数均被降去，
   剩下的是加性指数 $5$ 的素数 $2$；
   不能把它当作一个已满足平方自由假设的乘法素数来照搬证明。

本篇没有使用尚未公认、声称完全去掉这些假设的较新论证。
要在本题中从 (82.2) 推出实际有理非挠点，需要一个覆盖
(82.20) 及其残余类型的新全局输入，或直接构造该点。

## 6. 对 R51 原始高指标问题的作用及边界

给定一个满足 R51 全部条件的原始高指标整数点，
R19 已经构造实际 $E$。再由 R50 的 Legendre 符号
$$
S=
\begin{cases}
\{\ell\mid Z:(-3W/\ell)=1\},&\mathrm I,\mathrm{II},\\
\{\ell\mid Z:(-6W/\ell)=1\},&\mathrm {III},
\end{cases}
$$
可准确判断该点是否落在本篇适用的子族。
若 $r,q\in S$ 且 $|S|=3$，这个原始点所给出的实际曲线
必须具有 (82.1)–(82.3) 的结构。
这比任意三阶交替矩阵只知核维数为一或三强，
因为 R78 已证明其中的一个实际主块非退化。

反过来，抽象修改 Selmer 群的一维核，不构造整数
$$
I_L(u,v)=\pm\mu_e|Z|^{3k},\qquad (u,v)=1,
$$
也不证明该方程无解。
尤其辅助 $j=0$ 曲线 $D_a$ 与实际 $E$ 之间没有已经建立的
有理同源或 Selmer 传递；(82.2) 不给 $D_a$ 的秩一，
更不说明某个已知 $D_a(\mathbb Q)$ 点生成全部 Mordell–Weil 群。

(82.1) 也没有把残余同构提升为
$E[p^n]\simeq A[p^n]$。这里提升的是实际 $E$ 自己的 Selmer 群，
不是它与 CM 曲线的 Galois 表示同构。
因此不能借 (82.1) 擅自对 R35 取任意高层以加强分母指数。

下一项实际算术仍是 R51 的原始指标高次幂或等价的 R19 原始解；
本篇不再以扩大抽象奇数候选集替代该问题。

## 7. 来源

- [R50](R50-actual-selmer-alternating-matrix.md)：
  实际局部条件商、全局列类、$\operatorname{Sel}_p(E)=\ker M_E$。
- [R60](R60-selmer-matrix-kummer-residue-symbols.md)、
  [R78](R78-normalized-selmer-entry-and-second-order-coordinate.md)：
  规范惰性单素数类及实际非退化二阶块。
- F. Castella and X. Wan, 上述 2024 期刊论文，
  [作者提供的期刊版全文](https://web.math.ucsb.edu/~castella/Perrin-Riou-print.pdf)，
  Corollary B 的 Kummer／Cassels–Tate 论证；
  Theorems A、C、5.3、6.9–6.11 的准确假设。
  [作者出版目录](https://web.math.ucsb.edu/~castella/)
  给卷期页码。
- [R19](R19-converse-fermat-fixed-cm.md)、
  [R51](R51-primitive-index-sufficiency.md)：
  实际同余与精确原始高指标方程的双向归约。
