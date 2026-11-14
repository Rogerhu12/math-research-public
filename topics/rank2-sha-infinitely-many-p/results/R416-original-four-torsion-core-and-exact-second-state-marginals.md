# R416 — 原总和 core 的十六项二挠／四挠公式与第二状态的完整 Y 边际

日期：2026-11-14。**状态：已证明。** 对 R413 的同一个原三输入，完整总和 core 的第二状态满足
$$
\boxed{Y_*\widetilde\rho=-\tfrac13\nu_S,\qquad
       W_*\widetilde\rho=\nu_T.}
$$
因此两条真实 rank-two 来源的中央同时失败，确实传递给这个实际第二状态的两个完整边际；没有新添一个未经证明的中央零。证明包含整个七十二维 Heisenberg lift、十六个固定四挠平移的绝对系数、全部半周期归一，以及同一物理周期的完整测度比较。

## 1. 原来源与目标

全篇固定 R413 的 $E_b:y^2=x^3+b$，$b=17$、同一普通周期及 ray。
$$
\rho=\nu_D\otimes\nu_L\otimes\nu_C,\quad
S=DC,\quad T=DLC,\quad Y=x_1+x_3,\quad W=x_1+x_2+x_3.
\tag{1}
$$
$S,T$ 分别是原 $E_{17}$ 与实际 $E_{24}$ 的已付来源；后者的物理测度仍乘 R398 的固定常数 $-102816\sqrt[3]9$。这里不改这两个实际曲线或普通周期。

R413 给
$$
\mathcal H(z,r,u)=D(z+r+19u)L(z+r-8u)C(z-3r),\qquad
\widetilde{\mathcal H}=K_W\mathcal H,\quad K_W^2=1,
$$
及相应 $\widetilde\rho$。本篇先把同一个 $K_W=K_{72}$ 写为四挠平移，再计算 $Y$ 的完整推前。

## 2. 整个 Heisenberg 空间的绝对十六项公式

取原格的一组基 $\Omega,\omega\Omega$，暂将 $\Omega=1$。所有下式在还原物理周期后按同一缩放成立。
对 degree $N=72$ 使用原对称 lift
$$
(\mathsf T_t^{(N)}F)(z)=e^{-N\eta_t(z+t/2)}F(z+t).
\tag{2}
$$
置 $X=\mathsf T_{1/72}^{(72)}$、$Z=\mathsf T_{\omega/72}^{(72)}$。
原完整中心给
$$
X^{72}=Z^{72}=I,\qquad XZ=\zeta_{72}ZX.
\tag{3}
$$
在 Schrödinger 基 $e_j$（$j\bmod72$）中取
$Xe_j=\zeta_{72}^je_j$、$Ze_j=e_{j+1}$。

同一原 ratio 为
$$
g=91+72\omega\pmod{144}.
$$
按 (2) 而不是丢掉其中心，有
$$
\mathsf T_{g/72}=-X^{19},\qquad
\mathsf T_{g\omega/72}=-Z^{19}.
\tag{4}
$$
例如 $g/72=91/72+\omega$，完整交叉指数为 $e^{-91\pi i}=-1$；另一个由 $g\omega=-72+19\omega$ 同样给负号。

令 $De_j=e_{19j}$，$B=X^{36}Z^{36}D$。因 $19^2\equiv1\pmod{72}$，有
$$
B^2=I,\qquad BXB^{-1}=-X^{19},\qquad BZB^{-1}=-Z^{19}.
\tag{5}
$$
所以 $B$ 和真实 $K_{72}$ 只差标量。这个标量也可在同一空间内完整确定。
在标准 degree-$N$ theta 基中，六倍拉回的整个 degree-two 子空间由
$$
\sum_{r=0}^{5}e_{6j+12r},\qquad j=0,1,
\tag{6}
$$
张成；这是标准 theta 级数把整数指标按模六分组的准确恒等式。原 sigma 到该标准基的 Gaussian 在 $[6]$ 拉回下相容：degree-two 的指数乘以 $6^2$ 正是 degree72 的指数。
$B$ 将 (6) 的六个指标作置换，且 $(-1)^{6j+12r}=1$，所以在 (6) 上为恒等。

另一方面原非零来源 $\Theta(6z)$ 属于 (6)。其实际 core 为 $\lambda_0$，而 R413 统一的标量为 $\lambda=-\lambda_0$，故
$K_{72}\Theta(6z)=-\Theta(6z)$。这确定
$$
\boxed{K_{72}=-B.}
\tag{7}
$$
没有用未知的 $S'$ 或 $T'$ 来定标。

现在把 (7) 改写为实际四挠平移。记
$t_{r,s}=(s+r\omega)/4$，$0\le r,s<4$。由 (2)–(3)，
$$
\mathsf T_{t_{r,s}}^{(72)}e_j
=i^{s(j+r)}e_{j+18r}.
\tag{8}
$$
因此
$$
\frac14\sum_{r,s=0}^{3}(-1)^{rs+r+s}
                \mathsf T_{t_{r,s}}^{(72)}e_j
=(-1)^je_{19j+36}=Be_j.
$$
确实对固定 $r$ 的 $s$ 和只在 $r\equiv j+2\pmod4$ 时留下。
$(-1)^{rs+r+s}$ 在 $r,s$ 都偶时为正，其余为负。完整绝对公式是
$$
\boxed{
K_{72}
=\frac14\sum_{t\in E[4]}\mathsf T_t^{(72)}
 -\frac12\sum_{t\in E[2]}\mathsf T_t^{(72)}.
}
\tag{9}
$$
这里四挠代表的周期改变不添相位：$72/4=18$ 为偶数，原 (2) 的周期相位恰为一。因而 (9) 不依赖将这些固定代表另行平移一个格周期。

## 3. 同一原三输入的真实平移来源

总输出正交性使每个 (9) 中的平移准确因子化：
$$
\boxed{
\mathsf T_t^{(72)}\mathcal H
=D_t(z+r+19u)L_t(z+r-8u)C_t(z-3r),\qquad
F_t=\mathsf T_t^{(\deg F)}F.
}
\tag{10}
$$
指数中的另两轴项分别为 $16+38-54=0$、$16\cdot19-38\cdot8=0$，所以没有少一个平移后 Gaussian。

必须保留这些平移的正确线丛：若 $t\in E[4]\setminus E[2]$，$D_t$ 仍在原 degree16 空间，但 $L_t,C_t$ 分别有同一个二挠平坦 twist，因为 $38t=18t=2t$。它们不被单独误称为原 untwisted degree38、18 来源。在 (10) 的同一完整联合内这些 twist 已相容；R413 已证明其整体整性。

将 (10) 推到原两个输出 $(Y,x_2)$，等价于把原三个源变量置为 $(y,v,y)$。于是实际双变量来源为
$$
\boxed{
\widetilde F(y,v)
=\frac14\sum_{t\in E[4]} S_t(y)L_t(v)
 -\frac12\sum_{t\in E[2]}S_t(y)L_t(v),\qquad
S_t=\mathsf T_t^{(34)}S.
}
\tag{11}
$$
这个等式保整个双输出；没有把函数乘积当作 Mellin 乘积。

R398 的实际除子给 $L(t)=0$ 对全部 $t\in E[4]\setminus E[2]$。故设置 $v=0$ 时，它们连同自己的平坦 twist 一起确实为零，得到
$$
\boxed{
\widetilde S(y):=Y_*\widetilde\rho
\quad\text{的 Amice 来源为}\quad
-\frac14\sum_{t\in E[2]}L_t(0)S_t(y).
}
\tag{12}
$$
在 (12) 中剩下的所有 $t$ 都是原 degree34 的合法 Heisenberg 平移。

## 4. 非零二挠点的完整代数归一

写
$$
S=\sigma^{34}s(x),\qquad L=\sigma^{38}l(x),
$$
$$
s(x)=x^2(x^3+b)(x^3-8b)
       \left(x^6-\frac{4b}{7}x^3+\frac{16b^2}{7}\right),
$$
$$
l(x)=x(x^6+20bx^3-8b^2)Q_4(x^3).
\tag{13}
$$
对非零二挠点 $t$ 令 $e=x(t)$，则 $e^3=-b$、$y(t)=0$。
置
$$
c_t=e^{-\eta_t t/2}\sigma(t),\qquad
\sigma_t(z)=e^{-\eta_tz}\frac{\sigma(z+t)}{\sigma(t)}.
$$
原 sigma 加法公式和半周期准周期给
$$
\sigma_t(z)^2=(x(z)-e)\sigma(z)^2,\qquad
x(z+t)=e\frac{x(z)+2e}{x(z)-e}.
\tag{14}
$$
原对称 lift 的平方是 $\mathsf T_{2t}^{(2)}=I$。将其作用于 $\sigma^2$，由 (14) 得
$$
\boxed{c_t^4=(3e^2)^{-1}.}
\tag{15}
$$
因此没有选择一个任意平方根或四次根来给目标系数定标。
对 (13)，准确有
$$
S_t(z)=c_t^{34}(x-e)^{17}\sigma(z)^{34}
       s\left(e\frac{x+2e}{x-e}\right),\qquad
L_t(0)=c_t^{38}l(e).
\tag{16}
$$
由于
$$
l(e)=3^8 e b^6=3^8e^{19},\qquad c_t^{72}=(3e^2)^{-18},
$$
其**完整乘积**为
$$
\boxed{
L_t(0)S_t(z)
=\frac{\sigma^{34}}{3^{10}e^{17}}
 (x-e)^{17}s\left(e\frac{x+2e}{x-e}\right).
}
\tag{17}
$$
所有半周期常数在这个七十二次幂里已经确定；无需分别给 $c_t^{34}$ 或 $c_t^{38}$ 选符号。

## 5. 三个实际半周期的精确求和

令
$$
f(u)=u^2(u^3-1)(u^3+8)
           (u^6+4u^3/7+16/7),\qquad
P(u)=(u-1)^{17}f\left(\frac{u+2}{u-1}\right).
\tag{18}
$$
$P$ 是次数十六的多项式；(17) 等于
$\sigma^{34}e^{14}P(x/e)/3^{10}$。
完整展开后，可能在三根求和中留下的系数恰为
$$
\begin{array}{c|rrrrrr}
k&2&5&8&11&14&17\\ \hline
[u^k]P/3^8&-128/7&80/7&-12/7&53/7&1&0 .
\end{array}
\tag{19}
$$
这张表来自 (18) 的有限二项展开；其他列不是被忽略，而是随后被三个实际 $e^3=-b$ 根的和准确消去。

因为
$$
\sum_{e^3=-b}e^{14-k}
=\begin{cases}3(-b)^{(14-k)/3},&k\equiv2\pmod3,\\0,&\text{否则},\end{cases}
$$
(19) 和
$$
s(x)=x^{14}-\frac{53b}{7}x^{11}-\frac{12b^2}{7}x^8
                  -\frac{80b^3}{7}x^5-\frac{128b^4}{7}x^2
$$
给出整条来源恒等式
$$
\boxed{\sum_{t\in E[2]\setminus\{0\}}L_t(0)S_t(z)=\frac13 S(z).}
\tag{20}
$$
原点项是 $L(0)S=S$，故 (12) 完全化简为
$$
\boxed{\widetilde S=-\frac13S.}
\tag{21}
$$
这不是只核对一个 Taylor 系数：上面给出了所有可能留下的多项式列及其确切求和。

## 6. 完整普通测度、tame 与物理目标

(21) 在同一物理 $E_{17}$ frame 中是全函数身份。与 R413 整 Amice 构造相容，故准确给
$$
\boxed{Y_*\widetilde\rho=-\frac13\nu_S,\qquad
       W_*\widetilde\rho=\nu_T.}
\tag{22}
$$
第二式是同一个 $K_{72}T=T$，并非另一个独立选择的归一。
(22) 保全部普通单位／非单位部分、全部 tame 特征及任何连续输出测试。例如
$$
\int K_{\ell,u}(Y)\,d\widetilde\rho
=-\frac13J_{S,\ell}(u),\qquad
\int K_{\ell,u}(W)\,d\widetilde\rho
=J_{T,\ell}(u),
\tag{23}
$$
其中 $K_{\ell,u}$ 带各自真实输出的单位指示函数。
$\mu_6$ 只是在 (20) 的三个实际二挠横坐标中进行准确求和；没有预先给 (11) 的各个四挠项做独立型投影。
实际 $E_{24}$ 的周期和固定物理标量仍为 R398 的版本，故原两个中央条件正是 $J'_S(0)=J'_T(0)=0$；$-1/3$ 在所有当前素数是单位。

## 7. 两态循环给出的新合法零传播

对 $i=0,1$ 记 $\rho_0=\rho$、$\rho_1=\widetilde\rho$。于是
$$
\begin{array}{c|cc}
&Y_*&W_*\\ \hline
\rho_0&\nu_S&\nu_T\\
\rho_1&-\nu_S/3&\nu_T
\end{array}
\tag{24}
$$
并且原总和 core 在这两个状态之间准确交换。
因此若两个真实中央导数同时失败，则它们在每一次完整两态返回后的 $Y,W$ 边际也都失败。这一传播有 (22) 的全来源证明，而非由算子可逆性免费增加条件。

还可以用真正的特征状态
$$
\rho_+=\frac{\rho_0+\rho_1}{2},\qquad
\rho_-=\frac{\rho_0-\rho_1}{2}.
$$
它们在相同原三输入坐标上整有界，满足
$$
\boxed{
W_*\rho_+=\nu_T,\quad W_*\rho_-=0,\qquad
Y_*\rho_+=\frac13\nu_S,\quad Y_*\rho_-=\frac23\nu_S,
}
\tag{25}
$$
以及保留另外两个完整输出的 scalar core
$$
\boxed{\rho_\pm|_{W\in p}=\pm\lambda A_*\rho_\pm,}
\tag{26}
$$
其中 $A$ 正是 R413 (17)，未换域。
特别 $\rho_-$ 确实非零，因为其 $Y$ 推前为非零来源的 $2/3$ 倍。
所以 R413 的完整 $W$ 核已得到一个明确非零实际元素。

### 7.1 仍保全部补域的新增深层条件

置
$$
V=Y-\frac{17}{36}W
=-\frac{19}{108}R+\frac1{27}U,\qquad c=17/36.
$$
它在 $A$ 下保持不动。对 $n\ge1$，(26) 把同一真实域
$\{W\in p^n,Y\text{ 为单位}\}$ 准确送到
$\{V\text{ 为单位}\}$，因为 $Y\circ A^n=V+c\kappa^nW$。
因此原深层中央行是收敛的完整式
$$
\begin{aligned}
&\int_{\substack{W\in p^n\\Y\text{ 为单位}}}
 d\log_p\langle Y\rangle\,d\rho_\pm\\
&=(\pm\lambda)^n d\left[
 \int_{V\text{ 为单位}}\log_p\langle V\rangle\,d\rho_\pm
 +\sum_{j\ge1}\frac{(-1)^{j+1}c^j\kappa^{nj}}j
   \int_{V\text{ 为单位}}W^jV^{-j}\,d\rho_\pm\right].
\end{aligned}
\tag{27}
$$
每个第 $j$ 项赋值至少 $nj-v_p(j)$，所以所有尾确实收敛；耦合的 $V$ 单位域不能令 $j$ 只取六的倍数。

在原 $J'_S(0)=0$ 时，(25) 使整个 $Y$ 中央行在两特征状态上都为零。因此 $\{W\notin p^n,Y\text{ 为单位}\}$ 的完整补域中央值准确等于 (27) 的负数。
原 $V$ 斜率及所有混合正负矩仍在 (27) 中，不被删除。
这给出两条真正由原失败传来的补域约束，同时明确了要与 R399 移动管相交时还需控制的观察。

## 8. 剩余问题

本篇已把第二状态的完整 $Y$ 边际接回原 $S$，并产生两个实际 scalar-core 状态；其中负态有恒零 $W$ 推前和已知非零 $Y$ 推前。两个原中央失败已合法传入这些状态。

但 (27) 的 $V$ 中央行与混合矩尚未由原两个失败确定。原 $Y/Z$ 双移动管仍须保留自己的全部条件；不能从 (25) 的完整边际零推出任意受限叶域零。固定曲线的无穷素数非消失仍未完成。

直接依赖：R398 的原 $S,T,L$ 与四挠除子；R399 的共同真实源和相位；R413 的完整三输出模型及绝对总和 core。新增十六项公式、全部半周期常数、完整多项式求和与两态边际均在本文证明。
