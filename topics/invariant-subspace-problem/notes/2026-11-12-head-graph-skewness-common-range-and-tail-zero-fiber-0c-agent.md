# R208 附录：首位闭图的反对称性、共同闭值域和尾部联合零纤维

日期：2026-11-12（UTC）。作者：critical_kernel。

状态：完整实际必要条件。以下只使用已证的首位核图、R208 全等向性和明确的域内双线性恒等式。没有把慢一阶分母的全空间稠密像提升为不变限制上的稠密像，也没有假定最大闭商等于其最小参数图闭包。

## A. 两种已证首位接口

把原空间按首物理位分成
$$
H=\mathbb C^2\otimes\widehat H.
$$
在此分解下，总共轭和双线性型为
$$
C(x,y)=(\widehat C y,\widehat C x),
$$
$$
B((x,y),(u,v))
=\widehat B(x,v)+\widehat B(y,u),
\qquad
\widehat B(x,y)=\langle x,\widehat Cy\rangle.
\tag{A.1}
$$

使用如下已经在 R143 附录及首位四阶消元记录中证明的实际结构。
设原核 $M$ 中的两个分量均属于闭尾空间 $\mathcal K$，且在 $\mathcal K$ 上有交换的有界算子
$$
A_0,\ B_0,\ t,\qquad
(A_0^2-tB_0^2)|_{\mathcal K}=0.
\tag{A.2}
$$
$B_0$ 单射。$A_0,B_0$ 在 $\mathcal K$ 的向量对上具有真实双线性对称性：
$$
\widehat B(A_0x,y)=\widehat B(x,A_0y),\qquad
\widehat B(B_0x,y)=\widehat B(x,B_0y)
\quad(x,y\in\mathcal K).
\tag{A.3}
$$
这里不要求 $\widehat C\mathcal K=\mathcal K$。

原核满足准确的实际块方程
$$
A_0x+tB_0y=0,\qquad B_0x+A_0y=0.
\tag{A.4}
$$
在以下两种具体应用中，$M$ 恰为 (A.4) 在 $\mathcal K\oplus\mathcal K$ 中的解集，而不只是满足其必要方程。若整体乘子无界，$\mathcal K$ 的全幂域结论保证这些解已落在原乘子的真实自然域中；不能仅从一个形式块矩阵引用此充要性。

令
$$
L=\overline{\{x:(x,y)\in M\}}
 =\overline{\{y:(x,y)\in M\}}\subseteq\mathcal K.
\tag{A.5}
$$
两个闭包相等来自真实 $A$ 不变性及尾移位在每个不变限制上的稠密像。
$L$ 对 $A_0,B_0,t$ 不变，这些算子在 $L$ 上仍有界。
具体的首位四阶情形还对有界的尾第一阶限制 $W|_{\mathcal K}$ 不变。

本文额外假设
$$
B(M,M)=0,
\tag{A.6}
$$
这在 R208 的危险平方分支中已证明。

## B. 最大头图的域和两个稠密投影

在 $L$ 上定义
$$
\mathcal D=\{y\in L:A_0y\in B_0L\},\qquad
Jy=x\ \Longleftrightarrow\ B_0x=A_0y,\quad x\in L.
\tag{B.1}
$$
由于 $B_0$ 单射，$J$ 单值。此处的 $B_0^{-1}$ 只作用于 $B_0L$，没有使用有界逆。

由 (A.2)，若 $y\in\mathcal D$，则 $(-Jy,y)$ 满足第二个块方程。
把第一个块方程左边乘以 $B_0$，得到
$$
-B_0A_0Jy+tB_0^2y
=-A_0^2y+tB_0^2y=0.
$$
再由 $B_0$ 单射，第一式也成立。
结合 (A.4)，得到完整参数式
$$
\boxed{M=\{(-Jy,y):y\in\mathcal D\}.}
\tag{B.2}
$$
因此 $J$ 闭，且 (A.5) 精确给出
$$
\boxed{\overline{\mathcal D}=L,\qquad
\overline{J\mathcal D}=L.}
\tag{B.3}
$$
这是两个普通范数闭包，不是尚未证明的参数图核心。

对任意 $z\in L$，交换性给
$$
A_0B_0z=B_0A_0z,
$$
所以
$$
\boxed{B_0L\subseteq\mathcal D,\qquad JB_0z=A_0z.}
\tag{B.4}
$$
若再取 $z\in\mathcal D$，由 $A_0z=B_0Jz$ 得
$$
\boxed{JB_0z=B_0Jz\qquad(z\in\mathcal D).}
\tag{B.5}
$$
因此后面的每次 $J B_0$ 运算都有真实定义域依据。

## C. 新反对称性不要求尾空间受共轭保持

把 (B.2) 代入 (A.1)、(A.6)，得到
$$
0=-\widehat B(Ju,v)-\widehat B(u,Jv)
\qquad(u,v\in\mathcal D).
$$
即
$$
\boxed{
\widehat B(Ju,v)=-\widehat B(u,Jv)
\qquad(u,v\in\mathcal D).
}
\tag{C.1}
$$

(C.1) 是域内双线性反对称等式。
由于尚未证明 $\widehat CL=L$，它不是一个已经识别的 $L$ 上反自伴算子结论。
也不能由它断言 $J$ 的通常伴随与 $J$ 同域。

全尾最大商若另有 $C$ 对称实现，当然还能提供正号的双线性等式。
但当前慢分母情形并未建立那个最大图的参数核心；
R143 附录的相应充分条件要求分母在全部有限放大不变空间上稠密，
R183 则只覆盖其明确的快系数分式类。
以下结论不依赖这些额外条件。

## D. 加权对称性与两次稠密极限

虽然 $J$ 本身尚无正号对称等式，$B_0J=A_0$ 的加权对称性完全实际。
对 $u,v\in\mathcal D$，(A.3) 给
$$
\begin{aligned}
\widehat B(Ju,B_0v)
&=\widehat B(B_0Ju,v)\\
&=\widehat B(A_0u,v)\\
&=\widehat B(u,A_0v)\\
&=\widehat B(B_0u,Jv).
\end{aligned}
\tag{D.1}
$$
另一方面，$B_0u\in\mathcal D$，故 (C.1)、(B.5) 给
$$
\begin{aligned}
\widehat B(B_0u,Jv)
&=-\widehat B(JB_0u,v)\\
&=-\widehat B(B_0Ju,v)\\
&=-\widehat B(Ju,B_0v).
\end{aligned}
$$
因此
$$
\widehat B(Ju,B_0v)=0\qquad(u,v\in\mathcal D).
\tag{D.2}
$$

先用 $J\mathcal D$ 在 $L$ 中稠密；
再用 $\mathcal D$ 在 $L$ 中稠密和 $B_0|_L$ 有界，
得到
$$
\boxed{\widehat B(L,B_0L)=0.}
\tag{D.3}
$$
这里没有取消 $B_0$，也没有声称 $B_0L$ 已经稠密于 $L$。

还可准确比较两个闭像。
由于 $A_0|_L$ 有界、$\mathcal D$ 稠密，
$$
\overline{A_0L}=\overline{A_0\mathcal D}.
$$
又 $A_0\mathcal D=B_0J\mathcal D$，而 $J\mathcal D$ 稠密于 $L$，
所以
$$
\boxed{
N:=\overline{B_0L}=\overline{A_0L}.
}
\tag{D.4}
$$
若 $M\ne0$，则 $L\ne0$；$B_0$ 单射保证 $N\ne0$。
(D.3) 因连续性进一步给
$$
\boxed{
0\ne N\subseteq L\cap(\widehat CL)^\perp.
}
\tag{D.5}
$$
特别 $N$ 自身全等向。

$N$ 为闭尾移位不变空间：
$B_0$ 与尾移位交换，且尾移位保持 $L$。
在具体四阶情形，$N$ 还受 $W|_L$ 和所有相关有界系数保持。

## E. 危险平方的真实四阶实例

这里沿用首位四阶消元记录的记号，假设最低非零系数位已作为首物理位处理。
写
$$
X=aV_0+W,\qquad
Z=\sum_{j\ge1}a_j^2(I-V_j^2),\qquad
t=\eta_0N_1,\qquad
s=(I+t)(I-t)^{-1}.
$$
真正的平方乘子为
$$
P=X^2+\mathcal B_2-a^2I.
$$
其核在自然域内满足
$$
P=
\begin{pmatrix}
A_0&tB_0\\ B_0&A_0
\end{pmatrix},
$$
$$
A_0=W^2+2asW+Z,\qquad
B_0=-4a(I-t)^{-1}W.
\tag{E.1}
$$
尾行列式为
$$
\Delta=A_0^2-tB_0^2
=W^4+4asW^3+(2Z+4a^2I)W^2+4asZW+Z^2.
$$
R176 的 monic 闭域结论给
$$
\mathcal K=\ker\Delta
\subseteq\bigcap_{r\ge1}\operatorname{Dom}W^r,\qquad
W|_{\mathcal K}\in B(\mathcal K).
\tag{E.2}
$$
因此 (E.1) 的所有系数在 $\mathcal K$ 上有界。
$W$ 的全尾单射性给 $B_0$ 单射。

各实际有界尾系数都与 $W$ 完整域交换并为 $\widehat C$ 对称。
由 (E.2)，可对 $x,y\in\mathcal K$ 逐项移动 $W,W^2$，
所以 (A.3) 成立。
这没有把 $W|_{\mathcal K}$ 当作 $\mathcal K$ 上某个已知共轭下的自伴算子。

首位消元已经证明原核的两坐标均在 $\mathcal K$，
投影闭包 $L$ 受 $W|_{\mathcal K}$ 和上述尾系数保持。
R208 给 $M=\ker P$ 全等向，因此 B–D 节全部适用。

记 $U=-4a(I-t)^{-1}$。
$U,U^{-1}$ 均属于尾范数代数并保持 $L$。
它们也保持 $\overline{WL}$，因为与 $W$ 交换。
由 $B_0=UW$，
$$
\boxed{N=\overline{WL}=\overline{A_0L}.}
\tag{E.3}
$$
从 (E.1) 还得到
$$
Z=A_0-W^2-2asW
$$
在 $L$ 上的有界等式。右边三项的像都在 $N$ 中，故
$$
\boxed{ZL\subseteq N.}
\tag{E.4}
$$

于是对可能为零的闭尾子商
$$
Q=L/N,
$$
由有界 $W|_L$ 和 $Z|_L$ 诱导的算子同时满足
$$
\boxed{W_Q=0,\qquad Z_Q=0.}
\tag{E.5}
$$
这里 $W_Q$ 指这个明确有界限制再商，不是未经识别的另一最大闭尾实现。

若 $Q\ne0$，(E.5) 是一个具体的联合零纤维：
同一 Haar 尾子商上，一阶行和对应 Bell 二阶尾同时消失。
若 $Q=0$，则 $N=L$，(D.5) 迫使整个尾投影空间 $L$ 全等向。
本文不在这两个可能之间作未经证明的选择。

## F. 全空间联合循环尚不排除该尾商

R125 的全空间第一阶单射稠密、R144 的点态纯幂循环性，
以及 R145/R180 的全空间有限 gauge 联合循环性，
都不能直接排除 (E.5)。
它们没有断言当前慢 $W,Z$ 在每个指定尾子商上的联合强主理想包含单位。

具体地，已知 $W$ 在全尾空间单射稠密，
仍不自动给
$$
\overline{W L}=L.
$$
同样，某个由 $W^2+Z$ 正则化得到的有界全空间拟仿射，
并不自动在此 $L/N$ 上单射。
R140/R153 的强主理想机制可用于其明确覆盖的系数或分母类，
但一般慢行没有被归入那些类。

本附录把原先一个未定的最大图对称性问题，
替换成无需该对称性的闭像正交结论 (D.3)–(D.5)。
(E.5) 是接下来的准确子商问题，而不是已经解决的矛盾。

## G. 实系数时的偶奇图与有限头成本

若所有系数为实数，危险平方的分支可取实系数全纯支，
故逐点复共轭 $J_0$ 保持 $M$。
令
$$
R=CJ_0,\qquad R\chi_F=(-1)^{|F|}\chi_F.
$$
R208 给
$$
\langle v,Rw\rangle=0\qquad(v,w\in M).
$$
偶、奇 Walsh 投影 $P_+,P_-$ 因而满足
$$
\langle P_+v,P_+w\rangle
=\langle P_-v,P_-w\rangle
=\tfrac12\langle v,w\rangle.
$$
所以存在两个闭子空间 $M_\pm$ 之间的酉同构 $U$，使
$$
M=\{x+Ux:x\in M_+\}.
\tag{G.1}
$$
共同复相位的行经整体标量化也有相同结论。
一般复行不自动受 $J_0$ 保持，因此不自动享有 (G.1)。

R207 的有限头条件期望与 $R$ 交换，但 (G.1) 不给有限头横截角的下界。
例如 $R e_{0,m}=e_{1,m}$，而 $M\perp RM$ 只给
$$
\|P_Me_{0,m}\|^2+\|P_Me_{1,m}\|^2\le1.
$$
这不能把全一头的下界转成全零头的下界。
故 R207 的指数成本与当前偶奇图条件之间，尚无已经建立的矛盾。
