# R720 — 两个固定低度 CM 来源与密度一的长整窗

日期：2026-11-15。**状态：以下固定来源、坏素数计数、共同共振及原系数恢复已证明。**
本篇不假设任何固定元素的原根猜想，也不声称原中央条件已迫一个系数前缀为零。

保持 R718 的原曲线 $E:y^2=x^3+17$、$K=\mathbf Q(\omega)$，
$p=6s-1>101$、$w=z^6$、$L=(p^2-1)/6$ 及
$$
X=z^2x(z),\qquad U=(\sigma/z)e^{-cw^s},\qquad
[w^s]\log U=0.
$$
所有约化均在 $k=\mathbf F_{p^2}$，同一原 sigma 和 Gaussian 不变。

## 1. 固定的两个实际同源

取与 p 无关的
$$
\alpha_+=1+6\omega,\qquad \alpha_-=1-6\omega.
\tag{1}
$$
二者均为 $1\bmod6\mathcal O_K$，且
$$
N_+=31,\qquad N_-=43.
$$
R718 的完整归一化给
$$
\psi_\pm=\frac{\sigma(\alpha_\pm z)}{\sigma(z)^{N_\pm}}
 =\alpha_\pm F_\pm(x^3),\qquad
\deg F_+=5,\quad \deg F_-=7,
\tag{2}
$$
其中 $F_\pm$ 为首一的固定 $K$ 多项式。
它们由同一实际 $\alpha_\pm$ 核决定；对每个当前 p 均整，
因为 p 不除 $6\cdot17\cdot31\cdot43$，而核为素于 p 的挠点。
不是先读出原 sigma 的第二位，再把它们作为一个新的自由来源。

还有一个固定六倍公式，明确联系这两个多项式。
用原整数 division 函数
$$
\psi_6=\frac{\sigma(6z)}{\sigma(z)^{36}},\qquad
x([6]P)=\frac{\phi_6(P)}{\psi_6(P)^2}.
$$
sigma 加法式、$\sigma(6\omega z)=\omega\sigma(6z)$ 及
$x(6\omega z)=\omega x(6z)$ 给
$$
\begin{aligned}
\sigma((1+6\omega)z)\sigma((1-6\omega)z)
 &=\sigma(z)^2\sigma(6\omega z)^2
        (x(6\omega z)-x(z))\\
 &=\sigma(z)^{74}\{\phi_6-\omega^2x\psi_6^2\}.
\end{aligned}
$$
因此
$$
\boxed{\quad
\alpha_+\alpha_-F_+(x^3)F_-(x^3)
 =\phi_6-\omega^2x\psi_6^2 .
\quad}
\tag{3}
$$
两侧在 O 的首系数同为
$\alpha_+\alpha_-=1-36\omega^2$，无未定根单位。
(2) 的实际核分别指定两个因子；不以单纯的次数分解假设代替核条件。
所以 (2) 可由固定六倍加法和实际 $[1]\pm[6\omega]$ 构造，
总输入次数恒为五与七。

令
$$
M_\pm=(N_\pm-1)/6,\qquad
R_\pm(w)=w^{M_\pm}F_\pm(w^{-1}X(w)^3).
\tag{4}
$$
它们常数为一，在原 $n<L$ 窗内整。
R718 的准确分布式和第7节标量式成为
$$
\boxed{\quad
U(\alpha_\pm^6w)
 =U(w)^{N_\pm}R_\pm(w)e^{t_\pm w^s},\qquad
t_\pm=-[w^s]\log R_\pm.
\quad}
\tag{5}
$$
$s<p$，故第二式的约化只用单位分母。
尤其原完整 Fermat 商仍为
$$
\bar t_\pm=c_pN_\pm q_p(\alpha_\pm).
\tag{6}
$$
它已包含于实际 $R_\pm$ 的低行中，没有被假设为零。
由于这里 $N_\pm<p$，R718 一般标号的 $pN_1$ 指数项自然不存在；
这不删除任何原幂次。

## 2. 两生成元的小群只能出现在稀薄素数集合

先给所需的完整初等计数。
对固定 $1/2<\beta<2/3$，令 $X_0$ 充分大，
$$
M=X_0^\beta,\qquad Y=\lfloor\sqrt M\rfloor+1.
$$
考虑 $p\in[X_0,2X_0]$ 的惯性素数。记
$$
G_N(p)=\langle31,43\rangle\subset\mathbf F_p^\times,
\qquad
G_A(p)=\left\langle
\frac{\alpha_+}{\overline{\alpha_+}},
\frac{\alpha_-}{\overline{\alpha_-}}
\right\rangle\subset\mathbf F_{p^2}^{\,N=1}.
\tag{7}
$$
这里横线为复共轭，之后才作模 p 约化。

31、43 在 $\mathbf Q^\times$ 乘法独立。
另外两个比值也乘法独立：在
$(\alpha_+)$、$(\overline{\alpha_+})$ 两个不同的 31 上素理想处，
第一个比值的赋值分别为 $1,-1$，第二个均为零；
43 上的两个素理想反过来。
这些素理想不同，因为 31、43 在 K 分裂而不分歧。
因此比值的任何非平凡整指数乘积不等于一。

若 (7) 的任一群的阶至多 M，
$(Y+1)^2>M$ 个方框内的乘积发生碰撞。
所以存在不全为零的整数 a,b，满足 $|a|,|b|\le Y$，
使对应乘积在该 p 的剩余域等于一。

对范数群，p 因而整除非零整数
$$
B_{a,b}=31^{a_+}43^{b_+}-31^{a_-}43^{b_-},
\quad a_\pm=\max(\pm a,0),\quad b_\pm=\max(\pm b,0).
\tag{8}
$$
对反共轭群，p 上方的素理想整除非零代数整数
$$
\begin{aligned}
C_{a,b}={}&
 \alpha_+^{a_+}\overline{\alpha_+}^{a_-}
 \alpha_-^{b_+}\overline{\alpha_-}^{b_-}\\
&-\overline{\alpha_+}^{a_+}\alpha_+^{a_-}
 \overline{\alpha_-}^{b_+}\alpha_-^{b_-}.
\end{aligned}
\tag{9}
$$
故该有理 p 整除其非零整数范数。
两种式子的绝对值或范数的对数都是 $O(Y)$；
常数只依赖固定的 31、43 和 (1)。

把全部 $O(Y^2)$ 个非零指数对的 (8)、
以及 (9) 的非零整数范数的绝对值相乘。
所得正整数的对数为 $O(Y^3)$。
每个坏 p 至少贡献 $\log X_0$，于是
$$
\boxed{\quad
\#\{p\in[X_0,2X_0]:
 |G_N(p)|\le X_0^\beta
 \text{ 或 }|G_A(p)|\le X_0^\beta\}
 \ll \frac{X_0^{3\beta/2}}{\log X_0}.
\quad}
\tag{10}
$$
有限个分母或坏约化素数已经排除，(8)、(9) 没有零因子。

取 $\beta=3/5$，
例外个数至多 $O(X_0^{9/10}/\log X_0)$。
对二进区间求和，这是一组素数密度零的例外。
惯性类 $p\equiv5\bmod6$ 的素数定理给其主项阶 $X_0/\log X_0$，
故好素数在该类中相对密度一。
和任意已付的正密度惯性子族相交仍保原密度；
本论证没有改变普通分支的 ray 条件。

## 3. 共同共振的真实阶

令
$$
G(p)=\langle\bar\alpha_+,\bar\alpha_-\rangle
          \subset\mathbf F_{p^2}^{\times}.
$$
其范数像与反共轭像恰为 (7) 的两个群。
设两像的阶为 $m_N,m_A$。
由于 $m_N\mid p-1$、$m_A\mid p+1$，其最大公因数至多二。
两者又均整除 $|G(p)|$，所以
$$
|G(p)|\ge\operatorname{lcm}(m_N,m_A)\ge m_Nm_A/2.
$$
六次幂在这个循环群上的核至多六，故
$$
\boxed{\quad
|G(p)^6|\ge \frac{m_Nm_A}{12}
 >\frac{X_0^{6/5}}{12}
\quad}
\tag{11}
$$
对第2节的好 p 成立。

写 $\tau_\pm=\bar\alpha_\pm^6$。
因为 $6s=p+1$，
$$
\tau_\pm^s=N_\pm\quad\text{于 }k.
$$
因此两个原递推在次数 n 同时共振，当且仅当
$$
\tau_+^{\,n-s}=\tau_-^{\,n-s}=1
\quad\Longleftrightarrow\quad
|G(p)^6|\mid n-s .
\tag{12}
$$

给定任意固定实数 $C>0$，置 $K_p=\lfloor Cp\rfloor$。
对充分大的好 p，(11) 大于 $K_p+s$。
所以在整个 $1\le n\le K_p$ 窗内，
唯一可能的共同共振为 n=s。
若 s 不在该窗中，则没有共同共振。
这不要求 $\alpha_+$ 或 $\alpha_-$ 中某一个单独为原根。

## 4. 原整窗的唯一恢复

对上述好 p，取 p 再大到 $K_p<L$。
(5) 在 $k[w]/(w^{K_p+1})$ 中准确约化为
$$
\bar U(\tau_\pm w)
 =\bar U(w)^{N_\pm}\bar R_\pm(w)
   \sum_{j=0}^{\lfloor K_p/s\rfloor}
       \frac{\bar t_\pm^j w^{sj}}{j!}.
\tag{13}
$$
因为 $K_p<L$，出现的 j 均至多 $p-2$，全部阶乘为单位。
所有非线性交叉项与真实幂次均保留。

**定理。** 两个 (13)、常数项一和在窗口包含 s 时的原条件
$[w^s]\log V=0$，唯一决定
$$
V=\bar U\bmod w^{K_p+1}.
$$

存在性由原整 U 给出，不另添数据相容性假设。
若两个解首次不同于次数 n，
取至少一个 $\tau_\pm^n-N_\pm\ne0$ 的方程就迫该差为零。
(12) 保证 n≠s 时总能这样选；
在 n=s 时，原对数规范又迫首次差为零。
所以解唯一。

递推也完全明确。
已求 $V_{<n}=\sum_{i<n}v_iw^i$ 时，
对 n≠s 选任一个分母非零的符号 i，
$$
v_n=
\frac{[w^n]\left\{
 V_{<n}^{N_i}\bar R_i
 \sum_{j\le\lfloor K_p/s\rfloor}
       \bar t_i^j w^{sj}/j!
 \right\}}
 {\tau_i^n-N_i}.
\tag{14}
$$
若窗口包含 s，则该行使用
$$
v_s=-[w^s]\log V_{<s}.
\tag{15}
$$
(15) 同样只使用 $s<p$ 的单位分母。
(14) 是两条实际分布式的逐行择用，
不是把未选那条方程扔掉；其相容性由原解保证。

完整输入仅为固定 (2) 的五次、七次多项式，
原 $X\bmod w^{\max(K_p,s)+1}$，以及明确的有限域常数。
原 X 可由 R714 的 $xZ_1^2$ 在原整窗读取。
(5) 已决定两个完整标量，无独立的 sigma 第二位输入。
R717 因子分解可继续读取这个窗口中落入的原第二位组合，
它们受到两条固定全局同源分布的共同约束。

## 5. 精确范围与尚未完成的算术门

本篇覆盖任意固定倍数 p 的 w 窗；
等价地，可覆盖任意固定数目的原中央首块。
它没有覆盖 R708 约 $3p/4$ 个块所需的二次规模 w 窗。

同一计数还给一个直接推论：
任取固定 $0<\varepsilon<1/3$，
选择 $1/2<\beta<2/3$ 且 $2\beta>1+\varepsilon$，
便可把窗口换成 $K_p=\lfloor p^{1+\varepsilon}\rfloor$，
仍只有密度零例外和 n=s 的共同共振。
这仍是严格小于二次规模的窗口。

固定 degree 的 division 输入不等于同源 pullback 免费保持旧来源预算。
旧 $\mathcal W_D$ 的十九角、原极帽、同一个修正 R、
两十三行 carry 以及 R710 的全中央进位仍须实际支付。
用 $Z_1$ 写成有理来源时，它的所有其他零点与大极帽仍在。

(13) 约束的是原唯一 U。
它既未证明原 $j_m=0$ 迫任一长前缀全零，
也未证明第一 wild 层非零或实际 Weierstrass 次数的统一界。
固定曲线、无穷 p 的主目标仍由这些算术门控制。

依赖：
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R714](R714-original-height-two-rational-parameter-and-full-first-cartier-window.md)；
[R717](R717-original-height-two-artin-hasse-return-and-second-digit-support.md)；
[R718](R718-original-cm-distribution-and-unique-gaussian-resonance.md)；
[R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)。
