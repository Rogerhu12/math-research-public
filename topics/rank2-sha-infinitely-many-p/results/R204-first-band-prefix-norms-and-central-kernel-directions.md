# R204. 第一带的完整前缀值理想与中央删项后的核方向

日期：2026-11-12。**状态：以下全部前缀满行、准确 Smith/value-ideal 公式及核方向构造均已证明；不据此声称中央非零或净算术预算改善。**

本篇始终保留原次数格。比较曲线只是在同一第一带公式中删去指定中央轴项，不声称它仍是一条实际秩二 theta 截面。其用途是区分准确前缀核的位置与前缀值理想。

## 1. 原对象与精确范围

令 $p=4r-1\ge19$ 为素数，$R=r(p-1)$，$v_0=-22$，并取
$$
 E_D=\mathbb Z_p[A,C]_{\le D},\qquad C=B-A,\qquad D\ge2r-1.
 \tag{1}
$$
原实际参数满足 $A=w+\cdots$、$C=v_0w^2+\cdots$。R199 给出
$$
 A(w)\equiv e^{b w^r}f(w),\qquad
 C(w)\equiv e^{b w^r}c(w)\pmod{w^{R+1}},
 \quad b=\frac a p,\quad a=17\tau_p\in\mathbb Z_p^\times,
 \tag{2}
$$
其中 $f=y+\cdots,c=v_0y^2+\cdots$ 是同一个真实整轴。

设
$$
 q_*=\lfloor r/2\rfloor+2,\qquad k_*=r q_*,
 \quad
 M_1=E_D+p^{-1}\operatorname{span}\{A^iC^j:i+j\le D,\ i+2j\ge r\}.
 \tag{3}
$$
定义完整连续矩阵
$$
 J_{<k}(P)=\bigl(p^{\lfloor n/r\rfloor}[w^n]P(A(w),C(w))\bigr)_{0\le n<k}.
 \tag{4}
$$
这里 $k\le k_*<R+1$。在最终范围，$M_1$ 是 R196 已识别的第一整化格；对较早的前缀，本篇只用它的整像，不把它误认成各个前缀的全部第一原像。

比较轴 $(f^\circ,c^\circ)$ 可由 $(f,c)$ 删去任意若干向量项
$v_s y^{rs}$，$s\ge1$，并保持 (2) 中同一个 $b$。其矩阵记作 $J^\circ$。这些删项保留 $f_1=1,c_2=v_0$ 及全部角向次数小于 $r$ 的系数。

## 2. 真实完整矩阵在 $M_1$ 上满行

**定理 1。** 对每个 $k\le k_*$，
$$
 J_{<k}(M_1)=\mathbb Z_p^k,\qquad
 J^\circ_{<k}(M_1)=\mathbb Z_p^k.
 \tag{5}
$$
这是完整连续矩阵的断言，包含所有跨角向尾。

**证明。** 先取 $k=k_*$，把目标行按角向指标 $l=0,\ldots,r-1$ 排列，每块含 $h=0,\ldots,q_*-1$。在第 $l$ 块选一个低列 $A^l$，再选
$$
 p^{-1}A^{r+l-2c}C^c,\qquad c=0,\ldots,g-1,\qquad
 g=\lfloor r/2\rfloor+1=q_*-1.
 \tag{6}
$$
这些是真实原列：$r+l-2c\ge0$，原次数 $r+l-c\le2r-1\le D$，原权为 $r+l$。它们在角向行 $j<l$ 的模 $p$ 条目为零，故整个选定方阵的约化按角向分块三角。

对角块的 $h=0$ 行在低列为一，在所有高列为零。高列的 $h=1,\ldots,g$ 条目准确为
$$
 \frac{(17\tau)^{h-1}}{(h-1)!}
       (r+l-c)^{h-1}v_0^c,\qquad \tau=\tau_p\bmod p.
 \tag{7}
$$
这是 R199 的全部像式在真实最低角向系数处的值。节点 $r+l-c$ 连续且互异模 $p$，所有节点差、阶乘、$17\tau$、$v_0$ 都是单位。因此此 Vandermonde 方阵行列式是单位。低列的其余条目通过 $h=0$ 行消去，不影响此结论。每个角向对角块都是单位，故整个 $k_*\times k_*$ 子式是单位。

所选子式在 $\mathbb Z_p$ 上给实际右逆，证明 (5)；投影到任意早期完整前缀保持满行。比较轴具有完全相同的首项，以上证明不变。$\square$

这个满行端点是准确的。在角向零的所有 $M_1$ 列中，模 $p$ 仅常数列及原权恰为 $r$ 的列可能非零。后者有 $\lfloor r/2\rfloor+1$ 个不同原次数节点。因此角向零行空间的维数至多 $q_*$；加入第 $k_*$ 行（即 $h=q_*,l=0$）后，$J_{\le k_*}(M_1)$ 不再模 $p$ 满行。

这里仅断言 $M_1$ 满行的精确端点。端点后的新有理 jump 及下一 Smith 指数另由第 4.1 节的真实新列支付；不能仅由这个维数上界代替。

## 3. 原整源的全部 Smith 指数

令
$$
 \rho_0(k)=\operatorname{rank}_{\mathbb F_p}
                       (J_{<k}(E_D)\bmod p),\qquad k=rq+s,\quad0\le s<r.
$$
因为 $D\ge2r-1$，原源包含全部权小于 $r$ 的单项式。R196 的图形换元
$Z=C-\phi(A)$、$\phi=c\circ f^{-1}$ 保权 $(1,2)$，并在此有限权商上整可逆。正则化乘子 $\lambda/A^2$ 也是单位。因此其独立条件数准确为
$$
 \boxed{\quad
 \rho_0(rq+s)=\sum_{j=0}^{q-1}(r-2j)_+ +(s-2q)_+.
 \quad}
 \tag{8}
$$
这不是一个维数上界。每个被计数的图形 Hasse 系数均由原有限权商中的一个独立坐标给出。

当 $q\ge\lceil r/2\rceil$，
$$
 \rho_0(k)=N_r=\#\{(i,j):i+2j<r\}
              =\left\lfloor\frac{(r+1)^2}{4}\right\rfloor.
 \tag{9}
$$
删去中央轴项不改变 (8)：原模 $p$ 行只读取轴上角向次数小于 $r$ 的数据。

由 $pM_1\subset E_D$ 及 (5)，对于每个 $k\le k_*$，
$$
 p\mathbb Z_p^k\subset J_{<k}(E_D)\subset\mathbb Z_p^k.
$$
故全部非零 Smith 指数准确是
$$
 \boxed{\quad 0^{\,\rho_0(k)},\qquad1^{\,k-\rho_0(k)}.\quad}
 \tag{10}
$$
矩阵有理满行秩 $k$。比较矩阵有完全相同的 Smith 指数。

若 $M=\binom{D+2}{2}$，按 R198 的真实原像定义，对每个 $t\ge1$，
$$
 I_t(k)=\mathbb Z_p^k,\qquad
 \operatorname{length}(\Lambda_t(k)/E_D)
       =t(M-k)+k-\rho_0(k).
 \tag{11}
$$
比较矩阵同样成立。在本篇特定范围内，嵌入目标中的整化像确实都是整个 $\mathbb Z_p^k$；这比仅有抽象同构更强。它不意味着原像子格的位置相同。

## 4. 每一个真实连续前缀的值理想

令 $\ell_n(P)=[w^n]P(A,C)$，在同一原格中定义
$$
 E^{(n)}=E_D\cap\ker(\ell_0,\ldots,\ell_{n-1}),\qquad
 \ell_n(E^{(n)})=p^{v_n}\mathbb Z_p.
 \tag{12}
$$
所有 $n<k_*$ 都是真有理 jump，因为每个归一前缀有理满行。R198 的准确饱和旗标等式及 (10) 给
$$
 \sum_{n<k}v_n
   =k-\rho_0(k)-\sum_{n<k}\lfloor n/r\rfloor.
 \tag{13}
$$
逐行相减，而不是把稀疏前缀代替完整前缀，得到
$$
 \boxed{
 v_{rh+l}=
 \begin{cases}
  -h,&l\ge2h,\\
  1-h,&l<2h,
 \end{cases}
 \qquad 0\le rh+l<k_*.
 }
 \tag{14}
$$
这包括 $h=0$ 时全为零，以及 $2h\ge r$ 时整块为 $1-h$。

比较曲线的每个完整前缀也满足完全相同的式 (14)。因此，在本范围内删去中央轴项不改变任何一个实际前缀值理想；这个结论无需假设原两中央泛函为零。以下核方向变化不能再计作范数收益。

## 4.1. 紧接满行端点的第一个真实二层指数

令 $g=\lfloor r/2\rfloor+1$，故 $q_*=g+1$。取原整数多项式
$
 Q(X)=\prod_{m=\lceil r/2\rceil}^{r}(X-m)
       =\sum_{d=0}^{g}Q_dX^d.
 \tag{14a}
$
对 $1\le h\le q_*$ 将角向零行单位化为
$
 \mathscr R_h=(h-1)!\,a^{1-h}J_{rh}.
$
在 $M_1$ 上，模 $p$ 的准确关系是
$
                 \sum_{d=0}^{g}Q_d\mathscr R_{d+1}=0.
 \tag{14b}
$
因为这些行只读取原权恰为 $r$ 的列，(7) 的节点恰好是
$\lceil r/2\rceil,\ldots,r$；常数列在这些行均为零。
新行的系数 $Q_g=1$ 是单位。

现在加入真正原列
$
                   z=p^{-2}C^r.
$
其原次数为 $r\le D$，原权为 $2r$；R199 证明它在所需完整第一带
的所有归一行上都整。对 $h\ge2$，
$
 \overline{\mathscr R_h(z)}
   =a^{-1}v_0^r(h-1)r^{h-2},
 \qquad \overline{\mathscr R_1(z)}=0.
$
因此新列在 (14b) 左侧的值为
$
                  a^{-1}v_0^r Q'(r)\in\mathbb F_p^\times.
 \tag{14c}
$
$Q'(r)$ 的每个因子都是小于 $p$ 的非零整数。
原 $k_*$ 个完整行已在 $M_1$ 上满行，(14c) 遂给
$
     J_{<k_*+1}\bigl(M_1+\mathbb Z_pz\bigr)
                          =\mathbb Z_p^{k_*+1}.
$

这一新前缀仍处于 R196 识别 $\Lambda_1=M_1$ 的范围。
$M_1$ 的模 $p$ 像秩准确为 $k_*$，而
$p^2(M_1+\mathbb Z_pz)\subset E_D$。故原整源的完整 Smith 指数准确为
$
        0^{\,N_r},\qquad1^{\,k_*-N_r},\qquad2^1.
 \tag{14d}
$
新行是真有理 jump，其 raw 值理想指数为
$
                         v_{k_*}=2-q_*.
 \tag{14e}
$

也可直接给原始源见证：由旧前缀的整右逆，取 $u\in M_1$ 使
$J_{<k_*}u=J_{<k_*}z$，则
$P=C^r-p^2u\in E_D$ 满足全部真实早行准确为零。
因为 $p^2M_1\subset pE_D$，$P$ 是原始向量；(14c) 给新归一行的
准确赋值二。这里没有把两项分别要求为前缀零，也未使用中央消失条件。
比较矩阵的同一构造给相同结论。

## 5. 同一原次数格中的真核方向

现在令
$$
 q=\lceil r/2\rceil,\qquad2\le s\le r-2,\qquad k=rq+s,
 \tag{15}
$$
仍保 $D\ge2r-1$。以下构造在原 $M_1$ 中进行。

用 R200 的有限图形对数：
$$
 y=T^{-1}(C/A),\quad T=c/f,\quad
 \eta=\log\frac{A}{f(y)},\quad
 Z=C-\phi(A),\quad\lambda=\phi-A\phi'.
 \tag{16}
$$
只读所需 $Z$ 次数，先在特征零构造再约化；所有对数分母小于 $p$。置
$$
 F=C-\phi_{<r}(A),\qquad
 G_*=-a\,y^r\frac Z\eta.
 \tag{17}
$$
$\phi_{<r}$ 是严格低于 $r$ 阶的截断，故 $F$ 是原低权多项式、原次数不超过 $r-1$。这里 $Z/\eta$ 在有限 $Z$ jet 中有定义，因为 $\eta_1=\lambda^{-1}$。

只需 $G_*$ 至 $Z^{q-1}$。其第 $Z^j$ 系数的 $A$ 阶至少
$$
                 r+2-2j\ge r+4-2q>0.
 \tag{18}
$$
这是因为 $Z/\eta$ 的第 $j$ 系数阶至少 $2-2j$，而 $y^r$ 的相应卷积付 $r-2j$。将此有限 jet 转回原 $(A,C)$，再取原权小于 $2r$ 的部分，得到一个真正多项式 $G$，满足
$$
       \mathrm{wt}(G)\ge r+2,\qquad\deg G\le2r-1.
 \tag{19}
$$
非负 $A$ 次数由 (18) 保证；这不是任意 Laurent 源扩容。

在所需 jet 中
$$
 F+\frac{\eta}{a y^r}G
  =\phi-\phi_{<r}+O_{\rm wt}(r)+O(Z^{q+1}).
 \tag{20}
$$
原权截断的误差至少为 $2r$，乘 $\eta/y^r$ 后仍至少为 $r$。故 R200 的全部正则化行 $B_j$ 在 $j\le q$ 时都被 $A^r$ 整除。因此
$Y_0=F+G/p$ 是 $J_{<k}|_{M_1}\bmod p$ 的真实核向量。

由定理 1 的整右逆，可在同一 $M_1$ 中选 $Z_0$ 使
$JZ_0=JY_0/p$，从而
$$
              Y=Y_0-pZ_0\in M_1,\qquad JY=0.
 \tag{21}
$$
这个提升不会改变低权系数模 $p$。特别，按原单项式系数记
$Y_C=[C]Y$ 等，有
$$
           Y_C\in\mathbb Z_p^\times,\qquad
           Y_A=0,\qquad Y_{A^2}=-v_0Y_C.
 \tag{22}
$$
后两个是原真实 $w,w^2$ 前缀给出的准确等式。

## 6. 核确实变化，而所有值理想仍相同

假设比较轴删除了第一个中央项 $v_1y^r$；也可以同时删除第二、第三或更多中央项。写 $v_1=(v_{1,A},v_{1,C})$。在 $w^r,w^{r+1}$ 处，二次 Taylor 项以及所有后续中央项都尚未进入。因此对 (21) 的真核向量，准确有
$$
 \begin{aligned}
 (J-J^\circ)_r(Y)
       &=p\,v_{1,C}Y_C,\\
 (J-J^\circ)_{r+1}(Y)
       &=p\{-2v_0v_{1,A}Y_C+v_{1,C}Y_{AC}\}.
 \end{aligned}
 \tag{23}
$$
两个线性式对 $(v_{1,A},v_{1,C})$ 的矩阵行列式为
$2v_0Y_C^2\in\mathbb Z_p^\times$。所以
$$
 \min\{v_p((J-J^\circ)_r(Y)),v_p((J-J^\circ)_{r+1}(Y))\}
       =1+\min\{v_p(v_{1,A}),v_p(v_{1,C})\}.
 \tag{24}
$$
只要 $v_1\ne0$，真有理核便不同。原实际 $v_{1,A}=f_r=[w^r]A$ 的非零由 R195 的固定五进矩证书给出；此处不把它当成目标素数 $p$ 处的单位。

在以下有关共享第三格的条件性结论中，额外取比较轴至少删除前两中央项（也可继续删除更高项）。若原两完整中央泛函均为零，R201/R203 给
$v_1=p t_1$，$t_1\in\mathbb Z_p^2$，并在 (15) 的锚点给出共享的第三原像格。令
$\kappa=\min v_p(t_1)<\infty$，则 (24) 为 $2+\kappa$。
当 $\kappa=0$，$x=Y/p^2$ 位于两个共同的 $\Lambda_3$，而
$x/p$ 属于 $\Lambda_4(J)$、不属于 $\Lambda_4(J^\circ)$。
当 $\kappa>0$，至少在不迟于 $\kappa+4$ 层可以看见不同：
$Y/p^{\kappa+3}$ 属于 $\Lambda_{\kappa+4}(J)$，却不属于
$\Lambda_{\kappa+4}(J^\circ)$。不宣称其余行不会更早检测到差异。

这些格在每一层仍有式 (11) 给出的相同指数，而且每个真实前缀值理想仍满足同一个式 (14)。因此这里检测到的是原像核方向的变化，不是新的像指数、累计 jet 收益或严格算术预算。

## 7. 范围与下一未付步骤

本篇给出 $D\ge2r-1$、$k\le k_*$ 的完整实际连续前缀公式，精确定位第一整化像满行的终点，并构造保原次数的核方向见证。第 4.1 节进一步准确给出紧接端点的首个 $p^2$ Smith 及其原始源见证；再往后的完整像仍须分析。本文没有用比较曲线替代原两条秩二曲线的完整中央条件。

依赖：R196 的完整 Euler–Padé 核，R198 的真实 image/flag 恒等式，R199 的准确第一带共同指数，R200 的有限 graph–log 运输；条件性的共享第三层使用 R201，有限 central 整格使用 R203。原首中央向量的非零使用 R195，不使用其未支付的目标 $p$ 单位性。
