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
有序读取。原 $y_h$ 的完整 27 项、实际权、same-coset Cor、
算术未平滑及全局减法仍须用已登记的同一个 source 继续求和。
未对这些尚未求完的指定和宣称单位，也未宣本课题完成。

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
