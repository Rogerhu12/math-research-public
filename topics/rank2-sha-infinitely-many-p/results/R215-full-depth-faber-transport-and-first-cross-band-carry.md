# R215 — 全深原 theta 前缀的 Faber 运输、首跨带 carry 与积分成本

日期：2026-11-12。**状态：全深分母界、同一原源全部归一行的整单位运输、首跨带 carry 及有限 Laurent 原函数成本均已证明。它们没有给新的中央非零或净 Smith 收益。**

[R212](R212-negative-witt-grunsky-and-original-prefix-transport.md) 的几何核整性只直接覆盖第一带。本篇把其目标运输延伸到所有深度，并补出一个不能直接从 R173 引用的结论：原完整 $w$ 系数矩阵也可使用 R173 的全部行权整化。证明保留原 $E_D$，不对各齐次次数分别选 gauge。

## 1. 固定几何与原行权

取
$$
 E_0:y^2=x^3-x,\quad \omega=dz=\frac{dx}{2y},\quad
 s=x^{-2},\quad T=x^2=s^{-1},\quad w=z^4,
$$
以及惰性素数
$$
 p=4r-1\ge7,\qquad R=\frac{p^2-1}{4}=r(p-1).
$$
纯几何证明只需上述条件；与当前原双 theta 分支的其余结果共同使用时，仍保留该分支的 $p\ne11$ 限制。

原严格换元为
$$
 W(s)=sF(s)^4=w,\qquad
 F(s)=\sum_{j\ge0}F_js^j,\qquad
 F_j=\frac{\binom{2j}{j}}{4^j(4j+1)}.
 \tag{1}
$$
定义两种成本
$$
 \delta_j=\left\lfloor\frac jR\right\rfloor,
 \qquad
 e_j=
 \begin{cases}
 0,&\lfloor j/r\rfloor=0,\\
 \lfloor j/r\rfloor+
 \left\lfloor\frac{\lfloor j/r\rfloor-1}{p-1}\right\rfloor,
 &\lfloor j/r\rfloor\ge1.
 \end{cases}
 \tag{2}
$$
R173 已证明 $e$ 单调、超可加：
$$
 e_{i_1}+\cdots+e_{i_t}\le e_{i_1+\cdots+i_t}.
 \tag{3}
$$
$\delta$ 也有此性质，且 $\delta_j\le e_j$。因此
$$
 e_j-e_i\ge e_{j-i}\ge\delta_{j-i}\qquad(0\le i\le j).
 \tag{4}
$$

必须区分 R173 已有的两个输入：它给原图形参数 $b$ 下的全部行整性，以及原 $w$ 参数下消去全部低阶后的真实 jet 范数。它没有直接宣称未消元的全部 raw $w$ 行同样整。本篇第 4 节给出这一步的完整换元证明。

## 2. 原椭圆对数的全深分母

**命题 1。** 对全部 $j\ge0$，
$$
                     v_p(F_j)\ge-\delta_j.                  \tag{5}
$$
而在 $0\le j<2R$ 中，唯一可能非整的系数是 $F_R$，且
$$
                         pF_R\equiv-1\pmod p.               \tag{6}
$$

**证明。** 令 $h=v_p(4j+1)$。$h=0$ 时结论显然。若 $h\ge1$，$j$ 的最低 $h$ 个 $p$ 进数码由 $4j+1\equiv0\pmod{p^h}$ 唯一决定。从最低位开始，它们交替为
$$
                         3r-1,\ r-1,\ 3r-1,\ r-1,\ldots .
$$
将 $j$ 与自身相加时，高位 $3r-1$ 必进一位，而下一位满足
$2(r-1)+1=2r-1<p$。因此这 $h$ 位至少产生 $\lceil h/2\rceil$ 次进位。由阶乘赋值公式（等价于二项式的进位公式），
$$
 v_p\binom{2j}{j}\ge\lceil h/2\rceil,\qquad
 v_p(F_j)\ge-\lfloor h/2\rfloor.
 \tag{7}
$$
若 $a=\lfloor h/2\rfloor\ge1$，则
$$
 j\ge\frac{p^{2a}-1}{4}
   =R(1+p^2+\cdots+p^{2a-2})\ge aR,
$$
故 (7) 推出 (5)。这里没有把第一次非整位置错误地取为 $O(p)$。

在 $j<2R$ 中，若 $h\ge2$，则 $4j+1$ 是 $p^2$ 的正倍数，并小于 $2p^2$；所以只能为 $p^2$，即 $j=R$。其余 $h\le1$ 由 (7) 给整性。

为核定 (6) 的符号，$R$ 的两位数码是 $(r-1,3r-1)$，$2R$ 的两位数码是 $(2r-1,2r-1)$。去掉阶乘中的 $p$ 因子后，
$$
 \frac1p\binom{2R}{R}
 \equiv-
 \left(\frac{(2r-1)!}{(r-1)!(3r-1)!}\right)^2
 \equiv-1\pmod p.
$$
最后一步由 $(p-1)!\equiv-1$ 的配对式给
$((2r-1)!)^2\equiv1$ 以及
$(r-1)!(3r-1)!\equiv(-1)^r$。
又 $4^R\equiv1\pmod p$、$4R+1=p^2$，得到 (6)。$\square$

以下简单规则将反复使用。若一个非负超可加权 $\epsilon_j$ 满足 $\epsilon_0=0$，则
$$
 \mathscr B_\epsilon
 =\left\{\sum a_js^j:\ v_p(a_j)\ge-\epsilon_j\right\}
$$
对乘法封闭。常数项为一的元素的逆及全部整数次幂也在其中：逐阶取逆只有整加乘，或者直接使用整数二项式展开。若 $U(s)=sV(s)$、$V(0)=1$、$V\in\mathscr B_\epsilon$，则
$$
 v_p([s^j]U(s)^i)\ge-\epsilon_{j-i}\qquad(j\ge i).
 \tag{8}
$$
因此只要行权 $\alpha_j$ 满足
$\alpha_j-\alpha_i\ge\epsilon_{j-i}$，严格换元在各有限前缀上的加权矩阵都是整单位下三角矩阵；其矩阵逆也整。需要严格逆级数本身的同样界时，可从 $V_{\rm inv}(s)V(sV_{\rm inv}(s))=1$ 无除法逐阶求出。

由 (5)，$F^m\in\mathscr B_\delta$ 对每个整数 $m$ 成立，特别包括 $W(s)/s=F^4$。这里系数成本使用的是准确差 $j-i$，不是把第 $j$ 行的总阶免费给每一项。

## 3. 全深 Faber 核没有额外的 1/n 成本

对任意 $n\ge1$，令
$$
 c_{n,j}=[s^j]F(s)^{-4n},\qquad
 \mathcal F_n(T)=\sum_{j=0}^n c_{n,j}T^{n-j}.
$$
R210 的形式恒等式不受第一带范围限制：
$$
 F+4sF'=(1-s)^{-1/2},
$$
所以
$$
 d_{n,j}:=[s^j]F^{-4n-1}(1-s)^{-1/2}
     =\frac{n-j}{n}c_{n,j},\qquad d_{n,n}=0.
 \tag{9}
$$
定义
$$
 \mathcal D_n(T)=\sum_{j=0}^{n-1}d_{n,j}T^{n-1-j}
               =\frac{\mathcal F_n'(T)}n,\qquad
 \mathcal H_n=-xy\,\mathcal D_n(T).
 \tag{10}
$$
它仍满足准确主部
$$
                   \mathcal H_n=z^{-4n-1}+O(z^3).             \tag{11}
$$
由于 $(1-s)^{-1/2}$ 的系数在奇素数处整，(5) 和 (9) 给
$$
 \boxed{\quad
 v_p(d_{n,j})\ge-\delta_j,\qquad
 p^{\delta_{n-1}}\mathcal D_n\in\mathbf Z_p[T].
 \quad}                                                       \tag{12}
$$
首系数恒为一。这个全深界与 $v_p(n)$ 无关，不能再为 (10) 的形式写法另收一次 $v_p(n)$。

现在取任意 $1\le n\le M$ 和任意 $g(w)\in\mathbf Q_p[[w]]$，置
$$
 f_M(s)=[g(W(s))]_{\deg_s\le M},\qquad
 \eta=-\frac14f_M(T^{-1})\mathcal D_n(T)dT
      =\sum_{h=1-M}^{n}\beta_hT^{h-1}dT.
 \tag{13}
$$
写 $g_i=[w^i]g$。由 (8)、(12)，对 $0\le j\le M$ 有
$$
 \beta_{n-j}=-\frac14g_j+\sum_{i<j}\lambda_{j,i}g_i,
 \qquad
 v_p(\lambda_{j,i})\ge-\delta_{j-i}.
 \tag{14}
$$
证明中的每个 summand 的总偏移都是 $j-i$：从 $g_i$ 到某个 $s$ 系数的偏移与 $\mathcal D_n$ 系数下标相加，恰好等于它；$\delta$ 的超可加性支付它们全部的分母。

**全深目标运输定理。** 若非负整数行权 $\alpha_j$ 对所有所需下标满足
$$
                  \alpha_j-\alpha_i\ge\delta_{j-i},           \tag{15}
$$
则
$$
 \bigl(p^{\alpha_j}\beta_{n-j}\bigr)_{0\le j\le M}
 =
 \mathsf T_{n,M,\alpha}
 \bigl(p^{\alpha_j}g_j\bigr)_{0\le j\le M},
 \qquad
 \mathsf T_{n,M,\alpha}\in GL_{M+1}(\mathbf Z_p).
 \tag{16}
$$
其对角恒为 $-1/4$，且任意较短连续前缀也有同样性质。

剩余 $n-1$ 行对应 $M<j\le M+n-1$。给它们各乘同一规则的 $p^{\alpha_j}$ 后，它们是 (16) 右侧原 $M+1$ 行的整线性组合。故完整 Laurent 目标经整单位变换成为
$$
                            \begin{pmatrix}J\\0\end{pmatrix}. \tag{17}
$$
这些边界行没有读取 $g_{M+1},g_{M+2},\ldots$。

这是纯目标定理，尚不自行说明 $J$ 在某个给定源上整。$\alpha_j=\lfloor j/r\rfloor$ 已足以支付 (15)，但它不能因此被称为全深原 theta 源的整化权。下一节使用真正的 $e_j$ 并证明所需源整性。

## 4. 原 E_D 的全部 raw w 行确实按 e_j 整化

取同一个原 theta–sigma 平面
$$
 a=\vartheta^4,\qquad b=\sigma^4.
$$
原恒等式 $\vartheta^2=x\sigma^2$ 给
$$
                            b=s a.                           \tag{18}
$$
R167 已证明原 $A,B$ 是 $\mathbf Z[1/5][a,b]$ 的固定齐次次数十七多项式。令 $C=B-A$，始终保留原整源
$$
                     E_D=\mathbf Z_p[A,C]_{\le D}.             \tag{19}
$$
R173 给实际图形
$$
 a=f(b)=1+\sum_{k\ge1}c_kb^k,\qquad v_p(c_k)\ge-e_k.
 \tag{20}
$$
由于 (3)，对任意 $\mathcal P\in E_D$，其原 $b$ 参数展开
$$
 g_{\mathcal P}^{\,b}(b)
   =\mathcal P(A(f(b),b),C(f(b),b))
$$
的全部系数满足
$$
             p^{e_j}[b^j]g_{\mathcal P}^{\,b}\in\mathbf Z_p.  \tag{21}
$$
这里没有限制 $D$ 或只选齐次块；$p\ge7$ 也保证固定分母五是单位。

**关键补证。** 令 $B(s)=b(s)/s=a(s)$。由 (18)–(20)，准确有
$$
                       B(s)=f(sB(s)),\qquad B(0)=1.           \tag{22}
$$
从第 $j$ 阶看，右侧每项为
$c_k s^k B(s)^k$，$k\ge1$。其读到的各个 $B$ 下标均小于 $j$，且这些下标之和加 $k$ 等于 $j$。归纳和 (3) 因而给
$$
                           v_p([s^j]B)\ge-e_j.               \tag{23}
$$
递推没有除以 $j$、$k$ 或其他非单位数。

于是严格换元 $b=sB(s)$ 在 $e$ 加权的全部有限前缀上是整单位下三角矩阵。另一方面，$w=W(s)=sF^4$ 由 (4)、(8) 也有相同性质。将 (21) 先由 $b$ 运至 $s$，再由 $s$ 运至 $w$，得到
$$
 \boxed{\quad
 J_j(\mathcal P):=p^{e_j}[w^j]\mathcal P(A(w),C(w))
 \in\mathbf Z_p
 \quad\text{对所有 }j,D,\mathcal P\in E_D.
 \quad}                                                       \tag{24}
$$
而且原 $b$、$s$、$w$ 的这些完整归一矩阵是共同目标 $GL$ 等价，不只在已消元的真实 jump 上等价。

这一步是由原恒等式 (18) 和实际图形 (20) 新证明的。它没有直接把 R173 的前缀范数语句外推到 raw $w$ 行。

将 (24) 代入 (16)，取 $\alpha=e$，便得到同一原 $E_D$ 上的全深 Laurent 矩阵。对所有 $D,M,n$，它保留每个连续前缀的源核、任意 $p^N$ 精度的原像格、实际有限像的同构类型、非零 Smith 指数，以及在共同低阶核上、相同原源范数下的逐行真实值理想。整目标变换不改变源的次数；原底层 theta 次数 $17D$ 仍须支付。

## 5. 首跨带 carry 的准确整修正

在下列完整闭区间中，
$$
                          1\le a\le R,\qquad n=R+a,          \tag{25}
$$
有
$$
 \boxed{\quad
 p\mathcal D_{R+a}\equiv4a\,\mathcal D_a\pmod p,\qquad
 \mathcal H_{R+a}-\frac{4a}{p}\mathcal H_a
                          \in\mathbf Z_p[x,y].
 \quad}                                                       \tag{26}
$$
第一式是先把多项式乘 $p$ 后在整系数环中约化。更准确地，
$$
 \begin{cases}
 \mathcal D_{R+a}\in\mathbf Z_p[T],&p\mid a,\\
 v_p(\mathcal D_{R+a})=-1,&p\nmid a,
 \end{cases}                                                 \tag{27}
$$
其中多项式赋值是全部系数的最小赋值。

**证明。** 在次数小于 $2R$ 中，由命题 1 可写
$$
 F=F_0+F_Rs^R,\qquad F_0\in\mathbf Z_p[s],\quad F_0(0)=1,
$$
等式按此有限精度理解。对 $n\le2R$，$\mathcal D_n$ 只读次数至 $n-1<2R$；因此展开 $F^{-4n-1}$ 时至多出现一个非整因子 $F_R$。由 (6)，
$$
 p\,F^{-4n-1}(1-s)^{-1/2}
 \equiv
 (4n+1)s^R F_0^{-4n-2}(1-s)^{-1/2}\pmod p
 \quad\text{至次数 }<n.
 \tag{28}
$$
取 $n=R+a$，有 $4n+1=p^2+4a$。模 $p$ 的 Frobenius 给
$$
 F_0^{-p^2}\equiv1\pmod{s^{p^2}},
$$
而 (28) 右侧移去 $s^R$ 后只需次数至 $a-1\le R-1<p^2$。故它恰为
$4a s^R F^{-4a-1}(1-s)^{-1/2}$ 的所需截断。这在 $T$ 多项式中就是 (26) 的第一式。由 (12)，两边在除 $p$ 前都整，故相减后除 $p$ 仍整；乘 $-xy$ 给第二式。$\mathcal D_a$ 的首系数是一，遂有 (27)。$\square$

特别 $a=1$ 恢复首个非整核的准确符号；端点 $a=R,n=2R$ 也包含在证明中。没有宣称再往后仍只有一个 $F_R$ 因子。

修正不增加极点阶。对同一个保留至 $M\ge R+a$ 的原函数，其 Faber 留数行相应成为
$$
                         g_{R+a}-\frac{4a}{p}g_a.            \tag{29}
$$
按 (24) 归一，则是
$$
 \widetilde J_{R+a}
   =J_{R+a}-4a\,p^{e_{R+a}-e_a-1}J_a.
 \tag{30}
$$
由 (3)、$e_R=p-1$，该非对角系数属于 $p^{p-2}\mathbf Z_p$。因此这是同一原完整目标的整单位操作；它不强迫额外的原行消失，也不增加已知前缀之外的行。

## 6. 原全局微分、准确留数与一般 Witt 成本

仍取 $1\le n\le M$、同一 $\mathcal P\in E_D$，以 (13) 的有限代表定义
$$
                         \Omega=f_M(s)\mathcal H_n\omega
                               =\pi_T^*\eta.                 \tag{31}
$$
$T=x^2$ 在 $O$ 与 $T_0=(0,0)$ 的分歧指数均为四。由 (11)，
$$
 \operatorname{Res}_O\Omega=[w^n]g_{\mathcal P}=g_n,\qquad
                         \beta_0=-\frac14g_n.                \tag{32}
$$
故准确原函数分解是
$$
 \Omega=dU-\frac{g_n}{2}d\log x,\qquad
 U=\sum_{\substack{1-M\le h\le n\\h\ne0}}
                           \frac{\beta_h}{h}T^h.
 \tag{33}
$$
这包括全部原系数精度。没有先取模 $p$ 再凭 residue 选择一个不同代表。

从 (23)–(24) 或第 3 节换元可知 $v_p([s^i]f_M)\ge-e_i$。结合 (12)，置
$$
             L_p=e_M+\delta_{n-1},\qquad H=\max(n,M-1),
             \qquad q_p=\lfloor\log_p H\rfloor,
 \tag{34}
$$
便有
$$
 p^{L_p}\beta_h\in\mathbf Z_p\quad\text{对全部 }h,\qquad
                       p^{L_p+q_p}U\in\mathbf Z_p[T,T^{-1}].
 \tag{35}
$$
常数列若为零，最上面的 $h=n$ 项为零，可以把 $H$ 中的 $n$ 换成 $n-1$；本文使用含常数列的统一界。

更细地，令 $\gamma_h=p^{L_p}\beta_h$。按 $v_p(h)=t$ 分组，
$$
 V_t(X)=
 \sum_{\substack{q\ne0,\ p\nmid q\\1-M\le p^tq\le n}}
                  \frac{\gamma_{p^tq}}qX^q
              \in\mathbf Z_p[X,X^{-1}]
$$
给全部 Witt 层的准确有限分解
$$
 p^{L_p}\eta
   =\gamma_0\,d\log T
       +\sum_{t=0}^{q_p}\frac1{p^t}d\bigl(V_t(T^{p^t})\bigr).
 \tag{36}
$$
一层或两层 Cartier 不能删除尚存的其他层。模 $p$ 连续施加 $q_p+1$ 次 Cartier 后，非零 Laurent 指数全部消失，留下 logarithmic 项；这个事实不额外约束原源。

在全部整 Laurent 微分空间中，模去整 Laurent 原函数的像，准确商为
$$
 \mathbf Z_p\,d\log T
 \ \oplus\
 \bigoplus_{\substack{1-M\le h\le n\\h\ne0}}
           \mathbf Z_p/(h)\,\bigl[T^{h-1}dT\bigr].
 \tag{37}
$$
其扭部分长度为
$$
                    v_p(n!)+v_p((M-1)!).                    \tag{38}
$$
这里的整个目标商不能当作原 $E_D$ 像所产生的额外信息；第 4 节已确定其原像必须通过同一 $J$ 计算。

对一份给定 $\eta$，除 logarithmic 项外的实际最小标量清分母成本是
$$
 \max\left(0,\max_{h\ne0}\{v_p(h)-v_p(\beta_h)\}\right).
 \tag{39}
$$
这是系数逐项积分的必要充分条件。即使允许在 $E_0\setminus\{O,T_0\}$ 上选任意整正则原函数，也不会降低它：在未分歧扩环加入 $i$ 后，用四阶自同构平均原函数，得到不变整原函数；不变环恰为 $\mathbf Z_p[i][T,T^{-1}]$，于是又回到 (39)。式 (35) 是统一上界，没有声称原 theta 源在每一阶都取到它。

微分只在 $O,T_0$ 有极点，总极点阶至多
$$
                    (4n+1)+(4M-3)=4(n+M)-2.                 \tag{40}
$$
原函数部分的总极点阶至多 $4n+4(M-1)$。所有这些都是同一有限原 jet 代表的预算；它们不恢复 R207 的完整移动迹，也不改变原源的 theta 次数。

## 7. 额外跨素数成本只有线性阶

为对照真实全前缀预算，固定一个全局截断阶 $M$，允许每个目标素数选择任意 $1\le n_p\le M$。第 6 节在原 $e_M$ 之外只新增
$$
             \delta_{n_p-1}+\lfloor\log_p\max(n_p,M-1)\rfloor.
$$
跨全部惰性 $p\ge7$ 求和，有
$$
 \boxed{\quad
 \sum_{p\equiv3\ (4)}
 \left(\delta_{n_p-1}
       +\lfloor\log_p\max(n_p,M-1)\rfloor\right)\log p
                         =O(M).
 \quad}                                                       \tag{41}
$$
常数与 $D,M$ 及 $n_p$ 的选择无关。

第一项用
$$
 \sum_p\delta_{n_p-1}\log p
 \le4M\sum_{p\ge7}\frac{\log p}{p^2-1}=O(M).
$$
第二项至多
$$
              \sum_{p^t\le M}\log p=\psi(M)=O(M).
$$
这里最后的线性界只需二项式估计：对 $m\ge1$，
$\psi(2m)-\psi(m)\le\log\binom{2m}{m}\le2m\log2$；在二次幂处累加，再上取最近二次幂即可。

因此这份全深有理化与有限积分不会给 R173 的 $2M\log M+O(M)$ 原基线添加新的 $M\log M$ 主项。它同样没有降低这个主项。原两完整中央条件若要产生严格收益，仍须在同一个原连续前缀像内证明新增的饱和，而不是将 (37) 的环境扭长度重复计入。

## 8. 已支付与仍未支付的范围

本篇支付了全部深度的原椭圆对数分母、Faber 核分母、原 $b/s/w$ 完整归一矩阵比较、同一原 $E_D$ 的 Laurent 有限像、首跨带 carry，以及全部有限 Witt 原函数层。所有目标运输都为整单位变换；这些变换本身不会改变真实 Smith 指数。

行权是系数算子，不是把一份全局微分统一乘一个数。真正对微分及原函数使用的共同标量在 (34)–(35) 中另行支付。因此不能在 (16) 的行归一之后直接套 Cartier，假称已经给原未归一全局函数多除一层 $p$。

原完整中央非零、无界深前缀中由双中央失败导致的严格净预算，以及原 finite-image 到完整 Hasse core 的低损失观测，仍未由本篇得到。

依赖：[R167](R167-closed-theta-sigma-plane-and-integral-dynamics.md)、
[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R210](R210-full-first-band-faber-kernels-and-integral-witt-cost.md)、
[R212](R212-negative-witt-grunsky-and-original-prefix-transport.md)。
