# R236 附录：对称高位平均排除规范 Bell 解析核

日期：2026-11-12；修订：2026-11-13（UTC）。作者：central_next；第9节二次多项式推论由root补充。
状态：已证明。完整支付统一高位平均、真实自然幂域和局部交换子预算。
本稿关闭规范 first 的 Bell 解析分支，普通 ISP 仍未完成。

## 1. 目标定理与两个相匹配的成本

在实际 Haar 模型中，置
$$
 a_j=\frac{(-1)^j}{j+1},\qquad
 X=\sum_{j\ge0}a_jV_j,\qquad
 B=\sum_{j\ge0}a_j^2(I-V_j^2).
\tag{1.1}
$$
常数项为 `a_*=0`。令 `phi` 是零点邻域上任一固定全纯函数，定义
$$
 Y=\phi(B)\in\mathcal A,\qquad T=X-Y,\qquad M=\ker T.
\tag{1.2}
$$
所有闭域、自然幂及 `C` 自伴性质均取真实实现。

**定理。**
$$
 \boxed{\ker\bigl(X-\phi(B)\bigr)=\{0\}.}
\tag{1.3}
$$
证明不把“每个固定次闭像包含原核”直接升级到广义核。
它改为构造随幂次增长、输出仍一致有界的真实幂像逼近，并与局部交换子的实际四次衰减相配。

具体地将证明存在有限头有界算子 `mathcal B_r`，使
$$
 \mathcal B_r M\subseteq\operatorname{Dom}T^r,\qquad
 T^r\mathcal B_rf\longrightarrow f\quad(f\in M),
\tag{1.4}
$$
$$
 \boxed{\|\mathcal B_r\|\le e^{r^3}/r!\quad\hbox{对充分大 }r.}
\tag{1.5}
$$
另一方面，对每个固定有限局部矩阵 `D`，存在固定 `U_h∈Acal`，使
$$
 \boxed{
 \|\operatorname{ad}_T^rD\|
 \le \|D\|(2\|U_h\|)^r
 \exp\!\left[-\frac56r^4+105r^3\right].
 }
\tag{1.6}
$$
幂像输入的三次指数成本被局部交换子的四次衰减吸收。
第 8 节将用完整域配对把这变成 `B(Df,g)=0`，再由实际局部代数的不可约性推出 (1.3)。

## 2. 随 r 增长的高位窗口与输入算子

取整数
$$
 m=m_r=\lceil e^{r^2}\rceil,\qquad q=q_r=r^4,\qquad
 I_r=\{m,m+1,\ldots,m+q-1\}.
\tag{2.1}
$$
以下只使用充分大 `r`，故 `q≥r`。
对每个 `F⊂I_r`、`|F|=r`，记
$$
 J_F=\prod_{j\in F}M_{\chi_j},\qquad p_F=\prod_{j\in F}a_j,
$$
并定义有限头有界算子
$$
 \boxed{
 \mathcal B_r=\frac1{(-2q)^r}
       \sum_{\substack{F\subset I_r\\|F|=r}}p_F^{-1}J_F.
 }
\tag{2.2}
$$
所有 `p_F` 非零。绝对值求和已足够给
$$
 \|\mathcal B_r\|
 \le\frac1{(2q)^r}\binom qr(m+q)^r
 \le\frac{(m+q)^r}{2^r r!}.
\tag{2.3}
$$
充分大 `r` 时 `m+q≤2e^(r²)`，所以 (1.5) 成立。
这里不声称输入成本一致有界；它已经被明确记录。

## 3. 任意选中 r 元集的统一真实 gauge 误差

固定本节的 `r,m,q,F`，令 `ell=m+q−1`，`gamma_F(Q)=J_FQJ_F`，
并令 `s_k=−1` 当 `k∈F`，否则 `s_k=1`。

使用真实递归
$$
 N_k=E_k+\eta_kE_k^*N_{k+1},\qquad
 N_k^2=\eta_kN_{k+1},\qquad
 \eta_k\le\bar\eta_k:=e^{-770\,16^k}.
\tag{3.1}
$$
有对所有 `F` 统一的界
$$
 \|\gamma_F(N_k)-s_kN_k\|\le
 \begin{cases}
 2\alpha_m/\alpha_k,&k<m,\\
 2\eta_k,&m\le k\le\ell,\\
 0,&k>\ell.
 \end{cases}
\tag{3.2}
$$
第一行由在第 `m` 位切开的实际有限链得到。
窗口内若 `k∈F`，则
$$
 \gamma_F(N_k)+N_k
 =\eta_kE_k^*(N_{k+1}-\gamma_F(N_{k+1}));
$$
若 `k∉F`，同样公式改为差和反向符号，范数界不变。
这涵盖任意有孔的 `F`，没有把它默认为相邻块。

`||(I±N_k)⁻¹||<3`，故有理逆差给
`||gamma_F(V_k)−V(s_kN_k)||` 分别不超过 (3.2) 右端的 `18` 倍。
所有这些 `V` 的范数至多 `6`。

定义
$$
 \widehat X_F=X+\sum_{j\in F}a_j(V(-N_j)-V(N_j)),
$$
$$
 \widehat B_F=B+\sum_{j\in F}a_j^2(V(N_j)^2-V(-N_j)^2),
 \qquad \widehat Y_F=\phi(\widehat B_F),
$$
$$
 A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
 E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F).
\tag{3.3}
$$
`A_F∈Acal` 为有界算子，与 `T` 完整交换。
`E_F` 有界，但不被假定在 `Acal` 中。

### 3.1 固定全纯轮廓

固定一个位于 `phi` 全纯邻域中的圆 `Gamma={|z|=rho}`，`rho>0`，
并置
$$
 R_\Gamma=\max_\Gamma\|(z-B)^{-1}\|,\qquad
 C_\Gamma=2\rho\max_\Gamma|\phi(z)|R_\Gamma^2.
\tag{3.4}
$$
这些与 `r,m,q,F` 都无关。

由准确有理恒等式
$$
 V(-N)-V(N)=4N(I-N^2)^{-1},
$$
$$
 V(-N)^2-V(N)^2
 =8N(I+N^2)(I-N^2)^{-2}
\tag{3.5}
$$
可得
$$
 \|\widehat B_F-B\|
 \le32\sum_{j\in F}|a_j|^2
 \le\frac{32r}{(m+1)^2}\longrightarrow0.
\tag{3.6}
$$
故充分大 `r` 时，`widehat B_F` 的实际预解式在 `Gamma` 上至多为
`2R_Gamma`，统一于全部 `F`。
`gamma_F(B)` 与 `B` 酉等价，其轮廓预解式范数仍为 `R_Gamma`。
两次真实全纯逆差积分因此都可用同一个 `C_Gamma`。

### 3.2 与 F 无关的 carry 小量

由
$$
 \sum_{k<m}|a_k|\frac{\alpha_m}{\alpha_k}
 <2\bar\eta_{m-1},\qquad
 \sum_{k<m}|a_k|^2\frac{\alpha_m}{\alpha_k}
 <2\bar\eta_{m-1},
$$
以及 `sum_(k≥m)bar eta_k≤2bar eta_m`，(3.2) 给
$$
 \|\gamma_F(X)-\widehat X_F\|\le144\bar\eta_{m-1},
$$
$$
 \|\gamma_F(B)-\widehat B_F\|\le1728\bar\eta_{m-1}.
$$
所以
$$
 \boxed{
 \|E_F\|\le C_E\bar\eta_{m-1},\qquad
 C_E=144+1728C_\Gamma.
 }
\tag{3.7}
$$
该常数不随窗口大小或选中位数增长。

令
$$
 P_F=4\sum_{j\in F}a_jN_j,\qquad C_A=6+32C_\Gamma.
$$
由 (3.5)—(3.6)，
$$
 \boxed{
 \|A_F-P_F\|\le\frac{C_Ar}{(m+1)^2},\qquad
 \|P_F\|\le\frac{4r}{m+1}.
 }
\tag{3.8}
$$
充分大 `r` 时 `m≥C_A`，故另有
$$
 \|A_F\|\le\frac{5r}{m+1}.
\tag{3.9}
$$

## 4. 同一闭尾 first 上的完整域与非交换幂误差

置
$$
 \mathcal D=\operatorname{Dom}T,\qquad
 X_{>\ell}=X-\sum_{k=0}^{\ell}a_kV_k,\qquad
 D_\ell^{\rm bd}=\sum_{k=0}^{\ell}a_kV_k-Y.
\tag{4.1}
$$
`X_(>ell)` 与 `X` 只差有界项，完整域仍为 `D`。
这里的尾域交换可由真实图核心直接付清。R125 §4 证明有限柱空间
`P` 是 `X` 的图核心；减去有限头有界项后，它仍是 `X_(>ell)` 的图核心。
若 `L` 是支撑在前 `ell+1` 位的任意固定局部矩阵，则 `L P⊂P`。
在 `P` 上，尾部各有限截断都与 `L` 交换；R125 的核心收敛给
`X_(>ell)Lx=L X_(>ell)x`。对任意 `x∈D` 取有限柱图逼近，
`L` 有界与 `X_(>ell)` 闭性遂给
$$
 L\mathcal D\subseteq\mathcal D,\qquad
 X_{>\ell}Lx=LX_{>\ell}x\quad(x\in\mathcal D).
$$
这特别适用于 `J_F`，且用 `J_F²=I` 得 `J_F D=D`。
各 `Acal` 元素由 R125 的完整交换子域定理保持 `D`，与 `X` 交换；
又与有限头的 `Acal` 和交换，故也与 `X_(>ell)` 完整交换。

`E_F` 的具体构造是有限个
`J_FV_kJ_F−V(s_kN_k)` 的线性组合，再加 `J_FYJ_F−widehat Y_F`。
所以每个 `E_F` 确实保持 `D`，并与同一个 `X_(>ell)` 完整域交换。
这不是仅从交换有界生成元推断闭算子域。

于是
$$
 \operatorname{ad}_T^s(E_F)
 =\operatorname{ad}_{D_\ell^{\rm bd}}^s(E_F),\qquad
 \|\operatorname{ad}_T^s(E_F)\|\le d_r^s\|E_F\|,
\tag{4.2}
$$
$$
 d_r=2\|D_\ell^{\rm bd}\|
 \le12(1+\log(m+q))+2\|Y\|=O(r^2).
\tag{4.3}
$$
全部右侧交换子都保持 `D`，因为它们由保持 `D` 并与闭尾 first 交换的
有界算子相乘相减组成。

对 `f∈M`，`v=J_Ff∈D`，且
`Tv=−(A_F+E_F)v`。
定义有界域算子多项式
$$
 Q_0=I,\qquad
 Q_{n+1}=\operatorname{ad}_T(Q_n)-Q_n(A_F+E_F).
$$
逐步应用此式同时证明
`v∈Dom T^n` 和 `T^nv=Q_nv`。
如固定多位反射附录的自含权计数：给 `A_F` 权 1，
给 `ad_T^sE_F` 权 `s+1`，则 `Q_n` 的系数绝对值总和至多 `(n+1)!`，
唯一不含误差的项是 `(−A_F)^n`。
因此，充分大 `r` 时，
$$
 \boxed{
 \|T^rJ_Ff-(-A_F)^rJ_Ff\|
 \le(r+1)!C_E\bar\eta_{m-1}
 (1+\|A_F\|+d_r)^r\|f\|.
 }
\tag{4.4}
$$
该式及全部自然域统一于此窗口内的所有 `r` 元集 `F`。

## 5. 对称求和后的所有误差仍趋零

记绝对系数预算
$$
 S_r=\frac1{(2q)^r}
 \sum_{\substack{F\subset I_r\\|F|=r}}|p_F|^{-1}
 \le\frac{(m+q)^r}{2^rr!}.
\tag{5.1}
$$
令 `R_r=1+5r/(m+1)+d_r=O(r²)`。

### 5.1 非交换误差

把 (4.4) 逐项相加，误差至多
$$
 (r+1)C_E\bar\eta_{m-1}
 \left(\frac{(m+q)R_r}{2}\right)^r\|f\|
 \longrightarrow0.
\tag{5.2}
$$
其正的对数成本为 `O(r³+r log r)`，
而负项为 `−770·16^(m−1)`，`m=ceil exp(r²)`。
这里已支付求和项数及输入分母。

### 5.2 Bell 替换误差

不能只将 `A_F−P_F=O(r/m²)` 粗乘输入成本。
(3.8)—(3.9) 给
$$
 \|A_F^r-P_F^r\|
 \le\frac{C_Ar^2}{(m+1)^2}
       \left(\frac{5r}{m+1}\right)^{r-1}.
$$
乘 (5.1) 后，完整误差至多
$$
 \frac{C_Ar}{5(m+1)}
 \frac{(5r/2)^r}{r!}
 \left(\frac{m+q}{m+1}\right)^r
 \le
 \frac{C_Ar}{5(m+1)}
 \left(\frac{5e}{2}\right)^r e^{rq/m}
 \longrightarrow0.
\tag{5.3}
$$
`m=ceil exp(r²)` 吸收这里的指数因子，且 `rq/m=r⁵/m→0`。

### 5.3 实际重复位与纯主项

展开 `P_F^r`。全部指标不同的项恰为
$$
 4^r r!p_F\prod_{j\in F}N_j.
$$
其它项含某个 `N_j²=η_jN_(j+1)`，故
$$
 \left\|P_F^r-4^rr!p_F\prod_{j\in F}N_j\right\|
 \le4^r\bar\eta_m\left(\frac r{m+1}\right)^r.
$$
经 (5.1) 求和后的误差至多
$$
 \bar\eta_m(2e)^r e^{rq/m}\longrightarrow0.
\tag{5.4}
$$

物理位上 `E_jJ_j=E_j`，所以
$$
 \left\|\left(\prod_{j\in F}N_j\right)J_F
             -\prod_{j\in F}E_j\right\|
 \le r\bar\eta_m.
$$
主项的全部系数绝对值总和为
`(2/q)^r r! binom(q,r)≤2^r`；
这最后一次替换的误差不超过
$$
 2^r r\bar\eta_m\longrightarrow0.
\tag{5.5}
$$

令
$$
 C_{m,q}=\frac2q\sum_{j=m}^{m+q-1}E_j.
\tag{5.6}
$$
不同 `E_j` 交换且平方为零，故
$$
 C_{m,q}^r=(2/q)^r r!
  \sum_{\substack{F\subset I_r\\|F|=r}}\prod_{j\in F}E_j.
$$
(5.2)—(5.5) 以及 (2.2) 的符号给
$$
 \boxed{
 \|T^r\mathcal B_rf-C_{m,q}^rf\|\le\epsilon_r\|f\|,
 \qquad \epsilon_r\to0,\quad f\in M.
 }
\tag{5.7}
$$
每一项都使用实际 `T^r` 的自然域，不是形式矩阵幂。

## 6. 主项在全 Haar 空间强趋恒等

R23 的有限提升矩阵估计给
$$
 \|C_{m,q}\|\le1+1/q.
\tag{6.1}
$$
可直接核验：在 `q` 位计算基的 `s` 孔层上，
`sum E_j` 的范数平方至多 `(s+1)(q−s)≤(q+1)²/4`；
各层的像正交。

若 `v` 是只用低于第 `m` 位的有限柱向量，则
`2E_jv=(I−chi_j)v`。独立 Walsh 位给
$$
 \|(C_{m,q}-I)v\|=q^{-1/2}\|v\|.
$$
因此
$$
 \|(C_{m,q}^r-I)v\|
 \le\frac r{\sqrt q}(1+1/q)^{r-1}\|v\|
 \longrightarrow0
\tag{6.2}
$$
因为 `q=r⁴`。
同时
$$
 \|C_{m,q}^r\|\le e^{r/q}\le e.
\tag{6.3}
$$
有限柱稠密，故 `C_(m_r,q_r)^r→I` 强收敛于整个原 Haar 空间。
结合 (5.7)，得到 (1.4)，并且
$$
 \sup_{r\text{ sufficiently large}}\|T^r\mathcal B_r|_M\|<\infty.
\tag{6.4}
$$
这一步没有要求未知 `f∈M` 有任何指定尾速率。
正是对称平均消除了单个 `2^r E_F` 的范数爆炸。

## 7. 每个固定局部矩阵的真实四次交换子

固定有限局部矩阵 `D`，设其支撑位均小于 `h`。
定义
$$
 B_{\ge h}=\sum_{j\ge h}a_j^2(I-V_j^2),\qquad
 Y_{\ge h}=\phi(B_{\ge h}),
$$
$$
 Z_h=X_{\ge h}-Y_{\ge h}
       +\left(\sum_{j<h}a_j\right)I,
$$
$$
 K_h=\sum_{j<h}a_j(V_j-I)-(Y-Y_{\ge h}).
\tag{7.1}
$$
于是在同一个完整域上
$$
 T=Z_h+K_h.
\tag{7.2}
$$
`Z_h` 仅作用第 `h` 位及以后，故 `D` 保持其完整域并与它交换。
`K_h∈Acal` 有界、保持域，并与 `Z_h` 完整交换。

### 7.1 这个局部差可真正有界除以 A

有限和
$$
 \sum_{j<h}a_j(V_j-I)=A U_h^{(1)},\qquad
 U_h^{(1)}=-2\sum_{j<h}\frac{a_j}{d_j}
 A^{2^j-1}(I+N_j)^{-1}
$$
是真实有界分解。
类似地
$$
 B-B_{\ge h}=A U_h^{(2)},\qquad
 U_h^{(2)}
 =4\sum_{j<h}\frac{a_j^2}{d_j}
 A^{2^j-1}(I+N_j)^{-2}
\tag{7.3}
$$
有界且属于 `Acal`。
因为 `B,B_(≥h)` 交换、谱均为零，选取 `phi` 邻域中的固定圆周，真实逆差积分给
$$
 Y-Y_{\ge h}=(B-B_{\ge h})L_h,
$$
$$
 L_h=\frac1{2\pi i}\int_\Gamma
 \phi(z)(z-B)^{-1}(z-B_{\ge h})^{-1}\,dz
 \in\mathcal A.
\tag{7.4}
$$
这里 `h` 固定，不需要轮廓常数一致于 `h`。
因此
$$
 \boxed{K_h=A U_h,\qquad
 U_h=U_h^{(1)}-U_h^{(2)}L_h\in\mathcal A\subset B(H).}
\tag{7.5}
$$
这不是从零字符自动除以 `A`，而是两项有限低位差各自有明确有界因子。

### 7.2 完整嵌套交换子及衰减

因 `D` 与 `Z_h` 完整交换，而 `K_h` 也与 `Z_h` 完整交换，
逐次得到
$$
 \operatorname{ad}_T^rD=\operatorname{ad}_{K_h}^rD
\tag{7.6}
$$
在原完整域上成立，右侧有界且保持该域。
更明确地，令 `D_k=ad_T^kD`。每个 `D_k` 有界、保持 `D`，
且 `[T,D_k]=D_(k+1)` 在完整域成立。
归纳于 `n` 得每个 `D_k` 保持 `Dom T^n`，并有
$$
 T^nD_kx=\sum_{s=0}^n\binom nsD_{k+s}T^{n-s}x,
 \qquad x\in\operatorname{Dom}T^n.
$$
归纳步先用右端每项入 `Dom T`，再施加一次 `T`。
由此全部固定阶的通常 Leibniz 域公式可迭代，`D` 及每个嵌套交换子均保持
全部所需自然幂域。

实际权给（R109 的精确二进位式）
$$
 W_n=\|A^n\|,\qquad
 W_n\le\exp\!\left[-\frac{100}{15}n^4+105n^3\right],
 \quad n\ge0,\quad W_0=1.
\tag{7.7}
$$
`A` 与 `U_h` 交换，故 `||K_h^n||≤W_n||U_h||^n`。
展开有界交换子，
$$
 \operatorname{ad}_{K_h}^rD
 =\sum_{s=0}^r(-1)^s\binom rs K_h^{r-s}DK_h^s.
$$
使用
`s⁴+(r−s)⁴≥r⁴/8`、
`s³+(r−s)³≤r³`，得到
$$
 \|\operatorname{ad}_T^rD\|
 \le\|D\|(2\|U_h\|)^r
 \exp\!\left[-\frac56r^4+105r^3\right].
$$
这就是 (1.6)。全部指数来自原实际 `A` 的范数，不运输未知子空间。

## 8. 配对、最高交换子及排核

记实际双线性型 `mathcal B(u,v)=<u,Cv>`。
固定 `f,g∈M`，置 `u_r=mathcal B_r f∈Dom T^r`。
完整域 Leibniz 公式为
$$
 DT^ru_r
 =\sum_{k=0}^r(-1)^k\binom rk
       T^{r-k}(\operatorname{ad}_T^kD)u_r.
\tag{8.1}
$$
第 7 节已证明各项真实入域；不把仅形式交换子用于 (8.1)。

`Tg=0`，故 `g` 在全部自然幂域中。
对 `k<r`，逐次使用 `C` 自伴配对即得
$$
 \mathcal B\bigl(T^{r-k}(\operatorname{ad}_T^kD)u_r,g\bigr)=0.
$$
因此准确地
$$
 \mathcal B(DT^r\mathcal B_rf,g)
 =(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal B_rf,g).
\tag{8.2}
$$
由 (1.5)、(1.6)，右端绝对值至多
$$
 \frac{\|D\|(2\|U_h\|)^r}{r!}
 \exp\!\left[-\frac56r^4+106r^3\right]\|f\|\,\|g\|
 \longrightarrow0.
\tag{8.3}
$$
另一方面，第 6 节给 `T^r mathcal B_r f→f` 强。
所以
$$
 \boxed{\mathcal B(Df,g)=0
 \quad(f,g\in M,\ D\text{ 任意固定有限局部矩阵}).}
\tag{8.4}
$$

实际 Haar 无限张量表示中的全部有限局部矩阵不可约。
为自含说明：若正交投影 `P` 与它们全部交换，令 `Q_h` 是前 `h` 位投到
参考向量的局部投影，则 `Q_h→P_(C1)` 强。
所以 `P1=c1`，`c∈{0,1}`；局部矩阵作用于 `1` 的向量稠密，
再用交换关系便得 `P=cI`。

因而任意非零 `f` 的局部矩阵轨道线性张成稠密：
其闭包对局部矩阵及伴随都不变，故相应正交投影只能为 `I`。
若 `0≠f∈M`，在 (8.4) 中取 `g=f`，则 `Cf` 正交于这个稠密轨道，
迫 `Cf=0`，矛盾。因此 `M={0}`，完成 (1.3) 的证明链。

## 9. 危险平方的应用与未覆盖范围

取 `phi(z)=sqrt(1−z)` 及 `phi(z)=−sqrt(1−z)`，两者均满足定理假设，
故两个真实分支 `X−Y`、`X+Y` 都无核。
`Y` 是有界可逆 `Acal` 元素，与 `X` 完整交换。
R176 已付清的自然多项式与分支分解于是给
$$
 \ker(X^2+B-I)=0.
$$
该自然算子 `C` 自伴，故像稠密。
在 `a_*=0` 的规范点态接口下，R144/R176 的图循环性识别出
$$
 u=\sum_{j\ge0}\frac{(-1)^j}{j+1}\chi_j,\qquad
 \boxed{u^2-1\text{ 是实际 }A\text{ 的循环向量}.}
\tag{9.1}
$$


### 9.1 全部非零二次及更低次数多项式

事实上，对此固定规范 $u$，任意非零、次数至多二的标量多项式 $q$ 都给循环向量 $q(u)$。

若 $q(z)=c_2(z^2+\alpha z+\beta)$、$c_2\ne0$，置 $\Delta=\alpha^2/4-\beta$。当 $\Delta\ne0$ 时，在零点邻域选取平方根，令
$
\phi_\pm(z)=-\alpha/2\pm\sqrt{\Delta-z}.
$
两函数固定且全纯，故本定理排除 $X-\phi_\pm(B)$ 的核。它们与 $X$ 在完整域交换，R176 的自然多项式域给
$
X^2+\alpha X+B+\beta I
=(X-\phi_+(B))(X-\phi_-(B)),
\qquad \operatorname{Dom}=\operatorname{Dom}X^2.
$
两个因子单射遂使自然乘积单射。其完整 $C$ 自伴性及 R176 (7.8) 的图循环识别给 $q(u)$ 循环。当 $\Delta=0$ 时，$q(u)=c_2(u+\alpha/2)^2$，由 R144 已证的全部点态幂循环性得到同一结论。一次多项式同样由 R144 的一次情形，非零常数由真空向量的循环性处理。

这仍未覆盖任意高次 $q$ 的 Bell 累积量，不能以二次结论代替高次系数的分析。

本稿不擅自把 (9.1) 加上任意 first 指数权；那需要逐一核对其改变后的有界系数
是否也满足第 3 节的高位二次小量及第 7 节的局部有界除 `A` 分解。
也不把本证明升级为所有 `L²` 向量循环、所有实际有界交换子单射、
两个边界的 `N=M` 或一般正常湮灭者不存在。

全部有限局部算子只在原 Haar 表示中使用；没有将边界核或奇异态搬回未知 Haar 子空间。
证明的重点是第 5—6 节的均匀对称平均预算与第 7 节的真实局部四次衰减，
不能只引用固定 `r` 的弱逼近来替代它们。
