# R254：真实平方核符号的有限头相似预算与混合尾项的限制

日期：2026-11-13（UTC+8）。作者：boundary。
状态：以下有限头上界、真实误差及形式伴随运输已证明；尚未接成可用的分级能量，不宣称新的缺陷尾率或饱和结论。

## 1. 删去首位后按原物理位计费

沿用单比特缺陷度量工作笔记。尾空间的归一化真实后移为
$$
Ce_n=\frac{\alpha_{1+v_2(n)}}{\alpha_1}e_{n-1},\qquad Ce_0=0,\qquad \|C\|=1.
$$
记 $\bar W_n=\prod_{\ell=1}^n\alpha_{1+v_2(\ell)}/\alpha_1$、$\bar d_j=\bar W_{2^j}$、
$\bar N_j=C^{2^j}/\bar d_j$、$\bar Y_j=\bar N_j(I+\bar N_j)^{-1}$。
尾编号 $j$ 对应原物理位 $j+1$。准确地
$$
\boxed{\bar\Lambda_j:=-\log\bar d_j
=1600\,16^j-840\,8^j+(300j-760)2^j.}
\tag{1.1}
$$
这是原式 $d_{j+1}=\alpha_0^{2^j}\widehat d_j$ 再除以 $\alpha_1^{2^j}$ 得到；特别 $\bar\Lambda_0=0$。
由 (1.1)，
$$
0\le\bar\Lambda_j\le1600\,16^j,\qquad
\bar\Lambda_j/2^j\text{递增},\qquad
\bar\Lambda_{j+1}\ge16\bar\Lambda_j.
\tag{1.2}
$$
第二个断言的差为 $11200\,8^j-2520\,4^j+300>0$；第三个的差为
$6720\,8^j+(11240-4200j)2^j>0$，可用 $4^j\ge j$ 检查。

令 $b_j=(j+2)^{-2}$，
$$
A_N=\sum_{j\ge0}b_j\bar N_j,\quad
A_Y=\sum_{j\ge0}b_j\bar Y_j,\quad
Z_N=A_N,\quad Z_Y=A_Y(I+A_Y)^{-1}.
$$
两种 $A$ 均满足 $\|A\|<2/3$。例如
$$
\sum_{j\ge0}b_j\le\frac14+\frac19+\frac1{16}+\frac1{25}
+\int_5^\infty x^{-2}\,dx=\frac{2389}{3600}<\frac23;
$$
$Y$ 多出的误差至多该和的 $4\eta_1$ 倍，$\eta_1=e^{-17960}$，仍在余量内。
置
$$
\eta=\eta_0=e^{-1070},\qquad \mathcal F=Z^2-\eta C,\qquad K=\ker\mathcal F.
\tag{1.3}
$$
原慢核是 $M=\{(u,-Zu):u\in K\}$。新头预算用于 (1.3)，不是原线性慢符号的再一次相似。

## 2. 有限头与主结论

取 $m\ge2$、$d=2^m$。尾头含原物理位 $1,\ldots,m$。$C_m,A_m,Z_m$ 为在前 $d$ 个尾坐标上的实际限制，令
$$
F_m=Z_m^2-\eta C_m=f_m(C_m).
$$
所有有限多项式在模 $z^d$ 下使用。$f_m(z)=-\eta z+Z_m(z)^2$ 的线性系数非零。

**定理。** 两模型均有可逆 $S_m$ 满足
$$
F_m=S_m(-\eta C_m)S_m^{-1},
$$
且
$$
\boxed{\log\kappa(S_m)\le
6\bar\Lambda_{m-2}+(2140+11\log2)d+6\log d+\log4.}
\tag{2.1}
$$
因此 $\log\kappa(S_m)\le(75/2+o(1))d^4$。
若用含原第0位的总头长 $D=2d=2^{m+1}$ 表示，则
$$
\boxed{\log\kappa(S_m)\le(75/32+o(1))D^4.}
\tag{2.2}
$$
按同一个原物理最大位比较，原 R249 线性慢头的最优主指数是 $(35/6)D^4$，所以这里确有改进。未声称 (2.2) 对平方头最优。

## 3. 真实权积的统一单项式界

记 $\bar\omega_r=-\log\bar W_r$。准确二进位积给
$$
\bar\omega_r=\sum_{j\in\operatorname{bits}(r)}\bar\Lambda_j,\qquad
\|C^r\|=\bar W_r.
\tag{3.1}
$$
第二式的证明为：任意 $r$ 个连续正整数中，$2^j$ 的倍数至少有 $\lfloor r/2^j\rfloor$ 个；前 $r$ 个正整数对每个 $j$ 同时达到最小值。将递减权的负对数按这些计数展开，得任何长 $r$ 权积不超过首段权积，而首段达到等号。特别有限头幂和单个矩阵条目也受同一权积控制。

考虑来自 $k\ge1$ 个块的单项式。每块至少含两个 $\bar N_j$ 因子，且每块的物理总幂次小于 $d$。设总因子数 $p\ge2k$、各位重数 $k_j$、总物理幂次 $n=\sum_jk_j2^j$，并假设
$$
r=n-k<d.
$$
除去每块一个 $C$ 后的单项式为 $C_m^r/\prod_j\bar d_j^{k_j}$；必有 $r\ge k$、$j\le m-1$。

**引理。** 每个这样的单项式都满足
$$
\boxed{\sum_jk_j\bar\Lambda_j-\bar\omega_r\le3\bar\Lambda_{m-2}.}
\tag{3.2}
$$

证明。置 $s=d/2$、$t=d/4$、$L=\bar\Lambda_{m-2}$。
最高位 $m-1$ 至多出现一次。否则
$n\ge2s+(p-2)\ge d+2k-2$，所以 $r\ge d+k-2$；
$k\ge2$ 与 $r<d$ 矛盾；$k=1$ 则该单块的物理次数至少为 $d$，与块截断矛盾。

最高位不出现时，若 $r<s$，置 $\ell=\lfloor\log_2r\rfloor$。所有出现的 $j\le\ell$，因为一个 $2^j$ 加上至少 $2k-1$ 个单位贡献会迫 $r\ge2^j+k-1\ge2^j$。由 (1.2)，
$$
\sum_jk_j\bar\Lambda_j\le(\bar\Lambda_\ell/2^\ell)n
\le(\bar\Lambda_\ell/2^\ell)2r<4\bar\Lambda_\ell.
$$
再减去 $\bar\omega_r\ge\bar\Lambda_\ell$ 即得不超过 $3L$；$\ell=0$ 时全部相应系数为零，直接成立。
若 $r\ge s$，同理差小于 $8L-\bar\Lambda_{m-1}\le0$。

最高位恰出现一次时，写 $r=s+R$、$0\le R<s$。因 $p\ge2k$，
$$
k\le R+1,\qquad
\sum_{j<m-1}k_j2^j=R+k\le2R+1.
$$
最高位的 $\bar\Lambda_{m-1}$ 准确抵消。
若 $R\ge t$，余项至多 $(L/t)(2R+1)-\bar\omega_R\le(3-1/t)L$。
若 $R<t$ 而下一位 $m-2$ 出现，剩余至少 $2k-1$ 个因子给
$R\ge t+k-2$。故只能 $k=1,R=t-1$，且只剩这一个下一位因子；余项为 $L-\bar\omega_{t-1}\le L$。
若 $R<t$ 且下一位不出现，$m\ge3$ 时余项小于
$4\bar\Lambda_{m-3}\le L/4$；$m=2$ 时余下可能系数只有 $\bar\Lambda_0=0$，直接为零。证毕。

由 (3.1)，(3.2) 既控制该单项式范数，也控制每个真实加权矩阵条目。未使用纯平方零替代。

## 4. N/Y 全部内外分式的慢次数预算

用形式变量 $x_j$ 记录 $\bar N_j$，赋物理次数 $2^j$、慢次数1；只用于有限头系数计算。对 $0<t<1/2$，全部绝对系数按慢次数的生成函数满足
$$
|A_Y|_t\le t/(1-t),\qquad
|Z_Y|_t\le\frac{|A_Y|_t}{1-|A_Y|_t}\le t/(1-2t).
$$
$Z_N$ 也受最后一式控制。因此 $Z^{2k}$ 的慢次数 $p\ge2k$ 绝对系数总和至多
$$
\binom{p-1}{2k-1}2^{p-2k}\le4^p.
\tag{4.1}
$$
每个 $Z^2$ 块先按物理次数 $<d$ 截断只会删除单项式，不增大该预算。

令
$$
H(z)=-\eta^{-1}Z_m(z)^2/z\pmod {z^{d-1}},
$$
即只保留次数至多 $d-2$；于是 $g(z):=f_m(z)/(-\eta)=z(1+H(z))$，$H(0)=0$。
每个 $H^k$ 单项式符合 §3 的块假设，并多付 $\eta^{-k}$。非零头项必有
$p\le n=r+k\le2d-2$。由 (3.2)、(4.1)，对 $0\le k<d$，全部展开后的加权单项式范数绝对和不超过
$$
\boxed{M_d=2d\,16^d e^{1070d}e^{3\bar\Lambda_{m-2}}.}
\tag{4.2}
$$
$k=0$ 的恒等项显然也受此界控制。这里保留了绝对展开预算，所以下一步抽取任何多项式系数仍合法。

## 5. 相似与逆同时由 Lagrange 支付

令 $h$ 为 $g$ 的模 $z^d$ 复合逆，$C_g,C_h$ 为基 $1,z,\ldots,z^{d-1}$ 上的换元矩阵。设
$$
D_m=\operatorname{diag}(1/\bar W_0,\ldots,1/\bar W_{d-1}),
\quad
S_m=D_m C_h^\top D_m^{-1}.
$$
换元准确给
$$
F_m=S_m(-\eta C_m)S_m^{-1},
\quad S_m^{-1}=D_mC_g^\top D_m^{-1}.
$$
两个矩阵对角线均为1。对 $1\le r\le n<d$，
$$
[z^n]h(z)^r=\frac rn[z^{n-r}](1+H(z))^{-n}.
$$
展开负幂，$\binom{n+k-1}{k}\le4^d$；由 (4.2)，每个相似条目不超过 $d4^dM_d$。
$r=0$ 行只有单位条目。逆矩阵直接用
$[z^n]g(z)^r=[z^{n-r}](1+H(z))^r$ 和 $\binom rk\le2^d$，每项不超过 $d2^dM_d$。
所以
$$
\|S_m\|\le d^2 4^dM_d,\qquad
\|S_m^{-1}\|\le d^2 2^dM_d.
$$
相乘即
$$
\kappa(S_m)\le4d^6
\exp\!\left(6\bar\Lambda_{m-2}+(2140+11\log2)d\right),
$$
证明 (2.1)，包括最小头 $m=2$。

## 6. 原位号的真实 carry 与混合分级障碍

令
$$
A^{[m]}=A_m\otimes I+I\otimes D_{\ge m},\qquad
D_{\ge m}=\sum_{j\ge m}b_jE_j
$$
为尾编号混合截断。真实前头及全部 Cayley 逆的旧预算原样给
$$
\|A-A^{[m]}\|\le26\eta_m,\qquad \|A^{[m]}\|<2/3.
$$
这里 $\eta_m=\alpha_{m+1}/\alpha_m$ 是原物理编号。按同一函数定义 $Z^{[m]}$，并置
$$
\mathcal F^{[m]}=(Z^{[m]})^2-\eta(C_m\otimes I).
$$
两边的 $I+A$ 逆不超过3，故 $\|Z-Z^{[m]}\|\le234\eta_m$、两种 $Z$ 范数均不超过2。
准确跨头公式又给
$\|C-C_m\otimes I\|=\alpha_{m+1}/\alpha_1\le\eta_m$。因此
$$
\boxed{\|\mathcal F-\mathcal F^{[m]}\|\le937\eta_m.}
\tag{6.1}
$$
由于
$$
-\log\eta_m=1400d^4-630d^3+300d,
$$
(2.1) 确实给合法的全算子预算
$$
\boxed{\kappa(S_m)^2\|\mathcal F-\mathcal F^{[m]}\|
\le\exp\bigl(-(1325+o(1))d^4\bigr).}
\tag{6.2}
$$
这已按原位号付清可能遗漏的16倍尺度。

但 $N$ 模型中准确有
$$
\mathcal F^{[m]}=F_m\otimes I+2A_m\otimes D_{\ge m}
 +I\otimes D_{\ge m}^2.
\tag{6.3}
$$
把 $F_m$ 化为单链并不使全部项严格降相同次数。头链位置若赋权2以配合 $D_{\ge m}^2$，$S_m^{-1}A_mS_m$ 是链变量的有限多项式，混合项一般从降3次开始；$Y$ 还有解析分式的其他混合项。
所以不能将 (2.2) 或 (6.2) 直接代入 R249 的移位通量和尾率公式。

## 7. 缺陷正度量与形式伴随原像的固定成本运输

令原 $w\in W$，写 $w=(u,-Zu)$。尾全空间置 $G_0=I+Z^*Z$，则
$\langle G_0u,u\rangle=\|w\|^2$。在 $K$ 上压缩后是工作笔记中的
$G=I+(Z|_K)^*(Z|_K)$，不能混写作用空间。

取原规范形式原像 $T^*h=w$，且
$$
\|h_q\|\le H e^{c(q+1)},\qquad c_*<c<4,\qquad c_*=2+2\log(3/2).
$$
$N$ 模型写 $h=(h_0,h_1)$。准确方程
$$
Z^*h_0+\eta C^*h_1=u,\qquad h_0+Z^*h_1=-Zu
$$
消元给
$$
\boxed{\mathcal F^*(-h_1)=G_0u,\qquad
\|(h_1)_q\|\le H e^{c(q+2)}.}
\tag{7.1}
$$

$Y$ 先写 $T_Y=V(N_0+Z)$，其中 $V=(I+A)(I+N_0)^{-1}$。
这个单位在指数孔权 $X_c$ 上也有明确界。对 $2\le c\le4$，实际 borrow 级数给
$$
\|N_j\|_{X_c\to X_c}
\le e^{-c}+\frac{\eta_j}{1-e^4\eta_*}<\frac14,
\qquad\eta_*=\eta_0.
$$
纯删除降一次，长度 $\ell$ 的 borrow 改变孔数 $\ell-1$，每项付因子 $e^{c(\ell-1)}$。于是
$$
\|Y_j\|_{X_c\to X_c}\le\frac13,\quad
\|A\|_{X_c\to X_c}\le\frac29,\quad
\|V\|_{X_c\to X_c}\le\frac{44}{27}<2.
$$
将 $h$ 作为 $X_c^*$ 的逐层泛函，则 $\widetilde h=V^*h$ 合法、
$(N_0+Z)^*\widetilde h=w$，且 $\|\widetilde h_q\|\le2H e^{c(q+1)}$。
同样消元得到
$$
\boxed{\mathcal F^*(-\widetilde h_1)=G_0u,\qquad
\|(\widetilde h_1)_q\|\le2e^cH e^{c(q+1)}.}
\tag{7.2}
$$
这些等式在已定义指数权对偶中成立，未对非 Hilbert 的形式 $h$ 擅用全空间伴随。固定一次图消元不增加指数率，并保留正能量；其余混合分级仍未解决。

## 8. 结论范围

本稿的真实平方头相似上界包括 N/Y 全部内外分式、真实权积、Lagrange 双向预算、最小头和原物理 carry 尺度；形式伴随运输也只付固定成本。

若重新引入被删首位作标准二倍维数线性化，所得正是原头链问题，R249C 的最优主指数会重新适用。小头条件数只有在能另外处理 (6.3) 的混合项后才可能改进移动能量；本稿未由单独头预算推出 $N=M$ 或新的必要尾率。
