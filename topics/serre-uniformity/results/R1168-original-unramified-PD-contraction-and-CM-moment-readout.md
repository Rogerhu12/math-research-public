# R1168 — 原未分歧 PD cone 的显式收缩、实际 CM 矩与中央读取

**状态：已证明。** 日期：2026-11-28 Asia/Taipei。会话：Astra-serre-24b8836b-20261126。

本篇在 R1166 的实际 tame descent 之后，直接消去原 log-PD cone 的全部 normal 变量。它给完整链收缩，不只给上同调维数。代入 R1167 的实际第一层系数后，原四次、八次 theta 矩的读数成为指定的 Hurwitz–Eisenstein 系数；原中央项另有显示的有序 gauge 修正。

以下所有等式都沿原第一槽 Weil、$\omega,\eta=x\omega$、同根 theta 和原 $\Pi_r,\lambda_\infty$。没有重新选一个至多差单位的系数基。

## 1. 原全部六种系数及实际 normal Frobenius

令 $F=\mathbb Q_{p^2}$，$k=\mathbb F_{p^2}$。
原曲线、$b_E\in\mathbb F_p^\times$、$e=p^2-1$ 均沿 R1167。
R1166 的未分歧 embedding 为
$$
S_F=\mathcal O_F[u,\gamma_n(g):n\ge1]^\wedge_p,\qquad
g=u-p,\qquad \psi u=u^p,\qquad N=u\partial_u .
\tag{1168.1}
$$
沿原 generic fibre 的 $u\mapsto p$，不在 Frobenius 前令 $g=0$。

对原 $\operatorname{Sym}^dH(t)$，用同一几何实现
$$
M_d=\operatorname{Sym}^dH^1_{\rm dR}(\mathcal E),\qquad r=d+t.
$$
实际所需的 $(d,t)$ 为
$$
(4,1),\ (8,1),\ (0,5),\ (12,2),\ (8,4),\ (4,6).
\tag{1168.2}
$$
最后三项与 R1163 的共同 $\mathcal E^{12}$、weight $14$
实现经原 paired projectors 相同，原 coevaluation 的 $-1/2$
和 $\lambda_\infty$ 均已支付。

记
$$
e_k=\omega^{d-k}\eta^k,\quad w_k=d-k,\quad
q_k=r-w_k=t+k,\quad 0\le k\le d.
$$
对 (1168.2)，$1\le q_k\le14<p-2$。
由 R1167 的 actual crystalline 两列，
$$
F_k:=p^{-w_k}\Phi_M e_k
 \equiv\lambda_k e_{d-k},\qquad
\lambda_k=(-1)^k b_E^{\,2k-d}\in\mathbb F_p^\times .
\tag{1168.3}
$$
$(F_k)$ 是原强可除基的输出，不是另选的输入基。

以下均模 $p$，在同一有限 coefficient cone 中：
$$
\begin{aligned}
C^0&=\operatorname{Fil}^r(S_F\otimes M_d)/p,\\
C^1&=\operatorname{Fil}^{r-1}(S_F\otimes M_d)/p\,d\log u
          \ \oplus\ (S_F\otimes M_d)/p,\\
C^2&=(S_F\otimes M_d)/p\,d\log u,
\end{aligned}
$$
$$
d_0x=(Nx,(1-\phi_r)x),\qquad
d_1(a,y)=a-\phi_{r-1}a-Ny,\qquad
\phi_i=p^{-i}\Phi .
\tag{1168.4}
$$
一阶第一槽在公式中只写其 $d\log u$ 系数 $a$。

在唯一 normal 展开中，
$$
x=\sum_{k,n}x_{k,n}\gamma_n(g)e_k,\qquad
N(\gamma_n(g)e_k)\equiv n\gamma_n(g)e_k.
\tag{1168.5}
$$
令
$$
K_q(g)=\frac{(-1)^q}{q!}(1+\gamma_p(g))^q
\qquad(0\le q<p).
$$
R1155/R1167 的完整 factorial 尾界给
$$
\boxed{
\begin{aligned}
\phi_r(x)&=\sum_k\sigma(x_{k,q_k})K_{q_k}(g)F_k
              &&(x\in C^0),\\
\phi_{r-1}(a)&=\sum_k\sigma(a_{k,q_k-1})
                            K_{q_k-1}(g)F_k .
\end{aligned}}
\tag{1168.6}
$$
较高 source normal 项全被 $p$ 整除；
输出则保留 $K_q$ 的所有 $\gamma_{hp}$。
特别这些输出的正 normal 次数至少为 $p$，并被 $N$ 消去。
它们不能在构造 (1168.6) 之前丢掉。

## 2. 原 $H^1$ 的完整常数读式

对任意第二槽
$y=\sum y_{k,n}\gamma_n(g)e_k$，定义
$$
Y_{\rm hi}=\sum_k\sum_{n\ge q_k}y_{k,n}\gamma_n(g)e_k,\qquad
F(y)=\phi_r(Y_{\rm hi}),\qquad
F_+(y)=F(y)-F(y)|_{g=0}.
$$
这里 $|_{g=0}$ 只取已构造的 normal 常数项。
置
$$
\boxed{
T(y)=Y_{\rm hi}+F_+(y)\in C^0,\qquad
\mathcal R_{d,t}(y)=y|_{g=0}+F(y)|_{g=0}\in M_d/p .
}
\tag{1168.7}
$$
因为 $F_+$ 只含 $hp\ge p>q_k$，
$\phi_rF_+=0$、$NF_+=0$。因此准确有
$$
y-(1-\phi_r)T(y)
 =\mathcal R_{d,t}(y)
  +\sum_k\sum_{1\le n<q_k}y_{k,n}\gamma_n(g)e_k.
\tag{1168.8}
$$
这保留了 Frobenius 的高 normal carry 后再消去它。

展开实际 $\lambda_k$，读式成为
$$
\boxed{
\mathcal R_{d,t}(y)
 =\sum_i y_{i,0}e_i
  +(-1)^t\sum_{k=0}^d
       \frac{b_E^{\,2k-d}}{(t+k)!}\,
       \sigma(y_{k,t+k})\,e_{d-k}.
}
\tag{1168.9}
$$
它是 $\mathbb F_p$-线性的，显示保留系数上的 $\sigma$。
仅需每个原 basis 的 normal $0$ 和 $t+k$ 两项；
无需对整个 $y$ 另作不合法的 function-degree 截断。

**结论：** 对每个 (1168.2)，
$$
\boxed{\quad
H^0(C)=H^2(C)=0,\qquad
H^1(C)\xrightarrow[\ (a,y)\mapsto\mathcal R_{d,t}(y)\ ]{\ \sim\ }
M_d/p ,
\quad}
\tag{1168.10}
$$
且每个类有唯一常数代表
$$
\iota(m)=(0,m).
$$
下一节给完整同伦证明，因而 (1168.10) 不是根据维数猜测。

## 3. 全链收缩及所有被除的数

### 3.1. 只有一项常数方程

给定 $v=\sum v_{k,n}\gamma_n(g)e_k\in C^2$，
令 $T_k$ 暂表示所求 $a_{k,q_k-1}$。
定义 $\mathbb F_p$-线性映射
$$
\mathcal C(T)
 =\sum_{q_k=1}T_ke_k
 -\sum_k\frac{(-1)^{q_k-1}}{(q_k-1)!}
                  \sigma(T_k)F_k .
\tag{1168.11}
$$
所求 $d_1(a,y)=v$ 的 normal 常数式准确是
$\mathcal C(T)=v_0$。

若 $t\ge2$，第一和为空，第二和是一个可逆强可除基及
$\sigma$，所以 $\mathcal C$ 可逆。
明确地，
$$
T_k=(-1)^t(t+k-1)!\,b_E^{\,d-2k}
                    \sigma(v_{d-k,0}).
\tag{1168.12}
$$

若 $t=1$，本篇仅有 $d=4,8>0$。
唯一的第一和为 $T_0e_0$。
在 (1168.11) 先读 $e_d$ 系数即可唯一确定 $T_0$，
再读中间系数，最后读 $e_0$ 确定 $T_d$。
即
$$
\begin{aligned}
T_0&=-b_E^d\sigma(v_{d,0}),\\
T_k&=-k!b_E^{d-2k}\sigma(v_{d-k,0})\quad(1\le k<d),\\
T_d&=d!b_E^{-d}\sigma(T_0-v_{0,0}).
\end{aligned}
\tag{1168.13}
$$
因此这个实际 CM 反对角情形也可逆。
未把 $(d,t)=(0,1)$ 的额外 Kummer log 类包括进来；
该不在原 (1168.2) 中的情形本来不会满足同一结论。

### 3.2. 完整 $H_2$

用 (1168.12) 或 (1168.13) 的 $T_k$，定义仅含正低 normal
的 $y^{\rm lo}$：
$$
y^{\rm lo}_{k,n}=
\begin{cases}
-v_{k,n}/n,&1\le n<q_k-1,\\
(T_k-v_{k,n})/n,&n=q_k-1\ge1,\\
0,&\text{其它 }n .
\end{cases}
$$
所有被除的 $n$ 介于 $1$ 与 $13$，均为单位。
令
$$
F_T=\sum_k\sigma(T_k)K_{q_k-1}(g)F_k,\qquad
a=v+Ny^{\rm lo}+F_T,\qquad
H_2(v)=(a,y^{\rm lo}).
\tag{1168.14}
$$
常数方程和低次系数的定义保证
$a\in\operatorname{Fil}^{r-1}$ 且其 boundary 系数正是 $T_k$。
故 $\phi_{r-1}a=F_T$，从而
$$
d_1H_2(v)=v,\qquad
\mathcal R_{d,t}(y^{\rm lo})=0,\qquad T(y^{\rm lo})=0 .
\tag{1168.15}
$$

### 3.3. 完整 $H_1$ 与收缩身份

在 $C^1$ 上取 $H_1(a,y)=T(y)$。
对 $x\in C^0$，(1168.6) 的正 normal 输出均在 high 部分，
而再次 Frobenius 为零，故
$$
H_1d_0x=x.
$$
对一般 $(a,y)$，先减 $d_0T(y)$ 和
$\iota\mathcal R_{d,t}(y)$。
剩余第二槽恰为 (1168.8) 的正低 normal 部分。
其第一槽 boundary 系数由其 $d_1$ 的常数项
经 (1168.11) 唯一确定；其它低 normal 系数再由
(1168.14) 唯一确定。因此
$$
\boxed{\quad
dH+Hd=1-\iota\mathcal R,\qquad
\mathcal R\iota=1,\qquad
H\iota=\mathcal RH=H^2=0 .
\quad}
\tag{1168.16}
$$
$\mathcal R$ 在 $C^0,C^2$ 为零。
尤其 $\mathcal Rd_0=0$；也可由 (1168.7) 逐项看出
$x_{k,q_k}$ 的两份 Frobenius 常数恰相消。

这证明 (1168.10)，并给实际源的完整链同伦。
它在模 $p$ 的所列系数复形上成立；
没有宣称一个未经构造的全 $p^n$ 同伦。

## 4. 原四次、八次 theta 矩的实际有限读取

以下 $d=4,8$，$t=1$。沿 R1166 的原辅助数 $2$，记
$$
V_2(z)=-\frac1{z^3y(P(z))},\qquad
L_2(z)=\frac1p\log\frac{V_2(z)^p}{\psi V_2(z)}
       =\sum_{\ell\ge0}\ell_\ell z^\ell,
$$
其中 $L_2\in\mathcal O_F[[z]]$，$L_2(0)=0$。
原 $k_d(2)=4-2^{-d}$ 对所有 $p>37$ 为单位。
本节的 $L_2$ 是 theta Kummer 第二槽，
与 R1166 的 dilogarithm $L^\dagger_2$ 不同。

设
$$
j_k=p(d-k)+k,\qquad m_k=e-j_k.
\tag{1168.17}
$$
$0<j_k<e$，所以 $z^{j_k}L_2(z)$ 的零 $e$-block 为
$$
\sum_{a\ge1}\ell_{ae-j_k}u^a .
\tag{1168.18}
$$
它以 $u$ 开始，不能误取一个 $a=0$ 项。

R1167 给原 $e_k=\omega^{d-k}\eta^k$ 系数
$$
(-1)^d\binom dk b_E^{d-k}
 z^{j_k}(1+\gamma_p(g))^{d-k}g^k.
$$
将它与 $L_2$ 相乘后按 R1166 的无-log trace 取
$e$ 倍零块，再除原 $k_d(2)$，得到原 moment 第二槽 $y_d$。
其 normal 常数全部为零：$k>0$ 有 $g^k$，
$k=0$ 时 (1168.18) 在 $u=p$ 被 $p$ 整除。
(1168.9) 所需的另一项准确是
$$
(y_d)_{k,k+1}
 =\frac e{k_d(2)}(-1)^d
      \binom dk b_E^{d-k}(k+1)!\,\ell_{m_k}\pmod p.
\tag{1168.19}
$$
这里 $k+1<p$；$\gamma_p$ 的正幂在完成实际乘法和 trace
后仍有 normal 次数至少 $p$，所以确不进入这次指定读取。
(1168.18) 中只有 $a=1$ 进入 $k+1$ 项。

由 $d$ 偶、$e\equiv-1\pmod p$，代 (1168.9) 得
$$
\boxed{
\mathcal R_{d,1}(y_d)
 =\frac1{k_d(2)}
   \sum_{k=0}^d
       \binom dk b_E^k\sigma(\ell_{m_k})\,
                         \omega^k\eta^{d-k}.
}
\tag{1168.20}
$$
没有新 $d!$、平均 trace 或半点集。
本式先在实际未分歧二次底 $F$ 读取原类的 restriction；
原两槽及结果均来自 $\mathbb Q_p$，不为此再平均或乘二。
未分歧 restriction 后再 corestriction 为二，$p>37$ 时可逆，
故该读取也唯一锁定原底上的类。
第一层的 primitive/all-vector 因子 $1-p^d$ 为一；
高层的原 same-root gauge 仍沿 R1147。

## 5. 进一步实算为原 Hurwitz–Eisenstein 系数

### 5.1. 相同 formal logarithm 的有限范围

仅为读取这一已指定的有限系数，在特征零置
$$
v=\int\omega,\qquad v=z+O(z^{e+1}).
$$
第二式由 R1167 的 $\omega=(1+O(z^e))dz$ 得到。
它只用于次数严格小于 $e$ 的恒等式；
没有声称整个 formal logarithm 为整坐标。

用同一短 Weierstrass 模型定义原 Hurwitz–Eisenstein 多项式：
$$
x(v)=v^{-2}+
 \sum_{\substack{m\ge4\\m\ {\rm even}}}
           (m-1)G_m(\mathcal E)v^{m-2}.
\tag{1168.21}
$$
例如 $G_4=-A/15$、$G_6=-B/35$，
与 R1161 的 $G_m$/$Q_s$ 归一完全相同。
记
$$
\mathcal E(v)=v^{-1}-\sum_m G_m v^{m-1}.
$$
椭圆加法的倍点式给
$$
\mathcal E(2v)-2\mathcal E(v)
     =\frac{3x(v)^2+A}{2y(v)}.
$$
又 $dy/dv=3x^2+A$，所以
$$
\frac d{dv}\log\left(-\frac1{v^3y(v)}\right)
 =4\mathcal E(v)-2\mathcal E(2v)-\frac3v
 =\sum_m(2^m-4)G_m v^{m-1}.
\tag{1168.22}
$$
归一常数在 $v=0$ 为一，故该 formal logarithm 常数为零。

由于 $v/z=1+O(z^e)$，将 $v$ 换回 $z$，
所有 $m<e$ 的系数保持：
$$
[z^m]\log V_2(z)=\frac{2^m-4}{m}G_m(\mathcal E).
\tag{1168.23}
$$

### 5.2. 需要的系数确为整，且原平滑因子精确相消

(1168.17) 的指数满足
$$
m_k\equiv-(k+1)\pmod p,\qquad
m_k\equiv-d\pmod{p-1}.
\tag{1168.24}
$$
所以 $p\nmid m_k(m_k-1)$。
(1168.21) 在 $z^{m_k-2}$ 的系数与整 Laurent series $x(z)$
完全相同，故 $(m_k-1)G_{m_k}$ 整，
进而 $G_{m_k}\in\mathbb Z_p$。
这里没有对一个可能有 $p$ 分母的高权 Eisenstein 归一作猜测。

在 formal $F[[z]]$ 中，
$$
L_2(z)=\log V_2(z)-\frac1p\sigma(\log V_2)(z^p).
$$
因为 $p\nmid m_k$，第二项不贡献 $z^{m_k}$。
再用 $2^{m_k}-4\equiv-k_d(2)$，(1168.20) 准确化为
$$
\boxed{
\mathcal R_{d,1}(y_d)
 =\sum_{k=0}^d
   \frac{\binom dk}{k+1}\,
      b_E^k G_{\,p^2-1-pd+(p-1)k}(\mathcal E)\,
      \omega^k\eta^{d-k}\pmod p ,
 \qquad d=4,8.
}
\tag{1168.25}
$$
$\sigma$ 在这些 $G_m(\mathcal E)\in\mathbb Z_p$ 上为恒等。
原平滑因子通过同一个 theta 的实际系数消去，
不是在开始前把它规范成一。

### 5.3. 原两个 CM 中心的具体支持

cubic 模型上，$G_m=0$ 除非 $6\mid m$。
因此原四次读数只有一项：
$$
\boxed{
\mathcal R_{4,1}(y_4)
 =2b_E^2G_{(p-3)(p+1)}\,\omega^2\eta^2 .
}
\tag{1168.26}
$$
原八次读数准确为
$$
\boxed{
\begin{aligned}
\mathcal R_{8,1}(y_8)
={}&4b_EG_{p^2-7p-2}\,\omega\eta^7\\
 &+14b_E^4G_{(p-5)(p+1)}\,\omega^4\eta^4\\
 &+b_E^7G_{p^2-p-8}\,\omega^7\eta .
\end{aligned}}
\tag{1168.27}
$$

Gaussian 模型上，$G_m=0$ 除非 $4\mid m$，
所以 (1168.25) 只留偶数 $k$。
明确地，
$$
\mathcal R_{4,1}(y_4)
 =G_{p^2-4p-1}\eta^4
  +2b_E^2G_{p^2-2p-3}\omega^2\eta^2
  +\frac{b_E^4}{5}G_{p^2-5}\omega^4,
\tag{1168.28}
$$
$$
\begin{aligned}
\mathcal R_{8,1}(y_8)
={}&G_{p^2-8p-1}\eta^8
 +\frac{28b_E^2}{3}G_{p^2-6p-3}\omega^2\eta^6\\
 &+14b_E^4G_{p^2-4p-5}\omega^4\eta^4
 +4b_E^6G_{p^2-2p-7}\omega^6\eta^2\\
 &+\frac{b_E^8}{9}G_{p^2-9}\omega^8 .
\end{aligned}
\tag{1168.29}
$$
这些是原系数的实际模 $p$ 值公式，
没有据 CM 支持再假定其中任何一个 $G_m$ 为单位。
它们也没有由某一参考曲线的支持外推一般无 CM 曲线。

## 6. 原中央 primitive 的有序 gauge 读取

原向量一次 cochains 记为
$$
v=(a_4,a_8,c_5),\qquad dv=0,
$$
其 second-slot 向量记为 $y_v$。
原中央 cochain $h=(h_0,h_2,h_4)$ 满足
$$
dh=-\mathfrak b(v,v),\qquad
\mathfrak b((x,y,t),(x',y',t'))
 =(\Pi_0(x,y'),\Pi_2(x,y'),\Pi_4(x,y')+\lambda_\infty xt').
\tag{1168.30}
$$
这里的 $\lambda_\infty$ 保原正号；
$dh$ 的外负号不再重复并入 $\mathfrak b$。

逐个实际系数复形取
$$
R=T_V(y_v),\qquad A=\mathcal R_V(y_v).
$$
由完整收缩，对闭合 $v$，
$$
v'=v-dR=(0,A).
\tag{1168.31}
$$
原 R1163 的 cochain gauge 身份在这个方向准确给
$$
h'=h-\mathfrak b(v,R)+\mathfrak b(R,v)-\mathfrak b(R,dR).
\tag{1168.32}
$$
直接取微分得 $dh'=-\mathfrak b(v',v')=0$：
两个常数一次 cochains 的第一槽均为零，
原 ordered cone product 因而字面为零。

还可把 (1168.32) 的 second 槽完全写出。
原 product 在 degree $(1,0)$ 的 second 槽为
$y_vR$，在 $(0,1)$ 的 second 槽为 $\phi(R)y_v$。
又 $y_v-R+\phi(R)=A$。
因此
$$
\boxed{
y_{h'}=y_h-\mathfrak b(y_v,R)+\mathfrak b(\phi(R),A),
\qquad
H=\mathcal R_Z\!\left(
 y_h-\mathfrak b(y_v,R)+\mathfrak b(\phi(R),A)\right).
}
\tag{1168.33}
$$
$\mathcal R_Z$ 分别使用 (1168.2) 的后三个 $(d,t)$。
所有 $\Pi_r$、Tate coevaluation 和 $\lambda_\infty$ 均沿原 map。
这里的 $\phi(R)$ 逐个使用其原 divided weight，
并非一个没有 twist 的共同 raw Frobenius。

继续减去原中央 $dT_Z(y_{h'})$，便把同一 primitive
送到常数 $(0,H)$。
这些 gauges 均在原 $\operatorname{Fil}^r$ 中，
且 $r>\max w_k$，所以其几何 specialization 全为零。
因此它们不改变原映到一的唯一 Hodge lift；
没有新添一个常数 Hodge 平移。

## 7. 真正 Frobenius 中央坐标的最后符号

原 R1166 (1166.54)、(1166.54a) 已由同一 whole-path
matrix 与整 root tower 锁定
$$
Z=\mathfrak b(A,A)-H.
$$
把 (1168.33) 代入，得到本篇的完整实际读式
$$
\boxed{
Z=\mathfrak b(A,A)
-\mathcal R_Z\!\left(
 y_h-\mathfrak b(y_v,T_V(y_v))
        +\mathfrak b(\phi T_V(y_v),A)\right).
}
\tag{1168.34}
$$
$A=\mathcal R_V(y_v)$，每一个 $\mathcal R$ 都是
(1168.9) 的两层原 normal 读取，$T$ 则保
(1168.7) 的实际高 normal Frobenius carry。

所以不能把 $\mathcal R_Z(y_h)$ 直接叫作原中央 $F_0$；
也不能在未经 gauge 修正时把一个 scalar $\beta$ 的 trace
叫作该值。(1168.34) 精确保留了二者之间的原二次项。

本篇已实际读取两条原 abelian CM moments，并给全部
四十三维 coefficient cone 的常数收缩及中央
有序读取。原最高 correlation 的实际加权读数在下文 §§8–9 完成；
算术未平滑、其它中心及全局减法仍沿同一个原 source 继续。
本篇没有将一个尚未证明非零的指定系数宣称为单位。


## 8. 最高 correlation 的全部指定 normal 读数

本节沿 R1158 的 **raw** $n=2$ correlation 群。
对 $d=4,8$，令 $\mathcal A_{d,k}$ 是原 $X_{2,d}$
在 R1168 常数 frame 中的 $\omega^k\eta^{d-k}$ 系数；
令 $\mathcal A'_{i,d,k}$ 为同一实际二同源核
$C_i\subset E[2]$ 对应的 $X'_{2,C_i,d}$ 系数。
它们尚未除以 $k_d(2)$。置
$$
B_{k,l}
 =\mathcal A_{4,k}\mathcal A_{8,l}
  -\sum_{i=1}^3\mathcal A'_{i,4,k}\mathcal A'_{i,8,l},
\qquad 0\le k\le4,\quad0\le l\le8.
\tag{1168.35}
$$
原两个 primed 槽须使用同一个 $i$，求和保留原
same-coset trace，不能改成两个独立和。

**实际读数为**
$$
\boxed{
Z_{\rm corr}^{\rm BCH}
 =\sum_{k=0}^4\sum_{l=0}^8
   \frac{k-l}{2(k+l+2)}B_{k,l}\,
        \omega^{k+l}\eta^{12-k-l}.
}
\tag{1168.36}
$$
相同 frame 的原 ordered 中央坐标为
$$
\boxed{
Z_{\rm corr}^{\rm ord}
 =\sum_{k=0}^4\sum_{l=0}^8
   \frac{k+1}{k+l+2}B_{k,l}\,
        \omega^{k+l}\eta^{12-k-l}.
}
\tag{1168.37}
$$
所有分母的整数因子不超过 $28$，对 $p>37$ 均可逆。
这是完整原最高平滑相关项的模 $p$ Frobenius 值；
不含一个仍待指定的 $U$-primitive 系数。

### 8.1. 用原微分关系锁定唯一会进入的系数

按 R1166 §§19–21，原 highest primitive 在同一
coefficient cone 中满足
$$
h_{\rm corr}=(0,\tfrac12b_2(y,y)+J_U),\qquad
J_U=\frac1{54}\sum_{\mathcal J^\circ}
                  \mathscr Q(P,Q)\beta^U_{P,Q}.
\tag{1168.38}
$$
这里 $y$ 合记所有 raw original 与 primed moments。
R1166 已逐个实际源证明
$$
y_{d,k,n}=0\ (n<k+1),\qquad
(J_U)_{K,0}=0,\qquad
a=N_uy,\qquad\phi_d a=0.
\tag{1168.39}
$$
本节临时用的 $k$ 是输入基
$e_k^{(d)}=\omega^{d-k}\eta^k$ 的下标；
(1168.35) 则用 Frobenius 后的输出基
$e_{d-k}^{(d)}=\omega^k\eta^{d-k}$。
这两个下标通过 (1168.9) 准确对应。

原 ordered cone product 的第二槽为
$b_2(y,a)-b_2(\phi_d a,y)=b_2(y,N_uy)$。
由 $dh_{\rm corr}=-b_2(v,v)$、第一槽零和
$d_1(0,h)=-N_uh$，得
$$
\boxed{
N_uJ_U
 =\frac12\{b_2(y,N_uy)-b_2(N_uy,y)\}.
}
\tag{1168.40}
$$
这一步已带入原 $N_z=eN_u$ 及 log-trace 尺度；
不再另乘或除一个 $e$。

固定 $K=k+l$，令 $q=K+2$。
(1168.39) 表明，右边的 normal $q$ 项只能由
normal $k+1$ 与 $l+1$ 相乘给出。
没有其它低项或高 $\gamma_{hp}$ carry 可以降到这里。
又
$$
\gamma_{k+1}(g)\gamma_{l+1}(g)
 =\binom{q}{k+1}\gamma_q(g),\qquad
N_u\gamma_n(g)=n\gamma_n(g)\pmod p.
$$
所以，直接读 (1168.40) 的系数得
$$
\boxed{
\begin{aligned}
(J_U)_{K,q}
 =\sum_{k+l=K}
   \frac{l-k}{2q}\binom q{k+1}
   \Bigl(&y_{4,k,k+1}y_{8,l,l+1}\\
       &-\sum_{i=1}^3
           y'_{i,4,k,k+1}y'_{i,8,l,l+1}\Bigr).
\end{aligned}}
\tag{1168.41}
$$
$2\le q\le14<p$，故 (1168.40) 唯一确定这份系数。
$N_u$ 在其它 normal 层可能有核，不能据此解出整个
$J_U$；但那些层不进入本次读式。
唯一另外会进入的 normal 常数已经由
(1168.39) 的 actual ordinary source 支付为零。

### 8.2. 原 Frobenius、二项系数及两份负号

由 (1168.9) 和原 moments 的零常数，
$$
\begin{aligned}
\mathcal A_{d,k}
 &=-\frac{b_E^{2k-d}}{(k+1)!}
                   \sigma(y_{d,k,k+1}),\\
\mathcal A'_{i,d,k}
 &=-\frac{b_E^{2k-d}}{(k+1)!}
                   \sigma(y'_{i,d,k,k+1}).
\end{aligned}
\tag{1168.42}
$$
最高中心的 $t=2$ 则给正号：
$$
\mathcal R_{12,2}(J_U)
 =\sum_{K=0}^{12}
    \frac{b_E^{2K-12}}{(K+2)!}
       \sigma((J_U)_{K,K+2})\,
                    \omega^K\eta^{12-K}.
\tag{1168.43}
$$
将 (1168.41) 代入 (1168.43)，
二项系数与 $(K+2)!$ 消成
$1/((k+1)!(l+1)!)$；
两份 (1168.42) 的负号相乘为正，
$b_E$ 的指数恰为 $2(k+l)-12$。
因此准确有
$$
\mathcal R_{12,2}(J_U)
 =\sum_{k,l}\frac{l-k}{2(k+l+2)}
          B_{k,l}\,\omega^{k+l}\eta^{12-k-l}.
\tag{1168.44}
$$
R1166 (1166.80) 已在完整非线性 gauge 后给
$Z_{\rm corr}^{\rm BCH}=-\mathcal R_{12,2}(J_U)$，
故得到 (1168.36)。
原 ordered 坐标再加 $b_2(A,A)/2$，
其每项系数为
$$
\frac12+\frac{k-l}{2(k+l+2)}
 =\frac{k+1}{k+l+2},
$$
证明 (1168.37)。这里没有假定
$\mathcal R(xy)=\mathcal R(x)\mathcal R(y)$。

## 9. 这次求和关闭的范围与原未平滑接口

(1168.36)–(1168.37) 消去了最高相关 Frobenius
读取中全部尚未求值的 $J_U$ 项。
原独立点对、保留下来的全部依赖点对、三实际
$2$-同源核、同根相位及同陪集 Cor 都已经包括在
(1168.38) 的原源中；没有再删一类点对。
尤其不是只把每个 scalar $\beta^U$ 命名后留下其加权和。

实际剩余输入只是 (1168.35) 中已指定的 abelian
矩系数；unprimed 值由 (1168.25) 乘回 $k_d(2)$ 给出。
下文 §§10–11 继续给 primed theta 的同一个 $V'_i$
及其全部实际系数。
本节没有证明这些实际双线性组合是单位。

这里的群仍为 R1158 的 raw correlation 群。
R1159 的 $n$、$k_d(n)$、crossed $J_n$ 以及
R1160 的算术 $B_n/v_n$ 并未被这个局部读取删除。
原未平滑 $F_0$ 必须沿那一份实际比较继续；
另外两个 $\Pi_2,\Pi_4$ 中心及 $\lambda_\infty$
仍按 (1168.34) 保留。
所以本节关闭的是完整最高 **平滑相关读数**，
不把它冒称原未平滑中央值，更不称主目标完成。

上述 normal 微分读取、全部 factorial 与 BCH/ordered
符号已逐式纸推，并经 global_route 独立核准；
无数学程序执行。


## 10. 三个实际 primed 矩的 Hurwitz 系数闭式

本节把 (1168.35) 的每个 primed 输入也写成同一原微分
归一的实际 Hurwitz 系数。商曲线不必仍具有 cubic
或 Gaussian 的特殊短方程；本节不把 (1168.25) 的 CM
反对角矩阵直接套给商曲线。

### 10.1. 原二同源的准确短模型与共同参数

写原曲线为
$$
E:\ y^2=x^3+Ax+B,\qquad
A_i=(e_i,0),\qquad K_i=3e_i^2+A.
$$
所有 $e_i$ 在原未分歧二次底中，$K_i$ 为单位。
二扭点加法直接给
$$
x(P+A_i)=e_i+\frac{K_i}{x(P)-e_i}.
$$
于是实际 quotient $E_i=E/C_i$ 可使用
$$
\begin{aligned}
X_i&=x+x(P+A_i)-e_i=x+\frac{K_i}{x-e_i},\\
Y_i&=y\left(1-\frac{K_i}{(x-e_i)^2}\right),\\
E_i:\quad Y_i^2&=X_i^3+(A-5K_i)X_i+(B-7e_iK_i).
\end{aligned}
\tag{1168.45}
$$
最后的方程由 $x^3+Ax+B=(x-e_i)((x-e_i)^2+
3e_i(x-e_i)+K_i)$ 代入直接展开得到。
$X_i,Y_i$ 在 $P\mapsto P+A_i$ 下不变，
$X_i$ 在原两点各有二阶极，故此图准确是原 degree-two
quotient。其微分满足
$$
\psi_i^*\omega_i=\omega,\qquad
\omega_i=dX_i/(2Y_i).
$$
$K_i$ 与 $9e_i^2-4K_i=(e_j-e_k)^2$ 均为单位，
显示的 quotient 判别式
$256K_i(9e_i^2-4K_i)^2$ 也为单位。

在共同参数 $v=\int\omega$ 中，
$\psi_i^*\int\omega_i=v$，原点常数均取零。
$X_i(v)$ 的首项为 $v^{-2}$ 且无常数项，所以
$$
X_i(v)=v^{-2}+
 \sum_{\substack{m\ge4\\m\ {\rm even}}}
       (m-1)G_m(E_i,\omega_i)v^{m-2}.
\tag{1168.46}
$$
这里 $G_m(E_i,\omega_i)$ 是 (1168.45) 那一个具体
短模型的 Hurwitz 系数，不是一个另选的 isogenous
CM period。

### 10.2. 原 $V'_i$ 的每个所需系数

为简写，令
$$
x(P(v)+A_i)
 =\sum_{\substack{m\ge2\\m\ {\rm even}}}
          (m-1)H_{i,m}v^{m-2},
\qquad H_{i,2}=e_i.
$$
(1168.45)–(1168.46) 直接给
$$
G_m(E_i,\omega_i)=G_m(E,\omega)+H_{i,m}
\qquad(m\ge4).
\tag{1168.47}
$$
再置 $r_i=y/(x-e_i)$。实际微分为
$$
\frac{dr_i}{dv}=x-x(P+A_i).
$$
$r_i$ 是奇函数，首项 $-v^{-1}$，
所以在特征零准确有
$$
r_i=-v^{-1}
 +\sum_{\substack{m\ge2\\m\ {\rm even}}}
       (G_m(E,\omega)-H_{i,m})v^{m-1},
\qquad G_2(E,\omega)=0.
$$
另一方面，原 R1166 的
$V'_i=z^2(x-e_i)V_2$ 给
$$
\frac d{dv}\log\!\left(-\frac{x(v)-e_i}{v\,y(v)}\right)
 =\frac d{dv}\log\!\left(-\frac1{v^3y(v)}\right)
       +\frac2v+2r_i .
$$
使用 (1168.22)、(1168.47)，并按
$v/z=1+O(z^e)$ 换回原严格 LT 坐标，得
$$
\boxed{
[z^m]\log V'_i(z)
 =\frac{2^mG_m(E,\omega)-2G_m(E_i,\omega_i)}{m}
 \qquad(4\le m<e,\ m\ {\rm even}).
}
\tag{1168.48}
$$
这是原函数的系数恒等式；没有换掉 $\theta'_{2,C_i}$
或给它添加一个常数原函数。

对本篇所需 $m=m_k$，$p\nmid m(m-1)$。
(1168.45) 的 $X_i(z)$ 是整 Laurent series；
$v/z=1+O(z^e)$ 保持 $z^{m-2}$ 系数，
故 $(m-1)G_m(E_i,\omega_i)$ 整，
进而 $G_m(E_i,\omega_i)\in\mathcal O_F$。
同理 $H_{i,m}$ 也整。
所以 (1168.48) 在需要的高权处可以合法约模 $p$，
没有援引一个未经证明的高权 $p$ 整性。

### 10.3. 实际 raw primed 常数

为固定所有尺度，置
$$
c_{d,k}=\frac{\binom dk}{k+1}b_E^k,\qquad
m_{d,k}=p^2-1-pd+(p-1)k.
$$
(1168.25) 乘回原 $k_d(2)$，给
$$
\mathcal A_{d,k}
 =(4-2^{-d})c_{d,k}G_{m_{d,k}}(E,\omega).
$$
对 primed 槽直接用同一 normal 读取，
但不除原 $k_d(2)$，得到
$$
\mathcal A'_{i,d,k}
 =\binom dk\,b_E^k\,
     \sigma([z^{m_{d,k}}]\log V'_i).
$$
此处 $p\nmid m_{d,k}$，故原
$p^{-1}\log((V'_i)^p/\psi V'_i)$ 的
$\psi$ 项不贡献这个系数。
将 (1168.48)、$m_{d,k}\equiv-(k+1)\bmod p$ 和
$2^{m_{d,k}}\equiv2^{-d}\bmod p$ 代入，准确得到
$$
\boxed{
\begin{aligned}
\mathcal A_{d,k}
  &=(4-2^{-d})c_{d,k}G_{m_{d,k}}(E,\omega),\\
\mathcal A'_{i,d,k}
  &=c_{d,k}
    \left(2\sigma G_{m_{d,k}}(E_i,\omega_i)
                   -2^{-d}G_{m_{d,k}}(E,\omega)\right),
\qquad d=4,8.
\end{aligned}}
\tag{1168.49}
$$
保留 $\sigma$ 是必需的：$e_i$ 及商曲线未必定义在
$\mathbb Q_p$，而原 $G_m(E,\omega)\in\mathbb Z_p$。
整个式子的输出仍在原 $E$ 的
$\omega^k\eta^{d-k}$ 基中。

这里使用的是 primed theta 在原形式盘上的直接读取。
若改由商曲线的 whole moment 运输，必须同时带
R1159 (1159.30)–(1159.31) 的 exact 项及
$\omega_i\mapsto\omega/2$、
$\eta_i\mapsto\eta-e_i\omega/2$；
本式没有把那个实际 coefficient map 误当成恒等。

## 11. 同核相关项的完全显式三同源式

三个实际单位在原环中恰满足
$$
\prod_{i=1}^3V'_i
 =-\frac{\prod_i(x-e_i)}{z^3y^3}
 =-\frac1{z^3y}=V_2.
$$
这也核准原 theta Norm 的全部 leading：
$\prod_iK_i=-\Delta/16$，从而
$\prod_i\Delta/(16K_i^2)=\Delta/16$，
三个 $[z]$ 恰合成原 $3[z]$。
该等式按已给定的实际 Norm morphism 进入唯一 Hodge
frame；不将另一套 Galois 根相位擅自设为零。

同一乘积身份用 $v$ 代 $z$ 也严格成立。
因此由 §10.2 的特征零微分式，得到
$$
\sum_{i=1}^3G_m(E_i,\omega_i)
 =(2+2^m)G_m(E,\omega)\qquad(m\ge4,\ m\ {\rm even}).
$$
在 (1168.49) 所需的整系数处，得到
$$
\boxed{
\sum_{i=1}^3\sigma G_{m_{d,k}}(E_i,\omega_i)
 =(2+2^{-d})G_{m_{d,k}}(E,\omega),\qquad
\sum_i\mathcal A'_{i,d,k}=\mathcal A_{d,k}.
}
\tag{1168.50}
$$
这里只核准同一个已登记 Norm 在新系数公式中的值，
不以两个独立 Norm 代替同核乘积。

具体令
$$
m=m_{4,k},\qquad n=m_{8,l},\qquad
G_m=G_m(E,\omega),\qquad
G_{i,m}=G_m(E_i,\omega_i).
$$
把 (1168.49) 逐项代入 (1168.35)，
再用 (1168.50) 仅消去两个一次 trace，得
$$
\boxed{
B_{k,l}
 =c_{4,k}c_{8,l}
 \left\{(2^4+2^{-11})G_mG_n
       -4\sum_{i=1}^3
                 \sigma(G_{i,m})\sigma(G_{i,n})\right\}.
}
\tag{1168.51}
$$
完整 scalar 核准是：若 $a=2^{-4}$、$b=2^{-8}$，
则原项为
$$
(4-a)(4-b)+2b(2+a)+2a(2+b)-3ab
 =16+2ab=2^4+2^{-11}.
$$
原 primed 两个因子仍使用同一个 $i$。
也可由 (1168.50) 写为
$B_{k,l}=\sum_{i\ne j}\mathcal A'_{i,4,k}
\mathcal A'_{j,8,l}$，但不将它错误地置零。

(1168.36)–(1168.37) 与 (1168.51) 现在给完整
最高相关 Frobenius 的指定有限系数式，
其输入只含原曲线及三个具体 (1168.45) 的 Hurwitz 系数。
其中 $2^4+2^{-11}$、$4$ 与 R1159 的实际
$\mathcal V_2$ 功能方程相同。
这没有将跨同源的 $\mathcal V_2$ 改成单点 $v_2$，
也没有证明显示的三同源相关和非零。
原未平滑、其余中心和全局排点继续沿既有实际源推进。

以上 quotient 方程、原单位微分、全部高权整性及
同核 scalar 均由正文逐式证明，无数学程序执行。

## 已登记来源与执行

- R1163：原完整 coefficient projectors、paired coevaluation 和
  $(a,b,c;h)$ 的实际 gauge。
- R1165：原实际 log cone、$N$、divided Frobenius 和 ordered product。
- R1166：原 ambient/residue comparison、tame trace、theta $W^{-1}$，
  以及原 Steinberg $\beta$ 和 $Z=\mathfrak b(A,A)-H$。
- R1167：同一个 $b_E$、CM crystalline 两列、实际第一层 $x_P$
  与所有 pure-power normal 系数。
- R1161：同一 $G_m$ 的 Weierstrass/Hurwitz 归一。

以上线性收缩、有限读式、Eisenstein 系数和中央 gauge
均由正文自证。全部为纸面证明，无数学程序执行。
