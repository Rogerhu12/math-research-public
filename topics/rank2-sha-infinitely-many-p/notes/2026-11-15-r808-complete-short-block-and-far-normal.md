# R808 增补 — 同一修正的完整短块二支式与远支法向段

日期：2026-11-15。**状态：已证明。** 本文是
[R808](../results/R808-original-third-precision-corrector-split-branches-and-near-normal-jet.md)
的短增补，保同一个原来源及同一个首修正。新增的是整个长度 $\ell$ 的二支系数式；其中 $\lambda,B$ 是原实际轴上的单位函数，不能只取它们的常数项。

以下精确限于
$$
p=6s-1>101,\qquad f_D<p,\qquad k_{\rm carry}=0,\qquad
s=2h+r,\qquad 1\le\ell\le r<h,\qquad \ell<s-13.
\tag{1}
$$
不把新短块延长到首个 $p$ 共振，也不据此判断原全余像的指定类非零。

## 1. 同一来源、精度和有限轴函数

仍取 R808 的原格
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^n q_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad \mathcal E=Y\partial_Y,
$$
并保全部十九角与原次数帽。合法整提升为
$$
P^{\rm fact}=t^r\widetilde F^3\widetilde q\in\mathcal W_D,
\qquad
F(0,1)=0,\quad
(\mathcal EF)(0,1)q(0,1)\ne0.
\tag{2}
$$
$F$ 不可约，实际接触阶为 $h$。假设同一 $R$ 满足
$$
J(P^{\rm fact}+pR)\in p^2\Gamma_{2s+\ell}.
\tag{3}
$$
这可由原真正第三精度
$$
M^{\rm orig}(P^{\rm fact}+pR+p^2T)\in p^3,
\qquad
M^{\rm orig}=c_*U_0m_{13}J
\tag{4}
$$
推出，理由正是 R808 的完整行权引理：
$J_A$ 读第三精度、两条十三行 $J_B$ 读第二精度。
仅原第一次 $M\in p^2$ 不足以替代 (3)。

沿原 regularized 有限轴写
$$
\widetilde F(t(w),g(w))=w^h u(w)+p\xi(w),\qquad
e(w)=(\mathcal E\widetilde F)(t(w),g(w)),
$$
$$
C(w)=\left(\frac{t(w)}w\right)^r
       \widetilde q(t(w),g(w)),\qquad
t(w)=-w+O(w^2).
\tag{5}
$$
以下取同一个约化，并置
$$
\boxed{\lambda(w)=\frac{u(w)}{e(w)},\qquad
B(w)=\frac{C(w)e(w)u(w)^2}{a}\in k[[w]]^\times.}
\tag{6}
$$
$a$ 为原 Gaussian 单位。所用的 $u$ 只需到 $\max(r,\ell)-1$；
相应 $F(t,g)$ 只读到 $h+r-1<s$。故 (6) 只使用原整窗口，
不把未正规轴作无限约化，也不把 $q$ 投影成标量。
$\lambda,B$ 的任何形式延长给相同的下列有限结论。

令 $F(t,\psi(t))=0,\ \psi(0)=1$ 为原光滑支，简写
$$
R_C=R(t(w),\psi(t(w))),\qquad
R_i^g=(\mathcal E^iR)(t(w),\bar g(w)).
$$
全文的 $R$ 都是 (3) 中同一个修正的约化。

## 2. 全第三短块与沿 C 的三个完整段

**定理 1。** 在 (1)–(6) 下，
$$
\boxed{
\begin{aligned}
R_C&=-2B\lambda^2w^{2h}\pmod{w^{2h+\ell}},\\
(\mathcal ER)_C&=5B\lambda w^h\pmod{w^{h+\ell}},\\
(\mathcal E^2R)_C&=-6B\pmod{w^\ell}.
\end{aligned}}
\tag{7}
$$
这里每个右端都用同一轴函数 (6)，不是仅一个单位首项。

**证明。** 原三个实际块先给
$$
R_0^g=0\pmod{w^s},
$$
$$
R_1^g=-6w^{h+r}Cue\,\xi-a^{-1}w^hCu^3
                                      \pmod{w^s}.
\tag{8}
$$
完整第三块在这里还给
$$
R_2^g=-6w^rC\xi e^2-6a^{-1}Cu^2e
                                      \pmod{w^\ell}.
\tag{9}
$$
确切地，基准的 native 首商是
$3a^2w^rC\xi e^2$，第一次真实 carry 是 $3aCu^2e$；
修正项是 $(a^2/2)R_2^g$。其余含 $\mathcal E q$、
$\mathcal E^2F$ 或更多 $F$ 的项至少从 $w^h$ 或 $w^{h+r}$ 起。
普通二次 carry 在先作完整原乘法后除一次 $p$，仍含 $p$。
因此 (9) 在整个 $<\ell$ 段成立。由 $\ell\le r<h$，
(8) 的 native 项在 $<h+\ell$ 内消失，
(9) 的 native 项在 $<\ell$ 内消失；这正是所需范围。

可全程使用代数局部坐标，毋需无限对数。设
$$
v_g=\bar g/\psi-1.
$$
由 $F(\bar g)=w^hu$ 和 $e=(\mathcal EF)(\bar g)$ 为单位，
有限 Taylor 反解给
$$
v_g=w^h\lambda+O(w^{2h}).
\tag{10}
$$
对 $R$ 在原轴与真支间展开，保二阶项，可写成
$$
(\mathcal ER)_C
=R_1^g-w^h\lambda R_2^g+O(w^{2h}),
\tag{11}
$$
$$
R_C
=R_0^g-w^h\lambda R_1^g
+\frac{w^{2h}\lambda^2}{2}(R_2^g+R_1^g)
+O(w^{3h}).
\tag{12}
$$
式 (12) 采用从 $\bar g$ 到 $\psi$ 的代数坐标反向展开；
其中额外 $R_1^g$ 项与其符号都不影响所读窗口，
因为 $R_1^g$ 至少有 $h$ 阶。
(10) 的 $O(w^{2h})$ 误差乘 $R_1^g$ 也从 $3h$ 起。
由于 $\ell<h$，有
$h+\ell<2h,\ 2h+\ell<3h$；
由于 $\ell\le r$，又有 $2h+\ell\le s$。
因此所有显示余项都在相应最后已读行之后。

将 (8)–(9) 代入 (11)：
native 两项在更长的可读范围相消，而在本窗口中各自已足够深，
剩余系数为 $-1+6=5$。这给第二式。
再代入 (12)，剩余系数为 $1-3=-2$，给第一式。
最后 $(\mathcal E^2R)_C-R_2^g\in w^h$，
由 $h>\ell$ 得第三式。全部系数按 (6) 同时改写，得 (7)。证毕。

若不愿使用 (12) 的反向二阶式，也可从
$$
R_0^g=R_C+(\mathcal ER)_Cv_g
+\tfrac12(\mathcal E^2R-\mathcal ER)_Cv_g^2+O(w^{3h})
$$
出发，先代入已得第二、第三式。
同样得到 $-5+3=-2$，且不需要读任何截断外行。

## 3. 完整短块的二支 Hensel 形式

**定理 2。** 在同一个代数局部坐标中，有
$$
\boxed{
w^{-2h}R\bigl(t(w),\psi(t(w))(1+w^hz)\bigr)
\equiv
-3B(w)\bigl(z-\lambda(w)\bigr)
       \bigl(z-\tfrac23\lambda(w)\bigr)
\pmod{w^\ell}.
}
\tag{13}
$$
左端是整的 $w$ 级数，其系数为 $z$ 的多项式。
两支均为原 $k[[w]]$ 上的单位 Hensel 分支，而且
$$
\boxed{
\begin{aligned}
\psi_R^+/\psi-1
   &=w^h\lambda(w)\pmod{w^{h+\ell}},\\
\psi_R^-/\psi-1
   &=\tfrac23w^h\lambda(w)\pmod{w^{h+\ell}}.
\end{aligned}}
\tag{14}
$$

**证明。** 精确代数展开为
$$
R(t,\psi(1+v))
=R_C+(\mathcal ER)_Cv+
\tfrac12(\mathcal E^2R-\mathcal ER)_Cv^2+\cdots.
$$
代 $v=w^hz$，除 $w^{2h}$，再用 (7)。
二次系数中的 $-\mathcal ER$ 有 $h$ 阶，
三次及更高项在除法后至少有 $h$ 阶；
因 $\ell<h$，它们在所读短块中消失。
所得三项准确是
$-2B\lambda^2+5B\lambda z-3Bz^2$，即 (13)。

两个显示根之差为 $\lambda/3$，是单位，
而二次式在两根上的导数分别为 $-B\lambda$ 和 $+B\lambda$。
所以原 R808 的两个 Hensel 根模 $w^\ell$ 分别等于
$\lambda(w)$ 和 $2\lambda(w)/3$。
R808 已由 $R(0,Y)=-3B(0)(Y-1)^2$ 证明这恰为全部局部支；
没有新增根或常数域扩张。证毕。

(10)、(14) 特别给出远支的真实插值式
$$
\boxed{
\psi_R^-\equiv\frac{\psi+2\bar g}{3}
             \pmod{w^{h+\ell}}.
}
\tag{15}
$$
也可写成
$$
\psi_R^-\equiv\psi^{1/3}\bar g^{2/3}
             \pmod{w^{h+\ell}},
\tag{16}
$$
其中选常数项为一的单位三次根；$3$ 为单位，故该根唯一。
(15) 与 (16) 的差从 $w^{2h}$ 起。
这只是同一个有限分支等式，不给远支或 $\psi$ 任何新算术中央零。

## 4. 两个实际 normal 段及精度边界

同一源的两支法向段为
$$
\boxed{
(\mathcal ER)(t(w),\psi_R^-)
\equiv+a^{-1}w^h C(w)u(w)^3
                  \pmod{w^{h+\ell}},
}
\tag{17}
$$
$$
\boxed{
(\mathcal ER)(t(w),\psi_R^+)
\equiv-a^{-1}w^h C(w)u(w)^3
                  \pmod{w^{h+r}}.
}
\tag{18}
$$
(17) 是把 (14) 代入
$(\mathcal ER)_C+v(\mathcal E^2R)_C+O(w^{2h})$：
系数为 $5-4=1$。
近支在较短 $h+\ell$ 段给 $5-6=-1$；
较长 (18) 直接由 R808 原已付的
$$
\bar g-\psi_R^+\in w^{h+r}
$$
及完整 (8) 得到。两个窗口不混同。

尤其，(13) 的 $2h$ 缩放不将近支逼近提高到 $2h$。
由 $R(\bar g)\in w^s$ 解近支时，
另一个因子的阶恰为 $h$，故保证的精度为
$$
s-h=h+r,
$$
不是 $s$。在 $h+r$ 及以后，(8) 的 native $\xi$ 必须恢复；
$\ell>r$ 时，(9) 的 native 段也不能删除。
任何通过微分、除 $\mathcal EF$ 或 Cartier 算子继续比较的论证，
仍须保这些误差、实际极点和原来源返回成本。

原 $P_{134}/U_0$、两条完整十三行、同一个 $R$ 的其它所有块，
以及下一位同一 $p^2T$ 继续按 (3)–(4) 处理。
本文没有证明原指定余类零或非零，
也没有由远支插值、局部二支或全局交数声称主目标完成。
