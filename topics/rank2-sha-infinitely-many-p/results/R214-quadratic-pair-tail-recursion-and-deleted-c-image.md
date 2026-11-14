# R214 — 平方根双分量、实际高尾递推与降两次的删 C 商

日期：2026-11-12。状态：本文的整目标变换、真实 Schur 矩阵、有限像递推预算及中央比较恒等式均已证明；未取得定向的严格全素数收益。原课题未完成。

本文接 [R209](R209-coherent-source-reduction-and-mixed-euler-schur-image.md) 的 $\partial_A^2$ 原源降阶，使用 [R199](R199-exact-first-band-exponential-and-complete-divided-image.md) 的准确第一带及 [R206](R206-fourth-layer-interior-schur-and-true-deleted-column-quotient.md) 的删列循环商。这里把真实余矩阵写成两个实际级数的高尾；两个级数的高尾始终保留，不把形式二次关系截成一个假的代数曲线。

## 1. 固定原源与精度范围

取
$$
 p=4r-1\ge19,\quad r>2D,\quad O=\mathbf Z_p,\quad
 R=r(p-1),\quad E_D=O[A,C]_{\le D},\quad v_0=-22.
$$
原曲线在所需第一带内为
$$
 A(w)=e^{aw^r/p}f(w),\quad C(w)=e^{aw^r/p}c(w),\qquad
 f=w+\cdots,\quad c=v_0w^2+\cdots,\quad a\in O^\times.
 \tag{1}
$$
全部目标使用同一个原权
$$
 J_n(P)=p^{\lfloor n/r\rfloor}[w^n]P(A(w),C(w)),\qquad
 n<k=rq+s,\quad0\le s<r,\quad q\le p-2.
 \tag{2}
$$
特别 $k\le R-1$。下述平方根及逆参数最多需要额外一个原 $C$ 系数，仍在第一带内。本文没有把这个权或换参外推到 $n\ge R$ 的完整无限矩阵。

记 $\pi^r=p$。R199 给
$A(\pi z)/\pi,C(\pi z)/\pi^2\in O_\pi[[z]]$，所需指数阶乘均为单位。

## 2. 平方根参数及双分量目标的整同构

定义首项为 $w$ 的实际参数
$$
 v(w)=\sqrt{C(w)/v_0}
 =w e^{aw^r/(2p)}\sqrt{c(w)/(v_0w^2)}.
 \tag{3}
$$
因 $p$ 为奇数，取常数项为一的平方根在整形式级数上存在；故
$v(\pi z)/\pi\in zO_\pi[[z]]$，线性项为一。其形式逆有同样性质。因此从 $w$ 到 $v$ 的所有有限归一目标矩阵都是整下三角、对角为一，保持 (2) 的全部有限像和严格前缀值理想。

令
$$
 \alpha(v)=A(w(v))=u(C)+v\beta(C),\qquad C=v_0v^2,
 \quad u\in C\mathbf Q_p[[C]],\quad\beta(0)=1.
 \tag{4}
$$
对任意实际输出 $H(v)$，按奇偶部分写
$$
 H(v)=H_{\rm e}(C)+vH_{\rm o}(C),
$$
再定义
$$
 \mathscr H(H)=
 \begin{pmatrix}U_H\\V_H\end{pmatrix}
 =\begin{pmatrix}H_{\rm e}-u\beta^{-1}H_{\rm o}\\
                       \beta^{-1}H_{\rm o}\end{pmatrix}.
 \tag{5}
$$
这等价于唯一的表示 $H(v)=U_H(C)+\alpha(v)V_H(C)$。

双分量目标按原标号交错排列：$[C^n]U$ 的行号为 $2n$，$[C^n]V$ 的行号为 $2n+1$，相应归一分别为
$$
 p^{\lfloor2n/r\rfloor}[C^n]U,\qquad
 p^{\lfloor(2n+1)/r\rfloor}[C^n]V.
 \tag{6}
$$
**定理 2.1。** (5) 是这个完整连续目标的整下三角同构；其对角条目是 $v_0$ 的整数幂，均为单位。

**证明。** 令
$\nu_C(g)=\min_n(rv_p(g_n)+2n)$。由 $\alpha(\pi z)/\pi$ 整，
$$
 \nu_C(u)\ge1,\qquad \nu_C(\beta)\ge0,
 \qquad \nu_C(\beta^{-1})\ge0.
 \tag{7}
$$
奇偶拆分的对角因子是 $v_0^{-n}$。在奇行之间乘 $\beta^{-1}$，每个卷积条目的归一赋值非负。将奇分量乘 $u\beta^{-1}$ 后送到偶分量时，行号差比其 $C$ 次数的两倍少一，而 (7) 恰好补偿这一点。又 $u$ 无常数项，所以该交叉操作严格读较早行。逆变换 $H_{\rm o}=\beta V$、$H_{\rm e}=U+uV$ 同理。故两个有限矩阵都整且对角为单位。$\square$

这是一条统一的实际标量目标同构；没有按原齐次次数采用不同的规范化。

## 3. 实际二次关系及完整递推

置
$$
 T(C)=2u(C),\qquad
 N(C)=u(C)^2-\frac C{v_0}\beta(C)^2.
 \tag{8}
$$
于是
$$
 \alpha(v)^2-T(C)\alpha(v)+N(C)=0,
 \qquad T\in C\mathbf Q_p[[C]],\quad
 N=-C/v_0+O(C^2).
 \tag{9}
$$
这些是由原曲线定义的实际形式级数。定义
$$
 M(C)=\begin{pmatrix}0&-N\\1&T\end{pmatrix},\qquad
 \begin{pmatrix}U_a\\V_a\end{pmatrix}=M(C)^a\begin{pmatrix}1\\0\end{pmatrix}.
 \tag{10}
$$
则
$$
 U_0=1,V_0=0,\quad U_1=0,V_1=1,\qquad
 U_{a+1}=-NV_a,\quad V_{a+1}=U_a+TV_a.
 \tag{11}
$$
对每一个原单项式，准确有
$$
 \mathscr H(A^aC^b)=C^b\begin{pmatrix}U_a\\V_a\end{pmatrix}.
 \tag{12}
$$
因此全部原 $E_D$ 的有限像由同一 $T,N$ 的真实系数计算。这并未将 $T,N$ 的高尾变成独立源列。

## 4. 降两次原次数的显式 Schur 矩阵

以下设 $D\ge2$、$k>2D+1$。原核
$$
 K_D=\ker\partial_A^2
 =\operatorname{span}_O\{C^b:0\le b\le D\}
  \oplus\operatorname{span}_O\{AC^b:0\le b\le D-1\}
 \tag{13}
$$
在 (5) 的目标中恰是前 $2D+1$ 个标准单位列。这些行均小于 $r$，所以归一不额外乘 $p$。

令 $\operatorname{Low}_D(U,V)=(U_{\le D},V_{\le D-1})$，其余称为 $\operatorname{Tail}_D$。对原 $Q\in E_{D-2}$，定义实际源截面
$$
 \mathcal R_DQ=A^2Q-
  [\mathscr H(A^2Q)_U]_{\le D}(C)
  -A[\mathscr H(A^2Q)_V]_{\le D-1}(C).
 \tag{14}
$$
低项系数整，因为它们都是小于 $r$ 的已观察行的整组合；每个被减多项式总次数至多 $D$。因此
$$
 E_D=K_D\oplus\mathcal R_D(E_{D-2})
 \tag{15}
$$
是原整源同构。其与 R209 的 $\partial_A^2$ 右逆仅相差目标 $E_{D-2}$ 上的单位对角算子
$A^aC^b\mapsto(a+1)(a+2)A^aC^b$。

真正的余矩阵为
$$
 S_{D,k}(Q)=\operatorname{Tail}_D\left(M(C)^2\mathscr H(Q)\right),
 \tag{16}
$$
按 (6) 归一且只取标号 $<k$ 的全部连续行。因此
$$
 J_{D,<k}\sim_O I_{2D+1}\oplus S_{D,k}.
 \tag{17}
$$
若列标为 $A^aC^b\in E_{D-2}$，条目完全明确：
$$
 \begin{split}
 (S_{D,k})_{2n,(a,b)}
 &=p^{\lfloor2n/r\rfloor}[C^{n-b}]U_{a+2},
            &&D<n,\quad2n<k,\\
 (S_{D,k})_{2n+1,(a,b)}
 &=p^{\lfloor(2n+1)/r\rfloor}[C^{n-b}]V_{a+2},
            &&D\le n,\quad2n+1<k.
 \end{split}
 \tag{18}
$$
将最后任意未来行继续通过相同的整下三角目标变换和固定源 (14) 消元，仍得到它在严格前缀核内的同一个值理想。故 (17) 不只是有理秩分解。

## 5. 原删 C 商恰是这个小矩阵的删常数商

记
$$
 K_N(J,k)=\{P\in E_D:J_{<k}P\in p^NO^k\},\qquad
 \mathcal L_N(H)=\sum_i(N-s_i(H))_+.
$$
对 (15) 的分解 $P=K+\mathcal R_DQ$，真实前缀条件准确等价于
$$
 K\in p^NK_D,\qquad S_{D,k}Q\in p^NO^{k-2D-1}.
 \tag{19}
$$
由 (11)，$U_2=-N=C/v_0+O(C^2)$；而 $a\ge3$ 时 $U_a\in C^2\mathbf Q_p[[C]]$。所以 (14) 的原 $C$ 系数准确为
$$
 (\mathcal R_DQ)_C=-Q(0,0)/v_0.
 \tag{20}
$$
这里没有其他余列贡献这个系数。故对 $P\in K_N(J,k)$，
$$
 P_C\equiv-Q(0,0)/v_0\pmod{p^N}.
$$
删去 $S_{D,k}$ 的原常数 $Q=1$ 列，所得矩阵记 $S_{D,k}^{\setminus1}$。R206 的真实循环商论证于是给出
$$
 \boxed{\quad
 \{P_C:P\in K_N(J,k)\}=p^{a_N}O,\qquad
 a_N=\mathcal L_N(S_{D,k})-
                    \mathcal L_N(S_{D,k}^{\setminus1}).
 \quad}
 \tag{21}
$$
这把原 $C$ 门压到原次数 $D-2$ 的实际余源。其被删常数列正是
$$
 \mathbf c_{D,k}=
   \operatorname{Tail}_D\begin{pmatrix}-N\\T\end{pmatrix},
 \tag{22}
$$
使用 (6) 的实际偶、奇归一。特别 R206 第四层的 $a_3\ge2$ 问题，现在是这个双高尾列在其余真实余列模 $p^3$ 像中的准确阶问题；它仍没有被自动证明。

## 6. 真正的次数递推及两条边界行

设 $D\ge4$。将输入 $E_{D-2}$ 再按同一个原构造分解为
$K_{D-2}\oplus\mathcal R_{D-2}(E_{D-4})$，(16) 给出准确的整源等价
$$
 S_{D,k}\sim_O
 \left[\ G_{D,k}\quad
    \operatorname{Tail}_D\!\left(M^2\widetilde S_{D-2,k-2}\right)
 \right].
 \tag{23}
$$
$\widetilde S$ 表示把原低行补零后的完整双分量级数；乘 $M^2$ 只需输入标号 $<k-2$，故没有偷读未来行。

新增的 $2D-3$ 个列全部明确：
$$
 G_{D,k}=
 \left[
  \operatorname{Tail}_D C^b\binom{-N}{T}\ (0\le b\le D-2),\quad
  \operatorname{Tail}_D C^b\binom{-NT}{T^2-N}\ (0\le b\le D-3)
 \right].
 \tag{24}
$$
它们是原核 $K_{D-2}$ 在新的实际余矩阵中的像。它们的高尾一般一直延伸，不能把它们作为两个被删边界行一起丢掉。

为精确核算旧余矩阵的传递，观察
$$
 M^2=\mathcal U(C)\,\frac C{v_0}I,
 \qquad \mathcal U(C)=\frac{v_0}{C}M^2.
 \tag{25}
$$
$\mathcal U$ 是实际标量单位级数 $\alpha(v)^2/v^2$ 的双分量乘法矩阵。该单位及其逆的 ramified 加权系数都整，故它在 (6) 上是整下三角、对角为一。

旧余矩阵的首个可能非零行是 $2D-3$。乘 $C/v_0$ 后首行变为 $2D-1$，而新的 $\operatorname{Tail}_D$ 从 $2D+1$ 开始。因此 (23) 的旧余块只删除两个真实连续边界行 $2D-1,2D$；$\mathcal U$ 的低到高卷积仍完整保留。

记
$$
 c_{D,k}=\#\{m:2D-3\le m<k-2,
                  \ m\equiv r-2\text{ 或 }r-1\pmod r\}.
 \tag{26}
$$
乘 $C/v_0$ 在原标号 $m$ 上准确乘
$v_0^{-1}p^{\lfloor(m+2)/r\rfloor-\lfloor m/r\rfloor}$：其中恰有 $c_{D,k}$ 个额外 $p$。若 $q\ge1$，则
$c_{D,k}=2(q-1)+\min(s,2)$；若 $k<r$，该数为零。

对任意 $N\ge1$，令 (23) 中的旧余块为 $H_{D,k}$，则
$$
 \mathcal L_N(S_{D-2,k-2})-c_{D,k}-2N
 \le\mathcal L_N(H_{D,k})
 \le\mathcal L_N(S_{D-2,k-2}).
 \tag{27}
$$
证明是：目标单位 $\mathcal U$ 不改像长；一个目标坐标乘 $p$ 最多损失一个长度单位；投影删去两个目标坐标最多损失 $2N$。这些都应用于同一个实际像，而非独立源 summand。

把 (24) 的列也算入，得到完整且无遗漏的预算
$$
 \begin{split}
 \mathcal L_N(S_{D-2,k-2})-c_{D,k}-2N
 &\le\mathcal L_N(S_{D,k})\\
 &\le\mathcal L_N(S_{D-2,k-2})+N(2D-3).
 \end{split}
 \tag{28}
$$
等价地，原完整矩阵满足
$$
 \mathcal L_N(J_{D-2,<k-2})+2N-c_{D,k}
 \le\mathcal L_N(J_{D,<k})
 \le\mathcal L_N(J_{D-2,<k-2})+N(2D+1).
 \tag{29}
$$
这是真实源次数递推的有限像界。它没有比较中央实际曲线与比较曲线的收益方向。

## 7. 中央比较保留相同原源截面

现在取 R203 的中央比较 $(A^\circ,C^\circ)$。在共同原 $w$ 参数内，差满足
$$
 \operatorname{ord}(A-A^\circ),\operatorname{ord}(C-C^\circ)\ge r,
 \qquad \nu_\pi(A-A^\circ),\nu_\pi(C-C^\circ)\ge2r.
 \tag{30}
$$
分别用自己的平方根参数，得到 $\alpha,\alpha^\circ$，但把两个输出变量都写成 $v$。由取平方根和逆函数的整性，
$$
 \operatorname{ord}(\alpha-\alpha^\circ)\ge r-1,
 \qquad \nu_\pi(\alpha-\alpha^\circ)\ge2r-1.
 \tag{31}
$$
例如两个归一平方根 $v(\pi z)/\pi$ 的差在 $\pi^{2r-2}$ 中，逆函数保持这一精度；再复合 $A(\pi z)/\pi$ 即得后一界。第一界由相应普通形式阶得到。

记 $\delta T=T-T^\circ$、$\delta N=N-N^\circ$。奇偶拆分及 $\alpha$ 的加权阶至少一给
$$
 \begin{array}{ll}
 \operatorname{ord}_C\delta T\ge\lceil(r-1)/2\rceil\ge D,
       &\nu_C(\delta T)\ge2r-1,\\
 \operatorname{ord}_C\delta N\ge\lceil r/2\rceil\ge D+1,
       &\nu_C(\delta N)\ge2r.
 \end{array}
 \tag{32}
$$
递推 (11) 因而证明：对所有原单项式，两曲线的
$U_{\le D},V_{\le D-1}$ 完全相同。核列 (13) 在各自双分量目标中又都准确为相同的标准列。因此 **(14) 是两曲线共享的同一个原整源截面**，(21) 中被删的原常数列也保持相同身份。

更精确地，
$$
 \delta(M^2)=
 \begin{pmatrix}
  -\delta N&-\delta(NT)\\
  \delta T&\delta(T^2-N)
 \end{pmatrix}
 \tag{33}
$$
作为 (6) 的双分量目标算子，全部条目在 $p^2O$ 中，并且只读取至少早 $r$ 个原行号的输入。这里 $\delta T$ 从 $U$ 送到 $V$，行权额外加一，恰把 $2r-1$ 补成 $2r$；右上角则由 $N,T$ 的加权阶至少二、一补偿奇到偶少去的一。普通阶的延迟同理由 (32) 得到。

全矩阵差有准确递推
$$
 \boxed{\quad
 S_{D,k}-S^\circ_{D,k}
 =\operatorname{Tail}_D\left[
   \delta(M^2)\,\mathscr H^\circ_{D-2}
   +M^2(\mathscr H_{D-2}-\mathscr H^\circ_{D-2})
                         \right]_{<k}.
 \quad}
 \tag{34}
$$
全部分量按 (6) 归一。这里的 $\mathscr H_{D-2}$ 是同一原 $E_{D-2}$ 的完整双分量矩阵，包含其低行。不能把它直接替换成旧余矩阵 $S_{D-2}$；要这样做必须同时加入 (24) 的实际高尾列和 (23) 的两条边界行。

从 $D=0,1$ 的相同标准列出发，(33)–(34) 还直接证明全部双分量矩阵之差在 $p^2$ 中。因此
$$
 |\mathcal L_N(J_{D,<k})-\mathcal L_N(J^\circ_{D,<k})|
 \le(N-2)_+M_{D-2},
 \tag{35}
$$
与 R209 的 $j=1$ 界一致。这里的两曲线目标坐标不同，但每个变换都分别是已证明的实际整同构，所以有限像比较合法。

## 8. 原有样本的精确双分量校准

纯 JavaScript BigInt 证书
[check-quadratic-pair-schur.js](../scripts/check-quadratic-pair-schur.js)
从 R162 的原 $P,Q,W$ 有理系数重建同一个 $p=43,D=4$ 样本，准确取平方根、反演参数，并核 $C(v)=v_0v^2$ 至所需第 14 阶。完整输出见
[check-quadratic-pair-schur.json](../scripts/check-quadratic-pair-schur.json)。
这里有限阶 $s\leftrightarrow w$ 的整性已由 R206 在相同前缀核定；证书进一步同时核对原矩阵、双分量矩阵以及两者删原 $C$ 列的有限像。

| 原完整前缀 $k$ | $S_{4,k}$ 的 Smith 指数 | 删常数余列 | $\mathcal L_3(S)$ | $\mathcal L_3(S^{\setminus1})$ | 原 $a_3$ |
| --- | --- | --- | ---: | ---: | ---: |
| 14 | $0^3,1^2$ | $0^2,1^3$ | 13 | 12 | 1 |
| 15 | $0^4,1^2$ | $0^3,1^2$ | 16 | 13 | 3 |

两个原完整矩阵都准确分出 $I_9$，故相应原像长为 $40,43$，与 R206 一致。这验证了 (18) 的真实行归一、(17) 的原源分裂和 (21) 的同一个删列循环商。没有扩大素数样本，也没有把 $p=43$ 当成双完整中央零样本。

## 9. 定向比较的具体剩余对象

(18)、(21)、(24)、(34) 给出了不含独立 latent 源的实际递推。原第四层删 $C$ 门已准确化成次数 $D-2$ 余矩阵中双高尾列 (22) 的循环商。要证明 $a_3\ge2$，必须证明该列在其余真实列模 $p^3$ 的商中具有至少 $p^2$ 的阶；单凭 $\delta T,\delta N$ 在 (32) 中的精度，仍不能给出这个结论。

同样，(34) 没有规定像长度差的符号。每一递推步的两条边界行已经在 (27) 中付清，而新增的 (24) 列仍必须保留其真实重叠关系。把 $T,N$ 的高尾删掉、把它们当成互相独立可调列、或把 $S_D$ 直接认作原 $J_{D-2}$，都会丢失这个尚未支付的定向问题。

## 10. 使用 R215 原行权后的全深结构

§1 的深度限制针对旧行权 $\lfloor n/r\rfloor$。现采用
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)
已经证明的原全深行权
$$
 e_n=\begin{cases}
 0,&h=\lfloor n/r\rfloor=0,\\
 h+\lfloor(h-1)/(p-1)\rfloor,&h\ge1.
 \end{cases}
 \tag{36}
$$
该权单调且超可加。以下仍保留 $r>2D$，但不再限制完整前缀长度 $k$。所有 $J_n$、偶行和奇行分别改用 $p^{e_n}$、$p^{e_{2n}}$、$p^{e_{2n+1}}$。

**定理 10.1。** 对这个原全深权，§2–6 的统一目标整同构、同一个原源分裂 (14)–(17)、实际高尾矩阵 (18)、原删 $C$ 商 (21)，以及完整递推 (23)–(25)，对任意有限 $k$ 均成立。

**证明。** 写
$$
 \mathscr B_e=\{\sum h_nw^n:v_p(h_n)\ge-e_n\}.
$$
R215 的原等式 $a=B(s)$、$b=sa$ 给 $B\in\mathscr B_e$。原固定齐次多项式满足
$$
 A=a^{17}P(s),\qquad C=a^{17}Q_C(s),\qquad
 P(s)=s+\cdots,\quad Q_C(s)=v_0s^2+\cdots,
$$
且它们的固定分母在当前素数处都是单位。因此在原 $s$ 参数内，
$A/s,C/(v_0s^2)\in\mathscr B_e$。R215 的 $s\leftrightarrow w$ 严格换元、逆单位以及超可加性遂给
$$
 A(w)/w,\qquad C(w)/(v_0w^2)\in\mathscr B_e.
 \tag{37}
$$
这个成本环对乘法、常数项为一的逆、严格复合和严格逆参数封闭；证明均为逐阶整加乘，并用成本下标之和等于总下标。常数项为一的平方根也封闭：其递推只除以单位二。于是
$$
 v(w)/w,\qquad w(v)/v,\qquad\alpha(v)/v\in\mathscr B_e.
 \tag{38}
$$
第一项及严格逆证明全深的共同加权目标变换仍为整下三角单位。

对 (4) 的实际系数，(38) 精确给
$$
 v_p([C^n]u)\ge-e_{2n-1}\ (n\ge1),\qquad
 v_p([C^n]\beta),\ v_p([C^n]\beta^{-1})\ge-e_{2n}.
 \tag{39}
$$
乘 $u\beta^{-1}$ 的第 $C^d$ 个系数成本至多 $e_{2d-1}$。这正是奇到偶操作的原行号差；乘 $\beta^{\pm1}$ 的成本则是相应偶数行差。由
$e_j-e_i\ge e_{j-i}$，(5) 及其逆在所有有限前缀上都整。该论证保留了首项单位给出的精确下标差，不能仅用较粗的原 $A,C$ 行整性替代。

因为 $e_n=0$ 对所有 $n\le2D<r$ 成立，低核 (13) 仍是前 $2D+1$ 个标准单位列；(14) 的原系数仍整。全部原源与有限像恒等式随即成立。最后 $\alpha(v)^2/v^2$ 及其逆属于 $\mathscr B_e$，故 (25) 的乘法在全深权下仍为单位目标操作。$\square$

递推的两条边界行仍是 $2D-1,2D$；跨权成本现在应精确写为
$$
 c_{e,N}(D,k)=\sum_{m=2D-3}^{k-3}
              \min\{N,e_{m+2}-e_m\}.
 \tag{40}
$$
因此 (27)–(29) 在全深成立，只需将 $c_{D,k}$ 替换为 $c_{e,N}(D,k)$。每个实际目标坐标乘 $p^{e_{m+2}-e_m}$ 至多损失
$\min\{N,e_{m+2}-e_m\}$ 个模 $p^N$ 长度单位，这解释了 (40) 中必须保留的截断。

超可加性保证每项非负，而望远镜相消给显式上界
$$
 \begin{split}
 c_{e,N}(D,k)
 &\le\sum_{m=2D-3}^{k-3}(e_{m+2}-e_m)\\
 &=e_{k-2}+e_{k-1}-e_{2D-3}-e_{2D-2}
 =e_{k-2}+e_{k-1}.
 \end{split}
 \tag{41}
$$
在原第一带中，每个跳跃只有零或一，故所有 $N\ge1$ 的 (40) 都退化为 (26) 的
$2(q-1)+\min(s,2)$。

本节只延长实际坐标、源分裂、删列商和递推预算。§7 的中央比较 (30)–(35) 仍限于它原有的第一带输入；R215 的全深行整性本身没有给出全深中央差、双尾消失或新的定向收益。
