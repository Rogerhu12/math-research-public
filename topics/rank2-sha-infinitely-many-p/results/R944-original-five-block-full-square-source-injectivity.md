# R944 — 第五原输入的四长窗与完整平方子源的单射

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

**状态：下列同一原来源的完整核定理已证明。** R943 已付第五合法中央和旧完整来源的五块物理评价。本篇使用新增的第四个真实长窗，将 R939 的完整平方核从可能的四次来源进一步压到五次来源；在显示次数门下，它严格为零。它不把五个中央条件本身当作已存在的五层深核，也不把一般来源拆成各自入核的分量。

## 1. 原完整来源与五块的准确首核

保 [R938](R938-original-full-source-finite-offsets-and-affine-carry.md)、[R939](R939-original-three-long-full-square-kernel.md) 的同一十九角曲面 \(X\)、几何整 Cartier 曲线 \(C=(F)\)、光滑物理点 \(P_C=(0,1)\)，及完整原来源

\[
 \mathcal W=H^0(X,\mathcal O_X(B_D)),\qquad
 \kappa=C^2>0,\qquad d_D=B_D\cdot C .
 \tag{1}
\]

令 \(\mathcal E=Y\partial_Y\)，同一个 \(e=\mathcal EF\) 在 \(P_C\) 为单位；\(t\) 为原横坐标，\(\mathcal E(t)=0\)。原支为 \(Y=\psi(t)\)，实际原低轴为 \(g(t)\)，且

\[
 \operatorname{ord}_t(g-\psi)=
 \operatorname{ord}_t F(t,g)=h.
 \tag{2}
\]

不改变 \(P_{134}\)、charge40、固定分母、角帽或原 \(W_D\)。在 [R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)(66)–(71) 的整个物理矩阵中，\(w^{13}\) 后四个满块及末短块，经全部原公共单位和 charge 的可逆三角运输，给准确首核

\[
 K_5=\{R\in\mathcal W:
  (\mathcal E^iR)(t,g)\in t^N k[[t]]\ (0\le i\le3),\
  (\mathcal E^4R)(t,g)\in t^\ell k[[t]]\},
 \qquad N=s-13 .
 \tag{3}
\]

因 \(w/t\) 为单位，物理长度可以在 \(t\) 中读取。这里没有除掉原 \(w^{13}\) 后补回未读行；四个满块各自的真实长度就是 \(N\)，短块长度就是 \(\ell\)。\(1,a_p,a_p^2/2,a_p^3/6,a_p^4/24\) 都是单位。物理52跨界成本和较高页的全部原 carry 仍在 R943，不在 (3) 被删去。

采用旧负 fringe 的已付窗口

\[
 \begin{gathered}
 s=2h+d_0+2,\quad 1\le d_0\le13,\quad h>21,\\
 T=s-15,\quad h<T\le2h,\quad T-h>\kappa,\\
 T-h\le \ell-2\le h .
 \end{gathered}
 \tag{4}
\]

本证明实际使用的长度条件是

\[
 h<N,\qquad N\le2h+2,\qquad
 \ell\le h+2,\qquad h+\ell\ge N.
 \tag{5}
\]

(4) 蕴含 (5)。所有原素数与有限坏集门仍保，特别 \(p>211\)。

对 \(m=2,3,4,5\)，定义完整子源

\[
 \mathscr D_m=
 F^mH^0(X,\mathcal O_X(B_D-mC))\subset\mathcal W .
 \tag{6}
\]

它们不是某几个 native 列，也不是只在物理支上被 \(F^m\) 整除的 germ。

## 2. 零角及有限 Euler Taylor 的统一精度

原完整十九角中的零角仍给

\[
 v_0(F)=-3,\quad v_0(R)\ge-2,\qquad
 v_0\!\left(\sum_nH_n(t)Y^n\right)
   =\min_n(4\operatorname{ord}_tH_n-n).
 \tag{7}
\]

若 \(R=F^mH\in\mathscr D_m\)，则 \(v_0(H)\ge3m-2\)。因此在原固定 \(d\) 分母为单位的 \(t=0\) 环中，

\[
 \begin{array}{c|c}
 m&\text{整个乘子的逐系数含因子}\\ \hline
 2&H=t c+O(t^2),\quad c\in k\\
 3&H\in t^2k[[t]][Y]\\
 4&H\in t^3k[[t]][Y]\\
 5&H\in t^4k[[t]][Y].
 \end{array}
 \tag{8}
\]

第一行中 \(t^1\) 的系数只能是常数：\(4-n\ge4\) 迫 \(n=0\)。其它十八角仍由完整 (6) 保留。

若 \(R=F^2H\in K_5\)，第二 Euler 行的 \(t^1\) 系数为 \(2e(P_C)^2c\)。其余含 \(F(t,g)\) 的项阶至少 \(h+1>1\)，故由 (3) 该单位倍必须为零。因此

\[
 R\in K_5\cap\mathscr D_2
 \quad\Longrightarrow\quad
 H\in t^2k[[t]][Y].
 \tag{9}
\]

这也是 R939 的原零角机制；新增的是本篇在同一来源上实际可用的第四长行。

为避免特征 \(p\) 的无限对数，取 \(\delta=g-\psi\)，写 \(\mathcal E=a(t,Y)\partial_Y\)，其中本题 \(a=Y\)，令

\[
 \eta=\delta/a(t,\psi),\qquad\operatorname{ord}_t\eta=h.
\]

对于逐系数含 \(t^k\) 的任何实际来源 \(S\) 及其有限 Euler 导数，有

\[
 \begin{aligned}
 S(t,g)&=S|_C+\eta(\mathcal ES)|_C+O(t^{2h+k}),\\
 S|_C&=S(t,g)-\eta(\mathcal ES)(t,g)+O(t^{2h+k}).
 \end{aligned}
 \tag{10}
\]

这是一次普通有限 Taylor；\(a(t,g)-a(t,\psi)\) 的差也含 \(\delta\)，已计入二次误差。固定分母在此为单位，且 \(\mathcal E(t)=0\)，所以所有所用有限导数保持 \(t^k\)。没有把 \(\delta\) 当成 Euler 位移而漏掉 \(a\)。

## 3. 新第四长窗迫完整平方来源进入四次来源

假设明确次数门

\[
 d_D-2\kappa<N .
 \tag{11}
\]

取 \(R=F^2H\in K_5\cap\mathscr D_2\)。由 (9)，\(R\) 及其导数都逐系数含 \(t^2\)。将 (10) 用于 \(S=\mathcal E^2R\)，由 (3) 的第二、第三 Euler 长行及 \(N\le2h+2\)，得到

\[
 (\mathcal E^2R)|_C\in t^Nk[[t]].
\]

但在同一个 \(C\) 上准确有

\[
 (\mathcal E^2(F^2H))|_C=2e^2H|_C .
 \tag{12}
\]

于是 \(H|_C\) 是次数 \(d_D-2\kappa\) 的真实全球截面，且在 \(P_C\) 消到 \(N\)。由 (11)，它必须恒零；完整 Cartier 限制核给 \(H=FK\) 且 \(K\in H^0(B_D-3C)\)。这得到 \(R\in\mathscr D_3\)，没有假设限制满射。

现在由 (8) 的 \(m=3\)，\(K\) 逐系数含 \(t^2\)。对 \(S=\mathcal E^3R\) 用 (10)。原第三 Euler 长行深 \(N\)，原第四 Euler 短行深 \(\ell\)，而 \(h+\ell\ge N\)，所以

\[
 (\mathcal E^3R)|_C\in t^Nk[[t]].
\]

准确乘积公式为

\[
 (\mathcal E^3(F^3K))|_C=6e^3K|_C .
 \tag{13}
\]

(11) 自动给 \(d_D-3\kappa<N\)，故同样 \(K|_C=0\)，从而 \(R\in\mathscr D_4\)。于是

\[
 \boxed{K_5\cap\mathscr D_2=K_5\cap\mathscr D_4
          \quad\text{在 (5)、(11) 下。}}
 \tag{14}
\]

这里第二次相继除 \(F\) 正是实际新增长行与原第五短行共同支付的；旧 R939 三长系统没有这一步的同样强度。

## 4. 四次来源的准确剩余核及真实限制像

令 \(R=F^4L\in\mathscr D_4\)。由 (8)，\(L\) 逐系数含 \(t^3\)。沿 \(C\) 的前四个 Euler 值都为零，而

\[
 (\mathcal E^4R)|_C=24e^4L|_C .
 \tag{15}
\]

应用 (10) 和 (5)，得到

\[
 \begin{aligned}
 (\mathcal E^iR)(t,g)&\in t^N k[[t]]\quad(0\le i\le2),\\
 (\mathcal E^3R)(t,g)
   &=24e^4\eta L|_C+O(t^{2h+3}),\\
 (\mathcal E^4R)(t,g)
   &=24e^4L|_C+O(t^{h+3}).
 \end{aligned}
 \tag{16}
\]

最后误差已包含 \(\mathcal E^5R|_C\) 的全部乘积项，因其逐系数含 \(t^3\)。\(\ell\le h+2\) 使短行准确等价于 \(L|_C\) 深到 \(\ell\)；这个条件再由 \(h+\ell\ge N\) 使第三 Euler 长行通过。故

\[
 \boxed{
 K_5\cap\mathscr D_4=
 \{F^4L:L\in H^0(X,\mathcal O_X(B_D-4C)),\
            \operatorname{ord}_{P_C}L|_C\ge\ell\}.
 }
 \tag{17}
\]

尤其所有完整 \(\mathscr D_5\) 都在 (17) 中。限制映射的准确核是 \(F H^0(B_D-5C)\)，所以在 (11) 下有注入

\[
 \frac{K_5\cap\mathscr D_2}{\mathscr D_5}
 \hookrightarrow
 H^0\!\left(C,\mathcal O_C(B_D-4C)(-\ell P_C)\right).
 \tag{18}
\]

右侧只为实际全球限制像的容器；没有把它的全部截面认作原来源像。特别

\[
 \dim(K_5\cap\mathscr D_2)-\dim\mathscr D_5
 \le\max(0,d_D-4\kappa-\ell+1).
 \tag{19}
\]

这个上界使用几何整曲线上线束的基本 \(h^0\le\deg+1\)，不要求 \(H^1(B_D-4C)=0\)。

**定理。** 若 (4)、(11) 成立，且

\[
 d_D-4\kappa<\ell,
 \tag{20}
\]

则准确有

\[
 \boxed{K_5\cap\mathscr D_2=\mathscr D_5.}
 \tag{21}
\]

若另外

\[
 d_D<5\kappa,
 \tag{22}
\]

则整个完整平方子源上的五块物理首核为零。

证明最后一句：\(C\) 是光滑曲面上的几何整有效曲线且 \(C^2>0\)。它和任意其它整曲线的交数非负，和自身交数正，因此 \(C\) nef。若 \(H^0(B_D-5C)\) 有非零截面，其有效零除子与 \(C\) 的交数为 \(d_D-5\kappa<0\)，矛盾。于是 \(\mathscr D_5=0\)。证毕。

## 5. 原整矩阵中的实际收益与使用边界

在 (20) 下，原五块矩阵在完整 \(\mathscr D_2\) 子块上的单位 Smith 秩为

\[
 \dim\mathscr D_2-\dim\mathscr D_5.
 \tag{23}
\]

(22) 下它等于 \(\dim\mathscr D_2\)。这是同一原矩阵约化的真实秩，任何与其它子块的比较都必须先取联合像；不能与 R834 或 R939 的旧秩下界相加。若未通过 (20)，只能使用 (19) 的余像上界。

例如，在确实满足原窗口及

\[
 \frac h\kappa\longrightarrow\frac98,\quad
 \frac N\kappa\longrightarrow\frac94,\quad
 \frac\ell\kappa\longrightarrow\frac98,\quad
 d_D=4\kappa+o(\kappa)
 \tag{24}
\]

的一族原来源上，(11)、(20)、(22) 对充分大 \(\kappa\) 都严格成立。这是条件性的实际尺度核对，不宣称所有待处理来源都具有 (24)。

若两个同一指定目标的五块解之差确实属于完整 \(\mathscr D_2\)，则 (22) 下它们相等；差在该子源中的成员性必须实际证明。仍不能从 \(\jmath G+V_2\in K_5\) 推出 \(\jmath G\) 和 \(V_2\) 分别入核。

若另起真正的 \(F^5\) 候选，其原有效预算可能要求 \(d_D\ge5\kappa+3r\)；此时不能借用 (22)。更一般的原 \(W_D/\mathscr D_2\)、非平方来源、实际有限类、原固定强迫项与较高页仍须联合处理。

本篇没有从五条原中央零免费构造任何深核。R943 的五轴唯一必要条件、四长物理首核及52成本是三个不同的已付对象；本篇只给其中这个完整子源的精确首核与单位秩，后续仍回到同一个原 \(P/R/S\) 及全部 carry。
