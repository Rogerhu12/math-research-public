# 用辅助幅度选共同圆：任意复 ℓ² 主行、指数偏离及间隙平台

日期：2026-11-13（UTC）。作者：central_review。
状态：完整证明的充分准则，供主会话独立核验。
本稿继续首个偏离晚于首个主系数的二次分支；
不把新的指数／平台范围等同于规则慢幂的纯高阶偏离。

## 1. 设置与一般实际预解准则

取任意
$$
a,b\in\ell^2(\mathbb C),\qquad a_*,b_*\in\mathbb C,
$$
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j.
$$
另取有无限非零支撑的
$$
c\in\ell^1(\mathbb C).
$$
不要求主、辅助的相位、排序或大小逐位关联。
令 $\delta_N=c_N^*>0$ 为全部非零辅助幅度的非增重排，并置
$$
L_N=1+\log^+\delta_N^{-1},\qquad g=\|a\|_2,
$$
$$
\varepsilon=\frac1{128(1+g^2)},\qquad
\varrho_N=\varepsilon N\delta_N^2.
\tag{1.1}
$$
因为 $c\in\ell^1$，有 $N\delta_N\to0$，
故 $\varrho_N\to0$。

使用原实际倾斜算子
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad X=X_b,
$$
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2,\qquad
T=X^2+Y-B.
\tag{1.2}
$$
$Y,B\in\mathcal A$ 按范数绝对收敛，字符均为零；
$T$ 取准确自然域 $\operatorname{Dom}X^2$。
定义实际缩放预解预算
$$
\Gamma_Y(r)
=
\sup_{|z|=r}
\log^+\|z(z-Y)^{-1}\|.
\tag{1.3}
$$
$Y$ 拟幂零，所以 (1.3) 对每个 $r>0$ 均有定义。

**定理 1。** 若沿某个无穷整数子序列 $N$，
$$
\boxed{
L_N=O(N^{3/2}),\qquad
\Gamma_Y(\varrho_N)=O(N^2),
}
\tag{1.4}
$$
则
$$
\boxed{
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)
\right]e^w
\text{ 非零且对原 }A\text{ 循环}.
}
\tag{1.5}
$$

半径 (1.1) 由辅助排序选出。
它与此前按主幅度和固定 $\kappa$ 比较选出的
$\rho_N^{2\kappa-2}$ 半径不同；
因此 (1.4) 是另一条充分条件，不能在两种半径间无证互换。

## 2. 真实核、B 的四次预算与双删除选位

R176 给 $T$ 闭且完整 $C$ 自伴，
$\xi=e^w$ 循环并属于全部自然幂域，
而且
$$
T\xi=
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)
\right]\xi.
\tag{2.1}
$$
$\mathbb C[A]\xi$ 是 $T$ 的图核心。
若全部 $a_j=0$，直接取 $X=a_*I$，这些域结论在 $H$ 上直接成立，
不依赖 R176 开头的非零主行假设。

反设 $M=\ker T\ne0$。
由原最大图，
$$
M\subset\mathcal D_\infty(X),\qquad
X_M=X|_M\in B(M),\qquad
X_M^2=(B-Y)|_M.
\tag{2.2}
$$
$B-Y$ 拟幂零，限制不放大幂范数，因此
$$
\boxed{\sigma(X_M)=\{0\}.}
\tag{2.3}
$$

若 $a\ne0$，R270B 的真实局部二阶 carry 消去给 $B\in\mathcal G$，
且其首阶为 $2^{j_a+1}>0$。
R151 的精确四次型给某些 $K,d>0$，
$$
\|B^n\|\le K e^{-dn^4}.
$$
因此 Neumann 级数与实数最大值优化给
$$
\boxed{
\Gamma_B(r)\le C\bigl(1+\log^+r^{-1}\bigr)^{4/3}.
}
\tag{2.4}
$$
若 $a=0$，$B=0$，取 $\Gamma_B=0$ 即可。
本步不把整个 $B$ 有界除以 $A^2$。

从辅助幅度最大的 $N$ 个真实物理位中，
删去完整主行幅度最大的 $\lfloor N/4\rfloor$ 个非零位，
再删去物理位小于
$$
m_N=\lfloor N/4\rfloor
$$
的项。
主行不足指定数量时删其全部非零位。
剩余至少 $\lfloor N/2\rfloor$ 项，固定取
$$
I_N,\qquad Q_N=|I_N|=\lfloor N/2\rfloor.
$$
准确有
$$
\boxed{
\min I_N\ge m_N,\quad
|c_j|\ge\delta_N,\quad
|a_j|\le 2g/\sqrt N\quad(j\in I_N).
}
\tag{2.5}
$$
两个幅度排序可以完全不同，双删除仍成立。

固定小参数 $\theta>0$，令
$$
r=r_N=\lceil\sqrt{N/\theta}\rceil.
$$
对全部 $r$ 元 $F\subset I_N$，
$$
\sum_F|a_j|\le2gr/\sqrt N=O_\theta(1),\qquad
\sum_F|a_j|^2=O_\theta(N^{-1/2}),
\tag{2.6}
$$
以及
$$
\sum_F|c_j|
\le\sum_{j\ge m_N}|c_j|\longrightarrow0.
\tag{2.7}
$$
这里只要求 (2.7) 有界，不要求它的收敛速度。

## 3. 一次真实联合求值，而非逐因子重复预解成本

对 $j\in I_N$ 定义
$$
s_j=2a_j/c_j,\qquad
L_j=8a_jX_M+4c_jI_M
=4c_j(I_M+s_jX_M).
\tag{3.1}
$$
$c_j\ne0$，但允许 $a_j=0$；
此时 $s_j=0$，后面的逆自然成为标量逆。
由 (2.5)，
$$
|s_j|\le\frac{4g}{\sqrt N\,\delta_N}.
\tag{3.2}
$$
在共同双圆盘
$$
|z_B|,|z_Y|\le\varrho_N
$$
中，
$$
|s_j^2(z_B-z_Y)|
\le32g^2\varepsilon\le\frac14.
\tag{3.3}
$$

对一个固定 $F$，置
$$
h_F(z_B,z_Y)
=
\prod_{j\in F}
[1-s_j^2(z_B-z_Y)]^{-1}.
\tag{3.4}
$$
它在共同双圆盘邻域全纯，
$$
|h_F(z_B,z_Y)|\le(4/3)^r.
$$
用同一个二重 Cauchy 积分求实际联合函数：
$$
h_F(B,Y)
=
\frac1{(2\pi i)^2}
\int_{|z_B|=\varrho_N}\int_{|z_Y|=\varrho_N}
h_F(z_B,z_Y)(z_B-B)^{-1}(z_Y-Y)^{-1}
\,dz_Y\,dz_B.
\tag{3.5}
$$
$B,Y$ 交换且谱均为 $\{0\}$，所以这是真正的有界联合演算。
它属于 $\mathcal A$，保持 $M$，并满足
$$
\boxed{
\|h_F(B,Y)\|
\le(4/3)^r
\exp\{\Gamma_B(\varrho_N)+\Gamma_Y(\varrho_N)\}.
}
\tag{3.6}
$$
这里只有一次 $B$ 预解和一次 $Y$ 预解成本；
没有给每个 $j$ 重复支付同一个共同圆成本。

定义核内算子
$$
\boxed{
\mathfrak R_F
=
\left(\prod_{j\in F}(4c_j)^{-1}\right)
\left(\prod_{j\in F}(I_M-s_jX_M)\right)
h_F(B,Y)|_M.
}
\tag{3.7}
$$
由真实平方关系 (2.2)，
$$
(I_M+s_jX_M)(I_M-s_jX_M)
=I_M-s_j^2(B-Y)|_M.
$$
因全部因子交换，(3.4)–(3.7) 给
$$
\boxed{\left(\prod_{j\in F}L_j\right)\mathfrak R_F=I_M.}
\tag{3.8}
$$
这是同一个未知核上的有界逆公式；
没有在全空间对闭 $X$ 取预解式。

由 (3.2)、(3.6)，
$$
\begin{aligned}
\log^+\|\mathfrak R_F\|
&\le
\Gamma_B(\varrho_N)+\Gamma_Y(\varrho_N)
+2rL_N+C_Mr+C.
\end{aligned}
\tag{3.9}
$$
其中 $C_M$ 固定，可以依赖 $\|X_M\|$；
它只付 $r$ 次几何成本。
又
$$
1+\log^+\varrho_N^{-1}\le C_\varepsilon+2L_N.
$$
结合 (1.4) 与 (2.4)，
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K_0N^2+2rL_N+C_Mr+C.
}
\tag{3.10}
$$

## 4. 实际高位反射、自然深域与一次系数

本节使用已经完整证明的任意跨度提升计算；
其输入只需 (2.6)–(2.7) 与 (3.8)–(3.10)。
为明确这些输入没有隐藏主、辅助比例条件，写出所需实际式。

令
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad \gamma_F=\operatorname{Ad}J_F.
$$
只在 $F$ 中把参数 $t_jN_j$ 改成 $-t_jN_j$，
定义带帽的 $X,Y,B$。
R260 的真实最高物理位壳估计，
对全部需要的自然域导数给
$$
\|\delta_X^s(\gamma_FX-\widehat X)\|
+\|\delta_X^s(\gamma_FY-\widehat Y)\|
+\|\delta_X^s(\gamma_FB-\widehat B)\|
\le s!\epsilon_N,
$$
$$
\epsilon_N\le C e^{-385\,16^{m_N-1}}.
\tag{4.1}
$$
它只用 $a\in\ell^2$、$a^2,c\in\ell^1$。
385 是实际 carry 的粗上界常数；
没有把它写成真实 carry 的等式。

$J_F$ 双向保持 $\mathcal D_\infty(X)$。
若 $f_F=\mathfrak R_Ff\in M$，
则 $\|X^kf_F\|\le\|X_M\|^k\|f_F\|$。
由 (2.6)–(2.7)，带帽有限增量的系数绝对和一致有界。
结合 (4.1) 的有限词正规排序，得到固定 $R_{M,\theta}$，使
$$
\|X^kJ_F f_F\|
\le2R_{M,\theta}^k\|f_F\|
\qquad(0\le k\le4r).
\tag{4.2}
$$
全部误差词的代价不超过
$\epsilon_N e^{C_\theta r\log(r+2)}$。
这些是所用真实输入向量上的自然域估计。

准确的 $B$ 符号差为
$$
\widehat B-B
=
\sum_{j\in F}
16a_j^2(t_jN_j)^3(I-t_j^2N_j^2)^{-2}.
\tag{4.3}
$$
它从三次开始。
以真实
$$
N_j^3=\eta_j N_jN_{j+1},\qquad
\eta_j=d_{j+1}/d_j^2\le e^{-38516^j}
$$
支付余项后，主项在 $M$ 上为
$$
\widetilde A_F
=
8X\sum_Fa_jt_jN_j
+
16\left(\sum_Fa_jt_jN_j\right)^2
+
4\sum_Fc_jt_jN_j.
\tag{4.4}
$$
其一次系数恰为 $t_jL_j$。
所以
$$
\widetilde A_F^r
\equiv r!t_FN_F\prod_{j\in F}L_j
\pmod{(N_j^2:j\in F)}.
\tag{4.5}
$$
任何含二次主项的 $r$ 因子词，
在只有 $r$ 个不同位的平方零部分中总次数大于 $r$，
因此不贡献 (4.5)；
实际重复位由原 carry 支付。

顺序必须保持为
$$
T^rJ_F\mathfrak R_Ff
=
J_F(\gamma_FT)^r\mathfrak R_Ff.
\tag{4.6}
$$
先在 $M$ 内用 (3.8) 取消乘积，
再在最左边作用 $J_F$。
不假定 $J_FM\subset M$，不把核内逆移到反射左侧。

## 5. 同一有界弱平均支付全部成本

定义
$$
\mathcal V_N
=
(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F.
\tag{5.1}
$$
其像在 $\mathcal D_\infty(X)$。
组合数给
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=\frac{(2L_b)^r}{r!}\sup_F\|\mathfrak R_F\|,
\quad L_b=\max(1,\sup_j|t_j|^{-1}).
$$
因此
$$
\log^+A_N\le K_0N^2+2rL_N+C_M'r+C.
\tag{5.2}
$$

由 (4.1)–(4.6) 的实际提升计算，
$$
\left\|
T^r\mathcal V_N f-
C_{I_N}^rf
\right\|
\le
\left[
\epsilon_N e^{C_\theta r\log(r+2)}A_N
+2^r r\eta_{m_N}
\right]\|f\|\longrightarrow0,
\tag{5.3}
$$
其中
$$
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j
$$
为对应纯位算子。
它满足
$$
\|C_{I_N}^r\|\le(1+1/Q_N)^r.
$$
在两个固定有限柱之间，矩阵元是
$(Q_N)_r/Q_N^r$ 乘原内积。
由于 $Q_N\sim N/2$、$r\sim\sqrt{N/\theta}$，
$$
(Q_N)_r/Q_N^r\longrightarrow e^{-1/\theta}.
$$
一致范数界和 (5.3) 遂给
$$
\boxed{T^r\mathcal V_N f\rightharpoonup e^{-1/\theta}f.}
\tag{5.4}
$$
这里使用固定非零弱极限；
没有将 $r\gg\sqrt N$ 的高提升弱零改称近单位。

固定任意物理有限头的局部全矩阵 $D$。
原统一准则与固定盘稿的有限头解析因子证明，
在 (4.2) 所给真实 jets 上有
$$
\boxed{
\|(\operatorname{ad}_T^r D)\mathcal V_Nf\|
\le
2\|D\|A_N C_{D,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
}
\tag{5.5}
$$
每次局部交换提取一个真实 $A$ 因子，
其余有限词由 (4.2) 支付。
不把整个慢 $Y$ 除以 $A$，
也不宣称该交换子在全 $H$ 上有界。

若 $L_N\le C_L N^{3/2}$，则
$$
\limsup\frac{\log^+A_N}{r^4}
\le K_0\theta^2+2C_L\theta^{3/2}.
$$
先固定足够小的 $\theta$，使右边小于 $1/4$。
这个选择与局部测试 $D$ 无关。
(5.5) 便趋零；实际 carry 的双指数小量也支付 (5.3)。

对 $f,g\in M$，完整深域 Leibniz 与原 $C$ 配对给
$$
\mathcal B(DT^r\mathcal V_Nf,g)
=
(-1)^r\mathcal B((\operatorname{ad}_T^r D)\mathcal V_Nf,g).
$$
由 (5.4)–(5.5)，
$$
\mathcal B(Df,g)=0
$$
对全部局部全矩阵成立。
其不可约性迫 $M=0$。
完整 $C$ 自伴性给稠密像，
(2.1) 及真实循环图核心给 (1.5)。
定理 1 得证。

## 6. 辅助的伸缩指数尾：主行完全任意

**推论 2。** 假设某个 $0<\alpha\le1$ 满足
$$
c_n^*\le C e^{-\beta_- n^\alpha}\quad(n\ge1),
\tag{6.1}
$$
且沿无穷子序列 $N$，
$$
\delta_N\ge c_* e^{-\beta_+N^\alpha},
\qquad c_*,\beta_-,\beta_+>0.
\tag{6.2}
$$
则对任意复 $a,b\in\ell^2$，(1.5) 成立。

证明使用原函数正锥上的实际主控。
置
$$
L=\max(1,\sup_j|t_j|),\qquad
W(z)=\frac{2Lz}{1-Lz},\qquad
M_c=\sum_j|c_j|W(N_j).
$$
所有标量 Taylor 系数非负，
$$
|Y^nf|\le M_c^n|f|.
$$
原实际平方关系及物理有限头支付给
$$
\boxed{
\log\|e^{zM_c}\|
\le C+C(1+\log(2+|z|))^{4/3}
+\sum_n\log(1+C|z|c_n^*).
}
\tag{6.3}
$$
这里低位物理头按实际 $AU_h$ 处理，
高位使用 $\eta_j\le e^{-38516^j}$；
排序只作用于最后的非负标量和。
不按幅度重排算子，也不使用 Hilbert 自伴正性。

由 (6.1)，在 $n\asymp(\log(2+|z|))^{1/\alpha}$ 处分开标量和，
得到
$$
\log\|e^{zM_c}\|
\le C(1+\log(2+|z|))^{1+1/\alpha}.
$$
对 Cauchy 系数取半径 $R=\exp(\lambda n^\alpha)$，
其中 $\lambda>0$ 固定且充分小。
$n!$ 的对数成本是 $o(n^{1+\alpha})$，于是
$$
\|Y^n\|\le K e^{-d n^{1+\alpha}}
\tag{6.4}
$$
对某些 $K,d>0$ 成立。
Neumann 级数和 Young 不等式遂给真正复圆周预算
$$
\boxed{
\Gamma_Y(r)
\le C(1+\log^+r^{-1})^{1+1/\alpha}.
}
\tag{6.5}
$$

由 (6.2)，$L_N=O(N^\alpha)$；
共同半径仍精确使用 (1.1)，故
$$
1+\log^+\varrho_N^{-1}=O(N^\alpha).
$$
所以
$$
\Gamma_Y(\varrho_N)
\le C N^{1+\alpha}\le C N^2.
$$
定理 1 适用。
$\alpha=1$ 的端点由固定小 $\theta$ 支付；
$\alpha<1$ 时辅助预解成本是 $o(N^2)$。

## 7. 辅助尾间隙与长平台

**推论 3。** 若沿无穷子序列 $N$，
$$
\boxed{
L_N=O(N),\qquad
\sum_{n>N}c_n^*=o(N\delta_N^2),
}
\tag{7.1}
$$
则对任意复 $a,b\in\ell^2$，(1.5) 成立。

证明：将 $Y$ 分为幅度最大的 $N$ 个真实物理位构成的头 $Y_H$
与其余尾 $Y_T$。
(7.1) 及固定 $b$ 的统一局部范数界给
$$
\|Y_T\|\le\varrho_N/4
$$
对充分大指定 $N$ 成立。

原正锥有限头估计对任意物理排列统一给
$$
\|e^{sY_H}\|
\le K
e^{C(1+\log(2+|s|))^{4/3}}
\prod_{j\in H}(1+C|s|\,|c_j|).
\tag{7.2}
$$
因为 $|H|=N$、$Y_H,Y_T$ 交换，
对每个 $|z|=\varrho_N$，
实际 Laplace 积分
$$
z(z-Y)^{-1}
=
\int_0^\infty e^{-t}e^{tY/z}\,dt
\tag{7.3}
$$
按算子范数收敛：
尾贡献不超过 $e^{t/4}$，
有限头由 (7.2) 给次线性的对数增长乘固定 $N$ 次多项式，
可被剩余 $e^{-3t/4}$ 积分。
因此 (7.3) 对全部复方向成立，不只是某个实半轴。

令 $\ell_r=1+\log^+r^{-1}$。
将 (7.2) 代入 (7.3)，用有限多项式矩和次指数 Young 界，得到
$$
\Gamma_Y(r)
\le C\{1+N\log(N+1)+N\ell_r+\ell_r^{4/3}\}
\quad(r=\varrho_N).
\tag{7.4}
$$
因 $\ell_{\varrho_N}=O(L_N)=O(N)$，
右侧为 $O(N^2)$。
定理 1 适用。

一个具体排序辅助是：
固定 $\nu>1$ 和整数
$$
p>\frac{2\nu-1}{\nu-1},
$$
取
$$
N_0=0,\qquad N_k=2^{p^k}\quad(k\ge1),
$$
并在 $N_{k-1}<n\le N_k$ 上令
$$
c_n^*=N_k^{-\nu}.
\tag{7.5}
$$
它非增且属于 $\ell^1$。
沿 $N=N_k$，
$$
L_N=1+\nu\log N=O(N),
$$
$$
\sum_{n>N_k}c_n^*
\le2N_{k+1}^{1-\nu},
$$
所以
$$
\frac{\sum_{n>N_k}c_n^*}{N_k(c_{N_k}^*)^2}
\le
2N_k^{\,2\nu-1-p(\nu-1)}
\longrightarrow0.
\tag{7.6}
$$
这些辅助不满足任何固定伸缩指数的全局上界，
因为在右端点 $c_{N_k}^*=N_k^{-\nu}$。
实际物理位可以任意排列；相位也可任意。

## 8. 首位遗漏的明确新例

取
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad
\frac12<\sigma<1,\qquad a_*\in\mathbb C.
\tag{8.1}
$$
该主行在 R138 的全平面连续谱类；
这里不调用同射线空谱结论。

第一类辅助取
$$
c_0=0,\qquad
c_j=e^{-\beta j^\alpha}\omega_j\quad(j\ge1),
\qquad
0<\alpha\le1,\quad \beta>0,\quad|\omega_j|=1.
\tag{8.2}
$$
于是主首位为0、偏离首位为1，
不满足首支撑有序定理。
推论 2 对任意复 $\ell^2$ 指数权仍给 (1.5)。

第二类可在 $j\ge1$ 依次放置 (7.5)，并令 $c_0=0$。
例如 $\nu=2,p=4$ 时，
(7.6) 的比值不超过 $2N_k^{-1}$。
推论 3 同样给任意复指数权下的循环性。

两类均不要求 $|c_j|\asymp|a_j|^\kappa$。
在 (8.2) 中 $|a_j/c_j|\to\infty$，
所以固定盘逆准则也不直接适用。

为确认这不是把旧快辅助范围重记为新结论，
在 (8.2) 中取 $\omega_j=1$、$b=0$。
令
$$
Z=\sum_{j\ge1}c_jN_j.
$$
原归一化系数界及不同位无进位等式给
$$
\|Z^n\|
\ge n!\prod_{j=1}^n c_j.
$$
因此 $\tau_4(Z)=0$。
$Z$ 的首阶为2，若 $Z\in\mathcal G$，
R151 会迫 $\tau_4(Z)=\frac{100}{15}2^4>0$，矛盾。
又
$$
Y+2Z
=
\sum_{j\ge1}\frac{2c_jN_j^2}{I+N_j}\in\mathcal G
$$
由真实局部二阶 carry 消去成立，
所以 $Y\notin\mathcal G$。
这给旧 $\mathcal G$ 系数定理以外的明确辅助，
不是只比较一个充分衰减条件是否满足。

## 9. 本共同圆方法没有处理的规则慢幂纯高阶偏离

仍取 (8.1)，但令
$$
c_0=0,\qquad
c_j=\beta|a_j|^\kappa\omega_j\quad(j\ge1),
\qquad \kappa>2.
\tag{9.1}
$$
其辅助排序是规则幂尾。
(7.1) 的尾间隙不成立，
(6.1) 的伸缩指数上界也不成立；
用辅助圆 (1.1) 的一般幂尾估计同样超过 $N^2$ 预算。
本稿没有闭合 (9.1) 的零标量位移。

这个缺口仍然需要对同一未知核的新机制，
或不同于当前有界高位弱平均的实际估计。
本稿没有以有限轨道共同核零、代数直和，
或全空间 first 的单射稠密代替该步。

**后续范围更新（两位标量消元）：** 上节描述本共同圆方法的限制。随后[二位Bézout完整定理](../results/R236-appendix-two-site-scalar-bezout-and-late-support-quadratic-cyclicity.md)已对规则两侧慢幂、充分高位纯κ比较及有限物理头任意例外，证明全部标量位移的二次目标循环；(9.1)不再作为整个课题的开放类。极不规则双池仍须保留。

## 10. 依赖

- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  真实自然域、完整 $C$ 自伴、核内有界 first 与图循环。
- [R151](../results/R151-quartic-analytic-approximation-gauge-stability.md)、
  [R270B](../results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)：
  $B$ 的真实快类及四次幂预算。
- [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意物理跨度的实际进位壳、完整导数与有限词排序。
- [近共振统一准则](../results/R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)：
  原高位弱平均、局部四次交换子和完整双线性配对。
- [固定盘核内逆](../results/R236-appendix-fixed-disk-kernel-inverses-and-sparse-linear-deviations.md)：
  主、辅助不同排序的双删除，以及只依赖
  $a\in\ell^2,c\in\ell^1$ 的同一真实 jets 传递。
- [实际尾间隙源稿](2026-11-13-tail-gap-resolvent-budget-and-nonweak-l1-plateau-near-resonance-central-review.md)：
  (6.3)、(7.2) 的正锥物理头统一支付及全部复方向 Laplace 积分。
